# fleet03/B18 — exact quartic safe-cone frontier and repaired Gibbs target

**Run:** `20260922T092424Z-fleet03-B18`  
**Classification:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_REPLACED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact Campaign-B target and old missing implication

The previous B18 target was

\[
\Gamma^\dagger(u)=\Gamma_0(u)+0.268204856\,u(1-u),
\qquad C^\dagger=\Gamma^\dagger(1/2)=6.521851214,
\]

with the exact Gibbs normalization `B-GIBBS-KL-v1`

\[
D_{\Gamma^\dagger}(G;p)
=V_q\left[D_{\mathrm{KL},2}(w^+\|\nu_x^+)
-\log_2\frac{A_0}{x_q}\right].
\]

That fixed candidate is now source-exactly refuted by the composition-prime 18-input Numaro gate.  More strongly, the same actual Boolean truth table with one core bias

\[
p={223\over456},\qquad q={1019\over2048}
\]

has

\[
-0.038023735<D_{\Gamma^\dagger}<-0.038023734.
\tag{0.1}
\]

The immediately following quadratic replacement `Gamma_0+0.34 p(1-p)` is also refuted by this same source: its certified defect is still below `-0.01937`.

So the old missing implication, universal nonnegativity of `B-GIBBS-KL-v1` for `Gamma^dagger`, is **REFUTED**, not merely unpaid.  This run replaces the candidate while keeping the same exact Gibbs/Shannon residual architecture.

## 1. Completed cross-account theorem consumed substantively

