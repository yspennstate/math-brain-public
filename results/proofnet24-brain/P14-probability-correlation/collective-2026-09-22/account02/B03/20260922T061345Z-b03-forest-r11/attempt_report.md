# FOREST B03 — STAR-2 parent-hardness, mixed-interaction adversaries, and an irreducible corrected separator statement

Run: `20260922T061345Z-b03-forest-r11`  
Campaign: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**  
Context: **WITHOUT_VERIFIED_BRAIN**  
Parent FOREST remains **OPEN**; no public solved-problem or novelty claim is made.

## 1. Controls and continuation state

Fresh mandatory controls were read from `yspennstate/math-research-brain` at main commit `44c473e1d5af1c1712a165e969756e7b247e54a7`: `AGENTS.md`, `scheduled_tasks/README.md`, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, and `scheduled_tasks/PROTOCOL.md`, including OWNER MESSAGE, together with the live collective `ORDER.md`, `TARGETS.md`, and `ASSIGNMENTS.json`. OWNER CONTROL remained `2026-09-22.2`; the active programme remained `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`; B03 remained FOREST adversary/separator research. No later applicable owner/platform stop was found. Old brain-installation and benchmark work stayed stopped.

The newest local B03 report consumed was `20260922T051049Z-b03-forest-auto11`, report blob `57bd1c4cceaa39ba9db44f4f024a3b9a4f41c65c`. It proved exact rational two-terminal unitization and exact simple replacement of contraction-created parallel classes. This run does not repeat that construction; it changes mechanism to attack the newer source-generated STAR-2 conditional debt.

The latest campaign-lead handoff consumed was account01/B01 `20260922T050946Z-b01-forest-auto11`, shared blob `4cee205cb7d254caf785692838111988a0b8a155`, candidate `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`. Its source-safe route says: in an edge-minimal simple counterexample with bad pair `(e,f)`, every third edge `g` outside triangles is handled by deletion/contraction minimality plus an exact Simpson relation; triangle edges remain because contracting them creates weight 2 on a subset of one star.

The required named OTHER-account result actually applied was account03/B01 `20260922T053534Z-account03-B01-forest-r11`, shared blob `c49d586a18b973280db00e48457a4c2929775ec8`, candidate `FOREST-STAR2-SPLIT-CONDITIONING-v1`. It gives an exact source interpretation of STAR-2: if `J` is simple with nonadjacent terminals `u,v`, identify `u,v` and merge duplicate classes. Uniform forests of `J` conditioned on `u` disconnected from `v` correspond, with exact multiplicities, to the `{1,2}`-star weighted quotient. Thus the triangle-contraction debt can be written as the conditional source inequality

`Cov_J(1_e,1_f | u not connected to v) <= 0`.

That peer also refuted coordinatewise monotonicity of the gap under a single star doubling. The present run asks whether a universal conditional/STAR-2 theorem is a genuinely smaller lemma, and whether simultaneous doublings have any usable sub/supermodular sign.

## 2. Compact conditional end-to-end route and first missing implication

The lead's current source-safe route can be stated compactly as follows.

1. Assume an edge-minimal simple counterexample `G` with violating pair `(e,f)`.
2. For every third edge `g` in no triangle, both `G\g` and `G/g` remain smaller simple graphs, so minimality applies. The lead's total-covariance argument then forces the positive-correlation matching/budget constraints.
3. If the same conclusion can be obtained for every triangle edge `g`, the rank-homogeneous budget rules out the minimal counterexample.
4. By account03/B01's exact split identity, the first missing triangle implication is precisely the conditional inequality above, but only for `J=G\g` arising from an edge-minimal parent counterexample.

The key point established below is that **dropping the minimal-parent geometry and trying to prove the conditional inequality universally is parent-hard**. Therefore the correct missing implication must retain an irreducibility hypothesis; universal STAR-2/conditional preservation is not a lower-complexity induction lemma.

## 3. Parent-hardness of universal source-generated STAR-2

### Theorem 3.1 — even a pendant source-generated doubled edge can carry an arbitrary FOREST instance

Let `H` be any finite simple graph, let `e,f` be distinct edges of `H`, and choose any vertex `z` of `H`. Add fresh vertices `u,v` and the triangle edges

`uz, vz, uv`.

Call the resulting simple graph `G`, and let `g=uv`. The triangle is attached to `H` only at `z`, so this is a 1-sum.

Contract `g`. The vertices `u,v` merge to a vertex `x`, and `uz,vz` become one simple quotient edge `xz` of multiplicity/weight `2`. This is exactly a nonempty source-generated STAR-2 contraction: all nonunit weight lies on one star edge.

Because `xz` is a leaf edge of the weighted quotient, its forest polynomial factor is simply `1+2=3`. For each of

`X in {Z, Z_e, Z_f, Z_ef}`

we therefore have

`X_{G/g}=3 X_H`.

Consequently

**`Delta_{G/g}(e,f)=9 Delta_H(e,f)`.**

