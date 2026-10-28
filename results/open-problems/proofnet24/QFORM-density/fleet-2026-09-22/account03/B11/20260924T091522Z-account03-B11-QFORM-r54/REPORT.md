SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T09:15:22Z.
attacking: the Schur-difference Moyal compiler in the punctured indefinite collar — quantify all payable reciprocal-frequency moments and test whether a fiberwise shared-hub Fourier gain can survive a nonzero puncture.

# account03/B11 r54 — almost-second-order Schur negative moments and a sharp fiberwise puncture obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: genuinely rotated indefinite signatures `(2,1)` / `(1,2)`  
Status: **NEW SUPPORTING THEOREM + REFUTED INTERMEDIATE MECHANISM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **not proved by this run**.


This run keeps the current corrections: no law-uniform pointwise van-der-Corput decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea, no conditional cap after a sum/difference transform, no fiber-supremum argument, and no deletion of a small nonzero random perturbation.

The immediate predecessor is account03/B11 r53:

- repository `yspennstate/math-open-problems`
- commit `76badd15bb5b007835da3c731f56430bb7eb19b6`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260924T081221Z-account03-B11-QFORM-r53/REPORT.md`.

It introduced the product-valid Schur difference frequency `Z` and proved its 2D density cap. The designated partner theorem used below is account04/B11:

- theorem `QFORM-SPECTRAL-SCHUR-PSEUDODET-v1`
- repository `yspennstate/math-open-problems`
- commit `28cbe14c4381d5f1b58145b29bbcc160b4d2ea5c`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260924T041708Z-account04-B11-schur-pseudodet-r1/REPORT.md`.

A fresh account03/B03 result at commit `6d920f5ad706016d41d3072a2dc6e71a64bc0296` also proves a bounded-density theorem for a same-bank dependent pair coupled hyperbolically to one genuinely independent scalar. That theorem does not by itself absorb the B11 puncture term, because in the hard collar the additional translation of the hyperbolic scalar comes from the same residual product bank. The obstruction proved below explains why treating that translation perturbatively is unsafe.

## 1. Setup: exact rank three and the authentic difference-product frequency

Let

`A = R M R^T`, `R^T R = I_3`,

with all three eigenvalues of `M` nonzero. Write

`s := min_k |lambda_k(M)|`, `D := |det M|`.

Fix an ORIGINAL physical coordinate `h` with

`alpha := A_hh != 0`,

and leverage

`q := ||R^T e_h||^2`.

Block

`A = [[alpha,c^T],[c,B]]`

with respect to `h | h^c`, and form the physical Schur complement

`S_h := B - c c^T/alpha`.

Let `E` be an orthonormal basis of the rank-two range of `S_h`. For an independent copy `X'` of the original product input put

`U_j := X_j-X'_j`.

Then the `U_j` are independent and have cap-one densities

`mu_j(u)=int f_j(x)f_j(x-u)dx <= 1`.

Define

`Z := E^T S_h U_{h^c} in R^2`.

Account03/B11 r53 proves

`||p_Z||_infinity <= 2 / Delta_2(S_h)`,

where `Delta_2(S_h)` is the product of the two nonzero singular values of `S_h`.

The designated account04/B11 theorem proves the exact spectral identity

`Delta_2(S_h) = q D / |alpha|`.                                      (1.1)

Therefore

`K_Z := ||p_Z||_infinity <= 2 |alpha|/(qD)`.                        (1.2)

This law is an authentic deterministic linear image of the independent ORIGINAL-coordinate difference product. No conditional independence is asserted for the conjugate sum variables.

## 2. New theorem: every reciprocal Schur-frequency moment below order two is uniformly paid

### Theorem 2.1 — `QFORM-SCHUR-DIFFERENCE-NEGATIVE-MOMENTS-v1`

Let `Z` be any probability vector in `R^2` with density cap `||p_Z||_infinity <= K`. Then for every center `z0 in R^2` and every exponent

`0 < gamma < 2`,

one has

`boxed:
 E ||Z-z0||^(-gamma)
 <= [2/(2-gamma)] (pi K)^(gamma/2).
`                                                                    (2.1)

Consequently, for the Schur difference frequency above,

`boxed:
 E ||Z-z0||^(-gamma)
 <= [2/(2-gamma)]
    [2 pi |alpha|/(qD)]^(gamma/2).
`                                                                    (2.2)

