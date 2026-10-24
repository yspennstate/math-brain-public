# B14 — finite AND-bank dual certificate for the biased prime repair

**Classification:** `ESSENTIAL_STEP_APPLIED / UNIFORM-BANK SAME-CENTER REPAIR REFUTED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact current target and source use

The later owner direction is the all-gate formulation: construct one symmetric nonnegative finite-cap potential `Gamma` satisfying every gate inequality, or falsify a proposed gate extremality/candidate by a source-valid Boolean gate and bias vector.

This run substantively consumes two exact other-account results from the current private FEI archive:

1. account04/B18, `20260922T074308Z-repair-andloss-frontier/REPORT.md`, blob `7d295b4d9a480727ee2d08c0214e9ea1f55c99c1`; it records that
   \[
   \Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),\qquad \Gamma^\dagger(1/2)=6.521851214,
   \]
   is refuted by the exact composition-prime 18-input witness at
   \[
   p_1=3/8,\quad p_2=\cdots=p_{18}=1/2,\quad r=p_{out}=967/2048,
   \]
   with defect
   \[
   D_{\Gamma^\dagger}(P;p)=-d,\qquad d> d_0:=0.0176114.
   \]
   For a symmetric repair `eta`, its witness correction is
   \[
   L_{wit}(\eta)={57\over256}\eta(3/8)+{465\over256}\eta(1/2)-\eta(r).
   \]

2. account02/B17, `20260922T071234Z-and-slack-rigidity/REPORT.md`, blob `4a356a4ede8cadbf77347aac7cd746681048bbe4`; for a symmetric center-zero perturbation `psi`, it defines
   \[
   L_{p,q}(\psi)=q\psi(p)+p\psi(q)-\psi(pq),\qquad
   M(p,q)=pq(1-p)(1-q),
   \]
   and proves a finite-orbit estimate `R_wit(psi) <= 0.069645 K` under `L_{p,q}(psi)>=-K M(p,q)` for all AND pairs.

The first essential missing inference left by those reports is whether the exact prime repair can in fact be financed from the **source-certified uniform quadratic AND bank** already present in `Gamma^dagger`. The preceding coefficient `0.069645` left a narrow apparent gap: it only forced `K>0.2528769`, while the guaranteed bank is `A=0.258204856`.

This run closes that gap by an exact 35-constraint dual certificate.

## 1. The exact 35-AND theorem

For `t in (0,1)` write
\[
\bar t:=\min(t,1-t).
\]
Because `psi` is symmetric, every AND correction can be written
\[
L_{p,q}(\psi)=q\psi(\bar p)+p\psi(\bar q)-\psi(\overline{pq}).
\]
Define the prime-witness centered correction
\[
R_{wit}(\psi):={57\over256}\psi(3/8)-\psi(967/2048).
\]

### Theorem 1 — sharpened finite AND rigidity

Let `psi:(0,1)->R` be symmetric with `psi(1/2)=0`. If for every `p,q in (0,1)`
\[
L_{p,q}(\psi)\ge -K M(p,q),
\tag{1.1}
\]
then
\[
\boxed{
R_{wit}(\psi)\le \kappa_{35} K,
\qquad
\kappa_{35}:={2900397572141\over42924444221440}
=0.06756983403625068\ldots .
}
\tag{1.2}
\]
No continuity, differentiability, concavity, polynomial ansatz, or finite-dimensional assumption on `psi` is used.

### Proof

There are 35 explicit pairs `(p_j,q_j)` and 35 positive rational multipliers `lambda_j`, listed in `CHECKER.py`. They satisfy the following two identities by exact rational arithmetic:
\[
\sum_{j=1}^{35}\lambda_j L_{p_j,q_j}(\psi)
= -R_{wit}(\psi)
\tag{1.3}
\]
for every symmetric `psi` with `psi(1/2)=0`, and
\[
\sum_{j=1}^{35}\lambda_j M(p_j,q_j)
=\kappa_{35}.
\tag{1.4}
\]
All `lambda_j` are strictly positive. Multiplying the 35 instances of (1.1) by `lambda_j` and summing gives
\[
-R_{wit}(\psi)
\ge -K\kappa_{35},
\]
which is (1.2). QED.

This is a genuine finite dual certificate. The checker does not solve an LP or use floating point; it verifies the coefficient identity and bank sum using Python `Fraction` arithmetic only.

## 2. Consequence: the guaranteed same-center AND bank is insufficient

The completed read-once theorem certifies the AND inequalities for
\[
\Gamma_{cert}(p)=\Gamma_0(p)+0.01p(1-p).
\]
Hence `Gamma^dagger` contains the source-certified **uniform extra** AND reserve
\[
A:=0.268204856-0.01=0.258204856.
\tag{2.1}
\]
A center-preserving repair `psi(1/2)=0` which is financed only from this guaranteed reserve must obey
\[
L_{p,q}(\psi)\ge -A M(p,q)
\qquad\forall p,q.
\tag{2.2}
\]
Theorem 1 therefore gives
\[
R_{wit}(\psi)\le \kappa_{35}A.
\]
Exact rational arithmetic yields
\[
\boxed{
 d_0-\kappa_{35}A
 ={882852438006487413\over5365555527680000000000}
 =0.00016454073272599638\ldots>0.
}
\tag{2.3}
\]
But repairing the exact prime witness requires `R_wit(psi)>=d>d_0`. Contradiction.

Therefore:
\[
\boxed{
\text{No center-preserving symmetric repair can fix the prime witness while spending only the certified uniform quadratic AND reserve.}
}
\tag{2.4}
\]
Equivalently, the required normalized loss is now rigorously
\[
\boxed{
K>{d_0\over\kappa_{35}}
={11811868077522944\over45318712064703125}
=0.2606399771612821\ldots>A=0.258204856.
}
\tag{2.5}
\]
This improves the inherited `K>0.2528769` enough to cross the actual guaranteed-bank threshold. The former statement said the witness consumed more than 97.9% of the guaranteed bank; the new exact statement says it needs **more than 100%** of that bank.

## 3. Center lift: an exact minimum within the same bank-only mechanism

Use the account04/B18 center decomposition
\[
\eta(u)=E q_*(u)+\psi(u),\qquad q_*(u)=4u(1-u),\qquad \psi(1/2)=0.
\]
The center term changes the witness by
\[
aE,\qquad a={1078193\over1048576},
\]
and adds `4E M(p,q)` to every AND constraint. Thus a repair financed only from the certified uniform reserve plus its own center lift has
\[
K=A+4E.
\]
Combining witness repair with Theorem 1 forces
\[
aE+\kappa_{35}(A+4E)>d_0.
\]
Therefore
\[
\boxed{
E>E_{min}:={d_0-\kappa_{35}A\over a+4\kappa_{35}}
={882852438006487413\over6967304280623000000000}
=0.00012671363305630522\ldots .
}
\tag{3.1}
\]
Within this bank-only repair class, the center must consequently exceed
\[
6.521851214+E_{min}>6.521977927633056.
\tag{3.2}
\]
This is not a lower bound for unrestricted FEI: a repair may exploit nonuniform pre-existing AND slack or abandon the base potential entirely. It is an exact exclusion of the natural uniform-bank repair mechanism.

## 4. Stronger source-exact finite reduction for the next run

The 35-term identity gives a sharper target than the uniform-bank corollary. Let
\[
S_j:=D_{\Gamma^\dagger}(AND;p_j,q_j)
\]
be the **actual** pre-existing AND defects at the 35 certificate pairs. Any center-preserving repair that preserves every AND inequality must satisfy
\[
L_{p_j,q_j}(\psi)\ge -S_j.
\]
Multiplying by the same positive `lambda_j` gives the exact necessary condition
\[
\boxed{
R_{wit}(\psi)\le \sum_{j=1}^{35}\lambda_j S_j.
}
\tag{4.1}
\]
Hence a source-certified evaluation proving
\[
\sum_{j=1}^{35}\lambda_j S_j<d
\tag{4.2}
\]
would rule out **every same-center repair preserving the AND family**, not merely bank-only repairs. This is now the first unpaid inference. It is finite: 35 specified rational AND pairs, with an exact positive dual certificate already fixed.

The current text certificate proves nonnegativity of the read-once base but does not itself provide source-exact upper values of all 35 `S_j`; those values must be evaluated from the immutable numerical potential/certificate data with outward error control before (4.2) can be claimed. No such unsupported evaluation is asserted here.

## 5. Obstruction hygiene

This theorem does not assume an every-coordinate selector, a critical core, source monotonicity, or a bounded-depth restriction tree. Hence the known addressing, large-majority, tribes, sparse-defect and tensor obstructions do not falsify the argument. The witness is at a genuine interior biased point (`3/8,1/2,...,1/2`), so no biased-limit or dead-coordinate argument is being used. The earlier balanced high-ratio constructions are already incorporated in the choice of `Gamma^dagger`; this run addresses the newer biased prime obstruction rather than reopening the refuted read-once-center claim.

## 6. Exact old/new missing implication

**Old unpaid implication:** after the biased 18-input prime refuted `Gamma^dagger`, it was still possible that a same-center perturbation could repair it by spending the guaranteed quadratic AND bank `A=0.258204856`; the inherited finite-orbit estimate did not exclude this because `0.2528769<A`.

**New proved implication:** the exact 35-constraint dual improves the required normalized AND loss to `>0.2606399771>A`; therefore that same-center guaranteed-bank repair is impossible. More generally, all same-center AND-preserving repairs are reduced to the finite actual-slack test (4.2).

**Remaining target-level gap:** certify or refute (4.2) from the actual immutable read-once potential data; if (4.2) fails, the dual weights identify exactly which AND pairs contain the extra slack that a viable repair must transport. Even success at (4.2) would only rule out same-center repairs of this base potential; a complete finite-cap all-gate potential is still required for full FEI.

## 7. Verification and scope

`CHECKER.py` contains the 35 rational pairs and multipliers. It verifies exactly:

- all coefficient cancellations in (1.3);
- the exact value of `kappa_35` in (1.4);
- the positive reserve gap (2.3);
- the exact center threshold (3.1).

`CHECKER.out` records `PASS` and the resulting rational/decimal values.

Scoped privacy review: this package contains only FEI mathematics, immutable private-repository source identifiers, logical account/slot labels, and nonsecret constants. No credentials, scheduler IDs, machine paths, unrelated private data, email/Drive actions, remote/paid compute, workflows, public posting, or permission changes are included.
