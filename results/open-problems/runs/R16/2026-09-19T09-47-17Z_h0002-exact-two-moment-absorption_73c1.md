Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**. **FIXED-METRIC MOVEMENT:** active H0002 envelope `G_major -> G_mom > G_major`. Methods actually used: **B18 / B25 / B5**.

# R16 — exact two-moment absorption improvement

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, owned by R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Continuity, source status, and nominal Beck–Fiala assignment

I re-read the current campaign INDEX/RANKING, root POSTED/RESULTS/QUEUE, the owner policy `operations/NEW_METHODS_2026-09-16.md`, the canonical claim `operations/claims/H0002.md`, the newest own report

`runs/R16/2026-09-19T08-56-58Z_h0002-prefix-majorization-absorption_5e7c.md`,

and neighboring work from the same Christoph–Morawski–Wigderson source. I preserve all earlier R16 definitions and do not restart the argument.

The nominal Beck–Fiala target is still a current-primary-source baseline rather than an honest unresolved R16 research target. Bansal–Jiang, arXiv:2508.03961, gives the square-root scale directly for `t >= log^2 n` and a weaker polylogarithmic bound below that range. Guo–Fang–Lu, arXiv:2609.11189 (10 Sep 2026), states the stronger Komlós theorem with constant `3 sqrt(2 pi)` and explicitly deduces discrepancy `< 3 sqrt(2 pi t)` for every integer `t>=1`. Karingula–Lovett, ECCC TR26-188 (17 Sep 2026), independently gives the Komlós constant `36`. These are very recent preprint/technical-report results, not a claim of mature refereed consensus.

R16 therefore continues its already-exclusive outside successor `H0002`, Christoph–Morawski–Wigderson, arXiv:2608.19145v1, Question 5.1. A bounded current title/author/question search still recovered the August 19 v1 source and no later source-matching resolution. This is negative evidence only.

## 2. Incoming metric and notation

The frozen H0002 class is unchanged: H1 spectral deletion resilience, H2 macroscopic pair expansion, and H3 `lambda(G)->infinity`. The tracked quantity is the largest explicit uniform giant fraction proved for this class at

`p >= (1+epsilon)/lambda(G)`.

The incoming strongest complete envelope from the preceding run is `G_major`. I retain the established notation:

- `d_P=d_pad<alpha` is the endpoint of the all-padding positive profile;
- `b_P=alpha-d_P>0`;
- `a_P=rho-b_P`;
- `s=1-rho`;
- `Delta=epsilon(7-epsilon)/(8-epsilon)>0` is the limiting absorption reserve;
- for `b in (b_P,beta]`,

  `t(b) = [a_P/(rho-b)] [F_pad(alpha-b)/b]`,

  extended by `t(b_P)=0`;
- choose `b_max=min(beta,1-a_P)>b_P`, `bar_b=(b_P+b_max)/2`, and let `b_0 in [b_P,bar_b]` maximize `t`; write `t_0=t(b_0)>0`;
- `D_*:=b_P t_0>0`.

For a pre-absorption connected core of density `a_3=c_3 a_P`, with `c_3<1` and `c_3 -> 1`, sort the normalized outside degrees into that core as a nondecreasing function `x(q)`. For every finite old anchor family `D`, let `L_D(q)` be the corresponding old full-core degree floor. The previous prefix-majorization run established, uniformly over all such finite `D`,

`int_0^{b_0} [x(q)-L_D(q)] dq >= c_3 D_* - o(1),`       (2.1)

with

`0 <= L_D(q) <= c_3 t_0 + o(1),`                         (2.2)

and the spectral energy bound

`int x(q)^2 dq <= c_3 a_P + o(1).`                        (2.3)

The prior run converted (2.1)–(2.3) by a hard truncation into the positive increment

`delta_major = min{b_P/16, delta_0/16}`,

where

`delta_0=(Delta D_*/4) exp(-4 Delta a_P/D_*).`

The goal here is to solve the moment subproblem exactly instead of truncating at an arbitrary height.

## 3. B18 — say it in another language: size-biased moment optimization

Write

`phi_r(u)=1-exp(-r u)`, `0<r<Delta`.

On `[0,b_0]`, define the surplus above the old degree floor by

