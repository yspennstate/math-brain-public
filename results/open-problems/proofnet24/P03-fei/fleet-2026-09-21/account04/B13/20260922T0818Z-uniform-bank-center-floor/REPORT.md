# account04/B13 — quantitative center floor after spending the uniform AND bank

**Run:** `B13-20260922T081113Z-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Current source-exact correction and compact target

The later owner control asks the FEI fleet to converge on the source-exact all-gate formulation.  The fixed potential

\[
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p),
\qquad \Gamma^\dagger(1/2)=6.521851214,
\]

is no longer a viable universal all-gate potential: the completed composition-prime 18-input witness at

\[
p_1=3/8,\quad p_2=\cdots=p_{18}=1/2,\quad p_{out}=967/2048
\]

has source-certified deficit

\[
D_{\Gamma^\dagger}<-0.0176114.
\]

This refutes that fixed potential, not FEI.  The live question is therefore whether a finite symmetric potential can transport enough existing gate slack to repair this prime obstruction while keeping all gate inequalities nonnegative.

## 1. Named newest compatible other-account result consumed

The newest compatible cross-account result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T073227Z-bellman-and-bank/REPORT.md`

(report blob `c979ef4b55f3138d62e34c2c1914a659c8fde9d0`).  Its Theorem 2.1 proves the sharpened charged-AND transport inequality.  For every bounded symmetric center-zero perturbation \(\psi\) satisfying

\[
L_{p,q}(\psi):=q\psi(p)+p\psi(q)-\psi(pq)\ge-KM(p,q),
\]
\[
M(p,q)=pq(1-p)(1-q),
\]

one has

\[
R_{wit}(\psi):={57\over256}\psi(3/8)-\psi(967/2048)
\le \kappa K,
\]

with the exact rational coefficient obeying

\[
\kappa=0.0676346063971711006296130\ldots<\bar\kappa:=0.067635.
\tag{1.1}
\]

That peer result also identifies the uniformly guaranteed extra two-input-AND bank between the certified read-once potential and \(\Gamma^\dagger\):

\[
A=0.268204856-0.01=0.258204856.
\tag{1.2}
\]

Its stated endpoint consequence is that no **non-increasing-center** bounded symmetric repair can repair the witness while spending only this uniform bank.

