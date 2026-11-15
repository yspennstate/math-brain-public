# T197 state (12 Nov 2026)

Done: full reading of the original proof. Note: `T197_CHECK.md`. Tests: `t197_check.py` -> `t197_check.out`.
Searches: `lit/search/s1.xml`, `s2.xml`, `s3.xml`.

Kept locally, not in the repository: the OpenAI preprint (`lit/openai/main.pdf`, `main.txt`, `main_c.txt`), the
Shlyakhtenko paper (`lit/2610.19590/`), `lit/openai/folder_tree.json`.

Source addresses:
- OpenAI preprint: https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/An-isomorphism-of-the-free-group-factors-September-23-2026.pdf
  (in this folder the PDF carries the folder's name, not `main.pdf`)
- Shlyakhtenko: https://arxiv.org/abs/2610.19590

Not done: a line-by-line check of Shlyakhtenko's Sections 2-4 (the derivation and the automorphism group built from
it); a simulation of the flow of Section 3.

If the row is taken up again: the step that carries the most weight is Lemma 3.2 together with Lemma 3.4 (the flow
preserves every moment). A matrix-model test would integrate X_j' = i H_j(X) X_j for Haar matrices and watch the
mixed moments of (X(t), S) against those of (X(0), S); they should agree up to the 1/n error of the model.
