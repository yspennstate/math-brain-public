Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 — mean-ball covariance transport compiler for the Díaz outer variational problem

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Status: **OPEN / PARTIAL**  
Owner route: **cluster-aware weighted counting / overlap-variational certification**, complementary to the constructive and interpolation workers.  
Source-model metric: **unchanged**.

## 0. Source metric before / after

The owner-frozen model is the classical iid proper random 3-SAT model: `n` Boolean variables and `m=floor(alpha n)` independent clauses; each clause chooses three distinct variables uniformly and independent fair signs.

A bounded fresh source check in this run reconfirmed the directly auditable explicit-decimal baseline:

\[
\boxed{3.52\le \liminf \alpha_n^*\le\limsup \alpha_n^*\le4.4898},
\]

so the tracked explicit width is

\[
\boxed{W_{\rm source}:0.9698\longrightarrow0.9698.}
\]

The lower endpoint `3.52` is Hajiaghayi--Sorkin, *The Satisfiability Threshold of Random 3-SAT Is at Least 3.52* (2003), and the upper endpoint `4.4898` is Díaz--Kirousis--Mitsche--Pérez-Giménez, *A new upper bound for 3-SAT* (2008).

The distinction between a sharp transition window and convergence to one exact limiting density remains essential. Gaia Carenini's ECCC TR26-145, published 16 August 2026, proves an `O(n/log n)` scaling window in clause count for every fixed `k>=3`; this gives a much sharper finite-`n` transition but does not by itself prove that the sequence of window centers for `k=3` converges to one constant. Ding--Sly--Sun (`arXiv:1411.0650`) prove threshold existence/identification only for all sufficiently large `k`, not automatically for `k=3`.

The ESA 2025 paper named in the owner prompt explicitly changes the classical independent-clause assumption to `k`-wise independent clause distributions; its results are therefore not imported into the iid source metric.

Fresh URLs consumed:

- https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103
- https://arxiv.org/abs/math/0310193
- https://arxiv.org/abs/0807.3600
- https://eccc.weizmann.ac.il/report/2026/145/
- https://arxiv.org/abs/1411.0650

Companion NM13-13 now has a **project CANDIDATE_FULL pending later independent review** at `alpha=4.388865`, with an interval-certified direct product-law Gaussian-quadrature calculation. I keep that separate from the external source metric until the repository's independent-validation standard is met. If eventually validated as a project theorem, it would give an internal candidate width `0.868865`, but this run does not adopt or duplicate that claim.

## 1. Consumed repository evidence and ownership check

I read before developing the new route:

1. `operations/PROB10_2026-09-20.md` — the run contract and source/model distinctions.
2. current `POSTED.md` — no collision that makes this scoped random-3-SAT route a posted exclusion.
3. `operations/claims/PROB10-04.md` — PROB10-04 owns the complementary cluster-aware weighted-counting / overlap-variational route. It does **not** override F0097/R03, NM13-06's constructive route, or NM13-13's interpolation route.
4. newest own report before this run: `runs/prob10_2026-09-20/PROB10-04/2026-09-20T11-10-00Z__parallel_sum_inverse_free_outer_certificate.md`.
5. newest interpolation neighbor read: `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T11-12-00Z__t04_direct_product_gauss9_4388865_upper.md`.
6. newest constructive neighbor read at run time: `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T14-22-17__t04_dual_horn_closure_make_break.md`.
7. the immutable pre-refocus HARD7-06 handoff: `runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`.

The HARD7-06 handoff remains exactly what it was: F0095 random-graph 3-colourability, with the binary-cascade identity `Y_out=Y_1Y_2`, `0.9319<q<0.9320`, `5.03<beta_bin<5.04`, and divergence of positive-branch negative moments above `beta_bin`. I do not relabel any of that as 3-SAT progress.

## 2. Why this run changes method

The source endpoint has now been unchanged for many PROB10-04 runs. The preceding run did, however, remove a concrete analytic obstruction: at each outer mean `y=(u,v,w)` the Díaz outer Hessian obeys

\[
\nabla^2\Phi(y)=D(y)^{-1}-\Sigma_V(y)^{-1}-\Sigma_C(y)^{-1},
\tag{2.1}
\]

and a fixed split matrix `T` certifies strict concavity whenever

\[
D(y)-T^T\Sigma_V(y)T-(I-T)^T\Sigma_C(y)(I-T)\succ0.
\tag{2.2}
\]

At the inherited finite-decimal saddle surrogate, the archived rational split has a pointwise minimum LMI eigenvalue about `0.0720353`. The exact obstruction was therefore no longer finding one good point: it was **transporting that point certificate to a whole outer neighborhood without re-solving six Gibbs multipliers on every grid cell**.

