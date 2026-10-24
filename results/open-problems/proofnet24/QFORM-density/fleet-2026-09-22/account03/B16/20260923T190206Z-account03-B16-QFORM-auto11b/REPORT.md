SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-23T19:02:06Z.
attacking: close the zero-Rayleigh endpoint and remove the Schur-sign restriction in the true near-coloop projection-product reduction, then test whether the same marginal/conditional caps can control a small nonzero hub diagonal.

# account03/B16 — conditional-shift zero pivot, sign-free punctured payment, and a sharp caps-only obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T190206Z-account03-B16-QFORM-auto11b`  
**Assignment:** Projection-product interaction  
**Status:** `TWO PROVED SUPPORTING BRANCH THEOREMS + ONE RIGOROUS INTERFACE COUNTEREXAMPLE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the two new positive branches prove absolute continuity and an essential density bound. Continuity is not claimed. Global continuity remains open.

## 1. Exact target and current hard chamber

The owner target remains the unrestricted statement: independent real original-coordinate inputs with one-dimensional probability densities bounded by one, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one. No moments, support, log-concavity, Gaussianity, connectedness or independence after rotation is assumed.

This run works inside the inherited exact-rank-three true-near-coloop chamber. Write

`A=R Lambda R^T`, `R^T R=I_3`, `D=|det Lambda|>=1`,

and select the physical hub row

`r_0=sqrt(c)e`, `c>63/64`.

The preceding B16 reduction has already paid every transverse-heavy leaf, so in the surviving branch every leaf transverse row has squared norm `<1/64`. Rotate only the deterministic two-dimensional spectral plane `e^perp` so

`Lambda=[[a,b,0],[b,u,v],[0,v,w]]`.                             (1.1)

Write each leaf row as `(s_j,p_j,q_j)` and define the actual leaf projections

`S=sum_j s_j X_j`, `U=sum_j p_j X_j`, `V=sum_j q_j X_j`.         (1.2)

Parseval gives

`||p||_2=||q||_2=1`, `p.q=0`,

and each row of the two-dimensional frame `(p_j,q_j)` has leverage

`p_j^2+q_j^2<1/64`.                                             (1.3)

The full quadratic in this exact-rank-three chamber is

`Q=a(sqrt(c)X_0+S)^2+2b(sqrt(c)X_0+S)U+uU^2+2vUV+wV^2`.          (1.4)

No random coordinate has been rotated.

The exact dependencies used below are:

1. account04/B16 `QFORM-HEAVY-FRESH-TRANSVERSE-CROSS-LIFT-v1`, `yspennstate/math-open-problems@48d2f4234b05dfa527f1119c2c3dfc4a4b941f5d`, which preserves original-coordinate provenance and permits an arbitrary shift of a genuinely fresh physical square;
2. `QFORM-RANK2-AFFINE-HALF-RIESZ-v1`, `@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`; in its diffuse-frame proof the sharper constant is `4 sqrt(2e)|det H|^(-1/4)`;
3. `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1`, `@1bbe7c7c194bc92e10fc9c3cb3eb548d65e7043d`;
4. the two-dimensional Livshyts--Paouris--Pivovarov orthogonal projection density bound `<=2` for cap-one product laws;
5. the current B16 ultra-collar compiler `@f6f7e407aea4977e9b061d90eefd8e692d3191ed` and its scale sharpening `@e073f14465e781bf78996438d9c267750d90728c`.

## 2. A dependence-safe conditional shift

Define

`Y:=X_0+S/sqrt(c)`.                                               (2.1)

The crucial point is not independence. Conditional on `(U,V)=z`, let `mu_z` be a regular conditional law of `S`. The original physical coordinate `X_0` is independent of the entire leaf vector, so

`p_(Y|U,V=z)(y)=int f_0(y-s/sqrt(c)) mu_z(ds)<=1`                (2.2)

for almost every `z`. Thus the conditional scalar density cap is inherited from one untouched physical source even though `S,U,V` can be strongly dependent.

Equation (1.4) becomes exactly

`Q=acY^2+2b sqrt(c)YU+uU^2+2vUV+wV^2`.                           (2.3)

This elementary change is the main product-provenance bridge of the run.

## 3. New endpoint theorem: the true near-coloop zero Rayleigh quotient is paid

### Theorem `QFORM-NEARCOLOOP-CONDITIONAL-SHIFT-ZEROPIVOT-v1`

Under (1.1)--(1.4), if

`a=e^T Lambda e=0`,                                             (3.1)

then `Q` has an essentially bounded density and

`||p_Q||_infinity
 <=3*2^(4/3)(cD)^(-1/3)
 <7.6`.                                                         (3.2)

No independence of `(Y,U,V)` is assumed. Continuity is not asserted.

### Proof

When `a=0`, (2.3) is a zero-pivot quadratic in `(Y,U,V)` with coefficient matrix

`G_0=[[0,b sqrt(c),0],[b sqrt(c),u,v],[0,v,w]]`.                 (3.3)

Because

`det Lambda=-b^2 w`,

we have the exact identity

`det G_0=-c b^2 w=c det Lambda`,                                (3.4)

so `|det G_0|=cD`.

By (2.2), the conditional law of `Y|(U,V)` has density cap `K=1`. By the actual bounded-density projection theorem, the two-dimensional orthogonal leaf projection `(U,V)` has joint density cap `M=2`. Apply `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1`:

`||p_Q||_infinity
 <=3*2^(2/3)(KM)^(2/3)|det G_0|^(-1/3)
 =3*2^(4/3)(cD)^(-1/3).`                                       (3.5)

Since `c>63/64` and `D>=1`, the right side is less than

`3*2^(4/3)(64/63)^(1/3)=7.599314012744...<7.6`.                (3.6)

QED.

This removes `a=0` from the B16 true-near-coloop debt. The conditional cap (2.2) is source-valid: it comes from averaging translates of one independent physical density, not from conditioning a projection on another projection.

## 4. Designated partner applied to the actual near-coloop equation

Assume now `a!=0`. Complete the square in the genuine physical hub `X_0`:

`Q=ac[X_0+S/sqrt(c)+bU/(a sqrt(c))]^2+(U,V)^T B_a(U,V)`,         (4.1)

where

`B_a=[[u-b^2/a,v],[v,w]]`.                                     (4.2)

Direct expansion gives

`det B_a=det Lambda/a`.                                         (4.3)

This is an exact instance of the designated partner account04/B16 theorem `QFORM-HEAVY-FRESH-TRANSVERSE-CROSS-LIFT-v1`:

- fresh bank `J={0}` and reserved direction `n=1`, hence `|n_0|=1`;
- receiver bank is the leaf bank and `P=(U,V)`;
- the receiver frame is orthonormal, so `det(MM^T)=1`;
- fresh-square coefficient `gamma=ac`;
- the correlated shift `S/sqrt(c)+bU/(a sqrt(c))` is exactly an allowed `a^T X_I` term.

The partner theorem therefore gives the concrete inequality

`||p_Q||_infinity
 <=128/sqrt(|ac|) * |det B_a|^(-1/4)
 =128 c^(-1/2)(|a|D)^(-1/4).`                                  (4.4)

At the threshold `|a|D>=2^(-12)`, this is `<1033`. This partner application is not merely a citation; (4.1)--(4.4) identify every theorem parameter in the actual B16 survivor.

## 5. New sign-free sharpening from the diffuse leaf frame

The direct partner estimate can be sharpened by retaining the two-dimensional diffuse product frame rather than taking the general rank-two receiver constant.

Treat (1.4) as a quadratic polynomial in the genuine physical scalar `X_0`. Its root discriminant divided by four is

`c K_t`, with

`K_t=(b^2-au)U^2-2avUV-awV^2+a t
    =(U,V)^T H_a(U,V)+a t`,                                    (5.1)

where

`H_a=[[b^2-au,-av],[-av,-aw]]`.                                (5.2)

A direct determinant expansion gives

`det H_a=a det Lambda`.                                         (5.3)

For fixed leaves, the density of the quadratic image of the cap-one scalar `X_0` is the sum over at most two roots. At either root the derivative magnitude is `2 sqrt(c K_t)`. Hence

`p_(Q|leaves)(t)
 <=c^(-1/2)(K_t)_+^(-1/2)
 <=c^(-1/2)|K_t|^(-1/2)`                                      (5.4)

where roots exist, and the conditional density is zero otherwise.

Now spend the actual projection-product information. The coefficient rows of `(U,V)` have leverage `<1/64<1/2`, so the diffuse-frame part of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` gives, for every nonsingular symmetric `H` and either signature,

