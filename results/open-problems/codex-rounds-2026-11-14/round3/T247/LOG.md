# T247 session log

Task: “take the NEXT checkable step on this problem, building on that work” — received 15 November 2026, 03:34 Asia/Tbilisi (14 November 23:34 UTC).

## Orientation and bounded literature check

Read the earlier REPORT.md, LOG.md, PROOF.md, check_moments.py and LITERATURE.md without modifying that folder. Read startup memory/navigation and compute state. Compute status warn, mode owner_away_open. All numerical programs will run single-threaded at niceness at least 15, with a short timeout and below 1 GiB RSS. The task-specific instruction to write only here overrides the global mesh/checklist/brain writes; those commands are not run because they mutate external stores. No git or subagents.

Web search began at 23:34 UTC. Opened arXiv pages 1711.04735, 2103.13466, 2503.07872; the Collins–Hayase PDF; and the PMLR 2026 Haas et al. page. Searches included deep neural network Jacobian orthogonal joint depth width dynamical isometry 2026, Collins Hayase Pastur Slavin neural network Jacobian joint depth width limit, and dynamical isometry growing depth theorem tanh. No new resolution of the nonlinear joint-limit question was verified. Hanin–Jiang concerns independent i.i.d.-entry products on a depth-root scale; Haas et al. concerns fixed-gates Lyapunov behavior. Stopped this literature check within five minutes. Details and links will be in LITERATURE.md.

## Earlier-result recheck planned

Independently integrate the one-layer fourth-order expressions for arbitrary diagonal gates and an arbitrary symmetric matrix, using exact sphere monomials rather than the old script. Then iterate the resulting rational two-trace map and compare to the previous product formula. Do not execute the old script in its original folder: it writes results.json there.

## Independent recheck completed

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 recheck_earlier.py > recheck_output.txt 2>&1
```

Exit 0. Output: 20 exact rational invariant-tensor product checks passed. Earlier main claim holds, including n=1, empty depth, zero and inhomogeneous variances. This derivation uses E B_ij B_kl = a delta_ij delta_kl + b(delta_ik delta_jl + delta_il delta_jk), determining a,b from the two trace invariants, rather than importing the previous recurrence. The niceness warning also occurred previously; inherited niceness is 20, checked by the script.

## Chosen extension, before derivation

Derive the exact conditional first two trace identities for genuine orthogonal-network derivative gates, conditioned on the current forward vector and prior Gram matrix. Also derive the leading small-q error relative to independent gates. This is the missing one-layer lemma requested by the earlier report. The aim is an exact formula at finite n, plus a dimension-uniform Taylor remainder, rather than an unproved accumulated joint-limit assertion. Gate coordinates need not be independent; the input-aligned invariants must be retained.

Method: condition a Haar O on u=Oe, where e is the unit forward vector. The residual rotation is Haar on the (n-1)-dimensional perpendicular space. Decompose X into its scalar, cross-vector and perpendicular blocks. Their first two conditional moments can be computed by invariance. This avoids any freeness or Gaussian replacement.

## Derivation saved

Saved PROOF.md with exact formulas for E Tr X', E Tr((X')^2), and E(Tr X')^2 conditional on u=Oe, valid for arbitrary nonnegative diagonal A(u), n>=3. The previous Gram matrix contributes the additional directional invariants alpha=e^T X e and gamma=e^T X^2 e. For the spherically mean-normalized tanh squared derivative, derived the exact first-trace correction -kappa_n(q)(n alpha-T), with 0<=kappa_n(q)<=8q/(n+2) for q<=1/4. Its linear term is 4q/(n+2).

Derived the two second-trace linear corrections -8q(n gamma-Q)/(n+2) and -8qT(n alpha-T)/(n+2), and dimension-uniform absolute Taylor remainder bounds 1344q^2 Q and 1344q^2 T^2. The first-trace sharper remainder is at most 72q^2|n alpha-T|/(n+2). These constants are upper bounds, not sharp estimates.

Independent checks planned: exact rational circle-polynomial integration of the residual O(2) law for n=3 with generic cross blocks and non-coordinate u; direct Euler-angle Haar O(3) quadrature for actual tanh gates; and finite differences to check the signs and coefficients 4 and 8. Edge cases X=I, X=ee^T, zero X, scalar A, and n=3 will be included. The formulas have not yet been declared verified.

## First verification run

Ran the single-threaded nice command for verify_dependent.py, saving stdout/stderr to verification_output.txt. All numerical assertions and 15 exact rational residual-circle integrations passed. Direct Haar O(3) quadrature (8 q values, q=0 through 1/4) agreed within 2.49e-14; doubling sphere quadrature gave a 6.32e-13 maximum change. Extrapolated derivatives agreed with -0.4735555555555557, -2.0739060493827166, -5.200955432098766 to 9.0e-8. Higher-dimensional residual-Haar simulations were within 1.064 standard errors. Peak RSS 58.5 MiB, runtime 0.22 seconds, niceness 20.

Audit issue: this NumPy build emitted divide/overflow/invalid warnings on finite weighted vector matmul reductions, despite finite accurate outputs and passing assertions. Treat this as unresolved numerical-environment noise, not a clean verification transcript. Replace the weighted BLAS reductions with explicit math.fsum weighted sums, enable floating-point exceptions, and rerun. Preserve this observation here rather than hiding it.

## Verification rerun and adversarial checks

After replacing weighted vector BLAS reductions by math.fsum and setting NumPy floating-point errors to raise, reran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 verify_dependent.py > verification_output.txt 2>&1
```

