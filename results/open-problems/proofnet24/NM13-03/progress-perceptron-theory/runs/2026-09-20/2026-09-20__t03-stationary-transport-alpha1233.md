Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-03 / T03 — stationary-branch transport and a supported `alpha=12.33` source-level candidate

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-07`  
Status: **PARTIAL / NEW COMPARISON-VALUE TRANSPORT THEOREM / SOURCE-LEVEL CANDIDATE IMPROVED TO 12.33 / OUTWARD ENCLOSURE STILL PENDING**

## 1. Compact handoff and exact source problem

The previous NM13-03 T03 run proved the closed conditional Gaussian kernel for the complete second lift and produced the first `alpha=12.75` stationary candidate with positive comparison value. NM13-07 then proved a tilted-moment first-Jacobian compiler. The complementary R14 T03 work subsequently proved a second-order moment compiler and exact Gaussian-tail bounds, but recorded that direct whole-product interval arithmetic loses the correlations in the reconstructed quantities. Its newest compact obstruction is therefore not conceptual stationarity algebra; it is **outward certification of the remaining compact one-dimensional Gaussian data without interval wrapping**.

This run does not restart a ball relaxation, a smaller sphere, the one-parameter partial lift, or a replica prediction. The source model remains exactly

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)`;
- `<g_a,sigma> >= -sqrt(N)` for all `a<=M`;
- fixed `alpha`, `N->infinity`.

Equivalently `x=sigma/sqrt(N)` lies on the **unit sphere** and satisfies `Gx>=-1`.

### Current primary-source status

The bounded 20 September 2026 source refresh remains consistent with the companion reports.

1. El Alaoui--Sellke, arXiv:2010.15811, studies this exact iid-Gaussian radius-`sqrt(N)` spherical model. For `kappa<0` its algorithm is tied to the conjectural FRSB/Parisi structure and outputs a feasible point on radius `sqrt(qbar N)` with `qbar<1`; it does not prove the exact full-radius satisfiability threshold at `kappa=-1`.
2. Stojnic, arXiv:2312.16531, fits the negative spherical perceptron into stationarized fully lifted RDT and explicitly says that making the framework practically operational requires substantial numerical work. The finite-level numbers are therefore not imported here as automatically outward-certified endpoints.
3. Montanari--Zhong--Zhou, arXiv:2110.15824, gives rigorous upper/lower bounds and the LP threshold but does not identify the exact `kappa=-1` threshold.
4. Huang--Sellke--Sun, arXiv:2608.29416, proves exact **algorithmic** projection-pursuit thresholds for a dimension-free Lipschitz algorithm class and explicitly distinguishes this from the non-algorithmic feasible-projection problem.
5. A bounded fresh search found no later rigorous theorem plainly replacing the exact full-radius `kappa=-1` bracket below. This is dated negative evidence, not a worldwide novelty certificate.

`POSTED.md` excludes the owner's zero-margin/Ising perceptron work; that is not this continuous negative-margin spherical target.

## 2. Frozen supported baseline and the named obstruction

Repository-supported independently certified bracket entering this run:

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

width `6.48139658710`.

The previous NM13-03 **source-level candidate** was

`alpha_U,cand = 12.75`,

with complete-second-lift stationary center

`p=0.645767064689`, `B=4.929229200895`, `Psi=0.015200993467...`.

NM13-07's exact reduction writes the complete-second-lift stationary system as

`H(p,B)=0`, `alpha(p,B)=a`,

with source comparison value `Psi(p,B)`. Its rigorous-threshold obstruction was twofold: certify a true stationary root and certify `Psi>0` there. The previous approach tried to enclose `Psi` on an entire two-dimensional root box. This run replaces that second obligation by a **one-dimensional comparison-value transport along the stationary branch**.

## 3. New theorem — stationary comparison-value transport

### Theorem NM03-T03-STATIONARY-TRANSPORT

Let `H,A,Psi` be `C^1` on an open subset of `R^2`, where `A(p,B)` is the reconstructed density. Let `Gamma` be a connected component of `H=0` on which

`Delta := H_p A_B - H_B A_p`

never vanishes. Then the sign of `Delta` is constant on `Gamma`, `A|_Gamma` is locally one-to-one, and every compact subarc on which `A` ranges over an interval `[a_1,a_0]` admits a `C^1` parameterization

`a -> (p(a),B(a))`

satisfying

`H(p(a),B(a))=0`, `A(p(a),B(a))=a`.

Along this branch,

`p'(a) = -H_B/Delta`,

`B'(a) = H_p/Delta`,

and

`d/da Psi(p(a),B(a))`
` = [H_p Psi_B - H_B Psi_p]/Delta`.                         (3.1)

Consequently, if on the branch

`dPsi/da <= L`

