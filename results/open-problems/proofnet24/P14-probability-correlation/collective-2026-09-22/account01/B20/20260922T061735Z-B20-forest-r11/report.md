# FOREST / account01 B20 — multigraph-minimal reduction removes the STAR-2 conditioning debt

**Run:** `20260922T061735Z-B20-forest-r11`  
**Outcome:** **ESSENTIAL_STEP_APPLIED**  
**Candidate:** `FOREST-MULTIGRAPH-MINIMAL-SIMPSON-v1`  
**Parent target:** Grimmett–Winkler pairwise negative correlation for the uniform law on all unrooted forests of every finite simple graph.  
**Parent status:** **OPEN**; this report is not a full-proof candidate.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and newest lead state

For every finite simple graph `G=(V,E)`, choose uniformly from all acyclic edge subsets, including the empty forest, disconnected forests and every possible forest size. For distinct present edges `e,f`, prove

`P(e,f in F) <= P(e in F) P(f in F)`.

Equivalently, with `Z,Z_e,Z_f,Z_ef` the exact forest counts,

`Delta_G(e,f)=Z_e Z_f-Z Z_ef >= 0`.

The newest complete team-lead report consumed is

`account01/B01/20260922T050946Z-b01-forest-auto11/report.md`,

candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`.

That lead correctly preserves the source correction from its preceding run: the old fixed-graph Cocks upgrade is not source-secure and is not used. Its new source-safe mechanism chooses an edge-minimal **simple** counterexample. For a triangle-free third edge `g`, both deletion and contraction stay simple and are smaller, so total covariance gives the Simpson inequality

`rho_eg rho_fg >= rho_ef > 0`.

The lead combines this with the canonical rank-homogeneous completely-log-concave budget. The first unpaid step is the triangle-edge case: contracting a triangle edge produces parallel pairs, which simplify to a `{1,2}`-weighted star. The lead calls the missing statement the **STAR-2 contraction comparison**.

This run removes that debt by changing the minimal-counterexample category in a source-equivalent way.

## 2. Named OTHER-account result consumed and applied

I consumed the assigned partner result

`account04/B03/20260922T040956Z-B03-forest-r12/report.md`,

whose exact simple path-bundle lemma is the key input here.

For an unmarked simple edge `g=uv`, replace it by `k_g` internally vertex-disjoint `u-v` paths of length `a_g>=2`, with all internal vertices fresh. If

`d_g=2^{a_g}-1`, `q_g=k_g/d_g`,

then for one gadget the number of local forest states not connecting `u,v` is `d_g^{k_g}` and the number connecting them is `k_g d_g^{k_g-1}`. Hence, after multiplying the no-connect factors over gadgets,

`Delta_expanded(e,f;1)=C^2 Delta_base(e,f;q)`.

In particular an **integer** activity `r>=1` is realized exactly by taking `a=2` and `k=3r`, since `k/(2^a-1)=3r/3=r`.

I use this exact result below to show that passing to labelled loopless multigraphs is source-equivalent, rather than an unrelated strengthening.

## 3. New theorem A — simple unit FOREST is equivalent to loopless-multigraph unit FOREST

A loopless multigraph here has labelled edge copies; a forest may contain at most one edge from any parallel class because two parallel copies form a graphic 2-cycle.

### Theorem A

The following statements are equivalent:

**(S)** every finite simple graph satisfies unit pairwise forest negative correlation;

**(M)** every finite loopless multigraph, with the uniform law on its labelled forests, satisfies unit pairwise forest negative correlation.

### Proof

`(M)=>(S)` is immediate because simple graphs are a subclass.

For `(S)=>(M)`, let `M` be a loopless multigraph and collapse every parallel class to one edge of an underlying simple graph `H`. Let the class multiplicity of an edge `h` be the positive integer `r_h`.

A labelled forest of `M` projects to a forest of `H`; if the projected forest uses `h`, there are exactly `r_h` choices of the labelled copy. Therefore the forest partition function of `M` is exactly the weighted simple-graph forest polynomial of `H` evaluated at `y_h=r_h`.

If two marked copies `e,f` lie in the same parallel class then they can never occur together, so their covariance is automatically nonpositive. Suppose instead that they lie in distinct parallel classes `E,F`. Write `Z_H(y)` for the multiaffine weighted forest polynomial. Fixing one particular labelled copy in class `E` removes the multiplicity factor `y_E`; hence

`Z_e = partial_E Z_H(r)`,
`Z_f = partial_F Z_H(r)`,
`Z_ef = partial_E partial_F Z_H(r)`,
`Z = Z_H(r)`.

Thus the exact labelled-copy Rayleigh gap is

`Delta_M(e,f) = (partial_E Z_H)(partial_F Z_H)-Z_H partial_E partial_F Z_H`,

evaluated at the integer activities of the unmarked classes. Because `Z_H` is multiaffine, this Rayleigh difference is independent of the two marked variables `y_E,y_F` themselves.

Now apply the account04/B03 simple path-bundle gadget to every **unmarked** class activity `r_h`. Choose `a_h=2` and `k_h=3r_h`, so the gadget realizes `q_h=r_h` exactly. Leave the two marked base edges literal. The expanded graph is simple and its unit Rayleigh gap is a strictly positive square factor times `Delta_M(e,f)`. Under (S) that unit gap is nonnegative, so `Delta_M(e,f)>=0`.

Hence (M). QED.

### Consequence

If the source simple-graph conjecture were false, then the class of loopless-multigraph counterexamples would be nonempty. Therefore one may choose a counterexample with the **minimum number of labelled edges among all loopless multigraph counterexamples**. Proving that no such minimal multigraph exists proves the original source theorem; no fixed-graph weighted theorem is being assumed.

## 4. New theorem B — every deletion and contraction condition is source-safe in a minimal multigraph counterexample

Assume for contradiction that a minimal loopless multigraph counterexample `M` exists. Let its number of labelled edges be `m`, and fix a violating pair `e,f`:

`C_ef=Cov(X_e,X_f)>0`.

The marked edges cannot be parallel, because parallel copies can never occur together.

For any third labelled edge `g`, `0<P(g)<1`: the singleton `{g}` is a forest and deleting `g` from any forest containing it injects into forests omitting it, so in fact `P(g)<=1/2`.

Conditioning on `X_g=0` is exactly the uniform forest law of `M\g`, which has fewer labelled edges and therefore is not a counterexample. Hence

`Cov(X_e,X_f | X_g=0) <= 0`.

Conditioning on `X_g=1`, then deleting the compulsory edge `g`, is exactly the uniform independent-set/forest law of the contraction `M/g`. Contracting may turn edges parallel to `g` into loops. Such loops can never occur in a forest and may be deleted. The resulting loopless multigraph has strictly fewer labelled edges than `M`. If one of the marks becomes a loop its conditional variance/covariance is zero; otherwise minimality again gives

`Cov(X_e,X_f | X_g=1) <= 0`.

Therefore the exact binary law of total covariance gives, for **every** third edge `g`,

`C_ef <= C_eg C_fg / Var(X_g)`.

Standardizing, with

`a=rho_ef>0`,

we obtain the universal all-edge Simpson inequality

`boxed: rho_eg rho_fg >= a > 0  for every g notin {e,f}.`

This is precisely the inference that the simple-counterexample route could establish only for triangle-free `g`. No STAR-2 external-field comparison is needed.

## 5. New theorem C — the full positive-correlation matching geometry is source-secure

Define a graph on the labelled edge set of `M` by joining two distinct elements when their covariance is positive.

### Transitivity

If `C_ij>0` and `C_jk>0`, apply Theorem B to the violating pair `(i,j)` with third edge `k`:

`rho_ik rho_jk >= rho_ij >0`.

Since `rho_jk>0`, this forces `rho_ik>0`. Thus positive correlation is transitive.

### No positive triangle

Suppose distinct `i,j,k` had pairwise positive correlations

`x=rho_ij`, `y=rho_ik`, `z=rho_jk`.

Applying Theorem B cyclically gives

`x<=yz`, `y<=xz`, `z<=xy`.

Multiplying yields

`xyz <= (xyz)^2`.

For distinct nonloop edge indicators one has `0<rho<1`: the empty forest and the singleton forests separate their indicator values, so correlation `1` is impossible. Hence `0<xyz<1`, contradicting the displayed inequality.

Thus the positive-correlation graph is triangle-free. Together with transitivity it is a matching.

For the fixed violating pair `e,f`, Theorem B says `C_eg` and `C_fg` have the same nonzero sign for every third `g`. They cannot both be positive, because that would make the positive triangle `e,f,g`. Therefore

`boxed: C_eg<0 and C_fg<0 for every g notin {e,f}.`

This restores the old all-third-edge `FOREST-SIMPSON-MATCHING` geometry without the disputed fixed-graph Cocks bridge and without the lead's triangle-free restriction.

### Marked parallel classes are impossible

A useful immediate corollary is that neither member of a violating pair can have a parallel copy. If `e'` is parallel to `e`, the automorphism swapping the two labelled copies gives