Exit 0. No floating-point warnings remained. The cause of the first run's BLAS warnings was not proved; the rerun avoids those reductions and retains floating-point exception checking. Output:

```text
Exact residual O(2) polynomial integrations: 15 passed
Direct Haar O(3) tanh quadrature: 8 cases passed; max error 2.49e-14
24x48 versus 48x96 sphere quadrature: max difference 2.56e-13
Extrapolated derivatives: [-0.4735555558355031, -2.0739060353491823, -5.200955432371757]
Exact linear coefficients: [-0.4735555555555557, -2.0739060493827166, -5.200955432098766]
Max derivative difference: 1.4e-08; all explicit remainder bounds passed
Residual Haar O(3) simulation: max discrepancy 0.765 SE
Residual Haar O(6) simulation: max discrepancy 1.064 SE
Niceness 20; peak RSS 58.8 MiB; runtime 0.30 s
All dependent-gate verification checks passed
```

The only extra stderr line is the inherited-niceness warning, with actual niceness 20 confirmed. The exact circle checks cover a generic positive Gram matrix with nonzero cross block, identity, zero, aligned and transverse rank-one matrices, each against generic, scalar, and partially zero gates. The output direction u=(2/3,1/3,2/3) is not a coordinate axis, so the z cross terms do not disappear trivially. Both determinant components of the residual orthogonal group are integrated.

The leading 4 and 8 coefficients have two derivations: differentiation of the gate followed by exact row-sphere fourth moments, and direct full-Haar quadrature finite differences (the first coefficient also follows independently from the beta integration-by-parts identity). The bound constants were audited from the scalar remainder 26, the squared-deviation bound 32, and the sixth-moment contraction 16: (2*26+32)*16=1344. The first-trace constant is 4*(14+4)=72 using exact second/third spherical moments. They are deliberately coarse and pass all tested q values through the endpoint 1/4.

Scope audit: n>=3 is explicit because the residual tensor denominator vanishes at n=2. The original n=1 boundary was covered in the earlier-result recheck. No claim is made for the present formulas at n=1 or n=2. The small-q mean normalization is spherical and conditional; an actual fixed gain is restored by the exact scalar g^2 mu_n(q), not replaced silently. The current lemma is one-layer and does not bound accumulated directional energies or forward-variance drift.

## Accumulation consequence of the same lemma

A useful cancellation appeared while auditing the two trace errors together. For X=I+E, the linear contribution to the normalized squared distortion is 8q/(n+2) times [(Tr(E^2)+Tr E)/n - e^T(E^2+E)e]. The directional term is bounded below by -1/4 by completing the square, so no separate bound on alpha or gamma is required for an upper bound on distortion.

Extend the chosen conditional-error lemma by this direct corollary: for the actual tanh Jacobian divided by the product of conditional scalar gains, derive an explicit accumulated distortion bound under a deterministic forward-variance envelope q_l<=epsilon_l<=1/4. The sufficient joint-limit condition is sum epsilon_l^2 + (sum epsilon_l)/n -> 0. Recover empirical isometry of the original Jacobian if, additionally, its accumulated conditional scalar gain tends to 1. This remains part of the chosen task of quantifying and accumulating actual gate-dependence errors; it does not establish the scalar condition or forward-radius concentration.

