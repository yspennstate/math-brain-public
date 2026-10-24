Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.

# P03 FEI — sharp paid recombination and a fixed-Rényi/Clarkson obstruction

## Status / before-after

**Parent problem.** Friedgut--Kalai Fourier entropy--influence (FEI): prove one finite universal constant `C` such that
\[
H(\widehat f^{\,2})\le C I(f)
\]
for every Boolean function on every finite uniform cube.

**Source-level status before -> after:** **OPEN/PARTIAL -> OPEN/PARTIAL.** The unrestricted universal finite upper bound remains **UNKNOWN -> UNKNOWN**. P03's inherited native finite-dimensional atlas remains **6 -> 6**. No finite check, sharp auxiliary constant, or restricted theorem below is promoted to full FEI.

This run makes two substantive mechanism-level advances, using a method different from the preceding Wiener/product-width route.

1. The already-proved universal paid dependent-branch recombination coefficient `2/ln 2` is **exactly sharp**. A bent-background one-point perturbation has one-step Jensen--Shannon recombination cost divided by folded queried influence tending to `2/ln 2`. Thus the recombination coefficient cannot be improved universally; any remaining logarithmic divergence in that family lies in the hereditary allocation term, not in recombination.
2. For every fixed `1 <= s < 2`, the Fourier Rényi mass
   \[
   M_s(f)=\sum_A|\widehat f(A)|^s
   \]
   is a genuine physical-restriction supermartingale by a scalar Clarkson inequality, with an **exact adaptive-tree telescope**. The Shannon entropy decrement is its endpoint derivative as `s -> 2-`. However the one-point defect family proves that **every fixed exponent `s<2` is unpayable by influence**, locally and globally: its Clarkson deficit divided by queried influence grows like a positive constant times `2^{n(2-s)}`. Therefore a fixed-exponent interpolation cannot close FEI. Any viable Rényi interpolation must move the exponent toward two in a state-dependent way and pay the parameter-change error.

No fresh variables are introduced. No retired resolvent/interpolation inequality, false pointwise erasure shortcut, fixed-coefficient affine drift, Han absolute-overlap selector, derivative-degree scalar scheduler, blind curvature bound, or direct curvature/query ratio is revived.

## Dependencies actually consumed

The progress-first instruction was followed. I read only the complete dependencies needed for these arguments rather than scanning the repository.

