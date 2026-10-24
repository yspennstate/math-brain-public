# Independent referee report: T384 first-layer kernel nonfreezing

**Verdict: PASS for the stated narrow theorem.** I independently checked the argument in [T384_independent.md](../research/T384_independent.md) against the [T384 dossier](https://github.com/<private-repo>/blob/main/06_math_research/frontier/rows/T384/DOSSIER.md), its [moves ledger](https://github.com/<private-repo>/blob/main/06_math_research/frontier/rows/T384/moves.jsonl), and Favaro–Fortini–Peluchetti, [arXiv:2206.08065v3](https://arxiv.org/html/2206.08065v3), especially (4)–(9), Theorems 1, 2, 4, and Discussion. The proof establishes that for each $\alpha\in(0,2)$ and fixed $T>0$ there is a **fixed deterministic** scalar label $y$ for which

$$
\liminf_{m\to\infty}
\mathbb P\{\widetilde H_m^{(1)}(0)-\widetilde H_m^{(1)}(T)\ge\tfrac12\}>0.
$$

The theorem is about the first-layer part of the **rescaled** NTK under the paper's actual shallow ReLU parametrization, not the complete infinite-width feature-dynamics law. It does not contradict Theorem 4: that theorem bounds movement of $\widetilde H_m^{(2)}$ and the minimum eigenvalue of the full kernel. The paper's Discussion expressly says it is unclear whether fluctuations of $\widetilde H_m^{(1)}$ vanish.

## Independent calculation

For $d=k=1$, $x=1$, $f_m=c_m\sum_i W_i(U_i)_+$ with $c_m=(m\log m)^{-1/\alpha}$, loss $(y-f_m)^2/2$, and flow rate $\eta_m=(\log m)^{2/\alpha}$, put $\beta_m=\eta_m c_m=m^{-1/\alpha}(\log m)^{1/\alpha}$ and $r=y-f_m$. At differentiable times and with the specified zero derivative at the ReLU kink,

$$
\dot U_i=\beta_m r W_i{\bf1}_{U_i>0},\qquad
\dot W_i=\beta_m r(U_i)_+,\qquad
\dot r=-r K_m,
$$

where $K_m=\widetilde H_m^{(1)}+\widetilde H_m^{(2)}
=m^{-2/\alpha}\sum_{U_i>0}(W_i^2+U_i^2)$. Both the log cancellation and the sign in the residual ODE are correct. Piecewise smooth solutions are absolutely continuous; gate hits may change $K_m$ but do not jump $f_m$ or $r$. If $r(0)>0$, the ODE keeps $r>0$, so the common clock $\tau(t)=\beta_m\int_0^t r(s)\,ds$ is increasing. Until a gate hits zero, $U_i(\tau)=U_i(0)\cosh\tau+W_i(0)\sinh\tau$ and $W_i(\tau)=W_i(0)\cosh\tau+U_i(0)\sinh\tau$. A negative $W_i$ with $0<U_i<1$ hits at $\operatorname{arctanh}(U_i/|W_i|)$; afterward both parameters freeze under the stipulated convention. Initially inactive gates cannot activate.

For a symmetric nondegenerate standard $\alpha$-stable variable, $\mathbb P(W<-z)\sim c_-z^{-\alpha}$ with $c_->0$. Thus the number of indices satisfying

$$
0<U_i(0)<1,\qquad -2m^{1/\alpha}\le W_i(0)\le-m^{1/\alpha}
$$

is binomial with success probability asymptotic to $\lambda/m$, $\lambda=c_-(1-2^{-\alpha})\mathbb P(0<U<1)>0$. Consequently the event $E_m$ that at least one such index exists has probability tending to $p=1-e^{-\lambda}>0$. The output $f_m(0)$ and $K_m(0)$ are tight: respectively Theorems 1 and 2 of the primary paper apply at $k=1$. Equivalently, the former is the symmetric product-tail normalization $(m\log m)^{1/\alpha}$, and the latter follows from the regular-variation index $\alpha/2<1$ of squared stable variables. Pick finite $B,K$ such that each tail event has probability below $p/8$ for all large $m$, then set $y=B+1$, $R=y+B$. By a union bound, with asymptotic probability at least $3p/4$ there is a selected extreme neuron and simultaneously $1\le r(0)\le R$ and $K_m(0)\le K$; independence between these events is unnecessary.

Along an active trajectory, $d(W_i^2+U_i^2)/d\tau=4W_iU_i\le2(W_i^2+U_i^2)$. Deactivation removes a nonnegative term from $K_m$; hence

$$
K_m(t)\le e^{2\tau(t)}K_m(0),\qquad
\tau(t)\le\beta_m R t,\qquad
r(t)\ge r(0)\exp[-K e^{2\beta_m R T}t]\quad(0\le t\le T).
$$

In particular $K_m(t)\le2K$ on this event for all $t\le T$ and large $m$. At $t_m=4(\log m)^{-1/\alpha}<T$, $r(t)\ge1/2$ for all $t\le t_m$, so

$$
\tau(t_m)\ge\beta_m t_m/2=2m^{-1/\alpha}
>\operatorname{arctanh}\!\left(U_i(0)/|W_i(0)|\right)
$$

for all sufficiently large $m$. The selected gate is dead by $t_m$ and stays dead through $T$. This verifies the hitting time even more directly than the fixed-$T$ lower bound in the root proof.

The offsetting-increase estimate is valid but should be derived for **$W^2$ itself**, not inferred just from $W^2\le e^{2\tau}(W_0^2+U_0^2)$, which would leave a nonvanishing $U_0^2$ term. In fact

$$
\frac{d W_i^2}{d\tau}=2W_iU_i
\le W_i^2+U_i^2\le e^{2\tau}(W_i(0)^2+U_i(0)^2),
$$

so integrating until $T$ or a gate death gives each surviving neuron's increase at most $\tfrac12(e^{2\tau(T)}-1)(W_i(0)^2+U_i(0)^2)$. Dead neurons contribute zero and cannot offset the loss. Summing gives

$$
\widetilde H_m^{(1)}(T)-\widetilde H_m^{(1)}(0)
\le-\frac{W_i(0)^2}{m^{2/\alpha}}
+\frac{e^{2\beta_mRT}-1}{2}K_m(0)
\le-1+o(1)
$$

uniformly on the positive-probability event. Since $\beta_m\to0$, the last error tends to zero. Thus the claimed $1/2$ drop follows.

## Scope and minor edits

1. The zero-derivative-at-zero convention should remain explicit. Under that convention the finite-dimensional flow is unambiguous up to finitely many gate deaths and has no gate reactivation on the selected positive-residual event.
2. Say “there exists a sufficiently large fixed label $y$,” not “every label.” The intersection argument uses this choice.
3. The first-layer kernel's order-one movement is a rigorous form of gate/feature movement, but it does not identify a limiting nonlinear flow or prove that feature learning improves prediction. It answers the dossier's restated Target 2 nonfreezing claim, not the full deep-network T384 row.
4. No external novelty or publication-priority audit was performed. The result extends the dossier's numerical observation and addresses a question explicitly left open in the inspected 2023 paper; that is a scoped source comparison only.

No mathematical gap found in the proposed proof after the above conventions and scope are retained.
