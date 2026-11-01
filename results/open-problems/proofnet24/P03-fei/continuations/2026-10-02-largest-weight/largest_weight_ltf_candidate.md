# Candidate largest-weight split theorem for all deterministic LTFs

Date: 2026-10-02. **CANDIDATE PROOF — not a verified breakthrough.**
This new continuation is being subjected to independent audit. It combines
established biased-halfspace estimates with a proposed slab-noise lemma and
a dyadic KL argument. A failure at any step invalidates the full conclusion.
The previously completed restricted results are independent of this file.

All entropy and KL divergence below use base-2 logarithms; \(\ln\) is natural.
The uniform cube convention is \(\widehat f(S)=\mathbb E f\chi_S\).

## Proposed conclusion

There is an absolute \(C_*\) such that every nonconstant Boolean LTF,
split on a coordinate of largest absolute input weight, satisfies

\[
 \Delta_iH(f):=H(f)-\tfrac12[H(f^{+})+H(f^{-})]
 \le C_* I_i(f).
\tag{1}
\]

If (1) is correct, induction proves FEI for all deterministic LTFs because
each restriction is an LTF and
\(I(f)=I_i(f)+\tfrac12[I(f^+)+I(f^-)]\).
This does not imply FEI for all Boolean functions.

## 1. Established inputs and normalization

Coordinate sign changes and an output sign change preserve every quantity
in (1). Thus take a monotone LTF, with nonnegative input weights, and positive
output density \(p\le1/2\). Ties at the threshold can be removed by moving
the threshold slightly inside the finite gap between the largest negative
and smallest positive score; the Boolean function is unchanged.

Let coordinate \(i\) have largest weight \(w>0\). Let the remaining weights
be \(a_j\in[0,w]\), with
\(\sigma^2=\sum_j a_j^2\), and put

\[
 R=\sigma^2/w^2,\quad L=\ln(1/p),\quad M=\max\{1,R,L\}.
\]

Write the split as

\[
 f(x,z)=A(x)+zB(x),\qquad
 B(x)=\mathbbm1\{|\sum_j a_jx_j-\theta|<w\}.
\tag{2}
\]

The open slab notation is valid after the threshold perturbation. Its values
at endpoints otherwise use the corresponding half-open interval; all
concentration arguments also apply to closed intervals. Put
\(\alpha=\mathbb E B=I_i(f)\).

A coordinate of largest weight also has largest influence. Indeed, for
\(w_i\ge w_j\), monotonicity gives \(I_i=\widehat f(\{i\})\), and after
conditioning on other coordinates,

\[
 I_i-I_j=\tfrac12\mathbb E\bigl[
 f(T+w_i-w_j)-f(T-w_i+w_j)\bigr]\ge0.
\]

Keller–Klein (2019), Theorem 1.4, gives an absolute \(c>0\) with

\[
 \alpha\ge c p\min\{1,\sqrt{L/(R+1)}\}.
\tag{3}
\]

Therefore

\[
 \frac{p\sqrt L}{\sqrt M}\le\frac{\sqrt2}{c}\alpha.
\tag{4}
\]

For \(L\le R+1\), use \(R+1\le2M\); for \(L>R+1\), \(M=L\).
Also \(\alpha\le2p\), since the pivotal slab accounts for an edge joining
the rare output to the other output, and the rare endpoint has probability
\(\alpha/2\) in the full cube.

Klivans–O'Donnell–Servedio (2004), Theorem 18, gives

\[
 \operatorname{NS}_\varepsilon(f)\le20.5p\sqrt{\varepsilon L}.
\tag{5}
\]

These are established primary results, not newly proved here. Sources:
<https://arxiv.org/html/1710.07429v3>;
<https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>.

## 2. Proposed slab-noise lemma, with an elementary proof

**Lemma.** For \(B\) in (2), \(R>0\), and \(0\le\rho<1\),

\[
 \operatorname{Stab}_\rho(B)
 \le\alpha\min\left\{1,\frac6{\sqrt{(1-\rho)R}}\right\}.
\tag{6}
\]

Here stability is \(\mathbb E B(X)B(Y)\), without centering.

