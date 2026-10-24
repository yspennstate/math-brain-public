# B16 — the stronger Numaro bias refutes `TILTED-QUARTIC-GATE-REPAIR-v1`

**Classification:** `CANDIDATE_REFUTED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Bound candidate and conditional chain

Fresh owner control revision `2026-09-22.2` converges the FEI fleet on the all-gate formulation. The complete source-bound replacement candidate consumed here is account03/B12

`proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T074537Z-tilted-quartic-universal-repair/REPORT.md`

(blob `aef979498118365764734b16459d55cb0833a03c`), candidate version **`TILTED-QUARTIC-GATE-REPAIR-v1`**. It starts from the already-refuted

\[
\Gamma^\dagger(u)=\Gamma_0(u)+0.268204856\,u(1-u),
\qquad \Gamma^\dagger(1/2)=6.521851214,
\]

and proves that

\[
F_*(m)=1-m^4-\frac1{36}(1-m^2)^2,
\qquad
\eta_*(u)=\frac{F_*(1-2u)}8
\]

is a **universally gate-safe direction**:

\[
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}\eta_*(p_i)
-\eta_*(p_{\rm out})\ge0
\]

for every Boolean gate and every product bias. It then takes

\[
\lambda_*={34877\over250000}=0.139508,
\qquad
\Gamma^*=\Gamma^\dagger+\lambda_*\eta_* ,
\]

which repairs the earlier Numaro witness at `p_1=3/8` and has

\[
\Gamma^*(1/2)=6.538805311222222\ldots .
\]

The conditional end-to-end implication is exact: if `D_{Gamma^*}(G;p)>=0` for every finite composition-prime gate and every interior product bias, the composition cocycle gives every finite gate; the all-gate equivalence then gives full FEI with finite constant `Gamma^*(1/2)`. The first missing implication is therefore the universal prime-gate inequality for this exact candidate.

This run attacks that implication directly rather than constructing another auxiliary theory.

## 1. Named other-account obstruction consumed and applied

The decisive second source is account03/B17

`proofnet24/P03-fei/fleet-2026-09-21/account03/B17/20260922T073143Z-prime-bellman-dent-transport/REPORT.md`

(blob `b964337d039b2ed24828dfd0b61773651b68f3dc`). It uses the exact composition-prime 18-input Numaro truth table with SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`

and proves a **stronger one-core biased violation** of the old seed at

\[
p={223\over456},\qquad p_2=\cdots=p_{18}=\frac12,
\qquad p_{\rm out}={1019\over2048}.
\]

For this genuine Boolean prime gate,

\[
\boxed{D_{\Gamma^\dagger}< -{38023\over10^6}}
\tag{1.1}
\]

(the peer's rigorous logarithm enclosure is
`-0.0380237343652791923...`).  The biased coordinate has normalized influence / pivotal probability

\[
\alpha={57\over256}.
\tag{1.2}
\]

This source is stronger than the `p=3/8` witness that determined `lambda_*`, so it must be applied before promoting the replacement candidate.

## 2. New exact calculation: the safe tilted-quartic repair is far too small

For the same source truth table, the attached exact checker reconstructs the table from the peer's immutable hexadecimal source and verifies the following pivotal counts:

* coordinate `1`: `29184` pivotal pairs among `2^17`, hence `57/256`;
* coordinates `2,...,18` together: `119040` pivotal pairs on the `x_1=0` face and exactly `119040` on the `x_1=1` face, each face having denominator `2^16`.

Therefore, **independently of the bias of coordinate 1**, the sum of the other seventeen normalized influences is

\[
\boxed{\frac{465}{256}}.
\tag{2.1}
\]

For the safe direction `eta_*`, the additive gate defect at the stronger witness is thus exactly

\[
\begin{aligned}
D_{\eta_*}
&={57\over256}\eta_*\!\left({223\over456}\right)
 +{465\over256}\eta_*\!\left({1\over2}\right)
 -\eta_*\!\left({1019\over2048}\right)\\[1mm]
&=\boxed{\frac{7405187762554608605}{58643094782223581184}}\\
&=0.12627552809166093\ldots .
\end{aligned}
\tag{2.2}
\]

