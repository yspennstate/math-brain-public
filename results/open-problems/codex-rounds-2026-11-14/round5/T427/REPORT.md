VERDICT: PROVED the quantitative equal-mass square/torus semidiscrete-to-smoothing reduction by an independent Jacobian argument

The round 4 subdivision result survives rechecking. Its mass rescaling, repair construction, and dominant rate were re-derived; its exact exponent script also passed. The brief literature check found no change beyond Yunzong Xu's already recorded [arXiv:2610.40509v1](https://arxiv.org/abs/2610.40509v1), *Random matching between distinct distributions in two dimensions*.

New beyond round 4: [PROOF.md](PROOF.md) supplies the requested independent audit of the flat equal-mass case of Proposition 3.1. For the square or flat torus, it proves

\[
n\mathbb E\bigl[W_2^2(dx,\nu_n)-W_2^2(P_t\nu_n,\nu_n)\bigr]
=2F_\Omega(t)-F_\Omega(2t)
+O\!\left(\sqrt{\frac{\log(en)^3}{nt}}\right)
\]

when \(0<t\le1/2\) and \(nt\ge C\log(en)\). It also proves an expected absolute remainder bound before averaging the random spectral correction. At the earlier subdivision time \(t=n^{-5/6}\), the error is \(O(n^{-1/12}\log(en)^{3/2})\).

The proof uses the map \(S=I-\nabla f\). Its exact source density differs from \(1-\Delta f\) by \(\det D^2f=\tfrac12\operatorname{div}((\operatorname{cof}D^2f)\nabla f)\). This yields the small transport correction directly. The proof checks face preservation and onto for the square, all lattice lifts for the torus, Hessian concentration from explicit eigenfunctions, and the rough cost bound without assuming a matching asymptotic. This verifies an existing claimed reduction; it does not claim a new matching theorem or rate beyond that preprint.

Commands, from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T427/check_scaling.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_reduction.py
```

Both completed successfully. The new script checks the determinant and flux identities by exact rational polynomial arithmetic, tests 36 square and 36 torus pairs including seam crossings and cut-locus ties, and verifies the spectral expectation by exhaustive enumeration for sample sizes 1, 2, and 3. Its run took 0.015 seconds and 14,139,392 bytes peak RSS. Actual niceness was 20 despite the wrapper's priority-change warning. [LOG.md](LOG.md) records commands, output, and the adversarial audit.

What failed: two initial verifier launches stopped before mathematics because this platform rejected an optional RLIMIT_DATA setting. A diagnostic disproved the initial guess that an inherited lower limit caused it. Removing that optional setting allowed the bounded calculation to run; the CPU limit and priority guard remained. No mathematical assertion failed.

Limits and uncertainty: no numerical value of the universal equal-mass constant or \(c_\square\) is obtained. This audit covers the flat equal-mass reduction, not arbitrary densities, curved surfaces, or the remaining convergence proof. All new files stay in this folder; earlier folders were read only.

Next worker: independently audit Appendix C.4 and Section 4.2 of Xu's paper. In particular, check de-randomization of the binomial cell count at the rescaled heat time, the passage from subdivision to deterministic sample sizes, and the two-scale convergence lemma. Round 4 now supplies subdivision, and this folder supplies its required source-change/time comparison estimate; proving convergence still requires that separate step.

Task: “take the NEXT checkable step on this problem, building on that work.” First saved session clock: 15 November 2026, 09:17:31 Asia/Tbilisi (05:17:31 UTC).