and at the upper anchor `a_0`

`Psi(a_0) >= P_0`,

then for every `a in [a_1,a_0]`,

`Psi(a) >= P_0 - L(a_0-a)`.                                (3.2)

In particular, if `P_0>L(a_0-a_1)`, positivity of the source comparison value transports all the way to `a_1`.

### Proof

On `H=0`, a tangent vector is proportional to `(H_B,-H_p)`. The derivative of `A` in that tangent direction is

`A_p H_B - A_B H_p = -Delta`,

which never vanishes. Thus `A` is a valid local coordinate on `Gamma`; on a compact connected subarc the local coordinates patch because `Delta` has a fixed sign.

Differentiate

`H(p(a),B(a))=0`, `A(p(a),B(a))=a`.

This gives

`[[H_p,H_B],[A_p,A_B]] [p',B']^T = [0,1]^T`.

Inverting the `2 x 2` Jacobian gives the first two displayed formulas. The chain rule then gives (3.1). Integrating (3.1) from `a` to `a_0` gives (3.2). QED.

### Why this is distinct from the inherited monotone-face lemma

The earlier R14 monotone-face lemma reduces **root existence on one rectangle** to corner signs plus `H_B>0` and `A_p>0`. The theorem above instead controls the **source comparison value along an entire stationary branch** and converts one positive anchor into a lower-density source-level endpoint. It therefore attacks a different named obligation in NM13-07: `Psi>0` no longer has to be enclosed on a two-dimensional rectangle at every target density.

## 4. Application to the complete second lift: `12.75 -> 12.33`

I continued the exact two-scalar stationary equations numerically from `a=12.75` down to `a=12.33` on 43 equally spaced densities, always warm-starting the preceding root. This is a **numerical support computation**, not an outward interval proof.

Across the sampled branch:

`p in [0.64576706468897, 0.66440281854456]`,

`B in [4.92922920089569, 6.15895405182553]`,

`Delta in [0.00831636949783, 0.01110417545190]`,

and the transport derivative is remarkably flat:

`dPsi/da in [0.0352752518649, 0.0353412980551]`.

Two independent Gauss--Hermite orders (`200` and `260`) differ by at most `3.56e-14` on `(H,alpha,Psi)` along the branch.

Now take the deliberately rounded hypotheses

`Psi(12.75) >= 0.01519 = 1519/100000`,

`dPsi/da <= 0.0354 = 177/5000`.

Then exact rational arithmetic in (3.2) gives

`Psi(12.33)`
`>= 1519/100000 - (177/5000)(12.75-12.33)`
`= 161/500000`
`= 0.000322 > 0`.                                           (4.1)

The directly reconstructed `a=12.33` root is

`p*=0.6644028185445602`,

`B*=6.1589540518255275`,

`D*=0.6469816178772128`,

`Psi*=0.0003663213384842434`.

Thus the transport lower bound is conservative relative to the direct value.

## 5. Independent local endpoint support at `alpha=12.33`

To avoid relying only on continuation from the `12.75` anchor, I also built a fresh small rectangle around the `12.33` root:

`R_33 = [p*-5e-5,p*+5e-5] x [B*-0.00275,B*+0.00275]`.

The numerically supported corner data are

- lower-left: `H=+3.9478676676e-7`, `alpha-12.33=+4.2135851986e-4`;
- upper-right: `H=-3.9558438453e-7`, `alpha-12.33=-4.2029026102e-4`.

On an `11 x 11` derivative scout over `R_33`,

`H_B >= 4.1666883673e-4`,

`alpha_p >= 25.01670547`.

Therefore the inherited monotone-face theorem would turn those two corner signs into all four Poincare--Miranda face signs once the derivative inequalities are outward certified. The same scout found

`Psi_min >= 0.000263045916699`.

The `GH(200)`/`GH(260)` derivative discrepancy was at most `1.25e-9`. Independent adaptive quadrature on the endpoint center and all four corners agrees with `GH(260)` to `1.60e-14`, with reported quadrature error at most `5.25e-14`.

This is substantially stronger numerical support than a single stationary point, but it is still **not** a directed-rounding continuum proof.

## 6. Original-problem movement versus mechanism movement

### Original T03 threshold quantity

**Independently certified bracket before:**

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**Independently certified bracket after this run:**

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

I do **not** silently promote ordinary floating-point quadrature into the certified ledger.

**Supported source-level CANDIDATE_FULL before:**

`[6.30297437506, 12.75]`, width `6.44702562494`.

**Supported source-level CANDIDATE_FULL after:**

`[6.30297437506, 12.33]`, width

`6.02702562494`.

This improves the previous source candidate by `0.42` and lies `0.45437096216` below the current independently certified upper endpoint. This is a threshold endpoint for the original exact-sphere Gaussian problem, not an auxiliary constant.

