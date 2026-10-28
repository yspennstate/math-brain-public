SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T07:47:38Z.
attacking: the punctured near-singular definite-pair interpolation; retain the small same-sign Schur square jointly with the full original-coordinate star and obtain a linear interval bound uniform through determinant zero.

# account03/B09 r47 — one-sided arcsine maximal closure for nonnegative physical pairs

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / quantitative inequalities and rigorous computations  
Run: `20260924T074738Z-account03-B09-QFORM-r47`  
Status: **NEW SUPPORTING THEOREM / PUNCTURED DEFINITE-PAIR ENDPOINT PAID / FULL QFORM OPEN / FULL-TARGET CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**.

All stochastic variables below are literal ORIGINAL coordinates. No random-variable rotation, moment hypothesis, support restriction, log-concavity, Gaussianity, iid assumption, or pointwise law-uniform quadratic-phase decay is used. The proof keeps the complete outside quadratic remainder. It also avoids the false absolute half-Riesz extension across a nonzero quadratic coefficient: the decisive replacement is a one-sided square kernel and an arcsine maximal inequality.

## 1. Exact debt and source boundary

The same-slot predecessor is

`yspennstate/math-open-problems@0ec2761c15a4699ff4d7208f59f19b7e025e4305`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T064711Z-account03-B09-QFORM-r46/REPORT.md`.

It paid the exact singular physical-pair face by the polynomial star

`H=a v-c u`

but left the nonzero near-singular **definite** pair as the next debt. The fresh account02/B08 source

`yspennstate/math-open-problems@cdd0eb22227a505e827a658038a1512897c0ad56`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/account02-B08-20260924T034000Z-7c4f/REPORT.md`

explicitly warns that the punctured coefficient cannot be deleted. Its exact stress family has hub pair `L diag(1,delta)`, `delta>0`, and a third spectral resource hidden in a diffuse bank. This run pays that definite-sign puncture without deleting the `delta X^2` term.

The designated account04/B09 source is

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It is applied at an actual target-valid inequality in Section 8.

## 2. Why the absolute half-potential is the wrong interface

After peeling one original coordinate from a near-singular definite physical pair, the exact remainder has the scalar-star form

`R=s X^2+T X+G`,

with `s` small but nonzero and `T` a genuine original-product linear projection. The tempting goal

`sup_t E |t-R|^(-1/2) <= C`

is false uniformly even in a very benign subfamily: if `T=2Z`, `s>0`, and `G=Z^2/s`, then

`R=s(X+Z/s)^2`,

and at `t=0` the absolute half-potential contains an inverse first power of the linear variable and diverges logarithmically whenever the latter has positive density at zero. The full two-square quadratic form may nevertheless have a bounded density. Thus the absolute half-potential throws away the same-sign geometry that is needed at the punctured face.

For a positive outer square, the exact conditional square density naturally produces instead the **one-sided** kernel

`(t-R)_+^(-1/2)`.

That orientation is the key new resource.

## 3. Arcsine maximal lemma

Let `f` be a probability density on `R` with `0<=f<=1`, and define the centered Hardy--Littlewood maximal function

`M f(y)=sup_{r>0} (1/(2r)) int_{y-r}^{y+r} f(x) dx`.

Since `f<=1`, `0<=Mf<=1`.

### Lemma 3.1 — arcsine kernel dominated by the square root maximal function

For every `y in R` and every `r>0`,

`boxed:
 int_{|x-y|<r} f(x) / sqrt(r^2-(x-y)^2) dx
 <= pi sqrt(Mf(y)).
`

### Proof

Put `m=Mf(y)`. Scale `x=y+rs`. Then the left side is

`int_{-1}^1 h(s)(1-s^2)^(-1/2) ds`,

where `h(s)=f(y+rs)`, `0<=h<=1`, and

`int_{-1}^1 h(s) ds
 = r^(-1) int_{y-r}^{y+r} f
 <=2m`.

