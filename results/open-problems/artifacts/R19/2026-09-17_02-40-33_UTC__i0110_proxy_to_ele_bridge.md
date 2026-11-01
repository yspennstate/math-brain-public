# R19 / I0110 — proxy domination to ELE bridge

Status: **proved internal bridge lemma; application scope below remains source-specific and audit-pending.**

This artifact supplements the frozen Entropic Lift-Extraction (ELE) definition from
`artifacts/R19/2026-09-17_01-37-22_UTC__i0110_ele_certificate.md`.
It does not change that definition.

## C010. Proxy domination implies the ELE upper extraction clause after structural trimming

Let `X_n` be finite with `N_n=|X_n| -> infinity`. Let `pi_n,q_n` be probability measures on `X_n`, and let `s_n` be a nonnegative subprobability measure. Put

\[
\delta_n=\|q_n-\pi_n\|_{TV},\qquad
\zeta_n=1-s_n(X_n).
\]

Assume

\[
\delta_n\to0,\qquad \varepsilon_n\to0,\qquad \zeta_n\to0,
\tag{C010.1}
\]

and the one-sided pointwise domination

\[
 s_n(x)\le (1+\varepsilon_n)q_n(x)+\frac{\varepsilon_n}{N_n}
 \quad\text{for every }x\in X_n.
\tag{C010.2}
\]

Then there are deterministic sets `G_n subset X_n` such that, with

\[
r_n=s_n\mathbf 1_{G_n},\qquad m_n=r_n(X_n),
\]

we have

\[
m_n\to1
\tag{C010.3}
\]

and

\[
\boxed{
D_n:=\sum_{x\in X_n}
 \frac{(r_n(x)-m_n\pi_n(x))^2}{\pi_n(x)}\to0.
}
\tag{C010.4}
\]

Thus the frozen ELE upper extraction requirement follows from a high-mass one-sided domination by any proxy converging to stationarity in total variation.

### Proof

Choose

\[
a_n=\sqrt{\delta_n}+N_n^{-1},\qquad
b_n=\sqrt{\varepsilon_n}+N_n^{-1}.
\]

Define the relative-proxy-error and tiny-stationary-mass sets

\[
B_n=\{x:|q_n(x)-\pi_n(x)|>a_n\pi_n(x)\},
\]

\[
C_n=\{x:\pi_n(x)<b_n/N_n\},
\qquad
G_n=X_n\setminus(B_n\cup C_n).
\]

Since `sum_x |q_n(x)-pi_n(x)|=2 delta_n`,

\[
\pi_n(B_n)\le \frac{2\delta_n}{a_n},
\qquad
q_n(B_n)\le \frac{2\delta_n}{a_n}+2\delta_n.
\tag{C010.5}
\]

By (C010.2),

\[
s_n(B_n)
\le (1+\varepsilon_n)
 \left(\frac{2\delta_n}{a_n}+2\delta_n\right)
 +\varepsilon_n=o(1).
\tag{C010.6}
\]

Also

\[
\pi_n(C_n)\le b_n,
\qquad
q_n(C_n)\le b_n+2\delta_n,
\]

and hence

\[
s_n(C_n)
\le (1+\varepsilon_n)(b_n+2\delta_n)+\varepsilon_n=o(1).
\tag{C010.7}
\]

Together with `s_n(X_n)=1-zeta_n`, (C010.6)-(C010.7) imply (C010.3).

For `x in G_n`,

\[
q_n(x)\le(1+a_n)\pi_n(x),
\qquad
\frac{\varepsilon_n}{N_n}\le
\frac{\varepsilon_n}{b_n}\pi_n(x).
\]

Therefore

\[
r_n(x)\le(1+c_n)\pi_n(x),
\]

where

\[
c_n=(1+\varepsilon_n)(1+a_n)
 +\frac{\varepsilon_n}{b_n}-1\to0.
\tag{C010.8}
\]

Put `f_n=r_n/pi_n` on the support of `pi_n`; then `0<=f_n<=1+c_n` and

\[
\mathbb E_{\pi_n}f_n=m_n.
\]

Consequently

\[
\begin{aligned}
D_n
&=\mathbb E_{\pi_n}(f_n-m_n)^2\\
&=\mathbb E_{\pi_n}f_n^2-m_n^2\\
&\le (1+c_n)m_n-m_n^2\\
&=m_n(1+c_n-m_n)\\
&\le c_n+(1-m_n)\to0.
\end{aligned}
\]

This proves C010. `QED`

The exact rational self-check for the trimming inequalities and the final quadratic estimate is
`artifacts/R19/2026-09-17_02-40-33_UTC__i0110_proxy_ele_checker.py`; its archived output ends `ALL_EXACT_CHECKS_PASS`.

## C011. Bordenave–Caputo–Salez sparse random digraphs satisfy the frozen ELE certificate

Source family: Salez Problem 2.1 reference `[21]`, Bordenave–Caputo–Salez,
*Random walk on sparse random digraphs*, arXiv:1508.06600.

This application uses the source's own objects and does not modify ELE.

### Upper side

Let `pi_*` be the true stationary distribution and

\[
q_n=\pi_h^-:=\pi_0^-P^h,
\qquad
h=\left\lfloor\frac{\log n}{10\log\Delta}\right\rfloor.
\]

The source proves

