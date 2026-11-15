# T087 working log

Task received: 14 November 2026, about 20:54 Asia/Tbilisi. Task: “push this problem forward by one checkable piece.” All deliverables remain in this directory. No git, external posting, subagents, or simulation.

## 20:54–20:56 — orientation and first literature pass

Read the local startup memory and compute state. The state was `ok`, `owner_away_open`. A startup recall invoked with `OMP_NUM_THREADS=1 nice -n 15 python3 ... brain.py recall ...` completed, but `nice` reported `Operation not permitted`. No further Python or numerical computation will be used; this session's piece will be a proof. Shared checklist/mesh/brain writes are omitted because this task explicitly prohibits writes outside this folder. The recall itself reported an attempted index refresh; no further brain tools will be invoked.

Initial folder listing: PROMPT.md, codex.log, run.pid. Read commands also included `cat ...compute_state.json`, `cat ...startup_consult_the_brain_2026_07_07.md`, and `date '+%Y-%m-%d %H:%M:%S %Z'` (output: `2026-11-14 20:55:23 +04`). `ps` was denied by the sandbox.

Web queries: `three dimensional percolation critical exponents existence 2025 2026 rigorous`; `percolation hyperscaling three dimensions critical two point one arm 2025 2026`.

Opened arXiv pages (not just search snippets):

- Tom Hutchcroft, *Dimension dependence of critical phenomena in long-range percolation*, arXiv:2510.03951, submitted 4 October 2025, ICM 2026 contribution: https://arxiv.org/abs/2510.03951 . Full text still to inspect.
- M. Cabezas, D. Croydon, A. Fribergh, N. Kawamoto, *Range convergence and sharp one-arm asymptotics for the critical percolation cluster in high dimensions*, arXiv:2607.24561: https://arxiv.org/abs/2607.24561 . Abstract states sharp one-arm asymptotics in the high-dimensional regime, not dimension three.
- Caio Alves, Rangel Baldasso, Carlos Gustavo Moreira, Augusto Teixeira, *Percolation on hierarchical lattices*, arXiv:2606.11503: https://arxiv.org/abs/2606.11503 . Abstract establishes several exponents on hierarchical graphs, not on the cubic lattice.

No whole-problem solution identified. Literature search remains within the ten-minute limit.

## Choice, written before proving it

Prove a finite-scale inequality relating the one-arm probability, the truncated critical susceptibility, and the expected number of clusters crossing a cubical annulus. Deduce that, if the one-arm exponent exists and crossing-cluster multiplicity has subpolynomial expectation, the spatially averaged two-point exponent exists and satisfies the critical hyperscaling identity. Also quantify how any defect in this identity forces polynomially many crossing clusters.

Reason: this is a concrete reduction of one part of T087 to an explicit geometric estimate. It avoids assuming all exponents exist and makes the missing hypothesis measurable. It will not prove exponent existence on Z^3 or near-critical matching. The general geometric approach to hyperscaling is classical; no novelty claim will be made.

## 20:56 — scope check and sharpened target

