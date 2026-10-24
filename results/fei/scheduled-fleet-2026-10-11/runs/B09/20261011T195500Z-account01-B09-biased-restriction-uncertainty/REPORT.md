# B09 — product-biased restriction uncertainty: a prime-gate counterexample and an endpoint-safe repair

**Run:** `20261011T195500Z-account01-B09-biased-restriction-uncertainty`  
**Date:** 2026-10-11  
**Classification:** `PROVED_AUXILIARY_LEMMA_AND_REFUTED_HELPER`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Result in one line

For a genuine Boolean gate under an arbitrary product measure, the physical-block entropy decrement still splits exactly as

\[
L_A=M_A+J_A,
\]

where `M_A` is the actual conditional spectral-label entropy and `J_A` is the physical-child mixture information.  The uniform estimate `J_A<=M_A` is **false** at nonuniform biases, already for the two-bit AND sign gate.  The following endpoint-safe replacement is universal:

\[
\boxed{
0\le J_A\le M_A+\Delta_A(p),\qquad
L_A\le2M_A+\Delta_A(p),
}
\tag{0.1}
\]

where

\[
\boxed{
\Delta_A(p)=\sum_{i\in A}
\left[h_2(p_i)+\log_2\max\{p_i,1-p_i\}\right].
}
\tag{0.2}
\]

At the uniform bias, `Delta_A=0`, recovering `J_A<=M_A`.  At a rare endpoint,

\[
h_2(p)+\log_2(1-p)
=p\log_2(1/p)+O(p^2),\qquad p\downarrow0,
\tag{0.3}
\]

so the repair retains the rare-event logarithm required by the current B05 obstruction.

## 1. Continuity and source pins

The current campaign status and plan were read at the start of the run:

- `yspennstate/math-open-problems/reports/fei-2026-10-11/CURRENT_STATUS.md`, blob `b41d59bda7a8b8c67bb047894906b1cf3aa8a44e`;
- campaign `README.md`, blob `95f6d823ee84b409f761da44fe7ed7986ec7bd0a`;
- `FEI_100_agent_research_plan.tex` on current master;
- Brain campaign `CURRENT_STATUS.md`, blob `b41d59bda7a8b8c67bb047894906b1cf3aa8a44e`;
- Brain campaign `README.md`, blob `95f6d823ee84b409f761da44fe7ed7986ec7bd0a`.

No earlier completed B09 folder was found in the new `reports/fei-2026-10-11/runs/B09/` campaign tree.  The materially relevant originals were read, not merely their status labels:

- account01/B13 block currency and exact Numaro source calculation, blob `6e25a01be249fc1c60fe955e93187fa476d725be`;
- account02/B16 translation/XOR-fiber uncertainty, which proves the uniform Walsh-conjugate bound and sharp phase obstruction;
- account02/B13 physical block/Holevo identity, blob `69c9c84b24b7a201d46f6071591fafcc874aea75`;
- current B05 rare-restriction report, blob `1b7e3cb572354cac4e506d7de0a3ed8af720472b`;
- the corrected Numaro biased-prime falsifications and composition-prime reduction reports found in the September archive.

Primary literature checked:

- O'Donnell--Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347.  It is the source for the product-biased disjoint composition framework; no novelty is claimed for that framework.
- Maassen--Uffink, *Generalized entropic uncertainty relations*, Phys. Rev. Lett. 60 (1988), 1103--1106, DOI `10.1103/PhysRevLett.60.1103`.

The new point of this run is the exact specialization of the non-mutually-unbiased transform to a physical product-biased restriction, its explicit endpoint tax, and the source-valid prime-gate falsifier to the tax-free version.  Publication novelty has not been independently reviewed.

## 2. Exact product-biased block ledger

Work on `{0,1}^n`.  Let the coordinates be independent with

\[
\Pr[X_i=1]=p_i\in(0,1),
\]

and use the orthonormal one-bit basis

\[
\phi_i(0)=-\sqrt{\frac{p_i}{1-p_i}},\qquad
\phi_i(1)=\sqrt{\frac{1-p_i}{p_i}}.
\]

For Boolean `f`, write `hat f_p(S)` for the resulting product-biased Fourier coefficients and

\[
\mu(S)=\widehat f_p(S)^2.
\]

