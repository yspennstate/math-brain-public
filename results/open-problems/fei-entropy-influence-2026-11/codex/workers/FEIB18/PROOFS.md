# Fourier entropy of linear threshold functions

PROVED. Every linear threshold function on the uniform cube satisfies

\[
 H(f)\le \left[\frac3{\ln2}+4+2\log_2\left(1+2\frac{101913}{100}\right)\right]I(f)
 <30.316\,I(f)<31\,I(f).
\]

Here \(H(f)=\sum_T\widehat f(T)^2\log_2(1/\widehat f(T)^2)\) and \(I(f)=\sum_T|T|\widehat f(T)^2\). This section proves the assertion without a concentration theorem with an unspecified constant. The decimal evaluation is recorded in constants.json and verification.json; the expression in brackets is the proved constant.

Normalize the representation by negating and permuting coordinates so that \(a=w_1\ge w_j\ge0\). Constant functions need no proof; remove zero weights. Move the threshold slightly, if necessary, to preserve all function values and ensure \(w\cdot x\ne\theta\) on the finite cube. Write

\[
 s(y)=\sum_{j\ge2}w_jy_j-\theta,\quad S=\{|s|<a\},\quad h=1_S,
 \quad g=\operatorname{sgn}(s)1_{S^c},\quad\delta=\Pr(S).
\]

Then \(f=g+x_1h\), \(D_1f=h\), and \(\operatorname{Inf}_1(f)=\delta\). A nonconstant function has \(\delta>0\). Indeed, if a coordinate of weight \(b\le a\) is pivotal with \(x_1=e\in\{-1,1\}\), then, writing \(r\) for the remaining sum minus the threshold, \(|r+ea|<b\). Fixing that coordinate to \(e\) gives \(|r+eb|<a\), so coordinate 1 is pivotal. A nonconstant function has a pivotal edge somewhere.

All lemmas below are PROVED. Zero-mass entropy terms are defined by continuity.

## Window comparison

Let \(R=\sum_jv_j\epsilon_j\), where the signs are independent and uniform and \(0<v_j\le a\). For \(0\le c\le\alpha\),

\[
 \Pr(\alpha\le R\le\alpha+a)\le2\Pr(c-a\le R\le c+a). \tag{1}
\]

