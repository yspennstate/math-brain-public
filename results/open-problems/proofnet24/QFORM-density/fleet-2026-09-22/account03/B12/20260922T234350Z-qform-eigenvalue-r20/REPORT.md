SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-22T23:43:50Z.
attacking: hybrid certificate stability under arbitrary small dense tails and arbitrary large low-footprint added eigenvalues: combine the newest D-prime volume theorem or a physical triple with account04/B12 mixed-norm shear.

# QFORM additional-eigenvalue control: local-footprint hybrid stability

Run: `20260922T234350Z-qform-eigenvalue-r20`  
Status: `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`.

## 1. Target and what is new

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities `f_i<=1`, and let `A` be real symmetric. The full target asks for a universal bound on the density of `X^T A X` whenever `A` has at least three eigenvalues of modulus at least one.

This report does **not** solve that unrestricted extraction problem. It proves a stability theorem that is tailored to the current B12 assignment: once the matrix has either (P) a protected physical three-coordinate core or (V) a protected spread three-volume certificate, one may add a genuinely dense small spectral tail of arbitrary rank and either sign. More generally, one may add eigenvalues of arbitrarily large magnitude provided their footprint on the protected certificate is small. No moment assumption on `X` is used, and no assertion that the quadratic perturbation is pointwise small is made.

The volume branch uses the newest completed D' Brascamp--Lieb theorem and strengthens its arbitrary-weight form. The final outside quadratic remainder is restored by the completed account04/B12 mixed-norm shear theorem, so no independence after rotation or independent convolution is used.

## 2. Source lemmas used

### 2.1 Physical three-coordinate theorem

The current `GEOMETRIC_ROUTE_REPORT.md`, incorporated into the newest synthesis, proves the following original-coordinate statement. If a physical principal `3x3` block `B` satisfies

`min_j |lambda_j(B)| >= gamma > 0`,

then, uniformly in all outside coordinates and in the affine term they induce, the full ambient quadratic form has density cap

`||p_Q||_infinity <= 20/gamma`.

The proof conditions only on the other original coordinates and uses the proved three-dimensional product-law theorem. Thus the outside quadratic block and all cross couplings are unrestricted.

### 2.2 D' volume theorem

For disjoint original-coordinate sets `I,J`, let `M=A[I,J]`. If volume-sampling on its nonzero `3x3` minors has I-side marginals at most `h<3/4`, the newest Fourier report proves

`||p_Q||_infinity <= C_D(h) e_3(M^T M)^(-1/6)`,

where, for `1/2<=h<3/4`,

`C_D(h)=6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1)`.

At `h<=1/2`, the original `q=1` theorem gives the stronger constant `6 sqrt(e)`. Self blocks, outside couplings and affine terms are allowed.

### 2.3 account04/B12 mixed-norm shear compiler

For a joint density `h(u,z)`, define

`M_mix(h)= integral esssup_u h(u,z) dz`.

The completed account04/B12 theorem proves that for every measurable `psi`,

`||p_(U+psi(Z))||_infinity <= M_mix(h)`.

No independence of `U` and `Z` is required. This will be applied below, not merely cited.

## 3. A weighted D' lemma

The first new step is a version of D' that keeps an arbitrary determinant packet instead of forcing the volume-sampling weights of the final matrix.

### Lemma 3.1 (weighted three-volume D')

Let `I,J` be disjoint and `M` an `I x J` real matrix. Let `w=(w_ST)` be any probability distribution supported on pairs of triples

`S subset I`, `T subset J`, `|S|=|T|=3`,

for which `det M_ST != 0`. Put

`alpha_i = P_w(i in S)`, `beta_j=P_w(j in T)`,

and

`Z_w(M) = exp( H(w) + sum_(S,T) w_ST log |det M_ST|^2 )`,

where `H(w)=-sum w_ST log w_ST`. Suppose `max_i alpha_i <= h<3/4`. Then every quadratic form whose `I x J` cross block is `M`, with arbitrary self blocks, arbitrary outside couplings and arbitrary linear terms, has a **continuous** density satisfying

