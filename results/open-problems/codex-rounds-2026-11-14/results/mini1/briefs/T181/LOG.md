# T181 work log

Task received: 14 November 2026, approximately 21:19 Asia/Tbilisi (session start).
Task: “push this problem forward by one checkable piece.”

## 21:21 — scope and choice, before implementation

Work is confined to this folder. No git, external writes, subagents, or background workers. The task-specific restriction against writing elsewhere takes precedence over the earlier global instructions to update the mesh, checklist, and memory; these services were not mutated. Read the brain navigation/startup index and compute governor state. The latter reports `status=warn`, `mode=owner_away_open`, CPU saturation; this work will use one small, low-priority process at a time.

Chosen piece: an exact, reproducible finite-generation computation of Fav(K_n), initially n=0,...,4, extending to n=5 if inexpensive. Normalize Fav(E)=(1/pi) integral_0^pi |proj_theta E| dtheta. Partition slopes t in [0,1] at every rational crossing of projected square endpoints. Between crossings the unnormalized union length is A+B*t with integer coefficients. Integrate this affine expression exactly against (1+t^2)^(-3/2), then certify numerical enclosures using integer square roots and rational bounds for pi. Save the full piecewise affine functions and radical expressions, not just decimals.

Why this piece: it settles finite cases without missing narrow exceptional direction intervals, provides exact data against which later algorithms can be tested, and gives a finite algebraic reduction valid for every n. It does not identify an asymptotic exponent. No novelty claim is made for the general arrangement method or for small-generation values.

Planned independent audit: regenerate square coordinates from binary words; regenerate crossing slopes from all pairs of endpoints at the smaller generations; compare the adjacent-gap formula with an endpoint-occupancy sweep on every slope cell; check event slopes themselves and the horizontal, diagonal, and slope-1/2 directions; compare exact integration with direct numerical angular integration. Include n=0 and a hand-derived n=1 formula as normalization controls.

## Literature search begun at 21:20 (limit: ten minutes)

Web searches: `Favard length four corner Cantor Marshall 2026 exact decay rate`; `arxiv 2509.02882 Favard Marshall`; `arxiv 2609.33557 Favard`; `"Favard" "2026" "deterministic" "four"`; `"Favard" "four-corner" "exact" "2026"`.

Opened primary sources so far:

- Caleb Marshall, *Improved Power Laws for the Favard Length Problem in All Dimensions*, arXiv:2509.02882v2, revised 12 August 2026. https://arxiv.org/html/2509.02882v2 . Corollary 8.2 gives the four-corner bound N^(-1/5+u), u>0, already in the brief.
- Alan Chang, Damian Dąbrowski, Giacomo Del Nin, *Favard length of non-homogeneous random disc-like Cantor sets*, arXiv:2609.33557. https://arxiv.org/abs/2609.33557 . Concerns random variants.
- Alan Chang, Pablo Shmerkin, Ville Suomala, *Sharp Favard Length of Random Cantor Sets*, Geometric and Functional Analysis 36 (2026), 786–830. https://doi.org/10.1007/s00039-026-00743-3 . The introduction distinguishes random exact rates from the deterministic four-corner problem.
- Caleb Marshall, *Nearly Sharp Uniform Projection Bounds and Superlinear Vitushkin Inequalities for Deterministic Self-Similar Sets*, arXiv:2610.22908. https://arxiv.org/html/2610.22908v1 . Constructs other deterministic systems with rotations, depending on a prescribed exponent; this does not settle the fixed four-corner set.
- Damian Dąbrowski, *Survey on Favard length and rectifiability*, arXiv:2610.35502. https://arxiv.org/html/2610.35502v1 . Section 2.5 being checked.

A web result also led to https://github.com/CoolRmal/FavardLength claiming a formalized exponent 156307/625000 > 1/4. Opened its README, which says its underlying manuscripts have not been externally refereed. This is a claim requiring audit, not an established paper or an exact-rate solution. Will record it separately from verified literature.

## Literature search concluded (under ten minutes)

Dąbrowski's 26 October survey, Section 2.5, Problem 2.33 and equations (2.16), (2.20), explicitly still asks for the exact rate and gives the 1/5-epsilon upper exponent and log(n)/n lower bound. No complete solution was found. Marshall's October construction concerns different rotating systems. The repository claim above, even if correct, would only narrow the exponent gap; its kernel checks and analytic bridge were not independently run here. No SOLVED_ELSEWHERE.md declaring a solution is warranted.

## Implementation and first run

