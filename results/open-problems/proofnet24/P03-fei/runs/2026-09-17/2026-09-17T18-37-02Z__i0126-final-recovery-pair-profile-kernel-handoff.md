Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated model-family selector, reasoning-effort selector, guaranteed thinking-duration control, or applied-routing receipt, so this report does not claim GPT-6 or maximum reasoning. **NO MOVEMENT: `n_recon^cert = 13 -> 13`. Formal HARD recovery episode 2/2 is consumed; I0126 is handed off after this run. Methods actually used: #4 PROVE SOMETHING WEAKER, COMPLETELY, #11 DUALIZE, #27 SWAP THE QUANTIFIERS.**

# P03 / I0126 — final HARD recovery: rooted degree profiles and the exact directional-kernel obstruction

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Lane: HARD OUTSIDE.  
Source target: Kelly--Ulam Graph Reconstruction Conjecture for finite simple undirected graphs.

## 1. Metric, status, and terminal recovery state

Frozen source-matching metric:

`n_recon^cert = largest n for which every finite simple graph on at most n vertices is rigorously known reconstructible from its full vertex deck`.

Before: **13**.  
After: **13**.  
Movement: **NONE**.

The certified baseline remains Brendan McKay's all-graphs verification through order 13. The unrestricted conjecture remains OPEN / PARTIAL in current 2026 literature. This is the fourth I0126 mathematical run and the second and final permitted HARD recovery after the three-run unchanged trigger. There is no third I0126 recovery under the fleet rule.

Retained P03 results are not repaid:

- `P03-I0126-EXTENSION-COLLISION-247`: any hypothetical order-n counterexample can be represented as two nonisomorphic one-vertex extensions `G_A,G_B` of a common `(n-1)`-vertex card `C` with identical full decks; collisions have `|A|=|B|`, and neighborhoods in the same `Aut(C)` orbit give isomorphic extensions.
- `P03-I0126-DEGREE-PROFILE-THRESHOLD-RIGIDITY-249`: equal-deck common-base extensions conserve the base-degree occupancy vector, induced-edge count, and the C4-through-new-vertex moment; threshold common cards are collision-rigid.
- `P03-I0126-DOMINATING-PAIR-CARD-DEFECT-251`: the deck-visible scalar dominating-pair defect is `delta_G(v)=D2(G)-D2(G-v)=P_G(v)-Q_G(v)`, with the exact one-swap balance recorded in the previous report.

The final recovery below proves one positive card-rooted refinement and one exact negative/obstruction theorem. It does not cover every order-14 graph, so the metric cannot move.

---

## 2. Repository continuity and source gate

I continued from the immutable P03 report

`proofnet24/P03-fei/runs/2026-09-17/2026-09-17T17-32-28Z__i0126-stuck-recovery-1-dominating-defect.md`

at creation commit `3f15cd800021aa0359cabece6d28a2d0919b9677`, blob `9621caaf1c758e331240ef812a159d9d3fe89aee`, rather than restarting an older P03 target.

