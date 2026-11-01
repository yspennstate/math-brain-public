# QFORM fleet01/B01 — translation-uniform fractional-trace synthesis

Run: `20260922T200435Z-b01-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Control observed before publication: owner revision `2026-09-22.15`; QFORM only.  
Outcome: **ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREMS; FULL TARGET OPEN**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Target and correction discipline

The target remains: for independent real coordinates with densities bounded by one and symmetric `A` with at least three eigenvalues of absolute value at least one, prove a dimension-free bound on the density of `X^T A X`, or give a valid counterexample. No moment, support, log-concavity, diagonal-basis or post-rotation-independence assumption is used below.

The phase-aligned obstruction is preserved. For any fixed frequency `s>0`, choose a finite union of intervals of total length one inside

`{x : dist(s x^2,2 pi Z) <= delta}`

and let its indicator be the density. Then `Re E exp(i s X^2)>=cos(delta)`. Thus no law-uniform pointwise `|s|^{-1/2}` decay is available. The argument below uses a **small-ball/fractional-trace average**, not pointwise quadratic oscillation.

I also use the current correction that a worst scalar conditional density `sup_b ||p_(Q3|Q'=b)||_infinity` is false even for a target-valid product law; see designated partner fleet02/B01 r26. No worst conditional scalar fiber occurs below.

## External input: anisotropic concentration at Hilbert--Schmidt scale

Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492v2, Theorem 1.5 and Remark 1.7, prove the following. If `Y=(Y_j)` has independent coordinates whose densities are bounded by one, `M` is a nonzero real matrix, and

`r(M)=floor(||M||_HS^2/||M||_op^2)>=1`,

then for every `epsilon in (0,1)` there is an absolute `C_epsilon` such that

`sup_z P(||M Y-z||_2 <= t ||M||_HS) <= (C_epsilon t)^((1-epsilon)r(M))`, `t>=0`.

Fix `epsilon=1/4` and abbreviate `C_*:=C_(1/4)`. We only need existence of this universal published constant; no numerical value is asserted.

Their Theorem 1.2 also gives the sharp one-dimensional projection cap: for every coefficient vector `v`, the density of `v^T X` is at most `sqrt(2)/||v||_2` when the independent coordinate densities are at most one.

## Theorem 1 — translation-uniform fractional Hilbert--Schmidt trace

Let `M != 0` and `Y` be as above. Put `S=||M||_HS`, `r=r(M)` and `beta=3r/4`. Then for every `0<alpha<beta`,

`sup_z E ||M Y-z||_2^(-alpha) <= C_*^alpha * beta/(beta-alpha) * S^(-alpha)`.       (1)

In particular,

`sup_z E ||M Y-z||^(-1/2) <= 3 sqrt(C_*) S^(-1/2)`                         (2)

for **every nonzero** `M`, while if `r(M)>=2`,

`sup_z E ||M Y-z||^(-1) <= 3 C_* S^(-1)`.                                  (3)

### Proof

Let `Z=||M Y-z||/S`. The concentration theorem gives

`P(Z<t) <= min(1,(C_* t)^beta)`.

Layer cake gives

`E Z^(-alpha)=alpha int_0^infinity t^(-alpha-1) P(Z<t) dt`.

Split at `t_0=1/C_*`. Direct integration yields

`alpha C_*^beta int_0^(1/C_*) t^(beta-alpha-1)dt + alpha int_(1/C_*)^infinity t^(-alpha-1)dt`
`= C_*^alpha [alpha/(beta-alpha)+1]`
`= C_*^alpha beta/(beta-alpha)`.

For `r>=1`, `beta>=3/4`; taking `alpha=1/2` gives multiplier at most `3`. For `r>=2`, `beta>=3/2`; taking `alpha=1` again gives multiplier at most `3`. This proves (1)--(3). The estimate is translation-uniform and requires neither moments nor centering.

## Theorem 2 — zero-self bilinear block from stable rank two

Let `X` and `Y` be disjoint groups of original independent cap-one coordinates. Condition on any additional original coordinates `W`. Suppose the remaining quadratic expression has **zero `X` self block** and therefore has the form

`R(Y,W) + 2 X^T M Y + b(W)^T X + c(W)^T Y`,                         (4)

where `M` is deterministic and `r(M)>=2`. Then its law has an essentially bounded density satisfying

`||p||_infinity <= (3 C_*/sqrt(2)) ||M||_HS^(-1)`.                    (5)

### Proof

Condition on `(Y,W)`. As a function of `X`, (4) is a linear form with coefficient

`v=2 M Y+b(W)`.

By the sharp one-dimensional projection theorem, its conditional density cap is at most

`sqrt(2)/||v|| = (1/sqrt(2)) ||M Y+b(W)/2||^(-1)`.

Average this conditional density cap and apply (3), uniformly in the translation `b(W)/2`. This proves (5). The exceptional set `v=0` has probability zero whenever `M!=0`, and the finite negative moment already supplies the required integrability.

This proves essential boundedness. Continuity is **not claimed** here.

## Theorem 3 — one physical square lowers the stable-rank threshold to one

Let `X_0` be one original coordinate, independent of disjoint groups `X,Y,W`. Suppose after completing the square **only in this physical coordinate** the form is

`Q = a (X_0 + L(X,Y,W))^2 + R(Y,W) + 2 X^T M Y + b(W)^T X + c(W)^T Y`,       (6)

where `a!=0`, `M!=0`, and the `X` self block in the Schur remainder is zero. Then

`||p_Q||_infinity <= 3 * 2^(5/4) * sqrt(C_*) * |a|^(-1/2) ||M||_HS^(-1/2)`.   (7)

No stable-rank-two condition is needed: **any nonzero `M` suffices**.

### Proof

Conditioning all variables except `X_0`, the shifted-square pushforward gives

`p_Q(t) <= |a|^(-1/2) E |t-R_0|^(-1/2)`,                                  (8)

where `R_0` is the Schur remainder in (6). Indeed a cap-one density pushed through `a(x+h)^2` is bounded by `|a|^(-1/2) u^(-1/2)` on the appropriate half-line.

Next condition on `(Y,W)`. The remaining dependence on `X` is the linear form with coefficient `v=2MY+b(W)`, whose density is at most `K_v=sqrt(2)/||v||`. For any one-dimensional probability density bounded by `K`, the bathtub bound is

`sup_t int |t-z|^(-1/2) p(z) dz <= 2 sqrt(2K)`.                            (9)

Therefore

`sup_t E_X |t-R_0|^(-1/2) <= 2^(7/4) ||2MY+b(W)||^(-1/2)`
`=2^(5/4) ||MY+b(W)/2||^(-1/2)`.

Average over `(Y,W)` and apply (2), uniformly in the translation. Combining with (8) yields (7).

Thus a genuine physical square supplies exactly the extra half-power needed to reduce the linear-image stable-rank requirement from two to one. Again this proves an essentially bounded density; continuity is not claimed.

## Aggregate-before-inversion identity

For arbitrary singular values `s_j(M)`, Cauchy--Binet gives

`E_2(M):=sum_(|I|=|J|=2) det(M[I,J])^2 = sum_(p<q) s_p(M)^2 s_q(M)^2`.

Also

`E_2(M) = 1/2[(sum_p s_p^2)^2-sum_p s_p^4] <= (1/2)||M||_HS^4`.            (10)

Hence

`||M||_HS^(-1/2) <= (2 E_2(M))^(-1/8)`                                    (11)

whenever `E_2(M)>0`. Unlike a largest-minor reduction, (10)--(11) aggregate **all** physical `2x2` minors before reciprocal payment.

Applied to the current fleet03/B08 near-coloop exterior reserve

`E_2(M) >= (4191/281804800) gamma^4`

whenever that reserve enters the already identified **zero-self Schur endpoint**, Theorem 3 yields the dimension-free conditional payment

`||p_Q||_infinity <= 26.256320 sqrt(C_*) / sqrt(|a| gamma)`.                (12)

This is not claimed to close the current arbitrary-self near-coloop endpoint; the zero-self condition is essential and remains exactly stated.

## Designated partner fleet02/B01 applied to an actual inequality

I consumed fleet02/B01 r25, canonical source

`yspennstate/math-open-problems@bf4ba08b75ab774aef671c62ba4898a371059c0d`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T170850Z-fleet02-B01-qform-r25/REPORT.md`.

It proves that any invertible original-coordinate principal triple `T` gives

`||p_Q||_infinity <=216 |det A[T,T]|^(-1/3)`.                              (13)

In the setup of Theorem 3, write the original physical pivot row as `0`, and let `S` be its Schur complement. If `i` lies in the zero-self group (`S_ii=0`) and `j` is on the other side with `m=S_ij=M_ij`, then the exact Schur determinant identity is

`det A[{0,i,j},{0,i,j}] = a det [[0,m],[m,S_jj]] = -a m^2`.                 (14)

Therefore the partner theorem gives the **concentrated-cross** inequality

`||p_Q||_infinity <=216 |a|^(-1/3) |M_ij|^(-2/3)`                          (15)

for every nonzero entry `M_ij`, while the new Theorem 3 gives the complementary **diffuse aggregate** inequality

`||p_Q||_infinity <=3*2^(5/4)sqrt(C_*) |a|^(-1/2)||M||_HS^(-1/2)`.          (16)

Thus in this product-preserving Schur scope one may take the minimum of (15) over entries and (16). Large individual cross entries are paid by the partner's principal-triple theorem; high-cardinality diffuse cross energy is paid without selecting one entry by the fractional Hilbert--Schmidt trace.

I also consumed the newer fleet02/B01 r26 correction: its exact Hadamard-cube example proves the worst conditional scalar-fiber supremum is infinite. Equations (1)--(16) never invoke such a supremum; averaging occurs at the linear-image fractional trace before reciprocal payment.

## What this does and does not close

The new fractional-trace lemma is a source-matching, published-input theorem and gives a useful rigorous replacement for the false pointwise oscillatory bound. It is especially suited to the owner-requested `translation-uniform fractional-trace synthesis` and to grouped-coordinate currencies.

It does **not** solve the unrestricted QFORM conjecture. The remaining first obstruction for this B01 mechanism is the same genuinely hard one highlighted by fleet03/B08 r19: in the surviving near-coloop branch the grouped physical block can have arbitrary self curvature. The zero-self hypothesis in Theorems 2--3 cannot be deleted: already a single self-curved coordinate can create a stationary quadratic point, and the half-Riesz potential of one scalar quadratic at its critical value can diverge logarithmically. A valid next step must splice the aggregate random slope with that self curvature before taking a worst fiber, most likely by a two-currency Fourier/fractional estimate or by extracting a paid physical principal triple.

Full QFORM: **OPEN / not proved / not disproved**.  
Continuity for the full target: **OPEN**.  
Status of this run: **ESSENTIAL_STEP_APPLIED**.

## Sources actually used

- Current control/research/corrections in `yspennstate/math-research-brain`, owner revision 2026-09-22.15.
- Rudelson--Vershynin, arXiv:1402.4492v2, Theorem 1.2, Theorem 1.5, Remark 1.7.
- fleet02/B01 r25: `bf4ba08b75ab774aef671c62ba4898a371059c0d`, report path above.
- fleet02/B01 r26: `bda6ef89066f27778833b0f725b011d4ff64d8c8`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T180441Z-fleet02-B01-qform-r26/REPORT.md`.
- fleet03/B08 r19: `86cbf124545c3457b0037b49151f4f641391fc76`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T194215Z-fleet03-B08-qform-diffuse-r19/REPORT.md`.
- Current correction proof: `yspennstate/math-open-problems@f305dcc8ae0f602f2b21ab32cf4d8ddcdcb56b92`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/CORRECTIONS.md`.

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify (14), the layer-cake multipliers, and the grouped exterior-to-Hilbert--Schmidt arithmetic; the output terminates `STATUS=PASS`. Those finite checks are algebraic regression evidence, not a proof certificate.