## Accumulated corollary audit and simulation extension

Saved Theorem 3 in PROOF.md. Its recursion is E[Z_l|past] <= (1+12q_l/(n+2)+2760q_l^2)Z_(l-1)+6q_l/(n+2)+2904q_l^2. Summing gives B exp(A). Checked the cancellation directly by expanding X=I+E and completing (E+I/2)^2. The constants 2760 and 2904 are independently expanded in the proof from the earlier 1344 and 144 terms. The theorem is for the genuine network Jacobian divided by the explicitly defined scalar S=product g_l^2 mu_n(q_l); it is not an adaptive-gain Jacobian.

Extended verify_dependent.py to simulate actual gain-one tanh networks, n=4,8,16 and L=30, 1200 samples each, with deterministic envelope epsilon=.001. The n=4 and n=8 normalized distortions were .00118727 and .00101426 versus rigorous bounds .135098 and .118380; average S was approximately .943, illustrating why scalar normalization must be stated. The n=16 run stopped with FloatingPointError from NumPy batched matmul on ordinary finite arrays, matching the earlier BLAS warning issue. No claim of a completed final run yet. Replace batched BLAS products by explicit non-BLAS einsum and retain exceptions on errors.

## Final verification of the accumulated result

Replaced batched BLAS matrix products with non-BLAS einsum, retained floating-point exceptions, and reran successfully. The scalar-normalizer quadrature in the actual-network simulation was then improved to Gaussian quadrature for the exact spherical-coordinate weight, using a Gegenbauer Jacobi matrix. Its second and fourth moments were checked against 1/n and 3/[n(n+2)], and 24 versus 48 nodes agreed to less than 1e-13 for the mean gate at the largest simulated q. This avoids endpoint-density errors from the earlier normalized Legendre approximation.

Final verification command is unchanged. Exit 0, saved complete output in verification_output.txt and all parameters/results in results.json. Additional final output:

```text
Actual tanh n=4, L=30: mean normalized Z=0.00118727, bound 0.135098, mean S=0.942903
Actual tanh n=8, L=30: mean normalized Z=0.00101426, bound 0.11838, mean S=0.943129
Actual tanh n=16, L=30: mean normalized Z=0.000742813, bound 0.107635, mean S=0.943288
Niceness 20; peak RSS 91.8 MiB; runtime 0.92 s
All dependent-gate verification checks passed
```

The accumulated theorem was also audited for zero depth, the zero-q boundary, scalar or identity X, positivity of S, and the exact normalization of J_l J_l^T by S_l. The unnormalized conclusion needs only convergence of S_L in probability, not convergence of its expectation; its proof uses a samplewise Frobenius inequality. No spectral-edge or uniform-isometry conclusion is claimed. The actual forward process and gains in Theorem 3 are ordinary zero-bias tanh; adaptive-gain derivatives are not silently substituted.

What did not work: directly replacing dependent gates by independent ones omits the linear-q directional term. Attempting separate directional bounds is unnecessary for this sufficient distortion estimate: the combined expression has a useful square. NumPy BLAS warnings caused two verification revisions, documented above; the final calculation avoids the offending reductions/products, without suppressing floating-point errors. Forward-radius concentration and accumulated critical scalar gain are still unproved, and the full problem remains open in this work.

## Final artifact audit

Read the completed report and proof for scope consistency, including the introduction after adding Theorem 3. A final stdlib-only audit run under OMP_NUM_THREADS=1 and nice -n 15 checked the verdict prefix, all nine supporting files, Python syntax without creating bytecode, presence of all three theorems, 15 exact integrations and 8 Haar quadrature cases, finite JSON, the actual-network envelope/bound checks, all thread settings one, memory/time/niceness limits, saved success markers, and the arithmetic of 72,1344,2760,2904. Exit 0: “Final audit passed: reports, three theorems, exact checks, quadrature, actual-network data, resource limits and saved output agree.”

All intentional writes stayed in this task folder. The previous worker's files, shared brain/checklist/mesh stores and git state were not changed.
