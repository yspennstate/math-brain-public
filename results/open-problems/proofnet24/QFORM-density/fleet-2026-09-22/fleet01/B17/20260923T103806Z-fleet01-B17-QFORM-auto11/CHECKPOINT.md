# Substantive checkpoint: growing-activity rough banks can still saturate the `3 sqrt(2)` obstruction

Status: worked proof checkpoint; full QFORM remains OPEN. Continuity of the full target is separate.

## Exact source-valid row law

For integer `m` large set

\[
\lambda_m=m^{1/3},\qquad \varepsilon_m={\lambda_m\over m}=m^{-2/3},
\qquad a_m=m^{-1/12},\qquad
D_m=a_m\sqrt{m/\lambda_m}=m^{1/4}.
\]

Let `I=[-1/2,1/2]`, let

\[
R_{m,\pm}=[\pm D_m-\varepsilon_m/4,\ \pm D_m+\varepsilon_m/4],
\]

and define

\[
f_m(x)=(1-\varepsilon_m){\bf1}_I(x)
       +{\bf1}_{R_{m,+}}(x)+{\bf1}_{R_{m,-}}(x).
\tag{1}
\]

For large `m` the intervals are disjoint, so `0<=f_m<=1`, and its mass is
`(1-epsilon_m)+epsilon_m/2+epsilon_m/2=1`. It is symmetric. The expected number of remote selections in a bank of `m` iid rows is `m epsilon_m=lambda_m=m^(1/3)->infinity`, while the support diameter is `2D_m+o(1)~2m^(1/4)->infinity`.

The exact row variance is

\[
v_m={1-\varepsilon_m\over12}+\varepsilon_mD_m^2+{\varepsilon_m^3\over48}
={1\over12}+m^{-1/6}-{m^{-2/3}\over12}+{1\over48m^2}
\longrightarrow {1\over12}.
\tag{2}
\]

The fourth moment is

\[
E W_m^4={1-\varepsilon_m\over80}
 +\varepsilon_mD_m^4+{\varepsilon_m^3D_m^2\over8}
 +{\varepsilon_m^5\over1280}
=m^{1/3}+O(1),
\tag{3}
\]

so there is deliberately no uniform fourth-moment or bounded-support hypothesis.

## Bank local limit: actual use of fleet02/B17 and newest Claude

Let `S_m=m^{-1/2}\sum_{k=1}^m W_{m,k}` and let `h_m` be its density. The exact row characteristic function is

\[
\phi_m(s)=(1-\varepsilon_m)\operatorname{sinc}(s/2)
+\varepsilon_m\operatorname{sinc}(\varepsilon_ms/4)\cos(D_ms),
\qquad \psi_m(t)=\phi_m(t/\sqrt m)^m.
\tag{4}
\]