Before doing mathematics I reread/recovered the repository README, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current fleet and NEW-METHODS rules, `operations/FLEET_2026-09-16.md`, campaign `INDEX.md` / `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, canonical claim `operations/claims/I0126.md`, the newest own I0126 report, current task-health queue delta, and the newest accessible P04 report for directed audit. The very large queue/intake surfaces are connector-bounded, so exact paths / identifiers were used for the active rows instead of claiming an impossible simultaneous byte-for-byte rendering of unrelated material.

Fresh 2026-09-17 source/literature checks retained the exact source scope:

1. **Brendan McKay**, *Reconstruction of Small Graphs and Digraphs*, arXiv:2102.01942v4 (2022): every graph through 13 vertices is reconstructible.
2. **J. Antony Aravind and S. Monikandan**, *A Reduction of the Reconstruction Conjecture using Domination and Vertex Pair Parameters*, arXiv:2601.00620 (2 Jan 2026): `gamma(G)=2` is recognizable; the full conjecture reduces to 2-connected graphs with `gamma=2` or with both graph and complement diameter 2; their Problem 1 still asks whether connected `gamma=2` graphs are weakly reconstructible.
3. **Dufresne--Jeronimo--Kenkel--Lindo--Villamizar**, *Shuffling the Deck: Invariant Theory and the Graph Reconstruction Conjecture*, arXiv:2604.16567v1 (17 Apr 2026): surveys/reformulates the still-unrestricted conjecture rather than resolving it.

No fresh source-matching full proof/counterexample was recovered in the bounded search. That negative search is not a novelty certificate.

---

# 3. Idea before calculation

The last run identified the loss of **partner incidence** as the exact obstruction: the scalar defect `P_G(v)-Q_G(v)` can be reconstructed, but it forgets which vertices are the dominating partners of the missing vertex.

This final recovery therefore asks the weakest exact question first (#4): what genuinely partner-refined information can be attached to an individual unlabeled card without choosing labels? Then it dualizes (#11) the Aravind--Monikandan pair-count recurrences into a polynomial operator. Finally it swaps the quantifiers (#27): instead of trying to reconstruct every missing-vertex partner profile directly, characterize **all pair-profile directions invisible to the entire first deck-sum operator**.

The result is sharp enough to explain why the present domination route stalls. The card does determine the missing vertex's neighbor-degree and anti-neighbor-degree histograms exactly, but the full aggregate pair-count hierarchy sees the parent pair profile only through a directional derivative with a large, explicitly described kernel. Dominating pairs live on a boundary on which that kernel is nonzero. Thus one needs genuinely card-rooted incidence data beyond the global `dv/dav` hierarchy; more scalar moments cannot fix the marker-loss problem.

---

# 4. #4 PROVE SOMETHING WEAKER, COMPLETELY — the missing vertex's degree-refined neighborhood is card-rooted reconstructible

Let `G` be an n-vertex graph and let `C=G-v` be a specified card from its deck. Write

- `M_j(G)` for the number of degree-j vertices in `G`;
- `M_j(C)` for the number of degree-j vertices in the card;
- `d=deg_G(v)`;
- `N_j(v)=#{w in N_G(v): deg_G(w)=j}`.

The parent edge count and degree multiset are classical reconstructible invariants. For the specified card,

`d = |E(G)|-|E(C)|`.

Deleting v does three things to the degree counts: it removes v itself from degree class d, it moves every degree-j neighbor of v from class j to class j-1, and it leaves nonneighbors in their degree classes. Therefore, for every j,

`M_j(C)=M_j(G)-1_{j=d}-N_j(v)+N_{j+1}(v)`,

with `N_n(v)=0`.

Solving downward gives the exact recursion

`N_j(v)=M_j(G)-1_{j=d}+N_{j+1}(v)-M_j(C)`.

Hence the decorated card `(C,d)` determines the entire polynomial

`N_v(q)=sum_j N_j(v) q^j`.

The corresponding anti-neighbor degree profile is then also determined:

`A_v(q)=sum_j [M_j(G)-1_{j=d}-N_j(v)] q^j`.

This is genuinely more refined than the scalar missing degree, and it is attached to the actual card isomorphism type, not merely recovered after summing over the deck.

### Why this does not resolve the one-triple case

In the target one-triple common card `C`, the only repeated base-degree class is `{x,y,r}` and the other ten degree classes are singletons. Claim 249 already forces a one-swap ambiguity

`A=S union {x}`, `B=S union {y}`

with the same number selected from every base-degree class. The rooted degree profile above consequently distinguishes all singleton degree classes but **cannot distinguish x from y**, because their base degree is identical. It recovers exactly the degree-level anti-neighborhood information and stops precisely at the equal-degree cell where the reconstruction ambiguity lives.

So a successful final invariant must encode incidence **inside** that repeated-degree cell, not merely the degree histogram of anti-neighbors.

---

# 5. #11 DUALIZE — ordered pair-category polynomials

The Aravind--Monikandan parameters can be packaged without the `k2=k3` bookkeeping issue by using ordered pairs.

Fix `epsilon in {0,1}`. For every ordered pair `(u,v)`, `u != v`, whose edge indicator is `epsilon`, partition the other `n-2` vertices into four classes:

- `a(u,v)`: adjacent to both u and v;
- `b(u,v)`: adjacent to u only;
- `c(u,v)`: adjacent to v only;
- `d(u,v)`: adjacent to neither.

Thus `a+b+c+d=n-2`. Define the homogeneous ordered-pair polynomial

`F_G^epsilon(X,Y,Z,T)
 = sum_{(u,v): 1_{uv in E}=epsilon}
   X^{a(u,v)} Y^{b(u,v)} Z^{c(u,v)} T^{d(u,v)}`.

Because both orientations of every unordered pair occur,

`F_G^epsilon(X,Y,Z,T)=F_G^epsilon(X,Z,Y,T)`.

Let

`D = partial_X + partial_Y + partial_Z + partial_T`.

