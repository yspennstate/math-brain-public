VERDICT: COMPUTED exact Fourier concentration curves for every DNF on at most four variables

Enumerated all 65,536 four-variable Boolean functions. For every function, computed its minimum DNF term count and all sixteen signed Fourier coefficients in exact integer arithmetic. The resulting data settle the finite concentration problem at every error tolerance, with explicit extremizers.

For term budgets two and three the worst squared-error tails after retaining m=0,...,16 coefficients are identical:

```text
[256,220,184,148,112,80,64,48,32,28,24,20,16,12,8,4,0] / 256.
```

For every term budget at least four, the exact worst tail is `(16-m)/16`, attained by a four-term DNF with a flat Fourier spectrum. Thus the exact sparsity at any epsilon is the least m whose listed tail is at most epsilon.

As a corollary, for n<=4, t>=2, and 0<epsilon<=1/2, the bound `t^(2 log_2(1/epsilon))` holds. The constant 2 is optimal in this finite setting: the OR of two disjoint two-literal conjunctions needs four coefficients at epsilon=1/2. The proof, including the integer inequalities establishing the corollary, is in `PROOF.md`. The complete curves also cover epsilon>1/2; the constant-2 corollary does not.

Commands, run from this folder:

```sh
OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 compute_four_variable.py > computation_output.txt 2>&1
OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_saved_data.py > audit_output.txt 2>&1
```

Both passed. Enumeration took 1.789 seconds with peak RSS 26.516 MiB; the independent saved-data audit took 1.264 seconds with peak RSS 19.781 MiB. Both ran at actual nice 20 with one thread. macOS rejected the optional data-allocation limit; the scripts used small fixed arrays, and their measured peaks stayed far below 1 GB. The initial launch failed before enumeration while setting that limit; the failure and subsequent correction are recorded in `LOG.md`.

Checks completed:

- All 65,536 minimum term counts agree between union shortest paths and independent prime-implicant set cover, with overlapping terms allowed.
- Every Fourier vector agrees between the integer Walsh transform, a truth-set intersection identity, and a separate audit using explicit character products.
- Parseval holds for every function. All 153 envelope entries and witness DNFs were independently reconstructed and evaluated.
- The four-variable maximum minimum-DNF size of eight was also proved directly by pairing assignments; parity attains it.
- Named extremizers were re-derived algebraically in `PROOF.md`.
- A deliberate attempt to extend the constant-2 corollary to epsilon>1/2 failed at epsilon=27/32. This is recorded explicitly and is not a counterexample to Mansour's conjecture.

Data: `functions.csv` contains all function records; `tail_envelope.csv` contains exact tails and witness DNFs; `spectral_types.csv` and `spectral_types_by_terms.csv` contain spectral multiplicities. `summary.json` gives counts, timings, and hashes. The two output text files preserve the commands' complete output.

The literature check took under ten minutes and found no later resolution or substantial improvement to the general bound in the brief. Opened primary papers include Victor Lecomte and Li-Yang Tan, [arXiv:2109.04525](https://arxiv.org/abs/2109.04525); Adam Klivans, Homin Lee, and Andrew Wan, [ECCC TR10-023, revision 3](https://eccc.weizmann.ac.il/report/2010/023/); and Mohsen Heidari and Roni Khardon, [arXiv:2506.01075, revised 2026](https://arxiv.org/abs/2506.01075). The latter studies non-product distributions and does not report the desired general DNF concentration result. Further opened sources and search details are in `LOG.md`. This search cannot certify that no later result exists.

No asymptotic advance or literature priority is claimed. The upper envelope for term budgets two and three depends on exhaustive computation, rather than a structural classification proof. No extension beyond four relevant variables was established.

Next worker: give a structural proof of the two-/three-term envelope, or enumerate five-variable DNFs with at most three terms rather than all five-variable Boolean functions. The change of extremizer at m=5 and m=8 shows that one candidate family cannot describe the whole finite concentration curve. Preserve exact arithmetic and the independent overlap-aware cover check.

Task: “push this problem forward by one checkable piece” — 2026-11-14, 22:02 Asia/Tbilisi.
