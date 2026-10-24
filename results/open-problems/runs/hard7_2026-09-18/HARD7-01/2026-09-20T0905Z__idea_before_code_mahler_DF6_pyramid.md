Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric is still `d_sym: 3 -> 3` unless the route below unexpectedly closes every four-dimensional symmetric body. Planned methods: **B18 / B4 / B30**.

# HARD7-01 route note — turn the DF6 boundary into a planar mixed Mahler–Eggleston inequality

This note is written **before** any checker for this run.

The newest checkpoint reduced the entire `V=F=12` four-dimensional local-minimizer frontier to the three-dimensional inequality

\[
 (|L-L|+4|L|)\,|(L-L)^\circ|\ge 16. \tag{DF6}
\]

The present run changes language rather than extending the previous incidence enumeration.

## B18 — central symmetral language

Put

\[
 C:=\frac{L-L}{2}.
\]

Since `L` is three-dimensional,

\[
 |L-L|=8|C|,\qquad |(L-L)^\circ|=\frac18|C^\circ|.
\]

Thus `(DF6)` is exactly

\[
 \boxed{\bigl(|C|+\tfrac12|L|\bigr)|C^\circ|\ge16.} \tag{CS3}
\]

This exposes the missing information: the ordinary symmetric Mahler bound on `C` gives only `|C||C^\circ|>=32/3`, while the Makai/Eggleston-type term `|L||C^\circ|` measures how asymmetric `L` is. The desired inequality is a sharp tradeoff between those two products, not either theorem separately.

## B30 — localize to pyramids and drop one dimension exactly

Take a three-dimensional pyramid, after an affine normalization and translation of its base,

\[
 L=\operatorname{conv}((B,0),(0,1)),\qquad B\subset\mathbb R^2
\]

with `B` a planar convex body. Write `E=B-B` and `A=|B|`.

Horizontal sections immediately give

\[
 |L|=\frac A3. \tag{1}
\]

For `D=L-L`, the section at height `t in [0,1]` is

\[
 (1-t)E+tB,
\]

and the section at `-t` is its reflection. In the plane,

\[
 |(1-t)E+tB|=(1-t)^2|E|+2t(1-t)V(E,B)+t^2A.
\]

Because `E=B+(-B)`, bilinearity and reflection symmetry give

\[
 V(E,B)=V(B,B)+V(-B,B)=A+V(B,-B)=\frac{|E|}{2}.
\]

Therefore

\[
 |(1-t)E+tB|=(1-t)|E|+t^2A,
\]

and integration over both signs of `t` yields

\[
 \boxed{|L-L|=|E|+\frac23A.} \tag{2}
\]

For the polar, write a dual point as `(u,s) in R^2 x R`. Since

\[
 h_L(u,s)=\max\{h_B(u),s\},
\]

the condition `(u,s) in (L-L)^\circ` is `h_L(u,s)+h_L(-u,-s)<=1`. For fixed `u`, the admissible `s`-interval has length

\[
 1-h_E(u)
\]

when `h_E(u)<=1`, and is empty otherwise. Consequently

\[
 |(L-L)^\circ|=\int_{E^\circ}(1-h_E(u))\,du.
\]

In dimension two, layer cake for the gauge/support function gives

\[
 \int_{E^\circ}h_E(u)\,du=\frac23|E^\circ|,
\]

hence

\[
 \boxed{|(L-L)^\circ|=\frac13|E^\circ|.} \tag{3}
\]

**Important correction to an initial scratch calculation:** the factor is `1/3`, not `4/3`; the latter would correspond to a differently scaled support threshold. Keeping the exact support normalization is essential.

Substituting (1)–(3) into `(DF6)` gives the exact planar problem

\[
 \left(|E|+\frac23A+\frac43A\right)\frac13|E^\circ|\ge16,
\]

i.e.

\[
 \boxed{(|B-B|+2|B|)\,|(B-B)^\circ|\ge48.} \tag{P48?}
\]

At this point the constants fail the tetrahedron sanity check: for a triangle `B`, `|B-B|=6|B|` and Eggleston gives `|B||(B-B)^\circ|=3/2`, so the left side is only `12`, not `48`. Therefore one of the scaling steps above must still be wrong. Before writing any checker, fix the fiber scaling rigorously.