- `operations/PROGRESS20_2026-09-20.md`, blob `4a207f06e5c8294c83bcabcd9a1477f26f54b441`: P03 owns T01; new derivation has priority; the current complementary FEI theory worker is NM13-02.
- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`: the fresh-control result is explicitly restricted and not full FEI.
- The complete fresh-control proof `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-19/2026-09-19T22-18-30Z__report.md`, blob `22362306d41f9b6d3d0f221ddda3d303b8a47968`: for `Gamma_c f`, `c>=3`, and `2^{-c}M_0(f)<=1`, it proves `L(Gamma_c f)<=12 Delta_aff(Gamma_c f)`. It appends fresh controls and is not used as a fixed-domain theorem here.
- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`: full FEI remains open and the retired/refuted routes remain retired.
- P03 paid-recombination report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T02-31-19__fei-hereditary-recombination-refinement.md`, blob `8ffb9da5bc03c30e6ed5f62adc17640d1570878c`: exact one-step identity
  \[
  H(f)-\frac{H(f^+)+H(f^-)}2=B_i(f)+J_i^{\rm rec}(f),
  \]
  exact tree telescopes, and the valid universal bound
  \[
  0\le J_i^{\rm rec}(f)\le\frac2{\ln2}j_i(f),
  \qquad j_i=\min\{\operatorname{Inf}_i,1-\operatorname{Inf}_i\}.
  \]
- `proofnet24/P03-fei/continuations/2026-09-20-entropy-continuity/ERASURE_RIGIDITY.md`, blob `52a0834a88d957d0331da95aa444406530741f7f`: the bent-background one-point family used below was already introduced there to prove that an individual erasure ratio `B_i/Inf_i` can diverge. That report also gives a finite three-variable counterexample to the stronger recombination guess `Z<=2J`, but explicitly does **not** determine the optimal constant. The new result below is the all-dimensional sharpness calculation for the already-valid `2/ln2` coefficient; the family itself is not relabeled as new.
- Newest companion report `proofnet24/NM13-02/progress-entropy/runs/2026-09-20/2026-09-20T10-08-55+0300__quadratic-normalized-wiener-hereditary.md`, blob `aec413db2f0dca3b1733e40ba9fc22807bc909b8`: `Lambda_2` is restriction-monotone and gives a hereditary coefficient `C_QW(Lambda_2)`. This remains a parameterized theorem, not full FEI.
- Newest own substantive P03 report `proofnet24/P03-fei/runs/2026-09-20/2026-09-20T10-27-34+0300__fei-quadratic-product-wiener-recombination.md`: it defines quadratic-product width `Omega_2`, proves max rather than multiplicative recombination over independent high-degree blocks, and localizes the remaining high-degree difficulty to a connected interaction core. The present run does not duplicate that product decomposition; it attacks the orthogonal question of the exact paid recombination constant and a new fixed-Rényi interpolation route.
- Current `POSTED.md` was checked for exact-scope exclusion. The posted entropy/singularity result is a different restricted result; no posted unrestricted FEI theorem or exact claims below were found.

## Current source scope

A fresh 20 September 2026 source check of González--MacManus--Pereyra, arXiv:2606.00246, *Further evidence towards the Fourier Entropy-Influence conjecture*, still states universal FEI as a conjecture. Its restriction/stopping-tree mechanism observes that a suitable local branching inequality would imply FEI, and proves proper subclasses rather than the universal branching estimate.

The current Li--Han arXiv:2512.03117 strengthens Han's general bound to a coordinate-profile logarithmic correction; it still does not give a universal constant times total influence. The Friedgut--Kalai 1996 attribution remains the source attribution used in current FEI literature.

A bounded search did not locate the exact sharp recombination computation or the fixed-`s` Clarkson obstruction below. That is negative evidence only. **Publication priority is UNVERIFIED.**

## 1. Notation and the inherited allocation/recombination split

For Boolean `f` on `F_2^n`, use normalized Walsh coefficients `a_A=\widehat f(A)` and squared spectral law
\[
p_A=a_A^2.
\]
Let
\[
H(f)=-\sum_Ap_A\log_2p_A,
\qquad
I(f)=\sum_i\operatorname{Inf}_i(f).
\]
For spectral random set `Z`, define
\[
B_i(f)=H(Z_i\mid Z_{-i}).
\]
At a physical split at coordinate `i`, the established exact identity is
\[
H(f)-\frac{H(f^+)+H(f^-)}2
=B_i(f)+J_i^{\rm rec}(f),
\tag{1.1}
\]
where `J_i^{rec}` is the equal-weight Jensen--Shannon divergence between the squared Fourier laws of `f^+` and `f^-`. The established universal payment is
\[
0\le J_i^{\rm rec}(f)
\le\frac2{\ln2}j_i(f),
\qquad
j_i(f)=\min\{\operatorname{Inf}_i(f),1-\operatorname{Inf}_i(f)\}.
\tag{1.2}
\]
The same coefficient sums over arbitrary adaptive physical trees. This run determines that its constant is best possible.

## 2. The universal recombination coefficient `2/ln 2` is sharp

### Theorem 2.1 (sharp one-step recombination)

Among Boolean physical splits,
\[
\boxed{
\sup_{f,i:\ 0<j_i(f)}
\frac{J_i^{\rm rec}(f)}{j_i(f)}
=\frac2{\ln2}.
}
\tag{2.1}
\]
Consequently the coefficient `2/ln2` in the arbitrary stopping-tree recombination theorem cannot be replaced by any smaller universal constant.

### Proof

The upper bound is exactly the already-proved inequality (1.2). It remains to construct a Boolean sequence attaining it asymptotically.

Let `d=2m` be even, `N=2^d`, and put
\[
g(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{d-1}x_d}.
\tag{2.2}
\]
This is a quadratic bent function and `g(0)=1`. Write
\[
\rho=N^{-1/2},\qquad \delta=N^{-1}=\rho^2.
\]
Every Fourier coefficient has the form
\[
\widehat g(S)=\varepsilon_S\rho,
\qquad \varepsilon_S\in\{-1,1\}.
\tag{2.3}
\]
Fourier inversion at `0` gives
\[
\sum_S\widehat g(S)=g(0)=1,
\]
so
\[
\sum_S\varepsilon_S=\rho^{-1}.
\]
Hence the fractions of positive and negative Fourier signs are respectively
\[
\frac{1+\rho}{2},\qquad \frac{1-\rho}{2}.
\tag{2.4}
\]

Let `h` be obtained from `g` by flipping only the value at the origin:
\[
h=g-2\mathbf1_{\{0\}}.
\tag{2.5}
\]
Then for every `S`,
\[
\widehat h(S)=\rho\varepsilon_S-\frac2N
=\rho(\varepsilon_S-2\rho).
\tag{2.6}
\]
Now introduce one physical control coordinate `t` and let the two restrictions of a parent Boolean function `F` be `g` and `h`. The restrictions disagree at exactly one of the `N` points, so
\[
\operatorname{Inf}_t(F)=\delta,
\qquad
j_t(F)=\delta.
\tag{2.7}
\]

Let `P,Q` be the squared Fourier laws of `g,h`. Since `P(S)=1/N`, the likelihood ratio `Q(S)/P(S)` assumes only the two values
\[
r_+=(1-2\rho)^2,
\qquad
r_-=(1+2\rho)^2,
\tag{2.8}
\]
with proportions from (2.4).

For `r>=0`, define
\[
\psi(r)
=\frac12\log_2\frac2{1+r}
+\frac r2\log_2\frac{2r}{1+r},
\tag{2.9}
\]
with the continuous convention at `r=0`. A direct expansion of equal-weight Jensen--Shannon divergence gives the exact identity
\[
J_t^{\rm rec}(F)
=\frac{1+\rho}{2}\psi(r_+)
 +\frac{1-\rho}{2}\psi(r_-).
\tag{2.10}
\]

Differentiate (2.9):
\[
\psi'(r)=\frac12\log_2\frac{2r}{1+r},
\qquad
\psi''(r)=\frac1{2\ln2\,r(1+r)}.
\tag{2.11}
\]
Thus
\[
\psi(1)=\psi'(1)=0,
\qquad
\psi''(1)=\frac1{4\ln2},
\]
and Taylor's theorem gives
\[
\psi(r)=\frac{(r-1)^2}{8\ln2}+O(|r-1|^3)
\quad(r\to1).
\tag{2.12}
\]
Because
\[
r_\pm-1=\pm4\rho+4\rho^2,
\]
(2.10)--(2.12) yield
\[
J_t^{\rm rec}(F)
=\frac2{\ln2}\rho^2+O(\rho^3)
=\frac2{\ln2}\delta+O(\delta^{3/2}).
\tag{2.13}
\]
Combining with (2.7),
\[
\frac{J_t^{\rm rec}(F)}{j_t(F)}
\longrightarrow\frac2{\ln2}.
\tag{2.14}
\]
Together with the universal upper bound (1.2), this proves (2.1).

For the tree statement, take the one-node physical restriction tree that splits only at `t` and stops at its two children. Its recombination sum is exactly `J_t^{rec}(F)` and its charged folded influence is exactly `j_t(F)`. Therefore any smaller universal aggregate-tree coefficient would contradict (2.14). QED.

### Interpretation

The same bent-background one-point family was previously used to prove
\[
B_t(F)/j_t(F)\sim\log_2(1/j_t(F)),
\]
so its local allocation ratio diverges. The new calculation shows simultaneously that its recombination term is only
\[
\left(\frac2{\ln2}+o(1)\right)j_t(F).
\]
Hence this canonical bad split separates the two mechanisms cleanly: **the logarithmic obstruction is entirely hereditary allocation; the recombination payment is bounded and already uses its best possible universal coefficient.** Trying to improve `2/ln2` cannot remove the FEI obstruction.

## 3. A nonnegative fixed-Rényi/Clarkson restriction potential

The preceding theorem closes one avenue for improving recombination. I therefore tested a genuinely different interpolation mechanism aimed at the allocation/decrement itself.

For `1<=s<2`, define the Fourier `s`-mass
\[
M_s(f)=\sum_A|\widehat f(A)|^s.
\tag{3.1}
\]
This is the unnormalized spectral Rényi mass of order `s/2`.

### Lemma 3.1 (scalar Clarkson inequality in the needed range)

For real `a,b` and `1<=s<=2`,
\[
\boxed{
\frac{|a+b|^s+|a-b|^s}{2}
\le |a|^s+|b|^s.
}
\tag{3.2}
\]

### Proof

At `s=1`, the left side equals `max{|a|,|b|}`, hence is at most `|a|+|b|`.

Assume `1<s<=2`. By homogeneity and symmetry, take `|a|>=|b|`, set `t=|b|/|a| in [0,1]`, and reduce to
\[
(1+t)^s+(1-t)^s\le2(1+t^s).
\tag{3.3}
\]
Let
\[
F(t)=2(1+t^s)-(1+t)^s-(1-t)^s.
\]
Then `F(0)=0`, and with `r=s-1 in (0,1]`,
\[
F'(t)=s\left[2t^r-(1+t)^r+(1-t)^r\right].
\]
Subadditivity of `x^r` on the nonnegative line gives
\[
(1+t)^r=((1-t)+2t)^r
\le(1-t)^r+(2t)^r
\le(1-t)^r+2t^r,
\]
so `F'(t)>=0`. Hence `F(t)>=0` and (3.2) follows. QED.

