# B12 — AND/OR-atom stopping removes the ratio-32 spikes from the prime G10 block

**Outcome:** `ESSENTIAL_STEP_APPLIED / FINITE_GATE_STRUCTURE`. **Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** `WITHOUT_VERIFIED_BRAIN`. This run used authenticated repository sources and exact local arithmetic; no authenticated cognitive-brain retrieval or receiver context entered the proof.

## 1. Live target and why this is not another row-code pass

Fresh owner control revision `2026-09-22.2` supersedes the older interface-B row-coding prompt for substantive mathematics and orders every FEI worker to converge on the all-gate potential inequality

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},\qquad V_p=4p(1-p).
\tag{G}
\]

The source-exact gate-reformulation report proves that existence of one finite-cap symmetric nonnegative `Gamma` satisfying `(G)` for every Boolean gate and every product bias is equivalent to full FEI. The old read-once `Gamma` and the proposed AND/decomposable extremality are already source-validly falsified, so this run does not reopen that route.

The older account04/B18 mixed-curvature identity remains valid and preserved:
\[
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k.
\]
Nothing below assumes, uses, or implies `sum_k d_k = O(J)`.

## 2. Named newest compatible account02 results consumed

### account02/B13 — affine/character restriction atom

I consume

`proofnet24/P03-fei/fleet-2026-09-21/account02/B13/20260922T014831Z-g10-affine-restriction-atom/REPORT.md`.

