# Exact order-three obstruction for the present Fourier mechanism

Run: 20260924T181505Z-account04-B17-orderthree-obstruction-r1

Status: **proved as a limitation of the current method, not as a counterexample to the density conjecture.**

## Sources

- Main nine-eigenvalue candidate:
  proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex,
  commit eeb752c8943536541b34b42b8bf48e924f4d3d2f,
  blob 19fb119877426b640b2c0dae19ec2f78a399fe11.
- Independent reconstruction:
  proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/paper.tex,
  commit d3b12e27,
  blob 823201f05363fcc60c38cce0feb5abb636f081d7.

The two sources give exactly the same grouped physical-coordinate envelope.

## Exact exponent

After retaining \(h\) literal original-coordinate hub variables and leaving residual diffuse order \(m\), put \(q=h+m\). Both reconstructions prove

\[
 |\phi_Q(t)|\le \min\{1,B_{h,m}|t|^{-q/2}\}.
\]

Heavy-row promotion changes \(h\) and \(m\), but preserves their sum \(q\). Thus it can improve the constant but cannot improve the decay exponent.

Fourier inversion requires

\[
 \int_{\mathbb R}\min\{1,B|t|^{-q/2}\}\,dt<\infty,
\]

which holds exactly when

\[
 \frac q2>1,
 \qquad\text{equivalently}\qquad q\ge3.
\]

At \(q=2\),

\[
 \int_1^T \frac{B}{t}\,dt=B\log T,
\]

so the absolute Fourier integral diverges logarithmically. The order-two theorem correctly yields only the translation-uniform negative half-potential

\[
 \sup_a\mathbb E|Q-a|^{-1/2}
 \le C_2 E_2^{-1/8},
 \qquad
 C_2=8\sqrt e\,2^{-1/8}
 =12.095072570796\ldots,
\]

not a bounded density.

## Why constant optimization cannot lower the threshold

For order three, the promoted-branch density constants are

\[
\begin{array}{c|c}
h&c_h\\ \hline
0&14.818337662843\ldots\\
1&10.957714649270\ldots\\
2&8.263535690266\ldots\\
3&6.994931944791\ldots
\end{array}
\]

so promotion strictly improves constants while leaving the total exponent \(3/2\) unchanged. No optimization of these constants turns the order-two exponent \(1\) into an integrable exponent.

Consequently, the present spectral-to-volume route

\[
 s_{4k-3}(A)\ge1
 \Longrightarrow V_k(A)\gtrsim1
 \Longrightarrow E_k(A_{I,J})\gtrsim1
 \Longrightarrow |\phi_Q(t)|\lesssim |t|^{-k/2}
\]

closes a density bound first at \(k=3\), which corresponds to \(s_9(A)\). Improving numerical constants inside this chain cannot by itself yield an \(s_8\) or \(s_3\) theorem.

## Implication for the \(s_8\) overlap result

The existing \(s_8\) structural improvement supplies strong order-two mass with a shared original coordinate. The calculation above identifies the missing analytic statement precisely: one must exploit the shared-coordinate modulation to synthesize a genuinely third half-power of Fourier decay, or use a non-Fourier receiver that combines the order-two half-potential with additional curvature.

Treating the shared coordinate as an ordinary hub does not solve this, because the grouped theorem counts it in \(q\) only when it crosses an independent product bank with the required nondegenerate Gram factor. Merely relabeling the order-two certificate as order three would be circular.

## Scope

This is not a counterexample. It proves only that the existing grouped-Fourier/volume mechanism, with its current hypotheses, has an exact logarithmic endpoint at order two. The unrestricted three-eigenvalue conjecture remains open, and an \(s_8\) improvement requires a new shared-coordinate analytic receiver rather than sharper bookkeeping.