### Theorem 3.2 (exact adaptive Clarkson telescope)

For a physical split at coordinate `i`, define
\[
D_{s,i}(f)
:=M_s(f)-\frac{M_s(f^+)+M_s(f^-)}2.
\tag{3.4}
\]
Then for every `1<=s<=2`,
\[
\boxed{D_{s,i}(f)\ge0.}
\tag{3.5}
\]
For every full adaptive physical restriction tree `T`, with node cylinder weights `w_v`,
\[
\boxed{
\sum_{v\in T^\circ}w_vD_{s,i(v)}(f_v)
=M_s(f)-1.
}
\tag{3.6}
\]

### Proof

Pair the parent Fourier coefficients by the queried bit. If `A` does not contain `i`, write
\[
a=\widehat f(A),\qquad b=\widehat f(A\cup\{i\}).
\]
The two child coefficients at residual label `A` are exactly
\[
\widehat{f^+}(A)=a+b,
\qquad
\widehat{f^-}(A)=a-b.
\]
Applying Lemma 3.1 to each pair and summing gives (3.5).

For (3.6), multiply (3.4) at node `v` by `w_v`. Since each child has weight `w_v/2`, all nonroot internal `M_s` terms cancel on summation. A full tree ends at constants, and every constant leaf has `M_s=1`; the leaf weights sum to one. The remaining difference is exactly `M_s(f)-1`. QED.

