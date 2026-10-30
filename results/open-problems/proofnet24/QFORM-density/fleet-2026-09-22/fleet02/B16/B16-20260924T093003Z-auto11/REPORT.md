SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-24T09:30:03Z.
attacking: the partner r45 genuinely two-dimensional same-bank overlap by proving a determinant-homogeneous receiver for an arbitrary dependent projected pair plus one disjoint source scalar when that scalar has zero quadratic pivot.

# fleet02/B16 — dependent pair + source-separated null scalar

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `B16-20260924T093003Z-auto11`  
Role: Projection-product interaction / complementary constructions  
Status: **NEW TARGET-LEVEL SUPPORTING THEOREM + INTERFACE COUNTEREXAMPLE / FULL QFORM OPEN**  
Unrestricted continuity: **OPEN**.

## 1. First unpaid implication, early

`QFORM-SHAREDBANK-NONZERO-SCALARPIVOT-PRODUCTTRANSDUCER-v1`:

> The zero-pivot branch with one genuinely dependent two-dimensional product projection and one source-separated scalar is paid below with a determinant-homogeneous bound. What remains is the corresponding branch when the separated scalar has its own nonzero square. A bounded joint pair density plus a bounded independent scalar density is provably insufficient there; the next proof must retain more original-product provenance through Fresnel, a source-separated innovation, or a definite-plane exit.

The obstruction in Section 7 makes this distinction exact rather than heuristic.

## 2. Correction boundary and sources actually used

All original physical inputs are independent and have scalar densities at most one. No moments, support bounds, log-concavity, identical-law assumption, diagonal-basis independence, or post-rotation independence are introduced.

The live corrections remain binding: arbitrary-joint rank-three coarea is false; projected coordinates are generally dependent; worst conditional projection-density caps are unavailable; a small matrix coefficient is not a small random perturbation for unbounded laws; and physical-minor reciprocal certificates can fail on source-delocalized families.

The required pinned package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was reread at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The completed product-projection input used at the actual inequality below is the two-dimensional marginal cap

`||p_(R^T X)||_infinity <= 2 / sqrt(det(R^T R))`               (2.1)

for a rank-two projection of an original independent cap-one bank. It is used only as a **joint density** bound. No independence of the two projected coordinates is inferred. The scalar projection bound used below is

`||p_(v^T X)||_infinity <= sqrt(2)/||v||_2`.                   (2.2)

The latest compatible designated partner fleet03/B16 report is r45,

`yspennstate/math-open-problems@bc397f473db245b56f3a4a29a8af75b2562d1967`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260924T085813Z-fleet03-B16-QFORM-auto11-r3/REPORT.md`,

with checker PASS at `fb28047260afcaa64675fef64af6457e2815af2d`. Its named remaining B16 gap is the genuinely two-dimensional same-bank overlap. The theorem below closes the whole invertible zero-pivot part of that gap.

## 3. Main theorem: arbitrary dependent pair, one null scalar

Let `Z=(S,U)` have an arbitrary joint probability density `rho` on `R^2` satisfying

`||rho||_infinity <= M`,                                      (3.1)

and let `V` be independent of the **pair** `Z`, with scalar probability density `f` satisfying

`||f||_infinity <= N`.                                        (3.2)

Let `C` be a real symmetric `2 x 2` matrix, `ell in R^2`, and suppose

`B = [[C,ell],[ell^T,0]]`                                     (3.3)

is invertible. Allow arbitrary affine coefficients `p in R^2`, `q,c in R`, and put

`Q = Z^T C Z + 2 V ell^T Z + p^T Z + qV + c`.                (3.4)

### Theorem 3.1 — `QFORM-DEPENDENTPAIR-NULLSCALAR-DETERMINANT-v1`

The law of `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity <= 6 (MN)^(2/3) |det B|^(-1/3).`     (3.5)

No independence between `S` and `U` is assumed. Continuity is not claimed by this proof.

### Proof

Because `B` is invertible, `ell != 0`. First eliminate the affine `qV` term by a translation of the pair. Choose `z0` with `ell^T z0=q/2` and write `Z=Z'-z0`. Translation preserves the joint cap `M`; the coefficient of `V` becomes

