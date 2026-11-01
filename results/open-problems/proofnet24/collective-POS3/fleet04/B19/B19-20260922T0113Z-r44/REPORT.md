# POS3 fleet04/B19 — exact autonomous-chain corridor law and boundary-active reduction

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This run follows `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The later owner control supersedes the older installation/benchmark assignment, so this report contains only POS3 mathematics plus exact provenance. No benchmark or brain-installation work was performed.

## 1. Exact state consumed

The assigned task is to integrate the path, coupling and structural estimates into an arbitrary-size induction and directly resolve its first uncovered case.

I consumed the following exact completed results.

1. **Named other-account partner `fleet01/B10`.**  
   `proofnet24/collective-POS3/fleet01/B10/20260921T235306Z-fleet01-B10/REPORT.md`, blob `3a0d4e63665646adc853bb48192eba0f81629a15`. It gives the exact three-chain ideal-state path representation and, in any hypothetical counterexample, the heavy-slice law: for every relevant element/other-chain pair, the strong-majority insertion gap carries more than one third of all full extensions.

2. **Other-account chain-coupling result `fleet01/B19`.**  
   `proofnet24/collective-POS3/fleet01/B19/20260922T004631Z-b19-pos3-r11/REPORT.md`, blob `c2f771152d5be6943cce6872c500ca81c572e962`. For a deleted chain `C={c_1<...<c_m}`, it gives the exact dual prefix recurrence in terms of profile intervals `I(q)=[lambda(q),rho(q)]`, and proves an exact adjacent-swap short-gap defect formula. The only context-sensitive adjacent swaps are nested-profile swaps.

3. **Connected-core reduction `fleet02/B11`.**  
   Report blob `b71c5087c4982769946c31f1ec76242bf297fe17`. Exact ordinal factorization permits a cardinality-minimal counterexample to be taken with connected incomparability graph.

4. **Pinned-rank constraint `fleet03/B10`.**  
   `proofnet24/collective-POS3/fleet03/B10/fleet03-B10-20260922T001407Z-pos3-r11/REPORT.md`, blob `388ac28e375df4e7a49f72ffbf540f362e03696e`. In a width-at-most-three counterexample, every element has probability at least `3^-9` of occupying its rank in the common strong-majority order; in the three-chain path model this is a lower bound on the joint majority-gap cell.

5. **Prior fleet04/B19 structural step.**  
   `proofnet24/collective-POS3/fleet04/B19/B19-20260922T001218Z-r44/REPORT.md`, blob `ce30dae79d698103f026d4d871033238489b1fb1`. It proves that restriction of a uniform ambient linear extension to an autonomous subset is uniform on that induced subposet. Consequently a cardinality-minimal POS3 counterexample has no proper autonomous nonchain; every proper autonomous subset that survives is a chain.

At the two science snapshots checked during this run there was no complete source-bound `proofnet24/collective-POS3/fleet04/B10/` lead report, so no lead theorem was fabricated. The complete named partner result above was used directly, as required by the asynchronous team protocol.

## 2. Compact conditional end-to-end route

Assume a counterexample exists and choose one of minimum cardinality. The inherited reductions allow us to work in a width-exactly-three, incomparability-connected core with no proper autonomous nonchain. Fleet01/B10 converts the uniform extension law into exact three-chain path flux and says that every relevant strong-majority gap is a `>E/3` insertion slice. Fleet01/B19 says that deleting a general chain does not produce the uniform law on the remainder; the exact bias is an insertion-corridor multiplicity, with nested profiles as the only source of context-sensitive adjacent-swap sign.

The first uncovered induction branch after the prior fleet04/B19 report is therefore:

> **Proper autonomous chain branch.** Let `C` be a proper autonomous chain of a minimal counterexample. Determine its exact deletion weight and either lift the smaller-poset theorem or isolate the genuinely nonuniform residual.

This report resolves the constant-corridor part of that branch exactly, and localizes every remaining defect to two explicit boundaries.

## 3. Autonomous-chain trichotomy

Let `P` be a finite poset and let

`C={c_1<...<c_m}`

be a nonempty autonomous chain. Put `Q=P\C`. Autonomy says that each `q in Q` has one of exactly three relations to `C`:

- `q<c` for every `c in C`;
- `c<q` for every `c in C`;
- `q||c` for every `c in C`.

Define

`D={q in Q : q<C}`,  `N={q in Q : q||C}`,  `U={q in Q : C<q}`.

### Lemma 3.1 — boundary order facts

`D` is an order ideal of `Q`, `U` is a filter of `Q`, and every `d in D` is below every `u in U`. Moreover:

- there is no relation `n<d` with `n in N,d in D`;
- there is no relation `u<n` with `u in U,n in N`.

**Proof.** If `x<=d<C`, then `x<C`, so `x in D`; hence `D` is an ideal. The filter statement is dual. For `d in D,u in U`, transitivity through any `c in C` gives `d<c<u`, hence `d<u`.

If `n<d` with `n in N,d in D`, then `n<d<c` for every `c in C`, contradicting `n||C`. The second forbidden relation is dual. `□`

### Lemma 3.2 — the neutral region has width at most two

If `width(P)<=3`, then `width(N)<=2`.

**Proof.** Three pairwise incomparable elements of `N`, together with any `c in C`, would form a four-element antichain because every element of `N` is incomparable with every element of `C`. `□`

Thus an autonomous chain in width three leaves a genuinely width-two neutral region around it.

## 4. Exact autonomous-chain corridor formula

Fix `tau in L(Q)`. Let `last_D(tau)` be the position of the last `D` element, with a sentinel immediately before the word when `D` is empty. Let `first_U(tau)` be the position of the first `U` element, with a sentinel immediately after the word when `U` is empty. Since every `d<u`, these boundaries occur in this order.

Define

`K(tau)=#{n in N : last_D(tau)<position_tau(n)<first_U(tau)}`.