Fix a block `A` and put `B=[n]\setminus A`.  For a physical assignment `z` on `A`, let `f_z` be the restricted Boolean function on `B`, with the inherited product biases, and let `mu_z` be its biased spectral law.  For `S~mu`, write `S_A=S cap A` and `S_B=S cap B`.  Define

\[
M_A:=H(S_A\mid S_B),
\]

\[
J_A:=H(S_B)-\mathbb E_{z\sim\mu_{p_A}}H(\mu_z),
\]

and

\[
L_A:=H(\mu)-\mathbb E_zH(\mu_z).
\]

Exactly as in the uniform physical-restriction identity,

\[
\boxed{L_A=M_A+J_A.}
\tag{2.1}
\]

Indeed, biased Parseval on the revealed coordinates gives

\[
q_T:=\Pr[S_B=T]
=\sum_{R\subseteq A}\widehat f_p(R\cup T)^2
=\mathbb E_z\widehat{f_z}_{p_B}(T)^2.
\]

Thus the average child law is exactly the parent marginal `q`, so entropy concavity gives `J_A>=0`, and the chain rule gives (2.1).  Equivalently, under the joint experiment `Z~mu_{p_A}`, then `T~mu_Z`,

\[
J_A=I(Z;T).
\tag{2.2}
\]

All signs, child normalizations, physical branch probabilities, and zero masses remain in this identity.

## 3. PROVED: biased uncertainty bound with explicit rare-event tax

### Theorem B09-BIASED-BLOCK-UNCERTAINTY-01

For every finite Boolean `f`, every interior product-bias vector `p`, and every physical block `A`, equations (0.1)--(0.2) hold.

### Proof

Fix `T subseteq B` with `q_T>0` and define the normalized spectral-fiber vector

\[
a_R=\frac{\widehat f_p(R\cup T)}{\sqrt{q_T}},
\qquad R\subseteq A.
\]

Its squared entries have entropy `H(S_A | S_B=T)`.  Define the normalized physical posterior vector

\[
b_z=\frac{\sqrt{\mu_{p_A}(z)}\,\widehat{f_z}_{p_B}(T)}{\sqrt{q_T}},
\qquad z\in\{0,1\}^A.
\]

Its squared entries are the conditional law `Pr[Z=z | T]`.

The two vectors are related by the tensor orthogonal matrix

\[
b=U_Aa,
\qquad
U_A=\bigotimes_{i\in A}
\begin{pmatrix}
\sqrt{1-p_i}&-\sqrt{p_i}\\
\sqrt{p_i}&\sqrt{1-p_i}
\end{pmatrix}.
\tag{3.1}
\]

The largest absolute matrix entry is

\[
c_A=\prod_{i\in A}\sqrt{\max\{p_i,1-p_i\}}.
\]

Maassen--Uffink therefore gives, fiber by fiber,

\[
H(a^2)+H(b^2)
\ge-2\log_2c_A
=-\sum_{i\in A}\log_2\max\{p_i,1-p_i\}.
\tag{3.2}
\]

Average (3.2) with weights `q_T`.  The first average is `M_A`; the second is `H(Z|T)`.  Since

\[
J_A=H(Z)-H(Z\mid T),
\qquad
H(Z)=\sum_{i\in A}h_2(p_i),
\]

we obtain

\[
J_A\le M_A+\Delta_A(p).
\]

Together with `L_A=M_A+J_A` and `J_A>=0`, this proves (0.1).  The endpoint expansion (0.3) follows by expanding `h_2(p)` and `log_2(1-p)`; the linear `p/ln 2` terms cancel.  QED.

### Scope

This is a product-biased restriction lemma.  It is not a strong FEI inequality for arbitrary weighted thresholds, and it does not bound `M_A` by influence.  Its value is to identify exactly how the uniform Walsh uncertainty payment degrades at biased gate inputs.

## 4. REFUTED: the tax-free biased extension

### Candidate B09-TAXFREE-BIASED-UNCERTAINTY (false)

> For every genuine Boolean gate, every interior product bias, and every physical block `A`, `J_A<=M_A`.

Take the essential two-input Boolean gate

\[
g(x,y)=(-1)^{xy},
\]

which is AND up to the sign/output convention.  Let

