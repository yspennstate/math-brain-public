# account01/B11 — full binary-indefinite L^3 closure and majority-pivot smoothing

**Run:** `QFORM-B11-20260922T121344Z`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS PROVED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and corrections consumed

The target remains: for every dimension, every independent real inputs with one-dimensional densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X` (or give a valid counterexample). Continuity is a separate stronger conclusion.

This report does **not** use law-uniform pointwise quadratic-phase decay, post-rotation independence, a naive fiber supremum, a cross minor alone, or a universal constant `pi`. Before publication I consumed the live corrections including `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, and `QFORM-TWOSHEET-XRAY-ONLY-FALSE`.

The assigned partner result actually used is:

- `account02/B11`, scientific report `yspennstate/math-open-problems@ea26c080ff290b0f10ec701ec8bf8847cc84ceb6:proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T115006Z-account02-B11-qform-r18-7c1e/REPORT.md`. In particular, its Lemma 2 proves that if `W=cY^2+uY+v`, `c!=0`, and the density of `Y` is at most one, then `||p_W||_{3/2} <= 2 |c|^{-1/3}`. Its first unpaid implication was the full binary-indefinite `L^3` estimate proved below.

A second dependency, used only for the complementary definite-Schur branch, is:

- `account04/B18`, scientific report `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`, proving the dependent square-smoothing theorem and the definite-Schur scalar-pivot estimate.

## 2. Compact conditional end-to-end route

The rank-two opposite-sign obstruction should not be made bounded; it only needs enough integrability for the third direction to smooth it. The route is:

1. Prove a determinant-scale `L^3` bound for **every** nondegenerate indefinite binary quadratic in two original independent coordinates.
2. An uncoupled third square has a uniform `L^{3/2}` density, so Young gives `L^3 * L^{3/2} -> L^infinity`.
3. If the third coordinate is fully coupled, complete the square in that original coordinate. The residual is the binary Schur-complement quadratic. A new dependent Abel-smoothing lemma converts its `L^3` density into an `L^infinity` bound even though the completed-square shift depends on the binary variables.
4. For a `(2,1)` block, a majority-sign scalar pivot has an **indefinite** Schur complement, exactly the branch left open by the definite-Schur theorem of account04/B18. Thus the new result pays that local sign branch.

The full arbitrary-dimensional theorem still needs a dimension-free global extraction/aggregation argument: three large spectral directions need not produce one uniformly nondegenerate original-coordinate principal triple.

## 3. Standard analytic input

Let `H_{1/2}` denote the finite operator norm in the one-dimensional Hardy--Littlewood--Sobolev inequality

`|| I_{1/2} h ||_3 <= H_{1/2} ||h||_{6/5}`,

where

`I_{1/2}h(s)=integral_R |s-r|^{-1/2} h(r) dr`.

Only finiteness and universality of `H_{1/2}` are used.

## 4. Full binary-indefinite L^3 theorem

### Theorem 4.1 — `QFORM-BINARY-INDEFINITE-L3-v1`

Let `X,Y` be independent real random variables with densities `f,g` satisfying `0<=f,g<=1`. Let

`R = alpha X^2 + 2 a X Y + beta Y^2 + r X + s Y + c`

and suppose

`D := a^2-alpha beta > 0`.

Then `R` has a density and

`boxed( ||p_R||_3 <= C_bin D^{-1/3} )`,

where the universal finite constant can be taken as

`C_bin = max( sqrt(2) 5^{1/3} H_{1/2}, 6*2^{2/3}*(25/24)^{1/3} ).`

The exponent is scale-sharp: multiplying the quadratic by `lambda` multiplies `D` by `lambda^2` and the `L^3` norm by `|lambda|^{-2/3}`.

### Proof

Because the binary Hessian is invertible (`det[[alpha,a],[a,beta]]=-D`), translating `X,Y` separately removes the linear terms. Translation preserves independence and the density caps. A final constant only translates the output. Thus it suffices to treat

`q(x,y)=alpha x^2+2axy+beta y^2`.

