# POS3 fleet02/B10 r12 — exact backtracks leak through two disjoint external Hasse channel families

**Run:** `20260922T084851Z-b10-pos3-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and counts below are for the original uniform law on the full linear extensions of the original poset. No deletion-induced law is used.

## 1. Exact inherited state and other-account results consumed

Fresh shared control was OWNER revision `2026-09-22.2`, programme `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. The active fleet02/B10 assignment is the exact coupling / adjacent-swap route with all conditioning weights retained.

The newest complete campaign-lead report consumed is fleet04/B10 r18:

- `proofnet24/collective-POS3/fleet04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

Its first unpaid statement is `POS3-CROSS-ENVELOPE-BACKTRACK-EXIT-v1`. The local state relevant here is an exact-backtrack heavy bridge

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`,

where `prec_*` denotes the live strong-majority total order in a hypothetical no-balanced-pair candidate. With

`A = #{L:p<r<q}`, `H = #{L:p<q<r}`, `B = #{L:q<p<r}`, `E=e(P)`,

the lead proves

`E=A+H+B`,
`A/E=Pr(r<q)`, `B/E=Pr(q<p)`,
`H/E=Pr(p<q)+Pr(q<r)-1`,

hence `H>E/3`; in the low-endpoint branch `A,B<3E/11`, one has `H>5E/11`. A two-step opposite-ray switch is either span descent, strict envelope expansion, or literal exact backtrack through this bridge.

The named OTHER-account partner result consumed and applied is fleet03/B11 r11d:

- `proofnet24/collective-POS3/fleet03/B11/20260922T081117Z-fleet03-B11-pos3-r11d/REPORT.md`, blob `56374ff9d4b1bf188929919d05e52b34c00868b6`.

Its exact factor-two theorem says: if the only two distinguishers of `a||b` are comparable positive upper distinguishers `u<v` with `a<u<v`, `b||u,v`, then

`N(b<u)=2N(b<a)`,

with the exact order-dual identity for two comparable positive lower distinguishers. It is proved fiberwise with full lift multiplicities retained.

The immediate fleet02/B10 predecessor is

- `proofnet24/collective-POS3/fleet02/B10/20260922T075033Z-b10-pos3-r11/REPORT.md`, blob `c82c5309ce2cf74a1c103149b879249eaa1ffce9`.

For any strong incomparable pair `a prec_* b`, swapping the positions of `a,b` in full extensions gives outgoing/incoming illegal-swap sets `O,I` satisfying

`|O|-|I| = 2N(a<b)-E`.

Every outgoing failure has a Hasse witness in

`U(a,b)={z:a lessdot z, z||b}` or `D(a,b)={z:z lessdot b, z||a}`,

and width at most three gives `|U|,|D|<=2`.

## 2. Compact conditional route

Assume for contradiction a width-at-most-three no-balanced-pair poset and enter the lead's exact-backtrack heavy bridge. The lead had reduced the global obstruction to reuse of such heavy backtracks after envelope expansions. The first question is whether a literal backtrack can be locally closed, using only the central cover `p lessdot r` in both directions.

It cannot. Exact transposition accounting forces noncentral outgoing swap defects on **both** side pairs `(p,q)` and `(q,r)`. Width three then compresses each side into at most three external Hasse channels. In the lead's low-endpoint branch, one external channel on each side carries more than `2E/33` extensions. The two external channel families are vertex-disjoint because any common witness would contradict either incomparability or the cover `p lessdot r`.

Thus a heavy exact backtrack is not a two-state recycler: unless an endpoint is already in the near-balance range `[3/11,1/3)`, it emits two distinct external packets of the same `>2/33` scale used by the lead's typed-gate machinery.

## 3. Exact two-sided leakage theorem

