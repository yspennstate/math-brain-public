# T428 work log

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, 09:22 +04 (first recorded local clock).

## 1. Orientation and scope

Read the three earlier folders without editing them. The current task's explicit folder-only rule overrides global requests to mutate the shared brain, mesh, or checklist; those stateful commands are not run. Read the memory index and mesh protocol instead. No git, no subagents, no background processes. All new artifacts stay here.

Commands: `pwd`; `rg --files`; `ls -l` on the three supplied folders; `cat ~/.claude/compute/compute_state.json`; `date '+%Y-%m-%d %H:%M:%S %z'`; reads of the prior reports, logs, proofs and scripts. Compute state at entry: status ok, mode owner_away_open, 73 percent free memory. Only small scalar computations are planned, at nice 15 or lower priority with all numerical thread settings one.

## 2. Literature check (under five minutes)

Used the web search tool for `"2609.15832" "Conjecture 1.17"` and `"critical" "stochastic heat flow" "signed" "Drillick"`; opened https://arxiv.org/abs/2609.15832 and https://arxiv.org/html/2609.15832v1. The arXiv record lists only v1, 14 September 2026. The target authors are Hindy Drillick, Jonathan Hou and Shalin Parekh.

Also opened https://arxiv.org/abs/2610.31614, *The Critical 2D KPZ Process*, by Quentin Berger, Francesco Caravenna, Jeremy Clark, Alexander Dunlap, Yu Gu, Ziyang Liu, Shuta Nakajima, Rongfeng Sun, Li-Cheng Tsai, Zuodi Xie and Nikos Zygouras. Its abstract describes a renormalised Cole–Hopf construction, not the requested signed-kernel universality extension. This is not grounds to declare T428 solved elsewhere. No resolution of the precise extension was found in this bounded search.

The HTML was checked at lines 574–579: Conjecture 1.17 is still explicitly stated. The bounded literature check is complete.

## 3. Independent re-check of the previous result

The round 4 theorem holds on re-derivation. An independent block elimination checks its transform input. Write mu=m/(4 pi), P=u tensor v/m, and K for the weighted logarithmic kernel. Then P K P=(I_f/m)P. The sharp eigenvalue is mu+I_f/(m L)+O(L^-2). The damping correction is (-gamma-log z)mu P. Consequently, after the original tuning, the scalar block of I-B_N on range(P) is (log z+gamma-theta-epsilon_N)/L+O(L^-2). The two off-diagonal blocks are O(L^-1) and the complementary inverse is bounded. Eliminating that block changes the scalar by O(L^-2), confirming the cancellation without using the previous spectral-projection formula for the inverse.

Independently reconstruct the time limit by scalar quadratic forms: for each unit vector h, <h,e^-bt F_N(t)J h> is nonnegative and decreasing. Polynomial tests in e^-t converge from the real Laplace transforms. Their uniform approximation errors are bounded by eta times ||integral e^-bt F_N(t)J dt||, uniformly in h. Before/after time averages then squeeze the quadratic forms with an error independent of h. Taking the supremum over h gives operator norm convergence. A finite partition gives local uniformity. This also checks that no bound on integral ||F_N(t)|| dt is silently being used. J must equal 1 at zeros of f.

No defect was found. Re-running the old scripts in their original folders would overwrite old JSON files, so fresh independent scalar checks will be written here instead.

## 4. Choice of one extension (before proof)

Prove the round 4 time theorem uniformly over all real measurable Brownian profiles f with a common envelope C exp(-a|x|) and integral at least m_0>0. Equivalently, allow an arbitrary triangular array f_N with those bounds, without convergence of f_N, P_N or its sign multiplier. Retain each profile's sharp-time Lambda_N and its original critical tuning. The conclusion is sup_[delta,T] ||N R_N(Nt)/L-g_theta(t)P_N|| -> 0, and the associated continuous-time-test convergence with moving P_N.

Why this piece: it is exactly the concrete next task in the round 4 report. The delicate point is not merely calling fixed-profile constants uniform: one must bound the nonorthogonal projections, the perturbation contours, all weighted kernel remainders and the polynomial/order reconstruction independently of f. No compactness or convergence of the profiles will be assumed.

