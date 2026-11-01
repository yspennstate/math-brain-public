# FOREST / fleet01 B20 — fixed-graph closure fails; exact weighted-complete bridge and sharp Simpson interpolation

**Run:** `20260922T022012Z-b20-forest-r11`  
**Campaign:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** Grimmett–Winkler pairwise negative correlation for the uniform law on all unrooted forests of every finite simple graph.  
**Outcome:** **CANDIDATE_REFUTED** for the lead's global closure as written. The parent FOREST conjecture remains **OPEN**.  
**New exact step:** `FOREST-QUADRATIC-SIMPSON-BRIDGE-20260922`.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

The word `CANDIDATE_REFUTED` here is deliberately narrow: it means that the current lead's proposed *proof chain* contains a source-invalid fixed-graph implication. It is **not** a counterexample to the FOREST conjecture, and it does **not** retract the lead's independently derived unit-weight theorem on complete graphs.

## 1. Source-exact target and dependencies actually consumed

For a finite simple graph `G`, let

`P_G(y)=sum_{F acyclic} prod_{h in F} y_h`.

At unit weights this is the number-generating polynomial of **all** forests: all sizes, disconnected forests, and the empty forest are included. For distinct edges `e,f`, write, in derivative convention,

`R_ef(y) = (partial_e P_G)(partial_f P_G) - P_G (partial_ef P_G)`.

At positive weights the sign of this is the same as the Semple--Welsh inclusion-weight gap because the latter differs by the positive factor `y_e y_f`. The source target is

`R_ef(1) >= 0`

for every finite simple `G` and every distinct pair `e,f`.

This run consumed the following exact versions.

1. **Campaign lead, fleet01/B01.**  
   `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet01/B01/20260922T012234Z-fleet01-B01-forest-r11/hermite_complete_graph_reduction_report.md`  
   blob `e11be369a70e59449ea744da6f1e32040889c216`, candidate `FOREST-KN-HERMITE-REDUCTION-v1`.

   Its complete-graph calculation proves, by an exact labelled-forest/Hermite argument, the unit inequality for every `K_n`. The proposed global closure then uses the asserted fixed-graph step

   `unit FOREST pNC on K_n -> M(K_n) independence correlated for all positive weights`

   followed by weighted minor closure.

2. **Assigned OTHER-account partner, fleet04/B03.**  
   `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet04/B03/20260922T001033Z-B03-r43/REPORT.md`  
   blob `9b0e6f246b82be1647a85af62269035b538fd655`, theorem `FOREST-3CONN-FULL-SUPPORT-20260922`.

   It proves full support of the reconnection cells in a 3-connected obstruction and gives an exact abstract three-edge graphic-matroid mixture with
   `(Z,Ze,Zf,Zg,Zef,Zeg,Zfg,Zefg)=(31,11,11,7,4,1,1,0)`,
   for which `Delta(e,f)=-3` but `Delta(e,g)=Delta(f,g)=46>0`. It therefore rules out closing the conjecture from local sign/minor/full-support constraints alone.

3. **Later OTHER-account source correction, fleet02/B02.**  
   `proofnet24/P14-probability-correlation/collective-2026-09-22/fleet02/B02/B02-20260922T013646Z-forest-r12/cocks_scope_correction.md`  
   blob `733d840093ca109d38f4e336d228ae1ddedf77c0`.

   This later result directly attacks the fixed-graph Cocks scope used by the lead and classifies the global closure `CANDIDATE_REFUTED_AS_WRITTEN`.

4. **Primary source check.**  
   Semple--Welsh, *Negative Correlation in Graphs and Matroids*, Combin. Probab. Comput. 17 (2008), DOI `10.1017/S0963548307008978`. In the accessible source:
   - independence correlation is defined by the inequality for **all positive real weightings**;
   - Proposition 3.5 proves that this weighted class is minor-closed;
   - immediately afterward the authors explicitly say that they do **not** know whether the class of graphs satisfying the unit Conjecture 1.1 is minor-closed;
   - they only infer the conjecture for graph minors after already knowing that `M(G)` is independence correlated.

   Cocks, *Correlated Matroids*, Combin. Probab. Comput. 17 (2008), DOI `10.1017/S0963548308009152`, states a global equivalence between the Grimmett--Winkler conjecture and correlated graphic-matroid statements. The accessible class-level parallel-copy argument does not provide the fixed-graph implication used by the lead.

The source check is decisive: the weighted minor theorem begins **after** weighted independence correlation has been established. It cannot be used to upgrade a single unit point to all weights.

## 2. The lead's complete-graph theorem survives; its global bridge does not

The following part of `FOREST-KN-HERMITE-REDUCTION-v1` remains a valid and substantial subtheorem:

> For every `n` and every distinct pair of edges of `K_n`, the uniform all-forest law at unit edge weights is pairwise negatively correlated.

The report derives exact formulas from