Keep the heavy bridge

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`.

Let `O_L,I_L` be the outgoing and incoming illegal endpoint-position swaps for the pair `(p,q)`, oriented `p<q`. Let `O_R,I_R` be the analogous sets for `(q,r)`, oriented `q<r`.

### Lemma 3.1 — left external-defect mass

`|O_L cap {p<q<r}| >= H-B`.                                      (3.1)

**Proof.** For `(p,q)`, the majority and minority counts are

`M_L=A+H`, `N_L=B`.

The exact transposition identity gives

`|O_L|-|I_L|=M_L-N_L=E-2B`,

so `|O_L|>=E-2B`. Every extension in the cell `A={p<r<q}` is an outgoing illegal swap: exchanging `p,q` moves `p` to the right of `r`, violating the forced relation `p<r`. Hence `A subset O_L`. Since the `p<q` extensions are exactly the disjoint cells `A` and `H`,

`|O_L cap H|=|O_L|-A >= E-2B-A = H-B`.

No conditioning has occurred. `square`

Because `H>E/3` and `B<E/3`, the right side of (3.1) is strictly positive. Thus every exact backtrack has a noncentral outgoing defect on the left side.

### Lemma 3.2 — right external-defect mass

`|O_R cap {p<q<r}| >= H-A`.                                      (3.2)

**Proof.** For `(q,r)`, the majority and minority counts are

`M_R=B+H`, `N_R=A`.

Thus

`|O_R|-|I_R|=E-2A`,

so `|O_R|>=E-2A`. Every extension in `B={q<p<r}` is an outgoing illegal swap for `(q,r)`: exchanging `q,r` moves `r` to the left of `p`, violating `p<r`. Hence `B subset O_R`. Removing this central cell leaves

`|O_R cap H|=|O_R|-B >= E-2A-B = H-A`.

Again this is an identity on the original full extension set. `square`

Since `A<E/3`, (3.2) is also strictly positive.

### Lemma 3.3 — at most three external Hasse channels per side

For the left side, `r in U(p,q)` because `p lessdot r` and `r||q`. Width three gives

`|U(p,q)|<=2`, `|D(p,q)|<=2`.

Hence after deleting the central channel `r`, at most three Hasse witness vertices remain. Every extension counted by (3.1) has an external Hasse witness, because in the middle cell `p<q<r` the central vertex `r` is not between the swapped endpoints.

Therefore some left external Hasse channel carries at least

`(H-B)/3`                                                        (3.3)

marked full extensions.

Dually, `p in D(q,r)`, and some right external channel carries at least

`(H-A)/3`.                                                       (3.4)

### Lemma 3.4 — the two external channel families are vertex-disjoint

Put

`W_L=(U(p,q) union D(p,q))\{r}`,
`W_R=(U(q,r) union D(q,r))\{p}`.

Then

`W_L cap W_R = emptyset`.                                       (3.5)

**Proof.** Let `z` be a hypothetical common witness. There are four type combinations.

- `z in U(p,q) cap U(q,r)` would require `z||q` and `q<z`.
- `z in D(p,q) cap D(q,r)` would require `z<q` and `z||q`.
- `z in D(p,q) cap U(q,r)` would require `z<q<z`.
- `z in U(p,q) cap D(q,r)` would require `p<z<r`, contradicting the cover `p lessdot r`.

All four are impossible. `square`

Thus the left and right leak packets necessarily use different vertices. This is stronger than merely saying that a selected central channel can be left and re-entered: a literal backtrack has two disjoint noncentral Hasse-support families already present in the full-law swap defect.

### Theorem 3.5 — low-endpoint exact backtrack emits two `>2/33` packets

If additionally

`A<3E/11`, `B<3E/11`,

then the lead gives `H>5E/11`. Hence

`H-B>2E/11`, `H-A>2E/11`.

By (3.3)-(3.4), there is a left external Hasse channel and a right external Hasse channel, on distinct witness vertices, each carrying strictly more than

`2E/33`                                                         (3.6)

marked full extensions.

Each channel marks a genuine order event of an incomparable pair. Applying the same no-balanced dichotomy as in fleet02/B10 r11, a marked orientation either produces the accepted strict span-descent exit, or is the minority orientation of a new outward pair with probability `>2/33`.

Thus, after span descent is removed, a low-endpoint exact backtrack emits **two distinct external outward packets** of scale `>2/33`.

### Corollary 3.6 — exact-backtrack dichotomy

Every heavy exact backtrack in a no-balanced width-three candidate satisfies at least one of:

1. `A>=3E/11` or `B>=3E/11`; then one endpoint minority lies in `[3/11,1/3)`;
2. strict span descent occurs on one of the noncentral channels;
3. there are two distinct external Hasse witness vertices, one from each side, each supporting an outward minority event of probability `>2/33`.

The third branch is the only genuinely low-endpoint non-descent recycler left by this theorem.

## 4. Direct application of the named partner's factor-two identity

The partner theorem further pays the minimal-support same-sign comparable subcase of the two leaks.

On the left pair `(p,q)`, the central distinguisher `r` is positive upper: `p<r`, `q||r`. Suppose the only other relation distinguisher is `z`, it is also positive upper, and `z` is comparable with `r`. Because `p lessdot r`, the relation `p<z<r` is impossible, so comparability forces

`p<r<z`, `q||r,z`.

The fleet03/B11 factor-two identity gives

`N(q<r)=2N(q<p)`.

But `q prec_* r` requires `N(q<r)>2E/3`, while `p prec_* q` gives `N(q<p)<E/3`, a contradiction.

Dually, on `(q,r)`, the central distinguisher `p` is positive lower. If the only other distinguisher `z` is positive lower and comparable with `p`, the cover forces `z<p<r`, and the lower-chain factor-two identity gives

`N(p<q)=2N(r<q)`,

contradicting `p prec_* q` and `q prec_* r`.

Therefore an exact-two minimum-support side cannot hide its external leak in a comparable same-sign chain. Its remaining exact-two possibilities are crossed-sign or central-incomparable support, which are precisely the types already isolated by the partner/lead exact-two machinery. The new theorem above is needed for the non-exact / multi-distinguisher branch because it does not assume only two distinguishers.

## 5. What this changes in the lead residual

The lead r18 residual was global reuse of strict envelope expansions together with non-exact/multi-distinguisher exact-backtrack heavy bridges. The present result removes the possibility that such a heavy backtrack is locally closed.

A low-endpoint exact backtrack now has a compulsory **double leakage budget**:

- one noncentral left packet `>2E/33`;
- one noncentral right packet `>2E/33`;
- their Hasse witness vertices are distinct;
- either packet becoming majority is an already accepted strict span-descent exit.

So the first unpaid global implication is narrower:

> **`POS3-DISJOINT-DOUBLE-LEAK-REUSE-v1`.** In a span-descent-exhausted no-balanced width-three candidate, prove that the two disjoint `>2/33` outward leak packets forced by every low-endpoint exact backtrack cannot both be routed through later envelope expansions and then reused indefinitely. Show that the first attempted reuse yields a balanced pair, a strict span descent, a four-antichain, a proper autonomous/ordinal reduction, or one of the already controlled exact-two/coherent-gate states.

This is genuinely global; the present report does not supply a monotone potential across arbitrary sequences of envelope expansions.

## 6. Status and integrity

- fresh collective owner control and fleet02/B10 assignment: **CONSUMED**;
- campaign lead fleet04/B10 r18: **CONSUMED/APPLIED**;
- named partner fleet03/B11 r11d: **CONSUMED/APPLIED**;
- own r11 exact transposition/Hasse-channel identity: **CONSUMED/APPLIED**;
- exact left external defect lower bound `H-B`: **PROVED**, arbitrary finite size;
- exact right external defect lower bound `H-A`: **PROVED**, arbitrary finite size;
- left/right external Hasse witness families disjoint: **PROVED**;
- low-endpoint double packet `>2E/33` on distinct vertices: **PROVED**;
- minimal exact-two comparable same-sign support: **ELIMINATED** using the named partner factor-two identity;
- global disjoint-double-leak reuse: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- classification: **`ESSENTIAL_STEP_APPLIED`**.

No finite census or numerical computation was used in this run. The proof is exact and arbitrary-size. No benchmark material, held-out answers, credentials, scheduler identifiers, machine paths, unrelated private data, email/Drive data, paid model/API/Codex execution, workflow dispatch, permission change, or public posting was used.