\[
p=\Pr[X=1]=\frac18,
\qquad
q=\Pr[Y=1]=\frac14,
\qquad A=\{X\}.
\]

The exact squared biased Fourier masses, in the order `empty,{X},{Y},{X,Y}`, are

\[
\boxed{
\left(\frac{225}{256},\frac7{256},\frac3{256},\frac{21}{256}\right).
}
\tag{4.1}
\]

The residual spectral bit has probability

\[
\Pr[S_Y=1]=\frac3{32}.
\]

The `X=0` child is constant, while the `X=1` child is the `Y` character, whose biased spectral nonempty mass is `3/4`.  Hence

\[
M_A
=H\left(\frac{225,7,3,21}{256}\right)-h_2\left(\frac3{32}\right),
\tag{4.2}
\]

\[
J_A
=h_2\left(\frac3{32}\right)-\frac18h_2\left(\frac34\right).
\tag{4.3}
\]

The rational atanh-series interval certificate gives

\[
0.227909707141212807<M_A<0.227909707141212808,
\]

\[
0.347454723165637765<J_A<0.347454723165637766,
\]

and therefore

\[
\boxed{
0.119545016024424957
<J_A-M_A<
0.119545016024424958.
}
\tag{4.4}
\]

Thus the tax-free extension fails by more than `0.1195` bits on the smallest nonlinear genuine Boolean gate.  This is a gate-helper counterexample, not an FEI counterexample: it says nothing about unbounded `H/I`.

## 5. Composition and prime-gate consequences

O'Donnell--Tan's product-biased composition theorem already reduces disjoint read-once compositions to gate inequalities at the induced output biases.  The exact matrix in (3.1) is compatible with that reduction: it is a tensor product on disjoint blocks, and both `Delta_A` and the aligned `M_A,J_A` ledgers add.

Therefore:

1. decomposable gates do not create a new violation of (0.1) beyond their factors;
2. the two-bit AND gate proves that a prime-gate proof cannot simply transplant the uniform `J<=M` statement to induced nonuniform biases;
3. a composition proof using this uncertainty route must either pay `Delta_A(p)` once, amortize it against a hierarchy credit, or exploit stronger Boolean phase constraints;
4. because `Delta(p)=p log_2(1/p)+O(p^2)`, replacing it by `O(p)` is impossible at the endpoint scale relevant to rare activation.

The unpaid universal implication remains a dimension-free payment of the actual conditional label cost `M_A` plus the nonreused endpoint tax by the appropriate biased influence/gate potential.

## 6. Required obstruction suite

### Addressing / multiplexers

At uniform address inputs, revealing all `m` address bits gives exactly

\[
M_A=m,\qquad J_A=m,\qquad L_A=2m.
\]

Thus the uniform inequality is sharp and the whole address label is shared, rather than charged separately for each spectral coordinate.  Deterministic checks cover `m=1,2,3`.

### Sparse defects and rare restrictions

Full-block restrictions of one-point defects give the opposite endpoint `J_A=0`, `M_A=H`.  Checks cover dimensions `2..8`.  Trigger-block restrictions of majority-3 activated by `k=1..5` rare bits retain the full conditional cost and satisfy the proved inequality.  Analytically, (0.3) shows that the repaired theorem retains, rather than suppresses, the rare-event logarithm exposed by B05.

### Near tensors

For exact disjoint products and aligned blocks, the spectral law, physical posterior channel, `M`, `J`, and `Delta` all tensorize additively.  The checker includes quadratic bent tensors through seven factors.  This theorem makes no continuity claim for coherent near-tensor surgery; such a claim would need to pay the known `alpha^2 log(1/alpha^2)` term.

### Actual composition-prime gate

The exact source-reconstructed 18-bit Numaro gate was checked at the two previously adversarial biases `p_0=3/8` and `p_0=223/456`, with all other inputs uniform, plus the uniform point.

At `p_0=3/8`:

| block | `M_A` | `J_A` | `L_A` | `Delta_A` |
|---|---:|---:|---:|---:|
| `{0}` | 0.5762864062 | 0.4049643169 | 0.9812507231 | 0.2763620978 |
| `{0,9}` | 0.6023189002 | 0.4125076062 | 1.0148265063 | 0.2763620978 |
| `{9}` | 0.0234236096 | 0.0096299386 | 0.0330535482 | 0 |

