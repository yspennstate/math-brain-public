Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# NM13-04 / T07 — split-5 one-port-field Rayleigh theorem and PF macro-network extension

Status: **PARTIAL on the parent problem / CANDIDATE_FULL for the restricted all-parameter theorems below, pending later independent review.** The arbitrary-finite-graph Grimmett–Winkler conjecture remains OPEN. No source-valid counterexample was found.

Repository / branch: private `yspennstate/math-open-problems` / `master`  
Assigned root: `proofnet24/NM13-04/progress-forest/`  
Companion: NM13-08, `proofnet24/NM13-08/progress-forest-structure/`

## 0. Short predecessor handoff and why this run changes method

The preceding NM13-04 runs proved strict unit-weight pairwise negative edge correlation for

\[
K_3\vee\overline{K_n}
\quad\text{and then}\quad
K_4\vee\overline{K_n}
\qquad(n\ge1)
\]

by finite terminal-partition transfer. The second proof used all `B_4=15` partitions and `M=5I+N`, `N^4=0`. Those are genuine infinite non-series-parallel families, but they do not move the source-level all-graph metric.

The newest companion report, `proofnet24/NM13-08/progress-forest-structure/runs/2026-09-20/2026-09-20T01-39-00Z__portfield-sp-macronetwork-report.md`, then proved a materially different structural theorem: **PF-Rayleigh** (all real edges frozen at 1, one virtual terminal-port edge allowed arbitrary weight `s>=0`) is closed under terminal series and parallel composition. It also proved that port-deleted `K_4∨\overline{K_n}` atoms are PF-Rayleigh.

Because a third consecutive unit-only fixed-r transfer would be too close to the same route, this run does **not** merely prove the unit theorem for `K_5∨\overline{K_n}`. It upgrades to a one-port-field deletion/contraction sign theorem for every `s>=0`, encounters three genuinely non-coefficientwise Rayleigh quadratics, and closes them by an exact discriminant argument. This new PF atom family then plugs directly into NM13-08's macro-decomposition theorem.

`POSTED.md` was respected; the T07 parent and these split/PF extensions are not treated here as posted or settled source-level claims.

## 1. Parent problem before/after, separately from mechanism gain

For a finite simple graph `G=(V,E)`, let

\[
I_G(\mathbf y)=\sum_{F\subseteq E:\,F\text{ acyclic}}\prod_{e\in F}y_e,
\qquad
\Delta_G(e,f)=I_eI_f-I_GI_{ef}.
\]

At unit weights, `Delta_G(e,f)>=0` is exactly pairwise negative edge correlation for the uniform measure on **all** spanning forests.

**Parent source status:** `OPEN -> OPEN`.  
**Largest completely certified all-graph vertex order in repository continuity:** `9 -> 9`.  
**Equivalent source-valid counterexample lower bound:** `>=10 -> >=10`.

Finite/restricted family results do not move that metric.

**Mechanism scope before this run:** unit p-NC for all `K_4∨\overline{K_n}` (NM13-04), and PF-Rayleigh / series-parallel macro-closure for port-deleted `K_4∨\overline{K_n}` atoms (NM13-08).

**Mechanism scope after this run:** PF-Rayleigh for the new port-deleted `K_5∨\overline{K_n}` atom family for every `n>=1`, hence strict unit p-NC for every `K_5∨\overline{K_n}`, plus arbitrary finite NM13-08 series/parallel macro-networks whose leaves may be chosen from the split-4 and split-5 PF atom families.

For `n>=2`, `K_5∨\overline{K_n}` is noncomplete and 5-connected. Every member contains `K_6`, so this is far outside the series-parallel class.

## 2. Recovered P14 proof baseline and failed generic routes

Only the dependencies needed for this run were recovered.

Preserved successful P14 facts:

1. Grimmett–Winkler plus the repository dense-nine certificate cover every simple graph through nine vertices at unit forest weights.
2. Block/direct-sum factorization reduces a vertex-minimal counterexample to 2-connected.
3. The preserved two-separator transfer plus fixed-graph unit-to-positive-weight implication reduces a vertex-minimal counterexample further to 3-connected.
4. One-edge-field quadratics are exact and useful local invariants.

Preserved failed/insufficient routes:

1. partial ten-vertex enumeration does not move the source metric;
2. the generic degree-three star/mesh elimination leaves an old-edge/old-edge mixed three-terminal polarization;
3. that mixed term is not universally nonnegative;
4. the proposed reverse-Cauchy sufficient inequality was exactly refuted on a physical six-vertex graph even while its source Rayleigh gap stayed positive;
5. Lorentzian/complete-log-concavity does not by itself force the required entrywise Hessian sign;
6. naive real-stability perturbation and the unverified Gårding shortcut remain invalid as universal replacements.

