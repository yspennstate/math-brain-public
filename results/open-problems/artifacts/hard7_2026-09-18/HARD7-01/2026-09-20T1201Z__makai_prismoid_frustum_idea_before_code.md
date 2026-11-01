# HARD7-01 idea before code — support-fibre formula for prismoids and sharp Makai bound for homothetic frusta

Fresh Makai target: for convex `K subset R^3`, prove

`|K| |(K-K)^circ| >= 2/3`.

This note is deliberately written before any checker. The previous Makai run used B2/B5/B11 on pyramids. The new triple is **B6 / B18 / B24**.

## B18 — say the problem in support-function language

Take arbitrary planar convex bodies `A,C subset R^2` and the three-dimensional prismoid

`K = conv(A x {0}, C x {1})`.

For `y in R^2`, put

`p=h_A(y), q=h_A(-y), r=h_C(y), s=h_C(-y)`.

The support function is

`h_K(y,t)=max(p,r+t)`

and therefore

`h_{K-K}(y,t)=max(p,r+t)+max(q,s-t)`.

Let

`w_A(y)=p+q=h_{A-A}(y)`, `w_C(y)=r+s=h_{C-C}(y)`.

The two switch points are `alpha=p-r` and `beta=s-q`. If `alpha>=beta`, equivalently `w_A>=w_C`, the minimum of the preceding convex piecewise-linear function is `w_A`; if `alpha<=beta` its minimum is `w_C`. In either case a polar fibre exists exactly when

`max(w_A,w_C)<=1`,

and then direct solution of the two outer affine inequalities gives the fibre interval

`p+s-1 <= t <= 1-r-q`,

of length

`2-w_A(y)-w_C(y)`.

Hence, with

`P=(A-A)^circ intersect (C-C)^circ`,

there is the exact identity

`|(K-K)^circ| = integral_P [2-h_{A-A}(y)-h_{C-C}(y)] dy`.     (PF)

This is a genuine two-dimensional reduction for every prismoid, not sampling.

The ordinary volume follows from mixed area. With `V(A,C)` defined by

`|(1-z)A+zC|=(1-z)^2|A|+2z(1-z)V(A,C)+z^2|C|`,

integration over `0<=z<=1` gives

`|K|=(|A|+V(A,C)+|C|)/3`.                                      (PV)

Thus the full Makai inequality for prismoids is equivalent to a planar mixed-area/polar-intersection inequality through (PF)+(PV).

## B6 — deform one base to a solvable point: positive homothetic frusta

Now suppose the two bases are positively homothetic. Translation of the top base is removed by an affine shear, and interchanging the two bases if necessary reduces by affine invariance to

`C=lambda A`, `0<=lambda<=1`.

Write `B=A`, `D=B-B`, `Q=D^circ`. Then

`w_C=lambda w_A=lambda h_D` and `P=Q`.

Formula (PF) becomes

`|(K-K)^circ| = integral_Q [2-(1+lambda)h_D(y)] dy`.

Because `Q={h_D<=1}`, the function `h_D` is the gauge of `Q`. In dimension two,

`integral_Q h_D(y) dy = (2/3)|Q|`,

so

`|(K-K)^circ| = [2(2-lambda)/3] |(B-B)^circ|`.                 (1)

The frustum sections are `(1-(1-lambda)z)B`, hence

`|K| = [(1+lambda+lambda^2)/3]|B|`.                            (2)

Multiplying (1),(2) and using Eggleston's sharp planar theorem

`|B| |(B-B)^circ| >= 3/2`

gives

`|K| |(K-K)^circ| >= (1/3)(1+lambda+lambda^2)(2-lambda)`

` = 2/3 + (1/3) lambda(1+lambda-lambda^2) >= 2/3`.             (3)

Thus every three-dimensional convex hull of two positively homothetic planar convex bodies in parallel planes satisfies Makai's conjectured `2/3` bound. For a fixed ratio `lambda`, the lower bound in (3) is sharp, attained exactly when the planar base is a triangle. For the source constant `2/3`, equality is possible only at `lambda=0`, and then Eggleston rigidity forces a triangular base, so `K` is a tetrahedron.

The case `lambda>1` is affinely equivalent to the case `1/lambda<1` by exchanging the two bases and applying a horizontal dilation. Arbitrary relative translation of the two homothetic bases is removed by an affine shear. Thus the theorem covers all positive-homothety frusta, including pyramids (`lambda=0`) and prisms (`lambda=1`).

## B24 — find the extremal object

The exact class factor is

`F(lambda)=(1+lambda+lambda^2)(2-lambda)=2+lambda+lambda^2-lambda^3`.

For `0<=lambda<=1`,

`F(lambda)-2=lambda(1+lambda-lambda^2)`,

which is strictly positive for `lambda>0`. Therefore truncating a cone away from its apex cannot create a Makai counterexample inside this class: the worst object is the untruncated pyramid endpoint, and source equality collapses to the tetrahedron.

This is stronger than the previous pyramid theorem and also supplies a new exact planar reduction (PF) for arbitrary prismoids. The source metric `d_Makai` nevertheless remains `2`, because arbitrary three-dimensional convex bodies are still untreated.

Before promotion, check the algebraic factorization/endpoints exactly, re-search prior art for Makai plus frusta/prismoids/homothetic bases, and keep any novelty claim UNVERIFIED absent an independent audit.
