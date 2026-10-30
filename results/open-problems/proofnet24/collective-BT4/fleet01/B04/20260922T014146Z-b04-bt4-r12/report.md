# BT4 fleet01/B04 — exact-six companion amplification and support-entry ladders

Run: `20260922T014146Z-b04-bt4-r12`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Campaign: `BT4`  
Candidate: `BT4-MCR-v4-six-companion-ladder`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## Exact target and source boundary

The target remains the genuine k=4 Bermond--Thomassen statement: every finite loopless digraph with at most one arc per ordered pair and minimum outdegree at least seven contains four vertex-disjoint directed cycles. Digons are allowed in the target statement.

Fresh source check:
- Bessy--Muis--Sereni--Steiner--Wiederrecht, *A relaxation of the Bermond-Thomassen conjecture*, arXiv:2608.12948 (13 August 2026), still states that the genuine conjecture is unresolved for every k>=4; its threshold-(2k-1) theorem permits one reversed arc per cycle and therefore is not BT4.
- Lichiardopol--Pór--Sereni, *A Step toward the Bermond--Thomassen Conjecture about Disjoint Cycles in Digraphs*, SIAM J. Discrete Math. 23 (2009), 979--992, DOI 10.1137/080715792, proves both the k=3 minimum-outdegree-five theorem and the stronger k=2 input: outdegree at least three except at most two vertices of outdegree two forces two vertex-disjoint directed cycles.
- Lewandowski--Polcyn--Reiher, *Two disjoint cycles in digraphs*, J. Graph Theory 104 (2023), 461--469, arXiv:2205.10826, Theorem 1.4 characterizes outdegree sequences forcing two disjoint cycles via the paper's notion of a large sequence. I use only the explicit (r,s)=(1,2) specialization below.

No near-directed, edge-disjoint, tournament-only, finite-order, or larger-degree substitute is used.

## Exact team state consumed

Lead: fleet02/B04, `20260922T011943Z-b04-bt4-r11`, report commit `ca30763c69284b71c197ba0f49e37962f07e30c3`, blob `ee3294c169f9736cd8f0fdb943b5cefab5906a9e`. I use its exact-seven, oriented, arc-dominated, 3-vertex-strong normal form; its globally minimum-total three-cycle packing; the repaired path-fan inequality; equality-completion; and the off-pivot witness state.

Named OTHER-account partner actually applied: fleet02/B05, `BT4-RSC-v4-boundary-lift`, report commit `bddf6975e17279da0f57612c674f277146a6e871`, blob `2ea38c8ce3130b68fcce58e2b09fa32a8b6b37f4`. I adapt its repeated arc-domination ladder to a target lying on the support cycle rather than in the acyclic remainder.

Also compatible with fleet03/B05 `BT4-TCEX-v2-segment` (shared blob `372a194d54ba664dddae54e4d159ea6dd55e765b`) and fleet03/B04 `BT4-MENGER-COLLAR-v1` (shared blob `8a6ab560e2fe99d4e7637e0f529e8995f6597490`).

This run deliberately changes mechanism from fleet01/B04 `BT4-MCR-v3-dynamic-deficit`: instead of another contraction/neutral-orbit restatement, it uses deletion of the six-witness itself, the sharp two-cycle degree-sequence obstruction, and domination ladders.

## Inherited normal form

Assume BT4 false and work in the inherited minimum counterexample D with:

1. D oriented and d_D^+(v)=7 for every vertex;
2. (A,B,C) a three-cycle packing minimizing |A|+|B|+|C|;
3. R=V(D)\(A union B union C) nonempty and acyclic;
4. A,B,C chordless;
5. every arc is dominated: for every x->y, some q has q->x and q->y;
6. D is 3-vertex-strong.

For two packed cycles, say A,C, put H=D-(A union C)=D[B union R]. Then H contains no two vertex-disjoint directed cycles, since such two cycles together with A,C would be a four-packing.

The lead's remaining SIX closure explicitly includes a difficult cycle-supported `6-cross/0-R-exit` case. The next two lemmas show that this case cannot be an isolated six-witness.

## Lemma 1 — exact-six companion amplification

Let z in B satisfy

|N_D^+(z) intersect (A union C)|=6,   N_D^+(z) intersect R=empty.

Then one of the following useful alternatives occurs.

