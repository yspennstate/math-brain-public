# B14 FEI — residual mixed-boundary crossing cover and block activation refund

**Run:** `B14-20260921T232918Z-r11`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Outcome:** **ESSENTIAL_STEP_APPLIED (partial branch / exact reduction).** Full uniform-cube Fourier entropy--influence remains **OPEN / NOT PROVED**.  
**Claim level:** two universal lemmas plus an explicit realizable physical stopping phase that plugs into the current account01/B18 folded-cooling compiler. No novelty or publication-priority claim.

## 0. Candidate version and exact old/new missing implication

This run follows the newer `FEI-PROOF-EXECUTION-20260921T230620Z` reset rather than the stale slot wording. The campaign-A lead input is the newest completed account01/B18 candidate available on fresh scientific master:

- `proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.

Its folded potential is
\[
\mathcal A_z(f)=\min_T\sum_S\widehat f(S)^2\Phi_z(|S\triangle T|),
\qquad z_d=1-1/d,
\]
and its exact compiler says that full FEI follows if fixed universal `gamma>0`, `K<infinity`, `lambda>=0` exist such that every high-`\mathcal G_\lambda/\mathcal J` restriction-critical core contains a physical block/survivor pair `(A,j)` satisfying
\[
c_j(A)\ge \gamma p_j,
\qquad
E_A-\lambda\Lambda_A\le K h_2(p_j).
\tag{0.1}
\]
Here `E_A=Delta_A mathcal F`, `c_j(A)` is the posterior-majority crossing of the `j`-pivotality event, and `Lambda_A` is the genuine folded activation drop. The resulting finite constant is
\[
\max\{\rho_*,9K/(2\gamma)\}+\lambda+2/\ln2,
\qquad \rho_*=4h_2(1/4).
\]

The older account01/B18 curvature report used below is
`account01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`, blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`, which proves
\[
\Delta_A\mathcal F
\le B_A-\sum_{j\notin A}\mathfrak j'(p_j)c_j(A),
\qquad
D_A=\mathcal J-\mathbb E\mathcal J_{child}=I_A+C_A.
\tag{0.2}
\]

**Old missing implication:** produce (0.1) on a realizable original-coordinate block without reusing the global folded/crossing refunds.

**New implication proved here:** crossing is automatic once the unrevealed mixed pivotality boundary is small, and the folded activation drop of an arbitrary physical block dominates `e^{-1}` times the block's original folded influence. Hence any boundary-covering block with bounded Shannon rate `B_A/I_A` is already a full `(gamma,0,lambda)` certificate for the lead compiler. The remaining obstruction is isolated as a precise high-Shannon-rate boundary-cover exception, not prescribed-coordinate payment.

## 1. Normalization and the exact mixed-boundary object

Median-character center the current Boolean state, so
\[
0\le p_i=\operatorname{Inf}_i(f)\le\tfrac12,
\qquad \mathcal J=I=\sum_i p_i.
\]
For a survivor `j`, let
\[
\eta_j(x_{-j})=1_{\{f(x)\ne f(x\oplus e_j)\}},
\qquad \mathbb E\eta_j=p_j.
\]
For a physical reveal block `A` not containing `j`, write
\[
U_j^A=\mathbb P(\eta_j=1\mid X_A),
\qquad
c_j(A)=\mathbb E(2U_j^A-1)_+.
\]
For distinct `i,j`, define the original-coordinate mixed boundary
\[
b_{ij}:=\operatorname{Inf}_i(\eta_j).
\tag{1.1}
\]
On each `(i,j)` face, the statement that the two `j`-edges have different pivotality status is equivalent to the statement that the two `i`-edges have different pivotality status. Therefore
\[
\boxed{b_{ij}=b_{ji}.}
\tag{1.2}
\]
This is the support-boundary part of the live mixed-curvature object; no affine coordinate change is made.

For a reveal block `A`, define the **unrevealed exception boundary**
\[
R_j(A):=\sum_{i\notin A\cup\{j\}}b_{ij}.
\tag{1.3}
\]

## 2. PROVED: residual boundary forces posterior crossing

### Theorem 2.1 — posterior-crossing / exception inequality

For every centered Boolean `f`, every relevant `j`, and every physical `A` not containing `j`,
\[
\boxed{c_j(A)\ge p_j-\frac12R_j(A).}
\tag{2.1}
\]
Consequently, for every fixed `0<gamma<=1`,
\[
\boxed{R_j(A)\le2(1-\gamma)p_j\quad\Longrightarrow\quad c_j(A)\ge\gamma p_j.}
\tag{2.2}
\]

### Proof

