# T264 work log

Task: "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 11:34 +04.

## Orientation and task record

All authored files stay in this folder. Earlier folders are read only. No git,
subagents, external messages, or external-store mutations. The task-specific
folder-only rule overrides the general brain/checklist/mesh commands, which
write outside this folder. Startup memory/index and relevant stored material
are read directly instead. This file is the local task record.

Compute state read before work: status warn (cpu_saturated), mode
owner_away_open, 48% free memory. Only short, sequential standard-library
computations are planned, with OMP_NUM_THREADS=1 and nice -n 15. Every
verification script will check actual priority, wall/CPU time, and peak RSS.

## 1. Bounded literature check (11:34–11:36 +04)

Used the web search tool with ReLU, tempered overfitting, minimum norm,
fixed dimension, and 2025/2026 queries. Opened these primary arXiv pages:

- https://arxiv.org/abs/2207.06569 : Neil Mallinar, James B. Simon,
  Amirhesam Abedsoltan, Parthe Pandit, Mikhail Belkin, Preetum Nakkiran,
  *Benign, Tempered, or Catastrophic: A Taxonomy of Overfitting*.
  The source taxonomy; kernel theory and neural-network experiments.
- https://arxiv.org/abs/2305.15141 : Guy Kornowski, Gilad Yehudai,
  Ohad Shamir, *From Tempered to Benign Overfitting in ReLU Neural Networks*.
  Classification, including univariate and growing-dimensional regimes.
- https://arxiv.org/abs/2307.15396 : Nirmit Joshi, Gal Vardi,
  Nathan Srebro, *Noisy Interpolation Learning with Shallow Univariate ReLU Networks*.
  Univariate regression; not the multivariate limit.
- https://arxiv.org/abs/2410.19092 : Itamar Harel, William M. Hoza,
  Gal Vardi, Itay Evron, Nathan Srebro, Daniel Soudry,
  *Provable Tempered Overfitting of Minimal Nets and Typical Nets*.
  Binary-weight deep classification with minimum-size or random selection;
  not minimum-parameter-norm two-layer regression.
- https://arxiv.org/abs/2611.01105 : Weizhao Li, Lei Shi, Hanfei Zhou,
  *Minimum-Norm Interpolation in Weighted Variation Spaces: Direct and Inverse Problems*.
  Its abstract concerns noiseless interpolation of a variation-space target.

A search aggregator attached variation-space text to arXiv:2611.03362;
opening the actual arXiv page identified Martin Ehler's unrelated
*Optimal bounds for design curves on the torus*. The aggregator was discarded.
No resolution of the specified noisy minimum-norm/GD fixed-dimensional limit
was located. The bounded search ended within five minutes. This is not a
proof of absence; no SOLVED_ELSEWHERE.md is warranted.

## 2. Earlier work: reading and independent recheck in progress

The latest main claim is the all-fixed-n hemisphere theorem. Its argument
combines a bounded correction construction, localization at nearly sharp
close-pair cost, and a positive-probability all-one-hemisphere event.
The next recheck will independently verify the localization bound and the
tail/moment factors, then verify a correction example without changing any
earlier file.

Proposed extension, to be finalized after that recheck: the fourth-point case
with extras at e2 and -e2 and bounded labels. The old leading cost is impossible
there. The antipodal identity f(x)-f(-x) = (sum gamma_j u_j) dot x suggests
cancellation of the leading profile and a different exact dual problem.

Read all four predecessors' reports, logs, proofs and Python scripts. The
round-5 spanning lemma is valid: in the negative-first-coordinate cone, each
extra point's activation hyperplane has an isolated derivative jump; positive
second coordinates exclude both parallel duplicates and antipodes. Its finite
basis and finite-cover arguments give the asserted compact-set constants.
The localization inequality, summed gap, sign probability 2^(2-n), and
critical moment r=(d-1)/2 re-derive exactly as stated. The 2/d risk coefficient
also follows independently from the odd/even decomposition X2-|X2|.