**(H5)** There is a vertex w in H-{z} with |N_D^+(w) intersect (A union C)|>=5.

**(C4)** There are at least four distinct vertices w in H-{z} with |N_D^+(w) intersect (A union C)|=4, at least three of those four satisfy w->z, and at least two of the three z-dominators lie in R.

### Proof

Because B is chordless and D is oriented, the only outgoing arc of z inside B is the support successor z^+. The zero-R-exit assumption and exact outdegree seven therefore give d_H^+(z)=1.

Assume (H5) fails. Then every w in H-{z} has d_H^+(w)>=3.

First delete z. The digraph H-z still has no two vertex-disjoint directed cycles. For every remaining vertex,

d_{H-z}^+(w)=d_H^+(w)-1_{w->z}>=2.

If at most two vertices of H-z had outdegree two, the Lichiardopol--Pór--Sereni k=2 theorem would force two disjoint cycles in H-z, impossible. Hence at least three distinct vertices w satisfy d_{H-z}^+(w)=2. Since d_H^+(w)>=3, every such vertex necessarily has d_H^+(w)=3 and w->z. Exact outdegree seven then gives exactly four arcs from each such w into A union C.

Among vertices of the chordless support cycle B, only the predecessor z^- can dominate z. Thus at most one of these three degree-three dominators lies on B, and at least two lie in R.

The 2023 degree-sequence theorem supplies one further companion. Let d_1<=...<=d_n be the outdegree sequence of H. Under failure of (H5), d_1=1 (at z) and d_2>=3. If this sequence were (1,2)-large in the sense of Lewandowski--Polcyn--Reiher, Theorem 1.4 would force two disjoint cycles in H. Therefore it is not (1,2)-large.

For r=1,s=2, the first largeness condition is already satisfied by d_1>=1,d_2>=3. Thus the second condition must fail. Its failure forces n>=5 and d_5=3 (and, additionally, no later index j>=6 has d_j>=j). Since d_2>=3,

d_2=d_3=d_4=d_5=3.

Hence at least four vertices other than z have residual degree three, equivalently pair-fan four into A union C. This proves (C4).

## What Lemma 1 changes

The exact cycle-supported six-witness with no R-exit is not a one-vertex dead end. Either the same deleted pair already has a second five-or-more witness, or it produces a four-vertex layer of fan-four companions, including two distinct remainder predecessors of the six-witness.

The fourth-companion conclusion uses the full degree-sequence theorem; the stronger fact that three companions point directly to z comes from deleting z and applying the older k=2 theorem.

## Lemma 2 — support-entry domination ladder

Let z in B and u in R with u->z. Then there is a directed path

s=q_t -> q_{t-1} -> ... -> q_0=u -> z

such that q_0,...,q_{t-1} are in R; every q_i, including s=q_t, also has the direct arc q_i->z; and the packed apex satisfies s in A union C union {z^-}.

### Proof

This is the partner's domination-ladder mechanism with the target moved from R onto the support cycle. Start with q_0=u. While q_i is in R, domination of the arc q_i->z gives q_{i+1}->q_i,z. As long as the vertices remain in R, they are distinct: a repetition would close a directed cycle along the predecessor chain inside acyclic R. Finiteness forces eventual exit from R, hence the first outside vertex lies on A union B union C. It dominates z. Chordlessness and orientation of B imply that the only vertex of B that can dominate z is z^-.

## Corollary 3 — every remainder companion feeds the existing cross/exchange machinery

Assume alternative (C4) of Lemma 1 and let u in R be one of its z-dominating fan-four companions. Apply Lemma 2, with apex s. There are only three possibilities.

1. **Genuine cross-packed transition avoiding z.** If s=z^-, choose any a in N^+(u) intersect (A union C). Then z^- -> R -> u -> a is a B-to-(A or C) transition whose internal vertices lie in R and which does not use z. If s in A and u has any outneighbor on C, the ladder followed by that arc is an A-to-C transition. The symmetric statement holds with A,C exchanged.

2. **Fan-four equality exchange.** Suppose s in A and u has no outneighbor on C. Since u has four pair-fan arcs, all four hit A. The ladder segment from A to u is R-internal. The lead's repaired path-fan lemma with m=4 gives length L>=3. If L=3, the lead's equality-completion principle yields an explicit size-neutral globally minimum packing exchange.

