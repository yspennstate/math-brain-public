SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B08, 2026-09-22T20:19:56Z.
attacking: compress the surviving 99-percent two-sided ridge-coloop branch into an exact-rank-two endpoint or a quantified near-rank-two spectral tail, then identify the exterior determinant bank carried by the top singular plane.

# fleet03/B08 — near-rank-two compression of the surviving diffuse ridge obstruction

**Run:** `20260922T201956Z-fleet03-B08-qform-diffuse-r20`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control at start:** revision `2026-09-22.15`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING STRUCTURAL THEOREM / EXACT-RANK-TWO ENDPOINT PAID / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The full target remains: for every dimension, every independent real input vector `X=(X_i)` whose coordinate probability densities satisfy `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density with one universal finite essential-supremum bound, or construct a target-valid counterexample. No moment, Gaussian, log-concave, compact-support, connected-support, or post-rotation independence assumption is introduced. Continuity is tracked separately.

This run does not use the refuted law-uniform pointwise quadratic-phase decay, unrestricted fiber suprema, the false arbitrary-joint rank-three coarea inequality, the false positive conditional projection-density moment, or a reciprocal estimate obtained by selecting one tiny physical minor. The mechanism is deliberately changed from the preceding B08 ridge-leverage/determinant-bank iteration: the surviving branch is compressed spectrally first.

The incoming B08 theorem is the source-pinned run

`yspennstate/math-open-problems@86cbf124545c3457b0037b49151f4f641391fc76`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T194215Z-fleet03-B08-qform-diffuse-r19/REPORT.md`.

In its only unpaid nonzero-pivot O0 residual branch there are a scale `gamma>0`, an actual original-coordinate residual cross block `H`, and a genuine original-coordinate scalar pivot `a!=0`. If `h_1>=h_2>=...>=0` are the singular values of `H`, put

`x_nu=min(1,h_nu^2/gamma^2)`

and, at the fine scale

`g=gamma/16`,

`mu_nu=h_nu^2/(g^2+h_nu^2)`.

The source proves

`e_2(x)=sum_(mu<nu) x_mu x_nu >=2/3`,                         (1.1)

and the unpaid branch has

`theta=sum_nu mu_nu <201/100`.                                 (1.2)

It also has physical indices `j,r` such that the left and right ridge kernels

`K_L=HH^T(g^2 I+HH^T)^(-1)`,
`K_R=H^TH(g^2 I+H^TH)^(-1)`

satisfy

`(K_L)_jj>99/100`, `(K_R)_rr>99/100`.                         (1.3)

The objective here is to exploit simultaneously (1.1) and the fact that the fine-scale effective dimension in (1.2) is only barely below two.

## 2. Elementary transfer from coarse truncated singular mass to fine ridge mass

For `0<=x<=1` define

`f(x)=x/(x+1/256)`.

For every singular value,

`mu_nu >= f(x_nu)`.                                            (2.1)

Indeed, if `h_nu<=gamma`, equality holds. If `h_nu>=gamma`, then `x_nu=1` and

`mu_nu>=gamma^2/(gamma^2+gamma^2/256)=256/257=f(1)`.

For `0<=x<=1/2`,

`f(x)>= (256/129)x`,                                          (2.2)

because `x+1/256<=129/256`.

## 3. Two singular directions must already be macroscopically large

### Theorem 3.1 — `QFORM-BICOLOOP-NEAR-RANK2-SPECTRAL-GAP-v1`

Under (1.1)-(1.2),

`boxed(x_2>1/2.)`                                              (3.1)

Consequently

`boxed(h_2>gamma/sqrt(2))`,                                   (3.2)

`boxed(mu_1,mu_2>128/129)`,                                   (3.3)

and

`boxed(sum_(nu>=3) mu_nu <329/12900.)`                         (3.4)

Moreover, if `H_2` is the rank-two SVD truncation of `H`, then

`boxed(
 ||H-H_2||_HS^2
 < (329/3218176) gamma^2,
)`                                                             (3.5)

so

`||H-H_2||_op <=||H-H_2||_HS <0.010111 gamma`,                 (3.6)

and, whenever `rank(H)>=3`,

`boxed(h_3/h_2<0.014300.)`                                    (3.7)

#### Proof of (3.1)

Assume for contradiction that `x_2<=1/2`.

**Case 1: `x_1<=1/2`.** Then every `x_nu<=1/2`. By (2.1)-(2.2) and (1.2), with `S=sum x_nu`,

`S < (129/256)(201/100)=25929/25600`.

But

`e_2(x)=(S^2-sum x_nu^2)/2 <=S^2/2`,

hence

`e_2(x)< (25929/25600)^2/2 <2/3`.

