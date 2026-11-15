# Claimed solution located; independent verification incomplete

Reference: **OpenAI**, *A smooth three-torus diffeomorphism with simple
Lebesgue spectrum*, September 23, 2026, OpenAI Math Release preprint.

- [Manuscript and citation](https://github.com/openai/math/blob/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/README.md)
- [Introductory theorem, directly opened](https://raw.githubusercontent.com/openai/math/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/build/sections/01-introduction.tex)
- [PDF location](https://github.com/openai/math/blob/main/preprints/A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026/paper.pdf)

ArXiv id: none located. The primary citation uses
`OAI:A-smooth-three-torus-diffeomorphism-with-simple-Lebesgue-spectrum-September-23-2026`.
That is a repository identifier, not an arXiv identifier.

The main theorem claims a smooth diffeomorphism of the three-torus preserving
normalized volume, with a real mean-zero observable whose integer iterates
form an orthonormal basis of the entire complex mean-zero L² space. If
valid, this answers precisely the finite-measure question posed in T092.

The [scope note](https://raw.githubusercontent.com/openai/math/main/lean/docs/144.md)
claims a formalization. Its
[comparator configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/ThreeTorus.json)
points to a
[separate solution file](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Dynamics/ThreeTorus/Main.lean),
which was opened. Its top-level theorem contains a proof body. The challenge
file's `sorry` is not the solution artifact.

No Lean replay or full dependency audit was performed. No independent
mathematical validation was established in the bounded search. This notice
records an exact matching claim, not a certified resolution.