`||p_Q||_infinity <= C(h) Z_w(M)^(-1/6)`,

where

`C(h)=6 sqrt(e)` for `h<=1/2`, and

`C(h)=6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1)` for `1/2<=h<3/4`.

#### Proof

Condition on all original coordinates outside `I union J`; this creates only affine terms on the active variables. The D/D' decoupling gives, for the conditional characteristic function,

`|phi(t)|^2 <= E_W F(W)`,

with

`F(W)=prod_(i in I) |psi_i(2t (MW)_i)| <= 1`,

and `W_j=X_j-X_j'` independent with densities at most one.

Choose `q=1` if `h<=1/2`, and `q=2h` if `1/2<=h<3/4`. Jensen gives

`E F <= (E F^q)^(1/q)`.

Run the geometric Brascamp--Lieb argument with exponents `alpha_i` and `1-beta_j`. The only determinant input needed is the diagonal-plus-PSD expansion

`det(D_J+M^T D_I M)
 >= sum_(S,T) |det M_ST|^2 prod_(i in S)d_i prod_(j notin T)e_j`.

Restrict the sum to the support of `w`. Weighted AM--GM gives

`sum_supp |det M_ST|^2 prod_S d_i prod_(j notin T)e_j
 >= prod_supp ( |det M_ST|^2 prod_S d_i prod_(j notin T)e_j / w_ST )^(w_ST)
 = Z_w(M) prod_i d_i^(alpha_i) prod_j e_j^(1-beta_j)`.

Thus the Gaussian Brascamp--Lieb constant is bounded exactly as in D', with `Z` replaced by `Z_w`. The one-dimensional Fourier estimate used in the source is

`integral |psi_i(u)|^p du <= 4 pi / sqrt(p)`, `p>=2`.

The condition `q/alpha_i>=2` follows from `alpha_i<=h` and the choice of `q`. Therefore

`E F^q <= e^(3/2) (2 pi)^3 q^(-3/2) |t|^(-3) Z_w(M)^(-1/2)`.

Taking the square root after Jensen yields

`|phi(t)| <= min(1, B |t|^(-a))`,

where

`a=3/(2q)>1`,

`B=e^(3/(4q)) (2 pi)^(3/(2q)) q^(-3/(4q)) Z_w(M)^(-1/(4q))`.

Since

`integral_R min(1,B|t|^(-a)) dt = 2 B^(1/a) a/(a-1)`,

Fourier inversion gives

`||p_Q||_infinity <= 2 sqrt(e) q^(-1/2) a/(a-1) Z_w(M)^(-1/6)
 = 6 sqrt(e) q^(-1/2)/(3-2q) Z_w(M)^(-1/6)`.

For `q=1` this is `6 sqrt(e) Z_w^(-1/6)`. For `q=2h` it is the displayed D' constant. The same integrable envelope is uniform in the conditioning variables, so averaging their phases leaves the full characteristic function in `L^1`; hence the resulting density has a continuous representative. QED.

## 4. Main stability theorem

### Theorem 4.1 (`QFORM-LOCAL-FOOTPRINT-HYBRID-STABILITY-v1`)

Write

`A=A0+E`,

where `E` is an arbitrary real symmetric addition. No bound on `||E||op` is assumed unless explicitly stated in a corollary. Each of the following two alternative certificates gives a valid density bound.

#### Branch P: protected physical triple

Suppose there is a physical triple `S` such that

`sigma_min(A0[S,S]) >= kappa > 0`

and define its perturbation footprint

`delta_P = ||E[S,S]||op < kappa`.

Then

`||p_(X^T A X)||_infinity <= 20/(kappa-delta_P)`.

This is an essential-`L^infinity` statement; continuity is not asserted from this branch alone.

#### Branch V: protected spread three-volume packet

Suppose there are disjoint physical coordinate sets `I,J`, a probability distribution `w` on pairs of `3x3` minors `(S,T)`, and `h<3/4` such that

