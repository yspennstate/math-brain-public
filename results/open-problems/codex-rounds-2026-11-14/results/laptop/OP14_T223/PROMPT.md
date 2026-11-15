# Open problem T223: Global convergence of the mean-field gradient flow for two-layer networks

Statement: Let f_rho(x) = ∫ a·sigma(<w,x>) rho(da,dw) be a two-layer network written as an integral over a measure rho of neurons, and let rho_t be the Wasserstein gradient flow of the population square loss R(rho), the limit of gradient descent on a width-m network as m → ∞ under mean-field scaling. Prove that for ReLU units, Gaussian inputs, a target realizable by finitely many neurons and an initialization rho_0 such as a Gaussian (unbounded support, with a stated convention for the flow at the ReLU kink), the flow rho_t is well posed, R(rho_t) → inf R as t → ∞ without entropic regularization, and rho_t converges in W2 (these are separate questions: risk convergence does not imply convergence of the parameter law); give a rate.

Caveat: Chizat–Bach prove that IF the flow converges in W2 then the limit is a global minimizer, under hypotheses that include an initialization whose support is bounded (in a ball B(0, r_b)) and separates the spheres, plus technical conditions (Theorems 3.3 and 3.5, auditor codex-w687, 16 Oct); a Gaussian initialization is outside that scope. The open part is convergence itself, for natural initializations, and any rate. With added noise (mean-field Langevin, T225) convergence is known but the rate degrades with the temperature.

Source: L. Chizat and F. Bach, On the Global Convergence of Gradient Descent for Over-parameterized Models using Optimal Transport, arXiv:1805.09545 (2018); S. Mei, A. Montanari and P.-M. Nguyen, A Mean Field View of the Landscape of Two-Layers Neural Networks, arXiv:1804.06561 (2018)

Where it stands (checked by us, Nov 2026): Open in the stated generality. Known: global convergence under entropic regularization (Mei–Montanari–Nguyen 1804.06561; Hu et al. 1905.07769; Chizat 2202.01009), for special symmetric targets and one-dimensional settings, and the conditional theorem of Chizat–Bach. Petit, Poon and Peyré (arXiv:2605.10775) extend the conditional statement to bounded and asymptotically one-homogeneous activations with vector outputs and to multi-head attention: if the mean-field flow converges in W2, its limit is a global minimizer. Convergence of the flow itself is not proved. Open.

Your job for this session: push this problem forward by one checkable piece.
1. Ten minutes at most: search whether it was solved or substantially advanced after what "where it stands" says. If it
   was, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. Choose ONE concrete piece you can finish: a special case, a finite computation that settles small cases, a sharper
   bound, a counterexample search, a reduction to a cleaner statement. Write the choice and why in LOG.md first.
3. Do it. A proof goes in PROOF.md with every step written out. A computation is a script in this folder; put the exact
   command and its output in LOG.md and the data in a file.
4. Try to break your own result: re-derive every load-bearing number a second, independent way; look for the case your
   argument misses. Record what you checked.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> . Then what was proved or computed, the commands, what failed, what you are unsure
   of, and what the next worker should do. An honest NO PROGRESS is worth more than a claim that does not hold.

Rules (the author's standing laws):
- Work only inside this folder (~/brain-repo/12_cognitive_architecture/codex_local_1108/briefs/OP14_T223). Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs at below-normal priority,
  and finishes within 20 minutes per run. No GPU, no torch, no training. This laptop is the author's working computer; never fill its memory and never open a visible window.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.
