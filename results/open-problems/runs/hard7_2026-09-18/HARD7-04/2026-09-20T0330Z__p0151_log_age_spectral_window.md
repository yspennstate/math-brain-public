Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** **No movement** on the frozen source metric: `gamma_E >= b5 -> gamma_E >= b5`; methods actually tried: **B18 / B7 / B5**. New auxiliary result: the exact critical Pólya-point-tree mean operator, killed to an age interval of logarithmic length `L`, has Perron deficit `C_spec/L^2+O(L^-3)` with explicit `C_spec`, and its near-critical spectral crossing is therefore on the `L^-2` scale.

# HARD7-04 bounded research iteration — centered log-age spine and an exact killed-PPT spectral window

Status: **PARTIAL / SOURCE OPEN**. This run deliberately leaves the preceding bridge-amplification family and changes mechanism. It proves an exact operator-level theorem for the local-limit branching object and identifies the `L^-2` finite-log-age spectral scale with an explicit constant. It does **not** transfer that theorem to the finite sequential fixed-outdegree preferential-attachment graph, so it does not identify the source critical window or move the frozen finite-graph exponent `gamma_E`.

The complete analytic proof is archived at

`artifacts/hard7_2026-09-18/HARD7-04/p0151_log_age_killed_ppt_spectral_window_20260920T0330Z.md`

created at commit `39a25f150e33f9eb26b18cd7fa0ad969190f3b8b` and read back at that exact SHA.

---

## 1. Continuity, ownership, and evidence consumed

I resumed the exclusive canonical claim

`operations/claims/P0151.md`

owned by `HARD7-04`. I did not restart I0049, P0157, the configuration-model MST route, or an independently attached-edge growing-graph theorem.

Before the new mathematics I reread the required control and campaign surfaces:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/P0151.md` and the P0151 intake/catalog traces;
- the current neighboring preferential-attachment history, especially `runs/R08/20260917T223457Z_rotation_preferential_attachment_status_5d8c41.md` and its I0048 follow-up;
- the complete current HARD7-04 P0151 chain through the immediately preceding report
  `runs/hard7_2026-09-18/HARD7-04/2026-09-20T0230Z__p0151_full_attractiveness_bridge.md`.

A fresh repository search immediately before this report still showed that `P0151` is owned by HARD7-04 and that the 02:30 full-attractiveness report is the newest substantive predecessor. No peer claim collision was found.

The posting registry contains no source-equivalent P0151 paper.

### Fresh literature check, 20 September 2026

I reran source/current-literature queries for the exact fixed-outdegree critical-window scope.

1. Rajat Subhra Hazra, Remco van der Hofstad, and Rounak Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026), still gives the exact threshold for the fixed-outdegree affine PA model and identifies it through the Pólya-point-tree mean-offspring spectral radius. Its current abstract does not state a finite-size critical-window theorem for this sequential fixed-`m` model.
2. Joost Jorritsma, Pascal Maillard, and Peter Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937, submitted 22 December 2025, proves a `(log n)^(-2)` window and `sqrt(n)/log n` critical components for growing graphs in which a new vertex connects **independently** to each earlier vertex with a prescribed probability. Its proof uses branching random walks killed outside an interval of length `log n`. This remains a neighboring result, not a theorem for the exact sequential fixed-outdegree model here.
3. Peter Mörters and Lucas Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844, submitted 26 June 2026, treats an inhomogeneous PA-kernel graph with `tau in (2,3)` and a moving threshold `p_n`; it is a different ensemble and regime.

No source-matching finite fixed-outdegree critical-window theorem surfaced in this bounded refresh. This is bounded negative evidence, not a worldwide novelty certificate.

---

## 2. Frozen model and source metric

The model is unchanged. Fix integer `m>=2` and `delta>0`, and Ray/Hazra--van der Hofstad--Ray model (d): every arriving vertex contributes exactly `m` sequential edges, targets old vertices proportionally to current degree plus `delta`, intermediate updates are included, self-loops of the new vertex are excluded, and the completed graph undergoes independent bond retention with probability `pi`.

Put

`a:=m+delta`, `A:=2m+delta`.

The exact positive threshold is

`pi_c
 = delta/[2(m a+sqrt(m(m-1)a(a+1)))]`.

The frozen admitted metric remains

`gamma_E
 := liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

The immediately preceding run proved

`gamma_E >= b5`,

where

