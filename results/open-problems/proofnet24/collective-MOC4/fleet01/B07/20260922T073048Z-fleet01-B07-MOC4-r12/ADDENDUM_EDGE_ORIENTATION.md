# Addendum — the continuous strict-margin allocation collapses to eight edge orientations

This strengthens Section 6 of `REPORT.md` without changing its verdict.

For each row plane `alpha`, retain the exact covariance inverse

\[
G_\alpha=\begin{pmatrix}g_{11}^{(\alpha)}&g_{12}^{(\alpha)}\\g_{12}^{(\alpha)}&g_{22}^{(\alpha)}\end{pmatrix}>0
\]

and put

\[
\widehat G_\alpha=
\begin{pmatrix}g_{11}^{(\alpha)}&|g_{12}^{(\alpha)}|\\|g_{12}^{(\alpha)}|&g_{22}^{(\alpha)}\end{pmatrix}.
\]

Because replacing the off-diagonal entry by its absolute value leaves the determinant unchanged,
`widehat G_alpha` is positive definite.  If the two row-edge anisotropy norms incident to `alpha`
are `u_e^(alpha),u_f^(alpha)`, Cauchy--Schwarz in the exact reconstruction identity gives

\[
E_\alpha\le
(u_e^{(\alpha)},u_f^{(\alpha)})\widehat G_\alpha
\binom{u_e^{(\alpha)}}{u_f^{(\alpha)}}.                    \tag{A1}
\]

For each unordered row edge `e={alpha,gamma}`, the genuine pair-Hessian theorem gives

\[
u_e^{(\alpha)}+u_e^{(\gamma)}\le 2\sqrt{Q_e}.          \tag{A2}
\]

The right side of the sum of (A1) is a convex function of the six nonnegative endpoint variables.
The feasible set is the direct product of three triangles

\[
\{(u_e^{(\alpha)},u_e^{(\gamma)}):u,v\ge0,\ u+v\le2\sqrt{Q_e}\}.
\]

A convex function on this compact polytope attains its maximum at a vertex.  Moreover every
quadratic in (A1) is coordinatewise nondecreasing on the nonnegative quadrant, so a maximizing
vertex cannot leave an edge budget unused.  Consequently **each of the three pair reserves is
allocated entirely to one of its two endpoint rows**.  There are only `2^3=8` possibilities.

Fix the local edge ordering

- row 1: `(12,13)`,
- row 2: `(12,23)`,
- row 3: `(13,23)`.

For an orientation `omega` of the three edges of `K_3`, let `chi_{alpha,e}(omega)=1` when edge `e`
is oriented toward row `alpha`, and define

\[
v_1=(\chi_{1,12}\sqrt{Q_{12}},\chi_{1,13}\sqrt{Q_{13}}),
\]
\[
v_2=(\chi_{2,12}\sqrt{Q_{12}},\chi_{2,23}\sqrt{Q_{23}}),
\]
\[
v_3=(\chi_{3,13}\sqrt{Q_{13}},\chi_{3,23}\sqrt{Q_{23}}).
\]

Then the complete row-side continuous resource allocation obeys the finite ceiling

\[
\boxed{
\mathcal E
\le 4\max_{\omega\in\operatorname{Orient}(K_3)}
\sum_{\alpha=1}^3 v_\alpha(\omega)^T\widehat G_\alpha v_\alpha(\omega).
}                                                               \tag{A3}
\]

There are exactly eight quantities on the right.  The same construction on block columns gives a
second eight-value ceiling, and the minimum of the row and column ceilings is valid for the same
true exterior-square point.

Thus no continuous optimization over pair-Hessian reserve allocation remains at this stage.  Once
the spectra and the six `Q` values are fixed, the best consequence obtainable from the pairwise
anisotropy norms plus the exact covariance reconstruction is an eight-case source-exact check per
side.  Any further improvement must use information not present in the separate pair norm bounds,
most naturally the signs/angles of the two traceless-Gram vectors meeting at a row, the full-Hessian
cross-root coupling, or the endpoint/subgroup support roofs.

This also identifies the sharp next local datum needed from the campaign lead: a true-unitary
constraint on the cross-inner-products
`<W_{alpha gamma}^{(alpha)},W_{alpha delta}^{(alpha)}>_rho` can improve (A3), whereas another
separate bound on their norms cannot.