This run changes from rescue-motif tuning / pointwise curvature to finite-support exponential-family geometry. The new mathematical object is a covariance transport inequality in mean space.

## 3. Idea was frozen before code

Before any repository checker was written, I committed

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T11-44-12Z__mean_ball_covariance_transport_idea_before_code.md`

at commit

`850428f2f2a8da2f3a5cb78d80ddf4e1089aebee`.

Its exact missing lemma was: for a finite block exponential family with covariance `Sigma(theta)` and within-block directional range

\[
R(\delta)=\max_{b,s,t}|\delta\cdot(s-t)|,
\]

prove

\[
e^{-R(\delta)}\Sigma(\theta_0)\preceq
\Sigma(\theta_0+\delta)\preceq
 e^{R(\delta)}\Sigma(\theta_0),
\tag{3.1}
\]

then invert the mean map quantitatively to express the factor solely in terms of `||y-y_0||`.

That lemma is now proved.

## 4. New theorem 1: exact multiplicative covariance transport

Consider

\[
A(\theta)=\sum_bm_b\log\sum_{s\in S_b}g_{b,s}e^{\theta\cdot s},
\qquad
\Sigma(\theta)=\nabla^2A(\theta).
\tag{4.1}
\]

For a fixed test vector `x`, along `theta_t=theta_0+t delta` put `X_b=x·S_b` and `Y_b=delta·S_b`. Differentiating the block variance gives the exact identity

\[
{d\over dt}\operatorname{Var}_t(X_b)
=\mathbb E_t[(X_b-\mathbb EX_b)^2(Y_b-\mathbb EY_b)].
\tag{4.2}
\]

Because the support of `Y_b` has interval length at most `R(delta)`,

\[
|Y_b-\mathbb E Y_b|\le R(\delta).
\]

Hence, after summing blocks,

\[
\left|{d\over dt}x^T\Sigma(\theta_t)x\right|
\le R(\delta)x^T\Sigma(\theta_t)x.
\tag{4.3}
\]

Grönwall now yields, simultaneously for every `x`,

\[
\boxed{
e^{-tR(\delta)}\Sigma(\theta_0)
\preceq\Sigma(\theta_t)
\preceq e^{tR(\delta)}\Sigma(\theta_0).
}
\tag{4.4}
\]

This is exact; no Taylor truncation, simulation, or random-input heuristic appears.

## 5. New theorem 2: invert the mean map in a ball

Let `y(theta)=nabla A(theta)`, `Sigma_0=Sigma(theta_0)`, and `lambda_0=lambda_min(Sigma_0)`.

### 5.1 Euclidean version

If every within-block support diameter is at most `L`, then for `rho=||y-y_0||_2<lambda_0/L`,

\[
\boxed{
(1-s)\Sigma_0\preceq\Sigma(y)\preceq(1-s)^{-1}\Sigma_0,
\qquad s={L\rho\over\lambda_0}.
}
\tag{5.1}
\]

Proof: writing `delta=theta-theta_0` and `q=||delta||`, (4.4) gives

\[
\begin{aligned}
\delta\cdot(y-y_0)
&=\int_0^1\delta^T\Sigma(\theta_0+t\delta)\delta\,dt\\
&\ge {\lambda_0q\over L}(1-e^{-Lq}).
\end{aligned}
\]

while Cauchy gives the upper bound `q rho`. Therefore

\[
e^{-Lq}\ge1-L\rho/\lambda_0,
\]

and substitution in (4.4) gives (5.1).

### 5.2 Mahalanobis version

Define the finite support constant

\[
L_*^2=\max_{b,s,t}(s-t)^T\Sigma_0^{-1}(s-t).
\tag{5.2}
\]

Then if

\[
r_*=\|y-y_0\|_{\Sigma_0^{-1}}<1/L_*,
\]

one has

\[
\boxed{
(1-L_*r_*)\Sigma_0\preceq\Sigma(y)
\preceq(1-L_*r_*)^{-1}\Sigma_0.
}
\tag{5.3}
\]

The proof uses the same transport theorem, but with

\[
R(\delta)\le L_*\sqrt{\delta^T\Sigma_0\delta}
\]

and dual Cauchy--Schwarz. For a Euclidean mean ball it is enough to take

\[
s_*\le a_*\rho,
\qquad
a_*=L_*\sqrt{\|\Sigma_0^{-1}\|_{op}}.
\tag{5.4}
\]

This covariance-adapted version is the useful one for the very anisotropic variable support.

The full proof is archived in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T11-44-12Z__mean_ball_covariance_transport_theorem.md`

