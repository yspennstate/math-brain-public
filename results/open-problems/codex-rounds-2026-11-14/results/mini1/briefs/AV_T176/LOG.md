# T176 verification log

Task received: 14 November 2026 (Asia/Tbilisi); exact prompt receipt time was not supplied.

## Step 1 — orientation and first source search

Read the local startup note and compute-state JSON using `OMP_NUM_THREADS=1 nice -n 15 /bin/cat ...`; compute status was `ok`. The sandbox reports `nice: setpriority: Operation not permitted`, although the tiny read commands complete. No compute experiment is planned. The task's folder-only rule takes precedence over global instructions to write mesh, checklist, and brain state; those were not invoked.

Used the web search tool with `"Optimal-order mixing" "Thorp"` and `"Compatibility entropy" "Thorp"`. Tried all three supplied GitHub folder URLs; the web fetch returned cache misses. Search results identify all three as power-of-two results, and reveal family 238 Lean documentation and community follow-up notes. These are leads only until opened. No git commands, external writes, or subagents.

## Step 2 — repository access and formalization scope

Used the read-only GitHub connector `github_fetch` on each `api.github.com/repos/openai/math/contents/preprints/<folder>` directory. All three contain README.md, build/, and paper.pdf. Guessed build/paper.tex returned 404 for all three; listing build/ is the next step.

Opened `https://raw.githubusercontent.com/openai/math/main/lean/docs/238.md` and repository README.md. The family scope claims full mixing at 1600d for the first paper, but explicitly excludes bounded regular moments from the selected compatibility formalization, and says the routing formalization covers earlier nine statements rather than changed later statements. Scope remains n=2^d throughout. README describes model-generated manuscripts at different verification stages.

## Step 3 — all three manuscript statements opened

Listed build directories and fetched actual `build/main.tex` files, plus `build/sections/00-introduction.tex` for the two long papers, through the GitHub connector. Saved those exact source texts under sources/. All give author OpenAI and date September 26, 2026. The first theorem explicitly claims TV convergence at 1600d physical shuffles and a 2d-O(1) lower bound. Its history section expressly says the arbitrary-even question is not addressed. Compatibility's two main theorems are weighted compatibility and bounded regular moment; its corollary claims full physical mixing. Routing's main theorem gives a reflected-pair routing-density moment and forward-sweep representation contraction, with full mixing as a consequence. Exact quotes will be extracted into VERIFY.md.

Ran web searches for the three titles with arxiv/comment/error/refutation terms. Results include community notes, an exposition, a claimed constant improvement, and a November Monte-shuffle paper citing the result; these require opening before reporting as follow-ups.

## Step 4 — follow-ups and Lean statements opened

Opened all three oai-math-revised manuscript pages, the Latent Seminar exposition (6 October), Yunjiang Jiang's arXiv:2610.18884 abstract, and Ilya Mironov's arXiv:2611.03959 abstract and HTML paper (2 November). Mironov §1.3 cites OpenAI's optimal-order Thorp result; the new theorem is for a different, random-pair Monte chain. The community pages are explicitly automatically collected and unreviewed, so their links are leads rather than independent validation.

Opened repository history.md, lean/README.md, ComparatorChallenges/README.md, and the four Comparator statement files ThorpRemaining.lean, ThorpFirstReciprocal.lean, ThorpRouting.lean, and ThorpWeightedCompatibility.lean using github_fetch. Challenge files contain intentional `sorry` placeholders; solution/configuration files must be distinguished from those challenges. In the opened ThorpRemaining challenge, OptimalOrderMain explicitly gives IsTheta for log(2^d), while constants in other displayed propositions are 2048d and 32800d; 1600d is stated in the scope note. Repository history has no Thorp-specific correction or withdrawal.

Opened the pinned cert-machine statement audit JSON, release fd4aeeb, and located family 238 (lines 9537 onward). It reports headline statement MATCHES through ThorpRemaining, while separately flagging definition-body comparisons in OccupiedOverlap and SpinAngle. This is a statement audit, not a proof certificate. Opened the cutoff-agenda README, which proposes cutoff at 2d and says the OpenAI bounds do not settle cutoff. Follow-up constant-note paths need directory resolution after a guessed path failed.

## Step 5 — deliverables saved

Used apply_patch to write VERIFY.md and REPORT.md. Exact theorem environments were extracted directly from the stored source strings, including both compatibility theorems and its mixing corollary. Verdict: PARTIAL-CLAIMED for n=2^d only. VERIFY.md includes the clause-by-clause comparison, nine opened follow-up entries, Lean scope distinctions, and a three-sentence replacement status. Opened the configured Lean solution entry files and JSON configurations; no build was attempted. Opened R5's actual README and R25's note.tex; both leave author “[AUTHOR NAME]”, so no human name was invented. No arbitrary-even extension or proof refutation was found. Next: one load-bearing lemma spot check, after the required report exists.

## Step 6 — transfer lemma spot check and final source checks

Read §6 and its full proof of Proposition 6.1 (Eight-block Fourier bound) in the saved optimal-main.tex. Checked the multiplicity-independent orbit-span bound, coset orientation, Schur average, exponent −5/16 and constant √(32C1) by direct algebra. No defect found in that proposition under its stated hypotheses; this is not an audit of the conditional-flow stage or the complete theorem. Opened FirstFourier.lean, ThorpResults/Main.lean, Statements.lean, and formalization.yaml to distinguish actual solution entries from challenge placeholders. A read-only GitHub issue search `repo:openai/math Thorp` returned an empty issues list. No computation, Lean build, or third-party checker was run.

## Step 7 — exact formal clock located; spot check appended

Followed solution imports through ThorpResults/Mixing.lean, ThorpShuffle/FixedLists/Main.lean and FullDeck.lean to ThorpShuffle/Main.lean. It explicitly states `full_mixing : Tendsto (fun d => distance d (1600 * d)) ...` and a main theorem including worst-start equality and lower/upper order bounds. Saved that file under sources/lean-thorp-main.lean and added its exact statement to VERIFY.md. The catalogue review status is `unchecked`; no independent formal check is claimed. Appended the detailed spot check under “Spot check”. One apply_patch append initially failed because the context was only a substring of a paragraph; it made no change, then the correct full-line context succeeded.

## Step 8 — final audit

Ran a tiny read-only `OMP_NUM_THREADS=1 nice -n 15 python3 -B` check inside this folder. All five exact theorem/corollary source quotations in VERIFY.md match the saved primary TeX verbatim. REPORT.md has its required PARTIAL-CLAIMED first line and exactly three reason lines. Spot check is present. Removed a stray plus-only formatting line found by the audit. The sandbox still rejects the requested priority adjustment, as recorded in step 1; no substantial local computation was run. Final result: claimed optimal mixing on powers of two only; no claim resolving the whole arbitrary-even row. All authored output is in this folder.
