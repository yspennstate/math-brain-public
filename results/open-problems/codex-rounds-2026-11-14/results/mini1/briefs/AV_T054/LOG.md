# T054 verification log

Task received: “Verify: has open problem T054 been settled by the OpenAI math release?” Start observed 2026-11-14 21:02 +04.

## Step 1 — scope and orientation

- Read the supplied instructions and local startup memory (read-only). The task-specific instruction forbids writes outside this directory, so no shared checklist, mesh or brain mutation was run.
- Commands: `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c ...` for file listing, startup-memory reads, compute-state read and date. The system printed `nice: setpriority: Operation not permitted` but executed the short read-only commands. No simulation or heavy computation was started. Compute state reported `ok`, `owner_away_open`.
- Initial folder contained PROMPT.md, codex.log and run.pid.

## Step 2 — initial source retrieval and search

- Web `open`: the three supplied GitHub folders returned cache misses. Root-level raw `paper.tex` returned 404 for GOE and Anderson; Ising returned an unexpected status. These failures do not establish that the papers are absent.
- Opened https://github.com/openai/math successfully. README describes raw model-produced research, warns that unformalized results may have issues, and links the catalogue, history and Lean catalogue.
- Web searches: `"GOE bulk universality" "OpenAI" "2026"`; `"Fixed-energy universality for weak Anderson disorder"`; `"Conformal universality of bulk Ising correlations"`.
- Search results identify family 219 (GOE/Anderson), family 218 (Ising), community reading pages, and a potentially relevant November paper titled “Mesoscopic eigenvalue statistics for random regular graphs: a case study”. None yet substitutes for reading the original theorem.

## Step 3 — GitHub connector and release records

- Read-only GitHub connector `github_fetch` successfully listed the GOE folder, finding README.md, build/, and paper.pdf (610750 bytes). No git command was used.
- Opened Anderson `build/paper.tex`; it inputs separate sections and attributes the paper to OpenAI, October 5, 2026. Saved as Anderson-paper.tex.
- GOE and Ising `build/paper.tex` returned 404; checking actual filenames next.
- Opened and saved lean/README.md, history.md and CONTENTS.md. Release history through October 29 contains no named GOE/Anderson correction or withdrawal. This is not proof of correctness.

## Step 4 — original sources and follow-up leads

- GitHub connector listed GOE build/sections and found build/main.tex; listed Ising build/ and found build/main.tex and sections/.
- Saved the Anderson introduction, GOE main source, Lean formalization catalogue, and family-218 scope note. Listed lean/ and lean/docs/: there is a 218.md but no 219.md.
- Web opened arXiv 2610.08127 and 2611.09215 and the Latent Seminar exposition https://lowrank.github.io/latent-seminar/OpenAI-Math/219-random-regular-spectra (dated October 6). The exposition explicitly disclaims independent complete-proof verification.
- Web searches added `error OR gap OR refutation OR review` to the GOE title, `error OR arxiv OR review` to Anderson, and `error OR gap OR review` to Ising. Results include expositions and a November mesoscopic-statistics paper; these need direct reading before conclusions.
- Opening the raw GOE PDF with the web tool failed because its content type was application/octet-stream. The TeX source is accessible through the GitHub connector.

## Step 5 — main GOE statement and authors checked

- Opened and saved GOE build/sections/01-introduction.tex and Ising build/main.tex, and listed the Ising section filenames.
- GOE Theorem 1.1 states convergence of fixed-energy Laplace functionals for every fixed d≥3 and every energy strictly within the Kesten–McKay support, through all admissible sizes. Model is uniform simple labelled unweighted graphs, without extra conditioning.
- The GOE introduction attributes complete delocalization for every fixed d≥3 to Huang and Yau as an input; it describes sampled-edge Gaussian moments as an intermediate construction. Need to distinguish those averaged moment statements from spatial QUE.
- Directly opened arXiv 2610.08127: Yukun He, Jiaoyang Huang, Xiaoyu Wang; submitted October 6, 2026. Its abstract claims fixed-energy Sine_1 convergence, deterministic-label consecutive gap universality and fixed-energy correlation measures. It is a distinct author list/title, not an identified arXiv version of the OpenAI preprint.
- Directly opened arXiv 2611.09215: Jaehun Lee; submitted November 6, 2026. Abstract concerns a mesoscopic CLT at scales (log N)^(-1)≪η≪1, rather than the microscopic theorem or QUE.

