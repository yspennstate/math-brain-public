# HARD7-03 idea before code — remove the common-window decoupling on the nested adjacent pairs

Runtime identity for this execution: GPT-5.6 Sol; reasoning level UNVERIFIED. This is not GPT-6 maximum and no such claim is made.

The 14:18Z checkpoint improved the four-step lazy-LPP certificate by replacing one arbitrary shared predecessor with the maximum over the full common predecessor window. The next loss is the deterministic decoupling

\[
\min(S+C,T+D)\ge R+\min(C,D),
\]

where `R` is a common-window maximum. For two of the three reflection classes of adjacent endpoints the windows are nested, so this loss can be removed exactly without solving the genuinely nonnested centre pair.

## Exact two-clock kernel

For deterministic `s<=t`, `C,D iid Exp(1)`, `q=1-theta` and `0<theta<1`, put `d=t-s`. Then

\[
\Pr\{\min(C,d+D)>u\}=\begin{cases}
e^{-u},&0\le u<d,\\
e^{d-2u},&u\ge d.
\end{cases}
\]

Hence

\[
\mathbb E e^{\theta\min(s+C,t+D)}
=\frac{e^{\theta s}}{1-\theta}
\left(1-\frac{\theta}{2-\theta}e^{-(1-\theta)(t-s)}\right).
\tag{I.1}
\]

This is strictly larger than the old common-window lower bound whenever the larger predecessor value is not a.s. equal to the smaller one.

## Nested pair classes

With the time-two variables from the preceding checkpoint,

- edge pair: `S=Y_{-2}`, `T=max(Y_{-2},Y_{-1})`;
- near-edge pair: `S=max(Y_{-2},Y_{-1})`, `T=max(Y_{-2},Y_{-1},Y_0)`.

Both satisfy `S<=T` pointwise. Thus (I.1) reduces each exact pair moment to

\[
P=\frac1q\left(\mathbb E e^{\theta S}-\frac{\theta}{2-\theta}\mathbb E e^{S-qT}\right).
\tag{I.2}
\]

For the edge pair the remaining transform is elementary and should equal

\[
E_{\rm edge}:=\mathbb E e^{S-qT}
=\frac{5\theta^2-14\theta+10}{(2-\theta)^4(1-\theta)^2}.
\tag{I.3}
\]

For the near-edge pair, condition on the three first-layer exponentials. If

\[
m=\max(A_{-1},A_0),\quad d=(A_0-A_{-1})_+,\quad D=(A_1-m)_+,
\]

then `S=m+U` with `U=max(E_2,E_1-d)`. Its density on `u>=0` is

\[
f_{U|d}(u)=(1+e^{-d})e^{-u}-2e^{-d}e^{-2u}.
\]

A direct one-clock integration gives

\[
\mathbb E[e^{U-q\max(U,D+E)}\mid d,D]
=e^{-qD}\left[(1+e^{-d})\left(\frac{D}{2-\theta}+\frac1q-\frac{q}{(2-\theta)^2}\right)-\frac{2e^{-d}}{2-\theta}\right]
+\frac{2q e^{-d-(2-\theta)D}}{(2-\theta)(3-\theta)}.
\tag{I.4}
\]

On each of the six strict order cones for `(A_{-1},A_0,A_1)`, `d` is one of `0,v,w,v+w`, `D` is either `0` or `w`, and the density is `exp(-3u-2v-w)`. Therefore every term in (I.4) integrates by three scalar Laplace transforms, with the only polynomial factor being at most one power of `w`. This gives an exact rational number at rational `theta` without numerical quadrature.

## Planned certificate

Keep the centre adjacent-pair class at the already certified common-window bound. Replace only the edge and near-edge classes by their exact values. Because each reflection class occurs twice and each adjacent pair is counted in two fourth-step predecessor windows, the pair subtraction should improve by

\[
\Delta C=4\big[(P_{\rm edge}-Q_{\rm edge})+(P_{\rm near}-Q_{\rm near})\big],
\]

where `Q_type=2 J_type/(2-theta)` is the previous common-window value. Then

\[
U_4^{\rm nested}=U_4^{\cap}-\frac{\Delta C}{1-\theta}.
\]

At the inherited exact parameter `theta=723/1250`, exploratory exact arithmetic predicts `Delta C` about `5.78488` and `U_4` about `870.633`, enough to lower the certified shape constant from `2.932597567` to about `2.92584` without touching the centre class. The checker will verify all of this with `Fraction` arithmetic before any theorem-level claim is made.

Methods for this run: B6 (deform from the common-window bound to the exact kernel), B23 (assume the residual pair dependence matters rather than vanishes), B28 (prove the exact nested/order-cone classes first rather than forcing the full nonnested centre pair).