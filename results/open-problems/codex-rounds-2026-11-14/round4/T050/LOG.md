# T050 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded time: 2026-11-15 00:26:09 UTC / 04:26:09 Asia/Tbilisi.

## Orientation and prior work

Read both previous folders' REPORT.md and LOG.md, the original
SOLVED_ELSEWHERE.md, and round 3's complete PROOF.md. File enumeration
(`rg --files`) finds no research scripts in either folder and no PROOF.md
in the original folder. Read the startup memory and compute governor state.
Governor: warn, CPU saturated; no heavy computation planned. The current
folder-only instruction overrides shared checklist, mesh and memory writes;
none are made. No git or subagents.

Reads used `env OMP_NUM_THREADS=1 nice -n 15 cat <paths>`.
The sandbox reports `nice: setpriority: Operation not permitted` while
allowing the reads. Priority changes must not be represented as successful.

## Brief literature check

Web queries:
- `"first passage percolation" "strict convexity" 2026 November`
- `"Strict convexity and differentiability of the planar exponential" correction error`

Opened the manuscript landing page and its linked scope document:
https://mathcommunity.github.io/oai-math-revised/papers/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/
https://github.com/mathcommunity/oai-math-revised/blob/main/lean/docs/212.md

The scope document still excludes strict convexity from the selected
formalization. No verified solution of the general continuous-law problem
was located. Close the literature-update search here, within five minutes;
further source reads are for the mathematical audit.

Next: independently re-derive the round-3 defect comparison and its constants,
then select one contraction-side lemma to audit, as its report requests.

## Independent recheck of round 3: holds under its stated assumptions

Re-derived its main inequality without the source's Markov-event argument.
If the unchanged route has metric excess W, clip it at the saving v.
On the good event, `min(W(F omega),v) >= v-D1`; off it the clip is
nonnegative. Total variation therefore gives
`E D2 >= v(1-q-TV)-E D1`. Since both expected defects are at most
`CR beta`, this gives `beta >= 3v/(8 CR)` at q,TV <= 1/8.
An independent tail-integral derivation gives the same coefficient.

Checked the distributional inputs directly: the scaled Gamma likelihood
second moment is `(b(2-b))^(-kappa)` by integrating its density square.
For m changed edges this is `(1-(epsilon/n)^2)^(-kappa m)`.
With `m <= 2 CV n^2` and `epsilon <= 1/(8 sqrt(kappa CV))`, its logarithm
is at most 1/24, hence TV < 1/8. Independently the relative entropy is
`kappa(b-1-log b)` per edge, yielding the same tolerance by Pinsker.
For the cheap-path event, counting only length-floor(n/(2K)) prefixes
gives `(4/3) CV n^2 exp(theta a n) 2^(-floor(n/(2K)))`, bounded by
the previous `q_n`; `theta a = log(2)/(8K)` leaves exponent
`-3 log(2)n/(8K)`. Checked `CR=2(200+2)=404`.
The same-endpoint subtraction and full-period domination handle random
cuts without assuming their potentials have zero mean. No error found.
This verifies the auxiliary conditional lower bound, not contraction.

## One chosen extension, recorded before proving it

Audit and independently prove the finite-cell local-potential step, extending
it to independent inputs indexed by Z^d for every d >= 2, with an explicit
locality radius and error constant. This is the single next piece: round 3
specifically leaves Lemma 10.2 unchecked. The proof will replace its large
cutoff by a smaller cube and supply the boundary-detour argument in full.
It will also test the dimension restriction with a one-dimensional example.
It will not claim any higher-dimensional road construction or contraction.

Source read: OpenAI, the September 24, 2026 manuscript, printed pp. 35–37
(Lemma 10.2), and pp. 85–87 for context. PDF opened through link 8 on
the landing page; searches inside the PDF used `Lemma 10.2`, `15.6`, `15.7`.
All source reads used the web tool. No executable computation is needed
for the exact estimates now being proved.

## Finite-cell theorem proved and saved

Wrote PROOF.md with a full finite-projection construction, explicit cube
boundary path, error recovery, and covariance check. For d >= 2, H >= 2,
the local potential uses radius `L=5H+1`, with
`m=(2H+1)^d`, `R=3H+1`,
`N=(2R+1)^d 2^((4H+1)^d)`, `J=(d+3)R+2`,
and error constant `C=2+2 N J 2^m`. Constants depend only on d,H.
The previous manuscript uses planar radius `10H+20` and leaves its error
constant implicit. The gauge definition is compatible as labels are added;
it uses only the chosen label and a fixed reference label.

The cutoff error is controlled by traveling along the boundary of Q_R(k)
to its east side and one step beyond. All comparison supports miss every
projected cell set because `R-H=2H+1`. At most `(d+3)R+1` spatial steps
and one label change are needed. Every subset of the comparison support
appears in both endpoint gauges; the remaining symmetric-difference terms
are boundary terms. This verifies the recovery identity without requiring
an expansion of a nonlocal calibration.

## Attempts to break the result

Re-derived the finite projection identities using commuting coordinate
averaging/centering operators, independently of subset pairing. Checked
the strict clearance by the separate distance calculation
`dist(b,Q_(2H)(k)) >= R-2H=H+1`. Recounted the longest boundary route as
`2R+2R+(d-1)R+1` spatial moves; adding the label change gives J.
Checked the error count against the union of endpoint families, rather
than counting intersection and boundary terms separately: at most 2N
terms, each at most `J 2^m epsilon`, plus centered error `2 epsilon`.

Tested d=1 with iid symmetric signs and their cumulative sums. Their
increments are exactly local, yet any putative finite-radius gauge would
make the telescoped endpoint difference independent of a middle sign.
Its correlation with that sign must then be zero, whereas telescoping the
increments gives one. The contradiction also excludes a fixed-C estimate
for arbitrarily small positive epsilon. Thus the dimension restriction is
essential for this general auxiliary lemma, even without covariance.

Checked same-site label changes (no boundary terms), nonlocal extra
randomness (finite conditional projections remain local), nonidentical
independent cell laws (no identical-distribution step is used), and exact
error zero. No estimate takes a supremum over labels. The uncountable-label
statement is understood pairwise almost surely, not as one universal
version at all labels on one event.

No numerical experiment, simulation, or research program was run. All
load-bearing constants above have exact second derivations in PROOF.md.

## Readback and report

Command: `env OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md LOG.md`.
Output: complete proof and log; exit 0, with the previously recorded nice
priority warning. Clock after readback: 00:30:14 UTC.
Opened Section 10.3, including Lemma 10.4, and the rest of Sections 15.6–15.7
for the next-worker recommendation. Their proofs are not certified here.
Wrote REPORT.md with a PARTIAL verdict, the exact scope, commands, limitations
and next step. No SOLVED_ELSEWHERE.md is appropriate: no verified solution
of the full task was found.

The initial discovery command was `pwd; rg --files -g 'AGENTS.md' -g 'MEMORY.md'
-g '*.md' -g '*.py' -g '*.sh' . <both prior folders> ~/.claude
2>/dev/null | head -100`; it was not priority-wrapped. Subsequent shell reads
used the requested env/nice wrapper, whose priority change was denied.

Final report readback command: `env OMP_NUM_THREADS=1 nice -n 15 cat REPORT.md`.
Output: required PARTIAL verdict on the first line, complete report, exit 0;
the same priority warning appeared. Corrected its first read command to
include the startup-memory file that was read in the same invocation.
Deliverables: LOG.md, PROOF.md, REPORT.md, all in this folder.