I also retain the exact center decomposition from account04/B18

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T074308Z-repair-andloss-frontier/REPORT.md`.

For any bounded symmetric repair \(\eta\), put

\[
E:=\eta(1/2),\qquad q_*(u):=4u(1-u),\qquad
\psi(u):=\eta(u)-E q_*(u).
\]

Then \(\psi(1/2)=0\),

\[
L_{p,q}(q_*)=4M(p,q),
\tag{1.3}
\]

and the exact prime-witness repair functional splits as

\[
L_{wit}(\eta)=B E+R_{wit}(\psi),
\qquad
B={1078193\over1048576}=1.02824497222900390625.
\tag{1.4}
\]

## 2. New theorem — center versus fraction of uniform AND bank

The preceding endpoint can be strengthened to a quantitative interpolation.

### Theorem 2.1

Let \(0\le\rho\le1\).  Suppose a bounded symmetric additive repair \(\eta\) of \(\Gamma^\dagger\)

1. repairs the certified prime witness, so
   \[
   L_{wit}(\eta)>d_0,\qquad d_0:=0.0176114,
   \tag{2.1}
   \]
2. spends at most a fraction \(\rho\) of the uniformly guaranteed quadratic AND bank, meaning
   \[
   L_{p,q}(\eta)\ge-\rho A M(p,q)
   \qquad\forall p,q\in(0,1).
   \tag{2.2}
   \]

Then its center increase satisfies

\[
\boxed{
E>
{d_0-\bar\kappa\rho A\over B+4\bar\kappa}.
}
\tag{2.3}
\]

The numerator is positive throughout \(0\le\rho\le1\).  In particular, even after spending the **entire** uniformly guaranteed AND bank,

\[
\boxed{
E>{945373212416\over8312223822265625}
>0.000113732886966.
}
\tag{2.4}
\]

Hence every repair in this class has

\[
\boxed{
(\Gamma^\dagger+\eta)(1/2)>6.521964946886966.
}
\tag{2.5}
\]

### Proof

By (1.3), condition (2.2) and \(\psi=\eta-Eq_*\) give

\[
L_{p,q}(\psi)
=L_{p,q}(\eta)-4E M(p,q)
\ge-(\rho A+4E)M(p,q).
\tag{2.6}
\]

If \(\rho A+4E<0\), this is stronger than the zero-cost AND-rigidity condition; a nonzero bounded center-zero perturbation capable of a positive witness correction is impossible.  Thus an actual repair may be treated with

\[
K=\rho A+4E\ge0.
\]

Apply the account01/B13 theorem and the safe upper bound (1.1):

\[
R_{wit}(\psi)\le\kappa K
<\bar\kappa(\rho A+4E).
\tag{2.7}
\]

Using the exact decomposition (1.4) and the necessary repair condition (2.1),

\[
d_0
<L_{wit}(\eta)
=BE+R_{wit}(\psi)
<(B+4\bar\kappa)E+\bar\kappa\rho A.
\]

Rearranging proves (2.3).  Finally

\[
d_0-\bar\kappa A
={3692864111\over25000000000000}
=0.00014771456444>0,
\]

so the bound remains strictly positive even at \(\rho=1\), giving (2.4)-(2.5). `QED`

## 3. Quantitative ledger

Using only the conservative certified numbers \(d_0=0.0176114\) and \(\bar\kappa=0.067635\), the theorem gives

| fraction \(\rho\) of uniform AND bank spent | forced center increase \(E\) |
|---:|---:|
| 0 | \(>0.013559904354125\) |
| 1/4 | \(>0.010198361487335\) |
| 1/2 | \(>0.006836818620546\) |
| 3/4 | \(>0.003475275753756\) |
| 1 | \(>0.000113732886966\) |

This is an influence/slack-relative statement.  It does not use a cube-measure error multiplied by ambient dimension and does not charge ordinary second-derivative depth at unit price.

## 4. Exactly how the peer result changes the argument

Before the account01/B13 sharpening, the available transport constant did not force the uniform guaranteed bank below the prime-witness repair cost at the same center.  Account01/B13 lowers the coefficient to \(\kappa<0.067635\), crossing that threshold.  The present theorem uses that strict gap **again**, together with the exact center normalization from account04/B18, to quantify how much center must be bought back as progressively more of the uniform AND bank is spent.

Thus the repair search can no longer regard the center and the guaranteed uniform AND bank as interchangeable free resources.  Within bounded symmetric additive repairs of this base potential, a successful construction must do at least one of the following:

* raise the center by the amount forced by (2.3);
* exploit **nonuniform positive AND slack beyond** the guaranteed quadratic bank \(A M(p,q)\);
* or abandon this additive-repair/base-potential architecture and construct a different all-gate potential.

The sharp next calculation is therefore the actual source-certified nonuniform AND slack profile on the finite tent-map orbit used by the peer dual, rather than another free bump or another fixed-candidate collar.

## 5. Preserved interface-B facts

Nothing here weakens account04/B18's mixed-curvature conservation

\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k,
\]

including the opposite-sign contribution.  Its exact zero-depth classification also remains intact: the all-zero-depth branch is a character times a signed one-point defect, up to irrelevant variables, with the proved \(H<4J\) consequence.  Neither fact is used to assert the false shortcut \(\sum_k d_k=O(J)\).

## 6. Verification and scope

The exact-rational checker in `CHECKER.py` reproduces the conservative arithmetic in (2.3)-(2.5) and the five ledger values.  `verification.txt` records the exact fractions.  The analytic theorem depends on the two cited source theorems; the checker is an arithmetic guard, not an independent proof of those sources.

This result does **not** prove FEI and does not certify a universal repaired potential.  Full FEI remains open.  No novelty claim is made.  No benchmark gold, mocks, paid/remote compute, workflow dispatch, email, Drive, unrelated private data, notification changes, or permission changes were used.
