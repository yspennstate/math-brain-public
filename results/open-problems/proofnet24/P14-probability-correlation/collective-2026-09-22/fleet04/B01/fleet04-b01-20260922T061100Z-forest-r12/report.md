# FOREST / fleet04 B01 — loopless-multigraph Simpson closure and all-edge rank budget

**Run:** `fleet04-b01-20260922T061100Z-forest-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-MULTIGRAPH-SIMPSON-CLOSURE-v1`  
**Parent target:** **OPEN**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and exact inherited state

The source target is the Grimmett--Winkler unit law on **all unrooted forests of every finite simple graph**, with the empty forest, disconnected forests and every forest size retained. No rooted, fixed-size, spanning-tree or arbitrary-weight law is substituted for that statement.

Fresh owner controls were read from `yspennstate/math-research-brain` and remained on revision `2026-09-22.2`, directive `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; installation/benchmark work remains stopped for B01.

Latest complete lead consumed: fleet01/B01 run `20260922T050946Z-b01-forest-auto11`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`. Its source-secure inputs used below are:

1. the rank-homogeneous complete-log-concavity row budget for the graphic-matroid independent-set law; and
2. the exact total-covariance/Simpson identity, which the lead could apply only when the conditioning edge is triangle-free because it chose an edge-minimal **simple** counterexample.

Assigned partner consumed: fleet01/B02 run `20260922T032220Z-fleet01-B02-forest11`, report blob `404c46990062a1d16228a6ce4c3d28eedb1da06e`. I apply its warning that contraction-created parallel classes must not be silently replaced by unit simple edges. This run keeps every parallel member as a distinct labelled unit edge.

Named OTHER-account result actually applied: fleet02/B01 run `B01-20260922T0529Z-forest-r15`, candidate `FOREST-2CUT-INFLUENCE-BUDGET-v1`. Its source-valid move is to enlarge the induction universe to finite **loopless multigraphs**: a simple source failure is also a failure in that larger class, hence an edge-minimal loopless-multigraph counterexample exists. Its contraction children may have parallel classes, but those classes are retained exactly rather than aggregated into an unsupported weighted simple edge.

I also retain my previous exact separator theorem `FOREST-Q-3CONN-EXACT-v1`: unit FOREST on all finite simple graphs is equivalent to positive-rational weighted FOREST on all finite simple graphs and to positive-rational weighted FOREST on 3-connected simple graphs (with the K3 base), via exact rational two-terminal unitization and the complete same-bridge/cross-bridge two-cut formulas. That theorem remains the correct source-secure class-level three-connected reduction; it does **not** say an edge-minimal unit simple counterexample is itself 3-connected.

## 2. New mechanism: choose the minimal witness in the loopless-multigraph class

Assume the simple source conjecture fails. Because every simple graph is a loopless multigraph, choose a counterexample `G` with the minimum number `m` of labelled edges among **all finite loopless multigraphs**, and choose a violating pair `e,f`. Let `X_h` be the inclusion indicator of edge `h` under the uniform law on all graphic-matroid independent sets (forests) of `G`.

Write

`C_ij = Cov(X_i,X_j)`, `V_i = Var(X_i)`, `rho_ij=C_ij/sqrt(V_i V_j)`.

Then `C_ef>0`; put `a=rho_ef>0`.

Every present nonloop edge satisfies `0<p_h=P(X_h=1)<=1/2`: removing `h` is an injection from forests containing `h` into forests omitting it. Also `0<V_h<1/4` is nondegenerate because the empty forest and singleton `{h}` both occur.

### Lemma 2.1 — both conditioning children are smaller source-exact multigraph instances

Fix any third edge `g`.

* `X_g=0` is exactly the uniform forest law of `G\g`, which has fewer edges.
* `X_g=1`, after deleting the compulsory `g`, is exactly the uniform forest law of the graphic contraction `G/g`. Any edge parallel to `g` becomes a loop and is therefore never selectable in this conditional law; delete those loops. Every other parallel class is retained with its labelled unit members. The resulting loopless multigraph has fewer edges than `G`.

If one of the marked edges becomes a loop in the contraction child (equivalently it was parallel to `g`), its conditional indicator is identically zero and the corresponding conditional covariance is zero. Otherwise edge-minimality of `G` applies to the smaller loopless multigraph.

