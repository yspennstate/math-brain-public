# POS3 fleet04/B19 — one-sided same-cover span resets admit an exact lexicographic potential

**Run:** `B19-20260922T091459Z-r46`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities inherited below are for the original uniform law on full linear extensions. No deletion-induced law is substituted for it.

## 1. Source-bound state consumed

The latest complete campaign-lead report used is

- **fleet04/B10 r18**, `proofnet24/collective-POS3/fleet04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, Git blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

Its surviving normal form is a heavy Hasse bridge

`ell lessdot r`, `m || ell,r`, `ell prec_* m prec_* r`,

and every two-step opposite-ray switch is either strict strong-majority span descent, strict envelope expansion, or an exact backtrack. The bridge has an exact three-cell decomposition and middle mass `>E/3`.

The required named OTHER-account partner result applied here is the newest complete **fleet01/B10 r13**,

- `proofnet24/collective-POS3/fleet01/B10/20260922T084926Z-b10-pos3-r13/REPORT.md`, Git blob `907ef9d19e23c05bc68a13c34ddb5a4aad6e30df`.

It proves the threshold-free heavy-child theorem. If a heavy bridge has neither balance nor an authorized strict span-descent exit, then it has a heavy child with strictly smaller left strong-order rank. More precisely, with `rho` the rank in the strict strong-majority order:

- Mode T gives `(t,ell,m)` with `rho(m)<rho(r)`;
- Mode F gives `(c,m,r)` with `rho(c)<rho(ell)`.

Thus the partner eliminates closed recycling while the process stays in the span-exhausted heavy-bridge class, but leaves `POS3-SPAN-DESCENT-SPLICE-v1`: a strict span descent could reset the bridge geometry and apparently undo the left-rank progress.

I also use the preceding B19 exact-backtrack bypass,

- `proofnet24/collective-POS3/fleet04/B19/B19-20260922T081503Z-r11/ADDENDUM_GLOBAL_OUTSIDE_BACKTRACK_BYPASS.md`, Git blob `b56486c3c1fcace42c685686ab4897a797758611`,

only as continuity: low-endpoint literal exact backtracks already have a noncentral outside-envelope bypass. The argument below does not assume that all cover-changing reuse is solved.

## 2. First uncovered splice case

A strict span descent can occur on either adjacent incomparable boundary of a heavy bridge:

- the right boundary `(m,r)`, producing an incomparable pair `(u,r)` with
  `m prec_* u prec_* r`; or
- the left boundary `(ell,m)`, producing `(ell,u)` with
  `ell prec_* u prec_* m`.

The first genuinely uncovered reset is when the descended pair subsequently re-enters the **same Hasse cover** `ell lessdot r`. At first sight this can undo the partner's left-rank descent, because the cover endpoints may return unchanged.

The observation below pays this case exactly: a same-cover right reset strictly raises the bridge middle rank, while a same-cover left reset strictly lowers it. Combining that third coordinate with the partner's endpoint descent gives a well-founded lexicographic potential for every one-sided same-cover episode.

## 3. Same-cover re-entry lemma

### Theorem 3.1 — right-boundary re-entry moves the middle strictly right

Let

`B=(ell,m,r)`

be a heavy bridge:

`ell lessdot r`, `m||ell,r`, `ell prec_* m prec_* r`.

Suppose a strict span-descent step on the right boundary `(m,r)` chooses an incomparable pair `(u,r)` with

`m prec_* u prec_* r`.                                      (3.1)

Assume that the continuation from `(u,r)` re-enters a heavy bridge using the **same** Hasse cover `ell lessdot r`. Then necessarily

`u||ell`,

and the re-entered bridge is exactly

`B'=(ell,u,r)`.                                               (3.2)

In particular

`rho(u)>rho(m)`.                                              (3.3)

**Proof.** Re-entry through the same cover means its cover endpoints are again `ell,r`. A heavy bridge with those endpoints has a middle vertex incomparable with both. Since the active descended pair already contains the right endpoint `r`, the only same-cover re-entry whose middle is the descended active vertex is `(ell,u,r)`; its validity is exactly `u||ell` in addition to the inherited `u||r`. The strict span condition (3.1) gives (3.3). `square`

No probability approximation is involved: the new bridge is heavy automatically because `ell prec_* u prec_* r` and no-balancedness makes both endpoint minority cells `<1/3`, so the middle cell is `>1/3` by the exact three-position partition for the forced cover `ell<r`.

### Theorem 3.2 — left-boundary re-entry moves the middle strictly left

Dually, if a strict span descent from `(ell,m)` gives `(ell,u)` with

`ell prec_* u prec_* m`,                                     (3.4)

and the continuation re-enters the same cover `ell lessdot r`, then the re-entered heavy bridge is

`B'=(ell,u,r)`,                                               (3.5)

and

`rho(u)<rho(m)`.                                              (3.6)

The proof is the order-dual argument. `square`

## 4. Exact lexicographic splice potentials

For a heavy bridge `B=(ell,m,r)`, define two integer triples, ordered lexicographically:

`Phi_R(B) = ( rho(r), rho(ell), -rho(m) )`,                   (4.1)

