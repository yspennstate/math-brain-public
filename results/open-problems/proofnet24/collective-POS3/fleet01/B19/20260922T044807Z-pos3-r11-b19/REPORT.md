# POS3 fleet01/B19 — exact three-chain flux recurrence and a cover two-witness theorem

**Run:** `20260922T044807Z-pos3-r11-b19`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

This run performs no installation or benchmark work. It uses only the actual uniform law on the full linear-extension set of the poset; no deletion projection is renamed uniform.

## 1. Exact state consumed

The latest complete campaign-lead report consumed is

- fleet04/B10, `proofnet24/collective-POS3/fleet04/B10/20260922T041420Z-B10-POS3-r13/REPORT.md`, blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`.

Its unified strict-chain terminal selector proves that, once internal strong-majority span descent is exhausted in the delayed-predecessor corridor, a canonical incomparable pair has minority probability in `(1/6,1/3)`. In the small-minority branches a two-Hasse-blocker fork is forced. Its first unpaid step is a global amplification/charge theorem: upgrade the `1/6` selector to the target `1/3`, or prove that repeated bridged two-cover forks cannot propagate indefinitely through the three-chain corridor.

The required named **OTHER-account partner** input is

- fleet02/B10, `proofnet24/collective-POS3/fleet02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`, blob `e91498f0bb8e28f23aa1cada24e131c27182e0ff`.

Its Theorem 4.1 proves, by exact deletion-fiber multiplicities, that an incomparable pair having exactly one relation-distinguisher is automatically balanced. Consequently every incomparable pair in a hypothetical counterexample has at least two distinguishers. The two-distinguisher threshold is sharp as a local statement.

The immediate fleet01/B19 predecessor is

- `proofnet24/collective-POS3/fleet01/B19/20260922T034906Z-b19-pos3-r12/REPORT.md`, blob `dd68f31ee0dcf9a8fa08024062a5bc67b73fb77a`.

That run used a cross-skeleton covariance decomposition. The present run deliberately changes mechanism: it works with exact three-chain path flux and a cover-local fiber classification.

## 2. Compact conditional end-to-end route

Assume, for contradiction, a cardinality-minimal width-at-most-three counterexample `P` with no balanced pair. Fix a three-chain cover. The lead state reduces the hard first-fork geometry, after span descent is exhausted, to repeated cover/blocker corridors carrying nontrivial minority mass.

The desired end-to-end route is now:

1. encode the uniform extension law as exact forward/backward flow on the three-chain ideal lattice;
2. identify a strong probability flip across a cover with a single lattice-edge flux exceeding `1/3`;
3. prove that such a heavy edge cannot be supported by only one external asymmetry channel;
4. charge the at-least-two forced channels to distinct third-chain or next-fork transitions;
5. show that indefinite reuse of the same channels forces either a balanced pair, a width-four antichain, an excluded autonomous nonchain, or a strict majority-span descent.

Steps 1--3 are paid below. Step 4 is the new first essential missing implication.

## 3. Exact three-chain forward/backward recurrence

Let

`A={a_1<...<a_r}`, `B={b_1<...<b_s}`, `C={c_1<...<c_t}`

be a chain partition of `P`. A state `(i,j,k)` represents the prefix

`A_i union B_j union C_k`.

Call the state feasible exactly when that prefix is an order ideal of `P`.

Define `F(i,j,k)` as the number of feasible monotone paths from `(0,0,0)` to `(i,j,k)`. Then

`F(0,0,0)=1`,

and, away from the origin,

`F(i,j,k)=1_feas(i,j,k) [F(i-1,j,k)+F(i,j-1,k)+F(i,j,k-1)]`,        (3.1)

with negative-index terms zero.

Likewise define `G(i,j,k)` as the number of feasible monotone suffix paths from `(i,j,k)` to `(r,s,t)`. Then

`G(r,s,t)=1`,

`G(i,j,k)=1_feas(i,j,k) [G(i+1,j,k)+G(i,j+1,k)+G(i,j,k+1)]`,        (3.2)

with out-of-range terms zero.

Every linear extension is exactly one feasible path and vice versa, so

`E:=e(P)=F(r,s,t)=G(0,0,0)`.                                     (3.3)

### Proposition 3.1 — exact pair-order flux

For incomparable `a_p,b_q`,

`N(a_p<b_q) = sum_{j=0}^{q-1} sum_{k=0}^t F(p-1,j,k) G(p,j,k)`,     (3.4)

where a summand is understood as zero unless the edge

`(p-1,j,k) -> (p,j,k)`

is feasible. Dually,

`N(b_q<a_p) = sum_{i=0}^{p-1} sum_{k=0}^t F(i,q-1,k) G(i,q,k)`.     (3.5)

#### Proof

In a path corresponding to a linear extension, start inside the rectangle `i<p,j<q`. The first exit is unique. If `a_p` occurs before `b_q`, the first exit is through exactly one `A`-edge `(p-1,j,k)->(p,j,k)` with `j<q`; conversely every full path through one such edge has `a_p<b_q`. The number of full paths through that edge factors as forward count times backward count, `F(p-1,j,k)G(p,j,k)`. Summing the disjoint edge events proves (3.4). Equation (3.5) is symmetric. `square`

### Corollary 3.2 — gap-flux identity

Suppose consecutive chain elements `a_p<a_{p+1}` are both incomparable with `b_q`. Then

`N(a_p<b_q)-N(a_{p+1}<b_q)`
` = N(a_p<b_q<a_{p+1})`
` = sum_{k=0}^t F(p,q-1,k)G(p,q,k)`.                              (3.6)

Hence, after division by `E`, the probability drop across one `A`-gap is literally the total normalized `B`-edge flux across the line `(p,q-1,k)->(p,q,k)`.

More generally define

`Phi_p(b_q) := E^{-1} sum_k F(p,q-1,k)G(p,q,k)`                  (3.7)

for the successive `A`-gaps. Then

`sum_p Phi_p(b_q)=1`,                                            (3.8)

because every extension places `b_q` in one unique `A`-gap, and

`Pr(a_i<b_q)=sum_{p>=i} Phi_p(b_q)`.                              (3.9)

This is the requested chain-insertion/deletion bookkeeping in a global form: every bias caused by deleting or conditioning on a chain is retained as exact path multiplicity. There is no appeal to a uniform induced law.

## 4. A tempting amplification shortcut is false

One might hope that width three alone forbids a single cover gap carrying more than `1/3` of the extension mass. That is false already on five elements.

Take the poset on `{0,1,2,3,4}` with cover relations

`0<2, 0<3, 1<2`,

and no other generators. Let

`x=0`, `y=2`, `b=4`.

Then `x lessdot y`, and `b` is incomparable with both. Exact enumeration gives

`E=25`,
`Pr(x<b)=18/25>2/3`,
`Pr(y<b)=7/25<1/3`,
`Pr(x<b<y)=11/25>1/3`.                                          (4.1)

Thus a genuinely heavy cover flux exists in a width-three poset. The poset is not a POS3 counterexample: its incomparable-pair probabilities include

`Pr(0<1)=3/5`, `Pr(2<3)=2/5`, `Pr(3<4)=9/25`,

so it has balanced escape pairs.

The example is nevertheless sharp for the theorem below. Relative to `(x,b)`, after removing the unavoidable distinguisher `y`, the only extra distinguisher is `3`; relative to `(y,b)`, after removing the unavoidable distinguisher `x`, the only extra distinguisher is `1`. Thus a strong cover flip can occur with exactly two distinct external asymmetry witnesses, but not with fewer.

## 5. Cover two-witness theorem

For incomparable `u,v`, define

`D(u,v)={z notin {u,v}: rel(z,u) != rel(z,v)}`,

where `rel(z,u)` is one of `z<u`, `z||u`, `u<z`.

### Theorem 5.1 — cover two-witness theorem

Let `P` be any finite poset. Let `x lessdot y`, and let `b` be incomparable with both `x` and `y`. If

`|(D(x,b)\{y}) union (D(y,b)\{x})| <= 1`,                       (5.1)

then at least one of the pairs `(x,b)` or `(y,b)` is balanced.

Consequently, in a poset with no balanced pair, every strong cover flip

`Pr(x<b)>2/3`, `Pr(y<b)<1/3`                                    (5.2)

forces at least **two distinct external distinguishers** beyond the cover endpoints `x,y`.

This theorem itself does not require width at most three.

### Proof

Put

`X=D(x,b)\{y}`, `Y=D(y,b)\{x}`.

If `X` or `Y` is empty, then the corresponding incomparable pair has exactly one distinguisher: respectively `y` or `x`. The named OTHER-account fleet02/B10 r13 one-distinguisher theorem therefore makes that pair balanced. Hence, under the negation of the conclusion and (5.1),

`X=Y={z}`                                                        (5.3)

for one vertex `z`.

Let

`R=P\{x,y,b,z}`

and fix an arbitrary skeleton `tau in L(R)`. Every `w in R` has the same three-valued relation to `x`, `y`, and `b`, because it distinguishes neither endpoint pair. Therefore `x,y,b` have one common admissible external-gap interval `I=[L,U]` relative to `tau`. Let `J=[L_z,U_z]` be the admissible interval for `z`.

Because `x lessdot y` and `b||x,y`, the requirement that `z` distinguish both pairs leaves, up to order duality, only two cases:

- **II:** `x<y<z` and `z||b`;
- **III:** `z||x,y` and `z<b`.

The dual cases are `z<x<y,z||b` and `b<z,z||x,y`.

#### Case II: `x<y<z`, `z||b`

Here `L_z>=L` and `U_z>=U`. The allowed relative orders of the four special vertices are

`bxyz`, `xbyz`, `xybz`, `xyzb`.

Let the exact lift counts over the fixed skeleton be `A_0,A_1,A_2,A_3` in this order.

Swapping the positions of `x,b` maps the first family bijectively to the second; swapping `y,b` maps the second to the third. These swaps preserve every relation to `R`, and all required relations to `z` remain valid. Therefore

`A_0=A_1=A_2=:C`.                                                (5.4)

There is an injection from `xyzb` lifts to `xybz` lifts: swap the external gap positions of `z` and `b`. If the original gaps satisfy

`g_x<=g_y<=g_z<=g_b`,

then `g_z in I` because `g_y>=L` and `g_z<=g_b<=U`; and `g_b in J` because `g_b>=g_z>=L_z` and `g_b<=U<=U_z`. Equal-gap cases are handled by the displayed internal order. Hence

`A_3<=C`.                                                        (5.5)

For the pair `(y,b)`,

`N_tau(b<y)=A_0+A_1=2C`,
`N_tau(y<b)=A_2+A_3=C+A_3`.

Thus its conditional fiber probability lies in `[1/3,1/2]`. Summing the exact numerator and denominator counts over all skeletons preserves the same interval, so `(y,b)` is globally balanced.

#### Case III: `z||x,y`, `z<b`

Here `L_z<=L` and `U_z<=U`. The six allowed interleavings of the two chains `x<y` and `z<b` are

`xyzb`, `xzyb`, `xzby`, `zxyb`, `zxby`, `zbxy`.

Let their exact counts be `A_0,...,A_5`. Swapping equal-constraint vertices gives

`A_1=A_2`, `A_3=A_4=A_5`.                                       (5.6)

There is an injection `xyzb -> zxyb` obtained by swapping the external gaps of `x,z`. Indeed, for

`g_x<=g_y<=g_z<=g_b`,

we have `g_x in J` because `L_z<=L<=g_x<=g_z<=U_z`, and `g_z in I` because `L<=g_y<=g_z<=g_b<=U`. Hence

`A_0<=A_3`.                                                      (5.7)

For `(y,b)`,

`N_tau(y<b)=A_0+A_1+A_3`,
`N_tau(b<y)=A_2+A_4+A_5=A_1+2A_3`.

Equation (5.7) gives `N_tau(y<b)<=N_tau(b<y)`, while

`2N_tau(y<b)-N_tau(b<y)=2A_0+A_1>=0`.

Therefore the fiber probability of `y<b` lies in `[1/3,1/2]`, and exact summation over skeletons again gives global balance.

The two omitted relation patterns follow by taking the order dual; one obtains a balanced endpoint pair with probability in `[1/2,2/3]`. This proves Theorem 5.1. `square`

### Corollary 5.2 — a heavy cover flux must branch twice

In a hypothetical counterexample, if

`Pr(x<b)>2/3` and `Pr(y<b)<1/3`

across `x lessdot y`, then

`Pr(x<b<y)=Pr(x<b)-Pr(y<b)>1/3`,                                (5.8)

and Theorem 5.1 forces at least two distinct vertices in

`(D(x,b)\{y}) union (D(y,b)\{x})`.                              (5.9)

Thus the lead's global charge problem has a new hard combinatorial resource: every `>1/3` cover-crossing flux has branching number at least two. The five-point construction in Section 4 shows the lower bound two is best possible without additional global hypotheses.

## 6. How this applies to the campaign lead

The fleet04/B10 r13 lead state forces repeated two-cover blocker/fork configurations in the strict delayed-predecessor corridor, with a canonical pair of minority mass in `(1/6,1/3)`. The exact flux recurrence (3.1)--(3.9) converts a transition from strong-majority-early to strong-majority-late along one chain into a sum of literal three-chain edge fluxes. Whenever one cover edge itself carries the required `>1/3` drop, Corollary 5.2 says that edge cannot be supported by a single delayed asymmetry witness: at least two distinct external relation channels are compulsory.

This is compatible with the partner's r13 conclusion that every extreme pair has at least two distinguishers, but it is stronger in the cover-flip setting because the two witnesses must survive after deleting the two unavoidable cover endpoints from the two endpoint distinguisher sets.

The first unpaid implication is now:

> **Two-witness flux charging lemma.** In the lead's series/parallel-indecomposable width-three hard core, assign to every heavy cover-crossing edge flux two distinct external distinguishers as in (5.9), and prove that along the repeated bridged fork corridor these witness channels cannot be reused indefinitely without forcing at least one of: a balanced incomparable pair, a four-antichain, a proper autonomous nonchain, or a strict strong-majority span descent.

A proof must retain the exact `F*G` edge weights. Mere counting of witnesses is insufficient: the sharp five-point example already realizes exactly two witnesses, and the lead's known linear-depth adversaries rule out bounded-radius termination.

If this charging lemma is proved for each heavy edge generated by the lead's corridor reduction, the three-chain flux decomposition supplies the desired global induction step without ever replacing the induced weighted law by a uniform one.

## 7. Deterministic regression evidence

The companion verifier is `verify_cover_flux.py`, Git blob `568be0ed17593f3e2a636222eaf630db10ad4cea`. Its recorded output is `verify_cover_flux.out`, blob `27da263f376332a02765473df899f19aab907d71`.

It checks:

1. the two nondual fiber classifications on hundreds of interval instances;
2. every naturally labelled transitive closure through six vertices, restricted to width at most three for the poset regression;
3. all `24,996` cover configurations `x lessdot y`, `b||x,y` in that finite regression;
4. all `5,326` cases satisfying the hypothesis (5.1), with no failure;
5. all `2,471` observed strong cover flips, for which the minimum external-witness union size is exactly `2`;
6. the exact five-point sharp witness of Section 4.

Recorded tail:

```text
cover_configs_checked 24996
cover_two_witness_hypothesis_cases 5326
strong_flip_cases 2471
minimum_external_union_on_strong_flip 2
sharp_witness E 25 px 18/25 py 7/25 gap 11/25 Dx_extra [3] Dy_extra [1]
POS3_COVER_FLUX_TWO_WITNESS_REGRESSION_PASS
```

The arbitrary-size theorem is the symbolic fiber proof in Section 5; the finite computation is regression and sharpness evidence only.

## 8. Honest status and provenance

Outcome is `ESSENTIAL_STEP_APPLIED`, not `FULL_PROOF_CANDIDATE`. POS3 remains open. The run proves an exact global three-chain recurrence plus an arbitrary-size cover two-witness theorem, and constructs a source-valid counterexample to the stronger shortcut that every heavy cover gap is impossible in width three.

No benchmark material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive content, paid model/API/Codex execution, remote workflow, permission change, or public posting is included. Repository reads/writes are coordination/storage only and do not establish native brain retrieval or activation.
