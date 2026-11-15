# T189 state (12 Nov 2026)

Done as a partial check. Note: `T189_CHECK.md`. Tests: `t189_check.py` -> `t189_check.out`.
Searches: `lit/search/s1.xml`, `lit/search/s2.xml`.

Kept locally, not in the repository: the OpenAI preprint (`lit/openai/main.pdf`, `main.txt`), the Liu-Meng paper
(`lit/2610.26803/`), and the file lists of the openai/math repository (`lit/openai/preprints_list.txt`, 749 preprint
folders; `root_tree.json`, `preprints_tree.json`).

Source addresses:
- OpenAI preprint: https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-Fully-Polynomial-Randomized-Approximation-Scheme-for-Perfect-Matchings-in-General-Graphs-September-23-2026/main.pdf
- Liu-Meng: https://arxiv.org/abs/2610.26803

Not done: a line-by-line check of the proof of Theorem 2.1 (Liu-Meng Sections 2.2-2.4); Appendix A; the original
45-page proof beyond the start of its Section 2.3.

If the row is taken up again: the place to spend time is Section 2.4, the cell comparisons (2.17) and the claim that
each output pair (M, Q) has at most (10n)^60 occurrences. A direct test would enumerate the occurrences on K_8 or
K_10 for one ultrametric and count them per output pair.
