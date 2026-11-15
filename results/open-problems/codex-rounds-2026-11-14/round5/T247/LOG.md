# T247 work log, round 5

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 08:50 Asia/Tbilisi.

## Orientation and bounded literature check

Read startup memory, compute state (warn, owner_away_open), and the earlier reports, logs, proofs and scripts. Earlier folders remain read-only. The specific instruction that every write stay here supersedes global mesh/checklist/brain writes; none will be attempted. No git or subagents. All numerical runs use one thread, nice -n 15, a short alarm and a peak-memory check.

Within five minutes searched the web for joint depth-width Jacobian spectra, growing-depth orthogonal networks and the Collins–Hayase/Pastur results. Opened arXiv 1711.04735, 2103.13466 (including full HTML), 2201.04543, 2503.07872, and full HTML 2506.08764v3. No verified solution of the requested nonlinear joint limit appeared. Hanin–Jiang concerns independent i.i.d.-entry products; Dadoun et al. retains fixed-depth infinite-width analysis. This is a bounded check, not an absence theorem. Literature search is now closed.

## Earlier result: independent derivation underway

The round-4 scalar inequalities reproduce the radial expansion E log F(q,u)=-(2n/(n+2))q+O(q^2). Recomputed E M4^2 by separating diagonal eighth moments (105) and mixed fourth moments (9), obtaining n^2(9n+96)/((n+2)(n+4)(n+6)). Thus (17/45) E M6 + 2 E M4^2 <=71/3<24. Combining the trace remainders gives (2*26+32)*16=1344, then 1344*(2Z+2)+144*(Z/2+3/2)=2760Z+2904. No discrepancy found so far. A local rerun of the latest verification will precede a claimed extension.

## Earlier-result recheck completed

Copied the latest verification scripts here by read/write, changing only verify_critical.py's JSON destination to earlier_critical_results.json. Ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 verify_critical.py > recheck_critical_output.txt 2>&1
```

Exit 0. All exact moments, 110-digit inequalities, doubled sphere quadrature, 100000 crossing checks, forward-radius simulations and actual Jacobian products reproduce the prior output. Peak RSS 65.0 MiB, runtime 1.87 s, actual niceness 20. In particular the scalar/radius mismatch is -0.7999999996 versus -0.8. Together with the independent algebra above, the earlier main claim holds.

## Chosen extension, before new derivation

Extend the theorem to independent Gaussian biases at simultaneous Gaussian forward/backward critical initialization, still with a_n tending to zero and L a_n^2+L a_n/n tending to zero. This is the previous report's first next target. Define mu_G(a)=E sech^4(sqrt(a)G), A_G(a)=E tanh^2(sqrt(a)G), g^2=1/mu_G(a), and bias variance b=a-g^2 A_G(a). Seek the ordinary unnormalized Jacobian theorem with deterministic initial radius g^2||h_0||^2/n=a-b. Gaussian Poincare makes b nonnegative, and the global scalar remainders suggest b<=14a^3. That small bias is within the same accumulated scale.

Plan of proof: average the independent biases in the one-layer gate estimates before averaging Haar weights. The linear directional correction stays proportional to the signal variance q; bias only enters the O((q+b)^2) remainders. For the forward process, work first with relative radius increments rather than logarithms. Polynomial moment bounds handle the unbounded biases; on the high-probability stopped-radius event convert to logarithms using a quadratic remainder. This avoids assuming a deterministic bound on every bias coordinate or an integrability estimate near an accidentally tiny forward norm.

## Biased estimates derived

Let z=sqrt(nq)u+sqrt(b)G and r=q+b. Conditional bias averaging gives the same first-order gate term 2q(1-nu_i^2); the bias mean cancels in the normalizer. A direct global expansion gives |E_bias R_ii|<=40r^2(1+y_i^2) and E_bias Delta_ii^2<=128r^2(1+y_i^2). Spherical row moments then give first-trace remainder <=640r^2 T and second-trace remainder <=3328r^2 Q, with 3328=(2*40+128)*16. The normalized distortion recursion has coefficients 7296 and 8576, recomputed as 2*3328+1280/2 and 2*3328+3*1280/2.

For b<=14a^3, gain |log(g^2)-2a|<=15a^2 and q in [a/2,2a], the ordinary radial increment R=(q_next-q)/q satisfies |E R-(2a-2nq/(n+2))|<=300a^2 and E R^2<=12000a^2 (n>=64,a<=1/16384). A restoring-drift bound on q/a-1 gives radius error <=8/n+614a+2delta, with exceptional probability <=48000La^2/delta^2. A second martingale for R and the sum of R^2 compare the scalar normalization to the telescoping log radius. This appears to prove the unnormalized biased theorem under the previous scaling. Detailed proof and independent checks remain to be completed before the verdict.

## Proof saved; adversarial verification begins

Saved PROOF.md with all steps, including a direct interpolation proof of Gaussian Poincare to justify b>=0 and the bound b<=14a^3. The theorem covers simultaneous critical g^2=1/mu_G(a), b=a-g^2 A_G(a), input norm squared/n=A_G(a), and a wider deterministic parameter class. The stopped scalar comparison uses two martingales and the sum of squared relative radius increments; it never takes expectations of a log near a potentially tiny new radius. Equation (38) gives an explicit finite probability bound.

Audit targets: exact series for the critical bias by a second method; global bias-averaged gate bounds; direct Haar/Gaussian quadrature versus the linear coefficients including pure-noise gates; exact correlated-coordinate moment checks for the radial square bound; a real biased critical network and an accumulated forward simulation. No final verdict until these checks and a second proof audit complete.

## Verification completed

Ran, exit 0:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 nice -n 15 python3 verify_bias.py > verification_output.txt 2>&1
```

