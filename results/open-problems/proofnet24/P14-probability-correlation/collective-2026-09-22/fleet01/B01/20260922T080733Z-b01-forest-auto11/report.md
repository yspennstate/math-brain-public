# FOREST / fleet01 B01 — certified contraction conditioners and the exact STAR-2 handoff

**Run:** `20260922T080733Z-b01-forest-auto11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-CERTIFIED-CONTRACTION-STAR2-v2`  
**Parent target:** OPEN  
**Context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and inherited source-exact state

The active owner directive is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, owner-control revision `2026-09-22.2`. B01 remains the FOREST campaign lead; old brain installation/benchmark work is stopped.

The exact source target is P0001: for a finite simple graph `G`, under the uniform law on all acyclic edge subsets, prove

`P(e,f in F) <= P(e in F) P(f in F)`

for all distinct physical edges `e,f`.

Recovered dependencies used rather than rebuilt:

1. P0001's canonical claim records Grimmett's Conjecture 4.2 and the source-exact unit/unrooted/all-sizes interpretation.
2. P14's frozen predecessor state records exact source coverage through order 9; its later G0007 work is unrelated and is not imported.
3. R02 proved the source-secure partial theorem `r_block >= 6`: p-NC holds when every nontrivial 2-connected block has cyclomatic number at most 6. No later `r=7` claim that depends on the disputed fixed-graph weighted-Cocks step is used.
4. B01's immediately preceding run proved the triangle-free-conditioning Simpson implication and the rank-homogeneous budget

   `T_e + T_f + a^2 + s a <= 1`

   when `s` counts triangle-free third edges, where `a=rho_ef>0` and

   `T_i = Cov(X_i,K)^2 / ((R-EK) p_i(1-p_i))`.
5. Named OTHER-account input actually consumed: fleet02/B02 `20260922T041021Z-fleet02-B02-forest-r13` (as recorded in the preceding B01 report), whose source-valid core is the augmented homogeneous log-concavity / Hessian row budget. Its Cocks-dependent conclusions are not used.

The goal of this run is the first missing all-graphs comparison left by item 4: the conditional law after contracting a triangle edge, where parallel pairs appear on one contracted-vertex star.

## 2. Exact contraction-to-STAR-2 representation

Let `G` be simple, let `g=uv`, and condition the unit forest law on `X_g=1`. Contract `g` to a vertex `x`. Because `G` is simple, the only parallel classes created are the following: for every common neighbor `w` of `u,v`, the two physical edges `uw` and `vw` become a parallel pair joining `x` to `w`. Every such pair lies on the one star centered at `x`; there are no larger parallel classes.

Let `H_g` be the simple graph obtained by replacing every such parallel pair by one effective edge. Let `S_g` be the set of those effective star edges. Pushing the uniform forest law of the contracted multigraph to `H_g` gives exactly the independent-set/forest measure with edge activities

- `2` on `S_g`,
- `1` on every other edge.

Indeed, an effective forest `A` has exactly `2^{|A intersect S_g|}` physical lifts, since at most one edge from each parallel pair can be chosen and the choices for distinct included classes are independent.

This is the precise `STAR-2` object; no arbitrary external field appears.

## 3. Physical marked edges: exact sign-transfer lemma

The main technical point needed for source-exact conditioning is that the marked objects in the original conjecture are *physical edges*, not merely effective edges of `H_g`.

Fix two marked physical edges `e,f != g`.

For each marked physical edge that lands in a doubled parallel class, let `Y_s` be the effective inclusion indicator of that class. Conditional on the effective forest, if `Y_s=1` the selected physical copy is uniform among the two copies. Different doubled classes make these copy choices independently.

Therefore:

1. If `e` and `f` become the two members of the same parallel class, then they are mutually exclusive after conditioning on `g`, and

   `Cov(X_e,X_f | X_g=1) = -P(X_e=1|g) P(X_f=1|g) <= 0`.

2. Otherwise their effective images `bar e, bar f` are distinct. Put `alpha_i=1/2` when physical edge `i` lies in a doubled class and `alpha_i=1` otherwise. Then

   `Cov(X_e,X_f | X_g=1)
      = alpha_e alpha_f Cov(Y_bar_e,Y_bar_f)`

   under the `{1,2}`-weighted law on `H_g`.

