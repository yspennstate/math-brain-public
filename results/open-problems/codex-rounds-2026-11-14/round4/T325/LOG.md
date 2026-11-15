# T325 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, approximately 06:31 Asia/Tbilisi.

## 1. Orientation and bounded literature check

Read REPORT.md, LOG.md, SOLVED_ELSEWHERE.md in the first folder and
REPORT.md, LOG.md, PROOF.md, audit_scalar.py in the round-3 folder. The
first folder has no PROOF.md or numerical script. Read the startup memory
index and compute state. State: warn, owner_away_open, CPU saturated.
Only short, single-thread standard-library arithmetic will run.

All writes stay in this folder. The specific folder-only instruction
precludes shared brain, mesh, and checklist writes, so those services
are not invoked. No git, subagents, external mutations, or training jobs.

Read-only commands: pwd; rg --files in the two earlier folders; cat of
their deliverables and script; cat of the startup memory index and
compute_state.json; date '+%Y-%m-%d %H:%M:%S %Z'.

Initial web-tool queries:

- transformer multi layer linear attention gradient flow global convergence in context regression 2025 2026 random initialization
- "Can Looped Transformers Learn" gradient descent convergence untied
- "in-context" "untied" "gradient flow" convergence scalar transformer
- "transformer" "regression" "convergence" "November 2026"

Opened primary sources https://arxiv.org/html/2410.08292v1,
https://arxiv.org/abs/2501.16265, and https://arxiv.org/abs/2610.31089.
The latter still has the October 31 revision recorded previously. The
2501.16265 abstract concerns multi-head linear attention and merged versus
separate key/query parametrizations, not the requested untied-depth
convergence theorem. No inspected source changes the full-problem status.
The literature check is bounded to the initial five minutes, not an
exhaustive novelty claim.

## 2. Independent recheck and chosen extension

Re-derived the earlier two-step loss from the residual label-row update:
v_new=v+a S(w-v), S=sum_i x_i^2/n, hence
F_2=E[(1-aS)^2(1-bS)^2]. The moment recurrence is
m_(k+1)=(n+2k)m_k/n. Orthogonality of the optimal residual to S,S^2
gives coefficients 1,-2n/(n+2),n^2/[(n+2)(n+4)] and risk
8/[(n+2)(n+4)]. The earlier difference equation and negative curvature
at the diagonal have the stated signs. No defect found in the proof;
an independent exact-arithmetic audit will also check these identities.

Choice, before proceeding: extend this exact scalar, fixed-block model to
arbitrary finite depth L, with untied direct scalar step sizes. The key
observation is that splitting any repeated pair c,c into c+h,c-h changes
the loss by -2h^2 E[S^2(1-cS)^2 R(S)^2]+O(h^4), strictly negative.
This may handle the repeated-root obstruction named by round 3. Need
prove convergence of trajectories, rule out repeated-coordinate limits,
and derive the exact optimal polynomial and risk. A proof only for L=3
will be retained if the arbitrary-depth argument fails.

Additional sources opened during the initial five-minute check:

- Blake Bordelon, Mary Letey, Cengiz Pehlevan, *Theory of Scaling Laws for
  In-Context Regression: Depth, Width, Context and Time*,
  https://arxiv.org/html/2510.01098v1, Section 5.1 and Appendix G.1.
  Section 5.1 preserves balanced untied initializations and thereby
  reduces their dynamics to the recurrent model. This does not settle
  independently initialized finite-n scalar layers.
- Nicholas Barnfield, Subhabrata Sen, Pragya Sur, *Multi-layer
  Cross-attention is Provably Optimal for Multi-modal In-context
  Learning*, https://arxiv.org/html/2602.04872v4. The abstract and
  introduction explicitly restrict parameters and change the data model
  to multimodal latent factors. Not a solution to the requested setting.

