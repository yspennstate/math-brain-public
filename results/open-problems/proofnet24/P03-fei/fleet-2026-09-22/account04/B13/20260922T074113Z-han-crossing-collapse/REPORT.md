# B13 — Han collapse gives an all-row influence-relative crossing budget

**Run:** `B13-20260922T074113Z-fei-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## Change summary

The current Campaign-A gap after account04/B14 is that its terminal theorem gives only a per-coordinate posterior-crossing cap, which by itself could still sum to ambient dimension. This report proves that this accumulation cannot occur on an actual corrected-ratio critical core. The proof uses only the source-exact critical-core inequality, Han/chain-rule entropy, and the exact curvature refund.

For a median-centered Boolean function write

\[
q_i=\operatorname{Inf}_i(f)\le \tfrac12,\qquad
\mathcal J=\sum_i q_i,
\]
\[
\mathfrak j(q)=1-h_2\!\left(\tfrac12+\sqrt{q(1-q)}\right),\qquad
\mathcal P=\sum_i\mathfrak j(q_i),\qquad
\mathcal F=H-\mathcal P.
\]
For a physical singleton pivot `i`, let
\[
c_j(i)=\mathbb E(2q_j(X_i)-1)_+,\quad
C_i=\sum_{j\ne i}c_j(i),\quad
W_i=\sum_{j\ne i}\mathfrak j'(q_j)c_j(i),
\]
and let
\[
B_i=H(X_i\mid X_{-i})
\]
for the spectral sample `X`.

The account01/B18 critical-core theorem gives, at an actual \(\mathcal F/\mathcal J\)-critical core of ratio \(\rho>2\),
\[
B_i-W_i\ge \rho(q_i+C_i)\qquad\text{for every }i.
\tag{1}
\]

## Theorem — all-row crossing collapse

At every such critical core,
\[
\boxed{\rho\sum_i C_i+\sum_iW_i\le\mathcal P.}
\tag{2}
\]
Equivalently, defining the incoming all-row crossing load
\[
R_j:=\sum_{i\ne j}c_j(i),
\]
we have
\[
\boxed{\sum_j\bigl(\rho+\mathfrak j'(q_j)\bigr)R_j\le\mathcal P.}
\tag{3}
\]
Consequently
\[
\boxed{\sum_iC_i\le {\mathcal P\over\rho}
\le {2\over\rho\ln2}\,\mathcal J,}
\tag{4}
\]
and hence the sum of all singleton folded drifts satisfies
\[
\boxed{\sum_i(q_i+C_i)\le
\left(1+{2\over\rho\ln2}\right)\mathcal J.}
\tag{5}
\]
There is no ambient-dimension factor.

### Proof

Sum (1):
\[
\sum_i B_i-\sum_iW_i\ge \rho\mathcal J+\rho\sum_iC_i.
\tag{6}
\]
For any jointly distributed spectral bits, conditioning on all other coordinates is at least as informative as conditioning only on preceding coordinates. Thus for any fixed order,
\[
H(X_i\mid X_{-i})\le H(X_i\mid X_{<i}).
\]
Summing and using the chain rule gives
\[
\sum_iB_i\le H(X)=H(f).
\tag{7}
\]
At the ratio-critical core \(\mathcal F=\rho\mathcal J\), so
\[
H=\mathcal F+\mathcal P=\rho\mathcal J+\mathcal P.
\tag{8}
\]
Insert (7)--(8) into (6) and cancel \(\rho\mathcal J\), obtaining (2).

Reindexing the nonnegative crossing matrix gives
\[
\sum_iC_i=\sum_jR_j,
\qquad
\sum_iW_i=\sum_j\mathfrak j'(q_j)R_j,
\]
which is (3). Since \(\mathfrak j'\ge0\), (4) follows from the sharp scalar cap \(\mathcal P\le(2/\ln2)\mathcal J\), and (5) follows by adding \(\sum_iq_i=\mathcal J\). QED.

## Influence-relative exceptional rows

For \(\lambda>0\), define
\[
E_\lambda=\{j:q_j>0,\ R_j/q_j>\lambda\}.
\]
Then (3) immediately yields
\[
\boxed{
\sum_{j\in E_\lambda}q_j
\le {\mathcal P\over\rho\lambda}
\le {2\over\rho\lambda\ln2}\mathcal J.
}
\tag{9}
\]
Thus the exceptional set is controlled in the influence measure itself. This is precisely the type of all-row estimate missing from a per-row bound: arbitrary exceptional rows are allowed, but their total folded influence is paid from a single dimension-free bank.

A stronger weighted form, with \(r_j=R_j/q_j\), is
\[
\sum_j(\rho+\mathfrak j'(q_j))q_jr_j\le\mathcal P,
\tag{10}
\]
or, sampling a row proportionally to its folded influence,
\[
\mathbb E\big[(\rho+\mathfrak j'(q_j))r_j\big]\le\mathcal P/\mathcal J\le2/\ln2.
\tag{11}
\]

## Named newest compatible cross-account result and how it changes the argument

This run consumes account01/B14, commit `64c2dda1c7cc27fb28df263fd94f5c33eede1a0f`, `20260922T071413Z-majority-bounded-depth-barrier/REPORT.md`. It proves that for every fixed depth there are sufficiently high-dimensional odd majorities on which every local `F(d)` payment in the proposed F-only selector is negative. Therefore bounded-depth local positivity is the wrong target: diffuse majority-like states force one to retain leaf/critical-core structure or a genuinely amortized bank.

That changes the present argument exactly as follows. Instead of trying to show that each row, or each of finitely many successive pivots, pays locally, (2)--(9) aggregate *all* posterior-crossing rows at the actual critical obstruction and charge them once to \(\mathcal P\). Majority-like diffuse behavior is therefore not forced into an impossible bounded-depth positive-payment condition; it is compatible with the theorem but cannot create dimension-times-small-crossing leakage.

## Relation to account04/B14 and the remaining implication

Account04/B14's current candidate-independent stopping theorem leaves terminal states satisfying
\[
h_2(q_i)-W_i>K(q_i+C_i)\quad\forall i,
\]
and explicitly identifies the remaining danger: its per-coordinate cap on `C_i` alone does not control \(\sum_iC_i\) dimension-freely. The theorem above closes that accumulation issue on a genuine \(\mathcal F/\mathcal J\)-critical core: there \(\sum_iC_i\le\mathcal P/\rho=O(\mathcal J)\).

This is not yet the full terminal-class theorem. The remaining source-exact arrow is to pass from an arbitrary bad terminal leaf to an actual critical restriction descendant without losing the relevant physical-row structure, then use the global bank (3) together with a realizable selector/block argument. No claim is made that the ordinary second-derivative depth sum is `O(J)`.

## Preservation of account04/B18 interface-B invariants

The exact mixed-curvature identity
\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}(p_{ik}+4o_{ik})=4d_k
\]
is untouched. In particular the opposite-sign term is not discarded and \(\sum_kd_k\) is not replaced by `O(J)`. The exact zero-defect classification from account04/B18 is also preserved unchanged. The new theorem concerns posterior-crossing accumulation and is complementary to that signed-curvature rigidity.

## Status

`ESSENTIAL_STEP_APPLIED`: a dimension-free, all-row, influence-relative exceptional-set estimate is proved for the actual corrected-ratio critical core, eliminating the ambient-dimension accumulation that remained after the stopping theorem. Full FEI is still **OPEN / NOT PROVED**.
