# Round 6 vetting (an agent)

Round 6 runs on Mac mini 1 from 15 Nov 2026: 67 continuation briefs, one per round 5 brief whose REPORT.md says PARTIAL,
PROVED or COMPUTED, each asked to take the next checkable step; acc2, normal speed, made by `../make_r6.sh`. Each brief
dir here holds the worker's REPORT.md, PROOF.md, LOG.md and scripts; the raw codex.log stays on the Mac. Only briefs
whose `run.exit` exists are pulled.

How each report was read: the VERDICT line, whether the report says the round 5 result it builds on still holds, and
every line that mentions a counterexample, a false statement, an error or a failure. In this pull every such line is a
deliberate negative control (a dropped hypothesis that breaks the statement), a bug in the worker's own checker that it
fixed, or a stronger claim the worker tried and found false (T080: a face-connected separator; the eight-neighbour
statement it proves instead stands). No report says a round 5 result is wrong. A PROVED verdict below is a lemma or
special case unless the row says otherwise; no brief in this pull closes its top-200 row.

## First pull (15 Nov 2026, 10:53 mini time; 32 of 67 complete, all exit 0)

| brief | verdict as written by the worker |
|---|---|
| AV_T010 | PARTIAL conditional jitter-success estimate verified on regular zero-jitter boundary and common-shift data |
| AV_T030 | PROVED the bordered-form-to-Hilbert-multiplier implication and infinite-coordinate energy identity, conditional on the stated vector variational inputs |
| AV_T032 | PARTIAL verified the conditional density and exponential moments in Section 8's Skeleton encounters lemma |
| AV_T050 | PROVED the local-envelope lemma under the stated calibration and anchor-comparison hypotheses, including simultaneous physical-competitor bounds in a prescribed finite subgraph |
| AV_T054 | PROVED relative QUE for prescribed k-sets when k/(L^2 log N) tends to infinity, under all-eigenvector delocalization and label symmetry, without simple spectrum |
| AV_T083 | PROVED the ordinary selected-array Bessel bound under the source's bounded-height frequency, per-scale separation and smooth cancellation hypotheses |
| AV_T095 | PARTIAL BK and repeated-event itinerary reduction verified under the preceding rare-event and extraction inputs |
| AV_T132 | PARTIAL zero-cost local-certificate transfer under the retained raw-array and fixed-background hypotheses |
| AV_T136 | PROVED finite-depth signed compression identity E5, including shared cut blocks and repeated terminal labels. |
| AV_T137 | PARTIAL Bounded-insertion expansion, pattern replacement and Poisson-root transfer checked; regular-overlap concentration remains unaudited |
| AV_T176 | PARTIAL tagged-flow identity independently proved and checked; complete mixing proof not certified |
| AV_T304 | PROVED one-power h0 improvement in Lemma 6.3's exact-value quadrature error, conditional on the stated transported-jet and exact-flow inputs |
| T049 | PARTIAL a stronger local connectivity bound using both endpoint neighborhoods |
| T050 | PARTIAL proved phase-mesh-uniform two-wall link bounds and column independence |
| T053 | PROVED invariant collision map and exact suspension and velocity-correlation representations at fixed density |
| T056 | PROVED sharp m-2 coefficient-sensitive planar matching bound |
| T058 | PARTIAL proved that a deterministic correction transfers the joint Gaussian packing limit to every fixed interior phase band |
| T060 | PARTIAL any distinct pure ground state remains perfectly distinguishable in one fixed half-chain direction, conditional on the published spin-1 gap premise |
| T063 | PROVED local reconstruction and a perimeter free-energy bound for the all-level geometric-residual fold |
| T064 | PROVED quantitative annular arm stability at the height of a determinant-weighted saddle |
| T068 | PROVED sharper clique barrier with polynomial deletion disagreements and bounded exceptional queries |
| T071 | PARTIAL exact rank-occupation formula for the filtered descendant kernel |
| T073 | PARTIAL improved high-noise uniqueness by allowing every common-diagonal broadcast pattern |
| T075 | PARTIAL proved explicit parameter stability of prefix caps and delayed finite concentration at transcendental parameters; T075 remains open |
| T076 | PARTIAL sharp square-function bound under restricted transfer between diffusion scales |
| T078 | PROVED uniform sparse injection energy bound with isolated removed sites |
| T080 | PARTIAL local bond-direction defects separate arbitrarily filled strips between two fixed orientations |
| T081 | PARTIAL fixed-background contour expansion and exact finite-domain interaction verified |
| T087 | PARTIAL conditional almost sure largest-cluster exponent and all positive moment exponents |
| T089 | PARTIAL nine-moment GOE certificate from exact Vandermonde integration |
| T090 | PROVED second logarithmic weak-coupling correction for the Gaussian second-moment rate |
| T092 | PROVED an O(N^-1) summed coefficient-array bound for fixed smooth passage packets |