`y(q)=(x(q)-L_D(q))_+`.

The possible `o(1)` violation in the pointwise old floor can be absorbed by lowering the floor by a vanishing amount; consequently (2.1) gives

`mu_1:=int_0^{b_0} y(q)dq >= c_3 D_* - o(1)`,             (3.1)

while `0<=y<=x+o(1)` and (2.3) give

`mu_2:=int_0^{b_0} y(q)^2dq <= c_3 a_P + o(1)`.           (3.2)

The absorption gain over the entire old finite-anchor profile is

`int [phi_r(x)-phi_r(L_D)] dq`

`= int exp(-r L_D)(1-exp(-r(x-L_D))) dq`

up to a vanishing floor-cleaning error. By (2.2),

`>= exp(-r c_3 t_0-o(1)) int_0^{b_0}(1-exp(-r y(q)))dq-o(1).`    (3.3)

Thus the remaining problem is a one-dimensional two-moment extremum.

## 4. B25 — count the same surplus twice: exact two-moment lemma

### Lemma 4.1

Let `y>=0` on a finite measure space, with

`mu_1=int y>0`, `mu_2=int y^2<infinity`.

Then for every `r>0`,

`int (1-exp(-r y)) >= (mu_1^2/mu_2) [1-exp(-r mu_2/mu_1)].`     (4.1)

Moreover the inequality is sharp for the abstract two-moment problem: equality is attained by a two-point profile taking values `0` and `mu_2/mu_1` whenever the ambient measure permits the required atom size.

### Proof

Define

`g_r(u)=(1-exp(-r u))/u = int_0^r exp(-s u) ds`,

with `g_r(0)=r`. Since every `u -> exp(-s u)` is convex, `g_r` is convex; it is also decreasing.

Introduce the `y`-size-biased probability measure

`d nu = y d q / mu_1`.

Then

`int (1-exp(-r y))dq = int y g_r(y)dq = mu_1 E_nu[g_r(y)].`

Jensen gives

`>= mu_1 g_r(E_nu y)`

`= mu_1 g_r(mu_2/mu_1)`

`= (mu_1^2/mu_2)[1-exp(-r mu_2/mu_1)].`

For a profile supported on `{0,mu_2/mu_1}`, the size-biased law is a point mass, so Jensen is equality. `QED`

This is the precise concentration obstruction that the previous truncation argument was approximating. No better inequality can follow from only `mu_1` and `mu_2`.

## 5. B5 — add the absorption parameter and differentiate

Set

`H_r(m,v)=m^2/v [1-exp(-r v/m)].`

For fixed `v>0`, writing `z=rv/m`,

`partial_m H_r = (m/v)[2(1-exp(-z))-z exp(-z)]>0`,

because `2(e^z-1)-z>0` for `z>0`. For fixed `m>0`, `H_r(m,v)` decreases in `v`, since `(1-exp(-z))/z` decreases in `z`.

Therefore (3.1), (3.2), Lemma 4.1 and (3.3) yield, uniformly over every finite old anchor family `D`,

`gain >= c_3 exp(-r c_3 t_0) (D_*^2/a_P)`

`        * [1-exp(-r a_P/D_*)] - o(1).`                  (5.1)

Now let first the graph size tend to infinity, then `c_3 up 1`, and finally `r up Delta`. Define

`eta_* := exp(-Delta t_0) (D_*^2/a_P)`

`         * [1-exp(-Delta a_P/D_*)] >0.`                 (5.2)

The old finite-anchor envelope was a supremum over finite `D`. Since (5.1) is uniform in `D`, the same increment survives that supremum. Hence the new complete envelope is

`G_mom := min{1, G_coreavg + eta_*}.`                     (5.3)

Every fixed `g<G_mom` is therefore achieved with probability tending to one on the same frozen H1–H2–H3 class.

## 6. Strict comparison with the entire incoming `G_major` envelope

It remains to check that (5.3) is strictly stronger than the preceding run, not merely a different positive receipt.

From the prefix lower bound at `b_0` and the spectral `L^2` bound, Cauchy–Schwarz gives in the endpoint limit

`b_0 t_0^2 <= a_P.`                                      (6.1)

Since `b_0>b_P`,

`b_P t_0^2<a_P.`                                         (6.2)

Put

