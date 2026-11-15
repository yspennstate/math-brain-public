MINOR

# Independent referee report on G0010

The mathematics of (A)–(D) survives this review. I found no false inequality, dependence error, missing root term, or invalid high-probability amplification in these four results. The honest research status is **PARTIAL**, not a counterexample to a theorem or conjecture of Christoph–Morawski–Wigderson (CMW). The construction excludes a possible logarithmic answer in one regime that their question leaves open; it does not determine the requested tight bound.

(A) is a valid clique-calibrated refinement of an existing finite-tree obstruction, with a valid blow-up extension. (B) is known and correctly cited. (C) is a valid, nonsharp boundary estimate. (D) is a valid quantitative refinement of CMW's resolvent method. I did not locate the exact statements of (A), (C), or (D) in the inspected papers; this supports treating them as potentially new elementary refinements, not a certified priority claim. Their principal ingredients are established methods.

## 1. Errors, gaps, and required revisions

1. **Status and title: `claim_files/REPORT.md`, line 1 and the opening “counterexample” language.** `COUNTEREXAMPLE` misclassifies the result relative to the named open problem. CMW asks for a bound; it does not assert that every graph satisfying a fixed maximum-degree-to-radius ratio has logarithmic components. Change the research status to `PARTIAL`, and describe (A) as a polynomial lower-bound construction in the regime \(q(1+\delta)>1\). The report's own disclaimer is correct, but does not repair a misleading status line.

2. **Incomplete supplied literature evidence: “Source and literature outcome.”** The claim references `sources/CMW_2608.19145v1.txt` and `sources/LITERATURE_REVIEW.txt`; neither is in the supplied `claim_files/` tree. This is an artifact/provenance gap, not evidence against a proof. Include the sources and exact applicability comparisons with the reviewed submission. I independently retrieved the primary texts into this review's `sources/` directory and give the comparisons below. A search that does not find a predecessor cannot certify novelty.

3. **Scope of the improvement: Section 4, prose immediately after (17).** The displayed formula is correct with its stated fixed parameters. To call its displayed bound an improvement over \(B\log n\), choose
   \[
   0<\zeta<-\frac{\log q}{\log R},
   \]
   and consider a sequence with \(B\to\infty\). An arbitrary large allowed \(\zeta\) in (17) need not give a subunit displayed exponent. The proof does permit a smaller exponent, as its prose suggests. Also distinguish the fixed-\(R\) exponent formula from a uniform assertion for varying \(R\), since its constants depend on \(R\). Replace the loose sentence by these qualifications. This requires no change to (14)–(17).

4. **Remaining sharpness gaps: end of Sections 3–4 and Section 7.** These are explicitly acknowledged, rather than concealed errors: (C) leaves a logarithmic-versus-cubic-log gap under its broad hypotheses, and (A) and (D) generally have different exponents above the boundary. The cycle proves a worst-case logarithmic lower bound within the allowed class; it does not prescribe a matching example for every \((n,\Delta,\lambda)\), or prove sharpness when both constraints are saturated. Retain these qualifications and do not market the results as resolving Question 5.2.

No further mathematical correction is required for (A)–(D). In particular, the potential issues singled out in the referee request—the adaptive coupling, second moment, root in the MGF, and supermartingale sign—all check out. The exact degree formula in (A) is understood for \(h\ge1\), as its proof says; an irrelevant height-zero exception should not be included in that formula.

## 2. What the source actually asks

