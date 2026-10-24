SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T05:58:38Z.
attacking: the newest account03/B20 r48 strong-edge punctured-rank-two survivor by applying the exact arbitrary-rank physical-pair theorem and Schur rank-two completion before any post-puncture minor extraction.

# account02/B20 r47 — the r48 strong-edge leaf is fully paid by the arbitrary-rank physical-pair theorem

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL STEP APPLIED / STRONG-EDGE LEAF FULLY PAID / STALE SCHUR-R1 DEBT REMOVED / FULL QFORM OPEN**.

Execution context: **WITHOUT_VERIFIED_BRAIN**. Repository transport was authenticated, but no native learned-memory receiver ingestion was exposed.

Continuity: the new paid branch gives absolute continuity and an essentially bounded density; no claim of a universal continuous representative is made. Full-target continuity remains separate and open.

All coordinates below are literal ORIGINAL coordinates. No spectral rotation is applied to the random vector. No Gaussian, log-concave, moment, iid, compact-support or connected-support assumption is introduced. Arbitrary same-bank curvature, affine terms, outside couplings, extra spectrum and every nonzero coefficient tail are retained.

## 1. Fresh source-pinned inputs

The newest compatible designated partner actually consumed is account03/B20 r48:

`yspennstate/math-open-problems@67a9144806e9371e3ecb9b93d29e9aff915cb9f3`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T054542Z-account03-B20-QFORM-auto11-r48/REPORT.md`.

On account04/B20 r13's strong-anchor-edge leaf, in the still-unpaid all-small-diagonal chamber and after the child scalar-pivot exit has failed, r48 gives an ACTUAL original-coordinate principal pair

`B=[[a,d],[d,c]]`

with

`|a|<=1/64`,
`|c|<a0`,
`|d|>=1/1024`,
`a0=4.2146684313588616e-8`,

and proves that B is invertible indefinite with

`D:=|det B|>=D0=9.530157744638501e-7`,
`kappa:=s_min(B)>=kappa0=6.075614261408114e-5`.                 (1.1)

Its previous endpoint only paid this leaf when a disjoint post-puncture physical cross block had `s3>=2^-16`, leaving a punctured-rank-two survivor.

The required pinned Claude package is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its `RESULTS.md` explicitly records the full-matrix physical-pair closure: any invertible indefinite original-coordinate 2x2 principal block with quantitative determinant and smallest singular value is enough, under `s3(A)>=1`, whatever the rest of A. The complete proof is source-pinned at

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`,

theorem `QFORM-FULL-MATRIX-INDEFINITE-PAIR-LOG-v1`. The current continuation audit states that the earlier results labelled proved were re-derived and no such result was found false.

The same pinned `FOURIER_ROUTE_REPORT.md` proves unrestricted D5:

`||p_Q||_infinity <= 5 sqrt(2e) e5(A[I,J]^T A[I,J])^(-1/10)`     (1.2)

for every literal original-coordinate cut and with no volume-marginal gate.

## 2. Exact rank-two completion: the third target scale is already in the Schur remainder

Normalize the exact target to

`s3(A)>=1`,                                                     (2.1)

where singular values of a symmetric matrix are absolute eigenvalues in decreasing order. Reorder the physical pair first and write

`A=[[B,E],[E^T,C]]`,
`S=C-E^T B^(-1) E`.                                             (2.2)

Define

`A0=[[B,E],[E^T,E^T B^(-1)E]]`
`  =[I;E^T B^(-1)] B [I,B^(-1)E]`.                             (2.3)

Thus

`rank(A0)=2`,
`A-A0=diag(0,S)`.                                               (2.4)

By the singular-value min-max principle, or equivalently the best-rank-two approximation inequality,

`s3(A) <= ||A-A0||op = ||S||op`.                               (2.5)

Hence the target itself forces

`boxed: ||S||op>=1`.                                             (2.6)

This is the key point missed by the punctured-cross formulation: the mandatory third scale need not be a third physical crossing direction. It may sit entirely in same-side, diagonal or diffuse Schur curvature. The exact Schur remainder retains that scale with no loss and without rotating the product law.

Completing the original physical pair in the full affine polynomial leaves the other ORIGINAL coordinates independent and gives

`Q=(X_pair+m(Z))^T B (X_pair+m(Z))+R(Z)`,                       (2.7)

where the quadratic coefficient of `R` is exactly `S` and all induced affine terms are retained.

## 3. Arbitrary-rank quarter small ball plus the logarithmic pair envelope

The completed arbitrary-rank one-eigenvalue small-ball theorem gives, for every centre w and rho>0,

