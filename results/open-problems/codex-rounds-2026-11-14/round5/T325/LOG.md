# T325 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Started 15 November 2026, 09:12 Asia/Tbilisi.

## 1. Orientation and bounded literature check

Read REPORT.md, LOG.md, SOLVED_ELSEWHERE.md in the first folder (which has
no PROOF.md or scripts); REPORT.md, LOG.md, PROOF.md, audit_scalar.py in
round 3; and REPORT.md, LOG.md, PROOF.md, audit_depth.py in round 4.
Read the brain navigation index and compute_state.json. Compute state:
warn, owner_away_open, CPU saturated. Only short standard-library exact
arithmetic is planned, with one thread and nice >=15 verified in-process.
The task's folder-only rule supersedes shared brain, checklist, and mesh
writes. No git, subagents, external writes, or model training.

Read-only shell commands: pwd; rg --files over the earlier folders and
navigation locations; cat/sed on the listed deliverables and compute
state; date '+%Y-%m-%d %H:%M:%S %Z'. The initial file listing was too broad
and its output was truncated; subsequent reads targeted exact files.

Initial web search queries:

- transformers in context linear regression multilayer gradient flow convergence random initialization 2025 2026
- "transformers" "preconditioned" "gradient" "convergence" "2026"

Opened https://arxiv.org/abs/2506.05249 and HTML versions v1 and v4;
opened https://arxiv.org/abs/2410.08292 and its full HTML v1.
Zhen Qin, Jinxin Zhou, Jiachen Jiang, Zhihui Zhu, *On the Convergence of
Gradient Descent on Learning Transformers with Residual Connections*,
arXiv:2506.05249v4, concerns a finite-data supervised fitting objective
(Section II), not this population in-context Bayes-risk theorem.
Khashayar Gatmiry, Nikunj Saunshi, Sashank J. Reddi, Stefanie Jegelka,
Sanjiv Kumar, *Can Looped Transformers Learn to Implement Multi-step
Gradient Descent for In-context Learning?*, arXiv:2410.08292v1, remains the
restricted looped result already discussed. No full solution found.
The status check ended within the initial five minutes; no exhaustive
novelty claim is made. Later source lookups concern standard proof tools.

## 2. Independent recheck and chosen extension (before new proof)

Re-derived the finite-n loss from the residual label-row update:
v_new=v+a S(w-v), S=sum x_i^2/n, so F(a)=E[product_i(1-a_i S)^2].
In coefficient coordinates the Hessian is twice the positive moment
matrix H_ij=E[S^(i+j)]. Its normal equations give the earlier residual
polynomial. Orthogonality changes its squared norm to its expectation;
the finite binomial sum integrates to alpha B(alpha,L+1), hence
L!/(alpha+1)_L, alpha=n/2. Splitting a repeated pair gives the negative
quadratic coefficient -2 E[S^2(1-cS)^2 R^2]; differentiating independently
gives (a_i-a_j)'=2(a_i-a_j)E[S^2(1-a_i S)(1-a_j S)R^2]. The sign and
normalization agree with round 4. Its compactness/separation/Jacobian
argument holds, including one zero or negative initial step.

Chosen ONE extension: replace each direct scalar step by a_i=k_i q_i,
with both scalar factors trained by population Euclidean gradient flow,
at arbitrary finite depth. Seek almost-sure global convergence under an
absolutely continuous joint factor initialization. This is round 4's
named next step. Equal products no longer define an invariant collision
set, so its deterministic gap proof does not transfer. Instead test
boundedness using conserved factor imbalances and prove that every
nonglobal factor-space critical point is a strict saddle. Use analytic
gradient convergence and center-stable manifolds with precise hypotheses;
do not infer convergence merely from a landscape classification.