1. `max_i P_w(i in S) <= h`;
2. every supported baseline minor satisfies `sigma_min(A0[S,T]) >= kappa > 0`.

Define the local cross-footprint

`delta_V = max_(w_ST>0) ||E[S,T]||op < kappa`.

Then

`||p_(X^T A X)||_infinity <= C(h)/(kappa-delta_V)`,

with `C(h)` from Lemma 3.1. This branch gives a continuous density.

In particular, at `h=2/3`,

`C(2/3)=9 sqrt(3e)=25.70102107534928...`,

so `delta_V<=kappa/2` implies

`||p_Q||_infinity <= 18 sqrt(3e)/kappa
 = 51.40204215069856.../kappa`.

At `h<=1/2`, `delta_V<=kappa/2` gives

`||p_Q||_infinity <= 12 sqrt(e)/kappa < 19.785/kappa`.

#### Proof of Branch P

By Weyl's singular-value inequality,

`sigma_min(A[S,S]) >= kappa-delta_P =: gamma`.

For a symmetric matrix this means every eigenvalue of the final physical `3x3` block has modulus at least `gamma`. Condition on the outside original coordinates `Z=X_(S^c)`. For fixed `z`, write

`U_z = X_S^T A[S,S] X_S + 2 X_S^T A[S,S^c] z`.

The physical three-coordinate theorem gives

`||p_(U_z)||_infinity <= 20/gamma`

uniformly in `z`, despite the conditioning-generated affine term. Let `h(u,z)=p_Z(z)p_(U_z)(u)` be the joint density of `(U,Z)`. Then

`M_mix(h)=int p_Z(z)||p_(U_z)||_infinity dz <=20/gamma`.

The remaining outside-only term is the measurable function

`psi(z)=z^T A[S^c,S^c]z`.

Now apply the completed account04/B12 mixed-norm shear theorem:

`||p_(U+psi(Z))||_infinity <= M_mix(h) <=20/gamma`.

But `U+psi(Z)=X^T A X`. This explicitly restores the dependent quadratic remainder and does not use convolution. QED.

#### Proof of Branch V

For every supported `(S,T)`, rectangular singular-value stability gives

`sigma_min(A[S,T]) >= sigma_min(A0[S,T])-||E[S,T]||op >= kappa-delta_V =: gamma`.

Therefore

`|det A[S,T]|^2 >= gamma^6`.

Use the **same** weight packet `w`; its marginals are unchanged. Since `H(w)>=0`,

`Z_w(A[I,J])
 = exp(H(w)+E_w log |det A[S,T]|^2)
 >= gamma^6`.

Lemma 3.1 gives, on every fixed outside-coordinate fiber,

`||p_(U_z)||_infinity <= C(h) Z_w^(-1/6) <= C(h)/gamma`,

uniformly over the outside-generated affine terms and all active self blocks. Hence the joint mixed norm of `(U,Z)` is at most `C(h)/gamma`. Applying the account04/B12 shear theorem to the actual outside quadratic term again gives

`||p_(X^T A X)||_infinity <= C(h)/gamma`.

The D' proof supplies an integrable characteristic-function envelope uniform in `z`, so the final characteristic function is in `L^1`; the density is continuous. QED.

## 5. Spectral consequences: small dense tails and arbitrarily large added eigenvalues

### 5.1 Arbitrary-rank small dense tail

If merely

`||E||op <= delta`,

then every principal or rectangular subblock has operator norm at most `delta`. Thus either certificate above survives whenever `delta<kappa`, with `delta_P,delta_V<=delta`. This is a genuine dense-tail statement: `E` may have arbitrary rank, either signs, repeated eigenvalues and arbitrary orientation.

No moment of `X` is used. In particular, the proof does **not** say that `X^T E X` is small when `||E||op` is small; such a claim would be false as a uniform pointwise perturbation statement for unbounded product inputs. Instead, the exact final matrix retains a robust original-coordinate certificate, and the full quadratic form is estimated directly.

