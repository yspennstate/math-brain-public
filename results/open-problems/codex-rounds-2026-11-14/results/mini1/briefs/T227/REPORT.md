VERDICT: PARTIAL a probability-one catapult interval for an explicitly initialized sparse three-layer tanh network; eta_max remains open

For every finite width `m`, proved a catapult interval for

\[
 F_\theta(x)=m^{-1}\sum_{i=1}^m a_i\tanh(b_i\tanh(c_i x)),
 \qquad L=\tfrac12 F_\theta(1)^2.
\]

All `3m` parameters are trained. The two hidden layers have independent diagonal paths. Initial coordinates are independent uniforms on `[7.99,8.01]`, `[0.499,0.501]`, and `[1.999,2.001]`, respectively. Input and label law is the point mass at `(1,0)`. This is mean output normalization and a noncentered initialization, not standard dense Gaussian NTK initialization.

For every initial point in the box, simultaneously for every constant `eta in [0.9m,1.1m]`, the loss rises from below `6.5` to above `19` after one update. The scalar NTK drops from between `37/m` and `39/m` to within `10^{-8}/m` of `1/m`. Thereafter loss contracts by at least a factor `1/64` per step, tends to zero, and all parameters converge. The proof covers independent perturbations of every path, not just a symmetric trajectory. Probability is exactly one under the specified law.

Equivalently, a certified interval in units of the realized initial NTK is

\[
 \boxed{36/\lambda_0\leq\eta\leq40/\lambda_0}.
\]

The mechanism is explicit: the first step flips the second-layer weights into tanh saturation, leaving a much smaller kernel. The proof is in `PROOF.md`; exact rational certificates and independent numerical audits are in `verify.py` and `verification_data.json`.

Reproduce the certificate with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify.py
```

Result: exact rational certificates PASS; 63 full-network numerical audits PASS; finite-difference gradient error below `1.4e-10`; finite-difference NTK normalization error below `2.1e-10`. Peak RAM was `15712256` bytes and runtime was under one second. The inherited process nice value is 20; the sandbox prints a setpriority warning when `nice -n 15` is requested. No third-party numerical libraries, GPU, or parallel workers are used.

Exploration is reproducible with the same environment prefix followed by `python3 -B scout.py`; its 262 candidates are in `scout_data.json`. Exact commands and relevant outputs are recorded in `LOG.md`.

The literature search took less than ten minutes. Opened primary sources include [Libin Zhu, Chaoyue Liu, Adityanarayanan Radhakrishnan, Mikhail Belkin, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/949b3011c50300a2b4e60377466f52a8-Paper-Conference.pdf), [David Meltzer, Min Chen, Junyu Liu, arXiv:2301.07737v2](https://arxiv.org/html/2301.07737v2), [Benjamin Gess, Daniel Heydecker, arXiv:2603.10079](https://arxiv.org/pdf/2603.10079), [Quan Nguyen, Robin Yadav, Param Mody, Mark Schmidt, arXiv:2610.23007](https://arxiv.org/html/2610.23007v1), and [Thomas Hofmann, arXiv:2607.04993](https://arxiv.org/html/2607.04993v1). They provide quadratic, shallow-network, SGD, or invariant-manifold results; no solution of the requested deep finite-width random-initialization problem was identified. Details and scope checks are in `LOG.md`. This bounded search does not establish an exhaustive absence result.

What remains unresolved: the maximal learning rate, a divergence theorem, behavior between `2/lambda_0` and the certified interval, and the usual dense architecture with centered random weights and nontrivial data. No attempted argument identifies `eta_max`; the proof gives only a convergent interval. No novelty claim beyond this explicit checked construction is made.

Next worker: seek a comparable finite-step entrance certificate under a centered initialization, or first extend this saturated-region certificate to dense second-layer connections. The tail calculation only requires a common-sign, nearly constant output derivative and small other derivatives; it is the entrance step under a conventional law that remains to be supplied. Identifying `eta_max` requires a separate argument and cannot be inferred from the upper endpoint of this certificate.

Task T227: “push this problem forward by one checkable piece.” Session start: 2026-11-14 22:07 Asia/Tbilisi.