This is a genuine dependent-branch supermartingale/telescope and requires no fresh variables or branch independence.

## 4. Shannon entropy is exactly the endpoint derivative

### Theorem 4.1 (endpoint identities)

For every Boolean function,
\[
\boxed{
H(f)=\frac2{\ln2}
\lim_{s\uparrow2}\frac{M_s(f)-1}{2-s}.
}
\tag{4.1}
\]
At every physical split,
\[
\boxed{
H(f)-\frac{H(f^+)+H(f^-)}2
=\frac2{\ln2}
\lim_{s\uparrow2}\frac{D_{s,i}(f)}{2-s}.
}
\tag{4.2}
\]

### Proof

The Fourier support is finite, so termwise differentiation is valid. At `s=2`, Parseval gives `M_2(f)=1`, and
\[
M'_2(f)=\sum_A|\widehat f(A)|^2\ln|\widehat f(A)|.
\]
Since
\[
H(f)=-\sum_A|\widehat f(A)|^2\log_2|\widehat f(A)|^2
=-\frac2{\ln2}M'_2(f),
\]
(4.1) follows from the left derivative at two.

Apply the same derivative identity to the parent and the two children in (3.4). Because `D_{2,i}=0`,
\[
\lim_{s\uparrow2}\frac{D_{s,i}}{2-s}
=-D'_{2,i}
=\frac{\ln2}{2}
\left(H(f)-\frac{H(f^+)+H(f^-)}2\right),
\]
which is (4.2). QED.

