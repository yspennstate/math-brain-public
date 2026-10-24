# account02/B14 — graphical inverse-gap localization with exact cluster threshold

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Control revision:** `2026-09-22.5`  
**Run:** `20260922T160911Z-b14-qform-localization-r15`  
**Assignment:** Translations and localization  
**Status:** `PROVED SUPPORTING LOCALIZATION THEOREM / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and first unpaid implication

The owner target remains the full arbitrary-dimensional statement: for independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one universal finite `C` such that

`P{X^T A X in I} <= C |I|`

for every bounded interval `I`, or construct a genuine target-valid counterexample. No moments, bounded support, connected support, centering, sign condition, or independence after a spectral rotation is available.

The previous account02/B14 run proved the exact three-point estimate

`E |X1-X2|^-a |X2-X3|^-b |X3-X1|^-c < infinity`

uniformly over all cap-one independent laws precisely in the regime `a,b,c<1` and `a+b+c<2`, with an explicit constant and arbitrary deterministic shifts. Its first unpaid implication was to understand whether more general shell/coarea singularity patterns can be paid before any fragment abstraction, or whether they hit a genuine integrability obstruction.

This run answers that question for **every fixed finite graph of pair-gap singularities**. It gives an exact cluster criterion, a constructive support-free proof, and a matching cap-one counterexample when the criterion fails. This is a strict extension of the previous triangle theorem.

The newest completed assigned-partner result actually applied is account03/B14,

`yspennstate/math-open-problems@871a2d4c9f1ea58d89748ab1abab05021b4408de`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260922T153828Z-account03-B14-QFORM-r13/REPORT.md`.

It proves a law-level convex-mixture localization: every admissible product law is an `L1`/total-variation limit of finite convex mixtures of compact finite-fragment extreme product laws, with no moment, support-diameter, translation, or universal fragment-count assumption. Section 8 below combines that theorem with the new graph criterion and permits the active certificate to vary from mixture component to mixture component.

## 2. Main theorem — exact graphical inverse-gap criterion

Let `G=(V,E)` be a finite simple graph, `V={1,...,m}`, and assign exponents

`0 <= theta_e < infinity`

to its edges. For `S subset V`, write

`Theta(S) = sum_{e subset S} theta_e`,

where the sum is over graph edges with both endpoints in `S`.

### Theorem 2.1

The following are equivalent.

1. For every subset `S subset V` with `|S|>=2`,

   `Theta(S) < |S|-1`.                                           (2.1)

2. There is a finite constant `C(G,theta)` such that for every independent real `X_1,...,X_m` whose probability densities satisfy `0<=f_i<=1`,

   `E prod_{e={i,j} in E} |X_i-X_j|^-theta_e <= C(G,theta)`.      (2.2)

Moreover the same constant is valid after arbitrary separate deterministic shifts:

`X_i -> X_i + tau_i`,                                             (2.3)

and therefore pointwise after conditioning on an arbitrary outside vector `z` when `tau_i=tau_i(z)`.

If (2.1) fails for even one subset `S`, then (2.2) is infinite already when all `X_i` are iid `Uniform[0,1]`.

Thus (2.1) is not merely a sufficient localization condition; it is the **sharp law-uniform absolute-integrability threshold** for graphical pair-gap singularities under the target density cap.

## 3. Remove the far field without support assumptions

For every `r>0` and `theta>=0`,

`r^-theta <= 1 + r^-theta 1_{r<=1}`.                              (3.1)

Multiplying (3.1) over all edges gives

`prod_{e in E} |Delta_e|^-theta_e`

` <= sum_{F subset E} prod_{e in F} |Delta_e|^-theta_e 1_{|Delta_e|<=1}`,  (3.2)

where `Delta_{ij}=X_i-X_j`.

Fix one edge set `F`. The integrand in its term factors over the nontrivial connected components of `(V,F)`, and the input law is a product. Hence its expectation is the product of the corresponding connected-component expectations. Isolated vertices contribute exactly one.

It is therefore enough to bound a connected graph `H=(W,F_H)` on `q>=2` vertices under the additional constraints

`|X_i-X_j| <= 1` for every `e={i,j} in F_H`.                      (3.3)

Because `H` is connected, (3.3) implies that the diameter of all coordinates in `W` is at most `q-1`: along a graph path of length at most `q-1`, every step has size at most one.

No support bound on the original densities has been introduced. The diameter bound is only an **event-local consequence** of the near-edge term in (3.2).

## 4. Ordered-gap reduction and the common-translation gain

Fix one of the `q!` possible orderings of the variables in `W`, denoted

`x_{pi(1)} <= ... <= x_{pi(q)}`.

