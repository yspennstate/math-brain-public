# POS3 fleet04/B19 addendum — low-endpoint exact backtracks can be bypassed through a globally outside Hasse packet

**Run:** `B19-20260922T081503Z-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `x,y` with `1/3 <= Pr(x<y) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This addendum preserves the immutable main report and its lead-r18 reconciliation. It was added because a newer compatible other-account theorem landed during the same invocation and allows the first remaining exact-backtrack case to be sharpened substantially. Every probability below is under the original uniform law on all full linear extensions of the original poset.

## 1. New exact source consumed

The current campaign-lead state remains

- **fleet04/B10 r18**, `proofnet24/collective-POS3/fleet04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, Git blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

Its low-endpoint exact-backtrack state is

`p lessdot r`, `q||p,r`, `p prec_* q prec_* r`,

with three full-law cells

`A=#{L:p<r<q}`, `H=#{L:p<q<r}`, `B=#{L:q<p<r}`, `E=e(P)`,

and

`A/E=Pr(r<q)<3/11`, `B/E=Pr(q<p)<3/11`, `H>5E/11`.

The assigned OTHER-account partner result used here is

- **fleet01/B10**, `proofnet24/collective-POS3/fleet01/B10/20260922T072132Z-b10-pos3-r11/REPORT.md`, Git blob `85fa62968e584b5db7fe6270260f55f92c071438`.

It proves that, under the no-balanced-pair hypothesis, `prec_*` is a strict total order and supplies the strict fixed-ray potentials

`Psi_R(u,v)=n rho(v)+rho(v)-rho(u)`,

`Psi_L(u,v)=n(n-1-rho(u))+rho(v)-rho(u)`.

The decisive newer compatible result consumed and applied is

- **fleet02/B10 r12**, `proofnet24/collective-POS3/fleet02/B10/20260922T084851Z-b10-pos3-r12/REPORT.md`, science commit `57a563af112063929fae35a4aa28c4fe61aa64cf`.

It proves exact **double leakage** for every low-endpoint exact backtrack. For the left active pair `(p,q)`, after removing the central Hasse channel `r`, at most three external Hasse channels carry total outgoing defect more than `2E/11`, hence one carries more than `2E/33`. For the right active pair `(q,r)`, after removing the central channel `p`, the same statement holds. The two external witness families are vertex-disjoint. Each selected channel either gives strict span descent or an outward incomparable pair with minority probability `>2/33`.

The main report of this B19 run had already paid the thin-laminar typed subcase. The point below is stronger and orthogonal: **every** noncentral leak, irrespective of its F-type, lies outside the entire three-point strong-order bridge once both adjacent span-descent exits have been exhausted. Consequently the literal exact-backtrack edge can always be bypassed.

## 2. Global-outside leakage lemma

Assume throughout that there is no balanced pair and that strict strong-majority span descent has been exhausted for both adjacent active pairs `(p,q)` and `(q,r)`.

Use fleet02/B10's channel notation

`U(a,b)={z:a lessdot z, z||b}`,

`D(a,b)={z:z lessdot b, z||a}`.

The central backtrack witnesses are `r in U(p,q)` and `p in D(q,r)`.

### Theorem 2.1 — every noncentral left leak is outside `[p,r]_*`

Let `z` be any noncentral Hasse channel for `(p,q)` carrying positive outgoing marks.

1. If `z in D(p,q)`, then `z prec_* p`.
2. If `z in U(p,q)\{r}`, then `r prec_* z`.

#### Proof

If `z in D(p,q)`, then `z lessdot q` and `z||p`. Every marked extension lies in the event `p<z<q`. Thus `Pr(p<z)>0`. Under the no-balanced hypothesis the incomparable pair `(p,z)` is strongly oriented one way or the other. If `p prec_* z`, then the forced relation `z<q` gives

`p prec_* z prec_* q`,

so `(p,z)` is a strict strong-order subspan of `(p,q)`, contrary to the no-descent assumption. Therefore `z prec_* p`.

Now let `z in U(p,q)\{r}`. Then `p lessdot z` and `z||q`. No descent for `(p,q)` rules out `z prec_* q`, because `p prec_* z` is forced by the poset relation and would give the strict inner pair `(z,q)`. Hence

`q prec_* z`.

Compare `z` with `r` in the total order `prec_*`. If `z prec_* r`, then

`q prec_* z prec_* r`

and `(q,z)` is a strict subspan of the adjacent active pair `(q,r)`, again forbidden. The equality `z=r` was excluded. Hence `r prec_* z`. `square`

### Theorem 2.2 — every noncentral right leak is outside `[p,r]_*`

Let `z` be any noncentral Hasse channel for `(q,r)` carrying positive outgoing marks.

1. If `z in U(q,r)`, then `r prec_* z`.
2. If `z in D(q,r)\{p}`, then `z prec_* p`.

#### Proof

For `z in U(q,r)`, the relation `q lessdot z` and incomparability `z||r` hold. If `z prec_* r`, then `q prec_* z prec_* r`, giving a strict subspan of `(q,r)`. Hence no descent forces `r prec_* z`.

For `z in D(q,r)\{p}`, we have `z lessdot r` and `z||q`. No descent for `(q,r)` first forces `z prec_* q`: the opposite orientation `q prec_* z` would place `(q,z)` strictly inside `(q,r)`. Compare `z` with `p`. If `p prec_* z`, then, since `z prec_* q`, the incomparable pair `(z,q)` lies strictly inside `(p,q)`. Equality `z=p` was excluded. Therefore `z prec_* p`. `square`

### Corollary 2.3 — the double leak is globally external

