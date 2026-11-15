# T030 continuation log

Task: “Verify: has open problem T030 been settled by the OpenAI math release?”
Session date: 15 November 2026, Asia/Tbilisi. Exact start clock to be recorded below.

## 1. Earlier work and orientation

Read the earlier REPORT.md, LOG.md and VERIFY.md in `~/codex_op_1114/briefs/AV_T030` using `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c ...`. The listing contains no PROOF.md or scripts; the prior result is a literature scope finding and an algebraic spot check, rather than a computation. Its main claim is a smooth-boundary restriction, leaving the strict arbitrary-convex-boundary row unfilled. Its last check selected the Green-kernel regularization lemma and reported no algebraic defect.

The shell printed `nice: setpriority: Operation not permitted` but executed; inherited priority will be checked before further programs. No git or subagents. All writes remain in this folder. The later folder-only order rules out global brain/checklist/mesh mutations, including recall commands that log outside the folder. A startup-memory path attempted by the previous worker was absent; read-only orientation only is appropriate here.

Initial web searches: `"Strict hot spots and absence of interior critical points"` and `"hot spots conjecture" "2026" proof convex`. Results include the same smooth-domain claim, the existing follow-ups, and a seminar abstract describing the claim. No newly established full strict planar convex result was identified in these initial results. Search results are leads until opened.

## 2. Time, resource check and bounded literature update

The first clock call returned 2026-11-14 20:50:54 UTC, or 15 November 2026, 00:50:54 Asia/Tbilisi (the session began shortly before that reading). The local compute state is warn, owner_away_open, CPU saturated; no heavy computation will run. `OMP_NUM_THREADS=1 nice -n 15 python3 -c ...` confirms inherited priority 20 and Python peak RSS 11,747,328 bytes. Read the startup memory and memory index directly without changing external state.

Opened arXiv abstracts and full HTML for 2610.12622 (Krzysztof Burdzy), 2610.32920 (paper by Rodrigo Bañuelos), and 2610.18546v2 (Haiyun Deng, Xuyong Jiang, Xiaoping Yang; revised 2 November 2026). Searches for the exact title with error/refutation/correction, `"hot spots conjecture" "2026" proof convex`, `"hot spots" "November 2026" convex proof`, `"hot spots" "2611" convex`, and `"hot spots" "November 14" "2026"` found no later full strict convex-planar resolution. The first two sources remain conditional, non-strict and simple-eigenvalue results; the third controls strict maximum modulus and expressly distinguishes it from both signed extrema. This is a bounded search, not a proof of absence. No SOLVED_ELSEWHERE.md is warranted.

Reopened the actual OpenAI introduction, reciprocal-kernel section and `lean/docs/369.md` through read-only GitHub file tools. The introduction still assumes C-infinity boundary. The main theorem still quantifies over the full first-positive real eigenspace. The Lean scope still says smooth boundaries and multiplicity allowed. Thus the earlier scope comparison holds independently of the earlier report.

## 3. Chosen extension (recorded before working on it)

Check the next kernel step after the earlier regularization audit: the finite positive-quadrature resolvent and its passage to a bounded continuous kernel. Give an independent Schur-complement derivation of the node-elimination denominators and an explicit operator-norm error estimate for quadrature, rather than relying only on the manuscript's chain-counting description. This is one extension of the earlier spot check, not a proof of the hot-spots conjecture. First independently rederive the regularization's scalar mixture in a different variable and verify its normalization.

## 4. Independent recheck result

The earlier scope claim holds: the freshly opened introduction and Lean scope retain C-infinity/smooth boundary, the full eigenspace quantifier and the first-positive/second-counting-zero eigenvalue convention. The three follow-ups do not close both the regularity and strictness gaps for the exact universal row.

The earlier regularization spot check also holds. Change its mixture variable to r=1/(1+v) and integrate the alpha parameter explicitly. This gives `f(h)=integral_0^1 [(h+r)(log((1-r)/r)^2+pi^2)]^(-1) dr`, with f(0)=1/2 by the substitution t=log((1-r)/r) and pairing t with -t. This independently checks the sign, diagonal normalization and Stieltjes density. The disk-kernel Gram representation then gives exactly the same positive-semidefinite correction and bound `C_epsilon<=1/(2*pi*epsilon)` as before. Detailed derivation will be in PROOF.md.

Fresh source snapshots saved: source-introduction-current.tex (GitHub blob ca7f7f292379a95899f04a1de411eb610d1fe9ab), source-reciprocal-current.tex (bcb125482dbfe6874ffe4582625c01ea66571ca9), source-lean-scope-current.md (303e026dc76b6d793b2b441e8bbc2ad3d88f0af7). Source reads used github_fetch_file; no git commands.

## 5. Resolvent proof and exact arithmetic check

Wrote PROOF.md: independent explicit Stieltjes-density recheck of the earlier regularization; the finite update lemma; a Schur-complement derivation of the full finite resolvent and positive elimination denominators; and an explicit bound for passing positive quadrature to a bounded continuous compact-support kernel. The core additional check is the bounded resolvent step; no singular-kernel/boundary or eigenfunction proof is claimed.

