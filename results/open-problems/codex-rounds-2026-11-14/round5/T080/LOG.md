# T080 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Date: 2026-11-15. Exact receipt time unavailable. First retained clock reading: 08:05:35 Asia/Tbilisi (04:05:35 UTC).

## 1. Scope and orientation

Read the startup memory and compute governor state: warn / owner_away_open, CPU saturation, about 49 percent memory free. Read REPORT.md, LOG.md, PROOF.md and scripts from the initial, round-3 and round-4 folders. Earlier folders remain read only. The specific task instruction confines all writes here, so no mesh/checklist/recall logger or brain writer that changes external state is invoked. No git, subagents, background processes or external publication.

All Python commands use OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1, VECLIB_MAXIMUM_THREADS=1, and nice -n 15. The inherited priority is already 20; the wrapper warns when trying to adjust it. Mathematical audits check actual priority and have a 60-second CPU limit. Only small standard-library workloads are planned.

## 2. Literature check (04:05–04:07 UTC; within five minutes)

Web searches: `hard sphere crystallization phase transition continuum proof 2026 Euclidean`; `hard disks orientational order rigorous proof 2026`; `site.arxiv.org "hard sphere" "phase transition" "2026" Euclidean`; `site.arxiv.org "hard disks" "proof" "2026" crystallization`.

Opened these primary sources:

* Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/abs/2607.23873). The abstract explicitly says the Euclidean problem remains open; the theorem is hyperbolic.
* Andreas Göbel, Matthew Jenssen, Marcus Michelen, Marcus Pappik, Will Perkins, Leon Schiller, *Uniqueness, analyticity and mixing for Gibbs point processes via spectral gaps*, [arXiv:2606.28009](https://arxiv.org/abs/2606.28009). This improves uniqueness bounds and does not prove high-activity ordering.

No later Euclidean solution was found. This bounded search is not exhaustive. Search-only hits were not used as mathematical evidence. No SOLVED_ELSEWHERE.md is warranted.

## 3. Independent re-derivation of the round-4 estimate

The earlier main claim holds. For n chosen boxes, keep only zero-or-one particles in each of m_0 n protected balls: the denominator is at least (1+zb)^(m_0 n), with the labeled-coordinate factorial cancelling against assignments to balls. For K=floor(rn), discard every exclusion constraint in the numerator to obtain sum_{k=0}^K (zvn)^k/k!. Alternatively view this as exp(zvn) times a Poisson lower tail. Exponential Markov with theta=max(0,log(zv/r)) gives exponent n H_r(zv), and r=0 gives numerator one. Thus the ratio is at most exp[-n(m_0 log(1+zb)-H_r(zv))], capped at one.

An anchored connected n-set has a deterministic spanning-tree depth-first word of length 2(n-1), whose visited set recovers the set. Hence there are at most (2d)^(2(n-1)) choices. A component with at least n vertices contains such an n-set, so no sum over larger sizes is needed. This independently recovers the stated component tail. Finite-volume components must use only boxes wholly inside the sampling region, as the earlier proof specifies.

For ell=4,a=1/4,r=2^(d-1), the lower bound on tau is r log[z b^2 r/(e 4^d)]. Substituting b=pi/16 in d=2 gives 2 log[z pi^2/(2048e)]; b=pi/48 in d=3 gives 4 log[z pi^2/(36864e)]. Using pi>3,e<3 yields q<=4/9 at z=4096 and q<=729/16384 at z=65536. A copied audit will also be rerun here, so none of its output paths can touch the old folder.

## 4. Choice of one extension, before proof

Test the geometric implication requested by round 4 by constructing a robust planar interface between two fixed non-equivalent triangular orientations. Retain a slightly dilated triangular lattice in each of two half-planes separated by a bounded strip. Allow independent lattice phases and arbitrary particle displacements in small open balls. Prove a uniform lower count in every axis-parallel square, not merely a finite sampled grid.

The target is a counterexample to the implication that such an interface must create underoccupied boxes for the explicit ell=4,r=2 detector. More generally obtain a parameter-dependent count showing why any fixed density threshold below the bulk density can miss a bounded-width seam once the box scale is large. This is a geometric obstruction, not a counterexample to a Gibbs ordering theorem. The previous Gibbs estimate itself remains valid.

Preliminary exact-arithmetic check, run under the single-thread/nice wrapper: s=g=101/100, delta=1/400; s-2delta=g-2delta=201/200>1. Bounds 303/175<sqrt(3)<26/15 follow by squaring. Thus R=s/sqrt(3)<7/12 and rho_s=2/(sqrt(3)s^2)>150000/132613. The proposed four-square count lower bound is greater than

    (150000/132613)(1697/600)(391/600)
      =3317635/1591356
      =2+134923/1591356 >2.

The independent integer-product comparison has positive numerator 4,047,690,000 before fraction reduction. This establishes room for a displacement-robust count of at least three, pending the geometric counting proof.

## 5. Round-4 copied audit rerun

Command: single-thread environment and `nice -n 15 python3` wrapper, then `python3 prior_recheck/verify.py` inheriting nice 20. The copied source is byte-for-byte unchanged. Exit code 0. Complete output:

```text
Finite audits of integrated low-occupation and connected-set bounds.
nice_priority=20; thread_environment=1; CPU_limit_seconds=60
periodic_slots d=2: ell=100, rho=1/4, m_0=4225, r=2500, limiting_slot_density=4/9
periodic_slots d=3: ell=100, rho=1/4, m_0=274625, r=250000, limiting_slot_density=8/27
tilt_cases=150; all_finite_sums_below_exponent=PASS; independent_Poisson_derivation=PASS
weighted_graphs=512; exact_low_count_ratio_cases=3072; negative_controls=PASS
animals d=2: counts=[1, 4, 18, 76, 315]; independent_closed_walk_match=PASS
animals d=3: counts=[1, 6, 45, 344]; independent_closed_walk_match=PASS
d=2, z=4096: tau=3.97018440697, tau_lower=3.96521390452, q=0.301919249014
d=2, z=10000: tau=5.75239897971, tau_lower=5.75036231503, q=0.0508024723399
d=2, z=1000000: tau=14.9607230588, tau_lower=14.960702687, q=5.09050083408e-06
exact sufficient threshold d=2: z>=4096, exp(-tau)<=1/36, q<=4/9
d=3, z=10000: tau=-0.0485486301527, tau_lower=-0.0607624015223, q=37.7908711167
d=3, z=65536: tau=7.46116054602, tau_lower=7.45929566641, q=0.0206995854069
d=3, z=1000000: tau=18.3600405725, tau_lower=18.3599183424, q=3.82505947785e-07
exact sufficient threshold d=3: z>=65536, exp(-tau)<=81/65536, q<=729/16384
PASS; elapsed_seconds=0.431; peak_rss_mib=17.703
Wrote animal_counts.csv, contour_bounds.csv, verification.json
```

## 6. Proof and audit implementation

Wrote PROOF.md. A triangular lattice has Voronoi cells of area sqrt(3)s^2/2 and circumradius R=s/sqrt(3). Sites in a rectangle cover its R-erosion by their cells, giving a count lower bound rho_s(w-2R)_+(h-2R)_+. Applying this on the two sides of the strip, inside the delta-eroded square, yields

    N_X(Q) >= rho_s(ell-2delta-2R)_+(ell-2delta-g-4R)_+.

The explicit exact bound in Section 4 is >2, hence the count is at least three everywhere. The statement is uniform over phases, angles, all square translations and all radius-delta displacements. A general threshold rho<rho_s is missed at every side ell>(4delta+g+6R)/(1-rho/rho_s). The proof includes positive finite displacement-sector volume and an explicit reason the independent-jitter law is not Gibbs.

Wrote verify.py with a separate exact expansion in Q(sqrt(3)), exact cell vertex and shoelace computations, exact sampled lattice counts at orientations zero and pi/6, split-width cases, large-scale sufficient constants, and negative controls for omitting the strip width or erosion. Floating-point simultaneous-jitter checks are supporting checks only. A manuscript formatting typo was found by reading the saved opening lines and corrected before the audit. One attempted log patch had no matching context and made no change.

## 7. New audit run

Command (the runner captures both streams and appends the complete result here):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py > VERIFY_OUTPUT.txt 2>&1
```

Exit code 0. Complete captured script output:

```text
nice_priority=20; thread_environment=1; CPU_limit_seconds=60
exact_rational_count_floor=3317635/1591356=2+134923/1591356; required_count>=3
independent_Qsqrt3_bound=['-4390/303', '1757441/183618']; decimal_for_orientation=2.08932187097; exact_comparison_to_2=PASS
cell_vertices=6; exact_shoelace_area=sqrt(3)*s^2/2; vector_checks=720; PASS
exact_phase_and_square_cases=560; minimum_certified_safe_sites_in_sample=8; witness=[0, 1, '-2', '-7/4']
exact_split_width_cases=35; wide_strip_and_missing_erosion_negative_controls=PASS
conservative_large_box_examples=[{'threshold': '1/8', 'sufficient_integer_side': 6}, {'threshold': '1/2', 'sufficient_integer_side': 9}, {'threshold': '1', 'sufficient_integer_side': 39}, {'threshold': '11/10', 'sufficient_integer_side': 165}]
jitter_trials=3; seed=5080; smallest_sampled_separation=1.00577809998; floating_point_support_only
PASS; elapsed_seconds=1.862; peak_rss_mib=16.891
```

## 8. Attempts to break the result and independent checks

The audit passed on its first mathematical run. It took 1.862 seconds and peaked at 16.891 MiB RSS, at actual nice 20. The previous copied audit passed in 0.431 seconds at 17.703 MiB RSS. Both are far below the resource limits.

The exact four-square bound was checked by two different calculations. The factor-by-factor rational bound is 3317635/1591356>2. Expanding the original expression in Q(sqrt(3)), without replacing either the density or the radius, gives

    -4390/303 + (1757441/183618)sqrt(3).

Its numerical value is 2.08932187097, but the comparison to two is exact: b>0, 2-a>0, and 3b^2-(2-a)^2=33193389889/11238523308 >0. The exact Q(sqrt(3)) calculation also verifies that this original expression exceeds the rational lower bound. Thus no floating-point rounding supports the count of three.

The cell geometry was rechecked by an exact shoelace calculation of its six vertices and 720 comparisons with lattice-vector bisectors; each vertex has squared radius s^2/3. A separate exact enumeration of 560 phase/square combinations gives a minimum of eight retained sites already in the delta-eroded square. This sampled minimum is not claimed globally; the global conclusion is the proven lower bound of three. The finite enumeration includes squares on either side, off-center crossings and centered crossings, four independent phases per side, and a certified lattice-index cutoff. The analytic proof covers all phases and squares, not just the sampled list.

Omitting erosion would be a real error: a site at x=1/1000 can leave a square face after displacement -1/500, whose magnitude is below delta. The audit detects this shortcut. Omitting the strip width would also be false when a square fits inside a much wider empty strip; the negative control gives a zero bound in that case. Thirty-five exact width-splitting checks include rectangles of zero width and squares lying wholly to one side. The proof explicitly treats these cases with positive parts.

Arbitrary relative phases do not threaten exclusion: cross-side separation is bounded below by the horizontal gap, independent of lattice commensurability. Arbitrary simultaneous displacements do not threaten exclusion because both s-2delta and g-2delta are 201/200. Three sampled independent-jitter trials support this calculation, with smallest distance 1.00577809998; the proof uses the deterministic bounds, not the sampled value.

The general scale bound was expanded independently as rho_s[ell^2-(a_0+b_0)ell+a_0b_0]. Conservative rational constants give sufficient integer side lengths 6,9,39,165 for thresholds 1/8,1/2,1,11/10, respectively. These are sufficient scales for this construction, not sharp scales, and do not claim failure of every detector at every preassigned scale.

A bounded strip still removes O(length) particles. No claim says its free-energy cost is zero. In particular the round-3 vacant-seam estimate requires width at least 2(1+a)>2 for protected balls, while the certified center-free strip here has width 201/200. There is no contradiction. The round-4 Gibbs estimates remain valid; their events simply do not occur in this geometric example. Positive finite displacement-sector volume does not make a packing law Gibbs: the independent-jitter law forces one particle in a fixed displacement ball, contradicting the strictly positive DLR vacancy probability at finite activity. This supplies a direct scope check without relying on exact-contact singularities.

No novelty claim is established. Stronger local geometric detectors or a threshold coupled to a much finer scale are not excluded. No Euclidean freezing theorem, orientational order, translational symmetry breaking or Gibbs surface tension is proved.

## 9. Report and final artifact audit

Wrote REPORT.md with the required PARTIAL verdict, the uniform geometric counterexample, the parameter-dependent general count, reproduction commands, exact and sampled distinctions, failures, limitations, opened references and the next local-orientation test. Wrote a read-only artifact audit.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_artifacts.py > ARTIFACT_AUDIT.txt 2>&1
```

Exit code 0. Complete output:

```text
PASS: unchanged previous source; complete logged outputs; exact count constants; sampled/global distinction; resource records; report and proof scope agree.
```

Only this folder was written. Earlier sources remain read only. No git, subagents, external messages, accounts, GPU work, ML libraries or background processes were used. Completed the selected geometric test; T080 remains open.
