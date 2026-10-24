Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-07 / T03 — exact two-scalar reduction for the full second lift of the negative spherical perceptron

Date: 2026-09-20  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-07`  
Progress root: `proofnet24/NM13-07/progress-perceptron/`  
Parent target: T03, negative spherical Gaussian perceptron at `kappa=-1`  
Status this run: **PARTIAL / SOURCE OPEN / NO SOURCE-BRACKET MOVEMENT**

## 1. Transition handoff and exact target

The later owner policy `operations/PROGRESS20_2026-09-20.md` assigns NM13-07 to T03 and supersedes the older intake/audit-first allocation. I therefore freeze, rather than overwrite, NM13-07's preceding P0282/Chen-LIS work. Its latest substantive report is

`proofnet24/NM13-07/runs/2026-09-19/2026-09-19T22-56-00Z__p0282-bandnorm-15163-25163-row110.md`,

where that unrelated target remained OPEN/PARTIAL with exact finite metric `N_exact=110` and a proved restricted linear region. Nothing in this T03 run edits or reclaims that history.

The T03 source model is frozen exactly as follows. Let `M=floor(alpha N)`, let `g_a` be iid `N(0,I_N)`, and seek

`||sigma||_2=sqrt(N)`,

`<g_a,sigma> >= -sqrt(N)`,  `1<=a<=M`.

Equivalently, with `x=sigma/sqrt(N)`, seek `x` on the **unit sphere** satisfying `Gx >= -1`. A ball relaxation, a smaller-radius sphere, or a replica-only value is not source closure.

The current LIVE20 policy names NM13-03 as the comparison-theory companion. On current `master`, the intended new `proofnet24/NM13-03/progress-perceptron-theory/` root was not yet present when checked; `proofnet24/NM13-03/` exposed only its older `runs/` directory. I therefore did not wait for a nonexistent new companion report and instead reused the already source-matched R14 T03 derivations below.

## 2. Recovered rigorous baseline and current source status

The strongest repository-supported rigorous bracket entering this run is the R14 handoff bracket

`alpha_L = 630297437506/10^11 = 6.30297437506`,

`alpha_U = 1278437096216/10^11 = 12.78437096216`,

so

`W = alpha_U-alpha_L = 6.48139658710`.

The lower endpoint comes from Montanari--Zhong--Zhou's rigorous linear-programming success theorem, after exact model normalization: in the pure-noise model `delta_lin(kappa)=1/Phi(kappa)`, hence at `kappa=-1`, `alpha_c(-1)>=1/Phi(-1)=6.302974375068...`. The upper endpoint is the retained exact certification of the globally optimized one-parameter Stojnic-2013 / MZZ partial-lift Gordon family.

Primary-source hypotheses/status rechecked this run:

1. El Alaoui--Sellke, arXiv:2010.15811, uses exactly the Gaussian disorder and sphere radius `sqrt(N)` above. For negative `kappa`, its algorithm is conditional on the relevant Parisi/FRSB structure and returns a vector on radius `sqrt(qbar N)` with `qbar<1`; the paper explicitly says obtaining a genuine point on the radius-`sqrt(N)` sphere requires new ideas. Thus it is not a proof of the exact full-radius threshold.
2. Stojnic, arXiv:2312.16531, treats the Gaussian NSP on the unit sphere, connects feasibility to the sign of the random feasibility/free-energy problem, and develops stationarized fully lifted RDT. Its paper states that making the characterization operational requires substantial numerical work. The second-full and third-full displayed capacity values are numerical evaluations of stationarity systems unless separately certified.
3. Montanari--Zhong--Zhou, arXiv:2110.15824 / PTRF 2024, rigorously proves upper and lower bounds on the negative-perceptron threshold and the LP threshold; it does not identify the exact `kappa=-1` threshold.

A bounded 2026-09-20 search for later rigorous full-radius negative-spherical-perceptron capacity results found no theorem replacing the exact bracket above. This is negative search evidence, not a worldwide openness or priority certificate. Replica/full-RSB/jamming calculations remain useful guides but are not inserted into the rigorous bracket.

`POSTED.md` was also checked: it explicitly distinguishes posted zero-margin/Ising-perceptron work from the unrestricted negative-margin spherical target. This T03 target is therefore not a duplicate of the posted Ising result.

## 3. Source-level before/after versus mechanism progress

### Source-level metric

Before:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

After this run:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**No source-level movement is claimed.** The owner requested a strict bracket improvement; this invocation does not yet meet that final requirement because the remaining compact Gaussian quadrature/root certificate has not been made rigorous. I do not promote a numerical stationary point to a theorem.

### Demonstrated mechanism gain

The inherited complete second-full stationarity system has three nonlinear unknowns `(p,D,gamma)` at fixed `alpha`, with three scalar Gaussian expectations. This run proves that it can be reduced **exactly** to a two-scalar system in `(p,B)`, with `D`, `alpha`, and `gamma` reconstructed algebraically. For the capacity point itself, the system is again only two scalar equations. This removes one root variable and one entire stationarity equation from the certification problem.

A numerical-only sanity check then finds at `alpha=12.75` a second-full stationary point with comparison margin about `+0.015200993467`, much larger than the old `alpha=12.5` scout margin. If the compact integral/root enclosure is validated, this would immediately give the strict candidate upper endpoint `12.75`, shrinking the rigorous width to `6.44702562494`, an improvement of `0.03437096216`. That statement is **CONDITIONAL**, not current bracket movement.

## 4. Inherited source-matched second-full equations

Retain the exact R14 reduction of Stojnic's second-full stationarity. Let

`q=p D^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`.

For

`h_B(x)=exp(-B (x-1)_+^2)`,

`f_{p,B}(z)=E_H h_B(sqrt(p) z+sqrt(1-p)H)`,

put

`I(p,B)=E_Z log f_{p,B}(Z)`,

`I_B=partial_B I`,

`K=E_Z[(partial_z log f_{p,B}(Z))^2]`.

The Ornstein--Uhlenbeck identity proved in the predecessor chain is

`I_p = -K/(2p)`.

Let

`T(p,D,gamma) = (1/2)(1-pq)c - gamma_p + (1/(2c)) log(D/(2 gamma_p)) - q/(2D) + gamma`.

Writing derivatives of `c,T` as subscripts, complete second-full stationarity is equivalent, on the inherited interior branch with `c_D != 0`, to

`R1 = I_B + 4 gamma^2/alpha = 0`,

`R2 = I - B I_B + c^2 T_D/(alpha c_D) = 0`,

`R3 = K/(2p) + (c/alpha)(T_p-(c_p/c_D)T_D) = 0`.

The predecessor had already certified tiny tails for `I,I_B,K` outside `|z|<=9` near its `alpha=12.5` root. Its blocker was validated compact quadrature plus a three-dimensional stationary-root certificate.

## 5. New theorem-sized reduction

### Lemma T03-NM07-FULL2-2SCALAR

Assume `0<p,D<1`, `B>0`, the source-matched complete second-full equations above, and `c_D != 0`. Then every stationary point is determined by `(p,B)` as follows:

`D^2 = K(p,B)/[-4 p^2 B^2 I_B(p,B)]`,

`c=c(p,D)`,

`alpha = -c^2/[4 B^2 I_B(p,B)]`,

`gamma=c/(4B)`,

and `(p,B)` satisfies the single scalar equation

`H(p,B):= I - B I_B - 4 B^2 I_B (T_D/c_D) = 0`,

where in `T_D` one substitutes `gamma=c/(4B)` and the reconstructed `D`.

Conversely, if `0<p<1`, `B>0`, the displayed reconstruction yields `0<D<1` and `c_D!=0`, and `H(p,B)=0`, then the reconstructed `(p,D,gamma,alpha)` satisfies all three residuals `R1=R2=R3=0`.

Moreover, the second-full comparison/free-energy value on this stationary reconstruction is

`Psi(p,B) = T(p,D,c/(4B)) + c I/(4 B^2 I_B)`.

Hence:

- a fixed-density second-full stationary certificate at `alpha=alpha0` reduces to the **two scalar equations**
  `H(p,B)=0`, `alpha(p,B)=alpha0`;
- the full second-lift capacity candidate reduces to the **two scalar equations**
  `H(p,B)=0`, `Psi(p,B)=0`.

### Proof

For `B>0`, increasing `B` strictly decreases `h_B(x)` on the event `x>1`, which has positive conditional Gaussian probability; therefore `I_B<0`. Also `K>=0`, with strict positivity on the nonconstant branch. Thus the reconstructed quantities below have the expected signs whenever they lie in the interior source branch.

First use `B=c/(4gamma)` in `R1=0`:

`I_B + c^2/(4 B^2 alpha)=0`.

Therefore

`alpha = -c^2/(4 B^2 I_B)`.                                           (5.1)

The key cancellation is deterministic. Direct differentiation of the displayed elementary function `T` and `c` gives the exact identity

`T_p - (c_p/c_D) T_D = -(p D^2 c)/2`                                  (5.2)

after substituting `gamma=c/(4B)`. The executed symbolic checker verifies (5.2) identically, not at a numerical point.

Substituting (5.2) into `R3` gives

`R3 = [K - p^2 D^2 c^2/alpha]/(2p)`.

Thus `R3=0` is equivalent to

`K = p^2 D^2 c^2/alpha`.

Use (5.1):

`K = -4 p^2 D^2 B^2 I_B`,

so

`D^2 = K/[-4 p^2 B^2 I_B]`.                                           (5.3)

This reconstructs `D` from `(p,B)` and the two scalar OU expectations `I_B,K`; then (5.1) reconstructs `alpha`, and `gamma=c/(4B)` reconstructs `gamma`.

Finally substitute (5.1) into `R2`:

`R2 = I-B I_B-4B^2 I_B(T_D/c_D)`.

Thus `R2=0` is exactly `H(p,B)=0`. This proves the forward reduction. Conversely, definitions (5.1) and `gamma=c/(4B)` make `R1=0`; (5.3) and (5.2) make `R3=0`; and `H=0` makes `R2=0`, proving equivalence on the stated interior branch.

For the objective

`F = T - alpha I/c`,

substituting (5.1) gives

`F = T + c I/(4B^2 I_B)=Psi`,

which proves the last assertion. QED.

This is a mechanism theorem about the exact source-matched second-full stationary equations; it is **not** by itself an NSP capacity theorem because the remaining Gaussian expectations and root still need rigorous enclosure before Stojnic's feasibility implication can be invoked at a new density.

## 6. Executed sanity checks and numerical scouting

Executed artifact:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_full2_reduction.py`

