# T067 Tightness of the Kesten-Stigum bound for Potts reconstruction (q = 3, 4, ferromagnetic)

Lead: agent N, written 2026-10-14 23:3x from the papers themselves (Mossel-Sly-Sohn arXiv:2212.03362v2 read in
(local file); Sly arXiv:0811.1208; Bhatnagar-Maneva arXiv:0903.4812 and
Gu-Polyanskiy arXiv:2303.14688 from their abstracts only).

## STATEMENT
Broadcast on the d-ary tree (or a Galton-Watson tree of mean d) through the symmetric q-state Potts channel
M = lambda I + (1 - lambda) J/q with lambda > 0. Reconstruction holds iff d lambda^2 > 1, for q = 3 and q = 4, every d.
Equivalently (MSS Lemma 2.2; Sly Cor. 2.4 for d-ary): the magnetization x_n = E[X+(n)] - 1/q decreases to 0 for every
d lambda^2 <= 1. Reconstruction for d lambda^2 > 1 is classical (Kesten-Stigum); only NONreconstruction at and below
the bound is open.

## FRONTIER
- Sly, Reconstruction of symmetric Potts models (Ann. Probab. 2011, arXiv:0811.1208): q = 3 tight on the d-ary tree for
  d >= d0, d0 not explicit; q >= 5 not tight.
- Mossel-Sly-Sohn, Exact phase transitions for stochastic block models and reconstruction on trees (Ann. Probab. 2025,
  arXiv:2212.03362v2): Theorem 1.12, q = 3 and q = 4 tight, with nonreconstruction AT the bound, on GW(pi_d) for
  d >= d0 under Assumptions 1.10-1.11 (regular and Poisson included). d0 depends only on K(.), not explicit.
  Theorem 1.13: q = 4 antiferromagnetic not tight for d < d* (d*_Reg ~ 24.408, d*_Poi ~ 22.2694); q >= 5 not tight
  either sign. Their own open problems (p.6): "Can one prove Theorem 1.5 for q = 3 and small d?"
- Bhatnagar-Maneva arXiv:0903.4812: "surveys", a certified finite-size representation of the root-posterior law that
  does not grow with depth; gives reconstruction-threshold BOUNDS for Potts on small-degree trees. A purely
  computational method of this kind cannot reach the KS bound itself (at d lambda^2 = 1 the decay is polynomial, so no
  finite-depth computation shows x_n -> 0). It is the prior art for the computational half below.
- Gu-Polyanskiy arXiv:2303.14688: BP fixed-point uniqueness for d lambda^2 >= 1 + C max(lambda, 1/q) log q - the
  ABOVE-KS side, not this question.

## ARCHITECTURE
MSS (and Sly before them), for fixed q:
1. Monotonicity: x_n is nonincreasing; nonreconstruction iff x_n -> 0 (Lemma 2.2).
2. Bayes recursion (9)-(10): X+(n+1) = Z_1 / sum_i Z_i with Z_i = prod_j (1 + q(Y_ij - 1/q)), the Y's built from the
   children's subtrees; Proposition 2.3 gives the conditional independence and the symmetry that let Y's moments be
   written through (X+(n), X-(n)).
3. Local expansion (Sections 3-4): Taylor expand 1/(1+x) in (10); a priori estimates z_n - x_n/q = O_q(x_n^2)
   (z_n = E(X+ - 1/q)^2) and Proposition 4.4 (polynomial moments via factorization) give, WHEN x_n IS SMALL ENOUGH,
   (15): x_{n+1} = d lambda^2 x_n + E[C(C-1)] lambda^4 q(q-4)/(2(q-1)) x_n^2 + (third-order term) x_n^3 + o(x_n^3).
   For q = 3 the x^2 coefficient is negative (q(q-4) = -3), so at d lambda^2 = 1 it gives polynomial decay.
   For q = 4 it vanishes and the sign of the x^3 coefficient decides (negative at lambda = +d^{-1/2}).
