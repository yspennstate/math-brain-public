# Open problem T227: The catapult phase of large-learning-rate training

Statement: Lewkowycz et al. observe for wide networks three regimes in the step eta relative to lambda_0, the top eigenvalue of the neural tangent kernel at initialization: lazy for eta < 2/lambda_0, a catapult phase for 2/lambda_0 < eta < eta_max ≈ c/lambda_0 in which the loss first grows, the curvature drops, and training then converges, and divergence above eta_max. Prove the existence of the catapult phase and identify eta_max for a fixed deep nonlinear architecture of large finite width (stated activation, input and label law, normalization of the initialization), as an eta interval on which the loss rises and then converges with high probability.

Caveat: The two-layer linear 'uv' model is solved in the original paper; the question is about nonlinear and deep networks.

Source: A. Lewkowycz, Y. Bahri, E. Dyer, J. Sohl-Dickstein and G. Gur-Ari, The large learning rate phase of deep learning: the catapult mechanism, arXiv:2003.02218 (2020)

Where it stands (checked by us, Nov 2026): Proved for the uv model and some quadratic models (Zhu et al. 2022-23, to verify). Open for deep nonlinear networks.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T227 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.

----- earlier REPORT.md -----
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
