# Reconciliation with campaign lead r18

**Run:** `B19-20260922T081503Z-r11`  
**Status:** `ESSENTIAL_STEP_APPLIED`; parent POS3 remains **OPEN / NOT PROVED**.

This note was added after the immutable main attempt report because a newer complete campaign-lead version appeared during the same invocation. It does not rewrite the prior report; it source-binds its theorem into the newer lead normal form.

## Newer lead consumed

The latest complete team-lead version now available is

- **account04/B10 r18**, `proofnet24/collective-POS3/account04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`, Git blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

R18 proves that every surviving outward four-channel export recreates a heavy Hasse bridge. A two-step opposite-ray switch is then exactly one of: strict strong-majority span descent, strict envelope expansion, or an exact backtrack through such a heavy bridge. In the low-endpoint exact-backtrack branch, for a cover `p lessdot r` and `q||p,r` with `p prec_* q prec_* r`, its three cells satisfy

`B/E = Pr(q<p) < 3/11`,
`A/E = Pr(r<q) < 3/11`,
`H/E = Pr(p<q)+Pr(q<r)-1 > 5/11`.

R18 leaves the non-exact / multi-distinguisher exact-backtrack branch unpaid.

## Exact mapping of the B19 theorem into r18

Set

`x=p`, `a=q`, `y=r`.

Then the low-endpoint exact-backtrack bridge in r18 is literally the heavy-cover input used by B19's preceding `F1`-`F4` decomposition. After the already-paid high `F1/F4` exits, the surviving typed state has

`ell in F2`, `s in F3`,

`ell lessdot q lessdot s`,

`ell prec_* p prec_* q prec_* r prec_* s`,

with boundary pairs `(ell,p)` and `(r,s)`. The two old interior endpoint minorities required by the B19 thin-laminar theorem are exactly r18's endpoint cells:

`Pr(q<p)=B/E<3/11`,
`Pr(r<q)=A/E<3/11`.

Therefore the main report's Theorems 3.1 and 4.1 apply *verbatim* to the first low-complexity subcase of r18's newly isolated exact-backtrack obstruction.

### Right boundary

If

`Pred(r) proper_subset Pred(s)`, `Succ(s) subseteq Succ(r)`,

and `q` is the unique maximal element of `Pred(s)\Pred(r)`, then the opposite canonical successor fringe `M_R` is nonempty, has at most two members, and carries

`Pr(B_R \ {r<q}) > 2/33`.

If `M_R={u}` is a singleton, then `s prec_*u`,

`Pr(u<s)>2/33`,

and the same-ray transition `(r,s)->(s,u)` strictly increases account01/B10's `Psi_R`.

### Left boundary

Dually, if

`Pred(ell) subseteq Pred(p)`, `Succ(p) proper_subset Succ(ell)`,

and `q` is the unique minimal element of `Succ(ell)\Succ(p)`, then the opposite predecessor fringe `M_L` is nonempty, has at most two members, and carries

`Pr(A_L \ {q<p}) > 2/33`.

If `M_L={d}` is a singleton, then `d prec_*ell`,

`Pr(ell<d)>2/33`,

and `(ell,p)->(d,ell)` strictly increases `Psi_L`.

No independence or cross-anchor positive-association statement is used in either argument; the exact `2/33` is simply

`1/3 - 3/11`.

## Consequence for r18's first uncovered branch

A low-endpoint exact backtrack of r18 **cannot survive as a thin single-channel laminar `F2/F3` recycler**. To survive all already-paid exits, each unresolved `F2/F3` boundary must expose at least one higher-complexity feature:

1. a crossed-neighborhood inclusion fails, hence there is a reverse-direction relation distinguisher;
2. the central middle vertex `q` is not the unique extremal discrepancy, hence there is a second same-direction canonical discrepancy; or
3. the newly forced opposite fringe has two canonical members, hence a width-saturating two-channel fan whose union retains `>2/33` new mass.

Thus r18's non-exact/multi-distinguisher exact-backtrack obstruction is sharpened to a **double-fan / crossed multi-distinguisher exact-backtrack state** after the thin laminar subcase is removed.

The global strict-envelope-reuse obstruction in r18 is not solved here. Nor is an individual `>2/33` pair extracted from a two-member fan. Those are retained as genuine unpaid implications.

## Updated next implication

The next source-valid target after combining r18 with this run is:

> **POS3-EXACT-BACKTRACK-DOUBLE-FAN-EXIT.** In the low-endpoint exact-backtrack heavy bridge, after high `F1/F4` and thin-laminar `F2/F3` exits are removed, prove that the remaining two-channel fan / crossed multi-distinguisher state yields a balanced pair, strict span descent, proper autonomous/ordinal reduction, or a charged same-ray endpoint advance; then integrate that exit with r18's strict-envelope expansion normal form to forbid first envelope reuse.

This is a narrower statement than r18's original non-exact/multi-distinguisher exact-backtrack branch, but it is not claimed proved in this run.