### A bounded-weight interval concentration estimate

If \(Z=\sum_j b_jX_j\), independent unbiased signs, \(|b_j|\le w\), and
\(v=\sum_j b_j^2>0\), then for every center \(t\),

\[
 \Pr(|Z-t|\le w)\le\min\{1,3w/\sqrt v\}.
\tag{7}
\]

For a direct Fourier proof, use
\(K(u)=(\sin(u/(2w))/(u/(2w)))^2\). On \(|u|\le w\), \(K(u)>9/10\),
because \(\sin s/s\ge1-s^2/6\ge23/24\) on \(|s|\le1/2\). The identity

\[
 K(u)=w\int_{-1/w}^{1/w}(1-w|t|)e^{itu}\,dt
\]

follows by integrating the triangular kernel. For \(|t|\le1/w\), each
\(|b_jt|\le1\), and \(|\cos(b_jt)|\le e^{-b_j^2t^2/2}\). Hence

\[
 \begin{aligned}
 \Pr(|Z-t_0|\le w)
 &\le\tfrac{10}{9}\mathbb E K(Z-t_0)\\
 &\le\tfrac{10}{9}w\int_{-1/w}^{1/w}
        |\mathbb E e^{itZ}|\,dt\\
 &\le\tfrac{10}{9}w\int_{\mathbb R}e^{-vt^2/2}\,dt
 <3w/\sqrt v.
 \end{aligned}
\]

The bound is uniform in the center and permits atoms and endpoint ties.

### Apply concentration after a random resampling mask

To produce \(\rho\)-correlated \(X,Y\), independently keep each coordinate
of \(X\) with probability \(\rho\); otherwise resample a fresh unbiased
sign. Let \(J\) be the set of resampled coordinates and
\(V_J=\sum_{j\in J}a_j^2\). Conditional on \((J,X)\), the retained
coordinates only change the slab center. Its half-width stays \(w\), so (7)
gives

\[
 \Pr(B(Y)=1\mid J,X)\le\min\{1,3w/\sqrt{V_J}\},
\]

with upper bound 1 when \(V_J=0\).

Put \(\varepsilon=1-\rho\) and \(\mu=\varepsilon R\). A weighted
Bernoulli Chernoff bound gives

\[
 \Pr(V_J<\varepsilon\sigma^2/2)\le e^{-\mu/8}.
\tag{8}
\]

For completeness, scale summands by \(w^2\), so they lie in \([0,1]\).
For \(u\in[0,1]\), \(e^{-u}\le1-(1-e^{-1})u\). Exponential Markov with
parameter 1 yields an upper bound
\(\exp[-((1-e^{-1})-1/2)\mu]\le e^{-\mu/8}\).

On the good-mask event, conditional slab probability is at most
\(3\sqrt2/\sqrt\mu\). Crucially, \(J\) is independent of \(X\), and
the good/bad condition depends only on \(J\). Thus

\[
 \begin{aligned}
 \operatorname{Stab}_\rho(B)
 &=\mathbb E_{J,X}\left[B(X)\Pr(B(Y)=1\mid J,X)\right]\\
 &\le\alpha\left[\frac{3\sqrt2}{\sqrt\mu}+e^{-\mu/8}\right]
 \le\frac{6\alpha}{\sqrt\mu}.
 \end{aligned}
\]

The final inequality uses
\(\sup_{u>0}\sqrt u e^{-u/8}=2e^{-1/2}\), whose addition to
\(3\sqrt2\) is less than 6. The trivial stability bound is \(\alpha\).
This proves (6), if the preceding reasoning is correct.

## 3. Low-degree mass for the normalized slab spectrum

Let \(Q_S=\widehat B(S)^2/\alpha\), a probability law. Write \(K=|S|\)
under this law. The proposed consequence is

\[
 \boxed{Q(K\le k)\le18\sqrt{k/M}\quad(k\ge1).}\tag{9}
\]

First suppose \(R>0\). Choose \(\rho=1-1/(2k)\). For integer \(k\ge1\),
\(\rho^k\ge1/2\), so (6) implies

