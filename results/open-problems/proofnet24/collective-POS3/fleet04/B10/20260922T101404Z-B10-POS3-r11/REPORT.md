# POS3 fleet04/B10 — earliest-prefix chain kills the first exact-return recycler

**Run:** `20260922T101404Z-B10-POS3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14`, unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and extension counts in the dependencies below are under the original uniform law on all full linear extensions. No deletion-induced law is treated as uniform.

## 1. Exact state and named other-account result

The lead state consumed is fleet04/B10 run `20260922T091028Z-fleet04-B10-pos3-r11`, report blob `8a856fa924002567c01a8b70880003fe53b86da3`. It chooses the earliest strong-majority right endpoint `q`, then a left endpoint `p`, proves the lower Hasse family `D(p,q)` is empty, and proves that the first resulting heavy bridge cannot be span-exhausted. Its first unpaid statement is `POS3-EARLIEST-BARRIER-DESCENT-SPLICE-v1`: after taking the forced strict span descent, rule out a later reset to the original earliest barrier.

The named OTHER-account partner result consumed and applied is fleet01/B11 run `20260922T085231Z-b11-pos3-auto11`, report blob `a35d4aafa2b2dabca5e436de102475b21cd6bdc9`, together with its late source note blob `f3c4eb3e46b6a5e2906b16b412e9fd9689e816e2`. Its disjoint-support theorem proves that a rigid low-endpoint Mode-T exact backtrack either emits genuinely fresh distinguishing support or strictly expands the strong-order envelope. The late note sharpens the only surviving first-reuse obstruction to a genuinely multi-distinguisher Mode-T state carrying two distinct external leak packets.

I also use fleet01/B10 run `20260922T084926Z-b10-pos3-r13`, report blob `907ef9d19e23c05bc68a13c34ddb5a4aad6e30df`. It proves threshold-free heavy-bridge support purification: after balance and authorized strict span descent are excluded, positive support is exactly Mode T (`F2,F3`) or Mode F (`F1,F4`), and a span-exhausted heavy bridge has a child with smaller left strong-order rank.

The newer fleet01/B11 directory `20260922T091716Z-b11-pos3-r11` was checked but contained only its start marker at this run's scientific snapshot, so no uncommitted conclusion was inferred from it.

## 2. New extremal structural lemma: the whole earliest prefix is a chain

Assume for contradiction that `P` is a finite width-at-most-three poset with no balanced pair. Use the already-established fact that the strong-majority relation `prec_*` is a strict total order. Let `rho` be its rank.

Choose `q` with minimum `rho(q)` among all later endpoints of oriented incomparable pairs `u||v`, `u prec_* v`.

### Lemma 2.1 — prefix-chain lemma

The set

`C_q={v : v prec_* q}`

is a chain in the poset, ordered exactly as `prec_*`.

**Proof.** If two vertices `u,v prec_* q` were incomparable, orient them by the total order, say `u prec_* v`. Then `(u,v)` would be an incomparable pair whose later endpoint `v` has `rho(v)<rho(q)`, contradicting the choice of `q`. Hence every two prefix vertices are comparable. A poset relation must agree with `prec_*`, because a comparable pair has ordering probability one. `square`

### Lemma 2.2 — the left-incomparable set is a terminal chain segment

Let

`I_q={v prec_* q : v||q}`.

Then `I_q` is a nonempty terminal segment of the chain `C_q`.

**Proof.** It is nonempty by the definition of `q`. No prefix vertex can satisfy `q<v` in the poset, because then `q prec_* v`. Thus each prefix vertex is either below `q` or incomparable with it. If `x prec_* y prec_* q`, `x||q`, and `y<q`, then the chain property gives `x<y<q`, contradicting `x||q`. Therefore once incomparability with `q` begins along the prefix chain it persists to the end. `square`

Let `p` be the maximum element of `I_q` in `prec_*`.

### Corollary 2.3 — `(p,q)` is an adjacent strong-order incomparable pair

