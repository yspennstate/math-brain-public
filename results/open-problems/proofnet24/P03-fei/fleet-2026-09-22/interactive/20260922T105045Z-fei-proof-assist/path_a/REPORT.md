# A monotone occurrence-credit bank, an amortized generation theorem, and the obstruction to fixed-fraction reserves

**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Control:** `2026-09-22.3`  
**Work date:** 2026-09-22 UTC  
**Full uniform-cube FEI:** **OPEN; NOT PROVED HERE.**

This report proves two complementary statements. First, the canonical occurrence dependence credit can increase under physical restriction, but its increase is paid by the existing phase potential: their sum is a supermartingale for every physical restriction tree. An exact decomposition identifies six nonnegative terms in its drift. Consequently, all newly generated occurrence credit over an arbitrarily deep adaptive tree has a dimension-free budget. Second, reserving any fixed positive fraction of the occurrence credit inside a finite-center all-gate potential is impossible. A genuine sparse-defect suspension eventually defeats every nonempty physical block at the same root.

The first statement supplies a proved replacement for the false monotonicity of occurrence credit alone. The second eliminates a stronger Bellman target which cannot hold even on a simple family satisfying FEI with a bounded constant. Neither statement proves the missing universal payment of the remaining packet entropy.

## 1. Sources, scope, and notation

The following immutable internal sources were read and used. Abstract information identities are standard; no literature priority claim is made.

