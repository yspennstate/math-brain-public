# Independent audit: only Dirac laws are freely strongly unimodal

Audit date: 2026-09-30

## Verdict and scope

**Mathematical pass for the proof mechanism, with two explicit repairs to the branch-identification exposition supplied below.** I found no counterexample or substantive obstruction to the arbitrary-law argument. This is a mathematical audit, not a certificate of novelty, peer review, or completion of the repository's administrative closure requirements.

The most delicate assertions were checked analytically, not inferred from the finite symbolic checks. In particular:

- The local Voiculescu transform has the required sign for every probability law, without infinite divisibility
- Dilation makes its canonical domains exhaust the upper half-plane on compact sets
- Centering and normalization give genuinely locally bounded Pick maps, even when the imaginary scale is much smaller than the uncentered real drift
- Uniform local inversion gives an error of order the **square of the imaginary normalization**, not merely the square of the dilation
- A common inverse cone and the identity theorem identify the local solution with the actual free convolution
- The resulting strict valley rules out unimodality in the source's measure-theoretic definition

The literal C006 exposition should be edited before submission. Its use of weak convergence to obtain closeness throughout an upper-half-plane tube touching the real boundary is not justified by locally uniform convergence on the open half-plane. That statement is unnecessary. The replacement in Section 4 avoids it entirely. The report also leaves the uniform choice of a high anchor implicit; a standard published uniform-cone result supplies it.

## 1. Materials and primary-source checks

Repository files read through the GitHub connector, on master:

1. [C005 report](https://github.com/yspennstate/math-open-problems/blob/master/runs/R08/20260916T1928Z_i0082_local_phi_no_fsu_7f3a91.md), blob SHA `5288372d0c7c6cb96c0ae08e888ead839fb25e24`
2. [C006 branch-hardening report](https://github.com/yspennstate/math-open-problems/blob/master/runs/R08/20260916T2030Z_i0082_branch_hardening_b6d12c.md), blob SHA `b2da40ffb975a89ae5b2b42f47ecf38f98ab10ee`

Primary sources independently inspected:

- Hasebe–Ueda, [ALEA 15 (2018), 353–374](https://alea.impa.br/articles/v15/15-15.pdf), Definition 3.8, Theorem 3.10 and Problem 3.11, printed pp.361–362. The target is exactly preservation under free convolution with every unimodal probability law; the known exclusion assumes finite variance; the open question asks for a non-Dirac example
- Pata, [Pacific J. Math. 176 (1996), 235–248](https://msp.org/pjm/1996/176-1/pjm-v176-n1-p13-p.pdf), printed p.236. It explicitly gives the union-of-truncated-cones domain and the lower-half-plane sign for an arbitrary probability law, as well as the dilation formula
- Bercovici–Pata, [Annals of Mathematics 149 (1999), 1023–1060](https://arxiv.org/pdf/math/9905206), Section 2. The discussion on p.1027 gives the local inverse, sign, and nontangential smallness; Theorem 2.1 gives linearization; Proposition 2.6(1), p.1030, gives a common canonical inverse cone for every tight family

These references validate the analytic inputs. They do not themselves state the proposed new classification.

## 2. Arbitrary-law local transform and normalization

Use G_mu(z)=integral (z-t)^(-1) dmu(t), F_mu=1/G_mu, and phi_mu=F_mu^(-1)-id on the canonical inverse domain.

For w in the upper half-plane, Cauchy–Schwarz gives

    |G_mu(w)|² <= integral |w-t|^(-2) dmu(t),
    Im F_mu(w) >= Im w.

Equality holds only when t -> (w-t)^(-1) is constant mu-almost surely. This function is injective on the real line, so a non-Dirac law has strict inequality. For z=F_mu(w) in the canonical inverse range, this proves Im phi_mu(z)<0. No infinite-divisibility hypothesis enters.

Write the canonical domain as a union of cones Gamma_(alpha,beta(alpha)). Inverse branches on overlapping sufficiently high cones agree by their normalization at infinity and analytic continuation. The union is connected. Under dilation,

    phi_(D_c mu)(z)=c phi_mu(z/c).

Every fixed compact subset of the upper half-plane lies in one scaled cone for all sufficiently small c. Nontangential phi_mu(z)=o(z) then gives locally uniform phi_(D_c mu)->0; Cauchy estimates also give convergence of derivatives on smaller compacts.

For the witness transform point z_3, set

    S_c=-phi_(D_c mu),
    a_c=Re S_c(z_3),
    eta_c=Im S_c(z_3)>0,
    H_c=(S_c-a_c)/eta_c,
    lambda_c=D_c mu boxplus delta_(a_c).

Then phi_(lambda_c)=-eta_c H_c, H_c(z_3)=i, eta_c->0 and a_c->0. These signs are correct: translation by a adds a to the Voiculescu transform.

On any fixed bounded connected domain D compactly inside the upper half-plane, H_c maps D to the upper half-plane for small c. The Cayley transforms (H_c-i)/(H_c+i) are disk-valued and vanish at z_3. Schwarz–Pick on a chain of disks gives a uniform bound strictly below 1 on each compact subset of D; hence H_c and all needed derivatives are uniformly bounded there. This argument controls the ratio to eta_c even if eta_c is unusually small.

For completely explicit domain exhaustion one can take the nested disks

    D_R = {z: |z-iR| < R-1/R},  R>1.

They exhaust the upper half-plane. Their disk Harnack constants converge to the half-plane constant. Thus any strict half-plane Harnack margin persists on one sufficiently large fixed D_R. Enlarging the disk to include extra compact transform paths does not invalidate that margin.

## 3. Witness and finite comparison

The witness nu_r=r delta_0+(1-r)1_(0,1)(x)dx is unimodal with mode 0. On its upper boundary sheet,

    G_r(x)=A_r(x)-i beta_r,
    A_r(x)=r/x+(1-r)log(x/(1-x)),
    beta_r=pi(1-r),
    A_r'(x)=(x-r)/(x²(1-x)).

The three ordered points are x_1=r, x_2=2r, x_3=1/2. Therefore

    A_r'(x_1)=0,
    A_r'(x_2)=1/[4r(1-2r)],
    A_r'(x_3)=4-8r.

The original r=1/1000 constants and sign comparison are correct. In particular the reported lower Harnack bound 3/100 yields a coefficient strictly greater than 499/125 at x_2, while the x_3 coefficient is 499/125. This is a fixed positive gap, so an O(eta_c²) error is sufficient.

An independently checked strengthening suggested by the parent researcher is r=1/32. It also works and permits a cleaner sharp Harnack computation:

    beta=31 pi/32,
    Delta=A_r(1/2)-A_r(1/16)=(31/32)log 15-7/16 >0.

The half-plane automorphism z -> -1/z carries z_j=1/(A_r(x_j)-i beta) to -A_r(x_j)+i beta. Thus the two relevant points have equal imaginary coordinate beta, and the sharp Harnack lower ratio is

    L=(sqrt(Delta²+4 beta²)-Delta)/(sqrt(Delta²+4 beta²)+Delta).

The bounds log 15<11/4 and pi>3 give Delta/beta<95/124. The logarithm bound can be certified without decimals:

    sum_(k=0)^6 (11/4)^k/k! = 9019421/589824 >15.

Since

    (95/124)²=9025/15376 <121/180=(1-9/20)²/(9/20),

we have L>9/20. Domain exhaustion therefore supplies a fixed domain on which Im H_c(z_2)>9/20, while Im H_c(z_3)=1. The derivative comparison is

    (9/20)(128/15)-15/4=9/100>0.

This sharpening is optional. The original proof does not depend on it. The rational computations above check constants; the proof's analytic conclusions require the remaining sections.

## 4. Corrected identification of the actual branch

Here is a fully specified replacement for the delicate part of C006. It uses the same strategy and no moment assumptions.

First, lambda_c converges weakly to delta_0, and rho_c=lambda_c boxplus nu_r converges weakly to nu_r by weak continuity of free convolution. The families for c in a sufficiently small closed interval, including their limiting laws at c=0, are tight. Indeed c -> a_c is continuous on the small positive interval, tends to zero, and dilation and translation are weakly continuous. One can alternatively carry out the argument on any sequence c_n down to zero, which is already enough to contradict strong unimodality.

By Bercovici–Pata Proposition 2.6(1), choose a fixed common canonical inverse cone for lambda_c, rho_c and nu_r. Choose an interior point w_* sufficiently high in that cone and put

    z_*=F_(nu_r)^(-1)(w_*),
    z_c=F_(rho_c)^(-1)(w_*)
       =z_*+phi_(lambda_c)(w_*).

Thus z_c->z_* in the upper half-plane. This choice in inverse coordinates avoids an unstated assumption about uniform forward univalence. The same formulas hold for w in a fixed small open disk around w_*.

Choose paths in the upper half-plane from z_* to the upper neighborhoods of the three x_j, and add small disks crossing the real axis at the x_j on the chosen upper boundary sheet. There is a fixed bounded connected neighborhood V of this finite network, with a slightly larger neighborhood for estimates, such that the continued F_(nu_r) has compact image inside the upper half-plane. Choose V so V intersected with the upper half-plane is connected. The explicit logarithmic formula supplies the continuations near each x_j; there is no branch crossing at 0 or 1.

Enlarge the fixed normalization domain D to contain a compact neighborhood of this transform image. Uniform bounds on H_c and H_c' are then available. On a sufficiently small fixed neighborhood of the graph w=F_(nu_r)(z), the maps

    w -> Fhat_(nu_r)(z+eta_c H_c(w))

are contractions for all sufficiently small c: their w-derivatives are uniformly O(eta_c), and their displacement of the unperturbed graph is uniformly O(eta_c). They have a unique analytic fixed point Wtilde_c(z) along V. Local constructions glue by uniqueness. This is a quantitative implicit-function argument, so analytic dependence on the parameter c itself is not required.

For w near w_* let z_c(w)=F_(rho_c)^(-1)(w). Voiculescu linearization gives

    z_c(w)-phi_(lambda_c)(w)=F_(nu_r)^(-1)(w).

Consequently w is a solution of the local fixed-point equation at z_c(w). It lies in the uniqueness neighborhood for small c, hence Wtilde_c(z_c(w))=w. The actual reciprocal Cauchy transform also satisfies F_(rho_c)(z_c(w))=w. Since the inverse image of this small disk is open, the two analytic functions agree on a nonempty open subset of V in the upper half-plane.

The identity theorem now gives

    Wtilde_c=F_(rho_c) on V intersected with the upper half-plane.

The analytic continuation of Wtilde_c through each x_j therefore is the actual upper boundary continuation of the convolution transform.

**No uniform convergence at the real boundary was used.** The corresponding sentence in the original C006 is stronger than weak convergence warrants and should be removed. Common-cone uniformity should be cited explicitly as above.

## 5. Uniform remainder and density conclusion

On fixed smaller neighborhoods of the three x_j, the fixed-point equation and boundedness of H_c first give

    W_c-Fhat_r=O(eta_c).

Uniform bounds on H_c', Fhat_r' and Fhat_r'' then imply, directly by Taylor expansion,

    W_c=Fhat_r+eta_c Fhat_r' H_c(Fhat_r)+O(eta_c²).

No differentiability of c -> H_c and no comparison between eta_c and c are needed. Since Fhat_r is bounded away from zero on these fixed neighborhoods, reciprocal expansion yields

    G_(rho_c)=Ghat_r+eta_c Ghat_r' H_c(Fhat_r)+O(eta_c²).

The same constants work at all three points after taking the maximum of the finitely many local bounds. Analytic continuation and Stieltjes inversion give an analytic density locally around each x_j, with

    p_c(x_j)=1-r-(eta_c/pi) A_r'(x_j) Im H_c(z_j)+O(eta_c²).

At x_1 the first-order coefficient is zero; at x_2 it is uniformly positive and strictly greater than the x_3 coefficient. Therefore, for small positive c,

    p_c(x_1)>p_c(x_2)<p_c(x_3).

This is a valid obstruction to unimodality of a measure, not just of one arbitrarily chosen density version. On neighborhoods of these points the actual density is continuous (indeed analytic), and a density agreeing almost everywhere with a monotone function must preserve its monotonic order at interior continuity points. If the proposed mode equals x_2, continuity and positive-length subintervals on either side give the same contradiction; changing the density at the mode cannot remove the valley. A possible atom elsewhere is irrelevant.

Finally FSU is invariant under positive dilation and translation: pull an arbitrary unimodal test law back by the inverse affine map and use covariance of free convolution. Thus FSU of mu would imply FSU of lambda_c, contradicting this unimodal witness. Dirac laws preserve unimodality by translation.

## Bottom line

After the explicit branch repair above, the argument supports the full arbitrary-probability-law classification. The remaining need is independent expert review and a broader novelty check, not a missing finite-variance or infinite-divisibility extension. Do not describe numerical examples or rational-checker output as verification of the full theorem. No repository files were edited in this audit.

## Review of the September 30 reconstruction

I also read `FREE_UNIMODALITY_RECONSTRUCTION.md`, including its statement and Section 5. The sequential common-cone argument and identity-theorem continuation remove the two problems identified above. The passage from conclusions along every sequence to an all-sufficiently-small-c conclusion is valid: if the asserted property failed arbitrarily close to zero, choose a decreasing sequence of failures and contradict the sequential conclusion. Uniformity of all constants across different chosen sequences is not needed for this logical step.

For a final paper, I recommend making the high-anchor coordinate choice explicit, using w_* and z_c(w) as in Section 4 of this audit, and stating that local uniform convergence and uniqueness identify the branches on the interior starting neighborhood. This is clarification of a standard, available step, not a remaining obstruction. I found no material flaw in the reconstructed statement or Section 5.