Archived output:

`proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_full2_reduction.out`

The exact symbolic part verifies:

- (5.1) from `R1`;
- identity (5.2);
- `R3=[K-p^2D^2c^2/alpha]/(2p)`;
- the reconstruction (5.3);
- exact equality of `R2` with `H` after reconstruction;
- exact equality of the stationary objective with `Psi`.

It ends `ALL_EXACT_ALGEBRA_CHECKS_PASS`.

The same artifact then performs an explicitly labeled **NUMERICAL_ONLY** 120-node Gauss--Hermite/JAX scout.

It first reproduces the inherited `alpha=12.5` point from only `(p,B)`:

`p=0.656313184757223`, `B=5.590132429288564`,

reconstructing

`D=0.6526536898204747`, `alpha=12.499999999999979`, `gamma=0.1588618550122417`,

with `H` at numerical zero and `Psi=0.006373969149840508`.

At the conservative target `alpha=12.75`, the new two-dimensional solve gives

`p=0.6457670646889506`, `B=4.929229200895245`,

`D=0.6601219023283809`, `c=3.3578624160013266`,

`gamma=0.17030362553396142`, `q=0.2814000540463062`,

`gamma_p=1.5365408264934368`,

with

`I=-0.11844944245754509`,

`I_B=-0.009099082312160538`,

