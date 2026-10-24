Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**. **FIXED-METRIC MOVEMENT:** active H0002 complete envelope `G_tail -> G_dep > G_tail`. Methods actually used: **B6 / B21 / B29**.

# R16 — energy-depleted threshold deformation strictly improves the tail-persistence envelope

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Continuity, repository state, and source/current-status check

I continued from the newest immutable R16 report

`runs/R16/2026-09-19T10-42-23Z_h0002-tail-persistence-majorization_84d3.md`

and re-read/reconciled the campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, and the canonical claim `operations/claims/H0002.md`. I also checked the newest useful neighboring same-source tracks recovered by repository search: R7-07/G0011 (the distinct long-cycle conjecture from the same paper) and the terminal G0010 tight-subcritical track. Neither supplies a premise used below and no ownership conflict with H0002 was found.

Fresh primary/current checks dated 2026-09-19:

- Bansal–Jiang, arXiv:2508.03961v2, still states the Beck–Fiala square-root result directly for `t >= log^2 n`, with a weaker polylogarithmic-loss bound below that range: https://arxiv.org/abs/2508.03961 .
- Guo–Fang–Lu, arXiv:2609.11189v1 (submitted 2026-09-10), proves the stronger Komlós signing theorem with constant `3 sqrt(2 pi)` and explicitly deduces discrepancy `< 3 sqrt(2 pi t)` for every integer `t>=1`: https://arxiv.org/abs/2609.11189 .
- Karingula–Lovett, ECCC TR26-188 (2026-09-17), gives an elementary Komlós proof with constant `36` and explicitly describes itself as simplifying the recent Guo–Fang–Lu proof: https://eccc.weizmann.ac.il/report/2026/188/ .
- Christoph–Morawski–Wigderson, arXiv:2608.19145v1 (2026-08-19), remains the current primary source surfaced for H0002. Its Question 5.1 asks for natural conditions guaranteeing a linear-size component above `(1+epsilon)/lambda(G)` and identifies localization of the spectral radius as the main obstruction: https://arxiv.org/abs/2608.19145 . A bounded 2026-09-19 title/author/question/arXiv-ID search surfaced no later source-matching resolution. This is negative evidence only.

Thus the literal Beck–Fiala existence target remains a **KNOWN current-preprint baseline**, not R16 novelty. The source-valid active successor remains H0002 under the frozen H1–H2–H3 sufficient-condition class.

A bounded method search on `isotonic moment optimization`, `majorization`, `monotone quantile constraints`, and `bathtub principle` surfaced generic order-restricted optimization and moment-problem literature, but not the exact energy-depletion/tail-absorption inequality below. This is not a novelty certificate; majorization, isotonicity, Jensen, and moment extremization are standard tools.

## 2. Incoming metric and notation

All frozen H0002 hypotheses and every earlier proved reduction are retained unchanged. In particular:

- `d_P=d_pad<alpha`;
- `b_P=alpha-d_P>0`;
- `a_P=rho-b_P`;
- `Delta=epsilon(7-epsilon)/(8-epsilon)>0`;
- `t(b)` is the endpoint full-core threshold profile from the preceding reports;
- `b_0>b_P` is a maximizing point on the fixed compact interval selected previously;
- `t_0=t(b_0)>0`;
- `D_*:=b_P t_0>0`;
- `H_*:=a_P/D_*`;
- `phi_r(u):=1-exp(-r u)` and `g_r(u):=phi_r(u)/u`, with `g_r(0)=r`.

For a connected pre-absorption core `W` of density `a_3=c_3 a_P`, `c_3 up 1`, sort normalized outside degrees into `W` increasingly as `x(q)`. For every finite old anchor family `D`, let `L_{D,3}(q)` be its corresponding old degree floor. The earlier prefix-majorization theorem gives, uniformly in finite `D`,

`int_0^{b_0} (x-L_{D,3})_+ dq >= c_3 D_* - o(1)`,       (2.1)

`L_{D,3}(q) <= c_3 t_0 + o(1)` on `[0,b_0]`,             (2.2)

and

`int x(q)^2 dq <= c_3 a_P + o(1)`.                        (2.3)

The exact two-moment gain is

`eta_* = exp(-Delta t_0) D_* g_Delta(H_*)`.               (2.4)

