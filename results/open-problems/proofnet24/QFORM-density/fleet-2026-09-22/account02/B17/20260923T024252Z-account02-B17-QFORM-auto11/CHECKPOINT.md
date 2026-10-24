# B17 checkpoint — uniform finite-bank transfer for the one-heavy majority-sign witness

Run: `20260923T024252Z-account02-B17-QFORM-auto11`  
Status: substantive checkpoint; full QFORM remains OPEN.

For the exact source-valid family
\[
A_m=\operatorname{diag}(1,J_m/m,-J_m/m),\qquad
Q_{m,f}=X_f^2+S_m^2-T_m^2,
\]
where `f<=1` is arbitrary (and may depend on `m`) and the two banks are independent normalized sums of `m` iid `Unif[-1/2,1/2]`, I obtain the uniform transfer target
\[
\sup_{f\le1}\|p_{Q_{m,f}}-p_{Q_{\infty,f}}\|_\infty\to0,
\qquad Q_{\infty,f}=X_f^2+G_+^2-G_-^2.
\]

Key mechanism. Let `h_m` be the bank density and `gamma` the `N(0,1/12)` density. The completed account03/B17 local-limit argument gives `||h_m-gamma||_infty -> 0`; Scheffe then gives `eta_m:=||h_m-gamma||_1 ->0`. If `a_m` is the density of `S_m^2`, evenness gives exactly `||a_m-a_infty||_1=eta_m`, hence for the difference kernels `k_m=a_m*tilde(a_m)`, `k_infty=a_infty*tilde(a_infty)`,
\[
delta_m:=\|k_m-k_\infty\|_1\le2\eta_m\to0.
\]

Ball's one-dimensional cube-slicing bound gives `||h_m||_infty<=sqrt(2)` uniformly. Therefore every `k_m` and `k_infty` obeys the common logarithmic envelope
\[
k(w)\le C_0+M^2\log_+(1/|w|),\quad M=\sqrt2,\quad C_0=M+2M^2\log3.
\]
For `d_m=|k_m-k_infty|`, with `A=2C_0`, `B=2M^2=4`,
\[
|\{d_m>\lambda\}|\le\min\{\delta_m/\lambda,\ 2e^{-(\lambda-A)/B}\}\quad(\lambda>A).
\]
For every measurable `E subset R` and every `s`,
\[
|\{x:s-x^2\in E\}|\le2\sqrt{|E|}.
\]
Layer cake consequently yields, for every `Lambda>A`,
\[
\sup_s\int d_m(s-x^2)dx
\le4\sqrt{\delta_m\Lambda}+4\sqrt2 B e^{-(\Lambda-A)/(2B)}\to0.
\]
Since `0<=f<=1`, this controls the density difference uniformly over the entire heavy-law class. Combining with the preceding account02/B17 Gaussian-completion theorem
\[
\sup_{f\le1}\|p_{Q_{\infty,f}}\|_\infty\le
C_{maj}=\frac6\pi\left(\frac52+\log\frac43-\gamma_E\right)
=4.2216798636\ldots<3\sqrt2
\]
will imply an eventual strict no-overshoot theorem for every `m`-dependent cap-one heavy law.

Required e5 source application: its proved ruled-level-set Theorem C gives independently, for this same exact finite family, `p_{Q_{m,f}}(s)<=pi sqrt(2)` for every `s>=0` and every `m`; this rules out unbounded finite-bank escape on the positive one-sheet side but does not by itself reach the candidate sharp scale `3 sqrt(2)`.
