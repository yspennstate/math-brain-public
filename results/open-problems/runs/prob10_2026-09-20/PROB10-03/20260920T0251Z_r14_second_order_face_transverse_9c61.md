Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE METRIC NO MOVEMENT: rigorous `kappa=-1` bracket width `6.48139658710 -> 6.48139658710`. This is the fourth consecutive unchanged R14 PROB10 iteration; the method changes again within PROB10-03. Three materially different attacks: (A) exact second-order tilted-moment/OU compiler, (B) monotone-face corner reduction for the `alpha=12.75` Miranda rectangle, (C) transversality of the unique `B=0` OU seed.**

# PROB10-03 — R14 bounded iteration: second-order stochastic closure and continuum-face reduction

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / NO RIGOROUS ENDPOINT MOVED / NEW ANALYTICAL REDUCTIONS**.

## 1. Contract, continuity, ownership, and consumed state

I obeyed `operations/PROB10_2026-09-20.md` and stayed on the owner-refocused negative-margin spherical perceptron. I did not rotate to another target and did not edit any scheduler state.

Consumed current repository state before the mathematics:

- `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
- root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
- root `RESULTS.md`, blob `cede3c760e23a2fc8c01e82f31fdda3d2cfea321`;
- current Campbell–O'Rourke claim `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`, blob `d8fe3a276b9c59d4608a113c0d77ba5b5dc8717d`;
- the already-created immutable Campbell handoff `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md`, blob `edaa787e384c28a4b5a658dbba80f664cde75882`;
- newest prior R14 PROB10 report `runs/prob10_2026-09-20/PROB10-03/20260920T0220Z_r14_centered_hessian_boundary_43c1.md`, blob `462d5b2ded35bd58a2c50058a1901b7d92c775f2`;
- complementary T03 derivative report `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-moment-jacobian-broad-contraction.md`, blob `33a50238485e40a6dc0506e9def37ca5e4a250b3`;
- complementary T03 kernel/Miranda report `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-closed-kernel-miranda-alpha12p75.md`, blob `cab9e7126ca5c5c27ee8641b0448437082742bae`.

The required intervening-successor preservation is already satisfied by the immutable Campbell handoff above, which records navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`, inherited `S=5`, and the unresolved logarithmic-potential bridge. I did not create a redundant second handoff and did not overwrite Campbell's shared claim.

The older negative-margin failures remain active constraints: the MZZ linear weighted-second-moment route has its local curvature obstruction; the one-parameter Stojnic-2013 partial lift is globally exhausted at the retained upper endpoint; the `N^{-1/2}` sphere-net route pays `Theta(N log N)` entropy; simple Gaussian-facet first moment is too weak; smaller-radius algorithmic points do not close the exact sphere problem; and ordinary product intervals lose the cancellation in the exact complete-second-lift reconstruction.

## 2. Frozen source model and probability convention

Freeze

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`,

with fixed `alpha` and `N->infinity`.

A lower endpoint means SAT probability tends to one. An upper endpoint means SAT probability tends to zero.

Certified bracket entering this run:

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = alpha_U-alpha_L = 6.48139658710`.

Certified bracket leaving this run: identical.

No ansatz, finite mesh, ordinary floating point value, or smaller-radius constructive output is promoted to a bracket endpoint.

## 3. Fresh source/scope check

The bounded literature refresh through 20 September 2026 preserves the previous rigor distinction.

- El Alaoui--Sellke, arXiv:2010.15811, studies the exact Gaussian radius-`sqrt(N)` spherical model, but for negative margin the FRSB/Parisi structure is conjectural and its algorithm produces radius `sqrt(qbar N)` with `qbar<1`.
- Stojnic, arXiv:1306.3980, remains the rigorous negative-margin comparison/upper-bound baseline.
- Stojnic, arXiv:2312.16531, develops stationarized fully lifted RDT and explicitly says practical operation requires substantial numerical work; its finite-level numerical values are not silently treated here as certified endpoints.
- Montanari--Zhong--Zhou, arXiv:2110.15824, supplies rigorous information-theoretic/algorithmic bounds and the LP lower endpoint used by the repository, not an equality theorem at `kappa=-1`.
- Annesi--Malatesta--Zamponi, arXiv:2410.06717, states that its transition value is computed using a full-RSB ansatz.
- Winer--Herderschee, arXiv:2503.11761, introduces a jammed Parisi ansatz and matches previous threshold computations; it is not substituted for a rigorous full-radius proof.

