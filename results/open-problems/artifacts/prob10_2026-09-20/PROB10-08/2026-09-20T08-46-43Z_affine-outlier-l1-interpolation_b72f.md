Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested, but no authenticated runtime telemetry available to this run establishes that model/effort setting.

# PROB10-08 artifact — quantitative L1 rarity of the actual Haiman affine slow eigenmode

Status: **PROVED auxiliary mechanism theorem / Salez Problem 2.3 remains OPEN / no new source-level cutoff class certified here / independent validation pending / worldwide novelty UNVERIFIED**.

This artifact concerns Justin Salez, arXiv:2508.21055v1, Problem 2.3, under the source's rate-one continuous-time simple-random-walk convention. It does not reopen the posted Abelian Cayley/product-condition target.

## 1. Why this is a different recovery method

The preceding R16/PROB10-08 runs already exhausted or fenced off the following routes: product-varentropy, synchronous/tensor products, moving-weight/local-Poincare, ordinary or Hecke curvature, time-zero/global subcommutation, naive L2/Green mixing, relation concatenation, and the generic trace/nuclear superlevel estimate. The immediately preceding report left a concrete unresolved datum in the source-admissible affine stress test of Haiman--Schildkraut--Zhang--Zhao: the canonical induced-representation vector has an exactly L2-heavy/L1-rare matrix coefficient, but the **actual perturbed slow eigenvector** had only an L2 perturbation bound, not an L1 bound.

This run attacks precisely that missing datum. The new device is a two-norm resolvent interpolation: use the spectral gap of the lifted LPS subgroup action for long powers, and use the small L1 size of the perturbation source for short powers. This is neither another Green-function estimate nor another tensor/product construction.

The other two approaches tested in this run are recorded in Section 8 and were rejected for exact quantitative reasons.

## 2. Frozen affine family and representation block

Use the 18-regular Cayley graphs from Haiman--Schildkraut--Zhang--Zhao,

\[
\Gamma_q=\Pi_q\ltimes V_q,
\qquad
\Pi_q=\operatorname{SL}(2,q),
\qquad
V_q=\mathbb F_q^2,
\]

with the 16 lifted LPS subgroup generators `S` and the two translations `t,t^{-1}`. Put

\[
r:=|V_q|=q^2.
\]

The transitive permutation representation on the `r` cosets of `Pi_q` decomposes as

\[
1\oplus\phi_q,
\qquad \dim\phi_q=r-1.
\]

Work with the probability inner product on the `r` cosets,

\[
\langle f,g\rangle=\frac1r\sum_{x\in V_q}f(x)g(x),
\qquad
\|f\|_{p,\pi}=\left(\frac1r\sum_x|f(x)|^p\right)^{1/p}.
\]

Let `u_0` be the normalized contrast at the zero coset,

\[
u_0(0)=\sqrt{r-1},
\qquad
u_0(x)=-\frac1{\sqrt{r-1}}\quad(x\ne0).
\tag{2.1}
\]

Then `||u_0||_2=1`, `u_0 \perp 1`, and

\[
\|u_0\|_{1,\pi}=\frac{2\sqrt{r-1}}r=O(r^{-1/2}).
\tag{2.2}
\]

Let

\[
A_0:=\sum_{s\in S}\phi_q(s),
\qquad
B:=\phi_q(t)+\phi_q(t^{-1}),
\qquad
C:=A_0+B.
\tag{2.3}
\]

Because every subgroup generator fixes the zero coset,

\[
A_0u_0=16u_0.
\tag{2.4}
\]

Set

\[
W:=\{1,u_0\}^{\perp}.
\]

The lifted LPS spectral bound used in the Haiman construction gives

\[
\|A_0|_W\|_{2\to2}\le4\sqrt7.
\]

Since `||B||_{2->2}<=2`, the compression

\[
C_W:=P_WCP_W|_W
\]

satisfies

\[
\boxed{
\|C_W\|_{2\to2}\le \beta:=2+4\sqrt7=12.583005\ldots<16.
}
\tag{2.5}
\]

