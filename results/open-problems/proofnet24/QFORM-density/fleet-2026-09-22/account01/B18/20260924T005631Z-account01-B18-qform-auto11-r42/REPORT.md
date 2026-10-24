SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-24T00:56:31Z.
attacking: literature-to-proof transfer for the remaining product-preserving rank-three source geometry; use sharp product-marginal density bounds to pay a genuine two-sided anchor whenever two cross directions survive transversely.

# account01/B18 r42 — transverse-rank-two payment for the two-sided anchor

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.

Status: **PROVED SUPPORTING TARGET-LEVEL IMPLICATION + DESIGNATED PARTNER APPLIED. FULL QFORM REMAINS OPEN / NOT PROVED.**

Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source state and correction discipline

Fresh control was read from `yspennstate/math-research-brain` main; the full theorem remains open. The proof below preserves original-coordinate product provenance and uses none of the live-refuted interfaces: no independence after rotation, no arbitrary-joint quadratic coarea bound, no conditional-cap-as-independence substitution, no pointwise law-uniform Fresnel decay, no worst-fiber positive moment, no deletion of a small nonzero quadratic coefficient, and no claim that the spectral hypothesis forces a uniformly good physical minor.

The newest designated partner result used here is account02/B18, commit

`yspennstate/math-open-problems@39fec6de415da54a5947972780a6aa76816bdca0`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260924T000400Z-account02-B18-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-ONE-SIDED-ANCHOR-CROSS-SQUARE-LP-v1` pays

`X^T M Y + alpha^T X + G(Y) + a W^2 + h(Y)W + c`

for disjoint original-coordinate banks `X,Y,W`, but deliberately leaves the case where `W` also couples into the `X` bank.

## 2. Primary literature matched literally

### Livshyts--Paouris--Pivovarov

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949, Israel J. Math. 216 (2016), 877--889.

Their main marginal theorem applies to a genuine product probability density

`f(x)=prod_i f_i(x_i)`, `||f_i||_infinity<=1`,

and says every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. Thus, with no moment, iid, bounded-support, log-concavity, centering, symmetry or smoothness assumptions:

- every unit linear projection has density cap `sqrt(2)`;
- every two-dimensional orthogonal projection has joint density cap `2`.

This matches the owner's arbitrary cap-one product input class exactly. I use it only for marginal density caps, never to assert that projected coordinates are independent.

### Rudelson--Vershynin

Mark Rudelson, Roman Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, IMRN 2015, 9594--9617, arXiv:1402.4492, Theorem 1.2, gives the sharp one-dimensional predecessor: for independent coordinates of density cap `K` and `sum a_i^2=1`, the density of `sum a_i X_i` is at most `sqrt(2)K`.

### Quadratic-form regularity literature does not close the owner quantifiers

Ronan Herry, Dominique Malicet, Guillaume Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488, assumes iid inputs lying in a substantially smoother Gaussian-functional class for its principal regularity/strong-convergence results. It therefore does not imply the owner's arbitrary non-iid rough cap-one theorem. A targeted search found no exact published theorem matching all owner quantifiers; this is only a hypothesis comparison, not a novelty claim.

## 3. New theorem: `QFORM-TWOSIDED-ANCHOR-TRANSVERSE-RANK2-v1`

Let

- `X=(X_1,...,X_m)`, `Y=(Y_1,...,Y_n)` and scalar `W` be disjoint sets of ORIGINAL independent coordinates, each scalar density bounded by one;
- `M` be a real `m x n` matrix;
- `alpha,g in R^m`;
- `H(Y,W)` be an arbitrary measurable real-valued function (finite a.s.).

Define

`T = X^T M Y + alpha^T X + (g^T X)W + H(Y,W)`.                    (3.1)

For `g!=0`, let `P_g` be the orthogonal projection in coefficient space `R^m` onto `g^perp`; for `g=0`, set `P_g=I`. Let

`s_1 >= s_2 >= ...`

be the singular values of `P_g M`. If `s_2>0`, then `T` has a density and

`boxed: ||p_T||_infinity <= 4 sqrt(2 pi) / sqrt(s_1 s_2).`        (3.2)

No continuity assertion is made by this proof.

### Proof

Condition on the ORIGINAL bank `(Y,W)=(y,w)`. The retained `X_i` are still independent with their original density caps and

`T | (Y=y,W=w) = c(y,w)^T X + const`,

where

`c(y,w)=My+alpha+w g`.                                             (3.3)

Whenever `c!=0`, the `k=1` LPP/Rudelson--Vershynin theorem gives the conditional density cap

`||p_(T|y,w)||_infinity <= sqrt(2)/||c(y,w)||_2`.                 (3.4)

Projecting orthogonally to `g` deletes the troublesome two-sided anchor coefficient exactly:

`||c(y,w)|| >= ||P_g(My+alpha)||`.                                (3.5)

Choose top left singular vectors `u_1,u_2` of `P_g M` and let `U=[u_1,u_2]`. Put

`B=U^T P_g M`, `beta=U^T P_g alpha`.                              (3.6)

Then

`B B^T = diag(s_1^2,s_2^2)`

and

`||P_g(My+alpha)|| >= ||By+beta||`.                               (3.7)

Whiten the two-row map:

`A=(BB^T)^(-1/2)B`, so `AA^T=I_2`.                               (3.8)

Thus `AY` is literally a two-dimensional orthogonal marginal of the original product law. LPP gives density at most `2`. Linear change of variables therefore gives

`||p_(BY+beta)||_infinity <= 2/sqrt(det(BB^T)) = 2/(s_1 s_2) =: K`. (3.9)

Now use only the elementary two-dimensional inverse-radius estimate. If a probability density `f` on `R^2` is bounded by `K`, then for every shift `z_0` and every `R>0`,

`E |Z-z_0|^(-1)
 <= K int_(|z-z_0|<=R) |z-z_0|^(-1) dz + R^(-1)
 = 2 pi K R + R^(-1)`.                                            (3.10)

Optimizing at `R=(2 pi K)^(-1/2)` gives

`E |Z-z_0|^(-1) <= 2 sqrt(2 pi K)`.                               (3.11)

With `K=2/(s_1s_2)`,

`E ||BY+beta||^(-1) <= 4 sqrt(pi)/sqrt(s_1s_2)`.                  (3.12)

Equations (3.4)--(3.7), averaged over `(Y,W)`, yield

`P(T in I) <= |I| sqrt(2) E ||BY+beta||^(-1)
             <= |I| 4 sqrt(2 pi)/sqrt(s_1s_2)`                    (3.13)

for every interval `I`. The exceptional set where `c=0` is null because it is contained in `{BY+beta=0}`, while `BY+beta` has an absolutely continuous two-dimensional law. The interval domination implies absolute continuity and the claimed essential density bound. QED.

The crucial point is that `W` may be arbitrarily dependent with the random coefficient `c(Y,W)` after conditioning on neither bank; the proof never needs a conditional density of `W`. The `Wg` term disappears under the deterministic transverse projection before the LPP two-dimensional marginal is used.

## 4. Physical quadratic-form corollary

Suppose a retained ORIGINAL-coordinate packet has coefficient matrix

`A_S = [[0, C, r],
        [C^T, B_Y, h],
        [r^T, h^T, a]]`,                                         (4.1)

with banks `X`, `Y`, scalar `W`, arbitrary symmetric `B_Y`, arbitrary `h`, arbitrary scalar `a`, and zero retained `X-X` block. Let `c_1>=c_2` be the top singular values of `P_r C`, where `P_r` projects onto `r^perp` (and is the identity if `r=0`). If `c_2>0`, then

`boxed: ||p_Q||_infinity <= 2 sqrt(2 pi)/sqrt(c_1 c_2).`          (4.2)

Indeed the polynomial has `M=2C`, `g=2r`, so the transverse singular values in (3.2) are `2c_1,2c_2`.

Arbitrary coefficients and couplings outside `S` are allowed: condition all outside ORIGINAL coordinates. They induce only affine terms in the retained variables, which are already covered by `alpha` and `H`. The bound is uniform in the conditioning and therefore lifts to the ambient quadratic form. This is an essential-bound statement; no continuity is inferred from mixing the conditional laws.

## 5. Target-valid two-sided-anchor family now closed

Take `m>=3`, `n>=2`; choose orthonormal coefficient vectors `u_1,u_2,u_3 in R^m` and `v_1,v_2 in R^n`. For any `delta>0`, define

`Q_delta = 2(u_1^T X)(v_1^T Y)
          +(u_2^T X)(v_2^T Y)
          +2W(u_3^T X)+delta W^2`.                                (5.1)

The coefficient matrix splits orthogonally into three blocks:

- `[[0,1],[1,0]]` on `(u_1,v_1)`, eigenvalues `+1,-1`;
- `[[0,1/2],[1/2,0]]` on `(u_2,v_2)`, eigenvalues `+1/2,-1/2`;
- `[[0,1],[1,delta]]` on `(u_3,W)`, eigenvalues
  `lambda_+ = (delta+sqrt(delta^2+4))/2 >1`,
  `lambda_- = (delta-sqrt(delta^2+4))/2`, with `|lambda_-|<1`.

Hence for every `delta>0` this is an exact owner-target family with **exactly three eigenvalues of modulus at least one**, namely `+1,-1,lambda_+`.

Here

`M=2u_1v_1^T+u_2v_2^T`, `g=2u_3`,

so `P_g M=M` and its two singular values are `s_1=2`, `s_2=1`. Therefore (3.2) gives

`boxed: ||p_(Q_delta)||_infinity <= 4 sqrt(pi)
       = 7.0898154036220635...`                                   (5.2)

uniformly in `delta`, dimension, orientation of the orthonormal coefficient vectors, and all admissible product input laws. The small diagonal `delta W^2` is retained exactly; no perturbative deletion occurs.

This family lies precisely beyond the newest partner's one-sided interface because `W` is coupled into the `X` bank. The new theorem pays it because two `X-Y` cross directions survive after projecting away the anchor direction.

## 6. Actual application of the completed account02/B18 theorem

The partner theorem is complementary, not superseded. If `g=0` in

`T = X^T M Y + alpha^T X + G(Y)+aW^2+h(Y)W+c`,

then account02/B18 proves, at `q=3/2`,

`boxed: ||p_T||_infinity
 <=12*2^(1/3)(|a| ||M||op^2)^(-1/3),`                             (6.1)

with a continuous `C_0` density for the standalone displayed form.

Apply it literally to its target-valid near-null family

`Q_delta^one = 2 delta^(-1/2)(u^T X)(v^T Y)
              +2W(r^T Y)+delta W^2`,                              (6.2)

where `u` is unit and `v,r` are orthonormal. Here `M=2delta^(-1/2)uv^T`, hence `||M||op=2delta^(-1/2)`, and `a=delta`. Direct substitution into (6.1) gives

`||p_(Q_delta^one)||_infinity
 <=12*2^(1/3) (4)^(-1/3)
 =12/2^(1/3)
 =9.524406311809196...`.                                          (6.3)

Equivalently, this is the partner's physical-cross normalization. Thus the completed partner theorem is actually consumed at an equation, not merely cited.

Combining the two mechanisms sharpens the local debt:

- **one-sided anchor** (`g=0`, nonzero square pivot): paid by the partner even when the cross operator has rank one;
- **two-sided anchor** (`g!=0`) with `rank(P_g M)>=2`: paid by (3.2), with arbitrary `H(Y,W)` and no need for a useful square pivot;
- what this interface still does **not** pay is the genuinely two-sided/source-entangled state in which `rank(P_g M)<=1`, or retained nonzero `X-X` curvature destroys the conditional linear-form structure.

This is a strictly narrower remaining obstruction than the partner's entire two-sided-anchor bridge.

## 7. Continuity bookkeeping

The new transverse-rank-two argument proves absolute continuity and an `L^infinity` bound via interval domination. It does not provide an `L^1` characteristic-function envelope or another uniform continuity mechanism, so **continuity is not claimed** for (3.2)/(4.2)/(5.2).

The partner's theorem does supply a `C_0` density for its standalone one-sided form; that continuity conclusion is kept in that exact scope only.

## 8. What remains for full QFORM

Full unrestricted QFORM remains OPEN. The bare hypothesis `s_3(A)>=1` still has to be compiled, using ORIGINAL-coordinate product provenance, into one of the paid packets. The immediate structural target suggested by this run is:

> In the surviving small-diagonal/local-overlap compiler, show that either a one-sided square/cross packet is available, or a two-sided hub admits two cross singular directions transverse to its hub arm at universal scale, or else the rank-<=1 transverse failure forces an already-paid principal-pair/ridge/grouped-source branch.

No such exhaustive compiler is proved here.

## 9. Source pins

- Fresh designated partner: `yspennstate/math-open-problems@39fec6de415da54a5947972780a6aa76816bdca0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260924T000400Z-account02-B18-QFORM-auto11/REPORT.md`.
- Livshyts--Paouris--Pivovarov: arXiv:1507.07949, DOI 10.1007/s11856-016-1431-5.
- Rudelson--Vershynin: arXiv:1402.4492, DOI 10.1093/imrn/rnu243.
- Herry--Malicet--Poly: arXiv:2303.09488.

Full-solution status at finish: **OPEN / NOT PROVED**.
