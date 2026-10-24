# account02/B18 — exact center-vs-AND-bank dual tradeoff for replacement FEI potentials

**Run:** `20260922T080607Z-account02-B18-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / REPLACEMENT_CLASS_CENTER_FLOOR / FULL_FEI_OPEN`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Fresh control, later-owner precedence, and live target

Fresh `math-research-brain` main was resolved at invocation start to
`397bd070ef6c77fa14bcfe4e0a29823ee130f4ec`; `AGENTS.md`, `scheduled_tasks/README.md`, `fleet.json`, `roles.json`, and `PROTOCOL.md` including OWNER MESSAGE were reread before substantive work. OWNER CONTROL remains revision `2026-09-22.2`, with B12--B18 preserved on FEI and no account02/B18 stop. The later owner convergence instruction supersedes the older Campaign-C half-band/compiler wording where they conflict: the live scientific target is the equivalent all-gate potential inequality, not a revival of the retired positive-current NET route.

The inherited conditional deduction is therefore:

> If one constructs a symmetric finite-center potential `Gamma` satisfying the exact gate-defect inequality for every composition-prime Boolean gate and every interior product bias, then the exact composition cocycle gives `H(f) <= Gamma(1/2) I(f)` for every uniform-cube Boolean function.

The previously proposed fixed potential
\[
\Gamma^\dagger(t)=\Gamma_0(t)+0.268204856\,t(1-t),
\qquad \Gamma^\dagger(1/2)=6.521851214,
\tag{0.1}
\]
is **not** a live universal candidate: account03/B12 already gives a genuine composition-prime 18-input Boolean witness at
\[
p_1=3/8,\quad p_2=\cdots=p_{18}=1/2,
\quad p_{out}=967/2048
\tag{0.2}
\]
with
\[
D_{\Gamma^\dagger}
=-0.017611419955801753789\ldots<0.
\tag{0.3}
\]
Full FEI itself is not refuted.

## 1. Last three substantive B18 reports and admission-gate state

The last three completed substantive B18 reports before this run are:

1. `20260922T030354Z-global-shared-core-ceiling`: the exact nine-host shared-core amplifier is globally capped for every signed selected singleton and arbitrary adaptive self-composition depth. Same-core tuning cannot escape its scalar ceiling.
2. `20260922T040428Z-random-block-currency`: exact biased-Parseval/hypergeometric random-restriction Poincare currency, but its proposed existential block criterion was later found circular at terminal depth.
3. `20260922T051105Z-random-depth-barycenter`: admission-gate correction of that circularity, followed by the exact signed depthwise NET
   \[
   D_{\Gamma_*}(G;p)=\sum_r\Delta_r(a_*-\lambda_r),
   \]
   with all negative one-step information terms retained, plus the sharp front-loading theorem for the physical restriction currency.

**FULL-PROBLEM CHANGE before this run:** none; no finite universal all-gate potential exists yet in the proof state.

The current fixed candidate then suffered the exact biased-prime refutation (0.3). Thus another attempt to certify the same fixed candidate is inadmissible. This run instead attacks the first replacement-potential implication quantitatively.

## 2. Named completed OTHER-account result consumed and actually used