This is the spectral separation which the previous L2-only perturbation argument did not combine with the special L1 geometry of `u_0`.

## 3. Exact perturbation source

For a point `z`, let `u_z` be the translate of the contrast (2.1) with the distinguished coordinate at `z`. Since `t` and `t^{-1}` send zero to two distinct nonzero cosets for the Haiman family,

\[
Bu_0=u_a+u_b
\qquad(a,b\ne0,\ a\ne b).
\tag{3.1}
\]

Distinct normalized point contrasts satisfy

\[
\langle u_z,u_w\rangle=-\frac1{r-1}\qquad(z\ne w).
\tag{3.2}
\]

Hence

\[
\langle u_0,Bu_0\rangle=-\frac2{r-1}.
\tag{3.3}
\]

Define the `W`-source

\[
s:=P_WBu_0=Bu_0+\frac2{r-1}u_0.
\tag{3.4}
\]

Then

\[
\|s\|_2^2
=2-\frac2{r-1}-\frac4{(r-1)^2}
\le2,
\tag{3.5}
\]

while, crucially,

\[
\boxed{
\|s\|_{1,\pi}=O(r^{-1/2}).
}
\tag{3.6}
\]

Indeed each point contrast has `L1(pi)` norm `2 sqrt(r-1)/r`; (3.4) gives the claim directly. Also

\[
\|s\|_\infty=(1+o(1))\sqrt r,
\qquad
\|u_0\|_{1,\pi}=(2+o(1))r^{-1/2},
\tag{3.7}
\]

so

\[
\|s\|_\infty\|u_0\|_{1,\pi}=2+o(1).
\tag{3.8}
\]

## 4. A nontrivial L1 operator bound on the compressed bulk

Although `C_W` is an orthogonal compression rather than a Markov kernel, its L1 norm stays bounded by `20+o(1)`, not by an uncontrolled dimension-dependent quantity.

### Lemma 4.1

For `f in W`,

\[
\boxed{
\|C_Wf\|_{1,\pi}
\le L_r\|f\|_{1,\pi},
\qquad
L_r:=18+\|s\|_\infty\|u_0\|_{1,\pi}=20+o(1).
}
\tag{4.1}
\]

### Proof

The full adjacency operator `C` is a sum of 18 permutations, hence

\[
\|Cf\|_{1,\pi}\le18\|f\|_{1,\pi}.
\tag{4.2}
\]

It preserves constants, so `Cf` is mean zero whenever `f` is. Therefore projecting a mean-zero vector onto `W` only removes its `u_0` component. Since

\[
Cu_0=\left(16-\frac2{r-1}\right)u_0+s,
\]

and `f perp u_0`, self-adjointness gives

\[
\langle u_0,Cf\rangle=\langle Cu_0,f\rangle=\langle s,f\rangle.
\]

Thus

\[
C_Wf=Cf-\langle s,f\rangle u_0.
\]

Using `|<s,f>| <= ||s||_infty ||f||_{1,pi}` and (4.2) proves (4.1). QED.

The combination `(2.5)+(4.1)` is the key new input: powers of `C_W` have a small spectral norm `beta^k` but, before the spectral estimate becomes useful, grow in L1 by at most `L_r^k`.

## 5. Two-norm resolvent interpolation for the actual slow eigenvector

Let `mu_q` be the top eigenvalue of `C` on `phi_q`, and let `u` be a unit eigenvector. Rayleigh testing on `u_0` gives

\[
\mu_q\ge a_r:=\langle u_0,Cu_0\rangle
=16-\frac2{r-1}.
\tag{5.1}
\]

Since `a_r>beta` for all sufficiently large `q`, the top eigenvector cannot lie in `W`. Write

\[
u=\alpha u_0+w,
\qquad w\in W.
\tag{5.2}
\]

Projecting `Cu=mu_q u` onto `W` and using (3.4) gives the exact equation

\[
(\mu_q I-C_W)w=\alpha s.
\tag{5.3}
\]

Because `mu_q>beta`,

