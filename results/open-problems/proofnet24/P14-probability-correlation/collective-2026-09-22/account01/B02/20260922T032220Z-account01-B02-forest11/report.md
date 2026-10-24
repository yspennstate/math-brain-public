# FOREST account01/B02 — reversible marked-edge decomposition, alternate Hermite interval proof, and deletion-only closure audit

**Run:** `20260922T032220Z-account01-B02-forest11`  
**Programme:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** **FULL_PROOF_CANDIDATE** (internal candidate only; no public/external promotion)  
**Parent target:** FOREST  
**Context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact inputs consumed

I read the latest complete campaign-lead candidate `FOREST-KN-COCKS-RECONCILED-v3`, account01/B01 run `20260922T030948Z-b01-forest-auto11`, report blob `58b8b1d8ac522a4eda7479400820e590c12f22aa`.

I also consumed the named OTHER-account partner result account02/B03 run `20260922T022013Z-b03-forest-auto11`, report blob `b738b5381e0c4141d7f2a3a625f2647acb65bb1a`. Its load-bearing correction is that contraction-created parallel classes may be aggregated only by **summing** class weights and tracking a marked original member by the corresponding derivative; replacing a parallel class by a unit edge can reverse a Rayleigh cross-gap. Its book graphs show that the exact Simpson separator budget is sharp.

The lead's v3 proof does not need contraction in the final all-graphs transfer: after the weighted upgrade on `K_n`, only **deletion** of nonedges is required. I make that deletion transfer explicit below, thereby applying the partner warning rather than silently simplifying any induced parallel class.

## 2. Compact end-to-end chain being audited

The current candidate is:

1. prove the unit-weight forest Rayleigh inequality for every complete graph `K_n`;
2. use the fixed-graph Cocks implication recorded in the final Semple--Welsh paper, `unit Conjecture 1.1 on G => M(G) independence correlated`, on each `K_n`;
3. delete the nonedges of an arbitrary finite simple `G` from a sufficiently large `K_n` and take the exact positive-weight deletion limit;
4. set all surviving weights equal to one.

This run independently rederives the complete-graph marked-pair counting and gives a self-contained alternative proof of the Hermite interval estimate used in step 1. It also proves step 3 directly, without invoking contraction or parallel simplification.

## 3. Reversible marked-edge decomposition on `K_n`

Let

`R = z exp(R)`, `T = R-R^2/2`, `F=exp(T)`, `A=exp(R)`.

Here `R` is the EGF of rooted labelled trees, `F` the EGF of labelled forests, and `A=exp(R)` is the EGF for the branches incident to one already-labelled distinguished root.

### 3.1 One marked edge

Fix `e={1,2}`. From a forest containing `e`, delete `e`. Acyclicity implies that the tree containing `e` splits into exactly two components, one rooted at 1 and one at 2. Conversely, joining those two distinguished components by `e` creates a tree and cannot create a cycle. The operation is literally reversible with multiplicity one. Hence

`E_n=(n-2)![z^(n-2)] F A^2`.

### 3.2 Adjacent marked pair

Fix `e={1,2}`, `f={1,3}`. A forest containing both has them in the same tree. Deleting both produces exactly three components containing 1,2,3 separately. Conversely, adding the two marked edges makes their component quotient a 3-vertex tree. Again the map and inverse have multiplicity one, so

`J_adj,n=(n-3)![z^(n-3)] F A^3`.

### 3.3 Disjoint marked pair

Fix `e={1,2}`, `f={3,4}`. Delete both marked edges.

* If the two marked edges were in different tree components, the deletion produces four distinct distinguished components. This is the `F A^4` term.
* If they were in the same tree, deleting two edges from a tree produces exactly three components. The component quotient under `{e,f}` is a path of length two. Its unique middle component contains exactly one endpoint of `e` and exactly one endpoint of `f`; there are exactly `2*2=4` choices, recoverable from the original forest. The middle component is a tree with two fixed distinguished vertices. Decomposing its unique distinguished-vertex path gives `A^2(1+R+R^2+...)=A^2/(1-R)`. The two outer distinguished components contribute another `A^2`.