`P(|R-w|<rho) <= min(1,5 (rho/||S||op)^(1/4))`
`             <= min(1,5 rho^(1/4))`.                           (3.1)

The proof is product-safe: if a diagonal coefficient carries at least half of `||S||`, condition the other original coordinates and use the univariate quadratic sublevel bound; otherwise a random sign cut of the zero-diagonal part produces an ORIGINAL-coordinate cross block of norm at least `||S||/4`, and the regularized-determinant decoupling estimate gives the quarter-power small ball. No conditional projection-density supremum or post-rotation independence is used.

For the invertible indefinite pair, the completed logarithmic pair-density envelope says for every r>0,

`p_Q(t) <= 2 sqrt(2)/r`
`       + D^(-1/2) E log_+(2r^2/(kappa |t-R|))`.                (3.2)

Layer cake and (3.1) give

`E log_+(a/|t-R|) <= 20 a^(1/4)`.                               (3.3)

Therefore

`p_Q(t) <= A1/r + B1 sqrt(r)`,                                  (3.4)

where

`A1=2 sqrt(2)`,
`B1=20 2^(1/4) D^(-1/2) kappa^(-1/4)`.                          (3.5)

The exact minimizer is `r=(2A1/B1)^(2/3)`, and

`boxed:
||p_Q||_infinity
 <=3*400^(1/3) D^(-1/3) kappa^(-1/6).`                          (3.6)

This is the full-matrix pair theorem at target scale one.

## 4. New closure of the newest partner leaf

Insert the exact r48 pair constants (1.1) into (3.6):

`||p_Q||_infinity
 <=3*400^(1/3) D0^(-1/3) kappa0^(-1/6)`
` =11328.598626026012...`
` <11329`.                                                       (4.1)

### Theorem — `QFORM-R48-STRONGEDGE-FULLPAIR-CLOSURE-v1`

Under the full target hypotheses and the exact localized r13/r48 strong-anchor-edge leaf, including the all-small-diagonal gate and failure of the child scalar-pivot exit, the FULL ambient law of `X^TAX` has an essentially bounded density satisfying

`boxed: ||p_Q||_infinity<11329.`                                 (4.2)

No post-puncture third-cross condition is needed.

Consequently the r48 alternative

`for every disjoint L,M outside {i,j}, s3(A[L,M])<2^-16`

is **not an unpaid survivor at all** on the strong-edge leaf. It was only a survivor of the weaker pair+third-cross receiver. The rank-two completion (2.3)-(2.6) routes the third target resource through the entire exact Schur remainder instead.

This also retires this slot's preceding `QFORM-R50-PAIR-SCHUR-R1-COLLAPSE-WITH-INTERNAL-CURVATURE-PAYMENT-v1` debt whenever its quantitative indefinite physical pair is present. In that earlier heavier-pair collar,

`D>=3/4096`, `kappa>=1/64`,

so the same theorem gives directly

`||p_Q||_infinity
 <=3*400^(1/3)(3/4096)^(-1/3)(1/64)^(-1/6)`
` =490.4380367318739... <491`.                                  (4.3)

Thus no post-Schur rank-two lower bound, no near-rank-one cancellation analysis and no deletion of internal curvature are needed in that physical-pair subbranch.

## 5. Required pinned D5 application to a live physical cut

The fresh global r50 compiler retains the literal original-coordinate light-light block `M` with

`sigma2(M)>255/65536`

in its robust branch. Apply the pinned unrestricted D5 theorem (1.2) to this same ACTUAL cut. If

`e5(M^T M)>=1/1024`,                                             (5.1)

then

`||p_Q||_infinity
 <=5 sqrt(2e) (1/1024)^(-1/10)`
` =10 sqrt(2e)`
` =23.316439815971243...<23.317`.                               (5.2)

Therefore every still-unpaid r50 robust-light state may simultaneously assume

`e5(M^T M)<1/1024`.                                              (5.3)

This is an equation-level use of the required pinned `e5f71d79...` package. On the localized r13 transverse double-anchor block there are only two hub columns, so its fifth compound is identically zero; D5 cannot by itself pay that local leaf.

## 6. Quantitatively useful replacement on the next r13 transverse leaf

After the child scalar-pivot branch and the now-paid strong-edge branch are excluded, account04/B20 r13 supplies anchors `i,j`, a physical index set K and columns

`u=A[K,i]`, `v=A[K,j]`,                                         (6.1)

with

`||u||>beta0/sqrt(2)`,
`||v||>a0`,
`beta0=sqrt(3)/(128 sqrt(96))`,                                 (6.2)