Created recheck_prior.py, using a fresh 2x2 Cramer solve for a four-observation
competitor, direct scalar quadrature, signed ambient directions, and joint
label/hemisphere enumeration. Initial command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 recheck_prior.py > prior_output.txt
```

The first run passed localization but failed an arbitrary cost threshold of 8
for this new explicit competitor. Directly solving the two correction equations
gives bounded coefficients of magnitudes about 10.1 and 5.4, so that threshold
was too small. Replaced the competitor thresholds by 18 for excess cost, 20 theta
for uniform error, and 50 theta for squared-risk error. No predecessor bound
or theorem is altered. The exact per-case costs will be saved on rerun.
The sandbox denied nice's attempted adjustment; the script's inherited-priority
check passed (actual nice at least 15).

Reran the same command: exit 0. Output saved in prior_output.txt and
prior_data.json. Passed 12,600 signed ambient directions; the four-point
correction had maximum displayed interpolation error 8.88e-16. At theta=1e-4,
excess cost above 2/sin(theta) was 16.4694134573 and theta^2 R2 was
0.999653377691, tending to 1=2/d. Joint sign enumeration recovered 2^(2-n)
for n=3..9, and both angular and tail moment exponents equal -1 at the
endpoint. Runtime 0.1913 seconds, peak RSS 15,548,416 bytes, actual nice 20,
one thread. The earlier main claim holds.

## 3. One chosen extension, before proof and implementation

Solve the exact minimum-norm four-observation problem with the same close
opposite-label pair and extras (e2,A), (-e2,B), allowing arbitrary bounded
A,B and every ambient d>=2. This is precisely the latest report's proposed
next geometry. It tests whether opposite-hemisphere constraints can remove
the global close-pair risk divergence rather than merely changing its constant.

Use the atomic dual problem rather than a discretized optimizer. The candidate
dual subtracts b times the antipodal response difference from the pair response
difference. If its exposed atoms determine all minimizers, derive the exact
cost, limiting function and risk. Check all activation regions, ambient
off-plane directions, sign/label thresholds, and two independent risk integrals.
This is one deterministic four-point extension, not a random-design or
large-sample theorem.

## 4. Exact theorem written

Wrote PROOF.md. Let a=cos(theta/2), b=sin(theta/2), s=sin(theta),
u=(b,a), v=(-b,a). The dual multipliers
(1/(ab), -1/(ab), -1/a, 1/a) have price

    [sigma(ap+bq)-sigma(ap-bq)-bq]/(ab).

Its absolute numerator is min(a|p|,b|q|), whose unit-ball maximum is ab.
Equality forces the four planar directions (plus/minus b, plus/minus a),
even if weights outside the plane are permitted. Their response matrix fixes
the four coefficient totals. When A<=1/(2b) and B>=-1/(2b), their signs attain
the dual bound, proving every minimizer has the same function and exact cost

    Qmin = 4/s + (B-A)/a.

The zero-extra-label part is (|u.x|-|v.x|)/s, equivalently
sign(x1*x2) min(|x1|/a, |x2|/b). It is uniformly bounded by |x1|/a.
The full function is this base plus A sigma(v.x)/a + B sigma((-u).x)/a.
Consequently theta*f -> 0 uniformly, while the unscaled function converges
in every finite Lp to x1 sign(x2)+A sigma(x2)+B sigma(-x2). Its squared-risk
limit is [1+(A^2+B^2)/2]/d, finite and positive. The base is even and its
cross terms with the corrections' limiting parts vanish by x1 reflection.

Derived the exact risk a second way from the spherical ReLU product integral.
Also derived the zero-label risk by a quadrant integral of the clipping formula.
The formulas agree algebraically. A numerical verifier will check continuous
dual pricing, independently recovered multipliers, exact risk by activation-arc
quadrature, the small-angle cancellation, all four Rademacher label choices,
bounded non-Rademacher labels, the sign boundaries, and a deliberate
out-of-domain case. No direction-grid optimizer enters the proof.

## 5. First extension verification passed

Created verify_antipodal.py and ran:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_antipodal.py > verification_output.txt
```

Exit 0. All 109 admissible angle/label cases passed interpolation, primal/dual
equality, two independent circle integrals, and the quadrant risk formula.
Continuous pricing enumerates every activation boundary and every stationary
point on each arc, rather than sampling a direction grid. It gave maximum
price error 4.44e-16. The multipliers were separately recovered from four
exposed-atom equations. Maximum interpolation error was 1.82e-12, atom/clipping
discrepancy 2.55e-12, and normalized risk discrepancy 4.64e-10. A further 9,000
signed ambient directions checked the exact absolute-price identity in d=2,3,7.

