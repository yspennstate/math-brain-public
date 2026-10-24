# account03/B13 update — stronger prime source supersedes the first repair scale

**Status:** `AUXILIARY_ONLY / CURRENT_SCALE_UPDATED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Scope:** this update supersedes only the candidate-scale discussion in Sections 0, 5, 7 and 8 of `REPORT.md`. The coercivity theorem and zero-set classification proved there are unchanged.

## Fresh completed peer result consumed

After the first report was committed, a newer compatible cross-account result landed:

`proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T091146Z-strong-prime-shaped-repair/REPORT.md`, commit `f5946fb64d336ed7369de279159643944efc47af`.

It consumes the source-valid composition-prime Numaro gate and proves a stronger one-core witness

\[
p_1={223\over456},\qquad p_2=\cdots=p_{18}=\frac12,
\qquad p_{\rm out}={1019\over2048},
\]

with

\[
D_{\Gamma^\dagger}=-0.0380237343652791923\ldots<0.
\]

On this exact Boolean source the same universally safe direction used in the B13 theorem has exact currency

\[
M_\eta
={3522569893845884171958045614703407
\over3468518558332143666368348160000000}
=1.015583406749806\ldots .
\]

Therefore the shaped normalized margin satisfies the rigorous peer enclosure

\[
0.0374402867822\ldots
<c_G^{(\eta)}
<0.0374402877669\ldots .
\]

This **refutes** the earlier scale

\[
\lambda_{old}=0.01734442
\]

that was sufficient only for the older `p_1=3/8` witness. Thus the first report's statement that `Gamma^dagger+0.01734442 eta` was the current candidate became stale when this peer result landed.

The newest executed replacement is

\[
\boxed{\lambda_{new}={374403\over10000000}=0.0374403}
\]

and

\[
\boxed{
\Gamma^{new2}=\Gamma^\dagger+\lambda_{new}\eta,
\qquad
\Gamma^{new2}(1/2)
={327922264791373\over50000000000000}
=6.55844529582746.
}
\]

The peer certifies on the strong prime witness

\[
D_{\Gamma^{new2}}>1.2423734761601635\times10^{-8}>0.
\]

The coefficient clearance over the peer's rigorous upper requirement is only

\[
0.0374403-0.0374402877669>1.22331\times10^{-8}.
\]

## Application of the B13 theorem to the newest candidate

The strict-coercivity theorem from `REPORT.md` applies unchanged because the repair shape `eta` is unchanged. For every nonliteral Boolean gate and every interior product bias,

\[
M_\eta(G;p)>0,
\]

and more quantitatively, for every physical singleton reveal,

\[
M_\eta(G;p)\ge
r_0 d t(1-t)(2-d)+(\delta-d/2)\eta(t),
\]

with

\[
r_0={1999313322941\over16492674416640000000}>0.
\]

Therefore the **updated** universal missing implication is cleanly normalized:

\[
\boxed{
\sup_{G,p\,\text{nonliteral}}
{[-D_{\Gamma^\dagger}(G;p)]_+\over M_\eta(G;p)}
\le 0.0374403.
}
\]

If this holds, `Gamma^new2` is a universal all-gate potential and FEI follows with center `6.55844529582746`. This run does **not** prove that supremum bound.

Constants and literals are not zero-denominator obstructions: they satisfy the gate identity exactly, while the theorem proves every nonliteral gate has strictly positive repair currency.

## Decisive next attack, updated

The highest-value local falsification test is no longer the old `p_1=3/8` point. It is the one-core Numaro bias line through

\[
p_1=223/456,
\]

because the newest scale clears that actual composition-prime witness by only about `1.2e-8` in normalized coefficient units. Search source-exactly on the adjacent h96 interpolation cells for a value with

\[
c_G^{(\eta)}(p)>0.0374403.
\]

A single such point refutes `Gamma^new2`; otherwise a rigorous local maximum certificate would buy a genuine collar around the strongest currently known prime source.

A complementary peer mechanism from account03/B17 transports the same prime gate's Bellman dent close to the center; that return/cycle problem may expose a different successor obstruction, but it is logically separate from the normalized safe-direction bound above.

## Required collaboration fields, updated

- `exact_candidate_version`: `Gamma^new2 = Gamma^dagger + (374403/10000000) eta`, center `6.55844529582746`.
- `prior_missing_implication`: universal nonnegativity of the all-gate defect for the current shaped candidate.
- `new_proved_inference`: the B13 zero-set/coercivity theorem removes every nontrivial zero-denominator exception for this updated candidate as well.
- `exact_failed_claim`: `lambda=0.01734442` is sufficient for all prime gates — **REFUTED** by account02/B17's strong one-core source.
- `replacement_obligation`: prove the normalized shaped-margin supremum is at most `0.0374403`, or find a gate/bias above it.
- `consumed_peer_artifact`: account02/B17 strong-prime shaped-repair report, commit `f5946fb64d336ed7369de279159643944efc47af`.
- `applied_to_claim`: updates the B13 universal normalization from the obsolete old scale to the strongest currently executed shaped scale.
- `remaining_implication`: universal normalized-margin upper bound or explicit counterexample.
- `next_recipient`: account02/B17 for shaped-repair search; account03/B18 for all-gate integration.
- `full_problem_change`: none; full FEI remains OPEN / NOT PROVED.

No scheduler mutation, cross-account mutation, email, Drive write, public posting, workflow dispatch, paid model/API/Codex use, credential access, or unrelated private-data operation was used.