Thus `D_{s,i}` is not an arbitrary potential: after rescaling, its endpoint derivative is exactly the full Shannon entropy decrement that a stopping-tree proof must pay.

## 5. Every fixed exponent `s<2` is nevertheless unpayable by influence

The exact telescope might suggest proving, for one fixed `s<2`, either a local inequality
\[
D_{s,i}(f)\le K_s\operatorname{Inf}_i(f)
\tag{5.1}
\]
or a global inequality
\[
M_s(f)-1\le K_s I(f).
\tag{5.2}
\]
Either would provide a clean amortized interpolation handle. Both are false for every fixed `s<2`.

### Theorem 5.1 (one-point obstruction to every fixed Rényi exponent)

For `n>=2`, let
\[
w_n(x)=1-2\mathbf1_{\{0\}}(x),
\qquad N=2^n.
\tag{5.3}
\]
For every fixed `1<=s<2` and every coordinate `i`,
\[
\boxed{
\frac{D_{s,i}(w_n)}{\operatorname{Inf}_i(w_n)}
\sim
\left(2^{s-1}-2^{2s-3}\right)N^{2-s}
\longrightarrow\infty.
}
\tag{5.4}
\]
Also
\[
\boxed{
\frac{M_s(w_n)-1}{I(w_n)}
\sim\frac{2^{s-1}}{n}N^{2-s}
\longrightarrow\infty.
}
\tag{5.5}
\]
Hence no finite constant `K_s` can make either (5.1) or (5.2) hold universally for a fixed `s<2`.

### Proof

The Fourier coefficients of `w_n` are
\[
\widehat w_n(\varnothing)=1-\frac2N,
\qquad
\widehat w_n(A)=-\frac2N\quad(A\ne\varnothing).
\]
Therefore
\[
M_s(w_n)
=\left(1-\frac2N\right)^s
 +(N-1)\left(\frac2N\right)^s.
\tag{5.6}
\]
Restricting any coordinate gives one constant child and one copy of `w_{n-1}`. Hence
\[
D_{s,i}(w_n)
=M_s(w_n)-\frac{1+M_s(w_{n-1})}{2}.
\tag{5.7}
\]
For fixed `1<s<2`, expansion of (5.6) gives
\[
M_s(w_n)
=1+2^sN^{1-s}-\frac{2s}{N}
+o(N^{1-s}),
\tag{5.8}
\]
while, since `w_{n-1}` lives on `N/2` points,
\[
M_s(w_{n-1})
=1+2^{2s-1}N^{1-s}-\frac{4s}{N}
+o(N^{1-s}).
\tag{5.9}
\]
The `N^{-1}` terms cancel in (5.7), leaving
\[
D_{s,i}(w_n)
=\left(2^s-2^{2s-2}\right)N^{1-s}
+o(N^{1-s}).
\tag{5.10}
\]
At `s=1`, (5.6) gives `M_1(w_n)=3-4/N` and (5.7) gives exactly `D_{1,i}(w_n)=1`, which is also (5.10) at `s=1`.

The physical disagreement across coordinate `i` occurs exactly when all other coordinates are zero, so
\[
\operatorname{Inf}_i(w_n)=\frac2N,
\qquad
I(w_n)=\frac{2n}{N}.
\tag{5.11}
\]
Dividing (5.10) by `2/N` proves (5.4); the coefficient is positive because
\[
2^{s-1}-2^{2s-3}=2^{s-1}(1-2^{s-2})>0
\]
for `s<2`.