## Theorem `P03-I0126-PAIR-PROFILE-DIRECTIONAL-KERNEL-253`

**Status: PROVED / STRUCTURAL-OBSTRUCTION / PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED.**

For every finite simple n-vertex graph G and each `epsilon in {0,1}`:

1. the full vertex deck determines the polynomial `D F_G^epsilon`, via the exact identity

   `sum_{w in V(G)} F_{G-w}^epsilon = D F_G^epsilon`;

2. on the vector space `H_m` of homogeneous degree `m=n-2` polynomials in `X,Y,Z,T`,

   `ker(D|H_m)
    = { homogeneous degree-m polynomials in X-T, Y-T, Z-T }`;

3. the degree-refined dominating-pair boundary is not determined by `D F` as a linear-algebraic matter. In particular, if

   `R_G^epsilon(p,q)
    = (pq)^epsilon [T^0] F_G^epsilon(pq,p,q,T)`,

   then `R_G^epsilon` records ordered dominating pairs by endpoint degrees, but the map `F -> D F` does not determine `R`: the nonzero symmetric kernel element `(X-T)^m` has zero D-derivative and nonzero dominating boundary `X^m`.

The theorem does **not** assert existence of two graphs realizing an arbitrary kernel perturbation. It proves an exact information obstruction for every strategy that tries to recover the parent dominating-partner profile solely by linear inversion of the aggregate `dv/dav` deck recurrences.

### Proof of part 1

Fix an ordered pair `(u,v)` in G and its monomial

`M=X^a Y^b Z^c T^d`.

Cards deleting u or v contain no copy of this ordered pair. If a third vertex w is deleted, `(u,v)` remains with the same edge status. Exactly one of the four category counts drops by one:

- each of the a common neighbors contributes `X^{a-1}Y^bZ^cT^d`;
- each of the b u-only neighbors contributes `X^aY^{b-1}Z^cT^d`;
- each of the c v-only neighbors contributes `X^aY^bZ^{c-1}T^d`;
- each of the d neither-neighbors contributes `X^aY^bZ^cT^{d-1}`.

Summing this pair's contribution over all vertex-deleted cards is therefore

`a X^{a-1}Y^bZ^cT^d
 + b X^aY^{b-1}Z^cT^d
 + c X^aY^bZ^{c-1}T^d
 + d X^aY^bZ^cT^{d-1}
 = D M`.

Summing over all ordered pairs of edge status epsilon proves

`sum_w F_{G-w}^epsilon = D F_G^epsilon`.

The left side is computed from the unlabeled deck because `F_H^epsilon` is an isomorphism invariant of each card H.

### Proof of part 2

Introduce linear coordinates

`s=(X+Y+Z+T)/4`,
`u=X-T`, `v=Y-T`, `r=Z-T`.

Translating `(X,Y,Z,T)` by `(h,h,h,h)` increases s by h and leaves `u,v,r` fixed. Hence, in these coordinates,

`D = partial_s`.

Therefore a polynomial is annihilated by D exactly when it is independent of s, i.e. belongs to `R[u,v,r]=R[X-T,Y-T,Z-T]`. Intersecting with homogeneous degree m gives precisely the claimed homogeneous kernel.

For `m=12` (the order-14 problem), this kernel already has dimension

`binom(12+3-1,3-1)=binom(14,2)=91`.

Even imposing the required `Y <-> Z` symmetry leaves a large nonzero subspace; `(X-T)^12` is one explicit symmetric element.

### Proof of part 3

A pair `(u,v)` dominates G exactly when every third vertex is adjacent to at least one endpoint, i.e. exactly when `d(u,v)=0`. For such a pair,

`deg(u)=a+b+epsilon`,
`deg(v)=a+c+epsilon`.

Thus the displayed boundary transform

`R_G^epsilon(p,q)
=(pq)^epsilon [T^0]F_G^epsilon(pq,p,q,T)`

is exactly the ordered degree-pair generating polynomial of dominating pairs of edge status epsilon.

But for `H=(X-T)^m`,

`D H=0`

while

`[T^0]H=X^m != 0`.

Therefore `D F` cannot determine the dominating boundary as a linear map on the ambient pair-profile space. QED.

---

# 6. #27 SWAP THE QUANTIFIERS — what the obstruction says in the one-triple recovery target

The failed direct quantifier was:

> for every card / deleted vertex, reconstruct its degree-refined set of dominating partners.

The swapped question is:

> which parent pair-profile perturbations are invisible to **all first-order deck-sum equations at once**?

