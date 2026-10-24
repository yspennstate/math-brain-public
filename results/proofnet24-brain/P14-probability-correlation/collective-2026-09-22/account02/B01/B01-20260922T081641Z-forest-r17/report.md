# FOREST / account02 B01 — path-packing min-cut theorem and cut-surplus/root-spacing squeeze

**Run:** `B01-20260922T081641Z-forest-r17`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Parent target:** OPEN; no full-proof claim.

## 1. Fresh controls and exact inherited scope

Fresh main was resolved at invocation start as `7f43d781a3221d4d8ca0a3c03a8d9355eab60cc3`; after concurrent work it was re-resolved before this substantive write as `c3b1cf41f2fc42a4cb31da7edc31b8ab034aa974`. The required AGENTS/README/fleet/roles/PROTOCOL and collective ORDER/TARGETS/ASSIGNMENTS controls were read. OWNER CONTROL revision remains `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, with no account02/B01 pause or stop. The later owner control supersedes stale installation language in AGENTS.md: B01 remains FOREST research and new installation/benchmark work is stopped.

The exact target remains the unit uniform law on **all** unrooted acyclic edge subsets of every finite simple graph, including disconnected forests and every size. For distinct physical edges `e,f`, prove `P(e,f in F) <= P(e in F)P(f in F)`.

Latest complete lead payload actually consumed is account01/B01 handoff blob `4cee205cb7d254caf785692838111988a0b8a155`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`. It preserves the source-safe triangle-free deletion/contraction Simpson gate and localizes triangle contractions to the `{1,2}` STAR-2 comparison; it explicitly rejects fixed-graph arbitrary-weight globalization. I do not reuse its superseded rank-degree complete-log-concavity shortcut.

Named OTHER-account result consumed and applied: assigned partner account03/B02 run `20260922T065713Z-b02-r11-forest`, report blob `ec1cad8695af35213e021fa1e16bc521b996799a`. Its source-safe covariance-inverse mechanism proves that for an actual smaller unit forest law, the edge-indicator covariance matrix has nonpositive off-diagonals, positive definite covariance, and entrywise nonnegative inverse; Schur complementation then controls the covariance vector of a boundary event. Section 3 applies that mechanism directly to the actual two-terminal boundary-connectivity event.

The immediate own predecessor is `B01-20260922T072913Z-forest-r17`, report blob `5ffa588c859ed95a040a0ecc5c6bf6e7984fd50a`. Its exact mixed-theta epsilon-net result is retained, not re-proved.

## 2. Same-side proper two-separator setup

Work in the source-safe edge-minimal loopless unit counterexample class already transferred in team work. Consider a proper two-terminal separation with both bad marked edges in side `B` and outside side `O`, with terminals `u,v`. Let `m=|E(O)|`, and under the unit all-forest law on `O` let

- `D` = number of forests disconnecting `u,v`,
- `C` = number of forests connecting `u,v`,
- `lambda=C/D`,
- `q=C/(C+D)=lambda/(1+lambda)`.

Let `R(s)` be the marked Rayleigh gap of side `B` after adding a virtual `uv` edge of activity `s`. Exact gluing gives

`Delta_G(e,f)=D^2 R(lambda)`.

For a negative interval `J=(alpha,beta)` of `R` containing `lambda`, put

`ell=alpha/(1+alpha)`, `u0=beta/(1+beta)`.

For every physical outside edge `h`, with `T_h=1{h in F_O}` and `Y=1{u connected to v in F_O}`, predecessor r17 established the exact deletion/contraction straddling

`P(Y=1|T_h=0) <= ell < q < u0 <= P(Y=1|T_h=1)`.

No arbitrary external field appears here.

## 3. New theorem A — path-packing representation of the exact boundary response

For every simple `u-v` path `P` in `O`, let `N_P` be the number of forests of `O` containing every edge of `P`.

### Theorem A.1

The normalized weights

`x_P := N_P/D`

form a feasible fractional `u-v` path packing with unit capacity on every physical edge, and their total value is exactly `lambda`:

`sum_P x_P = lambda`,

`sum_{P contains h} x_P <= 1` for every `h in E(O)`.

Consequently, if `kappa_uv` is the physical `u-v` edge-connectivity of `O`, then

`boxed: lambda <= kappa_uv.`

Moreover each individual path obeys the sharper length cap

`boxed: x_P <= 1/(2^{|P|}-1).`

### Proof

Every connecting forest has a unique `u-v` path. Conversely, a forest containing `P` has unique `u-v` path exactly `P`. Therefore the connecting forests partition by their unique path and

`C = sum_P N_P`.

Fix an edge `h`. Let `A_h=sum_{P contains h}N_P`, the number of connecting forests whose unique `u-v` path uses `h`. Deleting `h` maps each such forest injectively to a disconnecting forest: deletion breaks the unique terminal path, and adding `h` recovers the source forest. Hence `A_h<=D`, proving the edge-capacity inequalities after division by `D`.

For any `u-v` cut `K`, every `u-v` path crosses `K` at least once, so

`lambda=sum_P x_P <= sum_P x_P |P intersect K| = sum_{h in K} sum_{P contains h}x_P <= |K|`.

Minimize over cuts to get `lambda<=kappa_uv`.

Finally fix a path `P`. For every forest `F` containing `P` and every nonempty subset `S` of the edges of `P`, `F-S` disconnects `u,v`. The map `(F,S) -> F-S` is injective for fixed `P`: from its image `H`, one recovers `S=P\E(H)` and then `F=H union S`. Thus `(2^{|P|}-1)N_P<=D`, which gives the length cap. QED.

This theorem explains why the predecessor's Mersenne reciprocals `1/(2^a-1)` arise naturally: they are not just gadget responses, but the sharp per-path capacity allowed by deletion in an arbitrary outside graph.

## 4. New theorem B — direct partner-covariance bound on the left response margin

Let `p_h=P(T_h=1)` and `c_h=Cov(T_h,Y)`. From the straddling condition,

`c_h=(1-p_h)(q-P(Y=1|T_h=0)) >= (1-p_h)(q-ell)`.

Deletion of a physical edge injects forests containing it into forests avoiding it, hence `p_h<=1/2`. Therefore

`c_h^2/Var(T_h) >= (q-ell)^2`.

Let `Sigma=Cov((T_h)_{h in E(O)})`. Since `O` is smaller than an edge-minimal counterexample, distinct physical outside edges are nonpositively correlated. The assigned partner's inverse-covariance lemma therefore gives `Sigma^{-1}>=0` entrywise, while each diagonal entry satisfies `(Sigma^{-1})_hh>=1/Var(T_h)`. Schur complementation for `(Y,T)` yields

`c^T Sigma^{-1}c <= Var(Y)=q(1-q)`.

Combining these facts gives the new one-sided boundary-margin inequality

`boxed: m(q-ell)^2 <= q(1-q).`

Writing `L=lambda-alpha`, this is equivalently

`boxed: L <= (1+lambda)sqrt(lambda)/(sqrt(m)+sqrt(lambda)).`

Indeed `q-ell=L/((1+lambda)(1+alpha))` and `alpha=lambda-L`. This is a direct application of account03/B02's covariance-inverse mechanism to the actual retained boundary-connectivity distribution, not a weighted surrogate.

## 5. New theorem C — cut surplus forces exponentially narrow no-hit intervals

Retain the predecessor's exact mixed-theta response semigroup. A unit gadget made of internally disjoint paths of lengths `a_i` has exact response

`s=sum_i 1/(2^{a_i}-1)`

and unit-edge cost `sum_i a_i`. Any such gadget of cost `<m` is a strictly smaller unit replacement, so its response cannot lie in `J`.

Write `lambda=n+r`, `n=floor(lambda)`, `0<=r<1`, and let `kappa=kappa_uv`, `s=m-kappa` be the **cut surplus**. The new path-packing theorem gives `lambda<=kappa`.