Planned independent audit: explicit envelope moments 2 pi C (k+1)!/a^(k+2); uniform block elimination; moving positive rank-one targets in the order squeeze; scalar tests for several signed Gaussian mixtures, including a nonconvergent sequence of profiles. No new stochastic-flow or KPZ claim is intended.

## 5. Uniform proof written

Wrote PROOF.md with a class-uniform statement, stronger than a single triangular-array statement. The supremum is over all profiles with the common envelope and mass >=m_0, and over tuning errors |epsilon|<=e_N tending uniformly to zero. Every contour and error threshold is chosen using only C,a,m_0 (and the stated time or transform parameters).

The proof explicitly bounds the fourth separation moment by 16 M_0 M_4, the second by 4 M_0 M_2, the projection norm by M_0/m_0 and the spectral separation by m_0/(4 pi). The logarithmic kernel's near-diagonal square integral is controlled by boundedness of f and the planar log-square integral, independently of f. The tuned real-axis transform error is O_z(1/log N+e_N).

The key new time step retains the moving positive target A_f=P_f J_f. The family e^-bt g_theta(t) A_f has a common modulus of continuity because ||A_f||<=M_0/m_0. The same polynomial, before/after averages and finite time partition work for every f and every allowed tuning error. Neither the profiles nor their sign multipliers are required to converge.

Audit begun: recomputed the sharp-time coefficient by a uniform Schur complement; it again has denominator (log z+gamma-theta-epsilon)/L+O(L^-2). Also checked the necessity of the proof's lower mass bound by f_delta=(1+delta)phi_1-phi_2: its mass tends to zero while its absolute mass stays away from zero, making ||P_f|| unbounded. This does not refute the original conjecture.

NEXT: fresh scalar checks here, then adversarial audit of all uniform quantifiers and final REPORT.md.

