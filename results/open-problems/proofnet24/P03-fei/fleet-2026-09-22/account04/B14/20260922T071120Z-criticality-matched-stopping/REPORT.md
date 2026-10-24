# B14 — criticality-matched posterior-crossing stopping theorem

**Run:** `B14-20260922T071120Z-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / REALIZABLE_STOPPING_REDUCTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim.

## 0. Change summary

This run changes mechanism from the preceding fixed-candidate MUX/two-face calculations. It proves a candidate-independent adaptive physical stopping theorem whose selection rule is exactly matched to the account01/B18 curvature-refunded critical-core inequality.

There are two forms. The literal-Shannon policy pays every queried spectral conditional-entropy term from exact folded-influence drift. The stronger curvature-aware policy first spends the account01/B18 survivor-crossing refund and charges only the remainder. Both terminate after at most the original dimension many queries along each branch.

Every terminal leaf has, for every physical coordinate, both small folded influence and a quantitative upper bound on singleton posterior-crossing drift. Conversely, every `F/J`-critical core of ratio `rho` satisfies exactly the terminal inequalities at `K=rho`.

This does **not** repair the now-refuted fixed all-gate candidate `Gamma^dagger`. The newest account01/B18 correction and account04/B18 prime-Bellman work show that fixed candidate fails on an exact composition-prime 18-input gate. The theorem here survives that correction because it is a candidate-independent restriction reduction for the original uniform-cube FEI problem.

## 1. Exact source dependencies consumed

### 1.1 account01/B18 curvature-refunded restriction inequality

Source:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`

blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`.

For a median-centered Boolean function write

\[
q_i=\operatorname{Inf}_i(f)\le\tfrac12,
\qquad
\mathcal J(f)=\sum_i q_i,
\]

\[
\mathfrak j(q)=1-h_2\!\left(\tfrac12+\sqrt{q(1-q)}\right),
\qquad
\mathcal P(f)=\sum_i\mathfrak j(q_i),
\qquad
\mathcal F=H-\mathcal P.
\]

For a physical block `A`, with pivotality posteriors `q_j(z)=E[eta_j|x_A=z]`, define

\[
c_j(A)=\mathbb E_z(2q_j(z)-1)_+,
\qquad
C_A=\sum_{j\notin A}c_j(A).
\]

The source proves the exact folded drift

\[
\boxed{D_A:=\mathcal J(f)-\mathbb E_z\mathcal J(f_{A=z})=I_A+C_A,
\qquad I_A=\sum_{i\in A}q_i,}
\tag{1.1}
\]

and the curvature-refunded corrected-entropy inequality

\[
\boxed{\Delta_A\mathcal F
\le B_A-\sum_{j\notin A}\mathfrak j'(q_j)c_j(A),}
\tag{1.2}
\]

where `B_A=H(X_A|X_{A^c})` for the Fourier spectral random set `X`.

At an `F/J`-critical centered core of ratio `rho`, the same source proves

\[
\boxed{B_A\ge\rho I_A+
\sum_{j\notin A}(\rho+\mathfrak j'(q_j))c_j(A).}
\tag{1.3}
\]

Also `j'(q)>=0` on `[0,1/2]`.

### 1.2 newest account01/B18 owner-pivot correction

Source:

`proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260922T065447Z-two-level-anti-amplification/CURRENT_OWNER_PIVOT_CORRECTED.md`

blob `13aacee16ac78f05d89cde2d493a115cf3579d6a`.

It records that the old fixed all-gate candidate

\[
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p)
\]

is refuted by an exact composition-prime 18-input gate. Therefore no fixed-`Gamma^dagger` collar is used here as universal closure evidence.

### 1.3 current prime-Bellman correction