\[
 Q(K\le k)\le2\operatorname{Stab}_\rho(B)/\alpha
 \le12\sqrt{2k/R}<18\sqrt{k/R}.
\tag{10}
\]

For real \(k\ge1\), replace it by \(\lfloor k\rfloor\).

Independently, the standard Bonami–Beckner hypercontractive inequality for
an indicator gives
\(\operatorname{Stab}_{1/2}(B)\le\alpha^{4/3}\). Consequently

\[
 Q(K\le k)\le2^k\alpha^{1/3}.
\tag{11}
\]

If \(L\ge2\ln2\), then \(\ln(1/\alpha)\ge L-\ln2\ge L/2\). For
\(1\le k\le L/(12\ln2)\), (11) is at most \(e^{-L/12}\), hence at
most \(1.5\sqrt{k/L}\) because
\(\sup_{L>0}\sqrt L e^{-L/12}=\sqrt6 e^{-1/2}<1.5\).
For \(k>L/(12\ln2)\), the trivial bound 1 is at most
\(3\sqrt{k/L}\). For \(L<2\ln2\) the same trivial bound works for all
\(k\ge1\). Therefore

\[
 Q(K\le k)\le3\sqrt{k/L}.
\tag{12}
\]

If \(M=R\), use (10); if \(M=L\), use (12); if \(M=1\), the trivial
bound is enough. This proves (9), including \(R=0\). The zero-degree mass
is known exactly:

\[
 Q(K=0)=\widehat B(\varnothing)^2/\alpha=\alpha.
\tag{13}
\]

## 4. Degree tails for the full split-pair spectrum

Let \(P_S=\widehat A(S)^2+\widehat B(S)^2\). The pointwise identity
\(A^2+B^2=1\) gives \(\sum_S P_S=1\). Its degree is the degree in the
remaining coordinates. For each \(S\), the two full-function spectral
coefficients are \(\widehat A(S)\) at \(S\), and \(\widehat B(S)\) at
\(S\cup\{i\}\). Hence

\[
 P(|S|\ge u)\le\Pr_{\widehat f^2}(|T|\ge u).
\]

The noise-tail calculation in `regular_biased_ltf_fei.md`, from (5), gives
for every real \(u>0\)

\[
 P(|S|\ge u)\le A_0p\sqrt{L/u},\qquad
 A_0=\frac{20.5\sqrt2}{1-e^{-1}}<46.
\tag{14}
\]

For \(u\ge1\), take noise \(1/(2u)\), so all contributing full degrees
lose at least \(1-e^{-1}\) of their stability. For \(u<1\), the full
nonconstant mass is \(4p(1-p)\le4p\), and
\(A_0\sqrt{\ln2}>4\). Thus the estimate includes small \(u\) without
discarding the zero-degree exception improperly.

Combining (14) and (4) gives

\[
 P(|S|\ge u)\le\Gamma\alpha\sqrt{M/u},\qquad
 \Gamma=\max\{1,\sqrt2 A_0/c\}.
\tag{15}
\]

## 5. Dyadic coarse-graining forces KL separation

Keep degree zero as a special atom \(\star\). For every positive degree,
define \(J=\lfloor\log_2(K/M)\rfloor\in\mathbb Z\). Let \(Q_j,P_j\)
be the probabilities of this bin under the slab law and split-pair law.

The lower endpoint of bin \(j\) is \(M2^j\), so (15) gives

\[
 P_j\le\Gamma\alpha2^{-j/2}\quad(j\in\mathbb Z).
\tag{16}
\]

For \(j<0\), the upper endpoint is \(M2^{j+1}\). If this is less than 1,
the positive-degree bin is empty. Otherwise (9) implies

\[
 Q_j\le18\sqrt2\,2^{j/2}.
\]

Therefore

\[
 \mathbb E_Q[|J|\mathbbm1_{J<0}]
 \le C_-:=18\sqrt2\sum_{m=1}^\infty m2^{-m/2}<\infty.
\tag{17}
\]

There is no required upper-tail bound on \(Q\).

