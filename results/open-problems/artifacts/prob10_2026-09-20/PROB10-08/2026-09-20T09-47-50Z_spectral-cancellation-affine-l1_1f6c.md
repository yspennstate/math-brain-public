Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** GPT-6 maximum was requested, but no authenticated runtime telemetry available to this run establishes that model/effort setting.

# PROB10-08 artifact — positivity forces spectral cancellation; sharpened affine slow-mode L1 bound

Status: **PROVED auxiliary mechanism theorems / Salez Problem 2.3 remains OPEN / PARTIAL / no new complete source-level cutoff class certified in this artifact / independent validation pending / worldwide novelty UNVERIFIED**.

Exact source target: Justin Salez, *Modern aspects of Markov chains: entropy, curvature and the cutoff phenomenon*, arXiv:2508.21055v1, Problem 2.3: every bounded-degree vertex-transitive spectral-expander sequence has total-variation cutoff for rate-one continuous-time simple random walk
\[
H_t=e^{t(P-I)}.
\]
This is not the already-posted Abelian Cayley/product-condition problem.

Primary current lead: Dylan J. Altschuler, arXiv:2609.14945v1, submitted 14 September 2026. A fresh bounded check on 20 September 2026 still exposed v1 and no correction/erratum. Its proof uses long-range expansion exactly before the ordinary spectral-gap cleanup: Lemma 3.2 transfers maximal-rate growth to the oriented-edge NBRW state space; Lemma 3.3 turns that growth into endpoint entropy; Proposition 3.1 obtains entropy `log n-O(log log n)`; after that, the ordinary spectral gap performs the short entropy-to-TV cleanup. Long-range expansion is strictly stronger than ordinary spectral expansion and is not inferred here from transitivity.

## 1. Why this run changes method

The prior R16/I0112 chain already exhausted or fenced off product-varentropy, synchronous/tensor constructions, moving-weight/local-Poincare, Hecke/information-curvature, global/time-zero subcommutation, generic Green/L2 mixing, invariant-superlevel trace/nuclear bounds, and finite-block relation propagation. The immediately preceding PROB10-08 report then attacked the Haiman--Schildkraut--Zhang--Zhao affine stress family by a two-norm eigenvector resolvent and proved a first polynomial `L1` rarity exponent for its actual slow eigenvector.

Three consecutive source-metric runs have not improved the already-optimal provisional exponent `W_exp=1/2`, so another renamed sufficient criterion is not useful. This artifact instead asks a different structural question:

> If a high-multiplicity slow spectral block is isolated from the rest of the spectrum, how large can its signed kernel be before positivity of the heat kernel forces cancellation from the faster spectrum?

The answer gives a general obstruction theorem, and then an exact `L1` projection identity substantially sharpens the affine calculation from the preceding run.

## 2. Positivity/cancellation theorem for an isolated slow block

Let `G` be a finite connected regular graph on `n` vertices and let
\[
L=I-P
\]
be the normalized continuous-time generator. Work in the standard counting inner product on `R^V`. Suppose the positive spectrum of `L` has the form
\[
0<\lambda<\lambda+\Delta\le \lambda_j
\]
for all eigenvalues outside the `\lambda`-eigenspace, where `\Delta>0`. Let `\Pi` be the ordinary orthogonal projector onto the `\lambda`-eigenspace. For a start `x`, put
\[
A_x:=\sum_y |\Pi(x,y)|.
\]

### Theorem 2.1 — positivity barrier

For every `x`,
\[
\boxed{
A_x\le 4\,n^{\lambda/[2(\lambda+\Delta)]}.
}
\tag{2.1}
\]
If the graph is vertex-transitive then `A_x` is independent of `x` whenever the automorphism group preserves `P`, as it does for simple random walk.

### Proof

The heat kernel decomposes exactly as
\[
H_t(x,y)=\frac1n+e^{-\lambda t}\Pi(x,y)+R_t(x,y),
\tag{2.2}
\]
where `R_t` is the contribution from rates at least `\lambda+\Delta`.

