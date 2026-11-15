# Open problem T264: Tempered overfitting of interpolating ReLU networks in fixed dimension

Statement: Mallinar et al. propose a taxonomy (benign, tempered, catastrophic) of interpolation with noisy labels and conjecture that interpolating ReLU networks in fixed input dimension are tempered: the excess risk stays bounded but does not vanish as n → ∞. For minimum-norm (or GD-trained) interpolating two-layer ReLU networks with inputs in a fixed dimension d ≥ 2 and label noise, determine whether the limiting excess risk is zero, finite and positive, or infinite.

Caveat: For univariate inputs (d = 1) the question is settled: tempered for some losses/norms, catastrophic for others (Kornowski–Yehudai–Shamir; Joshi–Vardi–Srebro).

Source: N. Mallinar et al., Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting, arXiv:2207.06569 (2022); G. Kornowski, G. Yehudai and O. Shamir, arXiv:2305.15141 (2023); N. Joshi, G. Vardi and N. Srebro, arXiv:2307.15396 (2023)

Where it stands (checked by us, Nov 2026): d = 1 settled; d ≥ 2 open as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T264 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T264 (read it,
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
VERDICT: PROVED Exact three-constraint minimum-norm ReLU interpolants with risk coefficient 2/d.

The earlier two-point result holds. Independent odd/even decomposition recovers its singular risk coefficient 1/d, and fresh direct integration checks its exact risk formula at acute and obtuse angles.

The new result solves the next suggested three-constraint problem for a specific third-point geometry in every ambient dimension d>=2. Put a=cos(theta/2), b=sin(theta/2), 0<theta<pi/3, and

```text
x1=(a,b), x2=(a,-b), x3=(0,1), labels=(1,-1,tau), tau in {-1,+1}.
```

The points lie in a plane embedded in R^d. The norm is one half the sum of squared parameters of both layers, with no biases, skip, or intercept. Width is unrestricted. Explicit dual certificates prove uniqueness as a function, including when ambient directions outside the plane are allowed.

Writing v=(b,-a), the exact solutions are:

- tau=+1: W=((1-b)/a,1), L=sqrt(2/(1+b)), C=(1-b)/(ab). The function is sigma(W dot x)-C*sigma(v dot x), with minimum cost L+C. Two units suffice.
- tau=-1: C=a/b, D=(1+b)/a. The function is sigma(x1 dot x)-C*sigma(v dot x)-D*sigma(-v dot x), with minimum cost 1+1/(ab)+1/a. Three units suffice.

For either third label, theta*f converges uniformly on the unit sphere to -2*sigma(-x_2). Therefore its conditional squared excess risk against the zero regression function satisfies

```text
lim(theta -> 0) theta^2 * R_d(theta) = 2/d.
```

The old odd linear component survives with leading risk coefficient 1/d. An even component contributes another 1/d. Thus this additional interpolation constraint doubles the leading risk coefficient, rather than removing the close-pair divergence. Exact finite-angle risks and every dual-feasibility/equality step are in PROOF.md.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_three_point.py > verification_output.txt
```

All assertions passed in 2.32 seconds, peak RSS 15,204,352 bytes, one thread, actual nice 20. The sandbox denied nice's attempted priority adjustment; inherited priority already satisfied the requirement. Independent direct circle integration agrees with the new exact risks to 3.95e-10 relative error. Exhaustive continuous dual pricing, separately recovered dual multipliers, interpolation, primal/dual equality, an S^2 surface integral, and odd-part coefficients all passed. Full commands, output, and audit are in LOG.md; per-case data are in verification_data.json.

What failed: the preliminary angular-grid LP only approximates kink atoms and emitted NumPy floating-point warnings. It supplied candidates, and none of its numerical values is needed for the theorem. The final proof and verification use no NumPy or optimizer. Deliberately extending the positive-label formula to theta=1.2 fails interpolation by 0.12928494679; the stated angle restriction is necessary for that formula.

The bounded literature check found no later resolution; opened sources and their scope are recorded in LOG.md. No SOLVED_ELSEWHERE.md was warranted.

What remains uncertain: random-triple risk, stability under perturbing the third point out of this geometry, additional interpolation constraints, penalized biases, and GD selection. This deterministic three-point family has probability zero under iid continuous inputs. It supplies no classification of the n-to-infinity risk limit and no new risk-moment assertion for random samples. No novelty claim is made for the elementary atomic calculation.

The next worker should perturb x3 to a general point at a fixed nonzero angle, including an out-of-plane component when d>=3. Prove or refute a uniform lower bound R>=c/theta^2 on an open set of third-point locations for bounded third labels. A positive-measure version is needed before inferring anything about training-averaged risk for random triples. The explicit certificates here give a starting point, but their kink equalities mean robustness cannot simply be assumed.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 03:38 +04.