`2 ell^T Z' V - 2 ell^T z0 V + qV = 2 ell^T Z' V`.            (3.6)

All other changes are affine/constant terms in `Z'` and do not affect the argument.

Put

`L=||ell||_2`, `e=ell/L`,                                    (3.7)

and let `w` be a unit vector perpendicular to `e`. Define the orthogonal pair coordinates

`x=w^T Z'`, `y=e^T Z'`.                                      (3.8)

This rotation is used only to rewrite a **joint density**: the density of `(x,y)` is still bounded by `M`; `x,y` are not declared independent. In these coordinates write

`C' = [[a,g],[g,d]]`.                                         (3.9)

The full quadratic carrier in `(x,y,V)` is

`B' = [[a,g,0],[g,d,L],[0,L,0]]`.                             (3.10)

A direct determinant expansion gives the key identity

`boxed: det B = det B' = -a L^2.`                             (3.11)

Hence `a != 0`.

Complete the square in the first projected coordinate. If its affine coefficient is `r`, set

`s = x + (g/a)y + r/(2a)`.                                   (3.12)

The map `(x,y)->(s,y)` is a determinant-one shear followed by translation, so its joint density `rho_tilde` still satisfies `||rho_tilde||_infinity<=M`. Equation (3.4) becomes

`Q = a s^2 + h(y) + 2 L y V + c0`,                           (3.13)

where `h` is an arbitrary real quadratic polynomial. This is the crucial source-safe normal form: dependence remains entirely inside the pair `(s,y)`.

For `y !=0`, integrate the genuinely independent scalar `V`. For almost every target `t`,

`p_Q(t)
 = integral_R [1/(2L|y|)] J_t(y) dy`,                        (3.14)

where

`J_t(y)
 = integral_R rho_tilde(s,y)
   f((t-c0-h(y)-a s^2)/(2Ly)) ds`.                            (3.15)

The set `y=0` has zero pair probability because `(s,y)` has a joint density. There are two complementary estimates on `J_t(y)`.

First, with

`m(y)=integral rho_tilde(s,y) ds`,                            (3.16)

use only `f<=N`:

`J_t(y) <= N m(y)`.                                           (3.17)

Second, spend the **joint** pair cap before resolving the square:

`J_t(y)
 <= M integral_R f((t-c0-h(y)-a s^2)/(2Ly)) ds`.              (3.18)

For every probability density `f<=N`, the one-half potential satisfies the bathtub estimate

`sup_z integral f(v)|v-z|^(-1/2) dv <= 2 sqrt(2N)`.           (3.19)

Indeed the decreasing kernel is maximized by density `N` on the centered interval of length `1/N`. The square substitution in (3.18) therefore gives

`integral f((T-a s^2)/(2Ly)) ds
 <= sqrt(2L|y|/|a|) 2sqrt(2N)
 = 4 sqrt(N L|y|/|a|)`,                                      (3.20)

uniformly in the shift `T=t-c0-h(y)`. Hence

`J_t(y) <= 4M sqrt(N L|y|/|a|)`.                             (3.21)

Insert (3.17),(3.21) into (3.14). With

`A=N/(2L)`,
`B0=2M sqrt(N/(|a|L))`,                                      (3.22)

we obtain

`p_Q(t)
 <= integral min(A m(y)/|y|, B0/|y|^(1/2)) dy`.               (3.23)

For every `R>0`, use the second branch on `|y|<=R` and the first outside. Since `integral m=1`,

`p_Q(t) <= 4B0 sqrt(R) + A/R`.                               (3.24)

Writing `x=sqrt(R)`, the minimum occurs at `x^3=A/(2B0)` and equals

