# T078 verification log

Task received: 2026-11-14, approximately 21:02 Asia/Tbilisi. Verify whether the three named OpenAI math preprints claim the full T078 statement.

## Step 1 — orientation and first source requests (21:03)

- Read the local memory index and brain navigation index, and the compute governor state using read-only shell commands prefixed with `OMP_NUM_THREADS=1 nice -n 15`. Governor: `ok`, `owner_away_open`. No heavy compute is planned.
- `nice` reported `setpriority: Operation not permitted`; the small read-only commands still completed. No background jobs, worker processes, git commands or external writes were started.
- The task's explicit folder-only rule takes precedence over older instructions to update the external brain, mesh and checklist. Those state-mutating utilities will not be run.
- Opened all three supplied GitHub folder URLs with the web tool. Each returned `Failed to fetch ...: Cache miss`. This is an access failure, not evidence about the mathematics. Raw-file and connected GitHub access are next.

## Step 2 — repository access recovered

- Web searches: `"openai/math" "Heisenberg"`; `"The spherical magnetization law" ferromagnet`; `"Spontaneous magnetization" "September 24" "2026"`. Located the spherical-law PDF and a possible independent review repository, `mathvet/mathvet`.
- Tried each candidate's root `paper.tex` with the web tool: two cache misses, one 404. No theorem has yet been inferred from those failures.
- Used the connected GitHub read-only `github_fetch` tool on `https://api.github.com/repos/openai/math/contents/<candidate-folder>` for all three. All succeeded. Each folder has a `build/` directory; PDFs are `spherical-magnetization.pdf`, `paper.pdf`, and `bloch-law-heisenberg.pdf`, respectively.
- Opened repository metadata: issues and discussions are disabled; last push reported 2026-10-30. This does not establish anything about independent review.

## Step 3 — main theorems read

- Read all three actual TeX entry points and their introduction files through GitHub's read-only contents API. Correct locations: spherical `build/main.tex` and `build/sections/01-introduction.tex`; ordering `build/source/main.tex` and `build/source/sections/00-introduction.tex`; Bloch `build/main.tex` and `build/sections/01-introduction.tex`.
- All three papers name the author `OpenAI`; dates match the supplied folders. Saved their introduction sources unchanged under `sources/`.
- Ordering Theorem 1.1 explicitly claims every integer dimension d >= 3 and every allowed spin, at every sufficiently large finite beta: a translation-invariant zero-field beta-KMS state with magnetization >= S/4. This matches the entire requested spontaneous-magnetization statement.
- Spherical Theorem 1.1 is restricted to d=3, but adds the pressure magnetization, spherical moment-generating function and limiting averaged two-point order. Bloch Theorem 1.1 is also d=3 and claims an exact magnetization-deficit asymptotic for a larger finite-range interaction class.
- Read all three paper READMEs, repository README, history, Lean README, `lean/docs/271.md`, and `lean/ComparatorChallenges/Heisenberg.lean`. The docs explicitly describe a formalization of the all-dimensions ordering theorem; its precise implementation is being checked. The repository history names no correction or withdrawal of these papers.
- Follow-up web queries: exact ordering title excluding openai GitHub; exact spherical-law phrase excluding openai GitHub; Bloch + Heisenberg + OpenAI + 2026; OpenAI + Heisenberg + error/correction/referee/review. Search hits alone are not treated as opened papers or expert validation.

## Step 4 — report saved; formal proof located

- Saved REPORT.md with SOLVED-CLAIMED for the entire stated row, and VERIFY.md with exact theorem environments and the phrase-by-phrase comparison. Follow-up investigation continues.
- Read `lean/ComparatorChallenges/Heisenberg.json`: solution module is `OAI.MathematicalPhysics.Heisenberg.Main`, theorem `OAI.Heisenberg.spontaneous_magnetization`; permitted axioms are propext, Quot.sound and Classical.choice; enable_nanoda is false in upstream configuration.
- Read the actual solution `lean/OAI/MathematicalPhysics/Heisenberg/Main.lean`, not just the challenge. Its final theorem has the advertised all-dimension/all-spin statement, using ell = 2S and lower bound ell/8 = S/4. Challenge `sorry` is intentional statement scaffolding; Main.lean supplies a proof using imported modules. No Lean build has been run here.
- Opened the community page for the September paper (updated November 9): it reports no human notes, labels its collected notes unreviewed, and links an accepted Comparator run dated October 26. Opened mathvet's primary STATUS.md (generated November 1), which lists Heisenberg among accepted checks. These are formal-check reports, not referee certification of the manuscript.

## Step 5 — follow-up sources opened and scope checked