4. Global entry (Section 5): for d large, a normal approximation conditional on T gives x_{n+1} <= g_q(d lambda^2 x_n)
   for a continuous g_q with g_q(s) < s on (0, (q-1)/q]; so x_n eventually enters the region where (15) holds.

## FAILURE POINT
Step 4, in the authors' words (p.10): "Unfortunately, for small d, we are not able to show that x_n becomes small
enough to apply the estimate (15)." The CLT needs many children; at d = 2, 3, ... the root's posterior is a product of
a few non-Gaussian factors and g_q is not available. Step 3 is also non-quantitative: "small enough" is a delta(q)
from O_q constants and o(1) terms, never written down, so even a perfect numerical computation of x_n has no explicit
target to hit.

## SHAPE
Perceptron shape, per degree. For fixed (q, d) on the d-ary tree the problem splits into
(A) an explicit local lemma: constants delta, c > 0 with x_{n+1} <= d lambda^2 x_n - c x_n^2 for all x_n <= delta
    (q = 3; at d lambda^2 = 1 this already forces x_n -> 0), uniformly in lambda in [lambda_lo, d^{-1/2}];
(B) a certified computation: an information-INCREASING (upper-bound) discretisation of the posterior-law recursion
    run to depth N shows x_N < delta.
Below some lambda_lo nonreconstruction is easy (e.g. by the entropy/SDPI bounds, which miss KS by a constant), so
(B) only has to cover a compact lambda-interval ending at d^{-1/2}. Then an explicit d0 for Sly/MSS step 4 (a
Berry-Esseen version of the normal approximation) would leave finitely many degrees. The first target is one degree.

## OBSTRUCTION
No explicit local radius: the expansion (15) holds "for x_n small enough" with constants never computed, and nothing
quantitative connects a computed x_N to it. A row move is anything that makes (A) explicit for some fixed (q, d), or
that joins an explicit (A) to a certified (B).

## SETTLED
- The supplied list omitted MSS 2025: q = 3 AND q = 4 ferromagnetic are tight for large mean, on GW trees too
  (worker R T067-LIT-001, checked against the paper here). The open part is SMALL d (and GW at small mean).