So `K(tau)` counts exactly the neutral elements lying in the central window after all `D` and before all `U`.

### Theorem 4.1 — exact fiber weight of an autonomous chain

For every `tau in L(Q)`,

`W_C(tau) := #{L in L(P): L|_Q=tau} = binom(m+K(tau),K(tau)).`     (4.1)

Consequently the restriction of the uniform law on `L(P)` to `L(Q)` is

`mu_C(tau) = binom(m+K(tau),K(tau)) / sum_sigma binom(m+K(sigma),K(sigma)).`     (4.2)

**Proof.** Apply the exact dual prefix recurrence of fleet01/B19. Relative to the deleted chain `C`, the profile interval is

- `I(d)={0}` for `d in D`;
- `I(n)=[0,m]` for `n in N`;
- `I(u)={m}` for `u in U`.

A lift is therefore equivalent to a nondecreasing prefix-count sequence along `tau`, with the above interval restrictions. Every neutral element before the last `D` is forced to prefix count `0`; every neutral element after the first `U` is forced to prefix count `m`. Only the `K=K(tau)` central neutral elements have free values

`0<=t_1<=...<=t_K<=m`.

The number of weakly increasing `K`-tuples from `{0,...,m}` is the stars-and-bars number `binom(m+K,K)`. This proves (4.1), and normalization gives (4.2). `□`

This is much sharper than the general deleted-chain recurrence: the entire nonuniform law collapses to a single integer statistic `K(tau)`.

## 5. Every coupling defect is a boundary defect

### Theorem 5.1 — adjacent-swap localization

Let `tau,tau' in L(Q)` differ by one adjacent swap of incomparable elements. Then

`|K(tau')-K(tau)|<=1`.

Moreover, `K` can change only in one of the following two situations:

1. a `D--N` swap at the **last-D boundary**;
2. an `N--U` swap at the **first-U boundary**.

Every other adjacent incomparable swap preserves `K` and hence preserves the exact fiber weight `W_C`.

When a boundary swap raises `K` from `k-1` to `k` (`k>=1`),

`W_k/W_{k-1} = binom(m+k,k)/binom(m+k-1,k-1) = (m+k)/k = 1+m/k.`     (5.1)

**Proof.** Swapping two adjacent letters can move at most one neutral element across either defining boundary, so `|Delta K|<=1`. Swaps internal to `D`, `N`, or `U` leave both boundaries and neutral membership unchanged. A `D--U` pair is comparable by Lemma 3.1 and therefore cannot be an adjacent incomparable swap. A `D--N` swap changes `K` only when that `D` is the last `D`; an `N--U` swap changes it only when that `U` is the first `U`. Formula (5.1) is the ratio from (4.1). `□`