Finally (5.6) gives
\[
M_s(w_n)-1\sim2^sN^{1-s}
\]
(with the same limiting statement valid at `s=1`), and division by `2n/N` proves (5.5). QED.

### Consequence for the route

The positive telescope (3.6) and endpoint identity (4.2) are exact, but **no fixed distance from the Shannon endpoint can be amortized by influence**. The obstruction grows polynomially in `N` with exponent `2-s`. Therefore any future interpolation attack must let `s=s(v)` approach two as the local rare-event scale shrinks. Once `s` varies with the node, the exact telescope (3.6) no longer closes without an additional parameter-change term. Controlling that new term is the precise surviving interpolation subproblem; simply choosing a fixed `s<2` is now retired.

This is distinct from the older failed resolvent/drift routes: the new potential is genuinely nonnegative under every physical restriction and telescopes exactly. Its failure is quantitative payment by influence, not a sign failure or a false identity.

## 6. How the two new results sharpen the full-FEI obstruction

The exact decomposition at every queried node is
\[
\text{entropy decrement}
=\text{hereditary allocation }B_i
+\text{recombination }J_i^{\rm rec}.
\]
The first result proves that recombination already has the best possible universal linear payment `2/ln2`. There is no hidden constant-factor improvement there capable of removing logarithmic bad splits.

The second result supplies a new nonnegative interpolation of the **entire** entropy decrement, but proves that every fixed Rényi order below Shannon is too coarse on rare one-point defects. Thus both obvious scalar repairs are now sharply delimited.

Combined with the newest quadratic-product width theorem, the remaining broad target is narrower:

> Construct a structure-sensitive hereditary allocation/stopping rule on a single connected high-degree interaction core, or an endpoint-adaptive (`s -> 2`) interpolation whose parameter-change cost is itself paid by influence. It must preserve the exact dependent-branch bookkeeping and cannot rely on improving the universal recombination coefficient.

No claim is made that such a rule is currently available.

## 7. Sanity checks actually executed