Conversely, adding `e,f` to either construction gives respectively two disjoint quotient edges or a 3-component quotient path, so acyclicity is automatic and the inverse is unique. Therefore

`J_dis,n=(n-4)![z^(n-4)] F A^4 (1+4/(1-R))`.

This supplies the requested multiplicity/acyclicity proof rather than assuming a local swap is injective.

## 4. Independent Cauchy--Hermite reduction

For `m>=0`, Cauchy's formula with `z=R exp(-R)` and `dz=exp(-R)(1-R)dR` gives

`m![z^m] F A^p = He_m(x)-m He_(m-1)(x)`,  `x=m+p+1`,

where `He_j` is the probabilists' Hermite polynomial, because

`exp(xR-R^2/2)=sum_j He_j(x) R^j/j!`.

For the extra factor `(1-R)^(-1)` in the same-tree disjoint case, the Jacobian factor `1-R` cancels exactly, giving `m![z^m]FA^4/(1-R)=He_m(x)`.

Set `k=n-4`, `x=n+1`, `a=He_k(x)` and

`s = k He_(k-1)(x)/He_k(x) = He'_k(x)/He_k(x)`.

The recurrence `He_(j+1)=x He_j-j He_(j-1)` then gives exactly

`J_dis=a(5-s)`,  `J_adj=a(4-s)`,

`E=a(2n+6-3s)`,

`Z=a(n^2+3n+10-(n+4)s)`.

Thus

`Delta_dis/a^2 = G_n(s)`

with

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`,

and also the exact signed identity

`Delta_adj = Delta_dis + Z a`.

So the disjoint orbit is the harder one.

## 5. Alternate self-contained proof of the needed Hermite interval

The lead used `L_n <= s < 1`. Here is a second derivation that removes any dependence on an informal coefficient-positivity assertion for the upper endpoint.

The roots `lambda_i` of `He_k` are real and symmetric about zero. The standard Jacobi matrix for `He_k` has zero diagonal and off-diagonal entries `sqrt(1),...,sqrt(k-1)`, hence every root satisfies

`|lambda_i| < 2 sqrt(k)`

by the maximum row-sum bound. Since `x=k+5`, all denominators below are positive and `a>0`.

By logarithmic differentiation,

`s=sum_i 1/(x-lambda_i)`.

Pairing roots `+lambda,-lambda`, and using `1/(1-u)>=1+u` for `0<=u<1`,

`1/(x-lambda)+1/(x+lambda) = 2x/(x^2-lambda^2) >= 2/x + 2lambda^2/x^3`.

A zero root, when present, contributes `1/x`. Since `sum_i lambda_i^2=k(k-1)` (read from the `x^(k-2)` coefficient of `He_k`),

`s >= k/x + k(k-1)/x^3`

`   = (n-4)(n-1)(n+4)/(n+1)^3 =: L_n`.

For the upper bound use the same paired identity and `lambda_i^2<4k`:

`s < k/x + k(k-1)/(x(x^2-4k))`.

With `x=k+5`, this is `<1` because it is equivalent to

`k(k-1) < 5((k+5)^2-4k) = 5(k^2+6k+25)`,

which is immediate for `k>=0`. Hence rigorously

`L_n <= s < 1`.

For `n>=6`, `G_n'(s)` is positive on `[0,1]` because its minimum there is

`G_n'(1)=n^2-6n+4>0`.

Therefore `G_n(s)>=G_n(L_n)`, and direct simplification gives

`(n+1)^6 G_n(L_n)=P(n)`