Put `M=max(|alpha|,|beta|)`.

#### Case A: a diagonal coefficient is at least `sqrt(D)/5`

Assume without loss of generality

`|beta| = M >= sqrt(D)/5`.

For fixed `X=x`, the equation `q(x,y)=t` has discriminant

`Delta_y = 4(Dx^2+beta t)`.

At every regular root,

`|partial_y q| = 2 sqrt(Dx^2+beta t)`.

There are at most two roots, and `g<=1`, hence the conditional density obeys

`p_{q|X=x}(t) <= (Dx^2+beta t)_+^{-1/2}`

(with the obvious interpretation that the right side is zero when the discriminant is negative). Therefore

`p_q(t) <= integral f(x)(Dx^2+beta t)_+^{-1/2} dx`.    (4.1)

Let `m` be the density of `U=DX^2`. By the **account02/B11 single-square theorem applied with coefficient `D`**, not merely by a formal analogy,

`||m||_{3/2} <= 2 D^{-1/3}`,

while `||m||_1=1`. Interpolation gives

`||m||_{6/5} <= ||m||_1^{1/2} ||m||_{3/2}^{1/2}
              <= sqrt(2) D^{-1/6}`.    (4.2)

With `z=-beta t`, the right side of (4.1) is dominated by `I_{1/2}m(z)`. Thus HLS and the change of scale in `t` give

`||p_q||_3
 <= |beta|^{-1/3} H_{1/2} ||m||_{6/5}
 <= sqrt(2) H_{1/2} |beta|^{-1/3} D^{-1/6}`

and since `|beta|>=sqrt(D)/5`,

`||p_q||_3 <= sqrt(2) 5^{1/3} H_{1/2} D^{-1/3}`.    (4.3)

If `|alpha|=M`, interchange `X` and `Y`.

#### Case B: both diagonal coefficients are smaller than `sqrt(D)/5`

Now

`|alpha|,|beta| < sqrt(D)/5`.

Since `a^2=D+alpha beta`,

`|a|^2 >= D-|alpha beta| > (24/25)D`,

and consequently

`max(|alpha|,|beta|)/|a| < 1/sqrt(24) < 1/4`.    (4.4)

Partition the input plane into

`E_x={|y|<=2|x|}`,  `E_y={|y|>2|x|}`.

On `E_x`, using (4.4),

`|partial_y q|
 =2|ax+beta y|
 >=2(|a||x|-|beta||y|)
 >= |a||x|`.    (4.5)

For every fixed `x!=0`, `y -> q(x,y)` is therefore monotone on the interval `|y|<=2|x|`. Let `h_x` be the density obtained by pushing `g(y)1_{E_x}` through this monotone map. Change of variables yields

`||h_x||_3^3
 = integral_{|y|<=2|x|} g(y)^3 / |partial_y q(x,y)|^2 dy
 <= |a|^{-2}|x|^{-2} integral g^3
 <= |a|^{-2}|x|^{-2}`.

Hence

`||h_x||_3 <= |a|^{-2/3}|x|^{-2/3}`.

Minkowski and the bathtub principle give

`||p_{E_x}||_3
 <= |a|^{-2/3} integral f(x)|x|^{-2/3}dx
 <= 3*2^{2/3}|a|^{-2/3}`.    (4.6)

Indeed the last integral is maximized, among `0<=f<=1` of mass one, by `1_{[-1/2,1/2]}`.

On `E_y`, for fixed `y`,

`|partial_x q|
 =2|alpha x+ay|
 >=2(|a||y|-|alpha||x|)
 > |a||y|`,

so the symmetric argument gives

`||p_{E_y}||_3 <= 3*2^{2/3}|a|^{-2/3}`.    (4.7)

Since `p_q=p_{E_x}+p_{E_y}`, (4.6)--(4.7) imply

`||p_q||_3 <= 6*2^{2/3}|a|^{-2/3}
            <= 6*2^{2/3}(25/24)^{1/3}D^{-1/3}`.    (4.8)

Combining (4.3) and (4.8) proves the theorem. QED.