`Cov(X_{e'},X_f)=Cov(X_e,X_f)>0`,

whereas `e'` is a third edge and the preceding theorem requires that covariance to be strictly negative. Contradiction.

Parallel classes disjoint from the marked pair are not eliminated by this argument and remain part of the next obstruction.

## 6. New theorem D — the lead's rank-homogeneous budget now applies to all third edges

The lead's completely-log-concave argument is matroidal and therefore applies unchanged to a graphic multigraph. Let `R` be the graphic-matroid rank, `K=|F|`, `mu=E K`, and

`c_h=Cov(X_h,K)`.

For a marked edge `e`, set

`T_e = c_e^2 / ((R-mu)p_e(1-p_e))`,

with the usual zero-limit interpretation if needed. The lead's diagonal budget is

`T_e + sum_{h!=e}(1-p_h) rho_eh^2 <= p_e`.

Add the budgets for the violating pair `e,f`. The mutual terms contribute

`(2-p_e-p_f)a^2 >= a^2`

because every edge has `p_h<=1/2`. For each of the `m-2` third edges, Theorem B and AM-GM give

`rho_eg^2+rho_fg^2 >= 2|rho_eg rho_fg| >= 2a`,

while `1-p_g>=1/2`. Hence the full source-equivalent minimal multigraph satisfies

