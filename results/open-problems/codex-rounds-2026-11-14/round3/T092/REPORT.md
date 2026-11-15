VERDICT: PROVED a necessary orbit-count bound for finite-stage approximations near an invariant observable

The earlier report holds: the external claim has exactly the scope of
T092, and the named Lean solution has a proof body. Neither observation
validates its construction. The bounded literature check found no newly
verified resolution. Banach's finite-measure problem is not resolved by
this session.

The new mathematical result is the following. If U is unitary, g has an
orthonormal bilateral orbit, `A=||h||>0`, and a Laurent polynomial P
approximates h to error `ε<A`, then

\[
 \#\operatorname{supp}P\ge
       \frac{A^2-\varepsilon^2}{A\|Uh-h\|}.
\]

A zero denominator makes such an approximation impossible. Completeness
of the orbit is unnecessary. The proof and an independent Fourier
derivation are in [PROOF.md](PROOF.md). The coefficient inequality used
in the proof has optimal universal constant one; this is checked using
geometric sequences, with their sums evaluated two ways. No claim of
historical novelty for the underlying sequence inequality is made.

For a map R uniformly δ-close to a twist fixing the slow coordinate u,
take `h=sin(2 pi u)`. Any approximation with error at most half its norm,
using an orthonormal orbit for R, requires

\[
 \#\operatorname{supp}P\ge\frac{3}{8\sqrt2\,\pi\delta}.
\]

This gives a checkable constraint on the claimed finite construction:
polynomial support must diverge as physical perturbations shrink. It
does not refute that construction, whose polynomials are unrestricted.

The source audit goes beyond the earlier top-level inspection. It traces
the basis through the diagonal to `Stages.exists_one_stage`, then to
controlled prediction and whitening. The opened sources and precise
locations are in [CLAIM_AUDIT.md](CLAIM_AUDIT.md). The full dependency
closure and actual construction remain unchecked.

Commands and checks:

- Read-only `cat` of the earlier REPORT.md, LOG.md and claim notice;
  directory inspection confirmed there was no earlier PROOF.md or script.
- Web searches for the exact title, 2026 Banach/simple-Lebesgue results,
  and errors or reviews; primary-source `open` and `find` calls listed
  in [LOG.md](LOG.md) and CLAIM_AUDIT.md.
- Read the startup memory and compute-state file. Tiny shell reads used
  `env OMP_NUM_THREADS=1 nice -n 15`; the sandbox denied the priority
  adjustment. No computation script, Lean build, git or external write
  was run. Files were saved with apply_patch.
- Symbolic checks covered both signs of the orbit, proper cyclic
  subspaces, sparse polynomials, zero residual, and changing coordinate
  charts. The torus constant was re-derived after normalizing h.

What failed or remains uncertain: source inspection supplied no proof
certificate, and the finite-stage theorem has not been independently
proved or disproved. The count bound alone gives no contradiction,
because its required growth is allowed by the theorem. It gives no
upper bound on the polynomial support produced by that construction.

Next worker: audit the centered block estimates feeding
`actual_controlled_tagged_prediction` in ControlledBlocks, especially the
simultaneous prediction error and Hellinger-loss estimates. Compare their
eventual Laurent support with the necessary bound above in the fixed
twist/slow-coordinate test. A sufficiently large support passes this
necessary check but does not establish validity. Do not spend another
session merely locating the top-level theorem.

Task: “take the NEXT checkable step on this problem, building on that
work” — received 2026-11-15 01:20 +04 (Asia/Tbilisi).
