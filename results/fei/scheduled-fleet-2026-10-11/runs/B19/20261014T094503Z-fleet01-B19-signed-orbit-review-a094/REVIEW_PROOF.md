# Independent reconstruction of signed orbit ownership

Target: `B05-A023-SIGNED-ORBIT-OWNERSHIP-v1` at canonical commit
`e1a663f08e373c8911cdfc7272985932777dbbe4`.

All logarithms are base two and

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad q(0)=0.
\]

## 1. Scalar input

On `(0,1]`,

\[
q'(t)=\log_2(1/t)+1/\ln2>0,
\qquad q''(t)=-1/(t\ln2)<0.
\]

Thus `q` is increasing and concave. For `a+b<=1`,

\[
q(a)+q(b)-q(a+b)
=a\log_2\frac{a+b}{a}+b\log_2\frac{a+b}{b}\ge0.
\]

For `a+b>=1`,

\[
q(a)+q(b)-q(1)
=a\log_2(1/a)+b\log_2(1/b)
+\frac{2(a+b-1)}{\ln2}\ge0.
\]

Therefore `q(min(1,a+b))<=q(a)+q(b)`.

## 2. Product transport

Let `f(X,U),g(X,V)` be Boolean with `U,V,X` pairwise disjoint and put
`h=fg`. For `i in U`, conditioning on `X` gives

\[
\widehat h(\{i\})=E_X[F_i(X)G_0(X)],
\]

where `F_i=E_U[f chi_i]` and `|G_0|<=1`. Cauchy--Schwarz and Parseval give

\[
\widehat h(\{i\})^2\le E_XF_i^2
=\sum_{A\subseteq X}\widehat f(A\cup\{i\})^2.
\]

The private terms are therefore paid by the corresponding orbit energies.
For `x in X`, the product changes across an `x`-edge only if at least one
factor changes, hence

\[
Inf_x(h)\le Inf_x(f)+Inf_x(g),
\qquad \widehat h(\{x\})^2\le Inf_x(h).
\]

Monotonicity and scalar subadditivity prove

\[
\Phi(h)\le\Theta_X(f)+\Theta_X(g).
\]

No independence of the shared variables is used, but disjointness of the
private blocks is essential in the conditional factorization.

## 3. Physical reveal contraction

For `x in X`, set `X'=X-{x}`. If `y in X'`, direct edge counting gives

\[
E_\sigma Inf_y(f|x=\sigma)=Inf_y(f).
\]

For `i notin X`, write parent Fourier coefficients in pairs `(a_B,b_B)`
according to absence/presence of `x`. The child orbit energy is

\[
Z_\sigma=\sum_{B\subseteq X'}(a_B+\sigma b_B)^2,
\qquad E_\sigma Z_\sigma=\sum_B(a_B^2+b_B^2)=E_X^f(\{i\}).
\]

Jensen contracts every surviving term, while the queried coordinate term
`q(Inf_x(f))` disappears. This proves

\[
E_\sigma\Theta_{X'}(f|x=\sigma)
\le\Theta_X(f)-q(Inf_x(f)).
\]

## 4. Signed tree identity

At node `v`, let `Y_v` be the inherited block, `X_v` the chosen active
block containing the query `x_v`, and let each child inherit
`Y_{v sigma}=X_v-{x_v}`. With

\[
O_v=\Theta_{X_v}(f_v)-\Theta_{Y_v}(f_v),
\]

\[
R_v=\Theta_{X_v}(f_v)
-\frac12\sum_\sigma\Theta_{Y_{v\sigma}}(f_{v\sigma}),
\]

one has identically

\[
R_v-O_v=\Theta_{Y_v}(f_v)
-\frac12\sum_\sigma\Theta_{Y_{v\sigma}}(f_{v\sigma}).
\]

Multiplication by path weights and summation cancels every internal
potential, including the root opening from `Y_root=empty`. Hence

\[
\sum_vw_v(R_v-O_v)=\Phi(f)-
\sum_\ell w_\ell\Theta_{Y_\ell}(f_\ell).
\]

This verifies that re-entry and branch-dependent block changes do not
double-spend credit when the signs are retained.

## 5. Endpoint implication

On a complete tree, leaf functions are constants, so both `U` and terminal
`Theta` vanish. The standard restriction identities give

\[
U(f)=\sum_vw_v\Delta_{x_v}U(f_v),
\qquad I(f)=\sum_vw_vInf_{x_v}(f_v).
\]

Therefore the still-unproved nodewise estimate

\[
\Delta_{x_v}U(f_v)\le KInf_{x_v}(f_v)+\lambda(R_v-O_v)
\]

would imply `U<=KI+lambda Phi`. For Boolean `f`,
`|fhat({i})|<=Inf_i(f)`, while

\[
q(t^2)=\frac{2t^2}{\ln2}(\ln(1/t)+1)
\le\frac{2t}{\ln2}.
\]

Thus `Phi<=2I/ln2`, giving the claimed U and FEI constants. This is a
correct sufficient implication, not a proof of the nodewise estimate and
not a GU' theorem.

## 6. Reviewer-supplied point-defect stress test

Let `d_r` equal `-1` at one point of the `r`-cube and `+1` elsewhere, and
put `epsilon=2^{1-r}`. Then

\[
Inf_i(d_r)=\epsilon,\qquad
|\widehat d_r(\{i\})|=\epsilon,
\qquad I(d_r)=r\epsilon.
\]

For the full block `X=[r]`,

\[
\Theta_X(d_r)=rq(\epsilon),
\qquad \Phi(d_r)=rq(\epsilon^2).
\]

Consequently

\[
\frac{\Theta_X(d_r)}{I(d_r)}
=\frac{q(\epsilon)}{\epsilon}
=r-1+\frac2{\ln2}\longrightarrow\infty, \tag{P1}
\]

and the root opening itself obeys

\[
\frac{\Theta_X(d_r)-\Phi(d_r)}{I(d_r)}
=r-1+\frac2{\ln2}
-\epsilon\left(2r-2+\frac2{\ln2}\right)\to\infty. \tag{P2}
\]

Thus `Theta_X` and `R_v` are not free `O(I)` credits. The accepted theorem
depends essentially on subtracting the signed opening `O_v`. Any consumer
that discards `-O_v`, takes positive parts, or charges `Theta_X` directly
revives the rare logarithm and is invalid. This is a scope obstruction, not
a defect in the signed theorem.

For a stopped rather than complete tree, both the terminal `Theta` in the
signed identity and terminal `U` in the restriction telescope must remain.
No leaf FEI hypothesis is supplied by this review.

