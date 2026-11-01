# fleet01/B15 — generic countable core and finite-critical-trace normal form

Run: `20260923T033225Z-fleet01-B15-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **ESSENTIAL_STEP_APPLIED / GENERIC-COUNTABLE-CORE / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction discipline

The sole target remains: for independent real coordinates with densities `0<=f_i<=1` and real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite constant for the density of `Q=X^T A X`, or give a valid counterexample. Continuity is a separate stronger conclusion.

This run uses no law-uniform pointwise quadratic Fourier decay, no independence after spectral rotation, no arbitrary-joint rank-three coarea estimate, no positive moment of a worst conditional projection-density cap, and no projection/X-ray-only shortcut. The theorem below is a reduction of the exact sharp constant, not a declaration that a local pivot has a uniform size.

The starting point is the exact compact smooth-kernel normal form already proved in the immediately preceding fleet01/B15 report on current master,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260923T031931Z-fleet01-B15-QFORM-auto11/REPORT.md`.

Fix once and for all

`psi(u)=c exp(-1/(1-u^2)) 1_{|u|<1}`,

where `c` makes `int psi=1`. If `s(A)=s_3(A)` is the third largest eigenvalue modulus and `C_*` is the extended sharp target density constant, that report proves

`C_* = sup s(A) E psi(y-X^TAX)`                                      (1.1)

where the supremum is over all target instances and `|y|>=2`. It also proves that, for this positive bounded payoff, the source supremum is unchanged if every marginal is an indicator `1_{E_i}` of a measurable set of length one, and then by symmetric-difference approximation if every `E_i` is a bounded finite union of intervals. Equation (1.1) uses only absolute continuity plus Lebesgue differentiation; raw-output continuity is not a premise.

The completed assigned-partner result actually applied below is fleet02/B15,

