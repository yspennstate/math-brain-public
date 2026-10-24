# FOREST / account04-B02 — component-reservoir coupling, exact Hermite bridge, and a K5 no-go for q-only routing

Run: `20260922T030824Z-account04-B02-forest-exchange-v1`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED** with a subsidiary **CANDIDATE_REFUTED**  
Parent status: **FULL_PROOF_CANDIDATE exists in the team; not promoted here to an established/public theorem**  
Execution context: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact scope and live peer inputs

The source target is the Grimmett--Winkler unit-weight uniform-unrooted-forest inequality: for every finite simple graph `G`, every two distinct edges `e,f`, and `F` uniform over every acyclic edge subset of `G` (all sizes, disconnected forests included),

`Pr(e,f in F) <= Pr(e in F) Pr(f in F)`.

I read the current team lead's complete candidate

`account01/B01/20260922T012234Z-account01-B01-forest-r11/hermite_complete_graph_reduction_report.md`, blob `e11be369a70e59449ea744da6f1e32040889c216`, candidate `FOREST-KN-HERMITE-REDUCTION-v1`.

Its end-to-end chain is:

1. prove the unit inequality for every complete graph `K_n` by exact labelled-forest/Hermite formulas;
2. use Cocks's fixed-graph implication to upgrade unit pNC for `K_n` to positive-weight independence correlation of `M(K_n)`;
3. use Semple--Welsh Proposition 3.5 (minor closure of independence-correlated matroids);
4. every finite simple graph on at most `n` vertices is an edge-deletion minor of `K_n`; then specialize surviving weights to one.

I independently checked the two externally delicate source statements in the final Semple--Welsh paper, *Negative Correlation in Graphs and Matroids*. Proposition 3.5 explicitly states that independence-correlated matroids are closed under minors. The final Section 5 Note explicitly says that Cocks showed: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. These are the fixed-graph and minor statements the lead actually needs, not merely a class-level paraphrase. Source locator: final author PDF `SW07.pdf`, printed pp. 6--7 for Proposition 3.5 and printed p. 13 for the Note; Cocks, *Correlated Matroids*, CPC 17 (2008), 511--518, DOI `10.1017/S0963548308009152`.

The required named partner result is account01/B03

`20260921T234923Z-b03-poprestore-r11/overlap_reconnection_report.md`, blob `4dbaa2d764eddbc02026736e5b1fe265ba14f24d`.

For `K=G-{e,f}`, a forest `H` of `K`, and addability indicators `X,Y`, let `n_ij` count the four `(X,Y)` cells, `N=sum n_ij`, and let `q` count the `A_11` forests for which `H+e+f` is cyclic. The partner proves the exact identity

`Delta = n10*n01 - n00*n11 + N*q`.                                      (P)

Equivalently, `Q` is the event that `e` and `f` join the same unordered pair of components of `H`.

I also consumed the named OTHER-account result account03/B01

`20260922T023025Z-account03-B01-forest-r11/second_end_to_end_review.md`, blob `ea161f8956619130775dd7b638d3f87408624941`, outcome `FULL_PROOF_CANDIDATE / INDEPENDENT_END_TO_END_REVIEW_PASS_2`. It independently rederived the complete-graph formulas, verified the fixed-graph Cocks bridge from the final source, and records that account03/B02 already supplied review pass 1. I use that result here by treating the lead chain as a live full proof candidate and attacking a genuinely different *direct coupling* route rather than repeating a third analytic review.

My immediately preceding B02 run, blob `70dd12f1c272a763642737810ecf5505b9f9438f`, refuted every coupling that preserves the full per-edge multiplicity fibre and left the exact residual product target

`A00 x D -> (A10 x A01) disjoint-union (A10 x Q) disjoint-union (D x Q) disjoint-union (Q x A01) disjoint-union (Q x Q)`,       (R)

where `D=A11\Q`. The present run changes mechanism: it factors the overlap reservoir by terminal-bearing components and carries those exact component multiplicities into the lead's EGF/Hermite variables.

## 2. A genuine component-reservoir bijection on K_n

Write the standard labelled-tree/forest series

`R = z exp(R)`, `T=R-R^2/2`, `F=exp(T)`, `A=T'=exp(R)`.

A tree containing two prescribed distinguished vertices has EGF

`T'' = A^2/(1-R)`.

This follows by differentiating `T'=A` and is also the direct labelled count: on `m+2` prescribed-plus-free vertices there are `(m+2)^m` trees.

### Adjacent marks

Let `e=ab`, `f=ac`. By the partner's quotient-component characterization, an overlap state `H in Q` has exactly one component containing `a` and a distinct component containing `b,c`; every other component is free. Hence there is a literal labelled-component bijection

`Q_adj  <->  FOREST(free labels) x TREE[a] x TREE[b,c]`.

