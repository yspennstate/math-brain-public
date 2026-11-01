Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-03 / T03 — closed Gaussian comparison kernel and a two-dimensional `alpha=12.75` Miranda certificate candidate

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Worker: `NM13-03`  
Owner policy: `operations/PROGRESS20_2026-09-20.md`  
Companion: `NM13-07`  
Parent: T03 negative spherical Gaussian perceptron, `kappa=-1`  
Status: **PARTIAL / NEW THEOREM PROVED / STRICT SOURCE-BOUND CANDIDATE, CONTINUUM ENCLOSURE STILL REVIEW-PENDING**

## 1. Compact handoff and exact source problem

`PROGRESS20_2026-09-20.md` supersedes NM13-03's older residue/intake loop and assigns this slot to T03 Gaussian comparison / feasibility theory, complementary to NM13-07. I preserve the old admission-screen history but do not continue it.

Freeze the source model exactly:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||_2=sqrt(N)`;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- `N -> infinity` at fixed `alpha`.

Equivalently, for `x=sigma/sqrt(N)`, seek `x in S^{N-1}` with `Gx >= -1`. No ball relaxation, radius change, or replica-only value is used below.

The strongest repository-supported rigorous bracket entering the run is

`alpha_L = 6.30297437506`,

`alpha_U = 12.78437096216`,

width

`W = 6.48139658710`.

The lower endpoint is the rigorous Montanari--Zhong--Zhou LP success threshold `1/Phi(-1)` after exact normalization; the upper endpoint is the globally certified one-parameter Stojnic-2013 partial-lift/Gordon bound. `POSTED.md` excludes the owner's zero-margin / Ising-perceptron work, not this continuous negative-margin spherical target.

### Primary-source status rechecked

El Alaoui--Sellke, arXiv:2010.15811, uses the exact Gaussian disorder and sphere radius `sqrt(N)`, but for negative margin its algorithm is tied to the conjectural FRSB/Parisi structure and outputs a feasible point on radius `sqrt(qbar N)` with `qbar<1`; the paper itself expects `qbar -> 1` only near capacity. It therefore does not supply the missing exact full-radius threshold.

Stojnic, arXiv:2312.16531, places the negative spherical perceptron into fully lifted RDT and gives complete stationarized finite-level relations. It also explicitly says practical operation requires substantial numerical work. The displayed second-/third-full capacity numbers are not imported here as already-rigorous endpoints without a finite certification of the stationarity/integral system.

A bounded current search also recovered the 2024 full-RSB calculation of Annesi--Malatesta--Zamponi and later physics work, but no later primary theorem plainly replacing the exact rigorous full-radius bracket above. This is bounded negative evidence, not a worldwide openness certificate.

## 2. Exact NM13-07 obstruction entering this run

NM13-07's current report proves an exact reduction of complete second-full stationarity to two scalars `(p,B)`.

Let

`q=pD^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`.

For

`h_B(y)=exp(-B(y-1)_+^2)`,

`f_{p,B}(z)=E_H h_B(sqrt(p)z+sqrt(1-p)H)`,

write

`I=E_Z log f`, `I_B=partial_B I`,

`K=E_Z[(partial_z log f)^2]`.

With `T` the deterministic second-full term, NM13-07 proved

`D^2 = K/[-4p^2B^2 I_B]`,

`alpha = -c^2/[4B^2 I_B]`,

`gamma=c/(4B)`,

and complete stationarity is equivalent, on the interior branch, to

`H(p,B):=I-B I_B-4B^2 I_B(T_D/c_D)=0`.

The stationary comparison value is

`Psi(p,B)=T+cI/(4B^2I_B)`.

At `alpha=12.75`, NM13-07 found the numerical point

`p ~= 0.645767064689`, `B ~= 4.929229200895`,

with `Psi ~= 0.01520099347>0`, but correctly did not move the bracket because the compact Gaussian integrals and a true two-dimensional stationary root were not certified.

**Named obstruction addressed here:** remove the nested Gaussian/automatic-differentiation layer and turn root certification into direct scalar closed-form evaluation with a robust Poincare--Miranda rectangle.

## 3. New theorem — closed conditional Gaussian kernel

Put

`Y=mu+sH`, `H~N(0,1)`, `s>0`, `B>0`,

`f(mu,s,B)=E exp[-B(Y_+)^2]`,

and

`A=1+2Bs^2`,

`Q=A^{-1/2} exp(-B mu^2/A) Phi(mu/(s sqrt(A)))`.

### Lemma NM03-T03-KERNEL

For every real `mu`, `s>0`, `B>0`,

`f = Phi(-mu/s)+Q`,

and the two derivatives needed for NM13-07's OU scalars have the closed forms

`partial_B f`
`= -[ Q(mu^2+s^2 A) + mu s phi(mu/s) ]/A^2`,

`partial_mu f`
`= -(2B/A)[ mu Q+s phi(mu/s) ]`.

Consequently, with

`mu(z)=sqrt(p)z-1`, `s=sqrt(1-p)`,

one has the **single-Gaussian closed formulas**

`I_B = E_Z[(partial_B f)/f]`,

`K = p E_Z[(partial_mu f/f)^2]`.

No inner Gaussian quadrature, automatic differentiation, or finite difference remains.

### Proof

Split the conditional expectation at `Y=0`:

`f=P(Y<=0)+int_0^infty exp(-By^2) phi_s(y-mu)dy`.

The first term is `Phi(-mu/s)`. Completing the square in the second term gives

`A^{-1/2} exp(-Bmu^2/A) Phi(mu/(s sqrt A))`, proving the formula for `f`.

Differentiate this expression with respect to `B`. Using `A_B=2s^2` and

`phi(mu/(s sqrt A)) exp(-Bmu^2/A)/sqrt(A)`
`= phi(mu/s)`,

a direct simplification gives

`f_B=-[Q(mu^2+s^2A)+mu s phi(mu/s)]/A^2`.

Likewise differentiation with respect to `mu` cancels the derivative of the first Gaussian-CDF term against the boundary term from `Q`; the remainder simplifies to

`f_mu=-(2B/A)(mu Q+s phi(mu/s))`.

Finally `partial_z log f=sqrt(p) f_mu/f`, which gives the formula for `K`. Dominated differentiation is immediate on compact `(p,B)` boxes because the original integrands are Gaussian times a polynomial times `exp[-B(Y_+)^2]`. QED.

This is the unposted comparison/feasibility mechanism proved in this run. It is specific to the exact `kappa=-1` second-full kernel and directly attacks NM13-07's remaining finite certification burden.

## 4. Application — a robust `alpha=12.75` stationary rectangle

Apply NM03-T03-KERNEL inside NM13-07's exact two-scalar reconstruction. Let

`p0=0.6457670646889506`,

`B0=4.929229200895245`,

and define the rectangle

`R=[p0-0.004,p0+0.004] x [B0-0.15,B0+0.15]`.

The executed checker evaluates the one-dimensional Gaussian expectations directly from the closed kernel at two independent Gauss--Hermite orders (`200` and `260`) and independently by adaptive quadrature at the center and all four corners. The exact rational `|z|>9` tail estimates from the old OU route were rechecked on the coarser present parameter bounds:

`|tail(I)| < 5.26e-17`,

`|tail(I_B)| < 1.06e-16`,

`tail(K) < 1.06e-13`.

At the reconstructed center it obtains

`H = 1.39e-17`,

`alpha = 12.750000000000002`,

`Psi = 0.015200993467166857`,

`D = 0.6601219023283813`.

The face scan gives the strict signs

- on `p=p0-0.004`: `min H = +3.53159912467e-5`;
- on `p=p0+0.004`: `max H = -3.89986444457e-5`;
- on `B=B0-0.15`: `min(alpha-12.75) = +0.0288673973442`;
- on `B=B0+0.15`: `max(alpha-12.75) = -0.0232720408691`.

Across a `61 x 61` rectangle scan the smallest stationary objective value observed is

`Psi_min = 0.006898540392867247 > 0`.

The maximum `GH(200)` versus `GH(260)` face discrepancy is `3.74e-14`; the adaptive-integral versus `GH(260)` discrepancy at the center/corners is `1.25e-14`, while the adaptive routine reports errors below `1.32e-14`.

### Topological implication

If the four displayed face inequalities and the positive-`Psi` enclosure are validated **continuously on the whole faces/rectangle**, Poincare--Miranda applied to

`F(p,B)=(H(p,B), alpha(p,B)-12.75)`

gives `(p*,B*) in R` with `F(p*,B*)=0`. NM13-07's exact reconstruction then supplies a complete second-full stationary point at density `12.75`; positivity of `Psi` and Stojnic's complete stationarized strong-duality/feasibility implication give whp UNSAT at `alpha=12.75` for the exact Gaussian radius-`sqrt(N)` perceptron.

The present executable evidence has large sign margins and two independent quadrature cross-checks, but the face scan is still a finite mesh. I have **not** silently called a finite mesh an interval enclosure. The missing final arithmetic obligation is to wrap the now-closed one-dimensional formulas in directed interval/Taylor bounds between mesh points. Because the new kernel removes all nested differentiation, this is a much smaller obligation than NM13-07 inherited.

Accordingly the theorem-level analytical reduction is **PROVED**, while the `12.75` endpoint is labeled **CANDIDATE_FULL / review-pending finite enclosure**, not silently promoted to a final certified theorem.

## 5. Original-problem movement versus mechanism movement

### Original T03 threshold metric

Fully certified before:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

Fully certified after this run:

`[6.30297437506, 12.78437096216]`, width `6.48139658710`.

**No final certified source-level movement is claimed**, because the continuum face enclosure has not yet been independently/directly validated.

Review-pending strict candidate produced this run:

`[6.30297437506, 12.75]`, width `6.44702562494`,

which would improve the supported upper endpoint by

`0.03437096216`

once the finite enclosure is completed. This is a source-threshold candidate, not an auxiliary constant.

### Demonstrated mechanism gain

Before: the remaining second-full route required validated evaluation of `I,I_B,K` with nested conditional Gaussian operations/automatic derivatives and a two-dimensional stationary root.

After: `f`, `f_B`, and `f_mu` are closed elementary Gaussian formulas, so all three OU scalars are direct one-dimensional expectations; a concrete `alpha=12.75` Poincare--Miranda rectangle has strict face margins of order `10^-5` and a positive objective margin `>6.8e-3` on the tested rectangle.

This removes the named analytic obstruction and leaves only outward-rounded continuum enclosure, not a new conceptual comparison problem.

## 6. Failed / excluded routes preserved

I did not restart routes already shown inadequate in the R14/NM13-07 chain:

- the globally exhausted one-parameter 2013 partial lift;
- the MZZ linear weighted-second-moment lower route, whose local ceiling is below the LP lower endpoint;
- the `N^{-1/2}` sphere-net route with `Theta(N log N)` entropy;
- plain Gaussian-polytope facet first moment, numerically far too weak;
- smaller-radius / ball / projection-pursuit feasibility;
- replica/full-RSB values without a rigorous transfer.

NM13-12's radial-margin universality theorem is complementary but does not move the original Gaussian T03 bracket and is not duplicated here.

## 7. Essential executed artifacts

Checker source:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_alpha1275_kernel_miranda.py`