\[
w=\frac{\alpha}{\mu_q}
\sum_{k\ge0}\left(\frac{C_W}{\mu_q}\right)^k s
\tag{5.4}
\]

in L2.

For any integer `K>=1`, split (5.4) at `K`. Lemma 4.1 and (3.6) give

\[
\left\|
\frac{\alpha}{\mu_q}
\sum_{k<K}\left(\frac{C_W}{\mu_q}\right)^ks
\right\|_{1,\pi}
\le
O(r^{-1/2})\sum_{k<K}\frac{L_r^k}{\mu_q^{k+1}}.
\tag{5.5}
\]

For the tail, `||f||_1<=||f||_2`, (2.5), and (3.5) give

\[
\left\|
\frac{\alpha}{\mu_q}
\sum_{k\ge K}\left(\frac{C_W}{\mu_q}\right)^ks
\right\|_{1,\pi}
\le
O(1)\left(\frac\beta{\mu_q}\right)^K.
\tag{5.6}
\]

Take

\[
K=\left\lfloor
\frac{\log r}{2\log(L_r/\beta)}
\right\rfloor.
\tag{5.7}
\]

The two bounds balance. Since `mu_q>=a_r`, one obtains, for every fixed

\[
\eta<\eta_*:=
\frac{\log(16/\beta)}{2\log(20/\beta)},
\qquad
\beta=2+4\sqrt7,
\tag{5.8}
\]

that for all sufficiently large `q`,

\[
\boxed{
\|w\|_{1,\pi}=O_\eta(r^{-\eta}).
}
\tag{5.9}
\]

Numerically,

\[
\boxed{
\eta_*=0.2592245387\ldots .
}
\tag{5.10}
\]

Since `||u_0||_1=O(r^{-1/2})`, the actual normalized slow eigenvector satisfies

\[
\boxed{
\|u\|_{1,\pi}=O_\eta(r^{-\eta})
\quad\text{for every }\eta<\eta_*.
}
\tag{5.11}
\]

This is the promised movement beyond the predecessor. The previous argument controlled only `||w||_2` by a fixed constant and therefore gave no improvement over the generic Schur-orthogonality `r^{-1/2}` scale for the average absolute matrix coefficient. Equation (5.11) is a quantitative L1 statement for the **actual perturbed eigenvector**.

## 6. Matrix-coefficient consequence

The following elementary observation requires only transitivity of the permutation action, not two-transitivity.

### Lemma 6.1

For any function `v` on a transitive `r`-point `Gamma`-set,

\[
\boxed{
\mathbb E_{g\sim U_\Gamma}
|\langle v,\rho(g)v\rangle|
\le \|v\|_{1,\pi}^2.
}
\tag{6.1}
\]

### Proof

By the triangle inequality,

\[
|\langle v,\rho(g)v\rangle|
\le\frac1r\sum_x|v(x)|\,|v(g^{-1}x)|.
\]

For fixed `x`, transitivity makes `g^{-1}x` uniform on the `r` points. Averaging in `g` therefore gives exactly the right-hand side of (6.1). QED.

Applying Lemma 6.1 to the eigenvector in (5.11), for every `eta<eta_*`,

\[
\boxed{
\mathbb E_g|\langle u,\phi_q(g)u\rangle|
=O_\eta(r^{-2\eta}).
}
\tag{6.2}
\]

In particular one may take any exponent below

\[
2\eta_*=0.5184490776\ldots,
\tag{6.3}
\]

which is a strict improvement over the generic `r^{-1/2}` L1 bound available from Schur orthogonality alone.

The earlier exact canonical-vector calculation had the much stronger value `2/r`, but it did not apply to the true slow eigenvector. Equation (6.2) is the first quantitative interpolation between those two facts in the R16 chain.

## 7. Consequence for the genuine slow spectral block in total variation

The preceding R16 spectral audit established that, for this affine family, `mu_q` is the second adjacency eigenvalue and has full-graph multiplicity exactly `r-1`: within `phi_q` the top eigenvalue is simple, and all other nontrivial representation blocks lie below the separated bulk edge.