The compatible account04/B18 continuation

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T071537Z-prime-repair-shape-barrier/PRIME_BELLMAN_ENVELOPE.md`

proves a prime-gate envelope fixed-point reduction. The restriction theorem below is orthogonal to that fixed-potential repair: it gives a universal physical-stopping reduction regardless of which all-gate potential eventually survives.

## 2. Singleton notation and the marginal entropy bound

At every reached node, median-center by multiplying by a character. This is bookkeeping only: it preserves `H` and `J`, and subsequent physical descendants differ only by harmless child characters.

For a physical coordinate `i`, abbreviate

\[
C_i:=C_{\{i\}},
\qquad
D_i:=D_{\{i\}}=q_i+C_i,
\tag{2.1}
\]

and define the account01/B18 weighted curvature refund

\[
W_i:=\sum_{j\ne i}\mathfrak j'(q_j)c_j(\{i\})\ge0.
\tag{2.2}
\]

The spectral random bit `X_i` has marginal `Pr(X_i=1)=q_i`; hence

\[
\boxed{B_i:=H(X_i\mid X_{-i})\le H(X_i)=h_2(q_i).}
\tag{2.3}
\]

No prescribed-coordinate payment is asserted. Payment is used only when a coordinate passes an explicit adaptive test.

## 3. Literal-Shannon stopping policy

Fix `K>2`. At a noncharacter node, query a physical coordinate `i` only if

\[
\boxed{h_2(q_i)<K(q_i+C_i)=K D_i.}
\tag{3.1}
\]

If no coordinate satisfies (3.1), stop. The strict selection convention is intentional: equality is left in the terminal class, which makes the terminal condition coincide exactly with criticality below.

### Theorem 3.1 — total literal Shannon payment

For the resulting physical tree,

\[
\boxed{\sum_{v\text{ internal}}\pi_v B_{i(v)}
\le K\sum_{v\text{ internal}}\pi_vD_{i(v)}
=K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_L)\bigr)
\le K\mathcal J(f).}
\tag{3.2}
\]

**Proof.** At every queried node, (2.3) and (3.1) give `B_i<KD_i`. Multiply by the reach probability and sum. The exact drift (1.1) telescopes on the adaptive physical tree. Since each query removes a physical coordinate, every branch has length at most `n`, so termination is finite. QED.

Thus the actual unpaid Shannon terms `B_i`, not merely a corrected surrogate, cost at most `KJ` over the entire selected phase.

## 4. Curvature-aware stopping policy

Use the account01/B18 refund before charging the Shannon term. Query `i` whenever

\[
\boxed{h_2(q_i)-W_i<K(q_i+C_i)=K D_i.}
\tag{4.1}
\]

Since `W_i>=0`, this covers every coordinate selected by the literal policy and possibly more.

### Theorem 4.1 — exact nonreused corrected payment

\[
\boxed{\mathcal F(f)-\mathbb E\mathcal F(f_L)
\le K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_L)\bigr).}
\tag{4.2}
\]

**Proof.** At a queried node, (1.2), (2.3), and (4.1) give

\[
\Delta_i\mathcal F\le B_i-W_i
\le h_2(q_i)-W_i<KD_i.
\]

Multiply by reach probability and sum. `F` and `J` telescope along the same actual physical tree. The refund `W_i` is spent only in the node where it is generated; it is never charged again. QED.

This is the exact source-to-next-arrow use of account01/B18: survivor curvature is converted into **extra selector coverage**, while exact folded drift remains the sole global currency.

## 5. Terminal structure

Every terminal leaf of the curvature-aware policy satisfies, for every physical coordinate,

\[
\boxed{h_2(q_i)-W_i\ge K(q_i+C_i).}
\tag{5.1}
\]

Since `W_i,C_i>=0`,

\[
h_2(q_i)\ge Kq_i.
\tag{5.2}
\]

Let `sigma_K in (0,1/2)` be the unique solution

\[
h_2(\sigma_K)=K\sigma_K.
\tag{5.3}
\]

The ratio `h_2(q)/q` is strictly decreasing because

\[
\frac{d}{dq}\frac{h_2(q)}q
=\frac{\log_2(1-q)}{q^2}<0.
\tag{5.4}
\]

Hence

\[
\boxed{q_i\le\sigma_K.}
\tag{5.5}
\]

Equation (5.1) also gives

\[
C_i\le\frac{h_2(q_i)}K-q_i.
\tag{5.6}
\]

The right side is maximized where `h_2'(q)=K`, namely

\[
q=\frac1{1+2^K},
\]

and the exact maximum is

\[
\boxed{\delta_K
:=\frac{\log_2(1+2^{-K})}{K}.}
\tag{5.7}
\]

Thus every terminal leaf obeys

\[
\boxed{q_i\le\sigma_K,
\qquad C_i\le\delta_K
\quad\text{for every }i.}
\tag{5.8}
\]

This is a per-physical-singleton conclusion. It deliberately does **not** multiply `delta_K` by dimension or claim `sum_i C_i=O(J)`.

For `K=4`,

\[
\sigma_4=0.156417354964272\ldots,
\qquad
\delta_4=\tfrac14\log_2(17/16)
=0.02186571031258485\ldots.
\tag{5.9}
\]

For calibration only, if one subtracts the universal phase cap `2/ln 2` from the formerly proposed center `6.521851214`, then

\[
K^\dagger=3.636461132222073\ldots,
\]

\[
\sigma_{K^\dagger}=0.196691838757933\ldots,
\qquad
\delta_{K^\dagger}=0.0306837862965097\ldots.
\tag{5.10}
\]

These numbers do not rehabilitate the refuted fixed all-gate candidate.

## 6. Exact match to account01/B18 criticality

Take an `F/J`-critical centered core of ratio `rho>2`. Apply (1.3) to `A={i}`:

