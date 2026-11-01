Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO SOURCE-METRIC MOVEMENT: I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; admission metric `E_ready: 0 -> 0`. Methods #2 ATTACK THE NEGATION FIRST, #6 DEFORM TO A POINT YOU CAN SOLVE, #12 FIND WHAT IS CONSERVED.**

# R15 CLOSABLE OUTSIDE — exact two-level reduction for the retained Talagrand successor screen

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

All mathematical statements newly derived below are **SELF_CHECK_ONLY** unless explicitly identified as standard/prior art. No closure, novelty certificate, or independent audit is claimed.

## 1. Continuity and exact source discipline

I continued from the newest R15 report

`runs/R15/20260918_1208Z_successor_admission_f0111_orbit_compact_z57f.md`

created at commit `0dce5ed4f2398fc8752c06b414195d0a587d1c16`. I also reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operative follow-up implementation manifest, the newest coordinator/task-health report, the controlling I0076 six-run handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`,

and the neighboring current Burdzy--Scheutzow I0077 work owned by R07. I used the durable successor-admission cursor reports now covering I0060--I0079 rather than restarting that bookkeeping from rank one.

I reread the primary Burdzy--Scheutzow PDF, including Definition 2.1 and Problem 7.2. The source definitions remain exactly:

- `X` is FBM if there are random times `S_n -> -infinity` a.s. such that each complete future increment process `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is BBM if the reversed process is FBM;
- `X` is 2BM if there exists a random time `S` such that the two complete centered half-paths `(X_{S+t}-X_S)_{t>=0}` and `(X_{S-t}-X_S)_{t>=0}` are independent standard Brownian motions.

Problem 7.2 assumes only FBM + BBM and existence of an arbitrary random time `T` at which those two complete centered half-paths are independent, and asks whether this forces 2BM. It does **not** assume that `T` is a stopping time and does **not** separately assume that either seam half is Brownian.

The primary source also explicitly distinguishes this from Proposition 6.2, whose negative result rules out a seam having independence **plus** a Brownian forward half for one constructed FBM. That stronger seam obstruction does not decide Problem 7.2.

Fresh dated exact-title / exact-problem searches on 2026-09-18 recovered the original publication and source PDF but no accessible later primary paper explicitly claiming to settle exact Problem 7.2. This is bounded negative search evidence only, not a worldwide openness certificate.

The six-run handoff therefore remains controlling. The Theorem-6.1-derived candidate was eliminated because it has no source-required independent real seam. The alternating Brownian-prefix/Bessel candidate did achieve FBM, BBM and exact seam independence but was then proved to be 2BM, so it was eliminated. There is currently **no surviving frozen counterexample candidate**. The copied continuous Brownian-cell construction is only a handoff architecture, not an object on which another one of the four source obligations may be counted.

Accordingly the historical I0076 metric stays `2/4`; its six-run retirement count stays frozen at `6`. I do not reopen it, replace the random seam by a deterministic seam, add a stopping-time assumption, use numerical path samples as law verification, or substitute Problem 7.5.