Because `\Pi` annihilates constants,
\[
\sum_y\Pi(x,y)=0.
\]
Let
\[
S_-:=\{y:\Pi(x,y)<0\}.
\]
Then the total negative mass of the projector row is exactly
\[
-\sum_{y\in S_-}\Pi(x,y)=\frac{A_x}{2}.
\tag{2.3}
\]
Since every heat-kernel entry is nonnegative, summing (2.2) over `S_-` gives
\[
0\le \frac{|S_-|}{n}-e^{-\lambda t}\frac{A_x}{2}
   +\sum_{y\in S_-}R_t(x,y),
\]
so
\[
\sum_{y\in S_-}R_t(x,y)
\ge e^{-\lambda t}\frac{A_x}{2}-1.
\tag{2.4}
\]

On the other hand, if `(\psi_j)` is an orthonormal counting-measure eigenbasis, then
\[
\sum_y R_t(x,y)^2
 =\sum_{j:\lambda_j\ge\lambda+\Delta}
 e^{-2\lambda_jt}\psi_j(x)^2
 \le e^{-2(\lambda+\Delta)t}.
\tag{2.5}
\]
Hence Cauchy--Schwarz yields
\[
\sum_y|R_t(x,y)|\le \sqrt n\,e^{-(\lambda+\Delta)t}.
\tag{2.6}
\]

If `A_x\le4`, (2.1) is immediate. Otherwise choose
\[
t=\lambda^{-1}\log(A_x/4),
\]
so that `e^{-\lambda t}A_x/2=2`. Equations (2.4)--(2.6) imply
\[
1\le \sqrt n\,(A_x/4)^{-(\lambda+\Delta)/\lambda}.
\]
Rearrangement gives exactly (2.1). `QED`

### Interpretation

The theorem is deliberately an obstruction, not a cutoff criterion. A polynomially large row-`L1` slow projector can coexist with a fixed spectral gap only if the faster spectrum cancels its negative entries for a logarithmic time. Therefore spectral separation plus an `L2` estimate cannot in general justify treating the slow block as an independent positive component of total variation. Any successful TV argument for such a graph must control signed cancellation, matrix-coefficient `L1`, Shannon information, or another positivity-sensitive quantity.

A crude transitive multiplicity estimate gives `A_x\le\sqrt m` for a slow eigenspace of multiplicity `m`. Theorem 2.1 can improve that estimate, but it still allows a polynomial amplitude. This is exactly the regime relevant to the affine stress family below.

## 3. Sharpening the affine `L1` interpolation: the compressed operator is an exact `L1` contraction after adjacency scaling

Use the same source-admissible 18-regular affine Cayley family as in the preceding R16 reports,
\[
\Gamma_q=\operatorname{SL}(2,q)\ltimes\mathbb F_q^2,
\qquad r=q^2,
\]
with 16 lifted LPS subgroup generators and two translations. On the mean-zero induced permutation representation `\phi_q` on the `r` affine cosets, write
\[
C=A_0+B,
\]
where `C` is the 18-generator adjacency operator. Let
\[
u_0(0)=\sqrt{r-1},\qquad
u_0(x)=-\frac1{\sqrt{r-1}}\quad(x\ne0),
\]
and
\[
W=\{1,u_0\}^{\perp}.
\]
The preceding artifact established
\[
\|C_W\|_{2\to2}\le\beta:=2+4\sqrt7=12.583005\ldots,
\qquad C_W=P_WCP_W|_W.
\tag{3.1}
\]
It used the crude estimate `||C_W||_{1->1}<=20+o(1)`. The following exact identity removes that loss.

### Lemma 3.1 — exact `L1` contraction of `P_W` on the mean-zero hyperplane

If `g` has mean zero on the `r` cosets, then
\[
\boxed{
\|P_Wg\|_{1,\pi}\le\|g\|_{1,\pi}.
}
\tag{3.2}
\]
Consequently, for every `f\in W`,
\[
\boxed{
\|C_Wf\|_{1,\pi}\le18\|f\|_{1,\pi}.
}
\tag{3.3}
\]

### Proof

