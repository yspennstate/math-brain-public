# FEI handoff — account03/B04 -> account01/B01

Programme: `FEI-ALL-TEAM-20260922T095941Z`  
Control revision: `2026-09-22.3`  
Run: `20260922T105911Z-account03-B04-fei-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED / BOUNDARY_QUOTIENT_DESINGULARIZED`  
Full FEI: `OPEN_NOT_PROVED`  
Brain: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Canonical result

Repository: `yspennstate/math-open-problems`  
Report path: `proofnet24/P03-fei/fleet-2026-09-22/account03/B04/20260922T105911Z-boundary-bellman-desingularization/REPORT.md`  
Report publication commit: `74e1f1da10b68c92ae3eaf6edf4f5990c8e8f2fc`  
Readback blob: `1a623f89e5bc35040599b282e4d12b8192bedb04`  
Claims publication commit: `27ed516cec4744e7eeb5c3dd86443f0bb507f600`.

## Exact input consumed

1. Compatible completed peer: `account04/B13`, `proofnet24/P03-fei/fleet-2026-09-22/account04/B13/20260922T1023Z-poincare-bellman-exception-tree/REPORT.md`. Used its exact singleton Poincare currency and child-slack-preserving defect cocycle.
2. Source-stable selector identities: `account02/B12`, commit `4ccd51ad517f425a529daa52c3352905b86ea69d`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`, Sections 2–4 only. Its obsolete `0.337` candidate is excluded.
3. Previous B04 equality/interior collar: `proofnet24/P03-fei/fleet-2026-09-22/account03/B04/20260922T103904Z-nearzero-poincare-trichotomy/REPORT.md`.

Assigned partner `account04/B04` has the live all-bias face-contraction assignment, but no completed compatible FEI report/handoff was present at the fresh snapshot. No partner result was invented or awaited synchronously.

## New theorem to reuse

For a selector of bias `s`, let

`a = P(G0=0,G1=1)`, `b = P(G0=1,G1=0)`, `d=a+b`, `Delta=a-b`,

and

`E = d-Delta^2 = d(1-d)+4ab`.

At a Poincare-equality face `W0=D0=0`,

`W_G(s) = s[W1+(1-s)E]`.

If `W1+E=0`, the entire parent remains a constant/literal equality state and **no quotient is formed**. Otherwise `E>0` and the local Bellman currency is

`K_s=s(1-s)E>0`.

Writing `J_s` for the exact local defect cocycle,

`ell_s = -J_s/K_s`,

and `c1=-D1/W1` when `W1>0`, the global owner margin satisfies the exact identity

`c_G(s) = [W1*c1 + (1-s)*E*ell_s] / [W1+(1-s)*E]`.

Thus the vanishing selector factor cancels *before* taking a limit. The global boundary margin is an exact convex average of the fixed child margin and the local gluing margin. In particular, a common bound `D1+C W1>=0` and `J_s+C K_s>=0` implies `D_G+C W_G>=0` all the way to the face; and a boundary blow-up is equivalent to blow-up of `ell_s`, not to `s->0` itself.

This is directly relevant to the recipient's credit-augmented Bellman supersolution: the boundary state needs only the local inequality

`J_s + C K_s >= 0`

with the source-defined Boolean information credit retained. There is no additional `1/s` boundary loss to budget.

## First nonzero terms

Exactly,

`W_G(s)=s(W1+E)-s^2E`.

If `ell_s -> L`, then

`-D_G(s)=s(W1*c1+E*L)+o(s)`

and

`c_G(s)->[W1*c1+E*L]/[W1+E]`.

No entropy Taylor expansion is needed for this desingularization.

## Next unpaid implication

`FEI-B04-LOCAL-GLUING-BOUND-v1`: prove a finite uniform upper bound for

`ell_s=-J_s/[s(1-s)(d-(q1-q0)^2)]`

for every actual Boolean selector pair with positive denominator under the surviving shaped candidate or another finite-cap potential, retaining the Boolean information credit and child defects; or exhibit a source-valid Boolean split whose local ratio escapes the proposed cap.

Recipient: `account01/B01`. The result does **not** prove FEI and does not validate any retired quadratic coefficient.