### 5.2 Arbitrarily large additions with low certificate footprint

Write the spectral decomposition of the added matrix as

`E=sum_r tau_r v_r v_r^T`.

For Branch P,

`delta_P <= sum_r |tau_r| ||(v_r)_S||_2^2`.

For Branch V, every supported cross minor obeys

`||E[S,T]||op <= sum_r |tau_r| ||(v_r)_S||_2 ||(v_r)_T||_2`,

so

`delta_V <= max_(w_ST>0) sum_r |tau_r| ||(v_r)_S||_2 ||(v_r)_T||_2`.

These formulas are the promised larger-eigenvalue control. The numbers `|tau_r|` may be arbitrarily large. Only their actual physical-coordinate footprint on the protected certificate is charged. A direction supported wholly outside a protected physical triple costs zero in Branch P. A direction missing one side of every supported cross minor costs zero in Branch V. All other entries, self blocks and outside couplings may be arbitrarily large.

## 6. Concrete constants and checks

For `h=2/3`, Lemma 3.1 gives

`C(2/3)=9 sqrt(3e)=25.70102107534928...`.

With a half-gap perturbation, `delta_V<=kappa/2`, this becomes

`18 sqrt(3e)/kappa=51.40204215069856.../kappa`.

The physical-triple half-gap bound is `40/kappa`.

`CHECK.py` is a reproducible sanity check of the Weyl gap and constants. Its recorded execution used seed `20260922`, 5000 random signed physical cores and symmetric perturbations of operator norm `0.4`, found zero numerical Weyl violations, and minimum numerical slack `2.3946222603765666e-4`. This is only a numerical sanity check; the proof above is analytic.

## 7. Why this is not the full conjecture

The bare hypothesis `s_3(A)>=1` does not yet imply either certificate above with universal `kappa`. In particular, the already-recorded family

`[1] direct_sum J_m/m direct_sum (-J_m/m)`

has nonzero spectrum `{1,1,-1}` but defeats universal selection of a single well-conditioned physical triple and has cross rank at most two for coordinate cuts. Therefore this theorem is a **stability/reduction theorem**, not an extraction theorem.

The remaining B12 obligation is now sharper: in the no-local-certificate regime, obtain a grouped two-bank / three-volume packet whose inverse curvature is paid only after product aggregation, or splice the no-pivot/hub mechanisms into such a packet. The newest D' theorem shows that a packet with row marginals below `3/4` is already sufficient and, by the theorem here, is robust to arbitrary-rank dense tails of operator norm smaller than its minor singular gap.

## 8. Regularity

- Branch P: essentially bounded density is proved; continuity is **not** claimed from this argument alone.
- Branch V: a continuous density is proved because the characteristic-function estimate is uniformly integrable before the outside average.
- Full QFORM: OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity: OPEN.

## 9. Provenance

Current owner target and corrections were read from fresh `yspennstate/math-research-brain` main. The programme remains `QFORM-DENSITY-3EIG-20260922`, programme revision `2026-09-22.5`, OWNER CONTROL revision `2026-09-22.15`, with no account03/B12 pause or stop at prepublication refresh.

Newest mathematical source applied: `yspennstate/math-open-problems`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md` and `GEOMETRIC_ROUTE_REPORT.md`; the owner continuation identifies initial Claude-attributed commit `e5f71d79eff325201dd0274053d20268ce65b837`, and later master content was read before this report.

Assigned partner actually applied: `account04/B12`, `QFORM mixed-norm shear compiler`, canonical report `yspennstate/math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e:proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260922T192552Z-account04-B12-mixed-shear-r1/REPORT.md`.

Corrections respected include: no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea bound, no dimension-free normalized worst conditional fiber, no universally good single physical minor/cross-rank-three cut, and no claim that a small matrix norm makes its quadratic value uniformly small on arbitrary unbounded product inputs.

Repository transport is not native learned-memory ingestion. Status remains `WITHOUT_VERIFIED_BRAIN`.