For mean-zero `g`, direct substitution gives
\[
\langle u_0,g\rangle_\pi=\frac{g(0)}{\sqrt{r-1}}.
\]
Therefore
\[
(P_Wg)(0)=0,
\qquad
(P_Wg)(x)=g(x)+\frac{g(0)}{r-1}\quad(x\ne0).
\]
Thus
\[
\begin{aligned}
\|P_Wg\|_{1,\pi}
&=\frac1r\sum_{x\ne0}
 \left|g(x)+\frac{g(0)}{r-1}\right|\\
&\le\frac1r\left(\sum_{x\ne0}|g(x)|+|g(0)|\right)
=\|g\|_{1,\pi}.
\end{aligned}
\]
The full adjacency `C` is a sum of 18 permutations, so `||Cf||_1<=18||f||_1`, and it preserves the mean-zero hyperplane. Applying (3.2) to `g=Cf` proves (3.3). `QED`

This exact identity is stronger than the predecessor's `20+o(1)` estimate and uses the special one-point contrast geometry rather than a generic projection bound.

## 4. A better lower bound on the actual slow adjacency eigenvalue

Write
\[
Cu_0=a_ru_0+s,
\qquad
a_r=16-\frac2{r-1},
\qquad s\in W.
\tag{4.1}
\]
The preceding artifact computed
\[
\|s\|_2^2
=2-\frac2{r-1}-\frac4{(r-1)^2}
=2+o(1).
\tag{4.2}
\]
Let `\mu_q` be the top eigenvalue of `C` on `\phi_q`. On the two-dimensional subspace spanned by `u_0` and `e=s/||s||_2`, the Rayleigh matrix is
\[
\begin{pmatrix}
a_r&\|s\|_2\\
\|s\|_2&b_r
\end{pmatrix},
\qquad b_r=\langle e,C_We\rangle\ge-\beta.
\]
The top eigenvalue of this matrix is increasing in `b_r`, hence
\[
\mu_q\ge
\frac{a_r-\beta+\sqrt{(a_r+\beta)^2+4\|s\|_2^2}}2.
\tag{4.3}
\]
Therefore
\[
\boxed{
\mu_q\ge \mu_0-o(1),
\qquad
\mu_0:=
\frac{16-\beta+\sqrt{(16+\beta)^2+8}}2
=16.0698011904\ldots .
}
\tag{4.4}
\]
This is strictly better than the predecessor's `16-o(1)` Rayleigh lower bound.

## 5. `L^p` resolvent interpolation and improved actual-eigenvector rarity

Let `u` be a normalized top eigenvector of `C` on `\phi_q` and write
\[
u=\alpha u_0+w,\qquad w\in W.
\]
As before,
\[
(\mu_qI-C_W)w=\alpha s.
\tag{5.1}
\]
For `1<p<2`, let
\[
\theta=2-\frac2p.
\]
Riesz--Thorin applied to (3.1) and (3.3) gives
\[
\|C_W\|_{p\to p}
\le18^{1-\theta}\beta^\theta.
\tag{5.2}
\]
Interpolation between the predecessor's `||s||_1=O(r^{-1/2})` and `||s||_2=O(1)` gives
\[
\|s\|_{p,\pi}=O\left(r^{1/2-1/p}\right).
\tag{5.3}
\]
Whenever the right side of (5.2) is strictly less than `\mu_q`, the Neumann resolvent in `L^p` is uniformly bounded, so (5.1)--(5.3) imply
\[
\|w\|_{p,\pi}=O\left(r^{1/2-1/p}\right).
\]
Since probability-space norms satisfy `||w||_1<=||w||_p`, and `||u_0||_1=O(r^{-1/2})`, one obtains the following.

### Theorem 5.1 — sharpened affine slow-mode `L1` rarity

For every
\[
\eta<\eta_{\rm aff}:=
\frac{\log(\mu_0/\beta)}{2\log(18/\beta)}
=0.3415891874\ldots,
\]
\[
\boxed{
\|u\|_{1,\pi}=O_\eta(r^{-\eta}).
}
\tag{5.4}
\]

This strictly improves the preceding run's exponent
\[
0.2592245387\ldots
\quad\longrightarrow\quad
0.3415891874\ldots .
\]

## 6. Consequence for the actual slow Peter--Weyl block