Reran the earlier script read-only, suppressing bytecode:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T325/audit_scalar.py
```

Exit 0. Process nice 20; peak RSS 13.66 MiB; all moment, gradient, gap,
difference-equation, and token checks passed for n=1,2,3,5,10,100,1000.
The wrapper warns `nice: setpriority: Operation not permitted`, and the
script reports its optional address-space cap unavailable. Its explicit
priority assertion passes. This rerun supplements the independent hand
derivation above; the new script will use a different linear-system
derivation of the optimum.

## 3. Arbitrary-depth convergence mechanism

The pair-difference coefficient is positive near a collision at EVERY
bounded parameter vector, not just a stationary point. On a compact
sublevel set, continuity therefore gives a uniform collision neighborhood
where each small nonzero gap grows. This bounds every initial nonzero
gap away from zero for all future time. The coefficient map is then
uniformly invertible along the trajectory. Its strictly convex quadratic
loss yields a trajectory-dependent Polyak–Lojasiewicz inequality and
exponential convergence to the unique optimum in that ordering chamber.
No general analytic-gradient convergence theorem or stable-manifold
theorem is needed.

Candidate exact residual, with alpha=n/2 and rising factorial (z)_k:

    r_*(s)=sum_(k=0)^L (-1)^k binom(L,k) alpha^k s^k/(alpha+1)_k.

Orthogonality E[S^j r_*(S)]=0 for 1<=j<=L follows from an Lth finite
difference of a degree-(j-1) polynomial. Its L roots are positive and
simple by a sign-change argument using weight s times the gamma density.
The learned step sizes are their reciprocals. Candidate exact risk:

    L!/(alpha+1)_L = 2^L L! / product_(j=1)^L (n+2j).

Need audit both the finite-difference cancellation and constant, including
L=1,2, n=1, negative initial steps, zeros, and repeated initial steps.

## 4. Proof and independent arithmetic checks

Wrote PROOF.md for all finite integers n,L>=1. No general analytic-flow
or stable-manifold theorem is used. The proof supplies compact sublevel
sets, global existence, the exact pair-difference ODE, a uniform
collision-repulsion neighborhood on a bounding box, and consequently a
uniformly invertible coefficient Jacobian along each distinct-coordinate
trajectory. A loss-gap inequality gives exponential convergence, with
constants depending on the initial sublevel and gaps. The positive simple
roots of r_* are proved by a sign-change argument with weight S.

Wrote audit_depth.py using only the standard library. It derives Gaussian
sum moments via integration-by-parts and truncated generating-series
exponentiation, solves the coefficient normal equations by exact
Gauss–Jordan elimination, and checks the proposed residual, its norm,
and its roots by an independent exact Sturm sequence. It also checks the
gradient chain rule, squared Vandermonde determinant, pair-difference
ODE, pair-splitting formula, equality invariance, and token forward pass.

Command:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_depth.py
```

Output (exit 0):

```
nice: setpriority: Operation not permitted
Process nice: 20
CPU soft limit: 120 seconds
n=1, L=2: exact risk=8/15; positive simple roots=2
n=1, L=3: exact risk=16/35; positive simple roots=3
n=1, L=8: exact risk=32768/109395; positive simple roots=8
n=2, L=2: exact risk=1/3; positive simple roots=2
n=2, L=3: exact risk=1/4; positive simple roots=3
n=2, L=8: exact risk=1/9; positive simple roots=8
n=3, L=2: exact risk=8/35; positive simple roots=2
n=3, L=3: exact risk=16/105; positive simple roots=3
n=3, L=8: exact risk=32768/692835; positive simple roots=8
n=5, L=2: exact risk=8/63; positive simple roots=2
n=5, L=3: exact risk=16/231; positive simple roots=3
n=5, L=8: exact risk=32768/2909907; positive simple roots=8
n=10, L=2: exact risk=1/21; positive simple roots=2
n=10, L=3: exact risk=1/56; positive simple roots=3
n=10, L=8: exact risk=1/1287; positive simple roots=8
n=100, L=2: exact risk=1/1326; positive simple roots=2
n=100, L=3: exact risk=1/23426; positive simple roots=3
n=100, L=8: exact risk=1/1916797311; positive simple roots=8
n=1000, L=2: exact risk=1/125751; positive simple roots=2
n=1000, L=3: exact risk=1/21084251; positive simple roots=3
n=1000, L=8: exact risk=1/104071785999568101; positive simple roots=8
56 independent moment-system/closed-form/risk/Sturm checks passed.
105 pair-difference checks and 315 collision checks passed.
Coefficient Jacobian, loss gap, zero/negative steps and token updates passed.
Elapsed: 0.584 seconds; peak RSS: 14.39 MiB
```

