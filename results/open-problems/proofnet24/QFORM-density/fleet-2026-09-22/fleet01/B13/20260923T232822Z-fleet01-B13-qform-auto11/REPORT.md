SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T23:28:22Z.
attacking: sharpen the partner aggregate Pluecker packet by proving a sharp universal disjointness floor for the leave-one-out rank-two determinant law, then feed it into the product-set slab obstruction.

# fleet01/B13 — sharp rank-two determinant-DPP disjointness and absolute Pluecker-packet currency

Programme: `QFORM-DENSITY-3EIG-20260922`. Owner control revision: `2026-09-22.15`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Status: **ESSENTIAL STEP APPLIED / NEW SUPPORTING STRUCTURAL THEOREM. The unrestricted QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Unrestricted continuity remains separately OPEN.**

Fresh source refresh before this write: `yspennstate/math-research-brain@eb02983a8a6dabc4cfc31eea56667692545ea766`; fresh `math-open-problems/master` head observed as `c4610f778836a217009f7d1c773b5e7cd3788f50`. The current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` remains in force; no B13 stop was found.

No random-coordinate rotation is used. No law-uniform pointwise quadratic oscillatory decay, arbitrary-joint coarea bound, projection-density-only shortcut, interval extremality, bounded support diameter, bounded fragment count, or deletion of a small coefficient tail is used.

## 1. Source-pinned premises actually used

1. My preceding grouped-hub theorem, `QFORM-GROUPED-HUB-3LEAF-TRANSVERSE-v1`, is source-pinned at

`yspennstate/math-open-problems@38a8a2ae1cb319211ab4be60f6f8d6f7f03f85f9`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T223205Z-fleet01-B13-qform-auto11/REPORT.md`.

In the exact chamber

`A=D+U Lambda U^T`, `U^T U=I_2`,

for a physical triple `L={k,r,s}` and its complement, it implies the slab obstruction

`Delta_{krs} (det Lambda)^2 |tau_{krs}| <= C_T rho^(-5)`,          (1.1)

where

`C_T=759375/2=379687.5`,                                          (1.2)

`q_ij=det(u_i,u_j)^2`,

`Delta_{krs}=det(U_{[n]\{k,r,s}}^T U_{[n]\{k,r,s})`,

and

`tau_{krs}=d_k q_rs+d_r q_ks+d_s q_kr`.                           (1.3)

The statement works for arbitrary cap-one product laws and retains the whole complementary hub bank before any physical pair is selected.

2. The latest completed designated partner result is fleet02/B13 r37, source-pinned at

`yspennstate/math-open-problems@4a8e12f1956a541cbd8a03961c29de79d1b12592`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T225517Z-fleet02-B13-qform-r37/REPORT.md`.

It consumes fleet03/B13 r36, source-pinned at

`yspennstate/math-open-problems@a558625206539a6eaee5aa6b2c6d851ccd2f1990`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T223116Z-fleet03-B13-qform-r36/REPORT.md`.