Hence a theorem asserting negative correlation for **all** source-generated nonempty STAR-2 contraction quotients would immediately imply FOREST for arbitrary `H`. The same construction shows that a universal theorem asserting

`Cov_J(e,f | u not connected to v) <= 0`

for arbitrary simple `J,u,v,e,f` cannot be regarded as a simpler induction input: after the exact account03/B01 identification it contains an arbitrary FOREST instance as a factor.

This is not a counterexample to FOREST or STAR-2. It is a counterexample to the proposed *proof architecture* that treats universal STAR-2/conditional preservation as a strictly easier local lemma.

### Why minimality matters

If `H` above were itself a counterexample, then the attached `G` could never be edge-minimal. The parent-hardness construction is therefore precisely what minimal-counterexample hypotheses must exclude. A correct triangle-edge lemma must exploit that irreducibility rather than erase it.

## 4. Exact mixed-interaction adversaries for simultaneous star doublings

Account03/B01 already showed that one-coordinate monotonicity can fail. A tempting repair is to hope that the full Rayleigh gap is nevertheless submodular or supermodular in the set of star edges doubled from `1` to `2`, allowing a sum of one-edge changes. Both signs fail on tiny exact examples.

### Negative mixed difference

Take `K4` on vertices `{0,2,3,4}` with edges

`02,03,04,23,24,34`.

Use star center `3`, variable star edges

`h1=23`, `h2=34`,

and marks

`e=03`, `f=24`.

Let `Delta(a,b)` denote the exact Rayleigh gap when `(h1,h2)` have weights `(a,b)` and all other edges have weight `1`. Direct enumeration gives

`Delta(1,1)=6`,
`Delta(2,1)=12`,
`Delta(1,2)=12`,
`Delta(2,2)=16`.

Thus the discrete mixed difference is

`Delta(2,2)-Delta(2,1)-Delta(1,2)+Delta(1,1) = -2`.

So the gap is **not supermodular** in the doubled-star coordinates.

### Positive mixed difference

Take the simple graph on vertices `{0,1,2,3}` with edges

`01,02,03,12`,

star center `0`, variables `h1=02,h2=03`, and marks `e=01,f=12`. Then

`Delta(1,1)=8`,
`Delta(2,1)=24`,
`Delta(1,2)=18`,
`Delta(2,2)=54`,

so the same mixed difference equals

`54-24-18+8 = 20`.

Thus the gap is **not submodular** either.

Therefore no proof may safely aggregate STAR-2 by assuming a fixed sign for pairwise interactions among doubled star edges. The obstruction already occurs on four vertices.

## 5. Corrected local certificate for one doubling

For a fixed unmarked edge `h`, put fugacity `t` only on `h`. Because the forest polynomial is multiaffine,

`q(t)=Delta(e,f;t)=D0 + M t + D1 t^2`,

where `D0` is the deletion-side Rayleigh gap and `D1` is the leading contraction-side gap. The identity

**`q(2)=2 q(1)-D0+2D1`**

is immediate. Therefore doubling `h` from weight `1` to `2` is safe **if and only if**

**`D0 <= 2 q(1)+2D1`.**

This exact criterion correctly allows the partner's phenomenon `q(2)<q(1)`; monotonicity is unnecessary. It also records the two conditional strata instead of replacing them by an unsigned surrogate.

For several doubled star edges, Section 4 shows that one cannot sum such inequalities using an assumed fixed interaction sign. A sequential application is an algebraically valid sufficient certificate only when every intermediate state is separately justified; it is not, by itself, a source-valid minimality argument because partially doubled weighted states need not be smaller unit-simple graphs.

## 6. Corrected source-valid sufficient statement: isolate the marked block

The parent-hardness example identifies the exact reducible geometry that should be removed first.

### Proposition 6.1 — block-separable STAR-2 is harmless

Let `Q` be a contraction quotient whose underlying graph is simple, with positive edge weights, and suppose its only nonunit weights are STAR-2 weights. Let `e,f` be the marks.

A forest of a graph is exactly a choice of a forest independently in every block, because every cycle lies inside one block. Hence the forest partition function factorizes over the block decomposition.

- If `e` and `f` lie in different blocks, their indicators are independent and `Delta_Q(e,f)=0`.
- If they lie in a common block `B`, all blocks outside `B` multiply each of `Z,Z_e,Z_f,Z_ef` by the same positive factor `K`. Therefore

`Delta_Q(e,f)=K^2 Delta_B(e,f)`.

In particular, if the common marked block `B` contains **no doubled edge**, then `B` is an ordinary unit simple graph. In an edge-minimal counterexample setting it is strictly smaller than the parent graph, so minimality gives `Delta_B(e,f)>=0`, and therefore the STAR-2 contraction is safe.

Thus the genuinely unresolved triangle-contraction configuration can be narrowed to:

> `e`, `f`, and at least one doubled star edge all lie in one common 2-connected block of the contraction quotient.

Equivalently, a pendant doubled edge, or any doubled branch separated from the marked block by an articulation, cannot be the hard case. This is the corrected sufficient statement that survives the parent-hardness adversary and retains the source's minimal-counterexample geometry.