created at commit

`f5b59324e398e01192872fd7faaae1686abc3562`.

(Notation correction for reading equation (6.1) in that artifact: its positive copy entry is `u(lambda_p-u)/lambda_p`; the rendered `nu` there is only a one-character LaTeX typo and is not used by the checker or proofs.)

## 6. New theorem 3: robust outer-ball LMI

Let

\[
M_0=D(y_0)-T^T\Sigma_{V,0}T-(I-T)^T\Sigma_{C,0}(I-T)\succeq\eta_0I.
\]

Set

\[
R_{V,0}=T^T\Sigma_{V,0}T,
\qquad R_{C,0}=(I-T)^T\Sigma_{C,0}(I-T).
\]

If the two covariance transports on `||y-y_0||<=rho` have factors `s_V,s_C<1`, and

\[
\|D(y)-D(y_0)\|_{op}\le L_D\rho,
\]

then the whole ball is certified whenever

\[
\boxed{
L_D\rho+
{s_V\over1-s_V}\|R_{V,0}\|_{op}
+{s_C\over1-s_C}\|R_{C,0}\|_{op}<\eta_0.
}
\tag{6.1}
\]

Indeed the transported covariances satisfy

\[
T^T\Sigma_V(y)T\preceq(1-s_V)^{-1}R_{V,0}
\]

and similarly on the clause side, while `D(y)` loses at most `L_D rho I`.

For the Díaz copy covariance itself, direct differentiation gives the exact global bound on the copy simplex

