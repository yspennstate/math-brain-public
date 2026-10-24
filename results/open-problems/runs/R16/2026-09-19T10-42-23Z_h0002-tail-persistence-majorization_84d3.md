Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**. **FIXED-METRIC MOVEMENT:** active H0002 complete envelope `G_mom -> G_tail > G_mom`. Methods actually used: **B8 / B12 / B23**.

# R16 — tail persistence rules out the two-moment spike extremizer

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Required continuity, source check, and nominal Beck–Fiala status

Before new work I re-read/reconciled the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/H0002.md`, the H-intake/source identity for arXiv:2608.19145, the newest own report

`runs/R16/2026-09-19T09-47-17Z_h0002-exact-two-moment-absorption_73c1.md`,

and the newest useful neighboring Christoph–Morawski–Wigderson-family work. I continue the existing H0002 chain and preserve all earlier definitions; I do not restart from the nominal Beck–Fiala prompt.

Fresh primary/current checks dated 2026-09-19 still show:

- Bansal–Jiang, arXiv:2508.03961, resolving the Beck–Fiala square-root scale directly for `t >= log^2 n`, with a weaker polylogarithmic-loss estimate below that range;
- Guo–Fang–Lu, arXiv:2609.11189v1 (submitted 2026-09-10), proving the stronger Komlós theorem with constant `3 sqrt(2 pi)` and explicitly deducing discrepancy `< 3 sqrt(2 pi t)` for every integer `t>=1`;
- Karingula–Lovett, ECCC TR26-188 (2026-09-17), giving an elementary Komlós proof with constant `36` and explicitly describing itself as a simplification of Guo–Fang–Lu;
- Christoph–Morawski–Wigderson, arXiv:2608.19145v1 (2026-08-19), still as the current source surfaced by bounded title/author/question searches; no later source-matching resolution of Question 5.1 was found. This last statement is negative evidence only.

Thus the literal Beck–Fiala existence target remains a **KNOWN current-preprint baseline**, not R16 novelty. The active source-valid successor remains H0002: natural conditions forcing a linear-size supercritical component at `p >= (1+epsilon)/lambda(G)`.

A bounded prior-art search on `prefix majorization`, `Lorenz order`, sorted degree sequences, percolation absorption, and spectral degree majorization returned classical majorization/degree-sequence material and standard percolation literature, but not the exact tail-persistence implication below. This is not a novelty certificate; sorting, majorization, sprinkling, and spectral `L^2` bounds are standard ingredients.

## 2. Incoming metric and notation

The frozen H0002 hypotheses remain exactly H1–H2–H3 from `operations/claims/H0002.md`.

Retain the notation of the preceding two reports:

- `d_P=d_pad<alpha`;
- `b_P=alpha-d_P>0`;
- `a_P=rho-b_P`;
- `u_P=1-a_P=s+b_P` with `s=1-rho`;
- `Delta=epsilon(7-epsilon)/(8-epsilon)>0`;
- on `b in (b_P,beta)`,

  `t(b)=[a_P/(rho-b)] [F_pad(alpha-b)/b]`,

  extended by `t(b_P)=0`;
- `b_max=min(beta,u_P)>b_P`, `bar_b=(b_P+b_max)/2`;
- choose `b_0 in argmax_[b_P,bar_b] t(b)` and write `t_0=t(b_0)>0`;
- `D_*:=b_P t_0>0`.

For a pre-absorption connected core `W` of density `a_3=c_3 a_P`, `c_3<1`, sort normalized outside degrees into `W` increasingly as `x(q)`. For a finite old anchor family `D`, let `L_{D,3}(q)` be its corresponding old degree floor.

The preceding prefix theorem gives, uniformly over finite `D`,

`int_0^{b_0} (x-L_{D,3})_+ dq >= c_3 D_* - o(1)`,         (2.1)

`0 <= L_{D,3}(q) <= c_3 t_0 + o(1)` on `[0,b_0]`,         (2.2)

and the spectral energy bound

`int x(q)^2 dq <= c_3 a_P + o(1)`.                         (2.3)

The preceding run solved the abstract two-moment problem exactly. With

`phi_r(z)=1-exp(-rz)`,

`g_r(z)=phi_r(z)/z`,

its endpoint gain over every old finite-family floor is

`eta_* = exp(-Delta t_0) D_* g_Delta(H_*)`,                (2.4)

where

`H_*:=a_P/D_*`.                                            (2.5)

Equivalently, (2.4) is the prior formula

`exp(-Delta t_0)(D_*^2/a_P)[1-exp(-Delta a_P/D_*)]`.

The incoming complete envelope is

`G_mom=min{1,G_coreavg+eta_*}`.

The goal is to use monotonicity of the *actual sorted degree profile* to show that the abstract zero/spike extremizer at height `H_*` cannot be realized without paying a second, disjoint absorption cost to the right of `b_0`.

## 3. B8 — discretize the obstruction before passing to the limit

The empirical profile is not an arbitrary measurable function: for every finite graph it is a nondecreasing step function obtained by sorting finitely many degrees

`x_1 <= x_2 <= ...`.

This finite ordering has a consequence the previous two-moment relaxation discarded:

> if a surplus spike makes `x_j` exceed a fixed level at any index `j <= b_0 n`, every later outside degree is at least that level as well.

Thus a spike used to minimize the concave absorption functional on the prefix cannot disappear immediately after the prefix. The continuum statement below is simply the limit of this exact finite ordering fact; no new probabilistic approximation is involved.

## 4. B12 — the conserved spectral-energy budget separates the spike height from every local old floor

The prefix constraint at `b_0` and Cauchy–Schwarz give, at the endpoint,

`b_0 t_0^2 <= a_P`.                                       (4.1)

Since `D_*=b_P t_0` and `b_0>b_P`,

`H_* = a_P/(b_P t_0) >= (b_0/b_P)t_0 > t_0`.              (4.2)

This strict gap is the key new invariant. The sharp two-moment extremizer wants its entire surplus concentrated at height `H_*`, but `H_*` lies strictly above the old floor height `t_0` at the maximizing prefix.

Let

`Gamma:=H_*-t_0>0`,

`T_+:=t_0+Gamma/4`,

`Y:=t_0+Gamma/2`.

Then

`t_0 < T_+ < Y < H_*`.                                    (4.3)

Because `b_0< b_max` and `t` is continuous on the positive terminal profile, there exists a fixed

`delta_loc>0`

with

`b_0+delta_loc < b_max`

and, shrinking it if necessary so that the isolated old `d_1` anchor is not yet active,

`sup_{b in [b_0,b_0+delta_loc]} t(b) <= T_+`.              (4.4)

Consequently, **for every finite old anchor family `D`**, its boundary floor obeys

`L_D(q) <= T_+` for `q in [b_0,b_0+delta_loc]`,            (4.5)

and the actual `c_3` floor obeys

`L_{D,3}(q) <= c_3 T_+ + o(1)` there.                     (4.6)

This bound is uniform in the choice of the old finite family.

## 5. B23 — assume the two-moment extremizer tries to occur

Put on the prefix

`y(q)=(x(q)-L_{D,3}(q))_+`.

After the usual vanishing floor-cleaning from the preceding run,

`int_0^{b_0} y >= c_3D_* - o(1)`,

`int_0^{b_0} y^2 <= c_3a_P + o(1)`.                       (5.1)

There are only two cases.

### Case A: the surplus never reaches the attempted spike height

Suppose

`y(q) <= Y`

a.e. on `[0,b_0]` (up to the vanishing finite-`n` slack). Since `g_r(z)=phi_r(z)/z` is strictly decreasing,

`phi_r(y) >= g_r(Y)y`.

Using `L_{D,3}<=c_3t_0+o(1)`, the gain over the old floor on the prefix is therefore

`int_0^{b_0}[phi_r(x)-phi_r(L_{D,3})]dq`

`>= exp(-r c_3t_0-o(1)) g_r(Y) int_0^{b_0}y dq-o(1)`

`>= c_3 exp(-r c_3t_0) D_* g_r(Y)-o(1)`.                  (5.2)

At the endpoint this exceeds the old exact two-moment gain by

`zeta_1 := exp(-Delta t_0)D_* [g_Delta(Y)-g_Delta(H_*)] >0`.    (5.3)

### Case B: the attempted spike occurs

Otherwise, for some prefix point one has `y>Y`, hence `x>Y`. Because the sorted degree profile `x` is nondecreasing, every later degree remains at least `Y`. In particular, throughout the **disjoint** interval `[b_0,b_0+delta_loc]`,

`x(q) >= Y-o(1)`.                                         (5.4)

But the old floor there is at most `c_3T_++o(1)`. Hence this tail interval alone contributes the extra gain

`>= delta_loc [phi_r(Y-o(1))-phi_r(c_3T_++o(1))]`.        (5.5)

The prefix `[0,b_0]` simultaneously retains the complete old two-moment gain from the preceding theorem. Sending graph size to infinity, then `c_3 up 1` and `r up Delta`, gives the additional disjoint increment

`zeta_2 := delta_loc [phi_Delta(Y)-phi_Delta(T_+)] >0`.    (5.6)

Thus the abstract zero/spike extremizer is impossible in the actual sorted degree problem: if the spike is capped below `Y`, the prefix functional is strictly larger; if the spike crosses `Y`, monotonicity propagates it into a positive-length tail on which no old anchor floor can catch it.

## 6. Uniform gain beyond the entire previous envelope

Define

`zeta_* := min{zeta_1,zeta_2} >0`.                         (6.1)

Sections 5A–5B show, uniformly over every finite old anchor family,

`absorption gain over that old floor >= eta_* + zeta_* - o(1)`

after the same endpoint limiting sequence used in the preceding reports. Since the estimate is uniform in the finite family, it survives the supremum defining `G_coreavg`.

Therefore define the new complete envelope

`G_tail := min{1, G_coreavg + eta_* + zeta_*}`.            (6.2)

Every fixed

`g < G_tail`

satisfies

`P(L_1(G_p) >= g n) -> 1`

uniformly on the unchanged frozen H1–H2–H3 class for every

`p >= (1+epsilon)/lambda(G)`.

No endpoint attainment is claimed.

### The cap at 1 does not destroy strict movement

The previous report wrote `G_mom=min{1,G_coreavg+eta_*}`. In fact the cap is inactive. Indeed,

`eta_* < D_*^2/a_P = b_P^2 t_0^2/a_P <= b_P^2/b_0 < b_P`,    (6.3)

using (4.1). The previous anchor theorem also gives

`G_coreavg <= 1-b_P`.                                     (6.4)

Hence

`G_mom=G_coreavg+eta_*<1`.                                (6.5)

Since `zeta_*>0`, (6.2) yields the strict comparison

`boxed: G_tail > G_mom`.                                  (6.6)

A conservative frozen receipt strictly beyond the complete incoming envelope is

`g_receipt := G_mom + (1/2) min{zeta_*,1-G_mom}`.          (6.7)

## 7. What this changes conceptually

The preceding run showed that first and second moments alone are exhausted: their exact extremizer is a zero/spike profile. This run identifies why that extremizer is **not compatible with the actual graph problem**. The degrees are sorted. A spike below the old prefix cannot be localized to that prefix; it creates a plateau to its right. Because the old anchor thresholds vary continuously and start strictly below the moment-extremizer height, that plateau incurs a fixed extra absorption cost before any old floor can catch up.

So the next obstruction is narrower. Further progress cannot come from another two-moment inequality or another arbitrary truncation. It must use one of:

1. repeat the tail-persistence argument across several successive local maxima of the threshold profile `t(b)`;
2. solve the full isotonic obstacle problem generated by the running envelope of `t(b)`;
3. improve the spectral energy budget using the three-block structure already available from earlier R16 reports.

The natural next target is (1): iterate local spike/plateau exclusions over a finite chain of profile cells and quantify the cumulative gain. This is genuinely beyond the one-prefix argument here.

## 8. Section-B accounting

- **B8 GO THE OTHER WAY AND DISCRETIZE:** successful. Returning to the finite sorted degree vector exposed that a high prefix spike forces every later coordinate to stay high.
- **B12 FIND WHAT IS CONSERVED:** successful. The spectral `L^2` budget plus the prefix constraint forces the sharp two-moment spike height `H_*=a_P/D_*` to lie strictly above `t_0`.
- **B23 DO WHAT THE PROPOSER DID NOT EXPECT:** successful. Assume the abstract moment extremizer tries to occur; either cap it and improve the prefix functional or let it occur and pay a disjoint tail-absorption penalty.

These differ from the preceding run's B18/B25/B5 triple.

## 9. Model/scheduler control

The exposed task-control schema still provides prompt/title, schedule/start, timing mode and enablement controls, but no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model/reasoning receipt. GPT-6/maximum therefore remains prompt text only. Enforcing it requires platform-level model/reasoning fields plus runtime attestation.

No scheduler modification was attempted, because this worker's controlling instruction forbids scheduler changes. The historical P26 permission denial is an authorization-boundary issue; the compliant route for any still-denied task is its owning authorized workspace/account or platform support, never duplication or permission bypass.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_beck_fiala_status: KNOWN_CURRENT_PREPRINT_BASELINE
  metric_name: g_twoaxis_complete_envelope
  before: G_mom
  after: G_tail = min(1, G_coreavg + eta_* + zeta_*)
  movement: STRICT_INCREASE
  status: PARTIAL
  supported_unchanged_count: 0
  methods: [8, 12, 23]
  finite_checker: NOT_APPLICABLE_ANALYTIC
  closure_audits: []
  remaining_obligation: >-
    Iterate the local spike/plateau exclusion across the threshold-profile cells
    or solve the full isotonic obstacle problem; source Question 5.1 remains
    broader than the frozen H1-H2-H3 sufficient-condition theorem.
```