In the live near-coloop collar

`q >= 63/64`, `0 < |alpha| <= s/64`, `D >= s^3`,                    (2.3)

this becomes

`boxed:
 E ||Z-z0||^(-gamma)
 <= C_gamma s^(-gamma),
 C_gamma := [2/(2-gamma)] (2pi/63)^(gamma/2).
`                                                                    (2.4)

Examples are

`C_1 = 0.6316109565672897...`,

`C_(3/2) = 0.7098874207331786...`.

Thus the punctured collar pays every reciprocal-frequency loss `||Z||^(-gamma)` strictly below the two-dimensional critical exponent `gamma=2`.

#### Proof

For every `r>0`, the density cap gives

`P(||Z-z0|| <= r) <= min(1, pi K r^2)`.                             (2.5)

Use layer cake with `Y=||Z-z0||^(-gamma)`:

`E Y = int_0^infinity P(Y>t) dt
     = int_0^infinity P(||Z-z0|| < t^(-1/gamma)) dt
     <= int_0^infinity min(1, pi K t^(-2/gamma)) dt.`               (2.6)

The two terms meet at

`t0=(pi K)^(gamma/2)`.

Since `gamma<2`,

`int_(t0)^infinity pi K t^(-2/gamma) dt
 = [gamma/(2-gamma)] t0`.

Adding the interval `[0,t0]` gives

`E Y <= [1+gamma/(2-gamma)]t0
      = [2/(2-gamma)](pi K)^(gamma/2)`,

which is (2.1). Substituting (1.2) gives (2.2), and (2.3) gives

`2 pi |alpha|/(qD)
 <= 2pi (s/64)/((63/64)s^3)
 = (2pi/63)s^(-2)`,

proving (2.4). QED.

### Interpretation

The earlier r53 bound used only the first negative moment `gamma=1`. The full two-dimensional density cap actually gives a much larger budget: any future Moyal/coarea compiler is allowed to lose almost two powers of the Schur frequency. The critical exponent `2` is sharp at the level of density-cap information: even a constant positive density near the center makes `E||Z||^(-2)` logarithmically divergent.

This is useful because it replaces the vague target “obtain a `1/||Z||` cost” by the quantitatively wider design window

`cost <= C ||Z||^(-gamma)` for any fixed `gamma<2`.                  (2.7)

A source-valid compiler in that range is already paid by the partner pseudodeterminant identity.

## 3. Exact physical puncture operator

The next question is whether one can obtain the missing time decay by first freezing all other variables and using a one-dimensional shared-hub Fourier operator. The answer is negative in the uniform-law class as soon as the puncture is nonzero.

For real nonzero `alpha0,beta0,delta`, a hub density `p` and quadratic/affine hub phase

`F_H(h)=a h^2 + ell h + const`,

define

`k_t(u) := int_R p(h) exp(i t F_H(h)) exp(i 2t h u) dh`             (3.1)

and the operator

`(T_t f)(y)
 := int_R k_t(alpha0 y + beta0 z)
            exp(i 2t delta y z) f(z) dz.`                           (3.2)

At the literal endpoint `delta=0`, the completed shared-hub argument gives a full `|t|^(-1)` `L^2 -> L^2` gain from the bounded hub density. A tempting puncture step is to claim that a sufficiently small nonzero `delta` retains that gain. The following theorem rules this out.

### Theorem 3.1 — `QFORM-NONZERO-PUNCTURE-FIBERWISE-TMINUS1-FALSE-v1`

Fix nonzero `alpha0,beta0,delta` and arbitrary real `a,ell`. For every `t>0` there exists a probability density `p_t` satisfying

`0 <= p_t <= 1`

such that the operator (3.2) obeys

`boxed:
 ||T_t||_(2->2)
 >= sqrt(pi/(8 t |delta|)).
`                                                                    (3.3)

Hence there is no universal constant `C` for which

`||T_t||_(2->2) <= C |t|^(-1)`                                     (3.4)

holds simultaneously for all cap-one hub laws once `delta !=0`, even when the hub phase is exactly quadratic plus affine. The best purely fiberwise puncture estimate cannot be continuous in the exponent at `delta=0`.

This refutes the intermediate **fiberwise perturbative compiler**, not the QFORM conjecture.

#### Proof