- Opened the primary community run log `mathcommunity/oai-math-revised/checks/comparator-2026-10-26/logs/Heisenberg.log`. Its final output says the Lean default kernel accepts the solution and `Your solution is okay!`.
- Opened that project's `docs/LEAN_CHECKS.md`. It distinguishes a checked Lean theorem from correspondence with a paper, notes precompilation in the same workspace, and says the run was set up by an AI agent. These qualifications will accompany the report of acceptance.
- Opened the Binary Verse AI exposition linked from the community page. It is an exposition, not expert refereeing; its byline and date are being checked directly.
- Opened mathvet's `fidelity-table.json` and `challenge-status.json` and extracted only family 271 / Heisenberg. The family has `partial` formal coverage because Bloch's law and the lattice correction have no statement there, while the selected theorem is exactly the September spontaneous-magnetization result. The challenge record reports a sandboxed pass on October 8 at 17:46:15Z for upstream adc7f124, with unchanged statement at the review snapshot. Its `referee_verdict` field is empty.
- Searched exact titles restricted to arxiv.org, and OpenAI/ferromagnet with Ueltschi, Seiringer, Toth, refutation, error and referee. No matching arXiv version or named specialist assessment has yet been located. The original repository's issues/discussions are disabled; the community issue-search page failed to load, so it cannot support an assertion that no reports exist.
- Read the ordering paper's full exposure-section source. Selected its Conditional next-pin first moment proposition as the spot check: this is the bridge from a conditioned cycle permutation to fresh one-particle Markov returns. The determinant calculation will be checked directly, with its hypotheses retained.

## Step 6 — follow-up findings saved

- Confirmed the exposition's byline is `Azmat`, October 15, 2026, directly on its page. It disclaims a full independent formalization audit.
- Opened mathvet's primary cloud `Heisenberg.comparator.txt` and `Heisenberg.cmp.txt`: Comparator exits 0, default kernel accepts, comparison output lists theorem and definitions as matching, standard three axioms only. Saved its log and extracted review/status records locally.
- Read the extra OpenAI companion's main source and introduction: `The first lattice correction to Bloch's law`, October 5, 2026. It is another same-release d=3 claim, not an independent paper or new all-dimension result.
- Read GitHub's `branches/main` endpoint: snapshot `4eaee87548250b2682affda7d05d947c05554bae`, committed October 30, 2026.
- Completed VERIFY.md's follow-ups, opened-source record and three-sentence recommended row wording. Saved the ordering exposure source, Lean scope/challenge/config/solution and independent formal-check records under `sources/`.
- One document-update tool cell had a JavaScript quoting error before execution; no files were changed by that failed cell. Reissued the update successfully.

## Step 7 — load-bearing determinant bridge checked

- Checked Proposition 4.3's determinant expansion, all-hit conditioning, Schur complement, substochastic transience and recovery of every first-moment entry; also checked the rank-one/exterior-moment algebra used in Lemma 4.2. No defect found under the stated hypotheses. Exposure-law and analytic bootstrap inputs remain outside this spot check.
- Ran `OMP_NUM_THREADS=1 nice -n 15 python3 sources/check_next_pin.py`: exact Fraction enumeration of three-label independent swaps, pins {1,2}, and a nonsymmetric determinant test. All 25 rational parameter pairs passed. At a=b=1/2 the outputs were P(G)=3/4, H=((2/3,1/3),(1/3,2/3)), determinant expectation -8.
- The process reported nice value 20: the earlier nice warning reflects an inherited priority already below requested 15, not normal-priority compute. OMP_NUM_THREADS was 1. The standard-library-only check completed in under a second.
- Appended Spot check to VERIFY.md. An initial append patch used an incomplete context line and made no change; the corrected append succeeded.

## Step 8 — final audit and completion

- Ran a read-only standard-library audit under `OMP_NUM_THREADS=1 nice -n 15 python3`: all three theorem environments in VERIFY.md match the saved manuscript sources verbatim; REPORT.md has the required verdict line and three reason lines; the recommended row wording has exactly three sentences; Spot check is present; linked local source paths exist; no draft placeholder remains.
- Audit passed. Process nice value 20; maximum resident memory 13,664,256 bytes. No git, push, posts, messages, accounts, background jobs, external file edits or heavy builds were used.
- Deliverables complete: REPORT.md, VERIFY.md, this LOG.md, and 13 small source/check artifacts in sources/. Verdict remains SOLVED-CLAIMED for the full stated spontaneous-magnetization formulation, without a judgment that the full proof is correct.
- Task: “Verify: has open problem T078 been settled by the OpenAI math release?” Received approximately 2026-11-14 21:02 Asia/Tbilisi.
