# Supplement — two-bank cross-square receiver removes the puncture at the exact zero-coupling endpoint

**Run:** `account01-B16-20260924T004217Z-auto11`  
**Status:** `SECOND NEW SUPPORTING THEOREM / FULL QFORM STILL OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

This supplement pushes the main report one step further. The r37-derived theorem there handles an arbitrary fresh-hub phase whenever a genuine `LP` puncture is present. The result below treats the complementary **exact zero-puncture** packet by using only a two-dimensional projection from each original product bank. It is again dependence-safe.

## 1. Theorem — `QFORM-HUBPHASE-TWOBANK-CROSSSQUARE-v1`

Let `H`, source bank `A`, and source bank `B` be mutually independent. Let

`(L_i,V_i)`, `i=A,B`,

be two-dimensional linear projections of bank `i`, with joint densities `g_i` satisfying

`||g_i||_infinity <= M_i`.                                         (1.1)

Let `R_H(H)`, `R_A(X^A)`, and `R_B(X^B)` be arbitrary real measurable functions of their respective original source blocks. Put

`L=L_A+L_B`, `V=V_A+V_B`.                                          (1.2)

Assume the hub density satisfies

`||f_H||_infinity <= L_H`.                                         (1.3)

For `alpha lambda !=0`, consider

`Q=R_H(H)+2 alpha H L+lambda V^2+R_A+R_B+affine`.                  (1.4)

Then `Q` has a continuous density vanishing at infinity and

`boxed:
 ||p_Q||_infinity
 <=3 [ L_H^2 M_A M_B/(alpha^2 |lambda|) ]^(1/3).
`                                                                    (1.5)

The theorem retains the dependence inside each pair `(L_i,V_i)`. The only independence used is between the three genuine original source blocks `H`, `A`, and `B`.

### Proof

For each outer Fourier time `t`, phase-weight bank `i` and push it to `(L_i,V_i)`:

`h_(i,t)(l,v)
 =g_i(l,v) E[exp(i t R_i)|L_i=l,V_i=v]`.                           (1.6)

Hence

`|h_(i,t)(l,v)|<=g_i(l,v)`                                        (1.7)

and therefore

`||h_(i,t)||_2^2
 <=int g_i^2
 <=M_i int g_i
 =M_i`.                                                            (1.8)

Let

`Phi_(i,t)(eta,xi)
 =int exp(i eta l+i xi v)h_(i,t)(l,v) dl dv`.                       (1.9)

Two-dimensional Plancherel gives

`||Phi_(i,t)||_2 <=2pi sqrt(M_i)`.                                 (1.10)

Thus Cauchy--Schwarz yields the exact product-energy estimate

`int_R2 |Phi_(A,t)(eta,xi) Phi_(B,t)(eta,xi)| d eta d xi
 <=(2pi)^2 sqrt(M_A M_B)`.                                        (1.11)

For `t lambda !=0`, use the one-dimensional Fresnel representation

`exp(i t lambda v^2)
 =c_(t,lambda)(4pi|t lambda|)^(-1/2)
   int_R exp(-i xi^2/(4t lambda)) exp(i xi v) d xi`,                (1.12)

where `|c_(t,lambda)|=1`. The identity may be obtained first with a Gaussian regulator and then passed to the limit; (1.11) supplies an integrable majorant for the resulting frequency integral.

Insert (1.12) with `v=V_A+V_B` into the characteristic function of (1.4). Since the two original banks are independent, their phase-weighted transforms factor, giving

`|phi_Q(t)|
 <=(4pi|t lambda|)^(-1/2)
   int_R int_R f_H(h)
      |Phi_(A,t)(2 alpha t h,xi) Phi_(B,t)(2 alpha t h,xi)|
   d h d xi`.                                                       (1.13)

The hub phase `exp(i t R_H(h))` has disappeared only because its modulus is one; no pointwise oscillatory estimate on the hub is used. Apply `f_H<=L_H` and change variables

`eta=2 alpha t h`, `d h=d eta/(2|alpha t|)`.                        (1.14)

Then (1.11) gives

`|phi_Q(t)|
 <= L_H/(2|alpha t| sqrt(4pi|t lambda|))
    (2pi)^2 sqrt(M_A M_B)`                                         (1.15)

and therefore

`boxed:
 |phi_Q(t)|
 <=pi^(3/2) L_H sqrt(M_A M_B)
   |alpha|^(-1)|lambda|^(-1/2)|t|^(-3/2).