A bounded current search found no later primary theorem plainly proving the exact full-radius SAT/UNSAT equality at `kappa=-1`. This is dated negative evidence only, not a novelty certificate.

## 4. Attack A — exact second-order tilted-moment/OU compiler

The main proof is in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_moment_face_reduction.md`

creation commit `1e6199d5a13c1b0a21c6226e7737dec1c3209f87`.

Starting from the companion closed conditional Gaussian kernel, define for `Y~N(mu,s^2)`

`J_r=E[Y_+^r exp(-B Y_+^2)]`, `f=P(Y<=0)+J_0`, `u=log f`.

I proved exact raw derivatives through total order three using only `J_0,...,J_6` and the boundary density `rho_0=phi(mu/s)/s`, including the kink term

`f_mumumu=-2B rho_0+12B^2J_1-8B^3J_3`.

This yields closed one-dimensional expectation formulas for

`I_BBB`, `K_BB`, `K_pB`, and, nontrivially,

`K_pp = p E[u_mumumu^2] + 2E[u_mumu^2] - 4pE[u_mumu^3]`
`       -6pE[u_mu u_mumu u_mumumu] -4E[u_mu^2u_mumu]`
`       +6pE[u_mu^2u_mumu^2] +2pE[u_mu^3u_mumumu]`.

The `K_pp` identity is proved from the OU PDE `u_t=Lu+u_z^2`, twice differentiating the Fisher quantity `K=E u_z^2` and then converting `p=e^{-2t}`. Combined with the already-proved first-derivative formulas, every stochastic input to

`H_pp,H_pB,H_BB, alpha_pp,alpha_pB,alpha_BB`

is now an explicit one-dimensional Gaussian expectation. The previous numerical-differentiation layer is removed completely. Only directed evaluation of closed formulas plus algebraic differentiation of the inherited deterministic `c,A_0` terms remains.

**Auxiliary metric movement:** highest stochastic derivative requiring finite-difference/AD evaluation `2 -> 0`.

This does not itself move `alpha_U`.

## 5. Attack B — reduce continuous Miranda faces to four corners plus two signs

The NM13-03 candidate rectangle at `alpha_0=12.75` had strong finite-mesh signs but lacked a continuum enclosure. I proved the following exact reduction.

If on a rectangle `R=[p_-,p_+]x[B_-,B_+]`

`H_B>0`, `alpha_p>0`

throughout, then the four corner inequalities

`H(p_-,B_-)>0`, `H(p_+,B_+)<0`,

`alpha(p_-,B_-)>alpha_0`, `alpha(p_+,B_+)<alpha_0`

already imply all four Poincare--Miranda face signs. The proof is simply monotonicity along each face followed by Poincare--Miranda.

Thus the continuum certification problem can be reorganized from four whole-face enclosures to

- four directed corner-value enclosures;
- two robust whole-box derivative signs;
- an independent Lipschitz enclosure for `Psi>0`.

This is materially different from the previous centered-Hessian contraction route. The companion scouts place `H_B` and `alpha_p` well inside the desired signs, but those numerical scouts are not promoted to proofs.

## 6. Attack C — test the `B=0` deformation for tangent degeneracy

The preceding R14 run proved that any complete-second-lift branch approaching `B=0`, `D=1` must use the unique interior solution of

`F(p)=E[(T_{sqrt(p)}(x-1)_+)^2]-p E[(G-1)_+^2]=0`.

I proved the root is simple:

`F'(p_*)<0`.

Writing the Hermite coefficients

`s_k=(E[(G-1)_+ He_k(G)])^2/k!`,

one has exactly

`F(p)=(1-p)G(p)`,

`G(p)=s_0-sum_{k>=2}s_k p(1+p+...+p^{k-2})`.

At least one `s_k`, `k>=2`, is positive because the hinge is not affine in Gaussian `L^2`, hence `G'(p)<0`. At the unique root `G(p_*)=0`, so

`F'(p_*)=(1-p_*)G'(p_*)<0`.

Therefore tangent degeneracy is **not** the obstruction to a local perturbative continuation from the `B=0` boundary. What remains is to derive and control the coupled branch equations sufficiently to connect that seed to a source-useful positive-`B` stationary branch.