`b2=[m+a m pi_c]/A`,
`b5=b2+m(m-1)pi_c^2 a/A`,

and `b5<1/2` for every `m>=2`, `delta>0`.

**Before:** `gamma_E>=b5`.

**After:** `gamma_E>=b5`.

So the frozen source metric has **no movement in this run**. This is the first unchanged run after a sequence of strict movements `b1->b2->b3->b4->b5`, and therefore does not yet trigger Section I.

---

## 3. Why the route changed

The 02:30 report ended with a specific warning: another finite collection of local bridge events was no longer the right mechanism. The remaining exponent gap was

`1/2-b5>0`,

while Ray's exact extended mean-offspring eigenfunction has age dependence `x^-1/2`. That is too structured to ignore.

The new run therefore asked a different question:

> What does the **critical Pólya-point-tree mean operator itself** become after gauging by its exact positive eigenfunction and changing from age `x` to log-age `u=-log x`?

The answer is unexpectedly rigid: it becomes a centered two-state Markov additive process with exponential jumps. Killing this process on a log-age interval of length `L` can then be solved by a constant-coefficient `2x2` ODE. The first eigenvalue loss is exactly quadratic, of order `L^-2`.

This gives a concrete local-limit mechanism for the same `(log n)^-2` scale appearing in the independent-edge growing-graph theorem, without pretending that the finite fixed-outdegree transfer has already been proved.

---

# 4. B18 — say it in another language: exact centered Markov-additive form

Let

`chi=(m+delta)/(2m+delta)`,
`alpha=chi-1/2=delta/[2(2m+delta)]`.

Ray's two-type mean-offspring constants are

`c:=c_OO=c_YY=m(m+delta)/(2m+delta)`,
`d:=c_OY=m(m+1+delta)/(2m+delta)`,
`e:=c_YO=(m-1)(m+delta)/(2m+delta)`.

Put

`g:=sqrt(de)`, `lambda0:=c+g`.

The `2x2` matrix `[[c,d],[e,c]]` has right Perron vector

`pvec=(sqrt(d),sqrt(e))`

and Perron eigenvalue `lambda0`. On Ray's **extended** age space `x in (0,infinity)`, the function

`h_s(x)=pvec_s x^-1/2`

satisfies exactly

`Tbar h=(lambda0/alpha)h`.

Since

`pi_c=alpha/lambda0`,

`pi_c Tbar h=h`.

Now set `u=-log x`. The Doob transform by `h` has the following exact transition law:

- if the next type is `O`, the log-age jump is positive and has magnitude `Exp(alpha)`;
- if the next type is `Y`, the jump is negative and has magnitude `Exp(alpha)`;
- the type transition matrix is

`Q=[[q,p],[p,q]]`,

where

`q=c/lambda0`, `p=g/lambda0`, `q+p=1`.

Thus the type chain is symmetric. Its stationary law is `(1/2,1/2)`, so the stationary log-age drift is exactly zero.

Writing

`rho:=q-p=(c-g)/(c+g)`,

the sign correlation is `rho^k`. If `X_k` denotes one stationary log-age increment, then

`E X_k=0`

and the asymptotic variance is

`sigma^2
 = 2/[alpha^2(1-rho)]
 = lambda0/(alpha^2 g)`.                                          (4.1)

This is a genuine change of category: the critical two-type branching mean kernel becomes, after its exact harmonic gauge, a **centered Markov additive walk in logarithmic age**.

A Fourier check is also exact. The transformed Fourier matrix is

`Khat(xi)
 = Q diag(alpha/(alpha-i xi), alpha/(alpha+i xi))`.

Its top eigenvalue has expansion

`lambda_+(xi)
 =1-(sigma^2/2)xi^2+O(xi^4)`.                                    (4.2)

There is no linear term because the transformed walk is centered.

**Outcome of B18:** succeeded at the local-limit operator level. It identifies the exact hidden centered walk and its diffusion coefficient, but does not itself couple the finite fixed-outdegree graph to that walk.

---

# 5. B7 — take the limit object seriously: solve the killed log-age interval

Restrict both parent and child ages to

`e^-L <= x,y <= 1`.

In log-age this is the finite interval

`0<=u,v<=L`.

Because the harmonic transform is an invertible similarity on this compact interval, the spectral radius of

`R_L:=pi_c T_L`

is exactly the Perron root of the centered Markov-additive kernel killed when it exits `[0,L]`.

For a positive eigenfunction `f=(f_O,f_Y)` with eigenvalue `z`, define

