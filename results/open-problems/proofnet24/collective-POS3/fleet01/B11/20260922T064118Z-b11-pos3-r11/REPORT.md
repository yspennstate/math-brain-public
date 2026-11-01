# POS3 fleet01/B11 — heavy-gap anti-return identity for repeated exact-two fibers

**Run:** `20260922T064118Z-b11-pos3-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities and counts below use the original uniform law on full linear extensions. No deletion-induced law is treated as uniform.

## 1. Exact collective state consumed

The latest complete campaign-lead result consumed is fleet04/B10 r15:

- `proofnet24/collective-POS3/fleet04/B10/20260922T061407Z-B10-POS3-r15/REPORT.md`, blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`.

It proves that in the surviving heavy-cover/no-span branch, with `x lessdot y`, `a||x,y` and strong-majority order `x prec_* a prec_* y`, all canonical failed-swap charge lies on the two outer strong-order rays. Writing

`A=#{a<x<y}`, `H=#{x<a<y}`, `C=#{x<y<a}`, `E=A+H+C`,

its low-endpoint branch is

`A<3E/11`, `C<3E/11`,

hence `H>5E/11`; the first remaining lead obligation is ray-return exclusion/global recycling.

The assigned OTHER-account partner result consumed is fleet02/B19 r13:

- `proofnet24/collective-POS3/fleet02/B19/20260922T053835Z-fleet02-B19-pos3-r13-1acb2f8a/REPORT.md`, science commit `c4c7985fe13db68f080c2c0b0def2bbe29888a52`, report blob `1669d5b58e69dac26d16cd6a942a5b30eb4eb82a`.

It gives a connected autonomous-prime width-three 11-element core with 515 extensions and a sharp heavy cover `(x,a,y)=(5,10,6)`. It refutes local two-witness unit charging. I use the exact same core below to test the stronger global-return intuition.

The exact fiber algebra inherited from fleet01/B11 r11 is:

- `proofnet24/collective-POS3/fleet01/B11/20260922T051731Z-b11-pos3-r11/REPORT.md`, blob `bba2357120a72c7e2d473dd23095240f61e2f266`.

For a repeated exact-two crossed cell, after summing the true lift multiplicities, there are nonnegative integers `a,b,c,t` with

`E=3a+2b+2c+t`, `t<=b`, `t<=c`,

and four actual incomparable-pair minority counts

`q0=a+c`, `q1=a+b`, `qR=2b+t`, `qL=2c+t`.

The two exact noninjective-fiber identities are

`6q0+3q1+2qR=3E+(b-t)`,

`3q0+6q1+2qL=3E+(c-t)`.

The slacks `b-t,c-t` are the exact missed-fiber counts of the two injections.

## 2. Compact conditional end-to-end route

Assume a cardinality-minimal no-balanced width-three candidate. The lead supplies a heavy cover with `H>1/3`, localizes all failed-swap charge to the outer rays, and in its low-endpoint branch has `A,C<3E/11`, hence `H>5E/11`.

If the outward ray enters the same repeated exact-two crossed geometry as the inherited B11 fiber block, the two outer canonical pair counts can be compared not merely with `3E/11` but directly with the two central endpoint counts. The new identity below shows that, once `H>5E/11`, the two outward moves cannot both fail to improve their corresponding central minority counts. Thus an exact-two return cycle cannot persist if one always follows a positive-gain side.

This pays the lead's ray-return obligation for the low-endpoint repeated-exact-two subbranch. The parent theorem remains open because a positive-gain corridor may exit into a non-exact, non-crossed, multi-distinguisher, high-endpoint, span-descent or autonomous-reduction branch.

## 3. Heavy-gap anti-return identity

Consider an oriented repeated exact-two block satisfying the previous B11 five-label hypotheses, after the harmless order-dual/relabeling needed to align the two central minorities with the lead heavy-cover endpoints. Denote the two central endpoint minority counts by

`A=q0`, `C=q1`,

and the corresponding two outward canonical minority counts by

`R=qR`, `L=qL`.

Let

`s_R=b-t>=0`, `s_L=c-t>=0`

be the two exact non-surjectivity slacks. Since the three relative positions of the lead middle vertex partition the extensions,

`H=E-A-C`.

Define the outward gains over the would-be return counts

`delta_R=R-C`, `delta_L=L-A`.

### Theorem 3.1 — exact heavy-gap anti-return identity

Under the repeated exact-two fiber hypotheses,

`2(delta_R+delta_L)=11H-5E+s_R+s_L`.               (3.1)

Equivalently,

`delta_R+delta_L=(11H-5E+s_R+s_L)/2`.              (3.2)

#### Proof

The inherited exact identities are

`6A+3C+2R=3E+s_R`,

`3A+6C+2L=3E+s_L`.

Substitute `R=C+delta_R` and `L=A+delta_L` and add. The left side becomes

`11(A+C)+2(delta_R+delta_L)`.

Since `A+C=E-H`, equality with `6E+s_R+s_L` gives

`11(E-H)+2(delta_R+delta_L)=6E+s_R+s_L`,

which rearranges to (3.1). `square`

### Corollary 3.2 — strict outward gain above the 5/11 heavy-gap threshold

If

`H>5E/11`,

then

`delta_R+delta_L>0`.

Hence at least one side satisfies

`R>C` or `L>A`.

More quantitatively,

`max(delta_R,delta_L) >= (11H-5E+s_R+s_L)/4 > 0`.   (3.3)

The noninjective fibers help: every missed target fiber enters (3.1) with a positive sign.

### Application to the lead low-endpoint branch

The lead r15 branch has

`A<3E/11`, `C<3E/11`.

Therefore

`H=E-A-C>5E/11`,

