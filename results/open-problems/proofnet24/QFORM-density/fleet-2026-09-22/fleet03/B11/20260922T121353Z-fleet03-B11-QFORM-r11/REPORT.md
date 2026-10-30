# fleet03/B11 — determinant-scale half-potential for arbitrary indefinite binary forms

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T121353Z-fleet03-B11-QFORM-r11`  
**Assignment:** Indefinite signatures  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL CONJECTURE OPEN`  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections retained

The target remains: for independent real coordinates `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal dimension/law/form-independent bound on the density of `X^T A X`.

This report keeps the original-coordinate product structure. It does **not** use law-uniform pointwise quadratic Fourier decay, which is false for fragmented phase-aligned densities; it does not diagonalize `A` and retain false eigen-coordinate independence; and it does not use a fiber supremum that can lose dimension.

The previous B11 run proved a `4/sqrt(|bc|)` theorem for the special physical saddle-plus-square block with binary part `2bXY+dY^2`. The missing local implication was to allow an arbitrary indefinite binary quadratic after the third coordinate has been pivoted, including both nonzero binary diagonal entries and arbitrary coupling of the pivot coordinate before completing the square.

## 2. Compatible completed peer result actually applied

The designated partner is `fleet04/B11`; no completed QFORM handoff from that exact slot was present at the fresh source snapshot, so no result from it is invented. I apply the completed compatible result `fleet04/B18`, scientific source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its key structural step is valid beyond its own bounded-base lemma: after conditioning outside a physical triple and completing a square in one original coordinate `Z`, the variable

`V=Z+m(U)`

need not be independent of the residual quadratic value `R(U)`, but conditional on `R=r` its law is a mixture of translations of the original density of `Z`; therefore its conditional density is still at most one. The peer used this with a bounded-density base `R`. Below I combine the same dependence-safe mechanism with a new **half-potential** bound for every indefinite binary quadratic, so the base itself may have an unbounded logarithmic density.

## 3. Rearrangement facts

### Lemma 3.1 — inverse-half rearrangement

If `f` is a probability density with `0<=f<=1`, then for every `r in R`,

`integral f(x) |x-r|^(-1/2) dx <= 2 sqrt(2)`.

The decreasing rearrangement of the kernel is maximized by putting unit density on the interval of length one centered at `r`; the integral there is `2 sqrt(2)`.

If the kernel is restricted to one side of a singular point and the mass on that side is `m`, the sharper bound is `2 sqrt(m)`. Consequently, for two disjoint endpoint branches carrying masses `m_1,m_2` with `m_1+m_2<=1`, the sum is at most

`2(sqrt(m_1)+sqrt(m_2)) <= 2 sqrt(2)`.

### Lemma 3.2 — quadratic quarter-potential

For every probability density `g<=1` and every `tau in R`,

`integral g(y) |y^2-tau|^(-1/4) dy <= 2 sqrt(2)`.

**Proof.** If `tau<=0`, then `|y^2-tau|^(-1/4)<=|y|^(-1/2)`, so Lemma 3.1 applies. If `tau=r^2>0`, then

`|y^2-r^2|^(-1/4)
 = ( |y-r|^(-1/2) |y+r|^(-1/2) )^(1/2)
 <= ( |y-r|^(-1/2)+|y+r|^(-1/2) )/2`,

and Lemma 3.1 applied to the two translated kernels gives the result. QED.

## 4. New theorem: every indefinite binary quadratic has a bounded half-order potential

Let `X,Y` be independent real random variables with densities bounded by one, and let

`R(X,Y)=aX^2+2bXY+dY^2+alpha X+beta Y+gamma`.

Assume the binary quadratic matrix is indefinite:

`Delta := b^2-a d >0`.

### Theorem 4.1 — `QFORM-INDEFINITE-BINARY-HALF-POTENTIAL-v1`

For every real `t`,

`E[(t-R)_+^(-1/2)] <= 8 Delta^(-1/4)`

and

`E[(R-t)_+^(-1/2)] <= 8 Delta^(-1/4)`.

The expectations are understood through the corresponding nonnegative kernels; the estimate implies finiteness uniformly in `t`.

### Proof

Because `Delta>0`, the binary matrix is invertible. A deterministic translation of `X` and `Y` removes the affine terms. Such separate translations preserve independence and both density caps, while only translating the output level `t`. Thus it suffices to treat

`R=aX^2+2bXY+dY^2`.

The second displayed inequality follows from the first applied to `-R`, since the discriminant `b^2-ad` is unchanged. We prove the first.

#### Case 1: `a=0`

Then `b!=0` and `Delta=b^2`. This is the saddle-axis case from the preceding B11 run. Conditioning on `Y=y`, the expression is affine in `X` with slope `2by`; the one-sided inverse-half rearrangement in `X`, followed by Lemma 3.1 in `Y`, gives

`sup_t E[(t-R)_+^(-1/2)] <= 4/sqrt(|b|)=4 Delta^(-1/4)`.

This is stronger than the claimed constant eight.

#### Case 2: `a>0`

Put `A=a` and `K=Delta/A`. Completing the square in the **original** `X` coordinate conditional on `Y=y` gives

`R=A U^2-KY^2`,

where `U=X+(b/A)Y`. For each fixed `Y=y`, `U` is only a translation of `X`, hence its conditional density is still bounded by one.

Fix `y` and set `s=t+Ky^2`. If `s<=0`, `(s-AU^2)_+^(-1/2)=0`. If `s>0`, let `r=sqrt(s/A)`. On `|u|<r`,

`s-Au^2=A(r-|u|)(r+|u|) >= sqrt(A s)(r-|u|)`.

Hence, by splitting the two endpoint branches and using Lemma 3.1 in its mass-sensitive form,

`E[(s-AU^2)_+^(-1/2) | Y=y]
 <= 2 sqrt(2) A^(-1/4) s^(-1/4)`.

Average in `Y`; Lemma 3.2 with `tau=-t/K` yields

`E[(t-R)_+^(-1/2)]
 <= 2 sqrt(2) A^(-1/4) K^(-1/4) (2 sqrt(2))
 =8 Delta^(-1/4)`.

#### Case 3: `a<0`

Put `A=-a>0` and `K=Delta/A`. Completing the square gives

`R=-A U^2+K Y^2`,

again with `U` a conditional translation of `X`. Set `s=t-Ky^2`. We need to bound `(s+AU^2)_+^(-1/2)`.

If `s>0`, AM-GM gives

`s+A u^2 >= 2 sqrt(sA)|u|`,

so Lemma 3.1 gives

`E[(s+A U^2)^(-1/2)|Y=y] <= 2 A^(-1/4)s^(-1/4)`.

If `s<0`, let `r=sqrt(|s|/A)`. On the support `|u|>r`,

`A u^2-|s|=A(|u|-r)(|u|+r)
 >= 2 sqrt(A|s|)(|u|-r)`.

The two outer endpoint branches therefore give, again by the mass-sensitive inverse-half rearrangement,

`E[(s+A U^2)_+^(-1/2)|Y=y]
 <=2 A^(-1/4)|s|^(-1/4)`.

(The exceptional level `s=0` is harmless as an extended-valued pointwise bound; after integrating in `y`, Lemma 3.2 gives a finite result.) Thus

`E[(t-R)_+^(-1/2)]
 <= 2 A^(-1/4) K^(-1/4)(2 sqrt(2))
 =4 sqrt(2) Delta^(-1/4)
 <=8 Delta^(-1/4)`.

This completes the proof. QED.

The determinant form is worth recording. If `S=[[a,b],[b,d]]`, then `det S=-Delta`, so

`sup_t max{E[(t-R)_+^(-1/2)],E[(R-t)_+^(-1/2)]}
 <=8 |det S|^(-1/4)`.

No diagonalization of `(X,Y)` occurred.

## 5. Dependence-safe Abel smoothing without a bounded base density

The fleet04/B18 mechanism can be stated at exactly the strength needed here.

### Lemma 5.1 — conditional Abel smoothing

Let `R` be any real random variable. Suppose the conditional law of `V` given `R=r` has, for almost every `r`, a density bounded by one. For `c!=0`, put

`T=R+cV^2`.

Then `T` has a density satisfying

`p_T(t)
 <= |c|^(-1/2)
    E[(sgn(c)(t-R))_+^(-1/2)]`.

Indeed, conditional on `R=r`, the density of `cV^2` is bounded by `|c|^(-1/2)|s|^(-1/2)` on the half-line with sign `c`. Tonelli then constructs the displayed mixture density. Notice that no density bound, or even a priori density, is assumed for `R` itself.

Combining Lemma 5.1 with Theorem 4.1 shows that an indefinite binary quadratic becomes bounded-density after adding one square whose conditional translated coordinate retains density cap one.

## 6. Main application: the fully coupled majority-pivot branch

Let a physical `3x3` principal block of the ambient quadratic form be written, after selecting one **original coordinate** as scalar pivot,

`B=[[c,u^T],[u,C]]`, `c!=0`,

and let

`S=C-u u^T/c`

be its `2x2` Schur complement.

Condition all coordinates outside this triple. They create only affine and constant terms. Completing the square in the scalar pivot variable `Z` gives

`Q_w = c (Z+m_w(U))^2 + R_w(U)`,

where the quadratic matrix of the residual polynomial `R_w` in the other two original coordinates is exactly `S`.

Assume `S` is indefinite. Then Theorem 4.1 gives

`sup_t max{E[(t-R_w)_+^(-1/2)],E[(R_w-t)_+^(-1/2)]}
 <=8 |det S|^(-1/4)`,

uniformly in the outside conditioning value `w` and in all induced affine terms.

Now set `V=Z+m_w(U)`. Before the square completion, `Z` is independent of `U`. Conditional on `R_w(U)=r`, the law of `V` is therefore a mixture of translations of the original density of `Z`; exactly as in the completed fleet04/B18 argument, its density remains at most one. Lemma 5.1 yields

`||p_{Q_w}||_infinity
 <=8 |c|^(-1/2)|det S|^(-1/4)
 =8 / |c det B|^(1/4)`,

because `det B=c det S`. The bound is uniform in `w`, so averaging the conditional densities proves the same bound for the full ambient quadratic form.

### Corollary 6.1 — exact inertia interpretation

If `B` has inertia `(2,1)` or `(1,2)` and the nonzero pivot `c` has the **majority sign**, Sylvester inertia additivity makes its Schur complement `S` indefinite. Hence

`boxed( ||p_Q||_infinity <= 8 / |c det B|^(1/4) ).`

If the pivot has the minority sign, the completed fleet04/B18 theorem instead makes `S` definite and gives the sharper

`2 sqrt(pi)/|c det B|^(1/4)`.

Thus every nonzero physical scalar pivot of an invertible indefinite `3x3` block is now covered by a determinant-sensitive square-completion argument: minority-sign pivots by the peer theorem, majority-sign pivots by the new half-potential theorem. This is a local theorem; it does not yet guarantee a dimension-free physical triple from the global spectral hypothesis.

## 7. A strict fully coupled majority-sign target example

Consider

`B=[[1,2,1],[2,2,-1],[1,-1,3]]`.

Its determinant is `-13`, all three diagonal entries are positive, and its inertia is `(2,1)`, so every diagonal pivot has the majority sign. Moreover

`B^2-I=[[5,5,2],[5,8,-3],[2,-3,10]]`.

The leading principal minors of `B^2-I` are `5`, `15`, and `13`, hence `B^2-I` is positive definite. Therefore every eigenvalue of `B` has absolute value strictly greater than one: this block itself satisfies the owner's three-large-eigenvalue threshold.

Using the first pivot `c=1`,

`S=[[-2,-3],[-3,2]]`, `det S=-13`.

Both diagonal entries of the indefinite Schur complement are nonzero and all original third-coordinate couplings are nonzero, so the preceding B11 saddle-axis lemma does not directly apply. Corollary 6.1 gives the explicit bound

`||p_{X^T B X}||_infinity <= 8/13^(1/4) <4.214`

for **every** product input law with marginal densities at most one.

This is a genuinely fully coupled `(2,1)` example in the previously unpaid majority-pivot geometry.

## 8. Rank-two logarithmic control remains mandatory

The binary half-potential theorem must not be mistaken for a binary bounded-density theorem. For independent uniforms on `[-1/2,1/2]`, the saddle `2bXY` has density

`p(s)=(1/|b|) log(|b|/(2|s|))`, `0<|s|<|b|/2`,

which is logarithmically unbounded at zero. What the third direction removes is exactly this singularity: the indefinite binary law has uniformly bounded one-sided order-`1/2` potentials, and the completed square in the third coordinate contributes the matching Abel kernel. This is why three directions can be bounded while the opposite-sign rank-two control is not.

## 9. What is paid and what remains

**Paid this run.** The first local B11 implication from the previous run is closed whenever the selected physical `3x3` indefinite block has a nonzero diagonal pivot: arbitrary binary diagonal perturbations and arbitrary coupling of the pivot to the other two coordinates are allowed, with a determinant-sensitive constant. The majority-sign branch is new; the minority-sign branch is supplied by the completed fleet04/B18 theorem.

**Not paid.** This does not solve the full high-dimensional conjecture. There are two remaining structural issues.

1. A `3x3` physical block with all three diagonal entries zero is outside this scalar-pivot formulation (although the broader fleet02/B15 `C/sigma_min(B)` local theorem already proves boundedness for every invertible physical triple).
2. More importantly, three large spectral eigenvalues do not force one coordinate principal triple with a dimension-free determinant or singular gap; flat rank-three projectors can make every fixed triple small. The global missing implication is a determinant/minor-weighted aggregation or equivalent product-measure argument that converts the total rank-three spectral mass into a dimension-free small-ball bound without selecting a single minor.

A natural next B11 step is therefore to combine the determinant-scale local inequality `|c det B|^(-1/4)` with Cauchy-Binet / averaged coordinate-pivot weights, rather than taking a worst triple. If repeated unchanged attempts fail, the mechanism should switch to a direct coarea/small-ball decomposition on the same indefinite target.

## 10. Status

- `QFORM-INDEFINITE-BINARY-HALF-POTENTIAL-v1`: **proved**.
- `QFORM-CONDITIONAL-ABEL-SMOOTHING-v1`: **proved** (dependence-safe extension of the completed peer mechanism).
- `QFORM-MAJORITY-PIVOT-3X3-v1`: **proved**.
- Opposite-sign rank-two logarithmic singularity: **retained as control**.
- Full universal bounded-density conjecture: **OPEN / NOT PROVED**.
- Continuous-density representative for the full target: **NOT PROVED**.
