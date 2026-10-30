# fleet04/B18 — aggregate robust-trigger overlap collapses to support-hidden curvature

**Run:** `20260922T101158Z-b18-fei-a11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / A-B_INTERFACE_INTEGRATION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim.

## 0. Current correction state and exact peer inputs

The current owner control converges FEI work on the all-gate potential inequality.  The earlier claim that the read-once base potential is universally extremized by AND/decomposable gates is now source-exactly refuted by the composition-prime 18-input Numaro witness; this is **not** a refutation of FEI.

The newest completed fleet01/B18 result consumed here is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T095300Z-shaped-safe-frontier/REPORT.md`, scientific commit `a5f19f05fa03671fb5ffeb435081ed92e9827e6a`.

It proves the universally safe physical-singleton direction

\[
\eta_{\varepsilon_*}(p)
=1-(1-2p)^4-\varepsilon_*[1-(1-2p)^2]^3,
\qquad
\varepsilon_*={56721646463783\over2500000000000000},
\]

and uses it to repair the strongest currently certified Numaro witness with the finite candidate

\[
\Gamma_*=\Gamma^\dagger+\lambda_*\eta_{\varepsilon_*},
\qquad
\Gamma_*(1/2)=6.5584452830718245\ldots .
\]

Its universal prime-gate obligation is still unpaid.  The point relevant to the A/B interface is that the added `eta` cocycle is nonnegative on **every actual original-coordinate reveal**; therefore it consumes none of the crossing/curvature refunds used below.  It may be carried through a restriction induction without double spending those banks.

Fresh fleet04 dependencies are:

* B12, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T094436Z-robust-row-codimension-staircase/REPORT.md`, commit `a1b2a93210fe7cc871cd10c5bbbf43b1b983a254`;
* B13, commit `c50e06733fc1e7f109e20dbb1a0013d67aa71dc7`, which independently proves universal singleton safety in the same cubic-corrected quartic family at `epsilon=0.02268865`; fleet01/B18's later exact value above strictly sharpens that scalar and is used instead of summing two copies of the same repair;
* B14, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260922T093843Z-mux-coordinate-marginal-credit/REPORT.md`, commit `d760311c3190002395f33b11fad6d12e5950be56`, which proves an exact realizable MUX data-block information credit.  That theorem is retained at its family-specific scope and is **not** promoted into the universal estimate below.

The A-side curvature bank is the source-exact fleet01/B18 theorem
`fleet01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md` used by the preceding B18 integration.  The B-side exact visible/hidden law and surplus theorem are

* `fleet04/B18/20260922T081002Z-visible-hidden-curvature-split/REPORT.md`, commit `40d53b2d7f2c8b388a95d4abd82221321f6fcfcf`;
* `fleet04/B18/20260922T091529Z-surplus-hidden-curvature/REPORT.md`, commit `200e3fd37fe201f78d882ba8809414d201efb829`.

No raw `sum d_i=O(J)` estimate, prescribed-coordinate entropy payment, fixed-relative near-subcube theorem, blind arity induction, or refuted AND-extremality claim is used.

## 1. Compact honest proof chain

Work in the centered character gauge and suppose a minimum restriction descendant is an actual `F/J`-critical core of ratio `rho>4`.  The inherited curvature-refunded inequality makes it all-block terminal at `K=4`.  The exact zero-depth branch is already closed: if every folded depth defect vanishes, Boolean integrability forces a character times a signed one-point defect (irrelevant variables allowed), and `H<4J`.

For the positive-defect branch, B12's fresh theorem says a relative-`1/16` near-subcube derivative row has a physical trigger set `F_i` of codimension `r_i>=3`, and every trigger `k in F_i` satisfies a quantitative support-boundary lower bound.  B12 explicitly left one obstruction: **different rows can reuse the same trigger coordinates**, so its single-row address payment did not sum.

The preceding B18 theorem paid the crossing-visible part of mixed curvature but left a hidden bank `U_4`.  The first missing implication is therefore: can the B12 trigger-overlap sum be paid by the A-side crossing bank plus a strictly identified part of that hidden bank, without charging the same physical influence once per row?

The answer below is yes.  It resolves this overlap step exactly, but leaves a smaller support-hidden bank, the nonrobust rows, and the universal all-prime-gate obligation unpaid.  Thus there is no FEI closure.

## 2. Split the old hidden bank one step further

For distinct coordinates `i,k`, retain the preceding notation

\[
c_{k\leftarrow i}=c_k(\{i\}),
\qquad p_{ki}=\Pr[1_{E_k}(Y)\ne1_{E_k}(Y+e_i)],
\qquad o_{ki}\ge0.
\]