Hence the sign of the physical conditional covariance is exactly the sign of the effective covariance, except in the same-class case where the physical covariance is automatically nonpositive.

This closes a bookkeeping gap in the earlier STAR-2 statement: a weighted theorem on `H_g` is sufficient for the *literal physical marked pair* with the exact factors above.

## 4. Certified-conditioner Simpson theorem

Take an edge-minimal simple counterexample `G` and a violating pair `e,f`, and write

`a = rho_ef > 0`.

Call a third physical edge `g` **certified for (e,f)** if the conditional covariance after `g=1` is source-securely known to be nonpositive. The following are certified without any disputed fixed-graph Cocks upgrade:

- **Type A:** `g` lies in no triangle. Then `G/g` is simple and has fewer edges, so edge minimality gives conditional p-NC.
- **Type B:** after contracting `g`, the marked physical edges `e,f` become the two copies in one parallel class. Their conditional covariance is automatically nonpositive by Section 3.
- **Type C:** the effective weighted pair in `H_g` is covered by a genuine all-positive-weight I-Rayleigh theorem for `H_g`. In particular this applies when `H_g` is series-parallel, by Erickson's weighted spanning-forest Rayleigh theorem. More generally any independently source-certified I-Rayleigh class can be inserted here.

Deletion is always a smaller simple graph, so

`Cov(X_e,X_f | X_g=0) <= 0`.

For a certified `g`, the binary law of total covariance gives

`Cov(e,f)
 = (1-p_g) Cov(e,f|g=0)
 + p_g Cov(e,f|g=1)
 + Cov(E[X_e|X_g],E[X_f|X_g])`.

The first two terms are nonpositive. For a Bernoulli conditioner,

`Cov(E[X_e|X_g],E[X_f|X_g])
 = Cov(e,g) Cov(f,g) / Var(g)`.

Therefore every certified third edge satisfies the exact Simpson inequality

`Cov(e,g) Cov(f,g) / Var(g) >= Cov(e,f) > 0`,

or equivalently

`rho_eg rho_fg >= rho_ef = a > 0`.

This strictly enlarges the previous run's safe set from only triangle-free edges to all certified triangle contractions, including the marked-triangle case and every contraction whose simplified STAR-2 graph is weighted-I-Rayleigh.

## 5. Quantitative budget with the enlarged certified set

Use fleet02/B02's homogeneous-Hessian row inequality in the strengthened rank-degree form already established by B01:

`T_i + sum_{h != i} (1-p_h) rho_ih^2 <= p_i`,

where

`T_i = Cov(X_i,K)^2 / ((R-EK) p_i(1-p_i))`.

Let `C(e,f)` be any set of certified third edges and put `s_cert=|C(e,f)|`. Add the inequalities for `i=e,f`.

Because the unit forest family is down-closed, `p_h<=1/2` for every edge. The two marked-pair terms contribute at least `a^2`, and for each certified `g`,

`(1-p_g)(rho_eg^2+rho_fg^2)
 >= (1/2) * 2 |rho_eg rho_fg|
 >= a`.

Also `p_e+p_f<=1`. Discarding all other nonnegative terms gives

`T_e + T_f + a^2 + s_cert a <= 1`.

Hence

`a <= (sqrt(s_cert^2 + 4(1-T_e-T_f)) - s_cert)/2
   <= (sqrt(s_cert^2+4)-s_cert)/2`.

Equivalently,

`s_cert <= (1-T_e-T_f-a^2)/a`.

Thus the remaining hard core of a minimal counterexample is now explicit: a large violation can survive only if most third edges are triangle edges whose STAR-2 contractions fall outside every weighted-I-Rayleigh class presently available.

In particular, for every non-certified triangle edge `g` not covered by the same-class marked exception, the simplified contraction `H_g` cannot be series-parallel; hence it contains a `K_4` minor. This is a structural necessary condition, not a solution.

## 6. Exact component formula for STAR-2 and an antitone likelihood-ratio lemma