Write

`x_{pi(1)}=t`,

`g_k=x_{pi(k+1)}-x_{pi(k)} >=0`, `k=1,...,q-1`.                  (4.1)

The Jacobian is one. By the diameter observation,

`0 <= g_k <= q-1`.                                               (4.2)

For fixed gaps `g=(g_1,...,g_{q-1})`, every coordinate is `t+a_i(g)`. Since every density is bounded by one,

`prod_{i in W} f_i(t+a_i(g)) <= f_j(t+a_j(g))`

for any fixed `j in W`. Therefore

`int_R prod_{i in W} f_i(t+a_i(g)) dt <= 1`.                    (4.3)

Equation (4.3) is the crucial product-law gain: the common translation direction costs **no support length, no moment, and no fragment count**. The remaining problem lives only in the `q-1` ordered gaps.

For an edge `e={u,v}`, let `P_e` be the consecutive set of ordered gaps between the positions of `u` and `v`. Then

`|x_u-x_v| = sum_{k in P_e} g_k`.                               (4.4)

The rest of the proof distributes every edge exponent fractionally across the gaps it spans.

## 5. Fractional gap allocation from the cluster inequalities

Define the strict global cluster slack

`delta = min_{S subset W, |S|>=2} [ |S|-1 - Theta_H(S) ] > 0`,   (5.1)

where `Theta_H` uses only the edges of `H`. Put

`epsilon = delta/(q-1)`.                                         (5.2)

### Lemma 5.1 — interval-flow allocation

For the fixed variable ordering there exist nonnegative numbers `w_{e,k}`, defined for `k in P_e`, such that

`sum_{k in P_e} w_{e,k} = theta_e` for every edge `e`,            (5.3)

and

`beta_k := sum_{e: k in P_e} w_{e,k} <= 1-epsilon`               (5.4)

for every ordered gap `k=1,...,q-1`.

### Proof

Form a capacitated bipartite network. The source sends `theta_e` units into an edge-node `e`; that edge-node may send mass to any gap-node `k in P_e`; every gap-node has capacity `1-epsilon` to the sink.

By weighted Hall/max-flow, it is enough to prove that for every collection `A` of edge-nodes,

`sum_{e in A} theta_e <= (1-epsilon) |N(A)|`,                   (5.5)

where `N(A)` is the union of the consecutive gap intervals `P_e`.

Write `N(A)` as a disjoint union of `r>=1` consecutive gap blocks. A block containing `d_l` gaps corresponds to a consecutive variable block `S_l` containing `d_l+1` vertices. Every edge in `A` lies entirely inside one such `S_l`. Hence, by (5.1),

`sum_{e in A} theta_e`

` <= sum_l Theta_H(S_l)`

` <= sum_l (d_l-delta)`

` = |N(A)| - r delta`.                                          (5.6)

Since `|N(A)|<=q-1` and `r>=1`,

`r delta >= delta >= epsilon |N(A)|`.                            (5.7)

Combining (5.6)-(5.7) gives (5.5). Therefore the flow exists, proving the lemma. QED.

This allocation is the precise higher-order replacement for the ad hoc radial estimate used in the previous triangle proof.

## 6. Weighted AM-GM pays every singular edge

For an edge with `theta_e>0`, put

`alpha_{e,k}=w_{e,k}/theta_e`,

so the nonzero `alpha` values sum to one. Weighted AM-GM gives

`sum_{k in P_e} g_k`

` >= sum_{alpha_{e,k}>0} g_k`

` = sum_k alpha_{e,k} (g_k/alpha_{e,k})`

` >= prod_k (g_k/alpha_{e,k})^{alpha_{e,k}}`.                    (6.1)

Consequently

`(sum_{k in P_e} g_k)^-theta_e`

` <= prod_k alpha_{e,k}^{w_{e,k}} g_k^{-w_{e,k}}`

` <= prod_k g_k^{-w_{e,k}}`,                                    (6.2)

because `0<alpha_{e,k}<=1`. Multiplying over all edges yields

`prod_{e in F_H} |x_u-x_v|^-theta_e <= prod_{k=1}^{q-1} g_k^-beta_k`.  (6.3)

By (5.4), every `beta_k<=1-epsilon`. Thus, using (4.2),

`int_0^{q-1} g_k^-beta_k dg_k`

` = (q-1)^{1-beta_k}/(1-beta_k)`

` <= (q-1)/epsilon`

` = (q-1)^2/delta`.                                             (6.4)

Combining the common-translation estimate (4.3), the `q!` orderings, and (6.4) proves the connected-component bound

`B(H) <= q! [ (q-1)^2/delta ]^{q-1}`.                           (6.5)

