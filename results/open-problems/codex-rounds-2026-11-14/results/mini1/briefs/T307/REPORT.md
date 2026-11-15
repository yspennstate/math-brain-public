VERDICT: PROVED an approximation-error floor for clipped homogeneous space–time score networks

T307 remains unresolved here. The completed piece is an obstruction to one proposed route, with a full proof and explicit constants.

For any fixed dimension `d>=1`, take a smooth initial density supported in the ball of radius `1/16` about `(1/2,0,...,0)`, run OU diffusion, and sample time uniformly in `[T0,T]`, where `0<=T0<=1/2` and `T>=2`. Every denoiser homogeneous in `(x,t-T0)`, clipped to the unit Euclidean ball, has weighted score error and excess population DSM loss at least

\[
\frac{C_d}{T-T_0},\qquad
C_d=\frac{5e^{-1}}{1024[32\sqrt{2\pi d}]^d}.
\]

The result holds at every width and for every choice of weights, so GD or SGD cannot remove this approximation error within that class. It includes bias-free joint space–time ReLU networks and their corresponding homogeneous tangent-kernel RKHS. When `T=O(log N)`, this precludes a polynomially decaying score-risk bound for this parameterization. It does not preclude such a bound for networks with biases.

The proof compares two dilated regions of positive Gaussian probability. Their posterior means lie in the same small offset ball, but the raw network predictions must double. Output clipping either leaves this relation intact or forces an output norm too large to fit the target. The two-point squared-error bound is `5/256`.

Files:

- [PROOF.md](PROOF.md): theorem, every proof step, score-loss conversion, RKHS corollary and a smooth non-Gaussian density example.
- [AUDIT.md](AUDIT.md): independent derivations and attempted escape cases.
- [LITERATURE.md](LITERATURE.md): bounded search and primary references actually opened.
- [audit_obstruction.py](audit_obstruction.py), [audit_data.json](audit_data.json), [audit_output.txt](audit_output.txt): reproducible finite checks and data.
- [LOG.md](LOG.md): decisions, commands, failures and outputs.

The nearby reference audited is Yinbin Han, Meisam Razaviyayn and Renyuan Xu, [arXiv:2401.15604v4](https://arxiv.org/abs/2401.15604v4). Its displayed network and projection match the class above. Its conditional training theorem is not treated as an unconditional resolution of T307; this proof does not verify its separate Gram-eigenvalue hypothesis. The search found no verified resolution after the prompt's November 2026 checkpoint.

Reproduction command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_obstruction.py > audit_output.txt 2>&1
```

Result: PASS; 9,225 exact identity/clipping checks and 1,025 scalar grid checks. The grid attains `5/256` at the exact minimizer `5/16`. Two independent formulas for `C_d` agree in dimensions 1, 2, 3 and 5. The script recorded nice 20, one OpenMP thread, approximately 14.75 MB peak RSS and 0.16 user CPU seconds. These finite checks support the analytic proof; they do not replace it.

What failed: two attempts to set RLIMIT_DATA were rejected before the mathematical checks ran; the setting was removed. The final audit retains a CPU limit. The nice wrapper emits warnings, but the process itself reports nice 20. A `ps` inspection was denied. One full-text HTML request failed; the main architecture was checked in both HTML and PDF. No heavy computation was used.

Limits and uncertainty: the lower bound uses clipping radius one and a specific homogeneous parameterization; it gives no impossibility theorem for general trained networks and no total-variation lower bound for generated samples. The literature search is not exhaustive. No positive GD/SGD statistical-rate theorem was obtained.

Next worker: add a constant input coordinate or a bias to remove the exact scaling constraint, then prove approximation and optimization guarantees for that modified class. Before using a kernel coupling argument, verify that its RKHS can approximate the intended denoising targets. The current obstruction shows why strict positive definiteness on a finite sample is not enough for that approximation step.

Task: “push this problem forward by one checkable piece” — 14 November 2026, approximately 22:12 +04.
