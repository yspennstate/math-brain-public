Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala existence metric remains a **KNOWN current-preprint baseline** at `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`; on the active exclusive R16/H0002 successor, the strongest complete giant-fraction envelope moves strictly from `G_coreavg` to `G_major>G_coreavg` on the same frozen H1--H2--H3 class. Section-B methods actually used: **#11 DUALIZE, #24 FIND THE EXTREMAL OBJECT, #3 PROVE SOMETHING STRONGER**. The immediately preceding triple was #9/#14/#27, so this is not a consecutive repeat.

# R16 — H0002: prefix-majorization recovers mass below every old degree quantile

## 1. Continuity, ownership, source status, and required reads

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1. The source asks for natural conditions under which `p >= (1+epsilon)/lambda(G)` produces an `Omega(|G|)` component with constant probability, and explicitly identifies localization of the spectral radius on a small part of the graph as the main obstruction.

Before new mathematics I reconciled the required state rather than restarting: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H0002 intake identity `arxiv_2608_19145::Question 5.1; Section 5, Concluding remarks`, the newest own report `runs/R16/2026-09-19T07-45-32Z_h0002-full-core-anchor-averaging_6f3a.md`, the preceding multi-anchor report and its connected-core repair, and the current neighboring CMW-family state. The older CMW long-cycle line is a different source statement; no competing H0002 ownership was found.

Fresh primary/current checks on **19 Sep 2026** recover:

- CMW only as arXiv:2608.19145v1; the bounded search did not surface a later source-matching resolution of Question 5.1;
- Bansal--Jiang, arXiv:2508.03961v2, which reaches the Beck--Fiala `O(sqrt(t))` scale directly for `t>=log^2 n` and has a weaker polylog-loss estimate below that regime;
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), which states a `3 sqrt(2 pi)` Komlos theorem and explicitly deduces set-system discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`;
- Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), which gives an elementary Komlos proof with constant `36` and describes itself as simplifying the Guo--Fang--Lu proof.

Those last two are extremely recent preprint/technical-report results rather than mature refereed consensus, but their stated theorems make the literal Beck--Fiala existence target a current literature baseline rather than R16 novelty.

For prior art on the mechanism below I also searched combinations of `prefix-sum / majorization / degree quantile / sprinkling / giant component / spectral`. The bounded search returned general spectral-majorization papers for prescribed degree sequences and standard expander/pseudorandom percolation literature, but not the source-matching prefix-majorization absorption theorem below. This negative search is **not** a novelty certificate. Spectral `L^2` control, sprinkling, degree sorting, and majorization are standard ingredients; only the exact new implication on the frozen H0002 class is claimed here.

## 2. Frozen class and incoming envelope

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n:=|G|`, `lambda:=lambda(G)`,

`h:=1-epsilon/8`,

`q0:=1-exp(-epsilon^2/288)`,

`alpha:=rho*q0/64`,

`s:=1-rho>0`.

The graph class is unchanged:

1. **H1:** `lambda(G-S) >= h lambda` whenever `|S|<=rho n`;
2. **H2:** `e_G(X,Y) >= kappa lambda n` for all disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. **H3:** `lambda -> infinity`.

Use the established deficient-side parameterization

`a(d):=rho-alpha+d`,

`b(d):=alpha-d`,

so `a(d)+b(d)=rho`.

The all-padding theorem supplies a universal positive pair-capacity profile `F_pad(d)` on

`d1<d<dP`,

where `dP=d_pad` is the first zero-capacity endpoint. Thus, for every fixed `d` in that interval and every relevant disjoint pair `A,B` of densities `a(d),b(d)`,

`e(A,B) >= F_pad(d) lambda n-o(lambda n)`.

The newest report proved two facts used here:

- `dP<alpha`, hence `bP:=alpha-dP>0`;
- after averaging every certified subanchor into one connected core, the complete envelope is

`G_coreavg = aP + sup_D integral_0^1 max_{d in D: Rcore(d)>=r} m(d) dr`,

where

`aP:=a(dP)=rho-bP`, `uP:=1-aP=s+bP`, `m(d)=uP-b(d)=s-(dP-d)`,

and, for `d>d1`,

`Rcore(d) = 1-exp[-Delta (aP/a(d)) F_pad(d)/b(d)]`,

with `Delta:=epsilon*(7-epsilon)/(8-epsilon)>0`.

At the isolated old anchor `d1`, retain its already-valid rate `Ranc`. Every fixed `g<G_coreavg` has already been proved to satisfy `P(L1(G_p)>=g n)->1` uniformly on the frozen class for every `p>=(1+epsilon)/lambda`.