This exactly identifies the autonomous-chain specialization of fleet01/B19's nested-profile obstruction. Here the only profiles are `{0}`, `[0,m]`, and `{m}`. The only strict nestings are therefore the two module boundaries above. The known unbounded one-swap distortion is no longer mysterious: it occurs at `k=1`, where the ratio is `m+1`.

## 6. Constant-corridor characterization

### Theorem 6.1 — when is the deleted law uniform?

`K(tau)` is constant over all `tau in L(Q)` if and only if

`d<n<u` for every `d in D,n in N,u in U`,

with the statements involving an empty class interpreted vacuously. Equivalently,

`D<N<U`.     (6.1)

In that case `K(tau)=|N|` for every `tau`, and the induced law (4.2) is exactly uniform on `L(Q)`.

**Proof.** If `D<N<U`, every extension places all of `D` before all of `N` before all of `U`, so every neutral element is central and `K=|N|`.

Conversely suppose some `d in D,n in N` are incomparable. In a finite poset, either orientation of an incomparable pair can be extended to a linear extension, so there is `tau` with `n<d`; then `n` occurs before the last `D` and is not central, giving `K(tau)<=|N|-1`.

On the other hand Lemma 3.1 forbids every relation `N<D` and every relation `U<N`; therefore choosing any internal linear extensions of `D,N,U` and concatenating them in the order `D,N,U` gives a valid extension of `Q`. For that extension `K=|N|`. Hence `K` is not constant. The same argument applies if some `n in N,u in U` are incomparable. Thus constant `K` forces all `D<N` and all `N<U`. `□`

### Corollary 6.2 — exact first uncovered induction case is eliminated

Let `P` be a cardinality-minimal counterexample to POS3 and let `C` be a proper autonomous chain. Then `D<N<U` is impossible.

Equivalently, **every proper autonomous chain in a minimal counterexample must be boundary-active**: there exist `d in D,n in N` with `d||n`, or there exist `n in N,u in U` with `n||u`.

**Proof.** If `D<N<U`, Theorem 6.1 says restriction of a uniform random extension of `P` to `Q=P\C` is uniform on `L(Q)`.

If `Q` is a nonchain, then `|Q|<|P|` and `width(Q)<=3`; minimality supplies a balanced incomparable pair in `Q`, and uniformity transfers exactly the same probability to `P`, contradicting that `P` is a counterexample.

If `Q` is a chain, then `P=C union Q` is the union of two chains and hence has width at most two. The known width-two theorem gives a balanced pair, again a contradiction. `□`

This closes the entire constant-corridor autonomous-chain branch of the arbitrary-size induction. Together with the prior fleet04/B19 theorem eliminating proper autonomous nonchains, a minimal counterexample can contain a proper autonomous subset only if it is a **boundary-active chain module**.

## 7. Exact heavy-atom formula inside the corridor

The same fiber formula can be refined to individual comparisons with `C`.

Fix `n in N` and let

`J_C(n)=#{c in C : c precedes n}`.

For a fixed `tau`, suppose `n` is central, there are `k=K(tau)` central neutral elements, and `n` is the `r`-th among those `k` elements in the order `tau`. Then the number of lifts with `J_C(n)=j` is

`binom(j+r-1,r-1) * binom(m-j+k-r,k-r)`,     (7.1)

for `0<=j<=m`.

If `n` lies before the last `D`, then every lift has `J_C(n)=0`; if it lies after the first `U`, every lift has `J_C(n)=m`.

**Proof.** In the dual prefix sequence, fixing the `r`-th central value to `j` leaves a weakly increasing sequence of `r-1` entries in `{0,...,j}` and a weakly increasing sequence of `k-r` entries in `{j,...,m}`. Their stars-and-bars counts are the two factors in (7.1). The noncentral assertions follow from the forced profile values. `□`

Fleet01/B10's heavy-slice law now applies to the pair family `(n,C)`: in a counterexample, there is a unique strong-majority gap `g(n) in {0,...,m}` satisfying

`Pr(J_C(n)=g(n)) > 1/3`.     (7.2)

