# account03/B14 — exact selector-occurrence split of the canonical occurrence KL

**Run:** `account03-B14-20260922T103926Z-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_KL_SELECTOR_SPLIT / FULL_FEI_OPEN / WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Current target and sources

The current owner assignment is the all-team FEI programme `FEI-ALL-TEAM-20260922T095941Z`, control revision `2026-09-22.3`. The account03/B14 target is to relate a physical selector disagreement to a logarithmic part of the canonical occurrence KL, using the actual signed packet source and retaining reference-law mismatch rather than setting it to zero.

This report uses the following exact sources.

1. **IPROJ:** `yspennstate/math-open-problems@4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`. It proves
   \[
   K_{\rm occ}=D_2(P\|Q_r)=H_{\max}(r)-H(P),
   \qquad
   R_\Gamma=B_{\rm inf}^\Gamma+K_{\rm occ},
   \]
   where `P=w^+` is the nonempty biased spectral law and `Q_r` is the maximum-entropy conditional-product law matching all coordinate occurrence marginals.
2. **SELECTOR_DEBIT:** `yspennstate/math-open-problems@4ccd51ad517f425a529daa52c3352905b86ea69d`, `proofnet24/P03-fei/fleet-2026-09-21/account02/B12/20260922T091546Z-uniform-selector-debit-and-safe-lift/REPORT.md`. For a physical selector coordinate `i` of bias `s`, restrictions with biased Fourier coefficients `u_T,v_T` give
   \[
   e_T=(1-s)u_T^2+s v_T^2,
   \qquad
   q_T={s(1-s)(u_T-v_T)^2\over e_T},
   \]
   \[
   p_i:=\operatorname{It}_i=\sum_T e_Tq_T=V_s d,
   \qquad V_s=4s(1-s),
   \]
   with `d=Pr[G_0\ne G_1]`.
3. **HIERARCHY:** `yspennstate/math-open-problems@2bf247373576eb406ca91bb3ea5f3ce5e5ab8588`, `proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T091017Z-iprojection-composition-transfer/REPORT.md`. It proves the exact nonnegative hierarchy KL under disjoint composition and, in particular, that binary gates can have local `K_occ=0`; therefore no positive lower bound depending only on physical disagreement can be universally valid.
4. **Named peer result consumed:** `yspennstate/math-open-problems@730731281a24e70b01b4021a90ff758575414db1`, `proofnet24/P03-fei/fleet-2026-09-22/account04/B14/20260922T101201Z-information-priced-crossing/REPORT.md`. Its Theorem 1.1 proves that for a Bernoulli variable of mean `p<=1/2` with posterior `U` after observing a physical block and crossing functional `c=E(2U-1)_+`,
   \[
   I\ge h_2(p)-h_2(p-c),
   \]
   and if `c>=gamma p`,
   \[
   I\ge \gamma p\log_2{1-p\over p}.
   \]
   Below this theorem is applied to the selector-occurrence Bernoulli variable in the actual spectral packet source, not merely quoted.

The former quadratic `0.337/0.34` candidates and old AND-extremality route are not used.

## 1. Actual selector packet source

Fix a nonconstant Boolean gate `G` at an interior product bias vector and a physical selector coordinate `i` of input bias `s`. Let `\widehat G(S)` denote the biased Fourier coefficients of the parent. Put
\[
 v:=\sum_{S\ne\varnothing}\widehat G(S)^2=V_q,
 \qquad
 p:=\sum_{S\ni i}\widehat G(S)^2=\operatorname{It}_i=V_s d.
\tag{1.1}
\]
Let
\[
 b:=\widehat G(\{i\})^2=e_\varnothing q_\varnothing,
 \qquad
 M:=v-b.
\tag{1.2}
\]
The packet formulas in SELECTOR_DEBIT imply that for every residual packet `T`, the unconditioned parent spectral law on the pair
\[
(T,B),\qquad B={\bf 1}_{\{i\in S\}},\qquad T=S\setminus\{i\},
\]
has masses
\[
\Pr_{\rm spec}(T,B=1)=e_Tq_T,
\qquad
\Pr_{\rm spec}(T,B=0)=e_T(1-q_T).
\tag{1.3}
\]
The unique excluded state when conditioning to the nonempty law `P=w^+` is `(T=emptyset,B=0)`. Therefore under `P`,
\[
P(T=\varnothing)=\frac b v,
\tag{1.4}
\]
and on the event `R={T\ne\varnothing}`,
\[
P(T\mid R)=\frac{e_T}{M},
\qquad
P(B=1\mid T,R)=q_T,
\tag{1.5}
\]
with mean occupation
\[
\rho:=P(B=1\mid R)=\frac{p-b}{v-b}=\frac{p-b}{M}.
\tag{1.6}
\]
Thus the physical disagreement enters the canonical occurrence source exactly through `p=V_s d`, while `b` records the singleton selector mass that must not be silently merged with the non-singleton packets.

## 2. Exact reference law after deleting the selector label

Let `r_j=P(j\in S)` and let `zeta` be the IPROJ parameter, so for `sum_j r_j>1`,
\[
1-\zeta=\prod_j(1-\zeta r_j),
\tag{2.1}
\]
and `Q_r` is obtained from independent Bernoulli coordinates of probabilities `zeta r_j` conditioned on nonemptiness. (The `sum r_j=1` singleton case follows by the evident limit and has `K_occ=0`.) Define
\[
\theta:=\zeta r_i=\zeta\frac pv.
\tag{2.2}
\]
Under `Q_r`, the probability that the selector is the **only** occupied coordinate is
\[
\boxed{
\sigma:=Q_r(S=\{i\})
=\frac{r_i(1-\zeta)}{1-\zeta r_i}.
}
\tag{2.3}
\]
Indeed the unconditioned singleton probability is
`theta prod_{j ne i}(1-zeta r_j)`, and
`prod_j(1-zeta r_j)=1-zeta`.

Conditioned on `R={T ne emptyset}`, the nonempty-conditioning event is already satisfied by the residual coordinates, so under `Q_r`

* `T` has the conditional-product law `Q_{-i}^{+,zeta}` generated by probabilities `zeta r_j`, `j ne i`, conditioned on `T ne emptyset`;
* independently of `T`, `B` is Bernoulli with parameter `theta`.

This is the reference-law mismatch that cannot be declared zero merely because `Q_r` matches the **unconditional** occurrence marginal `r_i`.

## 3. Main theorem: four-term selector decomposition of `K_occ`

Let
\[
P_T^*(T):=\frac{e_T}{M},\qquad T\ne\varnothing,
\tag{3.1}
\]
and let `Q_T^*=Q_{-i}^{+,zeta}` be the residual reference above. Define
\[
B_i^*:=\sum_{T\ne\varnothing} e_T h_2(q_T).
\tag{3.2}
\]

### Theorem 3.1 — exact selector-occurrence KL split

For every nonconstant Boolean gate and every interior physical selector coordinate with `M>0`,
\[
\boxed{
\begin{aligned}
vK_{\rm occ}
={}&v\,D_2\!\left(\operatorname{Ber}(b/v)\middle\|\operatorname{Ber}(\sigma)\right)\\
&+M\,D_2(P_T^*\|Q_T^*)\\
&+M\,D_2\!\left(\operatorname{Ber}(\rho)\middle\|\operatorname{Ber}(\theta)\right)\\
&+M\,I_P(B;T\mid R).
\end{aligned}}
\tag{3.3}
\]
Equivalently,
\[
\boxed{
\begin{aligned}
vK_{\rm occ}
={}&v\,D_2\!\left(\operatorname{Ber}(b/v)\middle\|\operatorname{Ber}(\sigma)\right)
+M\,D_2(P_T^*\|Q_T^*)\\
&+M\,D_2\!\left(\operatorname{Ber}(\rho)\middle\|\operatorname{Ber}(\theta)\right)
+M h_2(\rho)-B_i^*.
\end{aligned}}
\tag{3.4}
\]
Every displayed term in (3.3) is nonnegative.

### Proof

The map `S -> (R,T,B)` is lossless on nonempty spectral sets. Under `P`, conditional on `R=0` the state is deterministically the singleton `{i}`; the same is true under `Q_r`. The KL chain rule therefore gives
\[
K_{\rm occ}
=D_2(\operatorname{Ber}(b/v)\|\operatorname{Ber}(\sigma))
+{M\over v}
D_2(P_{T,B\mid R}\|Q_{T,B\mid R}).
\tag{3.5}
\]
By Section 2,
\[
Q_{T,B\mid R}=Q_T^*\otimes\operatorname{Ber}(\theta).
\]
A second chain rule yields
\[
D_2(P_{T,B\mid R}\|Q_T^*\otimes\operatorname{Ber}(\theta))
=D_2(P_T^*\|Q_T^*)
+\mathbb E_{P_T^*}D_2(\operatorname{Ber}(q_T)\|\operatorname{Ber}(\theta)).
\tag{3.6}
\]
For any posterior family with mean `rho`, the exact binary information identity is
\[
\mathbb E D_2(\operatorname{Ber}(q_T)\|\operatorname{Ber}(\theta))
=I(B;T\mid R)
+D_2(\operatorname{Ber}(\rho)\|\operatorname{Ber}(\theta)).
\tag{3.7}
\]
Finally
\[
M I(B;T\mid R)
=M h_2(\rho)-\sum_{T\ne\varnothing}e_T h_2(q_T)
=Mh_2(\rho)-B_i^*.
\tag{3.8}
\]
Substitution proves (3.3)-(3.4). QED.

The third term of (3.3) is the exact **mean-occurrence reference mismatch**. It is generally not zero: the canonical product reference uses the pre-conditioning Bernoulli parameter `theta=zeta r_i`, whereas the actual non-singleton packet source has mean `rho=(p-b)/(v-b)`. The first and second terms are additional singleton and residual-shape mismatches. Dropping any of them is an unjustified loss of KL credit.

## 4. Named peer theorem applied: logarithmic fractional-crossing payment

Assume `rho<=1/2` and define the **spectral selector crossing**
\[
 c_{\rm occ}:=
 \mathbb E_{T\sim P_T^*}(2q_T-1)_+.
\tag{4.1}
\]
Apply account04/B14's information-priced crossing theorem to the Bernoulli occupation variable `B` observed through the actual residual packet `T`. This is a direct application with posterior `U=q_T`, not an analogy. It gives
\[
I(B;T\mid R)
\ge h_2(\rho)-h_2(\rho-c_{\rm occ}).
\tag{4.2}
\]
Therefore (3.3) implies
\[
\boxed{
\begin{aligned}
vK_{\rm occ}\ge{}&
 vD_2(\operatorname{Ber}(b/v)\|\operatorname{Ber}(\sigma))\\
&+M D_2(\operatorname{Ber}(\rho)\|\operatorname{Ber}(\theta))\\
&+M\bigl[h_2(\rho)-h_2(\rho-c_{\rm occ})\bigr].
\end{aligned}}
\tag{4.3}
\]
where the omitted residual-shape KL `M D(P_T^*||Q_T^*)` is nonnegative and remains available.

If for some fixed `0<gamma<=1`
\[
 c_{\rm occ}\ge\gamma\rho,
\tag{4.4}
\]
then the same peer theorem yields the explicit rare-event logarithm
\[
\boxed{
 vK_{\rm occ}
\ge
\gamma(p-b)\log_2\frac{1-\rho}{\rho}
+vD_2(\operatorname{Ber}(b/v)\|\operatorname{Ber}(\sigma))
+M D_2(\operatorname{Ber}(\rho)\|\operatorname{Ber}(\theta)).
}
\tag{4.5}
\]
Thus whenever a fixed fraction of the non-singleton selector occurrence is produced by posterior crossing, the canonical occurrence KL contains the required logarithmic scale. Since `p=V_s d`, this is precisely a disagreement-to-occurrence-information bridge. It survives `d -> 0` whenever the non-singleton mass `p-b` remains a comparable fraction of `p` and `M` does not collapse at the same rate.

A second, assumption-free way to expose the same logarithmic component is the exact term
\[
\boxed{
L_i:=Mh_2\!\left({p-b\over M}\right)-B_i^*
=M I(B;T\mid R)\ge0.
}
\tag{4.6}
\]
For example, if a future source theorem proves `B_i^* <= C_0(p-b)`, then directly from `h_2(x)>=x log_2(1/x)` one gets
\[
L_i\ge(p-b)
\left[
\log_2{M\over p-b}-C_0
\right],
\tag{4.7}
\]
which has the exact rare-disagreement logarithm. No such universal linear bound on `B_i^*` is claimed here.

## 5. Decisive refutation: disagreement alone cannot lower-bound `K_occ`

A tempting but false strengthening would be
\[
K_{\rm occ}\ge F(d)>0
\qquad(0<d<1)
\tag{5.1}
\]
for all physical selector splits, or even `K_occ >= c d log(1/d)` with universal positive `c`.

This is **REFUTED** by any nonconstant binary Boolean gate such as `AND_2` at interior product bias. HIERARCHY proves that every binary gate has
\[
K_{\rm occ}=0,
\]
because a law on the three nonempty subsets of two coordinates is uniquely determined by its two occurrence marginals. But for a selector coordinate of biased `AND_2`, one restriction is constant while the other depends on the second input, so the physical disagreement probability lies strictly between `0` and `1` at every interior bias of the second input.

Hence the correct universal object cannot be a function of `d` alone. The selector must retain at least one of the genuinely source-sensitive quantities in (3.3): non-singleton posterior information, mean-reference mismatch, residual-shape mismatch, hierarchy credit after decomposition, or child/potential slack.

## 6. Exact insertion into the FEI ledger

IPROJ gives
\[
D_\Gamma=v\bigl(B_{\rm inf}^\Gamma+K_{\rm occ}\bigr).
\tag{6.1}
\]
Theorem 3.1 therefore yields the exact nonnegative decomposition
\[
\boxed{
\begin{aligned}
D_\Gamma
={}&vB_{\rm inf}^\Gamma
+vD_2(\operatorname{Ber}(b/v)\|\operatorname{Ber}(\sigma))\\
&+M D_2(P_T^*\|Q_T^*)
+M D_2(\operatorname{Ber}(\rho)\|\operatorname{Ber}(\theta))
+L_i.
\end{aligned}}
\tag{6.2}
\]
This is an exact gate-level insertion: no occurrence credit is reused and no product-reference mismatch is discarded. In a restriction recursion the term `L_i` is the part that directly measures how much the actual selector-occurrence posterior varies across residual packets; (4.5) shows that a fractional crossing produces the needed logarithmic currency.

The relation to SELECTOR_DEBIT is now explicit. Its nonempty packet entropy is
\[
B_i^*=Mh_2(\rho)-L_i.
\tag{6.3}
\]
Thus the difficult packet debit splits exactly into a scalar mean entropy minus a canonical occurrence-information credit. The singleton packet `T=emptyset` is deliberately excluded from (6.3) and is instead tracked by the singleton mismatch term in (6.2); this is where a naive packet argument would otherwise hide a reference change.

## 7. Remaining unpaid implication

This run does **not** prove a universal positive lower bound for `L_i` from physical disagreement alone, and Section 5 proves that such a statement is impossible. The next source-exact implication is a dichotomy on any dangerous selector step:

> either the actual non-singleton occurrence posterior has a fractional crossing, in which case (4.5) supplies logarithmic `K_occ`; or the explicit mismatch terms in (6.2), the exact hierarchy KL after a genuine decomposition, or retained child/potential slack must pay the scalar mean packet entropy.

Equivalently, to finish this route one must rule out a genuine prime Boolean source for which simultaneously

1. `d` is in the rare-disagreement dangerous regime;
2. `c_occ/rho -> 0` (no logarithmic crossing payment);
3. singleton, mean-reference and residual-shape KL mismatches are all too small;
4. the retained child/potential terms are also too small to pay the selector debit.

Producing such a source would refute this proposed selector-payment mechanism, not FEI. Proving it impossible with one dimension-independent quantitative bound would be a substantive step toward the all-gate inequality.

**Next recipient:** `account01/B01`.  
**Full FEI:** **OPEN / NOT PROVED.**