In the low-endpoint branch, fleet02/B10 r12 supplies one external channel on each side carrying more than `2E/33` marked full extensions. By Theorems 2.1-2.2, after span descent is removed, **both selected witness vertices lie outside the whole bridge interval** `[p,r]_*`: each is either strictly before `p` or strictly after `r` in the strong-majority total order.

This location statement is not present in the double-leak theorem itself. It uses the fact that the exact backtrack exposes *both* adjacent active pairs, so a would-be witness lying between `q` and `r` (or between `p` and `q`) is already a legal span-descent exit for the other pair.

## 3. Exact-backtrack bypass from the current active pair

The second half of the exact backtrack is the transition from the current pair `(q,r)` back to `(p,q)` through the central channel `p in D(q,r)`.

Fleet02/B10 r12 guarantees that, in the low-endpoint branch, there is instead a **noncentral** channel `z` for `(q,r)` carrying more than `2E/33` marks. Select that channel rather than the central `p` channel.

There are only two possibilities.

### Case R — `z in U(q,r)`

Then Theorem 2.2 gives

`q prec_* r prec_* z`,

and the marks lie in the genuine minority event `{z<r}` for the incomparable pair `(r,z)`, with

`Pr(z<r)>2/33`.

Thus the alternative transition is

`(q,r) -> (r,z)`.

It stays on the right ray and raises the assigned partner's fixed-right potential. Indeed, with `i=rho(q)<j=rho(r)<k=rho(z)`,

`Psi_R(r,z)-Psi_R(q,r)`
`= n(k-j)+(k-j)-(j-i)`
`>= n+1-(n-2)=3>0`.

### Case L — `z in D(q,r)\{p}`

Then Theorem 2.2 gives

`z prec_* p prec_* q prec_* r`.

The marks lie in the minority event `{q<z}` of the incomparable pair `(z,q)`, again with probability `>2/33`. The alternative transition is

`(q,r) -> (z,q)`.

This is not an exact return. It is precisely the strict opposite-ray envelope-expansion alternative from the lead's two-step switch normal form, since

`[p,q]_* proper_subset [z,q]_*`.

Therefore, in the low-endpoint no-descent branch, **the induction never needs to take the literal exact-backtrack edge**. At the very state where that edge would return to `(p,q)`, a noncentral `>2/33` channel is available which either strictly increases `Psi_R` on the same ray or performs a strict envelope expansion to the left.

The order-dual statement holds for a left-then-right exact backtrack.

## 4. Consequence for the global induction

This eliminates the local low-endpoint exact-backtrack branch as a required transition, not merely as a locally closed two-state recycler.

A choice-based recursive export may adopt the following deterministic rule:

1. use the fleet02/B10 four-channel export from the current strong incomparable pair;
2. accept a balanced pair or strict span descent immediately;
3. on a same-ray outward channel, continue and use fleet01/B10's strict fixed-ray potential;
4. if the chosen opposite-ray channel would be the central channel of a low-endpoint exact backtrack, replace it by the guaranteed noncentral `>2/33` channel from Theorem 3 above;
5. hence every surviving ray switch is a **strict envelope expansion**, never a literal low-endpoint exact return.

The lead r18 residual `strict envelope expansions + non-exact/multi-distinguisher exact backtracks` can therefore be sharpened, in the low-endpoint regime, to **strict outside-envelope reuse alone**. The earlier B19 thin-laminar/double-fan distinctions are not needed merely to bypass the exact return; they remain potentially useful for quantitative accounting after the expansion.

The first genuinely unpaid implication is now:

> **`POS3-OUTSIDE-ENVELOPE-REUSE-v1`.** In a no-balanced, span-descent-exhausted width-three candidate, rule out a recursive sequence of four-channel exports in which every fixed-ray segment has the fleet01/B10 strict integer potential and every ray switch is a strict envelope expansion through a witness lying outside the preceding heavy bridge. Show that the first reuse of a previously exposed outer strong-order region forces a balanced pair, strict span descent, a width-four contradiction, a proper autonomous/ordinal reduction, or an already-controlled exact-two state.

This addendum does **not** prove that global statement. In particular, a rank-only argument is not asserted: fixed-ray potential gain can coexist with later opposite-ray expansion, so a genuinely cross-envelope invariant or charge transfer is still required.

## 5. Status and integrity

- fleet04/B10 r18 heavy-bridge / two-step switch normal form: **CONSUMED/APPLIED**;
- assigned partner fleet01/B10 fixed-ray total-order/potential theorem: **CONSUMED/APPLIED**;
- newer fleet02/B10 r12 disjoint double-leak theorem: **CONSUMED/APPLIED**;
- every noncentral leak lies outside the complete exact-backtrack bridge interval after adjacent span descent is exhausted: **PROVED**;
- low-endpoint exact-backtrack edge has a noncentral `>2/33` bypass from the current pair: **PROVED**;
- bypass is either strict same-ray `Psi_R/Psi_L` gain or strict opposite-ray envelope expansion: **PROVED**;
- literal low-endpoint exact return as a necessary recursive transition: **ELIMINATED**;
- global outside-envelope reuse: **OPEN**;
- high-endpoint `[3/11,1/3)` branch: **REMAINS SEPARATE**;
- parent POS3: **OPEN / NOT PROVED**;
- run classification remains **`ESSENTIAL_STEP_APPLIED`**.

No computation was used in this addendum. No benchmark material, held-out answer, credentials, scheduler identifier, machine path, unrelated private data/transcript, email/Drive data, paid/remote compute, workflow dispatch, permission change, or public posting was used.