# account01/B15 — logarithmic branch compiler for the restriction KL chain

**Run:** `20260922T110241Z-account01-B15-r11-log-branch-compiler`  
**Classification:** `ESSENTIAL_STEP_APPLIED`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Exact current target and source pins

The current owner programme is `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`. The account01/B15 assignment is **Restriction I-projection chain rule**: transfer the exact occurrence-marginal KL credit through a genuine physical restriction and retain every reference-movement term.

This run starts from the preceding account01/B15 theorem

- repository `yspennstate/math-open-problems`, commit `b293d016f9bd94819fb11385986608b8acc0b83d`, path `proofnet24/P03-fei/fleet-2026-09-22/account01/B15/b15-20260922T103236Z-restriction-iprojection-chain/REPORT.md`,

which proved, for a physical restriction of coordinate `j` at bias `s`,
\[
\mathcal K(W)
=(1-s)\mathcal K(U)+s\mathcal K(V)
+C_{\rm marg}+C_{\rm erase}+C_{\rm pair}
-\operatorname{JS}_s(U,V),
\tag{0.1}
\]
where all three `C` terms are nonnegative and
\[
\mathcal K(W)=vK_{\rm occ}(W^+).
\]
The only negative term is the genuine child-mixture entropy `-JS_s(U,V)`.

The required named compatible OTHER-account result consumed is account02/B15

- repository `yspennstate/math-open-problems`, commit `ad83138c850372d14d0dcacaa76a50a2fe79bcaf`, path `proofnet24/P03-fei/fleet-2026-09-22/account02/B15/20260922T103316Z-account02-B15-r11/REPORT.md`.

Its Lemma 2.1 shows that binning both source and reference log-masses preserves KL up to at most two bits times the discarded source mass, and its Theorem 3.1 applies this to Boolean character suspensions with an `O(I)` loss while retaining the rare-event logarithm. I apply the same principle to the **negative restriction entropy** in (0.1), not merely cite it.

The current mandatory preflight is the recursive-majority low-level-KL obstruction: fixed or sub-half-depth individually labelled atoms followed by one merged tail do not recover the needed KL. The statistic below uses the complete child spectral laws at every restriction node and therefore is genuinely multiscale; no Fourier-level cutoff is introduced.

## 1. Physical split notation

Let the two genuine child Fourier amplitude vectors be
\[
u_T=\widehat {G_0}(T),\qquad v_T=\widehat {G_1}(T),
\]
and their full squared-spectrum laws
\[
U_T=u_T^2,\qquad V_T=v_T^2.
\]
Write
\[
\alpha=1-s,\qquad \beta=s,
\qquad E_T=\alpha U_T+\beta V_T.
\]
Let `B` be the physical branch label, with
\[
\Pr(B=0,T)=\alpha U_T,\qquad
\Pr(B=1,T)=\beta V_T.
\]
Then
\[
\operatorname{JS}_s(U,V)=I(B;T).
\tag{1.1}
\]

For Boolean children define the disagreement probability
\[
\delta=\Pr(G_0\ne G_1).
\]
Parseval gives
\[
\sum_T(u_T-v_T)^2=4\delta.
\tag{1.2}
\]
The parent spectral occurrence mass of the physical selector coordinate is therefore
\[
\boxed{
\rho_j
=s(1-s)\sum_T(u_T-v_T)^2
=4s(1-s)\delta.
}
\tag{1.3}
\]
This is the project quantity denoted `It_j` in the physical restriction normalization.

## 2. The logarithmic branch statistic

Fix a bin width `eta>0`. Define a deterministic statistic `Z_eta(T)` as follows.

- If `U_T=0<V_T`, record a one-sided-support tag, the `eta`-log bin of `V_T`, and the actual sign of `v_T`.
- If `V_T=0<U_T`, record the analogous one-sided-support tag, the `eta`-log bin of `U_T`, and the actual sign of `u_T`.
- If `U_T,V_T>0`, record
\[
\left(
\operatorname{sgn}u_T,\operatorname{sgn}v_T,
\left\lfloor{-\log_2U_T\over\eta}\right\rfloor,
\left\lfloor{-\log_2V_T\over\eta}\right\rfloor
\right).
\tag{2.1}
\]
Atoms with `U_T=V_T=0` have no source mass and are irrelevant.