`A_0(u)=int_u^L alpha e^-alpha(v-u) f_O(v)dv`,
`B_0(u)=int_0^u alpha e^-alpha(u-v) f_Y(v)dv`.

Then

`z f_O=q A_0+p B_0`,
`z f_Y=p A_0+q B_0`.

Differentiating gives the constant-coefficient system

`d/du [A_0;B_0]
 = alpha [[(z-q)/z,-p/z],[p/z,(q-z)/z]] [A_0;B_0]`,              (5.1)

with boundary conditions

`B_0(0)=0`, `A_0(L)=0`.

The square of the matrix in (5.1) is `-omega^2 I`, where

`omega^2
 = alpha^2(1-z)(z-rho)/z^2`.                                    (5.2)

Solving the ODE and imposing `A_0(L)=0` gives the exact principal-mode equation

`cos(omega L)
 + [alpha(z-q)/(z omega)] sin(omega L)=0`.                         (5.3)

For the positive first mode,

`omega L in (pi_math/2,pi_math)`.

The corresponding functions are explicitly positive; after using (5.3),

`A_0(u)
 = A_0(0) sin(omega L-omega u)/sin(omega L)>0`,

and `B_0(u)>0` for `0<u<=L`. The positive finite-interval kernel is Hilbert--Schmidt and irreducible after two steps, so this positive mode is its Perron mode.

Equation (5.3) forces

`omega=pi_math/L+O(L^-2)`.

Using (5.2),

`z_L:=r(R_L)
 = 1-C_spec/L^2+O(L^-3)`,                                        (5.4)

with the explicit coefficient

`C_spec
 := pi_math^2/[alpha^2(1-rho)]
 = (pi_math^2/2)sigma^2`.                                         (5.5)

The full algebra, positivity argument, and expansion are written out in the matching artifact rather than left as a sketch.

**Outcome of B7:** succeeded for the exact killed local-limit mean operator. The previously qualitative “spectral eigenfunction might explain the missing half exponent” has become a quantitative theorem: the first finite-log-age spectral loss is `C_spec/L^2+O(L^-3)`.

---

# 6. B5 — add the near-critical parameter and locate the operator crossing

Now deform the percolation parameter on the killed operator by

`pi_L(lambda)
 :=pi_c(1+lambda/L^2)`

for fixed real `lambda`.

Percolation scales the mean operator linearly, hence from (5.4)

`r(pi_L(lambda)T_L)
 = (pi_L(lambda)/pi_c) z_L`

`=1+[lambda-C_spec]/L^2+O(L^-3)`.                                 (6.1)

Therefore the finite-log-age **mean-operator** crossing occurs at the explicit relative shift

`lambda=C_spec`.                                                    (6.2)

If one inserts the finite-graph age cutoff `L=log n`, this is precisely a `(log n)^-2` operator scale.

This matches the *scale* of the neighboring Jorritsma--Maillard--Mörters theorem, whose proof also uses a branching random walk killed on a length-`log n` interval, but the models are different. Equation (6.1) is not a license to import their finite-graph theorem.

**Outcome of B5:** succeeded at the killed-PPT spectral level and produced an explicit local crossing constant. The finite fixed-outdegree graph transfer remains unpaid.

---

## 7. Counterexample-oriented stress test: what this mechanism does **not** prove

The most dangerous false inference would be:

> “The local mean operator crosses on `(log n)^-2`, therefore the fixed-outdegree finite graph has already been proved to have a `(log n)^-2` critical window.”

That implication is invalid.

The independent-edge theorem can run a killed branching-random-walk exploration because, conditional on the explored history, connections from a new vertex to old vertices are independently generated in its model. Here every new vertex has exactly `m` sequential attachment edges, with intermediate degree updates. The local weak limit forgets enough finite-population dependence that an operator theorem alone cannot control collisions, depletion, and within-birth dependence at the source component scale.

The exact missing theorem is now substantially sharper than “transfer the eigenfunction somehow”:

> **Finite-graph spectral/exploration transfer obligation.** Couple the fixed-outdegree sequential component exploration, uniformly for ages in `[n^-1,1]` and retention `pi=pi_c(1+O((log n)^-2))`, to the killed two-state log-age Markov-additive process strongly enough that the accumulated operator/exploration error is `o((log n)^-2)` at the relevant survival scale, or prove a direct finite-population substitute with the same principal eigenvalue expansion.

