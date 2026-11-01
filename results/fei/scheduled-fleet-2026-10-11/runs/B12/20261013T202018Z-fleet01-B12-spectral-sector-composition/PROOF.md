# Spectral-sector composition without an influence-density floor

All logarithms and entropies in this note are base two.  Let `u,v` be
Boolean signs on one physical block and let `h` be a Boolean sign on a
disjoint selector block.  Define

\[
 F(x,z)=\begin{cases}u(z),&h(x)=-1,\\v(z),&h(x)=+1.\end{cases}
\]

Put

\[
 r=\Pr[h=+1],\quad q=1-r,\quad \mu=2r-1,\quad
 \delta=1-\mu^2=4qr,
\]
and
\[
 \beta=\Pr[u\ne v]=\frac{1-\langle u,v\rangle}{2}.
\]
After swapping the labels of `u,v` and replacing `h` by `-h` if necessary,
we assume `0<=r<=1/2`.

## 1. Exact sector chain rule

Write `u_T,v_T` for the Fourier coefficients of the endpoints and set

\[
 c_T=qu_T+rv_T,\qquad d_T=\frac{v_T-u_T}{2},
 \qquad w_T=qu_T^2+rv_T^2.
\]

The selector-empty coefficient of `F` is `c_T`; for nonempty selector
frequency `S` it is `d_T \widehat h(S)`.  Coefficientwise,

\[
 \boxed{c_T^2+\delta d_T^2=w_T}. \tag{1}
\]

Let `s=delta beta`, so `sum_T delta d_T^2=s`.  The spectral law of `F`
may first choose `T` with law `w`, then choose the empty/nonempty selector
sector, and in the nonempty sector choose `S` from the normalized nonconstant
spectrum of `h`.  Hence

\[
 \begin{aligned}
 H(F)=H(w)&+\sum_Tw_T h_2\!\left(\frac{\delta d_T^2}{w_T}\right)\\
 &+\beta\,[H(h)-\psi_2(\mu)]+s\log_2\delta,                 \tag{2}
 \end{aligned}
\]
where zero-mass terms are omitted and
`psi_2(t)=t^2 log_2(1/t^2)`.  Concavity of binary entropy gives

\[
 \sum_Tw_T h_2(\delta d_T^2/w_T)\le h_2(s),                \tag{3}
\]
while the last two terms in (2) are at most `beta H(h)`.

The mixture entropy has the exact form

\[
 H(w)=qH(u)+rH(v)+J_r(p_u,p_v),                             \tag{4}
\]
where `p_u(T)=u_T^2`, `p_v(T)=v_T^2`, and `J_r` is weighted
Jensen--Shannon information.

## 2. Coherent mixture information

If `beta<=1/2`, put `rho=<u,v>=1-2 beta`.  Measuring the two unit Fourier
vectors `(u_T)_T,(v_T)_T` in the coordinate basis produces `p_u,p_v`.
Monotonicity of relative entropy under this measurement bounds their
Jensen--Shannon information by the entropy of the two-state mixture:

\[
 J_r(p_u,p_v)\le h_2(\lambda),\qquad
 \lambda=\frac{1-\sqrt{1-\delta(1-\rho^2)}}2.               \tag{5}
\]

For completeness, the average of the two rank-one projectors has only two
nonzero eigenvalues `lambda,1-lambda`; (5) is precisely the usual
data-processing proof of the binary Holevo bound and uses no dimension
assumption.

Now

\[
 \lambda(1-\lambda)=\delta\beta(1-\beta)=s(1-\beta).
\]
Since `0<=s<=beta<=1/2`,
`s(1-s)>=s(1-beta)=lambda(1-lambda)`.  The map `t(1-t)` and `h_2(t)` are
increasing on `[0,1/2]`; therefore

\[
 \boxed{J_r(p_u,p_v)\le h_2(s)\quad(\beta\le1/2).}           \tag{6}
\]

If `beta>=1/2`, the elementary label-entropy bound instead gives

\[
 J_r(p_u,p_v)\le h_2(r)\le2\beta h_2(r).                   \tag{7}
\]

## 3. Two scalar entropy payments