The active operational metric for this rotated slot remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors lawfully available to R15 in this bounded run`.

Before: `0`. After: `0`.

The durable admission screens now cover I0060--I0079 and find no lawful free CLOSABLE successor there. In particular I0076 remains a retired handoff, while distinct I0077 is owned elsewhere. I therefore create no new ownership claim this run.

With no lawful fresh assignment, I continue the already-retained Talagrand Problem 10.9 work only as **successor-screening mathematics**, without claiming the source.

## 2. Retained screen: Talagrand Problem 10.9 and the exact n=3,k=2 homogeneous slice

Source: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9.

For an up-class `A` and hazard vector `t>=0`,

`F_A(t)=-log(1-zeta_t(A))`,

where independent coordinate `i` is present with probability `1-exp(-t_i)`. Talagrand's class `C_gamma` asks, at each base point `q`, for a polynomial with nonnegative coefficients and no constant term that majorizes `F_A` pointwise and has the required small budget at `gamma q`. Problem 10.9 asks whether one universal `gamma>0` works for every cardinality threshold `A={|X|>=k}`.

Fresh searches on 2026-09-18 recovered Talagrand's source and related later threshold papers (including DeMarco--Kahn and later Kahn/Kalai-threshold literature) but did not expose an accessible theorem explicitly resolving this exact positive-multilinear-majorant Problem 10.9. Again this is bounded negative evidence only.

The preceding R15 run reduced any homogeneous strict weak-dual refutation to at most `n+1` permutation orbits. I now attack the smallest non-endpoint threshold directly:

`n=3, k=2, q=c(1,1,1), c>0`.

For `t=(t_1,t_2,t_3)`, put

`S(t)=e^{t_1}+e^{t_2}+e^{t_3}-2`,

so

`F(t)=F_{3,2}(t)=t_1+t_2+t_3-log S(t)`.

The new object is a two-degree symmetric tangent candidate

`P_c(t)=alpha_c e_1(t)+beta_c e_2(t)`.

This run does **not** yet prove `F<=P_c` globally. What it does prove is that the candidate has the exact budget and tangent conditions, is globally correct on the full homogeneous ray, and that any failure anywhere in the positive octant is forced onto one explicit two-level wedge. This replaces a three-dimensional continuum search by a one-parameter minimization nested inside one remaining scalar parameter.

## 3. Method #12 — FIND WHAT IS CONSERVED: the unique degree-1/2 tangent budget

Define

`f(r)=F(r,r,r)=3r-log(3e^r-2)`

and

`h(r)=f'(r)/3=2(e^r-1)/(3e^r-2)`.

For fixed `c>0`, set

`A_c = f(c)/(3c) = (1/c) int_0^c h(r) dr`,

`alpha_c = 2A_c-h(c)`,

`beta_c = (h(c)-A_c)/c`.

Then

`P_c(c,c,c)=f(c)`

and, for every coordinate `i`,

`partial_i P_c(c,c,c)=partial_i F(c,c,c)=h(c)`.

Indeed

`alpha_c+beta_c c=A_c`,

so `P_c(c1)=3cA_c=f(c)`, while

`alpha_c+2beta_c c=h(c)`.

Thus the two coefficients are exactly the solution of the two conserved requirements: **budget equality at the base point and first-order tangency there**.

The coefficients are strictly positive. We have

`h(0)=0`,

`h'(r)=2e^r/(3e^r-2)^2 >0`,

`h''(r)=-2e^r(3e^r+2)/(3e^r-2)^3 <0`.

Hence `h` is strictly increasing and strictly concave. Concavity with `h(0)=0` gives

`A_c > h(c)/2`,

so `alpha_c>0`, while `A_c<h(c)` gives `beta_c>0`.

A useful exact integral identity is

`beta_c=(1/c^2) int_0^c r h'(r) dr`.

Since `h'` is strictly decreasing and `h'(0)=2`,

`h'(c)/2 < beta_c < 1`.                                      (3.1)

The second conserved quantity that appears below is the common exponential secant slope at any stationary point. Writing

`D_c(t)=P_c(t)-F(t)=log S(t)-(1-alpha_c)e_1(t)+beta_c e_2(t)`,

the stationarity equations imply, whenever `t_i != t_j`,

`(e^{t_i}-e^{t_j})/(t_i-t_j)=beta_c S(t)`.                    (3.2)

Thus every unequal coordinate pair at one stationary point would have to share the **same secant slope of the exponential**.

## 4. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: full homogeneous ray is proved

### Theorem R15-F0111-DIAG

For every `c>0` and every `r>=0`,

`F(r,r,r) <= P_c(r,r,r)`,

with equality at `r=0` and `r=c`.

### Proof

Set

`Delta_c(r)=P_c(r,r,r)-f(r)=3alpha_c r+3beta_c r^2-f(r)`.

Then

`Delta_c'(r)/3 = L_c(r):=alpha_c+2beta_c r-h(r)`.              (4.1)

We have

`L_c(0)=alpha_c>0`,

`L_c(c)=0`.

Moreover

`L_c'(r)=2beta_c-h'(r)`.