`K=0.16069992652985324`,

and numerical residuals

`H=1.25e-16`, `alpha-12.75=1.95e-14`,

while

`Psi=+0.0152009934671678`.

This is strong numerical slack but is **not** a rigorous endpoint.

As a separate sanity check, solving the reduced capacity equations `H=Psi=0` gives

`alpha=12.319634346586879`,

`p=0.6649244864115346`, `B=6.197657822533089`,

`D=0.6466174492753871`, `c=3.719795964217405`,

`gamma=0.15004845664007072`, `q=0.27801432029740597`,

`gamma_p=1.6661284334279283`.

These parameters reproduce, to the displayed precision, the second-full numerical values reported in Stojnic's `kappa=-1` table. That agreement is a useful model/normalization check, not an independent proof of the table or of the threshold.

## 7. Why the bracket does not move yet

A strict new rigorous upper endpoint requires more than a floating-point root. The exact missing statement is now much smaller than in the R14 handoff:

> On a tiny rectangle around `(p,B)=(0.64576706469,4.92922920090)`, rigorously enclose `I,I_B,K` and certify a zero of `(H,alpha-12.75)`; at that certified zero prove `Psi>0`.

The previous R14 route required a validated three-dimensional zero in `(p,D,gamma)` plus the same Gaussian calculations. The lemma above removes `D` and `gamma` from the root problem and turns their consistency into algebraic reconstruction. The comparison margin `~0.0152` at `12.75` leaves much more room than the old `12.5` scout.