There is no vertex strictly between `p` and `q` in `prec_*`.

**Proof.** A vertex `w` between them would lie in `C_q`. If `w||q` it contradicts maximality of `p` in `I_q`; if `w<q`, then the prefix chain gives `p<w<q`, contradicting `p||q`. `square`

This is stronger information than the previous lead selection: the canonical earliest barrier can be chosen with its incomparable pair literally adjacent in the strong-majority order.

## 3. The earliest adjacent barrier has no lower Hasse support

For an oriented incomparable pair define

`D(p,q)={z : z lessdot q, z||p}`,
`U(p,q)={z : p lessdot z, z||q}`.

### Lemma 3.1

`D(p,q)=emptyset`.

**Proof.** If `z lessdot q`, then `z prec_* q`, so both `z` and `p` lie in the prefix chain `C_q`. Lemma 2.1 makes them comparable, contradicting `z||p`. `square`

The exact endpoint-transposition identity from the collective work gives

`|O|-|I| = 2N(p<q)-E > E/3`

because `p prec_* q` and the pair is assumed unbalanced. Hence some outgoing Hasse channel exists. Lemma 3.1 forces it into `U(p,q)`. Choose `r in U(p,q)`. Then

`p lessdot r`, `r||q`.

Since `p<r` in the poset, `p prec_* r`. Corollary 2.3 leaves no strong-order position for `r` strictly between `p` and `q`; therefore

`p prec_* q prec_* r`.                                           (3.1)

Thus the first export from the rightmost earliest pair always creates a heavy Hasse bridge `(p,q,r)`; the former inward-U subcase is absent for this selection.

## 4. New theorem: a heavy bridge based at the earliest barrier cannot be a span-exhausted return

For the heavy bridge `(p,q,r)` use the standard families

`F1={z : p lessdot z, z||q, z!=r}`,
`F2={z : z lessdot q, z||p}`,
`F3={z : q lessdot z, z||r}`,
`F4={z : z lessdot r, z||q, z!=p}`.

Lemma 3.1 says structurally

`F2=emptyset`.                                                    (4.1)

### Theorem 4.1 — earliest-barrier exact-return obstruction

Any heavy bridge `(p,q,r)` satisfying (3.1), whether it is the first export or a later attempted exact return to the same earliest barrier, cannot be both unbalanced and span-exhausted. Equivalently, every such attempted return exposes either a balanced pair or an authorized strict strong-majority span descent before the proof needs to accept the literal return.

**Proof.** Assume no balanced pair and remove all authorized strict span-descent exits from the bridge. Apply fleet01/B10's threshold-free purification. The surviving positive support must be one of:

- Mode T: `F2^+,F3^+` nonempty and `F1^+=F4^+=empty`;
- Mode F: `F1^+,F4^+` nonempty and `F2^+=F3^+=empty`.

Mode T is impossible by (4.1).

In Mode F choose `c in F4^+`. Ray localization in the same theorem places every positive `F4` witness strictly to the left of `p` in `prec_*`. Hence `c prec_* p prec_* q`, so `c,p` both belong to the prefix chain `C_q`. Lemma 2.1 gives the poset relation `c<p`. But the heavy bridge has `p<r`, while `c in F4` gives the cover `c lessdot r`. Thus

`c < p < r`,

contradicting `c lessdot r`.

Both span-exhausted modes are impossible. `square`

### Corollary 4.2 — the descent forced at the earliest barrier is one-sided

The pair `(p,q)` itself has strong-order span one, so it admits no strict subspan. Therefore the descent exposed by Theorem 4.1 cannot be a descent inside the left side `(p,q)`; it must occur on the right side of the heavy bridge or in its right-ray blocker geometry.

This matters for the global splice: the earliest barrier does not send the proof back into an uncontrolled left envelope.

## 5. Direct application of fleet01/B11: its remaining multi-support recycler is absent at the earliest barrier

