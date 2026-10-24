# POS3 account01/B11 — disjoint Mode-T support cannot exact-backtrack; purified low-endpoint backtracks funnel into the multi-distinguisher branch

**Run:** `20260922T085231Z-b11-pos3-auto11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and counts below are for the original uniform law on all full linear extensions of the original poset. No projected or deletion-induced law is called uniform.

## 1. Exact collective state consumed

The latest complete campaign-lead report consumed is account04/B10 r18:

- `proofnet24/collective-POS3/account04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

R18 proves that every surviving four-channel outward export recreates a heavy Hasse bridge and that every opposite-ray two-step switch has only three local outcomes: strict strong-majority span descent, strict strong-majority envelope expansion, or literal exact backtrack through the heavy bridge. In the low-endpoint branch, writing

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`,

`A=#{a<x<y}`, `H=#{x<a<y}`, `C=#{x<y<a}`, `E=A+H+C`,

one has `A,C<3E/11` and hence `H>5E/11`.

The immediate account01/B11 predecessor is run `20260922T081324Z-b11-pos3-r11`, blob `369bdbc02461f4a6a1c8b67d026f159766b20443`. It proves that, after balance and strict span descent are excluded, the entire positive canonical defect support purifies into exactly one of two modes:

- **Mode T (through-a):** only `F2/F3` are active;
- **Mode F (fork-fork):** only `F1/F4` are active.

In Mode T the selected side packets have minority mass `>E/11`; in Mode F the unique `F1` and `F4` packets each carry the full side defect `>2E/11`.

The assigned OTHER-account partner consumed and applied is account02/B19 r11:

- `proofnet24/collective-POS3/account02/B19/20260922T071111Z-account02-B19-pos3-r11/REPORT.md`, main blob `3dda5f9df837b64f7cf7fc6103eb353284ca60dd`.

Its exact eight-vertex width-three core has `108` full linear extensions, heavy state `(x lessdot y;a)=(2 lessdot 0;5)`, selected `F2` blocker `6` and selected `F3` blocker `7`, and the balanced child/frontier pair `Pr(4<5)=47/108`. Section 7 below identifies this witness exactly as the shared-support double-fork branch.

Two further source-exact dependencies are used.

1. account03/B11 r11d, `proofnet24/collective-POS3/account03/B11/20260922T081117Z-account03-B11-pos3-r11d/REPORT.md`, blob `56374ff9d4b1bf188929919d05e52b34c00868b6`: for an incomparable pair whose only two distinguishers are comparable positive upper distinguishers `p<u<v`, it proves the exact full-extension identity `N(q<u)=2N(q<p)`, with the order-dual lower-chain identity. It also proves that a shared external support in the live fully-crossed bridge is either impossible when comparable with the central witness or becomes a central double Hasse fork with at least two fresh outside distinguishers.
2. account04/B19 r46, `proofnet24/collective-POS3/account04/B19/B19-20260922T071535Z-r46/REPORT.md`, blob `26c2eab1c40a8da73357764efd0aab4160391e07`: every selected high `F1` or `F4` witness carrying `>2E/33` marks forces a charged unequal-neighborhood/multi-distinguisher exit, so it cannot remain a recycling state.

For the one-distinguisher step below I use account02/B10 r13, `proofnet24/collective-POS3/account02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`, blob `e91498f0bb8e28f23aa1cada24e131c27182e0ff`: an incomparable pair with exactly one relation distinguisher is balanced.

## 2. Compact conditional route and the new target

Assume for contradiction a span-descent-exhausted width-three no-balanced candidate. Lead r18 says a local ray switch is descent, envelope expansion, or exact backtrack. The previous account01/B11 support-purification theorem says every low-endpoint exact backtrack is Mode T or Mode F.

Mode F is already forced out of the local recycler by account04/B19 r46 because its unique active `F1` and `F4` packets have mass `>2E/11>2E/33`.

Thus the only possible low-endpoint exact-backtrack recycler is Mode T. Account03/B11 reduces its minimum-support form to the fully-crossed bridge

`l lessdot a lessdot r`, `x lessdot y`,
`l<y`, `x<r`,
`l||x`, `a||x,y`, `r||y`,
`l prec_* x prec_* a prec_* y prec_* r`.                        (2.1)

If either charged side already has at least three distinguishers, we are already in the multi-distinguisher exit branch. If each charged side has exactly two distinguishers, write

