# R15 idea note — projective Gram-polygon dual

Date: 2026-09-19 UTC. Status at creation: IDEA / NOT YET PROVED.

The previous full-support dimension barrier uses only two block test vectors in the projective fourth-order inequality. A potentially sharp way to finish that local linear-algebra subsystem is to change categories from the unknown PSD contact Hessian to a Gram-vector closure problem.

Suppose a candidate exact contact has `H >= 0`, `H h = 0`, diagonal `d_i`, cubic covector `b`, and projective fourth-order budget `b^T H^+ b <= C`. Since `h` is in `ker H` and `b` is in `ran H`, `h.b=0`. The rank-one downdate

`K = H - b b^T / C`

should be PSD whenever the projective budget holds. It has diagonal

`e_i = d_i - b_i^2/C`

and still kills `h`. Writing `K` as a Gram matrix turns `K h=0` into a closed-vector-polygon condition: there must exist vectors of lengths `|h_i| sqrt(e_i)` summing to zero. Hence the exact obstruction ought to be

`e_i >= 0` for every i, and `2 max_i |h_i| sqrt(e_i) <= sum_i |h_i| sqrt(e_i)`.

Conversely, if that polygon closes, build a Gram matrix `K` with the required diagonal and kernel and set `H=K+b b^T/C`; generalized Schur complement should give `b in ran H` and `b^T H^+ b <= C`. If this converse is correct, the polygon test is not merely another inequality: it exactly characterizes the entire PSD/diagonal/null/projective subsystem before coefficient nonnegativity and global majorization are imposed.

For the F0111 two-level null curve,

`h=m(1+delta) 1_J - m(1-delta) 1_K`,
`D_h^4 log S = m^4 R`,
`b_i=m^2 r_i t_J` on J and `b_i=m^2 r_i t_K` on K,
`d_i=r_i(1-r_i)`,

so taking `C=m^4 R/3` predicts residual diagonals

`e_i=r_i(1-A_J r_i)` on J, `A_J=1+3 t_J^2/R`,
`e_i=r_i(1-A_K r_i)` on K, `A_K=1+3 t_K^2/R`.

This recovers the preceding coordinate/block caps and should add a genuinely non-aggregated polygon obstruction. In particular, if one active sign block is a singleton, Cauchy on the other block should turn the polygon inequality into an explicit stronger support-size lower bound.

Next: prove both directions carefully, then specialize to the exact rational middle-branch point `delta=1/2, z=-3/5` to see whether the singleton support lower bound is strictly stronger than the old coordinate-cap count. No checker unless the symbolic specialization produces a claim worth validating.