## Step 6 — all three original theorem sources read

- Opened and saved Ising sections/model.tex and introduction.tex, GOE sections/02-preliminaries.tex and 03-entropy.tex.
- Ising Theorem 1.1 is about mixed spin/energy correlations in two-dimensional square-lattice Gibbs models, not graph adjacency spectra. Its full theorem is available in Ising-model.tex.
- Anderson Theorem 1.1 requires fixed positive uniform diagonal disorder 0<w<w0(d,κ), compact clean-bulk energies, and unfolding by the disordered infinite-tree density. It does not include w=0 as a theorem case.
- GOE Proposition 3.1 (Uniform endpoint moments) averages monomials over sampled edges, uniformly over finitely many bulk eigenindices. This is not itself the assertion that every deterministic spatial observable is equidistributed in every eigenvector.
- Lean family-218 scope note covers a finite-graph likelihood comparison in a different companion, not Ising conformal universality. The formalization catalogue search found no family-219 or Anderson/regular-graph entry.

## Step 7 — follow-up papers, expositions and preliminary report

- Opened the full HTML of He–Huang–Wang arXiv:2610.08127v1 and Jaehun Lee arXiv:2611.09215v1. Checked normalization: He–Huang–Wang use Nπρ_d(E) with Sine_1 intensity 1/π; OpenAI uses Nρ_d(E) with unit-intensity GOE. These differ by a deterministic dilation only.
- Opened Plectis Atlas family 219, the oai-math-revised Ising entry, and AI Proved What family 219. These are exposition/catalogue pages, not referee reports. The Atlas lists no family-219 Lean statement; original repository checks agree.
- Further web searches used the exact GOE title with “error” and “gap”, exact Anderson title with “arxiv”, and `"random regular" "OpenAI" "QUE"`. No specialist refutation or validation was identified from these queries.
- Wrote REPORT.md with PARTIAL-CLAIMED: the clean bulk eigenvalue claim matches, while spatial QUE is missing. A detailed theorem-by-theorem comparison and source register follow in VERIFY.md. Spot checking is limited to one main dependency and does not certify the proof.

## Step 8 — follow-up qualifications and original Lean statement

- Web `find` on the He–Huang–Wang full HTML returned no “OpenAI” match; do not infer a version relationship or a proof review from its parallel result.
- Web `find` on Lee’s full HTML found reference [40] to OpenAI’s clean GOE manuscript. Its introduction cites this and He–Huang–Wang for bulk universality; this is a later scholarly citation, not an audit of the OpenAI proof.
- Opened https://postcutoff.com/science/openai-math/: search snippet calls family 219 “Confirmed by an independent expert”, but the stated support is the separate He–Huang–Wang result. This must not be reported as a referee verification of the OpenAI argument.
- Opened all three manuscript READMEs: author OpenAI, dates as supplied, no correction/withdrawal notices. The Anderson README points to a differently named PDF; the actual TeX main source and introduction were read directly.
- Opened lean/OAI.lean and lean/ComparatorChallenges/BufferedIsing.lean. The latter is a finite-graph likelihood comparison statement ending in `sorry` as a challenge template; this does not mean the separate solution is absent. The family scope, not that template, establishes the limited formalization coverage.
- Attempted `ps` to verify niceness; the sandbox disallowed it. Read the existing niceness memory: relative nice may fail when a parent is already maximally niced. A tiny `os.getpriority` check is used next; no heavy computation.

## Step 9 — detailed verification saved

- Wrote VERIFY.md with exact source-extracted theorem environments for all three candidates, model definitions, clause-by-clause comparison, opened-source register, and a proposed three-sentence row update.
- Opened Huang–Yau arXiv:2102.00963v3: authors Jiaoyang Huang and Horng-Tzer Yau, revised February 2, 2025, abstract explicitly states complete delocalization for every fixed d≥3. This corrects the old note’s large-degree-only delocalization scope.
- Opened and saved the remaining three GOE sections (limits, switching, DBM) to check for an additional spatial QUE theorem; their theorem/section inventory supplies no such statement.
- Resource check: `OMP_NUM_THREADS=1 nice -n 15 python3 -c ... os.getpriority ...` reports inherited niceness 20, OMP_NUM_THREADS=1, and 11,927,552-byte peak RSS. Thus the earlier nice warning occurs while the process is already below the requested priority. No numerical job, threads, GPU or Lean build was launched.
- REPORT.md was written before the optional spot check, as requested. Selected the clean paper’s tensor-coercivity lemma, the strict finite-dimensional input in the Gaussian-moment argument.

