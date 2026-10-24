# account04/B15 — hierarchical Gibbs-KL composition and the indispensable activity credit

**Run:** `20260922T071345Z-b15-interfaceD-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_DECOMPOSABLE_TRANSFER / ACTIVITY-KL_CREDIT`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Live target and newest account02/B15 input

The controlling owner revision at run start was `2026-09-22.2`.  The later OWNER MESSAGE supersedes stale route-opening instructions and converges the FEI fleet on the all-gate inequality.  This report therefore does not open a new global route.  It resolves one source-exact transfer issue inside that target.

The newest completed account02/B15 report consumed is

`proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0704Z-gibbs-kl-prime-tube/REPORT.md`.

For a nonconstant Boolean gate/source `f` at product input bias, let

\[
w(S)=\widehat f(S)^2,
\qquad q=\Pr[f=-1],
\qquad v=V_q=4q(1-q).
\]

For each physical input coordinate `i`, put

\[
A_i=\Gamma(p_i)+h_2(V_{p_i}),\qquad
a_i=A_i/V_{p_i},\qquad x_i=2^{-a_i},
\]

\[
Z=\prod_i(1+x_i),\qquad
\nu(S)=Z^{-1}\prod_{i\in S}x_i.
\]

Writing `w^+` and `nu^+` for conditioning on `S != empty`, and

\[
x_q=2^{-[\Gamma(q)+h_2(v)]/v},
\]

account02/B15 proves the exact identity

\[
\boxed{
D_\Gamma(f)
=v\left[
D_{\rm KL,2}(w^+\|\nu^+)
-\log_2{Z-1\over x_q}
\right].
}
\tag{0.1}
\]

Thus the actual unpaid source remainder is

\[
\boxed{
R_\Gamma(f)
:=\log_2{Z-1\over x_q}
-D_{\rm KL,2}(w^+\|\nu^+),
\qquad D_\Gamma(f)=-vR_\Gamma(f).
}
\tag{0.2}
\]

The all-gate inequality is exactly `R_Gamma<=0`.  The relative-entropy term in (0.2) is retained with its sign; no packet integrality, positive-part replacement, or credit-free interpolation is used below.

The same account02 report makes the qualitative five-input prime neighborhood explicit: for the current candidate `Gamma^dagger`, every essential composition-prime five-input gate is certified on `max_i |p_i-1/2| <= 4.4e-6`.  Full FEI remains open outside the certified region.

## 1. Exact hierarchical spectral law for a disjoint composition

Let

\[
F=G(f_1,\ldots,f_m)
\]

where the Boolean `f_i` live on disjoint physical coordinate blocks and have output probabilities `q_i`, variances

\[
v_i=V_{q_i}>0.
\]

Let `w_G(T)` be the biased squared Fourier law of the outer gate `G` at bias vector `(q_1,...,q_m)`.  Let `w_i^+` be the nonempty spectral law of child `f_i`.

The biased composition formula gives the following *probability-law identity*, not an inequality:

\[
\boxed{
P_F\bigl(T,(S_i)_{i\in T}\bigr)
=w_G(T)\prod_{i\in T}w_i^+(S_i).
}
\tag{1.1}
\]

Here `T` records exactly which child blocks are spectrally active and each active `S_i` is nonempty.

Now form the account02 Gibbs law separately on each physical child block.  Write

\[
Z_i=\prod_{j\in\text{block }i}(1+x_j),
\qquad
r_i={Z_i-1\over Z_i},
\]

and let `nu_i^+` be its nonempty conditional law.  Since the physical Gibbs law itself is a product over all original coordinates, its induced law on the block-activity set `T` is

\[
\boxed{
\eta(T)={1\over\prod_i Z_i}\prod_{i\in T}(Z_i-1).
}
\tag{1.2}
\]

Conditionally on `T`, its active blocks are independent with laws `nu_i^+`.  Therefore the KL chain rule gives the exact first conservation law

