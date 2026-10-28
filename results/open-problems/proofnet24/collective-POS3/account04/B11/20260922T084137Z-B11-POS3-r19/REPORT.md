# POS3 account04/B11 r19 — bounded-range surgery makes the first-interruption renewal uniformly elliptic

**Run:** `20260922T084137Z-B11-POS3-r19`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x precedes y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are for the uniform law on the full linear extensions of the original finite poset. No deletion-induced or projected law is renamed uniform. No finite-kernel reduction is assumed or claimed.

## 1. Exact state consumed

Fresh control was resolved at invocation start and again before this delivery. At the pre-delivery reread the control repository main commit was

`851a52379991623a5509b2f60ab91ca38d491c64`.

The five mandatory control blobs were unchanged:

- `AGENTS.md`: `94387098453b9f4a9b10179183f6f6ec780fd987`;
- `scheduled_tasks/README.md`: `3d4a9372c87802ab734141a3374d04c8823372e3`;
- `scheduled_tasks/fleet.json`: `e647d5d2479749f80ce7bb4862bee0f28513c7d9`;
- `scheduled_tasks/roles.json`: `ed17ecc94f76720c0345b3e32249b791b20ec611`;
- `scheduled_tasks/PROTOCOL.md`: `83a9268bf5287ca203e4be69a79e25382397bca7`.


The newest complete campaign-lead result used is account04/B10 r18:

`proofnet24/collective-POS3/account04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, science commit `a4b6e9bf76d078c98a82f44be0af30c57def7f99`, report blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

It proves that a surviving four-channel export re-enters an exact heavy Hasse bridge, and that an opposite-ray two-step switch has only three outcomes: strict strong-majority span descent, strict strong-order envelope expansion, or literal exact backtrack through that bridge. Its first unpaid global implication is `POS3-CROSS-ENVELOPE-BACKTRACK-EXIT-v1`.

The assigned OTHER-account partner result applied directly is account01/B19's exact first-interruption renewal theorem, science commit

`173d55ae6cc201a23f530293c0e77161941b842e`.

For the first maximal strong-majority chain block `C={c_1<...<c_m}`, `Q=P\C`, and

`lambda(q)=max({j:c_j<q} union {0})`,

it defines the at-most-two first interrupters

`M={q in Min(Q): lambda(q)<m}`

and gives the exact full-extension decomposition

`e(P)=e(Q)+sum_{q in M} sum_{j=lambda(q)}^{m-1} e(R_{q,j})`,       (1.1)

where

`R_{q,j}=P\{c_1,...,c_j,q}`                                    (1.2)

and the prefix `c_1,...,c_j,q` is fixed before taking a **uniform** linear extension of the residual poset. For every event `A` depending only on the order of elements of `Q`,

`Pr_P(A)=alpha Pr_Q(A)+sum_{q,j} beta_{q,j} Pr_{q,j}(A)`,         (1.3)

with

`alpha=e(Q)/e(P)`, `beta_{q,j}=e(R_{q,j})/e(P)`.                 (1.4)

The partner's append-only late delta, science commit

`f24a85b4f5215de31914b25d2c51cb649d65c753`,

correctly warns that a bounded endpoint fringe of interruption depths cannot control (1.3) in general: an explicit width-three autonomous-chain family can force relevant balance migration to linear depth in the chain length. That warning is preserved below rather than bypassed.

The immediate same-slot predecessor is account04/B11 r18, science commit

`bc1fea690baa140d6e73f4f01120158e370890a1`.

It proves that for `K=pi(P)=max_v |Inc(v)|` and any fixed reference linear extension `L_0=(v_1,...,v_n)`, every linear extension `L` satisfies

`|rank_L(v_i)-i| <= |Inc(v_i)| <= K`,                            (1.5)

and that

`v_i || v_j  =>  |i-j| <= 2K-1`.                               (1.6)

It also gives an exact finite-memory transfer representation in the bounded-`K` branch while explicitly retaining arbitrary-size boundary vectors. Aires--Kahn's bounded-width large-range theorem, together with the inherited 6-thin result, therefore leaves any hypothetical POS3 counterexample in the qualitative finite band

`7 <= K <= K_3`,                                                (1.7)

for some source-dependent finite `K_3`. No numerical value for `K_3` is invented.

## 2. Conditional end-to-end route and the implication attacked here

Assume for contradiction a cardinality-minimal width-at-most-three POS3 counterexample `P`. The no-balanced relation `prec_*` is a strict total order extending `P`, hence itself a reference linear extension. By (1.7) its incomparability range `K` is finite and bounded by the source-qualitative constant `K_3`.

The lead r18 machinery turns every surviving charged incomparable pair into a heavy Hasse bridge and says that changing rays either descends in span, strictly enlarges the active `prec_*` envelope, or exactly backtracks. Account04/B11 r18 says every active incomparable pair has `prec_*` span at most `2K-1`. The assigned partner says that the first chain block has an exact full-depth renewal decomposition (1.1)--(1.4), but its late delta rules out simply truncating that renewal at an endpoint.

The first missing issue is therefore not to find another local constant. It is to show that, **inside the actual bounded-range counterexample branch**, the partner's full-depth renewal cannot become arbitrarily long or arbitrarily singular while the lead's active envelopes expand. The theorems below establish exactly that much:

1. every incomparable pair has a positive `K`-dependent minority floor by an explicit full-extension block surgery;
2. cardinality minimality forces the first strong-majority chain block to have length at most `K`;
3. consecutive interruption-depth components of the assigned partner's renewal differ by at most a factor `K`;
4. consequently one entire first-interrupter branch has every one of its depths carrying a uniform positive fraction `theta_K` of the original full-extension law;
5. the lead's strict envelope expansions can occur at most `2K-2` times before either descent or exact backtrack must intervene.

This is an arbitrary-size finite-depth/ellipticity theorem, not a finite-poset kernel.

## 3. Bounded-range local surgery gives a uniform minority floor

Fix any finite poset `P` with

`K=max_v |Inc(v)|`,

and any reference linear extension

`L_0=(v_1,...,v_n)`.

Let `x=v_i` and `y=v_j` be incomparable, with `i<j`.

By (1.5)--(1.6), in every full extension `L`,

`|rank_L(x)-rank_L(y)| <= (j-i)+2K <= 4K-1`.                   (3.1)

Thus the inclusive contiguous block between the two endpoint positions in `L` has at most `4K` elements.

### Theorem 3.1 — full-extension block-surgery comparison

Put

`C_K=(2K+1)^2 (4K)!`.                                          (3.2)

Then every incomparable pair satisfies

`1/C_K <= #{L:y<x}/#{L:x<y} <= C_K`,                            (3.3)

and therefore

`min{Pr(x<y),Pr(y<x)} >= eta_K:=1/(1+C_K)`.                     (3.4)

#### Proof

Take a full extension `L` with `x<y`. Let `S(L)` be the set of elements occupying the contiguous interval from the position of `x` through the position of `y`. By (3.1), `|S(L)|<=4K`.

Because `x||y`, the induced poset `P[S(L)]` has a linear extension in which `y<x`: adding the relation `y<x` creates no directed cycle precisely because `x` and `y` were incomparable. Choose once and for all a deterministic canonical such extension for every possible induced block and replace the internal order of `S(L)` by that canonical order, leaving all outside positions fixed.

The result is again a full linear extension of `P`. Indeed, if an outside element `z` lies before the entire block in `L`, there cannot be a relation `s<z` for any `s in S(L)`, because that would already contradict `L`; hence leaving `z` before the reordered block is safe. Dually, if `z` lies after the block, there cannot be a relation `z<s` with `s in S(L)`. All relations internal to the block are respected by construction.