Define the retained logarithmic branch information
\[
\boxed{J_\eta:=I(B;Z_\eta(T)).}
\tag{2.2}
\]
By data processing,
\[
0\le J_\eta\le \operatorname{JS}_s(U,V).
\]
The exact residual is
\[
R_\eta:=I(B;T\mid Z_\eta)
=\operatorname{JS}_s(U,V)-J_\eta\ge0.
\tag{2.3}
\]
One-sided-support cells have zero conditional residual because the branch is already determined by the support tag. Thus the rare `s\log(1/s)` information carried by support mismatch is retained exactly in `J_eta`.

## 3. A bounded-likelihood-ratio JS lemma

### Lemma 3.1

Let `P,Q` be probability laws and `t in (0,1)`. Put `M=(1-t)P+tQ`. If
\[
R^{-1}\le {P_x\over Q_x}\le R
\]
on their common support, then
\[
\boxed{
\operatorname{JS}_t(P,Q)
\le
{(1+\sqrt R)^2\over\ln2}
\,t(1-t)
\sum_x(\sqrt{P_x}-\sqrt{Q_x})^2.
}
\tag{3.1}
\]

#### Proof

Using `ln y <= y-1`,
\[
\operatorname{JS}_t(P,Q)
\le {t(1-t)\over\ln2}
\sum_x{(P_x-Q_x)^2\over M_x}.
\tag{3.2}
\]
Pointwise,
\[
{(P-Q)^2\over M}
=(\sqrt P-\sqrt Q)^2
{(\sqrt P+\sqrt Q)^2\over (1-t)P+tQ}.
\]
Writing `r=P/Q`, the final factor is
\[
{(\sqrt r+1)^2\over (1-t)r+t}
\le (1+\sqrt R)^2,
\]
because the denominator is at least `min(r,1)`. Summing proves (3.1). `QED`

## 4. Cell-mass lemma

### Lemma 4.1

Let `a,b>0`, `0<t<1`, and `0<=h<=2`. Then
\[
\boxed{
{ab\over (1-t)a+tb}\,h
\le
2\bigl[(\sqrt a-\sqrt b)^2+\sqrt{ab}\,h\bigr].
}
\tag{4.1}
\]

#### Proof

Since `(1-t)a+tb >= min(a,b)`, the left side is at most `max(a,b) h`. Suppose `a>=b` and write `r=sqrt(a/b)>=1`. It suffices to show
\[
r^2h\le2(r-1)^2+2rh.
\]
For `1<=r<=2` this is immediate. For `r>=2`, the left minus the `2rh` term is increasing in `h`, so use `h<=2`:
\[
h(r^2-2r)\le2r(r-2)\le2(r-1)^2.
\]
The case `b>=a` is symmetric. `QED`

## 5. Main theorem: the negative JS term splits into retained logarithmic information plus a uniform influence tax

### Theorem 5.1 — `B15-RESTRICTION-LOG-BRANCH-COMPILER-v1`

For every genuine Boolean physical restriction, every `s in (0,1)` and every bin width `eta>0`,
\[
\boxed{
\operatorname{JS}_s(U,V)
=J_\eta+R_\eta,
\qquad
0\le R_\eta\le c_\eta\rho_j,
}
\tag{5.1}
\]
where
\[
\boxed{
c_\eta={2(1+2^\eta)^2\over\ln2}.}
\tag{5.2}
\]
For one-bit log bins (`eta=1`),
\[
\boxed{c_1={18\over\ln2}=25.9685107360\ldots .}
\tag{5.3}
\]
Crucially, `c_eta` is independent of the selector bias `s`. The earlier direct estimate `JS_s <= kappa(s) rho_j` has `kappa(s)~log_2(1/s)` as `s->0`; (5.1) moves that rare logarithm into the explicit retained information `J_eta` and leaves only a bias-uniform influence tax.

#### Proof