Use induction on the number of summands, including the empty sum. For the empty sum the assertion follows directly: the left event is possible only when \(\alpha=c=0\). Put \(W_c=[c-a,c+a]\), \(J=[\alpha,\alpha+a]\), and write \(R=R'+v\epsilon\). It suffices to compare \(J+v\) with \(W_{c+v}\), and \(J-v\) with \(W_{c-v}\), each with factor 2. The first comparison is the induction hypothesis; so is the second if \(c\ge v\).

If \(c<v\), put \(e=v-c\in(0,a]\), \(\beta=\alpha-v\ge-e\). Symmetry gives \(\Pr(R'\in W_{c-v})=\Pr(R'\in W_e)\). If \(\beta\ge e\), use induction with center \(e\). If \(e-a\le\beta<e\), then \([\beta,\beta+a]\subseteq W_e\). Finally, if \(-e\le\beta<e-a\), split this interval into

\[
 [\beta,e-a)\quad\hbox{and}\quad[e-a,\beta+a].
\]

The second piece lies in \(W_e\). The reflection of the first is \((a-e,-\beta]\), which also lies in \(W_e\), since \(e\le a\) and \(\beta\ge-e\). Its mass is therefore at most the mass of \(W_e\). The two disjoint pieces give the factor 2. The half-open split counts every endpoint exactly once. This proves (1), including \(v=a\) and all atoms at endpoints.

## Tail comparison

With \(\sigma^2=\sum_jv_j^2\), for every \(t\ge0\),

\[
 \Pr(R>t+a)\le\frac{16}{3}(1+\sigma/a)\Pr(|R-t|\le a). \tag{2}
\]

The empty sum is immediate. For a nonempty sum, let \(S_k\) be its partial sums and let \(\tau\) be the first index with \(S_k>t+a\). Overshoot is at most \(a\), so \(S_\tau\le t+2a\). Conditional on \(\tau=k\) and the past, the remainder is independent, symmetric, and has variance at most \(\sigma^2\). Thus its probability of exceeding \(2\sigma\) is at most \(1/8\), by symmetry and Chebyshev.

Also \(\Pr(\tau<\infty)\le2\Pr(R>t+a)\). To see this directly, on every stopped path the remainder is nonnegative with probability at least one half, and then the final sum still exceeds \(t+a\). Summing over the disjoint stopping events proves this one-sided Lévy inequality, with strict inequalities and atoms allowed.

Put \(L=a+2\sigma\). A final value exceeding \(t+a+L\) forces the remainder after \(\tau\) to exceed \(2\sigma\). Consequently

\[
 \Pr(R>t+a+L)\le\tfrac14\Pr(R>t+a),
 \quad
 \Pr(R>t+a)\le\tfrac43\Pr(t+a<R\le t+a+L).
\]

Cover the latter interval by \(\lceil L/a\rceil\le2+2\sigma/a\) closed intervals of length \(a\), each starting at a point at least \(t\). Apply (1) with center \(t\) to each interval and sum. Overlap at their endpoints only increases this upper bound. This gives (2).

## Concentration with an explicit constant

For the same sum, if \(\sigma>0\), every interval of length \(2a\) has probability at most

\[
 Q(R,2a)\le\min(1,3a/\sigma). \tag{3}
\]

For any center \(u\), use the nonnegative kernel

\[
 k(v)=\left(\frac{\sin(v/(2a))}{v/(2a)}\right)^2
     =a\int_{-1/a}^{1/a}(1-a|z|)e^{izv}\,dz.
\]

On \(|v|\le a\), the alternating sine estimate gives \(k(v)\ge(23/24)^2\). For \(|z|\le1/a\), each \(|v_jz|\le1\); integrating \(\tan r\ge r\) shows \(0<\cos r\le e^{-r^2/2}\) there. Hence the characteristic function obeys \(|\mathbb E e^{izR}|\le e^{-\sigma^2z^2/2}\). The kernel representation gives

\[
 \Pr(|R-u|\le a)
 \le(24/23)^2\mathbb E k(R-u)
 \le(24/23)^2a\int_{\mathbb R}e^{-\sigma^2z^2/2}\,dz
 = (24/23)^2\sqrt{2\pi}\,a/\sigma <3a/\sigma.
\]

The last inequality follows, for example, from \(\pi<22/7\) and \((576/529)^2(44/7)<9\). Open intervals satisfy the same bound. If \(\sigma=0\), use the trivial bound 1. Thus \(K_0=3\) is admissible in the use of Kolmogorov–Rogozin in the original argument; (3) supplies its proof directly for the sums needed here.

## Crossing and remaining in the slab

For \(0\le\rho<1\), let \((y,z)\) be a uniform \(\rho\)-correlated pair. Define

\[
 \mathrm{Stay}=\Pr(y,z\in S),\qquad
 \mathrm{Cross}=\Pr(s(y)>a,s(z)<-a)+\Pr(s(z)>a,s(y)<-a).
\]

Then

\[
 \mathrm{Cross}\,\mathrm{Stay}\le80\delta^2. \tag{4}
\]

To prove this, independently refresh each coordinate with probability \(p=1-\rho\). Let \(T\) be the refreshed set, chosen independently of \(y\). Off \(T\), set \(z_j=y_j\); on \(T\), draw fresh independent uniform signs. Conditional on \(T\) and the unrefreshed signs,

\[
 s(y)=A+U,\quad s(z)=A+V,\qquad
 A=\sum_{j\notin T}w_jy_j-\theta,
\]

where \(U,V\) are independent copies of the symmetric sum on \(T\), and \(\sigma_T^2=\sum_{j\in T}w_j^2\). The same conditional description holds on conditioning only on \((T,A)\).

There are no atoms at the window endpoints \(\pm a-A\), because such an atom would give a full-cube tie for \(f\). Conditional on \(T,A\), symmetry and (2) yield

\[
 \begin{aligned}
 \mathrm{Cross}(T,A)
 &=2\Pr(U>a-A)\Pr(U>a+A)\\
 &\le2\Pr(U>a+|A|)\\
 &\le\frac{32}{3}(1+\sigma_T/a)\Pr(|U-|A||\le a)\\
 &=\frac{32}{3}(1+\sigma_T/a)\Pr(y\in S\mid T,A).
 \end{aligned}
\]

In the last line symmetry changes a center \(|A|\) to \(-A\), and absence of endpoint atoms changes the closed window to the slab's open window. Since \(T\) is independent of \(y\), averaging first over \(A\) and then over \(T\) gives

\[
 \mathrm{Cross}\le\frac{32}{3}\delta(1+x),\qquad
 x=\sqrt p\,\sigma/a,\quad \sigma^2=\sum_{j\ge2}w_j^2,
\]

using \(\mathbb E\sigma_T\le\sqrt{\mathbb E\sigma_T^2}=a x\).

Given \((T,y)\), (3) bounds the chance that \(z\in S\) by \(\min(1,3a/\sigma_T)\). This bound depends on \(T\) only. Independence again gives

\[
 \mathrm{Stay}\le\delta\,\mathbb E_T\min(1,3a/\sigma_T).
\]

For completeness, put \(Z=\sigma_T^2/a^2\), a sum of independent variables in \([0,1]\), with mean \(x^2\). Convexity gives

\[
 \mathbb E e^{-uZ}\le\exp(-(1-e^{-u})x^2).
\]

With \(u=\ln2\), Markov's inequality implies

\[
 \Pr(Z\le x^2/2)
 \le\exp(-\tfrac12(1-\ln2)x^2)\le e^{-x^2/8}.
\]

Thus, for \(x>0\),

\[
 \mathrm{Stay}\le\delta\left(e^{-x^2/8}+\min(1,3\sqrt2/x)\right).
\]

At \(x=0\) use the trivial bound \(\delta\); the displayed upper bound is interpreted by continuity and is also valid. Finally,

\[
 \begin{aligned}
 \sup_{x\ge0}(1+x)\left(e^{-x^2/8}+\min(1,3\sqrt2/x)\right)
 &\le 2+3\sqrt2+2e^{-1/2},\\
 \frac{32}{3}(2+3\sqrt2+2e^{-1/2})&<80.
 \end{aligned}
\]

Indeed, \((1+x)\min(1,b/x)\le1+b\) for \(b=3\sqrt2\), while \((1+x)e^{-x^2/8}\le1+2e^{-1/2}\). For the strict bound by 80 one may use \(\sqrt2<99/70\) and \(e^{-1/2}<61/100\); these rational bounds are checked in constants.py. This proves (4), including an empty refreshed set and zero remaining variance. No exchange between two different noise rates is required.

## From noise to level products

Write \(A_k=W^k(g)\), \(B_k=W^k(h)\), so that \(\sum A_k=1-\delta\), \(\sum B_k=\delta\), \(B_0=\delta^2\). For every integer \(K\ge0\),

\[
 A_{\ge K}B_{\le K}\le M\delta^2,\qquad M=\frac{101913}{100}. \tag{5}
\]

The case \(K=0\) follows from \(B_0=\delta^2\). For \(K\ge1\) use

\[
 W^{\le K}(v)\le\rho^{-K}\operatorname{Stab}_\rho(v),\qquad
 W^{\ge K}(v)\le\frac{\|v\|_2^2-\operatorname{Stab}_\rho(v)}{1-\rho^K}.
\]

Both follow term by term from the nonnegative Fourier weights. The second also counts level \(K\). Set \(\rho=1/2\) for \(K=1\), and \(\rho=1-1/K\) for \(K\ge2\). In the latter case \(1/4\le\rho^K\le e^{-1}\). In both cases the product of the two prefactors is at most \(4/(1-e^{-1})<6.33\).

Here \(\operatorname{Stab}_\rho(h)=\mathrm{Stay}\), and exchangeability of the pair gives the exact identity

\[
 \|g\|_2^2-\operatorname{Stab}_\rho(g)
 =\tfrac12\mathbb E(g(y)-g(z))^2
 =\Pr(y\notin S,z\in S)+2\mathrm{Cross}
 =\delta-\mathrm{Stay}+2\mathrm{Cross}.
\]

Consequently the product is at most

\[
 6.33(\delta+2\mathrm{Cross})\mathrm{Stay}
 \le6.33(1+160)\delta^2=M\delta^2.
\]

## Two sequences

Suppose nonnegative finite sequences satisfy \(\sum B_k=\delta>0\) and (5) for every \(K\ge0\). Then

\[
 \sum_k\Phi(A_k,B_k)
 \le\left[\frac1{\ln2}+4+2\log_2(1+2M)\right]\delta,
 \qquad \Phi(A,B)=A\log_2(1+B/A)+B\log_2(1+A/B). \tag{6}
\]

The first summand in \(\Phi\) is at most \(B/\ln2\). The function \(q(A,B)=B\log_2(1+A/B)\) is increasing in both arguments, concave, and homogeneous of degree one; hence \(\sum_{k\in G}q(A_k,B_k)\le q(A_G,B_G)\).

Put \(\beta_k=B_{\le k}/\delta\). Discard levels with \(\beta_k=0\), whose \(B_k\) and entropy contributions are zero. Group the others into \(G_j=\{k:2^{-j-1}<\beta_k\le2^{-j}\}\), for \(j\ge0\). For a nonempty group let \(k_j=\min G_j\). The product hypothesis and monotonicity of \(\beta\) imply

\[
 A_{G_j}\le M\delta/\beta_{k_j}\le2^{j+1}M\delta,
 \qquad B_{G_j}\le2^{-j}\delta.
\]

Thus its contribution to \(q\) is at most

\[
 2^{-j}\delta\log_2(1+2^{2j+1}M)
 \le2^{-j}\delta(2j+\log_2(1+2M)).
\]

Sum using \(\sum_{j\ge0}2^{-j}=2\), \(\sum_{j\ge0}j2^{-j}=2\), then add \(\delta/\ln2\). This proves (6). The hypothesis at \(K=0\) is essential for unrestricted sequences and has already been verified for these level weights.

## Entropy induction

For a coordinate split \(f=g+x_1h\), write \(a_T=\widehat g(T)\), \(b_T=\widehat h(T)\), and let \(\mathcal E_1\) be the conditional entropy of the spectral membership bit of coordinate 1, given the rest of its spectral set. Coarsening this conditioning to \(|T|\) gives

\[
 \mathcal E_1\le\sum_k\Phi(A_k,B_k).
\]

The entropy of the mixture of the two restricted spectra gives the exact identity

\[
 H(f)-\tfrac12[H(f_+)+H(f_-)]=\mathcal E_1+J_1,
\]

where

\[
 J_1=\sum_T(a_T^2+b_T^2)
 \left[1-h_2\left(\tfrac12+\frac{a_Tb_T}{a_T^2+b_T^2}\right)\right]
 \le\frac2{\ln2}\sum_Tb_T^2=\frac2{\ln2}\delta. \tag{7}
\]

One elementary verification of the last scalar inequality is as follows. With natural logs let

\[
 F(r)=\tfrac12(1+r)^2\ln\frac{(1+r)^2}{1+r^2}
       +\tfrac12(1-r)^2\ln\frac{(1-r)^2}{1+r^2}.
\]

For \(0\le r<1\), \(F(0)=F'(0)=0\) and

\[
 F''(r)=2\ln\frac{1-r^2}{1+r^2}+\frac4{1+r^2}\le4.
\]

So \(F(r)\le2r^2\), including \(r=1\) by continuity. This gives (7) when \(|b|\le|a|\). When \(|b|>|a|\), the entropy deficit is at most \((a^2+b^2)\ln2\le2b^2\) in natural-log units. Zero coefficients follow by continuity.

Equations (5)–(7) bound the entropy loss at coordinate 1 by \(C\delta\), with the constant in the theorem. Restrictions remain threshold functions, and Parseval gives

\[
 I(f)=\delta+\tfrac12[I(f_+)+I(f_-)].
\]

Induction on the number of remaining coordinates, ending with constants, now proves \(H(f)\le C I(f)\). This includes one-variable and two-variable functions and restrictions that become constant or acquire zero weights.

CHECKED with finite scope: attack.py and verify.py test the stated inequalities on the saved rational-grid and structured families through dimension 16. They are independent checks of the proof, not a replacement for any all-dimensional argument.

OPEN: the optimal constant in this route and the corresponding good-coordinate criterion for general Boolean functions. No general FEI theorem is asserted here.
