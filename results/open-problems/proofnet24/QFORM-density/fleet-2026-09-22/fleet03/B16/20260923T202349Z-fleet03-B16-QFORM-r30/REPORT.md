SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B16, 2026-09-23T20:23:49Z.
attacking: the live two-bank near-null collar by keeping the genuine hub density inside the Fourier integral, rather than paying the small LP coefficient before product aggregation.

# fleet03/B16 r30 — hub-aware punctured two-bank Fourier receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Projection-product interaction  
**Status:** `NEW SUPPORTING ANALYTIC RECEIVER / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new receiver gives a continuous `C_0` density on its stated branch. Global continuity remains open.

## 1. Scope and live source state

The owner target remains the unrestricted QFORM conjecture: independent original-coordinate inputs with one-dimensional probability densities at most one, arbitrary dimension, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moments, iid, compact support, log-concavity, connected support, smoothness, centering, Gaussianity, or post-rotation independence are assumed.


The immediate live source that motivates the calculation is the interactive two-bank curved-tube theorem

`yspennstate/math-open-problems@5e23223ed8626d8df8343d2d26879c08cf139093`

`proofnet24/QFORM-density/interactive/20260923T202245Z-two-bank-curved-tube/REPORT.md`.

It proves useful dyadic tube gains for the same canonical geometry, but records explicitly that direct inversion of the `2 epsilon L P` term costs `|epsilon|^(-1/2)` or a logarithm and is not uniform as `epsilon -> 0`. Its stated next mechanism is to keep the hub density inside the Fourier integral. The theorem below carries out that mechanism quantitatively.

I also read the current fleet02/B02 early shared-hub Fourier calculation at

`yspennstate/math-open-problems@ae1263e26df0a8d383fc98d1d2f73af75e157145`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T200844Z-fleet02-B02-qform-auto11/EARLY.md`.

That calculation pays an exact rank-one shared-hub crossing at the `epsilon=0` endpoint under its own coefficient reduction. It is not used as a proved global interpolation theorem here; the punctured-to-zero bridge remains open.

## 2. The new theorem

Let `H`, `A=(L_A,V_A,P_A)`, and `B=(L_B,V_B,P_B)` be mutually independent. Assume `H` has a probability density `f_H` with

`||f_H||_infinity <= L_H`.

Assume the bank vectors `A,B` have probability densities `g_A,g_B` on `R^3`, and let their `(L,V)` marginals be `m_A,m_B`. Write

`||m_i||_infinity <= M_{2,i}` and `||g_i||_infinity <= M_{3,i}`,

and set

`K_2=(M_{2,A}M_{2,B})^(1/2)`, `K_3=(M_{3,A}M_{3,B})^(1/2)`.

Put

`L=L_A+L_B`, `V=V_A+V_B`, `P=P_A+P_B`.

Consider, for real `beta,delta` and arbitrary real affine coefficients, the polynomial

`Q = 2 alpha H L + beta L^2 + 2 delta L V + lambda V^2 + 2 epsilon L P`

`    + u_H H + u_L L + u_V V + u_P P + u_0`,                     (2.1)

where

`alpha * epsilon * lambda != 0`.                                  (2.2)

### Theorem `QFORM-HUB-AWARE-PUNCTURED-TWOBANK-FOURIER-v1`

The law of `Q` has a continuous density vanishing at infinity and

`boxed: ||p_Q||_infinity <= 3 [ L_H K_2 K_3 / |alpha epsilon lambda| ]^(1/3).`   (2.3)

The constant is independent of `beta,delta` and of every affine coefficient in (2.1). Dependence inside each three-dimensional bank is arbitrary; only the three source objects `H,A,B` are independent.

This is a whole-line density theorem, not a conditional projection-height estimate.

## 3. Proof: preserve the hub Fourier factor until after bank aggregation

Use the Fourier convention

`hat f(xi)=integral exp(-i xi x) f(x) dx`.

Fix `t!=0`. Integrating only the genuine independent hub gives

`k_t(l)=integral f_H(h) exp[i t(2 alpha l+u_H)h] dh`

`      =hat f_H(-t(2 alpha l+u_H)).`                               (3.1)

Thus the characteristic function is the expectation over the two banks of

`k_t(L) exp{i t[beta L^2+2 delta L V+lambda V^2+2 epsilon L P`

`                 +u_L L+u_V V+u_P P+u_0]}.`                     (3.2)

For the convolution law of the banks, define the partial `P`-Fourier slice

