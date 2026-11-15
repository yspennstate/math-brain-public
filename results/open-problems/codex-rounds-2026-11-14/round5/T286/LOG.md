# T286 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Started 15 November 2026, 09:03 Asia/Tbilisi.

## Orientation and literature check

Read REPORT.md and LOG.md from the original, round-3 and round-4 folders, and the later PROOF.md files and verification scripts. The original folder has neither a proof nor a script. Read the startup memory index and compute_state.json (status ok, owner_away_open; other jobs occupy most CPU). All computations here are tiny, standard-library-only, one thread, run through nice -n 15 with bytecode disabled. The task-specific folder-only rule prevents external brain/checklist/mesh mutations; those stores are left untouched. No git or subagents.

The bounded literature check began at 09:03 and ended at 09:06, within five minutes. Queries: `"2408.03733" rigorous general activation proof`; `"Bayes-optimal learning" "extensive-width" 2026`; `"2510.24616" Gaussian replacement`; `"extensive-width" "rigorous" "general" "2026"`; `"2510.24616" proof Gaussian conjecture`. Opened https://arxiv.org/abs/2510.24616, https://arxiv.org/html/2510.24616v5 and https://arxiv.org/html/2503.14121v2. The latest displayed 2510 version remains v5, dated 24 July 2026. Remark 4 still conjectures exactness; Appendix B.6 retains replacement and concentration assumptions. No later rigorous solution was found. This bounded negative search does not prove absence of a solution. No SOLVED_ELSEWHERE.md is called for.

## Rechecking the earlier result

Read round 4's tensor contraction formula and the Gaussian-generator derivation of the Stein matrix. Next run both inherited exact verifiers read-only, with outputs saved here. Independently reconstruct the coefficient normalization and check the likelihood-functional obstacle before choosing one extension.

Both inherited verifiers passed (exit 0):

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T286/check_stein.py > recheck_stein.out 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T286/check_cubic.py > recheck_cubic.out 2>&1
```

Round 4: six exact contraction checks, seven mixed deterministic identities, four averaged Stein variance checks; 0.052 seconds, peak RSS 15,400,960 bytes. Round 3: five exact Wick checks and the asymptotic ratio checks; peak RSS 16,220,160 bytes. Actual nice priority 20, OMP_NUM_THREADS=1. The attempted further relative priority adjustment is denied because priority is already 20.

Independent normalization check, without either script: for d=k=1 and a Gaussian weight w, Gamma-K = (w^6/2)He_4(X)+(4w^6-2w^4)He_2(X). Thus its conditional variance is 38w^12-32w^10+8w^8, and its prior expectation is 38*10395-32*945+8*105=365610. This agrees with the inherited direct-coordinate verifier. The inverse Gaussian generator produces the factors 1/3 on the cubic chaos and 1 on the linear chaos, giving the mixed coefficients 1/2, 1/sqrt(6), sqrt(3/2), 1. The prior contraction expectation and Cauchy--Schwarz then give epsilon^2=14delta+o(d^-1), delta~(1+1/gamma)/d. The earlier main claim holds, including its restriction to the omitted-input law.

## Choice, recorded before the extension

Choose ONE piece: prove the likelihood-weighted integration-by-parts step (158) to (161) for the cubic activation and a smooth finite-output channel with every output probability bounded below by a fixed positive constant. Include the Gaussian interpolation offsets from (147). This is a restricted output-channel result; it does not replace the cubic hidden activation by tanh or ReLU.

Reason: writing log Z_full=log Z_cavity+log Z_one_sample cancels log Z_cavity after summing p_y', since sum_y p_y'=0. The one-sample normalization lies in [c,1]. Approximate it by R cavity replicas; the sum of derivative bounds is independent of R. Apply the inherited Stein identity, then take R to infinity using conditional laws of large numbers. This should control the random normalization and the log-partition factor without assuming posterior independence after averaging. The Gaussian offset terms can then be integrated exactly. Target: an explicit O(d^-1/2) error uniform in the interpolation parameter after the 1/sqrt(1-t) factor cancels, plus the known O(d^-1) covariance correction. Distinct-replica concentration, the Bayes-error formula and gradient descent remain outside this single extension.

## Derived identity and saved proof

Wrote PROOF.md. The key finite-replica test is h_R(z)=sum_y p_y'(a z_0+offset_0) log[(1/R)sum_{j=1}^R p_y(a z_j+offset_j)]. Its teacher derivative is bounded by |a|q L2 log(1/c), and each replica derivative by |a|q L1^2/(Rc). Thus the total derivative bound is |a|B, independent of R. The conditional law of large numbers, an L1 truncation for the kernel-weighted numerator, and Z>=c justify R->infinity.

Integrating the two scalar Gaussian offsets gives the exact coefficients aa'=-1/2, bb'=G'/2, ee'=(1-G')/2. Combining them gives the self coefficient (1-K_00)/2 and the cross coefficient (G'-K_0W)/2. The absolute error is B*epsilon/2; replacing K by the Hermite kernel C costs B*ell/2. The error is uniform on the open interpolation interval. Summing over observations with normalization 1/n adds no factor of n. For 1/d^2 normalization it costs n/d^2.

The large cavity log partition cancels pointwise after label summation, since sum_y p_y'=sum_y p_y''=0. This is essential: simply bounding the uncentered log Z would introduce a spurious extensive factor. The self term then has the previously proved O(d^-1) bound, using only the bounded one-observation logarithm. A noisy binary channel p_±=(1±lambda*tanh z)/2, lambda<1, is an explicit example. The hidden activation remains cubic.

Next audit: independently differentiate the finite-replica test, test the integrated identity against direct low-dimensional Gaussian quadrature with nontrivial random normalization, and check the constants and degeneracies. These computations verify the algebra and limits in examples; they are not a substitute for the written proof.

## First independent verification run

Command: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_cavity.py > check_cavity.out 2>&1`.