The present theorem does not revive those failed universal claims. It succeeds because the split family has a finite partition response **and** the one-port field exposes an exact quadratic whose three exceptional mixed terms can be controlled by discriminant rather than by a false universal sign assumption.

## 3. Current exact literature scope checked on 20 September 2026

A bounded public-source check recovered the following distinctions.

* Grimmett–Winkler, `math/0302185`, Random Structures & Algorithms 24 (2004), 444–460, is the uniform-all-forests problem. It reports numerical verification for every graph through eight vertices and nine-vertex graphs with at most eighteen edges; spanning-tree negative association is explicitly a different already-known theorem.
* Erickson, `arXiv:1008.3660`, proves the stronger weighted independent-set-Rayleigh statement for series-parallel graphs by sums of squares.
* Huang, `arXiv:2311.00965`, treats arboreal-gas negative correlation in restricted settings and still describes the general problem as open.
* Bado, DOI `10.1016/j.spl.2026.110960`, proves strict p-NC for every wheel graph by a `2 x 2` transfer method. Wheels are 3-connected non-series-parallel graphs, but they are not complete split graphs.
* Tang–Zhang, `arXiv:2603.10738` (11 March 2026), proves p-NC for specified complete-graph spanning-subgraph ensembles, including forests with a **fixed** number of components for fixed `k` and sufficiently large `n`; this does not equal the all-component uniform-forest law on arbitrary graphs.

Fresh bounded searches for `uniform forest + complete split graph`, `K_5 join independent set + negative correlation`, and `Rayleigh difference + split graph forest` did not surface the theorem below. That is negative evidence only. **Novelty/priority remains UNVERIFIED.**

## 4. New one-port-field theorem

Let

\[
H_n=K_5\vee\overline{K_n},\qquad n\ge1,
\]

with clique terminals `C={0,1,2,3,4}`. Give the distinguished clique edge

\[
g=01
\]

weight `s>=0`; every other edge has weight `1`. Write this weighted graph as `H_n(s)`. Let `Q_n=H_n-g`, with terminals `0,1`.

### Theorem `T07-SPLIT5-PORTFIELD-03`

For every `n>=1`, every `s>=0`, and every two distinct edges `e,f` in the port-completed graph,

\[
\boxed{\Delta_{H_n(s)}(e,f)>0.}
\]

Consequently `Q_n` is PF-Rayleigh in the sense of NM13-08. In particular, at `s=1`, every two distinct edges of `K_5∨\overline{K_n}` are strictly negatively correlated under the uniform measure on all forests.

### 4.1 Fifty-two-state transfer and deletion/contraction field

Process the independent-side vertices one at a time and retain only the connectivity partition `pi` induced on the five clique terminals. There are `B_5=52` states.

If a new independent vertex is attached to `A subseteq C`, the extension is acyclic iff `A` meets every block of `pi` in at most one terminal. Empty attachment and the five singleton attachments leave `pi` unchanged. Every other legal attachment strictly coarsens the partition. Thus

\[
M=6I+N,
\qquad N^5=0,
\qquad N^4\ne0.
\tag{4.1}
\]

Therefore

\[
M^n=\sum_{j=0}^4\binom nj6^{n-j}N^j.
\tag{4.2}
\]

The `K_5` initial forest vector has the exact deletion/contraction form

\[
u(s)=u^{(0)}+s\,u^{(1)},
\tag{4.3}
\]

where `u^(0)` counts clique forests omitting `g` and `u^(1)` counts clique forests containing `g` with its port weight removed. Every clique-marked initial vector is likewise linear in `s`; marked-spoke transfer operators do not depend on `s`.

Hence each of `I`, `I_e`, `I_f`, `I_{ef}` is `6^n` times a polynomial in `n` of degree at most four whose coefficients are linear in `s`. It follows that every Rayleigh gap has the exact shape

\[
\boxed{
\Delta_{H_n(s)}(e,f)=36^n\bigl(A_{ef}(n)+B_{ef}(n)s+C_{ef}(n)s^2\bigr),
}
\tag{4.4}
\]

with `deg A,deg B,deg C <= 8`.

This degree bound is what turns the exact interpolation in the attached checker into an all-`n` certificate rather than finite coverage: nine exact values determine each coefficient polynomial, and the checker verifies a tenth value independently.

### 4.2 Exact 25-orbit classification

The stabilizer of the port edge has symmetry `S_2 x S_3 x S_n`: swap `0,1`, permute `2,3,4`, and permute the independent vertices.

Use the following types:

* `g`: the port edge `01`;
* `A`: a clique edge joining a port endpoint to one of `2,3,4`;
* `B`: a clique edge inside `{2,3,4}`;
* `P`: a spoke to a port endpoint;
* `Q`: a spoke to one of `2,3,4`;
* `ssR`: two spokes on the same independent vertex;
* `ssD`: two spokes on distinct independent vertices.