`D(l,x)={a,z_L}`, `D(y,r)={a,z_R}`,                              (2.2)

where `z_L,z_R` are positive external supports. account03/B11 r11d pays the case `z_L=z_R` up to a central double-fork multi-distinguisher exit. The new mathematics below pays the remaining **disjoint-support** case `z_L!=z_R`: it cannot be a literal exact backtrack unless a genuinely fresh distinguisher is created.

## 3. Hasse localization of a rigid external support

For the orientation `l<x`, a positive support `z_L` has one of two types:

- **L-:** `z_L<x` and `z_L||l` (positive lower support);
- **L+:** `l<z_L` and `z_L||x` (positive upper support).

For the orientation `y<r`, a positive support `z_R` has one of two types:

- **R-:** `z_R<r` and `z_R||y`;
- **R+:** `y<z_R` and `z_R||r`.

### Lemma 3.1 — every rigid support is a Hasse attachment

Under (2.2),

- L- implies `z_L lessdot x`;
- L+ implies `l lessdot z_L`;
- R- implies `z_R lessdot r`;
- R+ implies `y lessdot z_R`.

**Proof.** Suppose L- and `z_L<w<x`. If `w<l`, then `z_L<w<l`, contradicting `z_L||l`; if `l<w`, then `l<w<x`, contradicting `l||x`. Hence `w||l`, so `w` would be a third distinguisher of `l,x`, contradicting (2.2). The L+ case is similar: if `l<w<z_L`, then neither `w<x` nor `x<w` is possible, so `w||x`, again a third distinguisher. The two right-side statements are the order-duals. `square`

This is useful because the external supports are not amorphous relation witnesses: in the rigid branch they are actual sibling Hasse channels.

## 4. Exact factor-two exchange forbids inward comparability with `a`

### Lemma 4.1 — an L+ support is incomparable with `a`

If `z_L` is L+, then `z_L||a`.

**Proof.** Since `l lessdot a` and `l<z_L`, the relation `z_L<a` is impossible: it would put `z_L` strictly between `l` and `a`.

If instead `a<z_L`, then the only two distinguishers of `l||x` are the comparable positive upper chain

`l<a<z_L`, `x||a,z_L`.

Apply account03/B11 r11d's exact factor-two exchange identity with `(p,q,u,v)=(l,x,a,z_L)`:

`N(x<a)=2N(x<l)`.                                                (4.1)

The live strong-majority order `l prec_* x` gives `N(x<l)<E/3`, so (4.1) gives `N(x<a)<2E/3`, contradicting `x prec_* a`, which requires `N(x<a)>2E/3`. Thus neither comparability is possible. `square`

### Lemma 4.2 — an R- support is incomparable with `a`

If `z_R` is R-, then `z_R||a`.

**Proof.** The relation `a<z_R<r` contradicts `a lessdot r`. If `z_R<a`, then the only two distinguishers of `y||r` form the comparable positive lower chain

`z_R<a<r`, `y||z_R,a`.

The lower-chain dual of (4.1) gives

`N(a<y)=2N(r<y)`.                                                (4.2)

Since `y prec_* r`, the right side is `<2E/3`, contradicting `a prec_* y`. `square`

These are exact full-extension statements: the factor `2` comes from a deletion-fiber label exchange, not from a projected uniformity assumption.

## 5. Span-exhaustion localizes the support in the strong order

### Lemma 5.1

In the span-descent-exhausted branch:

- L- implies `z_L prec_* l`;
- L+ implies `a prec_* z_L`;
- R- implies `z_R prec_* a`;
- R+ implies `r prec_* z_R`.

**Proof.** For L-, the poset relation `z_L<x` gives `z_L prec_* x`. If `l prec_* z_L prec_* x`, the incomparable pair `(l,z_L)` is a strict strong-order subspan of `(l,x)`, contrary to span exhaustion. Hence `z_L prec_* l`.

For L+, `l<z_L` gives `l prec_* z_L`, while `z_L||x` and `l prec_* x` exclude `l prec_* z_L prec_* x` by the same subspan argument. Thus `x prec_* z_L`. Lemma 4.1 gives `z_L||a`; if `x prec_* z_L prec_* a`, `(x,z_L)` is a strict subspan of `(x,a)`. Hence `a prec_* z_L`.

The right-side statements are the exact order-duals. `square`

Thus L- and R+ are automatically strict outward envelope channels. Only the simultaneous inward type `(L+,R-)` needs further work.