The immediately preceding tail-persistence report proved

`H_*>t_0`,                                                  (2.5)

set

`Gamma:=H_*-t_0`,
`T_+:=t_0+Gamma/4`,
`Y:=t_0+Gamma/2`,                                           (2.6)

and fixed `delta_loc>0` with

`L_{D,3}(q) <= c_3 T_+ + o(1)`

uniformly for all finite old anchor families on

`q in [b_0,b_0+delta_loc]`.                               (2.7)

It then defined

`zeta_1 = exp(-Delta t_0) D_* [g_Delta(Y)-g_Delta(H_*)]`, (2.8)

`zeta_2 = delta_loc [phi_Delta(Y)-phi_Delta(T_+)]`,       (2.9)

`zeta_* = min{zeta_1,zeta_2}>0`,                          (2.10)

and the incoming complete envelope

`G_tail=min{1,G_coreavg+eta_*+zeta_*}`.                   (2.11)

The goal of this run is to use the spectral energy consumed by a persistent tail plateau. The preceding proof charged the plateau to the absorption functional but **did not subtract its energy from the prefix two-moment budget**.

## 3. B6 — deform the old two-case threshold

Instead of freezing the dichotomy at `Y`, introduce a parameter

`X in [T_+,Y]`.                                            (3.1)

There are two cases.

### Case A(X): no prefix degree crosses X

Suppose

`x(q) <= X+o(1)` for all `q in [0,b_0]`.

With

`y(q)=(x(q)-L_{D,3}(q))_+`,

we have `y<=X+o(1)`. Since `g_r` is strictly decreasing,

`phi_r(y)=y g_r(y) >= y g_r(X+o(1))`.

Using (2.1)–(2.2), the prefix gain over the old floor is at least

`c_3 exp(-r c_3 t_0) D_* g_r(X)-o(1)`.

After `n->infinity`, `c_3 up 1`, and `r up Delta`, the gain **beyond eta_*** is

`A(X):=exp(-Delta t_0) D_* [g_Delta(X)-g_Delta(H_*)].`    (3.2)

Because `X<H_*`, `A(X)>0`; moreover `A` is continuous and strictly decreasing in `X`. At the old threshold,

`A(Y)=zeta_1`.                                             (3.3)

This deformation is useful only if the complementary branch also improves, which is the next step.

## 4. B21 — the tail plateau spends the same spectral-energy currency as the prefix spike

This is the new quantitative observation.

### Lemma 4.1 — energy-depleted tail branch

Fix `X in [T_+,Y]`. Suppose Case A(X) fails, so some prefix point has `x>X` (up to the vanishing finite-size slack). Since `x` is nondecreasing, throughout the disjoint interval

`I_tail=[b_0,b_0+delta_loc]`

we have

`x(q) >= X-o(1)`.                                         (4.1)

Hence this tail interval consumes spectral energy

`int_{I_tail} x(q)^2 dq >= delta_loc X^2-o(1)`.           (4.2)

Combining with the global energy budget (2.3), the **prefix** surplus second moment now obeys

`mu_2:=int_0^{b_0} y(q)^2 dq`

`<= c_3 a_P-delta_loc X^2+o(1)`.                          (4.3)

Meanwhile

`mu_1:=int_0^{b_0} y(q)dq >= c_3 D_*-o(1)`.              (4.4)

The exact two-moment lemma from the preceding run states

`int phi_r(y) >= mu_1 g_r(mu_2/mu_1)`.                    (4.5)

Because `g_r` is decreasing, (4.3)–(4.4) imply, whenever the tail branch is feasible,

`int_0^{b_0} phi_r(y)dq`

`>= c_3 D_* g_r((c_3 a_P-delta_loc X^2)/(c_3D_*))-o(1)`. (4.6)

After the endpoint limits, define

`V(X):=a_P-delta_loc X^2`.                                (4.7)

If `V(X)>0`, the prefix gain beyond the old exact two-moment value is therefore

`C(X):=exp(-Delta t_0)D_*`

`       *[g_Delta(V(X)/D_*)-g_Delta(H_*)] >0`.            (4.8)

The strict positivity follows from `V(X)<a_P` and strict decrease of `g_Delta`.

At the same time, (2.7) and (4.1) give the disjoint tail absorption gain

