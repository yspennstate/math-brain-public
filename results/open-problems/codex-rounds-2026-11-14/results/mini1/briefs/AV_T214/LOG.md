# T214 verification log

Task received: 14 November 2026, approximately 21:12 Asia/Tbilisi (17:12 UTC). Verify whether the OpenAI math release claims the full free-Ising factor-of-IID statement.

## Step 1 — orientation

Read the supplied instructions and local directory listing; read `~/.claude/compute/compute_state.json` with `OMP_NUM_THREADS=1 nice -n 15 python3`. Governor reports `ok`, `owner_away_open`. The shell printed `nice: setpriority: Operation not permitted` but the small read-only Python command completed; priority will be inspected before further local programs. Local files initially: `codex.log`, `PROMPT.md`, `run.pid`.

Scope: all writes stay in this folder. No git, subagents, external messages, or shared-brain/checklist/mesh mutations: those would write outside the explicitly authorized folder. Read-only startup-memory inspection is permitted. Web search and opening sources are next.

## Step 2 — source access and first search

Web `open` on all three supplied GitHub folders returned cache misses. GitHub connector `github_fetch` successfully opened repository metadata: repository exists, issues and discussions disabled, last push shown as 30 October 2026. Web search for the three exact titles found their records: the Ising abstract explicitly claims every d >= 3 and equality at tanh(beta)=(d-1)^(-1/2); this is only a search record, so the paper itself is still required. Search also located `lean/formalization.yaml` with `OAI.Problem367.free_ising_factor_iff_threshold`, and a Plectis Atlas transcription. These require opening.

Read startup memory index and brain navigation index without mutations. Priority inspection using `os.getpriority` returned 20: the processes already run at still lower priority than requested, explaining the denied attempt to reset niceness. All local programs remain small, single-threaded, and invoked through `OMP_NUM_THREADS=1 nice -n 15`.

## Step 3 — repository structure

Opened each candidate folder and its `build/` directory with the read-only GitHub connector. Ising has `article.pdf` and modular `build/main.tex`; forest has its title-named PDF and modular `build/paper.tex`; planar maps has `main.pdf` and modular `build/main.tex`. Opened repository README and `lean/` listing. README calls the collection raw research data and points to `history.md`, `lean/formalization.yaml`, and Comparator instructions. Root `docs/` was not found; documentation is under `lean/docs/`.

Read the existing brain note `openai_math_preprint_repo_as_a_source_2026_10_15.md` read-only: useful pointers are history and the formalisation catalogue; its old counts and judgments are not treated as current evidence.

## Step 4 — actual papers and formal statement

Opened all three main TeX files, their included introduction TeX files, and manuscript READMEs. Saved these exact fetched files under `sources/`. All authors are OpenAI, dated 26, 25, and 24 September 2026 respectively. Ising theorem is the sharp iff statement; forest theorem is graphwise FUSF sampling; maps theorem is measured metric convergence of finite decorated planar maps.

Opened `history.md`: no Ising-specific withdrawal or correction is listed in entries through 29 October. Opened `lean/formalization.yaml`, `lean/README.md`, Comparator README, `FreeIsing.json`, `FreeIsing.lean`, solution `Main.lean`, and `Model.lean`. The solution states the exact threshold iff and imports variance-analysis/recovery modules. Comparator challenge has an intentional `sorry` placeholder; this is the challenge, not evidence of a missing solution proof. Its configuration allows only propext, Quot.sound, and Classical.choice. `lean/docs/367.md` is about Bernoulli minimizers, so the internal namespace number must not be confused with a documentation family number. Correct documentation mapping is being located.

## Step 5 — comparison and later-source search

Read the exact main statements. Ising Theorem 1.1 covers every requested parameter and the equality endpoint, with the same spin law and full automorphism group. It additionally claims an everywhere-equivariant version and the known strict converse. FUSF Theorem 1.1 and planar-map Theorem 1.1 are different models/quantities. Saved REPORT.md with SOLVED-CLAIMED before optional proof spot checking.

Web searches: exact Ising title plus arXiv; OpenAI/free Ising plus error, refutation, proof, review; exact forest title plus error; exact maps title plus refutation/error/review/arXiv. Located Plectis Atlas's FreeIsing statement page, opened successfully; it links reports by MathVet and Carlos Toledo's cert-machine. Exposition pages at AI Proved What and DiscoverIA were attempted but web opening returned cache misses; search snippets are not treated as opened evidence. No matching arXiv version of the Ising preprint has been located by the searches so far.

Opened correct scope notes `lean/docs/236.md` (Ising), `231.md` (FUSF), and `211.md` (maps family). Ising scope explicitly includes equality and almost-sure equivariance for each fixed automorphism. Maps scope only links a different q > 4 CRT paper, not this q in (0,4) metric-measure paper. Independent report links and later map papers will be checked directly next.

## Step 6 — outside records and saved verification