## 6. New disjoint-support escape theorem

### Theorem 6.1 — disjoint rigid Mode-T support cannot be an exact local backtrack

Assume (2.1)-(2.2), `z_L!=z_R`, no balanced pair, and no strict strong-majority span descent. Then at least one of the following occurs:

1. one of the central incomparable pairs `(a,z_L)` or `(a,z_R)` has a relation distinguisher outside the seven-point set `{l,x,a,y,r,z_L,z_R}`; this is a genuinely fresh multi-distinguisher exit; or
2. the active strong-order envelope expands strictly on at least one side. In the only nontrivial simultaneous inward type `(L+,R-)`, it expands on **both** sides:

`z_R prec_* l prec_* x prec_* a prec_* y prec_* r prec_* z_L`.  (6.1)

In particular, a rigid disjoint-support Mode-T state cannot realize the literal exact-backtrack alternative of lead r18 without creating a fresh distinguisher.

### Proof

If `z_L` is L-, Lemma 5.1 gives `z_L prec_* l`, a strict left expansion. If `z_R` is R+, Lemma 5.1 gives `r prec_* z_R`, a strict right expansion. Therefore the only case in which expansion is not already immediate is

`z_L` of type L+ and `z_R` of type R-.                          (6.2)

By Lemmas 4.1-5.1,

`z_R prec_* a prec_* z_L`, `z_L||a`, `z_R||a`.                 (6.3)

Now inspect the central pair `a||z_L`. Because `z_L` is not a distinguisher of `y,r`, its relation to `y` and `r` is the same. Since `z_L||x` and `x<y`, `z_L` cannot lie above both. Thus exactly one of the following holds:

- `z_L<y,r`; then among the original five bridge vertices, `y` distinguishes `a,z_L` while `l,x,r` do not;
- `z_L||y,r`; then `r` distinguishes `a,z_L` while `l,x,y` do not.

So, apart from `z_R`, the pair `a,z_L` has exactly one distinguisher inside the seven-point core. Dually, apart from `z_L`, the pair `a,z_R` has exactly one distinguisher inside the core.

If an outside vertex distinguishes either central pair, alternative 1 holds. Assume therefore that no outside vertex does. By the one-distinguisher balance theorem, neither `a||z_L` nor `a||z_R` may have only its single bridge distinguisher. Consequently `z_R` must distinguish `a,z_L` and `z_L` must distinguish `a,z_R`. Since both supports are incomparable with `a`, this is equivalent to

`z_L` and `z_R` being comparable.                               (6.4)

The direction `z_L<z_R` is impossible: deterministic poset order would give `z_L prec_* z_R`, contradicting (6.3). Hence

`z_R<z_L`.                                                       (6.5)

Equation (6.5) forces the **outer** relation pattern. If `z_L<y`, then `z_R<z_L<y`, contradicting `z_R||y`; hence

`z_L||y,r`.                                                      (6.6)

If `x<z_R`, then `x<z_R<z_L`, contradicting `z_L||x`; hence

`z_R||l,x`.                                                      (6.7)

Now combine (6.3), (6.6) and the old order `a prec_* y prec_* r`. If `z_L` lay strictly between `a` and `y`, the pair `(z_L,y)` would be a strict subspan of `(a,y)`; if it lay strictly between `y` and `r`, `(z_L,r)` would be a strict subspan of `(y,r)`. Span exhaustion therefore forces

`r prec_* z_L`.                                                 (6.8)

Dually, (6.3), (6.7) and `l prec_* x prec_* a` force

`z_R prec_* l`.                                                 (6.9)

Together (6.8)-(6.9) give (6.1). `square`

The theorem is a direct exchange/injection application: the exact factor-two noninjective-fiber accounting rules out the only inward comparable supports, and the one-distinguisher fiber theorem forces the two disjoint supports either to interact or to emit fresh support. Their interaction is then incompatible with a neutral backtrack and becomes strict envelope expansion.

## 7. Direct application of the assigned account02/B19 witness

The account02/B19 108-extension core calibrates the **shared-support**, not the disjoint-support, branch.

For the selected Mode-T bridge

`l=6`, `x=2`, `a=5`, `y=0`, `r=7`,

an independent exact reconstruction gives

`D(6,2)={4,5}`, `D(0,7)={4,5}`.                                (7.1)

