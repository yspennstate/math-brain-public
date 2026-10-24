# Coefficient-one signed orbit ownership on physical reveal trees

All logarithms are base two. Put

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad q(0)=0.
\]

For a Boolean sign `f` and a set `X` of live physical coordinates, write

\[
E_X^f(S)=\sum_{A\subseteq X}\widehat f(S\cup A)^2
\quad(S\cap X=\varnothing)
\]

and define the influence-orbit potential

\[
\Theta_X(f)=\sum_{x\in X}q(\operatorname{Inf}_x(f))
 +\sum_{i\notin X}q(E_X^f(\{i\})). \tag{1}
\]

This replaces the earlier `|X| q(E_X(empty))` term. In particular

\[
\Theta_\varnothing(f)=\Phi(f):=
\sum_i q(\widehat f(\{i\})^2). \tag{2}
\]

The scalar `q` is increasing and concave on `[0,1]`. It is also
subadditive after truncation:

\[
q(\min\{1,a+b\})\le q(a)+q(b),\qquad 0\le a,b\le1. \tag{3}
\]

If `a+b<=1`, the linear terms cancel and (3) is
`a log(1/a)+b log(1/b)>=(a+b)log(1/(a+b))`. If `a+b>=1`, the
linear surplus `2(a+b-1)/ln2` and the two nonnegative logarithmic terms
pay `q(1)`.

## 1. Shared-product transport with coefficient one

Let `X,U,V` be pairwise disjoint, and let `f(X,U)` and `g(X,V)` be
Boolean. For `h=fg`,

\[
\boxed{\Phi(h)\le\Theta_X(f)+\Theta_X(g).} \tag{4}
\]

For a private coordinate `i in U`, define
`F_i(x)=E_u[f(x,u)chi_i(u)]` and `G_0(x)=E_v[g(x,v)]`. The singleton
coefficient of `h` is the empty Walsh coefficient of `F_iG_0`. Since
`|G_0|<=1`, Parseval gives

\[
\widehat h(\{i\})^2\le E_xF_i(x)^2=E_X^f(\{i\}). \tag{5}
\]

Monotonicity of `q` pays this term from `Theta_X(f)`; the `V` terms are
symmetric. For `x in X`, the pointwise pivotal event of `fg` is contained
in the union of the pivotal events of `f` and `g`, so

\[
\operatorname{Inf}_x(h)\le
\operatorname{Inf}_x(f)+\operatorname{Inf}_x(g). \tag{6}
\]

Also `hhat({x})^2<=Inf_x(h)`. Apply monotonicity and (3), then sum over
`x in X`, to obtain (4). The shared-coordinate coefficient is one and is
independent of `|X|`.

## 2. First physical revelation closes one packet

Let `x in X`, set `X'=X-{x}`, and write `f_sigma=f|_{x=sigma}`. Then

\[
\boxed{
E_\sigma\Theta_{X'}(f_\sigma)
\le\Theta_X(f)-q(\operatorname{Inf}_x(f)).} \tag{7}
\]

For every remaining shared coordinate `y in X'`, physical restriction
gives

\[
E_\sigma\operatorname{Inf}_y(f_\sigma)=
\operatorname{Inf}_y(f). \tag{8}
\]

Concavity of `q` contracts its term. For a private coordinate `i notin X`,
the two child `X'`-orbit energies have mean `E_X^f({i})` by the same
two-coefficient Parseval calculation used in the fixed-block theorem;
concavity again contracts. The `x` term is absent after revelation and
therefore supplies the explicit drop in (7). No dimension, depth, bias,
or block-size constant appears.

Iterating (7) proves full-revelation contraction and gives

\[
E_\xi\Phi(f|_{X=\xi})\le\Theta_X(f)
-\sum_{x\in X}E_{\text{prior reveals}}
q(\operatorname{Inf}_x(f_{\text{current}})). \tag{9}
\]

## 3. Exact signed ownership telescope for changing blocks

Consider any finite physical restriction tree. At an internal node `v`,
let `f_v` be its Boolean restriction, `w_v` its path probability, `Y_v`
the block inherited from its parent, and choose an arbitrary active block
`X_v` containing the queried coordinate `x_v`. At the root set
`Y_root=empty`. Define the signed opening cost

\[
O_v=\Theta_{X_v}(f_v)-\Theta_{Y_v}(f_v), \tag{10}
\]

and the revelation credit

\[
R_v=\Theta_{X_v}(f_v)
-\frac12\sum_{\sigma=\pm1}
\Theta_{X_v-\{x_v\}}(f_{v\sigma}). \tag{11}
\]

Each child inherits `Y_{v sigma}=X_v-{x_v}`. Equation (7) yields

\[
R_v\ge q(\operatorname{Inf}_{x_v}(f_v)). \tag{12}
\]

Direct cancellation of every parent-child potential gives the exact
identity

\[
\boxed{
\sum_{v\text{ internal}}w_v(R_v-O_v)
=\Phi(f)-\sum_{\ell\text{ leaf}}w_\ell
\Theta_{Y_\ell}(f_\ell).} \tag{13}
\]

Thus arbitrary changes of overlap block are allowed, but their costs must
remain signed. A coordinate may leave and re-enter active blocks; no
positive recharge is created because all intermediate potentials cancel.
On a complete physical reveal tree, leaves are constants and the terminal
term is zero, so the total is exactly `Phi(f)`.

The earlier alternating `X={y,x}`, `Y={y,z}` witness is consistent with
(13): its positive variations diverge only after negative refunds are
discarded. The signed openings telescope.

## 4. Explicit sufficient U-drift criterion

This ledger is not merely notation because it isolates one strictly smaller
unpaid inequality. Suppose absolute `K,lambda<infinity`, `lambda>=0`, exist
such that every Boolean `f` admits a complete physical restriction tree and
adapted blocks as above for which every internal node satisfies

\[
\Delta_{x_v}U(f_v)
\le K\operatorname{Inf}_{x_v}(f_v)
+\lambda(R_v-O_v). \tag{D}
\]

Summing (D), using the exact restriction telescopes for `U` and influence,
and applying (13), gives

\[
U(f)\le KI(f)+\lambda\Phi(f). \tag{14}
\]

For `0<=t<=1`,

\[
q(t^2)=\frac{2t^2}{\ln2}(\ln(1/t)+1)
\le\frac{2t}{\ln2}. \tag{15}
\]

Booleanity gives `|fhat({i})|<=Inf_i(f)`, so (2) and (15) imply

\[
\Phi(f)\le\frac2{\ln2}I(f). \tag{16}
\]

Consequently (D) proves the universal endpoint

\[
U(f)\le\left(K+\frac{2\lambda}{\ln2}\right)I(f), \tag{17}
\]

and the reviewed Theorem G then gives

\[
H(f)\le
\left(2+2K+\frac{4\lambda}{\ln2}\right)I(f). \tag{18}
\]

Thus the remaining gap is precisely the nodewise analytic domination (D),
with `Delta U=B-Gamma+KL` and all signs retained. The ownership, changing
overlap, terminal reserve, and nonreuse accounting in (D) are now proved.
No claim is made that (D), universal GU, or FEI has been proved.