### Rank-two logarithmic control is retained

For `q=XY` with independent uniforms on `[-1/2,1/2]`, the density is logarithmically divergent at zero. The theorem does not contradict that: a logarithm lies in `L^3`. This is exactly the correct rank-two regularity level for the third-direction smoothing below.

## 5. Uncoupled third square: exact third-direction regularization

### Corollary 5.1 — `QFORM-HYPERBOLIC-PLUS-SQUARE-v1`

Let `Z` be independent of `(X,Y)`, with density at most one, and let `d!=0`. Then for

`T=R+dZ^2+uZ+v`,

where `R` is as in Theorem 4.1,

`boxed( ||p_T||_infinity <= 2 C_bin D^{-1/3}|d|^{-1/3}. )`

If the three-variable quadratic block is

`B=[[alpha,a,0],[a,beta,0],[0,0,d]]`,

then `|det B|=D|d|`, so equivalently

`||p_T||_infinity <= 2 C_bin |det B|^{-1/3}`.

**Proof.** Theorem 4.1 gives `p_R in L^3`. The account02/B11 square theorem gives

`||p_{dZ^2+uZ+v}||_{3/2} <=2|d|^{-1/3}`.

The two terms are independent, so Young's inequality with conjugate exponents `3` and `3/2` gives the bound. Because convolution `L^3*L^{3/2}` is continuous (translation continuity plus Holder), this branch has a continuous bounded density. QED.

This is the exact analytic mechanism by which the third direction removes the opposite-sign logarithmic singularity: it is not pointwise Fourier decay; it is `L^3` rank-two control followed by `L^{3/2}` square smoothing.

## 6. A dependent square lemma starting from L^3

The third coordinate need not be uncoupled.

### Lemma 6.1 — `QFORM-DEPENDENT-SQUARE-L3-SMOOTHING-v1`

Let `R` have a density `p` with `||p||_3=M`. Suppose that, for almost every `r`, the conditional law of a real variable `V` given `R=r` has a density bounded by one. No independence between `R` and `V` is assumed. For `d!=0`, let

`T=R+dV^2`.

Then `T` has an essentially bounded density and

`boxed( ||p_T||_infinity <= 4 |d|^{-1/2} M^{3/4}. )`

### Proof

For `d>0`, the conditional density of `dV^2` is at most `d^{-1/2}s^{-1/2}1_{s>0}`. Thus

`p_T(t) <= d^{-1/2} integral_{r<t} p(r)(t-r)^{-1/2}dr`.    (6.1)

For any `L>0`, split the integral into `0<t-r<=L` and `t-r>L`. Holder on the near part gives

`integral_{t-L}^t p(r)(t-r)^{-1/2}dr
 <= M ( integral_0^L s^{-3/4}ds )^{2/3}
 = 2^{4/3} M L^{1/6}`.    (6.2)

The far part is at most `L^{-1/2}||p||_1=L^{-1/2}`. Choose

`L=(2^{4/3}M)^{-3/2}`.

Then both terms in (6.2) plus the far estimate equal `2M^{3/4}`, so the sum is at most `4M^{3/4}`. This proves the claim for `d>0`; reflection gives `d<0`. QED.

The exponent `3/4` is forced by scaling: an `L^3` density norm scales like output-scale `^{-2/3}`, while a half-order potential must scale like output-scale `^{-1/2}`.

## 7. Fully coupled majority-sign pivot: the B18 missing inertia branch

Let an original-coordinate physical principal triple have symmetric block

`B = [[C,b],[b^T,d]]`,

where `d!=0`, `C` is `2x2`, and define the Schur complement

`S=C-bb^T/d`.

Assume `S` is indefinite. Put

`D_S=-det S>0`.

### Theorem 7.1 — `QFORM-INDEFINITE-SCHUR-PIVOT-v1`

For independent ambient coordinates with densities at most one, with arbitrary couplings from this triple to every outside coordinate, the full quadratic form has an essentially bounded density satisfying

`boxed(
 ||p_Q||_infinity
 <= 4 C_bin^{3/4} ( |d| |det B| )^{-1/4}.
)`

