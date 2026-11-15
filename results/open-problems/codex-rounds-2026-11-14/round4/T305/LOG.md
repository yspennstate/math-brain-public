# T305 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Task orientation clock: 15 November 2026, 06:31 Asia/Tbilisi
(02:31 UTC; exact prompt receipt time unavailable).

## Orientation and bounded literature check

Read both earlier folders' REPORT.md, LOG.md, PROOF.md and audit.py, without
executing their scripts, which write into their own folders. Read the brain
navigation/startup memory and compute snapshot. Shared CPU is saturated;
only small single-thread standard-library computations will be used.
The folder-only order overrides global mesh/checklist/memory mutations.
No subagents, git, external messages, or writes outside this folder.

Literature check: 02:31–02:34 UTC, within five minutes. Web searches used
the source identifier, Metropolized HMC/operator-norm Hessian Lipschitz,
and recent HMC dimension/warm-start papers. Opened 2304.04724v3,
2603.22741v1, 2607.00586v2, 2609.06906v2, and 2106.05480v2.
The source retains Frobenius regularity. The potentially relevant new
warm-start paper, Matthew S. Zhang, Jason M. Altschuler, Sinho Chewi,
Algorithmic warm starts for Hamiltonian Monte Carlo, arXiv:2603.22741v1,
also explicitly requires Frobenius-Lipschitz Hessians in Assumption 3.1
and Theorem 3.4. No settlement of T305 located in this bounded search.
The other opened pages concern product scaling, a different integrator,
and older lower bounds; none supplies a new settlement of this class.

## Independent recheck of earlier results

Re-derived the first report's variance identity by conditioning on X:
576 Var(A)=8 E tr(K²)+Var(2 tr(K)-|g|²). Integration by parts yields
E[(tr K)²-(tr K)|g|²]=E tr(K²)-E(g^T K g); substitution gives the stated
identity. The Brascamp–Lieb bound Var(|g|²)<=4 E(g^T K g) gives its upper
bound. No error found.

