# A fixed witness against free strong unimodality

Date: 2026-09-30. Status: research proof reconstruction and quantitative sharpening of an existing repository candidate; not a new discovery claim, journal acceptance, or proof-assistant certification.

## Provenance and exact scope

Hasebe and Ueda's Problem 3.11 asks whether a probability measure other than a point mass can preserve unimodality under free additive convolution with every unimodal probability measure. Their finite-variance exclusion is Theorem 3.10. The primary statement is in [ALEA 15 (2018), p.362](https://alea.math.cnrs.fr/articles/v15/15-15.pdf), also [arXiv:1710.08240v2](https://arxiv.org/html/1710.08240).

The repository already contains the proposed complete negative answer in [R08 C005](https://github.com/yspennstate/math-open-problems/blob/master/runs/R08/20260916T1928Z_i0082_local_phi_no_fsu_7f3a91.md) and [C006](https://github.com/yspennstate/math-open-problems/blob/master/runs/R08/20260916T2030Z_i0082_branch_hardening_b6d12c.md). Those reports were left audit-pending. The older campaign index describes only the earlier Cauchy/stable partial results and is not the strongest available history.

This document reconstructs that argument, explicitly addresses its common-cone dependency, and replaces its test-law atom weight 1/1000 by 1/32. The new quantitative result is the larger fixed witness with an exact first-order margin 9/100. No publication-priority claim is made for either the original classification or this improvement.

## Statement

Let

\[
\nu=\frac1{32}\delta_0+\frac{31}{32}\mathbf1_{(0,1)}(x)\,dx.
\]

For every non-Dirac probability measure \(\mu\) on \(\mathbb R\), there are real \(a_c\to0\) such that, for all sufficiently small \(c>0\),

\[
\rho_c=(D_c\mu\boxplus\delta_{a_c})\boxplus\nu
\]

has analytic density neighborhoods at \(1/32,1/16,1/2\), with

\[
p_c(1/32)>p_c(1/16)<p_c(1/2).
\]

Consequently, the only freely strongly unimodal probability measures are Dirac measures. There are no moment, support, density, or infinite-divisibility assumptions on \(\mu\).

## 1. Analytic facts and their scope

Write \(G_\sigma(z)=\int(z-t)^{-1}\,d\sigma(t)\), \(F_\sigma=1/G_\sigma\), and \(\phi_\sigma=F_\sigma^{-1}-\mathrm{id}\) on its canonical inverse domain. We use these standard facts:

1. For every probability law, \(\phi\) is defined on a union of truncated Stolz cones of every aperture; its imaginary part is nonpositive and \(\phi(z)=o(z)\) nontangentially at infinity. It adds under free convolution and obeys \(\phi_{D_c\mu}(z)=c\phi_\mu(z/c)\).
2. A tight family of probability laws has common canonical inverse cones of any fixed aperture. Free convolution is weakly continuous, and weak convergence implies local uniform convergence of Cauchy and reciprocal Cauchy transforms on the upper half-plane.

For (1), see [Pata, *Domains of partial attraction in noncommutative probability*, pp.236–237](https://msp.org/pjm/1996/176-1/pjm-v176-n1-p13-p.pdf). For the common-cone assertion, see [Bercovici–Pata, *Stable laws and domains of attraction in free probability theory*, Proposition 2.6(1), printed p.1030](https://arxiv.org/pdf/math/9905206). The latter is important: the proof must not silently let the high starting point of a continuation path escape to infinity as c decreases.

The sign in (1) is local for arbitrary laws; extending \(\phi\) with that sign to the whole upper half-plane would be the stronger free-infinite-divisibility property, which is not assumed here.

## 2. Strict sign without moments

For \(z=x+iy\in\mathbb C^+\), Cauchy–Schwarz gives

\[
\Im F_\mu(z)-y
=\frac{y}{|G_\mu(z)|^2}\left(\int|z-t|^{-2}\,d\mu(t)-|G_\mu(z)|^2\right)\ge0.
\]

Equality holds only if \(t\mapsto(z-t)^{-1}\) is constant \(\mu\)-almost surely, equivalently if \(\mu\) is a point mass. Thus \(\Im F_\mu(z)>\Im z\) for non-Dirac \(\mu\). On the canonical inverse domain this implies \(\Im\phi_\mu<0\).

Set \(S_c=-\phi_{D_c\mu}\). Its domains exhaust every compact subset of \(\mathbb C^+\) as \(c\downarrow0\), and \(S_c\to0\) locally uniformly. Indeed every compact lies in some finite-aperture cone, and dilation lowers that cone's truncation height to zero. The asymptotic \(\phi_\mu(z)=o(z)\) then proves local uniform smallness. Derivatives also tend to zero on smaller compacts by Cauchy estimates.

## 3. The flat witness and sharp Harnack comparison

Put \(r=1/32\), \(\beta=\pi(1-r)\). The upper boundary branch on \((0,1)\) is

\[
G_\nu(x)=A(x)-i\beta,
\qquad A(x)=r/x+(1-r)\log(x/(1-x)),
\]

and direct differentiation gives

\[
A'(x)=\frac{x-r}{x^2(1-x)}.
\]

At \(x_1=r,x_2=2r,x_3=1/2\), let \(z_j=F_\nu(x_j)\in\mathbb C^+\). Then

\[
A'(x_1)=0,\quad A'(x_2)=128/15,\quad A'(x_3)=15/4.
\]

For a positive harmonic function h on \(\mathbb C^+\) with \(h(z_3)=1\), the optimal Harnack lower bound at \(z_2\) is

\[
L=\frac{\sqrt{\Delta^2+4\beta^2}-\Delta}
{\sqrt{\Delta^2+4\beta^2}+\Delta},
\qquad \Delta=\frac{31}{32}\log15-\frac7{16}>0.
\]

To see this formula, apply the real Möbius automorphism \(z\mapsto-1/z\); it sends the two points to \(-A(x_j)+i\beta\), which have equal height and horizontal separation \(\Delta\). Then use the disk Harnack factor \((1-\rho)/(1+\rho)\), with \(\rho=\Delta/\sqrt{\Delta^2+4\beta^2}\).

Now \(\log15<11/4\) because

\[
\sum_{k=0}^6\frac{(11/4)^k}{k!}=\frac{9019421}{589824}>15.
\]

Together with \(\pi>3\), this yields \(\Delta/\beta<95/124\). For \(0<\ell<1\), the displayed Harnack factor exceeds \(\ell\) precisely when

\[
(\Delta/\beta)^2<(1-\ell)^2/\ell.
\]

Take \(\ell=9/20\). The exact certificate is

\[
\frac{121}{180}-\left(\frac{95}{124}\right)^2
=\frac{58999}{691920}>0.
\]

Therefore \(L>9/20\). This lower bound can be used on a fixed relatively compact disk domain in \(\mathbb C^+\): map \(z_3\) to the disk center, choose a radius R sufficiently close to one so that the disk Harnack lower bound \((R-\rho)/(R+\rho)\) remains greater than 9/20, and pull back. Enlarge R if necessary to include all three witness points. This avoids assuming that the local \(S_c\) are globally Pick functions.

## 4. Normalization

Set

\[
a_c=\Re S_c(z_3),\qquad \eta_c=\Im S_c(z_3)>0,
\qquad H_c=(S_c-a_c)/\eta_c.
\]

Then \(a_c\to0\), \(\eta_c\to0\), and \(H_c(z_3)=i\). On any fixed connected relatively compact domain containing the required points, \(H_c\) eventually maps into \(\mathbb C^+\). Harnack and the analytic normalization give local uniform bounds for \(H_c\) and its derivatives. In particular,

\[
\Im H_c(z_2)>9/20,\qquad \Im H_c(z_3)=1.
\]

For \(\lambda_c=D_c\mu\boxplus\delta_{a_c}\),

\[
\phi_{\lambda_c}=-\eta_cH_c.
\]

## 5. Identification of the actual branch

This is the nonformal step. Fix any sequence \(c_n\downarrow0\). The families \(\lambda_{c_n}\), \(\nu\), and \(\rho_{c_n}\) are tight, since they converge weakly to \(\delta_0,\nu,\nu\), respectively. The common-cone theorem supplies a common canonical inverse cone in the transform variable w. Choose a fixed interior high point \(w_*\) and a small disk B around it in that cone. Put

\[
z_*=F_\nu^{-1}(w_*),\qquad
z_n(w)=F_{\rho_{c_n}}^{-1}(w)
=F_\nu^{-1}(w)+\phi_{\lambda_{c_n}}(w).
\]

Thus \(z_n(w)\to F_\nu^{-1}(w)\) uniformly on a smaller disk. Additivity, initially an identity of germs, holds throughout the common connected cone by analytic continuation. Choose a fixed neighborhood of the compact image \(F_\nu^{-1}(\overline B)\) in the original upper half-plane. The actual transform at \(z=z_n(w)\) equals w by canonical inverse composition. Applying \(F_\nu\) to the inverse identity yields the following equation on the nonempty open starting set \(z_n(B)\), which lies in that fixed neighborhood for all sufficiently large n. Here \(W_n=F_{\rho_{c_n}}\):

\[
W_n(z)=F_\nu\bigl(z+\eta_{c_n}H_{c_n}(W_n(z))\bigr). \tag{*}
\]

Join that fixed neighborhood to an upper-half-plane neighborhood of each \(x_j\) by a compact path, then include a small disk across \(x_j\) using the analytic upper-boundary continuation of \(F_\nu\). Because \(F_\nu(x_j)\in\mathbb C^+\), the disks can be chosen so that their images and those of the paths stay in a fixed compact subset of \(\mathbb C^+\). Choose slightly larger compact neighborhoods throughout.

On this fixed tube, \(\phi_{\lambda_{c_n}}\) and its first derivative tend uniformly to zero. Hence the equation

\[
w-F_\nu(z-\phi_{\lambda_{c_n}}(w))=0
\]

has a unique analytic solution near \(w=F_\nu(z)\), uniformly on the tube, by the analytic implicit-function theorem (or uniform contraction on small graph neighborhoods). On the nonempty open starting set \(z_n(B)\), uniqueness identifies it with the actual \(W_n\). The identity theorem propagates this equality along the connected upper-half-plane tube. Consequently the actual Cauchy transform continues analytically through each witness point and is represented by (*).

Local boundedness of the normalized \(H_{c_n}\), including derivatives, now gives the uniform expansion

\[
G_{\rho_{c_n}}(x_j)
=G_\nu(x_j)+\eta_{c_n}G_\nu'(x_j)H_{c_n}(z_j)+O(\eta_{c_n}^2).
\]

To check the remainder explicitly, (*) first implies \(W_n-F_\nu=O(\eta_{c_n})\). Substitute this into \(H_{c_n}(W_n)=H_{c_n}(F_\nu)+O(\eta_{c_n})\), Taylor expand \(F_\nu\), and invert; \(F_\nu\) is bounded away from zero on the selected neighborhoods. All constants are uniform along the chosen sequence. No differentiability in c is needed.

This proves the required conclusion along every sequence tending to zero. The all-sufficiently-small-c statement follows: a contrary sequence of exceptional c would contradict the preceding argument.

## 6. The strict valley

Stieltjes inversion on the analytic neighborhoods and the reality of \(G_\nu'(x_j)=A'(x_j)\) give

\[
p_c(x_j)=31/32-\frac{\eta_c}{\pi}A'(x_j)\Im H_c(z_j)+O(\eta_c^2).
\]

The first coefficient is zero; the second is greater than \((9/20)(128/15)=96/25\); the third is 15/4. Their gap satisfies

\[
96/25-15/4=9/100>0.
\]

Since \(\eta_c>0\) tends to zero, both asserted valley inequalities follow. A unimodal measure cannot have such a valley in three analytic density neighborhoods: according to which side of the middle point contains its mode, one of its two monotonicity conditions is violated. This remains true if the measure has an atom at its mode elsewhere.

Finally, \(\nu\) is unimodal with mode zero. Free strong unimodality is preserved under positive dilation and translation, because the same operations preserve unimodality and commute with free convolution in the corresponding way. Thus an FSU \(\mu\) would make \(\rho_c\) unimodal, a contradiction. Dirac measures plainly have the property by translation.

## What this establishes and what it does not

The mathematical reconstruction gives a full-scope negative answer conditional only on the explicitly cited standard analytic facts, and the finite constants are separately executable. It is an audit/strengthening of a recovered September 16 proof, not a newly discovered full solution. Specialist independent review and broader publication-priority clearance remain important before public theorem claims. The work does not solve FEI, Benjamini–Schramm, or any other famous conjecture.