`sup_s E |(U,V)^T H(U,V)-s|^(-1/2)
 <=4 sqrt(2e)|det H|^(-1/4).`                                  (5.5)

Apply (5.5) to `H=H_a` and `s=-a t`. Using (5.3)--(5.4),

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2e)c^(-1/2)(|a|D)^(-1/4).
`                                                                  (5.6)

This is the theorem `QFORM-NEARCOLOOP-SIGNFREE-PUNCTURED-OUTER-v1`. It has no Schur-sign restriction. In particular,

`|a|D>=2^(-12)
  => ||p_Q||_infinity
     <4 sqrt(2e)sqrt(64/63)*8
     =75.202439573290...<76.`                                  (5.7)

Thus the previous general `<1033` outer-pivot payment is sharpened by more than a factor thirteen in the actual B16 diffuse-transverse chamber, and it now follows from the same dependence-preserving projection mechanism on both signs.

Combining Sections 3 and 5, the only Rayleigh collar not paid by this run is

`0<|a|D<2^(-12).`                                               (5.8)

The endpoint `a=0` is paid separately by Section 3. The punctured collar (5.8) is exactly where the previously committed aggregate indefinite-pair/two-bank compiler is needed.

## 6. Why the zero-pivot argument cannot simply be continued to small nonzero `a`

The natural next idea would be to hope that a scalar conditional density cap and a two-dimensional marginal density cap, together with a fixed nonzero determinant, control every nonzero-pivot `3x3` quadratic. That interface is false. The following exact construction is useful because it prevents a mistaken perturbative closure of (5.8).

### Proposition `QFORM-NONZERO-PIVOT-CONDITIONAL-MARGINAL-CAPS-FALSE-v1`

For every `0<a<1`, there is a random vector `(Y,U,V)` such that

`||p_(U,V)||_infinity=1`,
`||p_(Y|U,V)||_infinity=1` almost surely,                       (6.1)

while the nonsingular quadratic matrix

`G_a=[[a,1,0],[1,0,0],[0,0,1]]`                                (6.2)

has

`det G_a=-1`,                                                    (6.3)

but the density of

`Q_a=aY^2+2UY+V^2`                                              (6.4)

satisfies

`||p_(Q_a)||_infinity>=4/(3a)`.                                 (6.5)

Hence no determinant-only extension of the zero-pivot conditional-trace theorem can follow from the two caps (6.1) when the pivot is nonzero, even arbitrarily small.

### Construction and proof

Set

`R_a=exp(4/a^(3/2))`.

Use parameters `p,q` with

`1<=p<=R_a`,
`a/(2p)<=q<=a/p`,                                               (6.6)

and map them to `(u,v)` by

`u=sqrt(a)(q-p)/2`,
`v=(p+q)/2`.                                                     (6.7)

The Jacobian in (6.7) is `sqrt(a)/2`, so the image set `E_a` has area

`|E_a|
 =sqrt(a)/2 * integral_1^(R_a) [a/(2p)] dp
 =a^(3/2) log(R_a)/4
 =1`.                                                           (6.8)

Let `(U,V)` have density `1_(E_a)`. Then its density cap is one. Conditional on `(U,V)=(u,v)`, let `Y` be uniform on the unit interval centered at `-u/a`:

`Y=-u/a+S`, `S~Unif[-1/2,1/2]`.                                (6.9)

This conditional density also has cap one.

The hyperbolic parametrization satisfies

`v^2-u^2/a=pq in [a/2,a]`.                                     (6.10)

Substituting (6.9) into (6.4),

`Q_a=aS^2+V^2-U^2/a`.                                          (6.11)

Therefore

`Q_a in [a/2,5a/4]` almost surely.                              (6.12)

The interval in (6.12) has length `3a/4`. Moreover `V>0` on `E_a`, so the gradient of the polynomial (6.4) is nonzero on the support; the coarea formula gives absolute continuity. Since its density has total mass one and is supported on an interval of length `3a/4`,

`||p_(Q_a)||_infinity>=4/(3a)`,                                 (6.13)

proving (6.5). QED.

This is **not** a counterexample to the owner QFORM conjecture: the constructed `(Y,U,V)` law is a deliberately dependent three-dimensional law and is not asserted to arise as the required projection/product image of independent cap-one original coordinates. It refutes only the tempting caps-only interface. In particular it explains why the remaining punctured collar must use the stronger original-product geometry recorded in the two-bank compiler; the term `acY^2` cannot be deleted merely because `a` is small.

## 7. Exact status and next implication

This run yields three durable conclusions.

1. `QFORM-NEARCOLOOP-CONDITIONAL-SHIFT-ZEROPIVOT-v1`: **PROVED**. The true near-coloop endpoint `a=0` has an essential density cap `<7.6`.
2. `QFORM-NEARCOLOOP-SIGNFREE-PUNCTURED-OUTER-v1`: **PROVED**. For `a!=0`, the B16 hard chamber obeys (5.6); in particular `|a|D>=2^-12` has essential density cap `<76` on both Schur signs.
3. `QFORM-NONZERO-PIVOT-CONDITIONAL-MARGINAL-CAPS-FALSE-v1`: **PROVED INTERFACE COUNTEREXAMPLE**. Conditional scalar cap plus two-dimensional marginal cap and fixed determinant do not control a nonzero-pivot indefinite quadratic uniformly.

The first unpaid exact-rank-three B16 implication is therefore sharply scoped:

`QFORM-PUNCTURED-ULTRACOLOOP-PRODUCT-RECEIVER-v2`:

> Under `0<|a|D<2^-12`, `c>63/64`, transverse leaf leverages `<1/64`, and the previously proved two-bank aggregate hyperbolic/Pluecker structure, exploit the genuine original-coordinate product provenance before taking any absolute curved trace. A proof may use the two balanced independent banks and the projected-crossing theorem, but it cannot replace them by only the caps `(6.1)` and cannot delete the small `aY^2` term.

Arbitrary additional spectrum remains a separate full-target interface after exact rank three. Full QFORM remains OPEN / NOT PROVED. Global continuity remains OPEN.

## 8. Finite verification

`CHECK.py` verifies the constants

- zero-pivot endpoint `<7.6`;
- sign-free threshold `<76`;
- direct designated-partner threshold `<1033`;
- the counterexample lower bound `4/(3a)`, including `5461.333...` at `a=1/4096`.

Committed `CHECK_OUTPUT.txt` ends `STATUS=PASS`.