Every tested row satisfies (0.1).  This finite test is numerical evidence only; the theorem is analytic.

The older uniform prime calculation is also preserved: for an expensive auxiliary singleton, `M/(4Q)=5.9529497461`, `J/(4Q)=2.4706909456`; after pairing it with its source host, these become `3.4570767826` and `2.4601328226`.  The repair is mostly compression of joint spectral multiplicity, not an increase in coherent KL credit.

## 7. Reproduction and outputs

Commands executed:

```text
python check_restriction_multiplicity.py > CHECKER_OUTPUT.json
python check_numaro_multiplicity.py > NUMARO_OUTPUT.json
python check_biased_restriction.py > BIASED_OUTPUT.json
python check_biased_and_counterexample.py > INTERVAL_OUTPUT.txt
```

Randomness: **NONE**.  Python numerical checks use IEEE double precision; the decisive two-bit counterexample uses rational arithmetic with an explicit atanh-series remainder.

SHA-256:

| file | SHA-256 |
|---|---|
| `check_restriction_multiplicity.py` | `681a863d484cd7652ec41f88d39f070ee28d45260db063846eea102f6fd80a14` |
| `check_numaro_multiplicity.py` | `7aea7e522c7afece7a57cdb37c0fa246a8c107b82f6980c8b814f9f8dd274d3e` |
| `check_biased_restriction.py` | `6f6c7b7e717e16b3cc34b4ac2aec822968aff3e6b571add2ba3296d6d97cdfaa` |
| `check_biased_and_counterexample.py` | `3147bc3d2dfeb54a2ecabce7c074131d9985a22fcd55b9a9fda3c4656b5af1fc` |
| `CHECKER_OUTPUT.json` | `1809a22dc91b44b28b3c8b0b84c501d3a1eee99d3c08fe4010f1edf62a2beb39` |
| `NUMARO_OUTPUT.json` | `88e0adb43f19609b8060f56eee29ab1bdecdcd12bf1866da8fd72b9bf1ec1d2e` |
| `BIASED_OUTPUT.json` | `b57599cbb6800cad549b45955103acb4adea9383893d5c30d1480c32f3c31f2d` |
| `INTERVAL_OUTPUT.txt` | `87c895efc5cd286203f253e84c0ba368fb8976e3939c6b2ca34d465249d92adf` |

## 8. Claim delta and handoff

**Previous status:** the uniform physical restriction fibers are Walsh conjugates and obey `J<=M`; arbitrary product biases were a live gate obstruction, and the current biased Numaro instances had already refuted several proposed finite-center potentials.

**New proved movement:** the exact restriction identity extends to arbitrary product biases, but the conjugate bases cease to be mutually unbiased.  The loss is universally bounded by the explicit additive tax `Delta_A(p)`.  The tax-free extension is rigorously refuted on the two-bit AND gate by (4.4).

**New first missing implication (OPEN):** construct a nonreusing composition/restriction potential that pays

\[
M_A+\Delta_A(p)
\]

by biased influence uniformly over composition-prime gates and arbitrary interior biases, or improve the Maassen--Uffink tax using a specifically Boolean constraint while retaining the exact two-bit counterexample and the rare endpoint asymptotic.

**Concrete next action:** solve the one-bit block optimization under Boolean-realizable coefficient fibers, beginning with all essential two-input gates.  Determine the sharp scalar replacement for `Delta(p)` and test whether its endpoint coefficient can be transported through the O'Donnell--Tan gate cocycle without being paid repeatedly.

## 9. Lifecycle and review status

- mathematical derivation: **PROVED on the page**;
- two-bit counterexample: **PROVED with rational interval certificate**;
- finite obstruction-suite calculations: **NUMERICAL / deterministic**;
- independent end-to-end review: **NOT RUN**;
- native Brain ingestion: **NOT CLAIMED**;
- full FEI proof or counterfamily: **NOT OBTAINED**.

No protected evaluation material, held proof-chain payload, new worker, paid computation, merge, deployment, email, public publication, scheduler change, or live-store/graph mutation was used.

Exposed runtime identity: Codex based on GPT-5.  A separate reasoning-effort selector, provider-side reasoning usage, billing identity, and remaining allowance meters were not exposed.
