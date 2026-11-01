# POS3 fleet01/B10 — cross-anchor PQD fails, and overlap-only amplification has a 2-sqrt(3) ceiling

**Outcome:** `CANDIDATE_REFUTED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run continues `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`. It does no installation or benchmark work. All probabilities below use the uniform law on the full set of linear extensions of the original poset.

## 1. Exact collective state consumed

The latest complete campaign-lead report consumed is

- **fleet04/B10**, `proofnet24/collective-POS3/fleet04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`, blob `50bac494667235f3630991a512438eac42c30521`.

It proves that the lead bridge in the majority-late strict corridor contains a cover `x lessdot y` with an incomparable point `a` such that

`Pr(x<a<y)>1/3`,

and that this heavy cover must export through at least two distinct external relation-distinguisher channels in a hypothetical counterexample. Its unpaid step is global recycling/realization of those channels.

The assigned **OTHER-account partner** result consumed and applied is

- **fleet02/B11**, `proofnet24/collective-POS3/fleet02/B11/20260922T055456Z-b11-pos3-r16-7136730f/REPORT.md`, blob `09ccf73a03359bcc0545abff5a8a5bc79cc2f42d`.

For an incomparability leaf `x` with unique incomparable neighbor `b`, it proves the exact splice

`N_P(b<x)=e(L)e(U)`, `N_P(x<b)=e(D)e(R)`,

and shows that in a series-indecomposable no-balanced candidate, a majority-facing nonempty chain side is impossible. Thus the only surviving nonboundary leaf state has a genuinely nonchain majority-facing side. This is used below to identify what kind of structural information must replace the correlation-only route refuted in this report.

The immediately preceding same-slot result is

- **fleet01/B10**, `proofnet24/collective-POS3/fleet01/B10/20260922T045216Z-fleet01-B10-pos3-r11/REPORT.md`, blob `7ab3502e574d795c8300fd0ec70dc33f12b87f0a`.

For a strict nested endpoint `a||b` with `Pred(b) subseteq Pred(a)`, fleet02/B11's canonical reverse-channel compression gives

`T=Max(Pred(a)\Pred(b))`, `U=Min{z:b<z and z||a}`,

with `|T|,|U|<=2`, and the reverse remainder is exactly

`R/E = Pr(A_T union B_U)`,

where

`A_T = union_{t in T}{b<t}`, `B_U = union_{u in U}{u<a}`.

Writing `p=Pr(a<b)`, the endpoint exchange identity gives

`R/E >= 1-2p`.

The same-slot exact three-chain flux theorem gives positive association *within* either same-anchor two-channel group and hence, if every atomic channel is at most `c`,

`Pr(A_T)<=F_|T|(c)`, `Pr(B_U)<=F_|U|(c)`,

where `F_0(c)=0`, `F_1(c)=c`, `F_2(c)=2c-c^2`.

The previous report deliberately left cross-anchor correlation unsupported. This run tests that missing implication directly.

## 2. Compact conditional route and the candidate tested

In the inherited no-balanced majority-late/no-span-descent branch,

`p=Pr(a<b)<1/3`,

and every canonical reverse channel satisfies

`Pr(b<t)<1/3` for `t in T`, `Pr(u<a)<1/3` for `u in U`.

The tempting next step is to extend the same-anchor TP2/Fishburn-Shepp positivity across the two anchors and assert, for every `t in T`, `u in U`,

`Pr(b<t and u<a) >= Pr(b<t) Pr(u<a)`.                 (2.1)

If true, (2.1) would permit systematic overlap subtraction between the predecessor and successor reverse-channel groups.

**Result of this run:** (2.1) is false even for a width-three, series- and parallel-indecomposable poset satisfying all of the local nested-endpoint inequalities above. Therefore same-anchor TP2 cannot simply be iterated across anchors. Any valid continuation must use additional global no-balanced/corridor information, or a structurally different invariant.

This is consistent with the classical literature: Fishburn-Shepp gives same-anchor positive correlation for three mutually incomparable elements, while Winkler's universal-correlation work shows that plausible ordering-event correlations outside such protected configurations need not be universally nonnegative. No literature claim is used as a substitute for the exact counterexample below.

## 3. Exact width-three counterexample to cross-anchor PQD

Let `P_0` be the ten-element poset on `{0,...,9}` with Hasse covers

`0<1, 0<3, 0<4,`

`1<5, 1<7,`

`2<3, 2<5,`

`3<6,`

`4<8, 4<9,`

`5<8,`

`6<7,`

`7<9`.

Its transitive closure is exactly the relation set encoded in the verifier accompanying this report. Exact subset dynamic programming gives

`e(P_0)=461`,

and the width is exactly three; for example `{4,5,7}` is an antichain. Both the comparability graph and the incomparability graph are connected, so this witness is not an ordinal-sum or parallel-sum artifact.

Choose

`a=5`, `b=4`.

Then `a||b`,

`Pred(a)={0,1,2}`, `Pred(b)={0}`,

so

`D=Pred(a)\Pred(b)={1,2}`, `T={1,2}`.

Moreover

`S={z:b<z and z||a}={9}`, `U={9}`.

Thus this is exactly the canonical nested-endpoint state used by the current reverse-channel compression. The exact endpoint and channel counts are

`N(a<b)=136`,

`N(b<1)=152`,

`N(b<2)=61`,

`N(9<a)=39`.

All four normalized probabilities are strictly below `1/3`, because

`3*136=408<461`,

`3*152=456<461`,

`3*61=183<461`,

`3*39=117<461`.

Hence the local strong-majority/no-span inequalities are all present:

`b prec_* a`, `1 prec_* b`, `2 prec_* b`, `a prec_* 9`.

Now select the cross-anchor pair

`A={b<2}`, `B={9<a}`.

Exact counting gives

`N(A)=61`, `N(B)=39`, `N(A intersect B)=5`.

Therefore

`N(A intersect B)e(P_0)-N(A)N(B)`

`=5*461-61*39`

`=2305-2379`

`=-74<0`.                                             (3.1)

Equivalently,

`Pr(A intersect B) < Pr(A)Pr(B)`.

So the cross-anchor PQD claim (2.1) is rigorously false under the exact local hypotheses of the current corridor endpoint.

The witness is **not** a POS3 counterexample. For example `(0,2)` has ordering counts `293` and `168`, both between `461/3` and `2*461/3`; the exact verifier records additional balanced pairs. Thus (3.1) refutes only the proposed correlation lemma, not the parent theorem.

The witness also has a two-element autonomous chain `{3<6}`. This does not make (3.1) irrelevant: the campaign has not proved a fixed-endpoint autonomous-chain lifting theorem, and the lead's latest report gives an explicit width-two counterexample showing that quotient balance may require migration of the outside endpoint. The present witness is additionally series- and parallel-indecomposable.

## 4. Exact algebraic ceiling for the entire overlap-only route

There is a second, independent obstruction. Even if one *grants the strongest possible cross-group overlap* rather than merely positive correlation, the scalar reverse-union argument still cannot reach `1/3` in a persistent two-channel state.

Assume all endpoint/channel minority probabilities are at most `c`. Same-anchor TP2 gives

`Pr(A_T)<=F_m(c)`, `Pr(B_U)<=F_n(c)`,

where `m=|T|`, `n=|U|`, and `F_2(c)=2c-c^2`.

For the worst persistent case with a two-channel group, suppose optimistically that the two cross-anchor group events overlap perfectly, so that the union obeys the strongest conceivable bound obtainable from those group sizes alone:

`r:=Pr(A_T union B_U) <= F_2(c)=2c-c^2`.              (4.1)

The endpoint identity supplies only

`r >= 1-2p >= 1-2c`.                                  (4.2)

Thus this style of argument yields a contradiction only while

`1-2c > 2c-c^2`.

The equality threshold is

`c^2-4c+1=0`,

so the smaller root is

`c_* = 2-sqrt(3) = 0.2679491924311227...`.             (4.3)

At and above this scale the scalar constraints (4.1)-(4.2) are compatible. In particular, even *perfect* predecessor/successor group overlap cannot push this method from `2-sqrt(3)` all the way to `1/3`.

This is a method ceiling, not a poset construction saturating every inequality. Its logical consequence is important: proving stronger cross-group covariance alone cannot finish POS3 through the present endpoint identity. A closing argument must add a new structural relation that changes the channel count/state, links the forward common-blocker term to the reverse groups, or forces descent/reduction/balance.

This explains why the preceding same-slot run already attained `2-sqrt(3)` in a pure double-fan: that constant is the natural ceiling of the channel-union scalar mechanism once a two-channel group remains.

## 5. Application of the assigned partner result and revised first missing implication

The new fleet02/B11 leaf-splice theorem removes the easiest possible structural escape: in a series-indecomposable no-balanced candidate, an incomparability leaf cannot have a majority-facing **nonempty chain** side. Any surviving leaf has an empty or genuinely nonchain majority-facing side.

Combining that partner theorem with Sections 3-4 gives a sharper global obligation:

> **Structural two-channel collapse / transport.** In a cardinality-minimal width-three no-balanced core, show that a persistent canonical state with a two-channel reverse group cannot pass through the lead's heavy-cover/two-witness corridor and the partner's nonchain leaf-splice residue without one of the following occurring: (i) one canonical group collapses to a single channel, (ii) a balanced pair appears, (iii) strict strong-majority span descent occurs, or (iv) a proper ordinal/autonomous reduction with a proved balance-transfer rule occurs.

The key point is that the missing theorem must genuinely use the *history/structure* of the corridor or the global no-balanced hypothesis. It cannot be replaced by an unconditional cross-anchor positive-correlation statement, and even an ideal overlap statement would not by itself reach `1/3`.

A second potentially viable direction is to relate the forward common-blocker count `Q` in

`p=1-(Q+R)/(2E)`

directly to the reverse-channel state, rather than discarding `Q` via the crude bound `Q<=E`. Such a relation would add information not present in the overlap-only ceiling calculation.

## 6. Exact certificate

The deterministic verifier in this run uses only integer subset dynamic programming. It checks the transitive closure, width, extension count, canonical sets, all exact counts in Section 3, the negative covariance numerator `-74`, connected comparability/incomparability graphs, and the existence of balanced pairs in the witness.

Files:

- `verify_cross_anchor_pqd.py`, locally executed SHA-256 `b1e4bc4ba6958a7d6229c1b657a2affaa87b02d5be2ee1fc8be93f97d4f0f5fa`;
- `verify_cross_anchor_pqd.out`, locally captured-output SHA-256 `f9d1b8da0fa148ba4d5bd723bb58b1f24dcf285ff714794a2fb3299941b4252c`.

Terminal marker:

`POS3_CROSS_ANCHOR_PQD_COUNTEREXAMPLE_PASS`.

The computation is a certificate for the finite counterexample to the auxiliary correlation lemma, not finite evidence for or against the universal POS3 target.

## 7. Public mathematical references

- P. C. Fishburn, *A correlational inequality for linear extensions of a poset*, Order 1 (1984), 127-137.
- L. A. Shepp, *The XYZ conjecture and the FKG inequality*, Annals of Probability 10 (1982), 824-827.
- P. M. Winkler, *Correlation among partial orders*, SIAM Journal on Algebraic and Discrete Methods 4 (1983), 1-7, DOI 10.1137/0604001.
- S. H. Chan and I. Pak, *Linear extensions of finite posets*, EMS Surveys in Mathematical Sciences (2025), DOI 10.4171/EMSS/97.

These references establish the surrounding correlation framework; the exact witness and ceiling calculation in this report are checked directly.

## 8. Status

- Parent POS3 target: **OPEN / NOT PROVED**.
- Same-anchor exact full-extension TP2/PQD: **retained**.
- Pairwise cross-anchor PQD for canonical predecessor/successor channels under the current local endpoint hypotheses: **REFUTED** by the exact ten-element witness.
- Overlap-only scalar amplification to `1/3`: **IMPOSSIBLE within the current `r>=1-2p` plus `F_2(c)` information; ceiling `2-sqrt(3)`**.
- Latest fleet02/B11 leaf-splice reduction: **CONSUMED/APPLIED**.
- Revised first essential obligation: **structural two-channel collapse/transport or a new `Q`-to-reverse-state inequality**.
- Honest outcome: `CANDIDATE_REFUTED`.

No benchmark work, brain-installation work, scheduler mutation, email/Drive action, public posting, paid/remote model call, workflow dispatch, permission change, benchmark gold, credentials, scheduler identifiers, machine paths, or unrelated private data were used.