Use the unitary scaled Fourier transform

`(F_t f)(s)
 := sqrt(t/pi) int_R exp(i2t s z) f(z) dz`.                         (3.5)

Then `||F_t f||_2=||f||_2`. If `G=F_t f`, inserting (3.1) into (3.2) gives

`T_t f(y)
 = sqrt(pi/t) S_t G(y)`,                                          (3.6)

where

`S_t G(y)
 := int_R p(h) exp(i t(a h^2+ell h))
        exp(i2t alpha0 h y)
        G(beta0 h + delta y) dh`.                                  (3.7)

We now construct a unit vector `G` and a cap-one density `p` for which `S_t` has norm bounded below by a positive multiple of `|delta|^(-1/2)`.

Set

`c0 := t alpha0/(beta0 delta)`,

`d0 := t ell/beta0`,

`theta := t(a-alpha0 beta0/delta)`.                               (3.8)

For `theta !=0`, the phase-aligned set

`E_theta := {h>=0 : cos(theta h^2)>=1/2}`                          (3.9)

has infinite Lebesgue measure. Indeed for large integers `k`, it contains the interval whose squared endpoints satisfy

`|theta| h^2 in [2pi k-pi/3, 2pi k+pi/3]`,

whose length is comparable to `k^(-1/2)`; the sum of those lengths diverges. Therefore one may choose a bounded measurable subset `E subset E_theta` of measure exactly one. If `theta=0`, simply take `E=[0,1]`.

Put

`p=1_E`.                                                          (3.10)

Then `p` is a probability density and `p<=1`. Translate the construction if necessary so that `E` lies in a bounded interval `[0,H]`; only its finite diameter matters below.

For `L >= 2 |beta0| H`, define

`G_L(s)
 := L^(-1/2) exp(-i c0 s^2 - i d0 s) 1_[0,L](s)`.                 (3.11)

Clearly `||G_L||_2=1`.

For every `y` such that

`beta0 E + delta y subset [0,L]`,                                  (3.12)

substitution of (3.11) into (3.7) gives the exact phase expansion

`t(a h^2+ell h)+2t alpha0 h y
 - c0(beta0 h+delta y)^2
 - d0(beta0 h+delta y)`

`= theta h^2 - c0 delta^2 y^2 - d0 delta y`.                       (3.13)

The `h y` coefficient vanishes because

`2t alpha0 - 2c0 beta0 delta=0`,

and the linear `h` coefficient vanishes because

`t ell-d0 beta0=0`.                                                (3.14)

Hence on the `y`-set (3.12),

`|S_t G_L(y)|
 = L^(-1/2) |int_E exp(i theta h^2) dh|
 >= (1/2) L^(-1/2),`                                               (3.15)

because `Re exp(i theta h^2)>=1/2` on `E`.

The range `beta0 E` has diameter at most `|beta0|H`. Therefore the set of translations `delta y` for which (3.12) holds contains an interval of length at least

`L-|beta0|H >= L/2`.

Thus the corresponding set of `y` has length at least

`L/(2|delta|)`.                                                     (3.16)

Equations (3.15)-(3.16) yield

`||S_t G_L||_2^2
 >= [L/(2|delta|)] [1/(4L)]
 = 1/(8|delta|)`.                                                   (3.17)

Since `||G_L||_2=1`,

`||S_t||_(2->2) >= 1/sqrt(8|delta|)`.

Finally (3.6) proves

`||T_t||_(2->2)
 >= sqrt(pi/t) / sqrt(8|delta|)
 = sqrt(pi/(8t|delta|))`.

QED.

## 4. Matching upper scale and sharpness of the obstruction

The preceding lower bound has the correct `t` and `delta` powers. Indeed, without using any hub oscillation, Cauchy-Schwarz gives the universal upper estimate

`boxed:
 ||T_t||_(2->2) <= sqrt(pi/(t|delta|)).
`                                                                    (4.1)

To see this, write (3.7) and use `int p=1`:

`|S_tG(y)|^2
 <= int p(h) |G(beta0h+delta y)|^2 dh`.

Integrating in `y` and changing variables gives

`||S_tG||_2^2 <= |delta|^(-1)||G||_2^2`.

Combine with (3.6). Therefore, uniformly over cap-one hub laws, any nonzero puncture has the sharp fiberwise scale

