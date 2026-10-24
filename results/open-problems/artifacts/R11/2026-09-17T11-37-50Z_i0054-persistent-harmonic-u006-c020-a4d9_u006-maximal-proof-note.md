# R11 I0054 / U006 — maximal Poisson-equation argument for random jump intervals

This note makes explicit the uniform-in-time step in U006. It is part of the C020 proof package, not a second run report.

Let the environment kernel be

\[
K=(1-\rho)I+\rho\Pi,
\]

where `Pi` replaces the current state by an independent draw from the stationary law `pi`. Let `f` be centered: `pi(f)=0`. Then

\[
Kf=(1-\rho)f,
\qquad
(I-K)g=f,
\qquad
g=f/\rho.
\]

Define

\[
M_n:=\sum_{r=0}^{n-1}\{g(J_{r+1})-Kg(J_r)\}.
\]

Relative to the joint filtration of the autonomous environment and the slow fragmentation randomness, `M_n` is a martingale, because the future environment transition uses fresh randomness and depends on the past only through `J_r`. Telescoping gives the exact Poisson decomposition

\[
\sum_{r=0}^{n-1}f(J_r)
=g(J_0)-g(J_n)+M_n.
\tag{A.1}
\]

If `J_0~pi`, stationarity and the martingale-difference identity yield

\[
E[(M_{r+1}-M_r)^2]
=\operatorname{Var}_\pi(g)-\operatorname{Var}_\pi(Kg)
=\frac{2\rho-\rho^2}{\rho^2}\operatorname{Var}_\pi(f)
\le \frac{2}{\rho}\operatorname{Var}_\pi(f).
\tag{A.2}
\]

For `n<=T/Delta`, Doob's inequality and (A.1)--(A.2) give

\[
E\max_{m\le n}
\left|\Delta\sum_{r=0}^{m-1}f(J_r)\right|^2
\le
C\left(
\frac{\Delta^2\|f\|_\infty^2}{\rho^2}
+T\frac{\Delta\operatorname{Var}_\pi(f)}{\rho}
\right).
\tag{A.3}
\]

Thus the centered environmental integral vanishes uniformly on compact physical time intervals whenever

\[
\Delta\|f\|_\infty/\rho\to0,
\qquad
\Delta\operatorname{Var}_\pi(f)/\rho\to0.
\]

For an arbitrary initial environmental state, let `tau` be the first refresh. Before `tau`, the environment is constant, so

\[
E[\Delta\|f\|_\infty(\tau\wedge n)]
\le \Delta\|f\|_\infty/\rho.
\tag{A.4}
\]

At the refresh, the new state is exactly `pi`-distributed and independent of the past environment transition noise, so the stationary maximal estimate (A.3) applies after `tau` by the strong Markov property. Therefore the same uniform convergence holds from every initial environmental state.

Now fix a visible partition state `sigma` and one generator/test-function observable

\[
f_{N,\sigma}(j)
=A_{N,j}\phi(\sigma)-\bar A_N\phi(\sigma).
\]

U006 assumes `|f_{N,sigma}|<=C_k L_{N,k}` and stationary second moment `<=C_k V_{N,k}`. Conditions

\[
\Delta_NL_{N,k}/\rho_N\to0,
\qquad
\Delta_NV_{N,k}/\rho_N\to0
\]

therefore imply that the difference between the environment-modulated and averaged compensators vanishes **uniformly in physical time while the visible partition remains at `sigma`**, even though the endpoint of that interval is a stopping time depending on the environment.

A `k`-label fragmentation has at most `k-1` proper refinement epochs. At each such epoch the environment may be biased by the event that just occurred, but (A.4) handles an arbitrary starting environmental state. Iterating at most `k-1` times gives uniform convergence of the full compensator difference on `[0,T]`.

The one-step remainder contributes at most

\[
O_k(T\Delta_NL_{N,k}^2)=o(1).
\]

Hence for every bounded test function `phi` on the finite partition state space,

\[
\phi(\widehat\Pi_N(t))-\phi(\widehat\Pi_N(0))
-\int_0^t \bar A_N\phi(\widehat\Pi_N(s))\,ds
\]

is asymptotically a martingale uniformly on compact intervals. Since `bar A_N -> Q` entrywise and the number of refinement jumps is uniformly bounded by `k-1`, the sequence is tight, every subsequential limit solves the finite-state `Q` martingale problem, and that martingale problem has the unique continuous-time Markov-chain solution. Therefore

\[
\widehat\Pi_N^{[k]}\Longrightarrow \Pi_Q^{[k]}
\]

in `J_1`.

For C020, `L_{N,k}=O_k(H_{N-1})`, `V_{N,k}=O_k(H_{N-1})`, `Delta_N=N^{-3}`, and `rho_N=N^{-1}`, so the two maximal terms are respectively

\[
O_k((\log N)/N^2),
\qquad
O_k((\log N)/N^2),
\]

while the accumulated nonlinear remainder is `O_k(log^2(N)/N^3)`. This completes the stopping-time/uniformity detail used in the main C020 report.