For the exact balanced ten-input prime witness `G10`, truth-table SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`,

it proves that every proper nonconstant physical restriction `h`, even after multiplying by any balancing character and applying any invertible affine re-basing, satisfies either `I=1,H=0` or
\[
\frac{H}{I-1}\le
R_*:=\frac{46}{5}-\frac95\log_2 3
=6.3470674987\ldots<6.35<6.4548.
\tag{2.1}
\]
The root itself has
\[
I(G_{10})=\frac{257}{128},\qquad
\frac{H(G_{10})}{I(G_{10})-1}>6.459372281637855731.
\tag{2.2}
\]

**Exact implication used here:** the root obstruction cannot be replaced by a smaller balanced descendant, even after the full affine/character re-gauge relevant to the prior B13 critical-core mechanism. Therefore the continuation that must be paid is genuinely the unbalanced physical-restriction corridor.

### account02/B16 — exact restriction-margin martingale

I also consume

`proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`.

For base potential `Gamma_0=0` at uniform input bias, write
\[
P(G)=\frac{I(G)}4-p_{\rm out}(1-p_{\rm out}),
\]
and on a physical restriction step write `Q_r` for the exact Poincare-currency drop and `L_r` for the exact spectral-entropy drop. Then
\[
P(G)=\mathbb E\sum_r Q_r,
\qquad
H(G)=\mathbb E\sum_r L_r,
\tag{2.3}
\]
and, for every bounded stopping time `sigma`,
\[
P(G)c_G
=
\mathbb E\left[
\sum_{r<\sigma}Q_r c_r+P(G_\sigma)c_{G_\sigma}
\right],
\qquad c_r=\frac{L_r}{Q_r}.
\tag{2.4}
\]

**Exact implication used here:** one is allowed to separate a genuinely signed/continuation-preserving preterminal block from its terminal gate currency. A large one-step `L/Q` is not a universal obstruction if it is carried into a terminal gate whose own potential constraint is treated separately.

## 3. Previous B12 obstruction and the new question

The preceding B12 fixed-order calculation on this same `G10` found a physical reveal order `0,1,...,9` with no proper balanced nonaffine state. It also found 96 positive-`Q` states along the corridor, with 37 states attaining the maximal raw local ratio
\[
\frac{L}{Q}=32,
\]
and total branch-weighted currency
\[
\frac{29}{1024}.
\tag{3.1}
\]

That result showed why a balanced-return proof fails, but left open whether the ratio-32 mass represents a diffuse high-dimensional prime phenomenon or a recognizable terminal atom.

This run answers that question exactly.

## 4. New theorem — first AND/OR-atom stopping

Follow the fixed physical reveal order `0,1,...,9`. Stop at the first node which is either

1. affine (`P=0`), or
2. after deleting dummy variables, a two-essential-input AND/OR gate, including input/output negations.

### Theorem 4.1

For the exact witness `G10`, this stopping rule has
\[
\boxed{\Pr(\text{AND/OR terminal})=\frac{29}{64}},
\qquad
\boxed{\Pr(\text{affine terminal})=\frac{35}{64}}.
\tag{4.1}
\]

Every nonaffine terminal has output bias `1/4` or `3/4` and exactly
\[
I=1,\qquad P=\frac1{16},\qquad H=2.
\tag{4.2}
\]
Hence its total expected continuation currency and entropy are
\[
\boxed{
\mathbb E P(G_\sigma)=\frac{29}{1024},
\qquad
\mathbb E H(G_\sigma)=\frac{29}{32}.
}
\tag{4.3}
\]

At the root
\[
P(G_{10})=\frac{129}{512},
\]
so the consumed preterminal block has exact Poincare currency
\[
\boxed{
Q_{\rm block}
=P(G_{10})-\mathbb E P(G_\sigma)
=\frac{229}{1024}.
}
\tag{4.4}
\]

Using rigorous rational logarithm enclosures for `H(G10)`, the block entropy/Poincare margin satisfies
\[
\boxed{
25.057083819433480
<
\frac{H(G_{10})-29/32}{229/1024}
<
25.057083819433481.
}
\tag{4.5}
\]
In particular it is strictly below `25.1`.

### Proof

The checker reconstructs the exact source witness from the inherited 18-variable construction and verifies its SHA-256. It then explores only the branches of the deterministic reveal order that have not yet hit an affine state or a two-essential-input AND/OR atom. Every branch terminates.

Exact rational branch weights sum to one. The AND/OR terminal weights sum to `29/64`; the affine terminal weights sum to `35/64`. Direct truth-table reduction at each nonaffine terminal verifies that its essential two-variable table is one of the four AND/OR sign forms, with the exact data in (4.2). Summing branch weights yields (4.3), and subtraction from the exact root `P=129/512` gives (4.4).

For (4.5), the root Walsh transform is computed over integers. Each spectral entropy term is enclosed by a rational atanh series with a rigorous tail. Subtract the exact terminal entropy `29/32` and divide by the exact block currency `229/1024`. No floating-point value decides the assertion. `square`

## 5. What the theorem identifies

Equation (4.3) exactly matches the `29/1024` branch-weighted `Q` mass previously carried by the 37 ratio-32 states. The apparently dangerous local value `32` is therefore not a mysterious high-dimensional continuation in this corridor: its entire terminal currency is concentrated in ordinary two-input AND/OR atoms.

This gives a concrete child-slack-preserving decomposition of the source-valid prime witness:

* **prime/unbalanced preterminal block:** raw `Gamma_0=0` margin `<25.1`;
* **terminal nonaffine continuation:** exact two-input AND/OR atoms with raw margin `32`;
* **other terminal continuation:** affine, hence zero Poincare currency and zero spectral entropy.

The newest certified balanced center obstruction from the independent shared-graft family satisfies
\[
C_{\rm FEI}>6.521850949550448\ldots,
\]
so in the `Gamma_0=0` scalar-margin units its center scale is already
\[
4C_{\rm FEI}>26.0874>25.1.
\tag{5.1}
\]
Thus the exotic prime block of `G10` itself is below the current center scale; the larger raw `32` demand is entirely exported to the classical arity-two terminal atoms.

This is exactly the sort of continuation credit that blind one-step induction discards.

## 6. Important limitation

This is **not** a proof that one may simply splice the read-once potential onto the `Gamma_0=0` block estimate. The all-gate inequality uses one and the same `Gamma` at every node and every bias. A nonlinear potential changes both block residuals and terminal constraints; raw `Gamma_0=0` margins do not add as independent certificates.

The next exact implication is therefore sharply isolated:

> **terminal-atom subtraction problem.** Recompute the preterminal stopping block under one common candidate symmetric potential `Gamma` that already certifies every two-input AND/OR gate, and prove that the resulting signed block margin is nonpositive (or uniformly bounded by the candidate center cap) while retaining the terminal continuation exactly.

For this explicit `G10`, account02/B13 removes the escape through hidden balanced descendants, and Theorem 4.1 removes the ambiguity about where the ratio-32 continuation lives. What remains is a single-potential compatibility calculation, not an ambient-dimensional row entropy payment.

## 7. Verification

Checker:
`check_and_atom_stopping.py`

Executed SHA-256:
`9dd5836d912347bcc4af6afdbeebffbd797495badc4f6fad328a82586dcfccb6`

Recorded output SHA-256:
`20821cb0eaf5fdaa5aa2664d873afbfdb572f550b03614c443c3192550a9c684`

`py_compile` passed and the exact checker returned `PASS`.

## 8. Ledger

- **PROVED / inherited:** all-gate `(G)` is equivalent to full FEI.
- **REFUTED / inherited:** the old read-once `Gamma` and AND/decomposable extremality as a universal all-gate candidate.
- **PROVED / account02/B13:** `G10` is an affine/character restriction atom; no proper descendant re-gauges into a smaller balanced obstruction above the old cap.
- **PROVED / account02/B16:** exact all-depth `P/Q` restriction-margin martingale with continuation slack retained.
- **PROVED / this run:** under the fixed physical corridor, all nonaffine terminal continuation is exactly two-input AND/OR, with terminal probability `29/64`, expected terminal `P=29/1024`, expected terminal `H=29/32`, and preterminal block raw margin in the interval (4.5).
- **OPEN:** common-`Gamma` terminal-atom subtraction and all remaining universal gates/biases.
- **FULL FEI:** `OPEN / NOT PROVED`.

No novelty or publication-priority claim is made.