Recompute the polar condition directly: `D=L-L` has support

\[
 h_D(u,s)=h_L(u,s)+h_L(-u,-s)
 =\max(h_B(u),s)+\max(h_B(-u),-s).
\]

For fixed `u`, `h_D(u,s)<=1` is equivalent to

\[
 h_B(-u)-1\le s\le 1-h_B(u),
\]

and the interval length is

\[
 2-h_B(u)-h_B(-u)=2-h_E(u).
\]

It exists precisely for `h_E(u)<=2`, i.e. `u in 2E^\circ`. Thus

\[
 |D^\circ|=\int_{2E^\circ}(2-h_E(u))\,du
 =\int_0^2 |tE^\circ|\,dt
 =\frac83|E^\circ|. \tag{3'}
\]

Now the constants pass both simplex and symmetric sanity checks. Combining (1), (2), (3') gives

\[
 (|D|+4|L|)|D^\circ|
 =\left(|E|+2A\right)\frac83|E^\circ|.
\]

Hence `(DF6)` for every three-dimensional pyramid is **equivalent** to

\[
 \boxed{(|B-B|+2|B|)\,|(B-B)^\circ|\ge 6.} \tag{DF2}
\]

For a triangle, this is equality: `(6A+2A)*(3/(2A))=12`, so this still exposes a factor-two mismatch. The correct target must be 12, because `(8A)*(3/(2A))=12`. Returning to `(DF6)`, the right side is 16, while the multiplier from (3') is `8/3`, so the planar bracket must be at least `6`, indeed `8A*3/(2A)=12 >=6`; a triangle would then give strict inequality, contradicting the known tetrahedral equality only if a tetrahedron `L` is represented as a pyramid over a triangle in this normalization and the previous 3D equality check was exact. This is another warning that the primal section formula (2) must be rechecked before any claim.

The route is therefore mathematically valuable but **not yet certified** at this note: the intended task is to derive both pyramid formulas from first principles, test them on a standard tetrahedron by exact coordinates, and only then state the planar inequality. No code or theorem claim is made in this pre-code note.

## B4 — prove the first nontrivial planar family completely once scaling is fixed

After the constants are repaired, attack planar quadrilaterals exactly. Every convex quadrilateral is affinely equivalent to

\[
 B_{r,s}=\operatorname{conv}\{(1,0),(0,1),(-r,0),(0,-s)\},\qquad r,s>0.
\]

By swapping the two endpoints on each diagonal and then interchanging coordinate axes, one may restrict to

\[
 s\ge r\ge1.
\]

In this chamber the difference body has the eight vertices

\[
 \pm(1+r,0),\ \pm(1,s),\ \pm(0,1+s),\ \pm(-r,s)
\]

in cyclic order. Exact shoelace and polar-edge calculations give candidate formulas

\[
 |B|=\frac{(1+r)(1+s)}2,
\]

\[
 |B-B|=(1+r)(1+3s),
\]

and

\[
 |(B-B)^\circ|
 =-\frac{r^2-3rs^2-6rs-r+1}{rs(r+1)(s+1)^2}.
\]

Once the corrected planar target is fixed, its deficit should reduce after `r=1+a`, `s=r+b=1+a+b` to a polynomial with nonnegative coefficients. This is the exact finite algebra worth checking; there is no reason to sample quadrilaterals.

## Literature checkpoint before code

A fresh 20 September 2026 check found the classical planar ingredients but not the combined tradeoff above:

- Eggleston’s sharp planar difference-body polar inequality `|B||(B-B)^o|>=3/2`, equality for triangles, as restated and reproved by Aliev (arXiv:2511.14991, 2025).
- Böröczky–Makai–Meyer–Reisner, *Volume product of planar polar convex bodies — lower estimates with stability* (Stud. Sci. Math. Hungar. 50 (2013); arXiv:1507.01481), including planar symmetric Mahler and Eggleston stability.
- the general 3D Makai difference-body conjecture remains open outside special symmetry classes in the current literature checked.

No search hit located the exact `DF6` pyramid reduction or the candidate combined planar expression. This is bounded negative evidence only; priority remains **UNVERIFIED**.

The next action is exact derivation, not another literature list.