# B19 / A091 independent review of B09: accepted lemma, repaired endpoint lower bound, narrowed composition scope

Run ID: `20261011T204627Z-account01-B19-b09-composition-review-a091`  
Primary packet: `A091` (Composition referee)  
Reviewed target: `B09-BIASED-BLOCK-UNCERTAINTY-v1` and the separate repaired two-bit certificate  
Full FEI status: **OPEN**

## Verdict summary

The B09 report was reviewed as three separate mathematical objects.

1. **Main product-biased restriction identity and uncertainty lemma — ACCEPTED at exact scope.** For every finite Boolean sign under an interior product bias and every physical coordinate block,
   \[
   L_A=M_A+J_A,
   \qquad 0\le J_A\le M_A+\Delta_A(p),
   \]
   with
   \[
   \Delta_A(p)=\sum_{i\in A}
   \left[h_2(p_i)+\log_2\max\{p_i,1-p_i\}\right].
   \]
   The physical-posterior transform, Maassen--Uffink constant, signs, normalization, zero fibers, and deterministic limits were independently reconstructed.

2. **Fixed two-bit tax-free counterexample — ACCEPTED at its certified finite scope.** The corrected rational interval code rigorously proves `J_A-M_A>0.1195` bits for `g(x,y)=(-1)^(xy)`, `p=1/8`, `q=1/4`, and `A={X}`. The invalid original signed-division routine is not used.

3. **Section 5 consequences — SPLIT.**
   * Exact additivity of `M,J,L,Delta` is proved for multiplicative tensor products on disjoint variables with the physical block split across the factors.
   * No general B09-ledger composition theorem follows merely from O'Donnell--Tan. Their primary theorem composes biased `FEI+` under disjoint substitution; it does not identify a gate-output restriction with a physical restriction of the inner variables. Shared or repeated variables are also outside that theorem.
   * The original sentence asserting endpoint necessity from the asymptotics of the *upper bound* `Delta` was unsupported. This review repairs it with a genuine lower-bound family:
     \[
     J_A-M_A=4q(1-2q)p\log_2(1/p)+O_q(p)
     \quad (p\downarrow0,\ 0<q<1/2).
     \]
     At `q=1/4`, the leading coefficient is `1/2`. Hence no universal additive correction `O(p)` can replace the logarithmic tax. Because this review supplies the repair, the endpoint claim needs a fresh independent reviewer.

## 1. Reviewed sources and exact objects

### Campaign sources

* B09 original report: open-problems commit `adb671ffcda143fa68347806bb96e8c305621a7d`, path `reports/fei-2026-10-11/runs/B09/20261011T195500Z-account01-B09-biased-restriction-uncertainty/REPORT.md`, blob `71b68e4decf9658a42fef6bb2668e19f25bd214a`.
* Corrected interval certificate: open-problems commit `a1ff93577685acd461b154b04e0c1aa0c65645c8`, path `reports/fei-2026-10-11/verification/B09_interval_repair_20261011/`:
  * `REPORT.md`, blob `2674d84116f7454c45b37fdd4991f78d65eaf31c`;
  * `CHECK.py`, blob `e0e834cca2e2705652c76bd38df98eb0bbdcab52`;
  * `CHECK.out`, blob `3bfcf7ddae830e0766863b41e89ebb2ef55f6ba2`.
* Current B19 compact contract: blob `ee688080aba90acd2daed1b26e809e38285dcb85`.
* Current protocol, claim registry, and obstruction registry: blobs `457358ff62cbf1141a72096bcabdf95bf18c1be2`, `6a3e1aa94f81ec01841a083c97449739b9e72baa`, and `dd482025647aed25166b46cc217a7ed77dcaa767`.
* Previous B19 review baseline: commit `7955d427222392911dc6af2e4ee3aa8aab67ac8c`, report blob `dcec4cb77233a7b233b4798b25aab5f2dd5c82b6`.

### Primary literature

* R. O'Donnell and L.-Y. Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347, especially Theorem 1 and Proposition 3.2: https://arxiv.org/abs/1304.1347
* H. Maassen and J. B. M. Uffink, *Generalized entropic uncertainty relations*, Phys. Rev. Lett. 60 (1988), 1103--1106, DOI: https://doi.org/10.1103/PhysRevLett.60.1103

No publication-novelty claim is made. The endpoint family below is a campaign repair of a stated logical gap.

## 2. Independent reconstruction of the main lemma

Let `X=(X_A,X_B)` have independent coordinates with `P[X_i=1]=p_i in (0,1)`. Use the normalized biased basis

