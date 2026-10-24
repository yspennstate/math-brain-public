# POS3 account04/B11 — exact finite-memory reduction of the bounded-incomparability residue

**Run:** `20260922T080947Z-B11-pos3-r18`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x precedes y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below refer to the original uniform law on all full linear extensions. No projected/deletion law is silently replaced by a uniform law. No finite-kernel reduction is assumed or claimed.

## 1. Exact state consumed

Fresh control was resolved at invocation start at `yspennstate/math-research-brain` main commit

`6f64e5b9989523a52d87669dbf053f8c0a35521f`.

The five mandatory control files and the full OWNER MESSAGE were read at that exact commit. OWNER CONTROL was revision `2026-09-22.2`; the collective-open-problems allocation remained active and there was no applicable `account04/B11` pause or stop. The matching `ORDER.md`, `TARGETS.md`, and `ASSIGNMENTS.json` were also read at that commit.

The latest complete team-lead report used is

- account04/B10 r17, `proofnet24/collective-POS3/account04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

Its remaining same-ray low-endpoint obstruction is the coherent width-saturating three-antichain gate. A compatible fresh OTHER-account theorem,

- account01/B11 r11, `proofnet24/collective-POS3/account01/B11/20260922T071414Z-b11-pos3-r11/REPORT.md`, science commit `01da2a8749560844b073d4f4fe8f1e2b1bafe658`,

pays that *local* coherent gate: a selected Hasse pivot either reaches an actual pair in `[3/11,1/3)`, triggers an already authorized span/reduction exit, or preserves a `>2/33` packet while exporting it to a non-return strong-order frontier. It explicitly leaves the global near-band/mixed-recycling step open.

The newest complete assigned-partner report available before the derivation is

- account01/B19 r13, `proofnet24/collective-POS3/account01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`.

It proves, from an exact eight-word full-extension decomposition, the four-pair selector `max M_i >= 3E/11`, the exact continuing-corridor recurrence

`A_(i-1)+3A_i+A_(i+1)=E+K`,

and an exponential Green-kernel boundary-decay formula for a repeated exact-two corridor. A newer B19 r14 had only a start record when this derivation began, so no unfinished result is treated as complete.

The source theorem used for the exceptional branch is Max Aires and Jeff Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134v1. Its Theorem 1.6 says that for fixed width, `delta(P)->1/2` when `pi(P)->infinity`; the paper explicitly presents this as a qualitative bounded-width large-range theorem. Thus a hypothetical width-three poset with `delta(P)<1/3` has `pi(P)<=K_3` for some finite source-qualitative constant `K_3`. I do **not** assign an invented numerical value to `K_3`.

Inherited B11 source work plus the 6-thin theorem places the actual exceptional band at

`7 <= pi(P) <= K_3`.

The earlier B11 `R_N` family shows that even `pi(P)=7`, connectedness, module-primality, bounded rank variance, and bounded insertion multiplicity do **not** bound `|P|`. That failure is retained below.

## 2. Why a different mechanism is needed

Recent B11 runs localized certified packet probabilities by variance and then studied Hasse-packet exits. The local coherent gate is now paid by account01/B11, but an arbitrary-size mixed walk can still propagate through many local windows. The earlier `R_N` family rules out a bounded-corridor-length argument.

This run therefore changes mechanism. Instead of trying to prove another local packet constant, it proves an exact **finite-memory representation** for every bounded-`pi` poset and then identifies precisely how the arbitrary-size exterior can still influence a local pair probability. The conclusion is finite *boundary dimension*, not a finite poset kernel.

## 3. Two deterministic locality lemmas

Let `P` be any finite poset, let

`L_0=(v_1,...,v_n)`

be **any** fixed linear extension, and put

`K=pi(P)=max_v |Inc(v)|`.

No width or no-balanced hypothesis is needed in this section.

### Lemma 3.1 — rank displacement is at most the incomparability degree

For every linear extension `L` and every `v_i`,

`|rank_L(v_i)-i| <= |Inc(v_i)| <= K`.                         (3.1)

#### Proof

For an element `v`, every predecessor is before `v` in every extension and every successor is after it. Hence

`rank_L(v)=|Pred(v)|+1+#{z in Inc(v): z precedes v in L}`.    (3.2)

The last term takes values between `0` and `|Inc(v)|`. Apply (3.2) to `L` and to the reference extension `L_0` and subtract. `square`