For the transitive `r`-point action, averaging over the group gives the elementary bound
\[
\mathbb E_g|\langle u,\phi_q(g)u\rangle|
\le\|u\|_{1,\pi}^2.
\]
Therefore Theorem 5.1 yields, for every `\eta<\eta_aff`,
\[
\boxed{
\mathbb E_g|\langle u,\phi_q(g)u\rangle|
=O_\eta(r^{-2\eta}).
}
\tag{6.1}
\]
Thus every matrix-coefficient exponent below
\[
\boxed{2\eta_{\rm aff}=0.6831783749\ldots}
\tag{6.2}
\]
is certified for the **actual** slow eigenvector.

The earlier spectral decomposition gives a full-graph slow-block multiplicity `r-1` and rate
\[
\delta_q=1-\frac{\mu_q}{18}.
\]
Hence its TV contribution obeys
\[
\operatorname{TV}_{\rm slow}(t)
\le O_\eta\left(r^{1-2\eta}e^{-\delta_qt}\right).
\tag{6.3}
\]
The previous upper bound
\[
\mu_q\le\mu_+=16.5093762187\ldots
\]
gives
\[
\delta_q\ge\delta_0:=1-\mu_+/18
=0.0828124323\ldots .
\]
Letting `\eta\uparrow\eta_aff`, the slow block is therefore negligible by
\[
\boxed{
t\ge(3.825774+o(1))\log r.
}
\tag{6.4}
\]
The predecessor's corresponding constant was `5.814959...`.

The separated bulk edge is still `\beta`, so its crude global `L2` estimate becomes negligible only by
\[
\frac{5}{4(1-\beta/18)}\log r
=(4.153595+o(1))\log r.
\tag{6.5}
\]
Thus, under the present spectral upper-bound method, the high-multiplicity slow outlier is **no longer the bottleneck**; the crude bulk estimate is. This is mechanism movement, not a cutoff theorem: neither (6.4) nor (6.5) is claimed to be the mixing location, and there is no matching TV lower profile.

## 7. Applying the positivity barrier to the affine stress test

For the continuous-time walk on the affine graph, the slow rate is `\lambda=\delta_q`, while the remaining nontrivial block is separated at least to
\[
\Lambda=\gamma_{\rm bulk}:=1-\beta/18
=0.3009441531\ldots .
\]
Theorem 2.1 therefore bounds the row-`L1` norm of the slow spectral projector by
\[
A\le4N^{\delta_q/(2\gamma_{\rm bulk})}.
\tag{7.1}
\]
Using (4.4),
\[
\delta_q\le1-\mu_0/18=0.1072332672\ldots,
\]
so the positivity argument alone still permits
\[
A\le N^{0.17817\ldots}=r^{0.4455\ldots+o(1)},
\]
because `N=|\Gamma_q|=r^{5/2+o(1)}`. This is weaker than the special affine estimate from Section 6, which gives `A=O(r^{0.316822+o(1)})`, but it explains why **spectral separation by itself cannot force the slow projector to have bounded TV mass**. The extra affine geometry genuinely matters.

## 8. Third approach tested: fractional Renyi interpolation cannot repair a polynomial Green excess

A natural response to the earlier failure of `L2`/Green mixing is to replace collision entropy by Renyi order `1+\theta` with `\theta\downarrow0`, hoping to approach Shannon entropy. This does not help without new structure.

Let `p` be a probability law on `n` points, let `u` be uniform, and write the likelihood ratio `L=np`. Put
\[
R:=\mathbb E_u[L^2]=n\sum_i p_i^2.
\]
For `0<\theta\le1`, log-convexity of moments between orders one and two gives
\[
\mathbb E_u[L^{1+\theta}]
\le(\mathbb E_uL)^{1-\theta}(\mathbb E_uL^2)^\theta
=R^\theta.
\]
Hence
\[
\boxed{
D_{1+\theta}(p\|u)\le\log R,
\qquad
D(p\|u)\le D_{1+\theta}(p\|u)\le\log R.
}
\tag{8.1}
\]
There is no vanishing prefactor as `\theta\downarrow0`. The bound is sharp: if `p` is uniform on a subset of size `n/R` (for integral parameters), every Renyi divergence, including Shannon, equals `\log R`.

Therefore the polynomial collision excess already exhibited by the affine stress family cannot be converted into `o(log n)` Shannon deficit by merely changing the Renyi order. A successful replacement for Altschuler's LRE entropy step must exploit additional geometry, signed cancellation, or a direct typical-mass/entropy mechanism.

