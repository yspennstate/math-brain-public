# T050 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First clock reading: 2026-11-14 21:00:35 UTC (2026-11-15 01:00:35 Asia/Tbilisi).

## Orientation and earlier files

Read the earlier REPORT.md, LOG.md and SOLVED_ELSEWHERE.md at
`~/codex_op_1114/briefs/T050`.
`rg --files` confirms that no PROOF.md or research scripts exist there.
Read the startup RESUME.md and compute state. The latter says `warn`,
`owner_away_open`, CPU saturated. No heavy computation is planned.
The present folder-only rule overrides shared mesh/checklist/brain writes;
none will be made. No git and no subagents.

Read commands used `env OMP_NUM_THREADS=1 nice -n 15 cat ...`.
The sandbox printed `nice: setpriority: Operation not permitted`, although
the reads succeeded. Priority cannot be assumed to have changed.

## Literature check, begun 21:00 UTC

Web search queries:
- `"Strict convexity and differentiability" "first-passage" correction`
- `"first passage percolation" "strict convexity" 2026 OpenAI review`

Reopened the primary scope note at
https://raw.githubusercontent.com/openai/math/main/lean/docs/212.md .
Search results again locate OpenAI's September 24, 2026 claim; no new
general continuous-law theorem or independent verification has appeared in
these searches. The PDF open initially failed. Next obtain its Part II and
independently check the earlier report's scope claim and a specific argument.

## Earlier result independently rechecked; one extension chosen

At 21:01 UTC, clicking the landing page's PDF link succeeded (95 pages).
The direct raw-PDF open gave unsupported content type; shell curl failed DNS.
No manuscript file was downloaded. Read Theorems 1.1–1.2, Definition 9.1,
Lemma 9.2, Proposition 9.5 and Proposition 15.2 from the web-parsed PDF.
Their statements independently confirm the earlier report: exponential planar
strict convexity is claimed, positive Gamma differentiability is separate,
and the contraction explicitly claims the original admissible road class.
The earlier result HOLDS as a report of a claim, not a verified theorem.

The bounded literature check is closed after roughly two minutes, well under
five minutes. No new verified solution was found. No SOLVED_ELSEWHERE.md will
be written here because the full problem has not been found solved.

Choice before the mathematical work: independently prove the uniform positive
lower bound of Proposition 9.5 for the finite-range road class, and extend this
one bound to all positive Gamma laws. Include random endpoints and explicit
change-of-measure constants. This is one contained piece suggested by the
earlier report, with a wider distributional scope. It isolates a necessary half
of the strict-convexity contradiction; the much longer contraction remains
open in this audit. The proof will state its conditional calibration input and
avoid comparing that nonlocal calibration across environments.

## Lower-bound audit: first derivation

Read the complete proof of Proposition 9.5 (printed pp. 33–35), the geometry
and road definitions (pp. 29–31), and the cheap-path estimate (p. 32).
The entropy transfer and random-cut cancellation both check algebraically.
The factor in the source's last line also checks: if the two error terms are
at most 1/8, then `3 CR beta >= (3/4) lambda`, with
`lambda = a_* epsilon/2`, giving `beta >= a_* epsilon/(8 CR)`.

A sharper route avoids the Markov event: clip the excess cost of the untouched
route over the passage metric at the guaranteed saving `v`. Its expectation
changes by at most `v TV`. On the cheap-path good event it is at least `v-D1`
after perturbation. Hence `E D1 + E D2 >= v(1-q-TV)`.
This gives three times the displayed source lower bound at the same two 1/8
error tolerances. For Gamma(shape kappa, rate lambda), scaling entropy is
`kappa(a-1-log a)`, and the cheap-path Laplace parameter can be
`theta=lambda(6^(1/kappa)-1)`. These are the two law-specific inputs.
Next write the complete conditional theorem, verify the geometric constants
and redo both distribution calculations in a second way.

## Proof saved and external input checked