The goal of this run is to show that the entire `G_coreavg` envelope is still leaving a fixed amount of certified mass unused.

## 3. Method #11 — dualize the layer-cake bound into a degree floor

Parameterize an anchor by its deficient density `b:=alpha-d`. For `b in (bP,beta)`, where `beta:=alpha-d1`, put

`d(b):=alpha-b`, `a(b):=rho-b`,

`C(b):=[aP/a(b)] F_pad(d(b))`,

`t(b):=C(b)/b`.

Thus the boundary full-core rate is `Rcore(b)=phi_Delta(t(b))`, where `phi_r(x):=1-exp(-r x)`.

The endpoint facts inherited from the preceding reports imply `F_pad(d)->0` as `d up to dP`. Hence `t` extends to the left endpoint by `t(bP):=0`.

For a finite anchor family `D`, let its non-special deficient densities be `b_j`. Define the nondecreasing degree floor on `[0,uP]`

`L_D(q):=max { t(b_j): b_j<=q }`,

with the maximum of the empty set equal to zero, and include the old `d1` threshold only for `q>=beta` if that anchor is present.

Then Cavalieri/layer-cake gives exactly

`integral_0^{uP} phi_Delta(L_D(q)) dq = integral_0^1 max_{d in D:Rcore(d)>=r} m(d) dr`.

So `G_coreavg-aP` is the supremum over finite `D` of a **tail-floor relaxation**: each old anchor remembers only that, after sorting outside vertices by their degree into the connected core, all positions after `b_j n` lie above `t(b_j)`.

This dual form exposes what the previous proof discarded: the universal pair-capacity theorem gives a lower bound on the **sum of the whole bottom prefix**, not merely on its last order statistic.

## 4. Method #3 — retain every prefix sum, not just every quantile

Fix a pre-absorption connected core `W` of density `a3:=a(d3)` with `d3<dP` but close to `dP`, obtained by the already-proved harvesting/gluing argument and, if necessary, the connected-core spanning-tree trimming repair. Put `c3:=a3/aP`.

Choose a fixed `b>bP` with `d(b)<d3`. The full-core averaging theorem applies to every set `B subset V\W`, `|B|=bn+o(n)`, and gives

`e(W,B) >= [a3/a(b)] F_pad(d(b)) lambda n-o(lambda n) = c3 C(b) lambda n-o(lambda n)`.

Now sort the outside vertices by normalized degree into `W`:

`x_1<=x_2<=...<=x_N`, `x_i:=d_W(v_i)/lambda`,

where `N=(1-a3)n+o(n)`. Taking `B` to be the `bn` least-degree outside vertices yields the **prefix-majorization constraint**

`boxed: sum_{i<=bn} x_i >= c3 b t(b) n-o(n).`

Equivalently, for the empirical step function `x(q)` indexed by vertex-density `q`,

`boxed: integral_0^b x(q)dq >= c3 b t(b)-o(1).`

The previous theorem retained only the weaker consequence `x(b)>=c3 t(b)-o(1)`. So this is strictly stronger information on exactly the same random core and exactly the same host-graph hypotheses.

## 5. A uniform prefix gap against every finite old anchor family

Let

`bmax:=min{beta,uP}>bP`, `bar_b:=(bP+bmax)/2`.

The profile `F_pad` is the value of a compact finite-dimensional semialgebraic feasibility problem on each branch, so on the inherited terminal cell `t(b)` is continuous after the extension `t(bP)=0`. Choose

`b0 in argmax_{b in [bP,bar_b]} t(b)`, `t0:=t(b0)`.

Because `F_pad>0` in the interior, `b0>bP` and `t0>0`. Define

`boxed: D_*:=bP*t0>0.`

For **any** finite old anchor family `D`, the degree floor satisfies on `[0,b0]`:

- `L_D(q)=0` for `0<=q<bP`, because no certified anchor has deficient density below `bP`;
- `L_D(q)<=t0` for `bP<=q<=b0`, by the defining maximality of `t0`;
- the isolated `d1` threshold cannot intervene here because `b0<beta`.

Hence `integral_0^{b0} L_D(q)dq <= (b0-bP)t0`.

For the actual `d3` core, the non-special thresholds are all multiplied by the common factor `c3`, so on the same prefix

`integral_0^{b0} L_{D,3}(q)dq <= c3(b0-bP)t0`.

The new prefix constraint at `b0` gives