By (3.1), `2beta_c<h'(0)` but `2beta_c>h'(c)`. Since `h'` is strictly decreasing, there is a unique `rho_c in (0,c)` at which `L_c'` vanishes. Therefore `L_c` decreases on `[0,rho_c]` and increases on `[rho_c,infinity)`. Since `L_c(c)=0` and `rho_c<c`, its minimum is strictly negative. Hence there is a unique first zero `r_0 in (0,rho_c)`, followed by the zero `c`, with sign pattern

`L_c>0` on `[0,r_0)`,

`L_c<0` on `(r_0,c)`,

`L_c>0` on `(c,infinity)`.

Because `Delta_c(0)=Delta_c(c)=0`, equation (4.1) says that `Delta_c` first rises from zero, then decreases monotonically to zero at `c`, and then rises again. Thus `Delta_c(r)>=0` for all `r>=0`. QED.

This is a genuine analytic result, not a grid or simulation. It also proves that a global failure of the tangent candidate cannot occur on the homogeneous ray.

## 5. Method #2 — ATTACK THE NEGATION: classify every possible negative minimizer

Assume for contradiction-search purposes that the candidate majorant fails somewhere:

`D_c(t)<0` for some `t>=0`.

Because `alpha_c,beta_c>0` and `F(t)` grows at most linearly while the `beta_c e_2` term controls directions with two growing coordinates, whereas the `alpha_c e_1` term controls one-coordinate escape, `D_c` is coercive on the positive octant. Therefore a negative global minimum exists.

I now prove that, up to permutation, every such negative minimum must lie in the single two-level wedge

`(y,y,x),  y>x>=0`.                                              (5.1)

### 5.1 Interior stationary points have at most two coordinate values

At an interior stationary point,

`partial_i D_c = e^{t_i}/S -(1-alpha_c)+beta_c sum_{j!=i}t_j =0`.

Subtracting the equations for `i` and `j` gives (3.2). If three coordinates were distinct, say `x<y<z`, strict convexity of `e^u` gives

`(e^y-e^x)/(y-x) < (e^z-e^y)/(z-y)`,

contradicting the fact that both must equal `beta_c S`. Hence an interior stationary point has either one coordinate value or exactly two.

The one-value case is on the homogeneous ray and therefore cannot be a negative minimum by Theorem R15-F0111-DIAG.

### 5.2 The repeated value cannot be the smaller value at a local minimum

Suppose an interior stationary point is `(x,x,y)` with `0<x<y`. Let

`v=(1,-1,0)`.

For `r_i=e^{t_i}/S`, the Hessian of `log S` is `diag(r)-rr^T`; the Hessian of `beta_c e_2` has zero diagonal and all off-diagonal entries `beta_c`. At `(x,x,y)`,

`v^T nabla^2 D_c v = 2(e^x/S-beta_c)`.

But the stationarity secant identity gives

`beta_c=(e^y-e^x)/(S(y-x)) > e^x/S`

by strict convexity of the exponential. Therefore

`v^T nabla^2 D_c v<0`.

So `(x,x,y)` with the repeated value smaller cannot be a local minimum.

Consequently every negative interior minimum, if one exists, is permutation-equivalent to

`(y,y,x)` with `y>x>0`.

### 5.3 Boundary faces reduce exactly to the same two-level wedge

It remains to rule out an arbitrary asymmetric face point as a genuinely new failure mechanism. By symmetry it suffices to take `t=(a,b,0)`. Write

`a=m+d`, `b=m-d`, `m>=0`, `0<=d<=m`.

Then

`D_c(m+d,m-d,0)
 = log(2e^m cosh d-1)-2(1-alpha_c)m+beta_c(m^2-d^2)`.            (5.2)

For `d>0`, define

`q_m(d)= e^m sinh d / [d(2e^m cosh d-1)]`.

Differentiating (5.2) gives

`partial_d D_c = 2d(q_m(d)-beta_c)`.                              (5.3)

The key exact fact is that `q_m` is strictly decreasing. Indeed, with `A=e^m`,

`q_m'(d)/q_m(d)
 = coth d - 1/d - 2A sinh d/(2A cosh d-1)`

`= (2A-cosh d)/[sinh d(2A cosh d-1)] - 1/d`.