\[
\boxed{
D_{\rm KL,2}(w_F\|\nu_F)
=D_{\rm KL,2}(w_G\|\eta)
+\sum_i\beta_iD_{\rm KL,2}(w_i^+\|\nu_i^+),
}
\tag{1.3}
\]

where

\[
\beta_i=\Pr_{w_G}(i\in T)=\operatorname{It}_i(G;q_1,\ldots,q_m).
\tag{1.4}
\]

Every negative information credit survives.  No source coordinate has been relaxed or averaged away.

## 2. The activity reference is an exact exponential tilt of the canonical outer Gibbs law

The canonical account02 Gibbs law for the outer gate uses

\[
y_i:=2^{-[\Gamma(q_i)+h_2(v_i)]/v_i}
\]

and

\[
\nu_G^{\rm can}(T)=Z_G^{-1}\prod_{i\in T}y_i,
\qquad
Z_G=\prod_i(1+y_i).
\]

Define each child's exact partition demand

\[
L_i:=\log_2{Z_i-1\over y_i}.
\tag{2.1}
\]

Because `Z_i-1=y_i 2^{L_i}`, the induced physical activity law (1.2) is an exponential tilt of the canonical outer reference.  Direct substitution yields

\[
\boxed{
D(w_G\|\eta)
=D(w_G\|\nu_G^{\rm can})
+\log_2\prod_iZ_i-\log_2Z_G
-\sum_i\beta_iL_i.
}
\tag{2.2}
\]

Combining (1.3), (2.2), and (0.1), and using

\[
D_\Gamma(f_i)=v_i\bigl[K_i-L_i\bigr],
\qquad K_i=D(w_i^+\|\nu_i^+),
\]

gives

\[
\boxed{
D_\Gamma(F)
=D_\Gamma(G;q_1,\ldots,q_m)
+\sum_i{\beta_i\over v_i}D_\Gamma(f_i).
}
\tag{2.3}
\]

Equation (2.3) was already known project-locally from the algebraic composition calculation.  The new point here is the **source-exact KL ledger** behind it: the child conditional relative entropies enter with their physical outer activity weights, and the only reference mismatch is the exact tilt `L_i`, which cancels the child partition demand rather than being thrown away.

Consequently, every disjoint decomposable gate is closed once its outer gate and children are closed.  The Interface-D debt is therefore genuinely concentrated on composition-prime gates; there is no hidden arithmetic remainder created by the decomposition step.

## 3. Tensor/product specialization: the missing cross-block activity KL

A particularly sharp specialization is multiplication of Boolean signs on disjoint blocks,

\[
F=\prod_{j=1}^m f_j.
\]

This is XOR of the output bits.  In this case the actual and Gibbs spectral laws both tensorize before conditioning on nonemptiness.

Put

\[
r_j={Z_j-1\over Z_j},
\qquad
v_F=1-\prod_j(1-v_j),
\qquad
r_F=1-\prod_j(1-r_j).
\]

Conditioned on the parent spectrum being nonempty, let `A=(A_1,...,A_m) != 0` record which blocks are nonempty.  Its source law is product Bernoulli `(v_j)` conditioned on `A!=0`, while its reference law is product Bernoulli `(r_j)` conditioned on `A!=0`.  Call these laws `P_A,Q_A`.

If

\[
K_j=D(w_j^+\|\nu_j^+),
\qquad
K_F=D(w_F^+\|\nu_F^+),
\]

then the conditional KL chain rule is

\[
\boxed{
v_FK_F
=\sum_jv_jK_j
+v_FD_{\rm KL,2}(P_A\|Q_A).
}
\tag{3.1}
\]

Thus conditioning on `S!=empty` creates an additional **block-activity KL credit**.  It is nonnegative and generally nonzero; simply adding child conditional KLs is not an exact tensor rule.

Let

\[
L_F=\log_2{Z_F-1\over x_{q_F}},
\qquad Z_F=\prod_jZ_j,
\]