For `n>=3` there are exactly 25 unordered edge-pair orbits. The checker constructs the full 72-element stabilizer for `n=3`, computes every orbit of the 25-edge graph, and proves that the 25 listed representatives are distinct and exhaustive. For `n=1,2`, the absent distinct-right-vertex orbits are simply omitted.

### 4.3 Twenty-two coefficientwise-positive orbit quadratics

For 22 of the 25 orbit types, the exact power-basis coefficients of each of `A(n),B(n),C(n)` in (4.4) are nonnegative, and `A(n)>0` on the admissible integer range. Therefore

\[
A(n)+B(n)s+C(n)s^2>0
\qquad(n\ge1,\ s\ge0)
\]

immediately for those orbits. Port-edge pairs have `B=C=0` and positive `A`.

The complete exact coefficient table is archived in

`2026-09-20T02-18-30Z__split5_portfield_checker.out`.

### 4.4 The three genuinely non-coefficientwise orbits

Exactly three orbit quadratics are not coefficientwise nonnegative in `s`. They are the reason this run is not just another copy of the split-4 unit proof.

#### (i) Two disjoint `A` clique edges: `e=02`, `f=13`

Writing `Delta/36^n=A+Bs+Cs^2`,

\[
A=\frac{25n^5+1556n^4+30365n^3+265702n^2+1091664n+1726272}{11664},
\]

\[
B=-\frac{55n^4+1086n^3+7121n^2+16362n+7776}{3888},
\]

\[
C=\frac{25n^4+738n^3+8321n^2+42468n+82944}{1296}.
\]

Both `A,C` are positive, while

\[
4AC-B^2=\frac{1}{15116544}
\bigl(2500n^9+226375n^8+8342452n^7+170281678n^6
\]
\[
{}+2159535964n^5+17826149167n^4+96390690828n^3
+330675470172n^2+655178730624n+572675152896\bigr)>0.
\tag{4.5}
\]

Thus the quadratic has negative discriminant and is positive for every real `s`.

#### (ii) An `A` clique edge and a spoke to the other port endpoint: `e=02`, `f=x1`

\[
A=\frac{625n^6+25875n^5+460123n^4+4519209n^3+25899532n^2+81965868n+111450816}{839808},
\]

\[
B=\frac{125n^5+3575n^4+36681n^3+146521n^2+63514n-639216}{46656},
\]

\[
C=\frac{75n^4+2278n^3+25869n^2+130178n+245088}{3888}.
\]

Here `B` itself changes sign, so a coefficientwise argument genuinely fails. Nevertheless

\[
4AC-B^2=\frac{1}{6530347008}
\bigl(328125n^{10}+24233750n^9+811112175n^8+16205881752n^7
\]
\[
{}+214066446879n^6+1953218099982n^5+12464481565377n^4
+54912151045636n^3+159757356700020n^2
+277021954843200n+217296269450496\bigr)>0.
\tag{4.6}
\]

Again the quadratic is positive for every real `s`.

#### (iii) Distinct independent vertices, spokes to the two port endpoints: `e=x0`, `f=y1`, `x!=y`

For `n>=2`,

\[
A=\frac{6875n^6+330000n^5+6600428n^4+70327986n^3+420679001n^2+1338801054n+1770932448}{7558272},
\]

\[
B=-\frac{1375n^5+57525n^4+948931n^3+7729323n^2+31131598n+49670160}{839808},
\]

\[
C=\frac{425n^4+13037n^3+149293n^2+756427n+1431330}{69984},
\]

and

\[
4AC-B^2=\frac{1}{2115832430592}
\bigl(41078125n^{10}+3203488750n^9+112384442775n^8
+2335210342776n^7
\]
\[
{}+31822194835743n^6+297124616086278n^5+1924881072477833n^4
+8542830141240596n^3+24856547474643540n^2
+42815686981147776n+33155245469456640\bigr)>0.
\tag{4.7}
\]

Thus this orbit is also positive for every real `s`.

Equations (4.4)–(4.7), together with the 22 coefficientwise-positive exact orbit certificates, prove `T07-SPLIT5-PORTFIELD-03`. QED.

## 5. Independent exact checks actually executed

