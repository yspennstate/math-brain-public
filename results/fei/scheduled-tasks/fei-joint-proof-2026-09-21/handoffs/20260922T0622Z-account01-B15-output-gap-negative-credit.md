# FEI handoff — account01/B15 empty-atom credit and unequal-output collar

**Classification:** `ESSENTIAL_STEP_APPLIED`; full unrestricted FEI remains **OPEN / NOT PROVED**.

**Scientific source:** `yspennstate/math-open-problems` master commit `19d552c0308fda509e1262e1078359da602343fc`.

Canonical mathematical package:

- `proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260922T0605Z-output-gap-negative-credit/REPORT.md`
- `.../CORRECTION.md` (typesetting correction for REPORT equation (3.4); no mathematical change)
- `.../check_empty_credit.py`
- `.../check_empty_credit.out`

## Exact peer inputs consumed

1. account04/B17 `20260922T031352Z-biased-restriction-margin-cocycle/REPORT.md`, blob `d32321447c5f30282f243d9a2907ec719d483c92`: exact local all-gate cocycle
   \[
   D_\Gamma(G)=qD_\Gamma(G_0)+tD_\Gamma(G_1)+\mathcal R_{\Gamma,j}+\mathcal C_j,
   \qquad \mathcal C_j=H(B\mid S)+I(S;J).
   \]
2. account03/B15 `20260922T052547Z-arity5-bias-tube/REPORT.md`: source-valid scalar bound `|(Gamma^dagger)'|<85` on `[1/64,63/64]`.
3. Live fixed candidate remains `LIMIT-PRIME-GATE-LIFT-v1`, `C^dagger=6.521851214`, `Gamma^dagger=Gamma_0+0.268204856 p(1-p)`.

## New exact negative-information credit

For a pivot of bias `t`, restrictions with output means `r_b`, disagreement `delta`, and
\[
m_b=1-2r_b,\quad d=|r_1-r_0|,\quad V_t=4t(1-t),
\]
define the empty spectral mass
\[
s=(1-t)m_0^2+t m_1^2.
\]
The vertical-layer bit `J` has marginal `mu=V_t delta`.  Coarsen the spectral atom to `E=1_{S=empty}`.  For `0<s<1`,
\[
\theta_0={V_t d^2\over s},
\qquad
\nu={V_t(\delta-d^2)\over1-s}.
\]
Data processing gives the exact usable refund
\[
I(S;J)\ge I(E;J)=:I_0
=h_2(\mu)-s h_2(\theta_0)-(1-s)h_2(\nu)\ge0.
\]
Together with B15's preceding sharp posterior theorem,
\[
\boxed{
\mathcal C_j\ge
\Psi(\sqrt{V_t}|1-2\delta|)+I_0,
}
\]
and Pinsker yields
\[
\boxed{
I_0\ge {2V_t^2\over\ln2}
{(d^2-s\delta)^2\over s(1-s)}
}
\]
for `0<s<1`.

## Applied unequal-output exclusion

The predecessor B15 theorem gives, for `u=min(t,1-t)<=1/64` and `delta>=1/4`, a scalar posterior-credit reserve
\[
F_u(\delta)>0.4194u.
\]
For child output measures `r_0,r_1 in [1/64,63/64]`, the consumed `85`-Lipschitz bound gives
\[
(1-t)\Gamma^\dagger(r_0)+t\Gamma^\dagger(r_1)
-\Gamma^\dagger((1-t)r_0+tr_1)
\ge-170u|r_1-r_0|.
\]
Therefore any physical pivot satisfying
\[
\boxed{
\min(t,1-t)\le1/64,\quad
\delta\ge1/4,\quad
r_0,r_1\in[1/64,63/64],\quad
|r_1-r_0|\le1/512
}
\]
has
\[
\boxed{
\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j
>{13979\over160000}\min(t,1-t)>0.
}
\]
So a minimum-essential-arity counterexample cannot use such a pivot as a negative local-gluing step.  The clean `1/512` is conservative; the proof permits `|r_1-r_0|<2097/850000`.

The diagnostic exhausts 2,048 small Boolean restriction-pair/bias cases for the information identities and ends `PASS`; the analytic proof does not depend on this finite test.

## Exact old/new missing implication

**Old:** unequal child output measures left the source-potential Jensen term unpaid in LOCAL-GLUING.

**New:** the previously unused `I(S;J)` contains an explicit empty-atom refund, and the rare-pivot theorem now covers a genuine unequal-output tube rather than only balanced/equal-output children.

**Next:** enlarge/remove the output-gap and interior-output restrictions by spending `I_0` quantitatively against the potential Jensen deficit; separately `delta<1/4` and intermediate pivot biases remain.

This handoff makes no full-FEI, novelty, or publication-priority claim.