\[
 \phi_i(0)=-\sqrt{\frac{p_i}{1-p_i}},
 \qquad
 \phi_i(1)=\sqrt{\frac{1-p_i}{p_i}}.
\]

For a Boolean sign `f`, let `mu(S)=hat f_p(S)^2`. Write `S_A=S cap A`, `S_B=S cap B`. For a physical assignment `z` on `A`, let `mu_z` be the biased spectral law of the actual child `f_z`. Define

\[
 M_A=H(S_A\mid S_B),
 \qquad
 J_A=H(S_B)-\mathbb E_zH(\mu_z),
 \qquad
 L_A=H(\mu)-\mathbb E_zH(\mu_z).
\]

### 2.1 Exact physical restriction identity

For a fixed residual frequency `T subset B`,

\[
 q_T:=\sum_{R\subseteq A}\widehat f_p(R\cup T)^2
     =\mathbb E_z\widehat{f_z}_{p_B}(T)^2.
\]

The second equality is Parseval on the revealed coordinates, not an assumed child prior. Hence `q` is the actual average child spectral law. Under the joint experiment

\[
 Z\sim\mu_{p_A},\qquad T\sim\mu_Z,
\]

we have

\[
 J_A=I(Z;T)\ge0.
\]

The entropy chain rule then gives

\[
 \boxed{L_A=M_A+J_A.}
\]

This retains physical branch probabilities, Fourier signs through the child transform, and every zero mass by the `0 log(1/0)=0` convention.

### 2.2 Fiber transform and uncertainty constant

For every `T` with `q_T>0`, define

\[
 a_R=\frac{\widehat f_p(R\cup T)}{\sqrt{q_T}},
 \qquad
 b_z=\frac{\sqrt{\mu_{p_A}(z)}\widehat{f_z}_{p_B}(T)}{\sqrt{q_T}}.
\]

The restriction expansion gives exactly

\[
 b_z=\sum_{R\subseteq A}\sqrt{\mu_{p_A}(z)}\phi_R(z)a_R.
\]

Thus `b=U_A a`, where

\[
 U_A=\bigotimes_{i\in A}
 \begin{pmatrix}
 \sqrt{1-p_i}&-\sqrt{p_i}\\
 \sqrt{p_i}&\sqrt{1-p_i}
 \end{pmatrix}.
\]

Each factor is orthogonal. Its largest absolute entry is `sqrt(max(p_i,1-p_i))`, so

\[
 c_A:=\max_{z,R}|(U_A)_{zR}|
 =\prod_{i\in A}\sqrt{\max\{p_i,1-p_i\}}.
\]

Maassen--Uffink, in bits, yields

\[
 H(a^2)+H(b^2)\ge-2\log_2c_A
 =-\sum_{i\in A}\log_2\max\{p_i,1-p_i\}.
\]

Average with weights `q_T`. The two entropies become `M_A` and `H(Z|T)`. Since `J_A=H(Z)-H(Z|T)` and `H(Z)=sum_i h_2(p_i)`, this proves

\[
 \boxed{0\le J_A\le M_A+\Delta_A(p).}
\]

Therefore `L_A<=2M_A+Delta_A(p)` as claimed.

### 2.3 Endpoint and zero-fiber audit

* If `q_T=0`, every coefficient in that fiber is zero and its weighted contribution is zero; no normalized vector is needed.
* At `p_i=1/2`, the one-bit transform is mutually unbiased and the summand of `Delta` is exactly zero.
* For `p<=1/2`,
  \[
  h_2(p)+\log_2(1-p)=p\log_2\frac{1-p}{p}\ge0.
  \]
  The expression is symmetric for `p>=1/2`.
* At `p_i=0` or `1`, the normalized biased character is undefined. The proved theorem is correctly restricted to interior biases. A deterministic coordinate must first be deleted; the limiting tax is zero. Calling the formula "endpoint-safe" is acceptable only in this limiting/dimension-reduced sense.

**Verdict:** `B09-BIASED-BLOCK-UNCERTAINTY-v1` is independently accepted at its stated interior-product-bias, physical-block scope.

## 3. Fixed two-bit certificate

For

\[
 g(x,y)=(-1)^{xy},\qquad p=P[X=1]=\frac18,
 \qquad q=P[Y=1]=\frac14,
\]

the squared biased Fourier masses are

\[
 (225,7,3,21)/256.
\]

The repaired certificate uses rational atanh-series enclosures, a positive interval for `ln 2`, and all four quotient corners for signed interval division. Entropy multiplication reverses bounds correctly for negative logarithms. The code proves

\[
 0.119545016024424957<J_A-M_A
 <0.119545016024424958.
\]

The repair script and saved output were inspected. The unchanged certificate was not rerun as new work.

