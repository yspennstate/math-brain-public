# QFORM B01 r22 — aggregated rank-two crossbank randomization plus transverse curvature

Status: **ESSENTIAL_STEP_APPLIED / proved supporting theorem / full target OPEN / WITHOUT_VERIFIED_BRAIN**.

Run: `20260922T150052Z-account02-B01-qform-r22`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`.  
Assignment: account02/B01 `Oscillatory replacement` — complementary constructions/source-valid counterexamples.

## 1. Exact target and live corrections

The sole target is the full arbitrary-dimensional conjecture: for independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `Q=X^T A X`, or give a target-valid counterexample. No moments, log-concavity, compact/connected support, sign condition, diagonal-basis hypothesis, or post-rotation independence is assumed.

Fresh controls were read from `yspennstate/math-research-brain` at main `4bcef1d2172af8d37989c2ba3a86c1748a8ec1c1`; immediately before publication the controls and live correction inbox were refreshed at main `b755bab369bf040df572f8ee8b40dea55a5362a7`, with owner revision still `2026-09-22.5` and no later stop for B01. The fresh owner sign-in request `QFORM-SIGNIN-20260922T145401Z` was acknowledged during this same substantive run.

Corrections retained: law-uniform pointwise quadratic-phase decay is false; spectral rotation does not preserve independence; a fixed cross minor/single Schur extraction is not forced by three large eigenvalues; the family `A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)` defeats a uniformly good fixed-size local gate; absolute ambiguity/Hölder aggregation can lose a logarithm. None of those refuted steps is used below.

## 2. Inputs actually consumed

### Own preceding theorem

account02/B01 r21, canonical report

`yspennstate/math-open-problems@949dd0672776cb2f4e100fe917faaee1644b80fc:proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260922T140625Z-account02-B01-qform-r21/REPORT.md`

proved the same mechanism for a single physical `3 x 2` rank-two cross block. Its proof supplies the exact two-dimensional Plancherel identity and the transverse one-dimensional weighted quadratic gate used below.

### Named partner actually applied

account03/B01 r12, canonical report

`yspennstate/math-open-problems@a80bb254a3a1e2883cbfabdf03b53919d6621990:proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/20260922T142626Z-account03-B01-qform-r12/REPORT.md`

proved the sharp dependence-safe square smoothing theorem and, combined with its diffuse rank-two averaged theorem, the bound

`||p_Q||_infinity <= 2 sqrt(pi) 3^(1/4) sqrt(B(S)) |d|^(-1/2)|det Gamma|^(-1/4)`

for a diffuse rank-two frame plus an arbitrarily coupled physical square pivot. I apply this theorem explicitly to the mandatory bank stress family in Section 6; it is not a citation-only mention.

### Sharp linear-image theorem

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Theorem 1.1, states that if the one-dimensional factors of a product probability density are bounded by one, every `k`-dimensional orthogonal marginal density is bounded by `2^(k/2)`. The source-valid transfer already proved in account01/B18,

`yspennstate/math-open-problems@dd421029601cf5663685c49f225af55567332fb6:proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260922T115514Z-qform-B18-a01/REPORT.md`,

is: for every rank-`k` real matrix `T`,

`||p_{T X}||_infinity <= 2^(k/2)/sqrt(det(T T^T))`.

For `k=2` the sharp universal numerator is `2`.

## 3. New theorem — aggregate all columns before paying the rank-two cost

### Theorem `QFORM-RANK2-CROSSBANK-AGGREGATED-v1`

Let `A` be any real symmetric matrix and let the input coordinates be independent with densities bounded by one. Choose disjoint original-coordinate sets `I,K` with `|I|=3` and arbitrary finite `|K|>=2`. Put

`M=A[I,K]`.

Assume `rank M=2`. Let `nu` be the unit vector spanning `ker(M^T)` in `R^I`, and define

`a = nu^T A[I,I] nu`,

`Delta_2 = sqrt(pdet(M M^T))`,

where `pdet` is the product of the two positive eigenvalues, equivalently the product of the two nonzero singular values of `M`. If `a != 0`, then the full quadratic form `Q=X^T A X`, with every outside coupling retained, has a bounded continuous density and

`||p_Q||_infinity`
` <= 1/pi + 4 sqrt(2) pi^(1/3) Delta_2^(-1/2)`
`       * max(3^(1/4), |a|^(-1/4)).`                    (3.1)

No independence after rotating the three `I` coordinates is asserted or used.

The important point is that `Delta_2` aggregates the **entire rank-two cross bank** `A[I,K]`; no individual pair of columns is selected.

## 4. Proof

Choose an orthogonal `3 x 3` matrix `O=[P,nu]`, where the two columns of `P` span `nu^perp`, and write the three physical coordinates in `I` as

`x=P u+nu w`, `u in R^2`, `w in R`.

Since `nu^T M=0`, the whole bank `X_K` couples to `u` but not to `w`. Put

`N=P^T M`,

so `N` is a rank-two `2 x |K|` matrix and `M=P N`. Hence

`det(N N^T)=pdet(M M^T)=Delta_2^2`.                    (4.1)

The rotated density on `(u,w)` is

`G(u,w)=prod_{i in I} f_i((P u+nu w)_i)`.

It obeys `0<=G<=1`, `int G=1`. Let

`m(u)=int G(u,w)dw`.

Some coordinate of the unit vector `nu` has modulus at least `1/sqrt(3)`, so exactly as in r21,

`m(u)<=sqrt(3)`, `int m(u)du=1`.                       (4.2)

Condition on all coordinates outside `I union K`, writing them as `R=r`. The phase involving `(u,w,v)` with `v=X_K` has the form

`u^T H u + 2 c^T u w + a w^2 + 2 u^T N v`
` + affine terms in (u,w) + terms independent of (u,w)`.

For fixed `r,t`, define

`Psi_{r,t}(z)=int exp(i t [u^T H u+2c^Tuw+a w^2+2u^Tz+ell_r(u,w)]) G(u,w)du dw`.

The internal quadratic/linear phase in the `K` variables has modulus one and is discarded only by Cauchy--Schwarz. Thus

`|phi_Q(t)|^2 <= E_r E_v |Psi_{r,t}(N v)|^2`.          (4.3)

By the sharp rank-two linear-image theorem and (4.1), the density of `N X_K` satisfies

`||p_{N X_K}||_infinity <= 2/Delta_2`.                 (4.4)

Therefore

`|phi_Q(t)|^2`
` <= (2/Delta_2) E_r int_{R^2}|Psi_{r,t}(z)|^2 dz`.    (4.5)

For fixed `u,r`, set

`F_{u,r}(t)=int exp(i t[a w^2+b_{u,r}w])G(u,w)dw`.

Two-dimensional Plancherel in `u` gives the exact identity inherited from r21,

`int |Psi_{r,t}(z)|^2 dz`
` = pi^2 |t|^(-2) int |F_{u,r}(t)|^2 du`.              (4.6)

Combining (4.5)-(4.6),

`|phi_Q(t)|`
` <= pi sqrt(2) Delta_2^(-1/2)|t|^(-1) H(t)`,          (4.7)

where

`H(t)=(E_r int |F_{u,r}(t)|^2du)^(1/2)`.

Now use the exact scalar gate from r21. If `0<=h<=1` has mass `m` and

`F(t)=int exp(i t(a w^2+bw))h(w)dw`,

then

`int_R |F(t)|^3dt <= 16 pi m/|a|`.                    (4.8)

Together with `|F(t)|<=m`, for `c0=4 pi^(1/3)` one gets

`int_1^infinity |F(t)|dt/t`
` <= m[c0+log_+(1/(|a|m^2))]`.                         (4.9)

Minkowski in the `L^2(du dP_R)` norm, followed by (4.2), gives

`||m(u)[c0+log_+(1/(|a|m(u)^2))]||_2`
` <= c0 max(3^(1/4),|a|^(-1/4)).`                     (4.10)

Thus from (4.7), on each half-line `|t|>=1`,

`int_1^infinity |phi_Q(t)|dt`
` <= pi sqrt(2) c0 Delta_2^(-1/2)`
`       * max(3^(1/4),|a|^(-1/4)).`                   (4.11)

On `[-1,1]` use `|phi_Q|<=1`. Hence `phi_Q in L^1`, Fourier inversion gives a continuous density vanishing at infinity, and division by `2pi` yields exactly (3.1). QED.

## 5. Exact all-pairs interpretation

Let the columns of `M` be `m_j in R^3`, all lying in `nu^perp`. Cauchy--Binet applied to `N=P^T M` gives

`Delta_2^2 = det(NN^T)`
` = sum_{j<k, j,k in K} det(N_{j,k})^2`
` = sum_{j<k} ||m_j x m_k||_2^2`.                      (5.1)

Thus the theorem pays the reciprocal cost only **after summing the squared areas of every column pair in the physical cross bank**. This is the requested many-column replacement for r21's single `3 x 2` minor.

## 6. Mandatory stress family and direct application of account03/B01

Take

`A_m=[1] direct_sum J_m/m direct_sum (-J_m/m)`, `m>=2`.

Its nonzero spectrum is exactly `{1,1,-1}`. Let `I` contain the singleton coordinate, one coordinate from the positive bank and one from the negative bank, and let `K` contain all remaining bank coordinates. Then `rank A[I,K]=2`, `nu` is the singleton direction, and

`a=1`,

`Delta_2=(m-1)/m^2`.                                    (6.1)

Indeed, the two nonzero rows of the cross bank have disjoint supports and each squared norm `(m-1)/m^2`. Therefore the new theorem gives a cost proportional to

`Delta_2^(-1/2)=m/sqrt(m-1) ~ sqrt(m)`.                 (6.2)

So **even the complete all-column rank-two aggregation around one physical triple is not forced to be uniformly good by the three-large-eigenvalue hypothesis**. This is a genuine source-valid counterexample to that stronger hoped-for structural implication; it is not a counterexample to QFORM.

Now apply the completed named-partner theorem instead of stopping at the obstruction. Write the same form as

`Q=X_0^2 + (U^T X_b)^T diag(1,-1)(U^T X_b)`,

where the two columns of `U` are the normalized constant vectors on the positive and negative banks. Every nonzero row leverage is `1/m<=1/2`, `det Gamma=-1`, and the physical square coefficient is `d=1`. The partner's bound gives

`||p_Q||_infinity`
` <= 2 sqrt(pi) 3^(1/4) sqrt(B(U))`
` <= 2*3^(1/4)*sqrt(pi e)`
` < 7.692,`                                                (6.3)

uniformly in `m`. Thus the stress family simultaneously proves that the new crossbank gate cannot be the entire structural theorem and confirms that the partner diffuse mechanism pays exactly the missing high-cardinality bank structure.

## 7. Conditional end-to-end route and first unpaid universal implication

The Fourier hierarchy is now sharper:

1. a physical triple with rank-three cross bank is controlled by random-slope Plancherel plus a three-dimensional bounded linear-image density (account01/B01 aggregate cross-volume theorem);
2. a physical triple with rank-two cross bank and nonzero transverse curvature is controlled by Theorem 3.1 above, with **all** rank-two bank columns aggregated before reciprocal payment;
3. the canonical family where that aggregate determinant still vanishes asymptotically is controlled by the named partner's diffuse rank-two plus square theorem;
4. the whole-range low-leverage branch is separately covered by the source-pinned regularized-determinant theorem announced in the current controls.

The first unpaid implication is therefore no longer “aggregate a rank-two bank”: that step is paid. It is the **global heavy/diffuse hierarchical dichotomy**: from only “at least three eigenvalues have modulus at least one”, prove that every matrix enters one of the already controlled aggregate-rank3, aggregate-rank2-plus-transverse-curvature, diffuse-square, or whole-range-low-leverage branches with dimension-free quantitative parameters, while retaining arbitrary additional small eigenvalues and all original-coordinate product structure; or construct a target-valid matrix family defeating all of those branches simultaneously.

I have not proved that dichotomy. The full conjecture remains OPEN, and this report is not a full-proof candidate.

## 8. Source/status summary

- New result: `QFORM-RANK2-CROSSBANK-AGGREGATED-v1`, **proved in stated scope**.
- Structural hope “three large eigenvalues force a uniformly good one-triple aggregate rank-two crossbank gate”: **refuted** by `A_m` via (6.1)-(6.2).
- Named partner account03/B01 r12: **applied** to that same family, yielding the uniform bound (6.3).
- Full QFORM theorem: **OPEN**.
- Execution context: `WITHOUT_VERIFIED_BRAIN`; repository retrieval is source transport, not verified native learned-memory ingestion.

No credentials, scheduler identifiers, machine paths, email, Drive, unrelated private data, benchmark material, public release, paid call, remote workflow, permission change, or cross-account authentication is included.