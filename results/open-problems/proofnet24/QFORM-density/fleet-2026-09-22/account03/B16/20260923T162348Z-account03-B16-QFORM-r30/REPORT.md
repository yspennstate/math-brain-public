SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T16:23:48Z.
attacking: co-locate the true-near-coloop aggregate hyperbolic pair mass with two genuinely independent transverse product banks, rather than paying a reciprocal local minor or a conditional projection-height supremum.

# account03/B16 r30 — hyperbolic-mass / transverse-product two-bank compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING STRUCTURAL COMPILER / ONE NEW PAID PAIR EXIT / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new single-pair exit proves an essentially bounded density; continuity is not asserted there. The structural two-bank branch is not itself a density theorem. Global continuity remains open.

## 1. Scope and current source boundary

The owner target is unchanged: for every dimension, independent real original-coordinate inputs with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `X^T A X`, or give a valid counterexample. No moments, compact support, connected support, Gaussianity, log-concavity, post-rotation independence, or diagonal-basis hypothesis is used below.


The immediate B16 sources are:

1. `yspennstate/math-open-problems@3185d21d594f9e06450da809ca97fab2132285a4`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T031836Z-account03-B16-QFORM-r24/REPORT.md`. In the exact-rank-three hard branch it supplies a hub row `r_0=sqrt(h)e`, `h>63/64`, and after the existing pair exit every residual transverse row `z_i=P_(e^perp)r_i` obeys `||z_i||^2<1/64`; also `sum_i z_i z_i^T=I_2`.

2. `yspennstate/math-open-problems@321c962d54aaeb625a9417dea9842f0910c13714`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260923T132339Z-account03-B16-QFORM-r29/REPORT.md`. It reduces the true near-coloop chamber to product-preserving diffuse physical-star geometry after already-paid diagonal and local-pair exits.

3. account01/B10, current source `proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260923T145337Z-account01-B10-QFORM-auto11/REPORT.md`, establishes the exact bordered-pair identity and, on the punctured ultra-collar `|a|D<2^-12`, the aggregate negative hub-pair determinant mass

   `N_- := sum_{i: Delta_i<0} |Delta_i| > c_*`,

   where

   `c_*=(63/64)(4093/4096)=257859/262144=0.983654022216796875`.

