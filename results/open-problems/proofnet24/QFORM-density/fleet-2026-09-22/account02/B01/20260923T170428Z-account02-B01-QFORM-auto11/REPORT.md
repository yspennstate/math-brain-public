SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B01, 2026-09-23T17:04:28Z.
attacking: the punctured near-null leakage logarithm left by account03/B01; spend one projected crossing direction at the residual half-Riesz level before restoring the outer scalar square.

# account02/B01 — one projected crossing plus one hub gives the exact half-Riesz currency needed by a scalar square peel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T170428Z-account02-B01-QFORM-auto11`  
Status: **PROVED SUPPORTING FULL-FORM ESTIMATE + STRICT-N3 TARGET FAMILY; FULL QFORM OPEN; CONTINUITY NOT CLAIMED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full target is unchanged: for independent original-coordinate real inputs with probability densities bounded by one and symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential-supremum density bound or give a valid counterexample. No moments, bounded/connected support, Gaussianity, log-concavity, identical laws, or independence after a rotation is used below.

The phase-aligned-density obstruction to any law-uniform scalar quadratic-phase pointwise decay is preserved. The proof below uses a joint original-coordinate projected crossing to obtain an **integrated frequency** estimate and then a half-Riesz potential. It never asserts pointwise scalar Fresnel decay.

## 1. Exact source inputs actually used

### 1.1 Required 20260922T211500Z Fourier package

At `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md` proves the two interfaces used here:

1. fractional potentials are controlled by the weighted Fourier integral `int |t|^(alpha-1)|phi(t)| dt`; and
2. if an original coordinate of coefficient `a!=0` is completed as

   `Q = a(X+h(V))^2 + R(V)`,

   then

   `||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`,

   where `H_(1/2)(R)=sup_s E|R-s|^(-1/2)`.

The exact Fourier constant at `alpha=1/2` is rederived below rather than imported.

### 1.2 Current projected-crossing theorem

At `yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, the grouped-hub theorem proves that for

`R = F(Y)+2Y(ell dot Z+beta)+H(Z)`

with `Y` one original coordinate, after a split `Z=Z_I union Z_J`, putting

`C = M_(I,J)(I-Pi_row(ell_J))`,

where `M` is the quadratic matrix of `H`, if `ell_J!=0`, `Z1=||C||_F^2>0`, and every row weight

`alpha_i=||C_(i,*)||_2^2/Z1 <=1/2`,

then its `k=1`, projected-volume `ell_volume=1` case gives

`|phi_R(t)| <= min(1, 2 pi (||ell_J||_2 ||C||_F)^(-1/2) |t|^(-1))`.       (1.1)

The source only needs the projected row-volume hypothesis; `H` may have arbitrary internal curvature and linear terms, and `F` may be arbitrary.

### 1.3 Designated partner account03/B01

The newest completed designated-partner report read in this run is

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T163050Z-auto11/REPORT.md`

at the current mathematical repository state. In its scalar-completed near-null leakage branch,

`R = delta Y^2 + 2Y(ell dot Z+beta)+H(Z)`,

and, with `W2` the overlap-two physical-pair currency, it proves

`sum_(k!=l) ell_k^2 ell_l^2 >= W2/(4a^2)`                       (1.2)

and hence

`||ell||_2 >= W2^(1/4)/(sqrt(2)|a|^(1/2))`.                     (1.3)

It also proves a full-Q signed-Fejer estimate with only one remaining logarithm. That logarithm is precisely what the new compiler below removes whenever one projected crossing direction survives transverse to `ell`.

## 2. Main theorem

### Theorem 2.1 — `QFORM-ONE-HUB-ONE-CROSS-HALFRIESZ-PEEL-v1`

Let one original coordinate be scalar-completed with coefficient `a!=0`:

`Q = a(X+h(Y,Z))^2 + R(Y,Z)`,                                   (2.1)

where `X` is independent of the original-coordinate tuple `(Y,Z)` and

`R = delta Y^2 + 2Y(ell dot Z+beta) + Z^T M Z + q dot Z + c`.    (2.2)

Split the original light coordinates as `Z=(Z_I,Z_J)`. Assume

`ell_J != 0`,

and define the projected crossing

`C = M_(I,J)(I-Pi_row(ell_J))`.                                  (2.3)

Suppose

`C != 0`,
`max_(i in I) ||C_(i,*)||_2^2 <= (1/2)||C||_F^2`.                (2.4)

Then the full original quadratic form has a density satisfying

`boxed:`
`||p_Q||_infinity <= 8 |a|^(-1/2) (||ell_J||_2 ||C||_F)^(-1/4)`. (2.5)

There is no reciprocal power of `delta`, the determinant of the corresponding physical pair, or its smallest singular value. No continuity claim is made.

#### Proof

Put

`P = ||ell_J||_2 ||C||_F`.                                       (2.6)

