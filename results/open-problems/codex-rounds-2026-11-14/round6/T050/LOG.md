# T050 work log, round 6

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded clock: 2026-11-15 06:08:11 UTC / 10:08:11 Asia/Tbilisi.

## Orientation and bounded literature update

Read startup memory, MEMORY.md, and the compute governor state (status ok,
mode owner_away_open). This task's folder-only restriction takes precedence
over shared brain, checklist, and mesh mutations; none are made. No git or
subagents. All shell programs are invoked with `env OMP_NUM_THREADS=1 nice
-n 15`. The sandbox prints `nice: setpriority: Operation not permitted`;
reads still exit 0. No heavy computation is planned or claimed.

Enumerated all four prior T050 folders using `rg --files`. They contain no
research scripts. The original folder has no PROOF.md. Read the original
REPORT.md, LOG.md, SOLVED_ELSEWHERE.md, and rounds 3–5 REPORT.md, LOG.md,
PROOF.md. Some aggregate output was truncated; bounded rereads are recorded
below as needed. Prior folders remain read-only.

Web queries (four queries in two calls):

* `"first passage percolation" "strict convexity" 2026`
* `"Strict convexity and differentiability" "September" exponential`
* `"strict convexity" "first-passage" correction November 2026`
* `"first-passage" "continuous" "strict convexity" 2026 proof`

Opened the manuscript landing page and formalization scope note:

https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/

https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/212.md

The same September 2026 planar exponential claim remains. The scope note
excludes strict convexity from its selected formalization. No verified
solution of the full continuous-law, all-dimensions problem was found.
The literature update is closed here, within five minutes of starting.
Further manuscript reads concern the mathematical audit, not an extended
literature search. A direct PDF open failed; clicking Open PDF on the
landing page succeeded (95 pages).

Source: OpenAI, *Strict convexity and differentiability of the planar
exponential first-passage limit shape*, September 24, 2026. No arXiv id
verified. PDF URL is the landing-page URL followed by `main.pdf`.

## Independent recheck of round 5

Write h=g-P and theta=t-i. On a period, h-h_i=F-theta C,
where F is nondecreasing from 0 to D and C=D-e. Thus variation is at
most D+|C| <= 2D+|e|. Joining two occurrences through their starting
anchors and the comparison tree uses each relevant period/tree edge at
most once, so every h difference is bounded by

    B = sum_periods(D+|C|) + sum_tree |e|.

Consequently E B <= Lambda = 2 sum E D + sum_period E|e| + sum_tree E|e|.
The local road envelope A=sum|C| and common-point gauge envelope S
both obey max(A,S)<=B. A concatenation with r switches has r+1 legs
and r gauge jumps, giving (2r+1)B. A physical competitor has one
endpoint h difference and two corrected arms, giving 3B. Therefore
the round-5 bounds hold with Lambda <= [2p+c(p+q)] beta.

Second check: h=(1-theta)h_i+theta h_(i+1)+F-theta D verifies the
sign C=D-e. Tree differences are exactly increments of h. Neither
step bounds the absolute additive offset of P. Local measurability
uses only observable records and finite-graph distances, as in the
prior proof. No mistake found under its explicit fixed-window hypotheses.

Next: inspect the actual phase constructions before choosing one extension.

## One chosen extension, before its proof

Prove a phase-uniform local link-field lemma: the negative first moment of
one two-wall link, the input support of that link, and independence of
sufficiently separated entire columns. This is the concrete next use of
round 5, rather than a new contraction argument. It tests whether averaging
over offset meshes or conditioning on wall phases changes the constants.
The physical windows will be kept identical across all offset meshes.

Source reads by web-tool PDF open/find: Sections 10.1–10.3, Remark 10.7,
Section 11, Section 14.1, and Sections 15.1–15.2, 15.6–15.7. They identify
the actual operations: deterministic averaging of gauges on the same
physical anchors, independent wall phases, and a link minimum over physical
crossings between two walls. These reads are for the audit. Only this
link-field lemma will be claimed; no conclusion about the full output road
or the contraction follows from it.

Proposed explicit bookkeeping, to be proved and stress-tested:

* For s<1/10 and r=s/1000, an endpoint in a band of half-width s/50
  is on a wall with nominal height within delta=s/50+2r of the row.
  This interval has length <1 and is enclosed in two complete marked
  periods per wall: p=4.
* Across every unit offset mesh, the two starting-anchor registrations
  have lattice distance at most 3. Consecutive marks have distance 1.
  With neighboring gauge error c beta, Lambda <= (8+7c) beta.
* Common normalized averaging preserves these same errors and the
  interpolation; it does not multiply p or the anchor comparison count.
  Round 5 should therefore give E X^- <= (24+21c) beta.

Will also supply explicit uniform local-comparison and spatial-support
constants, so the bound is not left conditional on untracked mesh counts.

## Extension saved

Wrote PROOF.md. A reference-grid construction supplies each neighboring
local P-increment comparison with error at most 7 beta: two enclosing
periods for each endpoint attachment and three for the network step.
All input cells lie within index radius 23; H=40 is sufficient. Applying
round 4 gives c=7 C_(2,40) as the neighboring gauge-error coefficient.
The theorem's assumptions explicitly retain the dominated potential,
local road rules, conditional period bounds, and spatial product inputs.