The named completed cross-account artifact is fleet04/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T071535Z-quartic-universal-repair/REPORT.md`.

It proves for every finite Boolean gate, every product-bias vector and

\[
\eta_4(u):=u(1-u)(1-2u(1-u))={1-(1-2u)^4\over8}
\]

that

\[
\boxed{
\sum_i \alpha_i\eta_4(p_i)-\eta_4(q)\ge0,
\qquad \alpha_i={{\rm It}_i(G;p)\over V_{p_i}}.
}
\tag{1.1}
\]

Therefore adding any nonnegative multiple of `eta_4` can never decrease any all-gate defect.  This is an actual Boolean theorem; its proof uses restriction induction and the Boolean disagreement constraint, not an arbitrary spectral relaxation.

For comparison, the ordinary quadratic direction

\[
\eta_2(u)=u(1-u)
\]

is also universally safe because its defect currency is

\[
\sum_i\alpha_i\eta_2(p_i)-\eta_2(q)
={I_p-V_q\over4}\ge0
\tag{1.2}
\]

by product-space Poincare.

## 2. Exact strong-witness currencies

On the strong Numaro source (0.1), the source checker gives the exact quadratic and quartic defect currencies

\[
M_2={62098577\over239075328}
=0.25974481565910473\ldots,
\tag{2.1}
\]

\[
L_4={211575825297187673\over1628974855061766144}
=0.12988280613402428\ldots.
\tag{2.2}
\]

A repair

\[
\eta=a\eta_2+b\eta_4,\qquad a,b\ge0,
\]

changes this witness defect by

\[
aM_2+bL_4,
\tag{2.3}
\]

while its center cost is exactly

\[
\Delta C={a\over4}+{b\over8}.
\tag{2.4}
\]

Define payment per unit center

\[
E_2:=4M_2,
\qquad E_4:=8L_4.
\]

Exact rational arithmetic gives

\[
\boxed{
E_4-E_2
={16938576520025\over203621856882720768}>0.
}
\tag{2.5}
\]

Numerically,

\[
E_2=1.038979262636419\ldots,
\qquad
E_4=1.039062449072194\ldots.
\]

### Theorem 2.1 — quartic is the exact optimum in the proved two-generator safe cone

Among all universally safe repairs `a eta_2+b eta_4` with `a,b>=0` that neutralize the strong Numaro witness, the minimum possible center increment is attained by a **pure quartic** repair.

Indeed (2.3)-(2.5) imply

\[
aM_2+bL_4
={a\over4}E_2+{b\over8}E_4
\le E_4\Delta C.
\]

If `d=-D_{Gamma^dagger}>0`, neutralization requires `aM_2+bL_4>=d`, hence

\[
\boxed{
\Delta C\ge{d\over E_4}={d\over8L_4}.
}
\tag{2.6}
\]

Equality in this two-generator cone forces `a=0`.  From the rigorous lower bound `d>0.038023734`, every such repair has

\[
\boxed{
\Gamma(1/2)>
6.521851214+{0.038023734\over 8L_4}
=6.558445486109393\ldots .
}
\tag{2.7}
\]

This is a candidate-design theorem, not an FEI lower bound: it is a lower bound only for repairs inside this particular universally-safe cone around the already-refuted seed.

## 3. New immutable candidate: `LIMIT-PRIME-GATE-LIFT-Q4-v1`

Choose the rational quartic scale

\[
\boxed{\lambda_Q={58551\over200000}=0.292755.}
\tag{3.1}
\]

Define

\[
\boxed{
\Gamma_Q(u):=\Gamma^\dagger(u)+\lambda_Q\eta_4(u).
}
\tag{3.2}
\]

Its center is exactly

\[
\boxed{
C_Q=\Gamma_Q(1/2)
={6558445589\over10^9}=6.558445589.
}
\tag{3.3}
\]

This is only about `1.02e-7` above the upper endpoint obtained by replacing the true strong-witness deficit by the rigorous coarse interval in (0.1).  More importantly it rigorously repairs the strong witness itself: using the worst allowed deficit `0.038023735`,

\[
\begin{aligned}
D_{\Gamma_Q}
&> -0.038023735+\lambda_Q L_4\\
&={1437702884772647393\over
13574790458848051200000000}\\
&>1.05909\times10^{-7}>0.
\end{aligned}
\tag{3.4}
\]

By (1.1), this move cannot make any previously nonnegative gate/bias pair negative.  In particular it also repairs the earlier weaker `p=3/8` Numaro witness.

The tempting higher-even-moment extension is not being smuggled into the candidate: fleet03/B17 has an exact Boolean four-input counterexample showing the pure `eta_r=[1-(1-2u)^r]/(2r)` directions are unsafe for every even `r>=6`.  Thus (3.2) uses only a proved universally safe direction.

## 4. Common Shannon target: `B-GIBBS-Q4-v1`

The completed fleet02/B15 Gibbs theorem is potential-agnostic, so it applies verbatim to `Gamma_Q`.  For the actual biased Boolean spectral law

\[
w(S)=\widehat G_p(S)^2,
\qquad q=\Pr[G=-1],
\qquad v=V_q,
\]

define original-coordinate prices

\[
a_i^Q={\Gamma_Q(p_i)+h_2(V_{p_i})\over V_{p_i}},
\qquad x_i^Q=2^{-a_i^Q},
\]

and

\[
A_0^Q=\prod_i(1+x_i^Q)-1,
\qquad
x_q^Q=2^{-[\Gamma_Q(q)+h_2(V_q)]/V_q}.
\]

Let `nu_Q^+` be the corresponding product Gibbs law conditioned on nonempty Fourier support.  Then exactly

\[
\boxed{
D_{\Gamma_Q}(G;p)=v\,R_Q(G;p),
}
\tag{4.1}
\]

where the immutable normalized residual is

\[
\boxed{
R_Q(G;p):=
D_{\mathrm{KL},2}(w^+\|\nu_Q^+)
-\log_2{A_0^Q\over x_q^Q}.
}
\tag{4.2}
\]

This keeps the actual signed Boolean Fourier law, every original coordinate label through `a_i^Q`, and the full conditional relative-entropy credit.  No negative KL credit is discarded.  Constants are the separate exact base case `v=0`.

The smallest universal proof chain is now:

1. **PROVED:** exact identity (4.1)-(4.2) for every nonconstant Boolean gate and every interior product bias;
2. **PROVED:** the quartic move from `Gamma^dagger` to `Gamma_Q` is globally defect-monotone and fixes the strongest source-certified Numaro obstruction currently used here;
3. **UNPAID:** prove
   \[
   \boxed{R_Q(P;p)\ge0}
   \tag{4.3}
   \]
   for every finite composition-prime Boolean gate `P` and every interior product-bias vector `p`, including all boundary limits required by the all-gate composition theorem;
4. **CONDITIONAL:** once (4.3) plus the already-recorded decomposition/base cases is universal, the all-gate theorem gives FEI with finite constant `C_Q=6.558445589`.

I do **not** promote step 4 to an unconditional theorem.  Full FEI remains open.

## 5. Refutation attempt and why this is genuine movement

Two plausible repairs are now source-exactly dead:

- the old `Gamma^dagger` candidate is refuted by (0.1);
- the subsequent pure quadratic coefficient `0.34` remains negative on the same strong witness, so merely raising the old scalar lift to that value is also refuted.

Inside the rigorous two-generator safe cone, Theorem 2.1 says another quadratic/quartic mixture cannot beat the pure-quartic center cost on this witness.  So repeated tuning of the same two coefficients is no longer the next useful attack.

A materially different next mechanism is required: either

- produce a new genuine Boolean prime/bias falsifier of `Gamma_Q`, or
- enlarge the universally-safe repair cone with a genuinely shaped non-polynomial (or otherwise source-valid) direction and prove its gate safety, or
- directly prove the low-price Gibbs residual (4.3) using the exact packet/JS and child-defect credits without replacing them by a credit-free scalar bound.

## 6. Exact handoff

- **candidate_version:** `LIMIT-PRIME-GATE-LIFT-Q4-v1`.
- **common_target_version:** `B-GIBBS-Q4-v1`.
- **old_missing_implication:** universal nonnegativity of `B-GIBBS-KL-v1` for `Gamma^dagger`.
- **old_claim_status:** **REFUTED** by the source-certified strong Numaro witness; the interim `+0.34 p(1-p)` candidate is also refuted.
- **new_proved_inference:** exact safe-cone efficiency ordering `E4>E2`; pure quartic is optimal in `cone{eta2,eta4}` for neutralizing the strong witness; the rational `lambda_Q=0.292755` repairs it with rigorous positive slack while worsening no gate.
- **replacement_obligation:** prove `R_Q(P;p)>=0` universally or find an actual Boolean prime falsifier; do not discard conditional KL/JS credits or coordinate prices.
- **consumed_peer_artifact:** fleet04/B17 `20260922T071535Z-quartic-universal-repair/REPORT.md`.
- **applied_to_claim:** global safety of the quartic candidate move and exact optimization of center cost in the quadratic/quartic safe cone.
- **next_recipients:** fleet02/B17 for a direct adversarial search against `Gamma_Q`; fleet03/B15 for the exact Gibbs/packet residual with the new prices; fleet04/B17 for any strictly richer proved safe repair direction.
- **implication_to_full_FEI:** conditional all-gate closure at constant `6.558445589` if and only if the remaining universal gate residual and boundary/decomposition obligations are discharged.  **Full FEI remains OPEN / NOT PROVED.**
