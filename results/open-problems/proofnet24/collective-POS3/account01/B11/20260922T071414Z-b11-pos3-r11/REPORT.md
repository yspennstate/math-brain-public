# POS3 account01/B11 — coherent three-antichain gates force a near-band endpoint or a non-return frontier packet

**Run:** `20260922T071414Z-b11-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all full linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are for the original uniform law on all full linear extensions. No deletion-induced distribution is treated as uniform.

## 1. Exact collective state consumed

The latest complete campaign-lead result used in the final derivation is:

- account04/B10 r17, `proofnet24/collective-POS3/account04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, Git blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

R17 starts from a low-endpoint heavy cover

`x lessdot y`, `a||x,y`, `x prec_* a prec_* y`,

with

`A=#{a<x<y}`, `H=#{x<a<y}`, `C=#{x<y<a}`, `E=A+H+C`,

and

`A<3E/11`, `C<3E/11`.

Its canonical Hasse families are

`F1={r:x lessdot r, r||a, r!=y}`,
`F2={r:r lessdot a, r||x}`,
`F3={r:a lessdot r, r||y}`,
`F4={r:r lessdot y, r||a, r!=x}`.

The left-swap bad family uses `F1 union F2`, the right-swap bad family uses `F3 union F4`. Under the inherited no-span hypotheses, `F2 union F4` lies strictly before `x` in the strong-majority order and `F1 union F3` lies strictly after `y`. R16/r17 supply one selected canonical witness on each swap side, each carrying strictly more than `2E/33` marked full extensions.

R17 pays the comparable same-ray case by a strict pair-minority strip and pays the anti-aligned incomparable same-ray case by an anchor-free `>2/33` blocker pair. Its first unpaid same-ray state is the **coherent width-saturating three-antichain gate**:

- right gate: selected `b in F1`, `c in F3`, `b||c`, and `y prec_* b prec_* c`, with `{y,b,c}` a 3-antichain;
- left gate: selected `b in F2`, `c in F4`, `b||c`, and `b prec_* c prec_* x`, with `{b,c,x}` a 3-antichain.

The required named OTHER-account result consumed and applied is:

- account02/B19, `proofnet24/collective-POS3/account02/B19/20260922T064049Z-account02-B19-pos3-06d9849e/REPORT.md`, Git blob `762258edb3b6081ee9b816a5a98eba48157a7862`, together with `ADDENDUM_LEAD_R16.md`, blob `9589fc10d5331e2578194b6766e8bbdb8f603a1e`.

B19 proves a reciprocal cover-pivot mechanism for canonical `F2/T_L` and `F3/U_R` transitions and gives an exact connected autonomous-prime 515-extension width-three example with a genuine positive-weight two-cycle. Its addendum correctly notes that the cycle lies outside the strict two-endpoint `<3/11` regime and that a valid proof must use the complete frontier, not a single greedy channel.

The argument below extends that reciprocity bookkeeping to all four canonical Hasse types and then applies it to R17's coherent gate.

## 2. Compact conditional end-to-end route

Assume a cardinality-minimal no-balanced width-three candidate and the inherited transitive strong-majority order. In the lead's strict low-endpoint branch, R17 reduces same-ray recycling to the coherent gate above.

For any canonical blocker `r`, pivot on its Hasse edge to form the natural next heavy state. Exactly one old endpoint minority survives unchanged; the second new endpoint minority is an actual pair event containing every canonical mark assigned to `r`. Therefore a selected `>2E/33` blocker transition has a sharp dichotomy:

1. its new endpoint minority is at least `3E/11`, giving an actual pair in the narrow near-balance band `[3/11,1/3)`; or
2. the new state is again strict low-endpoint, so the lead's two-packet theorem applies again.

In a coherent gate, choose the Hasse transition whose structural return is on one swap side. If case 2 occurs, the lead theorem simultaneously produces a selected packet on the *other* swap side. That opposite-side packet cannot be the return vertex and its blocker lies strictly beyond one endpoint of the transitioned strong-order interval. Thus the coherent gate cannot consume the entire certified mass in the reciprocal return.

This directly pays R17's local **COHERENT-GATE EXIT** obligation. It does not yet prove POS3: the remaining global problem is to close the `[3/11,1/3)` near-band and to show that successive genuine frontier expansions cannot recycle through a longer mixed sequence.

## 3. Four-type heavy-transition bookkeeping

Let `w(r)` be the number of canonical marked full extensions assigned to a positive blocker `r`. Define the transition minority count `M(r)` as follows.

| old type | Hasse transition state | transition minority `M(r)` | structural return in new state |
|---|---|---|---|
| `F1` | `(x lessdot r; pivot a)` | `#{r<a}` | old `y` is new `F1` |
| `F2` | `(r lessdot a; pivot x)` | `#{x<r}` | old `y` is new `F3` |
| `F3` | `(a lessdot r; pivot y)` | `#{r<y}` | old `x` is new `F2` |
| `F4` | `(r lessdot y; pivot a)` | `#{a<r}` | old `x` is new `F4` |