`||T_t||_(2->2) asymp (t|delta|)^(-1/2)`                           (4.2)

up to an absolute factor `sqrt(8)`, whereas the exact endpoint `delta=0` has the stronger `t^(-1)` shared-hub gain.

This discontinuity is precisely why “the puncture is small, so keep the endpoint estimate” is not a legal argument under arbitrary fragmented densities.

## 5. Designated account04/B11 result applied to an actual inequality

Apply the partner identity (1.1) in the live near-coloop collar (2.3):

`Delta_2(S_h)=qD/|alpha|
 >= (63/64)s^3/(s/64)
 =63s^2`.                                                          (5.1)

Together with r53's product-projection density theorem,

`||p_Z||_infinity <=2/Delta_2(S_h)`,

this gives the actual quantitative flattening

`boxed: ||p_Z||_infinity <= 2/(63s^2).`                             (5.2)

The new Theorem 2.1 then yields, for every `0<gamma<2`,

`boxed:
 E||Z-z0||^(-gamma)
 <= [2/(2-gamma)](2pi/63)^(gamma/2)s^(-gamma).
`                                                                    (5.3)

In particular

`boxed:
 E||Z-z0||^(-3/2)
 <= 0.7098874207331786... s^(-3/2).
`                                                                    (5.4)

So the designated partner result now pays much more than the first reciprocal moment: any valid aggregate Moyal estimate losing up to `||Z||^(-3/2)` is already dimension-free, and in fact every fixed loss below order two is affordable.

The fiberwise obstruction in Section 3 does **not** contradict this. It shows only that one must not take a worst-case shared-hub operator norm before exploiting the authentic distribution of `Z`. The large Schur pseudovolume is valuable only if the product/difference averaging is retained until after the puncture is coupled to it.

## 6. Mandatory opposite-sign rank-two control

For independent `X,Y ~ Uniform[-1/2,1/2]`,

`Q_2=2XY`

has density

`p_(Q_2)(x)=log(1/(2|x|))`, `0<|x|<1/2`.                          (6.1)

Thus the rank-two indefinite endpoint is genuinely logarithmically singular.

The current three-direction picture is now sharper:

1. the Schur two-volume from the third direction explodes like `1/|alpha|` as the physical pivot closes;
2. in the authentic independent-copy difference law this produces a 2D frequency whose density height is `O(|alpha|)` and whose negative moments of every order `<2` are uniformly finite;
3. nevertheless, if one freezes that averaging and passes to a fiberwise shared-hub operator, any nonzero puncture drops the available pointwise operator decay from `t^(-1)` to the sharp `t^(-1/2)` scale.

Therefore the third direction removes the logarithm only through **joint product averaging**, not through a perturbative continuation of the exact endpoint operator bound.

## 7. Consequence for the next compiler

The r53 target `QFORM-SCHUR-DIFFERENCE-MOYAL-COMPILER-v1` should be replaced by the more precise interface:

`QFORM-SCHUR-DIFFERENCE-AVERAGE-FIRST-COMPILER-v1`:

> Starting from the unnormalised original-coordinate kernels
> `F_j(u,xi)=int f_j(x)f_j(x-u)e^{i xi(2x-u)}dx`, keep the `U`-integration and the Schur frequency `Z=E^TS_hU` inside the estimate until the puncture has been averaged. It is sufficient to derive a time-integrable majorant whose final random cost is `C||Z||^(-gamma)` for any fixed `gamma<2`. Do not take a fiberwise shared-hub `L^2` operator supremum first: Theorem 3.1 shows that route necessarily loses the endpoint `t^(-1)` gain for every nonzero puncture.

The fresh account03/B03 same-bank square/hyperbolic theorem suggests a complementary direct-small-ball route when the same-bank overlap can be reorganized into one dependent pair plus one genuinely source-disjoint scalar. In the B11 collar the remaining obstacle is exactly the extra same-bank translation; the present theorem proves it cannot be discarded merely because its coefficient is small.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate bridge to the full owner theorem.

## 8. Verification scope

A deterministic checker accompanying this report verifies:

- the exact phase-cancellation coefficients in (3.13)-(3.14) over random signed parameters;
- the collar constants in (5.2)-(5.4);
- the layer-cake constants in Theorem 2.1 for selected exponents.

These finite checks are regressions only. The mathematical claims above are proved analytically.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.
