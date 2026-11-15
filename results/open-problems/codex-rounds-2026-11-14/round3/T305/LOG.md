# T305 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Task received: 15 November 2026, approximately 03:45 Asia/Tbilisi (orientation clock; exact prompt receipt unavailable).

## Orientation and earlier-result audit

Read the earlier REPORT.md, LOG.md, PROOF.md, and the full audit.py in
~/codex_op_1114/briefs/T305, without editing that folder.
Read startup memory and the compute snapshot: status warn, owner_away_open,
shared CPU saturated. Only tiny one-thread computations are planned.
All shell Python commands use nice -n 15 and single-thread environment
variables. The inherited nice value will be checked in the audit script.
The task's folder-only rule overrides global mesh, checklist, and memory
writes, so no commands that update those external stores are run.
No subagents, git, accounts, or external messages.

Independently re-derived the earlier variance identity directly: condition
on X in 24A=2p^TKp-S, giving
576 Var(A)=8 E tr(K²)+Var(2D-S). Integration by parts of gD and Kg
gives E(D²-DS)=E tr(K²)-E(g^TKg); inserting this into the direct
fourth-moment expansion gives exactly the reported identity. The lower
bound follows by conditional variance, and the upper bound follows from
Var(S)<=4 E(g^TKg). Rechecked the change-of-variables mgf argument
for both signs and its Chernoff constants; no error found. Thus the earlier
result holds on this independent paper check. A separate numerical audit
will verify the variance and finite-step signs without executing the old
script (which writes into its own folder).

## Bounded literature check

Search started with orientation and completed within five minutes. Web
queries included “Metropolized Hamiltonian Monte Carlo operator norm Hessian
Lipschitz dimension 1/4 2026”, the source identifier, and “Hamiltonian
smoothing ZAC26”. Opened the original source's current HTML,
https://arxiv.org/html/2304.04724v3 (Yuansi Chen, Khashayar Gatmiry,
Minhui Jiang), section 2.4 and Table 1: still explicitly Frobenius regularity.
Also opened arXiv pages/HTML for 2607.00586v2 and 2609.06906. These concern
scaling identities and a different smoothed integrator, respectively. No
settlement of T305 was located in this bounded search; this is not a
comprehensive priority search. Full bibliographic scope will be in REPORT.md.

## Chosen extension (before implementation)

Derive a sharp finite-step law for the exact-flow-subtracted remainder R
on all Gaussian targets with spectrum in [m,L], including explicit warm
tails. In particular, determine whether R vanishes at h~d^(-1/4), or
whether it has an unavoidable deterministic drift already for the standard
Gaussian. This directly tests the previous report's proposed next step and
clarifies the scale a possible general remainder lemma must allow. The
result will be a finite-step remainder theorem and obstruction to an o(1)
remainder claim, not a counterexample to the desired HMC mixing rate.

Log initialized: 2026-11-15T03:46:52+04:00.

## 2026-11-15 03:51 +04 — finite-step formulas derived

For one Gaussian precision lambda, put a=h² lambda/4, r=sqrt(1-a),
phi=2n asin(h sqrt(lambda)/2), tau=T sqrt(lambda),
v=(cos(phi),sin(phi)/r), w=(cos(tau),sin(tau)). In standardized
coordinates u=(sqrt(lambda)x,p), the exact remainder is

    R=u^T E u,   E=(a/2)(vv^T-ww^T).

Its stationary mean is exactly

    mu=sum_i h^4 lambda_i² sin²(phi_i)/(32(1-h² lambda_i/4)).

For h sqrt(L)<=1, the block operator norm is at most
b=h^4 L²(1+T sqrt(L))/8. Thus the centered remainder is bounded with
probability 1-delta from an M0-warm position start by

    |R-mu| <= 2b sqrt(2d s)+2b s,  s=log(2M0/delta).

At the critical scale d h^4 -> ell^4, the standard Gaussian has
R -> ell^4 sin²(T)/32 in L2 at stationarity, and in probability for
log(M0)=o(d). So a vanishing uncentered remainder is impossible in
general, even with constant Hessian. This does not contradict the earlier
report, which requested a bound, not an o(1) bound. It is not a
counterexample to d^(1/4) HMC.