`z=Delta a_P/D_*`, `w=Delta t_0`.

Because `D_*=b_P t_0`, (6.2) says `z>w`.

Compare (5.2) to the previous truncation increment

`delta_0=(Delta D_*/4)exp(-4z)`.

A direct ratio is

`eta_*/delta_0 = 4 exp(4z-w) (1-exp(-z))/z.`              (6.3)

Using `1-exp(-z)>=z exp(-z)`,

`eta_*/delta_0 >= 4 exp(3z-w)>4.`                         (6.4)

Also the old anchor-based envelope cannot absorb the first `b_P` fraction on which every old floor is zero, so

`G_coreavg <= 1-b_P.`                                    (6.5)

Thus the actual headroom is at least `b_P`. Define the conservative frozen increment

`delta_mom := (1/4) min{b_P,eta_*}>0.`                    (6.6)

Then (6.4) implies

`delta_mom > min{b_P/16,delta_0/16}=delta_major.`         (6.7)

Consequently

`G_coreavg+delta_mom > G_major`,

and therefore, a fortiori,

`boxed: G_mom > G_major.`                                 (6.8)

This is strict movement beyond the complete incoming envelope.

## 7. What this does and does not prove

The theorem is analytic and has no finite enumeration core, so no checker was manufactured. The exact two-moment lemma is self-contained above. It does **not** close CMW Question 5.1; H0002 remains a source-valid sufficient-condition result on the frozen H1–H2–H3 class.

The new lemma also certifies the next obstruction. Given only total surplus mass and spectral `L^2` energy, the worst surplus is exactly a zero/spike two-point profile. Hence another run cannot improve the moment step merely by choosing a better truncation threshold. A genuine next gain must use information discarded by the two-moment reduction: the full nested family of prefix constraints simultaneously, monotonicity of the sorted degree profile, or correlation between the surplus `y` and the baseline floor `L_D`.

The most promising next formulation is a convex-order/isotonic variational problem:

minimize `int phi_Delta(x(q))dq`

subject to all prefix lower bounds `int_0^b x >= b t(b)`, monotonicity of `x`, and `int x^2<=a_P`. Its extreme points should have finitely many plateaux. Proving that reduction, rather than producing another certificate, is the next substantive route.

## 8. Section-B accounting

- **B18 SAY IT IN ANOTHER LANGUAGE:** successful. Recast the remaining absorption gain as a size-biased two-moment optimization.
- **B25 COUNT THE SAME THING TWICE:** successful. The identity `g_r(u)=int_0^r exp(-su)ds`, combined with the `y`-size-biased law, gives the exact sharp moment inequality.
- **B5 ADD A PARAMETER AND DIFFERENTIATE:** successful. Differentiating `H_r(m,v)` proves the required monotonicity in the first and second moments and permits the boundary limit `r up Delta`.

These differ from the preceding run's B11/B24/B3 triple.

## 9. Model/scheduler-control status

The current exposed task-control interface still has no binding model-family selector, no reasoning-effort selector and no authenticated applied-model/reasoning receipt. It exposes scheduling/prompt/enablement-style controls, but GPT-6/maximum remains prompt text only. Actually enforcing the owner's request requires platform/API support for model and reasoning fields plus authenticated per-run runtime attestation.

No scheduler modification was attempted in this run, because the owner directive explicitly forbids scheduler changes from the research worker. The historical P26 `You cannot modify this task` denial remains an authorization-boundary issue; the compliant workaround is the owning authorized workspace/account or platform support, never duplication or permission bypass.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608_19145v1_Q5.1
  nominal_beck_fiala_status: KNOWN_CURRENT_PREPRINT_BASELINE
  metric_name: g_twoaxis_complete_envelope
  before: G_major
  after: G_mom = min(1, G_coreavg + eta_*)
  movement: STRICT_INCREASE
  status: PARTIAL
  supported_unchanged_count: 0
  methods: [18, 25, 5]
  finite_checker: NOT_APPLICABLE_ANALYTIC
  closure_audits: []
  remaining_obligation: >-
    Solve the full nested-prefix/isotonic absorption variational problem or
    otherwise use information beyond first and second surplus moments; source
    Question 5.1 remains broader than the frozen H1-H2-H3 theorem.
```
