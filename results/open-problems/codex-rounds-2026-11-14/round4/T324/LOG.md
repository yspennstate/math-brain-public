# T324 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First recorded session clock: 15 November 2026, 06:31 +04 (Asia/Tbilisi).

## 1. Orientation and brief literature check

Read the earlier REPORT.md, LOG.md, PROOF.md and verification scripts in the original and round 3 folders (read-only). Read the startup memory index and compute state. The governor reports warn / cpu_saturated, so computation will be short, standard-library only, one thread, under nice -n 15. The folder-only instruction overrides general requests to write to the shared brain, checklist and mesh. No external state, git, or subagents will be used.

The literature check used the web search tool and ended within five minutes of the first command. Queries included `"metastable" "transformer" clustering 2025 2026 Bruno Pasqualotto Agazzi`, `"2410.23228" metastable clustering subsequent`, and `transformer "clustering" "metastability" November 2026 theorem finite width`. Opened arXiv pages 2410.23228, 2312.10794, 2509.25040, 2610.08755 and the HTML of 2509.25040v1. No post-report resolution was found. The multiscale and conditional noisy results were already identified by the earlier workers. This is a brief update, not a novelty claim.

## 2. Independent analytic recheck of round 3

Let E=exp(beta(1-cos s)) and C=p/q+q/p. Directly adding the two cross-attention coefficients gives h(s)/sin(s)=(CE+2)/(E^2+CE+1). Polynomial division gives

    1/(h(s)/sin(s)) = E/C + 1 - 2/C^2 - (1-4/C^2)/(CE+2).

Thus the stated uniform time estimate and critical constant follow. Independently, differentiating c=v_1 dot v_2 gives c'=(w_1+w_2)(1-c^2), and endpoint integration at c=cos(x) gives T~exp(beta(1-cos x))/(C beta sin(x)^2) when this expression diverges. The factor C and the positive-part exponent hold. For noise, the angular difference variance is 4 nu, so the generator is 2 nu d^2/ds^2-h d/ds. Solving 2 nu u''-h u'=-1 with u'(pi)=0 reproduces the earlier decaying kernel; its near-diagonal lower bound and outward-excursion upper bound give min{(1-cos(x)-kappa)_+,r}. No error found. Independent numerical checks will be recorded below.

## 3. Chosen extension, before proof

Prove a deterministic finite-width two-group theorem on the circle, with fixed positive group masses and initial group diameters at most c/beta. Aim to prove uniform exponential contraction of each diameter until a prescribed separation threshold, and sandwich the group merging time between two scalar two-atom hitting times with a multiplicative error tending to one. This addresses the next worker's missing concentration estimate. It will not claim an independent-token noisy reduction or a generic cluster count.

The main issue is to obtain a negative spatial derivative of the attention velocity inside each narrow group despite the other group. A generic global Lipschitz estimate over an exponentially long interval is insufficient. The proof must use internal attraction and exponentially small cross-attention on the stopped domain.

## 4. Concentration mechanism and sharper scope

The spatial derivative is exactly V'(theta)=-E_theta cos(phi-theta)+beta Var_theta(sin(phi-theta)). If the group diameter is w and the cross-attention fraction is at most epsilon, then V'<=-1+(beta+1/2)w^2+(beta+2)epsilon. This yields diameter contraction at rate at least 1/2 for w<=1/(4 sqrt(beta)) and large beta, up to a fixed group-center separation threshold. This improves the initially planned c/beta width condition for the logarithmic law.

Symmetrizing the internal contribution to the conditional arithmetic group mean gives a factor (1/Z_i-1/Z_j), hence an internal mean drift bounded by C beta(w^3+epsilon w^2), rather than O(w). The accumulated initial displacement is therefore O(beta w_0^3), and after time 4 beta the widths are exponentially small. The same extension will prove log(T)/beta->1-cos(x) at w_0<=1/(4 sqrt(beta)), and the full two-atom prefactor when beta^2 w_0^3->0 (in particular w_0=O(1/beta)). This is one concentration-and-merging theorem, with a sharper conclusion under a narrower width hypothesis. The mass totals p,q remain fixed; no stochastic theorem is proposed.

## 5. Proof saved and analytic audit

Wrote PROOF.md, including the mean-field characteristic formulation. The diameter estimate is independent of token count and individual token weights. The interval span is invariant because it is shorter than pi. Until the center gap reaches delta, cross-group distances exceed delta/2 for large beta. This justifies the exponential cross-attention bound on the entire stopped interval, rather than at initial time alone.

After the initial contraction time t_0=4 beta, the proof gives an explicit relative error eta_beta->0 in s'=-h_beta(s)(1+error). The lower bound h_beta>=m exp(-2 beta) makes the internal mean residual negligible even over the exponentially long interval. The resulting hitting-time sandwich is equation (22). Initial center motion is O(beta w_0^3+beta epsilon_beta); it is o(1) for the exponent theorem, and o(1/beta) under the prefactor hypothesis. The latter distinction is necessary: an o(1) center displacement alone does not preserve the endpoint Laplace prefactor.

Second analytic derivation: write the attention weights alpha_j(theta). Then alpha_j'=beta alpha_j(sin_j-sum_k alpha_k sin_k); substituting into V'=sum_j alpha_j' sin_j-sum_j alpha_j cos_j gives the same variance formula and its sign. Independently symmetrizing the finite weighted double sum gives (12), agreeing with the integral derivation. In the scalar reduction, each coefficient is at least its numerator times exp(-beta(1-cos s)), so their sum is at least exp(-beta(1-cos s)); no monotonicity assumption about h_beta is used. These checks preserve all factors in (13), (18), and (22).