`boxed: T_e + T_f + a^2 + (m-2)a <= 1.`

In particular

`a <= (sqrt((m-2)^2+4(1-T_e-T_f))-(m-2))/2`

and therefore

`a <= (sqrt((m-2)^2+4)-(m-2))/2`.

This is the lead's triangle-free quantitative obstruction with `s` upgraded from the number of triangle-free physical edges to **all `m-2` third edge labels**.

## 7. Integration with the existing cross-fiber transport route

The account04/B02 path-cut transport identities (T1)--(T5) are formulated by deleting a labelled edge from the unique path in a forest and adding a labelled edge across the resulting component cut. They remain valid verbatim for loopless multigraphs: a forest contains no parallel 2-cycle and still has unique paths, while cut capacities simply count edge labels with multiplicity.

Thus two previously separated pieces can now be used simultaneously without a weighted Cocks step:

1. exact residual product-count/path-cut transport, including the overlap reservoir `Q`;
2. strict negative covariance of the violating pair with **every** third labelled edge, plus the full all-edge CLC budget above.

The old STAR-2 comparison is no longer the first unpaid universal implication.

## 8. Compact conditional end-to-end chain and the new first unpaid implication

The source-safe chain is now:

1. if a simple counterexample exists, Theorem A permits choosing an edge-minimal loopless multigraph counterexample;
2. proper deletion/contraction conditions are smaller loopless multigraph instances, after deleting loops;
3. exact total covariance gives the all-edge Simpson inequality;
4. hence positive pairs form a matching and the chosen violating pair is strictly negatively correlated with every third labelled edge;
5. complete log concavity gives the all-edge quantitative budget `T_e+T_f+a^2+(m-2)a<=1`;
6. the exact cross-fiber path-cut transport identities remain valid with labelled multiplicity.

**First remaining universal implication:** convert an overload/failure of the residual edge-labelled Hall/defect-routing transport into a positive covariance of some third labelled edge with `e` or `f` (contradicting Step 4), or obtain an equivalent global contradiction from the all-edge budget and the transport capacities.

This is a genuinely later obligation than STAR-2: all contraction strata have already been paid by minimality in the source-equivalent multigraph category.

## 9. Exact audit used in this run

`multigraph_equivalence_audit.py` checks the collapse identity on a nontrivial labelled `K_4` multigraph with parallel-class multiplicities

`(2,3,1,2,1,1)`

on edges `(01,02,03,12,13,23)` and one fixed marked copy from each of the first two classes.

Exact output:

```text
MULTIGRAPH_COLLAPSE_AUDIT
edge_labels = 10
forest_count = 114
multigraph_counts = (114, 26, 22, 4)
weighted_derivative_counts = (114, 26, 22, 4)
multigraph_gap = 116
weighted_gap = 116
identity = True
```

The computation is only an audit of the collapse formula; Sections 3--6 are algebraic proofs and do not depend on finite testing.

I also separately stress-tested the lead's raw STAR-2 sign before choosing the multigraph route: exhaustive exact integer enumeration over all labelled simple graphs on five vertices, every center, every subset of incident edges doubled, and every present marked pair checked 373,680 instances with no negative gap; an all-star exhaustive six-vertex check covered 5,160,960 additional marked instances with no failure. These finite checks are **not** used as proof evidence and do not close STAR-2.

## 10. Failure evidence and honest status

What was **not** proved:

- no contradiction to the existence of the minimal multigraph has yet been obtained;
- parallel classes disjoint from the violating pair can still occur;
- the exact residual Hall/defect-routing theorem remains unpaid;
- the parent FOREST conjecture is therefore still open in this pipeline.

What was proved is the exact source-equivalent change of category that removes the lead's STAR-2 conditional-covariance debt and restores the all-third-edge Simpson/matching geometry plus the strongest current CLC budget.

**Outcome: `ESSENTIAL_STEP_APPLIED`.**

## 11. Source-bound handoff

Next recipient should work from `FOREST-MULTIGRAPH-MINIMAL-SIMPSON-v1`, not from the refuted fixed-graph Cocks candidate and not from the triangle-free-only STAR-2 formulation. The most direct next target is the labelled Hall/defect-routing implication in Section 8, using strict external negativity for every third label. Any proof that silently simplifies parallel classes to unit edges loses the source-equivalent minimality and must supply the missing multiplicity argument explicitly.

Model self-report: `GPT-5.6 Sol`. Requested effort: highest actually exposed by the run instruction. Configured effort: `UNKNOWN / NOT_EXPOSED`. Provider usage/thinking counters: `UNKNOWN / NOT_EXPOSED`, not zero. No brain retrieval/context was authenticated in the mathematical derivation.