Thus the two charged sides share the same external support `z=4`. Moreover

`6<4,5<7`, `4||5`,                                             (7.2)

so this is exactly account03/B11 r11d's central double-Hasse-fork outcome. The central pair is indeed balanced:

`Pr(4<5)=47/108`.                                               (7.3)

The committed standard-library verifier reconstructs all `108` extensions and checks (7.1)-(7.3), ending with

`POS3_PARTNER_SHARED_SUPPORT_CHECK_PASS`.

Verifier SHA-256: `cc473f02fc0b81388c176e4023d2b96308a4f5425d8992f7ecd5ac95d8829446`.  
Captured-output SHA-256: `c07f53ea50a72449eb6819a3dfc27798dec8c578152c4c895cf312b225fb437b`.

This is a genuine application of the assigned partner: its formerly awkward opposite-ray frontier is now identified exactly with the shared-support double-fork escape, and its observed balanced pair is the central fork pair predicted by that structural funnel.

## 8. Mode F is also not a low-endpoint recycler

The previous account01/B11 purification leaves a second support mode, Mode F, with unique active blockers

`b in F1`, `c in F4`,

and full side-defect packet weights

`lambda_b>2E/11`, `rho_c>2E/11`.                                (8.1)

Since `2/11>2/33`, account04/B19 r46 Theorems 4.1 and 5.1 apply separately to (8.1): every such high `F1` or `F4` channel forces a charged unequal-predecessor/successor, hence multi-distinguisher, exit. Therefore Mode F cannot remain a local exact-backtrack recycler either.

This consumes r46 at precisely the point where its charged sibling-fork theorem is strongest; no new numerical threshold is being asserted.

## 9. Consequence for the lead's r18 residual

Combine Sections 6-8 with the previous support purification.

A low-endpoint exact-backtrack bridge has only two purified modes.

- **Mode F:** immediately exits to the charged multi-distinguisher branch by account04/B19 r46.
- **Mode T:** if a charged side has at least three distinguishers, it is already in that branch. If both sides have exactly two distinguishers, shared support is paid by account03/B11 r11d; disjoint support is paid by Theorem 6.1 through fresh support or strict envelope expansion.

Hence there is **no remaining rigid low-support literal exact backtrack**. Every such would-be return either strictly enlarges the strong-order envelope or enters a genuinely multi-distinguisher state.

This materially narrows lead r18's `POS3-CROSS-ENVELOPE-BACKTRACK-EXIT-v1`. Strict envelope expansions are finite unless some later state removes the accumulated envelope. After the present reduction, any such removal must pass through the multi-distinguisher branch.

The new first essential missing implication is therefore:

> **`POS3-MULTI-DISTINGUISHER-BACKTRACK-CHARGE-v1`.** In a span-descent-exhausted no-balanced width-three candidate, start from a charged multi-distinguisher exit produced by a purified low-endpoint heavy bridge. Prove that this branch cannot erase a previously gained strong-order envelope and return to an earlier heavy state without forcing a balanced pair, strict span descent, a proper autonomous/ordinal reduction, or a new charged state whose envelope/potential is strictly larger. The proof must retain full extension multiplicities and cannot collapse the extra distinguishers into a scalar projected-law error.

That is now the first place where a global recycler can still hide. POS3 itself remains open.

## 10. Status and integrity

- latest lead account04/B10 r18: **CONSUMED/APPLIED**;
- immediate account01/B11 support purification: **CONSUMED/APPLIED**;
- assigned partner account02/B19 r11: **CONSUMED/APPLIED**, exact 108-extension shared-support identification verified;
- account03/B11 r11d factor-two exchange/shared-support theorem: **CONSUMED/APPLIED**;
- account04/B19 r46 high-F1/F4 charged exit: **CONSUMED/APPLIED**;
- rigid external supports are Hasse attachments: **PROVED**;
- inward comparable support is ruled out by exact factor-two exchange: **PROVED**;
- disjoint rigid Mode-T exact backtrack: **ELIMINATED modulo fresh multi-distinguisher exit or strict envelope expansion**;
- purified Mode-F local recycling: **ELIMINATED into charged multi-distinguisher exit**;
- generic multi-distinguisher backtrack/charge transport: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- classification: **`ESSENTIAL_STEP_APPLIED`**.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, public posting, permission change, or cross-account authentication was used. The repository is only the authorized private coordination/scientific archive; no native-brain ingestion is claimed.