Therefore, for **every** third edge `g`, not merely triangle-free ones,

`Cov(X_e,X_f | X_g=0) <= 0`,

`Cov(X_e,X_f | X_g=1) <= 0`.                                    (2.1)

This is precisely where the partner's parallel-class warning is paid: no simplification to an unweighted simple graph occurs.

## 3. New theorem A — the Simpson inequality holds for every conditioner

For a Bernoulli conditioner, the law of total covariance gives the exact identity

`C_ef = (1-p_g) C_ef|0 + p_g C_ef|1 + C_eg C_fg / V_g`.          (3.1)

Combining (2.1) with `C_ef>0` yields

`C_eg C_fg / V_g >= C_ef > 0`.                                  (3.2)

After dividing by `sqrt(V_e V_f)`,

`boxed: rho_eg rho_fg >= rho_ef = a > 0`                         (3.3)

for **every** `g notin {e,f}`.

Thus the lead's triangle-free Simpson gate extends to the whole edge set once the minimality universe is chosen correctly. The source-generated STAR-2 contraction debt disappears from this induction: a triangle contraction is simply a smaller labelled unit multigraph, not a weighted simple graph requiring a new theorem.

This does not assert that every arbitrary `{1,2}`-weighted simple graph is Rayleigh. It is a narrower and fully paid statement about contraction children of the chosen minimal multigraph witness.

## 4. New theorem B — positive covariance pairs form a matching

The same argument applies to any positively correlated pair in `G`. Suppose three distinct edges `i,j,k` had

`rho_ij=x>0`, `rho_ik=y>0`, `rho_jk=z>0`.

Applying (3.3) cyclically gives

`x <= yz`, `y <= xz`, `z <= xy`.

Multiplication gives `xyz <= (xyz)^2`, hence `xyz>=1`. But for distinct edge indicators under the uniform forest law, `|rho|<1`: singleton forests separate the indicators, while a parallel pair cannot co-occur and in particular cannot be positively perfectly correlated. Contradiction.

Moreover, if `C_ij>0` and `C_jk>0`, applying (3.3) to the positive pair `(i,j)` with conditioner `k` forces `C_ik>0`, which would create the forbidden positive triangle. Therefore the graph whose vertices are physical edges and whose edges are positive-covariance pairs is a **matching**.

In particular, for the fixed violating pair `e,f`, every third edge satisfies

`rho_eg<0`, `rho_fg<0`, and `rho_eg rho_fg>=a`.                   (4.1)

This is the all-edge version of the lead's triangle-free matching structure.

## 5. New theorem C — all-edge rank-homogeneous budget

Let `R` be the graphic-matroid rank, `K=|F|`, `mu=E K`, and `c_h=Cov(X_h,K)`. The lead's rank-homogeneous complete-log-concavity inequality applies to every matroid, hence also to this loopless graphic multigraph. For each edge `e`,

`T_e + sum_{h!=e} (1-p_h) rho_eh^2 <= p_e`,                     (5.1)

where

`T_e = c_e^2 / ((R-mu) p_e(1-p_e)) >= 0`.

(The denominator is positive in a nontrivial counterexample because nonbasis independent sets, including the empty set, have positive mass.)

Add (5.1) for `e` and `f`. The mutual term contributes

`(2-p_e-p_f) a^2`.

For every third edge `g`, (4.1) and AM--GM give

`rho_eg^2 + rho_fg^2 >= 2 rho_eg rho_fg >= 2a`,

and `1-p_g>=1/2`. Therefore each third edge contributes at least `a`. Since `p_e+p_f<=1` and `2-p_e-p_f>=1`,

`boxed: T_e + T_f + a^2 + (m-2)a <= 1`.                         (5.2)

Consequently

`boxed: a <= [sqrt((m-2)^2 + 4(1-T_e-T_f))-(m-2)]/2`

`       <= [sqrt((m-2)^2+4)-(m-2)]/2`.                           (5.3)

This strictly strengthens the lead's source-safe bound

`T_e+T_f+a^2+s a<=1`

where `s` counted only triangle-free conditioning edges. Here **all `m-2` third edges** contribute, because contraction parallelism has been absorbed exactly into the loopless-multigraph induction universe.