- One-edge entropy (KL) contraction with uniform prior has coefficient strictly above lambda^2 for q >= 3, so a
  scalar SDPI route cannot reach KS (worker R T067-KL-001; consistent with Gu-Polyanskiy's sharp constants).
- A universal second-moment contraction x_out <= d lambda^2 x_in over all symmetric Bayes-consistent laws is FALSE
  (q = 3, d = 2, lambda = 7/10) - the leaf-started recursion's own invariants are needed (worker R T067-CHI-001).
- The second moment alone does not determine the next one (worker R T067-MOM-001).
- Censoring ferromagnetic trees does not rescue the KS-factor inequality (worker R T067-CENSOR-001).
- Fixed-point reduction (worker R T067-FIXEDPOINT-001, PASS) and the trivial-fixed-point radius 2.2e-9 (T067-LOCAL-001,
  PASS). Do not re-prove either; cite them.
- Corner bounds on V over all laws cannot widen the radius (reviewer, 14 Oct): the needed constant is ~2, the corner
  argument gives 2078.
- Certified upper-bound BP grids are prior art in spirit (Bhatnagar-Maneva 2009); a grid bound on x_N by itself is a
  numerical bound, not a move.

## FIXED-POINT FORM (added 14 Oct 23:5x from worker R's T067-FIXEDPOINT-001 v1 and T067-LOCAL-001 v1; both reviewer PASS
## 14 Oct, agent P, worker R/AUDITS_FROM_REVIEWER.tsv: N96 depth 500 re-run 0.011414236769 vs claimed 0.011414247507,
## the safe side; LOCAL-001 checked by hand and on 5 exact laws, true drift on a small orbit -0.380 x^2 = MSS's -3/8)
Reviewer's point for 1a: reaching sqrt(m) ~ 0.23 with LOCAL-001's own Section 3 would need the (2,2) corner constant near
2 instead of 2078. No tidying of corner bounds gets there; 1a has to use the fixed point's own structure (V and h as
functionals of mu satisfying mu = T_lambda mu), not norm corners over all laws.
No rate is needed. x_n decreases to a limit; FIXEDPOINT-001: the fully observed level law converges to a
colour-symmetric, uniform-mean fixed point mu of the binary BP update T_lambda, whose x is x_inf <= x_500 < 0.0114
(worker R's certified grid, T067-BP-UPPER v3; x here is E sum_i (p_i - 1/3)^2). LOCAL-001: such a fixed point with
x <= 1/450000000 (2.2e-9) is the uniform point mass. So the theorem at the point follows from an EXCLUSION RADIUS
>= 0.0115, and the gap is a factor of about 5e6.
Where LOCAL-001 loses it (proofs/T067-LOCAL-001_v1.md in worker R): Section 4's second-moment drift
x' <= 2 lambda^2 x - m^2/108 (m = 9 lambda^2 x) needs only t = sqrt(m) below roughly 1/32, i.e. x up to about 2e-4.
The radius is killed in Section 3, the fourth-moment step V <= 4m^2, by the crude bound V' <= V/2 + m^2 + 2078 V
sqrt(m): every monomial evaluated at the corner r0 = s0 = 2 and divided by 32. A sharp control of V (and of the
third absolute moment h) at a fixed point is the lever. The heuristic decay x_n ~ 1/(0.1875 n) = 5.3/n matches the
grid's 0.0107-0.0114 at n = 500, so x <= 2e-4 would need depth ~25,000 AND a grid fine enough that the
upper-bounding discretisation does not plateau above it - pushing the grid down is the expensive side.

## STATE
15 Oct 08:47, lead agent N. d = 5..255 PLAN from worker R's measured piecewise table (floating point, 08:28): the fixed-
point moment ratio U/M^2 peaks near 2.1 (Gaussian value 2) and the sampled gap gamma(s) = (s - g_3(s))/s^2 has minimum 0.5866
at s = 2/3 on [1/10, 2/3] (9/20 is conservative). Floors: with the PROVEN moment ceiling min(5, 2/(3s)) piecewise and a
general-L Lindeberg lemma (L = 1/sqrt(d)) about d >= 156 (next narrowing; needs certified piecewise gaps); with a proved
U <= ~2.2 M^2 about d >= 73. Degree 5 by orbits: 817 orbits, crossing x < 3/100 near depth 40-46 (approximate). Lead
misread the first table's R = 1 + 2U/M^2 as U/M^2 at 07:5x and corrected it at 08:47.
15 Oct 07:12, lead agent N. d >= 256 RECORDED NARROWED (T067-SHARP-D0-001; worker S passed SOFTMAX 07:03, SHARP-LINDEBERG
07:06, SHARP-D0 07:12, after the reviewer). q=3 open only for d = 5..255. Before planning d = 5..255: worker R's measured table of the
effective constant along the BP iterates (asked 05:4x, 06:1x). The method's floor is where (C_U U + C_M M^2)/(81x^2) really sits.
15 Oct 06:47, lead agent N. d >= 1981 RECORDED NARROWED (T067-D0-001, worker S PASS 06:44 after the reviewer's 04:5x;
SIGNED-LINDEBERG and GAUSSIAN-GAP also have both audits). q=3 is now open only for d = 5..1980. NEXT, already one audit:
T067-SHARP-D0-001 v1 (sha 95e6c24f) gives d >= 256 from SHARP-LINDEBERG-001 v1 (C_U<1/4, C_M<31/180, so the error is
< (576/(5d))x^2 against the (9/20)x^2 gap) and SOFTMAX-DERIVATIVES-001 v1; reviewer PASS on all three 06:2x-06:3x, worker S queued.
On its second audit record narrowed d >= 256. Then d = 5..255 is the open list; measure the effective constant before planning.
15 Oct 05:07, lead agent N. d = 4 IS SETTLED: worker S passed DEGREE4-LOCAL (04:25), -UPPER (05:00, own exact replay) and the composition (05:05), after the reviewer's 03:38 pass. Recorded as a special move. Settled at q = 3: d = 2, 3, 4.
15 Oct 04:5x, lead agent N. d0 = 1981 HAS ONE AUDIT: reviewer PASSED T067-D0-001 v1 (sha bd1b565e) and
SIGNED-LINDEBERG-001 v1 (04:50 rewrite, sha 651cb056): q = 3 critical (and subcritical) nonreconstruction on the regular
d-ary tree for EVERY d >= 1981. Lead read 04:5x: U <= 5M^2 by F2 over prefixes, so x - g_3(x) <= 891x^2/d at a fixed point
with x >= 1/10, against the certified (9/20)x^2 gap on [1/10, 2/3]; 9*1981 > 20*891, so the limit enters x < 1/10 and
UNIFORM-LOCAL (d >= 100) forces uniform. worker S has GAUSSIAN-GAP, SIGNED-LINDEBERG and D0-001 queued after DEGREE4 and T170.
On worker S PASS: record target 4 narrowed (explicit d0 = 1981; Sly / Mossel-Sly-Sohn had large d with no explicit constant).
Then q = 3 is open only for d = 5..1980 - a finite list; plan it then (signed-constant measurement first: is 1981 near the truth?).
15 Oct 04:3x, lead agent N. TARGET 4 PIECES ALL ONCE-PASSED: UNIFORM-LOCAL + CUBIC-FUSION (two audits; recorded 04:13),
GAUSSIAN-GAP-001 (reviewer 03:57; |x - g_3(x)| >= (13/200)x outside the local radius), LINDEBERG-001 (reviewer 04:25; constant
159839267/4050000 < 40, exact), GAUSSIAN-QUAD-001 and RESCALE-001 (reviewer 04:25). Together they give q = 3 nonreconstruction
at criticality for every d >= 378,699 = ceil((8000/13)^2) - but only as the composition T067-D0-001 with the entry step written
with constants (worker R, asked 03:5x, not yet posted); the reviewer has not ruled on any composition. Record target 4 narrowed
(all d >= d0, explicit) on D0-001's two audits. SIGNED-LINDEBERG-001 v1 (the O(x/d) route) is a draft.
15 Oct 03:4x, lead agent N. d = 4 HAS ONE AUDIT: reviewer agent P PASSED DEGREE4-LOCAL-001, DEGREE4-UPPER-001
and DEGREE4-001 v1 at 03:38 (independent replay of all 82 depths and every final orbit mass; x_82 = 2966661829103/140737488355328
< 19/900, gap 3.17e-5; LOCAL constants exact). worker S's second audit is first in its queue; record d = 4 settled when it passes.
worker R stays on target 4 (4a + x-proportional Lindeberg error), NOT d = 5.
15 Oct 02:50, lead agent N. d = 3 IS SETTLED: the reviewer's second audit of TERNARY-UPPER-001 and TERNARY-001 passed
at 02:50 (exact replay of all 106 depths from the text). Recorded as a special move and a settled route. Settled so far: q = 3 at d = 2 and d = 3.
15 Oct 02:3x, lead agent N. TARGET 4b HAS A CANDIDATE (unaudited): worker R's T067-UNIFORM-LOCAL-001 v1 (conditional on
T067-CUBIC-FUSION-001 v1 and TERNARY-MOMENTS F2,C) excludes every nontrivial symmetric critical fixed point with x <= 3/100
for EVERY d >= 3 and with x <= 1/10 for every d >= 100. The degree enters only through l = d^{-1/2} and r = (k-2)/(d-2), and
two exact Bernstein certificates of degree (17,6) on [0,L]x[0,1] (120 positive and 6 zero coefficients, none negative) cover all d at once:
no cutoff, no sampled degrees. The lead read it once (02:3x): the prefix induction M_k <= kM/d is ordered correctly and the
contradiction at k = d is sound; the load-bearing unaudited input is the cubic sign T >= 0 (CUBIC-FUSION). With delta = 0.1
the x-proportional estimate gives d0 ~ (C/(0.75*0.1))^2 ~ 180 C^2, against 1.2e4 C^2 at the old 0.0115. Reviewer agent P PASSED both
CUBIC-FUSION-001 v1 and UNIFORM-LOCAL-001 v1 at 02:39 (own flint rebuild; worker R/AUDITS_FROM_REVIEWER.tsv); worker S's audit, first in its queue, is the second. Remaining for target 4: 4a (certified g_3 gap)
and the x-proportional Lindeberg error; then canonical entry at large d comes from Sly's Gaussian map, not from this lemma.
15 Oct 01:55, lead agent N. d = 3 IS DONE TOO (one audit): worker R's T067-TERNARY-001 v1 gives q = 3 nonreconstruction
on the regular ternary tree for 0 < lambda <= 1/sqrt(3), the bound included, from TERNARY-UPPER-001 v1 (x_106 <=
23388195913597/1266637395197952 < 37/2000 for 0 < lambda <= 2887/5000), TERNARY-LOCAL-001 v1 (radius 37/2000) and
TERNARY-MOMENTS-001 v1. worker S PASSED all four, 01:10-01:48 (worker S/audits/w682_T067-TERNARY-*), replaying the upper bound
in unbounded integers over all 1,001,642 rows and 106 depths. The second audit (reviewer) is owed before it counts as
settled. d = 4 is written and unaudited: T067-DEGREE4-001 v1 (x_82 <= 2966661829103/140737488355328 < 19/900, radius
19/900 at lambda = 1/2), queued in worker R/AUDIT_QUEUE.md. The pattern now runs degree by degree; target 4 (an explicit d0)
is what turns it into all of q = 3, so the next worker on T067 goes to 4a/4b, not to d = 5 (worker R told 02:00). The degree-by-degree route is marked dead
only while d0 is unknown: once target 4 gives an explicit d0 that is small, the degrees below it come back as finite work.
Earlier, 15 Oct 00:26, lead agent N. TARGETS 1, 2 AND THE LAMBDA PART OF 3 ARE MET for q = 3, d = 2: worker R's T067-BINARY-001 v1 (from BP-UPPER-001 v3,
FIXEDPOINT-001 v1, LOCAL-001 v2, FOURTH-001 v1, all in worker R/proofs) gives nonreconstruction for every
0 < lambda <= 2^{-1/2}, the bound included. Reviewer PASS (agent P, 00:16, worker R/AUDITS_FROM_REVIEWER.tsv)
and the lead's own reading (00:19). SECOND AUDIT DONE: worker S (Codex, cross-model) PASSED all five pieces, 00:50-00:59 15 Oct
(worker S/AUDITS.tsv; files worker S/audits/w682_T067-*): FOURTH-001 v1 (233,289 Bernstein coefficients exact), LOCAL-001 v2
(radius 23/2000), BP-UPPER-001 v3 (all 334,153 transition rows and 500 depths replayed exactly; x_500 = 0.0114142),
FIXEDPOINT-001 v1, BINARY-001 v1 (composition and literature scope: no primary paper settles q=3,d=2). The q = 3 binary
case is SETTLED in the brain (computer-assisted). Do not redo any of it. Live now: q = 3, d = 3 (worker R: the same three pieces at d = 3); q = 4, d = 2 (worker V: target 5,
the cubic term). Target 4 (explicit d0) is open and unstaffed.