so Corollary 3.2 applies automatically. Thus a low-endpoint heavy state cannot have both exact-two outward channels no better than their corresponding return endpoints.

## 4. Finite anti-cycle consequence for an exact-two corridor

Suppose a sequence of repeated exact-two crossed cells is oriented so that an outward pair selected at one cell becomes the corresponding central endpoint pair at the next cell. At every cell in the lead low-endpoint regime `H>5E/11`, select any side with positive gain from Corollary 3.2.

The selected actual pair-minority count then increases strictly. Since the common poset has a fixed finite extension count `E`, these counts are integers in `{0,1,...,floor((E-1)/3)}` until balance. Therefore this positive-gain selector cannot revisit a previously selected pair with the same orientation and cannot form a finite cycle entirely inside the low-endpoint repeated-exact-two regime.

Consequently an infinite-looking recycler must terminate in finitely many steps by one of the already recognized exits: a balanced pair, strict strong-majority span descent, an endpoint minority reaching the near-balance/high-endpoint regime, a non-exact/non-crossed or multi-distinguisher state, or a proper autonomous/ordinal reduction.

This is deliberately different from the refuted largest-fringe rule: it does not choose the locally largest fringe. It uses the simultaneous two-sided identities and follows a side certified to have positive gain relative to the specific return endpoint.

## 5. Applying the assigned partner: autonomous-primality alone does not prevent a return cycle

The partner r13 core has covers

`0<1, 0<5, 1<2, 1<6, 1<10, 2<3, 4<1, 4<5, 5<3, 5<6, 6<7, 8<9, 8<0, 9<5, 9<10, 10<3, 10<7`.

The partner already certified width exactly three, connected incomparability graph, autonomous-primality and `E=515`.

For the same heavy triple `(x,a,y)=(5,10,6)`, exact enumeration gives

`A=#{10<5}=141`,

`C=#{6<10}=161`,

`H=#{5<10<6}=213`.

The two external canonical fringe counts in the consecutive crossed states are

`R=#{5<1}=128`,

`L=#{3<6}=88`.

Moreover the crossed discrepancies are

`Pred(10)\Pred(5)={1}`, `Succ(5)\Succ(10)={6}`,

and

`Pred(6)\Pred(10)={5}`, `Succ(10)\Succ(6)={3}`.

Thus the same largest-fringe rule that cycled in the older non-prime example also cycles here:

`(5,10) -> (10,6) -> (5,10)`.

This is a genuine source-valid counterexample to the tempting intermediate claim that connectedness plus autonomous-primality by itself makes the greedy fringe transport acyclic. It is not a POS3 counterexample; the partner lists balanced pairs elsewhere in the same poset.

The new identity diagnoses exactly why this core is outside the positive-gain regime. Its two noninjectivity slacks are

`s_R=6A+3C+2R-3E=40`,

`s_L=3A+6C+2L-3E=20`.

The outward gains are

`delta_R=R-C=-33`, `delta_L=L-A=-53`,

so their sum is `-86`. Equation (3.2) gives the same value because

`(11H-5E+s_R+s_L)/2=(2343-2575+60)/2=-86`.

And indeed

`H/E=213/515 < 5/11`.

So the autonomous-prime return cycle does not contradict Corollary 3.2. It instead shows that the `5/11` heavy-gap threshold, not module-primality alone, is doing genuine work in the anti-return argument.

## 6. Verification

A standard-library checker for this run was executed locally before attempted archival delivery. It tests the symbolic identity on 4549 bounded integer fiber configurations satisfying the inherited inequalities, including 1305 configurations with `11H>5E`, and verifies that every such configuration has a positive outward gain. It independently reconstructs the partner r13 11-element poset, enumerates all 515 uniform linear extensions, checks the counts above, the exact greedy two-cycle, the two slacks `(40,20)`, the gains `(-33,-53)`, and equation (3.1).

Terminal marker:

`POS3_HEAVY_GAP_ANTIRETURN_PASS`.

The symbolic proof of Theorem 3.1 is arbitrary-size; this computation is regression evidence and exact partner calibration only.

## 7. First essential remaining implication

The first missing implication is now narrower:

> **EXIT-CHARGE AMPLIFICATION.** When the strict positive-gain exact-two corridor exits before producing balance, show that the conserved heavy-cover defect transfers through the first high-endpoint, non-exact/non-crossed or multi-distinguisher state so that either (i) some actual incomparable-pair minority reaches `1/3`, (ii) strict strong-majority span descent occurs, (iii) a proper autonomous/ordinal reduction occurs, or (iv) a new low-endpoint exact-two block begins with pair-minority potential at least the outgoing positive-gain pair.

The present theorem rules out finite return cycles only while the exact repeated-two-sided fiber hypotheses and `H>5E/11` remain valid. It does not assert that every outer-ray state has those hypotheses.

## 8. Status and integrity

- lead fleet04/B10 r15 ray localization and low-endpoint branch: **CONSUMED/APPLIED**;
- assigned partner fleet02/B19 r13 autonomous-prime adversary: **CONSUMED/APPLIED**;
- previous B11 two-sided exact fiber identities: **CONSUMED/APPLIED**;
- exact heavy-gap anti-return identity (3.1): **PROVED**;
- strict positive outward gain for `H>5E/11`: **PROVED**;
- no finite cycle in a positively selected low-endpoint repeated-exact-two corridor: **PROVED under the stated corridor alignment hypothesis**;
- connected autonomous-prime alone excludes greedy return cycles: **REFUTED by exact partner r13 core**;
- full POS3 target: **OPEN / NOT PROVED**;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, public posting, paid model/API/Codex execution, remote workflow, permission change, or native verified-brain activation was used or claimed.