The standard-library checker

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T02-18-30Z__split5_portfield_checker.py`

was executed before persistence. Its archived output is

`proofnet24/NM13-04/progress-forest/runs/2026-09-20/2026-09-20T02-18-30Z__split5_portfield_checker.out`.

It verifies, using only integer/rational arithmetic:

1. exactly 52 terminal partitions;
2. `M=6I+N`, `N^4!=0`, `N^5=0`;
3. exactly 25 edge-pair orbits under the port stabilizer;
4. the all-`n` degree-8 interpolation identities for every coefficient of every orbit, with an extra independent tenth value;
5. exactly three non-coefficientwise orbit quadratics and positive `4AC-B^2` for all three;
6. an independent brute-force enumeration of **every edge subset** of `H_2` with at most six edges (all larger subsets are automatically cyclic), checking every single-edge and edge-pair deletion/contraction coefficient against the transfer calculation.

The brute-force result is

\[
I_{H_2(s)}=20826+6942s,
\]

so `I_{H_2(1)}=27768`. The run ends with

`ALL_EXACT_CHECKS_PASS`.

Checker creation commit: `1298afd7e564b1c94be250fe20bd3ec50de50785`.  
Output archive commit: `d2d3945dc7b6c04c8013c32d1e5f1e6bb1e653cd`.

## 6. Coordination with NM13-08: new macro-network class

NM13-08 proved that PF-Rayleigh two-terminal graphs are closed under terminal parallel and series composition. The present theorem supplies a new infinite leaf family

\[
Q_n^{(5)}=(K_5\vee\overline{K_n})-g,
\qquad n\ge1,
\]

in addition to NM13-08's split-4 atoms

\[
Q_n^{(4)}=(K_4\vee\overline{K_n})-g.
\]

Therefore every finite series/parallel expression tree whose leaves are chosen arbitrarily from

\[
\{Q_n^{(4)}:n\ge1\}\cup\{Q_m^{(5)}:m\ge1\}
\]

is PF-Rayleigh and hence p-NC at unit weights. This is a genuine multiparameter non-series-parallel macro-class: its atoms themselves contain large complete minors, while the closure is performed at the two-terminal macro level.

No ownership is changed; NM13-08 owns the decomposition theorem and NM13-04 supplies the new split-5 atom theorem.

## 7. What did not move and residual obstruction

The all-graph T07 conjecture remains open. This theorem does not certify all ten-vertex 3-connected graphs, does not prove a universal Gårding/stability property, and does not control the arbitrary three-terminal mixed response that blocked P14's degree-three elimination.

The fixed-r partition method also scales by Bell numbers (`B_6=203`, etc.), so simply doing `K_6∨\overline{K_n}` next would be another local extension rather than a direct attack on the parent obstruction.

The next materially different attack should therefore be a **minor/deletion-contraction discriminant criterion**: isolate general hypotheses under which the one-edge-field Rayleigh quadratic

\[
A+B s+C s^2
\]

has `A,C>=0` from the deletion and contraction minors and prove `4AC-B^2>=0` from a structural terminal-response inequality. The split-5 theorem shows that controlling the discriminant can succeed even when the mixed coefficient `B` is negative; this directly targets the precise failure mode of P14's false mixed-term sign route.

## 8. ledger_delta

```yaml
ledger_delta:
  track: NM13-04
  parent: T07
  source: "Grimmett-Winkler math/0302185 / Grimmett Conjecture 4.2"
  target: "uniform-all-forests pairwise edge negative correlation on every finite graph"
  parent_status_before: OPEN
  parent_status_after: OPEN
  source_metric: "largest completely certified all-graph vertex order"
  source_metric_before: 9
  source_metric_after: 9
  counterexample_order_lower_bound_before: ">=10"
  counterexample_order_lower_bound_after: ">=10"
  mechanism_before: "unit p-NC for K4 join independent family; companion PF split4 atoms"
  mechanism_after: "PF-Rayleigh for all port-deleted K5 join independent atoms; unit strict p-NC for all K5 join independent graphs; PF series/parallel macro-networks mixing split4 and split5 atoms"
  theorem_id: T07-SPLIT5-PORTFIELD-03
  theorem_status: CANDIDATE_FULL_RESTRICTED_PENDING_INDEPENDENT_REVIEW
  exact_checker: "2026-09-20T02-18-30Z__split5_portfield_checker.py"
  exact_output: "2026-09-20T02-18-30Z__split5_portfield_checker.out"
  exact_output_terminal: ALL_EXACT_CHECKS_PASS
  pair_orbits: 25
  exceptional_discriminant_orbits: 3
  brute_force_sanity: "n=2; all forest subsets/all edge and edge-pair coefficients; I(s)=20826+6942s"
  companion_consumed: "NM13-08 T07-PORT-FIELD-SP-CLOSURE-06"
  residual_obstruction: "arbitrary 3-connected terminal-response mixed coefficient; no general discriminant theorem"
  next_attack: "prove a deletion/contraction minor criterion forcing 4AC-B^2>=0 beyond split graphs"
  novelty: UNVERIFIED_BOUNDED_SEARCH_ONLY
```

`END OF REPORT`