The weight `(1-s^2)^(-1/2)` is symmetric and increases with `|s|`. By the elementary bathtub principle, at fixed mass at most `2m` the integral is maximized by filling the two endpoint intervals of length `m`. Hence it is at most

`2 int_{1-m}^1 (1-s^2)^(-1/2) ds
 =2 arccos(1-m)`.

For `0<=m<=1`,

`2 arccos(1-m) <= pi sqrt(m)`.

Indeed write `theta=arccos(1-m) in [0,pi/2]`; then `m=2 sin^2(theta/2)` and the inequality reduces to the monotonic lower bound for `sin x/x` on `[0,pi/4]`, with equality at `m=1`. QED.

## 4. Averaging the maximal function against a cap-K law

### Lemma 4.1

Let `Y` have a probability density `q` with `q<=K`. Then

`boxed:
 E sqrt(Mf(Y)) <=2 sqrt(3K).
`

### Proof

The one-dimensional centered maximal operator has the elementary weak `(1,1)` estimate

`|{Mf>lambda}| <=3/lambda`, `0<lambda<=1`,

because a Vitali disjoint subcollection of witnessing centered intervals has triple dilates covering the level set, while the intervals themselves are disjoint and each has average greater than `lambda`.

By layer cake and the density cap,

`E sqrt(Mf(Y))
 =int_0^1 P(Mf(Y)>u^2) du
 <=int_0^1 min(1, 3K/u^2) du
 <=2 sqrt(3K)`.

No support or regularity property of either density is used. QED.

## 5. Uniform one-sided scalar-star theorem

### Theorem 5.1 — `QFORM-SCALAR-STAR-ONESIDED-HALFPOTENTIAL-v1`

Let `X` be independent of a random object `Z`; assume `X` has probability density at most one. Let `T=T(Z)` have a density bounded by `M<infinity`, let `G=G(Z)` be arbitrary measurable, and let `s>=0`. Put

`R=sX^2+T X+G`.

Then

`boxed:
 sup_t E[(t-R)_+^(-1/2)] <=2 pi sqrt(6M).
`

The convention is that the integrand is zero when `t-R<=0`.

### Proof for `s>0`

Set

`Y=T/(2s)`,
`G_0=G-T^2/(4s)`.

Then

`R=s(X+Y)^2+G_0`.

For fixed `Z=z`, if `(t-G_0(z))/s<=0` the conditional contribution is zero. Otherwise set

`r(z)^2=(t-G_0(z))/s`.

Then

`E[(t-R)_+^(-1/2) | Z=z]
 =s^(-1/2)
   int f_X(x)[r(z)^2-(x+Y(z))^2]_+^(-1/2) dx`.

Lemma 3.1, centered at `-Y(z)`, bounds this by

`pi s^(-1/2) sqrt(M f_X(-Y(z)))`.

The variable `Y=T/(2s)` has density cap at most

`K=2sM`.

Lemma 4.1 therefore gives

`E[(t-R)_+^(-1/2)]
 <=pi s^(-1/2) 2 sqrt(3*2sM)
 =2 pi sqrt(6M)`.

The estimate is uniform in `t`, in the hidden dependence of `G` on `Z`, and in `s>0`.

### Endpoint `s=0`

For fixed `T=tau!=0`, the one-sided kernel in `X` is a translate/dilate of `u_+^(-1/2)`. The cap-one/mass-one bathtub bound gives

`E_X[(c-tau X)_+^(-1/2)] <=2 |tau|^(-1/2)`.

Since `T` has density cap `M`, another bathtub bound yields

`E |T|^(-1/2) <=2 sqrt(2M)`.

Thus the endpoint is at most `4 sqrt(2M)`, smaller than `2 pi sqrt(6M)`. QED.

### Mechanism

