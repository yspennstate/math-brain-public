VERDICT: PROVED finite binary-bridge swap invariance and conditional fair cluster signs for inhomogeneous weights c_v >= 1

The earlier result holds. Its reflection, insertion and entropy argument was independently re-derived; its unchanged script passed again; a separate all-edge enumeration reproduced both 2x2 partition polynomials. The five-minute literature check found no newer full-range GFF proof that could be certified.

The new result verifies one finite ingredient of the November uniqueness argument. In a finite face rectangle, take two independent six-vertex height functions with possibly different fixed boundary heights, but the same vertex weights a_v=b_v=1, c_v>=1. At a fixed integer level ell of D=(h2-h1)/2, independently open each saddle diagonal with probability

    1 - c_v^(-2).

A saddle has D=ell±1 with the same sign relative to ell on its two endpoints and D=ell on the perpendicular diagonal. Join nearest neighbours with D!=ell and open saddle bridges. Exchanging any union of components that avoid the boundary, with height shifts by ±2ell, preserves the augmented Gibbs law. Conditional on the height sum, |D-ell| and the bridges, all interior component signs are independent and fair. [PROOF.md](PROOF.md) gives every step, including the direct treatment of c_v=1.

This supplies a binary marginal of the geometric-residual swap in Lemmas 3.2–3.5 of Yan Ru Pei's [November preprint](https://hexagonmath.org/pdf/2611.00291v1), identifier hexagon:2611.00291v1, not an arXiv identifier. It extends the finite formulation to inhomogeneous weights and the weight-one endpoint. Global novelty is not claimed. Corollary 1.3 and its infinite-volume dependencies are still not certified here; neither uniqueness nor a GFF limit follows from this finite theorem alone.

[check_binary_swaps.py](check_binary_swaps.py) passed 5,184 local admissibility checks, 4,976 exact rational mass checks, 10,368 nonzero-level checks, and 51,660 whole-domain swap images across 26 cases. It enumerated 37,452 augmented states and checked all 32,184 conditional sign fibers. Tests include unequal boundaries, bridges at the collar, mixed weights 1,3/2,2,3, and levels -2 and 3. Runtime was 2.573 seconds; peak RSS 49,987,584 bytes; effective nice 20. All counts and outputs are in [LOG.md](LOG.md).

Commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_binary_swaps.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T063/check_two_flux.py
```

Audit: the factor c_v^(-2) was derived both from the changed vertex weights and from an independent geometric-series calculation. A separate nonrecursive enumerator confirmed the domain filling counts. Omitting bridges fails explicitly: a single-block swap changes pair weight from c^2 to one. The closed-bridge probability supplies exactly the missing factor. This is not a counterexample to Pei's augmented construction.

What failed or remains uncertain: a shell PDF download failed with DNS error; the web tool opened the paper. The nice launcher could not increase an already inherited nice value of 20. No mathematical checks failed. The bridge theorem is at one fixed level; passing to the all-level fold, infinite-volume Gibbs law, and roughness still requires proof. The formula gives a negative opening probability for c_v<1 and establishes nothing there. No full uniqueness audit was completed.

Next worker: audit Pei's Lemma 4.4, the local reconstruction of the fold, then its entropy consequence in Lemma 4.5. Keep the original all-level residual coupling explicit; the fixed-level binary result alone does not justify that passage. The earlier torus-minimisation result remains available if uniqueness is eventually certified.

Only this folder was written. No git, subagents, external messages or publication were used.

Task: “take the NEXT checkable step on this problem, building on that work” (T063); received approximately 07:48 Asia/Tbilisi, 15 November 2026.