The partner's late source note identifies the remaining low-endpoint first-reuse obstruction as a genuinely multi-distinguisher **Mode-T** state carrying two distinct external leak packets.

At the earliest barrier this state cannot occur at all. Its left active family is exactly `F2`, but (4.1) is structural, not a support-size estimate: there is no vertex `z lessdot q` incomparable with `p` because every vertex before `q` lies in the prefix chain. Hence the partner's `POS3-DISJOINT-DOUBLE-LEAK-MULTISUPPORT-REUSE-v2` obstruction is not live when the repeated envelope is the globally earliest barrier.

The same conclusion is visible directly in the partner's rigid two-distinguisher theorem. In a return with left pair `(l,x)=(p,q)`:

- an L- support has `z_L<q` and `z_L||p`, impossible by the prefix-chain lemma;
- in the only simultaneous inward disjoint-support case L+/R-, the partner theorem derives `z_R prec_* p` and `z_R||p,q`; again `z_R,p` are two incomparable vertices before `q`, impossible by Lemma 2.1;
- therefore a rigid disjoint-support return can only emit fresh distinguishing support or expand on the right; shared support was already reduced by the partner to a central double-fork/multi-distinguisher exit.

The threshold-free argument in Theorem 4.1 is stronger for the literal earliest return: even genuinely many-support Mode T is excluded because `F2` itself is empty, and Mode F is excluded by the Hasse-cover contradiction.

## 6. What this pays and what remains

This run pays the first-return part of `POS3-EARLIEST-BARRIER-DESCENT-SPLICE-v1`:

> **Paid implication.** Choose the rightmost incomparable predecessor `p` of the globally earliest incomparable right endpoint `q`. The prefix before `q` is a poset chain, `(p,q)` is adjacent in `prec_*`, every transposition export is outward, and **no later heavy-bridge exact return to `(p,q)` can be a span-exhausted recycler**. Before accepting such a return the proof has a balanced pair or a strict span-descent exit. The partner's remaining low-endpoint multi-support Mode-T first-reuse obstruction is impossible at this barrier.

What is still unpaid is strictly narrower:

> **`POS3-POST-BARRIER-SINK-CYCLE-v1`.** After taking the forced right-side descent away from `(p,q)`, rule out a finite closed reduction cycle that stays away from the earliest barrier and never needs a literal return to `(p,q)`. Equivalently, show that the first closed strongly connected reduction component to the right has a balance/descent/autonomous-or-ordinal exit, or construct a source-valid counterexample to that proposed splice.

The present argument does **not** prove that every later non-earliest state has a chain prefix, and it does not promote a generic multi-distinguisher state to balance. Those are not silently assumed.

## 7. Status

- exact width-three target: **OPEN / NOT PROVED**;
- inherited `n_bal=14`: **UNCHANGED**;
- latest lead earliest-barrier state: **CONSUMED/APPLIED**;
- OTHER-account fleet01/B11 `085231Z` report and late note: **CONSUMED/APPLIED**;
- fleet01/B10 threshold-free heavy-bridge theorem: **CONSUMED/APPLIED**;
- prefix before globally earliest incomparable endpoint is a chain: **PROVED**;
- left-incomparable prefix is a terminal chain segment: **PROVED**;
- rightmost earliest pair is adjacent in the strong-majority order: **PROVED**;
- lower Hasse family at that pair is empty: **PROVED**;
- every first export is an outward heavy bridge: **PROVED**;
- span-exhausted exact return through that earliest barrier: **ELIMINATED**;
- partner's remaining low-endpoint multi-support Mode-T first-reuse state at the earliest barrier: **ELIMINATED**;
- closed post-barrier cycle wholly to the right: **OPEN**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No computation was required for the new arbitrary-size implications. Scoped provenance/privacy review used only the named private mathematical repositories and current control archive. No benchmark gold or sealed answers, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid/remote model/API/Codex execution, remote workflows, public posting, permission bypass, notification enabling, or benchmark/installation work was used or claimed.