### Proof

Condition on all coordinates outside the triple. They create only affine and constant terms. Writing the selected scalar coordinate as `Z` and the other two as `U=(X,Y)`, complete the square in the **original** coordinate `Z`:

`Q_w(U,Z)
 = d( Z + m_w(U) )^2 + R_w(U)`,

where `m_w` is affine and the quadratic matrix of `R_w` is exactly `S`.

Theorem 4.1, uniformly in the affine terms generated by the outside conditioning, gives

`||p_{R_w}||_3 <= C_bin D_S^{-1/3}`.    (7.1)

Set `V=Z+m_w(U)`. Conditional on `R_w(U)=r`, the law of `V` is a mixture of translations of the original density of `Z`; therefore its conditional density is still at most one. Lemma 6.1 and (7.1) give

`||p_{Q_w}||_infinity
 <= 4 |d|^{-1/2} (C_bin D_S^{-1/3})^{3/4}
 =4 C_bin^{3/4}|d|^{-1/2}D_S^{-1/4}`.

Since `det B=d det S`, `D_S=|det B|/|d|`, hence

`|d|^{-1/2}D_S^{-1/4}=(|d||det B|)^{-1/4}`.

The bound is uniform in the outside conditioning and survives averaging. QED.

### Exact inertia interpretation

For a `3x3` block of inertia `(2,1)`, if the scalar pivot `d` has the majority sign (`d>0`), inertia additivity forces the `2x2` Schur complement to have inertia `(1,1)`, so Theorem 7.1 applies. For inertia `(1,2)`, the dual statement holds for a negative majority-sign pivot.

This is exactly the sign branch left unpaid in account04/B18. If instead the pivot has the minority sign, the Schur complement is definite and the account04/B18 theorem gives

`||p_Q||_infinity <= 2 sqrt(pi) (|d||det B|)^{-1/4}`.

Consequently **every invertible physical `3x3` block with a nonzero chosen diagonal pivot is controlled by one of the two Schur-pivot mechanisms**, with a universal constant times `(|d||det B|)^{-1/4}`. The exceptional all-zero-diagonal invertible block is not covered by this pivot statement and is not silently declared solved here.

## 8. What this does and does not solve

### Proved here

1. The full partner target `BINARY-INDEFINITE-L3` is closed for all affine nondegenerate indefinite binary quadratics, with determinant-scale exponent `D^{-1/3}`.
2. Every hyperbolic binary block plus an uncoupled third square has a bounded **continuous** density with determinant-scale bound `2C_bin |det B|^{-1/3}`.
3. Every fully coupled scalar-pivot triple whose Schur complement is indefinite has an essentially bounded density with bound `4C_bin^{3/4}(|d||det B|)^{-1/4}`.
4. Together with account04/B18, both majority-sign and minority-sign nonzero scalar pivots are paid.

### Not proved here

1. The full arbitrary-dimensional spectral-to-coordinate aggregation. Three eigenvalues of magnitude at least one do not automatically give one principal triple with `|d det B|` bounded below independent of dimension.
2. The all-zero-diagonal scalar-pivot exception by this mechanism.
3. Continuity in the fully coupled dependent-smoothing theorem. Only an essentially bounded density is established there.
4. Any universal constant `pi`; the live correction explicitly refutes that claim.

The new interactive correction supplies a separate rank-exactly-three diffuse-leverage bound (`<=24` when maximum row leverage is at most `1/12`). Thus the most useful next global implication is a **mixed-leverage aggregation theorem** combining diffuse cross-block smoothing with localized principal-pivot/indefinite-Schur estimates without selecting one dimension-losing minor.

## 9. Honest outcome

`ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS PROVED / FULL CONJECTURE OPEN`.

The principal new step is a complete determinant-scale `L^3` theorem for the rank-two indefinite law and its use to close the fully coupled majority-sign Schur branch. The remaining obstruction is global coordinate aggregation, not the local `(+, +, -)/(+, -, -)` smoothing mechanism treated here.
