Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested but is not authenticated by this runtime.**

# NM13-07 / T03 — certified stationary micro-continuation improves the exact-sphere upper endpoint to 12.31963485

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
LIVE20 parent: **T03 negative spherical perceptron**  
Companion: `NM13-03`  
Status: **PARTIAL / CANDIDATE_FULL COMPUTER-ASSISTED UPPER-BOUND IMPROVEMENT / INDEPENDENT REVIEW PENDING**

## 1. Compact handoff and exact source target

The exact source model remains frozen:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)` exactly;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- fixed `alpha`, `N->infinity`.

Equivalently `x=sigma/sqrt(N)` lies on the unit sphere and satisfies `Gx>=-1`. No radius change, ball relaxation or replica-only threshold is used as a source implication.

The latest NM13-07 report certified `alpha_U=12.75`. The companion NM13-03 report committed immediately before this run then consumed the same source-matched complete-second-lift equations and proved an a-posteriori interval certificate at

`alpha_0 = 12.319635`,

with a true-stationary-root comparison lower bound

`Psi(alpha_0) >= 23584189005311 / 1090044380000000000000`

`             = 2.163598972485047e-8 > 0`.

That report therefore moves the current supported exact-sphere upper endpoint entering this invocation to `12.319635`. This invocation does not reset the baseline to NM13-07's older `12.75` value.

The companion also notes that the complete-second comparison zero is numerically near `12.3196343465869`, so further second-level gain is intrinsically tiny. I nevertheless use the companion's exact box as an anchor to prove a strict source-level improvement without another Gaussian quadrature run. The main mathematical gain is a reusable certified branch-continuation lemma with an elementary analytic envelope bound.

## 2. Primary-source hypotheses and current proof status

Fresh bounded source screening on 20 September 2026 remains consistent with the repository handoff.

1. **El Alaoui--Sellke, arXiv:2010.15811.** Their source model is the iid Gaussian spherical perceptron on radius `sqrt(N)`, with constraints `<g_a,sigma> >= kappa sqrt(N)`. For `kappa<0`, the algorithm uses the conjectural FRSB/Parisi structure and outputs a feasible vector on radius `sqrt(qbar N)` with `qbar<1`; this is not the exact full-radius satisfiability-threshold theorem required here.
2. **Stojnic, arXiv:2312.16531.** This puts the negative spherical perceptron into stationarized fully lifted RDT and states a capacity characterization, while explicitly noting that making the construction practically operational requires substantial numerical work. The present proof consumes the already source-matched complete-second stationary system and its inherited comparison implication; it does not treat unvalidated finite-lift numerics as a theorem.
3. **Montanari--Zhong--Zhou, arXiv:2110.15824.** This rigorously gives upper and lower interpolation-threshold bounds and characterizes the LP threshold, but does not determine the exact `kappa=-1` threshold.
4. **Annesi--Malatesta--Zamponi, arXiv:2410.06717.** This computes the SAT/UNSAT transition using a full-RSB ansatz and is a structural/numerical guide, not a substitute here for a rigorous exact-radius comparison certificate.
5. **Huang--Sellke--Sun, arXiv:2608.29416, submitted 29 August 2026.** This gives exact algorithmic projection-pursuit thresholds for a dimension-free Lipschitz algorithm class and explicitly distinguishes the non-algorithmic feasible-projection problem as still open.

A bounded fresh search found no later rigorous theorem plainly closing the exact full-radius `kappa=-1` target. This is dated negative evidence, not a worldwide novelty certificate. `POSTED.md` continues to separate the owner's zero-margin/Ising perceptron work from this continuous negative-margin spherical target.

## 3. Consumed certified complete-second box

From NM13-03's new `alpha_0=12.319635` certificate, use the center

`p_c = 0.6649244534165579`,

`B_c = 6.197655366469065`,

with radii

`r_p=1e-7`, `r_B=4e-6`.

On the entire box the directed-interval computation certified

`H_p in [-0.03370146727424432,-0.02828455987858220]`,

`H_B in [0.0003284932328676832,0.0005043842197013973]`,

`alpha_p in [24.67157455631033,25.28760973547386]`,

`alpha_B in [-0.6024378692892906,-0.6008000232876709]`,

and

`c in [3.719659086779107,3.719931529382793]`.

The same source gives

`|H_c| < 4.7e-12`,

`alpha_c in [12.3196349999636175,12.3196350000364623]`,

and the frozen rational preconditioner

`A = [[-7294853/100000, -504965/10000000],`
`     [-3028867/1000,   -3758826/1000000]]`.

With `D_r=diag(1e-7,4e-6)`, exact vertex enumeration gives

`q = 70497781/125000000 = 0.563982248 < 1`

for the weighted derivative norm of `I-A DF_alpha`, uniformly because changing the target density changes only the constant second residual `alpha(p,B)-alpha_target`, not its Jacobian.

## 4. New theorem — uniform micro-continuation from one certified stationary anchor

### Theorem NM07-T03-MICROCONTINUATION

Let

`alpha_1 = 12.31963485`,

`alpha_0 = 12.319635`.

For every `a in [alpha_1,alpha_0]`, the complete-second system

`F_a(p,B)=(H(p,B), alpha(p,B)-a)=0`

has a unique zero in the certified NM13-03 box. These zeros form a `C^1` stationary branch. Along that branch the complete-second comparison value satisfies

`0 < dPsi/da = -I/c < 2/15`.

Consequently

`Psi(alpha_1) > 0`,

so the inherited stationarized fl-RDT comparison implication yields

`alpha_c(-1) <= 12.31963485`

for the exact iid-Gaussian radius-`sqrt(N)` spherical perceptron.

### Proof, part A: one contraction proves existence for every density in the interval

The target shift is

`alpha_0-alpha_1 = 3/20000000 = 1.5e-7`.

Together with the certified center-density error `<3.7e-11`, every `a` in the interval obeys the safe rational residual ceiling

`|alpha_c-a| < 1501/10^10 = 1.501e-7`.

Using the same preconditioner and the same whole-box Jacobian enclosure as at the anchor, exact arithmetic gives the uniform center-displacement bound

`eta <= 231374183/1600000000`

`    = 0.144608864375`.

Since

`1-q = 54502219/125000000 = 0.436017752`,

we have `eta<1-q`. Therefore for every target `a` the fixed-point map

`T_a(x)=x-A F_a(x)`

maps the certified weighted box into itself and is a contraction with the same constant `q`. Banach's theorem gives a unique zero `x(a)` in that box. The exact a-posteriori localization radius is uniformly

`rho <= eta/(1-q)`

`     = 1156870915/3488142016`

`     = 0.33165820362057186 < 1`.

Moreover `||I-A DF_a||<1` implies `A DF_a` is invertible throughout the box; since `A` is invertible, `DF_a` is invertible. The implicit-function theorem therefore makes the unique fixed points a `C^1` branch over the entire interval.

### Proof, part B: an elementary exact Gaussian bound gives a global envelope slope `<2/15`

NM13-03 proved the exact stationary-envelope identity

`dPsi/da = -I/c > 0`,

where

`I = E_Z log f_{p,B}(Z)`,

`f_{p,B}(z)=E_H exp[-B(Y_+)^2]`,

`Y=sqrt(p)z+sqrt(1-p)H-1`.

For fixed `z`, Jensen's inequality for `log` gives

`log E_H exp[-B(Y_+)^2] >= E_H[-B(Y_+)^2]`.

Hence

`-I <= B E_{Z,H}(Y_+)^2`.

Unconditionally `sqrt(p)Z+sqrt(1-p)H` is a standard normal `G`, independently of `p`, so

`-I <= B m_2`,

`m_2 := E[(G-1)_+^2]`.

Now

`m_2 = 2 Q(1)-phi(1)`,

where `Q(1)=P(G>1)` and `phi` is the standard normal density. I use only elementary rational inequalities to show

`Q(1)<4/25`, `phi(1)>6/25`,

hence

`m_2<2/25`.

For completeness, the rational proof is as follows.

- From the classical Archimedean inequality `pi<22/7` and `(627/250)^2>44/7`,
  `phi(0)=1/sqrt(2pi)>250/627`.
- For `0<=u<=1/2`, the alternating Taylor series gives
  `exp(-u)>=1-u+u^2/2-u^3/6`. Integrating with `u=x^2/2` on `[0,1]` gives
  `int_0^1 exp(-x^2/2) dx >= 479/560`.
  Therefore
  `phi(0) int_0^1 exp(-x^2/2)dx > 11975/35112 > 17/50`,
  and so
  `Q(1)=1/2-phi(0)int_0^1 exp(-x^2/2)dx <4/25`.
- Also `e^(1/2)<33/20`: after the terms `1+1/2+1/8`, the `n>=3` tail begins at `1/48` and has successive ratio at most `1/8`, so the tail is at most `1/42`; the resulting sum is `<33/20`. Hence `e^(-1/2)>20/33`, and therefore
  `phi(1)> (250/627)(20/33)=5000/20691>6/25`.

This proves `m_2<2/25`.

On the certified stationary box,

`B < 6.19766 = 619766/100000`,

`c > 3.71965 = 371965/100000`.

Because

`3*619766 < 5*371965`,

we have `B/c<5/3`. Thus on the whole branch

`0 < dPsi/da = -I/c < (5/3)(2/25)=2/15`.                 (4.1)

### Proof, part C: transport the already certified positive comparison value

At the true stationary anchor root `alpha_0`, NM13-03 certified

`Psi(alpha_0) >= 23584189005311/1090044380000000000000`.

Integrating (4.1) downward by

`delta=alpha_0-alpha_1=3/20000000`

gives

`Psi(alpha_1)`
` >= 23584189005311/1090044380000000000000 - (2/15)(3/20000000)`
` = 1783301405311/1090044380000000000000`
` = 1.6359897248504689e-9 > 0`.

Thus the true stationary root at `alpha_1=12.31963485` has positive complete-second comparison value. The box keeps `p,D,q,gamma_p,c,gamma` in the interior source branch, so the inherited source comparison theorem applies exactly as at the anchor. Therefore the exact-sphere model is asymptotically UNSAT at this density, and by monotonicity in the number of constraints

`boxed: alpha_c(-1) <= 12.31963485`.

QED.

## 5. Source-level before/after and demonstrated mechanism gain

### Original T03 threshold bracket

Retained rigorous lower endpoint:

`alpha_L = 6.30297437506`.

**Before this invocation, after consuming the companion's immediately preceding certificate:**

`[6.30297437506, 12.319635]`,

width

`6.01666062494`.

**After this invocation:**

`[6.30297437506, 12.31963485]`,

width

`6.01666047494`.

Strict upper-endpoint / width improvement:

`1.5e-7`.

This is small because the complete-second comparison zero is already nearly reached; it is nevertheless a source-level improvement for the original exact-radius model, not an auxiliary constant.

### Demonstrated mechanism gain

Before: each sharper density appeared to require another directed Gaussian quadrature certificate centered at a new root.

After: one certified contraction box plus the exact envelope identity yields a **uniform continuum of stationary roots**, and a simple analytic Gaussian moment bound transports objective positivity to a lower density with no new quadrature. The reusable transfer is

`certified anchor + uniform contraction + B/c bound + E[(G-1)_+^2] bound`

`=> certified source upper endpoint on an interval below the anchor`.

The exact checker verifies all rational contraction and transport arithmetic independently of floating-point integration.

## 6. Essential executed artifact and sanity checks

Exact checker source:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_microcontinuation_alpha1231963485.py`

