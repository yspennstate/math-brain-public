# POS3 fleet03/B11 — a width-saturating three-antichain gate must export through two disjoint Hasse channels

**Run:** `20260922T071406Z-fleet03-B11-pos3-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all full linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every count below is a literal count of full linear extensions of the original poset. No deletion-induced ordering is treated as uniform.

## 1. Fresh collective state used

The exact fleet03/B11 assignment is the distinct order-polytope/correlation route, partnered with **fleet04/B19**.

The required named other-account partner result consumed is fleet04/B19 r45:

- `proofnet24/collective-POS3/fleet04/B19/B19-20260922T061559Z-r45/REPORT.md`
- Git blob `7e142965f79f76b8a3ffb05da2c82080fbae50d2`.

Its essential contribution is the canonical-fringe reduction for the live heavy-cover state: every failed adjacent position swap can be charged to one of at most three canonical Hasse blockers on each side, with no strong-majority span descent placing those blockers on the outer rays. Its remaining obligation is **CANONICAL-FRINGE REUSE ACYCLICITY**.

The latest complete team-lead result used is fleet04/B10 r16:

- `proofnet24/collective-POS3/fleet04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`.

R16 losslessly re-anchors heavy-cover defect marks to fully outward actual incomparable pairs. In its low-endpoint branch it produces two distinct outward packets. If two selected packets land on the same ray, their blocker vertices are either comparable (a nested-channel case) or incomparable, in which case the boundary endpoint and those two blockers form a width-saturating three-element antichain. The latter is the branch attacked here.

Because several preceding B11 runs used two-point heavy-cover swap flux, this run deliberately changes mechanism: instead of iterating the same cover calculation, it works in the **six permutation chambers of a three-antichain** and uses two simultaneous adjacent coordinate transpositions of the order polytope.

## 2. Three-antichain chamber setup

Let `P` have width at most three and let `a,b,c` be pairwise incomparable. Write `E=e(P)` for the total number of full linear extensions and

`N(uvw) = #{L : u precedes v precedes w in L}`

for a displayed relative order of these three vertices. Assume the two adjacent majority orientations are strong:

`N(a<b) > 2E/3`,  `N(b<c) > 2E/3`.                         (2.1)

Put

`H = N(abc) = N(a<b<c)`.

Because `{a<b}` and `{b<c}` intersect exactly in the chamber `abc`, inclusion-exclusion gives

`H >= N(a<b)+N(b<c)-E > E/3`.                              (2.2)

This is an exact full-extension multiplicity statement. In the order-polytope picture, the chamber `abc` therefore has more than one third of the total normalized volume.

## 3. Two exact adjacent-swap deficits

For an extension `L` in the `abc` chamber, swap the **positions** of `a,b`, leaving all other positions fixed. Since `a||b`, every valid swap lands in the `bac` chamber, and the operation is injective on the valid subset. Let `B_ab` be the extensions of the `abc` chamber for which this position swap is invalid. Then

`|B_ab| = H - (# valid a<->b swaps) >= H - N(bac)`.        (3.1)

But `N(bac) <= N(b<a) < E/3`, so

`|B_ab| > H-E/3 > 0`.                                       (3.2)

Likewise, swapping the positions of `b,c` sends every valid swap injectively into the `acb` chamber. If `B_bc` is its bad-swap set, then

`|B_bc| >= H-N(acb) > H-E/3 > 0`.                           (3.3)

Thus a strong-majority three-antichain cannot be supported by a single local obstruction: **both adjacent chamber walls have positive exact swap-defect mass**.

## 4. Canonical Hasse compression on each wall

For the wall `(a,b)` define

`T_ab = Max{t : t<b and t||a}`,
`U_ab = Min{u : a<u and u||b}`,
`C_ab = T_ab union U_ab`.

For `(b,c)` define

`T_bc = Max{t : t<c and t||b}`,
`U_bc = Min{u : b<u and u||c}`,
`C_bc = T_bc union U_bc`.

### Lemma 4.1 — Hasse and width bounds

Every member of `T_ab` is a lower cover of `b`, every member of `U_ab` is an upper cover of `a`, and the dual statements hold for `T_bc,U_bc`. Moreover

`|T_ab|,|U_ab|,|T_bc|,|U_bc| <= 2`,                         (4.1)

so each canonical wall has at most four vertices.