Therefore

`q_adj(n) = (n-3)! [z^(n-3)] F * A * T''`

`          = (n-3)! [z^(n-3)] F A^3/(1-R)`.                    (2.1)

Retaining component sizes rather than suppressing them gives the exact multiplicity sum

`q_adj(n) = sum_{r>=1,s>=2,r+s<=n}`

` (n-3)!/((r-1)!(s-2)!(n-r-s)!) * r^(r-2) s^(s-2) F_(n-r-s)`,  (2.2)

with the one-vertex tree count interpreted as one.

### Disjoint marks

Let `e=ab`, `f=cd`. The overlap state has one of exactly two cross pairings of the four terminals:

`ac | bd` or `ad | bc`,

and the paired blocks must lie in two distinct tree components. Thus

`Q_dis <-> {two cross pairings} x FOREST(free labels) x TREE[pair 1] x TREE[pair 2]`,

so

`q_dis(n) = 2 (n-4)! [z^(n-4)] F (T'')^2`

`          = 2 (n-4)! [z^(n-4)] F A^4/(1-R)^2`.                (2.3)

Equivalently,

`q_dis(n) = 2 sum_{r,s>=2,r+s<=n}`

` (n-4)!/((r-2)!(s-2)!(n-r-s)!) * r^(r-2) s^(s-2) F_(n-r-s)`.  (2.4)

These are actual component decompositions, not heuristic independence assumptions. They preserve the exact sizes and tree multiplicities of both terminal-bearing components and the exact unrooted-forest multiplicity on all unused labels.

## 3. Exact Hermite formulas for the partner's overlap reservoir

The lead uses the Cauchy substitution `z=u exp(-u)` and the probabilists' Hermite polynomials `He_j`. Applying the same substitution to (2.1) gives, with `m=n-3`,

`q_adj(n) = He_(n-3)(n+1)`.                                      (3.1)

For the disjoint case, let `m=n-4`. The Jacobian cancels one of the two factors `(1-u)^(-1)`, leaving

`q_dis(n) = 2 m! [u^m] exp((n+1)u-u^2/2)/(1-u)`

`         = 2 m! sum_{j=0}^m He_j(n+1)/j!`.                     (3.2)

This is the exact analytic value of the B03 overlap reservoir inside the same Hermite coordinate system used by the lead. In particular, the overlap reservoir is **not** the lead's `same-tree` term in `J_dis`: the latter carries `4/(1-R)`, whereas `q_dis` carries `2/(1-R)^2`. On `K_4` the distinction is already numerical: `q_dis=2`, while the full both-edge count is `J_dis=5`.

## 4. Exact formula-level reconciliation with the lead candidate

For either orbit in `K_n`, let

- `Z` be the number of all forests;
- `E=Z_e=Z_f` by symmetry;
- `J=Z_ef`;
- `q` be the partner overlap count in `K_n-{e,f}`.

Deleting/adding the marked edges gives exact identities

`N = Z - 2E + J`,

`n11 = J + q`,

`n10 = n01 = E - 2J - q`,

`n00 = Z - 4E + 4J + q`.                                      (4.1)

For example `n11=J+q` because the individually-addable cell splits disjointly into `D` (both additions remain acyclic), whose size is exactly `J`, and `Q`, whose size is `q`.

Substitution of (4.1) into the partner identity (P) cancels every `q` term and gives identically

`n10*n01 - n00*n11 + N*q = E^2 - Z*J`.                        (4.2)

Thus the partner's overlap-reconnection comparison and the lead's two-orbit Hermite comparison are not merely compatible; on complete graphs they are the same integer gap under an explicit component-reservoir change of coordinates.

This also pinpoints how the lead's analytic proof pays the coupling obstruction. The `q` reservoir is indispensable in the base-forest coordinates, but after one passes to the full-forest orbit counts `(Z,E,J)`, its contribution is absorbed exactly into the change of coordinates (4.1).

## 5. A decisive no-go: q-only defect routing already fails on K5

The previous residual coupling (R) contains two qualitatively different target channels:

1. the ordinary switch channel `A10 x A01`, of cardinality `n10*n01`;
2. the overlap reservoir channels, of total cardinality `q(N-n00)` after the canonical cancellations.

A tempting component-coupling simplification is to route **all** of `A00 x D` only into the overlap reservoir, i.e. to seek

`n00*|D| <= q(N-n00)`.                                         (Q-only)

This is false even for a complete graph.

Take `G=K_5` and disjoint marked edges. Exact enumeration gives

`(n00,n10,n01,n11,q)=(49,21,21,43,14)`.

Here `D=n11-q=29` and `N=134`. Hence

`n00*|D| = 49*29 = 1421`,

while

`q(N-n00) = 14*(134-49) = 1190`.

The q-only target is short by exactly `231`.