This is materially stronger than saying merely that the quotient has a `{1,2}` weighted star: it strips all reducible STAR-2 mass and leaves only **cycle-entangled doubled edges**. That is exactly the overlapping-cycle regime assigned to B03.

## 7. Direct application of the named partner result

Account03/B01's exact split-conditioning result remains valid and is sharpened by Proposition 6.1 as follows.

For a triangle edge `g=uv` in a minimal counterexample, put `J=G\g`. Conditioning on `u` disconnected from `v` is equivalent to the STAR-2 contraction law. But a universal conditional-preservation theorem is parent-hard by Theorem 3.1. Therefore the next legitimate target is only the **irreducible conditional statement**:

`Cov_J(e,f | u not connected to v) <= 0`

under the additional source condition that, after identifying `u,v`, the marks and at least one doubled common-neighbor edge lie in the same 2-connected block.

This is the first essential missing implication retained after the present adversaries. It is strictly narrower than the peer's universal formulation and cannot be defeated by the pendant-triangle embedding.

A plausible next mechanism is the partner's component-factor identity

`Z_H = sum_{R forest of H-x} product_{C component of R} (1 + sum_{xw,w in C} r_w)`,

but applied only to components participating in the common marked block. Fixed-sign coordinate monotonicity, submodularity, and supermodularity are now all ruled out, so the next proof must use a genuinely global component coupling/flow or a signed inequality retaining the block connectivity.

## 8. Exact computation and regression

The committed checker `forest_star2_adversary_checker.py` has Git blob

`183dfcf54dc1f0601a39344ac8b3180e2a480e55`,

SHA-256

`c7d8f773a5156e67cfce9d9751a1653dd5a9542b7e3e1050f4576525a3a9e13d`,

and 4,561 bytes.

Its captured output has Git blob

`8e3aba77935ca63e221410792452675424981120`,

SHA-256

`726ca4a599895294da05ee4ad8a0ed9de44359ae75b554fec352acc6cd71b817`.

The checker exactly verifies both mixed-interaction witnesses above. It also exhausts the account03/B01 conditional source inequality for every labelled simple graph through six vertices with fixed terminal pair (vertex relabelling covers arbitrary terminal pairs), checking the following marked instances:

- `n=3`: 1,
- `n=4`: 80,
- `n=5`: 4,608,
- `n=6`: 372,736,

with zero failures. This finite PASS is regression evidence only and is not promoted to a universal theorem.

Finally, it exhaustively verifies the factor-9 pendant-triangle scaling identity on 11,766 marked graph instances with base graphs through five vertices. It ends `STATUS=PASS`.

## 9. Movement, failures, and next attack

**Target-level movement:** FOREST remains OPEN; no end-to-end proof is claimed.

**Mechanism-level movement:** substantive. The run (i) proves universal STAR-2/conditional preservation is parent-hard even for a source-generated pendant doubled edge, (ii) kills both submodular and supermodular simultaneous-doubling repairs by exact four-vertex witnesses, (iii) records the exact one-edge doubling certificate, and (iv) reduces the source-valid hard case to a doubled edge cycle-entangled with both marks in one common 2-connected block.

**CANDIDATE_REFUTED:** the candidate proof mechanism “prove universal STAR-2/endpoint-disconnection conditional preservation as a smaller local lemma” is refuted as a lower-complexity induction architecture by Theorem 3.1. This does **not** refute STAR-2 or FOREST as mathematical statements.

**Next exact attack:** work only in the irreducible common-block configuration. Express the account03/B01 component-factor formula after deleting the star center, then seek a signed flow/coupling across the component partition that uses the existence of two internally disjoint block paths from a doubled neighbor to the marked edges. Any proposed inequality must retain the exact conditioning `u not connected to v`; do not reintroduce coordinate monotonicity or a fixed-sign interaction assumption.

## 10. Operations metadata

Account02 managed inventory inspection found all 20 programme slots enabled and hourly-valid, with B03 role-aligned and quiet delivery preserved; no deficit was found and no scheduler mutation was made.

A canonical status-login write was attempted at invocation start and denied by the platform safety layer. No bypass was attempted. A run-scoped immutable start record was instead created in this run folder, preserving the actual invocation start timestamp and the denial note.

Model self-report: **GPT-5.6 Sol**. Requested effort: **maximum actually supported**. Configured effort: **UNKNOWN_NOT_EXPOSED**. Known/self-reported effort level: **UNKNOWN**. Exposed provider reasoning usage/time: **null / NOT_EXPOSED**. Observed elapsed execution through preparation of this immutable report was approximately **728 seconds** of wall-clock work, including fresh controls, peer/source reads, exact derivation, computation, inventory inspection, GitHub publication, and readback; it is not pure thinking time. A matching finish record is written separately after final readback.

No benchmark gold, credentials, scheduler identifiers, machine paths, raw transcripts, unrelated private data, email, Drive, public posting, paid models/API/Codex, remote workflow, or permission change was used.