Recheck command:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r4/briefs/T325/audit_depth.py
```

Exit 0. Output: wrapper warning `nice: setpriority: Operation not permitted`;
in-process nice 20; CPU soft limit 120 seconds; all 56 moment-system,
closed-form-risk and Sturm checks passed; all 105 pair-difference and 315
collision checks passed; Jacobian, loss-gap, zero/negative-step and token
checks passed. Elapsed 0.560 seconds, peak RSS 14.41 MiB. For n=1,L=3,
risk 16/35; for n=2,L=8, risk 1/9; for n=1000,L=3, risk 1/21084251.
The earlier result holds under both the independent hand derivation and
its exact arithmetic audit.

## 3. Factor-space proof route

Derived k_i'=-q_i F_i, q_i'=-k_i F_i, a_i'=-(k_i^2+q_i^2)F_i.
The invariant D_i=k_i^2-q_i^2 gives
(k_i^2+q_i^2)^2=D_i^2+4a_i^2. Thus bounded product steps imply bounded
individual factors along every trajectory, even at D_i=0.

Important extra case: at a double-zero pair k_i=q_i=0, product-space
stationarity need not hold. Nevertheless F_i at a_i=0 equals
-2 E[S product_(j!=i)(1-a_j S)^2]<0. The factor Hessian on that pair
has off-diagonal entries F_i and zero diagonal entries, so it has a
negative eigenvalue. If no pair is double zero, the product map has
full row rank. At a factor critical point F_i=0 for every i, and the
product-space negative splitting direction lifts to a negative factor
direction unless the product vector is globally optimal. This proves
the strict-saddle alternative on the WHOLE factor space, not just
nonzero-imbalance leaves.

Proof-tool web queries (separate from the bounded status check):
`"gradient flow" "strict saddles" "measure zero" analytic convergence theorem`;
`Lee Simchowitz Jordan Recht gradient descent only converges minimizers 2016 stable manifold theorem analytic`.
Opened PMLR lee16 and arXiv:1605.00405 (Ioannis Panageas, Georgios Piliouras).
These discrete-time theorems are not applied directly to an unbounded
polynomial Hessian. Opened the full primary paper Arthur Castello B. de
Oliveira, Milad Siami, Eduardo D. Sontag, *Convergence analysis of gradient
flow for overparameterized LQR formulations*, Automatica 182 (2025)
112504, https://sontaglab.org/FTPDIR/2025_automatica_olivera_siami_sontag_overparametrized_lqr_reprint.pdf .
Appendix A, Theorem 3 and Corollaries 3–4 give the applicable continuous-time
strict-saddle/analytic convergence statements, including nonisolated
critical sets. Need explicitly verify bounded forward flow and the
local, rather than global, diffeomorphism argument.

## 4. Proof and independent exact audit

Wrote PROOF.md. The theorem covers every finite n,L and trains both
scalar factors per layer. Every factor trajectory is bounded and
converges to one critical point; every nonglobal critical point is a
strict saddle; the full set of initial points converging to nonglobal
critical points has Lebesgue measure zero. Thus any joint initialization
law with a density succeeds almost surely. The learned products and
exact risk are the round-4 optimum, now reached under factor training.
The proof does not preserve or require the initial product ordering.

Opened https://arxiv.org/abs/1402.5087 and its full PDF (v3): Tobias Holck
Colding, William P. Minicozzi II, *Lojasiewicz inequalities and
applications*, equation (0.2). Stated the analytic gradient inequality
precisely, then derived finite-tail-length and single-point convergence
in PROOF.md. The center-stable argument uses a compactly supported local
cutoff, a countable cover of all strict saddles, and local invertibility
of the original time-m maps. It never assumes global backward existence,
a finite or countable critical set, or a globally bounded Hessian.

Created audit_factors.py independently of every earlier script. It uses
only standard-library rational arithmetic. Its factor-space directional
loss computation expands the actual key/query products as a polynomial
in S and a perturbation t, then squares and integrates. This is separate
from its product-space derivative and factor-Hessian chain-rule routines.
It also compares recurrence moments with n-fold Gaussian EGF expansion,
solves coefficient normal equations, and checks the risk by four forms.

Command:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_factors.py
```

Exit 0; output:

```
nice: setpriority: Operation not permitted
Process nice: 20
24 normal-system/squared-risk/Schur/binomial checks passed.
126 imbalance/product-speed/boundedness identities passed.
36 independent factor-path Hessian checks; 36 token checks passed.
63 double-zero Hessian checks; 45 lifted repeated-product checks; 18 critical-point checks passed.
Equal products 1,1 with unequal imbalances: gap derivative=99/2.
Anti-balanced obstruction and limiting factor-magnitude formulas passed.
Elapsed: 0.348 seconds; peak RSS: 15.12 MiB
All exact factor audits passed.
```

The wrapper cannot change the inherited priority, but the program
verifies nice=20, lower than the required priority. It installs a 120 s
CPU soft limit and a 120 s wall alarm, and checks RSS below 1 GiB.
No hard address-space cap is claimed. Bounded tiny sparse polynomial and
Fraction lists are used; no arrays, GPU, torch, MLX, or training runs.

## 5. Attempts to break the result

- The double-zero case is essential: grad f=0 need not imply grad F=0
  there. Rather than cancel nonexistent multipliers, use g_i<0 and the
  2x2 Hessian block [[0,g_i],[g_i,0]]. Its (1,1) curvature is 2g_i,
  independently reproduced by the exact t^2 perturbation of the product.
  The script checks 63 such cases, not only the all-zero origin.