This constant is crude but explicit and depends only on the finite singularity graph and its exponent slack, never on the input laws or their supports.

## 7. Finish the sufficient direction with an explicit combinatorial constant

Return to the expansion (3.2). Let

`delta_G = min_{S subset V, |S|>=2} [ |S|-1-Theta(S) ] >0`.       (7.1)

For each `F subset E`, let `cc_+(F)` denote the nontrivial connected components of `(V,F)`. A component `H` on `q_H` vertices has cluster slack at least `delta_G`, because it uses only a subset of the original edges. Therefore (6.5) gives

`B(H) <= q_H! [ (q_H-1)^2/delta_G ]^{q_H-1}`.                    (7.2)

Hence one valid fully explicit constant in (2.2) is

`C(G,theta)`

` <= sum_{F subset E} prod_{H in cc_+(F)}`

`      q_H! [ (q_H-1)^2/delta_G ]^{q_H-1}`.                     (7.3)

The sum is finite because `G` is finite. This proves (2.1) => (2.2).

A fixed-size active graph therefore has a genuinely dimension-free localization constant. If the active graph size is allowed to grow with the ambient dimension, (7.3) itself is not a dimension-free bound; a target-level application must either keep the active graph size uniformly bounded or supply an additional aggregation argument. This limitation is explicit rather than hidden.

## 8. Necessity: a cap-one connected-support counterexample at every failed cluster

Assume there is a subset `S subset V`, `q=|S|>=2`, with

`Theta(S) >= q-1`.                                               (8.1)

Take every `X_i` iid `Uniform[0,1]`, an exact admissible cap-one product law with connected support.

Because all pair distances in `[0,1]` are at most one, every edge factor is at least one. Hence the full graph moment is bounded below by the internal `S`-edge moment.

Inside `(0,1)^q`, restrict to a small neighborhood of the full diagonal. Use one common translation coordinate `t` and `q-1` relative coordinates `u`. The internal singularity product is homogeneous of degree `-Theta(S)` in `u`. Choose an angular cone of positive measure on which every internal edge difference that appears in the product is bounded above and below by positive multiples of `|u|`; such a cone exists by choosing one relative configuration with distinct coordinates and taking a small neighborhood of its direction.

Polar coordinates in the `q-1` relative dimensions then give a lower bound by a positive constant times

`int_0^rho0 rho^{q-2-Theta(S)} d rho`.                           (8.2)

This diverges logarithmically when `Theta(S)=q-1` and by a power when `Theta(S)>q-1`. Therefore the raw graph moment is infinite under the exact target density cap.

This proves necessity and completes Theorem 2.1.

Two useful controls are immediate:

- the previous triangle criterion is recovered exactly: each edge exponent must be `<1` and the three exponents must sum to `<2`;
- for the complete graph `K_4` with every edge exponent `1/2`, the full four-point cluster has total exponent `6/2=3=4-1`, so the moment diverges logarithmically already for iid `Uniform[0,1]`. Thus four-point six-edge square-root shell singularities hit a genuine critical obstruction even though each individual edge exponent is subcritical.

## 9. Arbitrary translations and deterministic outside conditioning

For arbitrary constants `tau_i`, define

`Y_i=X_i+tau_i`.

The `Y_i` remain independent, and their densities are just translates of the original densities, hence still bounded by one. Theorem 2.1 applied to `Y` gives the same `C(G,theta)` with no dependence on `tau`.

If `z` is an arbitrary deterministic outside vector and `tau_i=tau_i(z)`, the identical estimate holds pointwise in `z`. Thus any conditional shell/coarea estimate that produces shifted graph gaps can be integrated over completely arbitrary outside product laws without a moment, support-radius, fragment-separation, or translation penalty.

This is exactly the localization scope assigned to B14.

## 10. New target-level compiler using the completed partner mixture theorem

The law-level convex-mixture theorem of account03/B14 (`871a2d4...`) permits a useful strengthening of the interface to the rest of QFORM.

Fix universal constants `m_0`, `delta_0>0`, and `K<infinity`. Suppose that for every compact finite-fragment extreme product law `nu`, every target interval `I`, and every target matrix `A` in the owner class, one can choose — **depending on that extreme component** —

1. an original-coordinate active set `S` with `|S|<=m_0`;
2. a graph `G_nu` on `S` and edge exponents `theta_nu` satisfying the uniform cluster slack

   `|T|-1-sum_{e subset T} theta_e >= delta_0`                  (10.1)

   for every `T subset S`, `|T|>=2`;
