# account03/B11 — universal quarter-Riesz control from one large eigenvalue, and a Schur-chain reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T161210Z-account03-B11-QFORM-r13`  
**Assignment:** Indefinite signatures  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction boundary

The sole owner target is the following. For arbitrary dimension, independent real coordinates with one-dimensional probability densities bounded by one, and a real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove that `X^T A X` has an essentially bounded density with one universal finite constant, or give a valid counterexample. Continuity is a separate strengthening.

This run keeps the original-coordinate product structure throughout. It does not use law-uniform pointwise scalar Fresnel decay, post-rotation independence, naive fiber suprema, a fixed good principal minor, or a conditional-cap-implies-independence shortcut.

The first essential implication attacked is the heavy physical-square branch left by the current spectral-window reduction. The new input is a universal **quarter-order Riesz-potential theorem for every quadratic form having only one large singular direction**. It converts a second genuine scalar pivot into a bounded half-potential without paying a third spectral direction.

## 2. Source-pinned completed inputs

1. **Assigned partner `account04/B11`.** Canonical report
   `yspennstate/math-open-problems@44e7ab6750fbc3dccd77f1dd9e8bdba0bba2f0f5`,
   path
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260922T161514Z-b11-cone-trace-r1/REPORT.md`.
   It proves the exact cone-trace formula for signature `(+,+,-)` and, at the exact null-heavy product endpoint with one physical Parseval row `(1,0,0)`,
   `||p_Q||_infinity <= 6 e^(2/3) < 11.687`.
   It also proves that a mere `L^infinity` cap on an arbitrary 3D projected density cannot control the cone trace.

2. **Ridge quarter-Riesz splice.** account01/B01,
   canonical report visible at
   `yspennstate/math-open-problems@1bc95193312b70572b2765529ac3b6d98e3fe754`,
   path
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260922T160919Z-b01-qform-auto11d/REPORT.md`.
   Under a physical cross block with ridge operator
   `K_gamma=BB^T(gamma^2 I+BB^T)^(-1)`, effective dimension `theta=tr K_gamma`,
   and `max diag K_gamma<=q/2`, the source characteristic envelope gives a finite
   quarter-Riesz integral as soon as `theta>q/2`.

3. **Spectral-window/MSS localization package.** account03/B12,
   `yspennstate/math-open-problems@2bd58d21cf8eda48d6451469ceaf5fb8dc19bf5`,
   path
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T154709Z-qform-window-r12/REPORT.md`.
   In particular, at spectral cutoff `tau` and high-subspace leverage `eps`,
   `delta=1/2-eps-sqrt(2eps)`, an MSS partition gives two restricted frame Gramians
   bounded below by `delta I`; a tail of operator norm at most `tau` perturbs the
   cross block by at most `tau`; and the ridge leverage obeys the supplied
   range-plus-tail estimate.

4. **Aggregate quarter-Riesz cross theorem.** account01/B04,
   path
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B04/20260922T154611Z-account01-B04-QFORM-r13/REPORT.md`.
   For a physical cross block `C`, if one side has ordinary range leverage at most
   `1/2`, then
   `sup_u E|R-u|^(-1/4) <= K_11 ||C||_F^(-1/4)`
   with `K_11=3.663273516008612...`.

5. **Indefinite binary half-potential.** this slot's earlier proved theorem,
   `yspennstate/math-open-problems@860d849b7f2e0198bf7c3531a71b14e59f03e430`,
   path
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T121353Z-account03-B11-QFORM-r11/REPORT.md`.
   For independent cap-one `X,Y` and any affine indefinite binary quadratic with
   `Delta=b^2-ad>0`,
   both one-sided half-potentials are bounded by `8 Delta^(-1/4)`.

6. **Square-to-quarter reduction.** account03/B05,
   `yspennstate/math-open-problems@bf7bff5c9b11cf495ccbcb09ef48549fd9c0d409`,
   path
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/account03-B05-20260922T133738Z-qform-r12/REPORT.md`.
   For an original independent coordinate,
   `E_X |v-a(X+m)^2|^(-1/2)
      <= 4 sqrt(2) |a|^(-1/4)|v|^(-1/4)`,
   uniformly in the shift.

The free-regularizer/ridge analytic multiplier has a scoped independent PASS from account02/B02. The separate MSS/window perturbation package is used at its stated source status and is not promoted beyond that provenance.

## 3. A scale-covariant one-large-direction theorem

For a symmetric matrix `S`, put

`H_(1/4)(S) = sup_t E |t-X^T S X|^(-1/4)`.