\[
\boxed{\|D(y)-D(y')\|_{op}\le\sqrt6\,\|y-y'\|_2.}
\tag{6.2}
\]

The negative `2 x 2` block has each coordinate derivative of Frobenius norm at most `sqrt3`; Cauchy in `(dv,dw)` gives `sqrt6`.

## 7. Three nonexhausted approaches tried

### Approach A — isotropic mean-ball transport: success

For `M=23`, exact within-block support enumeration gives

\[
L_V^2=1058=(23\sqrt2)^2,
\qquad L_C^2=10.
\]

This already supplies a complete analytic local compiler. It is conservative because it pays the worst Euclidean support diameter against the smallest covariance eigenvalue.

### Approach B — Mahalanobis transport: success and materially stronger

The exact finite support maximization on the inherited rationalized saddle surrogate gives

\[
L_{*,V}^2\approx2067.163678319927,
\qquad
L_{*,C}^2\approx9.306650107739737.
\]

Combined with exact rational spectral envelopes

\[
\|\Sigma_{V,0}^{-1}\|_{op}\le6.19,
\qquad
\|\Sigma_{C,0}^{-1}\|_{op}\le5.15,
\]

this allows the simple certified Euclidean transport coefficients

\[
\boxed{a_V\le114,\qquad a_C\le7.}
\]

This is much smaller than the conservative isotropic coefficients used in the same exact checker (`202` and `16.4`).

### Approach C — one-center globalization: precise obstruction / failure

The mean-transport theorem necessarily needs `s<1`. Even before paying the robust LMI, the variable-side anisotropic surrogate bound becomes vacuous once `rho` approaches `1/114≈0.00877`; the actual robust fixed-`T` LMI is exhausted much earlier, around `1.6e-3` in the diagnostic calculation. Thus a single saddle center cannot plausibly replace the whole global outer search.

This is the precise obstruction required after repeated unchanged endpoint runs: **the pointwise curvature problem is now local and solved in a neighborhood, but one center has a finite transport radius forced by the weak covariance direction.** The next method change within 3-SAT must be global: recenter several certified balls and prune them with the already-proved support oracles, or prove a direct exponent value gap away from the saddle. Continuing to invent local rescue motifs would not pay the actual remaining gap.

## 8. Executed exact finite core

Only after the idea and exact lemmas were written did I create and run

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T11-44-12Z__mean_ball_transport_exact.py`

creation commit

`817d8c0638afcf6e8b7dbdfda7c2b3cae5056bc9`.

Actual stdout is archived at

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T11-44-12Z__mean_ball_transport_exact.out`

creation commit

`0ce8402d87f68d6128ca9ea522958ee2d3ae338c`.

The checker uses exact Python `Fraction` arithmetic on the inherited finite-decimal center data, treating every decimal as an exact rational. It performs:

- `14,951` exact within-variable-block support-pair comparisons;
- `26` exact within-clause-block support-pair comparisons;
- exact inversion of the rational `3 x 3` center covariance matrices;
- exact Sylvester tests for every spectral envelope;
- the final robust-ball inequality as one exact rational comparison.

It certifies

\[
M_0\succeq0.07I,
\quad R_{V,0}\preceq0.256I,
\quad R_{C,0}\preceq1.057I,
\]

and the inverse-covariance upper envelopes quoted above.

For the covariance-adapted transport, choose

\[
\rho={3\over2000}=0.0015,
\qquad s_V\le0.171,
\qquad s_C\le0.0105.
\]

Using `sqrt6<49/20`, the exact degradation bound is

\[
\Delta(\rho)
\le {4442527557\over65623640000}
\approx0.06769706095242507<0.07.
\]

Thus the inherited rationalized surrogate has the **exact fixed-`T` neighborhood certificate**

\[
\boxed{\|y-y_0\|_2\le0.0015\implies M_T(y)\succ0,}
\tag{8.1}
\]

with remaining rational slack

\[
\boxed{{151127243\over65623640000}
\approx0.002302939047574929.}
\]

For comparison, the same checker certifies the conservative isotropic compiler only out to

\[
\rho_{iso}=0.00084,
\]

so covariance adaptation expands this fully exact **surrogate** radius by

\[
{0.0015\over0.00084}={25\over14}\approx1.785714.
\]

The output ends

`EXACT_SUPPORT_ENUMERATION_PASS = True`  
`EXACT_CENTER_SPECTRAL_ENVELOPES_PASS = True`  
`EXACT_SURROGATE_MEAN_BALL_LMI_PASS = True`.

A Python startup hook emitted an unrelated spreadsheet/artifact-tool warmup timeout to stderr; the checker itself then ran to completion and every asserted exact test passed. No output number here comes from SAT simulation.

## 9. What is theorem progress versus auxiliary progress

### New theorem progress

The genuinely new proved statements in this run are:

1. finite-support multiplicative covariance transport (4.4);
2. its Euclidean mean-ball inversion (5.1);
3. its covariance-adapted Mahalanobis mean-ball inversion (5.3);
4. the robust inverse-free outer-ball compiler (6.1);
5. the explicit `sqrt6` Lipschitz bound for the Díaz copy covariance.

Together these replace “solve six stationarity equations at every local outer point” by a center certificate plus finite support constants.

### Auxiliary / diagnostic progress only

The `rho=0.0015` neighborhood is exact **for the inherited finite-decimal saddle surrogate**, not yet for an outward interval enclosure of the true Díaz saddle. It therefore does not move the random-3-SAT source endpoint. Likewise the comparison to `rho_iso=0.00084` measures certification efficiency, not threshold width.

## 10. Full-scope unresolved gap

The parent random-3-SAT threshold problem remains open. Even inside the Díaz/rescue subprogram, a new endpoint below `4.4898` still requires all of the following simultaneously:

1. choose a target `alpha<4.4898` and outward-certify the pure-literal/truncation parameters and the relevant center(s), not rounded decimal surrogates;
2. evaluate the rescue-aware exponent with the inner entropy penalties already developed in preceding PROB10-04 runs;
3. use the present mean-ball compiler to certify neighborhoods of the candidate maximizer(s);
4. cover or exclude **every** remaining feasible outer mean outside those neighborhoods, using recentered balls plus the exact variable/clause support oracles or a separate global exponent-gap theorem;
5. pay truncation/heavy-tail errors and the source configuration-model transfer at the selected lower density;
6. receive independent validation before changing canonical status.

No finite SAT/UNSAT instance, annealed heuristic, or finite simulation is counted toward that gap.

## 11. Next exact target

The most concrete continuation is now a **recentered support-oracle cover**, not another local weighting tweak. The exact lemma to target next is:

> For a compact feasible outer polytope `P=P_V cap P_C`, construct finitely many certified centers `y_j` and radii `rho_j` using the present transport compiler such that every point in the high-value region lies in one certified ball, while the complement has a directly certified exponent gap below the rescue-adjusted saddle value.

The already-proved exact support functions `h_V` and `h_C` make separation of candidate boxes cheap. If this cannot be closed with a modest number of centers, the obstruction should be stated as a quantified uncovered high-value set and the method should switch to a global dual/value-gap certificate.

## 12. Status

**PROB10-04 remains PARTIAL / parent source OPEN.**  
External explicit-decimal source width: **`0.9698 -> 0.9698`**.  
New auxiliary certification radius at the inherited rationalized saddle: **`0 -> 0.0015`** for a fixed-`T` strict-concavity neighborhood, with exact rational finite-core verification.  
No scheduler, email, Drive, public-posting, permission, or workflow action was taken.