For `U=U_j^A`, the pointwise identity
\[
u-(2u-1)_+=\min(u,1-u)
\]
gives
\[
p_j-c_j(A)=\mathbb E\min(U,1-U).
\tag{2.3}
\]
By concavity of binary entropy and the chord from `(0,0)` to `(1/2,1)`,
\[
h_2(u)\ge2\min(u,1-u),
\]
so
\[
p_j-c_j(A)\le\frac12H(\eta_j\mid X_A).
\tag{2.4}
\]
Now fix a fiber `X_A=z`. Applied to the deterministic binary label `eta_j` on the residual uniform cube, the standard chain-rule/JS--TV argument gives
\[
H(\eta_j\mid X_A=z)
\le\sum_{i\notin A\cup\{j\}}
\operatorname{Inf}_i(\eta_j\mid X_A=z).
\]
Averaging the fiber reconstructs the original residual edge boundaries, hence
\[
H(\eta_j\mid X_A)\le R_j(A).
\tag{2.5}
\]
Combining (2.4) and (2.5) proves (2.1), and (2.2) follows immediately. QED.

This inequality is exact on the two-survivor endpoint. If only coordinate `k` remains unresolved beside `j`, then every fiber posterior is in `{0,1/2,1}` and
\[
\boxed{c_j(A)=p_j-\tfrac12b_{jk},}
\]
recovering the existing non-affine-two-face identity rather than introducing a different relaxation.

The theorem also preserves the known addressing obstruction: it never asks a prescribed target coordinate to pay for itself. A target may cross only after revealing the physical coordinates that carry its pivotality boundary.

## 3. PROVED: arbitrary physical blocks have an `e^{-1}` folded-activation reserve

The lead report proves the exact block activation
\[
\Lambda_A
=\sum_S\widehat f(S)^2
z_d^{|(S\triangle T_*)\setminus A|}
\Phi_{z_d}(|(S\triangle T_*)\cap A|),
\]
where `T_*` is any parent minimizer for the folded potential. Its report states the singleton lower bound. The same formula yields a stronger block statement.

### Theorem 3.1 — block activation lower bound

At a state with `d` unresolved physical coordinates, for every physical block `A`,
\[
\boxed{
\Lambda_A
\ge e^{-1}\sum_{i\in A}\mathbb P(i\in X\triangle T_*)
\ge e^{-1}I_A.
}
\tag{3.1}
\]

### Proof

Put `z=1-1/d` (the `d=1` case is direct). For one spectral atom set
\[
k=|(S\triangle T_*)\cap A|,
\qquad
\ell=|(S\triangle T_*)\setminus A|.
\]
If `k=0` there is nothing to prove. If `k>=1`,
\[
z^\ell\Phi_z(k)
=z^\ell\sum_{r=0}^{k-1}z^r
\ge k z^{\ell+k-1}
\ge k z^{d-1}
\ge e^{-1}k.
\]
Average over the spectral atom. The first inequality in (3.1) follows. For every coordinate, the minimizing-gauge marginal `P(i in X triangle T_*)` is either `p_i` or `1-p_i`, hence is at least the folded marginal `min(p_i,1-p_i)=p_i` in the centered gauge. QED.

Together with the lead's adaptive cooling telescope, (3.1) is a genuinely nonreused resource: the sum of all realized `Lambda` expenditures down a restriction tree is still at most the root `J`.

## 4. PROVED: an explicit boundary-covering block is a complete lead certificate whenever its Shannon rate is bounded

Fix `gamma in (0,1]`. Call a physical block `A` a `gamma`-boundary cover for survivor `j` when
\[
R_j(A)\le2(1-\gamma)p_j.
\tag{4.1}
\]
Define its Shannon rate by `B_A/I_A`, with the zero-cost case interpreted separately.

### Theorem 4.1 — boundary-cover certificate

Fix finite `L`. If `(A,j)` satisfies (4.1) and
\[
\boxed{B_A\le L I_A,}
\tag{4.2}
\]
then, with the lead potential parameter
\[
\boxed{\lambda=eL,}
\tag{4.3}
\]
that same physical pair is a `(gamma,K=0,lambda)` folded-cooling certificate:
\[
\boxed{c_j(A)\ge\gamma p_j,\qquad E_A-\lambda\Lambda_A\le0.}
\tag{4.4}
\]

### Proof

The crossing statement is Theorem 2.1. The corrected decrement obeys `E_A<=B_A` because the corrected recombination rebate is nonnegative. Theorem 3.1 and (4.2) give
\[
E_A-eL\Lambda_A
\le L I_A-eL(e^{-1}I_A)=0.
\]
QED.

Therefore the account01/B18 compiler immediately gives the following honest conditional end-to-end statement:

> If some fixed finite `L` and fixed `gamma>0` have the property that every high-`G_{eL}/J` physical restriction-critical core has one survivor and one physical block satisfying (4.1)--(4.2), then full FEI follows with
> \[
> \boxed{H(f)\le\left(\rho_*+eL+\frac2{\ln2}\right)I(f).}
> \tag{4.5}
> \]

No such universal `L` is proved here. Equation (4.5) is conditional, not a claimed FEI bound.

## 5. A realizable adaptive stopping phase with total unpaid Shannon entropy `O(J)`