## 6. Connection to the separator / three-connected programme

There are now two source-secure structural reductions, serving different purposes.

1. `FOREST-Q-3CONN-EXACT-v1` pays every disconnected, cut-vertex and two-cut case at the class level, including induced virtual parameters and an original singleton separator edge, and confines the universal problem exactly to positive-rational weighted 3-connected simple cores.
2. `FOREST-MULTIGRAPH-SIMPSON-CLOSURE-v1` pays the triangle-contraction obstruction in the unit minimal-counterexample route. It gives an all-edge sign pattern and the quantitative budget (5.2) without any fixed-graph Cocks implication and without collapsing parallel classes.

The first remaining implication is therefore sharper than the lead's STAR-2 statement: **show that no edge-minimal loopless-multigraph counterexample can satisfy (4.1)--(5.2), or transfer those constraints to the rational-weight 3-connected core supplied by the exact separator theorem.** This is still unpaid. Equation (5.2) alone is not a contradiction because a positive correlation may in principle be very small.

The named fleet03/B03 cubic-vertex identity is compatible with this localization: for a simple unit 3-connected graph and a degree-three vertex `v`, if `e1,e2` are two incident edges then

`Delta(e1,e2)=4 B12 T + (B13+C)(B23+C) >=0`.

Thus any simple cubic-core violation must use vertex-disjoint marked edges. I use that only in its proved simple/unit scope; I do not extend it across parallel classes or arbitrary rational star weights.

## 7. Compact conditional end-to-end chain

A source failure would give:

1. by exact rational unitization and two-cut gluing, a positive-rational weighted 3-connected simple counterexample (`FOREST-Q-3CONN-EXACT-v1`);
2. independently, an edge-minimal unit loopless-multigraph counterexample `G`;
3. for every violating pair in `G`, all third-edge conditioning children are smaller exact unit multigraph instances, so (3.3) holds for **every** conditioner;
4. positive correlations form a matching and every third edge is negative to both marked edges;
5. complete log concavity forces the global all-edge budget (5.2).

The remaining target-level problem is to make steps 1 and 5 meet strongly enough to rule out the 3-connected core, or else construct a genuine graph realizing the full obstruction. No such final implication is claimed here.

## 8. Failure preservation and source discipline

* The fixed-graph implication `unit-good G => arbitrary-weight Rayleigh on the same G` remains fail-closed and is not used.
* The assigned partner's internal full candidate remains validation-sensitive because it uses that Cocks bridge; its reversible complete-graph counting and deletion-only algebra are preserved, but I do not promote the parent conjecture.
* The earlier claim that an edge-minimal **simple unit** counterexample must itself be 3-connected remains withdrawn. Exact rational unitization can enlarge the graph.
* No parallel class is aggregated into a unit edge. Labelled parallel unit edges remain distinct throughout contraction.
* No finite census or checker is counted as evidence in this run; the new step is algebraic/probabilistic.
* The parent FOREST conjecture remains **OPEN**.

## 9. Sources / exact peer versions

* Lead: fleet01/B01 `20260922T050946Z-b01-forest-auto11`, `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`.
* Assigned partner: fleet01/B02 `20260922T032220Z-fleet01-B02-forest11`, report blob `404c46990062a1d16228a6ce4c3d28eedb1da06e`.
* Named other-account mechanism: fleet02/B01 `B01-20260922T0529Z-forest-r15`, `FOREST-2CUT-INFLUENCE-BUDGET-v1`.
* Named other-account cubic restriction: fleet03/B03 `20260922T055815Z-fleet03-B03-forest-r12`.
* Prior own separator result: fleet04/B01 `fleet04-b01-20260922T051009Z-forest-r12`, `FOREST-Q-3CONN-EXACT-v1`.
* Complete-log-concavity input is inherited exactly from the lead's rank-homogeneous matroid independent-set argument; no stronger entrywise-Rayleigh conclusion is inferred from log concavity.

Scoped privacy/provenance review: this report contains only mathematical formulas, public-source/peer version identifiers, owner-control revision, and sanitized logical account/slot labels. It contains no credentials, scheduler identifiers, machine paths, benchmark gold, email/Drive material, unrelated private content, or public-release action.