All four Rademacher label choices, zero labels and non-Rademacher bounded labels
were checked. At theta=1e-6 and (A,B)=(-1,1), the risks were
1.00000028779 (d=2), 0.666666858529 (d=3), and 0.285714367941 (d=7), tending to
2/d. A separate S^2 surface integral gave 0.583030672094 versus formula
0.583010260173 at theta=.2, A=1, B=-1. The surface quadrature is an independent
normalization check, not the high-accuracy comparison used for the exact risk.
The run took 0.2793 seconds, peak RSS 17,006,592 bytes, actual nice 20,
one thread. The only diagnostic was nice's denied adjustment; actual inherited
priority passed before computation.

The sign-boundary test recovered the old two-point minimum exactly, both its
cost and risk. The labels A=1/(2b), B=-1/(2b) are unbounded as theta decreases;
this shows the bounded-label hypothesis is essential for the finite risk limit.
Deliberately crossing A's upper sign boundary made the v coefficient positive
and produced a strict primal/dual gap 2/a=2.02271288535 at theta=.3. Thus the
sign condition cannot be silently dropped. No extension check failed.

Added a separate odd/even audit to PROOF.md: all 1/s terms cancel in the odd
vector, leaving (-b(A+B)/a, A-B). The odd-part risk has finite limit
(A-B)^2/(4d), and the even-part limit is [1+(A+B)^2/4]/d. Their sum recovers
the total limit independently. Added checks of this vector identity and
direct activation-arc integration at theta=1e-6 to the verifier; a final run
will verify these additions.

Correction to the earlier recheck summary: across its three angles the maximum
interpolation error was 1.78e-15; 8.88e-16 was the smallest-angle record printed
in prior_output.txt.

## 6. Final mathematical and artifact audit

Reran verify_antipodal.py with the same command after adding the independent
odd-vector and small-angle arc-integral checks. Exit 0; all assertions passed.
All earlier numerical discrepancies and counts were unchanged. Final resource
record: 0.2532333340 seconds, peak RSS 16,252,928 bytes, actual nice 20,
one thread. The saved verification_data.json now includes independent_arc_risk
for all 18 limit cases.

Audited every theorem hypothesis: 0<theta<pi and the two exact coefficient
sign conditions for the finite-angle formula; bounded labels for all limits;
width m>=4 or unrestricted; no biases/skips/intercept; normalized spherical
measure; every minimizing function, including off-plane weights. Restricted
the recovery of the *two-point minimum* at the sign boundary explicitly to
theta<pi/2, where the earlier two-point formula applies. The four-point theorem
itself remains valid throughout its stated sign domain. Checked the second
risk derivation, the 2/d planar-radius multiplier, and the first-order
coefficient again against the saved values. No unresolved mathematical
discrepancy remains in the stated deterministic theorem.

Wrote REPORT.md with the exact required verdict line, result beyond the prior
work, commands/resources, failure record, limits of interpretation, and next
step (perturb away from antipodality). A first read-only artifact audit caught
a literal '+and' formatting typo in REPORT.md. Fixed it; no mathematical file
or numerical value changed. Saved the audit as audit_artifacts.py so the final
consistency check is reproducible:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_artifacts.py > audit_output.txt
```

Final artifact audit: exit 0. Saved audit_output.txt reports PASS for the
verdict, parsed scripts, all 109 exact cases, 18 independently integrated
limits, 9,000 signed directions, saved outputs, report figures and resource
limits. The nice diagnostic again reflected a denied adjustment with compliant
inherited priority. No numerical rerun was needed after the formatting-only fix.

Local task record: the requested next four-point geometry is solved exactly.
The general fixed-dimensional large-sample and GD questions remain unresolved.
No predecessor files were edited. No git, subagents, external-store writes,
accounts, or external messages were used.

Task: T264, "take the NEXT checkable step on this problem, building on that work" — 2026-11-15 11:34 +04.
