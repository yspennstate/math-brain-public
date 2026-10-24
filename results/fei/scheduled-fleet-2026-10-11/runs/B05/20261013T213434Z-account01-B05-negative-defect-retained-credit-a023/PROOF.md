# Negative point-defect towers: uniform retained endpoint

All logarithms are base two.  For a Boolean sign `f`, write

\[
U(f)=\sum_S\widehat f(S)^2\log_2
\frac{\sum_{T\supseteq S}\widehat f(T)^2}{\widehat f(S)^2},
\qquad I(f)=\sum_S|S|\widehat f(S)^2.
\]

## Theorem

Let `Q_r` be `+1` except at one point of the `r`-cube, put `N_r=-Q_r`,
and let

\[
A(q)(z,x)=\begin{cases}1,&z=+1,\\q(x),&z=-1.\end{cases}
\]

Take all blocks below on fresh disjoint physical variables.  For any Boolean
base `P`, a fresh fair character `w`, and any sequence `r_k>=2`, define

\[
F_1=A(wP),\qquad F_k=A(N_{r_k}F_{k-1})\quad(k\ge2).
\tag{1}
\]

Then

\[
\boxed{U(P)\le\frac{16}{9}I(P)
\Longrightarrow U(F_d)\le\frac{16}{9}I(F_d)}
\tag{2}
\]

for every finite depth and every rank sequence.  Moreover, for every finite
adaptive or pruned restriction tree on physical variables of `F_d`, with leaf
weights `w_l`, and every common Boolean factor `h` on a disjoint block,

\[
\boxed{U(F_dh)-\sum_lw_lU((F_d)_lh)\le\frac{16}{9}I(F_d).}
\tag{3}
\]

Consequently `H(F_d)<=50 I(F_d)/9` by `H<=2I+2U`.

## 1. Negative point-defect block

Put `p=2^{-r}` and `beta=1-2p`.  The spectrum of `N_r` has empty
coefficient `-beta` and every nonempty coefficient has magnitude `2p`.
Therefore

\[
I(N_r)=2rp,
\qquad
U(N_r)=\beta^2\log_2(1/\beta^2)+2rp\beta.
\tag{4}
\]

At `r=2` the ratio is one.  At `r=3`,

\[
\frac{U(N_3)}{I(N_3)}
=\frac34\left(1+\log_2\frac{16}{9}\right)<\frac32.
\]

For `r>=4`, the elementary inequality
`-ln beta <= (1-beta)/beta=2p/beta` gives

\[
\frac{U(N_r)}{I(N_r)}
\le\beta+\frac{2\beta}{r\ln2}
<1+\frac{1}{2\ln2}<\frac74<\frac{16}{9}.
\tag{5}
\]

The penultimate inequality uses `ln2>2/3`, obtained for example by the first
two positive terms of the atanh series
`ln2=2(1/3+1/(3^3 3)+...)>56/81>2/3`.

## 2. Exact activation recurrence and the sign benefit

The already independently accepted half-activation identity is

\[
U(A(q))=\frac12U(q)+R(Eq),
\qquad
I(A(q))=\frac12I(q)+\frac{1-Eq}{2},
\tag{6}
\]

where `R(t)<=1` on `[-1,0]`.  Both `U` and `I` add under disjoint products.
Let `m_k=E F_k`.  The first balancing character gives

\[
m_1=\frac12,
\quad U(F_1)=1+\frac12U(P),
\quad I(F_1)=1+\frac12I(P).
\tag{7}
\]

For `k>=2`, with `beta_k=1-2^{1-r_k}` and
`s_k=beta_k m_{k-1}`,

\[
\begin{aligned}
m_k&=\frac{1-s_k}{2},\\
U(F_k)&=\frac12U(F_{k-1})+\frac12U(N_{r_k})+R(-s_k),\\
I(F_k)&=\frac12I(F_{k-1})+\frac12I(N_{r_k})+\frac{1+s_k}{2}.
\end{aligned}
\tag{8}
\]

Because `1/2<=beta_k<1`, induction gives

\[
\frac14\le m_k\le\frac12,
\qquad \frac18\le s_k\le\frac12.
\tag{9}
\]

This lower bound is the credit absent from a one-node coarse estimate: for
`c=16/9`,

\[
R(-s_k)\le1\le c\frac{1+s_k}{2}.
\tag{10}
\]

## 3. Endpoint induction

At the first level, for every `c>=1`,

\[
U(F_1)-cI(F_1)
=\frac12(U(P)-cI(P))+(1-c)\le0.
\]

At every later level, (5), (8), and (10) imply

\[
U(F_k)-cI(F_k)
\le\frac12(U(F_{k-1})-cI(F_{k-1}))\le0
\]

at `c=16/9`.  This proves (2).  The constant is independent of base
dimension, ranks, biases `-beta_k`, the product activation probability,
depth, or correlation gap `1-beta_k`.

The method also explains the improvement over the prior negative-defect
endpoint `56/27`: it uses the sharp negative-side scalar cap `R<=1` together
with the uniform physical selector credit `s_k>=1/8`, rather than reflecting
to the weaker positive-side scalar bound.

## 4. Complete signed tree telescope

For any finite adaptive or pruned physical restriction tree,

\[
\sum_{v\text{ internal}}w_v\left(
U((F_d)_vh)-\frac{U((F_d)_{v,+}h)+U((F_d)_{v,-}h)}2\right)
=U(F_dh)-\sum_lw_lU((F_d)_lh).
\tag{11}
\]

Since the same disjoint `h` occurs at every node, tensor additivity cancels
its `U(h)` exactly.  Nonnegativity of leaf `U` and (2) then give (3).

This is an endpoint signed telescope.  It does not prove nonnegative charges,
a first-revelation stopping rule, or single-use ownership of individual
`mu[log(1/mu)-D]` credits.  It also does not cover biased outer selectors,
reused variables, or changing, overlapping, or leaf-dependent terminal cores.
Those remain the exact A023 obstruction.
