# Open problem T264: Tempered overfitting of interpolating ReLU networks in fixed dimension

Statement: Mallinar et al. propose a taxonomy (benign, tempered, catastrophic) of interpolation with noisy labels and conjecture that interpolating ReLU networks in fixed input dimension are tempered: the excess risk stays bounded but does not vanish as n → ∞. For minimum-norm (or GD-trained) interpolating two-layer ReLU networks with inputs in a fixed dimension d ≥ 2 and label noise, determine whether the limiting excess risk is zero, finite and positive, or infinite.

Caveat: For univariate inputs (d = 1) the question is settled: tempered for some losses/norms, catastrophic for others (Kornowski–Yehudai–Shamir; Joshi–Vardi–Srebro).

Source: N. Mallinar et al., Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting, arXiv:2207.06569 (2022); G. Kornowski, G. Yehudai and O. Shamir, arXiv:2305.15141 (2023); N. Joshi, G. Vardi and N. Srebro, arXiv:2307.15396 (2023)

Where it stands (checked by us, Nov 2026): d = 1 settled; d ≥ 2 open as far as the writer knows.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T264 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T264 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T264 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T264 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PROVED Infinite high-order risk moments at every fixed sample size for homogeneous minimum-norm ReLU interpolation on the sphere.

The earlier three-observation result holds. An independent re-derivation of
the mass-localization estimate and a fresh numerical audit confirm its risk
coefficient 2/d. Direct circle integration agrees with the earlier exact
special-case risks to 1.03e-9 relative error; 9,000 signed atom directions
also pass the localization inequality.

The new result extends the close-pair mechanism to any fixed number n>=3 of
observations. If the other n-2 distinct points all lie in one separation
hemisphere, bounded-cost corrections can vanish at both members of the close
pair. Every minimum-parameter-norm interpolant therefore satisfies

```text
theta f_theta(x) -> -2 epsilon sigma(-epsilon e2 dot x),
theta^2 R(f_theta) -> 2/d,
```

uniformly on the unit ball and over bounded labels. Here the close pair is
cos(theta/2)e1 +/- sin(theta/2)e2 with labels (1,-1), and epsilon is the common
sign of the other points' e2-coordinates. The convergence is uniform on compact
sets with positive cap distance and positive separation among the extra points.

The model is homogeneous two-layer ReLU regression, with objective one half
the sum of squared parameters in both layers. There are no biases, skips, or
output intercepts. Width is unrestricted, or fixed at any value m>=n.
The assertion covers every minimizer and permits off-plane inputs and weights.

Consequently, for n iid uniform inputs on S^(d-1) with independent Rademacher
labels and zero regression function, every measurable minimum-norm selection
has conditional squared excess risk R_n satisfying

```text
E[R_n^r] = infinity for every n>=3 and r >= (d-1)/2.

liminf(t -> infinity) t^((d-1)/2) P(R_n>t)
  >= 2^(2-n) C_d/(d-1) * (2/d)^((d-1)/2),
C_d = Gamma(d/2)/(sqrt(pi)*Gamma((d-1)/2)).
```

In particular, E[R_n]=infinity for every n>=3 in d=2 and d=3. The expected-risk
sequence thus has extended-real limit infinity in this precise model. Unlike
the predecessor's n=3 result alone, this establishes an expected large-sample
conclusion. It does not establish divergence in probability: the hemisphere
event used in the proof has probability 2^(3-n), which decreases to zero.
For d>=4 the mean-risk question remains open here. No matching upper tail or
finiteness of lower-order moments is proved.

The missing correction lemma is proved in PROOF.md: atom directions with
u dot e1<0 span arbitrary responses on distinct points in the positive
separation hemisphere. Each point's activation hyperplane meets this open
cone, so derivative jumps rule out any nonzero linear relation. Choose n-2
independent atoms; their response matrix inverse gives bounded corrections,
and their negative first coordinates make them vanish at both close samples
for small theta. Two base atoms plus these corrections give cost
2/sin(theta)+O(1). A compactness argument supplies the uniform constants needed
for the random-sample conclusion. On the full-measure subset of distinct
projected ratios, a separate explicit triangular construction proves the
same interpolation claim.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_finite_n.py --prior-only > prior_output.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_finite_n.py > verification_output.txt
```

Both commands passed. The full verifier checks 78 feasible networks in d=2,3,7
and n=3,4,5,6,10, both hemisphere signs, bounded labels and three angles. These
are explicit competitors, not computed minimizers. Maximum interpolation error
is 1.07e-13. A tied-projected-ratio example uses off-plane correction directions;
independent circle and S^2 integration check risk normalization. Sign enumeration
and spherical-cap integration separately check all tail factors for n=3..10,
d=2..7. The moment endpoint is checked by both angular and tail integration.
The full run took 0.626 seconds and 17,367,040 bytes peak RSS, one thread,
actual nice 20. Per-case data are in verification_data.json; LOG.md records
the commands, output, literature check and mathematical audits.

What failed or cannot be extended directly: duplicated points do not support
arbitrary labels, and projected-ratio ties defeat the triangular construction.
The general correction lemma covers distinct tied-ratio points, and a separate
numerical example verifies that case. Extra points in opposite separation
hemispheres contradict the sharp 2/sin(theta)+O(1) cost premise: localization
would force both limiting signed masses to zero although their sum tends to 2.
Their optimal leading cost and risk are not determined here. No mathematical
verification failed. The shell denied nice's attempted priority adjustment;
the script verified compliant inherited nice 20 before computing. An attempted
log patch had a context mismatch and was corrected without changing any result.

The literature check ended within five minutes and found no later full
resolution. The opened primary sources, exact author names and scope checks
are listed in LOG.md. No SOLVED_ELSEWHERE.md was warranted. This is a result
relative to the predecessor reports; no broader novelty claim is made.

Remaining uncertainty: conditional-risk convergence in probability, expected
risk in d>=4, lower-order moment finiteness, sharp tail constants, penalized
biases, full-dimensional homoscedastic designs, and GD selection. The constants
in the correction construction need not stay bounded as n increases.

Next worker: study a fourth point in the opposite separation hemisphere.
First take extras z=e2 and z'=-e2, both with bounded labels, and determine the
leading minimum cost and scaled-risk profile as theta decreases to zero.
The old sharp-cost premise is now provably impossible; a different limiting
atomic optimization is needed. This geometry occurs in typical large samples,
whereas putting every extra point in one hemisphere becomes exponentially rare.
Do not infer typical-risk behavior from the infinite expectations proved here.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 08:58 +04.