## TARGETS
1. Widen the fixed-point exclusion radius for q = 3, d = 2, 0 < lambda <= 2^{-1/2} from 2.2e-9 to >= 0.0115 (meeting
   the grid), every constant written down and checked; or widen it as far as possible and let target 2 meet it lower.
   Sub-steps: (1a) a sharp fourth-moment / third-absolute-moment bound at a fixed point replacing Section 3 of
   LOCAL-001 (the bottleneck); (1b) Section 4's drift with exact rather than worst-corner constants, so the radius is
   limited by the true third-order term of (15), not by the bookkeeping; (1c) if 0.0115 is out of reach analytically,
   a certified computation excluding fixed points with x in [radius, 0.0115] (an infinite-dimensional set of laws:
   say how it is made finite before computing). The recursion form x_{n+1} <= x_n - c x_n^2 is optional.
2. (B) at the same point: a certified x_N < radius from the information-increasing grid (worker R's N96/N168 runs are
   the instrument; x_500 < 0.0114 today; only worth pushing once target 1's radius is known). 1 + 2 together = q = 3 KS tight on the binary tree AT the bound, a new theorem if the literature
   check holds.
3. Extend 1 + 2 to all lambda <= 2^{-1/2} (monotonicity in lambda, or a lambda-uniform (A) plus a finite lambda-grid
   for (B) with a continuity bound), then d = 3, 4, ...
4. An explicit d0 for MSS/Sly step 4 (Berry-Esseen); together with 1-3 for d < d0 this closes q = 3 on regular trees.
   SCALE FIRST (lead, 15 Oct 00:5x, heuristic, unverified - do this before staffing the full target). The argument
   is Sly 2011 Thm 1.1 (sly_2008.txt l.2278-2290) = MSS Thm 1.12 for q = 3: (i) Sly Lemma 4.8 / MSS Prop 4.12 give
   x_{n+1} <= d lam^2 x_n - (3/4) lam^4 d(d-1) x_n^2 for x_n <= delta, delta independent of d (at d = 2 this is the
   -3/8 worker R measured); (ii) Sly Lemma 4.3 / MSS Prop 5.3 (Lindeberg) give |x_{n+1} - g_3(d lam^2 x_n)| <= eps(d);
   (iii) Sly Lemma 4.7: g_3(s) < s on (0, 2/3]. So d0 is the d where eps(d) < inf_{[delta, 2/3]} (s - g_3(s)),
   and near 0 that gap is about (3/4) delta^2. With a uniform eps(d) = C d^{-1/2} this gives d0 ~ (C/(0.75 delta^2))^2,
   about 1e8 C^2 at delta = 0.0115. Even with an error proportional to x (Lemma 5.1's moments are all multiples of
   x_n(T_j), so the third-moment term is about x d^{-1/2}) it is d0 ~ (C/(0.75 delta))^2, about 1.3e4 C^2. So a
   degree-by-degree BP certificate for every d < d0 is out of reach: worker R's d = 2 run took a night.
   MEASURED 00:5x (lead, uncertified, (local dir) + _output.txt): g_3 in Sly's form (4.7)
   with D_i = w_i - w_1 ~ N(-(9/2)s(1,1), s[[9,4.5],[4.5,9]]) (the mean -Var/2 is forced: with half of it the linear
   term is s/2) matches Sly's (4.9) s - (3/4)s^2 - (9/8)s^3 to 1e-11 at s = 1e-3; and 0.587 s^2 <= s - g_3(s) <=
   0.781 s^2 on [1e-3, 2/3] (the minimum ratio is at s = 2/3). So inf_{[delta,2/3]} (s - g_3) = 0.778 delta^2 at delta = 0.0115,
   0.779 at 0.1: the (3/4) delta^2 estimate holds. MSS's Appendix A (mossel_sly_sohn.txt l.3551-3667, the supplement
   is in our copy) gives D * C_{q,psi} * (C/sqrt D)^3, uniform and not x-proportional, and its Gaussian-matching step
   (132) is not quantitative at all (continuity of A^{1/2}); both are rewritable with x-proportional bounds since
   every moment in Lemma 5.1 is a multiple of x_n and |V_j| <= C d^{-1/2}. So d0 ~ (C/(0.78 delta))^2 with delta the
   d-uniform local radius of Sly Lemma 4.8 / MSS Prop 4.12: delta = 0.0115 gives 1.2e4 C^2, delta = 0.1 gives 160 C^2.
   THE LEVER FOR TARGET 4 IS THEREFORE THE SAME AS TARGET 1: an explicit local radius, here uniform in d (the x^2
   coefficient is -(3/4)(1 - 1/d), twice the d = 2 value, which should help).
   The real target is therefore (4a) a certified g_3 gap on [delta, 2/3] (a two-dimensional Gaussian integral, cheap);
   (4b) the Lindeberg error with an x-proportional bound and every constant written (MSS Supplement Sec. 1 gives the
   proof, Appendix A of our copy, to be redone x-proportionally); (4c) d0 from (4a)+(4b); and only if d0 is
   in the tens, (4d) per-degree runs. If d0 is large, the move is a method uniform in d for the middle range (the BP map
   with d as a continuous parameter, or a monotonicity-in-d argument), not more per-degree grids.