The partner's actual comparison survives because the ordinary switch channel contributes

`n10*n01 = 21^2 = 441`,

so the full target has `1190+441=1631` places and the resulting Rayleigh slack is

`1631-1421 = 210 = E^2-ZJ`.

This is a source-valid counterexample to `FOREST-Q-ONLY-DEFECT-ROUTING-v1`, **not** to the Grimmett--Winkler conjecture. It is also minimal inside the disjoint complete-graph orbit: `K_4` has `20 <= 22` for q-only routing, while `K_5` is the first possible larger complete graph and fails.

Consequently a direct coupling proof cannot merely cross multiplicity fibres and dump every defect into `Q`. For disjoint marks it must use the `A10 x A01` switch channel and the overlap reservoir together. This is exactly the two-term structure retained by the partner's (R4), so no valid future coupling should discard either term.

## 6. Conditional end-to-end argument and the remaining coupling obligation

The team's current conditional end-to-end proof is compact:

`complete-graph unit pNC for all n`

`=> [Cocks fixed-graph theorem] M(K_n) independence correlated`

`=> [Semple--Welsh Prop. 3.5] every deletion minor independence correlated`

`=> every finite simple graph G has unit uniform-forest pNC`.

The lead supplies the first line by exact Hermite positivity, and two existing independent workers have now recorded end-to-end review passes. I found no new source mismatch in the fixed-graph/minor bridge; the final Semple--Welsh source says exactly what the lead needs. Accordingly I do **not** invent an unpaid universal arrow in that analytic candidate.

For the **assigned direct coupling route**, however, the first genuine unpaid implication remains the residual Hall/exchange map (R). This run advances that route in two ways:

- it gives an exact component-factorized coupling representation of every `Q` state, including closed formulas in the lead's Hermite variables;
- it proves that a q-only Hall strategy is impossible already on disjoint `K_5`, so the ordinary `A10 x A01` switch channel must remain live.

The next coupling attempt should therefore build a two-channel flow whose inverse multiplicities are indexed simultaneously by terminal-component sizes and by a recoverable switch edge; it should not return to same-fibre recolouring and should not try to pay every defect solely from `Q`.

## 7. Exact executable check

`component_reservoir_checker.py` independently does all of the following with integer/rational arithmetic only:

1. brute-enumerates the partner `(n00,n10,n01,n11,q)` cells in `K_n-{e,f}` for adjacent marks through `n=6` and disjoint marks through `n=6`;
2. independently brute-enumerates full `(Z,E,J)` counts in `K_n`;
3. checks the component-size sums (2.2)/(2.4) and the Hermite formulas (3.1)/(3.2);
4. checks the reconstruction identities (4.1) and the partner-to-orbit identity (4.2);
5. extends the component-sum/Hermite equality exactly through `n=20` without using brute-force graph enumeration.

The archived output ends:

`FORMULA_CROSSCHECK_PASS adjacent n=3..20; disjoint n=4..20`

`BRUTE_PARTNER_RECONSTRUCTION_PASS adjacent n=3..6; disjoint n=4..6`

`ALL_EXACT_CHECKS_PASS`.

Selected exact rows include:

- adjacent `K_6`: states `(678,144,144,500,322)`, full `(Z,E,J)=(2932,822,178)`, gap `153788`;
- disjoint `K_5`: states `(49,21,21,43,14)`, full `(291,93,29)`, gap `210`;
- disjoint `K_6`: states `(676,242,242,354,128)`, full `(2932,822,226)`, gap `13052`.

The finite checker is an audit of the exact identities and the K5 route refutation; universal claims (2.1)--(4.2) are proved combinatorially/algebraically above, not inferred from the finite range.

## 8. Status, integrity, and handoff

**Outcome: ESSENTIAL_STEP_APPLIED.** The component-reservoir coupling bridge is exact and directly reconciles the partner's overlap term with the lead's Hermite proof. Subsidiary candidate `FOREST-Q-ONLY-DEFECT-ROUTING-v1` is **CANDIDATE_REFUTED** by disjoint `K_5`.

The parent result remains an internal **FULL_PROOF_CANDIDATE** because the lead candidate has the two required independent existing-worker end-to-end review records; this report does not promote it to an established theorem, make a novelty claim, or substitute operational status for mathematical scrutiny.

Scoped review found only mathematical formulas, public-source bibliographic locators, logical account/slot labels, and repository-relative scientific paths. No credentials, benchmark answers, scheduler identifiers, machine paths, unrelated private material, email/Drive action, paid/remote compute, workflow dispatch, permission change, or public release was used.

Next recipient: FOREST lead `account01/B01` and partner `account01/B03`. The useful formula-level handoff is `(2.1)--(4.2)` plus the K5 q-only obstruction; future direct coupling work must preserve both ordinary-switch and overlap-reservoir channels.