`delta_loc[phi_Delta(X)-phi_Delta(T_+)]`.                 (4.9)

Thus the complementary branch beats `eta_*` by

`B(X):=C(X)+delta_loc[phi_Delta(X)-phi_Delta(T_+)]`,      (4.10)

whenever `V(X)>0`.

If `V(X)<=0`, the complementary branch is impossible: (4.2) already exhausts the entire endpoint spectral-energy budget, while the positive prefix surplus (4.4) requires additional positive energy. In that case assign the branch cost

`B(X):=+infinity`.                                        (4.11)

This convention is not cosmetic; it exactly records infeasibility.

### Consequence at the old threshold

If `V(Y)>0`, then

`B(Y)=zeta_2 + exp(-Delta t_0)D_*`

`      *[g_Delta((a_P-delta_loc Y^2)/D_*)-g_Delta(H_*)]`

`> zeta_2`.                                                (4.12)

If `V(Y)<=0`, then the tail branch at `Y` is impossible, so again in the extended sense

`B(Y)>zeta_2`.                                             (4.13)

This is the strict information missing from the preceding report: whenever the spike persists into the tail, it pays **twice** — directly in the absorption functional and indirectly by shrinking the amount of `L^2` energy available for concentrating the prefix surplus.

## 5. B29 — close the variational interval by adding the infeasible point at infinity

The previous dichotomy used a single arbitrary threshold. The natural closed one-dimensional envelope is now

`zeta_dep := sup_{X in [T_+,Y]} min{A(X),B(X)}`.           (5.1)

Here the `+infinity` value in (4.11) compactifies the infeasible tail branch: no separate degenerate case is needed.

### Proposition 5.1 — strict improvement over the entire old tail constant

`zeta_dep > zeta_*`.                                      (5.2)

### Proof

Recall `A(Y)=zeta_1` and `B(Y)>zeta_2`.

**Case 1: `zeta_2<zeta_1`.** At `X=Y`,

`A(Y)>zeta_2` and `B(Y)>zeta_2`,

hence

`min{A(Y),B(Y)}>zeta_2=zeta_*`.

Therefore (5.2) holds.

**Case 2: `zeta_1<=zeta_2`.** At `X=Y`,

`A(Y)=zeta_1=zeta_*`,

while

`B(Y)>zeta_2>=zeta_*`.

Because `A` is strictly larger at every `X<Y`, and because `B` is continuous on its feasible branch (while an infeasible branch has value `+infinity`), there exists `X<Y` sufficiently close to `Y` such that simultaneously

`A(X)>zeta_*`, `B(X)>zeta_*`.

If `V(Y)=0`, use `g_Delta(0)=Delta`; the feasible-side limit of the positive correction in (4.8) remains strictly positive. If `V(Y)<0`, infeasibility persists on a left neighborhood of `Y`, making the second inequality automatic. Hence again

`min{A(X),B(X)}>zeta_*`.

This proves (5.2). `QED`

There is also a useful monotonic structure: on every feasible portion of `[T_+,Y]`, `A(X)` decreases with `X`, whereas both terms in `B(X)` increase with `X`. Thus `zeta_dep` is characterized by the unique crossing `A=B` when a crossing exists, and otherwise by an endpoint. This reduces the improvement to a one-dimensional scalar solve; no numerical certificate is required for the theorem.

## 6. New complete envelope and strict fixed-metric movement

The estimates above are uniform over every finite old anchor family `D`. Therefore, after taking the same finite-family supremum and endpoint limits as in the preceding reports, define

`G_dep := min{1,G_coreavg+eta_*+zeta_dep}`.                (6.1)

Every fixed

`g<G_dep`

satisfies

`P(L_1(G_p)>=g n) -> 1`                                   (6.2)

uniformly on the unchanged frozen H1–H2–H3 class for every

`p >= (1+epsilon)/lambda(G)`.                             (6.3)

No endpoint attainment is claimed.

It remains to rule out the possibility that the incoming `G_tail` was already capped at one. This can be done from the old constants themselves. Since `zeta_*<=zeta_1`,

`eta_*+zeta_*`

`<= eta_*+zeta_1`

`= exp(-Delta t_0)D_* g_Delta(Y)`

`< D_*/Y`

`= b_P t_0/Y`