## Step 10 — optional spot check completed

- Read all of Lemma 3.5 (Tensor coercivity), ent:tensor, and its proof in GOE-entropy.tex. Recomputed the frame normalization/weights, the projection deficit, the three-slot commutation identity, and the common-kernel equality case by hand.
- Independent algebra check: neighbor-frame inner product c=−1/(d−1), commutator determinant c²(1−c²)>0 on the two-plane for d≥3; the bulk condition makes both weights positive. The proof’s finite-dimensional compactness step then has the required hypotheses.
- Appended the exact lemma and detailed checks to VERIFY.md under “Spot check”. No error found in that lemma; no correctness conclusion about the full preprint.
- Final web queries target fixed-degree QUE and possible later comments on Anderson/Ising; any new primary result will be read before adjusting the conclusion.

## Step 11 — final search reveals a QUE qualification to check

- Fixed-degree QUE searches returned a 2026 ICM survey and an older Cayley-graph paper attributing a form of probabilistic QUE to Bauerschmidt–Huang–Yau for sufficiently large fixed degree. This contradicts a blanket reading of “QUE at fixed d is open”, though it need not settle every fixed d≥3 or a stronger QUE formulation.
- The candidate verdict remains about what the OpenAI theorem actually states. Checking the original older paper and survey before finalizing the proposed status sentence; the original row does not define QUE’s quantifiers or observable class.

## Step 12 — QUE caveat verified against primary literature

- Opened Bauerschmidt–Huang–Yau arXiv:1609.09052 abstract and original 106-page PDF. Corollary 1.3(ii), equation (1.7), explicitly states probabilistic QUE for deterministic test vectors, uniform over bulk eigenvectors, for sufficiently large fixed degree. Equation (1.8) treats deterministic vertex sets. The proof uses exchangeability; graph-dependent tests are explicitly excluded.
- Opened Jiaoyang Huang’s official ICM 2026 survey “Spectral Statistics of Sparse Random Graphs”, DOI 10.1137/25M180603X, Section 4.3. It explicitly mentions probabilistic QUE without averaging over eigenvectors. The passage does not itself state a quantitative all-degrees theorem.
- Opened the Huang–Yau arXiv:2102.00963v3 full HTML as well; its original complete-delocalization statement is confirmed.
- Revised VERIFY.md and REPORT.md to flag the old QUE-open sentence as overbroad, rather than silently perpetuating it. The explicit OpenAI theorem-scope verdict remains PARTIAL-CLAIMED. The recommended update now asks for a precise intended QUE formulation and does not assert that every fixed-degree QUE formulation is open.

## Step 13 — final audit and completion

- Tiny one-thread Python audit, invoked under `OMP_NUM_THREADS=1 nice -n 15`, compared each quoted theorem in VERIFY.md byte for byte with the opened local TeX source: GOE 385 characters, Anderson 800, Ising 1624; all exact matches.
- Verified REPORT.md has the required verdict prefix and exactly three reason lines, VERIFY.md has the recommended status and Spot check sections, and the superseded blanket QUE-open sentence is absent. No invalid control characters found.
- Audit process reported niceness 20 and peak RSS 16,334,848 bytes. All local programs were brief, CPU-light and below the 1 GB cap. No git, external write, subagent, GPU, MLX, torch or Lean build was used.
- Optional web screenshot of the older BHY PDF page 5 failed because screenshot handling was unavailable; the PDF’s text and equations were read through web open/find. No screenshot-derived claim is made.
- Final files: VERIFY.md (26,942 bytes; SHA-256 adf48b47d821396df0751b89b0de0c206d2c3c7f6372c16466e4c4be9bbeb565), REPORT.md (913 bytes; SHA-256 3f76bd86a465e4cfdfdbec00cd6c5ecaa6a18f3ce66cd62786b0133b3ed0e864). Original-source snapshots remain in this folder.
- Completed 2026-11-14 21:10 +04. Task: “Verify: has open problem T054 been settled by the OpenAI math release?” Received/start clock observed 2026-11-14 21:02 +04.