The exact B18 visible/hidden theorem proves

\[
2c_{k\leftarrow i}\le p_{ki},
\qquad
\omega_{ki}=p_{ki}-2c_{k\leftarrow i}+4o_{ki}\ge0.
\]

Define the **support-hidden** term

\[
\boxed{h_{ki}:=p_{ki}-2c_{k\leftarrow i}\ge0.}
\tag{2.1}
\]

Then

\[
\omega_{ki}=h_{ki}+4o_{ki}.
\tag{2.2}
\]

With

\[
w_k:=4+\mathfrak j'(q_k),
\]

define

\[
\boxed{
H_4:=\sum_{k}\sum_{i\ne k}w_k h_{ki},
\qquad
O_4:=4\sum_k\sum_{i\ne k}w_k o_{ki}.
}
\tag{2.3}
\]

Thus the old hidden bank splits exactly as

\[
\boxed{U_4=H_4+O_4.}
\tag{2.4}
\]

The opposite-sign orientation mode has not been discarded.  It remains in `O_4`; the new point is that the **trigger-address overlap problem itself only depends on support disagreement**, hence only on `H_4`.

## 3. Fresh B12 trigger lower bound and global A-side weights

Let `R` be the set of relative-`1/16` robust rows.  B12 proves that for every `i in R` and every trigger `k in F_i`,

\[
\boxed{p_{ik}\ge {7\over4}q_i.}
\tag{3.1}
\]

The same Boolean-square integrability gives

\[
\boxed{p_{ik}=p_{ki}.}
\tag{3.2}
\]

The preceding B18 terminal-surplus proof also establishes on a `rho>4` critical core

\[
q_k<\frac16,
\qquad
\mathfrak j'(q_k)>\frac{16}{7},
\qquad
w_k>\frac{44}{7}.
\tag{3.3}
\]

Let

\[
R_k:=\sum_{i\ne k}c_{k\leftarrow i}.
\]

The fleet01/B18 curvature bank gives