\[
B_i\ge\rho q_i+
\sum_{j\ne i}(\rho+\mathfrak j'(q_j))c_j(\{i\})
=\rho(q_i+C_i)+W_i.
\tag{6.1}
\]

Together with `B_i<=h_2(q_i)`,

\[
\boxed{h_2(q_i)-W_i\ge\rho(q_i+C_i)=\rho D_i
\quad\text{for every }i.}
\tag{6.2}
\]

Therefore a ratio-`rho` critical core is **automatically terminal** for the curvature-aware stopping rule at `K=rho`. In particular,

\[
\boxed{q_i\le\sigma_\rho,
\qquad C_i\le\delta_\rho
=\frac{\log_2(1+2^{-\rho})}{\rho}.}
\tag{6.3}
\]

This is the exact matching property: the adaptive policy removes every state that violates the local inequality a genuine critical obstruction is forced to satisfy.

## 7. Compact conditional end-to-end compiler

### Theorem 7.1 — terminal-class sufficiency

Fix `K>2`. Suppose every median-centered Boolean function satisfying

\[
\boxed{h_2(q_i)-W_i\ge K(q_i+C_i)
\quad\text{for every physical coordinate }i}
\tag{7.1}
\]

obeys

\[
\mathcal F(f)\le K\mathcal J(f).
\tag{7.2}
\]

Then every Boolean function obeys

\[
\boxed{H(f)\le\left(K+\frac2{\ln2}\right)\mathcal J(f)
\le\left(K+\frac2{\ln2}\right)I(f).}
\tag{7.3}
\]

**Proof.** Run the curvature-aware tree. By (4.2),

\[
\mathcal F(f)
\le\mathbb E\mathcal F(f_L)
+K\bigl(\mathcal J(f)-\mathbb E\mathcal J(f_L)\bigr).
\]

Every leaf satisfies (7.1), so (7.2) gives

\[
\mathbb E\mathcal F(f_L)\le K\mathbb E\mathcal J(f_L).
\]

The leaf terms cancel exactly, yielding `F(f)<=KJ(f)`. Finally the source cap `P<=(2/ln2)J` gives (7.3). QED.

The accounting point is important: the stopping phase does **not** add a second `K` to the final constant. It is paid from `J` lost before reaching the terminal leaf.

## 8. What remains open

The A-interface has now been reduced to a sharply described terminal class: prove `F<=KJ` for centered Boolean functions in which every original physical singleton has enough residual Shannon slack after its exact curvature refund to satisfy (7.1). Every survivor also has the explicit coordinate caps (5.8).

For `K=4`, every survivor has folded influences at most about `0.15642` and singleton crossing at most about `0.02187`. These pointwise bounds alone are not enough, because multiplying them by ambient dimension would reintroduce the forbidden dimension loss. The next implication must exploit compatibility among the singleton posterior rows or the current prime-Bellman/all-gate structure.

The fixed `Gamma^dagger` candidate remains refuted; no replacement all-gate potential is claimed. Full FEI remains OPEN / NOT PROVED.

## 9. Obstruction and accounting checks

- **Addressing obstruction preserved:** no prescribed coordinate is asserted to pay. The policy may stop with no selected coordinate.
- **Exact physical drift preserved:** every global charge uses only `D_i=q_i+C_i=J-EJ_child`.
- **Original coordinates only:** no affine coordinate change or free selector label is introduced.
- **No reused refund:** `W_i` is spent once at its generating node.
- **No second-derivative O(J) assumption:** no depth sum is priced at unit cost.
- **Fixed-candidate correction preserved:** the old all-gate candidate is explicitly treated as refuted.

## 10. Scalar calibration

Direct numerical evaluation of the exact formulas gives

| `K` | `sigma_K` | `delta_K` |
|---:|---:|---:|
| 3 | 0.289250264292641 | 0.0566416671474375 |
| 4 | 0.156417354964272 | 0.0218657103125849 |
| 5 | 0.0814618699711691 | 0.00887882387169069 |
| 6.521851214 | 0.0291493929107398 | 0.00239429885899343 |

The theorem is analytic; these decimals are calibration only.

## 11. Source-to-next-arrow handoff

**Consumed source:** account01/B18 curvature-refunded inequality, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`.  
**Applied arrow:** `(1.2)+(B_i<=h_2(q_i))+(exact drift)` gives adaptive criterion (4.1) and global nonreuse (4.2); `(1.3)` gives the exact terminal match (6.2).  
**New output object:** the curvature-terminal class (7.1), with coordinate caps (5.8).  
**Remaining implication:** prove `F<=KJ` on that terminal class by a dimension-free compatibility argument, or construct a genuine Boolean counterexample to that terminal-class claim.  
**Full-problem change:** a genuine reduction, not closure; full FEI remains open.  
**Mechanism change:** yes — adaptive drift-threshold stopping matched to criticality, rather than another fixed-candidate gate collar or finite sweep.