`6 B0^(2/3)(A/2)^(1/3)
 = 6(MN)^(2/3)(|a|L^2)^(-1/3)`.                              (3.25)

Use (3.11) to obtain (3.5). QED.

The theorem explains the exact safe interface. A two-dimensional projected density can be inserted into a curved integral **before** conditioning one projected coordinate on the other. The hyperbolic `1/|y|` Jacobian is softened by the square to the locally integrable `|y|^(-1/2)`. No projected conditional density is ever formed.

## 4. Product-projection corollary

Let `I,J` be disjoint original-coordinate source banks. On `I`, define

`S=r^T X_I`, `U=u^T X_I`,                                    (4.1)

with positive Gram determinant

`G = [[||r||^2,<r,u>],[<r,u>,||u||^2]] > 0`.                 (4.2)

On the disjoint bank `J`, define

`V=v^T X_J`, `tau=||v||_2>0`.                                (4.3)

The pinned completed two-dimensional product-projection theorem (2.1) gives

`M <= 2 det(G)^(-1/2)`,                                       (4.4)

while (2.2) gives

`N <= sqrt(2)/tau`.                                           (4.5)

Because `I` and `J` are disjoint, the vector `(S,U)` and scalar `V` are genuinely independent **source objects**. Within `(S,U)` no independence is assumed. Since

`(2 sqrt(2))^(2/3)=2`,                                       (4.6)

Theorem 3.1 yields

`boxed:
 ||p_Q||_infinity
 <= 12 [|det B| det(G) tau^2]^(-1/3).`                        (4.7)

The estimate remains valid after conditioning a further disjoint source bank whenever that bank contributes only affine coefficients/translations to the displayed three-scalar packet, because (4.4)-(4.5) and the proof are uniform in those affine terms.

## 5. Exact-rank-three target consequence

Let `T` be the physical `n x 3` carrier matrix whose first two columns are the embedded vectors `r,u` on `I` and whose third column is embedded `v` on `J`. Then

`T^T T = diag(G,tau^2)`.                                      (5.1)

For

`A=T B T^T`,                                                   (5.2)

with `B` as in (3.3), the three nonzero eigenvalues have product

`pdet(A)=det(B) det(T^T T)=det(B)det(G)tau^2`.                 (5.3)

This follows from Sylvester's determinant identity, or from a thin QR factorization `T=UR`: the nonzero carrier is `RBR^T`, whose determinant is `det(B) det(R)^2`.

Therefore, if this exact-rank-three form is in the owner target, i.e. its three nonzero eigenvalues satisfy `|lambda_k|>=1`, then

`|det B|det(G)tau^2 = product_k |lambda_k| >=1`,               (5.4)

and (4.7) gives the universal strict-target bound

`boxed: ||p_(X^T A X)||_infinity <= 12.`                       (5.5)

This exact-rank-three class allows arbitrary dependence between the first two spectral-source statistics induced by their shared original-coordinate bank. The required zero pivot is a statement about the three-scalar carrier, not an independence assumption.

## 6. Latest partner r45 applied at an actual inequality

Partner r45 considers the strict target family

`Q_* = 3 S^2 + 6(S+U)V`.                                     (6.1)

Its three-scalar matrix is

`B_* = [[3,0,3],[0,0,3],[3,3,0]]`,                            (6.2)

with

`det B_*=-27`.                                                (6.3)

The partner checker records the eigenvalues numerically as

`-3.7409388111..., 1.3351256037..., 5.4058132074...`,          (6.4)

so all three have modulus strictly above one. Partner r45 proved a source-separated rank-one-overlap bound `256/3` when its scalar outputs came from three disjoint banks and identified the genuinely two-dimensional same-bank overlap as the next gap.

Now put **both** `S,U` on one original product bank as an orthonormal two-dimensional projection and put unit `V` on a disjoint bank. The pinned completed result gives the legitimate joint cap

`||p_(S,U)||_infinity <=2`;                                   (6.5)

it does not make `S,U` independent. Also `||p_V||_infinity<=sqrt(2)`. Theorem 3.1 then gives