For rate-one continuous time, put

\[
\delta_q:=1-\frac{\mu_q}{18}.
\]

The slow block in the likelihood ratio started at the identity has the standard Peter--Weyl form

\[
(r-1)e^{-\delta_qt}\langle u,\phi_q(g)u\rangle.
\tag{7.1}
\]

Therefore (6.2) gives the total-variation contribution bound

\[
\boxed{
\operatorname{TV}_{\rm slow}(t)
\le O_\eta\!\left(
 r^{1-2\eta}e^{-\delta_qt}
\right),
\qquad \eta<\eta_*.
}
\tag{7.2}
\]

For completeness, the same block decomposition gives the uniform upper bound

\[
\mu_q\le\mu_+:=\lambda_{\max}
\begin{pmatrix}
16&\sqrt2\\
\sqrt2&2+4\sqrt7
\end{pmatrix}
=16.5093762187\ldots,
\tag{7.3}
\]

so

\[
\delta_q\ge\delta_0:=1-\frac{\mu_+}{18}
=0.0828124323\ldots .
\tag{7.4}
\]

Consequently the slow high-multiplicity block is rigorously TV-negligible by

\[
\boxed{
t\ge
\left(
\frac{1-2\eta_*}{\delta_0}+o(1)
\right)\log r
=
(5.8149593\ldots+o(1))\log r.
}
\tag{7.5}
\]

This is **not** a cutoff theorem. It is a quantitative answer to the predecessor's exact missing question: high multiplicity plus a slow eigenvalue substantially overstates the TV relevance of the actual affine slow block. The proof moves the available coefficient exponent from `1/2` to every value below `0.518449...` without assuming the perturbed eigenvector equals the canonical coset contrast.

For comparison, the separated bulk has normalized relaxation at least

\[
1-\frac{2+4\sqrt7}{18}=0.3009441531\ldots .
\]

Since `|Gamma_q|=q^3(q^2-1)=r^{5/2+o(1)}`, a crude bulk L2-to-TV bound is already negligible by

\[
(4.153595+o(1))\log r.
\]

Thus (7.5), not the bulk, is the remaining limitation of this particular spectral upper-bound route. The source problem is not moved because a matching lower profile and a sharp enough information estimate are still absent.

## 8. Three materially different attacks this run

### A. Two-norm resolvent interpolation for the actual affine outlier — RETAINED

This is Sections 2--7. It resolves part of the exact L1-eigenvector gap left by the 06:57 R16 report and yields the strict coefficient exponent improvement (6.3).

### B. Heat-kernel superlevel thickening by one-step propagation — REJECTED AS A GENERAL CLOSURE ROUTE

If `H_t(x,y)>=theta`, then forcing `k` prescribed additional jumps along a path during an extra interval `s` gives a lower bound of order

\[
e^{-s}\frac{s^k}{k!d^k}\,\theta
\]

at the path endpoint. The tempting plan was to combine this with ordinary vertex expansion to force a high-likelihood set to grow faster than its threshold decays. Optimizing `s` at `s=k` leaves the Stirling-scale factor approximately

\[
(ed)^{-k}
\]

per path layer. Ordinary bounded-degree expansion supplies at most a fixed base strictly below the ambient branching scale needed to compensate this loss. Hence the argument cannot turn spectral expansion alone into Altschuler-style maximal long-range growth. This precisely explains why a naive parabolic thickening of the predecessor's invariant localization relation does not replace LRE.

### C. Rule out the affine stress family from general eigenvalue-multiplicity bounds — REJECTED

Haiman--Schildkraut--Zhang--Zhao themselves construct the present family to show polynomial second-eigenvalue multiplicity, and their paper records the general `O(n/log log n)` upper scale together with constructions essentially saturating the approximate-multiplicity method. Thus a universal multiplicity-only contradiction cannot remove the stress family. The route must use coefficient geometry or entropy, not merely the count of slow modes.

These three attacks are different from the immediately preceding trace/nuclear superlevel method and from the old product, Green, local-Poincare and subcommutation routes.