Opened the full HTML of Hutchcroft's survey and Michael Aizenman's *On the Number of Incipient Spanning Clusters*, arXiv:cond-mat/9609240v4 (https://arxiv.org/html/cond-mat/9609240v4). The survey describes d=3,4,5 results as conditional. Aizenman's introduction already emphasizes subpolynomial multiplicity as the geometric hyperscaling mechanism. This confirms the approach is classical, not a newly discovered solution.

A targeted continuity search surfaced September 2026 AI/formalization claims. Attempts to open the OpenAI GitHub directory failed (cache miss), and its raw PDF was rejected by the web tool as `application/octet-stream`. These are not verified theorems in this log; primary-source access is being retried. Even if continuity is correct, it does not establish the exponents in T087.

The mathematical target can be sharpened: under subpolynomial expected crossing-cluster count, prove equivalence between existence of a nondegenerate one-arm exponent a in (0,d/2) and existence of the truncated susceptibility growth exponent s in (0,d), with s=d−2a. For the reverse direction, subtract the susceptibility at a smaller power scale before applying the separated-arm bound. This avoids assuming a pointwise two-point exponent exists.

## 20:59 — literature pass closed; proof saved

The literature search took less than ten minutes (started about 20:54). Opened the primary Microsoft-hosted PDF of C. Borgs, J. T. Chayes, H. Kesten and J. Spencer, *Uniform Boundedness of Critical Crossing Probabilities Implies Hyperscaling*, MSR-TR-98-26: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-26.pdf . Read the introduction and theorem statements 3.2–3.4. Their definition of exponent existence includes a stronger scale-ratio regularity condition than a mere logarithmic limit. The present proof uses logarithmic limits only, an expected annulus-component count, and an averaged two-point quantity. This distinction is a reason to state the reduction precisely, not a claim that it improves their theorem in its full scope.

Primary-source metadata for the OpenAI September 2026 continuity manuscript was accessible at https://raw.githubusercontent.com/openai/math/main/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/README.md . Its author is `OpenAI`; no arXiv identifier appears there. The PDF content remained inaccessible in the web reader despite raw, GitHub blob, and display-link attempts. The repository's own README describes a collection at mixed verification stages. No continuity claim from that manuscript is used in the proof or certified by this session.

Saved PROOF.md with:

- Exact finite-scale bound X(2n) ≥ (2n+1)^d π(3n)^2 / E K_n.
- Independent-endpoint-arm upper bounds for X and its outer shells.
- Under subpolynomial E K_n, equivalence of π(n)=n^(−a+o(1)), 0<a<d/2, and X(n)=n^(s+o(1)), 0<s<d, with s=d−2a.
- Defect bound E K_n ≥ n^(b−2a+o(1)) when a pointwise two-point exponent b exists in (0,d).

No numerical computation or estimated percolation data underlies these statements. The proof uses only translation invariance, independence on disjoint finite edge sets, monotonicity, two Cauchy–Schwarz inequalities, and sums of powers.

## 21:02 — audit and final strengthening saved

Added Corollary 4: the same hypotheses give existence of the supremum two-point exponent, M(n)=sup_{||x||≥n} τ(x)=n^(−2a+o(1)). This still does not give a lower bound at every prescribed x.

Saved AUDIT.md. Independently recovered the volume/count factor in (1) by introducing the component-count-biased probability measure and expanding a nonnegative variance. Counted the three-dimensional shell twice: difference of cubes and a disjoint face/edge partition both give 24r^2+2; at r=1 both give 26. Re-derived the hyperscaling defect as both d−2a−s and b−2a. Hypothetical mean-field inputs a=2, s=2 give d−6 by both routes, consistent with the high-dimensional obstruction.

Checked the cases most likely to invalidate the reduction: local versus whole-lattice clusters, boundary wiring, possible path escape, dependence of count and mass, rare large counts, the excluded zero-growth endpoint, all integer scales rather than a subsequence, and pointwise versus averaged decay. A potentially invalid step—inferring uniform scale-ratio regularity from a logarithmic exponent—was explicitly avoided by subtracting at a fixed power scale before taking that power to one. The proof does not rely on continuity at criticality.

All file creation and edits used the patch tool inside this folder. There is no computation command/output or numerical dataset to reproduce: this deliverable is a proof. The exact inequalities and their derivations are in PROOF.md; the independent checks are in AUDIT.md.

## 21:03 — final reread and correction

Command: `sed -n '1,310p' PROOF.md`. Output: the complete saved proof, reread for agreement with the claims in REPORT.md. A boundary-definition overstatement was found in the audit: full-lattice clusters do not invalidate the lower bound if the masses are regrouped consistently, although they change the observable and lose finite-volume measurability. Removed the assertion that the local definition was mathematically essential. Boundary wiring really does invalidate the connected-pair estimate, and remains excluded. The main inequalities, exponent transfer, and verdict are unchanged.

Saved REPORT.md and SOLVED_ELSEWHERE.md. The final verdict is PARTIAL: a conditional reduction, not exponent existence or an exponent value for three-dimensional percolation.

Final check: `sed -n '1,110p' REPORT.md` printed the complete report. Confirmed its first line has the required `VERDICT: PARTIAL` form and its claims retain the expected-count, exponent-range, and pointwise-decay qualifications from PROOF.md.