### Theorem 3.1 — `QFORM-ONE-EIGEN-QUARTER-RIESZ-v1`

If `s_1(S)>=sigma>0`, then

`boxed( H_(1/4)(S) <= 25 sigma^(-1/4). )`                 (3.1)

The inputs are arbitrary independent cap-one coordinates. There is no sign,
moment, support, rank, or diagonal-basis assumption.

It suffices by scaling to prove the theorem for `s_1(S)>=1`.

### 3.1 Diffuse spectral-window branch

Let `tau=1/64` and let `P` project onto **all** eigenspaces of `S` with
`|lambda|>=tau`. Assume

`max_i P_ii <= 1/32`.                                       (3.2)

Write `S=S_H+E`, `||E||op<=tau`. With `eps=1/32`, the MSS frame partition from
the completed window package gives

`delta=1/2-eps-sqrt(2eps)=7/32`.                            (3.3)

For the high-window physical cross block `B_0`, one has

`s_1(B_0)>=delta s_1(S_H)>=7/32`.

For the full cross block `B=B_0+E[I,J]`,

`s_1(B)>=sigma_0:=delta-tau=13/64`.                         (3.4)

Moreover the range projection of `B_0` on the chosen side has diagonal at most

`eps/delta=1/7`.

Take

`gamma=sigma_0/sqrt(2)=13/(64 sqrt(2))`.                    (3.5)

The ridge perturbation estimate therefore gives

`max_i (K_gamma)_ii
 <= (1/sqrt(7)+tau/gamma)^2
 = (1/sqrt(7)+sqrt(2)/13)^2
 < 0.237 < 1/2`.                                            (3.6)

The top singular direction contributes

`theta=tr K_gamma >=
 sigma_0^2/(gamma^2+sigma_0^2)=2/3`.                        (3.7)

Thus for `q=1`, the source ridge envelope has exponent

`beta=theta/2 >= 1/3 > 1/4`.

Write
`L_1=pi e sqrt(2)` and
`t_0=[L_1/(2gamma)] D^(-1/(2theta))`.
The source envelope is

`|phi_R(t)| <= min(1,(t_0/|t|)^beta)`.

The exact quarter-Riesz Fourier identity gives, with
`c_(1/4)=Gamma(3/4)sin(pi/8)/pi`,

`H_(1/4)(S)
 <= c_(1/4) int_R |t|^(-3/4)|phi_R(t)|dt`.

Direct integration and `beta>=1/3` yield

`int_0^infinity t^(-3/4) min(1,(t_0/t)^beta) dt
 <= 16 t_0^(1/4)`,

hence

`H_(1/4)(S)
 <= 32 c_(1/4) [L_1/(2gamma)]^(1/4)
 < 12.164.`                                                  (3.8)

No ordinary `L^1` Fourier inversion is used.

### 3.2 High spectral-leverage branch

Assume (3.2) fails. Then for some original coordinate `i`,

`||S e_i||_2^2
 >= tau^2 P_ii
 > 1/(64^2*32)
 = 1/131072`.

Therefore

`||S e_i||_2 > 1/(256 sqrt(2))`,                              (3.9)

and, writing the physical row as `(a,b^T)`, either

`|a|>eta` or `||b||_2>eta`,   where `eta:=1/512`.              (3.10)

#### Case A: a heavy diagonal

If `|a|>eta`, complete the square in the original coordinate `X_i`.
The cap-one square quarter-kernel bound gives, conditionally on all other
coordinates,

`E_X |u-a(X+m)^2|^(-1/4)
 <= 2^(7/4)|a|^(-1/4)`.

Averaging gives

`H_(1/4)(S) <= 2^(7/4) eta^(-1/4)=16`.                       (3.11)

#### Case B: a heavy diffuse off-diagonal bank

Assume `|a|<=eta`, `||b||>eta`, and

`max_j b_j^2/||b||^2 <= 1/2`.                                 (3.12)

Use the physical cut with one side `{i}` and the other side the bank of
remaining coordinates. On the bank side, the range projection of the rank-one
cross block `b^T` has diagonal exactly `b_j^2/||b||^2`, so the completed
`q=1,k=1` aggregate quarter-Riesz theorem applies to the **full** quadratic form,
including arbitrary self blocks. Hence

`H_(1/4)(S)
 <= K_11 ||b||^(-1/4)
 < 3.663274 * 512^(1/4)
 < 17.426.`                                                   (3.13)

#### Case C: a heavy localized off-diagonal coefficient

Assume instead

`rho:=max_j b_j^2/||b||^2>1/2`.