This is stronger, for bounded range, than the previous variance-derived packet radii: it controls **every** extension and **every** element, not only high-probability pair events.

### Lemma 3.2 — incomparability and cover bandwidth in every linear extension

For indices `i<j`:

1. if `v_i || v_j`, then

   `j-i <= 2K-1`;                                              (3.3)

2. if `v_i lessdot v_j`, then

   `j-i <= 2K+1`.                                              (3.4)

#### Proof

Assume first `v_i||v_j`. If an intermediate `v_t`, `i<t<j`, were comparable with both endpoints, the fact that `L_0` is a linear extension would force

`v_i < v_t < v_j`,

contradicting `v_i||v_j`. Thus every one of the `j-i-1` intermediate vertices lies in

`(Inc(v_i)\{v_j}) union (Inc(v_j)\{v_i})`,

whose cardinality is at most `2K-2`. This gives (3.3).

Now assume `v_i lessdot v_j`. Any intermediate vertex comparable with both would again satisfy `v_i<v_t<v_j`, contradicting that the relation is a cover. Hence all `j-i-1` intermediate vertices lie in `Inc(v_i) union Inc(v_j)`, of size at most `2K`; this gives (3.4). `square`

Two immediate campaign consequences in the exceptional branch `K<=K_3` are:

- the lead/account01-B11 coherent three-antichain `y prec_* b prec_* c` lies in a strong-order interval of at most `2K_3` positions, because the outer pair `y||c` itself is incomparable;
- every heavy Hasse turning triple `u prec_* v prec_* w` with `u lessdot w` lies in an interval of at most `2K_3+2` positions.

Thus the earlier universal radii `2790` and `5920` remain valid, but in the actual high-comparability residue they can be replaced by the sharper *structural* bounds `2K_3-1` for incomparable packet edges and `2K_3+1` for cover chords.

## 4. Direct application to account01/B19 r13

In the partner's continuing four-pair exact-two window, the displayed minority directions are

`d<e`, `x<d`, `y<x`, `u<y`.

Therefore the strong-majority reference order is

`e prec_* d prec_* x prec_* y prec_* u`,

and all four consecutive displayed pairs are incomparable. Lemma 3.2 gives a structural span at most `2K-1` for each adjacent pair. Hence the entire five-label exact-two window lies in a strong-order interval whose endpoint distance is at most

`4(2K-1)=8K-4`.                                                (4.1)

In the exceptional branch this is at most `8K_3-4`, independently of `|P|`.

This is a direct strengthening of the previous B11 use of the partner's `3/11` selector: it localizes not merely the selected pair but the *whole exact transfer gadget*. At the same time B19's Green-kernel formula shows why such localization is not closure: a repeated exact-two transfer word can be arbitrarily long, with boundary influence decaying but not becoming identically zero at a finite distance.

## 5. Exact finite-memory transfer theorem

The deterministic displacement bound (3.1) gives an exact arbitrary-size dynamic program.

Before output rank `t` is chosen in a linear extension, every reference index

`i < t-K`

has already been placed, because its latest possible rank is `i+K<t`. Every reference index

`i > t+K`

is still unplaced, because its earliest possible rank is `i-K>t`. Therefore the only uncertain vertices are in the sliding reference window

`W_t={v_i: t-K <= i <= t+K}`,                                  (5.1)

intersected with `[1,n]`, of size at most `2K+1`.

### Theorem 5.1 — exact bounded-memory enumeration

For fixed `K`, the full extension count `e(P)` is computed exactly by a left-to-right transfer process whose state at time `t` is the bit mask recording which vertices of `W_t` have already been placed. There are at most

`D_K = 2^(2K+1)`                                               (5.2)

mask states at any time. A candidate next vertex is legal iff all of its predecessors inside `W_t` are marked placed; predecessors to the left are forced placed by (3.1), and there are no predecessors to its right in the reference extension.

Thus there are finite nonnegative-integer transfer matrices `T_t` of dimension at most `D_K` such that

`e(P) = lambda_0^T T_1 T_2 ... T_n rho_n`                     (5.3)

for the canonical start/end vectors.

#### Proof

The forced-left/forced-right statement above proves that a prefix ideal is completely determined by its mask on `W_t`. For a candidate `v_i in W_t`, all predecessors have reference index `<i`; any predecessor left of `W_t` is already placed, and every other predecessor occurs in the mask. Hence legality is determined by the mask and the induced order in the current window. After a legal choice, slide the window one step and delete the forced-left coordinate / add the forced-right coordinate. This gives an exact transition between masks. Summing path counts gives (5.3). `square`