## Second pull, 15 Nov 2026 (24 more briefs, 56 of 67 exited, all exit 0)

Verdicts as each REPORT.md states them. PROVED: T105 (almost-everywhere flat-torus gap limsup bound above 2.021),
T122 (depth-uniform zero-temperature reformulation of the regular hierarchical upper bound), T133 (C2 simple closed
strictly convex completion at Delta = 1/sqrt(2), all weight ratios), T179 (running-path-supremum linear-growth drift
extension, conditional on the earlier drift-free input), T248 (TW1 with deterministic finite-size centering for the
projected spherical kernel, any fixed polynomial activation of Hermite rank a), T264 (antipodal four-point
minimum-norm ReLU interpolation has bounded positive collision-limit risk). COMPUTED: T102 (49 two-interface
measurements). PARTIAL: T097, T098, T101, T116, T127, T160, T185, T200, T221, T222, T224, T225, T226, T227, T245, T247,
T267. None of these closes its top-200 row; the PROVED lines are the stated sub-results only.

Fault scan: AUDIT.md exists for 9 of the 24; every line matching fail/counterexample/incorrect in them is a negative
control or a stated limit (T097 sign test, T185 failure-indicator bound not used, T222 no counterexample found, T225
omitted-term check). The other 15 carry their checks inside REPORT.md and PROOF.md, not a separate audit file, so their
verdicts rest on the worker's own checks and are unreviewed here.

T248 cites arXiv:2610.41416 as an input "used as stated". The record exists: G. Chen and X. Lyu, "Tracy-Widom law for
sample covariance matrices under quadratic form concentration", posted 30 Oct 2026 (arXiv API, read 15 Nov). Whether its
hypotheses match the projected spherical kernel case is not checked yet; that is the gap before T248 can be written up.
Closed 15 Nov: the hypotheses were checked (T248/CHECK_CHEN_LYU.md), and the paper is posted. It is the public repo
row-centered-conjugate-kernel-tracy-widom v1.0 and Zenodo 10.5281/zenodo.24246777 (T248/POSTED.md). The finite-N
excess seen in Monte Carlo is the weight-side edge shift of the paper's Remark 7.1. Next candidate for a write-up: T264.

T200 (listed PARTIAL above) was written up and posted 15 Nov. It does not settle the exact 3-D intersection exponent;
it sharpens R. Liu's explicit bound (arXiv:2609.18643, xi_3(1,1) < 0.9999) to xi_3(1,1) <= 1 - 9000/(2361557 log(17/5))
< 0.99689, a margin 31 times his, so the 3-D loop-erased walk growth exponent and the cut-point dimension are >= 1.0031.
Public repo brownian-intersection-exponent-bound v1.0 (90f6bd3d), Zenodo 10.5281/zenodo.24247997, check script
check_constants.py at sixty digits ends ALL PASS (T200/POSTED.md). Next candidate for a write-up: T264.
