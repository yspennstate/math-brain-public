# Audit of the 38-page threshold paper: the C_reg proof and the shared-data multiplexer extension

Auditor: Claude lead, stream B19, 2026-10-11 (21:59Z-23:55Z). Full FEI remains OPEN; nothing below proves it.

Source read: `~/fourier-entropy-threshold-functions/paper/main.tex`, 2,674 lines, local sha256
`de36fcdab064333565b2f311db861df57b50955245d747ae7c03653d5e9bf28e`. This hash differs from the published-source hash
85e9c4f3... recorded for commit b38ba0ab; I audited the bytes I read (line numbers below refer to them) and did not
determine whether the difference is line endings or content. Reviewer re-running this should hash first.

Certificates: run `runs/20261011T224700Z-claude-B19-paper-audit-rankcode/` (code/cert_constants.py,
code/exact_checks.py; outputs in out/). Constants were enclosed two ways: exact rational comparison with certified
rational brackets of e (Taylor series plus 2/(N+1)! tail) and pi (Machin, alternating brackets), and mpmath interval
arithmetic with outward rounding; Euler's gamma by the Euler-Maclaurin bracket at n = 2000, cross-checked against the
elementary bracket H_n - ln n - 1/(2n) < gamma < H_n - ln n - 1/(2(n+1)).

Verdict summary: every step of the C_reg proof of Theorem A that I checked HOLDS; every stated constant is correct;
the shared-data proposition and both multiplexer corollaries HOLD as stated. One scope remark (not an error) on the
shared-data proposition and one boundary result on the proof method (the global-order rank code cannot give universal
FEI) are recorded at the end.

## 1. Constants (eq:constants, lines 99-102; eq:ordinaryexact, 572-577; eq:cm, 643-646)

| quoted line | check | verdict |
|---|---|---|
| l.102 `\Creg=\Clev+2\log(e\pi)<8.937.` | ((4+e)e^2 pi^2)^1000 < 2^8937 exactly with rational upper brackets; also C_reg in (8.9364, 8.9366) by the 10^4-th power comparison; interval C_reg = 8.93647465787758280416 (width < 1e-40). A091 enclosed 8.936474657877582804-805 independently. | holds |
| l.632 `&=\bigl(\Clev+2\log(e\pi)\bigr)\D(f)=\Creg\D(f).` | (2 L_p + ln(pi^2/4))/ln2 - 2 log2(e pi) is in [-8.6e-50, 8.6e-50] (an identity: 2+2ln2+2lnpi-2ln2 = 2(1+ln pi)). | holds |
| l.576-577 `For $a=6/5$, the constant independent of $m$ is $11.2375133696\ldots$` | C_lev + (1 + ln 6 + (6/5)(2+gamma))/ln2 in [11.23751336963089074, 11.23751336963089165]. The quoted digits are correct. | holds |
| l.646 `<11.460+\frac{22}{5}\log m.` | C_lev + (1+ln7+(6/5)(2+gamma))/ln2 in [11.4599057909673386, 11.4599057909673396] < 11.460 (margin 9.4e-5). | holds |
| l.575 log m coefficient `(1+2a)\ln m` | (1+2a) = 17/5 at a = 6/5 (bits: (17/5) log m); centered version 2a+2 = 22/5. | holds |
| l.637-641 `b+6m\le7m^2,` `since $3m^2-6m+1>0$` | with b <= 4m^2-1: 7m^2-(b+6m) >= 3m^2-6m+1 > 0 for m >= 2 (roots 1 +- sqrt(6)/3). | holds |
| ρ = 4/(4+e) (Lemma levelentropy proof) | log2(ρ/(1-ρ)) + log2 e - 2 and 2 + log2(1/ρ) - log2(4+e) both enclose 0 to 5e-50. | holds |

## 2. Theorem A, regular case (statement l.107-117: `\HH(f)\le\Creg\,\D(f).`)

