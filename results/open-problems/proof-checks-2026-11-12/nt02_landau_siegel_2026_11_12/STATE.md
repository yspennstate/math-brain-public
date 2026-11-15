# NT02 state (12 Nov 2026)

Done: full reading of the original proof (9 pages) and of Kerr's variant (6 pages); the openings, statements and
closing remarks of Banks and Guo. Note: `NT02_CHECK.md`. Tests: `nt02_check.py` -> `nt02_check.out`,
`nt02_check2.py` -> `nt02_check2.out`. Searches: `lit/search/s1.xml`, `s2.xml`, `s3.xml`.

Kept locally, not in the repository: the OpenAI preprint (`lit/openai/main.pdf`, `main.txt`, `main_c.txt`,
`folder_tree.json`) and the three arXiv papers (`lit/2610.21099`, `lit/2610.30476`, `lit/2610.15483`).

Source addresses:
- OpenAI preprint: https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf
  (in this folder the PDF is `paper.pdf`)
- Banks: https://arxiv.org/abs/2610.15483 ; Kerr: https://arxiv.org/abs/2610.21099 ; Guo: https://arxiv.org/abs/2610.30476
- Not fetched: Banks, arXiv 2610.31402 (base field, effective Brauer-Siegel); Kimura, arXiv 2610.21511 (class number
  at most 2000); Tao's blog post of 19 Oct 2026; the Green and van Dijk notes cited by Guo.

Not done: a line-by-line check of Banks's explicit constants (0.003) and of Guo's elementary route (1/100); a
reading of Masser's 1981 paper, which Kerr's variant quotes for its zero estimate (tested here for N up to 6).

If the row is taken up again: the two steps that carry the weight are Lemma 3 (interpolation on the projected box)
and Lemma 7 (divisibility by the Frobenius congruence). The divisibility test stops at N = 3; N = 4 needs about
2,200 determinants of size 256 and belongs on a Mac mini, not the laptop.

Lean: `lean/formalization.yaml` of openai/math at commit 1581d4cb lists the theorem as formalized, declaration
`OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap` in
`lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean` (comparator configuration
`ComparatorChallenges/SiegelZeros.json`). The statement was read and matches Theorem 1. Not compiled here. Local
copies of the two files: `lit/lean/` (not in the repository).

Lead for the list: openai/math also holds `The-Quasi-Riemann-Hypothesis-September-30-2026` and
`...-October-5-2026` (a zero-free half-plane Re s > 7/8 is claimed). Unread. Row NT01 should be checked against it.