At the candidate scale `lambda_*=34877/250000`, the total repair is only

\[
\boxed{
\lambda_*D_{\eta_*}
=\frac{51654146718923416863317}
{2932154739111179059200000}
=0.017616446373011435\ldots
<0.017617.
}
\tag{2.3}
\]

Combining (1.1) and (2.3),

\[
\boxed{
D_{\Gamma^*}
=D_{\Gamma^\dagger}+\lambda_*D_{\eta_*}
<-0.038023+0.017617
=-0.020406<0.
}
\tag{2.4}
\]

The attached exact arithmetic gives the sharper certified upper bound

\[
D_{\Gamma^*}
< -0.020406553626988566\ldots .
\tag{2.5}
\]

Hence **`TILTED-QUARTIC-GATE-REPAIR-v1` is rigorously refuted by the same composition-prime Numaro gate at the stronger rational bias `223/456`.** This is a refutation of the proposed potential, not of FEI.

## 3. Consequence for this proved-safe repair direction

The same calculation quantifies the minimum scale required even to repair this single stronger witness using the proved-safe `theta=1/36` direction. Since (1.1) already gives deficit `>0.038023`, any such scale must satisfy

\[
\lambda>
\frac{0.038023}{D_{\eta_*}}
=
0.30111139168944795\ldots .
\tag{3.1}
\]

But

\[
\eta_*(1/2)={35\over288}.
\]

Therefore any candidate of the restricted form

\[
\Gamma^\dagger+\lambda\eta_*
\]

that repairs this one source-certified prime witness must already have

\[
\boxed{
\Gamma(1/2)>6.558444612295593\ldots .
}
\tag{3.2}
\]

This is **not** a lower bound on the true FEI constant: a different shaped potential may achieve a better witness-payment/center ratio. It is a rigorous lower barrier only for this one universally-safe tilted-quartic direction above the fixed `Gamma^dagger` seed.

The result also explains why optimizing the tiny `1/36` versus `1/35` deformation before testing the stronger witness would not have closed the problem. The required repair scale more than doubles from the candidate's `0.139508` to `>0.301111`; the bottleneck is the stronger prime gate, not the last fourth decimal of the quartic shape.

## 4. Old/new missing implication

**Old missing implication.** Prove `D_{Gamma^*}(P;p)>=0` for every composition-prime Boolean gate and every interior product bias, where `Gamma^*` is `TILTED-QUARTIC-GATE-REPAIR-v1`.

**New result.** That implication is false. The exact 18-input composition-prime Numaro gate at bias `(223/456,1/2,...,1/2)` satisfies `D_{Gamma^*}<-0.020406`.

**Replacement obligation.** Any next candidate must be tested against the **strong `223/456` Numaro bias** before promotion. A continuation within the proved-safe `eta_*` ray needs center above `6.558444612...` merely to pay this one witness. To stay below that cap, the next mechanism must use a more efficient universally gate-safe direction, a Bellman-shaped non-ray repair, or a different source potential. After producing such a candidate, it still faces the universal prime-gate quantifier.

No finite test, auxiliary theorem, or candidate equivalence is being promoted to full FEI. Full FEI remains open.

## 5. Verification and provenance

`CHECKER.py` is standard-library only. It reconstructs the exact Numaro truth table, verifies its source SHA-256, recomputes the pivotal-face counts `(29184,119040,119040)`, derives (2.1)-(2.3) in exact `Fraction` arithmetic, and combines them with the peer's rigorous rational defect bound (1.1). It returns `PASS`.

Scoped privacy/secret review: the package contains only FEI mathematics, source-bound public-within-repository truth-table data, exact rational arithmetic and repository-relative references. It contains no credentials, scheduler identifiers, machine paths, unrelated private material, benchmark gold, email/Drive material, paid or remote compute, workflow dispatch, public-posting action, or permission changes.