Condition on a common-support cell `z` of `Z_eta`. Let
\[
a_z=U(Z_\eta=z),\qquad b_z=V(Z_\eta=z),
\]
and let `U^z,V^z` be the normalized conditional laws. Put
\[
e_z=\alpha a_z+\beta b_z,
\qquad
s_z={\beta b_z\over e_z}.
\]
The chain rule for mutual information gives
\[
R_\eta
=\sum_z e_z\operatorname{JS}_{s_z}(U^z,V^z).
\tag{5.4}
\]
On a common-support cell, both raw squared masses vary by factors less than `2^eta`; hence the raw likelihood ratio `U_T/V_T` varies by a factor less than `2^{2eta}`. Since `a_z/b_z` is a `V^z`-weighted average of that raw likelihood ratio, the normalized likelihood ratio satisfies
\[
2^{-2\eta}
< {U^z_T\over V^z_T}
<2^{2\eta}.
\tag{5.5}
\]
Lemma 3.1 with `R=2^{2eta}` gives
\[
e_z\operatorname{JS}_{s_z}(U^z,V^z)
\le
{(1+2^\eta)^2\over\ln2}
\alpha\beta{a_zb_z\over e_z}
H_z^2,
\tag{5.6}
\]
where
\[
H_z^2=\sum_{T\in z}(\sqrt{U^z_T}-\sqrt{V^z_T})^2\le2.
\]
By Lemma 4.1,
\[
{a_zb_z\over e_z}H_z^2
\le
2\left[(\sqrt{a_z}-\sqrt{b_z})^2+\sqrt{a_zb_z}H_z^2\right].
\tag{5.7}
\]
The bracket is exactly
\[
\sum_{T\in z}(\sqrt{U_T}-\sqrt{V_T})^2.
\]
Summing common-support cells, while noting that one-sided-support cells have zero conditional residual, gives
\[
R_\eta
\le
{2(1+2^\eta)^2\over\ln2}
\alpha\beta
\sum_T(|u_T|-|v_T|)^2.
\tag{5.8}
\]
Finally
\[
(|u_T|-|v_T|)^2\le(u_T-v_T)^2,
\]
so by (1.2)-(1.3),
\[
R_\eta\le c_\eta\rho_j.
\]
`QED`

This proof preserves the actual Fourier signs: they are part of the statistic, and the last inequality only relaxes from signed amplitude distance to absolute-amplitude distance after the information decomposition has been made.

## 6. Applied to the exact I-projection restriction chain

Substitute
\[
\operatorname{JS}_s(U,V)=J_\eta+R_\eta
\]
into the exact predecessor identity (0.1). Then
\[
\mathcal K(W)
=(1-s)\mathcal K(U)+s\mathcal K(V)
+C_{\rm marg}+C_{\rm erase}+C_{\rm pair}
-J_\eta-R_\eta.
\tag{6.1}
\]
Therefore Theorem 5.1 yields the coefficient-one transfer
\[
\boxed{
\mathcal K(W)+J_\eta+c_\eta\rho_j
\ge
(1-s)\mathcal K(U)+s\mathcal K(V)
+C_{\rm marg}+C_{\rm erase}+C_{\rm pair}.
}
\tag{6.2}
\]
Every reference-movement credit survives with its correct sign. No fixed fraction of child `K_occ` is discarded. The only unretained part of the negative entropy term costs a fixed multiple of the **actual physical selector influence**, uniformly all the way to `s->0`.

This is the direct application of the account02/B15 log compiler to the account01/B15 restriction chain.

## 7. Nonreusing physical restriction trees

Consider any deterministic physical restriction tree under a product measure, never querying a coordinate twice along a root-to-leaf path. Let `pi_u` be the probability of reaching internal node `u`, let `j(u)` be its queried coordinate, and let `rho_{j(u),u}` be the corresponding spectral occurrence mass.

For each original coordinate `i`, nodes querying `i` have disjoint reach cylinders that are invariant under flipping `i`. Hence
\[
\sum_{u:j(u)=i}\pi_u\rho_{i,u}
\le \rho_i(\text{root}).
\tag{7.1}
\]
Summing over coordinates,
\[
\boxed{
\sum_u\pi_u\rho_{j(u),u}
\le I_{\rm spectral}(\text{root}).
}
\tag{7.2}
\]
At the uniform cube this is exactly the usual total influence `I(f)`.