It remains to bound congestion. In the original `L`, record the two rank displacements

`d_x=rank_L(x)-i`, `d_y=rank_L(y)-j`.

Each belongs to `[-K,K]` by (1.5), so there are at most `(2K+1)^2` possibilities. Given the output extension and `(d_x,d_y)`, the original two endpoint positions, hence the exact block positions and its element set, are recovered. The original internal order has at most `|S(L)|! <= (4K)!` possibilities. Thus any output has at most `C_K` preimages. This proves

`#{L:x<y} <= C_K #{L:y<x}`.

Applying the same construction with the roles of `x,y` reversed gives the reverse inequality and hence (3.3)--(3.4). `square`

### Corollary 3.2 — sharper floor at the first chain-block boundary

If `x=v_i`, `y=v_{i+1}` are consecutive in the reference extension, then the contiguous surgery block has size at most `2K+2`. Hence with

`C_K^bd=(2K+1)^2 (2K+2)!`,                                     (3.5)
`eta_K^bd=1/(1+C_K^bd)`,                                       (3.6)

one has

`min{Pr(x<y),Pr(y<x)} >= eta_K^bd`.                             (3.7)

The constant is intentionally crude; what matters is that it is strictly positive and depends only on the actual bounded range `K`, not on `|P|`.

## 4. Minimality bounds the first renewal block by K

Return to the cardinality-minimal hypothetical counterexample and let

`C={c_1<...<c_m}`

be the assigned partner's first maximal contiguous chain block in `prec_*`. Because `prec_*` extends the poset order and this is the first block, `C` is an order ideal.

### Theorem 4.1 — first-block length bound

`m <= K`.                                                       (4.1)

#### Proof

Take any outside element `z`. It appears after all of `C` in the reference extension `prec_*`, so `z<c_i` is impossible for every `i`. Hence each comparison between `z` and the chain has the form `c_i<z`, and transitivity shows that the comparable elements of `C` form an initial prefix

`c_1,...,c_lambda(z)`,

while

`c_{lambda(z)+1},...,c_m`

are all incomparable with `z`. The suffix has size at most `|Inc(z)|<=K`.

If `m>K`, then `lambda(z)>=m-K>=1` for every outside `z`; therefore `c_1<z` for every outside element. Of course `c_1<c_i` for every other member of `C`. Thus `c_1` is a global minimum of `P`.

Every full linear extension then begins with `c_1`, so deleting `c_1` is a bijection between `L(P)` and `L(P\{c_1})` preserving every ordering probability among the remaining elements. The remainder cannot be a chain, because adjoining a global minimum to a chain would make `P` itself a chain. It still has width at most three. Hence it would be a strictly smaller POS3 counterexample, contradicting cardinality minimality. `square`

This is the point at which the partner's general linear-depth adversary is genuinely neutralized in the **hypothetical minimal bounded-range counterexample branch**: the first renewal block has at most `K` depths. Nothing here bounds the whole poset.

## 5. Adjacent interruption depths are K-comparable

For `q in M` and

`j=lambda(q),...,m-1`,

write

`N_j(q)=e(R_{q,j})`.                                            (5.1)

These are the literal full-extension counts of the assigned partner's interruption channels.

### Theorem 5.1 — adjacent-depth surgery

For every permitted adjacent pair `j,j+1`,

`N_{j+1}(q) <= N_j(q) <= K N_{j+1}(q)`.                         (5.2)

#### Proof: the first inequality

Since `j>=lambda(q)`, one has `c_{j+1} not< q`. Also `q<c_{j+1}` is impossible because `C` is an ideal and `q` lies outside `C`. Hence

`q || c_{j+1}`.                                                 (5.3)

A channel-`j+1` extension begins

`c_1,...,c_j,c_{j+1},q,...`.

Swap the adjacent incomparable entries `c_{j+1}` and `q`. The rest of the extension is unchanged and the result begins

