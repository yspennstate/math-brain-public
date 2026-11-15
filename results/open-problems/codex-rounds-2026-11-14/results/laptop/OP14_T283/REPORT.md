VERDICT: PROVED sharp edge-uniformity threshold for the random alternating-form construction

For nonzero evaluation vectors of binary linear girth g, the graph obtained from an independent uniform alternating bilinear form has uniform marginals on every set of at most g-2 edges, and fails uniformity on some set of g-1 edges. This remains the exact threshold after uniform vertex permutation and independent edge resampling at every rate below one. If all evaluation vectors are independent, the whole graph is uniform.

Consequently, L-wise independent evaluation vectors suffice for uniform marginals through L-1 edges. This improves the sufficient floor(L/2) bound in Songtao Mao's Proposition 2.6, while keeping the construction unchanged. For a target degree D, the exact requirement in this construction is nonzero vectors and no dependence of size at most D+1, rather than the earlier sufficient independence through 2D vectors. Full details, including sharp examples, are in [PROOF.md](PROOF.md).

The proof also gives a precise obstruction to removing advice by simply randomizing the evaluation seed. Conditional on the seed and vertex permutation, every graph parity expectation is either zero or one. Averaging cannot cancel a bad seed's nonzero Fourier coefficient. Exact D-wise uniformity therefore requires the vector-girth condition almost surely. This obstruction assumes that the alternating form is uniform and independent of the seed; it does not exclude other graph constructions or correlated sampling strategies.

## Verification

Run from this directory:

```powershell
[System.Diagnostics.Process]::GetCurrentProcess().PriorityClass = 'BelowNormal'
$env:OMP_NUM_THREADS='1'
$env:OPENBLAS_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
$env:PYTHONDONTWRITEBYTECODE='1'
python -B .\verify_threshold.py
```

Final output: PASS; 5,884 vector configurations; 5.425 seconds. Peak working set: 25,640,960 bytes; peak private commit: 17,240,064 bytes; Windows priority class: 16384 (BelowNormal). The program uses the Python standard library and no worker threads. Exact data are in [verification.json](verification.json).

The audit compared subset-XOR enumeration against actual enumeration of alternating matrices followed by an independent shortest-syndrome dynamic program. It covered all distinct nonzero vector families with 2<=n<=5 in dimensions at most four, and all nonzero multisets with 2<=n<=5 in dimensions at most three. It also checked the rank inequality on every nonempty labeled graph on two through six vertices. Separate combinatorial formulas checked all configuration counts, independent-family counts, and the count 168 of five-element circuits in dimension four.

For vectors (1,2,3,4) in binary dimension three, independent permutation counting and direct form evaluation both gave a two-edge-star Fourier coefficient 1/4. Enumerating noise masks and fresh bits at resampling rate 1/2 gave 1/16, independently confirming the degree-two survival multiplier. The crucial rank bound was also derived twice in the proof: using an isotropic quotient, and using rank loss under two matrix products.

## What failed, limitations, and next step

The unconditioned random-seed shortcut fails the exact marginal requirement whenever it assigns positive probability to short circuits. A zero evaluation vector already obstructs single-edge uniformity; the theorem explicitly treats this exception. The endpoint resampling rate one is fully uniform and is excluded from the sharp-failure assertion.

No polynomial-time uniform sampler was constructed. The factor improvement does not change the polylogarithmic exponent or solve good-seed selection. The proof is self-contained linear algebra; no claim of literature novelty for the underlying girth identity is made. Exhaustive computations audit small cases, not the asymptotic sampler or Mao's separate null-rank theorem.

Next work should seek a polynomial-time construction or an exactly supported sampler for nonzero evaluation vectors with girth at least D+2, within a low-degree evaluation map that preserves the noisy rank test. An efficiently decidable sufficient certificate for this weaker girth target would also be useful. Accepting almost all candidate seeds without certifying exact support is insufficient in the independent alternating-form framework.

The bounded literature search found no resolution of the whole stated problem. Mao's latest posted revision still explicitly leaves the uniform-sampler question open in Section 4. No SOLVED_ELSEWHERE.md was created, and no general-conjecture replacement or integrator approval was claimed.

Papers actually opened:

- Songtao Mao, *The Polynomial-Time Low-Degree Conjecture is False*, arXiv:2607.20318v2, revised 28 October 2026, Proposition 2.6 and Section 4. https://arxiv.org/html/2607.20318v2
- Rares-Darius Buhai, Jun-Ting Hsieh, Aayush Jain, Pravesh K. Kothari, *The Quasi-Polynomial Low-Degree Conjecture is False*, arXiv:2505.17360. https://arxiv.org/abs/2505.17360

Searches, intermediate outputs, and the audit history are in [LOG.md](LOG.md).
