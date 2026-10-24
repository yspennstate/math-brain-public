# account01/B15 — exact restriction I-projection chain rule

**Run:** `b15-20260922T103236Z-restriction-iprojection-chain`  
**Classification:** `ESSENTIAL_STEP_APPLIED`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Exact target and source state

The active all-team assignment for account01/B15 asks for the exact transfer of the irreducible occurrence-marginal KL credit under a **physical coordinate restriction**, including movement of the occurrence marginals. The target is independent of which current candidate potential is ultimately used.

The exact predecessor used here is account02/B15's influence I-projection theorem:

- repository `yspennstate/math-open-problems`, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, path `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

For a nonempty spectral law `P` with occurrence marginals `r_i=P(i in S)`, it constructs the unique maximum-entropy conditional-product law `Q_r` and proves

\[
K_{\rm occ}(P)=D_{\rm KL,2}(P\Vert Q_r)=H_{\max}(r)-H(P).
\tag{0.1}
\]

The named compatible partner result consumed is account02/B15's suspension no-loss theorem and its same-run correction:

- report/addendum repository `yspennstate/math-open-problems`, commit `b5bf5c990f3597cf26c2aa0ab1eabea4ae9ea277`, path `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T085941Z-suspension-kl-no-loss/`.

It proves on genuine Boolean suspensions that for every finite center `C`, every finite `L`, and every fixed `theta<1`, replacing `K_occ` by `theta K_occ` and compensating by `L J` eventually fails. Thus a restriction recursion must preserve the dependence KL with coefficient one, up to additive source-scale debits; a fixed multiplicative loss is not admissible.

Two further source-exact inputs are used:

1. account03/B15, commit `8793c7e49e1de7921bc76c7724c92fae03024e26`, path `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T082654Z-js-packet-payment/REPORT.md`, which proves for a genuine physical restriction at selector bias `s`
\[
\operatorname{JS}_s(U,V)\le \kappa(s)\operatorname{It}_j,
\qquad
\kappa(s)=\frac{\ln((1-s)/s)}{(1-2s)\ln2},
\tag{0.2}
\]
with the continuous value `kappa(1/2)=2/ln 2`;
2. account04/B15, commit `2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, path `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`, which proves the corresponding exact KL hierarchy under **disjoint composition**. The restriction weights below are derived afresh; no composition weight is substituted for a restriction weight.

The current state also records the recursive-majority obstruction to fixed/low-depth labelled KL projections (account03/B18, commit `bff0d7b6c21485f386841c42582eb04f32705046`). The theorem below retains the full KL at every restriction depth, so it does not make that refuted compression.

## 1. Full-law lift of the occurrence I-projection

Let `W` be a probability law on all subsets of `[d]`. Put

\[
v:=1-W(\varnothing),\qquad
\rho_i:=W(i\in S).
\tag{1.1}
\]

If `v>0`, set `r_i=\rho_i/v` and let `Q_r` be the nonempty conditional-product I-projection from (0.1). Define

\[
\boxed{
\mathsf M(v,\rho)
:=(1-v)\delta_{\varnothing}+vQ_{\rho/v}.
}
\tag{1.2}
\]

This is the unique maximum-entropy law on all subsets with the prescribed empty mass and prescribed coordinate occurrences. Define the **weighted irreducible dependence credit**

\[
\boxed{
\mathcal K(W):=D_{\rm KL,2}(W\Vert \mathsf M(v,\rho))
=vK_{\rm occ}(W^+).
}
\tag{1.3}
\]

The corresponding maximum entropy is

\[
\boxed{
\mathscr H(v,\rho)
=h_2(v)+vH_{\max}(\rho/v).
}
\tag{1.4}
\]

Indeed, conditioning on the empty/nonempty indicator first gives `h_2(v)` and then the account02/B15 maximum-entropy problem on the nonempty branch.

This weighted normalization is the natural one for the all-gate defect, because the project residual satisfies `D_Gamma=v(B_inf^Gamma+K_occ)`.

## 2. Genuine physical restriction notation

Fix an actual Boolean gate/function `G`, an actual input coordinate `j`, and an interior product bias

\[
s=p_j\in(0,1).
\]

Let `G_0,G_1` be the genuine restrictions `x_j=0,1`. On the remaining physical coordinates write their actual biased Fourier coefficients as

\[
u_T=\widehat {G_0}(T),\qquad v_T=\widehat {G_1}(T).
\]

Let the two full child spectral laws be

\[
U_T=u_T^2,\qquad V_T=v_T^2.
\]