Wrote PROOF.md: a Gamma-law positive local-road defect theorem with a full
random-cut argument, planar corner construction, support separation,
all-path lower-tail bound, and clipped-excess transfer. The lower bound is
`beta >= 3 a epsilon/(8 CR)` for
`a=log(2)/(8 K lambda(6^(1/kappa)-1))`,
`epsilon=min(1/2,1/(8 sqrt(kappa CV)))`,
`CR=404`, `CV=(8M+3)^2`.
It is conditional on a stationary dominated calibration with prescribed mean,
which is the standard external input for a hypothetical flat face.

Opened the primary arXiv page and PDF of Michael Damron and Jack Hanson,
*Busemann functions and infinite geodesics in two-dimensional first-passage
percolation*, arXiv:1209.3036. Read their assumptions A1 and Section 3's
choice of any supporting functional, Proposition 3.2, Proposition 3.4,
and Theorem 3.5. These supply exactly stationarity, additivity, domination,
and the prescribed mean. Gamma laws satisfy the moment and zero-mass
conditions. No differentiability assumption is needed for this input.
No unverified claim about a formalized theorem is used.

## Adversarial checks, second derivations

- Recomputed the law change by the independent exact likelihood second moment:
  `(1-(epsilon/n)^2)^(-kappa m)`, at most `exp(1/24)` for the chosen epsilon.
  Cauchy–Schwarz gives TV < 1/8, agreeing with the entropy/Pinsker calculation.
- Recounted cheap paths using only length-R prefixes, instead of summing over
  all lengths. This gives factor 4/3 in place of 8/3 and verifies the weaker
  bound used in the proof. After rounding the exponent is
  `-3 log(2)n/(8K)`.
- Independently re-derived the clipped-transfer inequality by integrating tail
  events. It has coefficient 1 on `E D1`, not 2. This explains the improvement
  over the source's Markov-event calculation.
- Checked geometric constants directly from the matrix [[1,s],[s,1]]:
  inverse infinity norm `1/(1-s) <= 4/3`, weaker constant 2 sufficient;
  `L=200` leaves a separation exceeding 10; `2(L+2)=404`.
- Checked selected endpoints and pauses: complete-period containment is
  pathwise, and no zero mean of a potential at a selected cut is asserted.
  The changed law is used only for a bounded metric excess without calibration.
- Checked rate scaling: the lower bound is proportional to `lambda^(-1)`.
  For kappa=lambda=1 the threshold is `log(2)/(40K)` and the certified lower
  bound is three times the source's displayed constant with the same epsilon.

No numerical experiment or script is needed for these exact inequalities.
Only file reads and the failed curl used the shell. No heavy program ran.
The required nice invocation failed at the sandbox level; this limitation is
recorded rather than claiming a successful priority change.

## Final report and scope

Read back LOG.md and PROOF.md with
`env OMP_NUM_THREADS=1 nice -n 15 cat LOG.md PROOF.md`.
Output: files complete; the only shell diagnostic was the already recorded
`nice: setpriority: Operation not permitted`.
Wrote REPORT.md with the required PARTIAL first line. It distinguishes the
proved lower-bound lemma from the unverified contraction and the full open
problem. Removed a reading-process sentence from PROOF.md so its content is
mathematical statement, proof, checks, and references only.

Reproducible failed download command:
`env OMP_NUM_THREADS=1 nice -n 15 curl -L --fail --max-time 30 -o manuscript.pdf https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf`
Output: `curl: (6) Could not resolve host: mathcommunity.github.io`.
No PDF file was created. No executable research scripts or numerical outputs
are claimed. All new results are exact inequalities in PROOF.md.

Final inspection commands:
`env OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md` and
`env OMP_NUM_THREADS=1 nice -n 15 rg --files .`.
Both returned exit 0 with the same priority diagnostic. REPORT.md starts
with the required verdict. The file listing contains PROOF.md, LOG.md,
REPORT.md and the pre-existing prompt/runtime files, with no manuscript.pdf
or computation script. Corrected the report's command list to match the
separate readback commands actually executed.