The nice wrapper warning does not signal high priority: the process
explicitly verifies inherited nice=20, below the required priority.
No RAM cap is claimed; bounded Fraction polynomial/matrix sizes and
measured RSS stay far below 1 GiB. No numerical training or third-party
libraries are used. The root-count computation is a separate check,
not a substitute for the all-n, all-L sign-change proof.

## 5. Attempts to break the theorem

- Independently expanded the pair-difference coefficient around its
  midpoint: B_ij=2K-(delta^2/2)T, K=E[S^2(1-cS)^2 R^2],
  T=E[S^4 R^2]. The sign and factor 1/2 agree with direct product
  differentiation. Added exact checks for this identity and reran the
  command above: exit 0, all 56/105/315 checks passed, elapsed 0.710 s,
  peak RSS 15.48 MiB, nice 20.
- Added a second proof of the uniform gap neighborhood: K is at least
  the smallest eigenvalue kappa of the positive moment matrix
  W_jk=m_(j+k+2), 0<=j,k<=L-1, because (1-cs)R has constant term one.
  On |a_k|<=M, T<=U=E[S^4(1+MS)^(2L-4)]. Therefore
  |delta|<=sqrt(2kappa/U) gives B_ij>=kappa. This directly checks the
  compactness/continuity argument and does not assume finite critical
  points or convergence of the trajectory in advance.
- The proof does not divide by any a_i. One zero initial step is allowed
  when the steps are otherwise distinct. The Jacobian proof evaluates
  the monic polynomial product(z-a_i), so it remains valid at that zero.
- Repeated initial steps are a true obstruction. The same difference
  equation preserves equality; compactness separates their trajectories'
  risks strictly from the global optimum. No almost-sure claim is made
  for initialization laws with atoms or forced ties.
- The stationary repeated-coordinate set need not be classified or
  proved finite. All its points have a negative splitting direction;
  initially distinct trajectories stay uniformly away from the entire
  collision set. This closes the precise gap named in round 3 without
  relying on a generic saddle-avoidance assertion.
- Deterministic S=1 would invalidate positive definiteness and strict
  collision repulsion. The argument is at finite n throughout and takes
  n to infinity only after training. No uniform-in-n gap or rate is
  asserted.
- The loss-gap decay constant is 4 sigma^2 lambda, not 2 sigma^2 lambda:
  grad G=2H(c-c_*), and H^2>=lambda H. For L=1 it reduces to the exact
  quadratic flow rate 4m_2, checking the normalization independently.
- The n=1,L=3 risk is 16/35=48/(3*5*7), not zero. For n=2 the exact
  formula simplifies to 1/(L+1), independently checking every displayed
  risk at that prompt length. At fixed L the leading constant is
  2^L L!, consistent with 2,8,48 for depths 1,2,3.

No failure found in the restricted theorem. Still outside scope: all
random attention blocks, factorized trainable keys/queries, d>1,
softmax, discrete training, stochastic training, and uniform training
times. Literature priority for this elementary scalar theorem has not
been established; the claim is progress beyond the supplied report.

## 6. Final artifact audit

Read back REPORT.md and the load-bearing gap-separation and convergence
sections. Made the vacuous L=1 case explicit: K_eta=K with no minimum
over an empty pair set. Restricted the quantitative collision bound to
L>=2. Expanded the global-existence continuation step: bounded vector
field gives a time-Lipschitz path, a limit at a hypothetical finite
endpoint, and a local extension there. These are clarifications of the
proof; arithmetic formulas are unchanged.

Artifact command: a short standard-library Python heredoc under
`OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3`, reading the four deliverables,
checking final newlines, the report verdict, Python syntax via ast.parse,
and absence of an unwarranted SOLVED_ELSEWHERE.md. Output:
`Artifact checks passed; inherited nice: 20` (exit 0, with the same
wrapper warning). No writes outside this folder.

Deliverables: REPORT.md, PROOF.md, audit_depth.py, LOG.md. The next step
suggested in REPORT.md is scalar factorized key/query training, where
the metric weights differ between layers and the present pairwise-gap
argument no longer applies directly. The unrestricted T325 theorem is
not claimed.
