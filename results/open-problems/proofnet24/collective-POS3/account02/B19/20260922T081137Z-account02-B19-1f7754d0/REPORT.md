# POS3 account02/B19 — coherent same-ray gate is created by a two-point autonomous-chain expansion

**Outcome:** `CANDIDATE_REFUTED`  
**Parent POS3 status:** **OPEN / NOT PROVED**  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

All probabilities below are under the uniform law on the full set of linear extensions of the stated poset. No projected/deletion law is silently replaced by a uniform law.

## 1. Fresh source state actually used

This run uses the latest complete campaign-lead report visible at the source revision consumed:

- account04/B10 r17, `proofnet24/collective-POS3/account04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, Git blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

Its same-ray analysis pays comparable typed gates by a strict positive strip and anti-aligned incomparable gates by an anchor-free blocker pair. Its sole unpaid same-ray state is the coherent width-saturating three-antichain gate, e.g. on the right ray

`y prec_* r_L prec_* r_R`, with `{y,r_L,r_R}` a three-antichain,

where `r_L in F1`, `r_R in F3`.

The named partner result used is:

- account03/B10 r12-turning, `proofnet24/collective-POS3/account03/B10/20260922T071308Z-account03-B10-r12-turning/REPORT.md`, Git blob `7c194b61648e3a61dd64cfe06ee12bf9739b6123`.

It proves that an opposite-handed outer-ray reversal is an actual heavy Hasse sandwich and reduces recycling to bounded-turn activation. Therefore a same-ray coherent gate is genuinely outside that turning lemma until a handedness change is activated.

## 2. Conditional end-to-end state and first missing implication

A compact conditional closure route is now:

1. use the lead's heavy-cover analysis to emit typed outward packets;
2. comparable same-ray and anti-aligned same-ray states are paid by r17;
3. opposite-handed reuse is paid back into a heavy sandwich by account03/B10 r12;
4. therefore it would suffice to show that every coherent same-ray three-antichain gate either safely reduces through an ordinal/autonomous decomposition **with the exact uniform-law balance conclusion transferred back**, or activates a controlled turn/opposite-ray packet/span descent.

The emphasized transfer is not automatic for an autonomous **chain**. This run gives an exact source-valid counterexample to the tempting shortcut “contract the autonomous chain, use a balanced quotient pair, and lift the same pair back.” The obstruction occurs exactly inside the lead's coherent-gate geometry.

## 3. Exact three-chain family

For `m>=1`, define `P_m` on

`{0,1,2,3,4,c1,...,cm,7,8,9,10}`

by the transitive reduction

- `0<1<2<3`,
- `4<c1<...<cm<7`,
- `8<9<10`,
- cross covers `0<7`, `4<1`, `cm<10`, `7<2`, `8<4`, `9<3`.

The displayed three chains are a chain cover. `{0,4,9}` is a three-antichain, so every `P_m` has width exactly three. The incomparability graph is connected for `m=1,2` (checked exactly).

The lead-gate labels are

`x=0`, `y=1`, `a=9`, `r_L=7`, `r_R=10`.

Structurally,

- `x lessdot y`;
- `a || x,y`;
- `x lessdot r_L`, with `r_L || a,y` (`r_L in F1`);
- `a lessdot r_R`, with `r_R || y` (`r_R in F3`);
- `r_L || r_R`.

Thus the only question is the actual full-law strong-majority orientation.

## 4. Prime quotient `P_1`: the coherent gate is not yet present

Exact dynamic programming gives

`e(P_1)=299`.

The five gate orientation counts are

- `#(0<9)=221`, so `Pr(0<9)=221/299>2/3`;
- `#(9<1)=204`, so `Pr(9<1)=204/299>2/3`;
- `#(1<7)=185`, so `Pr(1<7)=185/299`, which lies in `[1/3,2/3]`;
- `#(1<10)=244`, so `Pr(1<10)=244/299>2/3`;
- `#(7<10)=230`, so `Pr(7<10)=230/299>2/3`.

An exhaustive autonomy check finds **no nontrivial proper autonomous subset** in `P_1`.

So the prime quotient already has the balanced pair `(1,7)`, and the full coherent strong-majority chain `x prec_* a prec_* y prec_* r_L prec_* r_R` fails exactly at this one orientation.

## 5. Expand one quotient atom to a two-chain: the full coherent gate appears

Replace the single quotient atom `c1` by the autonomous two-chain `M={c1<c2}`. This is `P_2`. Exact checking gives

`e(P_2)=533`, width exactly three, connected incomparability graph, and the **only** nontrivial proper autonomous subset is `{c1,c2}`.