The normalized biased Fourier transform in the selector coordinate gives the exact parent pair

\[
\widehat G(T)=(1-s)u_T+sv_T,
\qquad
\widehat G(T\cup\{j\})=\sqrt{s(1-s)}(v_T-u_T).
\tag{2.1}
\]

By orthogonality, the parent law after erasing the selector label is exactly

\[
\boxed{
E_T:=W(T)+W(T\cup\{j\})=(1-s)U_T+sV_T.
}
\tag{2.2}
\]

Thus this is a genuine physical mixture, not an abstract interpolation.

For child `b=0,1`, let

\[
v_b=1-P_b(\varnothing),\qquad
\rho_i^b=P_b(i\in S),\qquad
R_b=\mathsf M(v_b,\rho^b).
\tag{2.3}
\]

The erased source has

\[
\bar v=(1-s)v_0+sv_1,
\qquad
\bar\rho=(1-s)\rho^0+s\rho^1,
\tag{2.4}
\]

and let

\[
\bar R:=\mathsf M(\bar v,\bar\rho).
\tag{2.5}
\]

For the parent, put `R=mathsf M(v,rho)` and erase coordinate `j` from this reference:

\[
R^-:=\pi_{j\#}R.
\tag{2.6}
\]

This erasure remains in the same full conditional-product exponential family. Concretely, if the parent nonempty I-projection is generated by independent Bernoulli probabilities

\[
t_i=c\rho_i/v
\]
conditioned on nonemptiness, set

\[
c^-=1-\prod_{i\ne j}(1-t_i),
\qquad
v^-=v\,c^-/c.
\tag{2.7}
\]

Then

\[
\boxed{R^-=\mathsf M(v^-,\rho_{-j}).}
\tag{2.8}
\]

For every erased packet with `E_T>0`, define the actual parent selector posterior

\[
q_T={W(T\cup\{j\})\over E_T}
={s(1-s)(u_T-v_T)^2\over E_T},
\tag{2.9}
\]

and the corresponding reference posterior

\[
\theta_T={R(T\cup\{j\})\over R^-(T)}.
\tag{2.10}
\]

For `T nonempty`, `theta_T=t_j`. At the exceptional erased-empty packet,

\[
\theta_\varnothing
=
\frac{(v/c)t_j\prod_{i\ne j}(1-t_i)}
{1-v+(v/c)t_j\prod_{i\ne j}(1-t_i)}.
\tag{2.11}
\]

The special value (2.11) is required because the true empty spectral atom is not generated by the conditioned product component.

## 3. Main theorem: exact restriction I-projection chain rule

Define four terms, all in bits:

\[
C_{\rm marg}
:=(1-s)D(R_0\Vert\bar R)+sD(R_1\Vert\bar R),
\tag{3.1}
\]

\[
C_{\rm erase}:=D(\bar R\Vert R^-),
\tag{3.2}
\]

\[
C_{\rm pair}:=\sum_T E_T d_2(q_T\Vert\theta_T),
\tag{3.3}
\]

and

\[
\operatorname{JS}_s(U,V)
:=(1-s)D(U\Vert E)+sD(V\Vert E).
\tag{3.4}
\]

### Theorem 3.1 — exact physical-restriction transfer

For every nondegenerate physical restriction above,

\[
\boxed{
\mathcal K(W)
=(1-s)\mathcal K(U)+s\mathcal K(V)
+C_{\rm marg}+C_{\rm erase}+C_{\rm pair}
-\operatorname{JS}_s(U,V).
}
\tag{3.5}
\]

Equivalently,

\[
\boxed{
 vK_{\rm occ}(G)
=(1-s)v_0K_{\rm occ}(G_0)+sv_1K_{\rm occ}(G_1)
+C_{\rm marg}+C_{\rm erase}+C_{\rm pair}
-\operatorname{JS}_s(U,V).
}
\tag{3.6}
\]

All three `C` terms are nonnegative. Constant-child and boundary cases follow by contracting deterministic coordinates or by the corresponding finite-alphabet limit; no division by a zero nonempty mass is needed in that formulation.

### Proof

**Step 1: parent versus erased parent reference.** Apply the KL chain rule to the deterministic erasure map `pi_j` and then to the selector indicator inside each erased packet. The source marginal is `E` and the reference marginal is `R^-`, hence

\[
\boxed{
\mathcal K(W)=D(E\Vert R^-)+C_{\rm pair}.
}
\tag{3.7}
\]

No sign or packet information is discarded.

**Step 2: move the occurrence constraints.** The law `bar R` is the I-projection/max-entropy reference with the exact source constraints `(bar v,bar rho)`. The erased parent reference `R^-` is another member of the same finite exponential family. Therefore `log(bar R/R^-)` is affine in the sufficient statistics

\[
1_{S\ne\varnothing},\qquad 1_{i\in S}\ (i\ne j).
\]

The source `E` and `bar R` have identical expectations of these statistics. The Pythagorean identity is therefore exact:

\[
\boxed{
D(E\Vert R^-)=D(E\Vert\bar R)+C_{\rm erase}.
}
\tag{3.8}
\]

**Step 3: split the child mixture without losing its entropy credit.** The standard mixture identity gives

\[
(1-s)D(U\Vert\bar R)+sD(V\Vert\bar R)
=D(E\Vert\bar R)+\operatorname{JS}_s(U,V).
\tag{3.9}
\]

For each child, `R_b` is its own I-projection and `bar R` belongs to the same reference family. A second Pythagorean identity gives

\[
D(U\Vert\bar R)=\mathcal K(U)+D(R_0\Vert\bar R),
\tag{3.10}
\]

\[
D(V\Vert\bar R)=\mathcal K(V)+D(R_1\Vert\bar R).
\tag{3.11}
\]

Substitute (3.10)-(3.11) into (3.9), solve for `D(E||bar R)`, and then substitute into (3.8) and (3.7). This is exactly (3.5). QED.

## 4. The exact occurrence-marginal movement refund

The term that was absent from a naive restriction ledger has a closed entropy form. Since the weighted child references have pooled sufficient statistics `(bar v,bar rho)`, their cross-entropy against `bar R` averages to `H(bar R)`. Hence

\[
\boxed{
C_{\rm marg}
=
\mathscr H(\bar v,\bar\rho)
-(1-s)\mathscr H(v_0,\rho^0)
-s\mathscr H(v_1,\rho^1)
\ge0.
}
\tag{4.1}
\]

Thus movement of the occurrence marginals is not an uncontrolled error. It produces an explicit nonnegative information credit.

The only negative term in (3.5) is the **actual child-mixture entropy**

\[
-\operatorname{JS}_s(U,V).
\tag{4.2}
\]

This sign is essential. Dropping it gives a false monotonicity statement; Section 6 supplies a genuine Boolean counterexample.

## 5. Quantitative payment consequence with coefficient one on child KL

Because `C_marg,C_erase,C_pair>=0`, Theorem 3.1 immediately yields

\[
\mathcal K(W)
\ge
(1-s)\mathcal K(U)+s\mathcal K(V)-\operatorname{JS}_s(U,V).
\tag{5.1}
\]

Apply account03/B15's source-exact sharp physical restriction estimate (0.2):

\[
\boxed{
 vK_{\rm occ}(G)
\ge
(1-s)v_0K_{\rm occ}(G_0)+sv_1K_{\rm occ}(G_1)
-\kappa(s)\operatorname{It}_j(G;p).
}
\tag{5.2}
\]

Equivalently,

\[
\boxed{
(1-s)v_0K_0+sv_1K_1
\le vK+\kappa(s)\operatorname{It}_j.
}
\tag{5.3}
\]

This is the requested new sign/payment consequence. The child dependence KL is retained with **coefficient exactly one**. This matters because the consumed account02/B15 sparse-suspension theorem proves that any fixed multiplicative coefficient below one is eventually fatal, even after adding an arbitrary dimension-independent `O(J)` bank.

Moreover

\[
\kappa(s)\sim \log_2(1/s)\qquad(s\downarrow0),
\tag{5.4}
\]

so the only debit produced by this restriction step has the correct rare-event logarithmic scale rather than hiding it inside a false uniform constant.

## 6. Genuine four-bit Boolean counterexample to naive KL monotonicity

The negative term (4.2) is not optional. Consider the uniform four-bit Boolean function in little-endian truth-table order

\[
(1,1,1,-1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1).
\tag{6.1}
\]

Restrict physical coordinate `j=0` at `s=1/2`. Its raw Walsh vector is

\[
(4,4,4,-4,-4,4,4,4,4,4,4,-4,4,-4,-4,-4).
\tag{6.2}
\]

Therefore the parent squared spectrum is exactly uniform on all sixteen subsets. It is already its full I-projection reference, so

\[
\boxed{\mathcal K(W)=0.}
\tag{6.3}
\]

The two child raw Walsh vectors are

\[
(4,0,0,4,4,0,0,-4),
\qquad
(0,4,-4,0,0,4,4,0).
\tag{6.4}
\]

Their squared spectra are each uniform on four atoms and have disjoint supports. Hence

\[
\boxed{\operatorname{JS}_{1/2}(U,V)=1\text{ bit}.}
\tag{6.5}
\]

The exact numerical I-projection values, reproduced by `CHECKER.py`, are

\[
{\mathcal K(U)+\mathcal K(V)\over2}
=0.7831101582604267\ldots,
\tag{6.6}
\]

\[
C_{\rm marg}=0.2168898417395733\ldots,
\qquad
C_{\rm erase}=C_{\rm pair}=0.
\tag{6.7}
\]

Thus the full right side of (3.5) is

\[
0.7831101582604267
+0.2168898417395733
-1
=0,
\]
matching (6.3) exactly.

In particular, the tempting stronger claim

\[
\mathcal K(W)\ge(1-s)\mathcal K(U)+s\mathcal K(V)
\tag{6.8}
\]

is **false even for a genuine four-bit Boolean source**. Here the negative entropy term contributes exactly `-1` bit and cancels the positive child dependence plus the occurrence-movement refund. This is a concrete elimination, not evidence that FEI itself fails.

The same checker gives

\[
\operatorname{It}_j=1/2,
\qquad
\kappa(1/2)\operatorname{It}_j=1/\ln2
=1.442695040888963\ldots,
\]
so the proved lower bound (5.2) is respected.

## 7. Recursive-majority / multiscale preflight

The current correction state refutes retaining only individually labelled spectral atoms below a fixed depth, or below `d_m <= (1/2-epsilon)m`, and merging the rest into one tail on recursive ternary majority. The present theorem does not perform that operation.

Iterate (3.5) down any genuine physical restriction tree. If `pi_u` is the probability of reaching node `u`, then exactly

\[
\boxed{
\mathcal K_{\rm root}
=\mathbb E\,\mathcal K_{\rm leaves}
+\sum_u\pi_u
\bigl(C_{{\rm marg},u}+C_{{\rm erase},u}+C_{{\rm pair},u}
-\operatorname{JS}_u\bigr).
}
\tag{7.1}
\]

On a full tree to constants, the leaf term vanishes and **all dependence KL is represented by the multiscale node ledger**. No fixed-depth projection and no merged high-level tail has been introduced. Therefore the recursive-majority low-level-projection counterexample does not refute (7.1); instead it shows why the full multiscale ledger cannot be truncated without an additional theorem.

This is a preflight compatibility statement, not a proof of FEI.

## 8. Exact old/new missing implications

**Old missing implication, now proved:** derive a source-exact physical-restriction transfer for `K_occ` while retaining the movement of the occurrence marginals and every mismatch term.

The exact answer is (3.5)/(3.6). It has three nonnegative mismatch credits and one indispensable negative Jensen-Shannon term. The occurrence movement itself is paid by the explicit nonnegative entropy gap (4.1).

**Refuted stronger shortcut:** unconditioned monotonicity of weighted `K_occ` under restriction, equation (6.8). The four-bit Boolean function (6.1) refutes it exactly.

**New first unpaid implication toward full FEI:** combine the exact multiscale signed ledger (7.1) with the all-gate Bellman/influence term so that the accumulated negative `JS` payments are charged by actual physical selector prices/branch credits without losing a fixed fraction of `K_occ` and without truncating the high-cardinality dependence. Equivalently, one now needs a source-exact inequality on the **joint** node quantity

\[
C_{\rm marg}+C_{\rm erase}+C_{\rm pair}-\operatorname{JS}
+\text{(the corresponding Bellman/influence increment)}
\tag{8.1}
\]

that telescopes on every physical restriction tree, or a genuine Boolean family showing that such a proposed joint inequality is false.

The account02/B15 sparse-suspension theorem requires any successful version of (8.1) to preserve `K_occ` to additive influence scale; the recursive-majority correction requires it to remain genuinely multiscale. Neither condition is bypassed here.

## 9. Status

Primary classification: **`ESSENTIAL_STEP_APPLIED`**.

- Exact restriction I-projection chain rule: proved in this report.
- Exact occurrence-marginal movement refund: proved in this report.
- Coefficient-one restriction descent with sharp physical `kappa(s) It_j` debit: proved using the cited account03/B15 theorem.
- Naive restriction monotonicity: refuted by a genuine four-bit Boolean function.
- Full uniform-cube FEI: **OPEN / NOT PROVED**.