Multiplying (6.2) by `pi_u` and telescoping gives the multiscale restriction-tree compiler
\[
\boxed{
\mathcal K_{\rm root}
+\sum_u\pi_uJ_{\eta,u}
+c_\eta I(f)
\ge
\mathbb E\,\mathcal K_{\rm leaves}
+\sum_u\pi_u
(C_{{\rm marg},u}+C_{{\rm erase},u}+C_{{\rm pair},u}).
}
\tag{7.3}
\]
for the uniform cube, and the analogous product-bias statement with root spectral influence on the right side of (7.2).

This is genuinely multiscale: `J_{eta,u}` is computed from the complete child spectral laws at every physical node. It neither keeps only low Fourier levels nor merges all high levels into one tail, so the recursive-majority low-level-projection counterexample does not apply to the statement. Equation (7.3) also passes the sparse-suspension no-loss requirement: the exact `K_occ` is transferred with coefficient one and the only discarded conditional branch information is `O(I)`.

## 8. Required obstruction checks

- **Sparse defects / suspensions.** The partner theorem already shows the global log-magnitude compiler loses at most `2I` on every character suspension. The present theorem does not replace that rare logarithm by an unweighted quadratic statistic; support-mismatch logarithms are retained exactly in `J_eta`, and the remaining loss is `<=c_eta rho_j`.
- **Recursive ternary majority.** No fixed Fourier-level cutoff occurs. The compiler is recomputed from full spectra at every restriction depth, and the total fixed influence tax is bounded by (7.2), independent of depth.
- **Tensor products.** The theorem is local to a genuine physical restriction and uses original coordinates. Exact product factors can be restricted without creating a fictitious coordinate label or dropping the hierarchy/reference-mismatch credits.
- **Addressing, majority and tribes.** No symmetry, monotonicity, sparsity or low arity is assumed, so these are included without a separate case split.
- **Biased limit.** The uncontrolled remainder constant `c_eta` is independent of `s`; the `log(1/s)` scale is stored in the explicit mutual information `J_eta`, rather than hidden in the error coefficient.

## 9. Exact old/new missing implications

**Old missing implication after the preceding B15 run.** The exact restriction chain had the negative debit
\[
-\operatorname{JS}_s(U,V),
\]
and the only direct universal payment available was
\[
\operatorname{JS}_s(U,V)\le\kappa(s)\rho_j,
\qquad \kappa(s)\sim\log_2(1/s),
\]
so the rare-bias logarithm still appeared as an uncontrolled restriction tax.

**New result.** The debit now splits exactly as
\[
-\operatorname{JS}_s=-J_\eta-R_\eta,
\qquad
R_\eta\le c_\eta\rho_j,
\]
where `J_eta` is an explicit retained logarithmic mutual-information bank and `c_eta` is bias-uniform. The restriction tree pays the entire discarded remainder with at most `c_eta I(f)` while preserving child `K_occ` with coefficient one.

**New first unpaid implication.** Prove, for a nonreusing physical restriction/stopping strategy, that the exact Bellman deficit `[-B_inf^Gamma]_+` is dominated by the accumulated retained branch-information bank
\[
\sum_u\pi_uJ_{\eta,u}
\]
plus a fixed `O(I(f))` reserve, or construct a genuine Boolean family for which that domination fails. This is now the sharp place where the rare-event logarithm lives. Establishing that payment with one finite constant would combine with the exact `K_occ` chain toward the Path-B FEI closure. No such universal domination is proved here.

## 10. Status

`ESSENTIAL_STEP_APPLIED`.

The result removes the logarithmically divergent coefficient from the **unretained** restriction entropy loss, preserves all actual source signs and original-coordinate influence, transfers child `K_occ` with coefficient one, and gives a nonreusing multiscale tree inequality. It does **not** prove the full FEI inequality and does not claim that finite tests, a potential repair, or an equivalent reformulation settles FEI.