Wrote and ran `OMP_NUM_THREADS=1 nice -n 15 python3 audit_resolvent.py`. Standard-library Fraction arithmetic checks the direct full inverse against sequential updates in all 34 orderings across five fixtures, checks every pivot against its independent determinant ratio, and checks reciprocal inertia by exact symmetric congruence. Fixtures include zero weights, repeated evaluation points, integration endpoints and coincident integration nodes. Output:

```text
four_nodes_with_duplicate_evaluation_points: orders=24, row_bound=271/1575, minimum_pivot=85695828686/91043783325, final_inertia=(1, 3, 2)
zero_weights: orders=2, row_bound=61/675, minimum_pivot=44011/46575, final_inertia=(1, 3, 2)
one_node: orders=1, row_bound=72/595, minimum_pivot=523/595, final_inertia=(1, 3, 2)
coincident_integration_nodes: orders=6, row_bound=299/3570, minimum_pivot=78529/81360, final_inertia=(1, 3, 2)
empty: orders=1, row_bound=0, minimum_pivot=1, final_inertia=(1, 2, 3)
coincident-node merging: exact equality
negative update: initial inertia=(1,1,1), final inertia=(2,1,0)
critical one-node weight w=1: singular, as required
quadrature perturbation formula: 18 exact scalar equality checks
PASS: 34 elimination orders; exact rational arithmetic throughout
priority=20, peak_rss_bytes=14811136
```

Elapsed execution was under one second. Inertia tuples count positive, negative and zero eigenvalues. The negative-update test deliberately breaks an overgeneralization: coefficient c=-1/2 yields two positive reciprocal eigenvalues, despite all entries staying positive. Its Schur-complement eigenvalues 8/15 and -32/15 were also recomputed exactly. The strict subcritical threshold fails at the one-node weight w=1. Eighteen scalar exact tests attain equality in the quadrature perturbation bound and independently check its constants.

## 6. Other candidate statements and Lean target reopened

Opened and saved the current optimal-transport introduction, complex-geometry paper, and Lean target as source-mtw-introduction-current.tex (blob a17608323207e26c589bb4ed1f7b62f561d02dcd), source-symmetry-current.tex (75578580f59258c45f53aafb6b8345ca2e354f11), and source-lean-target-current.lean (9e8c905519d515e23be329f1e4a544618a9d2397). Extracted the first theorem verbatim from each actual paper. The first concerns tangent injectivity domains on compact boundaryless Riemannian manifolds; the second concerns bounded semialgebraic complex domains with compact quotients. Neither contains a Neumann hot-spots assertion.

The Lean target explicitly includes SmoothBoundary in AdmissibleDomain, defines the first-positive value by a mean-zero Rayleigh infimum, and asks for nonvanishing gradient plus both strict signed inequalities. Its `sorry` is in the challenge statement, not evidence of a defect in the separately supplied solution. No Lean execution or new comparator-log verification is claimed in this continuation.

## 7. Verification file saved

Created VERIFY.md with the three exact main-theorem quotations, the phrase-by-phrase row comparison, the three follow-ups reopened, current Lean scope/target evidence, the three-sentence proposed row update and the new spot-check result. Earlier comparator/exposition records are explicitly distinguished from new source reads. An initial JavaScript construction failed on an unescaped backtick before making any file change; the corrected construction succeeded. No mathematical finding changed.

## 8. Final report and artifact audit

Replaced the draft REPORT.md with the continuation verdict: PROVED the bounded positive-kernel resolvent lemma with quantitative quadrature error, expressly retaining PARTIAL-CLAIMED as the literature verdict for the full T030 row. The report identifies the unchecked singular/boundary/eigenfunction steps and gives the next checkable step.

Ran a small read-only artifact audit with `OMP_NUM_THREADS=1 nice -n 15 python3 - <<'PY' ... PY`. It checked that all three exact theorem blocks occur verbatim in the freshly fetched sources, all four current paper source snapshots agree with the earlier saved versions (ignoring a terminal newline), REPORT.md has the required continuation verdict and no draft wording, Markdown fences balance, and no control-character escapes corrupted the math. All passed. Peak RSS 13,975,552 bytes; inherited priority 20; elapsed under one second. Output artifact sizes before this final log entry: VERIFY.md 13,278 bytes, PROOF.md 14,385 bytes, REPORT.md 1,463 bytes, LOG.md 9,015 bytes.

Final clock: 2026-11-14 21:00:10 UTC = 15 November 2026, 01:00:10 Asia/Tbilisi. Only this task folder was written. No git, subagents, external mutations, messages, accounts, GPU, ML libraries, or long-running process was used.

Task completed: “Verify: has open problem T030 been settled by the OpenAI math release?” — 15 November 2026, about 00:50 Asia/Tbilisi (start).