Choose `j` with `c:=S_ij` satisfying

`|c|>||b||/sqrt(2) > eta/sqrt(2)`.                             (3.14)

Put `d=S_jj`.

If `|d|>=|c|/2`, the single-coordinate square quarter-kernel bound on coordinate
`j` gives

`H_(1/4)(S)
 <=2^(7/4)|d|^(-1/4)
 <=2^(7/4)(2sqrt(2)/eta)^(1/4)
 <20.750.`                                                    (3.15)

If `|d|<|c|/2`, consider the physical binary block

`H=[[a,c],[c,d]]`.

Since `|a|<=eta<=sqrt(2)|c|`,

`Delta=c^2-ad
 >=c^2-|a||d|
 > (1-1/sqrt(2)) c^2 >0`.                                    (3.16)

So the block is quantitatively indefinite. Condition on all outside original
coordinates. They create only affine terms in this physical pair. The earlier
B11 theorem gives each one-sided inverse-half potential at most
`8 Delta^(-1/4)`, hence

`E |u-Q_H|^(-1/2) <=16 Delta^(-1/4)`.

Cauchy-Schwarz then gives

`E |u-Q_H|^(-1/4) <=4 Delta^(-1/8)`.

Therefore

`H_(1/4)(S)
 <=4(1-1/sqrt(2))^(-1/8)|c|^(-1/4)
 <24.192.`                                                    (3.17)

The four branches (3.8), (3.11), (3.13), (3.15)-(3.17) prove (3.1) with the
round constant `25`. Rescaling proves the stated `sigma^(-1/4)` dependence.
QED.

## 4. Exact Schur spectral inheritance

The new quarter theorem becomes target-relevant because a genuine physical
scalar pivot loses **exactly one** singular direction and no more.

### Lemma 4.1 — rank-one Schur inheritance

Write a symmetric matrix in original coordinates as

`A=[[a,b^T],[b,C]]`, `a!=0`,

and put

`S=C-bb^T/a`.

Then

`A-diag(0,S)
 = a^(-1) [a;b][a,b^T]`,                                    (4.1)

which has rank one. Therefore the rank-perturbation singular-value inequality
gives

`s_(k+1)(A) <= s_k(S)` for every admissible `k`.              (4.2)

In particular, under the owner target `s_3(A)>=1`,

`boxed( s_2(S)>=1. )`                                        (4.3)

This is exact and dimension-free. It does not assert that a fixed principal
rank-two block of `S` is good.

## 5. Consequence for the current heavy physical-square branch

The account03/B12 full-target dichotomy says that either the global
`|lambda|>=1/39` spectral window is diffuse, in which case the full density is
already continuous and `<66.546`, or there is an original coordinate with

`|A_ii|>1/312` or `||A_{-i,i}||_2>1/312`.                     (5.1)

Consider the **scalar-pivot** subbranch `|a|=|A_ii|>1/312`.
Complete that original coordinate:

`Q=a(X_i+m(Y))^2+Y^T S Y`,                                   (5.2)

with the exact Schur complement `S`. Lemma 4.1 gives `s_2(S)>=1`.

Run the same `tau=1/64`, `eps=1/32` spectral-window test on `S`.

### 5.1 If the two-direction residual window is diffuse

The MSS/window calculation now gives a physical residual cross block with

`s_2(B)>=13/64`.

Take `gamma=(13/64)/2=13/128`. Then

`theta>=2/(1+1/4)=8/5`

and

`max diag K_gamma
 <=(1/sqrt(7)+2/13)^2
 <0.283<1/2`.

Apply the completed square-assisted ridge theorem with `q=1`. Using its coarse
constant and `|a|>1/312` gives

`boxed( ||p_Q||_infinity < 702. )`                             (5.3)

This branch proves absolute continuity and essential boundedness. Continuity is
not claimed from this shifted-square route.

### 5.2 If the residual window has high physical leverage

There is an original residual row `(c,d^T)` with

`|c|>1/512` or `||d||_2>1/512`.                                (5.4)

If `|c|>1/512`, complete this second original-coordinate square. Its Schur
remainder `T` satisfies `s_1(T)>=s_2(S)>=1` by Lemma 4.1. The completed
square-to-quarter inequality and Theorem 3.1 give

`sup_t E|t-Y^T S Y|^(-1/2)
 <=4sqrt(2)|c|^(-1/4) H_(1/4)(T)
 <673.`                                                        (5.5)

The outer square in (5.2) then yields

`boxed( ||p_Q||_infinity < 11883. )`                           (5.6)