The exact positive gap is

`2/3-(25929/25600)^2/2
 =604500877/3932160000>0`,

contradicting (1.1).

**Case 2: `x_1>1/2` while every `x_nu<=1/2` for `nu>=2`.** Then

`f(x_1)>f(1/2)=128/129`.

Put `S_tail=sum_(nu>=2)x_nu`. Again using (2.1)-(2.2),

`S_tail
 <(129/256)(201/100-128/129)
 =13129/25600`.

Since `x_1<=1`,

`e_2(x)=x_1 S_tail+e_2(x_2,x_3,...)
 <=S_tail+S_tail^2/2
 <2/3`.

Here the exact positive gap is

`2/3-[13129/25600+(13129/25600)^2/2]
 =87713677/3932160000>0`.

This again contradicts (1.1), proving `x_2>1/2`.

Then (3.2) is immediate, and (2.1) gives (3.3). Therefore (1.2) yields

`T:=sum_(nu>=3)mu_nu
 <201/100-256/129
 =329/12900`.                                                  (3.8)

Finally

`h_nu^2/g^2=mu_nu/(1-mu_nu)`.

Every tail `mu_nu<=T`; hence

`sum_(nu>=3) h_nu^2/g^2
 =sum_(nu>=3) mu_nu/(1-mu_nu)
 <=T/(1-T)
 <329/12571`.

Since `g^2=gamma^2/256`, this is exactly (3.5). Equations (3.6)-(3.7) follow from `h_3<=||H-H_2||_HS` and (3.2). QED.

### Interpretation

The previously unpaid two-sided `99%` ridge-coloop branch is not a generic high-rank cross block. It is forced to be within **1.011 percent of the live scale `gamma` in Hilbert-Schmidt norm of an exact rank-two cross block**, while its second singular value is larger than `0.707 gamma`. The whole higher-singular tail is less than `1.43%` of `h_2` in Hilbert-Schmidt norm.

This is a structural reduction, not yet a perturbative density theorem: under the target's arbitrary bounded marginal laws, a small operator coefficient cannot simply be discarded by a moment estimate.

## 4. Exact-rank-two endpoint is now completely paid

A fresh completed fleet03/B06 theorem is

`QFORM-EXACT-RANK2-CROSSBANK-L3-v1`,

source

`yspennstate/math-open-problems@1287456c9a709f8c3f117c23faa46e75f4560d01`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T194649Z-fleet03-B06-qform-r17/REPORT.md`.

It keeps arbitrary self quadratic terms and affine terms and proves for an exact rank-two original-coordinate cross block `C`

`||p_R||_3 <=(3e)^(2/3) Pi_2(C)^(-1/3)`.                      (4.1)

The compatible completed fleet04 result applied here is fleet04/B18
`QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its proof supplies the dependence-safe square kernel

`p_Q(t)<=|a|^(-1/2) int_0^infinity
              p_R(t-sgn(a)u)u^(-1/2)du`,                     (4.2)

because completing the genuine original pivot produces only a conditional translate of a cap-one coordinate density. Combining (4.1)-(4.2) with the `L^3` split proved in the B06 source gives

`||p_Q||_infinity
 <=(2^(4/3)+1)sqrt(3e)
   |a|^(-1/2) Pi_2(C)^(-1/4)`.                                (4.3)

If the present residual has `rank(H)=2`, (1.1) says `x_1x_2>=2/3`, and therefore

`Pi_2(H)=h_1h_2>=gamma^2 sqrt(2/3)`.

Substitution in (4.3) proves

`boxed(
 ||p_Q||_infinity
 <10.575/sqrt(|a| gamma).
)`                                                             (4.4)

This branch proves absolute continuity and essential boundedness. Continuity is not asserted by the `L^3` plus dependent-square endpoint.

The designated `fleet04/B08` current-QFORM path was checked directly and still has no completed canonical QFORM report or shared handoff, so no designated-partner theorem is fabricated. Fleet04/B18 is used because it is completed, source-pinned, mathematically compatible fleet04 work.

## 5. New exterior-square concentration: the surviving determinant bank is almost rank one

The spectral gap has an additional consequence not visible in the preceding determinant-only argument.

Take an SVD of the normalized cross block

`Z=H(g^2 I+H^TH)^(-1/2)
  =sum_nu sqrt(mu_nu) u_nu v_nu^T`.                            (5.1)

Let `W=wedge^2 Z`, represented in physical row-pair and column-pair coordinates. Then

`W=sum_(alpha<beta)
 sqrt(mu_alpha mu_beta)
 (u_alpha wedge u_beta)(v_alpha wedge v_beta)^T`.              (5.2)

