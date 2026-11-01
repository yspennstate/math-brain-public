# The top-400 frontier board, October 2026

Work on rows of the frontier board: open questions in probability (T001-T222) and in the theory of deep learning
(T223-T422). Each folder states its own scope. A proved result for a special case is not the same as settling a whole
row, and the folders say which one they have.

| Folder | Contents |
|---|---|
| `rows/` | Twenty-six rows whose result passed an independent check, from T039 to T417. Each holds the row's dossier, the scripts behind every numerical claim with their outputs, and the audit or referee report. The table in `rows/README.md` gives the question, the result and the checks for each. |
| `2026-10-10-two-agents-cross-family-referee/` | A test of two agents working through the brain: 48 proof audits, each clean or with one planted fault, under eight arms. A second copy of the same model added nothing; a referee from another model family did. |
| `2026-10-22-t353-independent-review-codex/` | An independent review and replay of the refutation of Conjecture 3.2 of Chua et al. (arXiv:2403.17673) on shuffled DP-SGD, with a short analytic proof of the main theorem and the check scripts. |
| `2026-10-23-codex30-frontier/` | Thirty agents on the deep-learning rows, mostly T336 (quantitative Gaussian-process posterior approximation by transformers and pretraining). The claim register, the directions tried and dropped, all thirty reports and the checks. |
| `2026-10-23-t228-closure-30-agents/` | The T228 certificate: an explicit nonlinear SGD model with a unique stationary law and an exact power tail of index between one and two. A 13-page proof, the scoped extensions and a package audit of 625 checks. |
| `2026-10-24-open-frontier-continuation/` | The continuation on T384 (training with stable weights: a scalar training-limit theorem and its extension to coordinate inputs), with partial results on T084, T262, T268, T336 and T364. |

Several of these rows became papers with their own repositories; `../../papers/README.md` lists them.
