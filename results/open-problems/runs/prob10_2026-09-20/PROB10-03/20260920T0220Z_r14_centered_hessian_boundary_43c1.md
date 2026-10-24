Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum, and I do not claim otherwise. SOURCE METRIC NO MOVEMENT: rigorous `kappa=-1` bracket width `6.48139658710 -> 6.48139658710`. This is the third unchanged R14 PROB10 iteration, so this run records a concrete obstruction and changes method within PROB10-03 rather than rotating. Three materially different attacks: #8 DISCRETIZE/direct interval falsification, #18 SAY IT IN ANOTHER LANGUAGE/centered Taylor-Hessian certification, #6 DEFORM TO A POINT YOU CAN SOLVE/`B->0` full-lift boundary.**

# PROB10-03 — R14 bounded iteration: interval-wrapping obstruction, centered-Hessian compiler, and `B=0` boundary selection

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / SOURCE OPEN / NO RIGOROUS ENDPOINT MOVED**.

## 1. Contract, continuity, ownership, and consumed state

I first read the current `operations/PROB10_2026-09-20.md`, root `POSTED.md`, root `RESULTS.md`, the current Campbell--O'Rourke claim, the immutable Campbell handoff, the newest R14 PROB10 report, and the two newest complementary T03 reports.

Consumed repository paths:

- `operations/PROB10_2026-09-20.md`;
- `POSTED.md`;
- `RESULTS.md`;
- `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md` (current blob `d8fe3a276b9c59d4608a113c0d77ba5b5dc8717d`);
- `artifacts/prob10_2026-09-20/PROB10-03/20260919T2354Z_campbell_q18_r14_handoff.md` (current blob `edaa787e384c28a4b5a658dbba80f664cde75882`), which preserves the intervening successor and the owner-supplied navigation point `3846db33296cfb6eea59ff7c488929087c7b62a2`;
- `runs/prob10_2026-09-20/PROB10-03/20260920T0106Z_r14_preconditioned_stationarity_compiler_2c91.md`;
- `proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/2026-09-20__t03-full2-two-scalar-reduction.md`;
- `proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-closed-kernel-miranda-alpha12p75.md`;
- older R14 obstruction report `runs/R14/2026-09-16T20-53-04Z_r14-c187-mzz-curvature-obstruction.md`.

The Campbell canonical claim still lists R14 historically/currently. I did **not** overwrite that shared claim. The immutable refocus handoff expressly preserves its `S=5` state and says coordinator/owner reconciliation is required for any canonical ownership reassignment. This run is the owner-directed, delimited PROB10-03 R14 route; it does no Campbell mathematics.

Posted zero-margin/Ising-perceptron work remains an exclusion but is not this target.

## 2. Frozen model, probability convention, and current rigorous metric

The source model remains

`M=floor(alpha N)`, `g_a iid N(0,I_N)`, `||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)` for every `a<=M`.

A lower endpoint means SAT probability tends to one; an upper endpoint means SAT probability tends to zero, with fixed `alpha` as `N->infinity`.

Current repository-supported rigorous bracket:

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

`W = alpha_U-alpha_L = 6.48139658710`.

Before this run: `W=6.48139658710`.

After this run: `W=6.48139658710`.

No ansatz, ordinary floating-point quadrature, finite mesh, or smaller-radius algorithmic output is entered into the metric.

## 3. Fresh source/scope check

The designated primary-source picture is unchanged in the sense relevant to rigor.

- El Alaoui--Sellke `arXiv:2010.15811` treats the exact Gaussian spherical model but describes the negative-margin FRSB/Parisi capacity picture conjecturally; its algorithmic output has radius `sqrt(qbar N)` with `qbar<1`.
- Stojnic `arXiv:1306.3980` remains the rigorous comparison/upper-bound baseline used by the certified partial-lift endpoint.
- Stojnic `arXiv:2312.16531` develops stationarized fully lifted RDT and reports concrete finite-level capacities after substantial numerical work. This run continues to require a true stationary certificate before importing a displayed number.
- Annesi--Malatesta--Zamponi `arXiv:2410.06717` describes its negative-perceptron transition calculation explicitly as using a full-RSB **ansatz**.
- Huang--Sellke--Sun `arXiv:2608.29416`, submitted 29 August 2026, proves exact **algorithmic** projection-pursuit thresholds for bounded continuous activations and explicitly distinguishes this from the outstanding non-algorithmic feasible-projection problem.

A bounded search through 20 September 2026 found no later primary theorem plainly proving the unrestricted full-radius SAT/UNSAT equality at `kappa=-1`. This is dated negative-search evidence only, not a global novelty certificate.

## 4. Attack #8 — falsify the naive interval implementation

