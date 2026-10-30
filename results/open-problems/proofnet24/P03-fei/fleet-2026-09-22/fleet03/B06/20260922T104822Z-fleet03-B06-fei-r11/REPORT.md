# fleet03/B06 — near-character fold: exact residual transport and conditional KL ledger

**Run:** `20260922T104822Z-fleet03-B06-fei-r11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, owner-control revision `2026-09-22.3`.  
**Assignment:** `FEI-20260922-fleet03-B06`, Path A, near-character influence channel.  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_NEAR_CHARACTER_REDUCTION / FULL_FEI_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Fresh-control correction and source scope

The fresh owner control supersedes the older BT4 assignment for this slot. This report therefore contains no new BT4 research. The current target is the full uniform-cube Fourier entropy-influence conjecture.

The exact inputs used here are:

1. **IPROJ**, fleet02/B15, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`: the nonempty spectral I-projection `Q_r`, the identity `K_occ=D_2(P||Q_r)=H_max(r)-H(P)`, and `R_Gamma=B_inf^Gamma+K_occ`.
2. **EQUALITY**, fleet03/B15, commit `84c69136ca6b008badb76f15bf1071d029c927aa`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T085625Z-product-equality-rigidity/REPORT.md`: exact balanced `K_occ=0` rigidity. It motivates a quantitative near-product channel but is not assumed quantitatively here.
3. **HIERARCHY**, fleet04/B15, commit `2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`: exact KL chain-rule accounting and the warning not to drop reference-change/hierarchy credit.
4. **SELECTOR_DEBIT**, fleet02/B12, commit `4ccd51ad517f425a529daa52c3352905b86ea69d`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`: the exact physical selector recursion and its retained child defects.
5. **FOLDED_JS**, fleet01/B12, commit `92c75e9bcd2fe9c5dc2bedc8a032b31b4afb5484`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B12/20260922T090347Z-folded-js-shannon/REPORT.md`: for a uniform selector, `JS_{1/2}(U,V) <= (2/ln 2) min{p,1-p}`.
6. **BALANCED**, fleet02/B18, commit `7d20a4bb4067085af7c5e7c9a82aef31998a7d36`, path `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260922T093253Z-balanced-slice-admission/REPORT.md`: on the balanced uniform slice, `D_Gamma=C(I-1)-H` and this is the same-constant FEI burden.

The assigned named partner is fleet04/B06. At the prepublication search, its latest completed artifacts were still BT4 artifacts from the superseded programme; no compatible completed FEI result for the new fleet04/B06 assignment was available. Per the current ORDER, this run did not wait or substitute that incompatible mathematics. The completed other-account FOLDED_JS and HIERARCHY results above were consumed directly.

## 1. Setup: fold a nearly-character coordinate

Let

\[
f:\{-1,1\}^n\to\{-1,1\}
\]

be balanced under the uniform measure, and fix a coordinate `j` with

\[
\operatorname{Inf}_j(f)=1-\epsilon,
\qquad 0\le\epsilon\le1.
\tag{1.1}
\]

Define the character-gauged Boolean function

\[
g(x)=x_j f(x).
\tag{1.2}
\]

Multiplication by `x_j` translates the Fourier spectrum exactly:

\[
\widehat g(S)=\widehat f(S\triangle\{j\}).
\tag{1.3}
\]

Consequently

\[
\boxed{H(g)=H(f),}
\tag{1.4}
\]

and, because toggling membership of `j` changes set size by `+1` off `j` and by `-1` on `j`,

\[
\boxed{I(g)=I(f)-1+2\epsilon.}
\tag{1.5}
\]

In particular

\[
\operatorname{Inf}_j(g)=\epsilon.
\tag{1.6}
\]

Let

\[
u=g\big|_{x_j=+1},\qquad v=g\big|_{x_j=-1}.
\tag{1.7}
\]

Since `g=x_j f`, these are `u=f_+` and `v=-f_-`. Balancedness of `f` gives

\[
\mathbb E u=\mathbb E v=:m.
\tag{1.8}
\]

Write their common `-1` bias as

\[
q={1-m\over2},\qquad V_q=4q(1-q)=1-m^2.
\tag{1.9}
\]

The physical disagreement of the children is exactly

\[
\Pr[u\ne v]=\operatorname{Inf}_j(g)=\epsilon.
\tag{1.10}
\]

Because two events of common measure `q` have symmetric difference `epsilon`,

\[
\boxed{\epsilon\le2\min\{q,1-q\}\le V_q.}
\tag{1.11}
\]

This elementary constraint is essential below: the rare folded branch always fits inside the nonconstant spectral mass of either child.

## 2. Main theorem A: exact all-gate residual transport

Let `Gamma` be any symmetric potential for which the project gate defect is defined, and put

\[
C=\Gamma(1/2).
\]

At uniform input, the gate defect is

\[
D_\Gamma(h)=C I(h)-\Gamma(q_h)-H(h),
\tag{2.1}
\]

where `q_h` is the output `-1` bias; for balanced `f`, `q_f=1/2`, so `D_Gamma(f)=C[I(f)-1]-H(f)`.

### Theorem 2.1 — `FEI-CHARACTER-FOLD-LEDGER-v1`

With the notation above,

\[
\boxed{
D_\Gamma(f)
={D_\Gamma(u)+D_\Gamma(v)\over2}
+\Gamma(q)-C\epsilon-\Delta(u,v),
}
\tag{2.2}
\]

where `Delta(u,v)` is exactly the conditional spectral-entropy increment of the uniform selector joining `u` and `v`.

#### Proof

Equations (1.4)-(1.5) give

\[
D_\Gamma(f)-D_\Gamma(g)
=\Gamma(q)-2C\epsilon.
\tag{2.3}
\]

Apply the exact selector recursion from SELECTOR_DEBIT to `g` at selector bias `s=1/2`. The two children have the same output bias `q` by (1.8), so the potential Jensen term cancels identically. The selector influence is `epsilon`, and `h_2(V_{1/2})=h_2(1)=0`. Hence

\[
D_\Gamma(g)
={D_\Gamma(u)+D_\Gamma(v)\over2}
+C\epsilon-\Delta(u,v).
\tag{2.4}
\]

Combining (2.3) and (2.4) proves (2.2). `QED`

This is the exact robust version of the familiar `epsilon=0` balancedization reduction. No continuity estimate, dimension factor, or discarded child defect appears.

## 3. Main theorem B: condition away the common output atom before Jensen

Let the uniform Fourier coefficients of `u,v` on the remaining coordinates be `u_T,v_T`, and let

\[
U_T=u_T^2,\qquad W_T=v_T^2,
\]

be their squared spectral laws. Put

\[
e_T={U_T+W_T\over2},
\qquad
\theta_T={ (u_T-v_T)^2\over 2(U_T+W_T)}
\tag{3.1}
\]

on nonzero packets. The exact selector identity from FOLDED_JS is

\[
\Delta(u,v)=B+\operatorname{JS}_{1/2}(U,W),
\qquad
B=\sum_T e_T h_2(\theta_T),
\tag{3.2}
\]

with

\[
\sum_Te_T\theta_T=\epsilon.
\tag{3.3}
\]

Equal child means improve the usual Jensen step. At the empty Fourier atom,

\[
u_\varnothing=v_\varnothing=m,
\]

so `theta_empty=0`, `e_empty=m^2=1-V_q`, and therefore

\[
\sum_{T\ne\varnothing}e_T=V_q,
\qquad
\sum_{T\ne\varnothing}e_T\theta_T=\epsilon.
\tag{3.4}
\]

Jensen only on the nonempty branch gives

\[
\boxed{
B\le V_q h_2\!\left({\epsilon\over V_q}\right),
}
\tag{3.5}
\]

with the value `0` at the degenerate `V_q=epsilon=0` endpoint.

There is a second exact two-branch identity. Since `U` and `W` have the **same** empty mass `1-V_q`, let `U^+,W^+` be their conditional laws on nonempty Fourier sets. The KL chain rule for Jensen-Shannon divergence gives

\[
\boxed{
\operatorname{JS}_{1/2}(U,W)
=V_q\operatorname{JS}_{1/2}(U^+,W^+).
}
\tag{3.6}
\]

Thus the common output atom is not charged as if it were part of the rare selector event. Applying FOLDED_JS at `s=1/2`,

\[
\operatorname{JS}_{1/2}(U,W)
\le {2\over\ln2}\min\{\epsilon,1-\epsilon\}.
\tag{3.7}
\]

For `epsilon<=1/2`, (3.5)-(3.7) yield the dimension-free near-character entropy debit

\[
\boxed{
\Delta(u,v)
\le
V_q h_2\!\left({\epsilon\over V_q}\right)
+{2\over\ln2}\epsilon.
}
\tag{3.8}
\]

Combining with Theorem 2.1 gives the main usable lower bound

\[
\boxed{
D_\Gamma(f)
\ge
{D_\Gamma(u)+D_\Gamma(v)\over2}
+\Gamma(q)
-\left(C+{2\over\ln2}\right)\epsilon
-V_q h_2\!\left({\epsilon\over V_q}\right).
}
\tag{3.9}
\]

### Corollary 3.2 — explicit near-character closure criterion

If the two child defects are nonnegative and

\[
\boxed{
\Gamma(q)
\ge
\left(C+{2\over\ln2}\right)\epsilon
+V_q h_2\!\left({\epsilon\over V_q}\right),
}
\tag{3.10}
\]

then `D_Gamma(f)>=0`.

This is a nonlocal payment lemma: the output-bias bank `Gamma(q)` pays the true folded selector entropy after the common output atom has been conditioned away. It retains the rare-event logarithm. Indeed, when `epsilon/V_q ->0`,

\[
V_q h_2(\epsilon/V_q)
=\epsilon\log_2(V_q/\epsilon)
+{\epsilon\over\ln2}
+O(\epsilon^2/V_q),
\tag{3.11}
\]

so no false `O(epsilon)` continuity claim is being made.

## 4. Main theorem C: exact two-branch I-projection KL under the character gauge

The same fold has a useful exact expression in the IPROJ coordinates.

Let

\[
P(S)=\widehat f(S)^2
\]

be the balanced nonempty spectral law and let `r_i=P(i in S)`. Thus `r_j=1-epsilon`. For the nondegenerate `mu=sum_i r_i>1` case, IPROJ constructs `Q_r` by taking independent Bernoulli coordinates with probabilities

\[
t_i=c r_i
\tag{4.1}
\]

and conditioning on the vector being nonempty, where `c` solves

\[
1-c=\prod_i(1-c r_i).
\tag{4.2}
\]

Define the actual branch laws on the remaining coordinates by

\[
A(T)={P(T\cup\{j\})\over1-\epsilon},
\qquad T\subseteq[n]\setminus\{j\},
\tag{4.3}
\]

and, for `epsilon>0`,

\[
B(T)={P(T)\over\epsilon},
\qquad \varnothing\ne T\subseteq[n]\setminus\{j\}.
\tag{4.4}
\]

Under the character translation (1.3), `A` and `B` are precisely the normalized squared spectra of the no-`j` and `j` parts of `g`. Let `Pi` be the **unconditioned** product law on the remaining coordinates with Bernoulli probabilities `t_i`, and let `Pi^+` be `Pi` conditioned on being nonempty.

### Theorem 4.1 — `FEI-CHARACTER-IPROJ-BRANCH-v1`

\[
\boxed{
K_{\rm occ}(f)
=(1-\epsilon)D_2(A\Vert\Pi)
+\epsilon D_2(B\Vert\Pi^+).
}
\tag{4.5}
\]

#### Proof

Under `Q_r`, the conditioned marginal probability that coordinate `j` is present is

\[
{t_j\over c}=r_j=1-\epsilon.
\]

If `j` is present, global nonemptiness is automatic, so the other coordinates have law `Pi`. If `j` is absent, the remaining coordinates must be nonempty, so they have law `Pi^+`. Therefore `P` and `Q_r` have the same two branch weights `(1-epsilon,epsilon)`, and the KL chain rule has zero branch-label term. The conditional terms are exactly (4.5). `QED`

This identity exposes the rare-event normalization exactly. Let

\[
\delta:=\Pi(T\ne\varnothing).
\]

Since the unconditioned global product has empty probability `1-c`,

\[
1-c=(1-t_j)(1-\delta)
=(1-c+c\epsilon)(1-\delta),
\]

hence

\[
\boxed{
\delta={c\epsilon\over1-c+c\epsilon}.
}
\tag{4.6}
\]

Moreover, because `B` is supported on nonempty sets,

\[
\boxed{
D_2(B\Vert\Pi)
=D_2(B\Vert\Pi^+)+\log_2{1\over\delta}.
}
\tag{4.7}
\]

Thus any argument that replaces the rare conditional reference `Pi^+` by the unconditioned product `Pi` must explicitly carry the weighted term

\[
\epsilon\log_2(1/\delta).
\tag{4.8}
\]

This is precisely the rare-event logarithm that unweighted-L2 or naive continuity arguments can lose. Equation (4.5) keeps the correct conditional reference, while (4.7) records the exact price of changing it.

The `mu=1` boundary is the singleton-spectrum case from IPROJ; for balanced Boolean functions this collapses to the dictator endpoint relevant here, where the high-influence fold has `epsilon=0` and all displayed identities reduce by the obvious limit.

## 5. What changed and what remains unpaid

### Proved in this run

1. **Exact character-fold residual transport**, (2.2): a balanced high-influence gate is reduced to two equal-bias children plus one explicit folded entropy debit.
2. **Output-conditioned entropy debit**, (3.8): the binary entropy term is `V_q h_2(epsilon/V_q)`, not the cruder `h_2(epsilon)`, because the common output atom is removed before Jensen.
3. **Dimension-free closure criterion**, (3.10), with the full rare-event logarithm retained.
4. **Exact character-gauged I-projection split**, (4.5), and the exact rare-reference normalization/logarithm (4.6)-(4.8).

These statements use one genuine Boolean source and its actual restrictions. No arbitrary unsigned law is substituted for Boolean realizability.

### Not proved

This report does **not** prove the current shaped candidate is universally gate-safe. To turn (3.10) into a full near-character safe collar for a concrete `Gamma`, one must prove a source-valid lower bound on `Gamma(q)` over the relevant `(q,epsilon)` corridor and retain the child defects. For the global conjecture, the remaining central/balanced region is still equivalent to FEI at the same constant, as BALANCED records.

The first unpaid implication for this slot is therefore:

> For a surviving concrete potential `Gamma`, prove that every balanced composition-prime gate outside a compact central influence region satisfies (3.10), using the exact candidate values `Gamma(q)` and child-defect/hierarchy slack; or construct a genuine Boolean counterexample to that corridor. Do not replace `V_q h_2(epsilon/V_q)` by `O(epsilon)`.

For the KL recipient, the corresponding next step is to use (4.5) to prove a quantitative lower payment from one of the two conditional branch divergences, while preserving the exact `epsilon log_2(1/delta)` reference-change term.

## 6. Partner and status

The assigned named partner fleet04/B06 had no compatible completed FEI result visible at the prepublication check; its newest completed work was still on the now-superseded BT4 programme. This is recorded as a partner-availability gap, not replaced by a fabricated PASS. The exact other-account result actually applied to the decisive inequality is FOLDED_JS from fleet01/B12; HIERARCHY from fleet04/B15 is also used to preserve exact KL/reference accounting.

**Full FEI status:** `OPEN_NOT_PROVED`.  
**Candidate universal all-gate status:** `OPEN / NOT ESTABLISHED`.  
**New theorem IDs:** `FEI-CHARACTER-FOLD-LEDGER-v1`, `FEI-CHARACTER-IPROJ-BRANCH-v1`.  
**New conditional criterion:** `FEI-NEAR-CHARACTER-CLOSURE-v1`.