If `r=0`, then `n=lambda<=kappa<=m`. If `n<m`, `n` parallel terminal edges are a cheaper exact unit response at `lambda`, contradicting no-hit. Therefore an integer no-hit response can occur only at the extremal boundary

`lambda=kappa=m`.

Now assume `0<r<1`. Since `lambda<=kappa` and `kappa` is integer,

`n<=kappa-1`, hence `m-n>=s+1`.

Let `L=lambda-alpha`. The predecessor's greedy mixed-theta theorem says a response in `(alpha,lambda)` is constructible with cost at most

`C_left=ceil(log_{3/2}(2r/L))*ceil(log_2(1+2/L)).`

No-hit therefore forces `C_left>=m-n>=s+1`.

When `s>=4`, set

`k=ceil(sqrt(s+1))-1 >= 2`.

If `L>=2(2/3)^k`, then both ceiling factors above are at most `k` (for the second factor use the elementary inequality `2(2/3)^k >= 2/(2^k-1)` for `k>=2`). That would give `C_left<=k^2<s+1`, contradiction. Thus

`boxed: L < 2(2/3)^k.`

Because `s>=1` implies `n+1<m`, the symmetric no-hit argument from r17 applies on the right. Let `Rr=beta-lambda`. No-hit first forces `beta<=n+1`, so the predecessor's approximation parameter `t=r+Rr/2` is `<1`. If `Rr>=4(2/3)^k`, its right approximation has both ceiling factors at most `k`, again contradicting the cost lower bound `s+1`. Therefore

`boxed: Rr < 4(2/3)^k`,

and every noninteger no-hit interval with cut surplus `s>=4` satisfies

`boxed: beta-alpha < 6(2/3)^{ceil(sqrt(s+1))-1}.`                 (5.1)

This is the first place the actual outside topology, through `kappa_uv`, improves the earlier edge-count-only epsilon net: high redundant edge surplus forces the admissible bad interval to be exponentially narrow in `sqrt(s)`.

## 6. New theorem D — integer root spacing converts narrowness into separator balance

Suppose the bad interval comes from a genuinely quadratic Rayleigh polynomial

`R(z)=gamma z^2+b1 z+c1`, with `gamma>0`,

for a marked side `B` containing `b` physical edges. All coefficients are integers because every coefficient is a product/difference of unit forest counts. If `R` has a negative interval, its two roots are real and distinct, so its integer discriminant `Delta=b1^2-4 gamma c1` is a positive integer. Therefore

`beta-alpha=sqrt(Delta)/gamma >= 1/gamma`.

Each coefficient of each affine-in-`z` forest count is at most `2^b`; since `gamma` is a positive difference of products of such nonnegative counts,

`gamma<=4^b`.

Hence

`boxed: beta-alpha >= 4^{-b}.`                                   (6.1)

Combining (5.1) and (6.1), an offending noninteger quadratic no-hit separator with `s>=4` must satisfy

`ceil(sqrt(s+1))-1 < (log 6 + b log 4)/log(3/2)`.

In particular

`boxed: s < (1 + (log 6+b log 4)/log(3/2))^2 - 1.`               (6.2)

Thus the unpaid separator obstruction has been reduced from arbitrary outside size to a **quadratic cut-surplus bound in the marked-side size**, plus the explicitly preserved degenerate branch `gamma=0`. This is not closure, but it is a source-valid structural restriction combining exact boundary law, unit replacement minimality, actual min-cut topology, and integer count arithmetic.

## 7. Genuine refutation of an overstrong exact-compression candidate

A tempting next claim would be:

> every `m`-edge two-terminal unit graph has the same response as a unit series-parallel two-terminal network using at most `m` edges.

That is false. Take `K4` with the terminal edge deleted, terminals `0,1`, and physical edges `02,03,12,13,23`. Exact enumeration gives

`D=14`, `C=10`, `lambda=5/7`, `m=5`.

An exhaustive dynamic program over all binary series/parallel unit expressions proves that response `5/7` first appears at cost **6**, not at any cost at most 5. An explicit cost-6 realization is one unit edge in series with five parallel unit edges, since