### Lemma 3.1 — exact endpoint inheritance

For every row in the table:

1. the displayed transition is a legitimate heavy-cover state whenever the blocker has the inherited outward strong-majority polarity;
2. one new endpoint minority is exactly one old endpoint count (`A` for `F1,F2`, `C` for `F3,F4`);
3. the other new endpoint minority is exactly `M(r)`;
4. every canonical mark assigned to `r` lies in the event counted by `M(r)`, hence

`M(r) >= w(r)`.

#### Proof

For `F1`, `x lessdot r`, `r||a`, and the old relation `x||a` make `(x lessdot r; a)` a valid heavy-state triple. The inherited outward polarity gives `a prec_* r`, while `x prec_* a`, so `Pr(x<a)>2/3` and `Pr(r<a)<1/3`. Its two endpoint minority counts are

`#{a<x}=A`, `#{r<a}=M(r)`.

An `F1` canonical left-swap mark has `x<r<a<y`, so it is counted by `M(r)`.

For `F2`, `r lessdot a`, `r||x`, and `a||x` give `(r lessdot a; x)`. Its endpoint minority counts are

`#{x<r}=M(r)`, `#{a<x}=A`.

An `F2` mark has `x<r<a<y`, hence lies in `{x<r}`.

For `F3`, `(a lessdot r; y)` has endpoint minorities

`#{y<a}=C`, `#{r<y}=M(r)`,

and an `F3` right-swap mark has `x<a<r<y`.

For `F4`, `(r lessdot y; a)` has endpoint minorities

`#{a<r}=M(r)`, `#{y<a}=C`,

and an `F4` mark has `x<a<r<y`.

The structural-return column follows directly from the sibling-cover definitions. For example, after an `F1` transition the old `y` still satisfies `x lessdot y`, `y||a`, so it is an `F1` blocker of the new state; after an `F2` transition the old `y` satisfies `x lessdot y`, `y||a`, which is the new `F3` relation. The other two cases are dual. `square`

### Corollary 3.2 — exact `3/11` transition dichotomy

Suppose the old state is strict low-endpoint and `r` is one of R16/R17's selected blockers, so

`w(r)>2E/33`.

Then

`M(r)/E > 2/33`.

Because the parent candidate has no balanced pair, `M(r)/E<1/3`. Hence exactly one of the following holds:

- **near-band:** `3/11 <= M(r)/E < 1/3`;
- **persistent low state:** `2/33 < M(r)/E < 3/11`, in which case both endpoint minorities of the transition state are `<3/11`.

Thus every selected transition either reaches the team's current near-balance scale or remains in the precise regime where the lead two-packet theorem can be reapplied.

## 4. Coherent right gate exits

Assume R17's coherent right gate. Write the selected blockers as

`b in F1`, `c in F3`, `b||c`,
`y prec_* b prec_* c`.

The selected `F1` blocker `b` carries `w(b)>2E/33` marks. Pivot on its Hasse edge:

`S_b=(x lessdot b; pivot a)`.

By Lemma 3.1 its endpoint minority counts are

`A` and `M_b:=#{b<a}`,

and `M_b>w(b)>2E/33`. The old vertex `y` is a structural `F1` return blocker in `S_b`.

### Theorem 4.1 — coherent right-gate dichotomy

One of the following occurs.

1. `M_b/E >= 3/11`, so the actual incomparable pair `(a,b)` has minority probability in `[3/11,1/3)`.
2. A strict strong-majority span descent / structural reduction occurs at the transitioned state.
3. `M_b/E<3/11` and, after applying the lead's low-endpoint two-packet theorem to `S_b`, there is a selected **right-swap** canonical packet of weight `>2E/33` whose blocker `d` is not the return vertex `y` and satisfies either

   `d prec_* x`  or  `b prec_* d`.

In case 3 the certified packet has therefore reached a genuinely new strong-order frontier outside the transitioned interval `[x,b]`, with no decrease in the `>2E/33` packet floor.

#### Proof

Case 1 is Corollary 3.2. If the new state triggers one of the already authorized reductions, we are in case 2.

Otherwise assume `M_b/E<3/11`. Since the inherited endpoint also has `A/E<3/11`, `S_b` is a strict low-endpoint state. Apply R16/R17's two-packet theorem to it. One selected packet comes from the new left-swap family `F1' union F2'`, and one from the new right-swap family `F3' union F4'`, each with `>2E/33` canonical marks.

The structural return `y` is in `F1'`, hence on the left-swap side. Therefore the selected right-swap blocker `d in F3' union F4'` cannot be the return vertex. Under the inherited no-span polarity for `S_b`, an `F3'` blocker lies strictly after the new right endpoint `b`, while an `F4'` blocker lies strictly before the new left endpoint `x`. This is exactly the stated alternative. `square`

There is an additional structural check consistent with the theorem: because the coherent order has `a prec_* y prec_* b`, the return pair `(a,y)` is a strict strong-majority subspan inside the new pair `(a,b)`. Thus any transition rule that invokes local span descent sees the old endpoint immediately; the packet argument above is stronger in the persistent-low branch because it also identifies a simultaneous non-return channel.