The previous R14 report reduced the candidate `alpha=12.75` proof to a preconditioned two-scalar contraction problem. I first tried the most literal completion: substitute a rectangular `(p,B)` interval directly into the closed one-dimensional Gaussian kernel and the exact algebraic reconstruction.

At the single center

`p_c=0.645767064689`, `B_c=4.9292292009`,

an outward interval-Simpson prototype on `|z|<=9`, with fourth-derivative remainder control, is well behaved. After adding the companion's exact value-tail bounds, it gives the self-check enclosures

`H in [-8.31902147e-7,8.31903592e-7]`,

`alpha in [12.74998595513,12.75001404488]`,

`Psi in [0.015199096066,0.015202890869]`.

On the compact interval before derivative-tail completion it also gives

`H_p in [-0.02581892329,-0.02560675743]`,

`H_B in [0.000435785389,0.000440026977]`,

`alpha_p in [26.83396764,26.83740113]`,

`alpha_B in [-0.888916790,-0.888847730]`.

But direct interval substitution over a two-dimensional product box loses the strong correlations among `I,I_B,K,D,c`. The quotient

`D^2=K/(-4p^2B^2I_B)`

and subsequent reconstruction wrap severely; the effect remains visible even after shrinking the parameter box by an order of magnitude. Therefore simply using a finer Gaussian quadrature does not close the proof.

**Obstruction recorded:** ordinary product interval arithmetic is the wrong representation of the remaining uncertainty because it destroys the cancellations in the exact two-scalar reconstruction. This is the required written obstruction after the third unchanged source-metric run.

## 5. Attack #18 — new centered-Hessian certification theorem

I replaced whole-box nonlinear interval substitution by a centered Taylor/Hessian representation.

The complete proof is in

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0220Z_r14_centered_hessian_boundary_analysis.md`.

Let

`F(p,B)=(H(p,B),alpha(p,B)-12.75)`

and keep the fixed rational approximate inverse Jacobian

`A=[[-1601/20,-493/12500],[-60418/25,-5789/2500]]`.

On the smaller box

`Q={|p-p_c|<=1/2000, |B-B_c|<=1/50}`,

the new lemma says it is sufficient to certify four point derivative intervals plus the six coarse Hessian bounds

`|H_pp|<=1/5`, `|H_pB|<=1/100`, `|H_BB|<=1/1000`,

`|alpha_pp|<=70`, `|alpha_pB|<=4`, `|alpha_BB|<=1/2`.

Together with the point derivative windows written in the artifact, the mean-value theorem yields a rational whole-box Jacobian enclosure. Exact enumeration of its 16 vertices gives

`q <= 62439/312500 = 0.1998048`.

With only

`|H(p_c,B_c)|<=10^-6`,

`|alpha(p_c,B_c)-12.75|<=2*10^-5`,

the center displacement obeys

`eta <= 202097/1250000 = 0.1616776`

while

`1-q >= 250061/312500 = 0.8001952`.

Thus the exact contraction margin is at least

`0.8001952-0.1616776 = 0.6385176`.

A companion Taylor bound shows that the point conditions

`Psi(p_c,B_c)>=7/500`, `|Psi_p(p_c,B_c)|<=1`, `|Psi_B(p_c,B_c)|<=1/25`,

plus

`|Psi_pp|<=2`, `|Psi_pB|<=1/5`, `|Psi_BB|<=1/20`

force throughout `Q`

`Psi >= 50751/4000000 = 0.01268775>0`.

This theorem is complete. Its source application is not: the full-line point derivative bounds and the stated Hessian bounds still require rigorous enclosure.

A numerical-only `7x7` finite-difference scout was used only to try to falsify those Hessian windows. The largest observed magnitudes were approximately

`|H_pp|=0.1203`, `|H_pB|=0.00644`, `|H_BB|=9.46e-5`,

`|alpha_pp|=58.05`, `|alpha_pB|=2.87`, `|alpha_BB|=0.364`,

`|Psi_pp|=1.079`, `|Psi_pB|=0.0805`, `|Psi_BB|=0.0124`.

They sit inside the proposed rational hypotheses, but the scout is not a proof and does not move `alpha_U`.

## 6. Attack #6 — exact `B->0` deformation boundary

As a genuinely different fallback, I asked whether the complete second lift can be deformed from the analytically simple `B=0` boundary instead of certifying an interior numerical root directly.

Let

`u(x)=(x-1)_+`,

`r_p(Z)=E[u(sqrt(p)Z+sqrt(1-p)H)|Z]=T_{sqrt(p)}u(Z)`,

`mu_1=E[u(G)^2]`.

I proved:

`I_B(p,B) -> -mu_1`,

`K(p,B)/B^2 -> 4p E[r_p(Z)^2]`

as `B downarrow0`.

Therefore any complete-second-lift stationary branch with

`B->0`, `p->p_0 in (0,1)`, `D->1`

must satisfy the scalar OU balance

`E[r_{p_0}(Z)^2]=p_0 mu_1`.                                           (B0)

Using the Hermite expansion of `u`, I further proved that `(B0)` has **exactly one** solution in `(0,1)`. If

`s_k=(E[u(G)He_k(G)])^2/k!`,

then for `p<1`

`[E r_p^2-p mu_1]/(1-p)`
`=s_0-sum_{k>=2}s_k p(1+p+...+p^{k-2})`,

which is strictly decreasing. It starts positive. Its limit at one is

`mu_1-P(G>1)=barPhi(1)-phi(1)<0`

because `mu_1=2barPhi(1)-phi(1)` and Mills' inequality is strict. Hence there is one interior zero; `p=1` is a separate endpoint zero.

The executable's numerical-only scout locates the interior boundary point at

`p_* ~= 0.1526513489316`.

This number is not a rigorous source parameter. The theorem's value is structural: a perturbative `B=0` continuation is reduced to a unique scalar boundary seed. It is not yet known whether that branch connects to the source-relevant interior branch near `p~=0.646`.

## 7. Executed artifacts

Exact/self-check source:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0220Z_r14_centered_hessian_boundary_checker.py`