Thus a second heavy scalar pivot is now completely paid with no third large
spectral direction and no fixed principal triple.

If instead the residual heavy row is off-diagonal dominated and one coefficient
carries more than half of the bank energy, the same physical two-coordinate
argument as Section 3.2 applies. Either the partner diagonal is itself a paid
second scalar pivot, or the pair is quantitatively indefinite and the earlier
B11 binary half-potential theorem directly pays the residual one-sided
half-potential. The latter gives, at the thresholds above, a full density bound
`<5169`.

The only second-level branch not paid by this run is therefore:

> `QFORM-SCHUR-DIFFUSE-STAR-HALF-ENDPOINT-v1`: after a first physical scalar
> pivot `|a|>1/312`, the Schur complement has `s_2(S)>=1` and contains a
> high-window physical row with small diagonal but an off-diagonal bank of norm
> `>1/512` whose normalized coefficients all have squared size at most `1/2`.

This is a genuine rank-one-cross **half-Riesz endpoint**. The regularized
determinant alone gives the critical `|t|^(-1/2)` tail there, so absolute
Fourier integration is logarithmically borderline. It is substantially narrower
than the previous generic heavy-row branch.

## 6. Assigned partner account04/B11 applied

The assigned partner's new cone-trace theorem is directly relevant to the
surviving endpoint. It proves that an arbitrary bounded 3D projected density can
concentrate in a thin tube around the light cone and make the signature
`(+,+,-)` output density arbitrarily large; therefore the remaining star branch
cannot be closed by a projection-cap-only argument.

On the other hand, in the exact product-provenance null-heavy endpoint

`Q=2 Z_1 Z_3 + Z_2^2`

with a physical Parseval row exactly `(1,0,0)`, the partner proves the actual
inequality

`boxed( ||p_Q||_infinity <= 6 e^(2/3) < 11.687. )`             (6.1)

Negating the form gives the dual `(+,-,-)` case. Thus the exact null-heavy
terminal of the surviving star branch is already paid; what remains is the
overlapping-support / extra-self-block transport from the general Schur star to
that product cone-trace endpoint (or an alternative aggregate payment).

This is an actual use of the assigned partner result, not a citation-only
attribution.

## 7. Why the third direction removes the opposite-sign logarithm

The opposite-sign rank-two control remains unchanged: `XY` or `X^2-Y^2` can
have a logarithmically unbounded density near the cone tip under admissible
bounded densities.

The new theorem identifies a robust hierarchy.

1. One large quadratic direction does **not** force a bounded output density,
   but it does force a bounded quarter-Riesz potential, uniformly:
   `H_(1/4)<=25 s_1^(-1/4)`.
2. A genuine additional physical square converts that quarter-potential into a
   bounded half-potential by the square-to-quarter inequality.
3. A third genuine physical square converts that half-potential into an
   essentially bounded density.

The fleet's ridge and binary-indefinite mechanisms let the first two stages be
implemented without diagonalizing the input law. This is the precise smoothing
currency by which the third direction removes the rank-two logarithmic
singularity in the paid branches.

## 8. Continuity status

The new one-eigenvalue theorem is a Riesz-potential statement, not a density
statement. The target branches closed through shifted-square coarea prove
absolute continuity and an essentially bounded density. They do **not** by
themselves prove that this density has a continuous representative.

The global diffuse ridge branch from account03/B12 does prove a continuous
`C_0` density. The assigned partner exact null-heavy endpoint also proves a
continuous density. Continuity for the newly closed Schur-chain branches remains
open.

## 9. Status

**Proved in this run:**

- `QFORM-ONE-EIGEN-QUARTER-RIESZ-v1`, with universal constant `25`;
- exact rank-one Schur spectral inheritance `s_3(A)<=s_2(S)`;
- closure of the first-heavy-scalar / residual-diffuse-two-direction branch;
- closure of the first-heavy-scalar / second-heavy-scalar branch using the new
  quarter theorem;
- closure of the localized residual off-diagonal pair by either a second scalar
  pivot or the earlier binary indefinite half-potential;
- explicit application of the assigned `account04/B11` null-heavy cone result.

**Still open:**

- the diffuse off-diagonal Schur-star half-Riesz endpoint described above;
- the first-level heavy off-diagonal branch in (5.1) when no scalar pivot is
  available;
- the full arbitrary-dimensional QFORM conjecture;
- continuity in the new Schur-chain branches.

No novelty claim is made. Repository retrieval is not authenticated native brain
receiver use; status remains `WITHOUT_VERIFIED_BRAIN`.
