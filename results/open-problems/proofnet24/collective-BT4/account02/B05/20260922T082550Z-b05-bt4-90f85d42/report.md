# BT4 account02/B05 — second-collar degree budget forces two fresh packed exits

Run: `20260922T082550Z-b05-bt4-90f85d42`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Candidate: `BT4-R4-F3-SECOND-COLLAR-TWOEXIT-v1`  
Outcome: `ESSENTIAL_STEP_APPLIED`; stronger always-clean-light shortcut `CANDIDATE_REFUTED`  
Target status: `OPEN_NOT_PROVED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. Source-exact target and controls

Target: every finite loopless digraph with at most one arc per ordered pair of distinct vertices and minimum outdegree at least seven contains four pairwise vertex-disjoint genuinely directed cycles. Digons are permitted in the source statement. No nearly-directed or edge-disjoint substitute is used here.


## 2. Exact inherited mathematics consumed

### Campaign lead account02/B04

Latest complete lead report consumed:

`proofnet24/collective-BT4/account02/B04/20260922T0619Z-b04-bt4-r11/report.md`, Git blob `713053330313bf5906035c7bfd5841eb4e6b88ef`.

Its normal form is a hypothetical oriented exact-outdegree-seven counterexample, arc-dominated and 3-vertex-strong, with three disjoint directed cycles chosen lexicographically: minimum total packed order, then maximum number of arcs induced by the acyclic remainder. Packed cycles are chordless. The lead's corrected four-port witness lift guarantees a genuine CROSS or same-support BYPASS but leaves coalesced-port and disjoint-splice closure unpaid.

### Named OTHER-account partner account03/B06

I consumed and apply the completed partner report

`proofnet24/collective-BT4/account03/B06/20260922T072201Z-account03-B06-bt4-r11/report.md`, candidate `BT4-R4-F3-APEX-COLLAR-v1`, Git blob `102e3a54d5cac3a14afd00122e3d485d99a1b632`, together with checker blob `4163d8856dd65ef7d8de8b01e2bf5a2bf03785e2` and output blob `7ef16c415f9e1fb948a8bada31eaf0411acda238`.

In the canonical four-remainder F3 both-repeat state, write

`S* = p -> x -> s -> p`,

let `U` be the other light packed cycle, let the old remainder be `R*={q,a,b,c}`, and let the two-indirect return be

`W = u -> a -> p -> b -> u`.

The partner proves that a packed three-hit apex on `U-{u}` lies in `{u^-,u^{--}}`. In the second-predecessor case `z=u^{--}` it forces the neutral whole-support replacement

`C_z = z -> b -> u -> U[u,z] -> z`,

and the exchanged remainder is exactly `{q,a,c,u^-}` and must be acyclic in a true BT4 counterexample. Put

`t := u^-`.

I also use account04/B04 `BT4-R4-F3-RETURN-CUT-v1`, report blob `425b7f0491ef4caf794ce862783c811edd26b110`, which proves the complementary one-cut acyclicity on `(U-{u}) union {s}` in this two-indirect state.

## 3. Compact conditional end-to-end route

Assume BT4 false and enter the inherited oriented exact-seven minimum-counterexample normal form. Run the established SIX/global-NO-SIX reduction and the four-remainder F3 split. In the both-repeat, two-indirect F3 branch, apply the partner's apex-collar theorem. The immediate-predecessor location remains a separate branch; in the second-predecessor location this report proves that the newly exposed vertex `t=u^-` cannot remain trapped in the neutral-exchange orbit: exact outdegree seven plus chordlessness force at least two direct exits from `t` to the other packed cycles.

Those exits yield either a fresh four-port opposite light-cross pair or a fresh light-to-heavy crossing. Thus the second-predecessor collar feeds the lead's genuine CROSS/heavy-entry splice interfaces without any reversed arc. Full BT4 would follow after the resulting fresh-port splice is closed together with the separate SIX, F2/other F3, and larger-remainder branches.

## 4. Theorem — `BT4-R4-F3-SECOND-COLLAR-TWOEXIT-v1`

Assume the exact partner second-predecessor state above. Let `t=u^-`. Then

`|N^+(t) intersect (H union S*)| >= 2`.                         (1)

Consequently at least one of the following holds.

1. **Clean light alternative.** There is `y in S*\{p}` with `t->y`. Together with the inherited return path `p->b->u`, this gives two opposite light-cross paths

   `t -> y` and `p -> b -> u`

   having four distinct packed endpoints `{t,y,p,u}` and vertex-disjoint interiors.

2. **Heavy-entry alternative.** There is `h in H` with `t->h`, a direct fresh light-to-heavy cross from a packed vertex `t` not used as the U-port of `W`.

### Proof

The old three-cycle packing partitions the vertex set into `H`, `S*`, `U`, and the four-vertex remainder `R*={q,a,b,c}`.

Because `U` is a packed cycle in the globally minimum packing, it is chordless. Therefore the only possible outneighbor of `t` inside `U` is its support successor `u`. Hence

`|N^+(t) intersect U| <= 1`.                                  (2)

There are only four vertices in `R*`, so

`|N^+(t) intersect R*| <= 4`.                                 (3)

The normal form has exact outdegree seven. Combining (2) and (3), at most five outneighbors of `t` can lie in `U union R*`, and therefore at least two distinct outneighbors lie in the complementary packed set `H union S*`. This proves (1).

If one of those targets is some `y in S*\{p}`, then `t->y` is a direct U-to-S* cross. The partner's two-indirect return contains the S*-to-U path `p->b->u`. Here `t!=u`, `y!=p`, and `b` lies in the old remainder, so the two cross paths have four distinct packed endpoints and disjoint interiors. This is the clean light alternative.

Otherwise every target of `t` in `S*` is contained in the singleton `{p}`. Since (1) supplies at least two distinct targets in `H union S*`, at least one lies in `H`. This is the heavy-entry alternative. QED.

### One-cut sharpening

If the clean target is specifically `y=s`, then `t=u^-` is the terminal vertex of the broken support path `U-u`. The inherited one-cut condition says every `s->U` port lies strictly after every `U->s` port on that path. Since `t` is already the last possible `U->s` port, there is no later position, so `s` has no outneighbor in `U-{u}`. This extra restriction is available to the splice stage but is not needed for theorem (1).

## 5. Source-valid refutation of a tempting stronger shortcut

The stronger statement

> the two forced exits always include a target in `S*\{p}`

is false even under the strong local inherited hypotheses.

The partner's exact 18-vertex certificate has

`H={0,1,2,3,4,5}`, `U={6,7,8,9,10}`, `S*={11,12,13}`,
`p=11`, `u=6`, `z=9=u^{--}`, `t=10`, and old remainder `{14,15,16,17}`.

Its exact row is

`N^+(10)={0,2,3,6,11,14,17}`.

Thus `t` has four targets in `H union S*`, namely `{0,2,3,11}`, but no target in `S*\{p}`. The heavy-entry alternative is therefore genuinely necessary; the source-valid certificate realizes it with three heavy targets `{0,2,3}`. This refutes only the stronger shortcut, not BT4.

## 6. Exact diagnostic

`checker.py` is source-bound to the partner report/checker blobs and checks the finite degree-budget arithmetic plus the exact row above. It was executed in the current run. The archived output reports `PASS`, universal maximum noncross budget `1+4=5`, universal minimum packed-exit count `7-5=2`, certificate cross targets `[0,2,3,11]`, no clean-light target, and heavy targets `[0,2,3]`.

This checker is only a sanity/source-validity diagnostic. The universal statement is proved by the counting argument in Section 4; no finite search is promoted to a theorem.

## 7. What this pays for

The preceding partner theorem left the second-predecessor collar as a neutral equal-size exchange with an acyclic four-vertex remainder. The present theorem proves that this collar is not a closed neutral orbit: the vertex newly omitted from `U` already carries at least two direct packed exits in the original graph, forced solely by exact outdegree seven, chordlessness, and the four-remainder budget.

This is exactly the requested reversed-arc-defect mechanism: an authentic forward reroute is supplied by the degree condition. No reversed edge, nearly-directed cycle, or edge-disjoint relaxation is introduced.

The result does **not** yet turn one or two crosses into two vertex-disjoint replacement cycles. In particular, the heavy-entry alternative may coalesce with an existing interface, and the clean four-port pair still needs the lead's splice/selection closure.

## 8. First unpaid implication

`BT4-R4-F3-FRESH-PORT-SPLICE-v1`:

> In the canonical four-remainder F3 second-predecessor state, combine either (A) the clean opposite light pair `t->y` and `p->b->u` with four distinct packed ports, or (B) the fresh direct light-to-heavy crossing `t->h`, with the inherited reciprocal/third-port/heavy-entry and CROSS/BYPASS machinery. Prove that the configuration yields two vertex-disjoint replacement directed cycles, a strictly smaller three-packing, a directed cycle in an exchanged remainder, SIX, or a fourth directed cycle.

Separate SIX, F2, immediate-predecessor/other F3, coalesced-port, and larger-remainder obligations remain explicit. Hence BT4 remains open.

## 9. Honest outcome and provenance

Outcome: `ESSENTIAL_STEP_APPLIED`. The theorem removes the possibility that the partner's second-predecessor neutral collar carries no new forward packed interface. The stronger claim that a clean light target is always forced is `CANDIDATE_REFUTED` by the exact partner certificate. No full-proof candidate is claimed.

Model self-report: `GPT-5.6 Sol`. Requested reasoning effort: no separate authenticated effort selector/value was exposed to this run; `UNKNOWN`. Configured reasoning effort: `UNKNOWN / NOT_EXPOSED`. Known effective reasoning effort: `UNKNOWN`. Provider reasoning-token/time counters: `null / NOT_EXPOSED`.

Account-local scheduler inspection found all twenty current managed B01-B20 assignments present, enabled on hourly cadences, quiet, and role-aligned, including B05 on BT4. No deficit requiring B20 action was observed and no scheduler mutation was made.
