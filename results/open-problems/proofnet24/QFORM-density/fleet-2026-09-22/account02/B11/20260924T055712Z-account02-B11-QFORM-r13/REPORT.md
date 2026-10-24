SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B11, 2026-09-24T05:57:12Z.
attacking: the volume-one LDL majority-sign collar; test whether its exact joint/pair/scalar density caps can by themselves regularize the opposite two-sheet logarithmic core, and retain the product factorization as the only admissible missing resource.

# account02/B11 r13 — two-sheet shell obstruction to dependence-blind LDL marginal compilers

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: indefinite signatures `(2,1)` / `(1,2)`  
Status: **NEW SOURCE-SCOPE OBSTRUCTION / REQUIRED PINNED RESULT APPLIED / FULL QFORM OPEN**  
Continuity of the full target: **not proved here**.

The unrestricted owner target remains OPEN / NOT PROVED / NOT DISPROVED. No moment, bounded-support, log-concavity, iid, diagonal-basis, or post-rotation independence hypothesis is added. The construction below is deliberately **not** a QFORM counterexample: it is an arbitrary dependent three-dimensional law engineered to match all of the coarse density-cap data available after the fresh account03/B11 r50 determinant-one LDL reduction. Its purpose is to prove that those coarse caps cannot replace the exact original-product characteristic-function factorization.

## 1. Fresh partner input and the exact hard normal form

The latest completed compatible designated-partner result consumed in this run is account03/B11 r50, source

