# Partial literature update; the whole stated problem is not settled here

Search date: 2026-11-14, approximately 21:16–21:21 Asia/Tbilisi. No full arbitrary-field resolution was found in this bounded search.

## Zero field: a substantially stronger claim than the supplied status

**OpenAI**, *A spectral gap throughout the high-temperature Sherrington–Kirkpatrick phase*, September 24, 2026. OpenAI mathematics release; no arXiv id is supplied in its original citation entry.

- [Original manuscript hosting page](https://github.com/openai/math/blob/main/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/main.pdf).
- [Original author/date/citation README](https://raw.githubusercontent.com/openai/math/main/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/README.md).

The claim is a positive dimension-independent spectral gap for rate-one-per-site heat-bath dynamics, with probability tending to one, for every fixed 0<β<1 in the **zero-field Gaussian SK model**. In discrete uniform-site updates this is a gap of order 1/n. This is a substantial special-case advance, not a theorem covering arbitrary external fields.

Access qualification: the original hosting page and citation README were opened, but the web tool could not extract the PDF body; shell downloading was unavailable. The statement above is corroborated in the full primary paper below, whose discussion explicitly calls these results claims and describes the proposed proof. The long spectral-gap proof and any formalization were not audited in this session. No claim of independently verified correctness is made.

**Hang Du, Brice Huang, Sidhanth Mohanty, Amit Rajaraman**, *Sampling from the Sherrington–Kirkpatrick Model up to Criticality*, [arXiv:2610.17717v1](https://arxiv.org/html/2610.17717v1), October 13, 2026. Abstract page and full HTML opened. Section 1.2, “Concurrent work by OpenAI,” reports the zero-field gap and worst-start cutoff claims and discusses the gap argument. Their own Theorem 1.1 proves inverse-polynomial total-variation accuracy using simulated annealing. It does not prove worst-start mixing of fixed-temperature Glauber dynamics with arbitrary fields.

## A further field special case omitted from the supplied status

**Afonso S. Bandeira, Ahmed El Alaoui, Almut Rödder**, *Mixing of Glauber Dynamics on High Overlap Gibbs Measures*, [arXiv:2607.06813](https://arxiv.org/abs/2607.06813), July 7, 2026. Original arXiv abstract opened. It states that for every fixed finite β there is an external-field strength θ independent of n for which SK Glauber dynamics mixes in polynomial time with high probability. This is a sufficiently strong-field regime, not all fields. Only the abstract was checked.

## Clarification of the stated near-1/2 result

**Mathews Boban, Anqi Li, Shayan Oveis Gharan**, *Rank-1-perturbed trickledown theorems: Mixing time of Glauber dynamics for the Sherrington-Kirkpatrick model up to β≤1/2+ε*, [arXiv:2609.13138v1](https://arxiv.org/html/2609.13138v1). Abstract page and full HTML opened. The model in equation (5) has no external field. Theorem 1.5 uses β<1/2+ε with an absolute ε≥5×10⁻⁵; Corollary 1.6 gives gap Ω(1/n) and O(n²) mixing. Thus the paper's main SK theorem is explicitly zero field.

## What remains

The bounded search did not locate a theorem proving the original claim uniformly for arbitrary external fields throughout β<1. The mathematical result in PROOF.md addresses an obstruction to extending a zero-field theorem by a general field-monotonicity comparison. It is independent of all the recent claims above.
