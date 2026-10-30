# fleet04/B13 — near-optimal universal singleton-restriction repair in the cubic correction family

**Outcome:** `ESSENTIAL_STEP_APPLIED / UNIVERSAL_SAFE_DIRECTION_OPTIMIZED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated native brain retrieval plus receiver-context consumption occurred.  
**Model self-report:** `GPT-5.6 Sol`. Configured reasoning/provider counters are not exposed.

## 0. Active target, correction state, and peer inputs


The newest completed compatible other-account result consumed substantively is fleet02/B17

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B17/20260922T091146Z-strong-prime-shaped-repair/REPORT.md`,

creation commit `f5946fb64d336ed7369de279159643944efc47af`.
It supplies the stronger source-valid composition-prime Numaro adversary

\[
p_1={223\over456},\qquad p_2=\cdots=p_{18}=\frac12,
\qquad p_{\rm out}={1019\over2048},
\]

with

\[
\alpha_1={57\over256},\qquad
\sum_{i=2}^{18}\alpha_i={465\over256},
\]

and the rigorous defect bracket

\[
-0.038023735<D_{\Gamma^\dagger}<-0.038023734.
\tag{0.1}
\]

It also proves that the formerly executed shaped-repair scale is too small on this stronger source, then repairs it with the universally safe direction inherited from fleet01/B14 at center

\[
C_{\rm peer}=6.55844529582746.
\tag{0.2}
\]

That result changes the argument here decisively: instead of optimizing a repair against the obsolete weaker `p_1=3/8` witness, this run optimizes the **universal source-safe direction itself** against the strongest currently certified composition-prime source.