1. [B01 signed credit Bellman report](https://github.com/yspennstate/math-open-problems/blob/d576857ad5101ca8b8f18215397e66598e132da5/proofnet24/P03-fei/fleet-2026-09-22/account01/B01/20260922T103250Z-account01-B01-fei-r11/REPORT.md), especially Sections 2–4 and 6. This defines the unnormalized credit and fixed-fraction reserve, gives the signed Bellman recursion, and refutes credit monotonicity by a four-bit Boolean example.
2. [B14 selector-occurrence KL split](https://github.com/yspennstate/math-open-problems/blob/a762a4b434958c6b16a5d5d07e17b26feec9e24e/proofnet24/P03-fei/fleet-2026-09-22/account03/B14/20260922T103926Z-occurrence-kl-selector/REPORT.md), Sections 1–3. This identifies the singleton, residual-shape, mean-reference, and selector-information terms.
3. [Influence I-projection and Pythagorean theorem](https://github.com/yspennstate/math-open-problems/blob/4bd6d05f1eb8325d665f2748f4d74dcee2550a04/proofnet24/P03-fei/fleet-2026-09-21/account02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md), Sections 2–4. This defines the maximum-entropy nonempty reference and its exact KL projection identity.
4. [Folded all-bias Jensen–Shannon payment](https://github.com/yspennstate/math-open-problems/blob/92c75e9bcd2fe9c5dc2bedc8a032b31b4afb5484/proofnet24/P03-fei/fleet-2026-09-21/account01/B12/20260922T090347Z-folded-js-shannon/REPORT.md), Sections 1–3. Only its candidate-independent information theorem is used in the optional biased corollary.
5. [Sparse-suspension occurrence-credit obstruction](https://github.com/yspennstate/math-open-problems/blob/7ec649dfb3d1ab2f92855f2069590fca2ac956dd/proofnet24/P03-fei/fleet-2026-09-21/account04/B15/20260922T093820Z-full-convolution-energy-obstruction/REPORT.md). The underlying family and its large occurrence credit are prior team inputs. Section 6 below derives the additional fixed-reserve and every-block implications.

The simultaneous companion derivation is `../interference/REPORT.md`, *Physical restriction entropy and the phase-potential refund*. It independently proves the phase function's strong concavity and its physical-tree accounting. We include the needed proof below so the new uniform-cube results do not depend on an unavailable external source or an unreviewed theorem statement. That companion should be pinned to the same publication commit as this report.

For a Boolean function at product bias, let its squared orthonormal Fourier law be

\[
 U_f(S)=\widehat f(S)^2,
 \qquad v_f=1-\widehat f(\varnothing)^2.
\]

For a nonconstant function put \(P_f(S)=U_f(S)/v_f\) on nonempty sets. Let \(Q_f\) be the unique maximum-entropy law on nonempty sets matching every occurrence marginal of \(P_f\). Define

\[
 K(f)=D_2(P_f\Vert Q_f),\qquad
 \mathcal C(f)=v_f K(f).
\tag{1.1}
\]

Set \(\mathcal C=0\) for constants. It also vanishes on characters, including products of several coordinates. All entropy and KL are in bits. For mixtures we use

\[
 \operatorname{JS}_{\omega}(P_0,P_1)
 =\sum_{a=0}^1\omega_aD_2(P_a\Vert\omega_0P_0+\omega_1P_1).
\tag{1.2}
\]

Terms with zero mixture weight are omitted. Degenerate references are interpreted on their actual support; equivalently, use finite-dimensional limits from the relative interior. A finite-entropy marginal face forces the same zero or deterministic coordinates in both the actual law and its maximum-entropy reference. Thus this convention does not discard positive actual mass.

## 2. An exact signed-transfer decomposition

Fix a physical selector with input bias \(s\in(0,1)\), children \(f_0,f_1\), and branch weights \(\alpha_0=1-s,\alpha_1=s\). Put \(v_a=v_{f_a}\), \(v=v_f\), and

\[
 b=\widehat f(\{i\})^2,\qquad
 M=v-b=\alpha_0v_0+\alpha_1v_1.
\tag{2.1}
\]

The last equality is Parseval on the nonempty residual packets. Suppose initially that \(M>0\). Put

\[
 \omega_a=\frac{\alpha_av_a}{M},\qquad
 P_* =\omega_0P_0+\omega_1P_1.
\tag{2.2}
\]

Under the parent nonempty reference \(Q_f\), let

\[
 \sigma=Q_f(\{i\}),\quad
 Q_* =\mathcal L_{Q_f}(S\setminus\{i\}\mid S\setminus\{i\}\ne\varnothing),
\]

and let \(\theta\) be the reference probability of including selector \(i\) conditional on a nonempty residual set. This selector is independent of the residual set under that conditional reference. Write

\[
 p=\operatorname{It}_i(f),\qquad
 \rho=\frac{p-b}{M}.
\]

For the actual parent law, let \(B=1_{i\in S}\) and \(T=S\setminus\{i\}\). Define four nonnegative quantities

\[
 E_{\rm singleton}=vD_2(\operatorname{Ber}(b/v)\Vert\operatorname{Ber}(\sigma)),
\]
\[
 E_{\rm mean}=MD_2(\operatorname{Ber}(\rho)\Vert\operatorname{Ber}(\theta)),
\]
\[
 L_{\rm occ}=M I(B;T\mid T\ne\varnothing),
\]
\[
 T_{\rm reference}=M\sum_a\omega_a D_2(Q_a\Vert Q_*).
\tag{2.3}
\]

Here \(Q_a\) is the child I-projection, whereas \(Q_*\) comes from the parent. Keeping this distinction is essential.

### Theorem 1 — the signed transfer has one explicit negative term

The signed credit transfer satisfies

\[
\boxed{
 \Xi_i:=\mathcal C(f)-\sum_a\alpha_a\mathcal C(f_a)
 =E_{\rm singleton}+E_{\rm mean}+L_{\rm occ}+T_{\rm reference}
  -M\operatorname{JS}_{\omega}(P_0,P_1).
}
\tag{2.4}
\]

In particular,

\[
\boxed{
 [-\Xi_i]_+
 \le M\operatorname{JS}_{\omega}(P_0,P_1)
 \le\operatorname{JS}_{\alpha}(U_0,U_1).
}
\tag{2.5}
\]

**Proof.** The parent reference on a nonempty residual set is a product of \(Q_*\) and an independent Bernoulli selector. Successive KL chain rules give the B14 identity

\[
 \mathcal C(f)=E_{\rm singleton}+E_{\rm mean}+L_{\rm occ}
     +MD_2(P_*\Vert Q_*).
\tag{2.6}
\]

For completeness, the excluded empty-parent state is the only residual-empty state with selector absent. Conditional on being nonempty, the residual-empty event is therefore precisely the singleton selector. Splitting off that event gives the first KL term. On its complement, splitting the joint residual/selector law against \(Q_*\otimes\operatorname{Ber}(\theta)\) gives the last residual KL, the mean Bernoulli KL, and the mutual information. No sign or packet is suppressed.

The mixture identity and I-projection Pythagoras give, respectively,

\[
 \sum_a\omega_aD_2(P_a\Vert Q_*)
 =D_2(P_*\Vert Q_*)+\operatorname{JS}_{\omega}(P_0,P_1),
\]
\[
 D_2(P_a\Vert Q_*)=D_2(P_a\Vert Q_a)+D_2(Q_a\Vert Q_*).
\tag{2.7}
\]

The latter follows directly because the log ratio of two nonempty conditional-product laws is affine in the occurrence indicators. Actual law \(P_a\) and reference \(Q_a\) match these indicators in expectation. Multiplying by \(M\), noting \(M\omega_a=\alpha_av_a\), and substituting into (2.6) proves (2.4).

Finally the child spectra decompose into an empty atom and a nonempty conditional law. The information chain rule for the branch label therefore gives exactly

\[
 \operatorname{JS}_{\alpha}(U_0,U_1)
 =\operatorname{JS}_{\alpha}(\operatorname{Ber}(v_0),\operatorname{Ber}(v_1))
   +M\operatorname{JS}_{\omega}(P_0,P_1).
\tag{2.8}
\]

Both information terms are nonnegative, proving (2.5). If \(M=0\), both children are constants and the parent depends on at most the selector. Every occurrence credit is zero, so (2.5) still holds; (2.4) extends with all residual terms zero. The other boundary cases follow on their support as stated in Section 1. \(\square\)

The inequality (2.5) is the new link needed to transfer the physical phase budget to the canonical occurrence credit. It does not suppose that \(\Xi_i\) has either sign.

### Independent proof of the one-sided payment

There is a shorter proof of the final inequality in (2.5), independent of the four-term parameter formulas. For any full spectral probability law \(U\), let \(\overline Q_U\) maximize entropy subject to its empty-set mass and all occurrence marginals. It has the prescribed empty mass and, conditional on nonemptiness, the nonempty product I-projection. Thus

\[
 \mathcal C(U)=D_2(U\Vert\overline Q_U)=H(\overline Q_U)-H(U).
\tag{2.9}
\]

Delete selector \(i\). The marginal of the actual parent law is \(E=\alpha_0U_0+\alpha_1U_1\). The marginal \(R\) of \(\overline Q_U\) remains in the same maximum-entropy exponential family on the smaller set: its nonempty masses are a common constant times the original product of coordinate odds, and its empty mass has an independently adjustable value. This can also be seen from the family \(\log R(S)=c_0+c_\varnothing\mathbf1_{S=\varnothing}+\sum_jc_j\mathbf1_{j\in S}\). Data processing and Pythagoras therefore give

\[
 \mathcal C(U)\ge D_2(E\Vert R)
 =\mathcal C(E)+D_2(\overline Q_E\Vert R)\ge\mathcal C(E).
\tag{2.10}
\]

The maximum attainable entropy is concave in its constraint vector. Indeed, mixing two feasible maximizers produces a feasible law for the mixed vector, whose entropy is at least the mixture of their entropies. Consequently

\[
 \mathcal C(E)\ge\sum_a\alpha_a H(\overline Q_{U_a})-H(E)
 =\sum_a\alpha_a\mathcal C(U_a)-\operatorname{JS}_{\alpha}(U_0,U_1).
\tag{2.11}
\]

Combining (2.10)–(2.11) proves \(-\Xi_i\le\operatorname{JS}_{\alpha}(U_0,U_1)\), and hence its positive-part version. Support faces follow by the same finite-dimensional continuity convention. This provides an independent route to the supermartingale theorem; the sharper nonempty JS bound and the six-term equality still use (2.4).

## 3. The correct monotone bank on the uniform cube

Now all input biases are \(1/2\). Write \(I_i(f)=\operatorname{Inf}_i(f)\), and define

\[
 j(t)=1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right),\qquad
 \mathcal P(f)=\sum_i j(I_i(f)),\qquad
 J(f)=\sum_i\min(I_i(f),1-I_i(f)).
\tag{3.1}
\]

The function \(j\) is symmetric and concave. More precisely, with \(z=2\sqrt{t(1-t)}\), direct differentiation and the power series of \(\operatorname{atanh}\) give

\[
 j''(t)=-\frac{4[\operatorname{atanh}(z)-z]}{(\ln2)z^3}
 =-\frac4{\ln2}\sum_{k\ge1}\frac{z^{2k-2}}{2k+1}
 \le-\frac4{3\ln2}.
\tag{3.2}
\]

The endpoints extend continuously, and the first derivatives match at \(t=1/2\), where the second derivative tends to minus infinity. Consequently

\[
 j(\mathbb EZ)-\mathbb Ej(Z)\ge\frac2{3\ln2}\operatorname{Var}(Z),
 \qquad
 0\le\mathcal P(f)\le\frac2{\ln2}J(f)\le\frac2{\ln2}I(f).
\tag{3.3}
\]

For the last assertion, use \(j(0)=0\), \(j'(0+)=2/\ln2\), its tangent bound, and symmetry.

At a uniform physical selector, put \(u_T=\widehat f_0(T)\), \(w_T=\widehat f_1(T)\),

\[
 e_T=(u_T^2+w_T^2)/2,\qquad
 q_T=\frac{(u_T-w_T)^2}{2(u_T^2+w_T^2)},\qquad d=I_i(f)=\sum_Te_Tq_T.
\]

The actual child-mixture information satisfies

\[
 Q_i:=\operatorname{JS}_{1/2}(U_0,U_1)=\sum_T e_Tj(q_T)\le j(d).
\tag{3.4}
\]

Indeed, if \(a=u_T^2/(u_T^2+w_T^2)\), the packet contribution to JS is \(e_T[1-h_2(a)]\). The identity \(q_T(1-q_T)=(u_T^2-w_T^2)^2/[4(u_T^2+w_T^2)^2]\) shows that \(1-h_2(a)=j(q_T)\). Jensen proves the inequality.

For each unqueried coordinate \(k\), physical restriction gives \(I_k(f)=[I_k(f_0)+I_k(f_1)]/2\). Hence the phase refund

\[
 B_i^{\rm phase}=\mathcal P(f)-\frac{\mathcal P(f_0)+\mathcal P(f_1)}2-Q_i
\tag{3.5}
\]

is nonnegative, with the stronger bound

\[
 B_i^{\rm phase}\ge
 \frac2{3\ln2}\sum_Te_T(q_T-d)^2
 +\frac1{6\ln2}\sum_{k\ne i}[I_k(f_0)-I_k(f_1)]^2.
\tag{3.6}
\]

This follows by applying (3.3) to the packet distribution and then to each equally weighted pair of child influences.

### Theorem 2 — occurrence credit plus phase is a physical supermartingale

Define \(\mathcal M(f)=\mathcal C(f)+\mathcal P(f)\). Every uniform physical restriction satisfies the exact six-term decomposition

\[
\boxed{
 \mathcal M(f)-\frac{\mathcal M(f_0)+\mathcal M(f_1)}2
 =E_{\rm singleton}+E_{\rm mean}+L_{\rm occ}+T_{\rm reference}
   +J_{\rm variance}+B_i^{\rm phase}\ge0,
}
\tag{3.7}
\]

where

\[
 J_{\rm variance}=\operatorname{JS}_{1/2}(\operatorname{Ber}(v_0),\operatorname{Ber}(v_1)).
\]

**Proof.** Add (3.5) to the signed decomposition (2.4). Equation (2.8) cancels the nonempty child-mixture information, leaving precisely the variance information. All six remaining terms are nonnegative. \(\square\)

Thus the four-bit counterexample to monotonicity of \(\mathcal C\) alone is consistent with an exact monotone replacement. The difference between the two banks is a bounded, explicit phase cost, not an unspecified reserve.

## 4. Dimension-free adaptive-tree generation and variation bounds

Consider any finite adaptive tree of genuine uniform coordinate restrictions. A path never queries an already fixed coordinate. Stop at arbitrary Boolean leaves. Let \(\pi_v\) be the actual probability of reaching node \(v\), and let \(F_L\) be the random leaf function. Put

\[
 N_T=\sum_{v\text{ internal}}\pi_v[-\Xi_v]_+,
 \qquad
 P_T^+=\sum_{v\text{ internal}}\pi_v[\Xi_v]_+,
 \qquad
 B_T^{\rm phase}=\sum_v\pi_v B_v^{\rm phase}.
\tag{4.1}
\]

Here \(N_T\) counts increases of average child credit, and \(P_T^+\) counts decreases. These are expected node drifts, rather than pathwise fluctuations of the credit random variable; the distinction matters.

### Theorem 3 — generated occurrence credit has one root budget

Every such tree satisfies

\[
\boxed{
 N_T\le\mathcal P(f)-\mathbb E\mathcal P(F_L)-B_T^{\rm phase}
 \le\mathcal P(f)\le\frac2{\ln2}J(f).
}
\tag{4.2}
\]

In addition,

\[
\boxed{
 P_T^+=\mathcal C(f)-\mathbb E\mathcal C(F_L)+N_T
 \le\mathcal M(f)-\mathbb E\mathcal M(F_L)-B_T^{\rm phase}.
}
\tag{4.3}
\]

Finally, the six nonnegative local terms in (3.7) sum exactly to

\[
 \mathcal M(f)-\mathbb E\mathcal M(F_L).
\tag{4.4}
\]

**Proof.** By (2.5), \([-\Xi_v]_+\le Q_v\). Sum with weights \(\pi_v\). Telescoping (3.5) gives

\[
 \sum_v\pi_vQ_v=\mathcal P(f)-\mathbb E\mathcal P(F_L)-B_T^{\rm phase},
\]

which proves (4.2). Telescoping the definition of \(\Xi\) gives

\[
 P_T^+-N_T=\sum_v\pi_v\Xi_v=\mathcal C(f)-\mathbb E\mathcal C(F_L).
\]

This proves (4.3). Telescoping (3.7) proves (4.4). Adaptive selection changes none of these cancellations, because each child is weighted by its genuine conditional branch probability. \(\square\)

The phase refund in (4.2) retains both variance payments in (3.6). If the leaves are constants or characters, their occurrence credit and phase both vanish. Then \(N_T\le\mathcal P(f)-B_T^{\rm phase}\) and \(P_T^+\le\mathcal C(f)+\mathcal P(f)-B_T^{\rm phase}\).

This is a dimension-free amortized result despite the fact that \(\mathcal C(f)/I(f)\) can be arbitrarily large, as recursive majority below proves. The inherited credit is counted once; extra credit created by restriction has a separate bounded budget. No influence-only bound on all positive transfers can hold, because their sum over a complete tree is at least the initial credit. The distinction between ordinary influence and folded influence is essential when using the other example below: for \(m\ge2\), the sparse suspension has \(I(F_m)=1+mp_m\), whereas \(J(F_m)=mp_m\); that particular family does not establish an unbounded ratio \(\mathcal C(F_m)/I(F_m)\).

### Optional all-bias corollary

The exact transfer theorem (2.4) is valid at arbitrary interior product biases. Set \(V_s=4s(1-s)\) and let \(d=\Pr[f_0\ne f_1]\) under the actual remaining product input law. Applying the already proved folded weighted JS estimate of Source 4 gives

\[
 [-\Xi_i]_+\le\kappa(s)V_s\min(d,1-d)\le\kappa(s)\operatorname{It}_i,
\quad
 \kappa(s)=\frac{\ln((1-s)/s)}{(1-2s)\ln2},
\tag{4.5}
\]

with \(\kappa(1/2)=2/\ln2\). Fixing the original coordinate prices \(\kappa(p_i)\), the weighted influence functional \(W(f)=\sum_i\kappa(p_i)\operatorname{It}_i(f)\) telescopes under physical restrictions. Thus every product-bias adaptive tree obeys \(N_T\le W(f)-\mathbb EW(F_L)\le W(f)\).

This extension uses Source 4's weighted two-point inequality; the uniform results above have a complete independent proof. Its bias prices are bounded by the natural input entropy price plus a fixed influence cost:

\[
 \kappa(s)\le\frac2{\ln2}+\log_2\frac1{V_s}
 \le\frac2{\ln2}+\frac{h_2(V_s)}{V_s}.
\tag{4.6}
\]

To see the first inequality, set \(x=|1-2s|\). Then
\(\kappa(s)\ln2=2\operatorname{atanh}(x)/x=2+\sum_{k\ge1}2x^{2k}/(2k+1)\le2+\sum_{k\ge1}x^{2k}/k=2-\ln(1-x^2)\). The second follows by dropping the other nonnegative term in binary entropy. No bias-independent pointwise price is asserted.

## 5. Why the monotone bank does not prove FEI

The target remains \(H(f)\le C I(f)\) with one finite universal \(C\). Theorem 3 controls credit generated by restriction. It does not provide a lower bound on the initial occurrence credit sufficient to pay the influence-marginal deficit, and it does not pay the rare-event packet entropy in the physical entropy recursion.

In particular, writing \(\mathcal M\) as a monotone bank does not justify reserving a fixed fraction of it in an all-gate supersolution. The next section proves that even the smaller reserve \(\lambda\mathcal C\) is too strong. A successful Bellman state would need to use credit in relation to the actual first-moment deficit, with a state-dependent amount, or combine the drift decomposition with an independently proved stopping rule. The explicit six-term identity prevents a reference mismatch from being silently discarded; it does not imply that those terms automatically pay the remaining packet entropy.

## 6. Fixed-positive-fraction reserves are impossible

Let \(\Gamma\) be symmetric with \(\Gamma(0)=\Gamma(1)=0\) and finite center \(c=\Gamma(1/2)\). At uniform inputs its gate defect is

\[
 D_\Gamma(f)=cI(f)-\Gamma(\Pr[f=-1])-H(f).
\]

The B01 reserve is

\[
 A_{\Gamma,\lambda}(f)=D_\Gamma(f)-\lambda\mathcal C(f),\qquad\lambda>0.
\tag{6.1}
\]

### An exact recursive-majority obstruction

Let \(R_m\) be depth-\(m\) recursive majority of three on \(n_m=3^m\) uniform bits. It is balanced, every coordinate influence is \(r_m=2^{-m}\), and

\[
 I_m=(3/2)^m,\qquad H(R_m)=4(I_m-1).
\tag{6.1a}
\]

These formulas have a direct proof: majority of three has four Fourier coefficients of magnitude \(1/2\), three at level one and one at level three, so its entropy is two and its total influence is \(3/2\). Under disjoint composition with balanced copies, the occupied outer set is recoverable from the nonempty child packets. Entropy therefore satisfies \(H_m=2+(3/2)H_{m-1}\), while influence multiplies by \(3/2\) and each leaf influence multiplies by \(1/2\). The initial values at depth zero are entropy zero and influence one, proving (6.1a).

Let \(\zeta\in(0,1)\) be the conditional-product I-projection parameter for \(R_m\). Because all marginals equal \(r_m\), its maximum entropy is exactly

\[
\begin{aligned}
 H_{\max}
 &=\log_2\zeta-I_m\log_2(\zeta r_m)
        -(n_m-I_m)\log_2(1-\zeta r_m)\\
 &=mI_m-(I_m-1)\log_2\zeta
        -(n_m-I_m)\log_2(1-\zeta r_m)\ge mI_m.
\end{aligned}
\tag{6.1b}
\]

Both remaining terms are nonnegative. Thus the following statements are exact, rather than asymptotic:

\[
\boxed{
 \mathcal C(R_m)\ge(m-4)I_m+4,
 \qquad \frac{\mathcal C(R_m)}{I_m}\ge m-4+\frac4{I_m}\longrightarrow\infty.
}
\tag{6.1c}
\]

The ordinary balanced gate defect is \(D_\Gamma(R_m)=(c-4)(I_m-1)\). If \(c<4\), the ordinary defect already fails. If \(c\ge4\) and \(\lambda>0\), then

\[
 A_{\Gamma,\lambda}(R_m)
 \le[c-4-\lambda(m-4)]I_m-(c-4)-4\lambda<0
\tag{6.1d}
\]

whenever \(m>4+(c-4)/\lambda\). Therefore no universal fixed-positive-fraction occurrence-credit reserve exists at any finite center. This example also proves that an influence-only upper bound on initial occurrence credit is false, even for functions with \(H/I<4\).

The remaining sparse family supplies the stronger simultaneous obstruction for every physical root block, which is not inferred merely from recursive majority's negative root defect.

Let \(x\) be \(m\) independent uniform bits and let \(y\) be one further uniform sign. Define actual Boolean functions

\[
 g_m(x)=1-2\mathbf1_{\{x=0^m\}},\qquad F_m(y,x)=y g_m(x).
\tag{6.2}
\]

Put \(p_m=2^{1-m}\), and define \(F_0=-y\). The coefficients of \(g_m\) are \(1-p_m\) at the empty set and \(-p_m\) at every nonempty set, up to the harmless signs determined by the bit convention. Multiplication by \(y\) shifts all these coefficients to sets containing \(y\). Hence \(F_m\) is balanced and

\[
 I(F_m)=1+mp_m,
\]
\[
 H_m:=H(F_m)=H(g_m)
 =-(1-p_m)^2\log_2(1-p_m)^2+(2p_m-p_m^2)(2m-2).
\tag{6.3}
\]

Every old occurrence marginal in \(F_m\) equals \(p_m\); the new coordinate \(y\) is always present. Thus the I-projection has \(y\) deterministically present and the old coordinates independently Bernoulli \(p_m\). It follows exactly that

\[
 \mathcal C(F_m)=mh_2(p_m)-H_m,
\qquad
 D_\Gamma(F_m)=cmp_m-H_m.
\tag{6.4}
\]

The nonempty spectrum of \(g_m\), by contrast, is uniform on all nonempty old subsets. It is itself a conditional-product law, so \(\mathcal C(g_m)=0\).

### Theorem 4 — no fixed positive reserve can hold universally

For every finite \(c\) and every fixed \(\lambda>0\), \(A_{\Gamma,\lambda}(F_m)<0\) for all sufficiently large \(m\), independently of the off-center shape of \(\Gamma\).

**Proof.** Put \(a=1/\ln2\). Elementary Taylor expansion at \(p=0\) gives

\[
 \frac{h_2(p_m)}{p_m}=m-1+a+O(p_m),
\qquad
 \frac{H_m}{p_m}=4m-4+2a+O(mp_m).
\tag{6.5}
\]

Therefore, writing \(a_m=A_{\Gamma,\lambda}(F_m)/p_m\),

\[
\boxed{
 a_m=-\lambda m^2+[c-4+\lambda(5-a)]m
          +(1-\lambda)(4-2a)+O((1+\lambda)mp_m).
}
\tag{6.6}
\]

The negative quadratic term dominates. \(\square\)

For \(c>4\), the ordinary defect is nevertheless positive for all sufficiently large \(m\), because \(D_\Gamma(F_m)/(mp_m)\to c-4\). Thus this is an obstruction to the proposed reserve architecture, not a counterexample to FEI or even to the balanced gate inequality on this family.

The exact necessary reserve at this state, whenever the denominator is positive, is

\[
 \lambda\le\frac{cmp_m-H_m}{mh_2(p_m)-H_m}
 \sim\frac{c-4}{m}\quad(c>4).
\tag{6.7}
\]

This gives a quantitative calibration: reserving a universal positive fraction is too much by a factor growing linearly in the number of rare-defect coordinates.

### Theorem 5 — every nonempty physical block can fail at the same root

Assume additionally that \(D_\Gamma(g_r)\ge0\) for every \(r\ge1\). This is a necessary elementary-subclass condition on any prospective universal \(\Gamma\), since \(g_r\) is an AND/OR gate up to input/output signs. Then for every fixed \(\lambda>0\), all sufficiently large \(m\) satisfy

\[
\boxed{
 A_{\Gamma,\lambda}(F_m)
 -\mathbb E\,A_{\Gamma,\lambda}(F_m\mid x_B)
 <0
}
\tag{6.8}
\]

for **every nonempty physical coordinate block** \(B\subseteq\{y,x_1,\ldots,x_m\}\). The expectation uses actual uniform restrictions. In particular no choice of a root selector, or of a larger fixed root block, can establish the fixed-reserve Bellman step.

**Proof.** First suppose \(B\) consists of \(b\ge1\) old coordinates. With probability \(2^{-b}\), every revealed bit is zero and the remaining function is \(F_{m-b}\). Every other restriction is a character \(\pm y\), whose defect and credit are both zero. For \(m-b\ge1\),

\[
 A(F_m)-\mathbb EA(F_m\mid x_B)
 =p_m(a_m-a_{m-b}),
\tag{6.9}
\]

since \(2^{-b}p_{m-b}=p_m\). For \(m-b=0\), this remains true upon setting \(a_0=0\).

Equation (6.6) implies

\[
 a_m-a_{m-1}=-2\lambda m+c-4+\lambda(6-a)+o(1).
\tag{6.10}
\]

Thus \(a_m\) is eventually strictly decreasing and tends to minus infinity. For all sufficiently large \(m\), it is consequently smaller than **every** preceding \(a_r\), including the finite initial segment and \(a_0\). This proves strict negativity simultaneously for all old-only blocks.

Now suppose the block includes \(y\). Each remaining function is either a constant or \(\pm g_r\). Its occurrence credit is zero. Symmetry of \(\Gamma\) and the assumed elementary-subclass validity imply that its defect is nonnegative. Theorem 4 makes the root augmented defect negative. Therefore root minus expected child augmented defect is strictly negative. This covers all remaining blocks. \(\square\)

Without the elementary-subclass assumption, Theorem 4 already rules out a universal nonnegative fixed-reserve supersolution. The extra assumption in Theorem 5 is stated explicitly because otherwise an off-center potential could assign negative defects to the very AND children used in its comparison.

The obstruction to a **universal nonnegative fixed-fraction reserve** also applies to \(\mathcal M=\mathcal C+\mathcal P\): \(\mathcal P\ge0\) only makes that proposed root augmented defect smaller. This observation alone does not transfer Theorem 5's separate every-block drift assertion to the enlarged bank. We do not infer that all possible state-dependent or nonlinear credit-reserving arguments fail.

## 7. Verification and concrete handoff

`CHECK.py` performs deterministic finite checks on genuine Boolean truth tables using integer Walsh transforms. It evaluates the parent and child maximum-entropy references separately and checks the signed decomposition, the nonempty/full JS split, the six-term monotone-bank equality, the quantitative phase refund, and complete adaptive-tree budgets. It also evaluates the explicit sparse reserve obstruction at high decimal precision and checks the depth-two recursive-majority entropy and influence from its actual truth table. These computations test implementation and endpoint conventions; the arbitrary-dimension results are proved above. `CHECK_RESULTS.json` records the actual cases and discrepancies.

The completed run checked **1,307 functions**, **25,874 local selector instances**, and **1,195 complete adaptive trees**. It exhausts all truth tables through three variables and adds deterministic larger samples, characters, one-point defects, suspensions, and depth-two recursive majority. The largest identity discrepancy was **1.78e-15**. For \(c=7,\lambda=0.1,m=100\), 160-digit evaluation gave \(A(F_m)/p_m=-663.42380148\ldots\), and the largest normalized old-only block drift was \(-16.54426950\ldots\). Blocks containing \(y\) use the analytic elementary-subclass assumption of Theorem 5; the checker does not invent an unspecified admissible potential.

What should be carried into active research memory:

* **Proved in this report:** signed occurrence-credit generation is bounded by actual child-mixture information; \(\mathcal C+\mathcal P\) is a physical supermartingale; all generated occurrence credit has a single dimension-free phase budget with retained variance refunds.
* **Refuted by analytic Boolean families:** a universal fixed-positive-fraction reserve \(D_\Gamma-\lambda\mathcal C\ge0\); an influence-only upper bound on initial occurrence credit or on total positive transfers over a complete tree; and, for an elementary-subclass-admissible potential, a policy promising a valid fixed-reserve step at some physical root block for every function.
* **Still unproved:** the full FEI inequality; any universal state-dependent reserve construction; any stopping rule that pays rare-event packet entropy from the displayed drift terms.

This is a project-level mathematical derivation with finite numerical checks. It is not a formal proof-assistant certificate, an independent full literature audit, or a global verification of the fleet's other claims.