`Phi_L(B) = ( rho(r), rho(ell),  rho(m) )`.                   (4.2)

### Theorem 4.1 — right-sided same-cover episodes are well founded

Along either of the following transitions, `Phi_R` strictly decreases:

1. any partner-r13 heavy-child transition from a span-exhausted bridge;
2. any right-boundary strict span descent followed by same-cover re-entry as in Theorem 3.1.

**Proof.** For a partner heavy child:

- Mode T replaces `(ell,m,r)` by `(t,ell,m)`, so its first coordinate drops from `rho(r)` to `rho(m)`;
- Mode F replaces it by `(c,m,r)`, so the first coordinate is unchanged and the second drops from `rho(ell)` to `rho(c)`.

For a right-boundary same-cover re-entry, the first two coordinates are unchanged and Theorem 3.1 raises `rho(m)`, hence strictly lowers `-rho(m)`. `square`

Because the poset is finite, `Phi_R` takes values in a finite set. Therefore no directed cycle can be made solely from partner heavy-child transitions and right-boundary same-cover span-reset transitions.

### Theorem 4.2 — left-sided same-cover episodes are well founded

The same statement holds with `Phi_L`: partner heavy-child transitions strictly decrease the first or second coordinate exactly as above, while a left-boundary same-cover re-entry strictly lowers `rho(m)`, hence the third coordinate of `Phi_L`.

Thus no directed cycle can be made solely from partner heavy-child transitions and left-boundary same-cover resets. `square`

## 5. Consequence for the partner's span-descent splice

The partner's remaining `POS3-SPAN-DESCENT-SPLICE-v1` is therefore not a generic reset problem anymore.

A recycler that defeats the heavy-child theorem must now do at least one of the following:

1. **change the Hasse cover** when it re-enters after span descent; or
2. **alternate splice sides** on the same cover, so that neither single potential `Phi_R` nor `Phi_L` governs the whole episode.

In particular, a span descent cannot repeatedly reset the same cover from only one adjacent side. The apparent possibility

`heavy-child progress -> right span descent -> same-cover reset -> heavy-child progress -> right span descent -> ...`

is eliminated by `Phi_R`, and its left-handed dual is eliminated by `Phi_L`.

This is an arbitrary-size statement. It does not use a finite census, a bounded-`n` frontier, or a threshold on the endpoint minorities beyond the no-balanced heavy-bridge hypotheses already present in the lead/partner normal form.

There is also a bounded local cover-choice fact useful for the next branch: for fixed `r`, all distinct lower covers of `r` form an antichain, so width at most three gives at most three possible left endpoints of a same-right Hasse-cover re-entry. Dually, a fixed left endpoint has at most three upper covers. This does not itself close alternating or cover-changing reuse, but it makes the next state space genuinely typed rather than arbitrary.

## 6. Compact conditional end-to-end route after this run

Assume a hypothetical width-at-most-three counterexample with no balanced pair.

1. The lead reduces surviving ray switches to heavy bridges, strict span descent, strict envelope expansion, or exact backtrack.
2. The previous B19 addendum bypasses the low-endpoint literal exact-backtrack edge through noncentral outside-envelope leakage.
3. The named partner fleet01/B10 r13 gives a heavy child whenever a heavy bridge is span-exhausted, lowering its left rank (and never raising the right endpoint rank).
4. Theorems 3.1-4.2 above show that a strict span descent followed by re-entry through the same cover cannot erase that progress indefinitely if the reset keeps using one boundary side: `Phi_R` or `Phi_L` strictly decreases.
5. Therefore the first still-unpaid splice is now a **cover-changing reset or an alternating-side same-cover bounce**.

The next essential implication is:

> **`POS3-ALTERNATING/COVER-SWITCH-SPLICE-v1`.** In a no-balanced width-three candidate, show that the first cover-changing re-entry or the first change of reset side cannot return to a previously exposed heavy-bridge state without producing a balanced pair, strict smaller span, proper autonomous/ordinal reduction, or a charged outside-envelope exit already controlled by the fixed-ray machinery.

The parent POS3 theorem remains open. No full-proof promotion is made.

## 7. Status and integrity

- latest lead fleet04/B10 r18: **CONSUMED/APPLIED**;
- required OTHER-account partner fleet01/B10 r13: **CONSUMED/APPLIED**;
- partner heavy-child transition effect on endpoint ranks: **USED EXACTLY**;
- right same-cover span-reset moves middle rank strictly right: **PROVED**;
- left same-cover span-reset moves middle rank strictly left: **PROVED**;
- `Phi_R` well-foundedness for right-only same-cover splice episodes: **PROVED**;
- `Phi_L` well-foundedness for left-only same-cover splice episodes: **PROVED**;
- one-sided same-cover span-reset recycler: **ELIMINATED**;
- alternating-side / cover-changing splice: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No computation was used for the new implication; there is no code/output artifact for this run. A scoped manual privacy/provenance review found only mathematical statements, logical run labels, repository-relative source references, and nonsecret Git object identifiers. No credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, benchmark gold, email/Drive data, paid/remote compute, workflow dispatch, permission change, or public release action was used.
