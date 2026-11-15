# T185 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
First local clock reading: 15 November 2026, 05:01:45 Asia/Tbilisi.
The exact prompt receipt time is unavailable.

## Orientation and scope

All writes stay in this folder. The task-specific restriction overrides the
global requests to mutate the shared brain, mesh and checklist. Those systems
are not updated. No git, subagents, external messages or accounts are used.
Read the startup instructions at `~/.claude/brain_startup.md` and the compute
state. The latter reports `warn`, `owner_away_open`, CPU saturation, ample
available memory. Only short single-thread checks are planned. The requested
`nice -n 15` wrapper prints `setpriority: Operation not permitted`; the
verification script will query its actual priority and report resource use.

Read the first session's REPORT.md, PROOF.md, LOG.md and check_certificate.py,
and round 3's PROOF.md. Remaining round 3 log/script reads follow below.

## Literature check (first five minutes)

Queries included `"alpha fair" "general" "stability" "2025" bandwidth`,
`"bandwidth sharing" "positive recurrence" "general" 2026`,
`"Fu" "Williams" "Stability of a subcritical fluid" stochastic`,
`"bandwidth sharing" "general file" stability after:2023-01-01`, and
`"alpha-fair" "positive Harris" general distributions`.

Opened Yingjia Fu and Ruth J. Williams's *Asymptotic behavior of a critical
fluid model for bandwidth sharing with general file size distributions*
(2022), https://mathweb.ucsd.edu/~williams/bandwidth/AAP1723forposting.pdf,
and Maria Vlasiou, Jiheng Zhang and Bert Zwart's *Insensitivity of
Proportional Fairness in Critically Loaded Bandwidth Sharing Networks*,
https://arxiv.org/abs/1411.4841. No later unrestricted stochastic stability
theorem was found. The first concerns critical fluid behavior; the second
concerns a dense class of file-size distributions in heavy traffic. Its
abstract does not identify this class as phase-type. This limited search
does not certify absence of a solution. The authors' publication-page fetch
returned HTTP 502. No solved-elsewhere claim is made.

## Independent rederivation of the earlier claim

For the earlier states with N through files of residual 1 and N^3 local
files of residual N^-4 on branch j, put a_i=kappa_i^(1/alpha). Directly
differentiate the two-route strictly concave allocation objective:
Lambda_0/(1-Lambda_0)=a_0 N/(a_j N^3). Thus service tends to e_j, while
W/N=e_0+N^-2 e_j tends to e_0. For homogeneous F of degree d with gradient
g at e_0, scale its arrival finite differences using their line integrals.
The two generator limits are nu.g-g_1 and nu.g-g_2. Their sum is
(2/5)g_0=(2/5)dF(e_0)>0. The larger is
dF(e_0)/5+|g_1-g_2|/2. This independently reproduces the main obstruction,
including d<1 and unequal positive weights. No error found.

## Chosen next piece (before proving it)

Prove a fixed-horizon expected drift formula for the maximum link workload
M=W_0+max(W_1,W_2), uniformly over the two hostile sequences (and, if the
proof permits, their accessible perturbations). Keep deterministic unit
arrivals and the local files arriving after the original tiny files clear.
The candidate limit is

    E[M(X_N(T))-M(X_N(0))]
      -> -(4/5)T + E max(P_1(T),P_2(T)),

where P_1,P_2 are independent Poisson processes of rates 1/2. Its upper
bound is -(3/10)T+(1/2)sqrt(T), negative for T>25/9. This directly tests
the next lemma named by round 3. It is a local asymptotic lemma, not a
recurrence proof for arbitrary states.

## Proof development

Finished reading both earlier reports, proofs, logs, scripts and audits.
The first script and the first session's output were read in the initial
batched tool response; the round 3 script and log were read in full in a
subsequent response. The symbolic rederivation above checks round 3 directly
rather than executing a script that would write into its protected folder.

The two-link allocation with n_0>0 has the explicit formula
Lambda_0=a_0 n_0/(a_0 n_0+H), where
H=(kappa_1 n_1^alpha+kappa_2 n_2^alpha)^(1/alpha).
Each occupied local route has rate 1-Lambda_0. This gives a lower bound on
every original local file's service rate using the *total arrival counts*
up to the fixed horizon. Consequently all initial local files clear by a
random upper bound of expected order N^-1. After that time the local
counts are bounded by the new Poisson counts, and cumulative loss of
through service is bounded by another term of expected order N^-1.

The proof works uniformly in a slightly larger class: N original through
files with residuals in [1-N^-8,1], and at most N^3 original local files
across both branches, all of residual at most N^-4. It includes both hostile
sequences and all the accessible perturbations from round 3. No assertion
uniform in alpha or the positive weights is intended.

Writing I_N=integral_0^T(1-Lambda_0(s)) ds and m=max(W_1(0),W_2(0)),
workload balance gives the useful pathwise sandwich

    -m <= Delta M - [A_0(T)-T+max(A_1(T),A_2(T))] <= I_N.

It retains actual unit jumps. The proposed expected limit follows once
E I_N -> 0; no exchange of a generator limit and a fixed-time limit is used.
The error calculation and all constants are now being independently checked.

## Exact verification run

Saved the complete argument in PROOF.md and the standard-library script
check_sampled_drift.py. Command:

```sh
nice -n 15 env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 check_sampled_drift.py
```