For one link and every fixed wall-phase assignment, the four-period
calculation gives

    E X^- <= 3(8+7c) beta = (24+147 C_(2,40)) beta.

The proof uses common normalized averaging on the same physical anchors.
It does not average different roads or exchange a minimum with an average
as an equality. Uniform conditional bounds can be integrated over the
independent phase law; they do not control a phase chosen from the weights.

Using the round-4 reference formula, R=121 and L=201. Every complete
window record/gauge lies within radius 407 of its own row center, and
one link has input radius 408 about the left center. Reference phases
lie among wall indices j through j+244, a span of 244 (245 indices).
Entire column fields are independent in residue classes modulo 2000:
their spatial strips have half-width 816, while 2000(1-s^2)>1980>1632;
their wall-phase lists are also disjoint. These are conservative constants,
independent of phase-group size, row spacing and small s.

No executable computation or simulation is used. These constants are
symbolic counts, to be independently checked in the adversarial pass.

## Adversarial audit and second derivations

Read back the entire new PROOF.md using
`env OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md` (exit 0; priority warning).

* Recounted the signed comparison: the endpoint-to-reference intervals
  lie in deterministic nominal windows of length <1, and the network
  step in a deterministic window of length <2. Thus 2+3+2=7 is a
  count of fixed full periods after phases are fixed, not the invalid
  expectation of a weight-selected set of periods. Clarified this point
  in the text. Cut labels are tagged separately from the reference label.
* Re-derived delta directly: delta=11s/500, so 2delta=11s/250<1.
  Start levels equal t_j-delta-u_j with u_j in [0,1). The difference
  is -s+u_j-u_(j+1); registration errors add at most one, making the
  integer vertical difference at most 2. Horizontal difference is 1.
  Period registrations differ exactly by (0,1), even at rounding ties.
* Recounted Lambda by its three kinds of terms: 8 beta for four doubled
  defects, 4c beta for period errors, 3c beta for the starts. Multiplying
  by 3 gives 24+21c=24+147 C_(2,40).
* Independently checked averaging at the objective level:
  inf_gamma average_a L_a >= average_a inf_gamma L_a. Negative parts
  then obey the required reverse monotonicity and Jensen inequality.
  This agrees with averaging anchor errors before applying round 5.
* Checked the support twice: a mark is within nominal height 2 of its
  center, registration adds 1/2, and a Q_L cell contributes at most
  (1+s)(L+1). This is <2L+9/2<407. The right center is <1 away.
  Separately, the phase reference site adds R+1 to a coordinate within
  R of the registration, giving index range [j+1,j+2R+1]. Both walls
  give [j,j+244]. Spatial conditional expectations keep that same list.
* Verified R=121, L=201, 2L+5=407, link radius 408, strip half-width
  816, and separation 1980>1632 (margin 348). The phase-list span 244
  is smaller than 2000. This proves joint column independence from
  disjoint primitive-coordinate sets, not merely pairwise independence.
* Tested pauses exactly at marks, repeated visits, internal edge endpoints,
  coinciding rounding ties, empty competitor sets, common additive gauge
  offsets, arbitrary finite phase-group size, and countably many rows.
  Restricted the optional competitor families to closed constraints that
  survive loop deletion and admit the stated finite-route description.

A categorical example checks the missing inference: fixed-phase negative
first moments beta and a normalized average beta coexist with a spatially
selected phase giving m beta. Hence no row/phase supremum is smuggled into
the theorem. This example does not contradict the source's fixed-link
estimate or the canonical FPP gauges.

The result establishes the link-level bounds for the explicit round-4
gauge construction. The source uses a larger reference cutoff; its exact
numeric support/phase constants would differ. The argument does not yet
establish compatibility of these smaller-cutoff gauges with the separate
common-baseline construction of Lemma 10.6. No contraction claim is made.

## Final readback and files

Re-read round 5's complete PROOF.md in one bounded invocation to remove
any ambiguity from the first aggregate output. Re-read the current full
REPORT.md and PROOF.md. Commands:

```sh
env OMP_NUM_THREADS=1 nice -n 15 cat ~/codex_op_1114r5/briefs/T050/PROOF.md
env OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md PROOF.md
env OMP_NUM_THREADS=1 nice -n 15 rg --files .
```

All exit 0 with the same denied-priority diagnostic. File enumeration
finds LOG.md, PROOF.md, REPORT.md and the pre-existing prompt/runtime files.
No script, simulation output or SOLVED_ELSEWHERE.md is claimed. Final
readback clock: 2026-11-15 06:23:14 UTC. Subsequent edits only clarified
the distinction between a reference anchor's parameter window (half-width
3 epsilon_r) and the larger input inspection window (4 epsilon_r),
spelled out that the calibration does not use phases/private seeds,
and made the nonempty event explicit in the alternative averaging check.
Neither the constants nor the stated result changed.

Deliverables are complete. The report starts with the required PARTIAL
verdict and states both the new link estimate and the remaining template,
common-baseline and output-road questions. No shared state outside this
folder was changed.