New executable checker:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-15-00Z__check_recombination_sharpness_clarkson.py`

creation commit `9f417989da3b1860f5c5681b7e9a0e99134fe61c`, blob `7a55956ec854d01b85978cd1bba9826aeba6d1ae`.

Archived actual output:

`proofnet24/P03-fei/runs/2026-09-20/2026-09-20T08-15-00Z__recombination_sharpness_clarkson_check.json`

creation commit `096cd70d196edc7013da42ad1bc10e3b6a49104b`, blob `72bd891872923b0fe755b1bbe4febf8204106685`.

The checker was executed before persistence and reports `PASS`. It performs:

1. exhaustive testing of all **65,812 Boolean functions through dimension four**, totaling **262,948 coordinate cases**, for nonnegativity of the Clarkson deficits at `s=1,1.25,1.5,1.75`;
2. exact endpoint-derivative versus Shannon-decrement numerical comparison in every one of those coordinate cases, with maximum discrepancy `1.4432899320127035e-15`;
3. direct Walsh verification of the bent-background one-point formula through background dimension 12, with maximum direct-vs-closed-form JS discrepancy `5.843849709696869e-17`;
4. formula evaluation through background dimension 20, where `J_rec/j=2.8853891645329224`, within `9.172450043948288e-7` of `2/ln2=2.8853900817779268`;
5. the fixed-`s` one-point asymptotics at dimensions 8,16,32,40. For example, at `s=3/2`, the normalized local ratio converges to `sqrt(2)-1=0.414213562373...`, while the unnormalized deficit/influence ratio grows as `N^{1/2}`.

These computations are self-checks only; the all-dimensional statements rest on the proofs above.

## 8. Metrics and exact remaining obligation

- full Friedgut--Kalai FEI: `OPEN -> OPEN`;
- unrestricted universal finite source constant: `UNKNOWN -> UNKNOWN`;
- P03 native finite-dimensional atlas: `6 -> 6`;
- fresh-variable dependence in the new results: `none`;
- paid recombination coefficient: `2/ln2 upper bound -> 2/ln2 EXACT OPTIMUM`;
- fixed-`s` Clarkson/Rényi supermartingale: `new exact telescope`;
- fixed-`s` universal influence payment: `candidate -> REFUTED for every 1<=s<2`;
- independent audit: `pending`;
- publication priority: `UNVERIFIED`.

The exact full-scope obligation remains a universal hereditary allocation/payment mechanism. The present run rules out spending another run on either constant-improvement of the JS recombination coefficient or a fixed Rényi exponent. A nonredundant next attack is an **endpoint-adaptive allocation potential** with an explicit correction for changing `s`, or a direct structure-sensitive selector on the connected high-degree core isolated by the preceding `Omega_2` theorem.

## ledger_delta

```yaml
ledger_delta:
  owner: P03
  parent: T01_Friedgut_Kalai_FEI
  source_status_before: OPEN_PARTIAL
  source_status_after: OPEN_PARTIAL
  universal_constant_before: UNKNOWN
  universal_constant_after: UNKNOWN
  native_finite_atlas_before: 6
  native_finite_atlas_after: 6
  new_claims:
    - id: P03-FEI-RECOMBINATION-CONSTANT-SHARP
      status: PROVED_SELF_CHECKED_AUDIT_PENDING
      statement: "The universal one-step and arbitrary-tree paid recombination coefficient 2/ln2 is optimal; bent-background one-point perturbations have J_rec/j -> 2/ln2."
    - id: P03-FEI-CLARKSON-RENYI-TELESCOPE
      status: PROVED_SELF_CHECKED_AUDIT_PENDING
      statement: "For every 1<=s<=2, M_s=sum |fhat|^s is a physical-restriction supermartingale and every full adaptive tree telescopes its deficits exactly to M_s(f)-1; Shannon decrement is the s->2 endpoint derivative."
    - id: P03-FEI-FIXED-RENYI-PAYMENT-OBSTRUCTION
      status: PROVED_SELF_CHECKED_AUDIT_PENDING
      statement: "For every fixed 1<=s<2, one-point defects force both local Clarkson-deficit/influence and global (M_s-1)/I ratios to diverge, so no fixed exponent supplies a universal influence-paid interpolation."
  mechanism_progress:
    recombination: "closed quantitatively: existing coefficient is sharp"
    interpolation: "new exact positive telescope, but all fixed exponents below 2 are decisively obstructed"
    remaining: "hereditary allocation on connected high-degree cores or endpoint-adaptive s(v) with paid exponent-change error"
  preserved_failures:
    - pointwise_erasure_shortcut
    - all_fixed_coefficient_affine_drift
    - resolvent_interpolation
    - Han_absolute_overlap_selector
    - derivative_degree_scalar_schedule
    - blind_root_curvature_bound
    - direct_curvature_query_ratio
    - fixed_Renyi_exponent_payment
  preserved_positive_results:
    - paid_dependent_branch_recombination
    - quadratic_normalized_Wiener_control
    - quadratic_product_Wiener_width
    - restricted_fresh_control_theorem_with_original_hypotheses
  fresh_controls_used: false
  checker:
    status: PASS
    script_commit: 9f417989da3b1860f5c5681b7e9a0e99134fe61c
    script_blob: 7a55956ec854d01b85978cd1bba9826aeba6d1ae
    output_commit: 096cd70d196edc7013da42ad1bc10e3b6a49104b
    output_blob: 72bd891872923b0fe755b1bbe4febf8204106685
  peer_coordination:
    companion: NM13-02
    peer_new_result_preserved: "quadratic-normalized Wiener hereditary theorem"
    own_previous_result_preserved: "quadratic-product width Omega_2 and cross-block recombination"
    overlap_policy: "no peer file/claim edited; present method is sharp JS plus fixed-Renyi endpoint interpolation"
  independent_audit: PENDING
  publication_priority: UNVERIFIED
```

**End of complete run report.**