Set \(r=2^{-1/4}\), \(Z=\sum_{j\in\mathbb Z}2^{-|j|/4}=(1+r)/(1-r)\),
and choose the reference law

\[
 R_\star=\tfrac12,\qquad R_j=\frac{2^{-|j|/4}}{2Z}.
\]

Nonnegativity of \(D(Q\|R)\) gives

\[
 D(Q\|P)\ge\sum_{j\in\mathbb Z\cup\{\star\}}
     Q_j\log\frac{R_j}{P_j}.
\tag{18}
\]

For positive-degree bins, (16) gives

\[
 \log\frac{R_j}{P_j}
 \ge\log\frac1\alpha-\log(2Z\Gamma)
      +\tfrac12j-\tfrac14|j|.
\]

The last two terms are nonnegative for \(j\ge0\) and equal \(3j/4\) for
\(j<0\). Also \(Q_\star=\alpha\), \(P_\star\le1\), so its contribution
to (18) is at least \(-\alpha\). Therefore

\[
 D(Q\|P)\ge(1-\alpha)\log\frac1\alpha
             -\log(2Z\Gamma)-\tfrac34 C_- -\alpha.
\]

Since \(\alpha\log_2(1/\alpha)\le(\log_2e)/e\), this proves

\[
 \boxed{D(Q\|P)\ge\log_2(1/\alpha)-C_D,}\tag{19}
\]

where \(C_D=\log_2(2Z\Gamma)+\tfrac34 C_-+1+(\log_2e)/e\) is absolute.
Data processing gives the same lower bound for KL on the individual
spectral subsets; (18) used only their coarse bin laws. There is no division
by a vanishing \(P_j\) on the support of \(Q_j\), since pointwise
\(P_S\ge\widehat B(S)^2=\alpha Q_S\).

## 6. Conditional spectral-bit entropy and the split increment

Let \(q_S=\widehat B(S)^2/P_S\). The conditional entropy of inclusion of
coordinate \(i\), given the other spectral coordinates, is

\[
 \mathcal C=\sum_S P_Sh_2(q_S).
\]

The contribution where \(i\) is included is exactly

\[
 \sum_S\widehat B(S)^2\log\frac{P_S}{\widehat B(S)^2}
 =\alpha\left[\log\frac1\alpha-D(Q\|P)\right].
\]

The other contribution is at most \(\alpha\log_2e\), by
\(\ln(1+t)\le t\). Thus (19) gives

\[
 \mathcal C\le\alpha(C_D+\log_2e).
\tag{20}
\]

For completeness, the exact split identity gives

\[
 \Delta_iH(f)=\sum_S P_S[1+h_2(q_S)-h_2(r_S)],\qquad
 r_S=\frac{(\widehat A(S)+\widehat B(S))^2}{2P_S}.
\]

The elementary inequality \(h_2(t)\ge4t(1-t)\) implies
\(1-h_2(r_S)\le4q_S(1-q_S)\le h_2(q_S)\). Hence

\[
 \Delta_iH(f)\le2\mathcal C
 \le2(C_D+\log_2e)\alpha.
\tag{21}
\]

One way to verify the elementary binary-entropy inequality is to expand
\(1-h_2((1+x)/2)\) as a positive power series in \(x^{2m}\), whose
coefficients sum to 1. Since \(x^{2m}\le x^2\) on \([-1,1]\), it is at
most \(x^2\).

If every preceding step survives audit, (21) is the proposed largest-weight
split theorem (1), with \(C_*=2(C_D+\log_2e)\). Induction over the input
dimension then proves FEI for every deterministic LTF. At the time of this
draft that conclusion is **not independently certified**.

## Audit focus

The critical new steps are (6) and the use of dyadic KL in (18)–(19). Audit
must check the resampling-mask independence after multiplication by \(B(X)\),
endpoint/atomic concentration, the rare-event Chernoff contribution relative
to \(\alpha\), the \(R\ll1\) and \(L\gg R\) regimes, the special zero-degree
atom, and the direction of KL data processing. The known primary results
(3) and (5) must be applied with the full-input variance and the physical
influence convention. Finite checks cannot certify this asymptotic argument.