`< b_P`,                                                   (6.4)

because `Y>t_0` and `g_Delta(Y)<1/Y`. The earlier full-core anchor theorem gives

`G_coreavg<=1-b_P`.                                       (6.5)

Hence

`G_tail=G_coreavg+eta_*+zeta_*<1`.                        (6.6)

Combining (5.2) and (6.6),

`boxed: G_dep > G_tail`.                                  (6.7)

A frozen coefficient strictly beyond the entire incoming complete envelope is

`g_receipt := G_tail`

`             + (1/2) min{zeta_dep-zeta_*, 1-G_tail}`.    (6.8)

Then

`G_tail < g_receipt < G_dep`.                             (6.9)

This is genuine movement of the same complete H0002 giant-fraction metric, not a new restricted subcase and not a relabeling of the old tail theorem.

## 7. What was learned / next obstruction

The preceding run showed that the two-moment spike extremizer must create a persistent tail. This run shows that the tail cannot be charged only once: the plateau also depletes the global spectral `L^2` budget, which forces the prefix moment extremum itself upward. Optimizing the dichotomy threshold turns this into a strict gain beyond the previous `min{zeta_1,zeta_2}` constant.

The remaining obstruction is now closer to the full isotonic obstacle problem. The one-threshold relaxation still forgets the **entire running profile** of lower bounds `b -> t(b)`. A next movement would have to use more than one persistent level simultaneously, or characterize the extremal nondecreasing `x` under all prefix constraints and the global quadratic budget. A natural target is a finite-plateau reduction for

`min int phi_Delta(x(q)) dq`

subject to

`x nondecreasing`,

`int_0^b x(q)dq >= the full certified prefix envelope for every b`,

`int x(q)^2dq <= a_P`.

The generic isotonic/moment literature suggests plateau extremizers are natural, but no external theorem found in the bounded search directly supplies this percolation-specific constrained functional. That remains the next substantive route.

## 8. Section-B accounting

- **B6 DEFORM TO A POINT YOU CAN SOLVE:** successful. Replacing the fixed old threshold `Y` by a free scalar `X` exposed a strictly better two-branch minimax bound.
- **B21 ASK WHO ELSE HAS THIS SHAPE:** successful as a method transfer. Viewing the tail plateau and prefix spike as competing for one conserved quadratic budget is the same resource-depletion geometry that appears in isotonic/moment and bathtub-style variational problems; this led to subtracting `delta_loc X^2` before applying the exact moment lemma. The literature search is comparison only, not a novelty certificate.
- **B29 ADD THE POINTS AT INFINITY:** successful. Assigning `B(X)=+infinity` exactly when the persistent tail alone exhausts the `L^2` budget closes the scalar variational domain and removes an otherwise awkward degenerate case.

These differ from the immediately preceding B8/B12/B23 triple and from the original exhausted B4/B19/B30 startup moves.

## 9. Model and scheduler-control status

The exposed scheduler/task-control surface still has no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning receipt. GPT-6/maximum therefore remains prompt text only. Actually enforcing it requires platform-level model/reasoning fields plus authenticated runtime attestation.

No scheduler modification was attempted because the controlling owner instruction for this worker forbids scheduler changes. The repository policy records historical native modification denials (`You cannot modify this task`) for P26/P01/P03; the compliant workaround is the owning authorized workspace/account or platform support. There is no legitimate duplication or permission bypass.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_beck_fiala_status: KNOWN_CURRENT_PREPRINT_BASELINE
  nominal_uniform_bound_current_primary_source: "B(t,n) < 3*sqrt(2*pi*t) for every integer t>=1 (Guo-Fang-Lu v1)"
  metric_name: g_twoaxis_complete_envelope
  before: G_tail
  after: G_dep = min(1, G_coreavg + eta_* + zeta_dep)
  movement: STRICT_INCREASE
  status: PARTIAL
  supported_unchanged_count: 0
  methods: [6, 21, 29]
  finite_checker: NOT_APPLICABLE_ANALYTIC
  closure_audits: []
  remaining_obligation: >-
    Use the full nested prefix profile simultaneously, ideally by proving a
    finite-plateau/extreme-point theorem for the isotonic obstacle problem;
    source Question 5.1 remains broader than the frozen H1-H2-H3 theorem.
```