and, at epsilon=1/64, either the aligned collar

`dist(v,span u)<||v||/64`,                                      (6.3)

or the transverse literal two-column cross block

`M2=[u v]=A[K,{i,j}]`

satisfies

`s2(M2)>a0/(64 sqrt(2))`
`      =4.6565947316667495e-10`.                                (6.4)

The completed physical-R2 fractional-smoothing theorem gives, for any literal cross block,

`H_(1/4)(Q):=sup_s E|Q-s|^(-1/4)
 <=3.929131770449763 e2(M2^T M2)^(-1/16)`.                       (6.5)

Since `e2(M2^T M2)=s1(M2)^2 s2(M2)^2>=s2(M2)^4`, (6.4) yields

`boxed: H_(1/4)(Q)<845.823`.                                    (6.6)

Hence every interval I of length delta satisfies

`boxed: P(Q in I)<711.250 delta^(1/4)`.                          (6.7)

This is a real full-ambient smoothing currency on the transverse child leaf, retaining arbitrary `A[K,K]`, all outside couplings and all tails. It is **not** an endpoint density theorem: generic interpolation from a quarter-potential/Frostman estimate to `L^infinity` is forbidden and false in the current correction record.

## 7. Target-valid obstruction to reducing the transverse branch to one physical edge

For each even m choose two orthonormal flat vectors in R^m,

`u=(1,...,1)/sqrt(m)`,
`v=(1,...,1,-1,...,-1)/sqrt(m)`,                                (7.1)

and put `M=[u v]`. Define on two hub coordinates H and m leaf coordinates K

`A_m=[[0_(2x2), M^T],[M,0_(mxm)]]`.                             (7.2)

Then the nonzero eigenvalues of `A_m` are exactly

`{1,1,-1,-1}`,                                                  (7.3)

so the exact target hypothesis is satisfied. The two-anchor crossing is maximally transverse,

`s1(M)=s2(M)=1`, `dist(v,span u)=1`,                             (7.4)

while every individual hub-leaf coefficient has magnitude

`1/sqrt(m) ->0`.                                                 (7.5)

Therefore no dimension-free implication

`transverse two-anchor aggregate => one physical edge of fixed size`

can be valid. This is a counterexample only to that stronger structural shortcut, not to QFORM. In fact the exact zero-hub-block subcase (7.2) is already paid by the completed two-hub theorem. The obstruction shows that the remaining transverse problem must exploit grouped/two-hub geometry or a genuinely additional smoothing resource rather than another one-edge extraction.

## 8. First unpaid implication after this closure

On the localized r13 child-window leaf, the first unpaid universal implication is now

`QFORM-R13-TRANSVERSE-OR-ALIGNED-TWOHUB-ENDPOINT-v2`:

Assume the full independent cap-one product hypotheses and `s3(A)>=1`; remain in the exact localized child-window scope of account04/B20 r13; exclude its already-paid scalar-pivot exit and the now-paid strong-edge leaf. Thus there are original anchors `i,j` and K satisfying (6.1)-(6.2), with

`|A_ii|<=1/64`,
`|A_jj|<a0`,
`|A_ij|<1/1024`,                                                 (8.1)

and either the transverse condition complementary to (6.3), carrying the full-law quarter-potential bound (6.6), or the aligned two-star collar (6.3). Prove a universal `L^infinity` bound while retaining arbitrary same-bank curvature on K, arbitrary outside couplings, affine terms, extra spectrum and every nonzero tail; or route either alternative source-preservingly into an already completed pair, grouped-hub, ridge/window, Fresnel or physical-volume receiver.

The target-valid family (7.2) rules out solving the transverse side by forcing a fixed individual edge. The existing two-hub arbitrary-remainder logarithmic profile also shows why one cannot merely take a worst conditional fiber. A successful closure must use the third target resource jointly with the grouped two-anchor smoothing.

A separate global debt remains the r50 `H_(1/4)+diffuse-third-source OR hubstar -> L-infinity` branch. It is not renamed as solved here.

## 9. Integrity/status

Preserved corrections: no law-uniform pointwise quadratic-phase decay; no worst-fiber/conditional-cap transfer; no independence after spectral rotation; no arbitrary-joint rank-three coarea; no deletion of nonzero coefficient tails as random-small perturbations; no generic Frostman-to-density interpolation.

Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.

No valid counterexample to the owner target was found. The stress family in Section 7 refutes only a stronger one-edge structural implication. Two independent end-to-end reviews are not triggered because this is not a full candidate proof.