I downloaded [CMW, arXiv:2608.19145v1](https://arxiv.org/abs/2608.19145v1) directly and converted its PDF bytes in memory to `sources/CMW_2608.19145v1.txt`. It has 22 pages. **Question 5.2 is on printed/PDF page 20**, not page 19. With mathematical typesetting transcribed, its exact statement is:

> Question 5.2. For a graph with given \(\Delta(G)\) and \(\lambda(G)\), what is the tight upper bound for the typical size of the largest component of \(G_p\), when \(p\leqslant(1-\varepsilon)/\lambda(G)\)?

The following paragraph singles out \(\Delta(G)\le(1+\delta)\lambda(G)\), allowing \(\delta\) to depend on the order of the graph. It poses a special case, without conjecturing a logarithmic answer throughout that class. Footnote 7 on the same page already identifies finite \(d\)-ary trees as polynomial lower examples, with exponents approaching \(1/2\) as the fixed branching parameter grows.

Theorem 1.4(II), pp. 4–5, gives a high-probability upper bound of order \(B\log n\), where \(B=\sqrt{n\Delta}/\lambda\). Lemma 2.4 on p. 9 constructs the resolvent weight, and Lemma 3.1(a), p. 11, gives its exponential component-weight tail; the combination is proved on p. 16. These statements are consistent with (A).

Here is a direct magnitude check. From \(k\ge2\sqrt b\),
\[
\mu=b(1-e^{-q/(k+1)})<\frac{qb}{k+1}<\frac{q\sqrt b}{2},
\]
so
\[
\frac{\log\mu}{(1+\tau)\log b}<\frac{1}{2(1+\tau)}.
\]
For (A), \(B=\Theta(n^{1/[2(1+\tau)]})\). Thus its polynomial lower bound is smaller even than the power in CMW's upper bound. For \(\tau=0\) its exponent is strictly below \(1/2\), also consistent with the constant-radius discussion on p. 20. There is no contradiction to Theorem 1.3(II), whose \(O(\sqrt n)\) conclusion is a bounded-in-probability statement rather than a fixed-constant bound holding with probability tending to one.

The quantifiers also matter near regularity. For each fixed \(\varepsilon>0\), (A) requires
\[
\delta>\frac{\varepsilon}{1-\varepsilon}.
\]
It says nothing contrary to logarithmic behavior for \(\delta=o(1)\) at fixed \(\varepsilon\); (B) eventually applies there. Arbitrarily small fixed ratios above 1 in (A) require correspondingly small subcritical margins.

## 3. Line-by-line audit of Theorem A

Write \(q=1-\varepsilon\in(0,1)\). Throughout this construction \(k,b,\tau\) are fixed and \(h\to\infty\).

**The parameter system (3) is feasible.** Choose \(1/q<r<1+\delta\), and set \(b=\lfloor rk\rfloor\). Then \(b/k\to r>1\), \(k^2\ge4b\) eventually, and
\[
(1+\delta)k-(b+1)\ge(1+\delta-r)k-1>0
\]
for sufficiently large \(k\). Also
\[
b(1-e^{-q/(k+1)})\longrightarrow rq>1.
\]
All four inequalities can therefore hold simultaneously. This uses the strict hypothesis, not a limiting choice on the boundary. My numerical witnesses include \(q=0.8,\delta=0.2501,k=65536,b=81923\), with \(\mu=1.00001525845\ldots\); the proof, rather than this witness, establishes feasibility for every admissible pair.

**The tree norm and bridge estimate are correct.** For each parent–child edge,
\[
2|x_ux_v|\le b^{-1/2}x_u^2+b^{1/2}x_v^2.
\]
An internal vertex receives at most \(\sqrt b\) from its parent role and \(\sqrt b\) from its child role. The root and leaves receive less. Consequently \(\|A_T\|_2\le2\sqrt b\). Independently, the exact tree radius is
\[
\lambda(T_{b,h})=2\sqrt b\cos\frac{\pi}{h+2},
\]
as follows from the symmetric quotient on levels. Before adding the bridge the radius is \(\max(k,\lambda(T))=k\). The bridge adjacency has eigenvalues \(1,-1,0,\ldots,0\), so its operator norm is 1. The clique Rayleigh vector gives the lower bound and the norm inequality the upper bound:
\[
k\le\lambda(H_h)\le k+1.
\]
For \(h\ge1\), the root has degree (b+1), an internal tree vertex has degree (b+1), and the clique bridge endpoint has degree \(k+1\le b+1\). Thus \(\Delta(H_h)=b+1\). In particular the connecting edge has been included correctly.

**Blow-up spectrum and order are correct.** The construction uses independent sets, not cliques, so its matrix really is \(A_H\otimes J_m\), with zero diagonal. The eigenvalues of \(J_m\) are \(m,0,\ldots,0\). Hence
\[
\lambda(G_h)=m\lambda(H_h),\qquad\Delta(G_h)=m(b+1).
\]
It stays connected and simple. The number of vertices is exactly the stated
\[
n_h=m_h\left(k+1+\frac{b^{h+1}-1}{b-1}\right).
\]
Since \(m_h=\lceil b^{\tau h}\rceil=\Theta(b^{\tau h})\),
\[
n_h=\Theta(b^{(1+\tau)h}),\qquad
\lambda(G_h)=\Theta(b^{\tau h})
=\Theta(n_h^{\tau/(1+\tau)}).
\]
For \(\tau=0\), \(m_h=1\) exactly. The bound \(\Delta\le(1+\delta)\lambda\) follows already from \(\lambda(H_h)\ge k\). No estimate of the bridge survival is needed.

**The selected-vertex branching process is legitimate.** From a single selected vertex in a parent set, the \(m\) edges into a particular child set have independent retention indicators. Each child set is reached with probability
\[
a_h=1-(1-p_h)^m\ge1-e^{-mp_h}
=1-e^{-q/\lambda(H_h)}\ge1-e^{-q/(k+1)}=:a_0.
\]
Choosing an endpoint by an ordering rule reveals only edges of that parent–child block. Edges from the chosen endpoint to the next level have not been tested. Distinct parent–child blocks have disjoint edge sets, and a tree set has a unique parent; there is never competition between two selected parents for the same child set. Conditional on the exploration history, all next offspring trials therefore have the same independent law. Independent thinning gives offspring \(\operatorname{Bin}(b,a_0)\). Counting one vertex per set discards possible connectivity and so is a lower bound, not an assumed description of the entire component.

**The second moment (8) is correct.** For offspring mean \(\mu>1\) and variance \(\sigma^2\), conditional variance and expectation give
\[
E Z_{\ell+1}^2=\mu^2 E Z_\ell^2+\sigma^2\mu^\ell.
\]
Summing the resulting geometric increments gives
\[
\frac{E Z_\ell^2}{\mu^{2\ell}}
=1+\frac{\sigma^2}{\mu(\mu-1)}(1-\mu^{-\ell})\le C.
\]
To spell out the Cauchy–Schwarz step, the contribution of \(Z_\ell<E Z_\ell/2\) to its expectation is at most \(E Z_\ell/2\). The expectation restricted to the complement is therefore at least that amount. Cauchy–Schwarz then yields
\[
P(Z_\ell\ge\mu^\ell/2)\ge\frac{(E Z_\ell)^2}{4E Z_\ell^2}\ge\frac1{4C}.
\]
No survival-limit theorem or conditioning on survival has been smuggled in.

**Amplification and exponent conversion are correct.** At depth \(j=\lfloor\eta h\rfloor\), there are \(b^j\) vertex-disjoint descendant trees, also after blowing up. Give each its own exploration and thinning coins, using no parent edges. The success events depend on disjoint Bernoulli variables, so
\[
P\left(L_1<\tfrac12\mu^{h-j}\right)\le(1-s_0)^{b^j}\to0.
\]
If several such components connect elsewhere, their sizes only increase. Finally,
\[
\log(\mu^{h-j}/2)=(1-\eta)h\log\mu+O(1),\qquad
\log n_h=(1+\tau)h\log b+O(1).
\]
Every strict \(c<\log\mu/[(1+\tau)\log b]\) admits a positive \(\eta\) that gives the claimed comparison for all sufficiently large \(h\). The strictness of the exponent is used correctly.

The report's small-ratio numerical example also checks: for \(q=0.98,k=100,b=108\), \(\mu=1.0428532233\ldots\). Its unblown exponent limit is \(0.0089618249\ldots\), so \(\tau=1\) allows any \(c<0.0044809124\ldots\), including (0.004). Many leaves are present; the construction satisfies CMW's spectral meaning of “close to regular,” not a condition comparing minimum and maximum degrees.

## 4. Proposition B and the cycle

[Diskin–Erde–Kang–Krivelevich, arXiv:2209.03722v3](https://arxiv.org/abs/2209.03722v3), **Theorem 2, PDF p. 3**, concerns any \(n\)-vertex graph of maximum degree \(d\), not just a product graph or a regular graph. At \(p=(1-\kappa)/d\), it gives maximum component order at most \(9\kappa^{-2}\log n\) with probability tending to one. Smaller \(p\) follows by monotonicity. The text itself calls variants of the theorem well known. The claim's theorem number, page, constant, and applicability are correct.

Its sharper self-contained tail (10) also follows. Dominate a rooted exploration by offspring \(\operatorname{Bin}(\Delta,p)\). If its total progeny is at least \(s\), the first \(N=s-1\) offspring variables sum to at least (N). Their MGF is bounded by that of a Poisson variable with mean \((1-\kappa)N\). At \(t=-\log(1-\kappa)\), the exponent becomes
\[
N[\kappa+\log(1-\kappa)]\le-N\kappa^2/2.
\]
A union bound gives (10). The asserted constant in this elementary tail need not match DEKK's larger constant.

On \(C_n\), \(\lambda=\Delta=2\), and \(p=q/2\in(0,1)\). Use \(M=\lfloor n/\ell\rfloor\) disjoint edge intervals of length \(\ell=\lfloor c\log n\rfloor\), where \(c<1/|\log p|\). They may share endpoint vertices; edge disjointness is sufficient for independence. Each is all open with probability \(p^\ell\), and
\[
Mp^\ell\asymp\frac{n^{1-c|\log p|}}{\log n}\to\infty.
\]
Thus \(P(\text{no open interval})\le e^{-Mp^\ell}\to0\), and an open interval has \(\ell+1\) vertices. This proves the stated logarithmic lower bound. It matches (B) as a worst-case order over its allowed class. This lower-bound example does not saturate \(p\Delta=1\), since \(q<1\).

## 5. Proposition C: all constants and the root checked

The result assumes a fixed spectral gap \(\varepsilon=1-q>0\). An edgeless graph or \(p=0\) is trivial; consider \(\lambda>0,p>0\).

For \(j\ge1\), symmetry and Cauchy–Schwarz give
\[
W_j(x)=\langle Ae_x,A^{j-1}\mathbf1\rangle
\le\sqrt{d(x)n}\lambda^{j-1},
\]
while direct counting gives \(W_j(x)\le\Delta^j\). Multiplication by \(p^j\), using both hypotheses, yields
\[
p^jW_j(x)\le\min\{(p\Delta)^j,
(\sqrt{d(x)n}/\lambda)(p\lambda)^j\}
\le\min\{1,Bq^j\}.
\]
Because \(\lambda\le\Delta\le n-1\), \(B\ge\sqrt{n/\Delta}>1\); because \(\lambda\ge\sqrt\Delta\), \(B\le\sqrt n\). The report's looser \(B\le n\) is true. With \(J=\lceil\log B/\log(1/q)\rceil\), \(Bq^J\le1\), so
\[
U\le1+J+\frac{Bq^{J+1}}{1-q}
\le1+J+\frac1\varepsilon=O_\varepsilon(\log n).
\]
There is no missing factor of \(\lambda\) or \(q\) in (12).

The multitype process has one independent Bernoulli((p)) child opportunity for each neighbor of a particle's type, allowing repeated types. Couple the graph exploration to those opportunities on edges leading to undiscovered labels; discarded repeated labels and extra fresh trials only enlarge the branching process. Reversing a graph edge in the process causes no difficulty: its extra copy is discarded when it would revisit an already discovered graph label. The mean matrix is (pA), and its expected total-progeny vector, **including the initial particle**, is \(u=(I-pA)^{-1}\mathbf1\).

Let \(T_{x,t}\) count particles through generation \(t\), including generation 0. Its exact MGF recursion is
\[
F_{x,0}=e^\theta,\qquad
F_{x,t+1}=e^\theta\prod_{y\sim x}(1-p+pF_{y,t}).
\]
Set \(a=1/(2U^2)\), \(\theta=1/(4U^2)\). Since every \(u_y\ge1\) and \(U\ge1\),
\[
au_y\le aU=\frac1{2U}\le\frac12,
\qquad \theta\le au_x.
\]
The second inequality verifies the root-only base case, which is essential. Under \(F_{y,t}\le e^{au_y}\), use \(1+v\le e^v\) and \(e^z-1\le z+z^2\) for \(0\le z\le1\). Then
\[
\begin{aligned}
\log F_{x,t+1}
&\le\theta+pa\sum_{y\sim x}u_y+pa^2\sum_{y\sim x}u_y^2\\
&\le\theta+a(u_x-1)+a^2U(u_x-1)\\
&\le au_x+\theta-a+a^2U^2=au_x.
\end{aligned}
\]
The identity \(\theta+a^2U^2=a\) is numerically and algebraically exact, and its use is in the correct direction. Monotone convergence as \(t\to\infty\) bounds the full total progeny. Consequently
\[
P(|C_x|\ge s)\le\exp\left(\frac1{2U}-\frac{s}{4U^2}\right)
\le\exp\left(\frac12-\frac{s}{4U^2}\right).
\]
At \(s=4U^2(3\log n+1)\), the union-bound probability is at most \(e^{-1/2}n^{-2}\). Rounding \(s\) up causes no problem. Thus (C) is valid, with constants depending only on the fixed spectral margin. It makes no sharpness claim.

## 6. Section 4: weighted exploration and exponent

For \(1<a<1/q\), the resolvent at \(a\lambda\) obeys
\[
1\le u_x\le U_a=1+\sum_{j\ge1}a^{-j}\min\{R^j,B\},
\qquad Au=a\lambda(u-\mathbf1).
\]
Normalize \(w=u/U_a\). Then \(1/U_a\le w_x\le1\), \(Aw\le a\lambda w\), and \(pa\lambda\le qa=1-\theta\).

There are at most \(|E(G)|\) queried edges, so padding to that deterministic horizon avoids any unbounded optional-stopping issue. At a query the endpoint weight \(z_i\in[0,1]\) is predictable and the previously untested edge indicator \(Y_i\) is independent Bernoulli((p)). For \(0\le t\le1/2\),
\[
E(e^{tY_iz_i}\mid\mathcal F_{i-1})
=1+p(e^{tz_i}-1)\le e^{pt(1+t)z_i}.
\]
Therefore
\[
M=\exp\left(t\sum_iY_iz_i-pt(1+t)\sum_i z_i\right)
\]
has expectation at most 1 at the padded terminal time. Every successful query discovers one new vertex, and every query is charged to a vertex in the explored component, so
\[
\sum_iY_iz_i=w(C)-w(x)\ge w(C)-1,
\qquad
\sum_i z_i\le\sum_{v\in C}(Aw)_v\le a\lambda w(C).
\]
The negative coefficient on the second sum reverses its upper bound in the required direction: it supplies a **lower** bound on (M). With \(t=\theta/2\),
\[
t[1-pa\lambda(1+t)]\ge
\frac\theta2\left[1-(1-\theta)(1+\theta/2)\right]
=\frac{\theta^2(1+\theta)}4\ge\frac{\theta^2}4.
\]
The root cost \(tw(x)\le1/2\) is bounded more loosely by 1 in the report. Thus \(M\ge e^{\theta^2w(C)/4-1}\), and
\[
P(w(C)\ge z)\le e^{1-\theta^2z/4}.
\]
Conversion by \(w(C)\ge|C|/U_a\) and a union bound give (15), including its \(n^{-2}\) constant.

For \(R>1\), let \(J=\lfloor\log B/\log R\rfloor\). The crossover is \(R^j\le B\) exactly for \(j\le J\), with either choice harmless if equality occurs. The remaining geometric sum is
\[
B\sum_{j=J+1}^\infty a^{-j}=\frac{Ba^{-J}}{a-1}.
\]
This proves (16) with its stated index and denominator. For \(R=1\), the value is (a/(a-1)). For fixed (R,a), summing the first part gives precisely the three cases in the report: bounded for \(R<a\), logarithmic in (B) for \(R=a\), and of order \(B^{1-\log a/\log R}\) for \(R>a\).

If \(R>1/q\) is fixed, \(a\uparrow1/q\) makes the power approach
\[
\beta(R,q)=1+\frac{\log q}{\log R}
=\frac{\log(qR)}{\log R}\in(0,1)
\]
from above. This proves (17) for every fixed positive slack. Choosing a sufficiently small slack proves a strict power improvement over CMW when \(B\to\infty\). Constants may deteriorate as the slack shrinks. A uniform improvement over a class \(1\le R\le R_0<\infty\) is also available by choosing one \(a\in(1,1/q)\), replacing \(R\) inside the minimum by a larger fixed \(R_* >\max(R_0,a)\), and applying the same sum; that is a weaker uniform exponent, not the ratio-specific formula (17).

The argument is an extension of CMW Lemma 2.4 and Lemma 3.1(a), not a new concentration principle. Nor does it match (A)'s exponent. At \(qR=1\), the fixed positive-drift choice \(a<1/q=R\) does not directly give a zero exponent in (17); one must use (C), or optimize a size-dependent slack in (15). Silently substituting the endpoint \(a=1/q\) would be invalid, and the claim does not do that.

## 7. Independent computations

I wrote `code/independent_audit.py` from scratch without reading, importing, or running `claim_files/code/`. It constructs the hosts independently. The independent sampler first chooses \(K\sim\operatorname{Bin}(E,p)\), then chooses a uniform (K)-element subset of the distinct host edges. For any prescribed subset (S), its probability is \(p^{|S|}(1-p)^{E-|S|}\); hence this is exact Bernoulli bond percolation, not fixed-edge-count percolation. Implicit blow-up edges are decoded by base-edge number and two endpoint indices.

**Exact small spectra.** An integer equitable quotient has classes consisting of the clique bridge endpoint, the other clique vertices, and the tree levels. Its largest root is the host radius, since its positive eigenvector lifts to a positive eigenvector of the connected graph. An independent characteristic-polynomial recurrence is
\[
P_0=1,\quad P_1=x,\quad P_{j+1}=xP_j-bP_{j-1},
\]
\[
F_{k,b,h}(x)=(x-k)(x+1)P_{h+1}(x)-(x-k+1)P_h(x).
\]
Thus \(\lambda(G)=m\rho\), where \(\rho\) is the largest real root of this explicit integer polynomial. This is an exact algebraic specification, supplemented in `data/proof_checks.json` by rational isolating intervals of width at most \(10^{-24}\). Degrees are computed as integers from full adjacency matrices. Representative cases are:

| (k,b,h,m) | \(n\) | exact \(\Delta\) | exact \(\lambda\), with decimal for readability |
|---|---:|---:|---|
| (4,4,1,1) | 10 | 5 | largest root of \(x^4-3x^3-9x^2+15x+16\), \(4.068322958474\ldots\) |
| (4,4,2,2) | 52 | 10 | twice the largest root of \(x^5-3x^4-13x^3+27x^2+36x-12\), \(8.152317891452\ldots\) |
| (6,8,1,2) | 32 | 18 | twice the largest root of \(x^4-5x^3-15x^2+45x+48\), \(12.062344587470\ldots\) |
| (8,12,1,1) | 22 | 13 | largest root of \(x^4-7x^3-21x^2+91x+96\), \(8.017301736732\ldots\) |
| (12,16,1,1) | 30 | 17 | largest root of \(x^4-11x^3-29x^2+187x+192\), \(12.007254320668\ldots\) |

The first two are spectral controls, rather than supercritical-offspring examples. The others admit suitable \(q,\delta\) in (3). Full-matrix eigenvalues and exact quotient-root evaluations agree, with maximum discrepancy \(7.11\times10^{-15}\). Full characteristic-polynomial factorizations were additionally checked for base hosts of at most 26 vertices. The blow-up eigenvalue and degree identities hold in every tested case.

Other checks include 100 second-moment recurrence steps, explicit-versus-series evaluation of (16) in all three regimes and at a crossover, direct MGF recursion through 100 generations on four small graphs, and 150 comparisons of sparse connected-components calculations with a separate breadth-first search. These are numerical checks of independently rederived proofs, not substitutes for them.

**Percolation runs.** There were 18 hosts and 60 realizations per host, totaling **1,080** realizations. Maximum order was **1,271,586**. For the main A families, \(k=12,b=16,q=0.9\); \(\Delta/\lambda\approx1.4158<1.5\), and the offspring lower bound has \(\mu=1.0702188504\ldots>1\). With \(m=2^h=16^{h/4}\), \(\tau=1/4\), so the proved exponent allows \(c<0.0195811691\ldots\); the unblown exponent allows \(c<0.0244764613\ldots\).

| Family | (h,m) | \(n\) | median \(L_1\) | empirical 10–90% interval | median/\(\log n\) |
|---|---|---:|---:|---|---:|
| A, \(q=0.9\) | (3,1) | 4,382 | 10 | 7–13.1 | 1.193 |
| A, \(q=0.9\) | (4,1) | 69,918 | 16 | 13–24.1 | 1.434 |
| A, \(q=0.9\) | (5,1) | 1,118,494 | 27 | 22–40.1 | 1.939 |
| A, blown up, \(q=0.9\) | (2,4) | 1,144 | 11 | 6.9–16.3 | 1.562 |
| A, blown up, \(q=0.9\) | (3,8) | 35,056 | 21 | 15–31.1 | 2.007 |
| A, blown up, \(q=0.9\) | (4,16) | 1,118,688 | 43.5 | 32.9–57.2 | 3.123 |
| \(p\Delta=1\), \(k=12,b=16\) | (5,1) | 1,118,494 | 19 | 16–24.1 | 1.364 |
| \(p\Delta=1\), blown up | (4,16) | 1,118,688 | 27 | 21–33.2 | 1.939 |
| \(p\Delta=1\), \(k=100,b=108\) | (2,1) | 11,874 | 15 | 7.9–28 | 1.599 |
| \(p\Delta=1\), \(k=100,b=108\) | (3,1) | 1,271,586 | 14 | 10–25.1 | 0.996 |

For each boundary host I used \(q_h=\lambda_h/\Delta_h\), \(\delta_h=\Delta_h/\lambda_h-1\), so \(p=q_h/\lambda_h=1/\Delta_h\) and \(q_h(1+\delta_h)=1\) exactly algebraically (floating evaluation error at most machine precision). In the last two rows the ratio is about **1.09**, \(q_h\approx0.9174321111\), and the spectral margin is bounded away from zero. The boundary runs therefore include an instance close to regular in the specific sense asked for. Both fixed-degree and growing-degree boundary hosts were tested. These are separately chosen finite boundary hosts; \(q_h\) is not claimed to be one fixed number across all heights.

These data are consistent with the proved bounds. At million-vertex sizes the conservative powers from (A) remain around 1–2 vertices, so the data cannot distinguish those eventual powers from logarithmic or polylogarithmic finite-size behavior. At the largest blown boundary case the median divided by \(\log^3 n\) is \(0.00999\ldots\), well below the scale allowed by (C), without demonstrating its sharpness. On boundary families with fixed \(\Delta\), the nonroot branching comparison uses \(\operatorname{Bin}(\Delta-1,p)\) and already has a fixed gap at \(p=1/\Delta\); those particular families have an \(O(\log n)\) upper bound. This prevents a mistaken interpretation of the boundary simulations.

The complete trials, summaries, seed, edge-count diagnostics, algebraic certificates and metadata are in `data/`. Maximum absolute edge-count mean z-score was 2.865 across 18 host cases, with no sampler discrepancy identified. Peak process RSS was **459,538,432 bytes**, inherited nice level **10**, one requested numerical thread, and measured run time **11.65 seconds**. NumPy was 2.2.3 and SciPy 1.15.2. No dense large adjacency matrix was built. Reproduce with:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 code/independent_audit.py
```

## 8. Literature result and value

The primary-source review was of the statements and their assumptions, with relevant proofs inspected where they overlap the claims:

| Primary source and checked location | What it supplies; consequence for (A)–(D) |
|---|---|
| [CMW, 2608.19145v1](https://arxiv.org/abs/2608.19145v1), Lemma 2.4 p. 9; Lemma 3.1(a) p. 11; proof p. 16; discussion and footnote 7 p. 20 | Supplies the walk resolvent, weighted exploration tail, and an existing polynomial finite-tree example. Does not give the clique calibration, blow-up statement, (C), or the min-of-two-walk-counts formula (D). These are extensions of its framework. |
| [DEKK, 2209.03722v3](https://arxiv.org/abs/2209.03722v3), Theorem 2 p. 3 | Gives (B)'s logarithmic order on every host with the specified maximum-degree margin. No novelty for (B). |
| [Diskin–Krivelevich I, 2408.04597](https://arxiv.org/abs/2408.04597), Theorems 1–2 p. 3 | Concerns supercritical percolation on regular graphs, with expansion hypotheses, and a construction with large second components. It does not imply the irregular spectral-subcritical claims here. |
| [Diskin–Krivelevich II, author preprint](https://www.math.tau.ac.il/~krivelev/ERCP2.pdf), Theorem 1 p. 3, surrounding discussion pp. 1–3 | Uses fixed degree \(d\), regularity and expansion in the supercritical regime \(p(d-1)>1\). Its parameter called \(\lambda\) is not the adjacency radius used here. No exact antecedent of (A), (C), or (D) found. |
| [Alon–Benjamini–Stacey, math/0207112](https://arxiv.org/abs/math/0207112), Theorem 2.1 pp. 4–5; Theorem 3.2 p. 14 | Studies uniqueness on bounded-degree expanders and the threshold (1/(d-1)) on high-girth regular expanders. Its branching-process discussion is relevant background, not the near-regular spectral statement or the boundary estimate here. |
| [Bollobás–Borgs–Chayes–Riordan, math/0701346](https://arxiv.org/abs/math/0701346), Theorem 3 PDF p. 8; Theorem 8 and proof pp. 22–23 | Gives logarithmic components for uniformly bounded subcritical graphon kernels, with a multitype branching domination and exponential total-progeny tails. This is a clear ancestor of the mechanism in (C), but its uniform kernel bound does not cover arbitrary \(n/\lambda\to\infty\) here, or state the quantitative \(U^2\log n\) bound. It does not provide (D)'s degree-sensitive exponent. |
| [Nachmias–Peres, 0707.2839](https://arxiv.org/abs/0707.2839), Proposition 1 pp. 2–3 | Gives general upper estimates for regular hosts and critical/near-critical random-regular results. Its hypotheses and scaling in (p(d-1)) differ from the arbitrary-host fixed spectral-gap boundary in (C). |
| [Nachmias–Peres, math/0701316](https://arxiv.org/abs/math/0701316), Theorems 1.2–1.3 pp. 2–3 | Gives critical component, diameter and mixing-time controls under a maximum-degree constraint. The \(n^{2/3}\)-scale bounds do not give (C)'s polylogarithmic conclusion using \(p\lambda\le q<1\). |
| [DEKK irregular products, 2211.10139](https://arxiv.org/abs/2211.10139), Theorem 9 p. 4; construction from p. 15 | Already gives polynomial components below an average-degree threshold on products of stars. For this host \(\lambda=t\sqrt s\), whereas its \(p=c/t\), \(c>1/3\), makes \(p\lambda=c\sqrt s>1\) for sufficiently large \(s\). It is not a predecessor of (A)'s spectral-subcritical near-regular assertion. |

For forward citations, a direct Semantic Scholar lookup returned one citer, and OpenAlex returned zero; raw responses are retained as plain text. I independently followed the original author link for [Anastos–Frieze–Krueger, *Perfect matchings in a random k-out subgraph of the hypercube*](https://www.math.cmu.edu/~af1p/Texfiles/CubeMatching.pdf), dated **27 August 2026**. It cites CMW in background on p. 2 and reference [7] on p. 10. Its perfect-matching theorems do not contain (A), (C), or (D). This verifies the later citation mentioned in the claim. Web searches by source identifier and by the relevant spectral, maximum-degree and resolvent terms found no further substantive 2026 citer addressing Question 5.2. Indexes are incomplete, so “every possible citer has been checked” would be unjustified.

I also retrieved [Krivelevich's September 2026 lecture notes, 2609.28552v1](https://arxiv.org/abs/2609.28552v1), a 77-page primary source surfaced during the search. Its extracted text contains no CMW citation or matching spectral/resolvent statement. It supplied no additional antecedent of the three refinements.

My value assessment is therefore:

- **(A): correct; incremental contribution plausibly new in its exact quantified form.** The finite-tree obstruction is already in CMW. Calibrating the radius with a clique, preserving connectedness, obtaining every strict \(q(1+\delta)>1\), and retaining the obstruction at arbitrary spectral growth exponent below 1 are the additional content. None contradicts the source.
- **(B): correct and known.** Both the upper-order bound and the elementary cycle obstruction are established territory.
- **(C): correct; exact quantitative statement not found in the inspected literature.** Its use of susceptibility and an MGF supersolution is a standard kind of branching argument. The useful new content, if priority holds, is this explicit uniform consequence of the two stated inequalities, not a new branching-process principle.
- **(D): correct; exact refinement not found in the inspected literature.** It is an explicit improvement of an existing proof by retaining the minimum of two available walk bounds. Its value is quantitative, and it leaves an exponent gap.

Question 5.2 remains unresolved by these results. Below the fixed degree margin the worst-case order is logarithmic; above it polynomial behavior is possible; at the boundary the supplied broad upper estimate is cubic logarithmic and is not shown sharp. A tight answer for all prescribed \((n,\Delta,\lambda)\), optimal powers in the polynomial regime, and a sharp boundary classification have not been supplied. Acceptance as a partial mathematical contribution, with the minor status and scope revisions listed above, is warranted. Acceptance as a counterexample to CMW, or as a solution of Question 5.2, is not.

Task: “You are an independent referee … Break it if it is wrong.” — first local clock reading 2026-11-13 09:17:20 +04 \(Asia/Tbilisi\).