The right side is negative because

`sinh d(2A cosh d-1)-d(2A-cosh d)`

`=2A(sinh d cosh d-d)+(d cosh d-sinh d)>0`                       (5.4)

for every `d>0`; both bracketed terms are strictly positive.

Thus, for fixed `m`, equation (5.3) can change sign at most once, and if it changes sign it changes from positive to negative. Therefore the minimum over the whole interval `0<=d<=m` is attained at an endpoint.

The endpoint `d=m` is an axis point `(2m,0,0)`, where

`F(2m,0,0)=0`,

`D_c(2m,0,0)=2alpha_c m>=0`.

Hence any negative boundary-face minimum must occur at `d=0`, i.e. at

`(m,m,0)`.

This is exactly the boundary `x=0` of the same two-level wedge (5.1).

### Conclusion of the negation attack

A global failure of `F<=P_c`, if one exists at all, has a negative minimizer which, after permutation, is

`(y,y,x),  y>x>=0`.                                              (5.5)

There is no other interior or boundary geometry to inspect.

## 6. Exact one-dimensional minimization inside each two-level fiber

The remaining wedge has one more exact simplification. Put

`G_c(y,x)=D_c(y,y,x)`

for `y>0` and `0<=x<=y`. Then

`G_c(y,x)
 = log(2e^y+e^x-2)
   -(1-alpha_c)(2y+x)
   +beta_c(y^2+2xy)`.                                           (6.1)

For fixed `y>0`,

`partial_x^2 G_c
 = e^x(2e^y-2)/(2e^y+e^x-2)^2 >0`.                              (6.2)

So `G_c(y,.)` is strictly convex and has a unique minimizer on `[0,y]`. Let

`C_c(y)=1-alpha_c-2beta_c y`,

`r_0(y)=1/(2e^y-1)`,

`r_1(y)=e^y/(3e^y-2)`.

Since

`partial_x G_c = e^x/(2e^y+e^x-2)-C_c(y)`,                      (6.3)

and the first term is strictly increasing in `x`, the exact minimizing coordinate is

- `x_*(y)=0` if `C_c(y)<=r_0(y)`;
- `x_*(y)=y` if `C_c(y)>=r_1(y)`;
- otherwise

`x_*(y)=log( 2 C_c(y)(e^y-1)/(1-C_c(y)) )`.                     (6.4)

At the tangent point `y=c`,

`C_c(c)=1-h(c)=e^c/(3e^c-2)=r_1(c)`,

so the formula joins continuously to `x_*(c)=c`.

Therefore the full three-dimensional candidate-majorant question is now equivalent to one scalar lower-envelope inequality:

`M_c(y):=G_c(y,x_*(y)) >=0 for every y>0`.                       (6.5)

The diagonal branch `x_*=y` is already proved nonnegative by Theorem R15-F0111-DIAG. The only unresolved pieces are the equal-pair face branch `x_*=0` and the explicit interior branch (6.4).

This is the main movement of the run: **a potential three-variable counterexample has been reduced exactly, with no numerical assumption, to a single scalar function with an explicit piecewise formula.**

I do not claim (6.5) yet. A proof of it would establish the global tangent majorant `F<=P_c` for every `c>0`, and consequently the homogeneous `n=3,k=2` slice would satisfy the `C_1` budget at its base point. That would still be only a restricted slice of Talagrand Problem 10.9, not a solution of the full heterogeneous-`q`, all-`n,k` source problem.

## 7. Why this route is materially different from the exhausted ones

The earlier R15/R20 routes attacked the weak dual, tropical asymptotics, Schur symmetry, FKG envelopes, one-atom witnesses, disjoint-support tensorization, and finite-orbit compactification. This run instead constructs a **primal tangent envelope** and proves an exact geometric classification of every possible failure.

The two source-scale invariants are:

1. exact budget + gradient matching at the homogeneous base, which uniquely fixes `alpha_c,beta_c`;
2. equality of exponential secant slopes at every stationary point, which forces at most two coordinate levels.

The deformation is also exact rather than perturbative: the full diagonal is solved, every face collapses to its equal-coordinate endpoint or an axis, and the remaining two-level cone is strictly convex in its lower coordinate.