## 7. Falsification and executed self-check

Before relying on the new second-order compiler, I tried to falsify it in two ways.

First, differentiating through the hinge while omitting the boundary density term gives a different third-`mu` derivative; the proof therefore explicitly retains `-2B rho_0`. This is the exact nonsmoothness point that must not be lost.

Second, the executable compares the closed `K_p,K_pp,K_B,K_BB,K_pB` formulas with independent centered finite differences at the `alpha=12.75` numerical center. This is deliberately **NUMERICAL_ONLY** evidence, not a certificate. The largest discrepancy at step `2e-4` is about `3.15e-6` for `K_pp`; all five checks pass their stated falsification tolerances.

Executed source:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_moment_checker.py`

creation commit `c3648f024c047eabab13236b59da19a7f930b201`.

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_moment_checker.out`

creation commit `61c96a16a2543315c8da4ab9bf9dc973839486d4`.

Its exact symbolic lines are

`EXACT_KPP_TRANSFORM_IDENTITY=PASS`,

`EXACT_B0_FACTOR_IDENTITY=PASS`,

and its final line is

`ALL_SELF_CHECKS_PASS`.

Self-checks are not independent audits.

## 8. Source metric versus mechanism movement

### Source metric

Before:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

After:

`alpha_L=6.30297437506`, `alpha_U=12.78437096216`, width `6.48139658710`.

**Movement: none.**

The review-pending candidate `alpha_U=12.75` remains outside the certified ledger.

### Auxiliary movement

1. second stochastic derivatives now have exact closed formulas with only `J_0,...,J_6`;
2. finite differences / AD are no longer mathematically needed anywhere in the R14 Hessian compiler;
3. a new monotone-face lemma reduces the Miranda face problem to four corner values plus two derivative signs;
4. the `B=0` scalar boundary seed is transverse rather than tangent.

## 9. Remaining full-scope gap and next bounded route

The highest-value next step is not another ansatz. It is a directed-arithmetic implementation of the formulas proved here, aimed first at the **coarse signs**

`H_B>0`, `alpha_p>0`

on the NM13-03 `alpha=12.75` rectangle. If those are enclosed, only four corner values are needed for the Miranda root. A directed Lipschitz enclosure for `Psi` can then certify objective positivity on the root box. Only after those steps pass can Stojnic's source-matched complete-second-lift implication move the rigorous upper endpoint to `12.75`.

If the monotone signs fail, the centered-Hessian contraction theorem from the preceding R14 run remains the fallback, now with its second stochastic derivatives closed analytically by this run.

Status remains **OPEN / PARTIAL**. No claim of full capacity determination, publication novelty, or independent validation is made.

```yaml
ledger_delta:
  worker: "R14 / PROB10-03"
  target: "negative-margin spherical Gaussian perceptron capacity at kappa=-1"
  status: "PARTIAL / OPEN"
  source_metric: "rigorous whp threshold bracket width alpha_U-alpha_L"
  before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  source_movement: "none"
  unchanged_run_count_for_current_PROB10_refocus: 4
  auxiliary_movement:
    stochastic_derivative_order_requiring_finite_difference: "2 -> 0"
    miranda_continuum_reduction: "four whole faces -> four corners + signs H_B>0, alpha_p>0"
    B0_seed: "unique interior root -> unique simple/transverse interior root"
  new_theorems:
    - "R14-T03-SECOND-MOMENT-COMPILER"
    - "R14-T03-MONOTONE-FACE"
    - "R14-T03-B0-TRANSVERSE"
  candidate_not_certified:
    alpha_U: "12.75"
    reason: "directed whole-box derivative signs/corner values/Psi positivity not yet enclosed"
  artifacts:
    proof: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_moment_face_reduction.md @ 1e6199d5a13c1b0a21c6226e7737dec1c3209f87"
    checker: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_moment_checker.py @ c3648f024c047eabab13236b59da19a7f930b201"
    output: "artifacts/prob10_2026-09-20/PROB10-03/20260920T0251Z_r14_second_order_moment_checker.out @ 61c96a16a2543315c8da4ab9bf9dc973839486d4"
  independent_audits: 0
  scheduler_changes: "none"
  external_actions: "GitHub-only; no email, Drive, public posting, permission, workflow, force push, or scheduler changes"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
```
