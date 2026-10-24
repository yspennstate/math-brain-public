# Revision-11 correction: scalar-rest conditional supremum is not uniformly bounded

Run: `20260922T182159Z-account01-B08-qform-r16`  
Status: `REFUTED INTERMEDIATE REDUCTION / FULL QFORM NOT REFUTED`.

A fresh owner-control read advanced to revision `2026-09-22.11` and proposed the scalar-conditioning target

`M = sup_b ||p_{Q3 | Q'=b}||_infinity`

as a universal quantity after separating three large spectral directions from the remaining quadratic form. The exact construction below shows that this `sup_b` target is false, already for a physically diagonal four-variable target for which the full density is bounded by `pi`. The identity

`p_Q(t)=int p_{Q3|Q'=b}(t-b) f_{Q'}(b) db`

remains correct; what fails is pulling out an unweighted supremum over the conditioning level.

## 1. Exact target example

Let `X_1,X_2,X_3,X_4` be independent `Uniform[0,1]`, hence each has density exactly one on its support. Define the orthonormal spectral coordinates

`Y=(X_1+X_4)/sqrt(2)`,
`Z=(X_1-X_4)/sqrt(2)`.

Take the spectral decomposition

`Q_3 = Y^2 + X_2^2 - X_3^2`,
`Q'  = Z^2`,
`Q   = Q_3+Q'`.

The four spectral eigenvalues are `(1,1,-1,1)`, so this is within the full target and in particular has at least three eigenvalues of modulus at least one. Yet

`Y^2+Z^2=X_1^2+X_4^2`,

so physically

`Q=X_1^2+X_2^2-X_3^2+X_4^2`.

Thus the known diagonal theorem gives

`||p_Q||_infinity <= pi`.                                      (1.1)

So the construction is not a QFORM counterexample.

## 2. Exact conditional law of `Y` given `Q'=b`

The orthogonal map `(X_1,X_4)->(Y,Z)` has Jacobian one, and `(Y,Z)` is uniform on the diamond

`0 <= (Y+Z)/sqrt(2) <=1`,
`0 <= (Y-Z)/sqrt(2) <=1`.

For fixed `z`, the allowed `Y` interval is

`[|z|, sqrt(2)-|z|]`

of length

`L(z)=sqrt(2)-2|z|`.

For `0<b<1/2`, conditioning on `Q'=Z^2=b` mixes `Z=+sqrt(b)` and `Z=-sqrt(b)`. The two conditional `Y` intervals coincide, hence the regular conditional density is exactly

`Y | (Q'=b) ~ Uniform[a,c]`,

where

`a=sqrt(b)`, `c=sqrt(2)-sqrt(b)`,
`L=c-a=sqrt(2)-2sqrt(b)`.                                      (2.1)

As `b` increases to `1/2`, `L` decreases to zero. The midpoint is independent of `b`:

`(a+c)/2 = 1/sqrt(2) =: y_0`.                                  (2.2)

## 3. The opposite-square pair has its rank-two logarithmic singularity

Let

`W=X_2^2-X_3^2`.

For `0<|w|<1`, direct convolution of the square densities gives the exact symmetric density

`g(w)
 = (1/4) int_0^(1-|w|) [v(v+|w|)]^(-1/2) dv
 = (1/2) asinh sqrt((1-|w|)/|w|)`.                             (3.1)

In particular, for `0<|w|<=1/2`,

`g(w) >= (1/4) log(1/(2|w|))`.                                 (3.2)

This is the standard rank-two logarithmic singularity; the third core spectral direction `Y^2` normally smooths it, but conditioning on an extreme value of `Z^2` makes `Y` nearly deterministic.

## 4. Conditional core density diverges along positive-measure conditioning levels

Conditionally on `Q'=b`, the variable `Y` is independent of `(X_2,X_3)`, so the density of

`Q_3=Y^2+W`

at `t=1/2` is

`p_b(1/2)
 = (1/L) int_a^c g(1/2-y^2) dy`.                               (4.1)

Write `y=y_0+r`. For `L<=1/8`, `|r|<=L/2` and

`|1/2-y^2|=|sqrt(2)r+r^2| <=2|r|`.                            (4.2)

Using (3.2),

`g(1/2-y^2) >= (1/4) log(1/(4|r|))`.                           (4.3)

Therefore

`p_b(1/2)
 >= (1/L) int_(-L/2)^(L/2) (1/4)log(1/(4|r|)) dr
 = (1/4)[log(1/(2L))+1]`.                                     (4.4)

As `b->1/2`, equivalently `L->0`, the right side tends to infinity. Moreover for every finite threshold the set of `b<1/2` close enough to `1/2` has positive `Q'`-density, so this is not a single null-fiber version issue. Consequently

`ess sup_b ||p_{Q3 | Q'=b}||_infinity = infinity`.             (4.5)

Hence there is no universal finite bound on the revision-11 scalar conditional supremum `M`.

## 5. What survives and the correct repaired interface

The exact mixture identity survives:

`p_Q(t)=int p_{Q3,Q'}(t-b,b) db`.                              (5.1)

The failed step is replacing the integral by the unweighted fiber supremum `sup_b ||p_{Q3|b}||infinity`. Rare edge fibers can have arbitrarily sharp conditional core laws even though their conditioning density is proportionally small.

A product-preserving repaired sufficient quantity is the mixed norm

`N := int sup_s p_{Q3,Q'}(s,b) db
    = E[ ||p_{Q3|Q'}||infinity ]`,                             (5.2)

where the equality is interpreted through `p_{Q3,Q'}(s,b)=f_{Q'}(b)p_{Q3|b}(s)`. Indeed

`p_Q(t)
 =int p_{Q3,Q'}(t-b,b)db
 <=int sup_s p_{Q3,Q'}(s,b)db=N`.                              (5.3)

The present counterexample does not refute a universal bound on this weighted mixed norm. In fact its bad conditional peak grows only logarithmically while `f_{Q'}(b)` vanishes linearly in the shrinking interval length, illustrating the compensation that the unweighted `sup_b` discards.

Thus the next source-valid scalar-conditioning target should be a dimension-free `L^1_b L^infinity_s` joint-density estimate, or an equivalent averaged conditional anti-concentration statement, not an unweighted uniform conditional density cap.

## 6. Scope

This correction does **not** disprove the quadratic-form bounded-density conjecture; the full example has the diagonal bound (1.1). It refutes only the proposed revision-11 intermediate reduction to a universal `sup_b ||p_{Q3|Q'=b}||infinity` bound. It also remains consistent with earlier corrections showing that conditioning can sharpen projected densities and that rank-two opposite signs carry a logarithmic singularity.
