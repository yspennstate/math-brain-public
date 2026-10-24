Model actually run: **GPT-5.6 Sol**; reasoning level **UNVERIFIED**—not verified GPT-6 maximum. **No movement in the certified pointwise bound `B_R13(n)` this run; two route obstructions were proved: `R13-X08` for arbitrary vertical reweightings of the standard Guo--Fang--Lu lift, and `R13-X09` for regular i.i.d. product cube densities. Methods used: #5 ADD A PARAMETER AND DIFFERENTIATE/OPTIMIZE IT, #11 DUALIZE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.**

# R13 — Boolean Komlós: sharp barriers for two natural constant-improvement routes

Run ID: `20260917T1134Z_weighted-lift-product-obstructions-4c91`  
Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and fixed metric

The target remains the **real Boolean** Komlós signing problem: for every deterministic real `m x n` matrix `A` whose columns have Euclidean norm at most one, choose `epsilon in {-1,+1}^n` with uniformly bounded `||A epsilon||_infinity`. Complex phases, vector/rank-two colorings and average-case statements do not replace this target.

The frozen metric remains the complete pointwise certified upper-envelope function `B_R13(n)`, with every constant and range stated. I continued from the newest complete R13 report

`runs/R13/20260917T1033Z_balanced4-symbolic-6a71.md`

at creation/readback commit

`cc122a082c24253ddc9a7bcfb969b731db997ef7`.

Its retained certified envelope is

`B_R13(1) = 1`,

`B_R13(2) = sqrt(2)`,

`B_R13(3) = (sqrt(11)+sqrt(2))/3`,

`B_R13(n) = sqrt(3n/4)` for `4 <= n <= 75`,

`B_R13(n) = 3 sqrt(2 pi)` for `n >= 76`.

The equality signs above define the selected **certified upper envelope**, not the unknown exact finite-`n` constants. The entries through `n=4` retain their earlier exact-value status; the later entries are upper certificates unless separately proved exact.

This run does **not** improve that function, so the metric is unchanged. The preceding report had stagnation count `0`; this run therefore records stagnation count `1`, not UNKNOWN.

Before research I reread/recovered the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the `E0042` Komlós intake record, the newest R13 report and its exact-artifact status, and neighboring current state. R12 is now on `I0002`, so its historical Komlós audit does not create duplicate current ownership. I did not edit any shared root or peer track.

All thirty section-B labels have already appeared somewhere in the long R13 history, so a literally never-used label is no longer available. This run does not repeat the preceding triple `#16,#24,#27`, and both mathematical routes below are different from the balanced-four-block certificate.

## 2. Fresh source and prior-art check — 17 September 2026

Current source navigation remains:

1. Nikhil Bansal and Haotian Jiang, `arXiv:2508.03961v2`, with the later exposition `arXiv:2608.28452v1`: full **Boolean** Komlós, with the earlier `\widetilde O((log n)^(1/4))` scale.
2. Shengtao Guo, Ethan X. Fang and Junwei Lu, *Vector Balancing via Directional Total Variation*, `arXiv:2609.11189v1`, submitted 10 September 2026: full deterministic **real Boolean** theorem
   `||sum epsilon_j v_j||_infinity < 3 sqrt(2 pi)`
   for Euclidean-unit vectors. The abstract explicitly gives the stability threshold `kappa ||v||_2 <= 1/3`.
3. Guillen--Kobzar `arXiv:2609.15071v1`, submitted 14 September 2026: unit-modulus complex phases / rank-two vector discrepancy on real input, not Boolean signing.

A bounded fresh search found no correction or withdrawal of Guo--Fang--Lu v1.

For the two mechanisms below I also checked Guo--Fang--Lu's discussion of the lifted-density proof and the related Smirnov--Vershynin paper *Discrepancy and Fisher information*, `arXiv:2605.13107`. Smirnov--Vershynin already connect densities of the form `pi=psi^2`, Fisher information, the first Dirichlet eigenfunction, and the cosine-squared cube density. Therefore the Fisher/Dirichlet ingredients in `R13-X09` are **not claimed as new**. I did not locate the exact diagonal-direction obstruction statement `R13-X09`, nor the arbitrary-vertical-marginal obstruction `R13-X08`, in the bounded search. That negative search is not a novelty certificate; publication novelty remains **UNVERIFIED**.

## 3. Method #5 — add a parameter: arbitrary vertical marginal in the standard lift

Guo--Fang--Lu prove finite-step stability by lifting a density `rho` through

`B = {(y,s): |s| < 3, y + s v in K}`

and starting from the factorized density proportional to `rho(y+s v)` with a **uniform** vertical marginal. A natural attempt to beat the threshold `kappa ||v|| <= 1/3` is to replace the uniform vertical law by an arbitrary probability density `w(s)` supported in `[-3,3]`:

`R_w(y,s) = w(s) rho(y+s v)`.

This preserves the horizontal directional-variation budget because `int w = 1`, and the same vertical fiber rearrangement is available. The only question is whether a better `w` can force a larger rearranged mean absolute height and thereby make the prescribed-section step work beyond `1/3`.

The answer is **no for this entire factorized-lift variation**. The obstruction is exact and one-dimensional.

## 4. Method #11 — dualize the vertical optimization by layer cake and rearrangement

For a nonnegative one-dimensional function `f`, let `f^#` be its symmetric decreasing rearrangement and let

`mu_f(t) = |{s : f(s)>t}|`.

Layer cake gives

`int |s| f^#(s) ds = (1/4) int_0^infinity mu_f(t)^2 dt`

and equivalently

`int |s| f^#(s) ds = (1/4) int int min(f(s),f(r)) ds dr`.      (4.1)

This identity turns the rearranged-height problem into a two-point kernel extremal problem.

### R13-X08 — arbitrary vertical reweighting cannot beat the `1/3` threshold in the standard factorized lift

Fix `0 < a <= 3`, take the one-dimensional convex body

`K_a = (-a,a)`,

translation vector `v=1`, and the uniform density

`rho_a(x) = (1/(2a)) 1_{(-a,a)}(x)`.

Its distributional directional variation is

`V_1(rho_a) = 1/a`.      (4.2)

Let `w` be **any** probability density supported in `[-3,3]`, and use the standard factorized lifted density

`R_w(y,s) = w(s) rho_a(y+s)`.

Let `R_w^#` denote symmetric decreasing rearrangement in the vertical coordinate `s`, separately for each horizontal coordinate `y`, and define its mean absolute height

`M_a(w) = int int |s| R_w^#(y,s) ds dy`.

Then

`boxed:  M_a(w) <= a/2 - a^2/18`,      (4.3)

and equality is attained by the uniform vertical marginal

`w(s)=1/6` on `[-3,3]`.

In particular,

`M_a(w) < 1` for every `a<3`, for every such `w`,

while `V_1(rho_a)=1/a>1/3`. Thus **no choice of a y-independent vertical probability marginal in the standard factorized lift can extend the Guo--Fang--Lu prescribed-section argument to every input density with variation parameter strictly above `1/3`**.

This is a route obstruction only. It does **not** show that the actual finite-step stability theorem is false above `1/3`, and it does not rule out a nonfactorized lifted density, a `y`-dependent vertical law, a different lift, or a different invariant.

### Proof of X08

For fixed `y`, apply (4.1) to the function `s -> R_w(y,s)`. For fixed `s,r`, the two horizontal intervals

`|y+s|<a`, `|y+r|<a`

have overlap length

`(2a-|s-r|)_+`.

Therefore

`M_a(w) = (1/(8a)) int_{-3}^3 int_{-3}^3 min(w(s),w(r)) (2a-|s-r|)_+ ds dr`.      (4.4)

Write the layer-cake superlevel sets

`E_t = {s in [-3,3] : w(s)>t}`,

with lengths `ell(t)=|E_t|`, so `0<=ell(t)<=6` and

`int_0^infinity ell(t) dt = int w = 1`.      (4.5)

For the even radially nonincreasing kernel

`k_a(h)=(2a-|h|)_+`,

one-dimensional rearrangement gives, for each fixed measure `ell`,

`int_{E} int_{E} k_a(s-r) ds dr <= q_a(ell)`,

where the right side is attained by an interval of length `ell`. Direct integration gives

`q_a(ell) = 2a ell^2 - ell^3/3` for `0 <= ell <= 2a`,

`q_a(ell) = 4a^2 ell - (8/3)a^3` for `ell >= 2a`.      (4.6)

For `0<a<=3`, the function `q_a(ell)/ell` is strictly increasing on `(0,6]`:

- on `ell<=2a`, its derivative is `2a - 2ell/3 >= 2a/3 >0`;
- on `ell>=2a`, its derivative is `(8a^3)/(3ell^2)>0`.

Hence, using (4.5),

`int_0^infinity q_a(ell(t)) dt <= (q_a(6)/6) int_0^infinity ell(t)dt = q_a(6)/6`.      (4.7)

Since `a<=3`, the second line of (4.6) applies at `ell=6` and

`q_a(6)=24a^2-(8/3)a^3`.

Substitute into (4.4):

`M_a(w) <= (1/(8a)) (q_a(6)/6) = a/2-a^2/18`.

The constant vertical density `w=1/6` has one superlevel set of length six and attains every inequality. At `a=3`, (4.3) equals one. For every `a<3`, it is strictly less than one. This proves X08.

### What X08 adds beyond the obvious cutoff calculation