The completed fleet02/B17 report at the source-pinned master snapshot
`b5377cf0235c71defa44a695048b463a9086d0b4`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T101548Z-fleet02-B17-QFORM-auto11b/REPORT.md`, proves the following tail estimates for precisely this three-interval shape. Their proofs use only `epsilon_m->0` and `|cos(D_ms)|<=1`, hence apply to the present variable `D_m`:

- for `|s|<=1`, eventually `|phi_m(s)|<=exp(-s^2/60)`;
- on `1<=|s|<=12`, `|phi_m(s)|<=q_1<1`;
- on `12<=|s|<=4/epsilon_m`, `|phi_m(s)|<=1/3`;
- on `|s|>=4/epsilon_m`, `|phi_m(s)|<=6/|s|`.

Consequently

\[
\int_{|t|>\sqrt m}|\psi_m(t)|dt\to0.
\tag{5}
\]

Also `max |W_m|/sqrt(m)<=m^{-1/4}+o(1)->0`, so the triangular-array Lindeberg condition holds deterministically; with (2),

\[
S_m\Rightarrow G,\qquad G\sim N(0,1/12).
\tag{6}
\]

Thus `psi_m(t)->exp(-t^2/24)` pointwise. On `|t|<=sqrt(m)`, the first partner estimate gives the integrable domination `exp(-t^2/60)`. Together with (5),

\[
\boxed{\int_{\mathbb R}|\psi_m(t)-e^{-t^2/24}|dt\to0.}
\tag{7}
\]

Fourier inversion yields

\[
\boxed{\delta_m:=\|h_m-\gamma_{1/\sqrt{12}}\|_\infty\to0.}
\tag{8}
\]

The newest-Claude Lemma 1 at
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, gives for every cap-one density `f` and `p>=2`

\[
\int |\widehat f(s)|^pds\le {4\pi\over\sqrt p}.
\]

Applying it to the actual `f_m` in (1) with `p=m` gives the concrete inequality

\[
\boxed{
\int|\psi_m(t)|dt
=\sqrt m\int|\widehat f_m(s)|^m ds\le4\pi,
\qquad \|h_m\|_\infty\le2.
}
\tag{9}
\]

This is used below for the uniform cone-tail estimate.

## Exact dense rotated target

Take

\[
O={1\over7}\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix},\qquad J=\operatorname{diag}(1,1,-1).
\]

Direct multiplication gives `O^TO=I` and

\[
B=O^TJO={1\over49}
\begin{pmatrix}
31&-36&-12\\
-36&-23&-24\\
-12&-24&41
\end{pmatrix};
\tag{10}
\]
all nine entries of `B` are nonzero.

Form a `3m x3` matrix `R_m` by repeating the row `(Oe_j)^T/sqrt(m)` exactly `m` times in bank `j`. Then `R_m^TR_m=I_3`. Put

\[
A_m=R_mJR_m^T.
\tag{11}
\]

Every finite `A_m` therefore has exact nonzero spectrum

\[
\boxed{\{1,1,-1\}},
\tag{12}
\]

and, because every entry of `B` is nonzero, its three bank-by-bank physical blocks are all dense. For `3m` independent physical inputs, all with the cap-one density (1),

\[
Q_m=X^TA_mX=Y_m^TBY_m=(OY_m)^TJ(OY_m),
\tag{13}
\]

where `Y_m=(S_{1,m},S_{2,m},S_{3,m})` consists of three independent copies of the bank sum.

## Cone-tip convergence

Let

\[
\rho_m(z)=\prod_{j=1}^3 h_m((O^Tz)_j),\qquad
\rho_\infty(z)=\prod_{j=1}^3\gamma_{1/\sqrt{12}}(z_j).
\]

The equality for `rho_infty` uses isotropy of the Gaussian only; no independence after a non-Gaussian rotation is asserted. For

\[
\omega_\pm(\theta)={1\over\sqrt2}(\cos\theta,\sin\theta,\pm1),
\]

the exact coarea formula at the cone tip is

\[
p_{Q_m}(0)
={1\over2\sqrt2}\sum_{\pm}\int_0^{2\pi}\int_0^\infty
\rho_m(r\omega_\pm(\theta))\,dr\,d\theta.
\tag{14}
\]

On `0<=r<=R`, (8)-(9) and the Gaussian peak `<2` give

\[
|\rho_m-\rho_\infty|\le 3\cdot2^2\delta_m=12\delta_m,
\]

hence the bounded-ray contribution to the difference in (14) is at most

\[
12\sqrt2\pi R\delta_m.
\tag{15}
\]

For every unit ray `omega`, write `v=O^Tomega`; some `|v_j|>=1/sqrt(3)`. With `M=2`,

\[
\int_R^\infty\rho_m(r\omega)dr
\le M^2\sqrt3\,P(|S_m|\ge R/\sqrt3)
\le {3\sqrt3M^2v_m\over R^2}.
\tag{16}
\]

The same bound holds for the limiting Gaussian. Since `v_m` is bounded, (16) is uniform in `m,theta,+/-`. First let `m->infinity` in (15), then `R->infinity` using (16):

\[
\boxed{p_{Q_m}(0)\longrightarrow p_{G_1^2+G_2^2-G_3^2}(0).}
\tag{17}
\]

For iid `G_j~N(0,sigma^2)` the same cone integral evaluates to

\[
p_{G_1^2+G_2^2-G_3^2}(0)={1\over2\sqrt2\,\sigma^2}.
\]

At `sigma^2=1/12`,

\[
\boxed{p_{Q_m}(0)\to3\sqrt2.}
\tag{18}
\]

Thus this exact finite, dense, rotated, source-valid family is a new rough-law saturation mechanism for the already known lower obstruction. It shows that `C_univ>=3sqrt(2)` remains forced even along laws with growing remote-fragment activity, diverging support diameter and diverging fourth moments. It does NOT prove the unrestricted upper bound `C_univ<=3sqrt(2)`.

Corrections respected: no law-uniform pointwise stationary phase; no post-rotation independence; no arbitrary-joint coarea inequality; no uniform positive conditional-density moment; no bounded-support/fourth-moment/finite-activity hypothesis; no claim that intervals are globally extremal.