The transition *types* are also finite for fixed `K`: each step sees only the induced order on at most `2K+2` consecutive reference vertices. This is a finite alphabet of local matrices, although the word length `n` remains arbitrary.

### Theorem 5.2 — every incomparable-pair probability has an exact finite-boundary representation

Let `v_i||v_j`, `i<j`, and let

`p_ij=Pr(v_i precedes v_j)`.

By Lemma 3.2, `j-i<=2K-1`. By (3.1), neither `v_i` nor `v_j` can appear outside output ranks

`[i-K,i+K]` and `[j-K,j+K]`.

Consequently the event `v_i precedes v_j` is completely decided inside the output-rank block

`I=[i-K, j+K]`,                                                (5.4)

whose length is at most

`(j-i)+2K+1 <= 4K`.                                           (5.5)

Let `A_I` be the transfer product across this block with all legal transitions, and let `B_I` be the same product with transitions that place `v_j` before the still-unplaced `v_i` suppressed. Let `lambda` be the nonnegative count vector produced by all transfer steps before `I`, and `rho` the nonnegative completion-count vector produced by all steps after `I`. Then exactly

`p_ij = (lambda^T B_I rho)/(lambda^T A_I rho).`                (5.6)

Moreover every transfer step in `I` only inspects reference indices within `K` of its output rank, so the union of reference vertices needed for the local block lies in

`[i-2K, j+2K]`,                                                (5.7)

containing at most

`(j-i)+4K+1 <= 6K`                                            (5.8)

vertices.

#### Proof

Before the first rank in `I`, neither endpoint can yet have appeared; after the last rank in `I`, both must already have appeared, by (3.1). Therefore suppressing exactly the local transitions that realize `v_j` first counts precisely the full extensions satisfying `v_i before v_j`. Prefix and suffix choices contribute only their exact count vectors `lambda,rho`, giving (5.6). The reference-window union bound is immediate from (5.1). `square`

### Corollary 5.3 — outside influence is finite-dimensional but not absent

For entries with `(A_I)_{ab}>0`, define the boundary-conditioned local ratio

`r_ab=(B_I)_{ab}/(A_I)_{ab}`.

Equation (5.6) writes `p_ij` as a weighted average of the finitely many `r_ab`, with nonnegative weights

`lambda_a (A_I)_{ab} rho_b`.

Hence

`min r_ab <= p_ij <= max r_ab`                                (5.9)

over boundary states receiving positive weight.

This is the exact distinction demanded by the assignment:

- **finite boundary dimension:** proved;
- **finite whole-poset kernel:** not proved and generally false as a consequence of bounded `K` alone;
- **boundary vectors can retain arbitrary-length information:** still live.

The `R_N` family is consistent with this theorem: its local transfer type repeats for arbitrarily long corridors while the terminal boundary continues to perturb interior probabilities by a decaying but nonzero amount.

## 6. What the actual Aires--Kahn theorem now gives

Aires--Kahn Theorem 1.6 states, qualitatively, that for fixed width `w`, `delta(P)->1/2` as `pi(P)->infinity`. Set `w=3` and use the contradiction hypothesis `delta(P)<1/3`. Then there exists some finite source-dependent `K_3` such that every hypothetical counterexample lies in `pi(P)<=K_3`.

Combining with Theorems 5.1--5.2 gives an exact arbitrary-size reduction:

> Any hypothetical POS3 counterexample is represented by an arbitrary-length word over a finite alphabet of local transfer matrices of dimension at most `2^(2K_3+1)`. Every individual incomparable-pair probability is a ratio of two bilinear forms across a local block involving at most `6K_3` reference vertices, with the rest of the arbitrarily large poset entering only through two nonnegative boundary count vectors.

This is a true consequence of the source theorem. It does **not** say that only finitely many posets need be checked, does **not** require an explicit numerical value of `K_3`, and does **not** replace the arbitrary-length problem by a finite census.

## 7. Compact conditional end-to-end route after this run

Assume a cardinality-minimal width-three no-balanced poset.