The terms in (5.2) are orthogonal in Frobenius inner product. Split

`W=W_12+W_tail`,                                               (5.3)

where `W_12` is the single `(1,2)` term.

From (3.8),

`||W_tail||_F^2
 =sum_((alpha,beta)!=(1,2)) mu_alpha mu_beta
 <=2T+T^2/2
 <17084641/332820000
 <0.051333`.                                                    (5.4)

Hence

`||W_tail||_F<0.226568`.                                      (5.5)

Now use the two-sided physical ridge-coloop condition (1.3). Put

`L_j=u_1(j)^2+u_2(j)^2`,
`R_r=v_1(r)^2+v_2(r)^2`.

The entire tail contribution to either diagonal ridge leverage is at most `T`; therefore

`L_j,R_r>99/100-T>6221/6450`.                                 (5.6)

Also `mu_1mu_2>(128/129)^2`. For the physical slice of exterior coordinates consisting of row-pairs containing `j` and column-pairs containing `r`, the top mode factorizes and has squared Frobenius norm

`||slice_jr(W_12)||_F^2
 =mu_1mu_2 L_j R_r
 > A_0`,                                                        (5.7)

where

`A_0=(128/129)^2(6221/6450)^2
    =158518644736/173076800625
    >0.915886`.

The residual slice has norm at most the global residual norm in (5.5). Therefore the reverse triangle inequality gives

`sum_(k!=j)sum_(s!=r)
 det Z[{j,k},{r,s}]^2
 =||slice_jr(W)||_F^2
 > (sqrt(A_0)-sqrt(B_0))^2`,                                  (5.8)

where

`B_0=17084641/332820000`.

Exact rational squaring verifies

`(sqrt(A_0)-sqrt(B_0))^2 >1067/2000=0.5335`.                  (5.9)

Thus

`boxed(
 sum_(k!=j)sum_(s!=r)
 det Z[{j,k},{r,s}]^2 >1067/2000.
)`                                                             (5.10)

This strengthens the previous `2349/5000=0.4698` lower bound.

More importantly than the numerical improvement, (5.3)-(5.7) prove that the entire incident determinant bank is within Frobenius distance `<0.226568` of the **single factorized exterior mode**

`sqrt(mu_1mu_2)
 [(u_1 wedge u_2)_{j,k}]_k
 [(v_1 wedge v_2)_{r,s}]_s^T`,                                (5.11)

whose own norm exceeds `sqrt(A_0)>0.9570`. So the surviving aggregate-before-inversion obstruction is not an arbitrary cloud of tiny minors: at the normalized ridge scale it is quantitatively close to a rank-one product bank generated by the top two singular planes.

### Exact check for (5.9)

Let `c=1067/2000`. Since `A_0+B_0-c>0` and

`(A_0+B_0-c)^2-4A_0B_0
 =1583861310111679009321/
   30674512808536064400000000
 >0`,

we have `A_0+B_0-2sqrt(A_0B_0)>c`, which is (5.9).

## 6. What this changes in the full proof tree

The r19 unpaid nonzero-pivot branch has now been reduced to two possibilities:

1. **Exact rank two.** Fully paid by (4.4), with arbitrary same-side self quadratic terms and arbitrary outside couplings retained.
2. **Strictly higher rank.** The full tail past rank two has Hilbert-Schmidt norm `<0.010111 gamma`, the singular gap obeys `h_3/h_2<0.014300`, and the two-sided physical determinant bank is within `<0.226568` in exterior Frobenius norm of a single factorized top-two-plane mode while retaining bank mass `>0.5335`.

The first unproved implication is therefore no longer generic determinant-bank aggregation. It is the much narrower **moment-free near-rank-two stability / grouped-factorized-bank transducer**:

> prove a product-preserving anti-concentration estimate for the actual original-coordinate cross form when its top two singular directions satisfy the exact-rank-two hypotheses above and the complete remaining singular tail obeys (3.5), without discarding that tail via moments, conditioning on spectral coordinates, or selecting one physical minor.

A plausible next mechanism is to combine the factorized exterior mode (5.11) with the rank-two `L^3` cross-bank estimate before taking absolute values over the tail. A naive norm perturbation is not asserted here; arbitrary cap-one laws have no moment bound.

The full universal QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full continuity also remains open; continuity is not obtained on the new exact-rank-two-plus-square branch.

## 7. Verification and provenance

The exact rational inequalities and constants are independently recomputed in `check.py`; its captured output is `check_output.txt`. No Monte Carlo evidence is used.

Fresh current-QFORM checks found no canonical `fleet04/B08` QFORM result, so the completed fleet04/B18 theorem is the fleet04 mathematical result actually applied. Repository transport is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