`c_1,...,c_j,q,c_{j+1},...`,

so it is a channel-`j` extension. The swap is injective. Therefore

`N_{j+1}(q)<=N_j(q)`.                                           (5.4)

#### Proof: the second inequality

Take a channel-`j` extension. After the fixed prefix

`c_1,...,c_j,q`,

locate `c=c_{j+1}`. In the residual poset after deleting `c_1,...,c_j`, the element `c` is minimal: all of its predecessors belong to the ideal chain and have already been removed. Consequently every residual element appearing before `c` in the extension is incomparable with `c`; if it were comparable, minimality would force `c<z`, contradicting the displayed order.

There are at most `K` such elements, because all belong to `Inc(c)`, and one of them is `q`. Move `c` left by adjacent swaps across all of them, including `q`, so that the extension begins

`c_1,...,c_j,c,q,...`.

Every swap is between incomparable elements, so the result is a valid channel-`j+1` extension.

For a fixed target extension, a preimage is recovered by moving `c` right across `q` and then across an initial segment of the following elements. In the source there were at most `K` residual elements before `c`, so there are at most `K` possible insertion depths. The map therefore has congestion at most `K`, which gives

`N_j(q)<=K N_{j+1}(q)`.                                        (5.5)

Together with (5.4), this proves (5.2). `square`

The theorem is exact and arbitrary-size. It uses only the ideal-chain renewal geometry and the bounded incomparability range.

## 6. One complete renewal branch is uniformly elliptic

For each first interrupter define the partner's aggregate coefficient

`beta_q=sum_j beta_{q,j}`.                                      (6.1)

Let `x=c_m`, and let `y` be the first element of `Q` in the reference order `prec_*`. By maximality of `C`, `x||y`, and `x,y` are consecutive in `prec_*`. Therefore Corollary 3.2 gives

`Pr_P(y<x) >= eta_K^bd`.                                       (6.2)

Every extension with `y<x` fails to begin with the whole chain `C`, so the total non-prefix renewal mass satisfies

`sum_{q in M} beta_q = 1-alpha >= eta_K^bd`.                    (6.3)

The assigned partner proves `1<=|M|<=2`. Hence some first interrupter `q_*` obeys

`beta_{q_*} >= eta_K^bd/2`.                                    (6.4)

Its number of interruption depths is

`ell=m-lambda(q_*) <= m <= K`.                                  (6.5)

Iterating (5.2), the largest and smallest channel counts differ by at most `K^(ell-1)`. Therefore, for every depth `j` in this branch,

`N_j(q_*) >= [sum_h N_h(q_*)]/[ell K^(ell-1)]`
`          >= [sum_h N_h(q_*)]/K^K`.                            (6.6)

Divide by `e(P)` and use (6.4).

### Theorem 6.1 — heavy-branch full-depth coefficient floor

There exists a first interrupter `q_* in M` such that **every** exact renewal component in that branch satisfies

`beta_{q_*,j} >= theta_K`,                                      (6.7)

where

`theta_K := eta_K^bd/(2 K^K)`
`         = 1/[2 K^K (1+(2K+1)^2(2K+2)!)].`                    (6.8)

Thus the assigned partner's full-depth sum cannot hide all of the non-prefix mass in a vanishingly thin endpoint tail in a minimal bounded-range counterexample. One whole interrupter branch has at most `K` depths and every depth has a strictly positive `K`-dependent share of the original uniform law.

This does **not** say that the residual posets `R_{q_*,j}` are bounded in size, and it does not say that a balanced pair in one residual survives with the same identity after reassembly. The account01/B19 late delta and the newer autonomous-chain examples correctly forbid such a shortcut. What has been paid is coefficient ellipticity, not pair migration.

## 7. Direct application to the newest campaign lead: strict envelope expansion has bounded run length

