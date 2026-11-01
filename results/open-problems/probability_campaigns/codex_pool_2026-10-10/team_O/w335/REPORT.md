15 draft lemma nodes and 27 edges are saved for the ten assigned problems, with both endpoints quoted on every edge. All ten numerical or algebraic check scripts passed. The strongest measured extension is P0205: an exact Metropolis relaxation formula for every complete Cayley graph, extending the earlier two-state calculation. All results await w347; zero independent keeps and zero full open-problem solutions are claimed.

For the lazy P0205 family with alpha=p=1/2, `python -X utf8 check_p0205.py` gives a relaxation ratio of 1.5 at n=2 and 682.777850 at n=1024 from the proved formula. Complete kernels were checked with exact fractions at n=2,3,4,8,16,32: 60 cases and 16,388 assertions. The ratio grows linearly while the base relaxation stays below 2; proposal degree grows with n. This is a measured family calculation, not a deployed recall benchmark or a fixed-degree result.

| Problem | Saved result | Run evidence |
|---|---|---|
| P0205 | Complete-Cayley spectrum and explicit parameter direction | 60 exact cases; 16,388 assertions |
| P0429 | Simultaneous arrivals obstruct path independence at the cubic scale | 170 exact hypergeometric cases |
| C0127 | Common-factor counterexample to the stated growing-peaks criterion; two-peak quantifier correction | Proof plus 1,200 illustrative samples |
| P0050 | Divergent squared marginal gap implies singularity under negative correlations | 40 exact product-law cases |
| P0255 | Weighted-star variation at most 1/(2 sqrt(6)) | 1,360 weight vectors, four one-leaf cases; 200 general graphs searched numerically |
| C0014 | Wired layer minima give the lower comparison; incompatible currents block gluing | Six exact four-vertex cases; ratio 25.5025 at M=100 |
| C0073 | Added dangling conductance slows a constant-speed walk while conductivity stays fixed | Eight exact clock cases |
| C0109 | Sharp scalar truncation envelope; rank-one nonnormal spectral obstruction | Ten exact tail cases and seven spectral cases |
| P0004 | A nonstationary bounded-degree tree lacks a connective limit; p=1 lattice boundary works | Eight block ends and lattice enumeration through length ten |
| P0027 | Smooth all-starts deterministic maps are rigid; positive displacement characterizes the isometry class | Four exact tensor ranks and 16 rotation gaps |

`python -X utf8 validate_deliverables.py` passed the integrator's isolated shape-validator function, all 27 endpoint quotations, and 18 existing targets read from SQLite in read-only mode. Recorded successful check-body runtimes total 1.974699 seconds; this excludes process launch, queueing, reading and inference cost. Commands and full receipts are in each `<problem>_measurement.json`; the additional star boundary command is `python -X utf8 finalize_corrections.py`.

The Lean helper returned `SETUP_UNVERIFIED: Compute status is distressed or unknown`. GapIdentity.lean formalizes only the scalar gap identity and remains unverified. No result is labelled Lean-checked.

Literature status is `literature_check_pending` for all ten. The ranking and observed cards record historical source statements, not present-openness certificates. Four named cached primary texts were inspected. The earlier Codex worktree path no longer exists; existing typed attempt cards supplied those six earlier attempts. No exact literature solution was established in this bounded offline pass; no web search was used. Source receipts are in results.jsonl and source_records.json.

The material limits are explicit in each node: P0429 treats whole paths, P0050 still needs a divergent forest marginal gap, C0127 keeps nonzero overlap, and the tree, periodic network and deterministic nonnormal examples lie outside the full models in their assigned questions. Numerical searches are not proofs. Six measured hook proposals passed one fire and one silent control each and are staged in hooks/math-w335.jsonl. Source-line alignment improved from 7 wrong windows to zero over 10 checked hits.

Apply: after w347's KEEP/FIX/DROP review, the reviewer should retain only approved entries and run `python -B -X utf8 ~/math-brain-build/tools/integrate_drafts.py --only w335`; patches/01_math_bundle_drafts.diff names the same live inbox paths, and patches/02_math_hooks.diff stages the separately audited hook proposals. No live store or code was edited. Audit and progress handoffs are files because the packet forbids sends and SQLite writes; PROGRESS_PENDING.jsonl is not a claim of publication.

NEXT: w347 audits REVIEW_PACKET.json; the reviewer integrates only KEEP entries and records the receipts in the brain.