The result is stable through `s=0` precisely because the dangerous double-root singularity lies on the wrong side of the positive-square kernel. When the moving vertex matters, its center is `-T/(2s)`; the center cannot remain concentrated for a diffuse genuine product-linear `T`. The maximal-function averaging spends that motion without conditioning on the hidden remainder `G`.

## 6. Main theorem: every nonnegative physical pair with a nonzero polynomial star is paid

Consider two literal original coordinates `p,q` and all remaining original coordinates `L`. Write the full ambient quadratic matrix as

`A=[[a,c,u^T],[c,b,v^T],[u,v,C]]`,

where `C` is completely arbitrary symmetric. Arbitrary affine terms are also allowed. Put

`B=[[a,c],[c,b]]`,
`H=a v-c u`.

Assume

`a!=0`, `det B>=0`, and `H!=0`.

Because a real symmetric `2 x 2` block with positive determinant is definite, and determinant zero here is the semidefinite endpoint, multiplying the whole form by `sign(a)` reduces to the case

`a>0`,
`delta=det(B)/a>=0`.

Completing only the ORIGINAL coordinate `p` gives exactly

`Q=a(X_p+ell(X_q,X_L))^2 + R(X_q,X_L)`,

where

`R=delta X_q^2 + T(X_L) X_q + G(X_L)`,

`T(X_L)=2 g^T X_L+beta`,
`g=v-(c/a)u`,

and `G` contains the entire remaining Schur quadratic block and all induced affine terms.

For fixed `(X_q,X_L)`, the conditional density of the translated square satisfies

`p_{a(X_p+ell)^2}(y) <= a^(-1/2) y_+^(-1/2)`.

Consequently

`p_Q(t) <= a^(-1/2) E[(t-R)_+^(-1/2)]`.

The standard one-dimensional product-projection theorem for independent cap-one coordinates gives

`||p_{g^T X_L}||_infinity <= sqrt(2)/||g||_2`.

Therefore the scaled variable `T=2 g^T X_L+beta` has density cap

`M <=1/(sqrt(2)||g||_2)`.

Theorem 5.1 yields

`||p_Q||_infinity
 <=a^(-1/2) 2 pi sqrt(6M)
 <=2^(5/4) pi sqrt(3) (a||g||_2)^(-1/2)`.

Since `H=a g`, `||H||=a||g||`. We obtain the denominator-free statement.

### Theorem 6.1 — `QFORM-NONNEGATIVEPAIR-POLYNOMIAL-STAR-v1`

Under the preceding hypotheses,

`boxed:
 ||p_Q||_infinity
 <= 2^(5/4) pi sqrt(3) ||H||_2^(-1/2)
 < 12.942 ||H||_2^(-1/2).
`

Therefore every interval `I` obeys

`boxed:
 P(Q in I)
 <= 12.942 ||H||_2^(-1/2) |I|.
`

The bound is **completely independent of `det B`** and passes uniformly through the singular face. It keeps every coefficient of `C` exactly. This proves essential boundedness in the stated branch. Continuity is not separately proved by this argument.

For `det B=0`, r46's sharper exact-singular constant `2^(11/4)` remains preferable; Theorem 6.1 supplies a single uniform theorem across the whole semidefinite/definite side.

## 7. The live punctured B08 definite branch is now closed

The account02/B08 r32 punctured state carries

`|a| > 4031 L/8192`,
`||g|| >= L/8`,
`0<|det B/a|<0.031747 L`.

Whenever this physical pair is on the definite side (`det B>0`), Theorem 6.1 gives

`||p_Q||_infinity
 < [2^(5/4) pi sqrt(3)] /
   sqrt((4031/8192)(1/8)) * 1/L`

and hence

`boxed:
 ||p_Q||_infinity <52.184/L.
`

No small-coefficient deletion is used. Thus the entire nonzero **definite** puncture adjacent to the singular-hub face is paid.

The explicit target-valid stress family from account02/B08 is even cleaner. In the four-dimensional reduced basis take