**Proof.** If `t in T_ab` and `t<z<b`, then `z<a` would imply `t<a`, while `a<z` would imply `a<b`; both contradict the defining relations. Hence `z||a`, contradicting maximality of `t`. So `t lessdot b`. The other Hasse assertions are dual. Members of `T_ab` are pairwise incomparable and all incomparable with `a`, so `{a} union T_ab` is an antichain; width three gives `|T_ab|<=2`. The other bounds are identical. `square`

### Lemma 4.2 — exact canonical blocker characterization

For `L` in the `abc` chamber, the `a<->b` position swap is invalid iff some member of `C_ab` occurs strictly between `a` and `b` in `L`. The analogous statement holds for `b<->c` and `C_bc`.

**Proof.** A position swap of incomparable `a,b` can fail only because an intervening vertex `v` must stay after `a` (`a<v`) or must stay before `b` (`v<b`). In the first case `v||b` (otherwise transitivity would force `a<b`); choose a minimal member of `{u:a<u,u||b}` below `v`. In the second case `v||a`; choose a maximal member of `{t:t<b,t||a}` above `v`. This produces an intervening canonical member. The converse is immediate from the required relation. `square`

This compression is lossless and uses no probability approximation.

## 5. New disjointness theorem for the width-saturating gate

### Theorem 5.1 — the two adjacent canonical blocker families are disjoint

For a three-element antichain `{a,b,c}`,

`C_ab cap C_bc = emptyset`.                                  (5.1)

**Proof.** An element of `T_ab` is comparable with `b` (`t<b`), whereas an element of `T_bc` is incomparable with `b` and an element of `U_bc` lies above `b`; hence `T_ab` meets neither component of `C_bc`. An element of `U_ab` is incomparable with `b`, so it cannot lie in `U_bc`, whose members satisfy `b<u`. The only remaining formal overlap would be `r in U_ab cap T_bc`, which would give `a<r<c`; transitivity would then imply `a<c`, contradicting that `{a,b,c}` is an antichain. `square`

This is the key recycling improvement: **the two positive bad-swap masses (3.2)-(3.3) cannot be absorbed by one reused canonical vertex at the three-antichain gate.** They must leave through two disjoint Hasse frontiers.

Assign each bad `a<->b` extension deterministically to its first intervening member of `C_ab`; define weights `lambda_r`. Assign `b<->c` bad extensions similarly with weights `rho_s`. Then

`sum lambda_r = |B_ab|`, `sum rho_s = |B_bc|`,               (5.2)

and because each side has at most four channels, there exist **distinct** `r in C_ab`, `s in C_bc` such that

`lambda_r > (H-E/3)/4`,
`rho_s    > (H-E/3)/4`.                                      (5.3)

These are exact integer incidence weights inside full extensions, not surrogate probabilities.

## 6. No-span polarity turns the two channels into outward minority pairs

Now specialize to the minimal-counterexample regime used by the collective proof. With no balanced incomparable pair, define `u prec_* v` when the uniform full-extension probability of `u<v` exceeds `2/3` (and use the deterministic order for comparable pairs). The usual union bound shows this is transitive: if `u prec_* v prec_* w`, then `Pr(u<w)>1/3`; no-balance excludes the opposite strong orientation. Thus `prec_*` is a strict total order.

Assume

`a prec_* b prec_* c`                                        (6.1)

and that strict strong-majority span descent has already been exhausted inside the two adjacent intervals `[a,b]_*` and `[b,c]_*`, as in the live lead branch.

Then every canonical blocker points outward:

- `t in T_ab` satisfies `t prec_* a`; its bad-swap mark has `a<t`, the minority orientation of `(t,a)`;
- `u in U_ab` satisfies `b prec_* u`; its mark has `u<b`, the minority orientation of `(b,u)`;
- `t in T_bc` satisfies `t prec_* b`; its mark has `b<t`, the minority orientation of `(t,b)`;
- `u in U_bc` satisfies `c prec_* u`; its mark has `u<c`, the minority orientation of `(c,u)`.

For example, `t in T_ab` has `t<b` in the poset. If instead `a prec_* t`, then `a prec_* t prec_* b` and the incomparable pair `(a,t)` is a strict subspan, contrary to the branch hypothesis. The other cases are identical/dual.

Combining with (5.3): unless a strict span descent has already occurred, the width-saturating three-antichain gate exports **two distinct outward actual incomparable-pair channels**, one through each adjacent chamber wall, and each receives more than `(H-E/3)/4` marked full extensions. In particular, the two packets cannot immediately merge into one canonical recycler.

## 7. Application to lead r16 and partner r45