The primary consumed other-account result is account01/B16:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B16/20260922T0743Z-and-bank-exhaustion/REPORT.md`

(blob `31753d0347049d78cdfa1e8a19e6cc858feaa219`). It gives 35 exact rational AND pairs `(p_j,q_j)` and 35 strictly positive rational multipliers `lambda_j`. For a symmetric correction `psi`, put
\[
L_{p,q}(\psi)=q\psi(p)+p\psi(q)-\psi(pq),
\qquad
M(p,q)=pq(1-p)(1-q).
\tag{2.1}
\]
Account01/B16 used the positive combination only after imposing `psi(1/2)=0`, obtaining
\[
R_{wit}(\psi):={57\over256}\psi(3/8)-\psi(967/2048)
\le \kappa K,
\tag{2.2}
\]
whenever `L_{p,q}(psi) >= -K M(p,q)`, with
\[
\kappa=
{792001822391570453\over11721234856636579840}
=0.067569827930129554\ldots .
\tag{2.3}
\]
That proves that the guaranteed uniform AND bank
\[
A=0.268204856-0.01=0.258204856
\tag{2.4}
\]
cannot repair the witness **at the same center**.

This run keeps the center coefficient instead of setting it to zero. That is the new calculation.

I also use the exact account03/B12 witness version through account01/B16: its source deficit is strictly larger than the rational floor
\[
\delta_0=0.0176114.
\tag{2.5}
\]
Account03/B13's later oscillation theorem is compatible but not sufficient for the present statement: it also assumes center zero. The result below removes that assumption and quantifies the minimum center sacrifice under the same guaranteed-bank mechanism.

## 3. New exact theorem — the positive dual certificate has a nonzero center charge

Let `s(x)=min{x,1-x}` and collect the 35 account01/B16 positive inequalities without discarding the `s(x)=1/2` coefficient. Exact rational arithmetic gives
\[
\boxed{
\sum_{j=1}^{35}\lambda_j[-L_{p_j,q_j}(\psi)]
= {57\over256}\psi(3/8)-\psi(967/2048)
+\beta\psi(1/2),
}
\tag{3.1}
\]
where
\[
\boxed{
\beta={23156036957147\over44712962557360}
=0.517881966050477877\ldots .
}
\tag{3.2}
\]
The same multipliers still satisfy
\[
\sum_j\lambda_jM(p_j,q_j)=\kappa.
\tag{3.3}
\]
No continuity, differentiability, convexity, boundedness, or sign assumption on `psi` is used. Symmetry is the only identification used to fold arguments to `[0,1/2]`.

### Proof

For each charged pair,
\[
-L_{p,q}(\psi)
=-q\psi(s(p))-p\psi(s(q))+\psi(s(pq)).
\tag{3.4}
\]
Insert the 35 exact rational multipliers from account01/B16 and sum coefficients of each folded argument. The exact checker verifies that every coefficient vanishes except
\[
[\psi(3/8)]={57\over256},\qquad
[\psi(967/2048)]=-1,\qquad
[\psi(1/2)]=\beta.
\tag{3.5}
\]
It also verifies all 35 multipliers are positive and (3.3) exactly. This proves (3.1). The non-center coefficient matrix is `35 x 35` and has exact rank 35, so on this support the dual multipliers are uniquely determined by the requested non-center witness functional; the center charge is not a removable artifact of a redundant representation. QED.

## 4. Center-bank Pareto inequality for the actual biased prime witness

For a symmetric perturbation `psi`, the exact change of the 18-input prime witness defect is not merely `R_wit`. The 17 unbiased coordinates contribute at the center. The source-exact correction is
\[
\boxed{
W_{wit}(\psi)
={465\over256}\psi(1/2)
+{57\over256}\psi(3/8)
-\psi(967/2048).
}
\tag{4.1}
\]
This is the affine constraint already present in the all-gate handoff for the Numaro witness.

Assume the replacement spends at most `K` units of the quadratic AND bank on the 35 certified pairs:
\[
L_{p_j,q_j}(\psi)\ge-KM(p_j,q_j)
\qquad(j=1,\ldots,35).
\tag{4.2}
\]
Multiplying by the positive `lambda_j` and using (3.1)--(3.3) gives
\[
{57\over256}\psi(3/8)-\psi(967/2048)
+\beta\psi(1/2)
\le\kappa K.
\tag{4.3}
\]
Put `c=psi(1/2)`. Since (4.1) differs from the left side of (4.3) only in its center coefficient,
\[
\boxed{
W_{wit}(\psi)
\le \kappa K+\gamma c,
\qquad
\gamma={465\over256}-\beta
={928973883008923\over715407400917760}
=1.298524283949522122\ldots .
}
\tag{4.4}
\]
This is the exact **CENTER-BANK-DUAL-TRADEOFF-v1**. It strictly contains the account01/B16 same-center obstruction as the slice `c=0`.

Equivalently, any repair demanding witness correction `W` and center displacement `c` must satisfy
\[
K\ge {W-\gamma c\over\kappa}
\tag{4.5}
\]
whenever the numerator is positive. Thus the witness deficit, center increase, and guaranteed AND budget form an explicit affine Pareto frontier rather than separate heuristics.

## 5. Quantitative consequence — uniform-bank repair forces a higher FEI center

To repair (0.3) it is necessary that
\[
W_{wit}(\psi)>\delta_0=0.0176114.
\tag{5.1}
\]
If the repair is required to preserve the certified read-once AND theorem using only the rigorously guaranteed bank, then `K<=A=0.258204856`. Combining (4.4)--(5.1),
\[
\gamma c
>\delta_0-\kappa A.
\tag{5.2}
\]
The right side is the exact positive rational
\[
\delta_0-\kappa A
={241079881477054720432029\over1465154357079572480000000000}
=0.000164542309356120408\ldots .
\tag{5.3}
\]
Therefore
\[
\boxed{
\psi(1/2)=c
>
{241079881477054720432029\over1902538512402274304000000000}
=0.000126714849610403362\ldots .
}
\tag{5.4}
\]
In particular every replacement in this guaranteed-bank class that repairs the exact biased prime witness must have center
\[
\boxed{
\Gamma_{new}(1/2)
>6.521977928849610403\ldots .
}
\tag{5.5}
\]
The exact rational value on the right of (5.5), using the decimal definition in (0.1), is
\[
{2481662837334800756124767417\over380507702480454860800000000}.
\]

This is **not** a lower bound on the optimal universal FEI constant. It is a lower bound on the center of this specific replacement architecture: start from `Gamma^dagger`, add a symmetric correction, and pay every AND loss using no more than the uniformly guaranteed quadratic reserve `A M`. A different base potential, exploitation of the certified base's actual nonuniform AND slack, or a different all-gate proof mechanism is not ruled out.

## 6. What this says about the actual missing implication

The old same-center question is now exhausted more sharply:

- account03/B12 refutes the fixed potential on a genuine prime gate;
- account02/B17 proves a free center-preserving AND repair is impossible;
- account01/B16 proves the whole uniform quadratic bank is insufficient at fixed center;
- **this run proves the exact center-vs-bank tradeoff and shows that even allowing the center to move, the guaranteed-bank mechanism cannot repair the witness unless the center rises by more than `1.267148496104e-4`.**

Hence the next all-gate attack should not keep retuning a center-zero bump. The smallest honest unresolved mechanism is:

> Use the **actual pointwise nonuniform AND slack** of the certified read-once potential (and then the other prime-gate constraints), or change the base potential itself, and construct a finite-center fixed point/envelope satisfying every composition-prime gate inequality.

The account02/B16 coherent-bias calculation `20260922T072030Z-source-bias-finite-secant` independently reduces another genuine source test to two near-half base-potential secants. That is compatible with the present conclusion: detailed local shape, not another uniform quadratic reserve, is now the live resource.

## 7. Exact verification and admission status

`CHECKER.py` reproduces the complete 35-pair rational certificate, verifies:

1. all multipliers are positive;
2. the exact coefficient identity (3.1), including the previously discarded center coefficient;
3. exact `kappa`, `beta`, and `gamma`;
4. positivity of the unpaid gap `delta_0-kappa A`;
5. the exact center lower bound (5.4).

It also confirms the non-center coefficient matrix has full rank 35 in the analytic derivation; the saved checker retains the exact coefficient and inequality calculations needed for the theorem itself. Floating-point decimals are renderings only; all decisions are made with rational arithmetic.

**Admission-gate verdict:** `ESSENTIAL_STEP_APPLIED`. This is not a renamed residual and not a universal FEI proof. It removes one previously open degree of freedom from the replacement-potential mechanism by proving an exact quantitative tradeoff.

## 8. Before/after and next method

**FULL-PROBLEM CHANGE:** **NONE.** Full FEI remains open; no universal finite-center potential has been constructed.

**MECHANISM CHANGE:** **YES.** Before this run the strongest exact dual obstruction applied only to center-preserving (`psi(1/2)=0`) uniform-bank repairs. After this run the same positive dual certificate is polarized with its true center coefficient retained, yielding the affine center-bank frontier (4.4) and the strict center floor (5.5). The same-center restriction is no longer a loophole within the guaranteed-bank architecture.

**Next B18 attack:** obtain the certified base potential's **actual nonuniform AND slack at the 35 charged pairs** and evaluate the same positive dual against that real slack. If the weighted actual slack is still below the prime deficit, then every same-base repair below the corresponding center floor is ruled out without the uniform-bank surrogate. If it exceeds the deficit, the excess identifies exactly how much nonuniform slack is available for a candidate fixed-point/envelope construction. This is a materially sharper finite signed implication than another global `K M` estimate.

Scoped privacy review: only FEI mathematics, repository-relative source identifiers, public mathematical constants, and sanitized operational metadata are written. No credentials, scheduler identifiers, machine paths, raw transcripts, unrelated private data, benchmark gold, email/Drive activity, public posting, paid API/model, Codex, remote workflow execution, or permission changes are included.