`1*5/(1+1+5)=5/7`.

So exact same-cost series-parallel compression is **CANDIDATE_REFUTED**. It must not be used to pay the remaining separator implication.

The checker beside this report independently enumerates the 24 forests of this graph, obtains path counts `4,1,4,1`, edge loads `5,5,5,5,2 <= D`, verifies `lambda=5/7<=kappa_uv=2`, checks the per-path deletion caps, and exhausts all unit series/parallel expression trees through cost 6. Captured output ends `STATUS=PASS`.

Checker SHA-256: `946c6046f4f894ce49ca14c7313ebc711557ef6f70e9d8598b806e4a6335239b`.  
Output SHA-256: `cbc1a6b8af7fdb0234f958ad3380e23c0540ce94ce6ef028e8e1c7b5a8ff8cff`.

The finite checker is regression evidence only; Theorems A-D above are symbolic.

## 8. Conditional end-to-end route and exact remaining implication

For a same-side proper two-separator, the paid chain is now:

1. exact gluing retains the true `(D,C)` law and gives `D^2R(lambda)`;
2. deletion/contraction straddling gives physical-edge covariance with terminal connectivity;
3. account03/B02's inverse-covariance mechanism applied to this actual law yields the one-sided margin bound in Section 4;
4. the new unique-path decomposition turns the exact response into a capacity-1 fractional path packing and gives `lambda<=kappa_uv` plus Mersenne path caps;
5. mixed-theta minimality turns cut surplus `s=m-kappa_uv` into the exponential interval-width upper bound (5.1);
6. integer root spacing for a genuinely quadratic marked-side response gives the opposing lower bound and hence the structural cut-surplus constraint (6.2).

The **first essential missing implication is now `CUT-SURPLUS-ROOT-SPACING-CLOSURE-v1`**:

> Rule out an actual same-side separator whose marked-side integer Rayleigh polynomial is either (i) the preserved linear/degenerate branch `gamma=0`, or (ii) genuinely quadratic but has cut surplus satisfying (6.2) and simultaneously satisfies the physical-edge straddling/covariance constraints; alternatively construct an actual graph-side/outside pair realizing such a violation.

This is narrower than the predecessor's unrestricted `MIXED-THETA-HIT / REALIZABILITY-v2`. The response-only exact series-parallel shortcut has been decisively refuted, so the next attack must use graph structure—most plausibly the partner's covariance-inverse geometry together with path/cut overlap—or construct a genuine source-valid obstruction.

Paying this same-side separator implication still would not by itself finish FOREST: the lead's triangle-conditioning `{1,2}` STAR-2 debt remains on the irreducible core. Accordingly this run is `ESSENTIAL_STEP_APPLIED`, **not** `FULL_PROOF_CANDIDATE`.

## 9. Inventory, failures, and provenance

Fresh current-account scheduler inspection found the existing B01-B20 managed research tasks active with their intended hourly recurrence and quiet task-level notification/email flags; no B01 scheduler mutation was made. No gap requiring B20 repair was observed.

Preserved failures and limits:

- fixed-graph unit-good => arbitrary-weight Rayleigh remains fail-closed;
- the invalid rank-degree complete-log-concavity shortcut remains retired;
- exact same-cost unit series-parallel compression is refuted by `K4-uv` above;
- the degenerate linear marked-side response `gamma=0` is not paid by the quadratic root-spacing argument;
- the quadratic cut-surplus bound is a restriction, not a contradiction;
- STAR-2 remains a later lead-level debt.

Model self-report: `GPT-5.6 Sol`.  
Requested reasoning effort: `maximum actually supported`.  
Configured reasoning effort: `UNKNOWN / not exposed`.  
Known actual reasoning effort: `UNKNOWN / not exposed`.  
Provider reasoning tokens: `null / NOT_EXPOSED`.  
Provider thinking time: `null / NOT_EXPOSED`.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

Elapsed execution is recorded in the immutable finish/receipt from actual clock observations and includes tool/network/output overhead; it is not pure thinking.