**Verdict:** `B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED-v1` is accepted at its finite helper-refutation scope. It is not an FEI counterexample.

## 4. New endpoint lower-bound family

The original B09 Section 5(4) argued that, because the *upper bound*

\[
 \Delta(p)=p\log_2(1/p)+O(p^2),
\]

has a logarithm, every valid correction must exceed `O(p)`. That inference is invalid without a matching lower bound for `J-M`. This is the first unsupported line in the original consequence chain.

The same two-bit Boolean gate supplies the missing lower-bound family. Fix `q in (0,1/2)` and let `p downarrow 0`. Put

\[
 r=4q(1-q),\qquad c=4q^2.
\]

The exact squared biased Fourier masses, ordered as `empty,X,Y,XY`, are

\[
\begin{aligned}
 m_0&=(1-2pq)^2,\\
 m_X&=4p(1-p)q^2,\\
 m_Y&=4p^2q(1-q),\\
 m_{XY}&=4p(1-p)q(1-q).
\end{aligned}
\tag{4.1}
\]

The residual spectral bit has nonempty probability `pr`. Since the `X=0` child is constant and the `X=1` child has nonempty spectral mass `r`,

\[
 J_A=h_2(pr)-p h_2(r). \tag{4.2}
\]

Conditioning the parent spectrum on whether `S_Y` is empty gives the exact formula

\[
 M_A=(1-pr)h_2\!\left(
 \frac{4p(1-p)q^2}{1-pr}
 \right)+prh_2(p). \tag{4.3}
\]

For any fixed `a>0`,

\[
 h_2(ap+O(p^2))=ap\log_2(1/p)+O_a(p).
\]

Equations (4.2)--(4.3) therefore give

\[
\begin{aligned}
J_A&=rp\log_2(1/p)+O_q(p),\\
M_A&=cp\log_2(1/p)+O_q(p),
\end{aligned}
\]

and hence

\[
 \boxed{
 J_A-M_A=4q(1-2q)p\log_2(1/p)+O_q(p).
 } \tag{4.4}
\]

At `q=1/4`,

\[
 \boxed{J_A-M_A=\frac12p\log_2(1/p)+O(p).} \tag{4.5}
\]

Consequently, any universal scalar correction `Gamma(p)` satisfying

\[
 J_A\le M_A+\Gamma(p)
\]

for every genuine two-bit Boolean gate and every interior product bias must obey

\[
 \liminf_{p\downarrow0}
 \frac{\Gamma(p)}{p\log_2(1/p)}\ge\frac12.
\]

This proves the logarithmic endpoint *order* is necessary. It does not prove that the coefficient `1` in `Delta(p)` is optimal.

Because B19 supplied this missing proof, claim `B19-A091-AND-ENDPOINT-LOWER-BOUND-v1` is **PROVED_PENDING_FRESH_INDEPENDENT_REVIEW**, not independently accepted by this same run.

## 5. Composition scope

### 5.1 Exact multiplicative tensors — proved

Let `f=f_1 f_2` with disjoint input sets and product input measure. Split the physical block as `A=A_1 union A_2`. The biased Fourier coefficients factor, hence the spectral law is the product of the two factor spectral laws. For every physical restriction, the child spectral law also factors. Therefore

\[
 M_A(f)=M_{A_1}(f_1)+M_{A_2}(f_2),
\]

\[
 J_A(f)=J_{A_1}(f_1)+J_{A_2}(f_2),
\]

and likewise `L` and `Delta` add. Induction gives the statement for finitely many disjoint multiplicative factors. This includes exact bent tensors and survives deterministic factor deletion.

### 5.2 General disjoint Boolean composition — not established by B09

O'Donnell--Tan's Theorem 1 concerns

\[
 f=F(g_1(x^1),\ldots,g_k(x^k))
\]

with disjoint inner variable blocks. It proves composition of their specifically normalized biased `FEI+` inequality. Proposition 3.2 gives the corresponding entropy, influence, and variance formulas using normalized centered inner functions and a partition of Fourier support by nonempty gate index sets.

That theorem does **not** say that B09's physical restriction channel `(Z,T)` tensorizes through an arbitrary gate. Conditioning on the gate input `g_i(x^i)` is not a physical coordinate restriction of `x^i`; it is generally a many-point fiber. A transfer theorem would have to state and prove how the gate-level `M,J,Delta` ledger couples to the inner physical restriction ledgers and how each endpoint tax is spent without reuse.

Accordingly:

* the B09 sentence that O'Donnell--Tan reduces disjoint read-once FEI questions to biased gate `FEI+` inequalities is **KNOWN / CORRECT**;
* the additive B09 ledger is **PROVED** only for exact multiplicative tensors;
* a B09-ledger closure theorem for arbitrary disjoint Boolean composition is **OPEN**;
* shared-variable or repeated-variable composition is **OUT OF SCOPE** and receives no conclusion.

The two-bit AND counterexample shows a gate-level obstruction to transplanting `J<=M`, but by itself it neither propagates a violation through a composition hierarchy nor produces an unbounded `H/I` ratio.

## 6. Mandatory obstruction and scope checks

* **Rare restrictions / sparse defects:** the new family itself has `p downarrow 0` and retains a positive `p log(1/p)` deficit. It is consistent with `B05_RARE_REFUNDS` and does not charge it to `O(p)`.
* **Addressing / multiplexers:** at uniform gate bias `Delta=0`; the accepted theorem reduces to the sharp uniform uncertainty ledger. No coordinatewise repetition of an address label is inferred.
* **Near tensors:** only exact multiplicative tensor additivity is asserted. Coherent surgery needs a separate `alpha^2 log(1/alpha^2)` payment.
* **Actual prime Boolean gate:** the lower bound uses the genuine two-bit AND sign, not a relaxed spectral vector.
* **Shared-variable interference:** explicitly excluded from the composition conclusion.
* **Deterministic and near-dictator endpoints:** deterministic inputs are deleted before biased normalization; (4.4) treats the near-deterministic limit from the interior.
* **Hierarchy/KL and child deficits:** the review does not claim a payment by influence, conditional total correlation, or child deficits. Those remain the missing universal bridge.

## 7. Validation

`check_b09_endpoint_family.py` evaluates the exact formulas (4.1)--(4.3) for `q=1/4`, `p=2^{-k}`, and

\[
 k\in\{3,4,6,8,10,12,16,20,24,30,40\}.
\]

It independently checks the conditional and joint formulas for `M`. The normalized ratio

\[
 \frac{J_A-M_A}{p\log_2(1/p)}
\]

rises from `0.3187867` at `k=3` to `0.4930337` at `k=40`, consistent with the proved limit `1/2`. At `p=1/8`, it reproduces the interval certificate's central values.

Command:

```text
python3 check_b09_endpoint_family.py
```

Observed runtime: 0.3 seconds. Arithmetic: IEEE-754 binary64, numerical corroboration only. Randomness: none. The asymptotic theorem is analytic.

## 8. Claim and dependency delta

### Accepted

* `B09-BIASED-BLOCK-UNCERTAINTY-v1`: `INDEPENDENTLY_REVIEWED_ACCEPT_AT_STATED_SCOPE`.
* `B09-TAXFREE-AND-COUNTEREXAMPLE-REPAIRED-v1`: `ACCEPT_FINITE_HELPER_REFUTATION_AT_STATED_SCOPE`.

### New / repaired

* `B19-A091-AND-ENDPOINT-LOWER-BOUND-v1`: `PROVED_PENDING_FRESH_INDEPENDENT_REVIEW`.
* `B19-A091-B09-COMPOSITION-SCOPE-v1`: exact multiplicative tensor additivity proved; broader B09-ledger composition explicitly open.

### Rejected overbroad reading

* The asymptotics of an upper bound alone imply endpoint optimality — **INVALID INFERENCE**, repaired by (4.4).
* O'Donnell--Tan automatically makes `M,J,Delta` additive through arbitrary Boolean composition — **NOT ESTABLISHED**.
* The two-bit gate certificate is an FEI counterexample — **FALSE SCOPE UPGRADE**.

## 9. Remaining obligation and handoff

The A091 artifact is complete for this review object. The mathematical packet remains short of a full-FEI bridge.

Fresh independent review should be routed to A090 or A085 for the new endpoint claim (4.4). The reviewer should derive (4.1)--(4.3) independently, check the asymptotic coefficient, and preserve the distinction between a necessary scalar tax and a hierarchy-level nonreuse theorem.

Concrete next action for the composition program: formulate a transfer identity for one gate coordinate substituted by one nonconstant Boolean inner function, comparing gate-output conditioning with actual physical restrictions of the inner block. The identity must expose the exact extra mixture/KL term; without it, no repeated composition payment should be claimed.

No protected evaluation material, held request, held PR229/source, live graph mutation, scheduler edit, email, public release, new worker, or paid compute was used. Native Brain ingestion and downstream use are not claimed.

## Execution metadata

Exposed assistant identity: Codex, based on GPT-5. A reasoning-effort selector, billing identity, remaining allowance, and continuous-hour guarantee were not exposed. Mathematical derivation, numerical corroboration, persistence, independent acceptance, and future review are recorded separately.

