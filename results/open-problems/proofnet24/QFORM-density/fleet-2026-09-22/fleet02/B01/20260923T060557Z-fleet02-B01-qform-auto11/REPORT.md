SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T06:05:57Z.
attacking: convert the entire strict-N3 small-diagonal class into a uniform sub-half-Riesz / near-square-root small-ball estimate using aggregate off-diagonal frequency energy, then compare it with the newest local rank-two logarithmic receiver before any tiny packet is inverted.

# fleet02/B01 auto11 — global sub-half-Riesz currency for the small-diagonal target class

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Oscillatory replacement  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** not claimed from the new fractional-potential estimate.

## 1. Target and correction boundary

The unrestricted conjecture remains OPEN: for arbitrary dimension, independent real physical coordinates with densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential bound for the density of `Q=X^TAX`, or give a valid counterexample.

The phase-aligned fragmented-support construction still refutes every law-uniform scalar pointwise Fresnel decay claim. No rotated coordinate is declared independent. The new estimate is obtained only after averaging over original-coordinate product structure, and is a fractional-potential / distribution-function statement rather than a pointwise one-dimensional stationary-phase assertion.

The newest owner continuation also asks B01 specifically for a frequency-averaged bound on a remaining N3 class. The result below applies to the whole target class with small physical diagonals, hence in particular to the usual strict-N3 region before pair determinants are inspected.

## 2. Source-valid inputs actually used

### 2.1 Fleet01/B01 aggregate off-diagonal compiler, generalized here to all beta<1/2

The completed source is

`yspennstate/math-open-problems@21cf221fb1e8b99c99298fb11a0d5a41a8382aba`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B01/20260923T054511Z-fleet01-B01-qform-auto11b/REPORT.md`.

It proves at `beta=1/4` that, for

`R=X^T C X+b^T X+c`,
`F(C)=sum_(i!=j) C_ij^2`,

one has

`H_(1/4)(R):=sup_s E|R-s|^(-1/4) <= C_off F(C)^(-1/8)`,

`C_off=5.095453495355205...`.

Its proof records two ingredients valid for every `0<beta<1/2`: the mixed-order determinant/Brascamp-Lieb beta-Riesz compiler for a diffuse order-one minor law, and the aggregate one-row random-slope characteristic-function envelope for the heavy-row alternative. Section 3 below recombines those exact source inequalities at general beta.

### 2.2 Required newest Claude package

The required pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`

was reread together with its compatible current state. Its Theorem F is applied in Section 6 to the diffuse strict-N3 stress family, giving the actual joint-frequency inequality

`|phi(t)| <= (4pi)^(3/2) 2^(-1/2)|t|^(-3/2)`

and hence `||p_Q||inf<=12*2^(-1/3)`. This is a three-direction Brascamp-Lieb/Fresnel estimate, not scalar law-uniform pointwise decay.

### 2.3 Newest designated partner fleet03/B01

Partner source:

`yspennstate/math-open-problems@c65e53a795f4f47c223a21698549857342bd1b5f`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T052757Z-auto11/REPORT.md`.

For a three-original-coordinate center with rank-two cross block `K`, `Delta=sigma_1(K)sigma_2(K)>0`, kernel unit vector `v`, and transverse curvature `d=|v^T Bv|>0`, its logarithmic endpoint theorem gives

`||p_Q||inf <= (135e/32) Delta^(-1/2) [4+log_+(sqrt(Delta)/d)]`.

Section 6 applies this theorem to an exact packet of the previous B01 diffuse target family and compares it with the new aggregate currency.

## 3. New theorem: aggregate off-diagonal sub-half-Riesz family

### Theorem 3.1 — `QFORM-GLOBAL-OFFDIAG-SUBHALF-RIESZ-v1`

Let `C=C^T` be any real matrix, let `X_i` be independent real random variables with densities at most one, and permit an arbitrary affine term. Put

`R=X^T C X+b^T X+c`,
`F=F(C)=sum_(i!=j) C_ij^2`.

If `F>0`, then for every `0<beta<1/2`,

`boxed:
 H_beta(R):=sup_s E|R-s|^(-beta)
 <= C_beta F^(-beta/2),`

where

`C_beta = e^(beta/2)(4pi)^beta /
          [ beta(1-2beta) Gamma(beta) cos(pi beta/2) ].`             (3.1)

At `beta=1/4`, this gives exactly

`C_(1/4)=8 e^(1/8)(4pi)^(1/4)/[Gamma(1/4)cos(pi/8)]
       =5.095453495355205...`,

so Theorem 3.1 genuinely extends, rather than changes, the completed quarter-Riesz theorem.

### Proof

Choose a fair independent two-coloring of the physical coordinates and write its cross block as `M=C[I,J]`. Since an ordered off-diagonal entry lands in `I x J` with probability `1/4`, some cut has

`E1:=||M||_F^2 >= F/4`.                                               (3.2)

Use the natural order-one minor law

`omega(i,j)=M_ij^2/E1`

on nonzero entries. Its entropy-determinant currency is exactly `K(omega)=E1`.

**Diffuse-row case.** If every row occupancy is at most `1/2`, apply the source mixed-order beta-Riesz compiler with `kbar=1`. For every `beta<1/2`,

`H_beta(R)
 <= e^(beta/2)(2pi)^beta
    /[beta(1-2beta)Gamma(beta)cos(pi beta/2)]
    * E1^(-beta/2).`                                                (3.3)

Using (3.2), `E1^(-beta/2)<=2^beta F^(-beta/2)`, and (3.3) becomes (3.1).

**Heavy-row case.** If some row occupancy exceeds `1/2`, that row has Euclidean norm `rho` satisfying

`rho^2>E1/2`.                                                        (3.4)

Condition every other coordinate on its side of the cut. The completed aggregate random-slope theorem retains all induced quadratic and affine phases and gives

`|phi_R(t)| <= min(1, sqrt(pi C1/(rho |t|)))`,
`C1<=sqrt(2)`.                                                       (3.5)

The Riesz identity

`|x|^(-beta)= [Gamma(beta)cos(pi beta/2)]^(-1)
               int_0^infinity t^(beta-1) cos(tx) dt`

and (3.5) yield

`H_beta(R)
 <= (pi C1)^beta rho^(-beta)
    /[beta(1-2beta)Gamma(beta)cos(pi beta/2)].`                      (3.6)

Indeed, with `B=sqrt(pi C1/rho)`, the integral of
`t^(beta-1)min(1,B t^(-1/2))` is exactly

`B^(2beta)/[beta(1-2beta)]`.

Now (3.4), (3.2), and `C1<=sqrt(2)` give

`(pi C1)^beta rho^(-beta)
 <= (pi sqrt(2))^beta 2^(beta/2) E1^(-beta/2)
 <= (4pi)^beta F^(-beta/2).`                                       (3.7)

Thus the heavy-row constant is no larger than the diffuse-row constant in (3.1), because the latter has the extra harmless factor `e^(beta/2)`. This proves the theorem. QED.

The endpoint `beta=1/2` is deliberately excluded: both the exact integral and known one-row examples have the expected logarithmic divergence there.

## 4. Spectral conversion: the entire small-diagonal QFORM target has uniform sub-half-Riesz currency

### Theorem 4.1 — `QFORM-SMALL-DIAGONAL-SUBHALF-RIESZ-v1`

Let `A=A^T` satisfy the exact QFORM spectral hypothesis: at least three eigenvalues have absolute value at least one. Suppose

`max_i |A_ii| <= delta <1`.                                         (4.1)

Then for every admissible cap-one product input and every `0<beta<1/2`,

`boxed:
 H_beta(X^TAX)
 <= C_beta [3(1-delta)^2]^(-beta/2).`                              (4.2)

### Proof

Let `D=diag(A)`. Mirsky's singular-value inequality gives

`||A-D||_F^2 >= sum_j (s_j(A)-s_j(D))^2`.                          (4.3)

The target hypothesis says `s_1(A),s_2(A),s_3(A)>=1`, while every singular value of `D` is at most `delta`. Hence

`||A-D||_F^2 >=3(1-delta)^2`.                                      (4.4)

But

`||A-D||_F^2=sum_(i!=j)A_ij^2=F(A)`.                               (4.5)

Apply Theorem 3.1. QED.

This is a dimension-free full-target dichotomy: for any fixed `delta<1`, either a physical diagonal exceeds `delta` and one is in a pivot branch, or the entire form already has the averaged-frequency currency (4.2). In particular the usual strict-N3 regime with `max|A_ii|<=1/2` satisfies a universal bound for every exponent below `1/2`.

At `beta=1/4`, (4.2) gives the clean numerical estimate

`boxed: H_(1/4)(Q) <=5.2820217398...`                              (4.6)

whenever `max_i|A_ii|<=1/2`.

## 5. Optimizing beta: near-square-root small-ball control throughout strict N3

The family (4.2) is stronger than one fixed exponent. Assume `max|A_ii|<=1/2`. For `1/4<=beta<1/2`, use the elementary bounds

`beta Gamma(beta) >= e^(-1)`,
`cos(pi beta/2)>=1/sqrt(2)`,
`e^(beta/2)<=e^(1/4)`,
`(4pi)^beta<=2sqrt(pi)`,
`(3/4)^(-beta/2)<=(4/3)^(1/4)`.

Thus

`H_beta(Q) <= C_* /(1-2beta)`,                                    (5.1)

where

`C_* = e^(5/4) 2sqrt(2pi) (4/3)^(1/4)
     =18.8028082161... .`                                         (5.2)

For every `s` and `r>0`, Markov's inequality gives

`P(|Q-s|<=r) <= r^beta H_beta(Q)`.                                 (5.3)

If `0<r<=e^(-2)`, put `L=log(1/r)>=2` and choose

`beta=1/2-1/(2L)`.                                                 (5.4)

Then `1-2beta=1/L` and `r^beta=e^(1/2)sqrt(r)`. Hence

`P(|Q-s|<=r)
 <= C_* sqrt(e) sqrt(r) log(1/r)
 <31.01 sqrt(r) log(1/r).`                                        (5.5)

For `e^(-2)<r<=1` the trivial bound `1` is stronger. Therefore a convenient all-scale form is

`boxed:
 sup_s P(|Q-s|<=r)
 <= min(1, 31.01 sqrt(r) log(e/r)),
 0<r<=1,`                                                         (5.6)

for every exact-target matrix with `max_i|A_ii|<=1/2`.

This is the principal new oscillatory replacement of the run: strict N3 has a universal **near-square-root distribution-function estimate** even before any physical pair, local minor, hub, ridge, or rank-three cross packet is selected. It is not yet a density bound; the logarithmic/subcritical endpoint is precisely the remaining analytic-structural debt.

## 6. Designated partner applied: local logarithmic receiver still deteriorates on the diffuse strict-N3 family

Reuse the exact target-valid family from B01 r37 only as a stress test for the **new** partner theorem:

`A_m=uu^T-2vv^T+ww^T+m^(-1)I`, `m>=3`,

where `u,v,w` are normalized constant vectors on three disjoint size-`m` banks. Its three distinguished eigenvalues are

`1+1/m, -2+1/m, 1+1/m`,

and `max_i|A_ii|=2/m`. For `m>=4`, Theorem 4.1 and (5.6) therefore apply uniformly.

For the exact packet `I={U_1,U_2,V_1}` and `J` all remaining coordinates, r37 computed

`Delta^2 = 8(m-2)(m-1)/m^4`,
`d=1/m`.                                                           (6.1)

Applying the newest fleet03/B01 logarithmic theorem gives the valid density certificate

`||p_Q||inf
 <= (135e/32)
    * m/[8(m-2)(m-1)]^(1/4)
    * [4+log([8(m-2)(m-1)]^(1/4))].`                              (6.2)

This grows like `const * sqrt(m) log m`. Thus the new logarithmic analytic receiver greatly improves its predecessor's `m^(3/5)` power loss in the transverse curvature, but **no fixed local three-coordinate packet can become a uniform structural currency on this family**.

In contrast, the whole-matrix off-diagonal energy is exact:

`F(A_m)=6(m-1)/m`,                                                 (6.3)

so Theorem 3.1 gives, simultaneously for every `beta<1/2`, a uniform global fractional-potential bound. At `beta=1/4`,

`H_(1/4)(Q)<=C_off[6(m-1)/m]^(-1/8)<=4.2847485784`.                (6.4)

The required newest Claude Theorem F also applies directly to the same matrix written as

`A_m=[u v w] diag(1,-2,1)[u v w]^T +m^(-1)I`.

Its Gram matrix is `I_3` and every row leverage is `1/m<=1/2`, hence

`|phi_Q(t)| <=(4pi)^(3/2)2^(-1/2)|t|^(-3/2)`,
`||p_Q||inf <=12*2^(-1/3)=9.5244063118...`.                        (6.5)

Equations (6.2)-(6.5) identify the remaining proof obligation cleanly: aggregate frequency currency survives precisely where every fixed packet deteriorates, and diffuse joint Fresnel geometry can sometimes spend it all the way to density.

## 7. First unpaid implication

`QFORM-GLOBAL-SUBHALF-RIESZ-SPEND-v1`:

> In the small-diagonal / strict-N3 target class, starting from the universal near-square-root concentration estimate (5.6), prove a dimension-free product-preserving upgrade to bounded density, or route quantitatively to one of the already-paid joint Fresnel/volume/hub/ridge/grouped-square/exact-null/physical-pair receivers before selecting a reciprocal tiny local packet.

A mere endpoint passage `beta up to 1/2` is not available: the constants in Theorem 3.1 diverge like `(1-2beta)^(-1)`, and known one-row mechanisms genuinely have a logarithmic endpoint. The next step must therefore use an additional independent/grouped direction or a matrix-level routing argument, not an unchanged attempt at scalar pointwise decay.

## 8. Status

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The new theorem is a supporting averaged-frequency/distributional estimate and has not received two independent end-to-end reviews. It preserves every target quantifier used in its stated scope, including arbitrary fragmented/unbounded input supports and the original-coordinate product law.

MODEL: GPT-5.6 Sol  
THINKING LEVEL: UNKNOWN / not exposed  
THINKING USAGE: reasoning tokens and provider thinking time null/not exposed  
ELAPSED WORK: recorded separately in the run finish/receipt; wall execution is not pure thinking.