For `a,b in [0,1]`,

\[
 \boxed{h_2(ab)\le a h_2(b)+b h_2(a).}                     \tag{8}
\]

One proof takes independent Bernoulli variables `A,B` with parameters
`a,b` and `Z=AB`.  Then the difference between the right and left sides is
`I(A;B|Z)-I(A;B)=I(A;B|Z)>=0`.

Also, for `0<=r<=1/2` and `delta=4r(1-r)`,

\[
 \boxed{h_2(\delta)\le4h_2(r).}                            \tag{9}
\]

When `delta<=1/2`, use `delta<=4r`, monotonicity on `[0,1/2]`, and
concavity with `h_2(0)=0` to obtain `h_2(delta)<=h_2(4r)<=4h_2(r)`.
When `delta>1/2`, necessarily `r>1/8`; then
`4h_2(r)>=4r log_2(1/r)>1>=h_2(delta)`.

Applying (8)--(9) to `s=delta beta` gives

\[
 h_2(s)\le\delta h_2(\beta)+4\beta h_2(r).                 \tag{10}
\]

Combining (2)--(10), in the first regime `J_r+h_2(s)<=2h_2(s)`;
in the second, `J_r+h_2(s)<=delta h_2(beta)+6 beta h_2(r)`.
Thus both regimes satisfy the single uniform bound

\[
 \boxed{
 H(F)\le qH(u)+rH(v)+\beta H(h)
       +2\delta h_2(\beta)+8\beta h_2(r).}                 \tag{11}
\]

No endpoint dimension, support size, influence density, selector bias floor,
or correlation gap appears in (11).

## 4. Payment by physical influence

The physical influence decomposes exactly:

\[
 \boxed{I(F)=qI(u)+rI(v)+\beta I(h).}                       \tag{12}
\]

For data coordinates this follows by conditioning on the selector branch.
For a selector coordinate, `F` flips exactly when `h` flips and `u(z)ne v(z)`.

The edge-isoperimetric inequality on the cube implies, for a Boolean event of
density `t`,

\[
 h_2(t)\le2m\log_2(1/m)\le I(\text{event sign}),
 \qquad m=\min(t,1-t).                                      \tag{13}
\]

Apply (13) to the `+1` event of `h` and to the disagreement sign `uv`.
Since a flip of `uv` forces a flip of `u` or `v`,

\[
 h_2(r)\le I(h),\qquad h_2(\beta)\le I(uv)\le I(u)+I(v).   \tag{14}
\]

Finally, with `r<=q`,

\[
 \delta[I(u)+I(v)]
 \le4[qI(u)+rI(v)].                                         \tag{15}
\]

Substitution in (11) proves the following closure theorem.

**Theorem.**  If one constant `C` satisfies

\[
 H(u)\le CI(u),\qquad H(v)\le CI(v),\qquad H(h)\le CI(h),
\]

then

\[
 \boxed{H(F)\le(C+8)I(F).}                                 \tag{16}
\]

The tax `8` is absolute and independent of endpoint dimension, selector
dimension, bias, disagreement density, weight groups, and correlation gap.

## 5. Scope and unpaid hierarchy step

Equation (16) covers every genuine Boolean slice pair and every genuine
Boolean selector on fresh disjoint physical blocks.  It strictly removes the
positive outer-influence-density hypothesis used by the preceding tensor
example.  It also survives constant endpoints, rare selectors, nearly equal
or nearly opposite endpoints, and arbitrary low-influence functions padded by
dummy coordinates.

It does **not** prove full FEI.  Iterating (16) naively pays the additive tax
at each compositional depth, and the proof uses disjoint selector/data blocks.
For an actual changing adaptive hierarchy the remaining obligation is to
telescope the two explicit local reserves

\[
 2\delta_v h_2(\beta_v),\qquad 8\beta_v h_2(r_v),            \tag{17}
\]

against one source-influence/terminal-reserve budget, rather than recharge
them at every node, and then survive shared-coordinate overlap.  This is the
same one-use obstruction as the changing `M(a_v,b_v)` reserve in A057, now
expressed directly in endpoint disagreement and selector activation entropy.