\[
\sum_k(\rho+\mathfrak j'(q_k))R_k
\le \mathcal P-\operatorname{DTC}(X).
\tag{3.4}
\]

Since `rho>4` and (3.3),

\[
\boxed{
\sum_kR_k\le {7\over44}
[\mathcal P-\operatorname{DTC}(X)].
}
\tag{3.5}
\]

Likewise, by (2.3) and (3.3),

\[
\boxed{
\sum_k\sum_{i\ne k}h_{ki}\le {7\over44}H_4.
}
\tag{3.6}
\]

These are global column payments; they are used once, after summing all trigger incidences.

## 4. New theorem: all robust trigger addresses aggregate without reuse

### Theorem 4.1 — `ROBUST-TRIGGER-OVERLAP-COLLAPSE-v1`

On every centered `F/J`-critical core with `rho>4`, the relative-`1/16` robust rows satisfy

\[
\boxed{
\sum_{i\in R} r_i q_i
\le
{2\over11}[\mathcal P-\operatorname{DTC}(X)]
+{1\over11}H_4.
}
\tag{4.1}
\]

Since B12 also proves `r_i>=3` for every such row,

\[
\boxed{
\sum_{i\in R}q_i
\le
{2\over33}[\mathcal P-\operatorname{DTC}(X)]
+{1\over33}H_4.
}
\tag{4.2}
\]

Using the source-valid scalar bound `P<=2J/ln 2`,

\[
\boxed{
\sum_{i\in R}q_i
\le
{4\over33\ln2}\,\mathcal J+{1\over33}H_4
<0.174873\,\mathcal J+0.030304\,H_4.
}
\tag{4.3}
\]

### Proof

Sum (3.1) over the **actual incidence set**

\[
\mathcal I=\{(i,k):i\in R,\ k\in F_i\}.
\]

Then, using (3.2) and the exact definition (2.1),

\[
\begin{aligned}
\sum_{i\in R}r_iq_i
&=\sum_{(i,k)\in\mathcal I}q_i\\
&\le {4\over7}\sum_{(i,k)\in\mathcal I}p_{ik}\\
&={4\over7}\sum_{(i,k)\in\mathcal I}p_{ki}\\
&={4\over7}\sum_{(i,k)\in\mathcal I}
(2c_{k\leftarrow i}+h_{ki}).
\end{aligned}
\tag{4.4}
\]

All summands are nonnegative, so enlarge the incidence set **once** to all ordered pairs:

\[
\sum_{i\in R}r_iq_i
\le {4\over7}
\left[
2\sum_kR_k+
\sum_k\sum_{i\ne k}h_{ki}
\right].
\tag{4.5}
\]

Insert (3.5)-(3.6):

\[
\frac47
\left[
2\cdot\frac7{44}(\mathcal P-\operatorname{DTC})
+\frac7{44}H_4
\right]
=
\frac2{11}(\mathcal P-\operatorname{DTC})+
\frac1{11}H_4.
\]

This proves (4.1).  B12's terminal staircase gives `r_i>=3`, proving (4.2), and `P<=2J/ln2` gives (4.3).  QED.

## 5. What was actually removed from the obstruction

B12's single-row theorem had already shown

\[
r_iq_i\le\frac87(J-q_i),
\]

but it correctly did not sum this over rows because the same trigger influence may appear in many `F_i`.  Theorem 4.1 performs the sum **before** spending any global bank.  Pairwise Boolean integrability turns every trigger incidence into `p_{ki}`; the A-side posterior-crossing bank pays its visible part once; only the support-hidden residual remains.

Therefore the robust-row address problem no longer carries:

* an ambient dimension factor;
* a raw second-factorial depth bank;
* repeated trigger influence;
* or the opposite-sign curvature term `O_4`.

The last point is a genuine sharpening of the preceding B18 `U_4` reduction.  The orientation term is still required in the exact mixed-curvature law and in other positive-defect estimates, but **it is not needed to pay robust trigger addresses**.  The correct unpaid bank for this particular subproblem is the strictly smaller `H_4<=U_4`.

In the special case `H_4=0`, all robust trigger addresses are paid dimension-freely by the already-existing phase/crossing bank:

\[
\sum_{i\in R}r_iq_i\le {2\over11}(\mathcal P-\operatorname{DTC}),
\qquad
\sum_{i\in R}q_i\le {2\over33}(\mathcal P-\operatorname{DTC}).
\]

This is a conditional branch statement, not a proof that `H_4=0`.

## 6. Integration with the live gate candidate and B14 terminal block

The newest fleet01/B18 shaped direction is safe by a literal physical-singleton inequality.  Hence carrying `lambda_* eta_{epsilon_*}` through any restriction tree can only **increase** the gate defect; it does not spend `P-DTC`, `H_4`, or B14's block-information bank.  This means Theorem 4.1 is compatible with the current repaired candidate `Gamma_*` without double counting.

However compatibility is not universal closure.  `Gamma_*` is known to repair the strongest current Numaro witness, but it has not been proved nonnegative on every composition-prime gate/bias.  Conversely, Theorem 4.1 is a terminal-core restriction theorem and does not by itself prove the all-gate inequality.

B14's fresh MUX theorem is also retained without reuse: on the genuine physical data block `{D_0,D_1}`, every child is terminal and the exact nonmodular information credit satisfies the analytic central-square bound

\[
{\mathcal C_D\over W_M}\ge
\log_2{800000\over19683}=5.3449779679\ldots .
\]

That credit belongs to the MUX block cocycle and is not used in (4.1).  No family-specific MUX estimate is promoted to an arbitrary-gate claim.

## 7. Remaining unpaid arrows

The smallest honest restriction-side remainder is now sharper:

1. **UNPAID `H_4`:** pay or realizably eliminate the support-hidden bank
   \[
   H_4=\sum_{k,i\ne k}(4+\mathfrak j'(q_k))
   [p_{ki}-2c_{k\leftarrow i}]
   \]
   on positive-defect terminal critical cores.  The opposite-sign component is no longer part of the robust-address subproblem.
2. **UNPAID nonrobust rows:** obtain an influence-relative positive-defect estimate or a realizable elimination outside the relative-`1/16` near-subcube class.
3. **UNPAID live all-gate candidate:** prove `D_{Gamma_*}(P;p)>=0` for every composition-prime Boolean gate and every product bias, including boundary limits, or produce a source-valid prime/bias counterexample.

The exact zero-defect classification is preserved unchanged.  All previously posted refutations remain in force.  No conditional item above is promoted into unconditional FEI closure.

## 8. Verification

`CHECK_TRIGGER_OVERLAP.py` contains the exact rational coefficient calculation used in (4.1)-(4.2):

\[
{1\over2(1-2/16)}={4\over7},
\qquad
{4\over7}{2\over44/7}={2\over11},
\qquad
{4\over7}{1\over44/7}={1\over11}.
\]

It also verifies the division by the terminal codimension floor `r_i>=3` and prints the decimal coefficient `4/(33 ln 2)`.  This checker is only arithmetic; the theorem is the analytic argument above.

No benchmark gold, mocks, paid/remote compute, workflow dispatch, email/Drive material, unrelated private data, public posting, permission changes, or weakened source/proof gate were used.