Claim 253 answers this exactly: they are the translation-invariant polynomial directions generated by differences `X-T,Y-T,Z-T`.

This is the polynomial form of the marker-loss obstruction. The Aravind--Monikandan recurrence is triangular only when a boundary condition kills the `d=0` layer (their `gamma>=3` regime). At `gamma=2`, the desired dominating pairs sit exactly on the `T^0` boundary. Differentiating in the all-ones direction couples that boundary to one-defect pair classes but supplies no transverse boundary condition. Claim 251's scalar `P-Q` is a zeroth-moment shadow of the same coupling.

For the one-triple 13-card case, the positive lemma in Section 4 reconstructs every degree-level anti-neighborhood count, so all ten singleton degree classes are visible. The unresolved swap `x <-> y` lies wholly inside the equal-degree triple. Claim 253 proves that global pair-category sums, even taken for **all** `(k1,k2,k3)` and for adjacent and nonadjacent pairs, do not by themselves supply the missing transverse incidence information. A successful proof must use more than their aggregate linear deck-sum equations — for example a genuinely card-rooted incidence correspondence that couples a particular anti-neighbor to a particular potential partner.

This is a sharp obstruction, not a counterexample. The full deck is richer than the sum of its pair polynomials, so no claim is made that the one-triple card class is nonreconstructible.

---

## 7. Why the metric still cannot move

Nothing proved above covers the entire one-triple class, still less the `2+2` repeated-degree pattern or every order-14 graph. No pair of nonisomorphic graphs with identical full vertex decks was found either.

Therefore

`n_recon^cert = 13`

must remain unchanged.

The simplest live structural case at handoff is:

- common card C has 13 vertices;
- exactly one degree class `{x,y,r}` has size 3 and all other degree classes are singletons;
- the two candidate extensions differ by one swap `S union {x}` versus `S union {y}`;
- the parents are in the 2-connected `gamma=2` reduction;
- all Claim 249 and Claim 251 balances hold;
- the missing obligation is a **card-rooted incidence invariant inside the equal-degree triple** that cannot be reduced to the directional derivative of the global pair-category polynomial.

The separate `2+2` repeated-degree residue was not silently merged into this case.

---

# 8. Formal HARD handoff / rotation state

This run is recovery episode 2/2. Since the metric is still 13, P03 must not perform another I0126 recovery. A separate immutable handoff is written for I0126 after this report and preserves Claims 247, 249, 251, and 253 with the exact blocker above.

A fresh successor screen was also performed rather than taking a stale queue row:

- current task-health `operations/task_health/runs/2026-09-17T175800Z/queue_delta.md` explicitly says historical queue rows are not automatically READY;
- `I0045`, `I0046`, `I0048` are `HOLD_SCOPE_KNOWN_LIKELY` after later preferential-attachment literature;
- `I0031` has conflicting stale scope: repository history records the `tau_0=O(n)` distance-regular clause as literature-resolved, so it is not safely dispatchable from the compact queue label;
- `I0055` is recorded by prior rotation screens as literature-resolved in the queued scope;
- `I0115` remains source-scope ambiguous after the Kahn/Kendall Poisson-line SIRSN construction;
- `I0129` remains blocked by a quantifier mismatch between finite multiplicity searches and Singmaster's universal boundedness statement;
- direct fetch of `operations/claims/I0047.md` returned 404, but the freshest coordinator screen classifies its broad preferential-attachment FPP source as `HARD / PENDING SOURCE NARROWING`, not READY.

Accordingly **no genuinely unassigned READY HARD OUTSIDE successor was certified in this bounded final-recovery run**. P03 therefore enters `I0126_HANDOFF_COMPLETE / ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED` rather than stealing an occupied target or inventing readiness. The next run must continue the source/status/ownership admission cursor, not reopen I0126.

---

# 9. Directed P04 second-audit duty

I independently audited a P04 claim not previously audited by P03:

- peer path: `proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T17-47-30Z__run-report.md`;
- creation commit: `095b08caf0c59bc50d22519a64ca4b5089f58810`;
- blob: `4cba9795ec3dbfced088c2ae6c66cc6a90c2313b`;
- peer claim: `P04-I0101-SCORE-COMPATIBLE-PRECISION-HOMOTOPY-29`.

### Independent audit

Let `s=sqrt(p)`, `z*=3/(2s-3)`, and

`P_lambda(z)=I+lambda z A+lambda z^2 D`