`h_zeta(l,v)=integral exp(i zeta p) (g_A*g_B)(l,v,p) dp`.           (3.3)

Its two-dimensional Fourier transform is, up to harmless sign conventions,

`phi_A(xi,nu,zeta) phi_B(xi,nu,zeta)`,                             (3.4)

where `phi_i` is the bank characteristic function. Put

`S(zeta)=integral_R2 |phi_A(xi,nu,zeta) phi_B(xi,nu,zeta)| dxi dnu`.   (3.5)

Now integrate the `P` phase exactly. The Fourier variable is constrained by

`zeta=t(2 epsilon l+u_P)`,

so

`l=l_t(zeta):=(zeta/t-u_P)/(2 epsilon)`,

`dl=dzeta/(2 |t epsilon|)`.                                       (3.6)

For this fixed `l`, the remaining `v` phase is quadratic with nonzero Hessian `2t lambda`. Fourier inversion in `(l,v)` and the full-line Fresnel formula give

`|integral_R exp{i t(lambda v^2+2 delta l v+u_V v)+i nu v} dv|`

`=sqrt(pi/(|t lambda|)).`                                         (3.7)

The `beta l^2`, `u_L l`, `u_0`, and Fourier-`xi` terms have modulus one. Consequently

`|phi_Q(t)|`

`<= [1/(8 pi^(3/2))] |epsilon|^(-1)|lambda|^(-1/2)|t|^(-3/2)`

`   * integral_R |hat f_H(-alpha zeta/epsilon + c_t)| S(zeta) dzeta`,   (3.8)

where `c_t=t(alpha u_P/epsilon-u_H)` is a translation depending on the affine terms. Translation is harmless below.

For rigor with rough, unbounded densities, (3.7)-(3.8) may be obtained first with a Gaussian cutoff `exp(-eta v^2)`, for which every exchange is classical. The complex Gaussian has the same uniform `C |t lambda|^(-1/2)` bound; the fixed-`zeta` bank product is integrable in `(xi,nu)` by the estimates below. Letting `eta downarrow 0` gives (3.8) by dominated convergence on the Fourier side and approximation of the original expectation. No pointwise decay of any input characteristic function is used.

## 4. The projection-product energy is exactly what is needed

For one bank define

`h_{i,zeta}(l,v)=integral exp(i zeta p) g_i(l,v,p) dp`.

Since `|h_{i,zeta}(l,v)|<=m_i(l,v)`, two-dimensional Plancherel and `integral m_i=1` give

`integral_R2 |phi_i(xi,nu,zeta)|^2 dxi dnu`

`=(2 pi)^2 ||h_{i,zeta}||_2^2 <=(2 pi)^2 M_{2,i}`.                (4.1)

Cauchy--Schwarz therefore yields the fixed-slice bound

`boxed: ||S||_infinity <=(2 pi)^2 K_2.`                            (4.2)

Three-dimensional Plancherel and `||g_i||_2^2<=M_{3,i}` give

`boxed: integral_R S(zeta) dzeta <=(2 pi)^3 K_3.`                  (4.3)

Interpolating only these two genuine bank-energy facts,

`||S||_2 <=(2 pi)^(5/2) (K_2 K_3)^(1/2).`                         (4.4)

The hub cap is converted to its own Plancherel energy rather than a pointwise oscillatory estimate:

`||f_H||_2^2<=L_H`, hence `||hat f_H||_2^2<=2 pi L_H`.             (4.5)

After the affine dilation in (3.8),

`||hat f_H(-alpha zeta/epsilon+c_t)||_2`

`<=sqrt(2 pi L_H |epsilon/alpha|).`                                (4.6)

Cauchy--Schwarz in the **remaining common frequency zeta** now gives

`integral |hat f_H(-alpha zeta/epsilon+c_t)| S(zeta) dzeta`

`<= (2 pi)^3 sqrt(L_H K_2 K_3 |epsilon/alpha|).`                   (4.7)

Substitution into (3.8) cancels half of the apparent `epsilon^(-1)` loss:

`boxed: |phi_Q(t)|`

`<= pi^(3/2) sqrt(L_H K_2 K_3) |alpha epsilon lambda|^(-1/2) |t|^(-3/2).`   (4.8)

This is the essential new implication. The common hub frequency is not estimated before the two product banks are aggregated.

Let

`A_0=pi^(3/2) sqrt(L_H K_2 K_3) |alpha epsilon lambda|^(-1/2)`.

Together with the trivial `|phi_Q(t)|<=1`,