## 6. First numerical check and a failed extrapolation

Command: `env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py`.

The first run exited 1 after passing the earlier-result checks and the local identities. Output: deterministic angular/cosine error 6.704e-13; noisy kernel mean 3.82727883172 versus BVP mean 3.82727875446 (relative error 2.019e-8); internal symmetrization error 9.385e-19. It then failed a width-contraction assertion in a full six-token solve at beta=6. This was an invalid test extrapolation: the theorem is for sufficiently large beta, and at beta=6 its sufficient bound (11) does not hold, especially near the small gap delta=.4. The all-beta contraction claim is false, and is not in PROOF.md. The moderate-beta full solves will be retained as time comparisons, with their measured width excess recorded; contraction will instead be checked at beta=500,1000,2000 where the explicit sufficient condition is satisfied. No theorem assumption or assertion threshold will be weakened.

The nice launcher prints `setpriority: Operation not permitted`, as in the earlier sessions. The process asserts its effective inherited nice value is at least 15 before any computation; this assertion passed. Each run also enforces a 90-second CPU limit and uses only small standard-library lists.

The diagnostic command, under the same thread/nice launcher, was `python3 -c 'import verify; print([(b, verify.token_hitting_time(b, 0.2/b, 0.1)) for b in (6,10,14,18)])'`. Output (beta, hitting time, maximum excess over w_0 exp(-t/2)): `(6, 3.6115333616232634, 0.005501422382645588)`, `(10, 19.248276783853868, 0)`, `(14, 159.65611477325484, 0)`, `(18, 1543.6212376451608, 0)`. Thus the failed assertion concerns a real finite-beta limitation, not a roundoff allowance. The final script retains the beta=6 excess in verification.json and asserts contraction only in the separate cases satisfying (11).

## 7. Successful run

Reran exactly:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify.py
```

Exit code 0. Output:

```text
nice: setpriority: Operation not permitted
Prior deterministic coordinate error: 6.704e-13
Prior noise kernel / BVP: 3.82727883172 3.82727875446 relative error 2.019e-08
Internal symmetrization max absolute error: 9.385e-19
Full six-token solve: 6 3.61138513 token/scalar 0.999003786 mesh error 4.104e-05
Full six-token solve: 10 19.2480316 token/scalar 0.999828507 mesh error 1.274e-05
Full six-token solve: 14 159.656205 token/scalar 0.999976064 mesh error 5.624e-07
Full six-token solve: 18 1543.62139 token/scalar 0.999994235 mesh error 1.010e-07
Concentration sufficient derivative bounds: [(500, -0.863807204), (1000, -0.959970992), (2000, -0.95999)]
Isolated skew group: beta, width power, beta*center shift
20 0.5 0.000167729663
20 1.0 1.87856583e-06
80 0.5 0.000335482445
80 1.0 4.69674333e-07
320 0.5 0.00067097645
320 1.0 1.17420543e-07
All checks passed. elapsed=3.817s; peak RSS=16.28 MiB; nice=20
```

The full six-token solves used unequal conditional token weights in both groups, total group masses .2 and .8, and initial diameter .2/beta. The two RK4 time steps were .1 and .05; maximum relative hitting-time discrepancy was 4.105e-5. The high-beta width checks used .2/sqrt(beta) and ran only to time 20, not to the inaccessible exponential hitting time; equation (22), not this finite-time experiment, supplies the long-time theorem. The derivative identity was independently checked by centered finite differences at beta=20,80,320. All data are in verification.json. These are floating-point checks, not certificates.

The isolated skew-group test tries to break a stronger prefactor assertion. At diameter .2/sqrt(beta), the observed beta times initial-relaxation center shift doubles when beta increases by four; at diameter .2/beta it decreases by four. This is consistent with the beta w_0^3 displacement bound and explains why the proof requires an additional width condition for the prefactor. It is not asserted as a rigorous counterexample to all possible broader prefactor theorems.

## 8. Final audit and deliverables

Read the saved proof and numerical data in full. Rechecked the sign of the mean cancellation, both group-mass factors in (12), the reciprocal-denominator estimate, and the time-sandwich orientation. The internal drift bound for one group has coefficient (beta/2) exp(1/16); adding both gives C_0=exp(1/16), as stated. The width and cross-attention estimates are valid throughout the stopped interval, and the finite-hitting conclusion follows from a uniform negative center-gap speed after t_0 rather than being assumed. No mathematical counterexample satisfying all large-beta hypotheses was found.

Wrote LITERATURE.md and REPORT.md. The theorem extends the earlier exact-atom result to two compact groups of nonzero width, uniformly in token count, with a mean-field version. The result remains partial relative to T324. No generic cluster count, multiple-merger sequence, or independent-token noisy reduction was proved. No earlier folder or external state was edited.

Final artifact audit: `head -1 REPORT.md; wc -l REPORT.md PROOF.md LOG.md LITERATURE.md verify.py verification.json; ls -lh REPORT.md PROOF.md LOG.md LITERATURE.md verify.py verification.json` exited 0. REPORT.md begins with the required verdict. All six deliverables exist in this folder and total less than 60 KiB. No additional computation was needed after the passing run.