Created `exact_favard.py`, a standard-library script using exact integers and fractions for the arrangement and certified radical bounds. It also performs an independent endpoint sweep and direct angular quadrature.

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 exact_favard.py --max-n 5 > run_output.txt 2>&1`.

The first run exited with an error; its output is being inspected before retrying. No result is claimed from that run.

Failure identified: Python's 4,300-digit integer-to-string guard rejected the unreduced-size certificate for n=3. Arithmetic had succeeded, but summing many unrelated rational radical bounds caused very large denominators. Changed `radical_bounds` to round each term outward onto the common grid 10^(-55). This is rigorous interval arithmetic and keeps numerator/denominator sizes small. The proof will include the rounding rule. Preserved the failed run in `first_run_output.txt` and reran the same command.

The launcher emits `nice: setpriority: Operation not permitted`: on this Mac the process inherits an already-low priority, and adding 15 exceeds the available range. Added an explicit `os.getpriority` check requiring actual nice >= 15 before computation, plus a check that OMP_NUM_THREADS=1. The command still invokes `nice -n 15`; the measured priority, rather than the launcher's warning, determines compliance.

## Successful exact computation

The rerun passed. Exact stdout is in `run_output.txt`; data and certificates are in `data/`.

```text
priority=20 OMP_NUM_THREADS=1 single_thread=standard_library
n=0 squares=1 candidate_cells=1 affine_pieces=1 radical_terms=1 Fav=[1.27323954473516, 1.27323954473517] quadrature_error=4.88e-10 seconds=0.006
n=1 squares=4 candidate_cells=2 affine_pieces=2 radical_terms=3 Fav=[1.04990339003727, 1.04990339003728] quadrature_error=4.07e-10 seconds=0.01
n=2 squares=16 candidate_cells=21 affine_pieces=11 radical_terms=12 Fav=[0.92793731495768, 0.92793731495769] quadrature_error=5.35e-10 seconds=0.027
n=3 squares=64 candidate_cells=204 affine_pieces=73 radical_terms=73 Fav=[0.84365831229531, 0.84365831229532] quadrature_error=2.11e-08 seconds=0.12
n=4 squares=256 candidate_cells=1919 affine_pieces=525 radical_terms=509 Fav=[0.77883017302463, 0.77883017302464] quadrature_error=1.42e-07 seconds=1.031
n=5 squares=1024 candidate_cells=17863 affine_pieces=3858 radical_terms=3750 Fav=[0.72637720829722, 0.72637720829723] quadrature_error=8.39e-07 seconds=22.303
PASS elapsed_seconds=23.504 peak_rss_bytes=27852800
```

For every candidate cell, two distinct rational interior slopes were checked by both the adjacent-gap formula and an endpoint-occupancy sweep. Every candidate crossing, including simultaneous ties, was checked against both neighboring affine formulas. All endpoint-pair crossings were independently enumerated for n<=4. Coordinates were regenerated from binary words at every n. Horizontal, diagonal and slope-1/2 lengths were checked against closed formulas. The 8,192-angle midpoint check is a floating-point cross-check, not the certificate.

Next audit: independently integrate the saved CSV functions by parts, using slope jumps and direct square-root intervals; use pi=4*(arctan(1/2)+arctan(1/3)) instead of the generator's Machin identity.

The first independent audit failed immediately at the n=0 normalization control. Its integration-by-parts endpoint term was missing `-B_last/sqrt(2)`. Re-derived the identity from `[L*t/sqrt(1+t^2)]_0^1 - integral L'*t/sqrt(1+t^2) dt`; the correct endpoint contribution is `(A_last-B_last)/sqrt(2)`. Corrected the independent verifier, preserving the failure in `audit_first_run_output.txt`. The original primitive formula and its computed certificates were unaffected. This is why n=0 is included even though the problem starts at positive n.

## Independent audit passed

Command: `OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 audit_favard.py > audit_output.txt 2>&1`.

```text
n=0 merge_checks=1 independent_integral=PASS decimal_enclosure=PASS width_lt_1e-50=PASS
n=1 merge_checks=2 independent_integral=PASS decimal_enclosure=PASS width_lt_1e-50=PASS
n=2 merge_checks=11 independent_integral=PASS decimal_enclosure=PASS width_lt_1e-50=PASS
n=3 merge_checks=73 independent_integral=PASS decimal_enclosure=PASS width_lt_1e-50=PASS
n=4 merge_checks=525 independent_integral=PASS decimal_enclosure=PASS width_lt_1e-50=PASS
n=5 merge_checks=3858 independent_integral=PASS decimal_enclosure=PASS width_lt_1e-50=PASS
PASS elapsed_seconds=0.788 peak_rss_bytes=21790720
```

The launch warning about `nice` is the same inherited-priority issue described above. The verifier checks actual nice >= 15 before running.

Wrote `PROOF.md` with the coordinate model, symmetry factor, complete crossing enumeration, adjacent-gap formula, primitive and slope-jump integration formulas, interval arithmetic, exceptional-direction controls, and hand calculation for n=1. The second audit supplies strictly interior rational enclosures for all six displayed decimal intervals. Saved CSVs contain 4,470 merged pieces in total. No asymptotic exponent is fitted or claimed.

## Final artifact audit

Added the full 11-piece n=2 slope table and a simplified exact expression for 4*pi*Fav(K_2) to `PROOF.md`. Extended the independent auditor to check its coefficients exactly, then reran the audit command above. It exited 0 and printed `n=2 printed_closed_form=PASS`, followed by successful independent integral and decimal-enclosure checks for all n=0,...,5. The final output is in `audit_output.txt`; its final line is `PASS elapsed_seconds=0.750 peak_rss_bytes=21069824`.

Wrote `LITERATURE.md` and `REPORT.md`. Checked the report's required first-line verdict, normalization, commands, resource bounds, and explicit statement that the asymptotic rate has not been determined. The n=2 expression has 11 terms (one rational and ten radicals); the report uses “11-term expression.” All created artifacts are inside this folder. No git, network publication, outside-file mutation, or subagent was used.
