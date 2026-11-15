VERDICT: PROVED local reconstruction and a perimeter free-energy bound for the all-level geometric-residual fold

The earlier finite binary-bridge swap theorem holds. Its weight cancellation was independently re-derived, and its unchanged script passed again: 5,184 local admissibility checks, 4,976 exact mass checks, 32,184 conditional sign fibers and 51,660 domain swap images. The five-minute literature check found the same updates already recorded by earlier workers; no newer full-range GFF solution was certified.

The new result checks the next step named by round 5: Lemmas 4.4–4.5 of Yan Ru Pei, [*Closing the identification step in the GFF limit: Uniqueness of the zero-slope six-vertex phase for -1 <= Delta < 1/2*](https://hexagonmath.org/pdf/2611.00291v1), November 2026, hexagon:2611.00291v1 (not an arXiv identifier). With M≥2 and infinite minus clusters at every band level, the original and folded local data determine each other after adding boundary band labels and one clipped difference. The proof retains the same geometric residual at every level, proves both reconstruction directions, and includes the countable-alphabet entropy justification. It allows inhomogeneous c_v>1. The reconstruction is already asserted in that preprint; global novelty is not claimed.

For a face rectangle with boundary size b and nearest-neighbour diameter δ, the clipping threshold can be reduced to L=M+δ+1. A boundary spanning tree gives at most

    K=2*3^(b-1)*(2M+2δ+3)

boundary data values. For any law satisfying the deterministic hypotheses and finite local residual means,

    |FE(image)-FE(original)| <= log K.

This sharpens the cited finite-box boundary cost and tends to zero per unit area on growing squares. [PROOF.md](PROOF.md) gives the complete proof and an equivalent finite wired formulation. It establishes neither the hypotheses for an infinite-volume Gibbs state nor uniqueness or GFF convergence.

[check_fold.py](check_fold.py) passed 46,882 exact fold/reconstruction cases, including 41,472 exhaustive two-by-two cases, 32 interior-band cases exceeding every boundary band, 996 saturated cases of both signs, 5,400 relative-shift checks, and nine restrictions of actual infinite affine-height examples. All 140,840 diagonal residual updates preserve the invariant exponent exactly. A separate finite distribution with 11,520 records checks the free-energy identity two ways; both give 0.128141507453, below log(594). Runtime was 3.058 seconds and peak RSS 27,492,352 bytes, one thread at effective nice 20.

Commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 -u check_fold.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r5/briefs/T063/check_binary_swaps.py
```

What failed: the first reverse decoder stopped at the largest boundary band. A larger-box test caught an interior band above that value. The corrected decoder continues through max(boundary band)+diameter, and an explicit three-by-three mountain is now a regression test. This was an implementation error, not a counterexample to Pei's induction. The priority launcher warns because inherited niceness is already 20. All corrected checks pass.

What remains uncertain: this does not certify the rest of Pei's uniqueness proof or the September OpenAI GFF argument. The all-level construction requires M≥2 and its stated infinite-cluster hypothesis. The geometric residual law is not normalizable at c_v=1; the earlier binary endpoint result does not resolve that issue. No conclusion for c_v<1 follows. The entropy bound explicitly assumes finite residual means.

Next worker: audit Lemma 4.6's pressure normalization, then Proposition 4.7 and the passage from zero relative-entropy density to independent geometric residuals in Lemma 4.8. The image Gibbs argument in Lemma 4.9 remains separate. Keep the infinite-cluster hypothesis explicit; local reconstruction alone does not establish the image's equilibrium or Gibbs properties.

All writes stayed in this folder. Earlier folders were read only. No git, subagents, external messages, accounts or publication were used. [LOG.md](LOG.md) records the search, derivations, failed first test, correction and final outputs.

Task: “take the NEXT checkable step on this problem, building on that work” (T063); received approximately 10:19 Asia/Tbilisi, 15 November 2026.
