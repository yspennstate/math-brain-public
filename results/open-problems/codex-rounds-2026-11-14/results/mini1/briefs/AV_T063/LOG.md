# T063 verification log

Task: “Verify: has open problem T063 been settled by the OpenAI math release?” Work began 2026-11-14 about 21:02 Asia/Tbilisi.

## Step 1 — orientation and access

Read startup memory index, compute state (status ok, owner away), and mesh protocol. The task-specific restriction to writes inside this folder overrides global checklist, mesh, and brain mutations. No git, subagents, or external writes.

Commands: `nice -n 15 env OMP_NUM_THREADS=1 python3` with short read-only scripts. `nice` warns `Operation not permitted`; process-priority inspection with `ps` is sandbox denied. An attempted RLIMIT_AS adjustment was rejected before any file write. Keep programs small and single threaded; no heavy computation.

## Step 2 — primary-source discovery

Opened all three candidate folder listings through connected GitHub GET. Each has a `build/` directory. Guesses `build/paper.tex` returned 404, so inspect actual build listings next. Opened repository README.md, history.md, and lean/formalization.yaml. History records October 7 repairs to four Lipschitz/Ashkin–Teller manuscripts. Opened arXiv:2610.07454 abstract and author list. Opened Yan Ru Pei’s November 2026 PDF at https://hexagonmath.org/pdf/2611.00291v1: it reports a missing state-identification justification and claims to supply it conditionally on two OpenAI inputs. Opened the Latent Seminar six-vertex exposition; it explicitly disclaims complete independent verification. A Chinese exposition URL returned Cache miss. Exact source statements still pending.

## Step 3 — exact statements read and saved

Opened each actual `build/main.tex`, `build/sections/01-introduction.tex`, and candidate README.md using GitHub GET. Saved exact returned text under sources/candidate1–3, and repository README/history/formalization catalogue under sources/. Main theorem of candidate 1 claims every fixed 0<c<=2 in the prescribed iterated balanced-torus plane state, covariance multiplier 2/arccos(Delta). Candidates 2 and 3 have byte-identical main theorem blocks: triangular-lattice integer Lipschitz heights, x in [1/sqrt(2),1], zero boundary, implicit positive sigma(x). October 6 README identifies it as a revision supplying the annulus circuit proof. Opened community oai-math-revised candidate 1 page and arXiv:2603.06268 abstract/author list. Catalogue text search has no six-vertex or weighted-height title. Opened Pei’s PDF Section 1.3 and Corollary 1.6: conditional repair uses existence and free-energy minimality as inputs and does not assess the rest of the OpenAI proof. These findings do not certify any proof.

## Step 4 — follow-up and formalization searches

Web searches combined exact titles with arxiv, error, gap, refutation, and revision; no separate arXiv version of the three OpenAI candidates located. Opened repository `lean/README.md`, recursive Lean tree, and all-state issues endpoint (four entries, all release/maintenance pull requests). Opened AI Proved What episode 232 as exposition. Read candidate 1 Section 4 source to inspect the reported identification gap. The repository has no top-level docs directory in its root listing; README points to Lean documentation and catalogue instead. No complete independent verification or referee report located. Search absence is not proof none exists.

## Step 5 — deliverables saved before optional spot check

Wrote VERIFY.md with exact source theorem blocks for all three candidates, model/range/quantity/strength comparison, opened follow-ups, and a three-sentence replacement note. Wrote REPORT.md: SOLVED-CLAIMED, qualified by the prescribed balanced plane state and lack of full verification. The Lean recursive tree response was truncated; will inspect smaller OAI/docs trees rather than rely on absence in a truncated listing. Main statement is a plane-state claim and does not quantify over all Gibbs states. Now checking the central boundary-division/scalar-continuation lemma, which underlies the angular spectral construction.

## Step 7 — documentation scope

Opened untruncated lean/docs tree (245 entries; no 225.md or 232.md), lean/OAI directory, OAI.lean import entry point, and Comparator README. No candidate import found. Full OAI recursive tree also truncated, so reduced scope to Probability and MathematicalPhysics subtrees. Numerical script confirmed inherited nice 20, already below the requested nice 15 priority; the warning came from trying to add niceness past the allowed range. No priority escalation was attempted.

## Step 8 — spot check written

Completed untruncated Probability (13,245 entries) and MathematicalPhysics (6,790 entries) subtree name searches: no relevant six-vertex or Lipschitz-height development. Appended Spot check to VERIFY.md: derived the local invariant-line identity analytically from the printed R matrix and checked it independently on 16 tiny numerical cases. The common-radius Gram/spectral limiting passage is explicitly left unaudited. No proof-correctness judgment made. REPORT.md remains the required four-line verdict/reasons artifact.

Web opening of all three supplied GitHub folders returned Cache miss. Connected GitHub read tool successfully opened repository root listing. Web search queries: `site:github.com/openai/math "balanced" "six"`; `"Gaussian free field limits of weighted integer Lipschitz heights"`; `"OpenAI" "math" "six-vertex" 2026`. Found candidate abstracts, expositions, and a potentially relevant November follow-up titled “Closing the identification step in the GFF limit: Uniqueness of the zero-slope six-vertex phase for -1 <= Delta < 1/2”; these are leads, not yet verified findings.

## Step 6 — optional local algebra spot check
2026-11-14T21:08:17.096033+04:00 Ran `nice -n 15 env OMP_NUM_THREADS=1 python3` with standard-library 8-by-8 complex matrix arithmetic (no numerical packages). Inherited nice priority: 20. Checked the boundary-division lemma invariant-line identity G(u)(Phi tensor e)=r(u)(Phi tensor e) and the range of G(0), at four lambda values and four real/complex u values. All 16 samples passed; maximum residual 2.2242544315530013e-16. These finite tests do not prove the uniform chain-length bounds or infinite-volume spectral conclusions. Exact source saved in sources/candidate1/angular-plane.tex and finite-rows.tex.

## Step 9 — final audit
2026-11-14T21:10:06.595583+04:00 Verified all three theorem quotations equal the opened local source blocks exactly; checked the required REPORT verdict prefix and two reason lines; corrected display delimiters in Spot check. Independently rechecked Delta conversion, amplitude versus squared multiplier, and the distinction between a claimed solution and proof verification. Deliverables: VERIFY.md, REPORT.md, LOG.md, and source excerpts under sources/. No writes outside this folder, no git, no external posting.