`||p_(Q_*)||_infinity
 <= 6(2sqrt(2))^(2/3) 27^(-1/3)
 = boxed: 4.`                                                 (6.6)

Thus the partner's named two-dimensional overlap is fully paid for every invertible zero-pivot carrier, and its strict target example improves from `85.334` to a global bound `4` in the shared-pair configuration.

For comparison, the pinned ruled one-sheet theorem gives a dimension-free majority-sign bound on this indefinite rank-three family. The new estimate (6.6) is global: it also covers the opposite side of the critical value for this packet.

## 7. Exact obstruction: why a nonzero separated-scalar square needs more provenance

Theorem 3.1 cannot be extended to an arbitrary nonzero scalar pivot using only the two caps `M,N`. There is a sharp caps-only counterexample.

Fix `0<delta<1` and set

`R0=exp(2/delta)`.                                             (7.1)

In `(x,y)` coordinates let

`E_delta = {(x,y): 1<=x<=R0, 0<=y<=delta/x}`.                 (7.2)

Its area is

`|E_delta|=delta log R0=2`.                                   (7.3)

Map

`S=(x+y)/2`, `U=(x-y)/2`.                                    (7.4)

The Jacobian from `(x,y)` to `(S,U)` is `1/2`, so the image has area one. Let `(S,U)` be uniform on this image. Its joint density is exactly the indicator of a set of area one and hence

`||p_(S,U)||_infinity=1`.                                     (7.5)

But

`R=S^2-U^2=(S+U)(S-U)=xy`.                                   (7.6)

For every `0<r<delta`, the density of `R` is

`p_R(r)
 = (1/2) integral_1^R0 dx/x
 = (1/2)log R0
 = 1/delta`.                                                  (7.7)

Thus `R` is exactly Uniform `[0,delta]`.

Let `V` be independent Uniform `[0,1]`, so `||p_V||_infinity=1` and

`p_(V^2)(w)=1/(2sqrt(w))`, `0<w<1`.                            (7.8)

For

`Q_delta = S^2-U^2+V^2`,                                     (7.9)

which has the invertible diagonal carrier `diag(1,-1,1)`, convolution gives at `t=delta`

`p_(Q_delta)(delta)
 = (1/delta) integral_0^delta [2sqrt(delta-r)]^(-1) dr
 = delta^(-1/2) -> infinity.`                                (7.10)

Therefore **bounded joint density of a pair plus bounded density of an independent scalar does not by itself control a nonzero scalar square**, even for a determinant-one `(+,-,+)` carrier. This is NOT a counterexample to the original QFORM conjecture: the dependent pair in (7.4) has not been shown to be a two-dimensional projection of independent cap-one physical coordinates. It is a counterexample to the proposed caps-only interface and proves that more product provenance is mathematically necessary beyond the zero-pivot branch.

## 8. What this changes in the live proof graph

The zero separated-scalar pivot is no longer part of the fleet03/B16 r45 same-bank overlap debt. In that branch the exact determinant identity `det B=-a||ell||^2` turns the curved split into a homogeneous target estimate, and exact rank three with three large eigenvalues gives `||p||_infinity<=12` automatically.

The new first unpaid implication is therefore

`QFORM-SHAREDBANK-NONZERO-SCALARPIVOT-PRODUCTTRANSDUCER-v1`:

> In the surviving near-coloop/shared-bank configuration with a genuinely dependent product projection pair and a source-separated scalar carrying nonzero self-curvature, use additional original-coordinate product information before reducing to a mere joint pair cap. Candidate exits are: Fresnel-linearize the separated scalar while keeping the pair density inside the pre-absolute curved integral; expose a second source-separated innovation and return to a hyperbolic receiver; or obtain a definite projected-plane block after conditioning. The caps-only reduction is impossible by Section 7.

Full unrestricted QFORM remains OPEN. Continuity remains OPEN outside branches with an integrable Fourier majorant.