Use `prec_*` itself as the reference extension in the same bounded-range counterexample. By (1.6), every active incomparable pair has strong-order endpoint distance at most

`2K-1`.                                                        (7.1)

In the newest lead r18 two-step ray-switch normal form, a surviving strict envelope expansion replaces an active interval by a **strictly larger** active interval whose endpoints are again incomparable. Therefore the integer endpoint distance increases by at least one at every strict expansion but can never exceed `2K-1` by (7.1).

### Corollary 7.1 — bounded strict-expansion run

Before a span-descent or literal exact-backtrack event intervenes, there can be at most

`2K-2`                                                         (7.2)

successive strict strong-order envelope expansions.

In the actual exceptional branch this is at most `2K_3-2`. This converts the lead's qualitative strict-envelope alternative into a finite-length alternative without assuming that the entire poset is finite-kernel bounded. A global recycler may still use exact backtracks to revisit earlier territory; (7.2) says it cannot postpone that issue indefinitely by strict expansion alone.

## 8. Compact conditional route after this run

The arbitrary-size conditional proof route is now narrower.

Assume a minimal no-balanced width-three candidate. The source theorem and 6-thin result put it in `7<=K<=K_3`. Every active incomparable pair is confined to a `2K-1` strong-order band. The lead r18 export either descends, strictly enlarges that band, or exactly backtracks; strict enlargement can occur only `2K-2` times in succession. At the first chain block, the assigned partner's exact renewal has at most two first interrupters, the block itself has at most `K` depths, and one entire interrupter branch has every depth coefficient at least `theta_K` under the **original** full-extension law.

Thus neither of the two previously plausible escape mechanisms remains available:

- the proof walk cannot evade exact backtracking by unbounded strict envelope expansion; and
- the renewal charge cannot evade analysis by being pushed to arbitrarily deep or arbitrarily tiny first-block components inside the bounded-range minimal branch.

The first genuinely unpaid implication is now:

> **`POS3-ELLIPTIC-BACKTRACK-RENEWAL-MIGRATION-v1`.** In a cardinality-minimal no-balanced width-three poset with `pi(P)=K`, combine a non-exact/multi-distinguisher exact backtrack from the lead r18 heavy-bridge normal form with the at-most-two, at-most-`K` first-interruption renewal decomposition. Prove that either an already-authorized span descent / ordinal-or-autonomous reduction occurs, or some incomparable pair (allowed to migrate between residual components) has aggregate signed renewal charge in its balancing window. It is enough to use the coefficient floor `theta_K`; it is **not** legitimate to demand that a single fixed balanced residual pair lift unchanged.

This is a smaller and more quantitative statement than the previous unrestricted cross-envelope reuse problem, but it is not proved here. In particular, a finite list of boundary masks or renewal depths is not itself closure, because the residual continuation vectors and the identity of the balancing pair may still vary through an arbitrarily large poset.

## 9. Integrity, counterexample pressure, and non-claims

The main new statements were proved symbolically; no finite enumeration or numerical computation was used, so there is no code/output artifact to promote beyond its scope.

The strongest tempting overclaim was explicitly rejected: (6.7) does **not** imply a same-pair transfer theorem. The assigned partner's late delta, and compatible other-account autonomous-chain examples, show that balance can migrate under exact reweighting. The next theorem must therefore select the pair adaptively across the full exact mixture.

A scoped fallback privacy/secret review was performed manually because no repository-native scanner is exposed in this runtime. The changed scientific file contains only mathematical statements, logical account/slot/run labels, repository-relative source references, and nonsecret commit/blob identifiers. It contains no credentials, scheduler identifiers, machine paths, private transcripts, benchmark gold or keys, email/Drive data, unrelated private data, paid/remote model calls, workflow dispatch, permission changes, or public-release action.

**Classification:** `ESSENTIAL_STEP_APPLIED`. The parent POS3 statement remains **OPEN / NOT PROVED**.