Exit code 0: `all exact checks passed`. Output is saved in
sampled_drift_checks.json. Arithmetic time 0.1249 seconds, peak RSS
15,892,480 bytes, actual nice 20, CPU limit 60 seconds. No numerical worker,
GPU, external library or subprocess was used. The nice wrapper warning
does not change the measured inherited priority.

Output that matters:

- The old obstruction's averaged-gradient identity passed 27 exact checks,
  with positive and negative local derivatives. The symbolic argument covers
  all admissible gradients and degrees, not just these checks.
- Two independent rational-series methods enclose d(4) in
  [-0.428494478548, -0.428494478547]: conditional symmetric random walk
  (71 terms) and a separate double Poisson sum (1,681 terms). Exponential
  factors and omitted tails have rational enclosures; no floating-point
  value is used to certify the sign.
- The elementary bound is d(4)<=-1/5. With equal weights and alpha=1,
  epsilon_200(4)=340000261/2000000000=0.1700001305. Thus every initial state
  in C_N, for every N>=200, has expected four-time-unit increment at most
  -59999739/2000000000=-0.0299998695.
- 360 exact, deterministic cohort paths (2,477 events) checked the clearing
  bound with early and simultaneous arrivals, service-loss integration,
  the workload sandwich and an independent identity: maximum link workload
  drains at rate one between arrivals. The paths include both old hostile
  branches, mixed branches, unequal local residuals, no original locals,
  unequal weights and weight ratio 10,000. These paths test the alpha=1
  algebra; the proof, not this finite check, covers all alpha>0.

No mathematical check failed. One earlier text-only patch failed to match
its context and made no change; it was corrected. The initial wording
that the opened arXiv abstract specifies phase-type distributions was
removed: the abstract says a dense class, which is all it justifies.

## Independent audit found a stronger bound for the same sampled lemma

An alternative charging argument can remove the initial count and individual
local-residual restrictions. At any time write o_j and m_j for original and
new local counts. Put q=1-Lambda_0. Service to original locals is
q*sum_j(o_j/n_j), with absent terms zero. If just one local route is present,
the remaining fraction is m_j/n_j. If both are present, its positive part
is theta=(m_1/n_1+m_2/n_2-1)^+, which is at most each m_j/n_j. By monotonicity
and homogeneity, theta*H(n_1,n_2)<=H(m_1,m_2). Hence

    q <= [service rate to original locals] + b*(m_1+m_2)/(a_0*n_0).

For unit files, n_0(t)>=W_0(t)>=W_0(0)-T. Integrating the displayed bound
therefore gives

    E I_N(T) <= W_1(0)+W_2(0) + b*T^2/[a_0*(W_0(0)-T)]

whenever W_0(0)>T. This is the same chosen sampled-drift piece, with a wider
initial-state class. The original clearing proof remains an independent
verification on C_N. The stronger bound will be proved in full and checked
against the exact cohort paths before it is reported.

## Wider version verified

Saved section 7 of PROOF.md with every step of the service charging bound.
Using the arrival counts at time s rather than their terminal values
sharpens the expected area from T^2 to T^2/2. The resulting estimate, for
every initial state with residuals <=1 and W_0(0)>T, is

    d(T)-max(W_1(0),W_2(0)) <= E Delta M
       <= d(T)+w+c*T^2/[2*a_0*(W_0(0)-T)],

where w=W_1(0)+W_2(0), and H(u)<=c*(u_1+u_2). One can use c=b for every
alpha and c=1 for equal weights with alpha=1. Thus the same fixed-horizon
limit holds uniformly over all finite states with residuals <=1,
W_0>=N-1 and w<=1/N, with no initial count restriction. At T=4,
equal weights and alpha=1, every N>=100 has expected drift at most
-201/1900, approximately -0.10578947. Both old hostile branches and their
accessible perturbations lie in this family.

The script was rerun after adding service-accounting and departure tests,
then once more after the area refinement. All runs passed. The final run
used the same command above: 504 paths, 3,554 cohort events, 0.222 seconds,
15,876,096 bytes peak RSS, actual nice 20, CPU limit 60 seconds. It checks
the exact identity -1/5+1/100+8/95=-201/1900. The previous N=200 bound
and all Poisson enclosures remain unchanged. AUDIT.md contains the
independent derivation of the factor 1/2 and the new rational constant.

One extra read obtained the first session's LOG.md and check_certificate.py
in an untruncated response; their contents agree with the earlier reads.
No earlier files were changed.

## Final audit and handoff

Saved REPORT.md with the required PARTIAL verdict. Read PROOF.md and
REPORT.md back in full. The final statement includes the wider class D_N,
the refined factor 1/2, the constant -201/1900, and the original accessible
sets. The older N=200 clearing estimate is retained as an independent,
weaker bound. The two calculations agree; no mathematical gap was found.

The remaining limitation is substantial initial local work and the absence
of an all-large-states recurrence estimate. The report proposes that next
step in the same deterministic-unit-file two-link network, rather than
claiming the unrestricted T185 theorem. Final read-back clock:
15 November 2026, 05:16:43 Asia/Tbilisi. All new artifacts are in this folder:
LOG.md, PROOF.md, AUDIT.md, REPORT.md, check_sampled_drift.py and
sampled_drift_checks.json. No further run is needed after documentation-only
edits; the last script run passed all exact checks.