where `q_F` is the XOR convolution of the child output probabilities.  Substituting (3.1) into (0.2), or equivalently tensorizing the unconditioned Gibbs KL, gives the exact activity-credit conservation law

\[
\boxed{
v_FD(P_A\|Q_A)+\sum_jv_jL_j-v_FL_F
=\sum_j\Gamma(q_j)-\Gamma(q_F).
}
\tag{3.2}
\]

Equivalently, the actual unpaid Gibbs remainder transfers as

\[
\boxed{
v_FR_\Gamma(F)
=\sum_jv_jR_\Gamma(f_j)
-\left[\sum_j\Gamma(q_j)-\Gamma(q_F)\right].
}
\tag{3.3}
\]

This is the weakest exact Interface-D transfer on Boolean tensor products: no KL term has been discarded.  If `Gamma` is subadditive under XOR convolution, the bracket is nonnegative, so tensoring cannot create a new positive remainder once the children are safe.

## 4. Balanced tensor powers show the activity KL is indispensable

If every child is balanced, then `v_j=v_F=1` and every source block is active.  For identical children with partition function `Z`,

\[
\boxed{
K_{f^{\otimes m}}
=mK_f+\log_2{Z^m-1\over(Z-1)^m}.
}
\tag{4.1}
\]

The second term is exactly the KL of the deterministic all-active source state against the conditioned Gibbs activity law.  For fixed `Z>1`,

\[
\log_2{Z^m-1\over(Z-1)^m}
=m\log_2{Z\over Z-1}+\log_2(1-Z^{-m}),
\tag{4.2}
\]

so the cross-block credit is linear in `m`.  A credit-free tensor interpolation that replaces `K_parent` by `sum K_child` can therefore lose `Theta(m)` genuine relative entropy on actual Boolean tensor powers.

Writing `C=Gamma(1/2)`, (3.3) becomes

\[
\boxed{
R_\Gamma(f^{\otimes m})
=mR_\Gamma(f)-(m-1)C.
}
\tag{4.3}
\]

The activity KL and the partition demands cancel *exactly* to produce the `(m-1)C` XOR-potential credit.  This is the source-level reason that the tensor/product step carries no hidden FEI debt.

## 5. Independent Boolean check

`check_gibbs_activity_tensor.py` reconstructs the actual two-bit Boolean seed `f(00)=-1`, `f=+1` elsewhere, its disjoint tensor square, and the Gibbs laws directly from the Walsh transform.  With the harmless test potential `Gamma(p)=1.7 V_p`, it verifies both versions of account02's Gibbs identity, the three-state activity chain rule, (3.2), and the defect composition law.

The captured output is

```
PASS
seed_q 0.25 seed_v 0.75
parent_q 0.375 parent_v 0.9375
activity_KL_bits 0.363598638780905
activity_ledger_bits 0.956249999999999
gamma_XOR_slack_bits 0.956250000000000
max_abs_identity_error 4.441e-16
```

The checker is only a falsification/self-consistency test; the proof is the KL chain rule above.

## 6. Consequence and next source-exact obligation

This closes the arithmetic/Shannon transfer **for every disjoint decomposable source** in a form that preserves all current Gibbs/relative-entropy credits.  It also rules out one recurring shortcut: conditional KL is not additive under tensor products; the omitted block-activity credit can be extensive.

What remains is exactly what the owner target says should remain: composition-prime outer gates.  The newest account02/B15 theorem already certifies essential five-input primes in the explicit `4.4e-6` central tube for the current candidate.  The next useful Interface-D calculation is therefore not another tensor or packet-integrality estimate.  It is to attack the prime outer activity law `w_G` against the induced activity reference `eta` in (1.3), while retaining the canonical-outer Gibbs KL and the tilt terms in (2.2).  Any proposed scalar compression should first be tested against the extensive activity credit (4.2).

No novelty or publication-priority claim is made for the KL-chain interpretation without a dedicated literature review.