creation commit: `b30962cd8ebc17d680778de4edb1ab8bf8662fb5`.

Archived actual output:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0220Z_r14_centered_hessian_boundary_checker.out`

creation commit: `5faddaf806faa91c9dfc5b46167d274e689d2946`.

The exact part ends with

`q=62439/312500`, `eta=202097/1250000`, `eta<1-q`,

and

`Psi_lower=50751/4000000>0`.

The final line is `ALL_SELF_CHECKS_PASS`. The `B=0` root is explicitly marked `NUMERICAL_ONLY`.

Mathematics-first proof artifact:

`artifacts/prob10_2026-09-20/PROB10-03/20260920T0220Z_r14_centered_hessian_boundary_analysis.md`

creation commit: `f4e8a60489a989e7f2672914d68ab13ef4eb5f19`.

Self-checks are not independent audits.

## 8. Source metric versus auxiliary movement

### Source metric

`alpha_L: 6.30297437506 -> 6.30297437506`.

`alpha_U: 12.78437096216 -> 12.78437096216`.

`width: 6.48139658710 -> 6.48139658710`.

**Movement: none.**

### Auxiliary movement

Before this run, the next instruction was effectively “directly interval-enclose the two-scalar Jacobian on a product box.”

After this run:

1. that literal approach has a recorded interval-dependency obstruction;
2. there is a proved centered-Hessian compiler with a large exact contraction margin, reducing the source-moving obligation to point/full-tail first derivatives plus six coarse second-derivative bounds;
3. there is an independent exact `B=0` OU boundary-selection theorem for perturbative continuation.

This satisfies the three-unchanged-run contract by changing method **within the same source problem**. No unrelated rotation is made.

## 9. Remaining full-scope gap

The highest-value next step is to implement a centered Taylor model for the closed Gaussian kernel and rigorously prove the six Hessian inequalities and the missing derivative-tail bounds. If those pass, the theorem in this run plus the already-proved exact second-full reconstruction would certify a true stationary point at `alpha=12.75` with `Psi>0`, after which the source theorem can be invoked and only then can the upper endpoint move.

The alternate route is to calculate the first nonzero coefficient of the stationary branch leaving the unique `B=0` boundary point and determine the sign of the induced change in `alpha`; this is analytically distinct from validated interior quadrature.

Status remains **OPEN / PARTIAL**. Closure still requires full source scope, exact proof/certification, current prior-art reconciliation, and the repository-standard independent validation.

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
  metric_movement: "NO MOVEMENT"
  prob10_unchanged_count: "2 -> 3"
  methods: [8, 18, 6]
  obstruction: "naive product interval arithmetic destroys correlation/cancellation in the reconstructed second-full map; finer quadrature alone does not fix it"
  new_theorems:
    - "R14-T03-CENTERED-HESSIAN: point derivatives + coarse Hessian bounds imply a contraction certificate at alpha=12.75"
    - "R14-T03-B0-BOUNDARY: exact small-B OU boundary equation, with a unique interior solution"
  conditional_candidate_if_hessian_enclosures_are_proved:
    alpha_U: "12.75"
    width: "6.44702562494"
    improvement: "0.03437096216"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
  scheduler_changes: "none"
  external_actions: "GitHub-only; no email, Drive, public posting, permission, workflow, or scheduler changes"
```
