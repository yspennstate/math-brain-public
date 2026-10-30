# B17 — the recursive shared-graft obstruction has a rigorously positive infinite tail

**Run:** `20260922T022208Z-fleet03-B17-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository controls and source-bound mathematical artifacts were read directly; no authenticated installed mathematical-brain retrieval/context was used.  
**Outcome:** **ESSENTIAL_STEP_APPLIED** and **CANDIDATE_REFUTED** for freezing the scalar gate lift at any of the already certified finite shared-graft stages.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 1. Candidate version and why this is the live adversarial step

The live owner target is the all-gate reformulation

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for every Boolean gate and every full-support product bias.  The older assignment-specific restriction wording is superseded by the newer natural-language control telling all FEI workers to converge on (G) and either prove an extremal reduction or produce source-valid larger-margin gates.

The exact candidate attacked here is **SG-TAIL-v1**: after the source-valid shared-coordinate grafts `F_1,...,F_4`, may one freeze a scalar quadratic lift at the latest finite balanced excess ratio?  Fleet03/B18 explicitly left this as the next implication: prove a tail theorem for the recurrence instead of certifying one giant rational stage at a time.

This is materially different from this slot's preceding uniform-quarter-slice and dyadic-restriction batteries.  No arity-five sweep or dyadic descendant classification is repeated.

## 2. Cross-account result consumed and applied

The principal cross-account input is fleet01/B18,

`fleet01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`, report blob
`cbe682d84b52232ab4e91367b08bbfe73d74a39e`.

It proves the source-valid shared-core transform for any balanced monotone gadget with a distinguished singleton coefficient.  If the current gate has

\[
R=\frac{H}{I-1},\qquad c=\widehat f(\{j\}),
\]

then fourth balanced self-composition followed by the nine-host shared graft gives

\[
I'=\frac{261}{128}+\frac9{256}(I^4-1),
\qquad
c'=\frac{57}{256}+\frac{c^4}{256},
\tag{2.1}
\]

and, with \(\alpha=9/256\), \(\beta=133/128\),

\[
R'-R=
\frac{K(c^4)-\beta R}
     {\alpha I^4+257/256},
\tag{2.2}
\]

where

\[
K(b)=H_{\rm core}(b)+\frac9{256}
\bigl[-\phi(b^2)+16(1-b^2)\bigr],\qquad
\phi(x)=-x\log_2x.
\tag{2.3}
\]

I apply this exact recurrence, rather than merely citing it, to prove the entire future tail has one sign.

A second compatible peer input is the exact gate-margin composition/barycenter theorem of fleet04/B15,
`fleet04/B15/20260922T004054Z-gate-margin-composition/REPORT.md`: disjoint composition propagates gate slack and Poincare currency with identical nonnegative weights, so a gate above a margin threshold has a composition-prime factor at least as bad.  I use that only after the new lower bound is established.

For the starting numerical enclosure I consume fleet03/B18's source-bound exact continuation
`fleet03/B18/20260922T011005Z-recursive-shared-graft-extension/REPORT.md`, blob
`4d1e86bd941df8bb941ba974f6478bbe4842ef84`, which rigorously encloses `F_4` by

\[
R_4\in[
6.5218509485644448965490881329959858569477358114202360,
6.5218509485644448965496895824490791318643557898359043].
\tag{2.4}
\]

## 3. New theorem: a rational trap for every future singleton coefficient

Let

\[
T(c)=\frac{57}{256}+\frac{c^4}{256}.
\]

The exact source gives \(c_1=14593/65536\); applying `T` three times gives the exact `F_4` coefficient

\[
c_4=0.22266585228323682345854077973015982230789629559137\ldots .
\]

Define the rational interval

\[
L=0.22266585228323679,
\qquad
U=0.22266585228323683.
\tag{3.1}
\]

Exact rational arithmetic gives

\[
L<c_4<U,\qquad T(L)>L,\qquad T(U)<U.
\tag{3.2}
\]

Since `T` is increasing on the positive axis, (3.2) proves

\[
\boxed{c_t\in[L,U]\quad\text{for every }t\ge4.}
\tag{3.3}
\]

Thus the singleton parameter can no longer drift into an unexamined part of the core functional.

## 4. Uniform exact enclosure for the core functional

The checker reconstructs the inherited nine-host core from its exact source representation and obtains only nineteen pairs of integer Walsh numerators \((A_S,Q_S)\).  For

\[
b\in[L^4,U^4],
\qquad
\widehat F_{\rm core,b}(S)=\frac{A_S+bQ_S}{512},
\]

every squared mass is rigorously below

\[
0.04958008177302022838<\frac1{20}<\frac1e.
\]

Hence \(\phi(x)=-x\log_2x\) is increasing throughout the entire relevant interval.  Bounding every affine coefficient at its rational endpoints and evaluating logarithms by an exact atanh-series enclosure therefore gives

\[
\boxed{
6.776610978572346708428848432334517762739242599071115146521012
\le K(c_t^4)
}
\tag{4.1}
\]

and

\[
\boxed{
K(c_t^4)\le
6.776610978572346710512595494365945798367450549777252949302550
}
\tag{4.2}
\]

for every \(t\ge4\).  The enclosure width is about \(2.084\times10^{-18}\).

Writing `K_-` for the lower endpoint, the critical ratio is

\[
\boxed{
K_-/\beta
=6.521851167347822396081899243149009576170098140459419088381124\ldots .}
\tag{4.3}
\]

This lies more than \(2.18\times10^{-7}\) above the certified upper endpoint of `R_4`.

## 5. Tail theorem: every later shared graft strictly improves the ratio

Let

\[
D_t=\alpha I_t^4+257/256=I_{t+1}-1.
\]

The exact influence recurrence gives

\[
I_4=8.9891831269165525119469526862195470748936495017444294\ldots,
\]

hence

\[
D_4=230.5571615297100612740059318140455\ldots>229.
\tag{5.1}
\]

Also

\[
D_{t+1}=\alpha(D_t+1)^4+257/256\ge\alpha D_t^4,
\]

so for every `t>=4`, once `D_t>=229`,

\[
\frac{D_{t+1}}{D_t}
\ge\alpha\,229^3
=422191.01953125>400000.
\tag{5.2}
\]

From (2.2), (4.1)--(4.2), and the certified `R_4` interval, while the increments are positive their numerators are bounded above by

\[
N_+
=2.27329603185192058606174804243882693808223413980552550\times10^{-7}.
\]

Thus the entire possible future positive increase beginning at `F_4` is at most

\[
N_+\sum_{t\ge4}\frac1{D_t}
<
N_+\frac{1/229}{1-1/400000}
<9.927081725354622\times10^{-10}.
\tag{5.3}
\]

But after paying this whole worst-case tail, the distance to the threshold (4.3) is still

\[
\boxed{
2.17790669326996747498436774549543155252853484712735837\times10^{-7}>0.
}
\tag{5.4}
\]

This closes the induction: `R_4<K_-/beta`; if all increments through stage `t-1` are positive, (5.3)--(5.4) keep `R_t<K_-/beta`, so the numerator in (2.2) is strictly positive and therefore `R_{t+1}>R_t`.  Hence

\[
\boxed{R_{t+1}>R_t\quad\text{for every }t\ge4.}
\tag{5.5}
\]

This is the tail theorem left open by the preceding peer report.

## 6. Improved finite Boolean lower bound and the limiting interval

For the first new stage, `I_4<9`, so

\[
D_4<\frac9{256}\,9^4+\frac{257}{256}=231.6640625.
\]

The numerator in (2.2) is rigorously at least

\[
2.27329603183107686600571021477286435411194745834802262\times10^{-7}.
\]

Therefore the actual finite balanced monotone Boolean gate `F_5` satisfies

\[
R_5-R_4>
9.81289893347647249346544725629537103585907917136704\times10^{-10}
\]

and in particular

\[
\boxed{
R_5>
6.521850949545734789896735382342530582577272915006143917136704.
}
\tag{6.1}
\]

Balanced disjoint self-composition of this finite gate has `H/I -> R_5`; consequently the source-valid FEI lower bound improves to

\[
\boxed{
C_{\rm FEI}>
6.5218509495457347898967353823425305825772729150061439.
}
\tag{6.2}
\]

The same tail estimate proves the infinite shared-graft sequence converges, and traps its limit by

\[
\boxed{
6.5218509495457347898967353823425305825772729150061439
< R_\infty <
6.5218509495571530690851517447122350266269428876059344.
}
\tag{6.3}
\]

The interval width is less than \(1.142\times10^{-11}\).  No extrapolation from a few stages is used.

## 7. Consequence for the normalized gate margin

At uniform biases for a balanced gate, relative to the old read-once center `C0=6.4548`,

\[
c_G=4\left(\frac{H(G)}{I(G)-1}-C_0\right).
\]

Thus the finite `F_5` obstruction alone forces any purely quadratic scalar lift of that reference potential to satisfy

\[
\boxed{
c\ge
0.2682037981829391595869415293701223303090916600245757.}
\tag{7.1}
\]

Anchoring instead at the proved read-once bound `6.4573` still forces

\[
\boxed{
c\ge
0.2582037981829391595869415293701223303090916600245757.}
\tag{7.2}
\]

By the consumed composition-barycenter theorem, if `F_5` decomposes then some composition-prime factor inherits at least this normalized margin.  Therefore restricting the same scalar-lift strategy to composition-prime gates does not evade (7.1).

This decisively supersedes the old small-arity picture in which the two-input AND margin `~0.0043974` appeared extremal.  It does **not** refute FEI: it raises a lower bound and constrains the potential that a proof must use.

## 8. Exact status, replacement obligation, and next recipient

**Exact candidate version:** `SG-TAIL-v1`, the fleet01/B18 shared-graft recurrence plus the fleet03/B18 `F_4` enclosure.

**Old missing implication:** determine whether the source-valid recurrence keeps raising the balanced obstruction after `F_4`, instead of freezing a new scalar center at the latest finite stage.

**New proved inference:** every future shared-graft increment is strictly positive; the whole future tail is summable and the limit is trapped by (6.3).  The explicit finite gate `F_5` already improves the rigorous FEI lower bound to (6.2).

**Refuted stronger bridge:** freezing the scalar-lift center at any already certified `F_1`, `F_2`, `F_3`, or `F_4` ratio is false, because the next genuine finite Boolean shared graft has a strictly larger balanced excess ratio.

**Replacement obligation:** a one-parameter gate potential must start with center at least (6.2), preferably respecting the limiting barrier (6.3), and then prove the all-gate/all-bias inequality on composition-prime gates.  Alternatively the proof needs a genuinely different finite-cap potential whose additional state survives shared-coordinate graft interference.  The present theorem does not supply that upper-bound mechanism.

**Consumed peer artifact:** fleet01/B18 shared-graft recurrence, blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`; applied to the tail-sign claim.  Fleet04/B15's margin barycenter is applied to the composition-prime consequence.

**Next recipient:** fleet01/B18 for incorporating the closed recurrence tail, and fleet02/B17 / fleet03/B18 for the next prime-gate/all-bias potential.  The remaining implication to full FEI is a finite universal upper envelope satisfying (G); no such envelope is proved here.

**Full FEI remains OPEN / NOT PROVED.**

## 9. Reproduction boundary

`CHECK_TAIL.py` is standard-library only.  It reconstructs the exact nine-host core Walsh data, uses rational arithmetic throughout, encloses logarithms by an 80-term atanh series with an explicit remainder, checks the invariant singleton interval and tail induction, and prints the bounds above. `CHECK_OUTPUT.txt` is the captured successful result.

A scoped fallback privacy/secret scan was applied to the changed mathematical files because no repository-native scanner was exposed in this invocation; it checked for credential-like prefixes and machine-path/account artifacts and found none.  The artifacts contain only source-bound mathematical data, formulas and nonsecret hashes.  No credentials, scheduler identifiers, machine paths, unrelated private transcripts, email/Drive actions, paid model/API calls, permission changes, public posting, or workflow dispatch occur here.