`R=z exp(R)`, `T=R-R^2/2`, `F=exp(T)`, `A=exp(R)`,

reduces the harder disjoint-edge orbit to a one-variable Hermite inequality, and proves it for every `n`, with independent exact small-order regression.

What fails is the inference

`unit point y=1 on K_n => all y>0 on K_n`.

The source definition of independence correlation is precisely the all-positive-weight assertion, so that inference would already supply an enormous amount of the missing theorem.

A particularly transparent sufficient replacement is:

> **Weighted-complete bridge.** For every `n`, every positive edge-weight vector `y` on `K_n`, and every distinct `e,f`,
> `R_ef^{K_n}(y)>=0`.

If this bridge were proved, every finite simple graph `G` would follow **directly by a zero-weight limit**, without even needing the minor theorem: embed `G` in `K_n`, put weight `1` on edges of `G` and weight `epsilon>0` on missing edges, apply the weighted-complete bridge, and send `epsilon -> 0`. Polynomial continuity gives the unit gap of `G`.

Thus the actual missing bridge is not a routine source-formality. It contains the original sparse-graph problem as a boundary limit. The unit complete-graph theorem is one highly symmetric interior point of this much larger region.

## 3. Exact coordinate interpolation: the first unpaid weighted obstruction

The source-correct way to see what must be controlled when an edge activity varies is multiaffinity.

Let `M` be a graphic matroid (or any matroid independent-set polynomial), fix distinct `e,f,g`, freeze every activity except `y_g=t>0`, and write

`P(t)=A+tB`,

where `A=P_{M\g}` and `B=P_{M/g}` (loops are trivial and may be deleted). Likewise,

`P_e=Ae+tBe`,  
`P_f=Af+tBf`,  
`P_ef=Aef+tBef`.

Define the two endpoint Rayleigh gaps

`d0 = Ae*Af - A*Aef`,  
`d1 = Be*Bf - B*Bef`,

the mixed coefficient

`m = Ae*Bf + Af*Be - Aef*B - Bef*A`,

and the two cross gaps

`ce = Ae*B - A*Be = R_eg`,  
`cf = Af*B - A*Bf = R_fg`.

Then exact expansion gives

`R_ef(t) = d0 + m t + d1 t^2`.                                      (3.1)

The non-obvious but elementary identity tying the mixed coefficient to the simultaneous third-edge correlations is

`A B m = B^2 d0 + A^2 d1 - ce cf`.                                 (3.2)

This was symbolically checked from the definitions; the checker and captured output are archived with this report.

### Theorem `FOREST-QUADRATIC-SIMPSON-BRIDGE-20260922`

Assume `A,B>0` and `d0,d1>=0`. Then

`R_ef(t)>=0 for every t>0`

if and only if

`ce cf <= ( B sqrt(d0) + A sqrt(d1) )^2`.                            (3.3)

#### Proof

If `m>=0`, (3.1) is nonnegative for every `t>0`. If `m<0`, its unique interior minimum is at `t=-m/(2d1)` when `d1>0`; the degenerate `d1=0` case is included by continuity. Therefore (3.1) is nonnegative on `(0,infinity)` exactly when

`m >= -2 sqrt(d0 d1)`.

Substitute (3.2) and multiply by `AB>0`:

`B^2 d0 + A^2 d1 - ce cf >= -2AB sqrt(d0 d1)`,

which is exactly (3.3). QED.

In normalized stratum notation

`p_e^0=Ae/A`, `p_f^0=Af/A`,  
`p_e^1=Be/B`, `p_f^1=Bf/B`,  
`r0=d0/A^2`, `r1=d1/B^2`,

the same sharp criterion is

`(p_e^0-p_e^1)(p_f^0-p_f^1) <= (sqrt(r0)+sqrt(r1))^2`.              (3.4)

So the missing phenomenon is a precise Simpson-reversal barrier: conditioning on `g` is allowed to move both marked-edge marginals in the same direction, but not by more than the residual Rayleigh slack in the two strata can pay for.

### Unit violating state

At the actual unit point `t=1`, if both minor strata satisfy `d0,d1>=0` but the parent violates the source inequality, then

`d0+m+d1<0`.

Combining this with (3.2) yields the stronger necessary inequality

`ce cf > (A+B)(B d0 + A d1)`.                                      (3.5)

Because

`(A+B)(B d0+A d1) - (B sqrt(d0)+A sqrt(d1))^2
 = A B (sqrt(d0)-sqrt(d1))^2 >= 0`,

a unit counterexample must cross the all-activity barrier (3.3) with quantitative room.

This is a precise refinement of the sign-cluster statement: `ce` and `cf` must not merely have the same sign; their product must beat an explicit combination of the deletion and contraction slack.

## 4. Applying the partner's exact OTHER-account witness

The fleet04/B03 local-cone witness has, in the `g=0` stratum,

`A=24`, `Ae=Af=10`, `Aef=4`, so `d0=4`;

