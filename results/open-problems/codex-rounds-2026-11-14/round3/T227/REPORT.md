VERDICT: PARTIAL a probability-one catapult interval for a fully connected three-layer tanh network with noncentered initialization; eta_max remains open

The earlier sparse-network certificate holds on independent recheck. The new result replaces its diagonal second hidden layer with a fully connected layer. All `m^2+2m` coordinates are independently initialized and separately trained; the proof does not restrict training to equal neurons or an invariant subspace.

For every finite width `m>=1`, the architecture is

\[
 F_\theta(x)=\frac1m\sum_i a_i\tanh\left(
 \frac1{\sqrt m}\sum_j B_{ij}\tanh(c_jx)\right),
 \qquad L=\tfrac12F_\theta(1)^2.
\]

The data law is the point mass at `(1,0)`. Independently initialize

\[
 a_i\sim\mathrm{Unif}[7.99,8.01],\quad
 B_{ij}\sim\mathrm{Unif}[.499/\sqrt m,.501/\sqrt m],\quad
 c_j\sim\mathrm{Unif}[1.999,2.001].
\]

Training is ordinary simultaneous Euclidean GD in `(a,B,c)`. The fixed middle-layer normalization is `m^{-1/2}`; output normalization is `m^{-1}`. The initialization is noncentered and narrowly concentrated.

For every initialization in this box, simultaneously for every

\[
 \boxed{.9m\leq\eta\leq1.1m},
\]

the initial loss is below `6.5`, the loss after the first update exceeds `19`, and the subsequent loss contracts by at least a factor `1/64` per step to zero. Every parameter converges. The scalar NTK satisfies

\[
 \frac{37}m<\lambda_0<\frac{39}m,\qquad
 \frac{1-10^{-8}}m<\lambda_t<\frac{1+10^{-8}}m\quad(t\geq1).
\]

Thus `[36/lambda_0,40/lambda_0]` is also a certified interval, entirely above `2/lambda_0`. The probability is exactly one under the stated law. The kernel quantity is the NTK, not the loss Hessian.

The new lemma bounds the full Euclidean cross-gradient throughout the saturated dense region

\[
 |a_i|\leq16,\qquad-26\leq\sqrt m B_{ij}\leq-18,\qquad c_j\geq1.
\]

In particular, the shared first-layer derivative obeys
`|m*partial F/partial c_j|<=416*10^{-10}`. The first update enters this region, and summable movement preserves both bounds on every dense weight. A segment integral then proves contraction. All steps are in [PROOF.md](PROOF.md).

Reproduce the independent old-result check and the two dense audits with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_dense.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_dense_intervals.py
```

All passed. The first script checks the earlier arithmetic independently and runs 50 sparse-network audits. The second checks exact rational bounds, 450 dense-network trajectories, and 256 cross-gradient pairs. Automatic-differentiation error was below `4.5e-16`, finite-difference gradient error below `2.0e-10`, and disagreement between actual Euclidean updates and the auxiliary-coordinate recurrence below `5.4e-15`. The third independently sums rational interval gradients in the original coordinates at widths 1, 4, 9 and 64, confirming the entrance and tail margins. Its checks cover full boxes, not sampled initializations. The general-width theorem is proved analytically.

Each script used less than 24 MB peak RAM and finished in under two seconds. They use one thread, standard-library scalar arithmetic, no torch or GPU, and a CPU limit of at most 120 seconds. The inherited nice value is 20; the sandbox's warning on `nice -n 15` does not increase the process priority. Commands, outputs, exact fractions and audit details are in [LOG.md](LOG.md), `previous_recheck.json`, `dense_verification.json`, and `interval_audit.json`.

The literature update took less than five minutes. Opened primary sources included Aitor Lewkowycz, Yasaman Bahri, Ethan Dyer, Jascha Sohl-Dickstein and Guy Gur-Ari, [arXiv:2003.02218](https://arxiv.org/abs/2003.02218); Libin Zhu, Chaoyue Liu, Adityanarayanan Radhakrishnan and Mikhail Belkin, [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/949b3011c50300a2b4e60377466f52a8-Paper-Conference.pdf); Quan Nguyen, Robin Yadav, Param Mody and Mark Schmidt, [arXiv:2610.23007](https://arxiv.org/abs/2610.23007); and Thomas Hofmann, [arXiv:2607.04993](https://arxiv.org/html/2607.04993v1). Their checked scopes did not supply a solution of the requested deep finite-width problem. This bounded check is not an exhaustive absence or novelty claim.

No certificate or numerical audit failed. A direct reuse of the sparse tail estimate would leave dense column sums uncontrolled; the bounded dense-weight region supplies the missing estimate. What remains open is `eta_max`, a divergence theorem, the behavior near `2/lambda_0`, centered initialization, and nontrivial data laws. The upper endpoint of this certificate is not a maximal stable step.

Next worker: retain the full-space dense tail lemma and seek an entrance certificate for a product initialization with independent signs. Simply symmetrizing this box does not preserve the common residual and row-sign estimates. Establish a concrete finite-width sign/margin event before using concentration; a centered law alone does not imply the entrance conditions. Identifying `eta_max` requires a separate argument.

Task T227: “take the NEXT checkable step on this problem, building on that work.” Session start: 2026-11-15 03:33 Asia/Tbilisi.