## 6. Fresh scalar verification passed

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 -B verify.py
```

Exit 0. Complete numerical output is verification.json. Scalar mpmath arithmetic, 45 digits, tolerance 1e-32, no arrays or workers, 90-second CPU cap. Wall time 0.781 seconds, peak RSS 26,968,064 bytes, all four thread settings one. The wrapper reported `nice: setpriority: Operation not permitted`; the script checks priority before numerical work and libc reported inherited nice 20, errno zero. Thus the actual priority meets the author's limit.

Results that matter:

- The common envelope for f_b=(1+b)phi_1-b phi_2, 0<=b<=3, is C=1.69855054462490385567205757914369834, a=1. Its envelope moments M_0,M_1,M_2,M_4 were independently integrated; maximum equality error 2.81e-45.
- Four signed-family constants, from both radial Gaussian logarithmic moments and independently renormalized rational heat integrals, agree with 2b(1+b)log(3/2)-b^2 log 2. At b=0,1/4,1,3 they are respectively 0, 0.210093993782606156897681189574082175, 0.928713251872712218494820340399219978, 3.49283796955643738271722567802079017. The b=1 value independently rechecks log(81/32).
- Twelve finite-N overlaps (N=100,10000,1000000 for each b) agree with exact sharp/exponentially damped formulas to less than 7.57e-44. Every sharp finite-part error is below the common bound 70/N, derived from sum |weight| times its shift. This is a matrix-element check, not a computation of Lambda_N.
- Exact projection norms, independently integrated radially across the changing sign, are 1,1.025,1.25,2.125. The formula is 1+b^2/[2(1+b)].
- For the lower-mass obstruction f_delta=(1+delta)phi_1-phi_2, the independent absolute-mass integrals agree with delta+1/[2(1+delta)]. Projection norms for delta=1,0.1,0.01,0.001 are 1.25,5.5454545...,50.5049505...,500.5004995.... This confirms divergence when the lower mass bound is dropped.
- Four gamma-integral versus pole/branch time-density checks (theta=0 or 0.7, t=0.05 or 1) agree to at most 3.51e-46. At theta=0,t=1 the value is 1.07462362226026949694805089628804418, independently rechecking the previous time normalization.

No assertion failed. Compute state was re-read before the run: ok, owner_away_open, 83 percent free memory. The calculation remained small despite high machine-wide CPU load.

## 7. Adversarial audit

Re-derived every class-dependent factor. Polar coordinates give M_k=2 pi C Gamma(k+2)/a^(k+2). Independently, scaling r -> r/a in the radial integral fixes the exponent a^(-k-2); repeated integration by parts gives (k+1)!. The separation inequality gives 2^(k-1) times two identical terms M_0 M_k, hence 2^k M_0 M_k, confirming the factors 4 and 16 used in the transform and sharp-time errors. Each weighted remainder bound is a Hilbert–Schmidt estimate before conversion to operator norm.

Uniform spectral audit: the contour radius mu_-/4 is fixed for the entire class. The resolvent bound is (1+2 kappa)/r, with kappa=M_0/m_0. Normalizing the eigenvector divides by ell(Pi u), whose error from m is at most M_0||Pi-P||; the common lower mass bound makes the denominator at least m_0/2 after one uniform threshold. No hidden pointwise-in-f spectral gap or eigenvector constant is left. The same argument about the fixed eigenvalue 1 applies to B_N(z). Uniform errors |epsilon|<=e_N are essential when taking a supremum over the whole class.

Time audit: independently apply the polynomial error bound to scalar quadratic forms for all unit vectors. Positivity bounds each error by rho times the common total-mass norm; taking the supremum in the vector therefore gives norm convergence with a common error. Before/after averages compare to the moving h_b(t)A_f, with common modulus kappa|h_b(s)-h_b(t)|. There is no fixed projection limit anywhere in this step. The finite partition is chosen before f, and the supremum over f commutes with the finite endpoint maximum. Highly oscillatory profiles, changing zero sets, and alternating f_N are allowed: no derivative, profile convergence or sign convergence was used.

The sign multiplier equals 1 at zeros. Its norm is exactly one; multiplying by it neither enlarges errors nor changes the signed potential alpha f. The spectral sandwich is positive as a Hilbert-space operator because the generator is self-adjoint, not because f is pointwise positive. Only the endpoint sign is removed. A nonsymmetric generator would invalidate this argument.

Independently recomputed the illustrative constants by elementary radial tail masses. For A phi_1-B phi_2, its zero is r^2=4 log(2A/B), and its negative tail mass is B^2/(4A). This yields both the bounded projection norms for f_b and the divergent norms for f_delta. The uniform scalar sharp-overlap remainder is bounded by [(1+b)^2+3b(1+b)+2b^2]/N=(1+5b+6b^2)/N<=70/N, agreeing with all twelve tests. The b=1 first-order scalar remainder cancels, consistent with its observed N^-2 behavior.

Attempted overextensions and limits:

- No uniform claim down to t=0: F_N(0)=(N alpha/L)M_f has norm of order N/L^2 for fixed nonzero f.
- No removal of the positive lower mass bound: the exact f_delta example makes the projection norms diverge.
- No replacement of the signed profile by its absolute value: that changes the leading mass and tuning, and can yield a much larger spectral growth rate.
- No inference from a positive total operator mass to an integral of operator norms. The latter remains a separate small-time problem.
- No full-flow conclusion: spatial endpoints, general gap processes and higher moments have not been proved here.

No defect in the earlier theorem or this uniform extension was found. No numerical assertion failed. The proof's final additions spell out exact scalar tail formulas; they do not change the computation or require it to be repeated.

## 8. Final artifact audit and result

Wrote REPORT.md with the required first line `VERDICT: PARTIAL Uniform time-resolved Brownian signed pair limit for N-dependent profiles with unchanged critical tuning`. It states the additional lower mass assumption, the full uniform quantifiers, the unchanged sharp-time tuning, the limits of the result, and one concrete next target: uniform small-time integrability of the operator norm.

Ran a short read-only standard-library Python audit under the same four single-thread settings, `PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 -B -`. It checked the five nonempty artifacts, report verdict, script syntax using ast.parse without bytecode output, JSON parsing, RSS and priority limits, and 48 saved exact-equality errors. Output:

```text
Artifact audit passed.
Exact-equality errors checked: 48
Maximum saved equality error: 7.567011707354012e-44
Numerical computation was not repeated.
```

Exit 0. The wrapper again reported the refused extra priority increment; the recorded computation's actual nice value is 20. All new artifacts are inside this folder; the three earlier folders were read only. Completed one extension, the class-uniform Brownian signed pair theorem. The stochastic-flow conjecture remains unproved here.
