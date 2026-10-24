# FOREST / account01 B01 — complete-graph reduction plus exact Hermite proof on `K_n`

**Candidate version:** `FOREST-KN-HERMITE-REDUCTION-v1`  
**Run outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent Grimmett–Winkler conjecture:** **OPEN pending review gate**  
**FULL_PROOF_CANDIDATE:** **false at this stage solely because the collective protocol requires two independent existing-worker end-to-end reviews before promotion.**  
**Brain context:** `WITHOUT_VERIFIED_BRAIN`.

This report contains an end-to-end mathematical candidate, but does **not** promote it to a solved/open-problem claim. The first job for the next two independent FOREST reviewers is to attack the two high-leverage steps: (i) the fixed-graph Cocks implication plus minor closure, and (ii) the complete-graph Hermite coefficient proof below.

## 1. Exact source scope and dependencies consumed

The source is the forest half of Grimmett–Winkler / Grimmett Conjecture 4.2: for a finite simple graph `G`, choose uniformly from **all** acyclic edge subsets, with every forest size present and disconnected forests allowed. For distinct present edges `e,f`, prove

`P(e,f in F) <= P(e in F) P(f in F)`.

Equivalently, with `Z` the number of forests, `Z_e` the number containing `e`, and `Z_ef` the number containing both,

`Delta_G(e,f) := Z_e Z_f - Z Z_ef >= 0`.

Only essential inherited dependencies were used.

1. Latest lead handoff: account01/B01, blob `498b6154449ed3028685e6c174cb5563b0478bde`, candidate `FOREST-SIMPSON-MATCHING-v1`. It proves the strict external-negative / matching geometry for a lexicographically minimal counterexample. I do not rebuild it here.
2. Overlap/reconnection identity: account01/B03, blob `b49c6b896238cd62508b98549526dd12a469ceb3`,
   `Delta=n10*n01-n00*n11+N*q`. This remains an exact source-valid local coordinate but becomes unnecessary if the global complete-graph reduction below is valid.
3. Named **OTHER-account result consumed and applied**: account02/B03, `FOREST-2SEP-WEIGHTED-TRANSFER-v1`, blob `5001e9cc0fb18f77c85ad0bb99d100da5937a1c0`. It proves exact two-separator transfer and shows why arbitrary induced boundary weights, not unit replacements, are required. This motivated checking the strongest available all-positive-weight theorem dependency rather than continuing a unit-only separator switching.
4. Assigned partner account02/B02 report, blob `c4df51c04673a212d591f6a4d218e28ebec60f19`, proves complete log concavity / PSD Rayleigh matrix consequences but correctly does not infer entrywise Rayleigh signs.
5. R02/P0001 handoff, blob `1b9109cc2ad960a6845940d85fb27adc24335926`, records the fixed-graph Cocks/Semple–Welsh minor-closure route and a cubic-completion partial theorem. It also correctly retires R02 source ownership in favor of the predating P14 track.
6. P14 source audit `proofnet24/P14-probability-correlation/runs/2026-09-17/2026-09-17T04-40-00Z__report.md` records the decisive published scope correction: the final Semple–Welsh paper states that Cocks proved **if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated**. Semple–Welsh Proposition 3.5 proves independence-correlated matroids are closed under minors.

The named account02/B03 two-separator result is applied as follows: its arbitrary positive virtual weight is exactly the kind of obstacle that disappears if the fixed-graph unit statement on a supergraph can be upgraded to all positive weights and then passed to deletions/minors. This prompted the complete-graph reduction in §2.

## 2. First missing all-graphs implication: all graphs reduce to complete graphs

This is the decisive comparison.

### Lemma 2.1 — complete-graph reduction, conditional only on the published fixed-graph Cocks theorem

Assume the unit forest inequality holds for `K_n` for every `n`. Then it holds for every finite simple graph.

### Proof

Fix `n`. The final Semple–Welsh note records Cocks's theorem:

> If Conjecture 1.1 holds for a graph `G`, then the graphic matroid `M(G)` is independence correlated.

Here Conjecture 1.1 is exactly the unit uniform-all-forests inequality. Therefore the unit theorem for `K_n` upgrades `M(K_n)` to the **all-positive-weight** independence-correlated property.

Semple–Welsh Proposition 3.5 says independence-correlated matroids are closed under minors. Every finite simple graph `G` with vertex set of size at most `n` is obtained from `K_n` by deleting the edges not present in `G` (isolated vertices are irrelevant to the graphic matroid and to forest counts). Hence `M(G)` is a deletion minor of `M(K_n)` and is independence correlated. Setting all surviving edge weights equal to one gives the source inequality for `G`.

Thus the source conjecture reduces to a single symmetric family:

`prove unit forest pairwise negative correlation on K_n for every n`.

No two-separator induction, bounded graph census, or positive-weight approximation is used in this reduction. The all-positive-weight upgrade is the published fixed-graph Cocks theorem itself.

## 3. Exact complete-graph forest enumeration

I now prove the unit inequality on `K_n` for every `n` by exact labelled-tree generating functions.

Let

`R(z)=sum_{m>=1} m^(m-1) z^m/m!`

be the rooted labelled-tree EGF. Cayley's/Lagrange's standard equation is

`R = z exp(R)`.

Let

`T(z)=R-R^2/2`

be the unrooted labelled-tree EGF and

`F(z)=exp(T(z))`

be the labelled-forest EGF. Put

`A(z)=T'(z)=exp(R)=R/z`.

`A` is the EGF of a tree containing one prescribed distinguished vertex, with all other vertices labelled from the ordinary variable.

For `K_n`, symmetry leaves one one-edge count and two two-edge orbits: adjacent and disjoint marked edges.

### 3.1 Total forests

`Z_n = n! [z^n] F(z)`.

### 3.2 One marked edge

Fix `e={1,2}`. A forest containing `e`, after deleting `e`, gives two rooted tree components rooted at `1` and `2`, plus an arbitrary forest on the remaining components. Conversely this construction is unique. Hence

`E_n := Z_e = (n-2)! [z^(n-2)] F A^2`.

### 3.3 Adjacent marked pair

Fix `e={1,2}`, `f={1,3}`. A forest containing both, after deleting the two marked edges, gives three rooted tree components rooted at `1,2,3`, plus an arbitrary remaining forest. Therefore

`J_adj,n := Z_ef = (n-3)! [z^(n-3)] F A^3`.

### 3.4 Disjoint marked pair

Fix `e={1,2}`, `f={3,4}`. There are two disjoint cases.

**Different tree components.** Deleting the two marked edges gives four rooted tree components rooted at `1,2,3,4`; contribution

`F A^4`.

**Same tree component.** Deleting the two marked edges from that tree gives exactly three components. One middle component contains one endpoint of each marked edge; there are four choices of the endpoint pair. The two outer components are one-rooted trees. The middle component is an unrooted tree with two prescribed distinguished vertices, whose EGF is

`T''(z)=A'(z)=A^2/(1-R)`.

Thus the same-tree contribution is

`4 F A^2 T'' = 4 F A^4/(1-R)`.

Hence

`J_dis,n = (n-4)! [z^(n-4)] F A^4 (1+4/(1-R))`.

This decomposition was independently brute-regressed in exact integer arithmetic through `K_6`; see §8.

## 4. Hermite coefficient evaluation

Let `He_m(x)` be the probabilists' Hermite polynomial,

`exp(xu-u^2/2)=sum_{m>=0} He_m(x) u^m/m!`,

with recurrence

`He_(m+1)(x)=x He_m(x)-m He_(m-1)(x)`.

For `a>0` define

`C_m(a)=m![z^m] exp(aR-R^2/2)`.

Lagrange inversion applied to `R=z exp(R)` gives, for `x=m+a`,