`P(n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

Writing `n=t+6`,

`P(t+6)=2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396>0`.

The remaining complete-graph cases are exact: `K_3` adjacent gap `2`, `K_4` disjoint gap `6`, `K_5` disjoint gap `210`. Thus the complete-graph unit theorem survives this independent derivation.

## 6. Direct deletion-only transfer; no parallel-edge hazard

Assume step 2 supplies weighted independence correlation for `M(K_n)`. Let `G` be a simple spanning subgraph of `K_n` (isolated extra vertices do not matter), with surviving edge weights `y_h>0`. Give every deleted nonedge weight `epsilon>0` in `K_n`. For any surviving marked pair `e,f`, the weighted forest Rayleigh difference

`Delta_Kn(e,f; y,epsilon)`

is a polynomial in `epsilon` and is nonnegative for every `epsilon>0`. As `epsilon -> 0+`, every forest using a deleted edge vanishes termwise, so

`lim_(epsilon->0+) Delta_Kn(e,f;y,epsilon)=Delta_G(e,f;y)>=0`.

This proves exactly the deletion step needed by the lead. It never contracts an edge and therefore never creates a parallel class. The account02/B03 book-graph warning is therefore fully respected: its contraction pathology is real, but it is not present in this final transfer route.

Setting all surviving `y_h=1` gives the source uniform law on all acyclic edge subsets.

## 7. Source-scope check on the Cocks bridge

The final Semple--Welsh paper explicitly records in its Section 5 Note that Cocks showed: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. That is exactly the fixed-graph implication needed in step 2. The same final paper's Proposition 3.5 proves weighted minor closure by the `epsilon->0+` deletion and scaled `epsilon->infinity` contraction limits.

I also checked Alejandro Erickson's 2008 Waterloo thesis, which presents a **different** gadget proof (Proposition 5.2.2 / Corollary 5.2.3) that establishes the global equivalence `all graphs I-negative correlated <=> all graphs I-Rayleigh`, using two-sum gadgets realizing a dense set of positive activities. Erickson describes this as independently obtained alongside Cocks. That global gadget proof by itself is weaker than the fixed-graph statement and must **not** be substituted for the final Semple--Welsh attribution in the lead chain. It does not contradict the final Note, but it makes direct inspection of the Cocks proof body a worthwhile publication-stage source check.

Sources checked:

* Charles Semple and Dominic Welsh, *Negative Correlation in Graphs and Matroids*, CPC 17 (2008), 423--435, DOI 10.1017/S0963548307008978; especially Proposition 3.5 and the Section 5 Note.
* Clifford C. Cocks, *Correlated Matroids*, CPC 17 (2008), 511--518, DOI 10.1017/S0963548308009152; accessible abstract confirms the paper proves equivalences with correlated graphic-matroid statements, but the full proof body was not available in this run.
* Alejandro Erickson, *Negative Correlation Properties for Matroids*, MMath thesis, University of Waterloo (2008), Proposition 5.2.2 and Corollary 5.2.3.

## 8. Exact regression certificate

`hermite_audit.py` is a standard-library exact-rational checker. It independently constructs the truncated EGFs `R,T,F,A`, compares the EGF counts with the Hermite formulas for every `n=4,...,30`, checks both Rayleigh-gap identities, checks `L_n<=s<1`, and checks exact positivity. It executed 271 exact assertions and ended `STATUS=PASS`. This computation is regression evidence only; the proof is the symbolic argument above.

## 9. Honest status

**FULL_PROOF_CANDIDATE**, matching the lead's current internal classification. This run found no mathematical counterexample or algebraic failure in the complete-graph step; instead it supplied a second, self-contained Hermite interval proof and an exact deletion-only closure that avoids the partner's parallel-edge obstruction.

I do **not** upgrade the result to an established/public theorem. The remaining validation-sensitive item is bibliographic rather than a missing displayed implication: inspect the primary Cocks proof body (or a journal-grade source reproducing the fixed-graph proof) before any external claim. If that primary source does not in fact prove the fixed-graph statement recorded by Semple--Welsh, step 2 must be reopened immediately; the Erickson global gadget proof does not repair it without already knowing the conjecture on the gadget graphs.