Apply the current grouped projected-crossing theorem to the residual (2.2), taking the original coordinate `Y` as the one-dimensional hub. Its density is bounded by one, so the source parameter `M_H<=1`. For projected volume one, `Z1=||C||_F^2`, the row marginals are exactly those in (2.4), and the singular-value product of the hub slope on the `J` side is `||ell_J||_2`. The source constant therefore reduces to

`K = 2 pi P^(-1/2)`,

and

`|phi_R(t)| <= min(1,K/|t|)`.                                   (2.7)

For the Fourier convention `hat f(t)=int exp(itx)f(x)dx`,

`hat(|x|^(-1/2))(t)=sqrt(2pi)|t|^(-1/2)`.

By the standard regularised Riesz-potential argument used in the required Fourier package,

`H_(1/2)(R)`
` <= (2pi)^(-1/2) int_R |t|^(-1/2)|phi_R(t)| dt`.                (2.8)

The right side is finite by (2.7). Splitting at `|t|=K`,

`int_R |t|^(-1/2) min(1,K/|t|) dt`
` = 2 int_0^K t^(-1/2)dt + 2K int_K^infinity t^(-3/2)dt`
` = 8 sqrt(K)`.                                                   (2.9)

Since `sqrt(K)=sqrt(2pi)P^(-1/4)`, (2.8)-(2.9) give the exact convenient endpoint

`boxed: H_(1/2)(R) <= 8 P^(-1/4)`.                               (2.10)

Finally apply the required source's scalar square peel to (2.1):

`||p_Q||_infinity <= |a|^(-1/2) H_(1/2)(R)`.

Substitution of (2.10) is exactly (2.5). QED.

### Why this is the right endpoint

The projected-crossing source requires `k+ell_volume>2` for a **direct density** bound. Here `k=1` and `ell_volume=1`, so the residual only has borderline `|t|^(-1)` decay and the direct `L1_t` route fails logarithmically. But the outer scalar square needs only `H_(1/2)`, whose Fourier weight is `|t|^(-1/2)`; the same `|t|^(-1)` tail is then integrable. Thus an apparently subcritical projected-crossing packet becomes exactly sufficient when spent at the half-Riesz level before the outer square is restored.

## 3. Concrete use of the newest account03/B01 leakage currency

Assume in addition the partner leakage alternative (1.2). If a split satisfies

`||ell_J||_2 >= theta ||ell||_2`, `0<theta<=1`,                  (3.1)

then (1.3) and (2.5) imply

`boxed:`
`||p_Q||_infinity`
` <= 8*2^(1/8) theta^(-1/4) |a|^(-3/8) W2^(-1/16) ||C||_F^(-1/4)`.  (3.2)

Indeed

`||ell_J||_2 ||C||_F`
` >= theta W2^(1/4) ||C||_F /(sqrt(2)|a|^(1/2))`,

and (3.2) follows by taking the negative quarter power and multiplying by `8|a|^(-1/2)`.

Equation (3.2) is an actual application of the newest designated-partner result: in the punctured near-null leakage branch it removes the partner's signed-Fejer logarithm whenever one spread projected crossing direction is quantitatively present. The determinant and `sigma_min(B)` do not appear.

## 4. Strict-N3 target family paid uniformly at 8

This family shows that the new compiler is not merely a bounded-dimensional pivot restatement. Fix

`0<eps<=1/4`, `0<nu<=1`,

and an even integer `m`. Let `e,q,w in R^m` be unit vectors with

`e_j=1/sqrt(m)`,
`w_i=1/sqrt(m)`,
`q_j=+1/sqrt(m)` on half the coordinates and `-1/sqrt(m)` on the other half,

so `e perp q`.

On original coordinates ordered as

`x, y, U in R^m, V in R^m`,

let

`A_(eps,nu,m) =`

`[ eps      0          0                 0               ]`
`[ 0       eps nu      0                 eps^(-1)e^T     ]`
`[ 0        0          0                 eps^(-1)w q^T   ]`
`[ 0       eps^(-1)e   eps^(-1)q w^T     0               ]`.     (4.1)

### 4.1 Target spectrum

The active subspaces are orthogonal. Besides the eigenvalue `eps` and zeros, the spectrum contains

`lambda_+/- = [eps nu +/- sqrt(eps^2 nu^2 + 4 eps^(-2))]/2`,

and

`+eps^(-1), -eps^(-1)`.                                         (4.2)

For `eps<=1/4`,

`min(|lambda_+|,|lambda_-|) >= eps^(-1)-eps nu/2 >1`,

and `eps^(-1)>1`. Therefore the matrix has at least four eigenvalues of modulus at least one for every `m` and every `0<nu<=1`.

### 4.2 Strict N3

Given any fixed no-pivot threshold `tau in (0,1]`, choose

`eps < min(tau,1/4)`

and then even