`A_delta=
 [[1,0,0,0],
  [0,delta,1,0],
  [0,1,delta^(-1),0],
  [0,0,0,1]],
  0<delta<1.`

Its spectrum is exactly

`{0,1,1,delta+delta^(-1)}`,

so it has three eigenvalues of modulus at least one. For the physical pair `(1,2)`,

`B=diag(1,delta)`,
`H=(1,0)` on the remaining two coordinates,
`||H||=1`.

Theorem 6.1 therefore gives, uniformly as `delta->0`,

`boxed:
 ||p_Q||_infinity <12.942.
`

At the checker value `delta=1/128`, the spectrum is

`{0,1,1,128.0078125}`.

This directly pays the punctured-singular mechanism stressed by the source, while preserving arbitrary cap-one input laws.

## 8. Designated account04/B09 theorem applied at an actual inequality

Account04/B09 proves that a literal invertible `3 x 3` original-coordinate cross block `K` gives a continuous density with

`||p_Q||_infinity <=3 |det K|^(-1/3)`,

with arbitrary same-side curvature, affine terms, and outside couplings.

Take

`K=diag(4,2,1)`,
`A_cross=[[0,K],[K,0]]`.

The spectrum is exactly

`{-4,-2,-1,1,2,4}`

and `det K=8`. Hence the completed partner theorem gives the target-valid bound

`boxed:
 ||p_Q||_infinity <=3*8^(-1/3)=3/2.
`

Thus

`P(Q in I)<=1.5 |I|`

for every interval, and this partner branch has a continuous density.

## 9. Deterministic verification

`CHECK.py` beside this report verifies:

1. `2 arccos(1-m)<=pi sqrt(m)` on a dense deterministic grid;
2. on 2000 seeded positive- and negative-definite physical pairs, `H=a g` to machine precision and `sign(a)*delta>0`;
3. the target-valid near-singular regression spectrum at `delta=1/128`;
4. the exact constants in Theorems 5.1 and 6.1;
5. the live account02/B08 definite-branch constant `<52.184/L`; and
6. the designated partner inequality `3*8^(-1/3)=1.5`.

The maximum relative `H-a g` error was below `1.9e-16`. These computations are regression checks only; the proof is Sections 3-6.

## 10. What remains

This run closes `QFORM-NEAR-SINGULAR-DEFINITE-PAIR-INTERPOLATION-v1` in the full-ambient original-coordinate sense whenever the polynomial star is nonzero. The exact singular endpoint was already paid by r46; the present theorem proves the punctured definite side without a determinant loss.

The next B09 debt is the **opposite-sign / indefinite near-singular carrier** after the same product-preserving reduction. The one-sided arcsine argument is sign-specific: when the scalar Schur square has sign opposite to the peeled square, the dangerous cone is real and the positive-side kernel no longer excludes the double-root geometry. Existing pair-log smoothing is the natural receiver, but its remainder square-root profile must be obtained from the actual arm geometry without conditioning away the product-linear provenance.

A precise next target is

`QFORM-NEAR-SINGULAR-INDEFINITE-ARM-COMPILER-v1`:

> combine the completed indefinite pair-log theorem with the full two-row arm / projected-cross resources so that a small negative Schur coefficient and a diffuse original-coordinate star yield a universal O(|I|) bound, with arbitrary remaining curvature retained exactly.

Full unrestricted QFORM remains **OPEN**. Full-target continuity remains **OPEN**.

## 11. Provenance

Startup math-brain main: `fdce34c28d041bb3a7e7efa237522e9e2b403835`.  
Prepublication control refresh observed: `53dd4d5734bc633ec5088ba95995b8c32c12a4b0`.  
Pre-write math-open-problems master observed: `1ec2c1d57ce156a13f1cdfa602e5de5e2b5dc43e`.

Repository retrieval and application are verified. Separate native learned-memory receiver ingestion is not verified; status remains `WITHOUT_VERIFIED_BRAIN`.