The paper's uniform-cutoff calculation can test changing one scalar cutoff. X08 optimizes **all probability densities `w` on the full allowed vertical interval**, including highly nonuniform and singular-limit shapes at the density level. The uniform marginal is already extremal for the explicit one-dimensional source density that sits at the stability boundary. Therefore “improve the constant by reshaping only the vertical marginal” is exhausted.

## 5. Method #17 — recognize `sqrt(2 pi)` as a Fisher/Dirichlet/CLT constant

The second possible place to improve Guo--Fang--Lu is the initial cube density. Their product cosine-squared density on `(-C,C)^d` has worst directional variation asymptotic to `sqrt(2 pi)/C`; combined with the `1/3` stability threshold this gives the universal half-side `3 sqrt(2 pi)`.

A natural question is whether one can keep the **i.i.d. product ansatz** but replace the one-dimensional cosine-squared factor by a better factor. For a regular zero-boundary factor, the answer is again no asymptotically.

### R13-X09 — regular i.i.d. product densities cannot beat `sqrt(2 pi)/C`

Fix `C>0`. Let `f` be an absolutely continuous probability density on `[-C,C]` satisfying

- `f>0` almost everywhere on `(-C,C)`;
- boundary traces `f(-C)=f(C)=0`;
- finite Fisher information

`I(f) = int_{-C}^C (f'(x))^2/f(x) dx < infinity`.

For dimension `d`, let

`rho_d(x_1,...,x_d)=prod_{j=1}^d f(x_j)`

on the cube `(-C,C)^d`, and let

`u_d = d^{-1/2}(1,...,1)`.

Then

`boxed: lim_{d->infinity} V_{u_d}(rho_d) = sqrt(2 I(f)/pi) >= sqrt(2 pi)/C`.      (5.1)

Consequently

`liminf_{d->infinity} C sup_{||u||_2=1} V_u(rho_d) >= sqrt(2 pi)`.      (5.2)

The cosine-squared factor attains equality in the lower bound. Thus, under the stated regularity assumptions, **no i.i.d. product density obtained merely by changing the one-dimensional factor can improve the asymptotic cube variation constant used by the current proof**.

Again, this is a route obstruction, not a universal lower bound over arbitrary correlated cube densities.

### Proof of X09

Let `X~f` and define the score

`Y = f'(X)/f(X)`.

The zero boundary traces imply

`E Y = int f'(x) dx = 0`,

while

`E Y^2 = I(f)`.      (5.3)

For `X_1,...,X_d` i.i.d. with density `f`, the directional derivative of the product density gives

`V_{u_d}(rho_d) = E |d^{-1/2} sum_{j=1}^d Y_j|`.      (5.4)

By the classical central limit theorem,

`d^{-1/2} sum Y_j -> N(0,I(f))`

in distribution. The second moments of these normalized sums are exactly `I(f)`, so the absolute values are uniformly integrable. Therefore first absolute moments converge:

`V_{u_d}(rho_d) -> E|N(0,I(f))| = sqrt(2 I(f)/pi)`.      (5.5)

Now put `g=sqrt(f)`. Under the assumptions above, `g in H_0^1(-C,C)` and

`I(f)=4 int_{-C}^C |g'(x)|^2 dx`,

with `int g^2=1`. The sharp one-dimensional Dirichlet Poincare inequality gives

`int |g'|^2 >= (pi/(2C))^2 int g^2 = pi^2/(4C^2)`,

so

`I(f) >= pi^2/C^2`.      (5.6)

Combining (5.5) and (5.6) gives

`sqrt(2 I(f)/pi) >= sqrt(2 pi)/C`.

Equality in (5.6) is attained by the first Dirichlet eigenfunction

`g(x) proportional to cos(pi x/(2C))`,

hence by

`f(x) proportional to cos^2(pi x/(2C))`,

which is exactly the familiar cosine-squared factor. This proves X09.

## 6. What moved, what failed, and what must be genuinely new next

### Fixed metric

No certified `B_R13(n)` entry changed. The complete retained bound remains

`B_R13(1)=1`,

`B_R13(2)=sqrt(2)`,

`B_R13(3)=(sqrt(11)+sqrt(2))/3`,

`B_R13(n)<=sqrt(3n/4)` for `4<=n<=75`,

`B_R13(n)<3sqrt(2pi)` for `n>=76` from Guo--Fang--Lu's universal theorem.

I retain the convention that the stored envelope may be written with equality signs to name the chosen certificate, while the mathematical statements are upper bounds except where exactness was separately proved.

### The three actual attacks

- **#5 ADD A PARAMETER.** Replaced the uniform vertical law in the standard Guo--Fang--Lu lift by an arbitrary probability density `w` on `[-3,3]`. This did **not** improve the stability threshold; X08 proves the uniform marginal is already optimal for an explicit boundary family.
- **#11 DUALIZE.** Rewrote rearranged mean height through a two-point `min` kernel and then layer-cake superlevel sets. One-dimensional rearrangement reduces the infinite-dimensional `w` optimization to the scalar length `ell`, yielding the exact X08 barrier.
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE.** Interpreted `sqrt(2pi)` through score CLT plus the first Dirichlet eigenvalue. This proves X09: changing only the regular i.i.d. product factor cannot lower the asymptotic initial-cube constant.