Let `H` be a simple graph with special center `x`, and double an arbitrary subset `S` of the star at `x`. Put `J=H-x`. For a forest `A` of `J`, let its connected components be `C`. Define

- `d_C` = number of star edges from `x` into `C`,
- `s_C` = number of those star edges that lie in `S`.

Given `A`, a forest can use at most one edge from `x` into any one component `C`. Therefore the exact extension factors are

`U(A) = product_C (1+d_C)`

for unit star weights and

`W(A) = product_C (1+d_C+s_C)`

for STAR-2 weights. The Radon ratio of the center-eliminated marginal is

`L(A)=W(A)/U(A)
    = product_C (1 + s_C/(1+d_C))`.

This ratio is antitone under legal forest extension in `J`. Indeed, adding an edge that joins components `C,D` merges them. Set `a=1+d_C`, `b=1+d_D`, `s=s_C`, `t=s_D`. Before the merge the relevant ratio is

`(1+s/a)(1+t/b)`,

while after the merge it is

`1 + (s+t)/(a+b-1)`.

Since `a+b-1 >= a,b`,

`s/a + t/b + st/(ab) >= (s+t)/(a+b-1)`.

Hence `L(before) >= L(after)`.

This identifies the exact qualitative effect of doubling a star: relative to the unit-star marginal on `H-x`, STAR-2 reweights toward forests with less component merging. This antitonicity is rigorous, but it is **not** being promoted to negative correlation: the forest poset does not supply the positive-association statement that would make such a tilt automatically preserve the desired pairwise signs.

## 7. Exact simple unit gadget for activity 2, and why gadget induction cannot use edge minimality

A `{1,2}` star edge can be simulated exactly by an unweighted simple two-terminal gadget.

Take terminals `a,b`, retain the direct edge `ab`, and add three internally vertex-disjoint paths `a-z_i-b`, `i=1,2,3`. This is the 7-edge theta gadget.

Let `A` be the number of gadget forests in which `a,b` are disconnected and `B` the number in which they are connected.

- Disconnected: the direct edge is absent and none of the three length-2 paths is complete. Each path has three allowed states, so `A=3^3=27`.
- Connected through the direct edge: direct edge present and no length-2 path complete, giving `27` states.
- Connected without the direct edge: exactly one of the three length-2 paths is complete; choose it in `3` ways and give each remaining path one of its `3` non-complete states, giving `3*3^2=27` states.

Thus `B=54=2A`.

Consequently, replacing a doubled effective edge by this gadget multiplies the disconnected state by `27` and the connected state by `54`, exactly reproducing activity `2` up to a common factor. Replacing `q` doubled star edges by disjoint copies gives an overall factor `27^q`; for marked host edges outside the gadgets, the Rayleigh difference is multiplied by `27^(2q)`.

The exact checker `activity2_gadget_checker.py` exhaustively enumerates every connected simple two-terminal graph with at most 6 edges. Any minimal two-terminal gadget may be assumed connected: an irrelevant component multiplies `A` and `B` by the same factor, while terminals in different components give `B=0`. A connected graph with at most 6 edges has at most 7 vertices, so the finite enumeration is complete. Output:

`CONNECTED_SIMPLE_GADGETS_AT_MOST_6_EDGES_CHECKED=22358`
`RATIO2_WITNESS_AT_MOST_6_EDGES=None`
`SEVEN_EDGE_CANDIDATE_A=27`
`SEVEN_EDGE_CANDIDATE_B=54`
`SEVEN_EDGE_CANDIDATE_RATIO2=True`

Therefore 7 edges is optimal among simple unweighted exact two-terminal activity-2 gadgets.

This also rules out a tempting minimal-counterexample shortcut. If contracting `g` produces `q>=1` doubled classes, then `H_g` has `m-1-q` effective edges when `G` has `m` physical edges. Exact simple gadgetization replaces each doubled effective edge by 7 edges, so the expanded simple host has

`m' = (m-1-q) + 7q = m-1+6q` if one counts replacement from the fully simplified edge list directly.