No finite checker was created because the new claims are theorem-sized analytic statements with proofs on the page. Creating a ceremonial grid certificate would not validate (6.5) and would violate the 90/10 instruction.

## 8. Admission/current-state check

The newest durable successor-admission reports now cover I0060--I0079 and find zero lawful free CLOSABLE successor in that cursor. The distinct Burdzy--Scheutzow I0077 route is owned by R07 and currently active; R15 does not duplicate it. A separate fresh CLOSABLE KNSV target was claimed create-only by R20 before this run and likewise is not free inventory.

Thus the operational admission metric remains

`E_ready: 0 -> 0`.

No claim file, paper package, audit request, shared-root edit, email, Drive write, public post, purchase, permission change, workflow action, or scheduler change was made.

## 9. Model / scheduler / authorization boundary

The exposed scheduler controls still provide task identity, title/prompt, schedule/relative start, timing mode and enabled state. They expose **no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long runtime field**. Therefore GPT-6/maximum remains prompt text only from this surface; this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

The historical P26 task ID `6aa7b43682948191b697d72fec69d539` did at one point return `You cannot modify this task` from one authorization context. Current repository configuration records that another authorized context later succeeded in updating P26. The lawful workaround is therefore the owning/authorized/admin product context or platform support for the same task, not cloning it, changing permissions, or bypassing authorization.

## 10. Next research move

The next run should not rederive the two-level reduction. It should attack the remaining scalar envelope (6.5), beginning with the boundary branch

`G_c(y,0)=log(2e^y-1)-2(1-alpha_c)y+beta_c y^2`,

and then the interior branch obtained by substituting (6.4). Fresh Section-B methods proposed for that run: **#5 ADD A PARAMETER AND DIFFERENTIATE, #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT.**

## 11. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE_OUTSIDE
  assigned_source:
    id: I0076
    source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
  assigned_metric:
    name: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: "2/4 historical carried"
    after: "2/4 historical carried"
    movement: false
    status: OPEN_PARTIAL_RETIRED_HANDOFF
    unchanged_count: 6_frozen_at_retirement
    surviving_frozen_candidate: null
  admission_metric:
    name: E_ready
    before: 0
    after: 0
    definition: "newly verified source-clean current-open ownership-clear genuinely CLOSABLE OUTSIDE successors lawfully available to R15 in this bounded run"
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9"
    ownership_claim_created: false
    exact_slice: "n=3, k=2, homogeneous base q=c*1"
    new_result:
      - "unique positive degree-1/2 polynomial satisfying exact homogeneous budget and gradient tangency"
      - "global majorant proved on the full homogeneous ray"
      - "any negative global minimizer forced, up to permutation, to (y,y,x) with y>x>=0"
      - "every boundary-face failure reduces to the equal-pair face"
      - "for fixed y, remaining two-level objective is strictly convex in x with explicit minimizer x_*(y)"
      - "global candidate verification reduced exactly to scalar lower envelope M_c(y)>=0"
    status: SELF_CHECK_ONLY_PARTIAL
    remaining_obligation: "prove or refute M_c(y)>=0 on the equal-pair face and explicit interior branch; even success would remain a restricted Talagrand slice"
  methods_this_run: [2, 6, 12]
  method_outcomes:
    2: "negation attack classifies every possible failure as a two-level minimizer"
    6: "deformation to the homogeneous ray is solved globally and face asymmetry collapses to endpoints"
    12: "budget+tangency coefficients and stationary exponential secant slope are exact invariants"
  evidence:
    primary_source_rechecked: true
    current_literature_search_date: 2026-09-18
    latest_r15_checkpoint: 0dce5ed4f2398fc8752c06b414195d0a587d1c16
    admission_cursor_used: "I0060-I0079 durable peer screens"
  audit_ids: []
  new_checker: null
  new_artifact: null
  new_claim: null
  shared_root_edits: none
  peer_edits: none
  scheduler_changes: none
  scheduler_model_selector: null
  scheduler_reasoning_selector: null
  authenticated_runtime_model_telemetry: false
  guaranteed_duration_control: false
```