The scalar exact Stein variance, 24 finite-difference gradient checks, summable derivative bounds and tanh-channel constants passed. Direct two-dimensional quadrature uses a sine output channel so that the independent latent U can be integrated analytically, with the nontrivial normalization left inside the X,V integral. The first mixed-weight case had identity errors 6.83e-5, 3.19e-7 and 1.75e-11 at 120, 240 and 480 Simpson intervals per axis. The script correctly failed its separate grid-convergence check: the change from 240 to 480 was still about 2.4e-7, above 2e-9. Saved this output as check_cavity_initial.out. Increase the final resolution to 960 intervals and retain the original convergence tolerance; no proof change is indicated by this quadrature-resolution failure.

## Successful refined verification and attempts to break the result

Re-ran with 960 final Simpson intervals per axis, leaving the error tolerances unchanged:

```
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 -u check_cavity.py > check_cavity.out 2>&1
```

Exit 0. All checks passed. Runtime 21.675 seconds, peak RSS 14,991,360 bytes, actual priority 20, one thread. The final direct normalized identity errors were 7.08e-14 (mixed weights), -1.92e-16 (opposite and duplicate weights), and -4.36e-15 (zero weights). The final grid changes also passed the 2e-9 tolerance. The mixed example has I=0.0116670380365 and covariance-only J_K=0.0103829830083: their difference 0.00128405502813 is recovered by the independently evaluated exact Stein correction. Thus dropping that correction in a finite deterministic network would be detected. These are algebra checks for deterministic finite cavity measures, not estimates of a Bayes error or of the prior-averaged asymptotic bound.

Independent checks of load-bearing constants: direct scalar Gaussian polynomial integration gives 365610; a separate Hermite expansion gives 38*10395-32*945+8*105=365610. The 24 gradient cases compare every analytic component against finite differences for R=1,2,7,31, two likelihood floors, and positive/negative a; they check both each 1/R bound and the summed bound. Maximizing lambda*h*(1-h^2) on [-1,1] and separately evaluating its grid maximum verifies L2=1/(3sqrt(3)) for lambda=1/2. Two evaluations of the channel coefficient agree at 0.516792474190. The quadrature analytically eliminates U using E exp(i e U)=exp(-e^2/2), including its differentiated first moment; it computes the original score-times-dotS expression before using any normalized-test derivatives.

Proof audit: the teacher is excluded from the empirical denominator. Replicas are independent only conditional on cavity data; their unconditional dependence is retained throughout. The mixed Stein matrix need not be symmetric. The R->infinity step uses truncation of the integrable kernel numerator, not an unjustified bounded-kernel assumption. All posterior denominators stay above c. The normalizer contains an independent integrated latent u, not the teacher's U_0. Omitting the sample includes its input and shared V, so the Stein input is independent of the joint cavity law. Both first- and second-label-derivative cancellations remove log Z_cavity exactly. The endpoint derivative is not claimed; only the remainder bound is uniform on 0<t<1 and hence integrable.

Limits tested conceptually: q=1 is trivial; singular/duplicate/opposite and zero networks are covered without inverse covariance. With c tending to zero the bound diverges. Therefore no limit to the ordinary logistic channel or Gaussian regression is justified. The activation in the hidden layer is cubic even when tanh is used in the output probability. No conclusion about a general hidden activation or gradient descent follows. The C cross kernel remains permutation invariant and has not been replaced by a trace overlap.

## Final artifacts and scope check

Wrote REPORT.md with the required first-line verdict and checked it against the theorem. PROOF.md states the channel constants are fixed with dimension, retains the true covariance and its row-norm correction, and proves the cavity normalization limit before using the interpolation coefficients. REPORT.md records the initial numerical failure, the successful refined command, and all unresolved steps. Final file inspection confirms the report, proof, log, verifier and its successful/failed outputs are in this folder; both earlier verification outputs are also saved here. No change to the verified script after its successful run. No edits outside this folder, external writes, git operations or subagents.

Result: the cubic likelihood-weighted passage (158) to (161) is proved for fixed uniformly positive smooth finite-output channels, with explicit O(d^-1/2) error. The full general-activation problem and gradient-descent question remain unresolved.
