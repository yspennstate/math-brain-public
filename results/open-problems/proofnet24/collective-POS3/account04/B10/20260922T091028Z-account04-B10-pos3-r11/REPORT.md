# POS3 account04/B10 — the canonical earliest-ending pair cannot enter a span-exhausted heavy-bridge recycler

**Run:** `20260922T091028Z-account04-B10-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14`, unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and extension counts below are under the original uniform law on all full linear extensions of the original poset. No deletion-induced law is called uniform.

## 1. Exact collective state consumed

The latest complete campaign-lead report consumed is account04/B10 r18:

- `proofnet24/collective-POS3/account04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, report blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

It proves that every surviving four-channel outward export recreates a heavy Hasse bridge and that an opposite-ray two-step switch is exactly one of strict strong-majority span descent, strict envelope expansion, or literal exact backtrack through such a bridge.

The decisive named OTHER-account result consumed and applied is account01/B10 r13:

- `proofnet24/collective-POS3/account01/B10/20260922T084926Z-b10-pos3-r13/REPORT.md`, report blob `907ef9d19e23c05bc68a13c34ddb5a4aad6e30df`.

It removes the former `3/11` cutoff from the qualitative heavy-bridge analysis. If

`l lessdot r`, `m || l,r`, `l prec_* m prec_* r`,

and neither balance nor an authorized strict span descent has occurred, the positive canonical defect support purifies into exactly one of two modes:

- **Mode T:** `F2,F3` are the positive families and `F1,F4` are empty;
- **Mode F:** `F1,F4` are the positive families and `F2,F3` are empty.

Equivalently it constructs a heavy child with strictly smaller left strong-order rank: `(t,l,m)` in Mode T or `(c,m,r)` in Mode F.

I also consume account02/B10 r12,

- `proofnet24/collective-POS3/account02/B10/20260922T084851Z-b10-pos3-r12/REPORT.md`, report blob `0d6b6aaf49e848e27daf8bc78d672cb28ed58aa4`,

for the exact full-law transposition identity/Hasse-channel framework and the fact that exact backtracks have genuine noncentral external defects on both sides. The predecessor account01/B11 support theorem

- `proofnet24/collective-POS3/account01/B11/20260922T081324Z-b11-pos3-r11/REPORT.md`, report blob `369bdbc02461f4a6a1c8b67d026f159766b20443`,

supplies the canonical families and the same-ray exclusion: simultaneous positive `F1,F3` support gives balance or a strict right-ray subspan; the order-dual statement holds for `F2,F4`.

Finally I use account01/B10 r11, report blob `85fa62968e584b5db7fe6270260f55f92c071438`, for the proved fact that in a hypothetical no-balanced candidate the strong-majority relation `prec_*` is a strict total order. Write `rho(v)` for its rank.

## 2. Why a rank-only global splice is not enough

Before choosing the extremal pair below I tested the tempting purely rank-theoretic statement that fixed-ray moves plus strict envelope expansions at every ray switch are automatically acyclic. That statement is false even in the abstract transition model.

The committed standard-library checker `rank_switch_cycle_check.py` searches ordered-pair states `(i,j)`, with right moves `(i,j)->(j,k)`, left moves `(i,j)->(h,i)`, and, at direction changes, exactly the lead r18 no-descent/no-backtrack inequalities: after a right-then-left switch require `h<i`, and after a left-then-right switch require the new right endpoint to lie strictly beyond the old one.

Its exact output is:

```
n=3 cycle=False
n=4 cycle=False
n=5 cycle=False
n=6 cycle=True
((3, 4), (4, 5))
((4, 5), (2, 4))
((2, 4), (1, 2))
((1, 2), (0, 1))
((0, 1), (1, 3))
((1, 3), (3, 4))
((3, 4), (4, 5))
```

This is **not** a poset counterexample and is not evidence against POS3. It only refutes the stronger unsupported idea that the rank-switch normal form by itself supplies a global potential. The proof below therefore uses width-three Hasse support and an extremal actual incomparable pair rather than rank arithmetic alone.

## 3. Canonical earliest-ending pair

Assume for contradiction that `P` is a finite width-at-most-three nonchain with no balanced pair. By the consumed total-order theorem, `prec_*` is a strict total order.

Among all oriented incomparable pairs

`u || v`, `u prec_* v`,

choose `q` with `rho(q)` minimum. Among all `p || q` with `p prec_* q`, choose `p` with `rho(p)` minimum. Call `(p,q)` the **canonical earliest-ending pair**.

Define the standard Hasse witness families for `(p,q)`:

`U(p,q)={z : p lessdot z, z||q}`,

`D(p,q)={z : z lessdot q, z||p}`.

### Lemma 3.1 — the lower Hasse family is empty

`D(p,q)=emptyset`.

**Proof.** Suppose `z in D(p,q)`. Then `z<q` in the poset, hence `z prec_* q`. Also `p prec_* q` and `z||p`. Therefore whichever way the total order compares `z,p`, the incomparable pair `{z,p}` has both endpoints strictly before `q`. Its later endpoint has rank `<rho(q)`, contradicting the defining minimality of `q`. `square`

This is the first place where the global pair selection does real work: the canonical pair has no lower Hasse swap witness at all.

## 4. The first transposition export must enter a heavy bridge or already descend

Let `E=e(P)` and `M=N(p<q)`. Since `p prec_* q` and the pair is not balanced,

`M>2E/3`.

For the endpoint-position transposition of `p,q`, let `O,I` be the outgoing and incoming illegal-swap sets. The exact full-law identity consumed from account02/B10 is

`|O|-|I| = 2M-E > E/3`.                                      (4.1)

Thus `O` is nonempty. Every outgoing failure has a Hasse witness in `U(p,q) union D(p,q)`. Lemma 3.1 gives `D(p,q)=emptyset`, so some positive channel

`r in U(p,q)`

exists. Hence

`p lessdot r`, `r||q`.                                        (4.2)

If `r prec_* q`, then the poset relation `p<r` gives

`p prec_* r prec_* q`,

and `(r,q)` is a strict strong-majority subspan of `(p,q)`. This is exactly the already-authorized strict-span exit.

Therefore the only branch still needing analysis is

`p prec_* q prec_* r`.                                        (4.3)

Equations (4.2)-(4.3) make `(p,q,r)` a heavy Hasse bridge in the sense of account01/B10 r13: its endpoints satisfy `p lessdot r`, while the middle vertex `q` is incomparable with both.

## 5. New theorem: the extremal heavy bridge cannot be span-exhausted

For the heavy bridge `(p,q,r)` define the canonical families, in the account01/B11 notation,

`F1={z : p lessdot z, z||q, z!=r}`,

`F2={z : z lessdot q, z||p}`,

`F3={z : q lessdot z, z||r}`,

`F4={z : z lessdot r, z||q, z!=p}`.

Observe immediately from Lemma 3.1 that

`F2=emptyset`.                                                  (5.1)

### Theorem 5.1 — canonical earliest-ending pair forces a strict span descent

Starting from the canonical pair `(p,q)`, the first exact transposition/Hasse export cannot enter a span-exhausted heavy-bridge recycler. More precisely, under the no-balanced hypothesis, either

1. the first positive `U(p,q)` witness already gives the strict subspan `(r,q) proper_subset (p,q)`; or
2. it gives a heavy bridge `p lessdot r`, `p prec_*q prec_*r`, and that bridge necessarily exposes an authorized strict strong-majority span descent.

There is no third span-exhausted branch, at any endpoint probability scale and with any number of relation distinguishers.

**Proof.** The first alternative is Section 4. Assume the heavy branch (4.3) and, seeking a contradiction, assume that this bridge has neither balance nor any authorized strict span descent.

Because `p prec_* q prec_* r`, the two endpoint minority cells of the bridge are both `<E/3`. The threshold-free account01/B10 r13 inequalities therefore make both middle-cell bad-swap sets nonempty. The left bad-swap set is supported on `F1 union F2`; by (5.1), some `F1` channel is positive.

The right bad-swap set is supported on `F3 union F4`, so at least one of those families is positive.

If `F3` has positive support, then positive `F1` and positive `F3` occur simultaneously. The account01/B11 same-right-ray theorem applies: their boundary recodings are two actual incomparable pairs on the same right strong-order ray. In a no-balanced candidate those two blockers are strictly ordered, and the nearer pair is a strict strong-majority subspan of the farther pair. This is the forbidden authorized descent. Hence, under our assumed no-descent branch,

`F3^+=emptyset`.                                                (5.2)

Right-side positivity now forces `F4^+ != emptyset`. Choose `c in F4^+`. Then

`c lessdot r`, `c||q`, `c!=p`.                                 (5.3)

Compare `c` with `q` in the total order.

- If `q prec_* c`, then (5.3) and the poset relation `c<r` give
  `q prec_* c prec_* r`, so `(q,c)` is a strict subspan of `(q,r)`, again forbidden.
- Hence `c prec_* q`. Compare `c` with `p`.
  - If `p prec_* c prec_* q`, then `(c,q)` is a strict subspan of `(p,q)`, forbidden.
  - If `c prec_* p`, then `(c,q)` is an incomparable pair ending at the same canonical endpoint `q` but with `rho(c)<rho(p)`, contradicting the defining leftmost choice of `p`.
  - Equality `c=p` is excluded in (5.3).

Every possibility contradicts the assumed no-descent/no-balance branch. Thus the heavy bridge cannot be span-exhausted. `square`

### Corollary 5.2 — no support-size or `3/11` exception at the first pair

The conclusion of Theorem 5.1 is independent of the low-endpoint cutoff used in earlier lead runs. In particular the first canonical pair cannot escape through a high-endpoint `[3/11,1/3)` exception, an exact-backtrack exception, or a genuinely multi-distinguisher heavy bridge **without first exposing strict span descent**.

The reason is structural: `F2` is globally forbidden by earliest-endpoint minimality, while a surviving `F4` would either itself descend or violate the leftmost choice of `p`.

## 6. First-return barrier

The same extremal choice gives one further splice fact.

### Lemma 6.1 — any nontrivial return to the earliest endpoint is already a descent

Let `(s,q)` be any oriented incomparable pair with right endpoint `q`.

- `s prec_* p` is impossible by the choice of `p`;
- `p prec_* s prec_* q` makes `(s,q)` a strict subspan of `(p,q)`;
- `s=p` is the literal original state.

And no incomparable pair can have right endpoint strictly before `q` by definition of `q`.

Consequently, after the canonical state is left, the first re-entry into the strong-order prefix ending at `q` can only be either an already-authorized strict descent or the literal state `(p,q)` itself. If the immediate predecessor of a literal return is `(q,r)`, that predecessor is exactly a heavy bridge `p lessdot r`, `q||p,r`; Theorem 5.1 says the proof may take a strict-span exit there instead of accepting a neutral span-exhausted return.

This does not yet rule out all later global recycling, but it turns the old generic backtrack obstruction into a one-way earliest-endpoint barrier plus a specific right-side descent problem.

## 7. What remains

The new first unpaid implication is:

> **`POS3-EARLIEST-BARRIER-DESCENT-SPLICE-v1`.** Starting with the canonical earliest-ending pair `(p,q)`, take the strict span descent forced by Theorem 5.1. Prove that subsequent Hasse-export/bridge reductions can be continued with a globally well-founded statistic before any exact return to `(p,q)`, or else produce a balanced pair or a valid proper autonomous/ordinal reduction. In particular, the forced right-side same-ray descent arising from simultaneous `F1/F3` support must not be able to migrate to the right and later reset the proof to the original earliest barrier without paying one of those terminal outcomes.

This is strictly narrower than the lead r18 generic cross-envelope/backtrack residual and than account01/B10 r13's generic `SPAN-DESCENT-SPLICE`: at the first global incomparable endpoint, the lower Hasse family is empty and every nontrivial return to that endpoint is already a strict descent.

I do **not** claim the remaining splice here. POS3 remains open.

## 8. Exact computation used only to reject a false stronger route

Supporting files in this immutable run directory:

- `rank_switch_cycle_check.py` — deterministic standard-library abstract transition checker;
- `rank_switch_cycle_output.txt` — exact output reproduced in Section 2.

These files are used only to reject the stronger rank-only acyclicity lemma. They are not a finite POS3 certificate and not a counterexample to the target.

## 9. Status and integrity

- lead account04/B10 r18: **CONSUMED/APPLIED**;
- OTHER-account account01/B10 r13 threshold-free heavy-child theorem: **CONSUMED/APPLIED**;
- OTHER-account account02/B10 r12 full-law transposition/Hasse leakage: **CONSUMED/APPLIED**;
- account01/B11 canonical support/same-ray exclusion: **CONSUMED/APPLIED**;
- abstract rank-only global-potential shortcut: **REFUTED as a stronger auxiliary claim**;
- `D(p,q)=emptyset` for the canonical earliest-ending pair: **PROVED**;
- first transposition export is `U`-only: **PROVED**;
- canonical first heavy bridge cannot be span-exhausted: **PROVED, arbitrary finite size**;
- every nontrivial return to the earliest endpoint is descent/impossible: **PROVED**;
- global earliest-barrier descent splice: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- inherited `n_bal=14`: **UNCHANGED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

Scoped provenance/privacy review: only the named private mathematical repositories, source-bound peer reports, sanitized logical run labels, exact mathematical formulas and deterministic standard-library checker were used. No benchmark gold or sealed answers, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid model/API/Codex execution, remote workflows, permission bypass, public posting, notification enabling, or production-brain mutation was used or claimed.