`math-open-problems@00d696f70a758aa3e5c94dc1711f178ff03d9ebb`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T030440Z-fleet02-B15-QFORM-auto11/REPORT.md`.

Its Theorem 6.1 gives an ambient original-coordinate majority-sheet bound from any invertible indefinite physical `3 x 3` principal block. I apply it in Section 6 to the exact kernel functional, not merely as a citation.

## 2. Strongly generic rational matrices

Call a real symmetric `n x n` matrix **strongly physical-generic** if

1. every nonempty principal minor is nonzero; and
2. its spectrum is simple.

For fixed `n`, this class is open and dense in `Sym_n(R)`. Indeed, the failures are contained in the finite union of the algebraic hypersurfaces

`det A_{S,S}=0` for `empty != S subset {1,...,n}`

and the zero set of the characteristic-polynomial discriminant. None of these polynomials is identically zero: a diagonal matrix with distinct nonzero diagonal entries avoids all of them. Hence their union has empty interior. Since rational symmetric matrices are dense, strongly physical-generic rational symmetric matrices are dense as well.

The point is not that their principal minors are uniformly good; they can be arbitrarily small. The reduction below removes exact algebraic zero cases from the sharp problem, while leaving the genuinely hard **near-zero** geometry intact.

## 3. Exact countable-core theorem

### Theorem 3.1 — `QFORM-GENERIC-COUNTABLE-CORE-v1`

Let `G` be the following countable family of data, over all `n>=3`:

- `A in Sym_n(Q)` is strongly physical-generic and `s_3(A)>1`;
- `y in Q` with `|y|>2`;
- each `E_i` is a bounded finite union of pairwise disjoint intervals with rational endpoints and total length exactly one.

Then the sharp extended constant satisfies the exact identity

`boxed{
C_* = sup_{(A,y,E_1,...,E_n) in G}
      s_3(A) int_{E_1 x ... x E_n} psi(y-x^T A x) dx.
}`                                                                  (3.1)

In particular, if the full QFORM conjecture is false, there is a sequence of completely finite algebraic witnesses in `G` for which the right side tends to infinity.

### Proof

The `<= C_*` direction is immediate from (1.1): every datum in `G` is an admissible target instance, because `1_{E_i}` is a probability density bounded by one.

For the reverse direction, fix one datum from the finite-interval version of (1.1): a target matrix `A`, a center `|y|>=2`, and bounded finite unions of intervals `E_i` of length one. Set

`K=cl(E_1) x ... x cl(E_n)`.

This is compact. Write

`F(A,y,E)=s_3(A) int_{prod E_i} psi(y-x^T A x) dx.`

We show that `F` can be approximated arbitrarily well by data in `G`.

#### Step 1: create strict spectral margin

For `delta>0`, let

`A_delta=(1+delta)A`.

Then `s_3(A_delta)=(1+delta)s_3(A)>1`. Because `K` is compact,

`sup_{x in K}|x^T(A_delta-A)x| ->0`

as `delta->0`. The function `psi` is uniformly continuous and bounded, while `s_3(A_delta)->s_3(A)`. Therefore

`F(A_delta,y,E)->F(A,y,E)`.                                        (3.2)

Thus we may first move a target point an arbitrarily small amount into the strict open set `s_3>1`.

#### Step 2: generic rational approximation of the matrix

Fix a small `delta` for which the error in (3.2) is already below a prescribed tolerance. By density from Section 2, choose a rational strongly physical-generic symmetric matrix `B` with

`||B-A_delta||op < eta`.

For `eta` small enough, Weyl's eigenvalue inequality preserves `s_3(B)>1`. On `K`,

`|x^T(B-A_delta)x| <= eta sup_{x in K}|x|^2`,

so uniform continuity of `psi` gives

`int_{prod E_i} psi(y-x^T Bx)dx -> int_{prod E_i} psi(y-x^T A_delta x)dx`.

Also `s_3(B)->s_3(A_delta)`. Hence

`F(B,y,E)->F(A_delta,y,E)`.                                       (3.3)

#### Step 3: rationalize the center

Choose rational `y'` arbitrarily close to `y`, but outward if `|y|=2`, so that `|y'|>2`. Uniform continuity of `psi` gives

`F(B,y',E)->F(B,y,E)`.                                            (3.4)

#### Step 4: rationalize the product sets while retaining mass exactly one

A bounded finite union of intervals can be approximated in symmetric difference by a finite union `F_i` of disjoint rational-endpoint intervals. Its total length is rational and can be made arbitrarily close to one. If `|F_i|<1`, add a far disjoint rational interval of length `1-|F_i|`; if `|F_i|>1`, remove rational subintervals of total length `|F_i|-1`. The resulting rational-endpoint union still satisfies

`|F_i|=1`

and can be made arbitrarily close to `E_i` in symmetric difference.

Since all other factors have measure one and `psi` is bounded,

`| int_{prod E_i} psi(y'-x^T Bx)dx
   -int_{prod F_i} psi(y'-x^T Bx)dx |
 <= ||psi||infinity sum_i |E_i triangle F_i|.`                   (3.5)

Combining (3.2)--(3.5), every value in the exact finite-interval normal form is approximated arbitrarily well by a datum in `G`. Taking suprema proves (3.1). QED.

### Consequence 3.2 — exact-zero pivot cases are not a separate sharp obstruction

For purposes of proving or disproving the universal constant, one may assume **every physical principal block is nonsingular** and every scalar physical diagonal is nonzero. This does **not** allow division by a universal lower bound: the approximating principal minors may converge to zero. Thus the owner-identified zero/near-zero pivot problem reduces rigorously to the **near-zero** problem.

This is the useful distinction. An argument may perturb away an exact zero before a limiting passage, but it still must aggregate before paying a reciprocal quantity that can diverge along the approximating sequence.

## 4. Finite critical-value trace structure on the countable core

The reduction has an additional regularity payoff. Fix one core datum `(A,E_1,...,E_n)`. The product set is a finite disjoint union, up to boundaries, of bounded axis-parallel boxes. For one closed box `R`, consider every coordinate face `F` of `R`. If the free coordinate set of the face is `S`, the restriction of

`q(x)=x^T A x`

to the affine span of `F` has the form

`q_F(z)=z^T A_{S,S} z+2 b_F^T z+c_F`.                            (4.1)

By strong physical genericity, `A_{S,S}` is nonsingular whenever `S` is nonempty. Hence `q_F` has at most one critical point on the relative interior of `F`. For a vertex (`S=empty`) record its single value. Let `Sigma_R` be the finite set of all critical values of all face restrictions, and let `Sigma` be the finite union over the finitely many boxes.

### Proposition 4.1 — `QFORM-GENERIC-BOX-PIECEWISE-SMOOTH-v1`

For the product-indicator input from a core datum, the raw output law has a density `p_Q`, and

`boxed{ p_Q in C^infinity(R \ Sigma). }`                         (4.2)

No uniform bound on the derivatives, on `|Sigma|`, or on the spacing of `Sigma` is asserted.

### Proof

Absolute continuity follows already from the nonconstant-quadratic coarea argument. It remains to prove local smoothness away from `Sigma`.

Take a compact interval `J` disjoint from `Sigma`. For every point `x` in a box closure with `q(x) in J`, let `F` be the smallest coordinate face containing `x`. Since `J` contains no critical value of `q|_F`, the tangential differential of `q` along `F` is nonzero at `x`. In a manifold-with-corners chart respecting the coordinate faces, the implicit-function theorem therefore allows `q` itself to be used as one tangential coordinate, while the inward normal corner coordinates remain fixed half-line coordinates. After multiplying by a smooth partition of unity subordinate to finitely many such charts, Lebesgue measure takes the form

`a(t,z) dt dz`

with `a` smooth and compactly supported in the remaining local variables `z`. Integrating `a(t,z)` over those variables gives a `C^infinity` function of `t` on `J`. Summing the finitely many chart contributions and then the finitely many boxes proves (4.2). QED.

Thus on the exact sharp core, rough arbitrary measurable source laws have been replaced by a finite stratified trace problem: every individual density is smooth except possibly at finitely many face-critical output values. The number and geometry of those values are allowed to deteriorate along a bad sequence, so this proposition is not a universal modulus or a height bound.

## 5. Bounded density and continuity remain logically distinct

The generic reduction itself concerns the positive fixed kernel and needs neither a bounded nor continuous raw density. Proposition 4.1 gives only piecewise smoothness.

Separately, fleet02/B15's completed principal-pivot theorem (`20260922T120155Z-fleet02-B15-qform-r1`) gives, for every invertible physical `3 x 3` principal block `B`,

`||p_Q||infinity <= (2pi+3sqrt(3))/sigma_min(B)`.                (5.1)

On the present generic core every physical triple is invertible, so each fixed core instance has many finite matrix-dependent certificates of this form. Formula (5.1) does not become universal because `sigma_min(B)` may tend to zero simultaneously for every physical triple.

This cleanly separates the three regularity levels relevant to B15:

1. **absolute continuity:** automatic for a nonconstant quadratic under an absolutely continuous joint law;
2. **fixed-instance boundedness:** available on every target matrix from a finite physical pivot, but with matrix-dependent constants;
3. **universal boundedness:** still the open theorem and exactly the finiteness of (3.1).

Raw-density continuity is a fourth assertion; it is not used anywhere in Theorem 3.1.

## 6. Completed partner result applied to an actual kernel inequality

Now use the newest assigned-partner theorem at an equation.

Take any physical triple `S` in a core instance and set `B=A_{S,S}`. Strong genericity makes `B` invertible. Suppose first that `B` is indefinite. Let

`beta_S=sigma_min(B)>0`.

Condition on the outside original coordinates `W`. Completing the square in the three selected **original** coordinates gives

`Q=Z^T B Z+c(W)`,                                                  (6.1)

where the coordinates of `Z` remain independent translated cap-one variables. If `B` has signature `(2,1)`, define the majority event

`M_S={Z^T B Z>=0}`;

for signature `(1,2)`, reverse the sign and take `M_S={Z^T B Z<=0}`. Fleet02/B15 Theorem 6.1 proves that the corresponding output submeasure `nu_S(E)=P(Q in E, M_S)` satisfies

`nu_S <= C_B dt,      C_B<=pi sqrt(2)/beta_S`.                   (6.2)

Since `psi>=0` and `||psi||_1=1`, (6.2) gives the actual exact-kernel inequality

`boxed{
s_3(A) E[psi(y-Q) 1_{M_S}]
 <= pi sqrt(2) s_3(A)/beta_S.
}`                                                                 (6.3)

Therefore

`boxed{
s_3(A) E psi(y-Q)
 <= pi sqrt(2) s_3(A)/beta_S
    + s_3(A) E[psi(y-Q) 1_{M_S^c}].
}`                                                                 (6.4)

The second term is precisely the conditional minority/two-sheet contribution. Equation (6.4) is source-valid: the conditioning is on original independent coordinates, and the partner theorem already includes all outside quadratic coefficients, cross couplings, and induced affine terms.

For comparison, if a physical triple `B` is definite, every physical `2 x 2` principal subblock `D` of it is definite. The earlier completed fleet02/B15 definite-pair theorem gives the full-output bound

`s_3(A) E psi(y-Q)
 <= s_3(A)||p_Q||infinity
 <= pi s_3(A)/sqrt(|det D|).`                                    (6.5)

Hence on the generic core every triple falls into one of two rigorously paid forms:

- **definite triple:** the entire kernel functional is paid by (6.5), modulo the quantitative size of a physical pair determinant;
- **indefinite triple:** the majority-sheet part is paid by (6.3), and only the minority/two-sheet part remains.

There is no third singular-triple case in the exact sharp core.

Equivalently, for an indefinite triple let

`H_S^-(A,E;y)=E[psi(y-Q) 1_{M_S^c}]`.

Then every core instance obeys

`s_3(A)E psi(y-Q)
 <= inf_{S indefinite}
       {pi sqrt(2)s_3(A)/sigma_min(A_{S,S}) + s_3(A)H_S^-(A,E;y)}` (6.6)

whenever at least one indefinite triple is present, while any definite physical pair supplies (6.5).

This is a genuine application of the completed partner result to the exact full-target normal form. It does not assert a uniformly good triple and does not use generic X-ray control of `H_S^-`, which is forbidden by the live two-sheet correction.

## 7. What this changes in the proof map

The full sharp problem may now be attacked on a **countable, finite-box, strongly generic** core without loss. In particular:

- arbitrary rough source laws are not needed as primitive extremizing objects for the fixed-kernel formulation;
- exact zero physical pivots/principal minors may be removed before taking the sharp supremum;
- every core density has only finitely many possible nonsmooth face-critical output values;
- every indefinite physical triple has its majority-sheet kernel contribution already paid by the newest fleet02/B15 theorem;
- a definite physical pair pays the full kernel contribution directly.

What remains genuinely quantitative is unchanged in substance but sharper in formulation: a bad sequence must drive physical minors toward zero and/or retain large minority/two-sheet kernel mass across all useful indefinite triples, while evading the diffuse-volume, bank, hub and cross-block exits. Exact singular algebra is not the obstruction; **near-singular aggregate geometry is**.

The first unpaid implication after this run is therefore:

> On the countable generic core in Theorem 3.1, prove one universal bound for the minority terms in (6.4) after aggregating across physical triples/banks before paying reciprocal `sigma_min`, or force one of the existing diffuse-volume/definite-pair exits.

The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction means this cannot be done from a generic line/X-ray cap alone; the original product provenance must remain present.

## 8. Status

**Full QFORM: OPEN / NOT PROVED.**  
New proved structural result: exact sharp reduction to a countable strongly generic rational finite-box core, plus finite-critical-value piecewise smoothness on that core.  
Completed partner theorem applied at the central exact-kernel inequality: equations (6.3)--(6.4).  
Execution remains `WITHOUT_VERIFIED_BRAIN`; repository transport is not evidence of native learned-memory ingestion.
