# T264 work log

Task: "take the NEXT checkable step on this problem, building on that work".
Session start: 2026-11-15 08:58 +04. All new files remain in this folder;
predecessor folders are read only. No git, subagents, or external publication.
The specific folder-only order precludes mesh/checklist/brain writes elsewhere.
Startup memory and compute state were read. A brain recall was attempted at
startup; its automatic refresh could not spawn. No further brain commands will
be used. Local task record: working on the fixed-sample extension below.

## 1. Bounded literature check

Within five minutes, used the web search tool for `"ReLU" "tempered"
"overfitting" 2025 2026 fixed dimension`, `"minimum norm" "ReLU"
"interpolation" "fixed dimension" risk`, and two follow-up 2025/2026 queries.
Opened these primary sources (author names checked on the arXiv pages):

- Neil Mallinar, James B. Simon, Amirhesam Abedsoltan, Parthe Pandit,
  Mikhail Belkin, Preetum Nakkiran, *Benign, Tempered, or Catastrophic:
  A Taxonomy of Overfitting*, [arXiv:2207.06569](https://arxiv.org/abs/2207.06569).
  Kernel results and neural-network experiments; no new learned-feature theorem.
- Nirmit Joshi, Gal Vardi, Nathan Srebro, *Noisy Interpolation Learning with
  Shallow Univariate ReLU Networks*,
  [arXiv:2307.15396](https://arxiv.org/abs/2307.15396). Univariate regression.
- Guy Kornowski, Gilad Yehudai, Ohad Shamir, *From Tempered to Benign Overfitting
  in ReLU Neural Networks*, [arXiv:2305.15141](https://arxiv.org/abs/2305.15141).
  Classification; univariate and high-dimensional regimes.
- Weizhao Li, Lei Shi, Hanfei Zhou, *Minimum-Norm Interpolation in Weighted
  Variation Spaces: Direct and Inverse Problems*,
  [arXiv:2611.01105](https://arxiv.org/abs/2611.01105).
  Approximation of a target in the variation space; not noisy interpolation risk.
- Sunil Madhow, Yu-Xiang Wang, *"Deep lifts": Neural networks can generalize
  even with the dumbest optimizer*,
  [arXiv:2610.23009](https://arxiv.org/abs/2610.23009).
  Uniform-random bounded-parameter interpolators rather than minimum norm or GD.
- Moritz Haas, David Holzmüller, Ulrike von Luxburg, Ingo Steinwart,
  *Mind the spikes: Benign overfitting of kernels and neural networks in fixed
  dimension*, [arXiv:2305.14077](https://arxiv.org/abs/2305.14077).
  Kernel/NTK setting and modified activations; not the requested feature-learning
  classification.

No later full resolution found. This limited search does not prove absence.
No SOLVED_ELSEWHERE.md is justified. Literature search now closed.

## 2. Independent mathematical recheck of round 4

Read the predecessor reports, logs, proofs and scripts. Re-derived the round-4
mechanism directly: the three-unit competitor has sample values (1,-1,tau),
because v=(b,-a) is zero at x1 and has value s=2ab at x2, while -v is zero at
both. For q=z_2>=delta, h=aq-bp>=delta/2 and its correction coefficient is
(tau-sigma(p)/a)/h. Hence its cost is at most 2/s+2+2(H+2)/delta.

For an arbitrary unit u and coefficient sign t, ReLU monotonicity and Lipschitz
continuity give sign(g)=sign(u_2) and |g|<=|u_2|/a, where
g=[sigma(u.x1)-sigma(u.x2)]/s. Thus ||u-t e2||^2<=4(1-a t g).
Summing with weights theta|gamma| gives squared displacement at most
4(M-theta/b), M=theta sum|gamma|. Pair interpolation forces M>=theta/b,
and the competitor bounds M<=2theta/s+Ktheta. The total displacement error
is at most 2 sqrt(M(M-theta/b))=O(sqrt(theta)). At a bounded third response
with q>=delta the positive limiting mass is O(sqrt(theta)); negative mass
tends to 2. Therefore theta f converges uniformly to -2 sigma(-x_2).
Its squared spherical norm is 4 E[X_2^2 1_{X_2<0}]=2/d. Independently,
the odd/even decomposition x_2-|x_2| contributes 1/d+1/d.
The angular density is C_d sin(theta)^(d-2), so the critical moment is
r=(d-1)/2, with logarithmic divergence at equality. The earlier main claim
holds. A fresh computational audit will also be recorded below.

## 3. One chosen extension (before proof or computation)

Extend the close-pair theorem from one extra observation to any fixed finite
number of distinct observations in the same separation hemisphere. The missing
lemma is that ReLU directions strictly negative at the limiting pair point e1
span all responses on those extra observations, so bounded corrections can
vanish at both members of the close pair. Prove this using derivative jumps on
the atom side, then transfer the round-4 mass estimate. This would imply infinite
training-averaged risk moments at every fixed n>=3, rather than only n=3, for
the same spherical input and independent Rademacher noise. The price is a
same-hemisphere event whose probability decreases with n. It supplies no
convergence-in-probability classification.

Compute: startup state status ok / owner_away_open. All numerical runs will use
OMP_NUM_THREADS=1, nice -n 15, small standard-library arrays, a CPU/wall limit,
and a peak-RSS check below 1 GB. The shell reports a denied nice adjustment;
the predecessor observed inherited nice 20, which will be checked in each run.

## 4. Extension proof written

Wrote PROOF.md. The correction lemma holds for every finite set of distinct
points in the open positive separation hemisphere, including equal projected
ratios in d>=3. For each point its weight-space activation hyperplane meets
u.e1<0, so a derivative jump isolates its coefficient in any alleged response
relation. A finite basis of k=n-2 correction atoms follows. Those atoms have
strictly negative first coordinate, hence vanish at the close pair for small
angles. Their response matrix inverse supplies a bounded correction cost.
Compactness gives uniform constants when cap distance and point separation
are bounded below. Two base units plus k correction units suffice, so the
result covers every minimum at fixed width m>=n as well as unrestricted width.

The scaled risk coefficient remains 2/d. The probability that all k remaining
points occupy one separation hemisphere is 2^(1-k)=2^(3-n). With the independent
opposite-label factor 1/2 this gives the designated-pair tail lower constant
2^(2-n) C_d (2/d)^((d-1)/2)/(d-1). The critical moment is unchanged.
In particular, the conclusion is now E[R_n]=infinity for EVERY fixed n>=3
in d=2,3; thus the expected-risk sequence has infinite extended-real limit
in this precise model. This is stronger than a statement at n=3 only, but it
still does not show divergence in probability. No constants uniform in n are
claimed.

Independent construction for auditing: if p_i/q_i are distinct, sort these
ratios and choose unit directions (-e1+t_j e2)/sqrt(1+t_j^2) with t_j between
successive ratios (and one above the last). The correction matrix is upper
triangular with positive diagonal. This gives a separate explicit proof on
a full-measure subset and will be checked numerically against generic Gaussian
elimination. The general derivative-jump proof handles ratio ties.

An initial attempted LOG.md patch had a context mismatch and made no change;
the proof and all mathematical assertions were unaffected.

## 5. Fresh predecessor computation

Created verify_finite_n.py (standard library only). Ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_finite_n.py --prior-only > prior_output.txt
```

Exit 0. The command emits the sandbox's denied nice-adjustment diagnostic;
the script checks actual inherited nice>=15 before computing. Output is in
prior_output.txt and prior_data.json. It integrates the actual prior networks
on the circle independently of the closed risk formula, for both third labels
and three angles, and checks the pointwise mass inequality at 9,000 signed
ambient directions in d=2,3,7. This supplements the independent mathematical
recheck in Section 2. The main prior result holds.

The prior-only run gave maximum relative circle-risk error 1.03015e-9,
9,000 signed directions, 0.242628 seconds, 16,629,760 bytes peak RSS,
actual nice 20, one thread.

## 6. Extension computation passed

Ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_finite_n.py > verification_output.txt
```

Exit 0. Full output is in verification_output.txt and per-case values are in
verification_data.json. The script verifies 78 explicit feasible competitors:
d=2,3,7, n=3,4,6,10, both hemisphere signs, three angles per configuration,
plus a d=3,n=5 configuration with tied projected ratios and genuinely off-plane
correction atoms. The competitors use exactly n listed units (zero coefficients
are allowed). They are not computed minimizers; the proof, not a numerical
optimization, transfers their cost bound to every minimizer.

Representative output:

```text
PASS prior: actual circle quadrature vs exact risk; max relative error 1.03e-09
PASS prior: mass inequality in 9000 signed ambient directions
PASS independent circle integral: 0.757107445036, kernel 0.75710744514
PASS triangular_d2_n10: smallest theta=1e-08, theta^2 R=1.00000033683, limit=1
PASS triangular_d3_n10: smallest theta=1e-08, theta^2 R=0.666666889859, limit=0.666666666667
PASS triangular_d7_n10: smallest theta=1e-08, theta^2 R=0.285714382653, limit=0.285714285714
PASS independent off-plane surface integral: 0.818670413684, kernel 0.818639430728
PASS tied_ratios_d3_n5: smallest theta=1e-08, theta^2 R=0.666666776011, limit=0.666666666667
PASS negative check: duplicated points produce rank one, not two
PASS probability: sign enumeration, sine recurrence, cap integrals, endpoint shells; n=3..10, d=2..7
PASS extension: 78 feasible networks; maximum interpolation error 1.07e-13
All assertions passed.
Resources: {'seconds': 0.6256710829911754, 'peak_rss_bytes': 17367040, 'nice': 20, 'threads': 1}
```

The largest tested excess-cost bound K is 3988.6507781933965, which illustrates
why the proof supplies no useful constant uniform in n. The precise value is
an audit output for these constructed configurations, not a theorem constant
or an optimal cost. All actual interpolation errors were below 1.07e-13.

## 7. Attempts to break the result and second derivations

- The general correction lemma was checked against an independent explicit
  triangular matrix construction. Matrix entries were computed as actual ReLU
  responses and separately as q_i (t_j-r_i)_+/sqrt(1+t_j^2). Generic elimination
  and backward substitution independently recovered the correction coefficients.
- A projected-ratio tie makes that triangular construction singular, but the
  theorem assumes distinct full points, not distinct projected ratios. Tested
  z1=(0,.8,.6), z2=(0,.8,-.6), z3=(.4,.8,sqrt(.2)). A separate selection of
  weight directions with negative first coordinate gave an invertible response
  matrix; all interpolation and scaled-risk checks passed. The proof uses the
  full activation hyperplanes and therefore covers this case.
- Duplicate points with different labels are impossible to interpolate. The
  verifier independently finds rank one for their two identical response rows.
  The theorem's distinctness and compact-set separation assumptions exclude
  this case. No uniform inverse bound is assumed as points collide.
- Opposite separation hemispheres invalidate the 2/sin(theta)+O(1) premise:
  localization would make both limiting masses zero while their sum tends to 2.
  Section 6 of PROOF.md gives the contradiction. Such configurations may have
  a different leading cost; their risk is not determined here.
- Re-derived the risk coefficient from 4 E[sigma(-X2)^2]=2/d and separately
  from the orthogonal odd/even parts X2-|X2|, each with squared norm 1/d.
  Actual circle and S^2 integrals independently check kernel normalizations
  on multi-constraint networks, including off-plane correction directions.
- Re-derived the tail probability factor by enumerating all k hemisphere signs
  and both pair-label signs. The joint probability is 2^(2-n); the test does
  not import this factor from the theorem. Sine-integral recurrences independently
  verify C_d, and numerical cap integration verifies the tail lower constants.
  At n=3 the constant reduces exactly to the predecessor's. For d=2 and 3 it
  simplifies to 2^(2-n)/pi and 2^(2-n)/6 respectively.
- Checked the moment endpoint by angular powers and independently by the tail
  integration identity. Equality yields a 1/theta integrand, hence logarithmic
  divergence, not finiteness.
- Checked the large-sample statement carefully: because E[R_n] is infinite for
  every integer n>=3 in d=2,3, its extended-real limit is infinite. No interchange
  of limits or monotonicity of the optimizer's risk is used. In contrast, the
  event probability 2^(3-n) decreases to zero, so the argument cannot classify
  convergence in probability. It also says nothing about the mean in d>=4.
- Fixed-width existence uses a compact parameter sublevel and a feasible n-unit
  construction. Unrestricted-width existence uses compact atomic convex hulls.
  No uniqueness, rotation-equivariant selection, or identification of GD bias
  was inserted into the random-data argument.

No mathematical check failed. The only execution diagnostic was the denied
nice adjustment; actual nice 20 was verified before both runs. No memory-limit
changes, external writes, or heavier numerical libraries were needed.

## 8. Completion audit

Wrote REPORT.md with the required first-line verdict, the all-fixed-n theorem,
its expected-risk implication in d=2,3, model/width restrictions, commands and
resources, limitations and the opposite-hemisphere fourth-point next step.
Audited its statements against Theorems 1 and 2, equations (15)--(24), and the
saved output. A final small read-only consistency check confirmed the verdict,
the 2^(2-n) factor, 78 data records, compliant priority and peak RSS, and the
existence of every listed deliverable. It passed. No new numerical or
mathematical changes required repeating the verifier.

All authored files are in this folder; all predecessor files remain read only.
No git, subagents, publication, accounts, or external messages were used.
Local task record: done — finite-sample heavy-tail theorem extended to every
fixed n>=3, with infinite expected-risk limit in d=2,3 for the specified model.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 08:58 +04.