### Demonstrated mechanism gain

Before: objective positivity had to be enclosed together with root existence on a two-dimensional stationarity box.

After: NM03-T03-STATIONARY-TRANSPORT reduces objective positivity to one anchor value plus a one-dimensional bound on `(H_p Psi_B-H_B Psi_p)/Delta` along the stationary branch. The numerical branch from `12.75` to `12.33` has `Delta` bounded well away from zero and transport slope confined to a width below `6.7e-5`.

This is the complementary scope to NM13-07: NM13-07 supplies exact first-derivative Gaussian moment formulas; NM13-03 uses them to transport the comparison value into a materially stronger threshold candidate.

## 7. Failed routes and exclusions preserved

I did not restart:

- the globally exhausted one-parameter/partial-lift upper-bound route;
- the MZZ weighted-second-moment family with its positive-overlap obstruction;
- `N^{-1/2}` sphere nets with `Theta(N log N)` entropy;
- plain Gaussian-polytope facet first moments;
- direct whole-product interval arithmetic, which R14 showed destroys the correlations in `D,c,H,alpha`;
- generic entropy convexity as a sign proof for `H_B`, which R14 showed misses the radial correction;
- smaller-radius / ball / projection-pursuit feasibility;
- replica/full-RSB transition values without a rigorous transfer.

## 8. Essential executed artifacts

Checker source:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_stationary_transport_alpha1233.py`

creation commit:

`4c5cebf39897157d711772196716ad62a673f5c6`.

Archived actual output:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_stationary_transport_alpha1233.out`

creation commit:

`d9a9d5c214211a45a9e0e6c6bb4e6a40e86cfdb7`.

The output ends `ALL_NUMERICAL_SUPPORT_CHECKS_PASS`. It explicitly names the new endpoint `SUPPORTED_CANDIDATE_ALPHA_U 12.33`; it does not label it independently certified.

## 9. Remaining rigorous obligation and next attack

The highest-value next step is now narrower than the previous two-dimensional Hessian program:

1. outward-certify the `12.33` endpoint rectangle's `H_B>0` and `alpha_p>0` using the existing `J_0,...,J_6` second-order compiler plus R14's proved full-line tails;
2. outward-certify either the direct local `Psi>0` bound on `R_33` or the transport hypotheses `Psi(12.75)>=0.01519` and `dPsi/da<=0.0354` on a covering of the one-dimensional branch;
3. read those enclosures through the monotone-face theorem and NM03-T03-STATIONARY-TRANSPORT;
4. only then promote `alpha_U=12.33` into the independently certified bracket.

This is a concrete compact Gaussian-integration problem. No new variational ansatz, radius relaxation, or replica input is needed.

No peer file, shared root ledger, schedule, permission, workflow, email, Drive object, paid compute, or public resource was modified.

```yaml
ledger_delta:
  worker: NM13-03
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, exact radius sqrt(N)"
  status: "PARTIAL / NEW STATIONARY-TRANSPORT THEOREM / CANDIDATE_FULL endpoint 12.33"
  original_problem_metric: "threshold bracket width alpha_U-alpha_L"
  independently_certified_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  independently_certified_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
    movement: "none; outward continuum enclosure still missing"
  supported_candidate_before:
    alpha_U: "12.75"
    width: "6.44702562494"
  supported_candidate_after:
    alpha_U: "12.33"
    width: "6.02702562494"
    improvement_vs_previous_candidate: "0.42"
    improvement_vs_certified_upper: "0.45437096216"
  theorem:
    name: "NM03-T03-STATIONARY-TRANSPORT"
    statement_gain: "comparison-value positivity transported along nondegenerate stationary branch by exact derivative formula"
  application:
    alpha_interval: "[12.33,12.75]"
    Delta_sampled_min: "0.008316369497829384"
    dPsi_dalpha_sampled_range: "[0.035275251864871564,0.03534129805509402]"
    exact_transport_lower_at_12_33: "161/500000 = 0.000322, conditional on rounded enclosure hypotheses"
    direct_Psi_12_33: "0.0003663213384842434"
  named_obstruction_reduced: "two-dimensional Psi positivity enclosure in NM13-07 source-threshold certificate -> one-dimensional stationary-branch transport bound"
  remaining_obligation: "directed compact Gaussian enclosure of endpoint monotonicity and transport slope/anchor; independent review later"
  artifacts:
    code: ".../artifacts/t03_stationary_transport_alpha1233.py @ 4c5cebf39897157d711772196716ad62a673f5c6"
    output: ".../artifacts/t03_stationary_transport_alpha1233.out @ d9a9d5c214211a45a9e0e6c6bb4e6a40e86cfdb7"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
```