`m > 1/(tau eps^2)`.                                             (4.3)

Every physical diagonal has magnitude at most `eps<tau`. The only nonzero physical two-coordinate determinant scales are

`eps^2 nu`,
`1/(eps^2 m)`,
`1/(eps^2 m^2)`,                                                  (4.4)

coming respectively from `(x,y)`, `(y,V_j)`, and `(U_i,V_j)`. By (4.3), all are below `tau`. Thus (4.1) lies in strict N3 while `nu` may tend to zero through nonzero values.

### 4.3 The near-null physical pair and projected crossing

Use the physical pair `{x,y}`:

`B=diag(eps,eps nu)`,
`|det B|=eps^2 nu`,
`sigma_min(B)=eps nu`.                                           (4.5)

So this is genuinely punctured near-null as `nu ->0+`.

Scalar-complete `x`. There are no `x`-light couplings, so the residual is already

`R = eps nu Y^2 + 2 eps^(-1)Y <e,V> + 2 eps^(-1)<w,U><q,V>`.     (4.6)

Take `Y=y` as the original hub and split the light variables as `I=U`, `J=V`. Then

`ell_J=eps^(-1)e`,
`C=eps^(-1)w q^T`,                                               (4.7)

because `q perp e`. Hence

`||ell_J||_2=eps^(-1)`,
`||C||_F=eps^(-1)`,
`alpha_i=w_i^2=1/m<=1/2`.                                       (4.8)

Theorem 2.1 gives

`||p_(X^T A_(eps,nu,m) X)||_infinity`
` <= 8 eps^(-1/2)(eps^(-2))^(-1/4)`
` = 8`.                                                          (4.9)

This bound is uniform in `eps`, `nu`, `m`, and in every admissible product input law.

### 4.4 The designated partner's leakage branch really applies

For the pair (4.5), the partner's scalar-completed `a=eps`, `delta=eps nu`, and `ell=eps^(-1)e`. Its exact overlap-two identity gives

`W2`
` = eps^2 [eps^(-4)(1-1/m) + 2 nu^2]`
` = eps^(-2)(1-1/m) + 2 eps^2 nu^2.                              (4.10)

The leakage side is

`sum_(k!=l) ell_k^2 ell_l^2 = eps^(-4)(1-1/m)`.                 (4.11)

For `eps<=1/4`, `nu<=1`, `m>=2`,

`eps^(-4)(1-1/m) >= W2/(4eps^2)`,                               (4.12)

so the newest account03/B01 leakage alternative is indeed the active one.

Its full-Q Fejer theorem gives only

`D_T law(Q)(s)`
` <= 20 sqrt(2) eps^(-1/4) W2^(-1/8)`
`    [1+log_+(sqrt(T)/H0)]`,                                    (4.13)

with `H0=4sqrt(2)eps^(1/4)W2^(-1/8)`. Since `W2` is asymptotic to `eps^(-2)`, the prefactor in (4.13) stays order one but the displayed upper bound still grows logarithmically with `T`; it therefore cannot itself yield a uniform density bound through the partner's Fejer equivalence. Equation (4.9) removes that logarithm by spending the transverse projected crossing before the outer square peel.

## 5. Exact remaining implication

This run pays the punctured near-null leakage class whenever, after the first scalar completion, there is a split carrying a nontrivial portion of the random slope and **one** projected light-crossing direction with row weights at most `1/2`.

The first unpaid implication is therefore sharpened to:

`QFORM-NEARNULL-ZERO-OR-HEAVY-PROJECTED-CROSSING-ROUTING-v1`.

In a surviving near-null leakage state, for every split `I,J` with substantial `||ell_J||`, either

1. `C=M_(I,J)(I-Pi_row(ell_J))` has zero/tiny Frobenius norm, or
2. its one-volume law is concentrated in a row of weight `>1/2`.

One must route those zero/heavy projected-crossing states to the completed exact-singular random-slope, mixed-hub, heavy-row/single-hub, volume, grouped-square, or other paid receivers without paying a reciprocal tiny physical-pair singular value. A pure or nearly pure slope-star is the natural borderline obstruction to the new compiler because then `C` is zero after projection. This is a genuine smaller structural debt; no full-Q proof is claimed.

## 6. Scope and correction safety

- No post-rotation independence is used. All conditioning/projections act through source-valid original-coordinate product estimates.
- No moment, support diameter, convexity, Gaussianity, or log-concavity assumption is introduced.
- The phase-aligned-density refutation remains intact: the only frequency decay used is the joint `|t|^-1` estimate obtained from one original hub plus one projected crossing direction.
- The outer scalar square is not assigned a false pointwise Fresnel bound; it is restored only after the residual half-Riesz potential is finite.
- Small matrix norm is never treated as a uniformly small random quadratic perturbation.
- Full QFORM remains open and no continuity statement is inferred from the half-Riesz peel.
