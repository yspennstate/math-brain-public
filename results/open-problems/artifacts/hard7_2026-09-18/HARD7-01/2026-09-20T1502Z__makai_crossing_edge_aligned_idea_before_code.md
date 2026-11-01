# HARD7-01 route note before code — crossing triangular prismoids with two aligned edge directions

Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

Current canonical target: `operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md` (owner `HARD7-01`). Frozen source metric remains `d_Makai=2`; this note proposes a restricted all-parameter theorem, not source closure.

The preceding RECOVERY1 theorem settles triangular prismoids whenever the two planar difference bodies are comparable by inclusion. The first six-vertex frontier left there is the crossing/non-nested case. This run attacks an all-parameter crossing subfamily before writing any checker.

## Proposed family

Normalize the lower triangle by an affine map to

\[
T=\operatorname{conv}\{0,e_1,e_2\}.
\]

Take the upper triangle, after an irrelevant translation, to be

\[
C=\operatorname{conv}\{0,a e_1,b e_2\}=\operatorname{diag}(a,b)T.
\]

Geometrically, the two triangles have a chosen vertex at which the two incident edge directions agree. The genuinely crossing regime can, after interchanging the coordinate axes and/or the two bases, be written

\[
a\ge1\ge b>0.
\]

The same-side regimes `a,b<=1` and `a,b>=1` are already covered by the nested-difference-body theorem.

## B8 — discretize the support-function geometry, exactly

Let `B=T-T` and `E=C-C`. Then

\[
h_B(x,y)=\max\{|x|,|y|,|x-y|\},
\]

\[
h_E(x,y)=\max\{a|x|,b|y|,|ax-by|\}.
\]

The dual prismoid formula already proved on this track is

\[
J:=|(K-K)^\circ|
=\int_Q(2-h_B-h_E),
\qquad
Q=B^\circ\cap E^\circ.
\]

In the crossing regime `a>=1>=b`, the upper half of `Q` should have only three affine roof pieces. Put

\[
x_0=-\frac{1-b}{a-b},\qquad y_0=\frac{a-1}{a-b}.
\]

The predicted upper boundary is

\[
y\le\frac{ax+1}{b}\quad(-1/a\le x\le x_0),
\]

\[
y\le x+1\quad(x_0\le x\le0),
\]

\[
y\le1\quad(0\le x\le1/a).
\]

Thus the infinite convex-body integral becomes finitely many exact polynomial/rational cells, but **not** a finite sample: the goal is a symbolic integration valid for every `a>=1>=b>0`.

## B13 — find what only increases

After obtaining the exact product, subtract `2/3`, clear the positive denominator, and substitute

\[
x=a-1\ge0,\qquad y=1-b\in[0,1).
\]

The target is to show that the defect polynomial has nonnegative coefficients as a polynomial in `x`, with each coefficient nonnegative on `0<=y<=1`. If successful, expansion away from the `a=1` boundary is a monotone direction for the cleared defect. This would give a global sign proof rather than a numerical scan.

## B27 — swap the quantifiers

Do not search for a favorable crossing pair `(a,b)`. Fix the contraction parameter `b` and prove the inequality simultaneously for **every** expansion `a>=1`, then quantify over all `0<b<=1`. This turns the first crossing family into a two-parameter theorem rather than an example.

## Expected primal term

For the normalized triangle, `|T|=1/2`, `|C|=ab/2`. In the crossing chamber `a>=1>=b`, the mixed-area support formula predicts

\[
2V(T,C)=a,
\]

hence

\[
|K|=\frac{1+a+ab}{6}.
\]

## Success criterion

Derive a closed formula for `J`, prove on the page that

\[
\frac{1+a+ab}{6}J\ge\frac23
\qquad(a\ge1\ge b>0),
\]

and only then use exact symbolic code as a self-check. If the sign does not close, record the exact offending coefficient/cell and do not promote a theorem.