For round 3, volume preservation gives KL(S#rho||rho)=E DeltaH directly;
exact-flow invariance gives E(A-A o Phi_T)=0. Hence E R equals this KL.
Independently expanding the standardized Gaussian map C^n gives
E DeltaH=(||C^n||_F²-2)/2=a² sin²(phi)/(2(1-a)), a=h²lambda/4.
This agrees with its mean remainder and the critical limit sin²(T)/32
when d h^4->1. A new script will audit the signs and powers independently.

## Chosen extension — recorded before proof/implementation

Prove finite-step proposal entropy <= C d h^4 for nonquadratic potentials
that are sums of independent blocks of uniformly bounded size, assuming
only C² potentials and operator-Lipschitz Hessians in each block. Also
derive an explicit energy-error tail bound from every M0-warm start:

    |DeltaH-E_rho DeltaH| <= C[h² sqrt(d s)+h s],
    s=log(2M0/delta).

The route is deterministic local energy estimates plus the exact identity
E exp(-DeltaH)=1, then independence. It avoids fourth derivatives and
does not assume numerical endpoints are stationary. This extends round
3's Gaussian entropy computation to a nonquadratic special case, and
resolves the naive M0 loss for energy-error tails there. Bounded blocks
automatically satisfy a dimension-independent Frobenius condition, so
this is not a resolution of the full operator-norm class or a claim of
priority over the source theorem.

## 06:37 +04 — deterministic route and an additional identity

For one step put v=p-h g(x)/2, q=x+h v. Direct algebra gives

    DeltaH = V(q)-V(x)-(q-x)·(g(q)+g(x))/2
             +h²(|g(q)|²-|g(x)|²)/8.

The two usable bounds, summed along a bounded-time numerical trajectory,
are |DeltaH|<=B h²(W²+W³) and |DeltaH|<=D h W², W=|(x,p)| measured
from the block minimizer. B,D depend only on L,M and the time bound.
The second bound makes exponential moments integrable without claiming
that exp(c W³) is integrable.

Reversibility supplies a useful sharpening of the entropy argument:
E f(DeltaH)=E[e^(-DeltaH) f(-DeltaH)]. In particular,

    0 <= KL(S#rho||rho)=E DeltaH <= E(DeltaH)²/2.

Here E(DeltaH)² means E[(DeltaH)^2], not (E DeltaH)^2.
The upper bound follows from tanh(t/2)<=t/2 for t>=0, applied symmetrically.
It needs no exponential remainder estimate. Strong convexity bounds
E W^6 by C k³ in a k-dimensional position block, so entropy tensorizes
as C h^4 sum_j k_j³ <= C k0² d h^4. This gives polynomial dependence on
the block-size cap for the mean. Centered exponential tails will use
both deterministic bounds and have constants allowed to depend on k0.

## 06:39 +04 — proof and audit script saved

Wrote PROOF.md, including exact constants, the fluctuation identity,
the C^{2,1} local trapezoidal formula, radial moment bounds, tensorized
entropy, centered exponential moments, and warm-start tails. The proof
explicitly checks that bounded blocks still have a Frobenius bound.

The first attempted audit run stopped before any computation because
macOS rejected RLIMIT_AS=768 MB with `ValueError: current limit exceeds
maximum limit`, despite getrlimit reporting an unlimited ceiling.
Removed that unsupported guard. The script stores only a 401-entry
momentum grid, scalars, and small 2x2 matrices. CPU and wall limits remain
180 and 240 seconds, and peak RSS will be recorded and checked below 1 GB.
No substantive mathematical check failed in that startup attempt.

Command for all audit runs:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py > audit_output.txt 2>&1
```

The second startup run reached the Gaussian audit and caught an overly
tight hand-entered convergence tolerance (7e-9 at n=512). Re-derived the
finite-n bias independently: n²(mean-limit) tends to
sin²(1)/128+sin(2)/768, approximately 0.006716. Thus the actual error is
about 2.56e-8. Replaced the arbitrary tolerance by a check of this scaled
bias coefficient and an error bound 3e-8. No earlier theorem is contradicted.

## 06:40 +04 — first complete audit passed; quadrature limitation found

The audit completed in 4.181 seconds, one Python thread, maximum RSS
15,876,096 bytes, inherited nice 20. The `nice` wrapper warning is due to
the already lower inherited priority. Exact rational Gaussian means and
second moments agree with the prior formula, including the stability
boundary. The cubic trapezoid constant 1/12 is attained in an exact
rational check. Direct energy versus the local formula agrees below
2e-12 over zero, kink crossings, small steps, h=1 and a large state.

The nonquadratic potential used is

    U(x)=x²/2+0.4 F(|x|)+0.15(sin x-x),
    F(r)=r³/6 (r<=1), r²/2-r/2+1/6 (r>=1).

It has 0.85<=U''<=1.55 and Hessian Lipschitz constant <=0.55;
U''' jumps at 0 and +/-1. The reversibility-based mean/h^4 is
0.0395851, 0.0388367, 0.0386539, 0.0386085 for n=4,8,16,32
on the 400-interval grid. The second moment/h^4 is approximately twice
those values, consistent with (9) and a fourth-order mean drift.

Attempt to break the computation: the *direct* quadrature of the mean
is less stable, particularly at n=32: mean/h^4=0.0401102 on the fine
grid versus 0.0480563 on the coarse grid. Its cancellation error is
visible in E(exp(-Delta)-1)=-1.43e-9 on the fine grid, so direct
quadrature should not be presented as an accurate entropy estimate at
that step size. The reflected integrand -Delta*expm1(-Delta)/2 has
positive size h^4 and avoids that cancellation; its identity with the
mean is proved exactly. Refine n=32 once more to quantify the remaining
direct quadrature bias. These are numerical audits, not enclosures.

## 06:42 +04 — refined audit passed

Re-ran the command above after adding the 800-interval n=32 case and
independent rational/combinatorial checks for the radial moments and
Chernoff constants. Exact output:

```text
nice: setpriority: Operation not permitted
PASS: independent rational Gaussian mean, second moment, and prior critical drift
PASS: exact local energy identity and sharp cubic trapezoid constant
grid=200 n=4 mean/h4=0.0395583017 reflected/h4=0.0395857377 second/h4=0.0791941124 exp_res=1.07e-07
grid=200 n=8 mean/h4=0.0387606522 reflected/h4=0.0388383838 second/h4=0.0776781299 exp_res=1.9e-08
grid=200 n=16 mean/h4=0.0397857923 reflected/h4=0.0386580009 second/h4=0.0773160897 exp_res=-1.72e-08
grid=200 n=32 mean/h4=0.0480562615 reflected/h4=0.0386065804 second/h4=0.0772131678 exp_res=-9.01e-09
grid=400 n=4 mean/h4=0.0395809514 reflected/h4=0.0395850676 second/h4=0.0791927598 exp_res=1.61e-08
grid=400 n=8 mean/h4=0.038825235 reflected/h4=0.0388366634 second/h4=0.0776746859 exp_res=2.79e-09
grid=400 n=16 mean/h4=0.0387271478 reflected/h4=0.0386538951 second/h4=0.0773078747 exp_res=-1.12e-09
grid=400 n=32 mean/h4=0.0401102025 reflected/h4=0.0386085128 second/h4=0.0772170314 exp_res=-1.43e-09
grid=800 n=32 mean/h4=0.039191706 reflected/h4=0.0386081096 second/h4=0.0772162246 exp_res=-5.57e-10
PASS: C2,1 nonquadratic entropy/second-moment scaling and fluctuation identities
Resources: {"elapsed_seconds": 10.716166625032201, "max_rss_bytes_macos": 16121856, "nice": 20, "python_threads": 1}
```

The direct mean bias decreases under refinement but remains visible:
3.73761234435425e-8 direct versus 3.68195625680590e-8 reflected.
The reflected mean changes only 3.85e-13 from 400 to 800 intervals.
The reversal identity for the *second* moment has residual 6.29e-17 at
the finest n=32 grid. Neither the grid nor these residuals is a certified
integration bound. No further refinement is needed for the analytic result.

## Final independent mathematical audit

Rechecked round 3's centered remainder as well as its mean: the preserved
quadratic p²+(1-a)y², a=h²lambda/4, gives Delta=a(y_n²-y²)/2. Exact
energy conservation gives h²(A-A o Phi_T)=a(y_T²-y²)/2. Hence
R=a(y_n²-y_T²)/2, with coefficient matrix
(a/2)(v v^T-w w^T). With r=sqrt(1-a), h sqrt(lambda)<=1,
|v-w|<=a+a T sqrt(lambda)/3 and |v|+|w|<=5/2. Thus its norm is at most
5h^4lambda²(1+T sqrt(lambda)/3)/64, below the prior report's
h^4 L²(1+T sqrt(L))/8. Wick's formula gives Var(R)<=4d b²; diagonal
Gaussian integration supplies its stated two-sided tail. This independently
confirms the earlier remainder theorem's scale and constants. Its mean
limit and the finite-n bias were also checked by the new exact-moment code.

For the new coefficient 1/2 in the entropy bound, a second derivation is
to condition on |Delta|=a. The fluctuation identity makes the two signs
have weights in ratio exp(a), so their conditional mean is
a tanh(a/2)<=a²/2. Averaging yields E Delta<=E Delta²/2 again.

Checked the radial constants a second way by expanding sums of independent
Gaussian squares: in phase dimension 2k, fourth moment=4k(k+1), sixth
moment=8k(k+1)(k+2). These agree with the integration-by-parts recurrence.
The trapezoid factor 1/12 is checked by an exactly cubic segment:
U=x²/2+(2/5)x³/6, x=1/5 to q=4/5 gives defect -9/1250 exactly.
The h² gradient-square term in the local identity was separately recovered
by expanding (v-hg(q)/2)²-(v+hg(x)/2)².
The Chernoff threshold's exponent equals s in three exact rational tests.

Checked boundary and omitted cases: h=1, M=0, zero state, both directions
of crossing every Hessian kink, large states, unequal Gaussian precision,
and a nonproduct warm law. The last case needs only density domination;
independence is used under rho before warm transfer. The mean is always
the stationary mean. The centered exponential proof uses the coarse
quadratic estimate, not an unjustified exponential of a cubic polynomial.

The task remains partial. The failure to extend the argument to the full
class is explicit: treating all d coordinates as one block gives only
O(d³h^4) from the deterministic sixth moment, while tensorization is what
recovers O(dh^4). Bounded blocks satisfy Frobenius regularity with
constant sqrt(k0) M. No full-class result or mixing theorem is inferred.

REPORT.md now contains the required verdict, the result, reproduction
command, failures and quadrature limitation, exact scope, primary-source
links, and the proposed next second-moment lemma. All writes stayed here;
earlier folders and global coordination/memory stores were not changed.