`integral_0^{b0} x(q)dq >= c3 b0 t0-o(1)`.

Therefore, uniformly over **every finite old anchor family**,

`boxed: integral_0^{b0} [x(q)-L_{D,3}(q)]dq >= c3 D_*-o(1).`

This is the decisive fact: the old layer-cake relaxation misses at least a fixed amount of normalized degree mass before the first `bP n` vertices can be discarded.

## 6. Method #24 — find the extremal obstruction, then use spectral energy to rule it out

A prefix-sum improvement does not by itself imply a fixed improvement in attachment probability, because `phi_r(x)=1-exp(-rx)` is concave. The formal worst case would concentrate all the extra degree mass on an asymptotically tiny set at arbitrarily large normalized degree, where `phi_r` is almost saturated. That is the extremal obstruction to a naive Karamata/Jensen argument.

The spectral radius rules out enough of that concentration. For the connected core `W`,

`sum_{v outside W} d_W(v)^2 <= ||A_G 1_W||_2^2 <= lambda^2 |W|`.

Thus

`boxed: integral_0^{1-a3} x(q)^2 dq <= a3+o(1).`

Set `M_*:=4 aP/D_*`. On the set `E={q in [0,b0]: x(q)>M_*}`, the inequality `x<=x^2/M_*` gives

`integral_E x(q)dq <= a3/M_*+o(1) = c3 D_*/4+o(1)`.

Since `L_{D,3}>=0`, at most that much of the prefix excess can hide in `E`. Combining with Section 5, for all large `n`,

`boxed: integral_{[0,b0]\E} [x(q)-L_{D,3}(q)]dq >= c3 D_*/2.`

Now fix an effective absorption numerator `r` with `Delta/2<=r<Delta`. The already-established probability split can reserve an independent final sprinkling round with edge probability at least `r/lambda` for all large `lambda`. Therefore a vertex with normalized core-degree `x` attaches directly to the connected core with probability at least `phi_r(x)=1-exp(-r x)`.

On the set `x<=M_*`,

`phi_r'(x)=r exp(-r x) >= (Delta/2) exp(-Delta M_*)`.

Since `x>=L_{D,3}` pointwise up to inherited vanishing slack, the mean-value theorem gives

`phi_r(x)-phi_r(L_{D,3}) >= (Delta/2) exp(-Delta M_*) [x-L_{D,3}]`

on `[0,b0]\E`. Hence the total attachment-probability gain over the old finite-family floor is at least

`boxed: c3 delta_0-o(1),`

where

`boxed: delta_0 := (Delta D_*/4) exp[-4 Delta aP/D_*] >0.`

The attachment events of distinct outside vertices use disjoint edge sets into `W`; conditional on the earlier rounds they are independent. The usual Poisson-binomial Chernoff bound therefore turns this expectation gain into a linear realized gain with probability `1-o(1)`.

This is exactly why the spectral `L^2` inequality matters: without it, a spike on an `o(n)` set is a genuine finite-dimensional obstruction to extracting a uniform concave-function gain from the prefix constraint.

## 7. Strict movement beyond the entire incoming supremum

The previous envelope is a supremum over finite `D`, so the comparison must be uniform in `D`. Section 5 made the degree-mass gap `D_*` uniform in `D`, and Section 6 converted it into the uniform attachment gap `delta_0`.

Let

`boxed: delta_major := min{ bP/16, delta_0/16 } >0,`

and define

`boxed: G_major:=G_coreavg+delta_major.`

Fix any `g<G_major`. First choose a finite anchor family `D` whose boundary layer-cake value is arbitrarily close to the supremum defining `G_coreavg`. Because `D` is finite, choose `d3<dP` close enough to `dP` that

- `d3` lies beyond every anchor in `D` and beyond the new fixed anchor `d(b0)`;
- `a3` is arbitrarily close to `aP` and `c3` is arbitrarily close to `1`;
- the actual finite-family degree floors are arbitrarily close to their boundary floors.

Then choose `r<Delta` close enough to `Delta` that the old finite-family absorption contribution is arbitrarily close to its boundary `Delta` value. The new prefix gain remains at least `c3 delta_0-o(1)` throughout this limiting process; in particular it is at least `delta_0/2` after taking `d3` sufficiently close to `dP`.

The losses from (i) approximating the old supremum by finite `D`, (ii) taking `d3<dP`, (iii) taking `r<Delta`, and (iv) the uniform `o(1)` terms can be made jointly much smaller than `delta_0/2`. The conservative factor `1/16` in `delta_major` leaves ample fixed slack. Consequently