Lead r16 leaves, when two boundary packets select the same ray, exactly two local geometries:

1. comparable blocker vertices: a nested channel;
2. incomparable blocker vertices: the boundary endpoint plus those blockers form a three-antichain.

Theorem 5.1 plus Section 6 pays the second branch of that local dichotomy. Relabel the three-antichain in its `prec_*` order as `a prec_* b prec_* c`. Its majority chamber has `H>E/3`; if neither adjacent interval gives the desired strict span descent, the gate necessarily creates two **disjoint** outward canonical Hasse frontiers. Thus a same-ray width-saturating gate is not a terminal recycler and cannot send both adjacent defect masses through a single old vertex.

This is directly compatible with fleet04/B19 r45: r45 reduced diffuse blocker mass to bounded canonical fringes and asked for canonical-fringe reuse acyclicity. The present result removes one concrete reuse mechanism: **coalescence across the two adjacent walls of a saturated three-antichain is impossible before the next generation.**

What remains is not hidden: the comparable/nested-channel branch and reuse of vertices introduced in *different generations* can still occur. The global POS3 theorem therefore remains open.

## 8. Exact deterministic regression and calibration

`verify_pos3_three_antichain_gate.py` exhausts every distinct naturally labelled transitive closure through six vertices, retains width at most three, and for every ordered antichain chamber verifies:

- each canonical extremal set has size at most two;
- the two adjacent canonical wall sets are disjoint;
- a bad adjacent position swap occurs iff a canonical blocker intervenes.

It checked 47,832 ordered antichain chambers at `n=6`, with 102,326 bad-swap occurrences on each adjacent side, and terminated with

`POS3_THREE_ANTICHAIN_GATE_CHECK_PASS`.

A separate exact seven-element calibration has covers

`0<2, 0<4, 0<6, 1<4, 1<5, 1<6, 2<5, 3<4, 3<5`.

For `(a,b,c)=(3,2,6)` it has exactly `E=124` extensions and

`N(a<b)=90`, `N(b<c)=90`, `H=N(a<b<c)=60`,
`N(b<a<c)=24`, `N(a<c<b)=24`,
`|B_ab|=|B_bc|=36`.

Its canonical wall sets are disjoint: `C_ab={0,4}`, `C_bc={1,5}`. Thus the exact inequalities in Section 3 are attained with equality in this calibration (`36=60-24`). This example contains balanced pairs and is **not** a POS3 counterexample; it only certifies the chamber accounting is nonvacuous and sharp at that local step.

Verifier SHA-256: `5867ac4b3120c8fb561ff7c4acc413f50a7884c62d86940ebcc6deb0b9d314f6`.  
Captured stdout SHA-256: `d9169d9d5cbebc4294fefcc869b2b3c52dbd8e40b88413ecb215a7ebe00dec95`.

## 9. Remaining first implication

**NESTED-CHANNEL / INTERGENERATION REUSE.** In the live minimal-counterexample branch, use the exact outward Hasse channels from r16/r45 and this three-antichain export theorem to show that a sequence of comparable same-ray nested channels cannot later reuse an older blocker vertex across generations without forcing one of:

1. a balanced pair;
2. strict `prec_*` span descent;
3. a four-antichain;
4. a proper autonomous/ordinal reduction; or
5. a charged non-crossed multi-distinguisher exit.

The width-saturating three-antichain branch no longer has an immediate one-vertex coalescence loophole. The nested branch is now the first local recycling mechanism still unpaid.

## 10. Claim ledger

- fleet04/B19 r45 canonical-fringe compression: **CONSUMED/APPLIED**;
- fleet04/B10 r16 outward boundary-anchor recoding and same-ray dichotomy: **CONSUMED/APPLIED**;
- exact three-antichain majority chamber mass `H>E/3`: **PROVED**;
- two exact adjacent-swap deficit bounds: **PROVED**;
- Hasse compression of both walls: **PROVED**;
- disjointness of the two canonical wall families: **PROVED**;
- no-span outward minority recoding: **PROVED**;
- same-ray three-antichain immediate coalescence loophole: **ELIMINATED**;
- nested-channel/intergeneration recycling termination: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- run classification: **ESSENTIAL_STEP_APPLIED**.

No novelty or priority claim is made. Scoped privacy review: this report contains only mathematics, repository-relative scientific provenance, nonsecret run labels and content hashes; no benchmark material, credentials, scheduler identifiers, email/Drive content, machine paths, or unrelated private transcripts are included.
