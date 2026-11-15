# Rows closest to a solution: starting rank

Task T-20261110-055. Written 10 Nov 2026 07:00 from `../frontier/PAPER_CANDIDATES.md` (scans to 7 Nov) and
`VERDICTS.tsv`. A row is here because a verified partial result of ours already stands on it; the row itself
is still open, which is why each stays in the list. Order is by how much of the row the partial result covers,
judged from the one-line summaries only. Read each row's dossier (`frontier.py brief TNNN`) and run
`brain.py recall` on its id before working it.

| rank | row | what stands | what is left for the row |
|---|---|---|---|
| off the list | T067 | Kesten-Stigum tight for q=3 Potts on every regular tree d>=2 (posted 30 Oct), q=4 on the binary tree (posted 7 Nov) | Read in full 10 Nov 09:05. The row's open part is NOT ours to claim: two public OpenAI preprints (github.com/openai/math, family 229: three states, 25 Sep 2026; four states, 5 Oct 2026; repository public since 6 Oct) state q=3 and q=4 at every regular degree and every Poisson mean, equality included. They are unrefereed and their Lean covers only the above-threshold direction. Our proofs are independent and later. The 24 Oct package (research-repo `research_pushes/2026-10-24-t067-*`) proves q=3 and q=4 for every finite-mean offspring law; its q=3 certificates were replayed exactly on 3 Nov and its q=4 traversals on 7 Nov (both modes pass, `12_cognitive_architecture/top10_7_10_agent/rank10_t067_q4_traversal/RESULT.txt`), so the earlier "UNRUN" note was stale. Verdict changed to REMOVE_SOLVED_BY_OTHERS. What is still a candidate new result: the finite-mean Galton-Watson case at q=3, which with the four-state cone of the OpenAI paper gives Formentin-Kulske Conjecture 2.13. Before a paper: the Prop. 6.1 ordering repair in the text, and an audit of the analytic chain from the two residual inequalities to the dichotomy (the 3 Nov review did not re-derive it). Neither posted paper cites the OpenAI preprints: to be added |
| off the list (already ours) | FK 2.13 | Formentin-Kulske Conjecture 2.13 (no reconstruction for q<=4 below the bound on every iid offspring tree). NOT NEW: this is the theorem of our public paper yspennstate/posterior-cones-reconstruction (24 Oct 2026, 16 pages; mirrored in math-brain-public papers/public and in the T067 release of 31 Oct). A second write-up posted by mistake on 10 Nov 10:53 (yspennstate/potts-reconstruction-galton-watson) was set private at 11:07 the same day. | one citation clause for Formentin-Kulske in the October paper (it does not cite them); nothing else |
| far (was 2) | T366 | Kaczmarz last iterate 1/k in the plane case | the general lemma. Moved down 10 Nov 08:43 after reading both row folders: route (B) has no dimension-free bound (its sup grows with each transverse dimension, 1.2638 to 1.2690 so far) and would give 2.25 at best, not 2; the residual route has no certificate; a split into a monotone and an orthogonal part fails (`../frontier/rows/T366/agent/NOTES.md`). Not near a solution |
| 3 | T249 | smallest NTK eigenvalue of a deep tanh net in the ordered phase, leading order | the negative half is reduced to an infinite-width bound; the positive half needs a trained-network statement |
| 4 | T362 | random reshuffling lower bound on one 1-D instance (posted) | the general condition-number rate |
| 5 | T346 | no base-classifier-independent certificate beyond 8.5 sigma sqrt(log) for any noise with bounded second moment | whether the row asks for more than this barrier |
| 6 | T084 | arboreal gas on K_n: all pairs of edges negatively correlated (posted) | general graphs |
| 7 | T021 | Han's Question 3.1 refuted (posted); FEI campaign active under another agent | the conjecture itself; do not duplicate the campaign |
| 8 | T180 | prophet secretary upper bound 0.72294 (posted) | the optimal constant |
| 9 | T417 | heavy-ball speedup on Gaussian least squares (prior art found, demoted) | nothing of ours to add yet |
| 10 | T383, T357, T336, T384 | verified partial results | each far from the row's statement |

Outside the two lists: P0355 (Aldous-Bandyopadhyay Conjecture 34, reduced and proved in the regular case) and
P0245 (Aldous-Fill Open Problem 6.30, proved at n=3 and certified at four states, 10 Nov memories) are close and
belong to the `P` pool, not to the top-200 rows.

Not yet done: a pass over `../frontier/BOARD.md` (252 lines) for rows marked narrowed with a short stated target,
and over `~/brain_workers/OPEN_PROBLEMS_200/`.