`C_m(a)=He_m(x)-m He_(m-1)(x)`.

A direct Cauchy change of variable `z=u exp(-u)` also gives

`m![z^m] exp(aR-R^2/2)/(1-R)=He_m(m+a)`.

For all four forest counts above the Hermite argument is the same:

`x=n+1`.

Write

`H_j := He_j(n+1)`,
`D_j := H_j-j H_(j-1)`.

Then

`Z_n=D_n`,
`E_n=D_(n-2)`,
`J_adj,n=D_(n-3)`.

Set `k=n-4`. The disjoint formula becomes

`J_dis,n = D_k + 4 H_k = 5H_k-kH_(k-1)`.

By the Hermite recurrence,

`J_adj,n = 4H_k-kH_(k-1)`,

so

`J_dis,n = J_adj,n + H_k`.

Therefore the **disjoint pair is always the harder orbit**: once

`E_n^2 >= Z_n J_dis,n`

is proved, the adjacent inequality follows strictly for `n>=4` because `Z_n H_k>0`.

## 5. Reduction to a one-variable polynomial inequality

For `n>=4`, set

`k=n-4`, `x=n+1=k+5`, `a=H_k`,

and

`s := k H_(k-1)/H_k = H_k'(x)/H_k(x)`.

The recurrence reduces all four counts to

`J_dis,n = a(5-s)`,

`J_adj,n = a(4-s)`,

`E_n = a(2n+6-3s)`,

`Z_n = a(n^2+3n+10-(n+4)s)`.

Therefore

`E_n^2-Z_n J_dis,n = a^2 G_n(s)`,

where

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

It remains to prove `G_n(s)>0` for `n>=6`; the small cases are in §7.

## 6. A self-contained Hermite root bound forces `G_n(s)>0`

All roots `lambda_i` of `He_k` are real and symmetric about zero. One standard self-contained realization is that they are the eigenvalues of the symmetric `k x k` Jacobi matrix with off-diagonal entries `sqrt(1),...,sqrt(k-1)`. Gershgorin therefore gives

`|lambda_i| < 2 sqrt(k) < k+5=x`.

Hence `H_k(x)>0`, and the logarithmic derivative is

`s=H_k'(x)/H_k(x)=sum_i 1/(x-lambda_i)`.

The Hermite coefficient of `x^(k-2)` (or the Jacobi trace identity) gives

`sum_i lambda_i^2 = k(k-1)`.

Pair the symmetric roots `+/-lambda`. For every pair,

`1/(x-lambda)+1/(x+lambda)`
`=2x/(x^2-lambda^2)`
`>=2/x+2lambda^2/x^3`.

The possible zero root contributes exactly `1/x`. Summing yields

`s >= k/x + k(k-1)/x^3`.

With `k=n-4`, `x=n+1`, this is

`L_n := (n-4)(n-1)(n+4)/(n+1)^3 <= s`.

We also need `s<1`. But

`H_k-kH_(k-1)=k![z^k] exp(5R-R^2/2)=k![z^k] F A^4 > 0`,

so `H_k(1-s)>0`, hence

`0 <= s < 1`.

For `n>=6`,

`G_n'(s)=2(5-n)s+n^2-4n-6`.

Because its slope is nonpositive in `s`, its minimum on `[0,1]` is at `s=1`, where

`G_n'(1)=n^2-6n+4>0`.

Thus `G_n` is increasing on the entire admissible interval and

`G_n(s) >= G_n(L_n)`.

Exact simplification gives

`G_n(L_n)=P(n)/(n+1)^6`,

with

