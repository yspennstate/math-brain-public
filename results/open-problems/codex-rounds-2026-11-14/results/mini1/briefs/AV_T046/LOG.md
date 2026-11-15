# T046 verification log

Task received: 14 November 2026, approximately 21:00 Asia/Tbilisi (17:00 UTC).

## Step 1 — scope, startup, and initial access

Read `PROMPT.md`, the brain startup/navigation files, and the compute governor state. The task-specific instruction confines all writes to this directory, so no shared checklist, mesh, or memory writes are made. No git commands or subagents are used.

Commands ran through `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c ...`, using only short reads and file listings. The sandbox reports `nice: setpriority: Operation not permitted`; `ps` is also denied. Thus the requested priority cannot be verified or changed here. No heavy computation is attempted. Governor snapshot: `warn`, `owner_away_open`, CPU saturated.

Web tool opened all three supplied GitHub preprint folder URLs. Every request returned `Failed to fetch ...: Cache miss`; no preprint text was obtained. Next: try raw sources, search indexing, and independent access routes.

## Step 2 — indexed records and raw-source attempts

Web tool tried `paper.tex` at all three raw GitHub paths: all returned 404. Searches: `site:github.com/openai/math "SK" "Glauber"`, `"A typical-start upper bound" Glauber`, and `"The low-temperature Sherrington-Kirkpatrick" "2026"`.

Search found all three release records (author OpenAI, 24 September 2026), community catalogue pages, and a free-energy record on Proofweave. Abstracts describe Gaussian zero-field Sherrington–Kirkpatrick spin glasses, not the two-dimensional nearest-neighbour ferromagnet. The dynamics abstract gives typical-equilibrium-start mixing by `exp(n^(1-1/40000000))`; the other two abstracts concern free-energy variance and limiting law. These are abstract-level observations; exact theorem statements still need manuscript access. A community search excerpt mentions a 20 October follow-up by Aronow and Patrick Lopatto; it has not yet been opened or verified.

Read startup memory and the memory index directly. No recall program was invoked because it logs outside the permitted folder. The index contains a verified note about macOS `nice` saturation, but the current process priority remains unverified.

## Step 3 — manuscript PDFs and follow-up access

Opened the community catalogue entries for the dynamics and limiting-law papers, then followed their PDF links. Successfully opened the actual 22-page dynamics manuscript (OpenAI, 24 September 2026) and the actual 126-page limiting-law manuscript (same author/date). Dynamics Theorem 1 is “Mixing from a typical Gibbs state,” with explicit exponent `1/40000000`. Its model section defines all-pairs independent Gaussian couplings and no boundary.

Also opened the release README, the family-227 Lean scope page, `SKFluctuations/EventuallyNatPos.lean`, and the Hexagon record `2610.00402v1`. Community notes are expressly unreviewed and AI-collected, so their descriptions are leads rather than proof verification. The fluctuation-scale raw `paper.pdf` request returned a cache miss; alternate filename/source paths are next.

## Step 4 — source structure and formalization scope

Web opened raw `build/paper.tex` successfully for the dynamics and fluctuation-scale papers; these are wrappers importing introduction/section files. The corresponding limiting-law wrapper path is 404, but its PDF is readable. Opened raw `lean/docs/227.md`: the listed formalized low-temperature result is a mixing obstruction (lower bound), not this candidate's upper bound. Raw `lean/docs/217.md` returned 404. Read limiting-law PDF pp. 1–3: `F_n=log Z_n`, Theorem 1.1 claims standardized convergence to a nondegenerate law for every fixed real `beta>1`.

## Step 5 — exact main statements obtained

Opened the dynamics `build/introduction.tex` and fluctuation-scale `build/sections/introduction.tex`, obtaining their complete main theorem environments. Read limiting-law PDF Theorems 1.1 and 1.2, including the moment-rate and positive-variance-prefactor assertions. All three manuscripts are now readable at theorem level. The dynamics model matches the row's rate-one-per-site convention, but differs in interactions, geometry, boundary, initial-state quantifier, and bound.