### Corollary 7.2 — singleton neutral neighbor cannot split a nontrivial module internally

Assume `|N|=1`, write `N={n}`, and `m>=2`. Then in a hypothetical counterexample the strong-majority gap of `n` relative to `C` is an endpoint:

`g(n) in {0,m}`.

In particular `n` cannot lie strictly inside the chain `C` in the common strong-majority order.

**Proof.** Let `M` be the number of extensions `tau in L(Q)` in which `n` is central. For each such `tau`, `k=r=1`, so (7.1) equals `1` for every `j=0,...,m`. For a noncentral `tau`, the only possible values are `j=0` or `j=m`, and its fiber weight is `1`.

Hence for every interior `1<=j<=m-1`, the exact numerator of `Pr(J_C(n)=j)` is `M`. The full extension count satisfies

`E >= (m+1)M`,

because each central `tau` contributes `m+1` lifts. Therefore

`Pr(J_C(n)=j)=M/E <= 1/(m+1) <= 1/3`.

This contradicts the strict heavy-atom requirement (7.2) for any interior gap. `□`

This does not eliminate the singleton-neutral branch completely; it proves that all of its surviving bias is one-sided at an endpoint.

## 8. Regression computation

A standard-library verifier, `verify_autonomous_chain_corridor.py`, independently enumerates small source posets and checks the exact formulas. Its executed output is archived beside this report and ends with

`POS3_AUTONOMOUS_CHAIN_CORRIDOR_CHECK_PASS`

with

- `generated_cases = 1470`;
- `fiber_checks = 9681`;
- `adjacent_incomparable_swap_checks = 21294`.

The test family uses autonomous chains of lengths `m=1,2,3`, `|D|,|U|=0,1,2`, `|N|=1,2`, with varying admissible `D--N` and `N--U` relations. It checks direct full-extension fibers against `binom(m+K,K)`, verifies the constant-corridor characterization, and checks the exact adjacent boundary ratio. These computations are regression evidence only; Theorems 4.1, 5.1 and 6.1 are proved combinatorially above.

## 9. Updated minimal-counterexample core and next obligation

Combining the consumed peer results with this run, a cardinality-minimal POS3 counterexample can be assumed to satisfy simultaneously:

1. width exactly three and the inherited finite small-order exclusions;
2. connected incomparability graph;
3. no proper autonomous nonchain;
4. every proper autonomous chain is boundary-active;
5. every relevant strong-majority insertion gap has mass `>E/3` in the exact three-chain path law;
6. every element has the pinned majority-rank atom from fleet03/B10;
7. deleting a surviving autonomous chain produces the exact one-statistic density `mu(tau) proportional to binom(m+K(tau),K(tau))`, whose only adjacent-swap defects occur at the last-D and first-U boundaries;
8. if the neutral set is a singleton and `m>=2`, its majority gap relative to the module is an endpoint.

The parent target remains open. The first essential unpaid implication is now substantially narrower:

> **Boundary-active chain-module charge.** In the connected minimal core, for a proper autonomous chain `C`, use the two exact boundary defects of Theorem 5.1 together with the `>E/3` heavy-gap constraints to prove that either a `C--N` pair is balanced or a balanced pair in the width-at-most-two remainder survives the corridor weighting. If no proper autonomous subset remains at all, attack the module-prime heavy-slice core by the signed-flux mechanism.

The important point is that no arbitrary chain-weight distortion remains in this branch: it is exactly a binomial function of one central-window statistic, and all nonuniformity is concentrated at two adjacent-swap boundaries.

## 10. Claim status

- Exact autonomous-chain fiber law `W_C(tau)=binom(m+K,K)`: **PROVED**.
- Boundary localization of all adjacent-swap defects: **PROVED**.
- Constant-corridor iff `D<N<U`: **PROVED**.
- Constant-corridor proper autonomous chain impossible in a minimal POS3 counterexample: **PROVED**.
- Singleton neutral element cannot occupy an interior strong-majority gap of a nontrivial autonomous chain: **PROVED**.
- Width-three `1/3–2/3` parent theorem: **NOT PROVED**.
- Outcome: `ESSENTIAL_STEP_APPLIED`.

No novelty or priority claim is made. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid model/API/Codex call, remote workflow, permission change, or public release was used.