4. account01/B06, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260923T130129Z-account01-B06-QFORM/REPORT.md`, proves `QFORM-RANK3-INDEFINITE-PAIR-DET-ONLY-v1`: for an exact-rank-three target with spectral scale `s`, any literal original-coordinate indefinite physical pair with determinant magnitude `delta` yields

   `||p_Q||_infinity <=4 sqrt(30) delta^(-3/8) s^(-1/4)`.

5. Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889 / arXiv:1507.07949: every `k`-dimensional orthogonal marginal of a cap-one product density is bounded by `2^(k/2)`. I use it below only for genuine linear projections of disjoint original-coordinate banks.

The exact-rank-three notation is

`A=R Lambda R^T`, `R^T R=I_3`, `D=|det Lambda|>=1`,

with hub spectral row

`r_0=sqrt(h)e`, `h>63/64`, `||e||=1`.

Write each leaf row as

`r_i=alpha_i e+z_i`, `z_i perpendicular e`.

Then

`sum_i z_i z_i^T=I_2`,
`sum_i alpha_i^2=1-h`,
`sum_i alpha_i z_i=0`.

The new theorem below is used only after the inherited B16 transverse-smallness reduction

`||z_i||^2<1/64` for every leaf i.

## 2. Elementary balanced transverse partition

### Lemma 2.1 — `QFORM-TRANSVERSE-TWO-BANK-BALANCE-v1`

Let `(z_i)` be vectors in `R^2` satisfying

`sum_i z_i z_i^T=I_2`, `max_i ||z_i||^2<1/64`.

Then there is a partition of the leaf indices into two disjoint banks `J,K` such that, with

`G_J=sum_(i in J) z_i z_i^T`, `G_K=sum_(i in K) z_i z_i^T`,

one has simultaneously

`(1/4) I_2 <= G_J,G_K <= (3/4) I_2`.                         (2.1)

#### Proof

Take independent Bernoulli variables `xi_i` with `P(xi_i=1)=1/2` and define

`G=sum_i xi_i z_i z_i^T`, `S=G-(1/2)I_2`.

Since the centered Bernoulli variables are independent and have variance `1/4`,

`E ||S||_F^2
 =(1/4) sum_i tr[(z_i z_i^T)^2]
 =(1/4) sum_i ||z_i||^4
 <(1/4)(1/64) sum_i ||z_i||^2
 =1/128`.                                                     (2.2)

If `||S||_op>=1/4`, then `||S||_F^2>=1/16`. Markov therefore gives

`P(||S||_op>=1/4)<(1/128)/(1/16)=1/8`.                         (2.3)

Hence a realization with `||S||_op<1/4` exists. Set `J={i:xi_i=1}`, `K=J^c`. Then `G_J=I_2/2+S`, `G_K=I_2/2-S`, proving (2.1). QED.

This is deterministic existence obtained from a finite probabilistic argument; it does not randomize the input law.

## 3. Co-locating the order-one indefinite-pair mass

For each leaf put

`Delta_i=det A[{0,i}]`,
`d_i=(-Delta_i)_+=|Delta_i| 1_(Delta_i<0)`.

On the account01/B10 punctured ultra-collar,

`N:=sum_i d_i=N_->c_*`.                                         (3.1)

The essential new point is that the transverse balance from Lemma 2.1 can be imposed **simultaneously** with a balance of this hyperbolic determinant mass, unless one individual physical pair is already quantitatively usable.

### Theorem 3.1 — `QFORM-ULTRACOLOOP-HYPERBOLIC-TRANSVERSE-TWO-BANK-v1`

Under the exact-rank-three hard-branch hypotheses above and `|a|D<2^-12`, one of the following alternatives holds.

**(A) One paid physical hyperbolic pair.** There is a leaf `i` such that

`Delta_i<0`, `d_i>=N/32>c_*/32`.                               (3.2)

Consequently, by `QFORM-RANK3-INDEFINITE-PAIR-DET-ONLY-v1` with `s=1`,

`||p_Q||_infinity
 <=4 sqrt(30) d_i^(-3/8)
 <4 sqrt(30)(c_*/32)^(-3/8)
 =80.8604159438... <81`.                                        (3.3)

This conclusion is an essential density bound; continuity is not claimed by this receiver.

**(B) Two independent, transverse-balanced, hyperbolic-mass banks.** The leaves admit a partition into disjoint original-coordinate banks `J,K` such that

`(1/4)I_2 <=G_J,G_K <=(3/4)I_2`,                               (3.4)

and

`N/4 <= sum_(i in J)d_i <=3N/4`,
`N/4 <= sum_(i in K)d_i <=3N/4`.                               (3.5)

In particular each bank carries strictly more than

`c_*/4=0.24591350555419921875`                                 (3.6)

of negative physical hub-pair determinant mass. Moreover, within either bank the normalized negative-determinant weights are diffuse:

`max_(i in J) d_i / sum_(j in J)d_j <1/8`,
`max_(i in K) d_i / sum_(j in K)d_j <1/8`.                     (3.7)

#### Proof

If (A) occurs, (3.3) follows immediately from the cited determinant-only physical-pair receiver. Assume therefore

`max_i d_i<N/32`.                                               (3.8)

Use the same independent Bernoulli partition as in Lemma 2.1 and set

`W=sum_i xi_i d_i`.

Then `E W=N/2`, and

`Var(W)
 =(1/4)sum_i d_i^2
 <=(1/4)(max_i d_i)sum_i d_i
 <N^2/128`.                                                      (3.9)

Chebyshev gives

`P(|W-N/2|>=N/4)<(N^2/128)/(N^2/16)=1/8`.                       (3.10)

The transverse-balance failure probability is `<1/8` by (2.3). Therefore, with probability greater than `3/4`, neither failure occurs. Choose such a realization. Then (3.4) holds, while

`N/4<W<3N/4`.

The complementary bank has determinant mass `N-W` and obeys the same interval, proving (3.5). Finally, (3.8) and the lower bound `W_B>N/4` give

`max_i d_i/W_B <(N/32)/(N/4)=1/8`,

which is (3.7). QED.

This is the main new compiler. It puts the hyperbolic two-coordinate currency and the genuinely two-dimensional transverse product currency in the **same two disjoint physical source banks**. It is stronger than separately knowing a large total pair mass and a diffuse transverse frame.

## 4. Actual bounded-density projection theorem applied to the two banks

For `B in {J,K}`, let `M_B` be the `2 x |B|` matrix whose columns are the transverse rows `z_i`, and define the genuine original-product projection

`Z_B=M_B X_B in R^2`.

Then

`M_B M_B^T=G_B`.

By (3.4), `G_B` is invertible and

`det G_B>=1/16`.                                                  (4.1)

Whiten only the deterministic coefficient matrix:

`Y_B=G_B^(-1/2) Z_B`.

The rows of `G_B^(-1/2)M_B` are orthonormal. Therefore the Livshyts--Paouris--Pivovarov theorem with `k=2` gives

`||p_(Y_B)||_infinity<=2`.

Changing variables back yields the actual joint transverse-projection bound

`boxed: ||p_(Z_B)||_infinity
 <=2/sqrt(det G_B)
 <=8.`                                                          (4.2)

Because `J` and `K` are disjoint sets of original independent coordinates, `Z_J` and `Z_K` are independent random vectors. This is genuine bank independence, not spectral-coordinate independence.

The same determinant lower bound can be spent in the completed rank-two affine half-Riesz theorem. For every invertible symmetric `2x2` matrix `H`, every affine vector `ell` on the original coordinates of bank `B`, and every `t`,

`E |Z_B^T H Z_B+ell^T X_B-t|^(-1/2)
 <=128[det(G_B)|det H|]^(-1/4)
 <=256 |det H|^(-1/4).`                                        (4.3)

Thus each bank is not merely a bounded joint projection; it carries a universal nonlinear rank-two receiver. Equation (4.3), rather than a naked fiber supremum, is the projection-product currency meant for the next curvature step.

## 5. The third rank-three resource is also split across the banks

For `i in J`, `j in K`, let `det(z_i,z_j)` be the oriented transverse area. Since `G_K=I_2-G_J`, if `lambda_1,lambda_2 in[1/4,3/4]` are the eigenvalues of `G_J`, then

`sum_(i in J,j in K) det(z_i,z_j)^2
 =tr(G_J)tr(G_K)-tr(G_J G_K)
 =lambda_1+lambda_2-2lambda_1lambda_2
 >=3/8`.                                                        (5.1)

The minimum is attained at the corners `(1/4,1/4)` and `(3/4,3/4)`.

Because the hub row is `r_0=sqrt(h)e`,

`det(r_0,r_i,r_j)^2=h det(z_i,z_j)^2`.

For an exact-rank-three principal triple,

`|det A[{0,i,j}]|
 =D det(r_0,r_i,r_j)^2`.

Therefore

`boxed:
 sum_(i in J,j in K)|det A[{0,i,j}]|
 >=(3/8)hD
 >(189/512)D
 >=189/512.`                                                    (5.2)

So alternative (B) has three simultaneous scale-free resources:

1. more than `c_*/4` negative hub-pair determinant mass in **each** bank;
2. a well-conditioned rank-two transverse projection in **each** bank, with joint density cap at most eight and half-Riesz cost at most `256|det H|^-1/4`;
3. at least `189D/512` of bordered physical triple-determinant mass crossing the two banks.

No single vanishing local minor has been inverted to obtain these currencies.

## 6. Designated account04/B16 result applied at an actual inequality

The completed account04/B16 ruled/Pluecker endpoint used by the preceding B16 chain gives, in exact rank three,

`||p_Q||_infinity <=12 D^(-1/3) d^(-1/6)`,                      (6.1)

where `d` is its disjoint Pluecker-basis mass. Hence at the actual fleet threshold

`d>=1/64`, `D>=1`,

one obtains the literal target inequality

`boxed: ||p_Q||_infinity<=24.`                                  (6.2)

The new Theorem 3.1 is entered only on the complementary partner branch `d<1/64` after the prior B16 reductions. I also consumed the newer account04/B16 transverse-fresh-bank theorem at `yspennstate/math-open-problems@4c11848f5274047472b374f9d64594480a11c2c4`; its heavy-coordinate fresh direction is a distinct paid branch and does not justify treating the diffuse banks in (4.2) as independent coordinates internally.

## 7. What changed and the next unpaid implication

Before this run the ultra-coloop obstruction had two separate facts: order-one aggregate indefinite hub-pair mass, and diffuse transverse product geometry. The missing product interaction was that these resources might live on incompatible coordinates. Theorem 3.1 removes that ambiguity: unless one physical pair already pays the density by `<81`, the **same two disjoint source banks** each carry both a full two-dimensional transverse frame and a diffuse order-one share of the negative hub-pair determinant mass, while the cross-bank bordered triple volume is also order one.

The exact next B16 implication is therefore

`QFORM-TWO-BANK-HYPERBOLIC-THIRD-RESOURCE-RECEIVER-v1`:

> Given the packet in alternative (B), combine one bank's determinant-diffuse hub hyperbolicity with the other bank's rank-two affine half-Riesz receiver, while spending the cross-bank bordered triple mass (5.2) before any reciprocal local-minor operation. The estimate must keep the exact same-side quadratic terms and longitudinal leakage, and must not condition to a worst projection slice.

A bare use of `||p_(Z_B)||_infinity<=8` is explicitly **not** enough; the live arbitrary-joint and fiber-trace counterexamples still apply to that shortcut. The point of (4.3) and (5.2) is to expose the nonlinear and third-rank resources needed beyond the marginal cap.

Arbitrary additional spectrum remains a separate owner-level interface after exact rank three. Full QFORM remains OPEN / NOT PROVED. Full-target continuity remains OPEN.