The exact partner chamber used below is

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i c_i<=1/3`, `c_i=||u_i||^2`, `s_3(A)>=1`.    (1.4)

A physical coordinate `k` is selected with `|d_k|>=1`. For unordered pairs `E={i,j}` disjoint from `k`, define

`q_E=q_ij`,

`Delta_E=sum_{F: |F|=2, F cap E=empty, k notin F} q_F`,            (1.5)

`W=sum_E q_E Delta_E`,

`mu(E)=q_E Delta_E/W`.                                             (1.6)

Fleet02/B13 r37 lifts this pair law to a four-set law. For `R={a,b,c,d}` disjoint from `k`, put

`w_1=q_ab q_cd`, `w_2=q_ac q_bd`, `w_3=q_ad q_bc`,

`S_R=w_1+w_2+w_3`,                                                 (1.7)

and

`nu(R)=S_R/(sum_T S_T)`.                                          (1.8)

It proves the exact identities/inequalities

`W=2 sum_R S_R`,                                                   (1.9)

`max_m w_m <=(2/3)S_R`,                                           (1.10)

and the sampling rule: sample `R~nu`, then a perfect matching with probability `w_m/S_R`, then one of its two edges uniformly; the resulting edge has law `mu`.

If `M=E_mu |tau_E|`, an edge is declared good when `|tau_E|<=M/eta`. At `eta=1/64`, `gamma=1/4`, partner r37 proves

`nu(core)>=25/32`,                                                 (1.11)

where every core four-set is either:

- `C_2`: exactly two clean perfect matchings, the dirty matching has weight at most `S_R/4`, and each clean matching has weight at least `S_R/12`; or
- `C_3`: all three perfect matchings are clean.

For `C_3`, if the heaviest perfect matching is relabelled `{rs,tu}`, and

`Q_i=q_ki`, `beta_ab=2 sqrt(Q_a Q_b)/(Q_a+Q_b)`,                  (1.12)

partner r37's exact denominator-free identity yields

`beta_rs beta_tu sqrt(S_R) <=128 sqrt(3) M/|d_k|`.                (1.13)

Since `|d_k|>=1`, it is enough to control `M`.

3. I source-checked the prior weaker rank-two disjointness bound `1/10` in fleet01/B09. The theorem below is a strict sharp improvement under the same leverage cap `<=1/2`, not a renaming of that prior bound.

## 2. Extremal product-law reduction, at the safe optimizer-free level

I record the exact reduction used for slab witnesses because this slot is responsible for product-law extremality.

### Proposition `QFORM-PRODUCT-INDICATOR-PURIFICATION-v1` (source-checked/reproved here)

Let `K:R^n->[0,M]` be measurable. If `0<=f_i<=1` and `int f_i=1`, then there are measurable sets `E_i` with `|E_i|=1` such that

`int K(x) prod_i 1_{E_i}(x_i) dx >= int K(x) prod_i f_i(x_i) dx`. (2.1)

#### Proof

Fix all coordinates except coordinate `i` and define the bounded nonnegative fiber payoff

`g_i(t)=int K(x_1,...,x_{i-1},t,x_{i+1},...,x_n) prod_{j!=i} f_j(x_j) dx_{-i}`. (2.2)

The one-coordinate objective is `int g_i f_i`. By the bathtub principle on nonatomic Lebesgue measure,

`sup_{0<=h<=1, int h=1} int g_i h = sup_{|E|=1} int_E g_i`,        (2.3)

and a measure-one top-level set can be chosen so that replacing `f_i` by its indicator does not decrease the current objective. Perform this replacement successively for `i=1,...,n`. Each step preserves all already-purified coordinates and does not decrease the total integral. This proves (2.1). QED.

For the slab kernel

`K(x)=1_{ {x^T A x in J} }`,                                     (2.4)

this gives **zero-loss transfer for the same `A` and same interval `J`** from every actual cap-one product-law witness to a product of arbitrary measurable unit-measure sets.

For strict witnesses, each `E_i` can further be approximated in symmetric difference by a bounded finite union of intervals `F_i` of exactly measure one. Indeed Lebesgue regularity first gives a bounded finite union with arbitrarily small symmetric difference, and an arbitrarily small interval adjustment restores measure one. Since

`||prod_i 1_{E_i}-prod_i 1_{F_i}||_1 <= sum_i |E_i triangle F_i|`, (2.5)

slab probability changes by arbitrarily little. There is no uniform diameter or fragment-count bound, and no claim that a single interval or centered uniform law is extremal.

## 3. New sharp rank-two determinant-DPP disjointness theorem

### Theorem `QFORM-RANK2-DPP-DISJOINTNESS-316-v1`

Let `V` be a real `m x 2` matrix with

`V^T V=I_2`.                                                       (3.1)

Write its physical rows as `v_i^T`, and let

`ell_i=||v_i||^2 <=1/2`.                                          (3.2)

For each unordered pair `E={i,j}`, define

`p_E=det(v_i,v_j)^2`.                                              (3.3)

By Cauchy--Binet, `sum_E p_E=1`, so this is a probability law on two-element physical subsets. If `E,F` are iid with this law, then

`boxed: P(E cap F=empty) >=3/16.`                                 (3.4)

The constant `3/16` is sharp.

#### Proof

Write, for nonzero rows,

`v_i=sqrt(ell_i)(cos theta_i,sin theta_i)`,                        (3.5)

and choose arbitrary `theta_i` for zero rows. Parseval gives

`sum_i ell_i=2`,                                                   (3.6)

and, with

`z_i=e^(2 i theta_i)`,                                             (3.7)

also

`sum_i ell_i z_i=0`.                                               (3.8)

Indeed the real and imaginary parts of (3.8) are respectively

`sum_i(v_{i1}^2-v_{i2}^2)=0`, `2 sum_i v_{i1}v_{i2}=0`,           (3.9)

which follow from `V^T V=I_2`.

The pair weights are

`p_ij=ell_i ell_j sin^2(theta_i-theta_j)
     =(ell_i ell_j/2)(1-cos(2theta_i-2theta_j)).`                  (3.10)

First compute the one-point marginals. For each `i`,

`sum_{j!=i}p_ij
 =ell_i sum_j ell_j- sum_j <v_i,v_j>^2
 =2ell_i-ell_i
 =ell_i`,                                                         (3.11)

because `sum_j v_jv_j^T=I_2`. Therefore, if

`S=sum_i ell_i^2`, `C=sum_E p_E^2`,                               (3.12)

then the iid intersection identity gives

`boxed: delta:=P(E cap F=empty)=1-S+C.`                           (3.13)

Indeed `E|E cap F|=S`, while `P(E=F)=C`; if `P_1` is the probability of a one-point intersection, then `S=P_1+2C` and `1=delta+P_1+C`.

It remains to estimate the exact pair-collision term `C`. Put

`A_1=sum_i ell_i^2 z_i`, `A_2=sum_i ell_i^2 z_i^2`.               (3.14)

Using

`(1-cos t)^2=3/2-2cos t+(1/2)cos(2t)`                             (3.15)

in (3.10), then converting the three sums over `i<j` into squared moduli, gives the exact identity

`boxed: C=(3/16)S^2-(1/4)|A_1|^2+(1/16)|A_2|^2.`                  (3.16)

For completeness, if `T=sum_i ell_i^4`, then

`sum_{i<j}ell_i^2ell_j^2=(S^2-T)/2`,

`sum_{i<j}ell_i^2ell_j^2 cos(2theta_i-2theta_j)=(|A_1|^2-T)/2`,

`sum_{i<j}ell_i^2ell_j^2 cos(4theta_i-4theta_j)=(|A_2|^2-T)/2`;   (3.17)

the three `T` contributions cancel exactly, proving (3.16).

Set

`epsilon=1-S`.                                                     (3.18)

The leverage cap and (3.6) give `S<=1`, so `0<=epsilon<=1`. From (3.8),

`A_1=sum_i ell_i(ell_i-1/2)z_i`,                                  (3.19)

hence

`|A_1|<=sum_i ell_i(1/2-ell_i)=1-S=epsilon`.                      (3.20)

Drop the nonnegative `|A_2|^2/16` term in (3.16), substitute `S=1-epsilon`, and use (3.13):

`delta >= epsilon +(3/16)(1-epsilon)^2-(1/4)epsilon^2`

`       =3/16 +(10epsilon-epsilon^2)/16`

`       >=3/16`,                                                   (3.21)

because `0<=epsilon<=1`. This proves (3.4).

For sharpness, take four rows of norm `1/sqrt(2)` at angles

`0, pi/4, pi/2, 3pi/4`.                                           (3.22)

They form a Parseval two-frame, every leverage equals `1/2`, and `S=1`, `A_1=A_2=0`. Hence (3.16)-(3.13) give exactly

`delta=3/16`.                                                      (3.23)

QED.

The theorem is entirely deterministic. The angles in its proof rotate only the two-dimensional **coefficient representation** of a Parseval frame; no random coordinate is rotated or declared independent.

## 4. Leave-one-out consequence in the partner's diffuse rank-two chamber

Return to (1.4) and the partner-selected `k`. Put

`G=I_2-u_k u_k^T`, `Q_k=det G=1-c_k`.                              (4.1)

Since `c_k<=1/3`, `G` is positive definite and `Q_k>=2/3`. Whiten the remaining coefficient rows by

`v_i=G^(-1/2)u_i`, `i!=k`.                                        (4.2)

Then

`sum_{i!=k}v_i v_i^T=I_2`,                                       (4.3)

and

`det(v_i,v_j)^2=q_ij/Q_k`.                                        (4.4)

Thus the determinant-weighted pair law of the whitened frame is exactly the partner's normalized leave-one-out Pluecker law

`tilde q_E=q_E/Q_k`.                                               (4.5)

Its physical row leverage is

`ell_i=u_i^T G^(-1)u_i
      =(c_i-q_ik)/(1-c_k)
      <=c_i/(1-c_k)
      <=1/2`.                                                      (4.6)

Theorem 3 therefore applies and gives the sharp universal floor

`boxed: delta_k:=P_{E,F~tilde q}(E cap F=empty)>=3/16.`            (4.7)

The partner aggregate normalization has the exact identity

`W=Q_k^2 delta_k`.                                                 (4.8)

Consequently

`boxed: W>= (2/3)^2 (3/16)=1/12.`                                (4.9)

This improves the previously used `W>=1/1152` by a factor of `96` at the raw `W` level. More precisely, for ratios in which one factor of `Q_k` cancels, the gain is a factor of `144` over the preceding coarse chain.

Using partner r37's exact relation (1.9), we also obtain an **absolute, unnormalized four-packet currency**:

`boxed: sum_R S_R=W/2>=1/24.`                                    (4.10)

No individual physical Pluecker minor is lower-bounded.

## 5. Designated partner r37 applied to an actual slab inequality

Let

`rho=P{X^T A X in J}/|J|`                                        (5.1)

be an actual slab ratio in the non-rank-one branch of the partner chamber.

From my prior grouped theorem (1.1), multiply by `q_E`, sum over all pairs `E`, and divide by the partner's `W`:

`M:=E_mu|tau_E|`

`<= C_T [Q_k/W] |det Lambda|^(-2) rho^(-5)`

`= C_T [1/(Q_k delta_k)] |det Lambda|^(-2) rho^(-5)`.             (5.2)

Now (4.7) and `Q_k>=2/3` give

`Q_k delta_k>=1/8`.                                               (5.3)

Hence the sharpened intrinsic cancellation estimate is

`boxed:
 M<=8 C_T |det Lambda|^(-2) rho^(-5)
   =3037500 |det Lambda|^(-2) rho^(-5).}`                         (5.4)

Fleet03/B13 r36's partner split says that outside its rank-one approximation exit,

`|det Lambda|>H_0 rho^(-2)`,                                     (5.5)

where

`H_0=sqrt(1536 e^2)=106.534455308869...`.                         (5.6)

Substituting (5.5) into (5.4) gives the actual target-level inequality

`boxed:
 M< [3037500/(1536 e^2)] rho^(-1)
  =267.630809134903... rho^(-1).}`                                (5.7)

The previous coefficient in this branch was `38538.8365...`; the determinant-DPP floor therefore sharpens this step by the exact factor `144`.

Now apply the **completed designated partner fleet02/B13 r37 packet theorem** at `eta=1/64`, `gamma=1/4`. At least `25/32` of the normalized four-set law `nu` lies in its `C_2 union C_3` core. Because of the new absolute floor (4.10), this means

`boxed:
 sum_{R in core} S_R >= (25/32)(1/24)=25/768.`                    (5.8)

This is an absolute dimension-free aggregate packet mass, not merely a positive fraction of an a priori tiny normalization.

Every good edge now obeys, by (5.7),

`|tau_E|<=64M<17128.371785 rho^(-1)`.                              (5.9)

On a `C_3` packet choose its heaviest base matching `{rs,tu}`. Partner r37's exact denominator-free identity (1.13) and (5.7) give

`boxed:
 beta_rs beta_tu sqrt(S_R)
 <128 sqrt(3) (267.630809135) rho^(-1)
 <59334.421 rho^(-1).}`                                           (5.10)

Thus the diffuse exact-rank-two near-null branch now has an exhaustive aggregate statement with **absolute currency**:

- at least `25/768` total raw `S_R` mass lies in partner r37 core packets;
- each `C_2` packet has two clean cross-dominant matchings and a dirty matching of weight at most `S_R/4`;
- each `C_3` packet obeys the denominator-free balance-volume collapse (5.10);
- no `q_ki`, `q_ij`, `Delta_E`, or individual four-set weight is inverted.

This is the promised equation-level application of the completed fleet02/B13 result.

## 6. A useful random-cut corollary (structural only)

The same `W` floor implies a literal-coordinate cross-volume certificate. For a fair random partition of `[n]\{k}` into `I disjoint_union J`, a fixed ordered disjoint pair `(E,F)` with `|E|=|F|=2` has probability `1/16` of satisfying `E subset I`, `F subset J`. Therefore, for the rank-two carrier cross block

`B=U_I Lambda U_J^T`,                                             (6.1)

Cauchy--Binet gives

`E e_2(B^T B)=(det Lambda)^2 W/16`.                               (6.2)

Hence some **physical original-coordinate cut** satisfies

`boxed:
 e_2(B^T B)>=(det Lambda)^2/192.`                                 (6.3)

This does not by itself close the rough-law density problem: the small/near-zero physical scalar pivot and arbitrary same-bank curvature still have to be paid by a dependence-safe receiver. I record (6.3) only as a structural consequence and do not delete any residual curvature.

## 7. What has and has not been closed

The new theorem eliminates one concrete source of quantitative loss in the latest partner chain: the normalized leave-one-out rank-two Pluecker law cannot have vanishing disjointness under the diffuse leverage cap. Its disjointness probability is in fact at least the sharp constant `3/16`. Consequently the partner four-set packet law carries at least `1/24` raw matching mass and its `25/32` good core carries at least `25/768` raw mass.

The first unpaid implication is now

`QFORM-ABSOLUTE-PLUCKER-PACKET-TO-BANK-RECEIVER-v1`:

> Convert the absolute `25/768` aggregate packet currency into a product-preserving bank/finite-center density receiver when the `C_2` cross-dominant matching varies from packet to packet or the `C_3` star-balance factors degenerate. In the general non-exact-rank-two survivor, retain the already-proved `s_5=O(rho^-1)` physical cross-tail obstruction rather than deleting a coefficient-small tail. If such a receiver fails, construct a genuine bounded-finite-union unit-product-set counterexample.

The rank-two random-cut certificate (6.3) is available to that next step, but no assertion is made that pair volume alone solves the indefinite pushforward.

The full unrestricted conjecture remains **OPEN**. No continuity claim is made for the unrestricted target.

## 8. Corrections retained

- Uniform law-wise pointwise quadratic oscillatory decay is false.
- Spectral rotations do not preserve independence of the product inputs.
- Projection density by itself does not control an indefinite quadratic pushforward.
- Arbitrary-joint rank-three coarea and positive conditional-density-moment shortcuts are false.
- Small coefficient/operator norm is not a law-uniform small quadratic perturbation on arbitrarily translated or fragmented supports.
- Single-interval/centered-uniform, bounded-diameter, and uniform-fragment-count extremality are not assumed.
- The diagonal `pi` theorem is a scoped control only, not the general constant.