and in the `g=1` stratum,

`B=7`, `Be=Bf=1`, `Bef=0`, so `d1=1`.

Its cross gaps are

`ce=cf=10*7-24*1=46`.

Therefore

`ce*cf = 2116`,

whereas the sharp all-activity threshold is

`(7*sqrt(4)+24*sqrt(1))^2 = 38^2 = 1444`.

The stronger unit-violation threshold in (3.5) is

`(24+7)(7*4+24*1) = 31*52 = 1612`.

The witness has

`2116 > 1612 > 1444`.

Hence the partner's abstract local graphic-matroid cone violates **exactly** the quantitative barrier isolated in this run. This is a useful application, not merely a citation: it proves that neither full support nor simultaneous third-edge sign coherence can force (3.3). A successful proof has to use a graph-global compatibility law absent from that cone.

This is consistent with the prior B20 theorem `FOREST-PATH-CUT-FLUX-20260922`, which supplies exact graph-global path/cut conservation identities. The remaining problem is to make those global conservation laws pay the sharp Simpson debt rather than only give unscaled capacity lower bounds.

## 5. Corrected compact end-to-end argument

The shortest source-secure state after this run is now:

1. **Unit complete graphs:** fleet01/B01 proves the source inequality at `y=1` for every `K_n` by exact Hermite analysis.
2. **Global target:** every arbitrary simple graph is a zero-weight boundary specialization of a positively weighted complete graph.
3. Therefore a sufficient global bridge is all-positive-weight independence correlation of every `M(K_n)`.
4. The fixed-graph Cocks implication used by the lead does **not** presently supply step 3; Semple--Welsh distinguish unit graph pNC from weighted independence correlation and explicitly do not know unit minor closure at that stage.
5. Coordinatewise, the precise obstruction to preserving a Rayleigh gap while varying one activity is the sharp inequality (3.3).
6. The assigned fleet04/B03 witness violates (3.3), so local three-edge matroid membership/sign/full-support data cannot prove it.
7. **First unpaid universal mathematical implication:** derive a genuinely graph-global mechanism—most plausibly using path/cut flux, separator conservation, or an equivalent global flow—that forces the Simpson payment needed for the actual simple-graph strata. A proof that only establishes pointwise local cone inequalities is now formally ruled out.

The weighted-complete bridge should be treated as a **sufficient restatement containing the original problem at its boundary**, not as progress by itself. The new useful object is the sharp scalar debt (3.3)/(3.5), because it gives the global switching/flow work an exact quantity to pay.

## 6. Exact computation used in this run

The only computation used to support a mathematical identity in this report is symbolic expansion of (3.1)--(3.2).

Checker:
`quadratic_bridge_check.py`

SHA-256:
`3bd4f62b982dbb830ff5e8934b4db52f3d7b66285e952ac1eaca327190587974`

Captured output:
`quadratic_bridge_check.out`

SHA-256:
`ba14ecf8eda66a9d5a7a60d3da2f4bc77f6e5ac3dfb416c489f5d873eabe8188`

Exact output:

```text
DELTA_COEFFS [-B*Bef + Be*Bf, -A*Bef + Ae*Bf - Aef*B + Af*Be, -A*Aef + Ae*Af]
DELTA_MINUS_QUADRATIC 0
AB_IDENTITY 0
PASS
```

The theorem itself is proved algebraically above; the script is a regression check, not a substitute for proof.

## 7. Classification and handoff

**Run classification:** `CANDIDATE_REFUTED`.

- Refuted object: the lead's global closure **as written**, specifically the unsupported fixed-graph upgrade from one unit weighting on `K_n` to weighted independence correlation of `M(K_n)`.
- Not refuted: the FOREST conjecture.
- Not refuted: the lead's unit complete-graph Hermite theorem.
- New exact theorem: `FOREST-QUADRATIC-SIMPSON-BRIDGE-20260922`.
- Applied other-account result: fleet04/B03's exact local-cone witness, which violates the new barrier numerically and therefore proves the need for graph-global information.
- Later source correction independently consumed: fleet02/B02, blob `733d840093ca109d38f4e336d228ae1ddedf77c0`.

**Next FOREST worker:** combine the exact path-cut flux identities from the previous B20 run with (3.5). In a minimal unit counterexample, for every third edge `g`, minor minimality gives `d0,d1>=0`; the parent violation forces the explicit excess

`R_eg R_fg > (A+B)(B d0+A d1)`.

The next genuinely useful theorem would sum or transport these third-edge debts through one common graph without a graph-size factor. The fleet04/B03 witness should remain a mandatory regression: any proposed local-only inequality that also holds for that witness cannot be the missing universal theorem.

No full-proof, novelty, priority, publication, or counterexample claim is made. No benchmark material, credentials, unrelated private data, email, Drive object, remote workflow, permission change, public repository, or cross-account native action was used.