The same five gate events now have counts

- `#(0<9)=389`, so `389/533>2/3`;
- `#(9<1)=360`, so `360/533>2/3`;
- `#(1<7)=364`, so `364/533>2/3`;
- `#(1<10)=448`, so `448/533>2/3`;
- `#(7<10)=408`, so `408/533>2/3`.

Hence `P_2` realizes **exactly** the lead's coherent right-ray state:

`0 prec_* 9 prec_* 1 prec_* 7 prec_* 10`,

with `{1,7,10}` a three-antichain, `7 in F1`, and `10 in F3`.

Contracting `{c1,c2}` back to one atom reproduces `P_1` exactly as a poset. Yet the quotient-balanced pair `(1,7)` moves from

`185/299 ~= 0.61873`

to

`364/533 ~= 0.68293 > 2/3`.

Therefore **same-pair balance does not lift through this autonomous-chain expansion under the uniform extension law**. In particular, the coherent-gate “proper autonomous reduction” branch cannot be paid merely by cardinality minimality plus contraction unless a separate weighted pair-migration/substitution theorem is supplied.

This does not contradict the campaign lead: r17 listed decomposition as a possible exit but did not prove a uniform same-pair lifting theorem for chain modules. It also does not contradict account03/B10 r12: the example stays in the same-ray coherent state and does not instantiate an opposite-handed turn.

## 6. All incomparable-pair probabilities in the adversary

The verifier checks all **19** incomparable pairs of `P_2` exactly. Five are balanced:

- `Pr(0<4)=18/41`;
- `Pr(1<c2)=15/41`;
- `Pr(2<10)=264/533`;
- `Pr(c1<9)=25/41`;
- `Pr(c2<9)=215/533`.

The exact output records the other fourteen probabilities as well. Thus `P_2` is **not** a counterexample to POS3. It is a counterexample to the stronger local selector shortcut that a coherent gate can be discharged by contracting its autonomous chain and lifting the same balanced quotient pair.

Arbitrary ordinal padding `C_s \oplus P_2 \oplus C_t` preserves every internal incomparable-pair probability, because every full extension is forced to concatenate the prefix chain, one full extension of `P_2`, and the suffix chain. Hence this selector obstruction occurs at arbitrarily large finite sizes without changing the uniform internal law.

## 7. Materially different product screen

Because several previous B19 runs attacked local packet/conditioning mechanisms directly, this run first switched mechanisms and screened rectangular product posets. Exact ideal-DP checks of `C_m x C_3` for `m=3,4,5,6,7` found **zero** instances satisfying all of the lead's `F1/F3` coherent right-ray probability inequalities. The extension counts were respectively

`42, 462, 6006, 87516, 1385670`.

This is only a finite product screen, not an arbitrary-size theorem and not a POS3 closure claim. It motivated the chain-module substitution construction above, which does realize the exact residual.

## 8. First essential missing implication after this run

The sharp next step is now:

> **COHERENT CHAIN-MODULE MIGRATION.** In a cardinality-minimal no-balanced width-three candidate, suppose a lead-r17 coherent same-ray gate meets a proper autonomous chain `M`. After contracting `M`, minimality supplies some balanced quotient pair. Prove under the exact expansion weights that either some (possibly different) original incomparable pair is balanced, or the expansion necessarily activates a controlled opposite-ray/turn state, strict strong-majority span descent, an ordinal reduction, or another already-paid branch.

The pair is explicitly allowed to migrate. `P_1 -> P_2` proves that demanding the *same* pair is false even in a connected width-three example whose quotient is autonomous-prime.

If no proper autonomous chain exists, the remaining lead obligation is the genuinely prime coherent-gate exit. The present example separates these two cases cleanly instead of conflating them.

## 9. Exact executable evidence

`verifier.py` Git blob: `52fca0180d6fcd0b0d994bcf0f49748c2a38f312`  
`verifier.py` SHA-256: `3877e0fce69ed5f5d26629858a21579e20e6efc9f1b6bef1de79639debf6ed83`

`output.txt` Git blob: `f4faeb5c3a09187d948dab8eda2100cdef0f70a3`  
`output.txt` SHA-256: `90fb9dc1d074a0370b863a4188fec39cf75b7bf1ca3ba542a8fea9b3e00e66f6`

The run terminates `POS3_COHERENT_GATE_MODULE_PHASE_PASS`.

Scoped privacy/provenance review: only mathematical statements, logical account/slot/run labels, repository-relative source references, and nonsecret source hashes are recorded. No credentials, scheduler identifiers, machine paths, private transcripts, benchmark gold, email, Drive data, remote workflow dispatch, or permission changes are present.