A general identity explains the drift: for every volume-preserving
leapfrog map S, E_rho R=E_rho DeltaH=KL(S_#rho || rho), since the exact
flow preserves rho and the Jacobian of S is one. This will be proved
with integrability justification. The same finite-step remainder theorem
will include this identity as its structural interpretation.

Next: write PROOF.md and independently audit with exact rational matrix
powers, direct kick/drift iteration, Gaussian fourth moments, and a
non-Gaussian quadrature check of the earlier identity.

## 2026-11-15T03:51:33+04:00 — proof and independent audit saved

Wrote PROOF.md with the full-class entropy identity, the finite-step
Gaussian remainder formula, an explicit M0-warm tail bound, and the
critical-scale positive-limit example. Wrote a new standard-library
audit.py; no old scripts were executed and no old files were modified.

Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py > audit_output.txt 2>&1
```

Output:

```text
nice: setpriority: Operation not permitted
PASS: earlier variance identity by independent asymmetric 1D quadrature
  max residual: 6.938893903907228e-18
PASS: exact rational invariant, direct leapfrog, two drift formulas, energy variance, exponential identity
PASS: finite-step matrix theorem in 61 cases
  max pointwise residual: 4.9461051116486904e-15
  max drift/entropy residual: 2.261472217617335e-16
  max operator norm / proved bound: 0.14898876065995623
Critical scale T=1, h=1/n, d=n^4:
n d mean_R sd_R variance_DeltaH
4 256 0.0225541369291 0.0025287 0.0451122479917
8 4096 0.0222326674398 0.000624649 0.0444655762329
16 65536 0.022153555267 0.000155699 0.0443071255114
32 1048576 0.0221338544311 3.88959e-05 0.0442677097966
64 16777216 0.0221289340285 9.72217e-06 0.0442578681153
128 268435456 0.0221277042279 2.43043e-06 0.0442554084594
256 4294967296 0.0221273967965 6.07601e-07 0.0442547935933
mean limit: 0.0221272943210491
PASS: T=pi resonance tends to zero; positive-limit exception checked
Resources: {"nice": 20, "python_threads": 1, "elapsed_seconds": 0.024099834030494094, "max_rss_bytes_macos": 19202048}
```

The nice wrapper warning is explained by the inherited nice value 20,
verified inside the script. The run used one Python thread, about
19.2 MB maximum RSS, and 0.024 seconds measured inside Python. No arrays
in the displayed dimensions are allocated: d is a scalar multiplier of
2-by-2 covariance calculations. The largest represented d is 2^32.

Earlier result recheck: the variance identity agrees independently on
V(x)=x²/2+0.3(1-cos x)+0.25(sin x-x), with Hessian in [0.45,1.55].
Composite Simpson grids of 4096 and 8192 intervals on [-12,12] agree;
the identity residual is 6.939e-18. This is a floating-point check, not
a certified quadrature proof. Exact rational Gaussian-square variance
separately gives 5 lambda²/288, as previously claimed.

Self-audit / attempts to break the new claim:

1. Derived DeltaH from the exactly preserved quadratic form, and checked
   it separately by direct rational kick/drift iterations.
2. Derived the mean from E(y_n²-y²), then independently from the Gaussian
   relative entropy formula using the powered leapfrog matrix. Maximum
   discrepancy over 61 finite-step cases: 2.262e-16.
3. Exact rational algebra checks det(C^n)=1 and E exp(-DeltaH)=1 through
   det(I+2 Sigma D)=1. It also checks Var(DeltaH)=2mu+2mu² for each
   coordinate, separately from the remainder matrix calculation.
4. Reconstructed R directly from energies and A at the exact endpoint,
   instead of using the invariant. Maximum residual: 4.947e-15.
5. Tested precisions 0.25,1,1.7,4; times 0.3,1,pi,6; step counts
   1,2,7,16,31 subject to h sqrt(lambda)<=1, including the boundary.
   The operator bound is conservative: maximum observed ratio 0.149.
6. The positive-limit assertion excludes resonance. At T=pi the mean
   remainder tends to zero; the script checks this separately.
7. The tail bound is centered at the stationary mu even under a warm
   start; it does not silently substitute a numerical stationary law or
   claim that the warm mean equals mu. The factor M0 is explicit.
8. The entropy identity is for the unadjusted, pre-accept/reject proposal.
   Applying it to the Metropolized endpoint would be wrong: that kernel
   is stationary at rho and includes rejections.

No failure of the earlier theorem was found. The route that fails is
trying to make the exact-flow-subtracted remainder o(1) at critical
steps: its expectation is asymptotically sin²(1)/32 for the standard
Gaussian, and its variance vanishes. The correct remainder target must
allow at least an O(dh^4) drift. This is compatible with constant
acceptance and does not disprove the conjectured exponent.

## 2026-11-15T03:53:40+04:00 — final mathematical and artifact review

Added the stationary rejection identity
E r=TV(S_#rho,rho)<=sqrt(E R/2), with a proof from change of variables
and the binary relative entropy inequality. Rechecked the orientation
of S versus S^-1: their two TV expressions agree after pushing both
measures through S. This concerns the unadjusted proposal, and the
REPORT explicitly retains the M0 loss for a naive warm average transfer.

REPORT.md records the partial verdict, new theorem, command, limitations,
opened references, resonance exception, and next suggested entropy bound.
Final checks confirmed all six expected artifacts exist, the required
verdict is the first line, the audit JSON contains all 61 cases, and the
resource record has one Python thread. The final proof edits only added
an analytic corollary; no numerical implementation changed after the
passing audit. No additional or broader tests were needed.

Unresolved: the original uniform operator-norm class and logarithmic warm
dependence. No claim that T305 is solved or that the Gaussian obstruction
is a lower bound on mixing complexity.
