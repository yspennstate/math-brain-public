# T247 work log, round 6

Task: “take the NEXT checkable step on this problem, building on that work” — received 15 November 2026, approximately 11:28 Asia/Tbilisi.

## 11:30 — orientation and literature check

Read startup memory/navigation and compute state (status ok, owner_away_open). The task-specific instruction to write only in this folder overrides global mesh, checklist, recall logging and brain mutations. Those commands are not run. No git or subagents. All numerical programs will run with one thread, nice -n 15, a time limit below 20 minutes and memory below 1 GiB. Earlier work is read-only.

The web search began at approximately 11:28 and ended by 11:30, within five minutes. Queries covered joint depth-width Jacobian spectra, orthogonal tanh networks and Collins–Hayase/Pastur. Opened arXiv pages 1711.04735, 2103.13466, 2201.04543, 2503.07872, 2506.08764, 2508.02882, and the full Springer Collins–Hayase article. No verified resolution of the requested dependent nonlinear joint limit appeared. The search is bounded, not an absence theorem. Detailed sources will be recorded in LITERATURE.md.

Initial proof audit: round 5 Sections 5–6 bound the relative forward radius using La^2 alone. Section 7 compares log S_L with the telescoping log radius and loses 4q/(n+2) per layer. That signed term should have a nonzero limit when La/n does not vanish. The choice of extension will be made after independently rechecking the earlier computation.

## Earlier result rechecked

Read the earlier reports, logs, proofs and scripts, following duplicate scripts through their original versions. Copied round 5 verify_bias.py to recheck_bias.py in this folder, changing only its JSON destination to recheck_results.json. Ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 -B recheck_bias.py > recheck_output.txt 2>&1
```

Exit 0. All formal bias coefficients, 70-digit Gaussian quadratures, 42 global gate bounds, 25 direct Haar/bias trace quadratures, 48 exact eighth-moment calculations, 36 drift/scalar quadratures, 100000 stopped crossing checks and actual-network products reproduce the earlier computation. The earlier main claim holds. The nice warning reflects inherited niceness 20, verified by the script.

Independent arithmetic audit: the leading radial drift is 2a-(2n/(n+2))q; the leading scalar log gain is 2a-2q. Their signed difference is -4q/(n+2). The biased second-trace remainder constant is (2*40+128)*16=3328, and its combination with twice the first-trace remainder gives 7296Z+8576, agreeing with round 5. The proof has not used any independence between gates and fresh weights.

## Chosen extension, before its proof

Prove the accumulated logarithmic volume drift of the actual biased critical Jacobian under La^2 -> 0, allowing La/n to stay positive or diverge. Track the signed -4q/(n+2) term rather than its absolute bound. Target: log S_L/(La/n) -> -4 when La/n does not vanish, with a uniform-in-depth error statement; then show n^(-1) log det(J_L J_L^T)-log S_L -> 0. This extends an auxiliary scalar observation to a genuine Jacobian spectral statistic, the geometric mean of its squared singular values.

Why this piece: the previous report asks whether La/n can be removed. A precise volume law identifies what changes at that scale without assuming that the existing normalization remains close to one. It will not by itself prove or disprove empirical W2 isometry: very small singular values can change log determinants while occupying a vanishing spectral fraction.

## Proof saved; independent verification planned

Saved PROOF.md. The retained signed mismatch is |s(q)-d(q)+4q/(n+2)|<=452a^2. With the existing stopped radius estimate, this yields max_k |log S_k+4ak/(n+2)| <= C_0+4(La/(n+2))epsilon on a quantified high-probability event, where C_0 and epsilon tend to zero under La^2->0 alone.

The new determinant step uses 0<=x^2/2-log cosh x<=x^4/12 and the exact conditional variance of n^(-1)sum z_i^2. On active steps the expected absolute difference between the layer-average log squared gate and log mu_n(q,b) is at most 150a^2. Thus max_k |n^(-1)log det(J_k J_k^T)-log S_k|->0. No singular-value truncation or freeness is used. The theorem includes finite La/n limits, diverging La/n with relative error control, and a uniform time version at depth floor(t(n+2)/a).

Second derivation of the coefficient: the leading forward equilibrium is q_*=a(n+2)/n, so the logarithmic volume increment is 2a-2q_*=-4a/n. This is only an algebraic check; the proof controls the transient rather than assuming stationarity.

Verification targets: high-precision global log-cosh bound; exact sphere moments and independent marginal quadrature for the signed coefficient; direct determinant of small full Jacobian products against the sum of layer log determinants; determinant/scalar comparison with Gaussian biases; and a longer forward-only simulation. The forward-only simulation is exact in law for radius and determinant because a fresh Haar image of a fixed nonzero vector is uniform on its sphere. It will not be used as evidence about the rest of the spectrum.

## First verification: numerical backend exception

Ran the one-thread nice command for verify_volume.py. The 75-digit scalar checks, 18 rational coefficient checks, nine 65-digit sphere marginal quadratures (largest extrapolation error 2.19e-14), and 24 whole-vector biased comparisons passed. The first direct full-product determinant calculation stopped with FloatingPointError in NumPy slogdet. This resembles the earlier rounds' numerical backend exceptions, but its cause is not established. Saved the complete first output in verification_first_failed.txt. No mathematical conclusion is based on that failed run.

Replaced slogdet with scalar partial-pivot Gaussian elimination on the already computed small matrices; all other floating-point exceptions remain enabled. This is an independent direct determinant calculation and avoids suppressing the failing backend warning. A clean rerun is required.

Created forward_volume.cpp for longer exact-in-law radius/determinant paths. Its parameter choice log(g^2)=2a-5a^2, b=4a^3/3, q_1=a-b is in the wider class (4), and is explicitly not the exact Gaussian critical initialization. The full-product Python check uses the exact Gaussian critical values computed at 65 digits. C++ paths use n=16,32,64, a=1/(64n^2), three replicates, and La/n=.025,.05,.1, with a 180-second alarm and small vectors only. Compute state was re-read before compiling: ok, owner_away_open.

## Clean verification completed; long paths running

Ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 -B verify_volume.py > verification_output.txt 2>&1
```

