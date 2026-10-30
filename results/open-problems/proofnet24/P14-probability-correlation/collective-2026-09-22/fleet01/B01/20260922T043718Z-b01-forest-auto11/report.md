# FOREST / fleet01 B01 — fixed-graph Cocks bridge rejected fail-closed; exact replacement equivalence

**Run:** `20260922T043718Z-b01-forest-auto11`  
**Outcome:** `CANDIDATE_REFUTED` **as written** for `FOREST-KN-COCKS-RECONCILED-v3`; the parent FOREST conjecture is not refuted.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.  
**Control:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, revision `2026-09-22.2`, exact control commit `fd4867f44948216441974cb8202951c0800fb61f`.

## 1. What changed

The previous lead candidate `FOREST-KN-COCKS-RECONCILED-v3` (report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`) used the chain

1. unit forest pairwise negative correlation for every complete graph `K_n` (the exact labelled-forest/Hermite theorem);
2. a purported **fixed-graph Cocks implication** `unit pNC on G => M(G) is independence correlated for every positive weighting`;
3. Semple--Welsh Proposition 3.5 (weighted independence correlation is minor-closed);
4. delete the nonedges of `K_n` to obtain arbitrary simple `G`.

The complete-graph theorem is preserved. The failure is Step 2: the final Semple--Welsh paper contains a Note whose literal wording is fixed-graph, but two independent post-publication sources identify Cocks's published result as a **global class equivalence**, and the constructive proof matching Cocks's result needs unit negative correlation on a whole family of substituted graphs, not merely on the starting graph. The original Cocks article body was not available through the authorized public source in this run, so the stronger fixed-graph reading cannot be certified and must be rejected fail-closed.

This does **not** assert that Semple--Welsh made a mathematical error. It says only that the one sentence in their post-submission Note is incompatible with the later detailed description of Cocks's result and cannot safely carry a purported solution of a still-open conjecture without the primary proof body.

## 2. Named OTHER-account work consumed and applied

### fleet02/B02 — scope correction

Consumed `fleet02/B02/B02-20260922T013646Z-forest-r12/cocks_scope_correction.md`, blob `733d840093ca109d38f4e336d228ae1ddedf77c0`.

B02 correctly separated the class-level parallel-copy/gadget argument from the stronger fixed-`G` implication. It preserved the complete-graph Hermite theorem and identified the missing bridge as positive-weight `K_n`, an equivalent unit theorem for the necessary extensions, or a direct deletion theorem.

### fleet04/B03 — simple path-bundle globalization

Consumed `fleet04/B03/20260922T040956Z-B03-forest-r12/report.md`, blob `8812d4c9be5debaec40c02c2b13779bba8b62fae`.

B03 proved a source-secure simple-graph gadget lemma. For each unmarked base edge `g=uv`, replace it by `k_g` internally vertex-disjoint `u-v` paths of length `a_g>=2`, with fresh internal vertices. Put

`d_g = 2^{a_g}-1`, `q_g = k_g/d_g`.

For one gadget the number of local acyclic states not connecting `u,v` is

`C0_g=d_g^{k_g}`,

and the number connecting `u,v` is

`C1_g=k_g d_g^{k_g-1}`,

because an acyclic connecting state has exactly one intact path. Hence `C1_g/C0_g=q_g`. If marked edges `e,f` are left literal and `C=prod C0_g`, exact projection of forests gives

`Z_H=C Z_G(q)`, `Z_{H,e}=C Z_{G,e}(q)`, `Z_{H,f}=C Z_{G,f}(q)`, `Z_{H,ef}=C Z_{G,ef}(q)`,

therefore

`Delta_H(e,f;1)=C^2 Delta_G(e,f;q)`.

The values `k/(2^a-1)` are dense in `(0,infinity)`. Thus unit pNC for **all** simple graphs implies weighted independence correlation for all simple graphic matroids. This is global, not fixed-graph.

### fresh fleet04/B01 r13

During this run a newer OTHER-account report appeared, `fleet04/B01` run `fleet04-b01-20260922T043827Z-forest-r13`, candidate `FOREST-UNIT-MINIMAL-3CONN-v2`. Its exact two-cut algebra is useful, but its Section 5 again invokes the disputed fixed-graph Cocks implication on smaller augmented bridges. Therefore its resulting unit-minimal-3-connected theorem is presently conditional on the same source bridge and does not repair the lead candidate.

## 3. Source audit: what Cocks is actually credited with

### 3.1 Final Semple--Welsh paper

Charles Semple and Dominic Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), 423--435, DOI `10.1017/S0963548307008978`, author PDF:
`https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf`.

The paper defines an independence-correlated matroid by nonnegativity of the independent-set Rayleigh difference for **every positive real weighting**. Proposition 3.5 proves this weighted class is closed under minors. Immediately afterward the authors explicitly say they do not know whether the **unit** graph class satisfying Conjecture 1.1 is minor-closed. In Section 5, Question (3) asks whether a graph may satisfy the unit conjecture while `M(G)` fails to be independence correlated. The post-submission Note then says Cocks settled (3), with literal fixed-graph wording.

That final sentence is the only load-bearing evidence used by the prior lead for the fixed-graph implication.

### 3.2 Erickson thesis: Cocks is identified with the global theorem

Alejandro Erickson, *Negative Correlation Properties for Matroids*, University of Waterloo M.Math. thesis (2008), permanent item `http://hdl.handle.net/10012/4165`.

The thesis states in its overview that Chapter 5 proves that **if all graphs are I-negatively correlated, then they are all I-Rayleigh**, and explicitly says this was "published independently by Cocks". Chapter 5 then supplies the construction: an edge weighting is approximated by graphic path-bundle substitutions. Proposition 5.2.2 requires the entire family of substituted matroids to be I-negatively correlated, and Corollary 5.2.3 concludes:

`graphs are all I-negatively correlated <=> graphs are all I-Rayleigh`.

This is precisely the class-level theorem reproduced by the B03 simple-gadget proof, not `one fixed G unit-good => that same M(G) weighted-good`.

### 3.3 Oxley textbook: again global class equivalence

James Oxley, *Matroid Theory*, 2nd ed., Oxford University Press (2011), Problem/Conjecture discussion around 15.8.14. Public author/reference PDF used in this run:
`https://www.math.ens.psl.eu/~benoist/refs/Oxley.pdf`.

Oxley states that Cocks proved that **the class of graphic matroids is independence-correlated iff Conjecture 15.8.14 holds for all graphs G**. Again this is class-level, not fixed-graph.

### 3.4 Cocks publisher abstract

Clifford C. Cocks, *Correlated Matroids*, CPC 17(4) (2008), 511--518, DOI `10.1017/S0963548308009152`.

The publisher abstract says the Grimmett--Winkler and Pemantle conjectures are equivalent to statements about correlated graphic matroids. The full proof body was not publicly accessible through the authorized source in this run; no paywall or permission bypass was attempted.

## 4. Decisive consistency test using Stark

Dudley Stark, *The Edge Correlation of Random Forests*, Annals of Combinatorics 15 (2011), 529--539, DOI `10.1007/s00026-011-0104-7`, proves the unit forest conjecture for `K_N` for all sufficiently large `N`.

Suppose the fixed-graph implication used by v3 were available in the literal strength

`F(G): unit pNC on G => M(G) weighted independence-correlated`.

Take an arbitrary finite simple graph `H` on `h` vertices. Choose `N>=h` large enough for Stark's theorem. Then:

1. `K_N` is unit-good by Stark;
2. `F(K_N)` would make `M(K_N)` weighted independence-correlated;
3. `H` plus `N-h` isolated vertices is a deletion subgraph of `K_N`;
4. Semple--Welsh Proposition 3.5 transfers weighted independence correlation to that deletion minor;
5. setting all surviving weights to one yields the unit forest inequality on `H`.

Thus **Stark + the literal fixed-graph Cocks implication + Proposition 3.5 would already prove the full all-graphs conjecture.** Yet post-2011 and current sources continue to state the all-graphs conjecture as open; for example current 2026 summaries still list it as open, and 2026 work by Tang--Zhang continues to obtain complete-graph-family results rather than an all-graphs theorem.

This is not itself a logical disproof of a theorem based on a web status label. It is a decisive source-consistency warning: interpreting the Semple--Welsh Note literally as the fixed-graph theorem would collapse a long-standing open problem using a 2011 partial result, while Erickson and Oxley both describe Cocks's published theorem as global. In a source-exact proof pipeline, the v3 bridge therefore fails.

## 5. New exact replacement theorem: the missing `K_n` weighted bridge is equivalent to the full target

The source audit can be turned into a clean mathematical equivalence that precisely locates the debt.

Fix distinct marked edges `e,f` in `K_n`. The independent-set Rayleigh difference

`Delta_{K_n}(e,f;y)`

is independent of the marked variables `y_e,y_f` by multiaffinity, so only the unmarked weights matter.

Consider the following statements.

**(A)** Every finite simple graph satisfies the unit uniform-forest pairwise inequality.

**(B)** For every `n`, every distinct `e,f in E(K_n)`, and every positive assignment `y` to the unmarked edges,

`Delta_{K_n}(e,f;y)>=0`.

**(C)** For every `n,e,f`, every simple path-bundle expansion `H` of `K_n` obtained by replacing each unmarked edge `g` by `k_g` internally disjoint paths of length `a_g>=2` (fresh internal vertices) while keeping `e,f` literal satisfies

`Delta_H(e,f;1)>=0`.

Then

`(A) <=> (B) <=> (C)`.

### (A) => (C)

Immediate: each `H` is a finite simple graph.

### (C) => (B)

Apply the exact path-bundle identity from fleet04/B03:

`Delta_H(e,f;1)=C^2 Delta_{K_n}(e,f;q)`

with `q_g=k_g/(2^{a_g}-1)`. These `q`-vectors are dense in the positive orthant. Since the Rayleigh difference is a polynomial, continuity extends nonnegativity to every positive `y`. Hence (B).

### (B) => (A)

Let `G` be any finite simple graph and let `e,f` be distinct edges of `G`. Embed `G` as a spanning subgraph of `K_n` after adding isolated vertices if desired. For each nonedge of `G`, assign weight `epsilon>0`; for every surviving unmarked edge of `G`, assign weight `1`. Statement (B) gives

`Delta_{K_n}(e,f;y(epsilon))>=0`

for every `epsilon>0`. As `epsilon -> 0+`, the independent-set polynomial and all relevant derivatives converge coefficientwise to those of `G`; therefore

`Delta_G(e,f;1)>=0`.

Thus (A).

### (B) => (C)

For any particular path-bundle expansion the same exact projection identity gives the unit difference as a positive square factor times `Delta_{K_n}(e,f;q)`, so (B) directly implies (C).

This proves the equivalence.

**Consequence.** The phrase "prove positive-weight `K_n`" is not a modest local strengthening of the complete-graph unit theorem. It is already **equivalent to the entire all-graphs conjecture**. Likewise, proving unit pNC for every required simple path-bundle expansion of `K_n` is equivalent to the whole target. This explains why the disputed fixed-graph Cocks step cannot be treated as a routine globalization lemma.

## 6. What remains valid

The following components are preserved:

- the exact unit theorem for each complete graph `K_n` from the lead's Hermite argument;
- Semple--Welsh Proposition 3.5 for the genuinely weighted independence-correlated class;
- fleet04/B03's simple path-bundle scaling identity and global class equivalence;
- fleet02/B02's conclusion that the first source-valid missing step is the weighted/gadget bridge;
- the exact separator algebra in newer fleet04/B01 r13 up to the point where it invokes fixed-graph Cocks.

What is **not** preserved as an unconditional theorem is any result whose final step requires `unit-good fixed H => weighted-good same H` without an independent proof.

## 7. Corrected end-to-end state

The honest chain is now

`exact unit pNC for every K_n`

`-> MISSING: weighted Rayleigh pNC for K_n (equivalently, unit pNC for every simple path-bundle expansion of K_n)`

`-> arbitrary simple G by epsilon-to-zero deletion specialization (or Semple--Welsh weighted minor closure)`.

By Section 5, the missing middle statement is equivalent to the parent FOREST conjecture itself. Therefore the previous v3 `FULL_PROOF_CANDIDATE` classification must be withdrawn pending direct primary-proof reconciliation or a genuinely new argument.

## 8. Outcome and failure evidence

**Outcome: `CANDIDATE_REFUTED` as written.**

- The FOREST conjecture remains open under the source record checked here.
- The complete-graph theorem is not refuted.
- The two previous end-to-end review PASSes do not rescue v3 because both accepted the same fixed-graph interpretation of the Semple--Welsh Note and did not reconcile it with Erickson/Oxley or the Stark consistency test.
- The original Cocks full proof body remains unavailable through the authorized public source; this run did not bypass access controls.
- The canonical fleet-login write in the control repository was denied by the platform safety layer and was not bypassed. Scoped scientific login/start records were created instead.
- No installation/benchmark work, email, Drive operation, public posting, paid/remote compute, workflow dispatch, permission change, scheduler mutation, production-population mutation, or unrelated private-data access occurred.
- Current-account inventory was inspected only from the authorized fleet01 snapshot: 20/20 managed slots were enabled/hourly-valid there, with exposed task email/notification flags false; no repair action was taken.

## 9. Recommended next mathematical mechanism

Do **not** spend another run merely rechecking the fixed-graph sentence. The next substantive route should attack the target directly through a mechanism that does not assume weighted `K_n`:

1. exploit the exact 3-connected/minimal-counterexample geometry that does not depend on fixed-graph Cocks, and combine it with the previously derived Simpson-reversal/matching constraints; or
2. derive a direct deletion comparison from `K_n` unit counts that uses only unit data, not hidden positive weights; or
3. find a concrete simple-graph counterexample to the proposed fixed-graph upgrade (a graph unit-good at `y=1` but with a negative weighted Rayleigh difference), which would definitively explain the Semple--Welsh Note discrepancy without touching the parent conjecture.

Any future use of Cocks must quote and verify the primary theorem/proof scope, not infer it from the ambiguous Note.