\[
\|q_n-\pi_*\|_{TV}=o_{\mathbb P}(1)
\tag{C011.1}
\]

in equation (11). Its Definition 1 and Proposition 10 define the subprobability `s_n=P_0^t(i,.)` obtained by retaining only nice paths and prove, for every fixed `epsilon>0`,

\[
s_n(j)\le(1+\varepsilon)q_n(j)+\frac{\varepsilon}{n}
\quad\text{uniformly in }i,j,
\tag{C011.2}
\]

with high probability, while the omitted nice-path mass tends to zero once `t` lies just past the entropic threshold.

Choose

\[
u_n=(\log n)^{-1/4},
\qquad
t_n^+=(1+u_n)t_*.
\]

Since `t_*=Theta(log n)` and the source has bounded degrees, Proposition 8 applied at threshold `1/(n log^3 n)` gives

\[
\sup_i\{1-s_n(X_n)\}=o_{\mathbb P}(1),
\tag{C011.3}
\]

because

\[
\frac{\mu t_n^+ +\log(1/(n\log^3 n))}{\sqrt{t_n^+}}
\to+\infty.
\]

A standard diagonal choice converts the source's fixed-`epsilon` Proposition 10 into a deterministic sequence `epsilon_n downarrow 0` for which (C011.2) still holds with probability tending to one. Combining (C011.1)-(C011.3) with C010 gives a structural retained nice-path subprobability `r_n` with mass tending to one and the exact frozen ELE defect

\[
\sum_j\frac{(r_n(j)-m_n\pi_*(j))^2}{\pi_*(j)}\to0.
\]

This supplies the ELE upper side uniformly over initial vertices.

### Lower side

Set

\[
t_n^-=(1-u_n)t_*,
\qquad
\theta_n=\frac{\log^3n}{n}.
\]

Proposition 8 now gives, uniformly over initial vertices,

\[
\mathcal Q_{i,t_n^-}(\theta_n)\to1,
\]

because

\[
\frac{\mu t_n^-+\log\theta_n}{\sqrt{t_n^-}}
\to-\infty.
\]

Let the lower ELE auxiliary law be the actual trajectory law and let `E_n^-` be the trajectories of weight greater than `theta_n`; the structural projection is the endpoint map. The retained mass tends to one. Because every retained trajectory has probability greater than `theta_n`, there are at most `1/theta_n=n/log^3 n` such trajectories, hence their endpoint image has at most that cardinality.

The source's proof of Proposition 7 establishes precisely the needed small-mass estimate for any such image: its equation (13), followed by the bound

\[
\mathbb E\sum_j(\pi_h^-(j))^2
=O(\log^2n/n),
\]

makes the stationary-proxy mass of a set of cardinality at most `n/log^3 n` equal to `o_P(1)`. Equation (11) transfers the conclusion from `pi_h^-` to `pi_*`. Thus the lower ELE image has vanishing stationary mass.

Finally `t_n^+/t_n^- -> 1`. Hence the same frozen ELE definition covers reference `[21]`.

## C012. Hermon–Šarković–Sousi community random graphs satisfy the frozen ELE certificate in their cutoff regime

Source family: Salez Problem 2.1 reference `[62]`, Hermon–Šarković–Sousi,
*Cutoff for random walk on random graphs with a community structure*,
Annals of Applied Probability 35 (2025), 2080–2127; arXiv:2212.04469.

Their cutoff regime is

\[
\alpha_n\log n\to\infty,
\]

where `alpha_n` is the Cheeger constant of the finite community chain.

The paper's Section 2 proof overview states that it follows the same entropic architecture as earlier sparse-random-graph work: first control the `L^2` distance at the entropic time, then use the Poincare inequality/spectral profile to drive that distance to `o(1)`. The Benjamini–Schramm multi-type random tree supplies quantitative information concentration; a coupling transfers the walk to the finite graph.

For the lower ELE side, at a pre-entropic time the coupled walk is, with probability tending to one, supported on `o(n)` vertices. Degrees are uniformly bounded above and below in the theorem's sparse setup, so stationary mass of an `o(n)` set is `o(1)`. The coupling error is `o(1)`.

For the upper side, after an additional

\[
O\!\left(\sqrt{\frac{\log n}{\alpha_n}}\right)
\]

steps, the source's `L^2(pi)` density distance is `o(1)`. In the frozen ELE definition take the auxiliary law to be the actual finite-graph walk, projection equal to the identity, and `E_n^+=X_n`. Then `m_n=1` and the ELE defect is exactly the corresponding chi-square / squared `L^2(pi)` density distance, hence tends to zero.

The source explicitly upgrades the fixed-start entropic argument to worst starting points using `K`-roots. Since

\[
\sqrt{\log n/\alpha_n}=o(\log n)
\quad\text{when}\quad \alpha_n\log n\to\infty,
\]

the lower and upper times have ratio tending to one. Thus reference `[62]` also satisfies the unchanged ELE certificate.

## Scope

C010 is a general internal bridge theorem. C011 and C012 are source-paper-to-ELE mappings. They do **not** claim that Salez Problem 2.1 is solved: the common metric is now seven of nine families, and `[14]` and `[13]` remain to be checked under the identical frozen definition. Even at nine of nine, the fleet closure protocol still requires a source-scope audit of whether ELE qualifies as the structural property intended by Problem 2.1, prior-art review, and two independent OTHER-track audits.
