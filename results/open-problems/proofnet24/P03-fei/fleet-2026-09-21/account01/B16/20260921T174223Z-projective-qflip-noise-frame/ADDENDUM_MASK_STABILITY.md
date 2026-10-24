# Addendum — source stability under compiler masks and exact one-subcube plaquette cost

**Status:** proved local identities; unrestricted FEI remains **OPEN**. No novelty claim.

The parity-current handoff identifies a precise remaining difficulty: syndrome translation changes the base Boolean phase, so one cannot average a q-flip source theorem over translated compiler states merely by asserting that influence is unchanged. The following identities replace that qualitative warning by an exact local error term.

## 1. `B16-PLAQUETTE-MASK-LIPSCHITZ`

For a Boolean phase `h` and translations `u,v`, define the plaquette sign
\[
Q_h(x;u,v)=h(x)h(x+u)h(x+v)h(x+u+v)
\]
and the dependent-face transport probability
\[
P_h(u,v)=\Pr_X\{Q_h(X;u,v)=-1\}.
\]
For two phases `f,m`,
\[
Q_{fm}(x;u,v)=Q_f(x;u,v)Q_m(x;u,v).
\tag{1.1}
\]
Thus the bad-plaquette indicator for `fm` is the XOR of the two bad-plaquette indicators. Pointwise,
\[
|1_{\{Q_{fm}=-1\}}-1_{\{Q_f=-1\}}|
\le1_{\{Q_m=-1\}}.
\]
Averaging gives the exact Lipschitz estimate
\[
\boxed{
|P_{fm}(u,v)-P_f(u,v)|\le P_m(u,v).
}
\tag{1.2}
\]
In particular, if the mask is unfrustrated on that face, `P_m(u,v)=0`, then the local B18 transport kernel is **exactly invariant** under multiplication by the mask.

Combining (1.2) with the projective plaquette theorem from the companion addendum gives
\[
\boxed{
|P_{fm}(u,v)-P_f(u,v)|
\le2\min\{\beta_m(u),\beta_m(v),\beta_m(u+v)\}.
}
\tag{1.3}
\]
This is substantially more local than trying to compare the total influences of `f` and `fm`.

## 2. Multiplicative projective triangle inequality

The same error-variable argument gives, for every translation `u`,
\[
\boxed{
\beta_{fm}(u)\le\beta_f(u)+\beta_m(u).
}
\tag{2.1}
\]
Indeed, choose optimal projective derivative signs for `f` and `m`; the derivative error of their product is the XOR of the two derivative errors. Consequently
\[
\boxed{J(fm)\le J(f)+J(m).}
\tag{2.2}
\]
For a product of compiler masks `m=prod_j g_j^{z_j}`,
\[
\beta_m(u)\le\sum_{j:z_j=1}\beta_{g_j}(u),
\tag{2.3}
\]
but (1.2) is often sharper because a mask can have nonzero edge cost while being exactly unfrustrated on the particular dependent face used by the compiler current.

## 3. Exact plaquette probability of a one-subcube defect

The ordered-min dual generators are one-subcube defects, so their local mask cost can be computed exactly.

Let `F subseteq [n]` have size `c`, fix `b in F_2^F`, and let
\[
g_{F,b}(x)=1-2\,1_{\{x_F=b\}}.
\tag{3.1}
\]
For translations `u,v`, let
\[
r_F(u,v)=\dim_{F_2}\operatorname{span}\{u_F,v_F\}\in\{0,1,2\}.
\]

### Theorem — `B16-SUBCUBE-PLAQUETTE-RANK-TWO`

\[
\boxed{
P_{g_{F,b}}(u,v)
=
\begin{cases}
2^{2-c},&r_F(u,v)=2,\\
0,&r_F(u,v)\le1.
\end{cases}
}
\tag{3.2}
\]

### Proof

The four vertices of the `(u,v)` face project to the affine coset
\[
x_F+\operatorname{span}\{u_F,v_F\}.
\]
If the rank is two, the four projected vertices are distinct. The face contains an odd number of points of the cell `x_F=b` exactly when this affine two-plane contains `b`, in which case exactly one of the four vertices lies in the subcube. A uniform `x_F` yields a coset containing `b` with probability `4/2^c=2^{2-c}`.

If the rank is one, the projection has two values, each repeated twice among the four face vertices, so the intersection count with the cell is `0` or `2`. If the rank is zero it is `0` or `4`. In either case the parity is even and the plaquette sign is `+1`. QED.

Thus a one-subcube compiler mask perturbs a local q-flip transport kernel **only when the two physical directions remain linearly independent after restriction to the fixed coordinates of that generator**. Its exact perturbation probability is then `2^{2-c}`.

For comparison, when `c>=2` the folded physical influence of this generator is
\[
J(g_{F,b})=c\,2^{1-c},
\tag{3.3}
\]
so an active rank-two plaquette costs exactly
\[
P_g(u,v)=\frac{2}{c}J(g).
\tag{3.4}
\]
This is a rank-sensitive factor that is invisible to a total-mask-influence comparison.

## 4. Products of randomly selected generator masks

Let `M=prod_j g_j^{Z_j}` where the selectors `Z_j` are independent Bernoulli variables with parameters `theta_j`. For fixed `x,u,v`, let
\[
a_j(x;u,v)=1_{\{Q_{g_j}(x;u,v)=-1\}}.
\]
Conditional on the physical face,
\[
1_{\{Q_M=-1\}}
\]
is the parity of the selected active generator defects. Hence
\[
\boxed{
\Pr_Z\{Q_M(x;u,v)=-1\}
=
\frac{1-\prod_{j:a_j=1}(1-2\theta_j)}2.
}
\tag{4.1}
\]
This exact expression preserves cancellations among multiple selected mask defects. The crude but sometimes useful consequence is
\[
\boxed{
\mathbb E_Z P_M(u,v)
\le\sum_j\theta_j P_{g_j}(u,v).
}
\tag{4.2}
\]
For one-subcube generators, (3.2) turns the right side into an explicit weighted count of rank-two restrictions:
\[
\mathbb E_Z P_M(u,v)
\le
\sum_{j:\,r_{F_j}(u,v)=2}\theta_j 2^{2-c_j}.
\tag{4.3}
\]

## 5. Consequence for the syndrome-average blocker

Equation (1.2) shows that the account04 warning can be localized precisely:

> changing the base phase under syndrome translation is harmless on a dependent q-flip face except for the **plaquette frustration of the translating mask on that same face**.

For the actual ordered-min dual generators, that mask frustration is the explicit rank-two quantity (3.2). Therefore the next compiler-side test is no longer a generic comparison of translated total influences. It is the following sharper question:

> After the signed same-syndrome aggregation and the two inverse-number current weights are inserted, is the accumulated rank-two mask cost
> \[
> \sum \text{(current weight)}\,2^{2-c_j}
> 1_{\{r_{F_j}(u,v)=2\}}
> \]
> controlled by the retained R16 first-separation/moment bank or by the physical projective incidence budget?

If yes, syndrome/Walsh averaging can be transferred back to the original source kernel with a dimension-free error. If this weighted rank-two cost grows on authentic compiler coefficients, it gives a precise obstruction and shows where further signed cancellation must be retained.

A brute-force falsification check of (3.2) over all coordinate subcubes, base patterns and translation pairs for dimensions `2<=n<=5` passed; the proof above is exact and does not rely on the check.