- Off a product critical point, Hess f contains sum_i g_i Hess pi_i.
  Dropping it generally gives a wrong Hessian. All 36 arbitrary-point
  checks include this term. The proof drops it only after proving all
  g_i vanish. A second lift varies only one multiplier per layer and
  gives the exact product splitting path, with no Hessian correction.
- A family of actual nonglobal factor critical points has one active
  layer at n/(n+2) and every other pair double zero. The script checks
  its criticality, negative curvature and strict risk gap for L>=2.
- Factor sublevels are noncompact. Boundedness uses both conserved D_i
  and compact PRODUCT sublevels. Two independent algebraic bounds are
  h_i^2=D_i^2+4a_i^2 and max(k_i^2,q_i^2)<=|D_i|+|a_i|. Both hold also
  at zero imbalance and have exact arithmetic checks.
- Equal products need not remain equal: for n=2,L=2, (1,1),(2,1/2)
  gives product gradient (22,22), h=(2,17/4), and gap derivative 99/2.
  Hand expansion with moments (1,1,2,6,24) gives g=22 independently.
  This demonstrates why the earlier deterministic noncollision proof
  cannot simply be reused.
- Absolute continuity matters. At L=1 the atomless law k=-q, k continuously
  distributed, is supported on a null line and fails: k'=-2k(1+m_2 k^2),
  so the product tends to zero and risk tends to 1 rather than 2/(n+2).
  More generally each anti-balanced hyperplane is invariant and cannot
  reach the all-positive product optimum. The theorem includes independent
  Gaussian factors, not every singular or atomless joint law.
- An uncountable union of saddle attraction sets need not be null.
  PROOF.md uses a countable subcover of the local trapping neighborhoods
  and integer-time preimages; it does not take that invalid union.
- The original polynomial flow need not be globally backward complete.
  Only the cutoff flow is made complete in both directions. Original
  time-m maps have invertible variational derivatives and local inverses;
  these suffice to pull back null sets.
- The finite-length coefficient is C/(1-beta): integrating
  -d e^(1-beta)/dt >= (1-beta)||grad f||/C gives it directly. Independently,
  arc length satisfies |ds/de|=1/||grad f||<=C e^(-beta); integrating
  over e gives the same coefficient and exponent.
- Risk constants agree by the solved moment system, squared-polynomial
  integration, Schur complement, and alternating-binomial expression.
  At n=2 the value is 1/(L+1); at depths 1,2,3 the leading constants
  are 2,8,48. All n remain finite during training, so no degenerate
  S=1 population is substituted in the proof.

No defect found in the stated restricted theorem. No uniform training
time, discrete-time result, stochastic result, higher-dimensional result,
softmax result, or full-matrix training result is established. Literature
priority for this scalar factorized theorem is not claimed.

## 6. Final artifact audit

Read back the factor critical-point classification, finite-length
argument, cutoff-flow localization, countable cover, and time-map
preimages. Checked the layer normalization and fixed-block restriction
against the explicit K_i,Q_i definition. The null-set theorem concerns
all R^(2L), so an absolutely continuous initialization is sufficient
without restricting its support or factor imbalances. Successful
product limits are positive, so formula (15) has two strictly positive
squared magnitudes and consistent equal signs.

Wrote REPORT.md with the exact required verdict prefix, commands,
limitations, failure cases, and a concrete discrete-training next step.
The next-step imbalance identity was re-expanded independently:
(k-eta qg)^2-(q-eta kg)^2=(k^2-q^2)(1-eta^2 g^2); multiplying the two
updated factors gives the displayed product update. These are only
suggestions for the next worker, not a discrete convergence claim.

Final artifact command: a standard-library Python heredoc under the
same one-thread/nice/bytecode-suppression environment, checking the
four deliverables' final newlines, parsing audit_factors.py with
ast.parse, checking the report verdict, and confirming no unwarranted
SOLVED_ELSEWHERE.md. Output: PROOF.md 459 lines; REPORT.md 96 lines;
LOG.md 217 lines before this final append; audit_factors.py 329 lines;
`Artifact checks passed; inherited nice: 20`. Exit 0 with the recorded
wrapper warning. No arithmetic code changed after its passing run.

Deliverables: REPORT.md, PROOF.md, audit_factors.py, LOG.md. The full
T325 conjecture remains unresolved; the completed step is almost-sure
training convergence with both scalar key/query factors trainable at
arbitrary finite depth in the fixed-block d=1 architecture.