1. Aires--Kahn + the inherited small-range theorem put it in `7<=K<=K_3`.
2. The present transfer theorem makes the full extension law a bounded-memory one-dimensional cocycle with finite boundary dimension.
3. Account01/B19 r13 controls one important repeated local word exactly: a continuing exact-two word has a `3/11` actual-pair selector and an explicit exponentially decaying Green-kernel boundary term.
4. Account04/B10 r17 plus account01/B11 r11 control the current non-exact coherent gate locally: it yields a `[3/11,1/3)` pair, a known reduction, or a non-return `>2/33` frontier packet.
5. Lemmas 3.1--3.2 show every such packet/gate/turn is `O(K_3)`-local in the reference order.

The first unpaid implication is therefore no longer a vague finite-kernel step. It is the following finite-dimensional but arbitrary-word statement.

> **FINITE-BOUNDARY MIXING / SIMPSON CLOSURE.** For the admissible width-three transfer cocycle with `K<=K_3`, prove that the boundary count vectors in (5.6) cannot keep every locally produced `[3/11,1/3)` / `>2/33` packet globally below `1/3` through an arbitrarily long mixed sequence of exact-two and coherent-gate matrices, unless one of the already-authorized strict span, autonomous/ordinal, opposite-ray, or terminal-boundary exits occurs.

The target is specifically about the *boundary vectors*. A local finite census by itself would be insufficient: an older account01/B19 renewal counterexample already shows that biased lift weights can move a pair from an endpoint-balanced uniform residual law to `9/13` in the full law. Conversely, B19 r13 proves genuine boundary contraction for the repeated exact-two subword. The new reduction says that extending such contraction/charge control to the finite set of mixed gate transfer types is exactly the remaining high-comparability task.

This is materially different from the last packet-radius runs and preserves the known failure rather than renaming it.

## 8. Deterministic regression

Two independent local scripts were run as regression only; neither finite computation is used as proof of the arbitrary-size theorems.

`verify_banded_transfer.py` enumerates every transitive closure generated by forward relations on `[n]` for `2<=n<=6`, then every linear extension, checking Lemmas 3.1--3.2. Captured output:

```text
n=2 closures=2 extensions=3
n=3 closures=7 extensions=20
n=4 closures=40 extensions=260
n=5 closures=357 extensions=6105
n=6 closures=4824 extensions=245877
POS3_BANDED_TRANSFER_REGRESSION_PASS
closures_total 5230
extensions_total 252265
```

`verify_finite_memory_transfer.py` independently compares the sliding-window transfer count with direct topological-sort enumeration and checks both orientation counts for every incomparable pair. Captured output:

```text
n=2 closures=2 extensions=3 incomparable_pair_tests=1
n=3 closures=7 extensions=20 incomparable_pair_tests=11
n=4 closures=40 extensions=260 incomparable_pair_tests=130
n=5 closures=357 extensions=6105 incomparable_pair_tests=1984
n=6 closures=4824 extensions=245877 incomparable_pair_tests=41044
POS3_FINITE_MEMORY_TRANSFER_CHECK_PASS
closures_total 5230
extensions_total 252265
incomparable_pair_tests_total 43170
```

The exact scripts and captured outputs are stored beside this report.

## 9. Status and integrity

- latest complete lead account04/B10 r17: **CONSUMED/APPLIED**;
- assigned partner account01/B19 r13: **CONSUMED/APPLIED**;
- fresh account01/B11 coherent-gate theorem: **CONSUMED/APPLIED**;
- source theorem Aires--Kahn Theorem 1.6: **RECHECKED AT SOURCE AND APPLIED QUALITATIVELY**;
- deterministic rank displacement `<=pi(v)`: **PROVED**;
- incomparability span `<=2K-1` in any reference linear extension: **PROVED**;
- cover span `<=2K+1`: **PROVED**;
- exact sliding-window state dimension `<=2^(2K+1)`: **PROVED**;
- exact local pair block length `<=4K` and reference support `<=6K`: **PROVED**;
- exact bilinear boundary-vector formula (5.6): **PROVED**;
- finite whole-poset kernel: **NOT CLAIMED**;
- finite-boundary mixing / global Simpson closure: **OPEN / FIRST ESSENTIAL MISSING IMPLICATION**;
- POS3: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No novelty/priority claim is made from search. No benchmark work, brain installation, benchmark gold, credentials, email/Drive access, paid/remote compute, workflow dispatch, public posting, permission bypass, or scheduler mutation was used. The run remains `WITHOUT_VERIFIED_BRAIN` because no genuine authenticated brain retrieval/context use occurred.