`P(n)=2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

Put `n=t+6`. Then

`P(t+6)=2t^6+142t^5+3147t^4+33233t^3+187651t^2+551661t+666396`.

Every coefficient is strictly positive. Hence `P(n)>0` for all `n>=6`, and therefore

`E_n^2-Z_n J_dis,n >0` for every `n>=6`.

As `J_dis,n=J_adj,n+H_k` with `H_k>0`, the adjacent pair gap is even larger.

## 7. Exact small cases

The only remaining complete graphs are immediate exact counts:

- `K_2`: only one edge, so there is no distinct edge pair.
- `K_3`: `(Z,E,J_adj)=(7,3,1)`, gap `3^2-7*1=2`.
- `K_4`: `(Z,E,J_adj,J_dis)=(38,14,4,5)`, disjoint gap `14^2-38*5=6`.
- `K_5`: `(Z,E,J_adj,J_dis)=(291,93,23,29)`, disjoint gap `93^2-291*29=210`.

Thus the unit all-forest pairwise inequality holds for `K_n` for every `n`.

## 8. Exact computational audit

The proof above is symbolic. The computation is a regression/audit only.

Checker:
`forest_kn_hermite_checker.py`

SHA-256 of executed source:
`c72f54f037f68967d59eb0684e11102fd2455621f16b95f31789f48958f7ec1c`

Archived output:
`forest_kn_hermite_checker.out`

SHA-256 of captured output:
`22d457587944021fdd86373df96b8106ec12665c111ae1cbd6752f54c5fe1c35`

The checker:

1. brute-enumerates every edge subset of `K_n`, `2<=n<=6`, rejects cycles by exact union-find, and confirms the EGF/Hermite formulas exactly;
2. verifies the small exact Rayleigh gaps;
3. checks the derived integer/rational identities, `s` bounds, `G_n(s)` identity, polynomial shift, and positive adjacent/disjoint gaps for every `6<=n<=500` using exact integer/Fraction arithmetic.

Captured terminal line: `ALL_EXACT_CHECKS_PASS`.

This is not used to replace the all-`n` proof.

## 9. Conditional end-to-end conclusion

Combining §§2–7 gives the following candidate theorem.

> **Candidate theorem.** Every finite simple graph `G` satisfies the Grimmett–Winkler pairwise negative-correlation inequality for the uniform law on all forests.

The logical chain is short:

1. exact Hermite argument -> unit forest pNC for every `K_n`;
2. Cocks fixed-graph theorem -> `M(K_n)` is independence correlated for all positive edge weights;
3. Semple–Welsh Proposition 3.5 -> every deletion minor of `M(K_n)` is independence correlated;
4. every finite simple `n`-vertex graph is a deletion subgraph of `K_n`;
5. set the surviving weights to one -> source inequality for arbitrary `G`.

No unproved separator comparison remains **if** the Cocks fixed-graph theorem is read exactly as the final Semple–Welsh note states.

## 10. Why this is not yet promoted

The collective protocol requires two independent existing-worker end-to-end reviews before a full candidate can be promoted. This run has not received those reviews. Therefore the honest status is

`ESSENTIAL_STEP_APPLIED`, parent operational status `OPEN`, `FULL_PROOF_CANDIDATE=false`.

The next reviewers should independently verify, in this order:

1. Semple–Welsh's final note and Cocks's fixed-graph scope: **unit Conjecture 1.1 on one graph `G` -> all-positive-weight independence correlation of `M(G)`**.
2. Proposition 3.5 minor closure and the fact every simple `G` is a deletion restriction of `K_n`.
3. The disjoint-pair decomposition `F A^4(1+4/(1-R))`.
4. The two coefficient identities from Lagrange/Cauchy inversion.
5. The Hermite root/log-derivative lower bound and the exact polynomial `P(n)`.

A failure in item 1 would kill the all-graphs reduction but leave the all-`K_n` theorem intact. A failure in items 3–5 would kill the new complete-graph proof. No such failure was found in this run.

## 11. Source/current-status caution

The source was still treated as open in the inherited campaign state and in recent special-case literature. I do **not** infer external novelty from a search miss, and I do not claim publication priority here. This report is an internal proof candidate awaiting independent mathematical review.

No brain installation, benchmark, production state, email, Drive, public posting, workflow, permission, or paid/remote-compute action was performed.
