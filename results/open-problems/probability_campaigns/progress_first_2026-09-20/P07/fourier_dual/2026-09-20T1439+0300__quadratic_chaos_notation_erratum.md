# P07-B notation erratum for the 14:39 quadratic-chaos report

This is a transport-only notation correction to immutable report

`probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1439+0300__quadratic_chaos_additive_energy_dichotomy.md`

created at commit `85722d96a6678c4b65fedcd192a0ad6a17a7014b`.

In Section 5, several occurrences of the coefficient-vector symbol `u` acquired a stray backslash/newline during transport. Read equations (5.1)--(5.6) with the single symbol `u` throughout:

\[
u_0=0,
\qquad
u_a=u_{-a}=\frac{z_a}{2}\quad(a\in D),
\qquad
u_k=0\quad\text{otherwise},
\]
where the leading characters above mean `u_0`, `u_a`, and `u_k` (not a Greek `nu`; Markdown transport may visually join the preceding newline). Equivalently, in plain text:

`u[0]=0`, `u[a]=u[-a]=z[a]/2` for `a in D`, and `u[k]=0` otherwise.

Then
\[
f_z(j)=\sum_{k\in\mathbb Z_n}u_ke^{2\pi i k j/n},
\]
\[
\mathbb E_{q_0}f_z^2=\frac n{n-1}\|u\|_2^2,
\qquad
\mathbb E_{q_0}f_z^4=\frac n{n-1}\|u*u\|_2^2,
\]
and therefore
\[
\boxed{
\mathcal K_4(z)=\frac{n-1}{n}\frac{\|u*u\|_2^2}{\|u\|_2^4}.
}
\]
The Section 8 handoff phrase `||nu*nu||_2^2/||nu||_2^4` should likewise be read as `||u*u||_2^2/||u||_2^4`.

No mathematical claim, constant, proof, or status changes. The original immutable report is intentionally not overwritten.