creation commit:

`519b44523861eef046ab35f30e01091c24f14edd`.

Archived actual output:

`proofnet24/NM13-03/progress-perceptron-theory/runs/2026-09-20/artifacts/t03_alpha1275_kernel_miranda.out`

creation commit:

`abc2e6a2de8e07001684997e08aef6b339a37d55`.

The output ends `ALL_CHECKS_PASS`. Its `CANDIDATE_ALPHA_U` line is deliberately named candidate rather than certified endpoint.

## 8. Next attack

Do not invent another variational ansatz. The next T03 theory step is now finite and precise: implement directed interval/Taylor evaluation of the closed formulas for `f,f_B,f_mu` on the four rectangle faces, with a mesh-to-continuum derivative bound, and enclose `Psi>0` on the resulting root box. If that passes, `alpha_U=12.75` becomes a genuine rigorous bracket movement immediately through the already-proved stationary reconstruction.

No peer file, root ledger, schedule, permission, public resource, email, or Drive object was modified.

```yaml
ledger_delta:
  worker: NM13-03
  parent: T03
  target: "negative spherical Gaussian perceptron, kappa=-1, exact radius sqrt(N)"
  status: "PARTIAL / NEW CLOSED-KERNEL THEOREM / CANDIDATE_FULL threshold endpoint"
  source_metric: "rigorous threshold bracket width alpha_U-alpha_L"
  certified_before:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
  certified_after:
    alpha_L: "6.30297437506"
    alpha_U: "12.78437096216"
    width: "6.48139658710"
    movement: "none; continuum finite enclosure still missing"
  candidate_after_review:
    alpha_L: "6.30297437506"
    alpha_U: "12.75"
    width: "6.44702562494"
    strict_upper_improvement: "0.03437096216"
  mechanism_gain:
    theorem: "NM03-T03-KERNEL"
    application: "closed 1D Gaussian evaluation + explicit Miranda rectangle at alpha=12.75"
    center_Psi: "0.015200993467166857"
    tested_rectangle_Psi_min: "0.006898540392867247"
  named_obstruction_removed: "nested Gaussian/AD burden in NM13-07 second-full root certification"
  remaining_obligation: "directed continuum enclosure of face signs and Psi positivity; no new conceptual variational step"
  coordination:
    NM13-07: "consume exact two-scalar reconstruction; complementary kernel/certification route only"
    NM13-12: "radial universality acknowledged but not used as Gaussian source closure"
  runtime:
    model: "GPT-5.6 Sol"
    reasoning: "UNVERIFIED"
```