for the two-localized Paley graph, with `0<=lambda<=2`. On an edge, `P_ij=lambda z`; on the diagonal `P_ii=1+lambda z^2 d_i`. Hence

`P_ii - z sum_{j~i} P_ij = 1`

exactly.

Using `A=(J-I+K)/2`, `J >= 0`, `||K||<=s`, and the prior exact degree lower bound

`d_i >= d_min=(s^2-2s-15)/8`,

one obtains for every vector v

`v^T P_lambda(z) v
 >= [1-lambda z(1+s)/2 + lambda z^2 d_min] ||v||^2`.

The bracket is decreasing on `0<=z<=z*`, because its stationary point

`z0=2(1+s)/(s^2-2s-15)`

satisfies `z*<z0`; after cross multiplication the gap is

`s^2+4s+39>0`.

At the endpoint,

`lambda_min(P_lambda(z*))
 >= 1-lambda*3(5s^2+2s+33)/(8(2s-3)^2)`.

This is decreasing in lambda, so lambda=2 is worst, giving

`lambda_min(P_2(z*))
 >= (s^2-54s-63)/(4(2s-3)^2)`.

The numerator is positive exactly for

`s>27+6 sqrt(22)`,

whose square is below 3041. Therefore every admissible prime `p>=3041` has the stated positive-definite homotopy margin. All algebra and quantifiers in the peer claim check.

Audit verdict:

`P03-AUDIT-P04-I0101-SCORE-COMPATIBLE-PRECISION-HOMOTOPY-254 = PASS (CLAIM-SCOPED)`.

This audit validates Claim 29 only; it does not certify P04's asymptotic Conjecture 27 or any additional finite prime.

---

# 10. Exact remaining obligation for any future I0126 owner

Do **not** restart from scalar domination counts. The current sharp obligation is one of:

1. construct a card-rooted incidence object which, in the one-triple common-card case, distinguishes `S union {x}` from `S union {y}` whenever x,y are nonautomorphic and all retained balances hold; or
2. construct an exact pair of nonisomorphic equal-deck extensions, which would refute the source; or
3. find a different uniform order-14 argument covering all common-card multiplicity types.

Any route based only on linear inversion of global adjacent/nonadjacent pair-category deck sums must first overcome the explicit 91-dimensional order-14 directional kernel in Claim 253.

---

## 11. `ledger_delta` for P26

```yaml
ledger_delta:
  worker: P03
  target: I0126
  lane: HARD_OUTSIDE
  status: PARTIAL_OPEN_HANDOFF
  metric:
    name: n_recon^cert
    before: 13
    after: 13
    movement: NONE
  stuck_state:
    unchanged_trigger_reached: true
    recovery_episode_before: 1/2
    recovery_episode_after: 2/2
    further_P03_I0126_recovery_allowed: false
  new_claim:
    id: P03-I0126-PAIR-PROFILE-DIRECTIONAL-KERNEL-253
    status: PROVED_STRUCTURAL_OBSTRUCTION_PARTIAL
    novelty: PUBLICATION_NOVELTY_UNVERIFIED
    content:
      - specified card reconstructs missing-vertex neighbor-degree and anti-neighbor-degree histograms
      - full deck determines D F_epsilon for ordered pair-category polynomial
      - kernel on degree n-2 is homogeneous polynomials in X-T,Y-T,Z-T
      - dominating degree-pair boundary is not determined by this aggregate linear operator
  retained_claims:
    - P03-I0126-EXTENSION-COLLISION-247
    - P03-I0126-DEGREE-PROFILE-THRESHOLD-RIGIDITY-249
    - P03-I0126-DOMINATING-PAIR-CARD-DEFECT-251
  peer_audit:
    id: P03-AUDIT-P04-I0101-SCORE-COMPATIBLE-PRECISION-HOMOTOPY-254
    verdict: PASS_CLAIM_SCOPED
    path: proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T17-47-30Z__run-report.md
    creation_commit: 095b08caf0c59bc50d22519a64ca4b5089f58810
    blob: 4cba9795ec3dbfced088c2ae6c66cc6a90c2313b
  successor:
    state: ROTATION_HOLD_SUCCESSOR_ADMISSION_REQUIRED
    claim_created: false
    reason: no genuinely unassigned READY HARD OUTSIDE successor certified after fresh current screening
  shared_root_ledgers_edited_by_P03: false
```

No root ledger, peer file, Gmail/email, Drive, public post, paid compute, permission, workflow, or additional schedule was changed.

**End of complete run report.**