Equivalently, relative to retaining each effective edge as one direct edge, each gadget adds 6 edges. In either accounting `m' > m` for every `q>=1` except no-doubling. Thus edge-minimality cannot certify the gadget-expanded graph. (The earlier informal `m-1+5q` bookkeeping was corrected here: simplification removes `q` duplicates, but the effective doubled edges themselves are already among the `m-1-q` edges and each is replaced by seven, so the net is `m-1-q+6q` only if one erroneously adds six without first removing the effective edge; the correct replacement is `m-1-q-q+7q = m-1+5q`. See the next paragraph for the canonical count.)

Canonical count: `H_g` contains `q` effective doubled edges among its `m-1-q` edges. Removing those `q` edges and inserting seven edges per gadget gives

`m_expanded = (m-1-q) - q + 7q = m-1+5q > m`.

So the exact activity-2 gadget route is useful as a representation theorem but cannot by itself close the minimal-edge induction.

The gadget statement is restricted to marked host edges outside the gadgets. If a marked physical edge belongs to a doubled class, its image is a terminal-connectivity event inside the gadget, not a literal gadget edge; ordinary edge-pNC on the expansion does not automatically control that event. Section 3 is the correct physical-edge treatment.

## 8. Decisive computation / construction status

The only finite computation counted substantively is the exact gadget minimality certificate above; it is not being counted as closure of FOREST.

A separate bounded exploratory STAR-2 scan over random connected graphs on 8--10 vertices found no positive covariance in the sampled `{1,2}` star-weight instances. This is not a theorem and is not used in any claim; it is omitted from the candidate status precisely to avoid mistaking a census/search miss for proof.

## 9. Current-source cross-check

Current public sources remain consistent with the blocker isolated here:

- Erickson's series-parallel result proves a weighted Rayleigh/SOS theorem for spanning forests of series-parallel graphs, so Type C above is source-valid for that class.
- Semple--Welsh explicitly note that they could not show that the *unit* graph conjecture is preserved by arbitrary series or parallel extension; this is why the gadget representation cannot be silently turned into an induction theorem.
- Fang--Ma, arXiv:2604.27755 (2026), still list as conjectures that every regular matroid is I-Rayleigh and that every graph's unrooted spanning-forest generating polynomial is Rayleigh. Their Theorem 1.3 gives Rayleigh consequences for several classes, including cycle matroids of series-parallel networks, but not all graphic matroids.

Thus the new result does not rely on a hidden all-weights theorem that would already settle the parent problem.

## 10. Honest status and next exact obligation

**Outcome: `ESSENTIAL_STEP_APPLIED`.**  
**Parent conjecture: OPEN.**  
**FULL_PROOF_CANDIDATE: false.**

The all-graphs debt is now narrower than the previous generic STAR-2 phrase. For an edge-minimal counterexample and violating pair `e,f`, every third edge in the certified set pays the exact Simpson product and enters the quantitative Hessian budget. The remaining conditioners are triangle edges for which:

1. the marked edges do not collapse to the same parallel class; and
2. the `{1,2}`-weighted simplified contraction is not covered by a known I-Rayleigh class (in particular it is non-series-parallel, hence has a `K_4` minor).

The next mechanism should attack this residual **non-series-parallel STAR-2** class directly. Two precise routes survive:

- use the component formula of Section 6 to prove the needed Rayleigh sign under the special antitone merger tilt, without assuming an unsupported association theorem; or
- exploit the forced `K_4`-minor structure of every residual contraction together with the rank-homogeneous spectral budget to obtain a contradiction for a minimal counterexample.

The optimal-gadget certificate shows that an exact local unit-gadget reduction cannot be combined naively with edge minimality, so repeating that route without a new global comparison would not advance the proof.

## 11. Runtime / provenance boundary

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token/time usage: `NOT_EXPOSED`; unknown is not zero. Elapsed runtime is reported separately in the immutable finish record and includes reasoning, connector/network and runtime overhead rather than pure thinking.

No verified brain retrieval/context use occurred, so this run remains `WITHOUT_VERIFIED_BRAIN`. No installation/benchmark work, email, Drive, public posting, paid/remote compute, permission changes, scheduler mutation, credential handling, or unrelated private-data access was performed.