## 9. Relation to Altschuler's new LRE theorem

The current arXiv record for Dylan J. Altschuler, arXiv:2609.14945, still exposes v1 submitted 14 September 2026; the bounded current check found no v2 or erratum. Its proof uses long-range expansion to obtain maximal-rate growth on the oriented-edge nonbacktracking state space and then near-maximal endpoint Shannon entropy; ordinary spectral expansion enters only in the short entropy-to-TV cleanup. Nothing in the present affine calculation assumes that transitive spectral expansion implies LRE; in fact the earlier R16 report proved this affine family is not a fixed-constant LRE family.

The theorem above is therefore complementary: it studies a source-admissible family specifically on the hard side of Altschuler's hypothesis and quantifies why its large slow eigenspace is less dangerous in TV than in L2.

## 10. Prior-art boundary

Primary baseline: Haiman--Schildkraut--Zhang--Zhao, arXiv:2109.13131 / Bull. LMS 54 (2022), constructs the 18-regular affine Cayley family and proves its large second-eigenvalue multiplicity. Their target is eigenvalue multiplicity, not cutoff or the L1 size of the perturbed slow matrix coefficient.

A bounded 20 September 2026 search for combinations of `Haiman eigenvector L1`, `high multiplicity Cayley matrix coefficient`, and `L1 eigenvector localization Cayley expander` surfaced the Haiman multiplicity paper and generic eigenvector-localization literature, but no exact match to the two-norm estimate (5.11)--(6.2). This is only negative search evidence. Worldwide novelty is **UNVERIFIED**.

## 11. Tests and verification

No finite mixing plot, brute-force graph enumeration, numerical optimization or finite exact checker is used; there is no finite computational core.

Analytic self-checks performed:

- exact point-contrast inner products and the formulas (3.3)--(3.6);
- the `20+o(1)` L1 compression bound (4.1);
- the separated L2 bound `beta=2+4sqrt(7)`;
- the Neumann split at (5.7) and exponent calculation (5.8);
- the transitivity-only matrix-coefficient inequality (6.1);
- the standard Peter--Weyl multiplicity factor in (7.1);
- numerical constants in (5.10), (6.3), (7.3)--(7.5).

These are self-checks, not independent audits. Independent audit count remains `0`.

## 12. Source before/after and exact remaining gap

```yaml
ledger_delta:
  target: "Salez arXiv:2508.21055 Problem 2.3"
  exact_walk: "rate-one continuous-time simple random walk"
  source_status_before: "OPEN / PARTIAL"
  source_status_after: "OPEN / PARTIAL"
  source_metric: "W_exp"
  source_metric_before: "1/2 provisional"
  source_metric_after: "1/2 provisional"
  source_metric_movement: false
  new_graph_class_with_TV_cutoff: false
  mechanism_before:
    - "actual affine slow eigenvector had only a fixed L2 perturbation bound"
    - "canonical coset contrast was L1-rare, but transfer to the true slow vector was missing"
  mechanism_after:
    - "actual affine slow eigenvector has L1(pi)=O(r^{-eta}) for every eta<0.2592245387"
    - "actual slow matrix coefficient has average absolute value O(r^{-2eta}), any exponent below 0.5184490776"
    - "slow high-multiplicity block is TV-negligible by (5.8149593+o(1)) log r"
    - "naive heat-superlevel thickening and multiplicity-only elimination are quantitatively rejected"
  finite_checker: "not applicable"
  independent_audits: 0
  publication_novelty: "UNVERIFIED"
  status_label: "OPEN/PARTIAL"
```

The remaining full-source obligation is not an L2 multiplicity estimate. One needs either:

1. strengthen the affine coefficient control far enough to prove an information/varentropy profile and hence cutoff for this non-LRE stress family; or
2. replace the affine-specific argument by a transitivity mechanism controlling positive-information mass for arbitrary source graphs; or
3. construct an admissible family where that positive-information mass actually persists across a macroscopic fraction of the mixing scale.

This artifact does not claim any of those three tasks completed.