`boxed: P(L1(G_p)>=g n) -> 1 for every fixed g<G_major,`

uniformly over the same H1--H2--H3 class and every `p >= (1+epsilon)/lambda(G)`. No endpoint attainment is claimed.

The additional cap `delta_major<=bP/16` also keeps the numerical receipt away from the trivial ceiling: the old tail-floor mechanism cannot account for the first `bP n` outside positions, so `G_coreavg<=1-bP`, and hence `G_major<1`.

Thus this run moves the complete metric beyond the **entire** incoming `G_coreavg` supremum, not merely beyond one finite-anchor approximation.

## 8. What the three methods did

- **#11 DUALIZE — success.** Rewriting the multi-anchor layer-cake formula as `integral phi(L_D)` on the sorted degree variable exposed that the old theorem retained only tail floors.
- **#24 FIND THE EXTREMAL OBJECT — success after identifying the obstruction.** The adversarial shape is to concentrate the newly recovered prefix degree mass on an infinitesimal high-degree spike. The spectral `L^2` budget prevents enough concentration to give the explicit `delta_0` above.
- **#3 PROVE SOMETHING STRONGER — success.** Instead of one order-statistic inequality per anchor, retain the full prefix-sum inequality `sum_{i<=bn} x_i >= c3 b t(b)n`; this is what creates a gain uniform over all finite old anchor families.

No finite checker was created: the new result is analytic and has no finite-enumeration core. Producing a checker here would violate the 90/10 policy rather than strengthen the theorem.

## 9. Remaining obstruction and next genuinely different route

H0002 is still **PARTIAL / SOURCE OPEN-LOOKING / ACTIVE**. The source asks for natural conditions in general, whereas R16 has proved one increasingly quantitative sufficient-condition theorem on the frozen H1--H2--H3 class.

The present majorization argument is no longer losing the first-order prefix information, but it still uses the crude global energy inequality `sum d_W(v)^2 <= lambda^2 |W|`.

A stronger next route would optimize the complete concave functional

`sum_v [1-exp(-Delta d_W(v)/lambda)]`

under **all** inherited prefix constraints and the spectral quadratic budget, rather than the one-threshold truncation at `M_*`. That is a genuine one-dimensional variational problem and may identify the exact extremal degree profile. If that optimization stops moving the envelope, the next route should be a nonuniform Perron-weight constraint on the reservoir, not another scalar padding identity.

The supported unchanged count is reset to **0** because the tracked complete envelope moved strictly.

## 10. Model / scheduler-control status

The limitation remains exactly the one recorded by the controlling repository policy and current root ledger. The exposed scheduler schema has fields for task title/prompt, schedule or relative start, timing mode and enablement, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt**. Therefore GPT-6/maximum is prompt text only here; actual runtime for this report is GPT-5.6 Sol with reasoning level UNVERIFIED.

The earlier P26 `You cannot modify this task` event was context/authorization specific. The current root ledger records a later successful P26 prompt update from an authorized context, while other contexts still recorded denied edits. Where a task still refuses modification, the compliant route is the owning authorized account/workspace or platform support; do not duplicate the task and do not bypass permissions.

```yaml
ledger_delta:
  track: R16
  canonical_target: H0002
  lane: HARD_OUTSIDE
  source: "Christoph--Morawski--Wigderson, arXiv:2608.19145v1, Question 5.1"
  nominal_scheduler_target: "Beck--Fiala 1981 discrepancy conjecture"
  nominal_metric_status: "KNOWN current-preprint baseline: B(t,n)<3 sqrt(2 pi t) for all integer t>=1 and all n, per Guo--Fang--Lu v1; Bansal--Jiang v2 alone only directly covers t>=log^2 n"
  active_metric_before: "G_coreavg"
  active_metric_after: "G_major = G_coreavg + delta_major"
  delta_definition: "delta_major=min{bP/16, (Delta*D_*/64)*exp(-4*Delta*aP/D_*)}, D_*=bP*t0>0"
  movement: "STRICT: G_major > G_coreavg"
  status_before: "PARTIAL / SOURCE OPEN-LOOKING / ACTIVE"
  status_after: "PARTIAL / SOURCE OPEN-LOOKING / ACTIVE"
  supported_unchanged_count: 0
  methods: [11, 24, 3]
  finite_checker: "none; analytic theorem"
  next_obligation: "solve the full prefix-plus-L2 concave variational problem, or add nonuniform Perron-weight constraints if that variational route saturates"
  shared_root_edits: false
  scheduler_edits: false
```