`                                                                    (1.16)

Set

`C=pi^(3/2)L_H sqrt(M_A M_B)|alpha|^(-1)|lambda|^(-1/2)`.           (1.17)

Combining (1.16) with `|phi_Q(t)|<=1`,

`int_R |phi_Q(t)|dt<=6 C^(2/3)`.                                   (1.18)

Fourier inversion now gives

`||p_Q||_infinity
 <=(1/(2pi))6C^(2/3)
 =3[L_H^2M_AM_B/(alpha^2|lambda|)]^(1/3)`,                         (1.19)

which is (1.5). The `L^1` characteristic function also gives a continuous `C_0` density. QED.

## 2. Insert the actual bounded-density projection theorem

If each `(L_i,V_i)` is an orthonormal two-dimensional projection of an arbitrary cap-one original product bank, the actual bounded-density projection theorem gives

`M_A,M_B<=2`.                                                      (2.1)

For a cap-one fresh hub,

`boxed:
 ||p_Q||_infinity
 <=3*2^(2/3)|alpha|^(-2/3)|lambda|^(-1/3).
`                                                                    (2.2)

In the normalized case `alpha=lambda=1`,

`3*2^(2/3)=4.7622031559...`.                                       (2.3)

This uses only genuine product-bank independence and projection-density **energy** before the nonlinear Fresnel integration; it does not insert a bounded dependent projection density directly into an indefinite level-set integral.

## 3. Strict owner-target family with arbitrary hub square and genuinely dependent projected pairs

Take one fresh cap-one coordinate `H`, two arbitrary disjoint cap-one product banks `X^A,X^B`, and an additional independent cap-one coordinate `W`. In each bank choose two orthonormal coefficient rows and set

`(L_i,V_i)=T_i X^i`.                                                (3.1)

Let `E_A,E_B` be arbitrary symmetric same-bank matrices with

`||E_A||_op,||E_B||_op<=1/4`.                                     (3.2)

For arbitrary real `theta`, define

`Q_theta
 =theta H^2
  +2H(L_A+L_B)
  +(V_A+V_B)^2
  +(X^A)^TE_A X^A+(X^B)^TE_B X^B
  +W^2`.                                                           (3.3)

The theorem applied before the independent `W^2` convolution gives

`boxed:
 ||p_(Q_theta)||_infinity<=3*2^(2/3)<4.763
`                                                                    (3.4)

for every real `theta`; convolution with the independent `W^2` law cannot increase essential height. The density remains continuous and vanishes at infinity.

To verify the spectral target, let

`ell=(ell_A,ell_B)/sqrt(2)`, `v=(v_A,v_B)/sqrt(2)`                  (3.5)

be the normalized aggregate coefficient directions. Before the `E` perturbations and the direct `W` block, the carrier on `(H,ell,v)` is

`[[theta,sqrt(2),0],[sqrt(2),0,0],[0,0,2]]`.                       (3.6)

The `H,ell` block has roots

`(theta +/- sqrt(theta^2+8))/2`,                                   (3.7)

whose product is `-2`. If `theta>=0`, its positive root is at least `sqrt(2)`; if `theta<0`, its negative root has magnitude at least `sqrt(2)`. The `v` direction has eigenvalue `2`. Under the same-bank perturbation of norm at most `1/4`, Weyl leaves the relevant extreme eigenvalue with magnitude at least

`sqrt(2)-1/4>1`,                                                    (3.8)

and leaves a positive eigenvalue at least `2-1/4>1`. The independent `W` direction is an exact eigenvector with eigenvalue `1`. Hence the full matrix in (3.3) has at least three eigenvalues of modulus at least one for every `theta`.

Thus (3.4) is a strict target-valid, arbitrary-dimensional projection-product inequality in which each bank pair can be strongly dependent after projection and the fresh hub square is completely unrestricted.

## 4. Relation to the completed account02/B16 result

The completed account02/B16 r37 theorem at `c9c865f02890e5fe7108c49759ee82b84f42ee38` controls the complementary punctured packet carrying a nonzero `2 epsilon L P` term, via two three-dimensional bank energies. The main report of this run showed that its bound is invariant under an arbitrary hub phase.

The theorem here covers the exact `epsilon=0` cross-square packet with only two-dimensional bank energies. Therefore, in this canonical two-bank geometry:

- `epsilon!=0`: r37 plus the main report's hub-phase lift applies;
- `epsilon=0`: `QFORM-HUBPHASE-TWOBANK-CROSSSQUARE-v1` applies directly.

This does **not** yield a law-uniform perturbative estimate in `epsilon`, and does not contradict r37's explicit obstruction to such a comparison. It instead supplies two separate source-preserving receivers on the punctured and exact-zero strata.

## 5. Remaining structural debt

The B16 obstruction is now narrower than “a small nonzero fresh-hub square.” The hub square is harmless both with a genuine three-dimensional puncture and on the exact two-bank cross-square stratum. What remains for the true near-coloop survivor is to reduce its leaf quadratic, while preserving original-product source banks, to one of these two receivers with a quantitative transverse currency. A bare joint projection-density bound remains insufficient for the generic indefinite leaf quadratic.

Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**; global continuity remains open.