## 9. Three approaches compared

**A. Positivity/spectral-cancellation route — retained as a general obstruction.**  
Theorem 2.1 is exact and shows why an isolated high-multiplicity slow eigenspace cannot be analyzed as if it were a positive Markov component. It identifies signed cancellation by the faster spectrum as a necessary phenomenon whenever the slow projector has large `L1` rows.

**B. Special affine `L1` interpolation — retained as auxiliary progress.**  
The exact contraction (3.2) plus the two-dimensional Rayleigh improvement sharpen the true slow-eigenvector exponent from `0.2592...` to `0.3415...` and remove the slow block as the bottleneck of the current crude affine spectral upper bound. This still does not prove cutoff for the affine family.

**C. Fractional-Renyi repair of Green/L2 — rejected.**  
Equation (8.1) and the uniform-subset equality case prove that interpolation alone cannot turn polynomial collision excess into near-maximal Shannon entropy. Repeating this route would only rename the existing L2 obstruction.

## 10. Exact source boundary and remaining full-scope gap

**Source before:** Salez Problem 2.3 `OPEN/PARTIAL`; historical R16 metric `W_exp=1/2 provisional`.

**Source after:** unchanged. No new complete source-admissible graph class with a proved TV cutoff is certified in this run, so `W_exp` does not move.

**Mechanism before:** the affine slow block had a first actual-eigenvector `L1` exponent but remained the bottleneck of the available crude spectral TV upper bound; generic spectral separation had no explicit positivity/cancellation theorem in the R16 chain.

**Mechanism after:** Theorem 2.1 gives a general positivity barrier; Theorem 5.1 improves the affine actual-eigenvector exponent to `0.341589...`; the slow block is no longer the bottleneck of that spectral upper route; fractional Renyi interpolation is proved incapable of repairing polynomial Green excess by itself.

The remaining source-level obligation is still the hard one: derive a **Shannon/typical-mass estimate from vertex transitivity plus ordinary spectral expansion alone**, or produce an admissible counterexample sequence. For the affine stress family specifically, the next nonduplicating target is to control the bulk in an `L1`/entropy-sensitive way rather than by global `L2`, and then obtain a matching profile rather than just an upper bound.

## 11. Tests actually run

No finite mixing plots, graph enumeration, Monte Carlo simulation, or asymptotic claim from finite data was used. There is no finite computational core in Theorems 2.1, 3.1, or 5.1.

Calculator-level numerical evaluations were used only to display the constants `\beta`, `\mu_0`, `\eta_aff`, `\delta_0`, and the derived coefficients. The proofs are symbolic and do not depend on floating-point certification. Independent audit count remains `0`.

## 12. Continuity links

Required state and histories consumed before this attack:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- `operations/claims/I0112.md`;
- `artifacts/prob10_2026-09-20/PROB10-08/2026-09-19T23-45-09Z_r16-h0002-handoff.md`;
- `runs/R16/2026-09-16T22-43-00Z_i0112-stuck-recovery-1.md` and its linked product-varentropy / synchronous-tensor / moving-weight-Poincare / Hecke-curvature / tree-subcommutation history;
- immediate predecessor `runs/prob10_2026-09-20/PROB10-08/2026-09-20T08-46-43Z_affine-outlier-l1-interpolation_b72f.md`;
- neighboring P26 report `proofnet24/P26-progress-cutoff-transfer/runs/2026-09-20/2026-09-20_10-10-50__biregular-halved-green-transfer.md`, whose Green-shell/biregular-halving route is not duplicated;
- neighboring NM13 report `proofnet24/NM13-01/progress-cutoff/runs/2026-09-20/2026-09-20T07-22-00Z__reversal-arc-orbit-likelihood.md`, whose arc/Hodge/reversal route is not duplicated.

Preserved R16/H0002 handoff: the actual successor remains Christoph--Morawski--Wigderson Question 5.1 with the all-prefix isotonic/KKT obstruction recorded in the handoff artifact; this refocus does not erase or reassign it.

No scheduler state, cadence, enablement, email, Drive object, public post, permissions, workflow, shared ledger, peer-track file, or force push is changed by this artifact.