A merely `o(1)` local-weak convergence estimate is far too weak for this purpose.

This stress test is why the source metric remains unchanged despite the exact operator calculation.

---

## 8. Before/after and auxiliary delta

### Frozen source metric

Before:

`gamma_E>=b5`.

After:

`gamma_E>=b5`.

**No movement.** Source status remains **OPEN / PARTIAL**.

### New auxiliary quantitative result

Before this run, the P0151 record had Ray's infinite-age spectral radius and HARD7-04's bridge lower exponents, but no proved finite-log-age principal-eigenvalue asymptotic for the exact two-type kernel.

After this run, for the exact critical PPT mean operator killed to log-age length `L`,

`1-r(pi_c T_L)
 = C_spec/L^2+O(L^-3)`,

with

`C_spec=pi_math^2/[alpha^2(1-rho)]`,
`alpha=delta/[2(2m+delta)]`,
`rho=(c-g)/(c+g)`,
`c=m(m+delta)/(2m+delta)`,
`g=sqrt(m(m-1)(m+delta)(m+1+delta))/(2m+delta)`.

The associated local near-critical spectral crossing is

`pi=pi_c[1+C_spec/L^2+o(L^-2)]`.

This is **auxiliary movement**, not movement of the frozen finite-graph source metric.

---

## 9. Actual validation performed

- Re-read the exact P0151 claim, current campaign exclusions, newest own report, and neighboring PA status before research.
- Reran dated literature queries against the exact fixed-outdegree wording and the newest critical-window papers.
- Re-derived the `2x2` Perron vector and threshold identity from the source kernel constants.
- Checked the Doob transform algebra in both jump directions, including the Jacobian `dy=e^-v dv`.
- Derived the transformed type matrix exactly and verified it is symmetric.
- Derived the asymptotic variance both from sign correlations and independently from the Fourier characteristic polynomial.
- Solved the killed eigenproblem by converting the two integral equations into the constant-coefficient ODE (5.1), imposed both boundary conditions, and checked positivity of the first mode explicitly.
- No finite simulation or sampled random graph is used as proof.
- No checker was manufactured because the substantive new claim is analytic, not a finite exhaustive assertion. The complete derivation is in the matching artifact.

---

## 10. Remaining full-scope gap and next route

The source problem is still open. The missing obligations are:

1. prove the sharp finite-graph exploration transfer described in Section 7 despite fixed-outdegree and within-birth dependence;
2. from that transfer, prove both sides of the actual critical window, not only a mean-operator crossing;
3. obtain the finite-graph critical component scale and tightness/joint scaling law;
4. reconcile the local spectral constant with collision/depletion corrections rather than assuming the independent-edge constant survives unchanged.

Because the source metric moved in each of the four immediately preceding P0151 runs and is unchanged only now, Section I is **not** triggered. The next run should not return to B18/B7/B5 unchanged. A useful next triple would attack the finite-population coupling itself, for example B2 (try to break a candidate coupling on two edges of one birth), B19 (make the exploration transfer algorithm explicit), and B30 (localize the error by log-age slab).

---

## 11. Runtime and scheduler capability honesty

The prompt requests GPT-6 with maximum reasoning. The actual model exposed to this run is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The available scheduler surface still exposes task title/identity, prompt, timing/schedule, and enabled state, but no bindable model selector, no bindable reasoning-effort selector, and no guaranteed execution-duration field. Thus GPT-6/maximum remains a prompt request only. Making it binding requires a scheduler/product/API surface that actually exposes model-family and effort fields and routes execution through them, ideally with authenticated runtime attestation.

The repository records that earlier `You cannot modify this task` failures for P26/P01/P03 were authorization-context boundaries; P26 was later updated from an authorized context. For any task that still returns that denial, the compliant route is its owning/authorized account or workspace, an exposed ownership/admin transfer path, or platform support — not a duplicate scheduler job, repository metadata edit, or permission bypass.

This run made **no scheduler changes**, did not re-enable or disable anything, and used no email, Drive, public posting, workflow, permission change, or force push.

### `ledger_delta`

`HARD7-04 | P0151 fixed-outdegree PA critical regime | gamma_E lower bound | b5 -> b5 (NO MOVEMENT) | PARTIAL / SOURCE OPEN | auxiliary: killed-PPT spectral deficit C_spec/L^2+O(L^-3), explicit C_spec; finite-graph transfer unpaid | methods B18/B7/B5`