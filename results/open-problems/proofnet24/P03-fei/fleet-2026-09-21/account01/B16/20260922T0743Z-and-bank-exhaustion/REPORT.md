# B16 — exact finite AND-bank exhaustion for the first biased prime witness

**Classification:** `ESSENTIAL_STEP_APPLIED / SAME-CENTRE_UNIFORM-AND-BANK_REPAIR_REFUTED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Current target and correction of the stale candidate state

Fresh owner control revision `2026-09-22.2` converges all FEI workers on the all-gate formulation. The earlier fixed candidate

\[
\Gamma^\dagger(t)=\Gamma_0(t)+0.268204856\,t(1-t),\qquad
\Gamma^\dagger(1/2)=6.521851214,
\]

is no longer a live universal candidate. I consume and apply the exact other-account result account03/B12

`proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`

(blob `36fea824c2dcae8c65c3d485e5d5714899699855`). Together with account04/B14's composition-primality certificate, it gives a genuine composition-prime 18-input Boolean gate at

\[
p_1=3/8,\qquad p_2=\cdots=p_{18}=1/2,\qquad p_{out}=967/2048,
\]

for which

\[
D_{\Gamma^\dagger}=-0.017611419955801753789\ldots<0.
\tag{0.1}
\]

Thus `LIMIT-PRIME-GATE-LIFT-v1` is **refuted**, not an open candidate to certify. Full FEI itself is not refuted.

The second named other-account result consumed substantively is account02/B17

`proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T071234Z-and-slack-rigidity/REPORT.md`

(blob `4a356a4ede8cadbf77347aac7cd746681048bbe4`). It introduces the correct replacement mechanism: reshape the potential while explicitly spending existing AND slack. For a symmetric perturbation `psi`, define

\[
L_{p,q}(\psi)=q\psi(p)+p\psi(q)-\psi(pq),
\qquad
M(p,q)=pq(1-p)(1-q).
\tag{0.2}
\]

The certified read-once theorem already pays every AND gate for
\(\Gamma_{.01}=\Gamma_0+0.01t(1-t)\). Hence the refuted \(\Gamma^\dagger\) contains the rigorously guaranteed additional uniform AND bank

\[
A=0.268204856-0.01=0.258204856,
\tag{0.3}
\]

because a quadratic lift changes the AND defect by exactly \(A M(p,q)\).

Account02/B17 proved that a same-centre repair of the prime witness needs to spend more than `0.2528769` units of this bank, i.e. more than 97.9%, but its estimate left a small logical window because `0.2528769 < A`. This run closes that window exactly.

## 1. The exact replacement question attacked

Let

\[
\Gamma_{new}=\Gamma^\dagger+\psi,
\qquad \psi(1/2)=0,
\]

so the FEI centre is kept at `6.521851214`. The prime witness (0.1) requires

\[
R_{wit}(\psi)
:=\frac{57}{256}\psi(3/8)-\psi(967/2048)
>0.0176114.
\tag{1.1}
\]

Suppose the repair preserves all certified AND inequalities using only the uniform guaranteed bank (0.3). More generally, assume

\[
L_{p,q}(\psi)\ge-KM(p,q)
\qquad\forall p,q\in(0,1).
\tag{1.2}
\]

The question is whether `K=A` can possibly allow (1.1).

## 2. New theorem — 35 exact AND constraints already force a sharper transport bound

### Theorem 2.1

For every symmetric real-valued \(\psi\) with \(\psi(1/2)=0\) satisfying (1.2),

\[
\boxed{
R_{wit}(\psi)
\le \kappa K,
\qquad
\kappa=
\frac{792001822391570453}{11721234856636579840}
=0.06756982793012956\ldots .
}
\tag{2.1}
\]

No continuity, boundedness, differentiability, or sign hypothesis on \(\psi\) is used.

### Proof

Write every argument through the symmetry representative
\(s(x)=\min\{x,1-x\}\). Each charged AND inequality is

\[
-L_{p,q}(\psi)
=-q\psi(s(p))-p\psi(s(q))+\psi(s(pq))
\le K M(p,q).
\tag{2.2}
\]

The adjacent exact checker contains 35 explicit rational pairs \((p_j,q_j)\) and 35 strictly positive rational multipliers \(\lambda_j\). Direct exact `Fraction` arithmetic verifies the coefficient identity

\[
\sum_{j=1}^{35}\lambda_j[-L_{p_j,q_j}(\psi)]
=rac{57}{256}\psi(3/8)-\psi(967/2048)
=R_{wit}(\psi),
\tag{2.3}
\]

where every intermediate \(\psi\)-coefficient cancels exactly and the only unused coefficient is at `1/2`, where \(\psi(1/2)=0\). The same exact arithmetic verifies

\[
\sum_{j=1}^{35}\lambda_jM(p_j,q_j)
=\kappa.
\tag{2.4}
\]

Multiplying (2.2) by \(\lambda_j>0\), summing, and using (2.3)--(2.4) proves (2.1). QED.

The 35 pairs live on the same rational tent-map orbit already identified by account02/B17, together with the physical witness values `3/8`, `967/2048`, `1/4`, and `1/2`; the new step is the exact positive-multiplier elimination rather than a one-chain estimate.

## 3. Consequence — the entire guaranteed uniform AND bank is insufficient

The source witness deficit is strictly larger than the rational floor

\[
\delta_0=0.0176114.
\]

By (2.1), any same-centre repair satisfying (1.2) must have

\[
K>\frac{\delta_0}{\kappa}
=
0.2606400007146834\ldots .
\tag{3.1}
\]

But the entire rigorously guaranteed extra AND bank is only

\[
A=0.258204856.
\]

Therefore

\[
\boxed{K_{required}>0.26064>A=0.258204856.}
\tag{3.2}
\]

Equivalently, the first biased prime witness requires more than

\[
\boxed{1.009431057}
\]

times the **whole** uniform guaranteed bank. Thus:

> **No same-centre perturbation can repair the exact prime witness while preserving every AND inequality merely by spending the uniform bank guaranteed by the certified `0.01` read-once theorem.**

This strictly strengthens account02/B17's `>97.93%` estimate to a genuine impossibility for that uniform-bank repair mechanism.

The statement is deliberately not stronger than proved. The actual AND defects of \(\Gamma^\dagger\) may contain additional nonuniform slack beyond `A M(p,q)`. A successful same-centre replacement is therefore not ruled out absolutely; it must exploit that detailed slack at some of the 35 charged pairs (or elsewhere), rather than rely only on the universal quadratic reserve. Alternatively the centre or the base potential shape must change.

## 4. Compact conditional chain after this result

1. **PROVED:** the all-gate inequality for one symmetric nonnegative finite-cap potential implies full FEI.
2. **REFUTED:** the fixed `LIMIT-PRIME-GATE-LIFT-v1` potential fails on the exact composition-prime 18-input witness.
3. **PROVED BY account02/B17:** a free centre-preserving AND repair is impossible; a charged repair must transport existing slack.
4. **PROVED THIS RUN:** even the *entire uniform guaranteed* AND bank `A=0.258204856` is insufficient for a same-centre repair of that one witness. The exact finite transport lower requirement is `K>0.2606400007`.
5. **OPEN:** exploit the **actual nonuniform AND slack**, raise/reshape the centre/base, or construct another finite-cap potential satisfying every gate inequality. Only such a universal potential would prove FEI.

Thus the old missing implication “certify the fixed lifted potential on every prime gate” is dead. The new missing implication is sharper: a replacement potential must solve the exact prime affine constraint while paying its losses from detailed gate-specific slack, not from a uniform quadratic reserve.

## 5. Exact verification

`check_and_bank_exhaustion.py` uses only Python standard-library `Fraction`. It checks:

- all 35 multipliers are strictly positive;
- their exact coefficient sum is precisely `R_wit` modulo the fixed centre value;
- the exact cost is
  `792001822391570453 / 11721234856636579840`;
- `kappa < 0.067570`;
- the coarse certified witness deficit `>0.0176114` already forces `K>0.26064`;
- `0.26064 > 0.258204856`.

The checker returns `PASS`. The theorem itself is the positive linear combination (2.3); no floating-point optimization appears in the certificate.

Scoped privacy review: this package contains only FEI mathematics, repository-relative mathematical source identifiers and deterministic rational verification data. It contains no credentials, scheduler identifiers, machine paths, unrelated private material, benchmark gold, email/Drive actions, public posting, paid/remote compute, workflow dispatch, or permission changes.