The previous theorem gives a physical stopping policy, not just an existential algebraic rewrite.

At each reached nonconstant centered state:

1. for each relevant survivor `j`, inspect physical boundary-cover blocks satisfying (4.1);
2. if at least one such block also satisfies `B_A<=L I_A`, reveal one of them in the original coordinates and recurse on the actual physical children;
3. otherwise stop and label the leaf `HIGH_RATE_BOUNDARY_COVER_EXCEPTION`.

Every executed step has
\[
B_A\le L I_A\le L D_A,
\qquad
D_A=J-\mathbb E J_{child}=I_A+C_A.
\]
Thus the exact folded drift telescopes and proves
\[
\boxed{
\sum_{u\,internal}w_u B_{A_u}
\le L\sum_u w_uI_{A_u}
\le L\sum_u w_uD_{A_u}
\le LJ(root).
}
\tag{5.1}
\]
The same tree spends at most the root `J` from the folded activation bank by the lead theorem. Hence neither Shannon payment nor folded refund is reused.

This is a genuine adaptive physical policy with an `O(J)` unpaid-Shannon budget on its active phase. It is **not** a complete FEI induction because it can stop at the exception leaves in step 3.

The exact remaining universal obstruction is therefore:

\[
\boxed{
\text{Every }\gamma\text{-boundary cover of every candidate survivor has }B_A/I_A>L
}
\tag{5.2}
\]
for arbitrarily large fixed `L`, on a high corrected-ratio critical core. This is the next interface-A/B arrow: either rule out (5.2), or show that this high-rate covering obstruction forces one of the already influence-relative mixed-curvature/stability payments.

## 6. Relation to account01/B18 curvature refund and no-reuse accounting

The exact source-to-next-arrow use of the curvature theorem is now transparent. On a high critical core, account01/B18 gives
\[
B_A\ge\rho I_A+\sum_{j\notin A}(\rho+\mathfrak j'(p_j))c_j(A).
\tag{6.1}
\]
Theorem 2.1 supplies an original-coordinate lower bound on the **same** `c_j(A)` already present in (6.1); it does not create a second crossing bank. Theorem 3.1 supplies a lower bound on the **same** `Lambda_A` already present in the newer folded-cooling compiler; it does not create a second activation bank. Consequently the branch theorem (4.4) uses each refund exactly once.

The exception (5.2) is intentionally not replaced by the false statements `sum d_i=O(J)`, fixed-relative near-subcube payment, or prescribed-coordinate restriction payment. Those remain refuted at their recorded scopes.

## 7. Decisive computation

A fresh checker tested the exact new statements rather than rerunning an old FEI battery.

- `628602` event/block cases: every Boolean event through four variables with density at most `1/2`, over every reveal block. Maximum violations of `H(Y|X_A)<=residual boundary`, `c>=p-R/2`, the identity `p-c=E min(U,1-U)`, and the one-residual-coordinate equality were all exactly `0.0` in double arithmetic.
- `21084250` `(d,k,l)` termwise activation cases through `d=500`: maximum violation of the `e^{-1}` block-activation atom bound was `0.0`.
- `2138` centered Boolean functions/samples (all sign-normalized functions through dimension three plus 2000 deterministic pseudorandom dimension-four functions): mixed-boundary symmetry and the full block activation bound had maximum violation `0.0`.
- For the concrete entropy-cheap specializations `L in {3,4,6,8}` and `gamma=1/2`, `29959` triggered boundary-cover policy cases had zero crossing violation; the maximum value of `B_A-e L Lambda_A` was `-2.0580670570164257`.

Checker SHA-256: `4dbb37442b074c846042eac4123ca65f047f88adc776c4581ddd9273485bba9e`.  
Captured output SHA-256: `81358e6d0ebac1ba33e3eb43691a26141122c40c620cff9475b596adbd0e4b3d`.

These computations are sanity checks only. The all-dimensional results above are analytic.

## 8. Status and next arrow

**PROVED this run:** (2.1), (3.1), the complete boundary-cover certificate (4.4), and the adaptive phase budget (5.1).

**PRESERVED:** the addressing obstruction to prescribed-coordinate payment; exact block drift `D_A=J-EJ_child=I_A+C_A`; all fixed-relative near-subcube and ordinary-depth no-go results; full FEI status OPEN.

**NOT PROVED:** a dimension-independent upper bound on the minimum Shannon rate of a boundary-covering block at every high corrected-ratio core. This is the only new condition needed to turn the current branch into a complete use of the lead compiler.

**Next recipient / arrow:** campaign-A lead account01/B18 and induction partner account04/B18 should combine the high-rate boundary-cover exception (5.2) with the current mixed-curvature/row-stability branch. A successful next theorem would show that if all low-rate physical blocks leave more than `2(1-gamma)p_j` of every pivotality boundary unresolved, then the resulting joint derivative boundary mass triggers an already telescoping influence-relative payment.

Full FEI remains **OPEN / NOT PROVED**.
