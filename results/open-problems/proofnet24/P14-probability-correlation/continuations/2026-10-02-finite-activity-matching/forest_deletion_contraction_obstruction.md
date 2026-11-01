# Exact obstruction to coefficientwise deletion/contraction

**Result.** The coefficient of an unmarked edge activity in the forest Rayleigh difference can be negative. A positively weighted `K4` gives the exact polynomial

\[
R_{01,23}(w)=36-6w+2w^2.
\]

The polynomial is strictly positive for every real `w`, and in particular every positive activity. Thus this is an obstruction to coefficientwise-positive deletion/contraction induction, **not** a counterexample to the all-fugacity weighted forest negative-correlation conjecture.

## General deletion/contraction identity

Let

\[
Z_G(z)=\sum_{F\text{ acyclic}}\prod_{h\in F}z_h,
\qquad R_{ef}(Z)=Z_eZ_f-ZZ_{ef},
\]

where `e`, `f`, and `g` are distinct edges. Write `w=z_g`. Contraction retains distinct parallel edges and discards loops, as required by the bijection between forests containing `g` and forests of `G/g`. The exact identity is

\[
Z_G=A+wB,\qquad A=Z_{G\setminus g},\quad B=Z_{G/g}.
\]

Differentiating while retaining both cross terms gives

\[
R_{ef}(Z_G)=R_{ef}(A)+wM_{ef}(A,B)+w^2R_{ef}(B),
\]

\[
M_{ef}(A,B)=A_eB_f+B_eA_f-AB_{ef}-BA_{ef}.
\]

There is no missing factor of two in this formula. If the two marked activities are `x` and `y`, write

\[
A=a_{00}+a_{10}x+a_{01}y+a_{11}xy,
\quad B=b_{00}+b_{10}x+b_{01}y+b_{11}xy.
\]

The Rayleigh difference is independent of `x` and `y`, and its three coefficients are

\[
R(A)=a_{10}a_{01}-a_{00}a_{11},
\]

\[
M=a_{10}b_{01}+b_{10}a_{01}-a_{00}b_{11}-b_{00}a_{11},
\]

\[
R(B)=b_{10}b_{01}-b_{00}b_{11}.
\]

## A three-parameter weighted `K4` family

Use vertices `0,1,2,3`, marked edges `e=01`, `f=23`, and unmarked recursion edge `g=02`. Give the other three edges activities

\[
a=z_{03}>0,\qquad b=z_{12}>0,\qquad c=z_{13}>0.
\]

The eight coefficients are obtained directly by contracting the marked edges. For example, after including both `01` and `23`, all three remaining edges `03,12,13` join the two contracted components, so at most one may be selected. This gives `a11=1+a+b+c`. After also including `02`, they are all loops, giving `b11=1`.

| Coefficient | Exact value |
|---|---|
| `a00` | `(1+a)(1+b)(1+c)` |
| `a10` | `(1+b)(1+a+c)` |
| `a01` | `(1+a)(1+b+c)` |
| `a11` | `1+a+b+c` |
| `b00` | `(1+a)(1+b)(1+c)-abc` |
| `b10` | `1+a+c` |
| `b01` | `1+b+c` |
| `b11` | `1` |

Consequently,

\[
R(A)=ab(1+a)(1+b),\qquad R(B)=c(1+c),
\]

\[
M=c(1+c-2ab).
\]

This middle coefficient is negative whenever `2ab>1+c`. Taking `a=b=2,c=1` gives

\[
A=18+12x+12y+6xy,\qquad B=14+4x+4y+xy,
\]

and therefore

\[
R_{ef}(w)=36-6w+2w^2
=2(w-3/2)^2+63/2>0.
\]

More generally, the entire family admits the exact positive decomposition

\[
\boxed{R_{ef}(w)=(ab-cw)^2+ab(1+a+b)+cw^2+c(1+c)w.}
\]

The negative middle term comes from the square. Dropping or bounding each cross term separately by zero would destroy this cancellation.

## An unweighted `K5` example

On `K5`, take `e=02`, `f=13`, `g=01`, and give every other edge activity one. Exact enumeration gives

\[
A=82+46x+46y+24xy,\quad B=52+18x+18y+5xy,
\]

\[
R_{ef}(w)=148-2w+64w^2.
\]

Thus weighting is not required once five vertices are allowed. The discriminant is `-37884`, so this polynomial is also strictly positive.

## Independent exact checks and search scope

`forest_deletion_contraction_exact.py` implements two different exact calculations:

1. Union-find enumeration of every edge subset, retaining precisely the acyclic subsets.
2. Enumeration of all vertex partitions, multiplying the Kirchhoff spanning-tree determinant of each induced block, and summing over partitions. Every forest occurs exactly once by its component partition. Evaluating the three marked activities at zero and one and applying Boolean Möbius inversion extracts the eight coefficients.

Both computations give the eight coefficients displayed above, with no floating-point arithmetic. A further nontrivial positive integer weighting on `K5` gives Rayleigh coefficients `[25968,-7784,2424]`.

The script also exactly computes all sixty symbolic middle-coefficient polynomials in `K4`, treating the remaining three edge activities as independent indeterminates. The twelve cases with negative monomials correspond to disjoint marked pairs and a joining recursion edge, up to vertex relabeling. Their negative term is `-2abc`. The other cases have nonnegative coefficients. For a simple graph on at most three vertices, the only nontrivial case is the triangle, whose middle coefficient is `1`; forests without a cycle give zero. Thus four vertices are necessary and sufficient for a negative middle coefficient among simple graphs. This statement concerns the number of vertices; it makes no general claim about minimality by edge count over larger graphs or about multigraphs.

## Exact remaining frontier

Assume the two minor Rayleigh differences are nonnegative at the specified other activities, and put `r0=R(A)`, `r2=R(B)`. The quadratic

\[
r_0+wM+w^2r_2
\]

is nonnegative for every `w>0` if and only if

\[
\boxed{M\ge -2\sqrt{r_0r_2}.}
\]

The statement includes the cases where a minor Rayleigh difference is zero. For `r0,r2>0` and `M<0`, it follows by minimizing at `w=-M/(2r2)`; the zero cases follow by limits or direct inspection. Therefore a deletion/contraction proof needs a mixed discriminant bound, not merely the two minor inequalities. This bound is exactly equivalent to the remaining one-edge slice of the original conjecture and is not established here for arbitrary graphs. The explicit `K4` square proves it for the family above only.

No all-fugacity or new major open-problem solution is claimed by this calculation.