## 5. Coherent left gate exits — dual theorem

Assume instead R17's coherent left gate. Let

`b in F2`, `c in F4`, `b||c`,
`b prec_* c prec_* x`.

Pivot on the selected `F4` blocker `c`:

`S_c=(c lessdot y; pivot a)`.

Its endpoint minority counts are

`M_c:=#{a<c}` and `C`,

and the selected `F4` marks give `M_c>2E/33`. The old `x` is a structural `F4` return blocker in `S_c`.

### Theorem 5.1 — coherent left-gate dichotomy

One of the following occurs.

1. `M_c/E >= 3/11`, so the actual pair `(c,a)` has minority probability in `[3/11,1/3)`.
2. A strict strong-majority span descent / structural reduction occurs.
3. `M_c/E<3/11` and the lead theorem applied to `S_c` supplies a selected **left-swap** packet of weight `>2E/33` with blocker `d` different from the return vertex `x`, satisfying

   `d prec_* c`  or  `y prec_* d`.

Thus the persistent-low branch again exports full certified packet mass to a new strong-order frontier beyond `[c,y]`.

#### Proof

This is the order-dual bookkeeping of Theorem 4.1. Since `C/E<3/11`, the transition remains strict low-endpoint whenever `M_c/E<3/11`. The return `x` lies in the new `F4'` family, hence on the right-swap side. The simultaneously selected left-swap blocker belongs to `F1' union F2'`, so it is not `x`; no-span polarity puts `F2'` strictly before `c` and `F1'` strictly after `y`. `square`

As in the right gate, the coherent order also makes the old incomparable pair `(x,a)` a strict subspan of the transitioned pair `(c,a)` because `c prec_* x prec_* a`.

## 6. Direct application of account02/B19's exact return witness

B19's 515-extension autonomous-prime witness gives the genuine greedy two-cycle

`S0=(5 lessdot 6;10) -> S1=(1 lessdot 10;5) -> S0`.

Its endpoint minorities are:

- at `S0`: `141/515` and `161/515`;
- at `S1`: `128/515` and `141/515`.

The threshold is `3/11`, and

`141/515 - 3/11 = 6/5665 > 0`.

So every state in that exact return cycle has at least one endpoint already outside the strict two-endpoint `<3/11` regime. This is exactly why the witness does not contradict Theorems 4.1-5.1. More importantly, it shows the new dichotomy is not cosmetic: **the remaining return obstruction is concentrated at the near-band/high-endpoint interface**, not inside the strict low-endpoint coherent gate.

The partner's example therefore supplies a source-valid adversary to any attempt to replace the new `3/11` split by an unqualified local acyclicity claim.

## 7. What is paid and what remains

The campaign lead's first local missing implication in r17 was `COHERENT-GATE EXIT`. Theorems 4.1 and 5.1 pay it in the following precise form:

> A coherent same-ray three-antichain gate cannot remain a closed strict-low-endpoint reciprocal gadget. Pivoting on its typed selected blocker either reaches an actual pair with minority in `[3/11,1/3)`, triggers an already authorized structural descent/reduction, or re-enters the strict-low regime with a simultaneous non-return packet of weight `>2E/33` whose blocker lies strictly beyond the transitioned strong-order interval.

Thus the coherent gate is no longer an unclassified local exception. The certified packet floor `>2/33` is retained through the persistent-low transition.

The first essential remaining implication is now:

> **NEAR-BAND / GLOBAL-FRONTIER CLOSURE.** Starting from an actual incomparable pair whose minority lies in `[3/11,1/3)`, or from successive `>2/33` packets that strictly leave each current low-endpoint interval, prove that the complete canonical frontier forces a minority to reach `1/3` before a longer mixed return cycle can close; alternatively force strong-span descent, a proper autonomous/ordinal reduction, or the already controlled exact-two/non-crossed exit. The account02/B19 515-extension cycle shows that a single-channel greedy potential is insufficient at this interface.

This is still a genuine global obligation. No full POS3 proof is claimed.

## 8. Status and integrity

- latest lead account04/B10 r17: **CONSUMED/APPLIED**;
- assigned partner account02/B19 reciprocal-return result/addendum: **CONSUMED/APPLIED**;
- all-four canonical Hasse transition/end-point inheritance table: **PROVED**;
- exact `>2/33` to `[3/11,1/3)` / persistent-low dichotomy: **PROVED**;
- coherent right three-antichain gate local exit: **PROVED**;
- coherent left three-antichain gate local exit: **PROVED**;
- strict-low coherent reciprocal gadget as a closed local exception: **ELIMINATED**;
- near-band/global mixed recycling: **OPEN**;
- parent POS3 theorem: **OPEN / NOT PROVED**;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No finite census is used as proof. The argument is symbolic and arbitrary-size under the stated inherited hypotheses. No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public release, paid model/API/Codex execution, remote workflow, permission change, or verified-brain activation was used or claimed.