Exit 0. All scalar, exact moment, marginal quadrature and biased comparison checks passed. Independent direct elimination of full Jacobian products agrees with the summed layer log determinants to 1.74e-13, 1.35e-13 and 1.84e-14 in the three cases. Full-product mean H values: -0.277198582 (n=8,L=1000,a=.001), -0.100947984 (n=16,L=800,a=.001), and -2.52175987e-5 (n=32,L=240,a=1/16384). Their H/log S comparisons satisfy the pathwise comparison inequalities. Runtime 2.47 seconds, peak RSS 157.7 MiB, niceness 20. First failed output remains preserved separately.

Compiled and launched the longer radius/determinant simulation:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 clang++ -std=c++17 -O2 forward_volume.cpp -o forward_volume
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 ./forward_volume > forward_results.json 2> forward_stderr.txt
```

Compilation exited 0. The simulation is running; no outcome claimed yet. The n=16,32 cases are finite-width diagnostics outside the n>=64 finite-bound assumptions in PROOF.md, and are not used as proof of those bounds.

## Long paths completed

The C++ simulation exited 0: 27 path checkpoints, 8.861 seconds, 1.312 MiB peak RSS, one thread, niceness 20. All radii stayed in [a/2,2a], logarithmic remainder checks and compensated-volume comparisons passed. At La/n approximately .1, the mean H values for n=16,32,64 were respectively -.268188795, -.336817678, -.368997457, approaching the asymptotic target -.4. The corresponding La^2 values were 9.76548e-5,4.88281e-5,2.44141e-5. Initial forward-radius relaxation is still visible at these widths; do not describe these finite numbers as already equal to the asymptotic target.

At n=64,L=1677722, the maximum compensated error |H-log(q_final/q_initial)+4 sum q/(n+2)| was .00213316 across the three replicates. The exact spherical scalar log S is bracketed by its linear approximation sum(log g^2-2(q+b)) plus or minus 15 sum(q+b)^2; the bracket half-width was at most .000387718. No approximate scalar value is presented as exact quadrature.

The finite-width first-order ODE dy/ds=y(2-c_n y), y(0)=1 has y(s)=(1+2/n)/(1+(2/n)e^(-2s)) and H(s)=-4s/n+(1+2/n)log y(s). Its diagnostic values at the same three endpoints are -.273205891,-.335696291,-.368266911. This is a second sign/magnitude check with the initial transient included, not a proved approximation bound. The computation is saved in summarize_forward.py, with output forward_summary.txt.

## Mathematical audit

Re-read the stopping argument, signed comparison and determinant proof. The radius proof requires only La^2->0; the signed scalar estimate permits arbitrary La/n after division by 1+La/(n+2). The determinant comparison is absolute o_P(1), even when La/n diverges. Gaussian bias cancellations never require taking an expectation of a logarithm of a small radius: logarithms of radius ratios are used only on the no-exit event. Fresh gate/weight dependence is retained throughout. The log-cosh bound is global, so rare large coordinates are included.

Checked the constant 150 by a second expression: 4qb+2b^2 <= (112+392a^2)a^4 <=113a^4; then 2sqrt(113/64)+144<147<150. The signed factor is independently checked by exact Dirichlet moments, 65-digit marginal quadrature, and the leading forward equilibrium. The distinction between squared singular values and singular values fixes the factor 4 in H; half that factor would apply to n^(-1)log |det J|.

The explicit spectrum with one squared singular value exp(-4tn) and all others one was checked separately. It confirms that the volume law does not establish necessity of La/n->0 for empirical W2 isometry. No claim about the number of exceptional directions in the actual network is proved here.

## Report and final artifact audit

Saved REPORT.md with the PARTIAL verdict, the precise logarithmic volume theorem, the earlier-result recheck, all reproduction commands, the preserved failed numerical run, limitations and the next mathematical target. Saved LITERATURE.md with only papers actually opened. All intentional writes remained inside this folder; no earlier folder, shared brain/checklist/mesh store or git state was modified.

Ran the saved summary and artifact checks:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 -B summarize_forward.py > forward_summary.txt
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 -B audit_artifacts.py > audit_output.txt 2>&1
```

Both exited 0. Final output: “Final artifact audit passed: 31 equation labels, proof delimiters, script syntax, report links, exact and numerical check counts, finite data, preserved failure, saved outputs, and resource limits agree.” The theorem is partial progress on a logarithmic spectral statistic; the requested full joint-limit density and empirical-isometry extension remain open in this work.