The second essential peer dependency is fleet01/B14

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B14/20260922T091217Z-universal-singleton-repair/REPORT.md`,

commit `63189a15a82c34331909a42fe35786109f3c8a29`. It proves universal singleton-restriction safety for the one-parameter family below at

\[
\varepsilon_0={113009\over5000000}=0.0226018.
\]

This run sharpens that theorem nearly to the exact obstruction threshold of the family.

## 1. The repair family and the source-valid local reduction

For `0<=epsilon<1`, define in mean coordinates `m in [-1,1]`

\[
\phi_\varepsilon(m)
=1-m^4-\varepsilon(1-m^2)^3,
\tag{1.1}
\]

and for a Bernoulli bias `p`

\[
\eta_\varepsilon(p)=\phi_\varepsilon(1-2p).
\tag{1.2}
\]

Since

\[
\phi_\varepsilon(m)
=(1-m^2)\bigl[1+m^2-\varepsilon(1-m^2)^2\bigr]\ge0,
\tag{1.3}
\]

this is symmetric, endpoint-zero and nonnegative.

Fix an actual original coordinate with bias `t`. Let its Boolean restrictions have means `a,b`, and put

\[
\delta=\Pr(G_0\ne G_1),\qquad c=(1-t)a+tb.
\]

Boolean realizability gives the sharp signed constraint

\[
|a-b|\le2\delta.
\tag{1.4}
\]

Because `phi_epsilon(1-2t)>=0`, it is enough to prove the local inequality at the minimum admissible disagreement `delta=|a-b|/2`:

\[
(1-t)\phi_\varepsilon(a)+t\phi_\varepsilon(b)
+{|a-b|\over2}\phi_\varepsilon(1-2t)
-\phi_\varepsilon(c)\ge0.
\tag{1.5}
\]

After exchanging the children if needed, put `d=b-a in [0,2]` and write

\[
a=-1+u(2-d),\qquad b=a+d,\qquad u\in[0,1].
\tag{1.6}
\]

Thus the complete universal problem for this repair direction is a three-variable polynomial nonnegativity problem on the unit cube.

## 2. New theorem: a sharper universally safe direction

### Theorem 2.1 — `B-NEAROPT-SINGLETON-SAFE-DIRECTION-v1`

Put

\[
\boxed{\varepsilon_*={453773\over20000000}=0.02268865.}
\tag{2.1}
\]

Then for **every** finite Boolean gate `G`, every interior product-bias vector, and

\[
\alpha_i={\operatorname{It}_i(G;p)\over V_{p_i}},
\]

one has

\[
\boxed{
\sum_i\alpha_i\eta_{\varepsilon_*}(p_i)
-\eta_{\varepsilon_*}(p_{\rm out})\ge0.
}
\tag{2.2}
\]

Consequently, for every symmetric potential `Gamma` and every `lambda>=0`,

\[
\boxed{
D_{\Gamma+\lambda\eta_{\varepsilon_*}}(G;p)
\ge D_\Gamma(G;p)
}
\tag{2.3}
\]

for every Boolean gate, every arity and every product bias.

### Proof

Let `X=d/2`. Substitute (1.6) into the left side of (1.5), with `d=2X`. The resulting exact rational polynomial

\[
G_{\varepsilon_*}(X,t,u)
\]

has tensor degrees `(6,6,4)` on `[0,1]^3`.

The committed standard-library checker constructs this polynomial from (1.1) exactly in `Fraction` arithmetic, converts its power coefficients to the tensor Bernstein basis, and recursively bisects dyadically by exact de Casteljau subdivision. On any terminal box, nonnegativity of all Bernstein coefficients implies nonnegativity of the polynomial because the Bernstein basis is nonnegative and sums to one.

The exact certificate terminates with

- `159` total boxes including internal nodes,
- `80` terminal boxes,
- `0` unresolved boxes,
- maximum subdivision depth `26`, and
- minimum terminal Bernstein coefficient `0`.

The zero is expected from the genuine equality faces of the local inequality; there is no negative terminal coefficient. Hence (1.5) holds for all `d,t,u`. By (1.4), increasing `delta` from `d/2` only adds the nonnegative amount `(delta-d/2)phi_epsilon(1-2t)`, so the actual Boolean local inequality holds.

Finally reveal original coordinates one at a time. Pivotal probabilities of every unrevealed coordinate are exactly the bias-weighted averages of the corresponding child pivotal probabilities, so the local inequalities telescope to constants. This is the same literal physical-restriction induction as fleet01/B14, now with the sharper exact scalar certificate. That proves (2.2), and (2.3) follows by linearity of the gate defect in the added potential. `QED`.

The proof uses actual original-coordinate restrictions and the Boolean signed constraint (1.4). It is not a sign-free spectral-law relaxation and contains no ambient-dimension continuity loss.

## 3. Near-optimality inside this one-parameter family

The family itself has a source-valid exact obstruction.

Take a genuine two-input Boolean gate with pivot `X` of bias

\[
t={3\over5},
\]

and a second bit `Y` with `Pr(Y=+1)=3/5`. Define

\[
G_0=Y,\qquad G_1=+1.
\]

Then

\[
a=\mathbb EG_0={1\over5},\qquad b=1,
\qquad \delta=\Pr(Y=-1)={2\over5},
\]

and the parent mean is

\[
c={2\over5}{1\over5}+{3\over5}={17\over25}.
\]

For this actual Boolean source the repair currency is exactly

\[
\begin{aligned}
L_{\rm crit}(\varepsilon)
&={4\over5}\phi_\varepsilon(1/5)-\phi_\varepsilon(17/25)\\
&={288\over244140625}\bigl(10625-468288\varepsilon\bigr).
\end{aligned}
\tag{3.1}
\]

Therefore every universally safe member of this exact one-parameter family must satisfy

\[
\boxed{
\varepsilon\le\varepsilon_{\max}:={10625\over468288}
=0.02268902897362306956\ldots .
}
\tag{3.2}
\]

The proved value (2.1) lies only

\[
\boxed{
\varepsilon_{\max}-\varepsilon_*
={55459\over146340000000}
=3.78973623069564\times10^{-7}
}
\tag{3.3}
\]

below this exact universal-safety ceiling. At `epsilon_*`, the same near-critical gate still has positive repair currency

\[
{3993048\over19073486328125}
=2.093507149824\times10^{-7}.
\tag{3.4}
\]

Thus the old fleet01/B14 value `0.0226018` can be raised to `0.02268865` with a universal proof, while no value above `0.02268902897...` can possibly work in this family. This essentially closes the scalar optimization problem for this particular shaped direction.

## 4. Application to the strongest known composition-prime source

For the fleet02/B17 source from Section 0, the new unit repair currency is exactly

\[
\boxed{
L_*=
{14089027843865471581106016370764179
\over13874074233328574665473392640000000}
=1.01549318584590899148\ldots .
}
\tag{4.1}
\]

The center cost of one unit is

\[
\eta_{\varepsilon_*}(1/2)=1-\varepsilon_*=0.97731135,
\]

so source currency per unit center is

\[
\boxed{
{L_*\over\eta_{\varepsilon_*}(1/2)}
=1.03906824150349731586\ldots .
}
\tag{4.2}
\]

This is strictly larger than the peer's previous shaped efficiency

\[
1.0390682188178841\ldots .
\]

Using the rigorous deficit endpoint `0.038023735` from (0.1), choose

\[
\boxed{\lambda={1872181\over50000000}=0.03744362.}
\tag{4.3}
\]

Then

\[
\lambda L_*-0.038023735
=
{4136835207899802946270318131404399
\over693703711666428733273669632000000000000000}
>5.9634\times10^{-9}.
\tag{4.4}
\]

Hence this scale repairs the strongest currently certified prime witness while remaining globally non-decreasing on every Boolean gate by Theorem 2.1.

Starting from the peer base center `6.521851214`, the resulting center is exactly

\[
\boxed{
C_{new}=6.558445288811087.
}
\tag{4.5}
\]

Compared with fleet02/B17's executed safe-direction repair center (0.2), this is a strict improvement of

\[
\boxed{7.016373\times10^{-9}.}
\tag{4.6}
\]

The numerical gain is deliberately reported at its true scale: it is tiny. The substantive result is the almost-sharp **universal-safety frontier** (2.1)--(3.3), not the seven-nanounit center change.

## 5. What this changes, and what it does not

The fleet02/B17 strong prime result changes the singleton-repair program from “find a direction that patches one old witness” into a quantitative optimization problem against the strongest current actual-Boolean adversary. This run shows that, within the peer's cubic-corrected quartic family, essentially all remaining safe scalar freedom has now been extracted. The exact two-input gate (3.1) leaves only a `3.79e-7` interval in `epsilon` above the proved value.

Therefore a materially better all-gate center is unlikely to come from merely retuning this single scalar `epsilon`. A next improvement must alter the shape in a new source-valid direction (for example an additional term with its own independently certified singleton inequality), or use the canonical KL/Boolean-support refunds to avoid paying the whole prime deficit through a pointwise safe additive repair.

This report does **not** prove that the resulting finite potential is universal. Unknown composition-prime gates may have negative base defect larger than the shaped payment. It does not prove decomposable/AND extremality. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

## 6. Preserved fleet04/B18 interface-B structure

The later all-gate owner instruction changes the immediate convergence target, not the validity of the existing interface-B mathematics. This run preserves unchanged fleet04/B18's exact mixed-curvature conservation

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
\tag{6.1}
\]

including the opposite-sign overlap term, and the exact zero-defect classification that vanishing folded depth defects force a character times a signed one-point defect up to sign and irrelevant variables.

The newer fleet04/B18 visible/hidden reduction

\[
4d_k=2R_k+\Omega_k
\]

and its surplus-weighted hidden-curvature bank are likewise untouched. No claim `sum d_k=O(J)` is introduced, and no small cube-measure error times ambient dimension is used.

## 7. Verification boundary

`CHECK.py` is a deterministic standard-library exact-rational checker. The bytes committed in this folder were executed locally before publication and produced `CHECK_OUTPUT.txt`. Its Bernstein certificate is an exact finite certificate for the continuum local inequality at `epsilon_*`; the strong-prime arithmetic and the actual two-input obstruction are also exact rational calculations.

The checker does not establish full FEI, novelty, or universality of the repaired **base potential**. It establishes exactly the theorem claimed here: the added direction is universally non-decreasing for every actual Boolean gate/bias, the scalar family has the stated exact obstruction ceiling, and the displayed stronger-source repair arithmetic is positive.

No benchmark gold, mock activation, paid/remote compute, workflow dispatch, email/Drive data, unrelated private data, scheduler mutation, or notification change was used.