Opened Plectis Atlas links to MathVet fidelity/status CSVs and Carlos Toledo cert-machine statement/kernel JSONs. GitHub web pages mostly showed file metadata, so opened actual contents through the GitHub connector. MathVet's FreeIsing row reports `full` and `comparator-sandboxed-pass` at 2026-10-08T19:33:18Z. Cert-machine's FreeIsing record reports `CERTIFIED`, Comparator exit 0, Lean and nanoda accept, at 2026-10-10T09:06:43Z; its statement record says MATCHES. These are reported checks, not a local rerun or a referee report.

Opened all three mathcommunity/oai-math-revised manuscript pages: no reader notes listed; pages link expositions and automated checks. Opened Latent Seminar expositions for Ising and forest (6 October), each explicitly excluding independent verification of the whole proof. Opened arXiv abstract pages 2610.10501 and 2610.10505 for related planar-map work; exact titles/authors and relevant passages remain to be read.

Saved VERIFY.md with exact TeX theorem quotations copied programmatically from all three opened introductions, a clause-by-clause comparison, formalisation scope, and the three-sentence recommended status. REPORT.md already exists. Follow-up details and the optional load-bearing-lemma check will be appended.

## Step 7 — endpoint estimate and further literature

Opened and read the full Ising `08-critical-comparison.tex` and `08b-recovery.tex`; also opened solution modules `ActualVarianceAnalysis.lean` and `SharpVarianceRecovery.lean`. Selected the small-time log-factor lemma (Lemma 8.2) for the optional spot check: it improves S <= C V just enough to remove the nonintegrable 1/t coefficient at the endpoint. Saved its complete section under `sources/` with the main Lean definition/statement/configuration files and repository history.

Read arXiv author/title metadata directly: Nina Holden, The Tutte embedding of tree-weighted planar maps converges to Liouville quantum gravity, arXiv:2610.10501; Nina Holden and Pu Yu, The circle packing and Riemann uniformization embedding of the tree-weighted planar maps converges to Liouville quantum gravity, arXiv:2610.10505. Both are later related planar-map works, not versions of the Ising manuscript. Opened their HTML papers next to check the reported comments rather than relying on a catalogue summary. Repeated exact-title arXiv/error/gap/referee searches; no specific refutation of the Ising claim or matching arXiv version was located.

## Step 8 — direct follow-up verification

Opened the original mathcommunity FreeIsing Comparator log and `docs/LEAN_CHECKS.md` through the connector. Log ends with Lean-kernel acceptance and successful comparison. Documentation dates the run 25–26 October, says it was agent-operated and used precompiled modules, and explains its scope limitations. It did not run nanoda for this challenge; the separate cert-machine record did. Saved relevant outside records and the full community log. An initial Add File patch failed because generated CSV lines lacked patch prefixes; retried with correct line prefixes, without altering any source.

Opened Danny Nam, Allan Sly, and Lingfu Zhang's arXiv:2012.09484v2 abstract, confirming the prior model and constant-times-threshold result. Read both later planar-map HTML papers; Holden–Yu explicitly state that neither their paper nor the OpenAI results imply the other. The community page's assertion of an OpenAI comment in Holden's single-author paper was not confirmed: `OpenAI` is absent from both the opened v1 HTML and PDF, so that assertion will not be repeated as fact. This is why the original papers were opened.

## Step 9 — completed follow-up inventory and spot check

Expanded VERIFY.md with direct links, checking dates and limits, later-paper authors/titles as displayed on arXiv, attempted-but-unreadable exposition pages, and bounded negative search findings. Appended Spot check on Lemma 8.2. Independently differentiated log a, derived the cavity-to-site L2 discrepancy bound, checked both branches of the exceptional-event estimate, and evaluated the two small-time integrals and Osgood divergence. Found no algebraic or inequality defect in that lemma assuming its upstream inputs; made no verdict on the full paper's proof.

Next and final step: audit the saved theorem quotes against the exact local TeX snapshots, verify REPORT format and recommended-sentence count, and read back the deliverables. No compilation or heavy computation is needed.

## Step 10 — final audit

Ran a small read-only `OMP_NUM_THREADS=1 nice -n 15 python3` audit. All three quoted main theorem TeX blocks match their saved introduction sources exactly. REPORT has the required verdict first line and exactly three reason lines. Recommended replacement has exactly three sentences. Spot check is present and the draft placeholder is gone. Priority remains 20. Read back REPORT; final sizes before this log entry: REPORT 698 bytes, VERIFY 17,977 bytes, LOG 9,770 bytes. No git command, external write, subagent, compilation, or heavy program was used.

Completed task: “Verify: has open problem T214 been settled by the OpenAI math release?” Received 14 November 2026, approximately 21:12 Asia/Tbilisi. Result: SOLVED-CLAIMED for the whole statement, with exact quotations, comparison, opened-source follow-ups, and conditional Lemma 8.2 spot check in VERIFY.md.