| step (main.tex) | what was checked | verdict |
|---|---|---|
| Lemma levelentropy, l.252-291 | Edge-isoperimetry I >= 2p log2(1/p); the difference [2p log(1/p)] - [v + (1/2) v log(1/v)] with v = 4p(1-p), q = 1-2p, equals (1-q)/2 · φ(q), φ(q) = (q-1)log(1-q) + (1+q)log(1+q) - 2q; φ(0) = φ(1) = 0 and φ'' = -2q/((1-q^2) ln2) <= 0, so φ >= 0 on [0,1]. h2(v) <= v log(1/v) + v log e <= 2I + (log e - 2)v. The geometric level reference with ρ = 4/(4+e) cancels the v-coefficient exactly and leaves log(4+e) I. | holds |
| Lemma centering, l.295-322 | min{α,1-α} <= 2α(1-α) <= 2(α - c^2); D(f) = min_U I(χ_U f) (l.82, l.299) and D <= 4(I - Var). | holds |
| Lemma pivotal-antichain, l.328-336 `On each fiber obtained by fixing the coordinates outside $U_i\cup\{i\}$, the support of $d_i f$ is an antichain in the cube on $U_i$.` | for y < y' pivotal and j flipping -1 -> 1: pivotality gives f(y,i=1) = 1, desirability (eq:desire, l.89-93, applied at y_j = -1) gives f(y^{j=1}, i=-1) >= 1, monotonicity gives f(y', i=-1) = 1, contradiction. | holds |
| Lemma antichain-density, l.339-342 `c_q=2^{-q}\binom q{\lfloor q/2\rfloor}\le(q+1)^{-1/2}.` | induction ratio: (2r+1)(2r+3) <= (2r+2)^2. | holds |
| Lemma antichain-noise, l.354-381 | restriction of the antichain to a subcube, E[1/(B+1)] = (1-(1-t)^r)/(rt), Cauchy-Schwarz. (Lemma multi-rank, l.457-497, uses the same estimate with 1 - e^{-u} >= u e^{-u} at l.488-490; checked.) | holds |
| Lemma ranktail, l.386-444 | tail with t = 1/(2K) and -(K-1) ln(1-1/(2K)) <= (K-1)/(2K-1) <= 1/2, giving sqrt(2e) e^{-u/2}; mean via beta integrals; c_{2j-1} = c_{2j} = b_j; Σ b_j/(2j-1) = 1 and Σ b_j/(2j) = ln 2 (substitution w = sqrt(1-z)). | holds |
| Euler reference, l.507-541 | l.519-520 `=\frac{\sinh(\pi\sqrt z)}{\pi\sqrt z} =\sum_{k\ge0}\frac{\pi^{2k}}{(2k+1)!}z^k.`; l.524 `Q_k(S)=\frac{(2k+1)!}{\pi^{2k}}\prod_{i\in S}i^{-2},` is a subprobability since e_k(1, 1/4, 1/9, ...) <= π^{2k}/(2k+1)!; -ln Q_k = 2 Σ ln(i_j/j) + ln(π^{2k}(k!)^2/(2k+1)!) (l.534) and (2k+1)! >= 4^k (k!)^2 (l.539): the left side grows by (2k+2)(2k+3), the right by 4(k+1)^2 = (2k+2)^2, quotient (2k+3)/(2k+2) >= 1. | holds |
| m = 1 centering and final display, l.594-633 | coordinates with Inf > 1/2 have rank 1 (one predecessor gives Inf <= 1/2), so b <= 1 and the rank cost vanishes; d_i(χ_U f) = χ_U d_i f keeps the antichain support; E Σ F <= L_p I(g); final constant (2L_p + ln(π^2/4))/ln2 = 2 log2(eπ) (Section 1). | holds |
| LTFs regular, l.94-96 and sgn(0) = 1 (l.78) | orientation and ordering by |w_i|; the sgn(0) convention handled by perturbing the threshold off the finite score set. | holds |
| Theorem B Frullani step, l.499-504 | ∫_0^{m^2}(1-e^{-t})/t dt + ∫_{m^2}^∞ (m t^{-1/2} - e^{-t})/t dt = (Ein(m^2) - E1(m^2)) + 2 = 2 ln m + γ + 2, using Ein(x) - E1(x) = ln x + γ and ∫_{m^2}^∞ m t^{-3/2} dt = 2; Frullani needs 0 < Z <= 1, stated. | holds |
| Theorem B eq:rankcost, l.567-570; eq:normalizer | normalizer term 1 + ln(a/(a-1)) and the a(L_mix + 2 ln m) I rank cost combine as in eq:ordinaryexact. | holds (constants in Section 1) |

Executed validation of the reduction behind Theorem A (code/exact_checks.py, section D): for 180 random Boolean f on
3-4 variables and every coordinate order (3,240 pairs), H(f) <= [log2(4+e) + log2(π^2/4)] I(f) + (2/ln2) R_π(f)
held with proved intervals. This is the general inequality that the paper's lemmas give for every Boolean f
(Gibbs on each level, Lemma levelentropy, the Euler normalizer); Theorem A then bounds R_π <= L_p I for regular f.

## 3. Shared-data multiplexers (l.2212-2333)