I did not complete a trustworthy outward-rounded compact Gaussian quadrature in this invocation. Therefore promoting `12.75` would fabricate progress and is explicitly forbidden.

## 8. Next attack

The next run should stay on this route but change the computational core:

1. Construct validated interval enclosures for `I(p,B)`, `I_B(p,B)`, and `K(p,B)` on `|z|<=9` over a tiny `(p,B)` box around the `12.75` scout. Reuse or re-prove Gaussian tails outside that interval for the new box.
2. Use a 2D Poincare--Miranda or interval-Newton/Krawczyk certificate on `(H,alpha-12.75)`; no `D`/`gamma` root dimensions remain.
3. Reconstruct `D,c,gamma,q,gamma_p` by interval arithmetic and verify the interior branch and all source stationarity hypotheses.
4. Enclose `Psi` strictly above zero. Only then invoke the source comparison/feasibility theorem and move `alpha_U` from `12.78437096216` to `12.75`.
5. After that conservative first endpoint, tighten toward the numerical second-full crossing `12.3196343465...` rather than jumping directly to the table value.

A distinct fallback, if validated quadrature stalls again, is an overlap/second-moment lower-bound optimization from MZZ; it should be pursued only after a preliminary certified calculation shows it can beat `1/Phi(-1)` at `kappa=-1`.

## 9. Literature/access scope

Fresh web checks dated 2026-09-20 covered exact arXiv records for `2010.15811`, `2312.16531`, `2110.15824`, plus queries for 2025--2026 rigorous negative-spherical-perceptron threshold/full-RSB work. No later full-radius exact theorem was found in that bounded search. The conclusion is only that no such theorem was recovered here.

The new companion progress root for NM13-03 was not available on current `master`, so this run could not consume a post-LIVE20 comparison-theory report. This does not block the exact reduction, which is complementary to comparison theory: it lowers the dimensionality of the source-matched dual stationary certificate rather than proving a new Gaussian comparison inequality.

## 10. Ledger delta

```yaml
ledger_delta:
  worker: NM13-07
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, exact sphere radius sqrt(N)"
  status: "PARTIAL / OPEN"
  source_metric: "rigorous threshold bracket width alpha_U-alpha_L"
  before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  source_movement: "NONE — validated compact root/quadrature not yet complete"
  mechanism_gain:
    theorem: "T03-NM07-FULL2-2SCALAR"
    statement: "complete second-full stationarity reduces exactly from three variables to the two-scalar systems (H,alpha-alpha0) or (H,Psi) with algebraic D,alpha,gamma reconstruction"
    candidate_if_validated:
      alpha_U: "12.75"
      width: "6.44702562494"
      improvement: "0.03437096216"
      numerical_Psi_margin: "+0.0152009934671678"
      status: "CONDITIONAL / NUMERICAL ROOT ONLY"
  executed_artifacts:
    code: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_full2_reduction.py"
    output: "proofnet24/NM13-07/progress-perceptron/runs/2026-09-20/artifacts/t03_full2_reduction.out"
    exact_output_marker: "ALL_EXACT_ALGEBRA_CHECKS_PASS"
  residual_obstruction: "outward-rounded compact Gaussian enclosure and 2D root certificate at alpha=12.75, followed by strict Psi>0"
  next_attack: "validated I,I_B,K quadrature + 2D interval Newton/Poincare-Miranda on (H,alpha-12.75)"
  handoff_preserved: "P0282 predecessor frozen at N_exact=110; no files overwritten"
```

No email, Drive, public posting, paid compute, workflow execution, access change, schedule change, or peer-file overwrite was performed.