`yspennstate/math-open-problems@d8d9b012dd63602c80919b2dbf53296905ba05a8`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260924T051120Z-account03-B11-QFORM-r50/REPORT.md`.

Its theorem `QFORM-PUNCTURED-VOLUME1-LDL-v1` writes the exact-rank-three punctured majority-sign collar as

`Q = a U^2 + gamma Y^2 + d V^2`,

where the three coefficient vectors `(u,y,v)` in the ORIGINAL source space have

`det Gram(u,y,v)=1`, `det Gram(y,v)=1`, and `a gamma d = det M`.

In the majority-sign branch `gamma d<0`; in the live small-pivot collar `|gamma d|` is large as `|a|` becomes small. The true law of `(U,Y,V)` retains the exact product-source characteristic-function factorization. Its coarse consequences include

`||p_(U,Y,V)||_infinity <= 2^(3/2)`, `||p_(Y,V)||_infinity <= 2`,

and, for the explicit shear of r50,

`||p_U||_infinity <= sqrt(2)/sqrt(1+r^2/a^2)`.

The question tested below is whether those caps plus the determinant/sign budget could already close the two-sheet side. They cannot.

## 2. A fixed target-spectrum coefficient family

Fix `0<epsilon<1` and put

`r = sqrt(1-epsilon^2)`,

`M_epsilon = [[epsilon,r,0],[r,-epsilon,0],[0,0,1]].`

The upper-left `2x2` block squares to the identity, hence

`spec(M_epsilon) = {1,1,-1}`.

Thus this is a strict target-spectrum `(2,1)` matrix for every `epsilon`, including `epsilon -> 0+`. Completing the first square gives the exact LDL identity

`epsilon Z^2 + 2r ZY - epsilon Y^2 + V^2
 = epsilon (Z + (r/epsilon)Y)^2 - epsilon^(-1) Y^2 + V^2.`

Set

`U = Z + (r/epsilon)Y`.

Then the completed coefficients are

`a=epsilon`, `gamma=-epsilon^(-1)`, `d=1`,

so

`a gamma d = -1 = det M_epsilon`,
`gamma d = -epsilon^(-1)`.

The shear `(Z,Y,V) -> (U,Y,V)` has determinant one. Its `U` coefficient vector has squared norm

`1+r^2/epsilon^2 = epsilon^(-2)`,

so a genuine product projection would obey the scalar cap

`||p_U||_infinity <= sqrt(2) epsilon`.

This family is therefore an exact algebraic model of the r50 majority-sign small-pivot geometry.

## 3. New obstruction theorem

### Theorem `QFORM-LDL-MARGINAL-CAPS-SUFFICIENT-FALSE-v1`

For every `0<epsilon<1`, every `0<delta<=1`, and every sufficiently large `R`, there is a probability density `rho_(epsilon,delta,R)` on `(U,Y,V)` such that

1. `||rho||_infinity = 1`;
2. `||p_(Y,V)||_infinity <= delta/(2R sqrt(epsilon))`;
3. `||p_U||_infinity <= sqrt(epsilon) delta/(2R)`;
4. for

   `F_epsilon(U,Y,V)=epsilon U^2-epsilon^(-1)Y^2+V^2`,

   the output density satisfies

   `p_(F_epsilon)(s) >= sqrt(2/3)/delta`

   for every `s in [-delta,0]`, provided `R>=2`.

In particular, choosing

`R >= max(2, delta/sqrt(epsilon))`

gives simultaneously

`||rho||_infinity <= 1 < 2^(3/2)`,
`||p_(Y,V)||_infinity <= 1/2 < 2`,
`||p_U||_infinity <= epsilon/2 < sqrt(2) epsilon`,

while `||p_(F_epsilon)||_infinity >= sqrt(2/3)/delta -> infinity` as `delta -> 0`.

Thus even the **joint cap, the determinant-one residual-pair cap, the shear-improved scalar cap, the exact coefficient determinant, the correct majority-sign residual product, and the exact small-pivot scaling** do not imply a uniform density bound for an arbitrary dependent law. The missing datum is genuinely the original-product projection/factorization.

#### Proof

First work in variables `(x,v,z)` with the canonical signature `(2,1)` form

`q_0(x,v,z)=x^2+v^2-z^2`.

For `R>=2`, `0<delta<=1`, and `L>0`, define

`E_(R,L,delta) = { R<=x<=R exp(L), 0<=v<=1, z>=0, -delta<=q_0(x,v,z)<=0 }.`

For fixed `(x,v)` put `A=x^2+v^2`. The permitted `z` interval is

`sqrt(A) <= z <= sqrt(A+delta)`,

of width

`w(A)=sqrt(A+delta)-sqrt(A)=delta/(sqrt(A+delta)+sqrt(A)).`

Put

`c_R = sqrt(1+(1+delta)/R^2) <= sqrt(3/2)`.

Since `x<=sqrt(A+delta)<=c_R x`,

`delta/(2 c_R x) <= w(A) <= delta/(2x)`.

Therefore

`delta L/(2c_R) <= |E_(R,L,delta)| <= delta L/2.`

The volume is continuous and strictly increasing in `L`, tends to zero with `L`, and tends to infinity with `L`. Hence there is a unique `L=L(R,delta)` for which `|E|=1`; for that choice

`2/delta <= L <= 2c_R/delta.`                                           (3.1)

Let `(X,B,Zeta)` have density `1_E`; this is a cap-one probability density. For every `s in [-delta,0]`, one-dimensional coarea in `z` gives

`p_(q_0)(s)
 = integral_R^(R exp L) integral_0^1 [2 sqrt(x^2+v^2-s)]^(-1) dv dx.`

Because `-s<=delta`,

`sqrt(x^2+v^2-s) <= sqrt(x^2+1+delta) <= c_R x`.

Using (3.1),

`p_(q_0)(s) >= L/(2c_R) >= 1/(c_R delta) >= sqrt(2/3)/delta.`       (3.2)

This concentration is on the **two-sheet side** `s<0`, not on the ruled one-sheet side.

The `x` marginal is just the cross-sectional `z` width integrated over `v`, hence

`p_X(x) <= delta/(2x) <= delta/(2R).`                              (3.3)

For fixed `(v,z)`, the admissible values of `x^2` lie in an interval of length `delta`; after intersecting with `x>=R`, the map `x=sqrt(t)` has derivative at most `1/(2R)`. Hence

`p_(B,Zeta)(v,z) <= delta/(2R).`                                  (3.4)

Now make the determinant-one anisotropic change of variables

`x=sqrt(epsilon) U`, `v=V`, `z=Y/sqrt(epsilon)`.

Its Jacobian is one, so the pulled-back joint density still has cap one and

`q_0(x,v,z)=epsilon U^2+V^2-epsilon^(-1)Y^2=F_epsilon(U,Y,V).`

The marginal transformations give

`p_U(u)=sqrt(epsilon) p_X(sqrt(epsilon)u)`,

and

`p_(Y,V)(y,v)=epsilon^(-1/2) p_(Zeta,B)(y/sqrt(epsilon),v)`.

Combining with (3.3)-(3.4) proves items 2-3, while (3.2) proves item 4. QED.

## 4. Why this is not a QFORM counterexample — and a required pinned result at a real inequality

The shell law above is an arbitrary dependent three-dimensional density. It is **not** asserted to be an orthogonal projection of independent cap-one original coordinates, and therefore does not disprove QFORM.

The contrast is exact. Take genuinely independent cap-one original variables `(Z,Y,V)` and the same matrix `M_epsilon`. The required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was read at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed Theorem A says that an `n=3` quadratic form all of whose eigenvalues have modulus at least `sigma` has

`||p_Q||_infinity <= 6 sqrt(pi)/sigma`,

uniformly in arbitrary linear terms and arbitrary independent cap-one laws. Since `spec(M_epsilon)={1,1,-1}`, this gives the actual target-valid inequality

`boxed: ||p_( (Z,Y,V)^T M_epsilon (Z,Y,V) )||_infinity <= 6 sqrt(pi) = 10.6347...`

for every `epsilon in (0,1)`.

The same pinned source's ruled Theorem C gives the sharper sign-specific estimate

`boxed: p_Q(s) <= pi sqrt(2),  s>=0.`

The shell obstruction was deliberately placed on `s in [-delta,0]`, the opposite two-sheet side, so no illicit one-sheet-to-two-sheet transfer occurs.

This is the clean separation needed in the live collar: the same coefficient geometry is uniformly harmless for the true product input, but can be arbitrarily bad after product provenance is replaced by even very strong joint/pair/scalar density caps.

## 5. Mandatory rank-two logarithm and the exact third-direction repair in the model family

Delete the independent third square `V^2` from the target matrix. The remaining block is

`B_epsilon=[[epsilon,r],[r,-epsilon]]`, `r=sqrt(1-epsilon^2)`,

with eigenvalues `+1,-1` for every `epsilon`.

For independent centered unit uniforms `(Z,Y)`, let `(P,N)` be the orthogonal eigen-coordinate rotation. Their joint density is the indicator of a rotated unit square, hence equals one throughout the Euclidean disk of radius `1/2` around the origin. Put

`S=P-N`, `T=P+N`.

Then

`R_epsilon = epsilon Z^2+2r ZY-epsilon Y^2 = P^2-N^2 = S T`.

The `(S,T)` density equals `1/2` on `|S|,|T|<=1/2`. Therefore for `0<|t|<1/4`,

`p_(R_epsilon)(t)
 >= integral_{|t|/(1/2) <= |s| <= 1/2} (1/2) ds/|s|
 = log(1/(4|t|)) -> infinity.`                                    (5.1)

The logarithmic saddle is thus present **uniformly through the entire small-pivot family**; making the physical pivot small does not remove it.

Restoring `V^2`, with `V` independent of `(Z,Y)`, removes the singularity without first making the rank-two density bounded. The current brain's completed orientation-free rank-two half-Riesz theorem applies to the determinant-one block and gives

`sup_t E |R_epsilon-t|^(-1/2) <= 16 sqrt(30)`

in the homogeneous/in-range case. Since a cap-one scalar square has density at most `y^(-1/2)` on the positive half-line,

`||p_(R_epsilon+V^2)||_infinity <= 16 sqrt(30)`.

The required pinned Theorem A improves the constant to `6 sqrt(pi)` for this literal three-coordinate target family. Conceptually, the third direction removes the rank-two logarithm by a half-order square convolution. In the hard high-dimensional r50 collar the difficulty is not curvature loss — r50 proves the coefficient product and three-volume stay quantitative — but that the third square shares the projected source bank, so this independent convolution argument is unavailable.

## 6. First unpaid implication after the obstruction

The first unpaid B11 implication is now more specific:

`QFORM-VOLUME1-LDL-TWOSHEET-PRODUCT-FACTOR-v2`.

For the r50 normal form

`Q=aU^2+gamma Y^2+dV^2`,

in the majority-sign branch with `gamma d<0`, exact determinant/Schur budget, a fresh-hub component inside `U`, and the determinant-one coefficient-volume identities, prove the opposite two-sheet essential-density bound by using the **exact original-coordinate product characteristic-function factorization before taking any worst marginal, X-ray, or absolute-value envelope**; or force a previously paid physical-pair, projected-volume, localized-triple, or source-disjoint-square exit.

The theorem above rules out a whole class of tempting compilers: no argument depending only on

`||p_(U,Y,V)||_infinity`, `||p_(Y,V)||_infinity`, `||p_U||_infinity`, `a gamma d`, `gamma d`, and the signature

can close this branch, even when the three density caps are made strictly *smaller* than the genuine product-projection bounds. The remaining resource is genuinely factorization/orthogonal-product provenance, not another marginal cap.

Arbitrary additional nonseparable spectrum beyond exact rank three remains a separate bridge to the full owner target. Full continuity remains separate.