| quoted line | check | verdict |
|---|---|---|
| l.2218 `F(x,y)=g_x(y),\qquad N=2^a.` and l.2226-2235 (R_T, r_T, u_T, ν_T) | r_T sums to 1 by definition of R_T; ν_T is a probability vector because u_T is a unit vector over b and the selector characters are orthonormal (Parseval over x): Σ_S ν_T(S) = Σ_b u_T(b)^2 = 1. Exact check: every F̂(S,T)^2 = R_T ν_T(S) and Σ r_T = Σ ν_T = 1 on 216 multiplexers (a = 1..3, data 2-4 bits, constant and biased branches included). | holds |
| l.2238-2241 eq:shared-data-collision | chain rule through the comparison law P(B = b, T) = ĝ_b(T)^2/N, whose entropy is a + avg_b H(g_b) = H(R) + Σ_T R_T H(r_T), while H(F) = H(R) + Σ_T R_T H(ν_T). Interval check: the difference encloses 0 (to 1e-30) on all 216. | holds |
| l.2243-2245 eq:shared-data-upper `\HH(F)\le2a+\frac1N\sum_b\HH(g_b).` | H(ν_T) <= a (support 2^a), H(r_T) >= 0. Checked on all 216. | holds |
| l.2248-2254 influence formulas | I_data = avg I(g_b), Inf_{x_j}(F) = avg_b P[g_b ≠ g_{b^(j)}] (exact, three ways: direct, formula, spectral), I_sel = Σ_T R_T Σ_S |S| ν_T(S): exact equality on all 216. | holds |
| l.2293-2296 `For Boolean branches, orthogonality is equivalent to disagreement probability $1/2$.` | E[gg'] = 1 - 2 P[g ≠ g'] for ±1 functions; exhaustive over all 65,536 pairs on 3 bits. | holds |
| l.2296-2299 `the selector term is $4\I_{\rm sel}(F)$` | 2a = 4 · (a/2); the general version 2a <= (2/c) I_sel. | holds |
| l.2303-2312 Cor recursive-multiplexers | induction: branch functions extended by irrelevant coordinates keep H and I; deeper selectors (possibly shared between branches) act as data for the parent; orthogonality is required over the parent's whole common cube; C_reg > 4 (enclosed above) keeps max{4, C_reg} = C_reg. | holds |
| l.2324-2332 Maj3 example | E[g_+ g_-] = 0 exactly; spectrum of the one-bit multiplexer: two atoms 1/4 and eight atoms 1/16; H(F) = 3 (interval width 6e-40), I(F) = 2. | holds |

Scope remark (not an error). Proposition shared-data-collision assumes nothing about F: for any Boolean F and any split
of its coordinates into a block x of size a and the rest y, put g_b = F restricted to x = b. The identity and the upper
bound are therefore the general block-restriction identity and bound (campaign C005/C006 form H(F) <= 2|A| + E H(F_{A<-b}))
written in multiplexer language; "fresh selector" and "shared data" impose nothing. The content of the extension is in
Corollary orthogonal-multiplexers: the hypothesis I_sel >= c·a (orthogonality gives c = 1/2) plus FEI for every
restriction. Any extension to non-orthogonal neighbours must pay the correction Σ_T R_T[H(ν_T) - H(r_T)], which for
a = 1 is the regime of the B05 and bent-splice obstructions.

## 4. Boundary of the proof method (new, proved here; not about FEI itself)

The rank code of Theorem A uses ONE coordinate order. For every Boolean f and every order π the paper's lemmas give
H(f) <= [log2(4+e) + log2(π^2/4)] I(f) + (2/ln2) R_π(f), with R_π(f) = E_{S~f̂^2} Σ_j ln(i_j/j). For
f_{m,L} = XOR of m disjoint AND_L blocks, every order has

  R_π(f_{m,L}) >= 2^{1-L} Σ_{p=1}^{mL} max{0, ln p - ln((L+1)/2 + (p-1) 2^{1-L})},

by Jensen per coordinate (proof in the run REPORT.md, claim B19-RANKCODE-GLOBAL-ORDER-NOGO). Hence (2/ln2) R_π/I >= 2(L-1) - o(1)
as m -> ∞ while H/I = H(AND_L)/I(AND_L) < 4 for every L. Certified rows: L = 8, mL = 10^9 gives rank term >= 13.99997 I
against H <= 3.8428 I; L = 16, mL = 10^15 gives >= 29.99999 I against H <= 3.9303 I. Exhaustive check over all orders for
(m, L) = (2,2), (3,2), (2,3) confirms the displayed lower bound. So extending Theorem A beyond regular-type functions needs
a block-adaptive or non-product reference measure, not a better order.