creation commit:

`dd40e11663967ffc60841d97dcda9dbceb4cf3d9`.

Archived actual output:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_microcontinuation_alpha1231963485.out`

creation commit:

`81ef7b73db35ef7d8ab709285c7ebf8385af6474`.

The executed output includes

`Q_EXACT 70497781/125000000`,

`ETA_UNIFORM_EXACT 231374183/1600000000`,

`ENVELOPE_SLOPE_UPPER 2/15`,

`PSI_NEW_LOWER 1783301405311/1090044380000000000000`,

and ends

`ALL_EXACT_MICROCONTINUATION_CHECKS_PASS`.

## 7. Residual obstruction and next attack

This run deliberately does not pretend that shaving the remaining complete-second digits will materially solve T03. The high-accuracy second-full crossing is numerically around

`12.3196343465869`,

only about `5.0e-7` below the new certified endpoint. Therefore the second-full mechanism has essentially saturated.

The next attack should be materially different and seek a non-microscopic gain:

1. derive the **third-full / next lifting-level** stationary reduction in a form analogous to NM13-07's two-scalar complete-second system, then seek an a-posteriori contraction/objective certificate; or
2. derive an independent overlap/dual-feasibility inequality that improves the `12.31963485` upper endpoint without relying on finite-level full-lift convergence.

A further run whose only achievement is another decimal shaving of the complete-second endpoint should not be counted as substantial progress.

No historical or peer file was overwritten. No shared root ledger, schedule, permission, workflow, email, Drive object, paid resource or public resource was modified.

```yaml
ledger_delta:
  worker: NM13-07
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, iid constraints, exact radius sqrt(N)"
  status: "PARTIAL / CANDIDATE_FULL / STRICT RIGOROUS-BRACKET IMPROVEMENT / INDEPENDENT REVIEW PENDING"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
  source_metric: "upper endpoint and width of exact-sphere threshold bracket"
  before:
    alpha_L: "6.30297437506"
    alpha_U: "12.319635"
    width: "6.01666062494"
  after:
    alpha_L: "6.30297437506"
    alpha_U: "12.31963485"
    width: "6.01666047494"
  source_movement:
    upper_endpoint_gain: "0.00000015"
    width_gain: "0.00000015"
  mechanism_gain:
    theorem: "NM07-T03-MICROCONTINUATION"
    uniform_contraction_q: "70497781/125000000"
    uniform_eta: "231374183/1600000000"
    uniform_rho: "1156870915/3488142016"
    gaussian_second_moment_bound: "E[(G-1)_+^2] < 2/25"
    envelope_slope_bound: "0 < dPsi/dalpha < 2/15"
    new_true_root_Psi_lower: "1783301405311/1090044380000000000000"
  consumed_companion:
    report: "proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/2026-09-20__t03-aposteriori-objective-alpha12319635.md"
    report_commit: "02ec2e9f8f1ef961166d928eaabefe3a10a7d6ce"
  artifacts:
    checker_commit: "dd40e11663967ffc60841d97dcda9dbceb4cf3d9"
    output_commit: "81ef7b73db35ef7d8ab709285c7ebf8385af6474"
  residual_obstruction: "complete-second comparison zero is essentially saturated; substantial gain requires next lifting level or a distinct overlap/feasibility mechanism"
  next_attack: "third-full stationary reduction or independent overlap/dual-feasibility upper bound; do not spend another run only shaving complete-second digits"
```
