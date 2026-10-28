# account02/B01 — exact two-gate Farkas barrier for the singleton-safe shaped family

**Run:** `20260922T110344Z-account02-B01-fei-r18`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-account02-B01` — **Dual gate constraints on the center**  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_DUAL_FAMILY_BARRIER / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Full uniform-cube FEI remains **OPEN / NOT PROVED**. This report proves a necessary center barrier only for one explicitly defined finite-dimensional repair family. It does not promote a repaired candidate to a universal potential.

## 0. Fresh control/correction state and sources actually used

The run started from `yspennstate/math-research-brain` main `64da1689498fe3b5ae05c2ccbd0b5de76e5085cd`, owner-control revision `2026-09-22.3`, and was refreshed before publication at main `f9aaf6ef22e36842073dee46affc726d6d018164`. The active programme is `FEI-ALL-TEAM-20260922T095941Z`; installation, benchmark, FOREST, BT4, MOC4 and POS3 work is suspended for this slot. The canonical state remains `FEI-20260922T1000Z-v1`; all mandatory correction events `FEI-DELTA-20260922-01` through `-14` were consumed and the live correction inbox was empty at the refresh.


The mathematical premises used are source-pinned:

1. **STRONG_PRIME.** `yspennstate/math-open-problems@f5946fb64d336ed7369de279159643944efc47af:proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T091146Z-strong-prime-shaped-repair/REPORT.md`, Sections 1–4. It supplies the actual 18-input composition-prime witness
   \[
   p_1=223/456,\quad p_2=\cdots=p_{18}=1/2,\quad p_{out}=1019/2048,
   \]
   the exact normalized pivotal weights
   \[
   \alpha_1=57/256,\qquad \sum_{i=2}^{18}\alpha_i=465/256,
   \]
   the base center `Gamma^dagger(1/2)=6.521851214`, and the rigorous strict bracket
   \[
   -0.038023735<D_{\Gamma^\dagger}<-0.038023734.
   \tag{0.1}
   \]

2. **SHAPE_FRONTIER.** `yspennstate/math-open-problems@a5f19f05fa03671fb5ffeb435081ed92e9827e6a:proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T095300Z-shaped-safe-frontier/REPORT.md`, Sections 2–5. It proves universal singleton-restriction safety for a rational member of the family below and, crucially here, gives the later sharper **genuine two-input AND-line obstruction**
   \[
   \varepsilon\le E(r),\qquad r={8004417\over20000000},
   \]
   with exact
   \[
   E(r)=
   {87063976298056383004191692840000000000000000000000000000
    \over
    3837334674058112811005758660502687481768624593225620567041}.
   \tag{0.2}
   \]
   It also supplies the current source candidate center
   \[
   C_*= {8198056603839780478193093835089
   \over1250000000000000000000000000000}
   =6.5584452830718243825\ldots .
   \tag{0.3}
   \]

3. **OTHER-ACCOUNT RESULT APPLIED.** `yspennstate/math-open-problems@374c4874e914c7414abc9109fadf77cfc3947298:proofnet24/P03-fei/fleet-2026-09-22/account03/B05/account03-B05-20260922T104025Z-fei/REPORT.md`, Sections 1–3. It introduced the exact strong-witness payment functional and proved the prior one-parameter family barrier using the older looser necessary ceiling `epsilon<=10625/468288`, obtaining
   \[
   C>6.5584452821060159825\ldots .
   \tag{0.4}
   \]
   I apply its exact linear-payment setup, but replace its old ceiling by the later source-valid AND-line constraint (0.2), yielding a strictly stronger dual certificate below.

The named assignment partner `account03/B01` had **no compatible completed FEI run** under `proofnet24/P03-fei/fleet-2026-09-22/account03/B01/` at the fresh scientific heads checked during this run. I did not wait and did not import that slot's superseded FOREST work. The compatible completed other-account dual result in item 3 was used instead.

A later scientific master file, `yspennstate/math-open-problems@c7fd21f97c4eb821bc25c370c97f56cae0bbd1d7:proofnet24/P03-fei/fleet-2026-09-22/FLEET_TASKS_2026-09-22.md`, records new measurement targets for a read-once-potential normalization. Those measurements are not used as proof premises here; this report keeps the exact strong-prime/shaped-family normalization fixed and therefore does not transfer margins across candidate versions.

## 1. Finite-dimensional family and exact strong-prime payment

Use mean coordinate `m=1-2p` and define the two rational basis directions

\[
A(m)=1-m^4,
\qquad
B(m)=(1-m^2)^3.
\tag{1.1}
\]

Consider additive repairs of the fixed seed

\[
\Gamma_{x,y}(p)
=\Gamma^\dagger(p)+xA(1-2p)-yB(1-2p),
\qquad x\ge0,\ y\ge0.
\tag{1.2}
\]

This is the linearized two-parameter form of `lambda eta_epsilon`, with `x=lambda`, `y=lambda epsilon`. Its center increment is exactly

\[
\Gamma_{x,y}(1/2)-\Gamma^\dagger(1/2)=x-y.
\tag{1.3}
\]

On the strong 18-input source, define

\[
S(x,y)=L_Ax-L_By.
\tag{1.4}
\]

Direct exact substitution of the source biases and pivotal weights gives

\[
L_A={211575825297187673\over203621856882720768}
=1.0390624490721942\ldots,
\tag{1.5}
\]

\[
L_B=
{720628392668455225196366177
\over693703711666428733273669632}
=1.038812940667922\ldots .
\tag{1.6}
\]

Indeed

\[
L_A={57\over256}A(5/228)+{465\over256}A(0)-A(5/1024),
\]

and the analogous identity holds for `L_B`. Since the source defect satisfies the strict upper inequality in (0.1), **any repair that makes this genuine gate nonnegative must satisfy**

\[
S(x,y)>d_0,
\qquad d_0={38023734\over10^9}.
\tag{1.7}
\]

This is a necessary gate constraint, not a sufficient universality statement.

## 2. The second genuine gate constraint

Restrict attention to the assignment-relevant class in which the additive direction itself is required to be **universally singleton-restriction safe**. This is the proved source-valid mechanism used by the current shaped candidate; it is strictly narrower than the broad globally-safe cone whose local-selector implication is marked `NEEDS_REVALIDATION` in the correction ledger.

For the actual two-input AND gate and exact bias `r=8004417/20000000`, SHAPE_FRONTIER proves that the local singleton-restriction inequality forces

\[
{y\over x}\le E(r)
\tag{2.1}
\]

whenever `x>0`. Write the numerator and denominator in (0.2) as

\[
N=87063976298056383004191692840000000000000000000000000000,
\]

\[
D=3837334674058112811005758660502687481768624593225620567041.
\]

Then the exact second gate constraint is simply

\[
T(x,y):=Nx-Dy\ge0.
\tag{2.2}
\]

No unproved converse is used: universal singleton-restriction safety implies this particular genuine-gate inequality, which is all the dual argument needs.

## 3. Exact Farkas certificate

Let `c=(1,-1)`, `s=(L_A,-L_B)` and `t=(N,-D)`. Define

\[
\kappa={D-N\over DL_A-NL_B}
\tag{3.1}
\]

and

\[
\beta={L_A-L_B\over DL_A-NL_B}.
\tag{3.2}
\]

All four quantities `D-N`, `L_A-L_B`, and `DL_A-NL_B` are strictly positive, so

\[
\kappa>0,\qquad \beta>0.
\tag{3.3}
\]

Exact rational arithmetic gives the coefficient identity

\[
\boxed{
(1,-1)=\kappa(L_A,-L_B)+\beta(N,-D).
}
\tag{3.4}
\]

Equivalently, **for every pair `(x,y)`**,

\[
\boxed{
x-y=\kappa S(x,y)+\beta T(x,y).}
\tag{3.5}
\]

This is the requested finite nonnegative Farkas combination of the two exact source gate constraints. Applying (1.7), (2.2), and positivity of the multipliers yields

\[
x-y>\kappa d_0.
\tag{3.6}
\]

The exact multiplier is

\[
\kappa=
{2481056883611677820411383499489394345818195191383463971821673286778526747328512
\over
2577987413130097731815030453151470049543709179161775267109737344625404822891657},
\tag{3.7}
\]

and the corresponding maximum strong-witness payment per unit center allowed by this necessary two-gate system is

\[
\kappa^{-1}=
{2577987413130097731815030453151470049543709179161775267109737344625404822891657
\over
2481056883611677820411383499489394345818195191383463971821673286778526747328512}
\]

\[
=1.0390682415057400901163096420403996485\ldots .
\tag{3.8}
\]

The exact `beta` is positive and is checked in `CHECK.py`; it is tiny only because `(N,D)` was left in the source's unnormalized integer scaling.

## 4. New necessary center barrier and comparison

Since

\[
\Gamma^\dagger(1/2)={3260925607\over500000000}=6.521851214,
\]

(3.6) proves the family barrier

\[
\boxed{
\Gamma_{x,y}(1/2)>
{8453794693490283414456762500544729467463887461248205727128972786378852618684856373412703
\over
1288993706565048865907515226575735024771854589580887633554868672312702411445828500000000}
}
\tag{4.1}
\]

or numerically

\[
\boxed{
\Gamma_{x,y}(1/2)>6.5584452821094235394849468470378889886\ldots .
}
\tag{4.2}
\]

This is a strict **necessary** bound for every repair in the two-parameter shaped family whose additive direction is universally singleton-restriction safe and which repairs the certified strong Numaro witness. It is not a lower bound on the true FEI constant and not a proof that any endpoint direction is universally safe.

The prior account03/B05 family barrier (0.4), derived from the older two-input ceiling, is sharpened by

\[
3.4075569542063482092548071221078\times10^{-12}.
\tag{4.3}
\]

The current source candidate (0.3) lies only

\[
\boxed{
9.6240084306952822103331101139832\times10^{-10}
}
\tag{4.4}
\]

above this new exact necessary floor. Thus, **inside this particular safe shaped family, the strong witness plus one exact two-input gate leave less than one nanounit of center room** between the present candidate and the best possible necessary floor obtainable under the certified defect bracket (0.1).

This is the substantive conclusion: scalar retuning of this family is quantitatively exhausted at the `1e-9` center scale unless either the strong-prime defect enclosure is sharpened or the shape family itself changes.

## 5. Verification

`CHECK.py` is a standard-library exact-`Fraction` checker. It was executed before publication. It reconstructs `L_A,L_B` from the exact strong-source biases and pivotal weights; verifies positivity of all dual denominators; checks the exact vector identity (3.4); computes the strict center floor; verifies that it is larger than the prior source floor; and verifies that the current candidate is still above it. The captured output ends `STATUS=PASS` and records every exact rational and decimal comparison.

The checker is a verification of this finite rational dual argument only. It does not verify the full source truth table, the source's Bernstein continuum proof, or full FEI; those remain scoped to their pinned source reports.

## 6. Partner status, first unpaid implication, and next recipient

The named partner `account03/B01` did not yet have a compatible completed FEI artifact at the fresh scientific heads observed in this run, so no partner theorem was fabricated or replaced by stale FOREST material. The exact other-account result actually consumed was account03/B05's prior dual family barrier, and this run tightens it using the later account01/B18 source obstruction.

**First unpaid implication after this result:** move beyond the essentially exhausted two-basis safe family. A useful next dual target is a genuinely larger source-valid repair cone with at least one additional independently certified physical-restriction direction, and then combine its exact strong-prime payment with genuine two-input/low-arity constraints. Merely retuning `epsilon` again cannot materially lower the known center: (4.4) quantifies the remaining room.

The assignment recipient is `account04/B17`. The shared handoff should carry (3.4), the exact center floor (4.1), and the `9.6240e-10` remaining-family gap, together with the warning that this is a family barrier, not an FEI constant.

## 7. Scope and correction guardrails

- `Gamma^dagger`, coefficients `0.337/0.34`, and the old fixed-potential extremality claim remain refuted at their recorded scopes.
- The broad safe-cone local-selector inference remains `NEEDS_REVALIDATION`; this proof uses only the stronger **singleton-restriction-safe** hypothesis and one direct genuine gate consequence of it.
- No raw-U4, unweighted-L2, fixed-depth-KL or fixed-potential route is revived.
- The exact rare-event/KL credits are not discarded; they are simply not needed for this narrow Path-A dual necessary condition.
- Full FEI remains `OPEN_NOT_PROVED`.