Opened Hexagon `2610.00402v1` overview/provenance: authors/contributors P. M. Aronow and Patrick Lopatto; 20 October 2026; explicitly primarily AI-generated. It claims strengthened typical-start SK bounds and Lean formalizations. This is a follow-up claim, not independent proof certification or a 2D Ising result.

## Step 6 — targeted follow-up searches

Web searches used each exact candidate title followed by `error refutation arxiv`, plus `Ising plus boundary mixing time polynomial Lifshitz 2026 2605.08052`. No direct refutation, referee report, or arXiv reissue of the three candidates appeared in those returned results. This is a limited search finding, not a claim that none exists. Opened release `CONTENTS.md`, `lean/formalization.yaml`, and `history.md` for scope/revision checks. Search independently recovered Gheissari–Sly's May 2026 phase-ordering paper and the original quasi-polynomial Ising paper PDF.

## Step 7 — current Ising references and release-wide scope

Opened arXiv pages `2605.08052` (Reza Gheissari, Allan Sly), `1112.3160` (H. Lacoin, F. Simenhaus, F. L. Toninelli), and `1102.3466` (Hubert Lacoin). Attempted `https://math.nyu.edu/~eyal/papers/Tc.pdf`: 404. Release contents search found no `Lifshitz`; `Ising` results concern other equilibrium/critical models, not the target plus-boundary mixing law. The catalogue's family 217 has no Lean scope link. Its formalization index has no `SKFluctuations` match. At the opened historical Lean file, `main_of_positiveLaplaceWindow` explicitly takes `hw : PositiveLaplaceWindow` as a hypothesis; this is conditional coverage, not an unconditional limiting-law formalization. No Lean compiler run is claimed.

## Step 8 — provenance, formal scope, and verdict saved

Opened all three manuscript README files: they confirm OpenAI and 24 September 2026 and give the actual PDF filenames. Opened Gheissari–Sly's full arXiv HTML, the `pmaronow/fluctuations-palomar` repository README, the full perceptron follow-up HTML, and Latent Seminar's family-227 exposition. The Lean follow-up README expressly excludes a fluctuation limiting law and positive variance prefactor; its upper bound remains typical-start SK. It also qualifies verification receipts by revision. No build or comparator replay was attempted. The mean-bias Hexagon link initially returned a cache miss. Saved `REPORT.md`: `VERDICT: NOT-THIS`, with three lines of reasons.

## Step 9 — verification document saved

Opened arXiv `1012.1271`, confirming the four authors and quasi-polynomial bound, and arXiv `2610.31736`, confirming its four authors and submission date. Read Gheissari–Sly's explicit open-problem statement and Lemma 8 of the SK dynamics manuscript (pp. 19–20) for a possible spot check. The mean-bias record remained inaccessible; the raw fluctuation PDF returned unsupported content type. Saved `VERIFY.md` with all three main theorem statements (including both principal limiting-law theorems), clause-by-clause comparison, opened follow-ups, formal scope qualifications, and a three-sentence replacement row note. No proof correctness verdict is made.

## Step 10 — spot check saved

Read the remainder of Lemma 8 and the proof's final parameter substitution on PDF pp. 20–21; also requested screenshots of dynamics p. 19 and limiting-law p. 3. Re-derived pruning, the `2R/B^2` Poincaré constant, entropy dissipation, complement-mass control, and the exponent sign. Appended the check under `Spot check` in `VERIFY.md`. No discrepancy was found in that finite-state conversion, but the upstream SK flow estimate and the other papers' proofs are not certified. No numerical computation or formal proof compilation was needed.

## Step 11 — final audit

Ran a short standard-library-only check via `OMP_NUM_THREADS=1 nice -n 15 python3 -S`: confirmed the required verdict prefix, exactly three reason lines, all theorem sections, spot-check section, explicit exponent, and paired display delimiters. Files: REPORT.md 533 bytes, VERIFY.md 17,437 bytes, LOG.md 7,919 bytes before this final entry. The priority-setting sandbox warning persisted; no heavy process was run. Rechecked the model/geometry, worst-start versus typical-start quantifier, and exponent comparison independently against the opened statements. Deliverables complete; all writes remained inside AV_T046.