3. deterministic-outside shifts `tau_i(z)`;
4. a source-valid conditional small-ball estimate

   `P_nu{X^T A X in I | z}`

   ` <= K |I| E_{nu_S} prod_{e={i,j} in G_nu}`

   `      |(X_i+tau_i(z))-(X_j+tau_j(z))|^-theta_e`.            (10.2)

Then Theorem 2.1 supplies a single finite constant `C_0=C_0(m_0,delta_0)` for every allowed graph, for example by taking the maximum of (7.3) over the finitely many graph topologies on at most `m_0` vertices and using the worst permitted slack. Thus every extreme component satisfies

`P_nu{X^T A X in I} <= K C_0 |I|`.                              (10.3)

Now apply account03/B14's completed global convex-mixture localization. An arbitrary admissible product law is a total-variation limit of finite convex mixtures

`nu^(r) = sum_alpha p_alpha nu_alpha`

of such extreme product laws. The active set, graph, exponent allocation and shifts in (10.2) may be selected **separately for each component `nu_alpha`**; no single physical triple or graph has to work uniformly across all mixture components. Linearity gives the same bound `K C_0 |I|` for every finite mixture, and total-variation passage gives it for the original arbitrary law with exactly the same constant.

This is a genuine application of the newest completed partner theorem. It converts a component-adaptive local certificate into a full arbitrary-support certificate without choosing a common localization branch in advance.

It also respects the correction `QFORM-ONE-TRIPLE-RANK2-AGGREGATE-UNIFORM-FALSE-v1`: that correction refutes forcing one universally good physical triple from the three-large-eigenvalue hypothesis. Section 10 does not force one. It says only that if a uniformly subcritical bounded-size graph certificate can be found **for each extreme component**, possibly by different physical branches, localization itself introduces no further loss. The existence of those certificates is the remaining structural/analytic debt.

## 11. What changed relative to the preceding B14 runs

The preceding localization line had three increasingly structured mechanisms:

1. acyclic fragment-anchor packing, with a logarithmic obstruction for arbitrary cyclic anchors;
2. exact three-point pair-gap integration, whose common translation raises the sharp triangle threshold to total exponent two;
3. the present **graphical cluster theorem**, which identifies the complete sharp condition for any fixed finite pair-gap graph and proves both directions.

The advance is not a new selector name. The previous scalar condition `a+b+c<2` is now recognized as the three-vertex instance of the exact family of inequalities

`sum_{e subset S} theta_e < |S|-1`

for every collision cluster `S`. The proof supplies a constructive max-flow/AM-GM compiler and an exact connected-support counterexample at every violated cluster.

## 12. First remaining implication

Full QFORM remains OPEN.

The next B14-relevant implication is now sharply stated:

> In each unresolved localized/heavy branch, derive a deterministic-outside shell/coarea estimate whose singular factors can be represented by a **uniformly bounded-size shifted pair-gap graph with positive cluster slack**, or prove from the exact shell geometry that some collision cluster necessarily reaches the critical exponent `|S|-1`.

If the former holds with universal `m_0,delta_0,K`, Section 10 and the completed account03/B14 convex-mixture theorem remove all translation, unbounded-support, distant-fragment and branch-selection debts at once. If a cluster reaches criticality, Section 8 shows that raw absolute integration cannot be the closing mechanism even for iid connected-support uniforms; one must retain cancellation or another operator-level aggregation.

No full solution is claimed here, and no existence theorem for the required active graph has been smuggled into the localization result.

## 13. Source pins and correction status

- initial control snapshot: `yspennstate/math-research-brain@14e37c18dc0be3144252be6506896224997ee3d3`;
- fresh pre-write control/correction snapshot: `yspennstate/math-research-brain@949e6ab6b5a141d41667fa08551b256b40401003`;
- owner programme/control: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`;
- exact assignment: `scheduled_tasks/work/shared/qform-density-2026-09-22/assignments/account02/B14.json`;
- completed partner law-level convex-mixture localization actually applied: `yspennstate/math-open-problems@871a2d4c9f1ea58d89748ab1abab05021b4408de`;
- preceding account02/B14 three-point inverse-gap theorem: `yspennstate/math-open-problems@3f241388d9bcacf1379ef8ef640b35d7d14aad91`;
- live corrections consumed through pre-write snapshot include the bounded-diameter and fixed-fragment-count localization obstructions, the no-independence-after-rotation correction, conditional-cap correction, no-one-uniform-triple correction, and the newer Pluecker-pivot support-disjoint obstruction. None contradicts Theorem 2.1 because its proof stays in original independent coordinates and makes no structural-existence claim about `A`.

No FEI work, scheduler mutation, email/notification action, new task, cross-account authentication, paid call, public release, remote workflow, permission change, or unrelated private-data access is used by this result.
