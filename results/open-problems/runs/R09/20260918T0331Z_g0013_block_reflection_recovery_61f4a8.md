Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT on active R09 successor G0013: `U_* = 1289727882057511/11918000000000000 = 0.10821680500566462... -> same`; supported G0013 unchanged count `4 -> 5`. Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B1 CHANGE THE CATEGORY, B6 DEFORM TO A POINT YOU CAN SOLVE, B11 DUALIZE.** GPT-6 / maximum was requested in prompt text, but this runtime identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry, so I do not claim GPT-6 or maximum reasoning.

# R09 CLOSABLE OUTSIDE — G0013 recovery: one-interface mixed-orientation graph copulas are strictly subextremal

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

## 1. Continuity, ownership, and controls

I did **not** reopen Pengfei Tang, Question 4.11. The periodic-tree clause remains retired from R09 at the frozen metric `UNBOUNDED_ABOVE` after its source-level refutation, independent audits and six-unchanged retirement threshold. The transitive-graph clause remains open but is not active in this slot. G0002 / Cerf 53.1 remains handed off at `Delta_8=UNMEASURED`.

The controlling exclusive R09 claim remains `operations/claims/G0013.md`: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034, Remark 3, asking whether the diagonal and antidiagonal maximize quadratic Wasserstein distance from independence among all copulas with uniform marginals. With `lambda=Unif[0,1]`, `nu=lambda tensor lambda`,
\[
M=\sup_{\pi\in\Pi(\lambda,\lambda)}W_2^2(\pi,\nu),
\qquad M\stackrel{?}=1/10.
\]
R09's fixed global metric remains
\[
U_*=\text{smallest rigorous source-valid global upper bound on }M.
\]

The newest complete own report before this run is
`runs/R09/20260918T0311Z_g0013_stuck1_graph_recovery_4c7e2a.md`.
It was the required STUCK1 thinking-only run and chose exactly one recovery action: prove the simplest unresolved one-interface mixed-orientation graph family. That run fixed the next methods as B1/B6/B11. I follow that instruction here rather than tuning the global scalar relaxation again.