3. **Strict fan-four collar.** In the same pure-return case, if equality does not occur then L>=4. This is a strict R-collar attached to a fan-four remainder witness. Again the C case is symmetric.

Therefore the two guaranteed remainder companions from Lemma 1 each produce a concrete cross transition, a neutral exchange, or a strict fan-four collar. Their ladders need not be disjoint; no disjointness is silently inferred.

## Corollary 4 — exact interaction when two companion ladders overlap

Let u,v in R be two distinct z-dominating companions from Lemma 1 and choose domination ladders as in Lemma 2.

If the two ladder interiors are disjoint, they give two separately supported instances of Corollary 3.

If they overlap, take the last common vertex q before their suffixes toward u and v separate. The union contains two directed suffixes from q toward the two companion branches (unless one companion lies on the other ladder, in which case the nesting itself gives a directed shortcut), and in every case q->z is also present. Thus overlap is not an unstructured failure: it becomes the same common-apex/coalescence geometry isolated by fleet02/B05 in `BT4-RSC-v4-boundary-lift`.

This does not by itself give the second opposite vertex-disjoint crossing. It identifies the exact residual obstruction.

## Updated conditional end-to-end argument

The lead's current proof has three named closures: SIX, cross-linkage, and long neutral orbit. The present step narrows the hardest corrected exact-six subcase.

Assume a minimum counterexample and a pair {A,C} has a cycle-supported exact-six witness z in B with zero R-exit.

- If Lemma 1 gives (H5), the SIX branch has at least two same-pair high-cross witnesses rather than one.
- Otherwise it gives four fan-four companions, including two distinct remainder predecessors u,v->z.
- Lemma 2 and Corollary 3 send each of those two companions directly into the already-live cross / equality-exchange / strict-collar interfaces.
- Equality moves to another globally minimum packing, where the lead's universal pair deficits regenerate.
- A strict undercut, if produced by the partner's segment/linkage exchange, contradicts global packing minimality.
- The only genuinely unpaid local obstruction is now simultaneous coalescence/disjointness: the two companion routing objects may overlap in precisely the common-apex form, and a single cross-pair does not preserve two cycles.

Thus the old label `6-cross/0-R-exit` no longer describes an isolated terminal configuration. It either has high-witness multiplicity or forces two R-supported companion routing objects.

## First essential missing implication

The next exact statement to prove is:

**Companion coalescence closure.** In the inherited exact-seven normal form, for a cycle-supported exact-six witness z in B with zero R-exit and with no second same-pair five-or-more witness, let u,v in R be the two fan-four predecessors guaranteed above. The two support-entry ladders and their fan-four exits must force either (i) two suitably opposite vertex-disjoint crossings enabling a legal two-cycle splice, (ii) a strict packing reduction, or (iii) a directed cycle in the exchanged remainder. Equivalently, the common-apex/nested coalescence configurations from Corollary 4 cannot all persist without triggering one of those outcomes.

This is strictly narrower than "close the SIX branch": the isolated-witness and no-R-interface loopholes have been removed. It also matches the named partner's current first unpaid issue, namely obtaining the second disjoint crossing before lifted paths coalesce.

## Failure audit and boundary cases

- The proof uses the oriented minimum-counterexample normal form; it does not exclude digons from the original BT4 statement.
- H=D-(A union C) has no two disjoint cycles for the exact reason that two such cycles plus A,C would give four. No edge-disjoint substitute is used.
- The degree-three companions are distinct vertices. Only two are guaranteed to lie in R; the fourth companion from the degree-sequence theorem need not dominate z.
- Corollary 4 does not claim overlapping ladders are internally disjoint or already form a splice.
- A single cross transition, or one opposite cross-pair, is not counted as two replacement cycles.
- No claim is made here for an arbitrary seven-cross witness. The new structural closure is specifically the lead's corrected cycle-supported exact-six, zero-R-exit subcase.
- No computation was used. The result is analytic and source-bound.
- Full BT4 remains open.

## Honest status

`ESSENTIAL_STEP_APPLIED`.

A named separate obstruction in the lead's SIX closure has been reduced to high-witness multiplicity or two concrete remainder-supported companion routing objects. The remaining obstacle is their disjointness/coalescence, not absence of an R-interface.