These are not auxiliary lemmas toward the same missing line. They eliminate two broad, natural constant-improvement directions.

### What a successful next route must contain

To improve the universal constant `3sqrt(2pi)` through the directional-variation framework, the next route must escape at least one side of both obstructions. Concrete possibilities are:

1. a **correlated, non-product cube density** with directional variation constant strictly below `sqrt(2pi)/C`;
2. a **nonfactorized or y-dependent lifted density** that beats the height obstruction X08;
3. a different transform/invariant whose finite-step threshold exceeds `1/3` without using the standard factorized lift;
4. a discrepancy argument not routed through directional total variation at all.

The strongest next attack is therefore not another finite-`n` denominator search and not another vertical-weight tweak. It is to attack the variational problem

`inf_{rho supported in (-1,1)^d} sup_{||u||_2=1} V_u(rho)`

for genuinely correlated `rho`, first in dimensions `d=2,3`, and determine whether the product cosine-squared density is locally or globally extremal. A strict correlated improvement would feed directly into the universal Komlós constant; a rigorous lower bound matching the product value would prove an explicit method obstruction.

## 7. Validation status

No finite enumeration claim was introduced in this run, so I did **not** manufacture a checker merely to create a certificate. X08 and X09 are theorem-sized analytic claims and their full arguments are written above. They are **self-checked only** in this run and have no two-track independent audit package.

The existing distinct `R12-AUDIT-R13-KOMLOS-01=PASS` and `P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11=PASS` concern the Guo--Fang--Lu universal theorem package, not X08/X09 or the previous balanced-four-block theorem.

Status remains **PARTIAL / NO METRIC MOVEMENT / NEW ROUTE OBSTRUCTIONS / outside audits not requested because the source metric did not move**.

This is the first unchanged run after the preceding metric movement, so the section-I stuck protocol is **not** triggered yet. `stagnation_count=1`.

## 8. Runtime/model control and scheduler permissions

The exposed task interface still provides prompt/title/schedule/enabled/timing controls but no native model-family or reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt-only; this run cannot authenticate that setting and does not claim it.

The repository record also remains clear about the historical `You cannot modify this task` error: it is context/ownership dependent. P26 was later editable from an authorized P/C context, while R-series edits were denied from another context. A genuine fix requires an authorized task/workspace-owner context or platform support exposing model/reasoning fields. I did not attempt to bypass permissions, duplicate a task, alter the scheduler, email, write to Drive, post publicly, execute workflows, or use paid compute.

```yaml
ledger_delta:
  track: "R13 HARD OUTSIDE"
  source: "Boolean Komlos; E0042/Bandeira Open Problem 0.1; current Boolean source navigation Bansal-Jiang arXiv:2508.03961v2 and Guo-Fang-Lu arXiv:2609.11189v1; Guillen-Kobzar arXiv:2609.15071v1 is complex/rank-two only"
  target: "complete rigorously certified pointwise real-Boolean discrepancy upper envelope B_R13(n)"
  status: "PARTIAL"
  metric_before: "B_R13(1)=1; B_R13(2)=sqrt2; B_R13(3)=(sqrt11+sqrt2)/3; B_R13(n)=sqrt(3n/4) for 4<=n<=75; B_R13(n)=3sqrt(2pi) for n>=76"
  metric_after: "UNCHANGED"
  movement: "no movement; proved method obstructions X08 and X09"
  methods: [5,11,17]
  obstruction_ids: ["R13-X08", "R13-X09"]
  X08_scope: "all y-independent vertical probability marginals w in the standard factorized |s|<3 lift, tested against the one-dimensional uniform boundary family"
  X09_scope: "regular zero-boundary iid product cube densities with finite Fisher information; asymptotic diagonal direction"
  exact_checker: "NONE -- no finite claim introduced"
  audits:
    universal_GFL_R12: "R12-AUDIT-R13-KOMLOS-01=PASS"
    universal_GFL_P26: "P26-AUDIT-R13-GFL-KOMLOS-ENDTOEND-11=PASS"
    X08_X09: "SELF-CHECK ONLY"
  prior_art: "fresh bounded search 2026-09-17; Smirnov-Vershynin Fisher/Dirichlet ingredients are known; exact X08/X09 formulations not located; novelty UNVERIFIED"
  stagnation_count: 1
  next_obligation: "leave factorized vertical weights and regular iid product cube densities; test genuinely correlated cube densities or a nonfactorized/y-dependent lift for a strict universal-constant improvement"
```