5. q = 4: the x^2 term vanishes, so (A) needs the third-order coefficient of (15) with explicit error - harder; only
   after q = 3 is done for one degree.
NOT moves: a sharper grid bound on x_N with no delta to compare against; more auxiliary counterexamples to universal
contraction; Taylor coefficients already in MSS.

<!-- T067-D91-ADMISSION-20261015 -->
2026-10-15T16:51:14.972584+03:00 T067 narrowed: uniform-root q=3 ferromagnetic Potts broadcasting on every regular d-ary tree, integer d>=91, is nonreconstructible for every0<lambda<=1/sqrt(d), including equality. Exact T067-COMPENSATED-D91-001v1 SHA256 3f41f2986e611f38d248077ab2da3352d70634fec300ae91cb40e83655ceb9bd. Two independent full exact-content audits PASS: worker S and P, actual account-id hashes distinct; account W froze identity before semantic read and at completion. Lead independently rebuilt86F+86Q endpoints, all85continuous intervals,124derivative leaves, local126coefficients and analytic composition. Certified E91>3/200 over the entire global-entry interval. Checked large-degree cutoff improves256 to91. Degrees2,3,4 retained; degrees5..90 remain open. Critical canonical convergence and Blackwell subcritical transfer checked. Inherited fusion/moment/softmax premises remain scoped; no unrestricted RESCALE F1 corollary used. No q4/arbitrary-offspring/fullT067 or priority claim.