Exact rational formal small-a coefficients derived from tanh'=1-tanh^2 give b(a)=4a^3/3-8a^4+748a^5/15-1048a^6/3+... . Independent 70-digit Gaussian quadrature gives b/a^3=1.3333253333831996 at a=1e-6, agreeing with the leading coefficient. All 42 global bias-averaged gate checks passed, including zero signal, zero bias, and coordinate parameters y=10000. Direct biased Haar O(3) quadrature passed 25 cases, maximum refinement difference 1.24e-14; the mixed signal/bias linear coefficient agreed to 1.4e-7. Pure-noise gates also matched the original independent-gate second-moment identity.

Forty-eight exact correlated eighth-moment calculations independently verified the radial squared-increment bound (largest exact-bound/coarse-bound ratio .0200272). Thirty-six forward drift/scalar quadratures passed, including both extreme permitted gain choices, zero and maximal allowed bias, and critical bias, at q/a=.5,1,2 in dimensions 64 and 128.

Actual biased critical network n=64,L=180,24 samples,a=1/16384: mean unnormalized distortion 3.18116915e-5, normalized 3.18122648e-5, stopped bound .0563979862, mean S=.999992801. Longer forward-only stress test n=64,L=10000,a=.0002 (La=2,La/n=.03125) gives mean S=.910487743 and maximum radius error .0392780875. This finite-width drift is retained; the theorem requires La/n to vanish. Runtime 3.88 s, peak RSS 95.2 MiB, actual niceness 20, every thread setting one. The inherited priority produces a harmless nice warning; no floating-point warning or failed assertion occurred.

Also reran recheck_independent.py and recheck_dependent.py locally, exit 0. Reproduced 20 exact rational product checks, 15 residual Haar exact integrations, eight full Haar quadratures (max error 2.49e-14), and all depth-30 actual-network checks. Their outputs are saved separately. Earlier files were not changed.

## Final adversarial audit

Added 100000 crossing checks with nonzero initial radius error, the asymmetric stopping interval (-1/2,1), and jumps crossing its boundary. Also integrated conditional forward drifts along actual biased-network paths to check both martingales, the pathwise radius inequality, the logarithmic Taylor remainder and the scalar comparison. Reran the full verification: exit 0, all checks passed, runtime 3.71 s and peak RSS 92.1 MiB. The final output includes these added checks.

Re-read the proof from the ordinary network recursion through the final probability bound. Checked that fresh biases are independent only of past layers and weights; gates retain their dependence on the fresh Haar image. Normalizing uses the spherical-plus-Gaussian mean, while initialization uses the conventional Gaussian critical mean. The proof never substitutes one for the other. Stopping is predictable, includes the exit step, and the frozen Gram and radius processes use the same active indicators. Logs are used only on the no-exit event, with every adjacent radius ratio in [1/4,4].

The critical bias is in fact strictly positive for a>0: the interpolation proof of Gaussian Poincare is strict because the derivative of tanh(sqrt(a)G) is nonconstant. Added that observation to PROOF.md. The theorem proves empirical convergence in probability, not convergence of expected unnormalized distortion, and no singular-value edge statement.

What failed: no numerical assertion or mathematical check failed. Attempting to carry over the old log-radius estimate directly would require new integrability control near a cancellation by the unbounded Gaussian bias. The relative-increment proof avoids that additional lemma. The finite constants are coarse. The long forward stress test continues to show finite-width scalar drift, consistent with the retained La/n condition. Fixed positive a and the full density remain outside the result.

## Report and artifact audit complete

Saved REPORT.md with the required PARTIAL verdict, the new critical-bias theorem, precise scope, reproduction commands, verification output, limitations and next targets. A final stdlib-only audit under the same one-thread nice environment checked the verdict, all 38 consecutive equation labels, balanced mathematical delimiters, script syntax without bytecode writes, every reported check count, saved success markers, report links, positivity/scaling of the simulated critical bias, pathwise scalar margins, and RAM/time/priority limits. Exit 0: “Final artifact audit passed: theorem scope, 38 numbered equations, proof delimiters, script syntax, exact and numerical checks, saved outputs and resource limits agree.” Final measured verification was 3.710 s, 92.141 MiB, niceness 20. All intentional writes remained here. Completed approximately 09:06 Asia/Tbilisi, 15 November 2026.