`integral_R |phi_Q(t)| dt <=6 A_0^(2/3)`.                          (4.9)

Indeed the crossing point is `t_0=A_0^(2/3)` and each half-line contributes `t_0+2A_0 t_0^(-1/2)=3A_0^(2/3)`. Fourier inversion now gives

`||p_Q||_infinity <=(1/(2 pi))*6 A_0^(2/3)`

`=3 [L_H K_2 K_3/|alpha epsilon lambda|]^(1/3)`,                  (4.10)

which is (2.3). Since `phi_Q in L^1`, the inverse Fourier transform supplies a continuous `C_0` density. QED.

## 5. Product-coordinate corollary

Suppose each of the two banks is an original-coordinate product block with cap-one scalar inputs, and its three-row coefficient map has Gram matrix at least `kappa I_3`. Then every two-row `(L,V)` Gram is at least `kappa I_2`. The actual bounded-density projection theorem gives

`M_{2,i} <=2/kappa`,

`M_{3,i} <=2^(3/2) kappa^(-3/2)`.                                 (5.1)

Therefore, with `L_H<=1`,

`boxed: ||p_Q||_infinity`

`<=3*2^(5/6) kappa^(-5/6) |alpha epsilon lambda|^(-1/3).`         (5.2)

For example, if `kappa>=1/4` and `|alpha|,|lambda|>=1`, then the punctured branch `|epsilon|>=1/64` is paid by

`||p_Q||_infinity <=67.883`.                                      (5.3)

The numerical threshold is merely illustrative; (5.2) is the actual statement.

The theorem is also stable under conditioning on outside ORIGINAL coordinates whenever such conditioning changes only the affine coefficients in (2.1), because all constants above are uniform in those coefficients.

## 6. Designated fleet04/B16 result applied to an actual inequality

The completed partner report is

`yspennstate/math-open-problems@a70c05e517e8a195a31ab4f4c301c672d1c8d4e6`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B16/20260923T192012Z-fleet04-B16-QFORM-r2/REPORT.md`.

Its theorem `QFORM-PHYSICALPAIR-BANK-OVERLAP-v1` gives, in the live exact-rank-three physical-pair packet,

`||p_Q||_infinity <=9.2002740353 [D |det Lambda| tau det G_b]^(-1/5).`   (6.1)

If one live bank obeys the partner gate

`det G_b >= W_b s^2/(64 D tau)`,                                  (6.2)

then the packet identities `W_b>61/1728` and `|det Lambda|>=s^3` imply

`D |det Lambda| tau det G_b`

`>=W_b s^5/64 >61 s^5/(64*1728)`.                                (6.3)

Thus the actual target inequality is

`||p_Q||_infinity`

`<9.2002740353 (64*1728/61)^(1/5) s^(-1)`

`=41.2552799658... s^(-1) <=41.256`,                              (6.4)

because the target normalization has `s>=1`. This branch is continuous by the partner theorem. The hub-aware receiver above is therefore aimed only at the complementary small-volume/shared-bank collar, not at duplicating the already-paid partner branch.

## 7. What this changes and what remains

The newest curved-tube proof showed that direct inversion of the small `epsilon P` term exposes a bad `epsilon` factor. The new theorem keeps the true hub density in the common Fourier variable and replaces the raw `|epsilon|^(-1)` Fourier prefactor by the sharper pointwise characteristic-function cost `|epsilon|^(-1/2)`, which after time integration becomes the density cost

`boxed: |epsilon|^(-1/3).`                                        (7.1)

The argument is genuinely dependence-preserving: arbitrary dependence inside each projected three-dimensional bank is kept, and only disjoint original source banks are independent.

It does **not** close the full conjecture because (7.1) still deteriorates as `epsilon ->0`. The exact-zero endpoint has a separate shared-hub Fourier mechanism in the current fleet02/B02 calculation, but no uniform punctured-to-zero interpolation has yet been proved. The first B16 debt is now therefore sharply phrased:

**`QFORM-HUB-AWARE-EPSILON-UNIFORM-INTERPOLATION-v1`** — in the canonical two-bank packet, combine the rank-one shared-hub operator at `epsilon=0` with the punctured rank-three `LP` coupling above without paying any negative power or logarithm of `epsilon`, while retaining arbitrary within-bank dependence and rough cap-one source laws.

A second, separate full-target interface remains: stability under arbitrary additional spectral components beyond the exact-rank-three packets used by several current structural reductions.

No full solution or counterexample is claimed. Global continuity remains open even though the new receiver and the partner branch both give continuity on their stated scopes.