<!-- T067-DEGREE6-ADMISSION-20261015 -->
2026-10-15T19:15:29.104526+03:00 Degree6 admitted: uniform-root q3 ferromagnetic regular-tree Potts broadcasting is nonreconstructible for every0<=lambda<=1/sqrt6, equality included. Proof SHA256 3d378d6f3b9a0d8275ee82e082e22e775a27e693b70ab3eb7fc59d7618a9e5c9. Five exact-v1 claims passed full independent mathematical reviews on distinct actual accounts. Both fresh direct Bayes replays check667489 rows/all817 final masses/all26 signals. Local radius217/4500 and critical canonical limit checked. Uniform-root q3 ferromagnetic Potts broadcasting, regular six-child tree, every0<=lambda<=1/sqrt6 including equality. Explicit previously reviewed cubic/F2,C/prefix premises retained. No unrestricted F1, degree5, degrees7..90, q4, arbitrary offspring or priority claim. Degree5 and degrees7..90 remain open in this campaign; retained2,3,4 and all d>=91.

<!-- T067-Q4-D2-ONE-ACCOUNT-AUDIT-20261017 -->
2026-10-17 23:3x (agent J): q = 4, d = 2 (target 5) - every piece of the worker V/worker R route checked by one account, NOT admitted.
GRID-001 v2 replayed exactly (U = 1375940705703331/30399297484750848, 478 orbits, 500 depths), FIXEDPOINT-001, SUPPORT-001
(rho = 677/1000), CUBIC-GAIN-001 (six Klein cosets rebuilt), the kernel expectations, and the missing pointwise K >= 0 by an
independent 192-case Bernstein cover (indep_cover.py, delta = 1743/480965 in g24; controls fail both ways). Report:
12_cognitive_architecture/audits/reports/2026/10/17/t067_q4_ks_c259/REPORT.md; paper draft paper_draft_q4_d2_c259/main.pdf
(8 pp). Owed before admission: a second account's audit (requested on the mesh 23:3x, topic t067-q4-second-audit), the
reference details, a public home for the certificates. 