At run start I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/TANG-2020-Q4.11.md`, `operations/claims/G0013.md`, the newest R09 report, the newest searchable neighboring R08/R10 reports, and the exact G0013 intake/attempt records including `probability_1000_intake_G_20260910/batches/patch_G0013_A002.py`. The large intake JSONL corpus is connector-large, so exact target/source searches were used rather than pretending that all roughly 780 rows were visibly rendered.

## 2. Current-literature and ownership check

A bounded fresh 18 September 2026 search again found Catalano--Lavenant arXiv:2510.06034 and Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1 (submitted 9 September 2026). Schrott still states the uniform monotone/antimonotone assertion as a conjecture and proves the Gaussian analogue instead. Searches combining the exact title/authors with `uniform copula`, `quadratic Wasserstein`, `farthest from independence`, `diagonal antidiagonal`, `1/10`, and the one-interface/block-reflection terminology found no later source-level resolution or prior exact treatment of the family below. This is bounded dated evidence, not a novelty certificate.

Repository search found no conflicting owner for G0013. Historical block-reversal/permutation experiments are preserved in the intake attempts; they did not contain the continuous coupling proved below.

## 3. Recovery target

For \(0\le c\le1\), define the measure-preserving involution
\[
g_c(s)=
\begin{cases}
s,&0\le s\le c,\\
1+c-s,&c<s\le1,
\end{cases}
\]
and the graph copula
\[
\pi_c=\operatorname{Law}(S,g_c(S)),\qquad S\sim\operatorname{Unif}[0,1].
\]

It has exactly one orientation interface: a diagonal segment on `[0,c]` and an antidiagonal segment on `[c,1]`. The endpoints are the two conjectured extremizers:
`c=0` is the full antidiagonal and `c=1` is the full diagonal.

The STUCK1 report identified this as the smallest unresolved sign-gluing laboratory.

## 4. Main theorem — the entire one-interface family is strictly subextremal

**Theorem (R09-G0013 one-interface block-reflection theorem).** For every \(c\in[0,1]\),
\[
W_2^2(\pi_c,\lambda^{\otimes2})\le \frac1{10}.
\]
For every interior parameter \(0<c<1\),
\[
W_2^2(\pi_c,\lambda^{\otimes2})<\frac1{10}.
\]

More explicitly, there is a deterministic transport from the independent square to \(\pi_c\) having the following cost.

If \(0\le c\le1/2\), put
\[
a=\sqrt{c/2}\in[0,1/2].
\]
Then
\[
W_2^2(\pi_c,\lambda^{\otimes2})
\le
\frac1{10}
-\frac{4a^2}{15}
\left(13a^3-5a^2-10a+5\right).
\tag{4.1}
\]
Since the cubic in parentheses is at least \(3/8\) on `[0,1/2]`,
\[
W_2^2(\pi_c,\lambda^{\otimes2})
\le \frac1{10}-\frac{c}{20}
\qquad (0\le c\le1/2).
\tag{4.2}
\]

If \(1/2\le c\le1\), put
\[
b=\sqrt{(1-c)/2}\in[0,1/2].
\]
Then
\[
W_2^2(\pi_c,\lambda^{\otimes2})
\le
\frac1{10}-\frac45 b^5
=
\frac1{10}
-\frac45\left(\frac{1-c}{2}\right)^{5/2}.
\tag{4.3}
\]

At `c=1/2` both constructions give the explicit cost
\[
\frac{3}{40}=0.075.
\]

This is a **PARTIAL subclass theorem**. It does not prove the full Catalano--Lavenant conjecture and does not move the global metric \(U_*\).

## 5. B1 — change category: from planar OT to a one-dimensional branch assignment

Let `(X,Y)` be uniform on the source square and introduce diagonal/antidiagonal coordinates
\[
Z=\frac{X+Y}{2},
\qquad
D=\frac{X-Y}{2}.
\]
The map `(x,y) -> (z,d)` has Jacobian factor `2`, so `(Z,D)` has density `2` on the diamond
\[
\mathcal D=\{(z,d):0\le z\le1,\ |d|\le m(z)\},
\qquad
m(z)=\min(z,1-z).
\]

The marginal density and CDF of \(Z\) are
\[
f_Z(z)=4m(z),
\]
and
\[
F(z)=
\begin{cases}
2z^2,&0\le z\le1/2,\\
1-2(1-z)^2,&1/2\le z\le1.
\end{cases}
\tag{5.1}
\]

Choose the unique `a=F^{-1}(c)` and split the source square into
\[
A=\{Z\le a\},\qquad B=\{Z>a\},
\]
so `P(A)=c`, `P(B)=1-c`.

On `A`, define
\[
S=F(Z).
\]
Then the unconditional pushforward of `A` by `S` is Lebesgue measure on `[0,c]`: for `0<=t<=c`,
\[
\mathbb P(S\le t,\ A)=t.
\]

On `B`, let \(H_B\) denote the conditional CDF of \(D\) given \(B\), and define
\[
S=c+(1-c)H_B(D).
\]
Then the unconditional pushforward of `B` by `S` is Lebesgue measure on `[c,1]`.

Consequently `S` is uniform on `[0,1]`, and
\[
T(X,Y)=(S,g_c(S))
\]
has exactly law \(\pi_c\). Thus `T` is an admissible deterministic transport from the independent square to the target graph copula.

The quadratic cost separates in `(Z,D)` coordinates. On `A`,
\[
|(X,Y)-(S,S)|^2
=
2\big((Z-S)^2+D^2\big).
\tag{5.2}
\]
On `B`, writing
\[
m_c=\frac{1+c}{2},
\qquad
D'=S-m_c,
\]
we have
\[
|(X,Y)-(S,1+c-S)|^2
=
2\big((Z-m_c)^2+(D-D')^2\big).
\tag{5.3}
\]

This is the useful category change: the lower branch is monotone transport in the diagonal statistic `Z`, while the upper branch is monotone transport in the antidiagonal statistic `D`.

## 6. B6 — deform from the solved endpoints and compute the cost exactly

### 6.1 Regime `0 <= c <= 1/2`

Here
\[
a=\sqrt{c/2},\qquad c=2a^2,\qquad 0\le a\le1/2.
\]

On `A={Z<=a}`, `m(Z)=Z` and `S=2Z^2`. Conditional on `Z=z`, the variable `D` is uniform on `[-z,z]`, hence
\[
\mathbb E[D^2\mid Z=z]=\frac{z^2}{3}.
\]
Therefore the lower-branch contribution is
\[
C_A
=
\int_0^a
2\left((z-2z^2)^2+\frac{z^2}{3}\right)4z\,dz.
\tag{6.1}
\]

For the upper branch, the unnormalized density of `D` on `B` is symmetric and, for `d>=0`,
\[
w_B(d)=
\begin{cases}
2(1-a-d),&0\le d\le a,\\
2(1-2d),&a\le d\le1/2.
\end{cases}
\tag{6.2}
\]

Because `B` is symmetric in `D`,
\[
D'=(1-c)\left(H_B(D)-\frac12\right)
\]
is odd. For `d>=0`,
\[
D'(d)=\int_0^d w_B(u)\,du
=
\begin{cases}
2(1-a)d-d^2,&0\le d\le a,\\
2d-2d^2-a^2,&a\le d\le1/2.
\end{cases}
\tag{6.3}
\]

The perpendicular upper-branch contribution is
\[
C_{B,\perp}
=
\int_a^{1/2}2(z-m_c)^2\,4z\,dz
+
\int_{1/2}^{1}2(z-m_c)^2\,4(1-z)\,dz,
\tag{6.4}
\]
while the along-branch contribution is
\[
C_{B,\parallel}
=
4\int_0^a(d-D'(d))^2\,2(1-a-d)\,dd
+
4\int_a^{1/2}(d-D'(d))^2\,2(1-2d)\,dd.
\tag{6.5}
\]

Exact integration gives
\[
C_A+C_{B,\perp}+C_{B,\parallel}
=
\frac1{10}
-\frac{4a^2}{15}
\left(13a^3-5a^2-10a+5\right).
\tag{6.6}
\]

It remains only to check the sign of
\[
P(a)=13a^3-5a^2-10a+5.
\]
On `[0,1/2]`,
\[
P'(a)=39a^2-10a-10
\le \frac{19}{2}a-10
\le -\frac{21}{4}<0,
\]
where `39a^2 <= (39/2)a` was used. Hence `P` decreases on this interval, and
\[
P(a)\ge P(1/2)=\frac38.
\]
This proves (4.1), strictness for `c>0`, and the simpler deficit (4.2).

### 6.2 Regime `1/2 <= c <= 1`

Write
\[
a=1-b,
\qquad
b=\sqrt{(1-c)/2},
\qquad
c=1-2b^2.
\]
Now `B={Z>1-b}` is the top triangle of the `(Z,D)` diamond. Its unnormalized `D` density is simply
\[
w_B(d)=2(b-|d|),\qquad |d|\le b.
\tag{6.7}
\]

For `d>=0`,
\[
D'(d)=\int_0^d2(b-u)\,du=2bd-d^2.
\tag{6.8}
\]

The lower branch still uses `S=F(Z)`; the upper target has
\[
m_c=\frac{1+c}{2}=1-b^2.
\]
Using (5.2)--(5.3), exact integration over the two pieces gives
\[
C_A+C_{B,\perp}+C_{B,\parallel}
=
\frac{1-8b^5}{10}
=
\frac1{10}-\frac45b^5.
\tag{6.9}
\]
This proves (4.3), with strictness for every `b>0`, i.e. every `c<1`.

At `b=a=1/2` both regimes give `3/40`, so the construction matches continuously at `c=1/2`.

This completes the theorem.

## 7. What the theorem says about orientation gluing

The theorem gives a clean quantitative answer in the smallest one-interface model: **one orientation change cannot preserve the extremal value**.

For `0<c<=1/2`,
\[
\frac1{10}-W_2^2(\pi_c,\nu)\ge \frac{c}{20}
\]
for the explicit transport bound.

For `1/2<=c<1`,
\[
\frac1{10}-W_2^2(\pi_c,\nu)
\ge
\frac45\left(\frac{1-c}{2}\right)^{5/2}.
\]

The second exponent `5/2` is especially informative for the global program: a small antidiagonal block attached to the diagonal can approach the extremal value with a high-order deficit. Therefore any global orientation-gluing theorem must tolerate a very soft singular-interface cost near the diagonal endpoint; a linear penalty in the minority block mass cannot be true uniformly for this family.

This is new useful geometry even though the global metric did not move.

## 8. B11 — dualize: what succeeded and what did not

For the graph target, the primal problem is equivalently
\[
\inf_{\gamma\in\Pi(\lambda^{\otimes2},\lambda)}
\int\left|(x,y)-(s,g_c(s))\right|^2\,d\gamma(x,y,s).
\]
Its Kantorovich dual is a one-dimensional target-potential problem in `s`.

I attempted to use that dual to certify the **exact** value of the family. That route does not close here: the explicit transport above is not numerically optimal for generic interior `c` (the earlier finite approximations already suggested this), so no matching dual equality certificate should be expected for this particular partition.

The dual attempt was nevertheless useful diagnostically: proving the subclass inequality `W_2^2<=1/10` only requires a primal feasible coupling, not exact optimality. The B1/B6 construction therefore solves the recovery target without forcing an unnecessary exact dual. I record B11 as a failed exact-optimality route, not as a theorem certificate.

## 9. Exact self-check

The exact symbolic checker
`artifacts/R09/20260918T0331Z_g0013_block_reflection_exact.py`
recomputes (6.1)--(6.9), the two factorizations, the midpoint match and the sign bound used for `P(a)`.

Its archived output
`artifacts/R09/20260918T0331Z_g0013_block_reflection_exact.out`
ends

`SELF_CHECK_ONLY / PASS`.

The checker certifies the algebraic integrations only. The theorem-sized argument is the written proof above.

## 10. Metric, stuck state, and next obligation

The fixed **global** metric does not move:
\[
\boxed{
U_*^{\rm before}=U_*^{\rm after}
=
\frac{1289727882057511}{11918000000000000}
=
0.10821680500566462\ldots .
}
\]

Hence the supported G0013 unchanged count is
\[
4\to5.
\]

Status remains **PARTIAL / OPEN_CURRENT**.

This recovery did complete the simplest special case selected by STUCK1, so it is not a receipt-only run. But the owner's fixed metric is global, and the theorem cannot be relabeled as global movement.

A sixth unchanged global run is the CLOSABLE retirement threshold. Therefore the next R09 run has only two honest possibilities:

1. produce a genuine source-valid improvement `U_* < 0.10821680500566462...`, using the new one-interface geometry in a full-class argument; or
2. if no such global improvement is obtained, write the immutable six-run handoff and rotate to the next fully admitted eligible CLOSABLE outside target. Do not extend G0013 by changing the metric to a subclass quantity.

For one final source-valid attempt before that gate, the next three unused methods should be **B3 PROVE SOMETHING STRONGER, B17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, B27 SWAP THE QUANTIFIERS**: seek a full-class theorem that bounds total orientation-interface mass by the determinant/spectral deficit; identify whether the `5/2` interface exponent is a known sharp-interface/Monge--Ampere scaling; and replace pointwise interface control by a statement saying that any copula with `S>1/10` must have a uniformly positive amount of same-orientation mass across almost every level.

## 11. Model / scheduler control and permissions

The exposed automation control schema still offers title, prompt, schedule/relative start, timing mode and enabled state, but **no model-family selector, no reasoning-effort selector and no authenticated completed-run model telemetry**. GPT-6/maximum therefore remains prompt-only here.

The repository records that a historical P26 edit returned `You cannot modify this task` in one authorization context and later succeeded in another authorized context. The legitimate remedies for a currently denied task are the owning authorized context, ownership/admin transfer, or platform support. A repository write, cloned task, or permission bypass is not a scheduler repair.

No scheduler modification, workflow execution, email, Drive action, public posting, permission change or paid compute was performed.

## 12. Structured ledger delta

```yaml
ledger_delta:
  track: R09
  lane: CLOSABLE_OUTSIDE
  active_claim: G0013
  source_status: OPEN_CURRENT_BOUNDED
  result_status: PARTIAL
  metric:
    name: U_*
    before: "1289727882057511/11918000000000000"
    after: "1289727882057511/11918000000000000"
    movement: false
  unchanged_count:
    before: 4
    after: 5
  theorem_added:
    label: R09-G0013-ONE-INTERFACE-BLOCK-REFLECTION
    scope: "pi_c = Law(S,g_c(S)); one diagonal block plus one antidiagonal block"
    verdict: "W2^2(pi_c,lambda^2) <= 1/10 for all c; strict for 0<c<1"
    source_closure: false
  methods:
    - 1
    - 6
    - 11
  previous_target_Tang:
    status: RETIRED_FROZEN
    metric: UNBOUNDED_ABOVE
    retirement_count: 6
  previous_target_G0002:
    status: HANDOFF_FROM_R09
    metric: Delta_8=UNMEASURED
  next_gate: "one more unchanged global run triggers six-run CLOSABLE handoff/rotation"
  next_methods:
    - 3
    - 17
    - 27
```
