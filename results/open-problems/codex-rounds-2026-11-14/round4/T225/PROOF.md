# A prediction-relevant proximal bottleneck arbitrarily near initialization

The model is the same one-neuron sine regression as in the two earlier
folders. The theorem concerns proximal measures of explicit nearby laws.
It makes no assertion that those laws occur on a nonlinear MFLD trajectory.

## 1. Statement

Let \(\gamma=N(0,1)\), \(\pi=\gamma\otimes\gamma\), and

\[
 f_\rho(x)=\int a\sin(wx)\,d\rho(a,w),\qquad
 R(\rho)=\tfrac12\mathbb E_{X\sim\gamma}(f_\rho(X)-\sin X)^2.
 \tag{1}
\]

Write

\[
 K(v,w)=\mathbb E\sin(vX)\sin(wX)
 =e^{-(v^2+w^2)/2}\sinh(vw),\qquad g(w)=K(1,w).
 \tag{2}
\]

For \(0<\eta\leq1\), take independent \(B,W\sim\gamma\) and define

\[
 \rho_\eta=\operatorname{Law}(B+\eta g(W),W),\quad
 H(x)=\mathbb E[g(W)\sin(Wx)],\quad
 G_\eta(w)=\mathbb E[(\sin X-\eta H(X))\sin(wX)].
 \tag{3}
\]

The associated proximal law at temperature \(\lambda>0\) is

\[
 p_{\eta,\lambda}(da,dw)
 =Z_{\eta,\lambda}^{-1}e^{aG_\eta(w)/\lambda}\pi(da,dw).
 \tag{4}
\]

Let \(S(a,w)=(-a,-w)\). For an S-invariant probability law \(p\), set

\[
 \beta_S(p)=\inf_{\substack{u\circ S=u\\0<\operatorname{Var}_p(u)<\infty}}
 \frac{\int|\nabla u|^2\,dp}{\operatorname{Var}_p(u)}.
 \tag{5}
\]

The tests in (5) have finite Sobolev energy. Define \(\alpha_S(p)\) by
\(\operatorname{Ent}_p(u^2)\leq2\alpha_S(p)^{-1}\int|\nabla u|^2dp\)
for S-invariant tests.

**Theorem.** The laws \(\rho_\eta\) are S-invariant, and

\[
 \begin{split}
 J&:=\mathbb E g(W)^2=\frac{e^{-1/3}-e^{-1}}{2\sqrt3}>0,\\
 \operatorname{KL}(\rho_\eta\Vert\pi)&=\eta^2J/2,\\
 \mathbb E_{\rho_\eta}(a^2+w^2)&=2+\eta^2J,\\
 R(\rho_\eta)-R(\pi)&\leq-\eta(1-\eta/2)J<0.
 \end{split}
 \tag{6}
\]

Their residual correlation has the exact formula

\[
 G_\eta(w)=e^{-(1+w^2)/2}\sinh w
 -\frac\eta{\sqrt3}e^{-(1+w^2)/3}\sinh(w/3).
 \tag{7}
\]

There is exactly one \(r_\eta>0\) for which \(G_\eta(r_\eta)=0\).
The residual is strictly positive on \((0,r_\eta)\) and strictly
negative on \((r_\eta,\infty)\). Define the positive constants

\[
 A_\eta=\max_{0\leq w\leq r_\eta}G_\eta(w),\qquad
 B_\eta=\max_{w\geq r_\eta}[-G_\eta(w)],\qquad
 D_\eta=\tfrac12\min(A_\eta^2,B_\eta^2)>0.
 \tag{8}
\]

Then

\[
 \boxed{\limsup_{\lambda\downarrow0}\lambda^2
 \log\beta_S(p_{\eta,\lambda})\leq-D_\eta,\qquad
 \limsup_{\lambda\downarrow0}\lambda^2
 \log\alpha_S(p_{\eta,\lambda})\leq-D_\eta.}
 \tag{9}
\]

Both constants also have a lower bound
\(e^{-M_\eta^2/(2\lambda^2)}/(1+L_\eta/\lambda)^2\), where
\(M_\eta=\sup|G_\eta|\) and \(L_\eta=\sup|G_\eta'|<\infty\).
Thus their logarithmic scale is \(-\Theta_\eta(\lambda^{-2})\),
without an assertion of a sharp exponent.

For every \(\eta,\lambda\), centered S-invariant cutoff perturbations of
\(p_{\eta,\lambda}\) across \(|w|=r_\eta\) have nonzero changes of
predictor. The teacher risk is a nonconstant quadratic along each such
one-parameter perturbation. Thus the separating mode is visible to
prediction, unlike the S-odd mode in the original report.

## 2. Nearby laws and their predictors

Conditioned on \(w\), the law \(\rho_\eta\) has output distribution
\(N(\eta g(w),1)\), while its w marginal is \(\gamma\). Consequently

\[
 \frac{d\rho_\eta}{d\pi}(a,w)
 =\exp\{\eta a g(w)-\eta^2g(w)^2/2\}.
 \tag{10}
\]

Taking its logarithm and conditioning on \(w\) gives
\(\operatorname{KL}(\rho_\eta\Vert\pi)=\eta^2\mathbb E g(W)^2/2\).
Conditional variance one gives the second-moment formula in (6).
Oddness of g and symmetry of \((B,W)\) show S-invariance.
The conditional mean also gives \(f_{\rho_\eta}=\eta H\).

The Gaussian identity

\[
 \mathbb E e^{tW-W^2/2}=2^{-1/2}e^{t^2/4},\qquad t\in\mathbb C,
 \tag{11}
\]

follows by completing the square for real t and extending the absolutely
convergent integral, or by its power series. Use
\(g(W)=e^{-1/2}e^{-W^2/2}\sinh W\) and write the sine and hyperbolic
sine as exponentials in (11). The imaginary part is

\[
 H(x)=\frac1{\sqrt2}e^{-(1+x^2)/4}\sin(x/2).
 \tag{12}
\]

Fubini is justified by boundedness of g and the sine. In particular

\[
 \langle\sin,H\rangle_{L^2(\gamma)}
 =\mathbb E_W[g(W)\mathbb E_X\sin X\sin(WX)]=J.
 \tag{13}
\]

Pointwise Cauchy--Schwarz gives
\(|H(x)|^2\leq J\mathbb E_W\sin^2(Wx)\leq J\), so
\(\|H\|_{L^2(\gamma)}^2\leq J\). Expanding the half squared loss,

\[
 R(\rho_\eta)-R(\pi)
 =-\eta J+\tfrac12\eta^2\|H\|^2
 \leq-\eta(1-\eta/2)J<0.
 \tag{14}
\]

To evaluate J, use \(\sinh^2w=(\cosh(2w)-1)/2\) and
\(\mathbb E e^{-W^2+tW}=3^{-1/2}e^{t^2/6}\):

\[
 J=\frac{e^{-1}}{2\sqrt3}(e^{2/3}-1),
 \tag{15}
\]

which is the value in (6). In particular the KL and second moments in
(6) tend to their initialization values as \(\eta\downarrow0\).

## 3. Residual correlation and its unique positive zero

Put \(h(w)=\mathbb E_X H(X)\sin(wX)\). By (12), the product-to-sum
identity for the sines and
\(\mathbb E e^{-X^2/4}\cos(tX)=\sqrt{2/3}e^{-t^2/3}\) give

\[
 \begin{split}
 h(w)&=\frac{e^{-1/4}}{2\sqrt3}
 \left[e^{-(w-1/2)^2/3}-e^{-(w+1/2)^2/3}\right]\\
 &=\frac1{\sqrt3}e^{-(1+w^2)/3}\sinh(w/3).
 \end{split}
 \tag{16}
\]

Thus \(G_\eta=g-\eta h\), proving (7). For positive w, both g and h
are positive. The triple-angle identity gives their ratio as

\[
 Q(w):=\frac{h(w)}{g(w)}
 =\frac{e^{(1+w^2)/6}}{\sqrt3[1+2\cosh(2w/3)]}.
 \tag{17}
\]

We verify strict monotonicity, rather than only a tail sign change.
Logarithmic differentiation gives

\[
 (\log Q)'(w)
 =\frac{w[1+2\cosh(2w/3)]-4\sinh(2w/3)}
 {3[1+2\cosh(2w/3)]}.
 \tag{18}
\]

The numerator has the convergent power series

\[
 \frac w3+
 \sum_{n=1}^{\infty}
 \frac{2(2/3)^{2n}}{(2n)!}
 \left(1-\frac4{3(2n+1)}\right)w^{2n+1}.
 \tag{19}
\]

Every coefficient is positive. Hence Q is strictly increasing on
\((0,\infty)\). Moreover

\[
 Q(0+)=\frac{e^{1/6}}{3\sqrt3}<1,
 \qquad
 Q(w)\geq\frac{e^{(1+w^2)/6-2w/3}}{3\sqrt3}
 \longrightarrow\infty.
 \tag{20}
\]

For the first inequality, \(e^{1/6}\leq(1-1/6)^{-1}=6/5\), obtained
by comparing the exponential series with the geometric series. For the
second, use \(1+2\cosh z\leq3e^z\) for \(z\geq0\).
Since \(0<\eta\leq1\), continuity and strict monotonicity give one
and only one solution of \(\eta Q(w)=1\). This is \(r_\eta\).
The signs follow from \(G_\eta=g(1-\eta Q)\).

Both g and h tend to zero at infinity, so \(G_\eta\) does too.
Its positive lobe is nonempty and compactly bounded. Its negative lobe
has a strictly positive maximum of \(-G_\eta\): choose one point in
that lobe, then use decay at infinity to restrict its maximization to a
compact interval. This proves existence and positivity in (8).
Let \(M_\eta=\max(A_\eta,B_\eta)=\sup|G_\eta|\).

## 4. Symmetry-restricted exponential upper bound

The first variation of (1) at \(\rho_\eta\) is \(-aG_\eta(w)\).
This proves that (4) is its proximal law. Square completion gives

\[
 \begin{split}
 \nu_{\eta,\lambda}(dw)
 &=Z_{\eta,\lambda}^{-1}
     e^{G_\eta(w)^2/(2\lambda^2)}\gamma(dw),\\
 a\mid w&\sim N(G_\eta(w)/\lambda,1),\\
 Z_{\eta,\lambda}&=\int e^{G_\eta(w)^2/(2\lambda^2)}\gamma(dw)
 \leq e^{M_\eta^2/(2\lambda^2)}.
 \end{split}
 \tag{21}
\]

These laws are finite and S-invariant, since G is bounded and odd.
Write \(\gamma_+\) for the law of \(|W|\) when \(W\sim\gamma\).
The folded marginal \(q_{\eta,\lambda}\) has density
\(Z^{-1}e^{G_\eta(r)^2/(2\lambda^2)}\) relative to \(\gamma_+\).
Its normalization is the same Z by evenness.

Fix \(0<\delta<\min(A_\eta,B_\eta)/2\). There are compact intervals
\(I_+\subset(0,r_\eta)\), \(I_-\subset(r_\eta,\infty)\), of positive
\(\gamma_+\) masses \(c_+,c_-\), on which respectively
\(G_\eta\geq A_\eta-\delta\) and
\(-G_\eta\geq B_\eta-\delta\). Continuity at the zero permits a
fixed \(s>0\) small enough that \(s<r_\eta\), both intervals avoid
\([r_\eta-s,r_\eta+s]\), and
\(|G_\eta|\leq\delta\) throughout that strip.

Take the piecewise linear cutoff on the folded coordinate

\[
 v_s(r)=\begin{cases}
 1,&0\leq r\leq r_\eta-s,\\
 (r_\eta+s-r)/(2s),&|r-r_\eta|<s,\\
 0,&r\geq r_\eta+s.
 \end{cases}
 \tag{22}
\]

The full test \(u_s(a,w)=v_s(|w|)\) is S-invariant and Lipschitz;
it is constant near \(w=0\). The energy is bounded by

\[
 \int|\nabla u_s|^2\,dp_{\eta,\lambda}
 \leq\frac1{4s^2Z}e^{\delta^2/(2\lambda^2)}.
 \tag{23}
\]

For any real random variable U, its variance is
\(\tfrac12\mathbb E(U-U')^2\) for an independent copy U'. The two
ordered pairs of intervals \(I_+,I_-\) have values 1 and 0 under
the cutoff. Therefore

\[
 \begin{split}
 \operatorname{Var}_{p_{\eta,\lambda}}u_s
 &\geq q_{\eta,\lambda}(I_+)q_{\eta,\lambda}(I_-)\\
 &\geq\frac{c_+c_-}{Z^2}
 e^{[(A_\eta-\delta)^2+(B_\eta-\delta)^2]/(2\lambda^2)}.
 \end{split}
 \tag{24}
\]

It is essential to retain both interval masses: the smaller well can
have exponentially small mass. Dividing (23) by (24), then using (21),

\[
 \beta_S(p_{\eta,\lambda})
 \leq\frac1{4s^2c_+c_-}
 \exp\left\{\frac{M_\eta^2+\delta^2
 -(A_\eta-\delta)^2-(B_\eta-\delta)^2}{2\lambda^2}\right\}.
 \tag{25}
\]

Here s and the interval masses may depend on eta and delta but not on
lambda. Multiply the logarithm by \(\lambda^2\), take the upper limit
as lambda tends to zero, then let delta decrease to zero. Since
\(M_\eta^2=A_\eta^2+B_\eta^2-\min(A_\eta^2,B_\eta^2)\), this proves
the first inequality of (9).

For the second, apply the restricted LSI to \(1+\epsilon u\), where
u is a bounded, mean-zero, invariant test. Its entropy is
\(2\epsilon^2\operatorname{Var}_p u+o(\epsilon^2)\) and its energy
is \(\epsilon^2\int|\nabla u|^2dp\). Thus
\(\alpha_S\leq\beta_S\); approximation extends from bounded tests.
This proves the other inequality. Mollification of the cutoffs near
their two corners, with dominated convergence, also permits smooth
tests throughout the Rayleigh quotient argument.

For completeness, the comparison lower bound survives for this residual.
Let \(\mu=\gamma(db)\otimes\nu_{\eta,\lambda}(dw)\). Its density
relative to \(\gamma\otimes\gamma\) has supremum-to-infimum ratio at
most \(e^{M_\eta^2/(2\lambda^2)}\). To verify the entropy comparison,
write \(\Psi(k,c)=k\log(k/c)-k+c\geq0\), and use
\(\operatorname{Ent}_\mu(k)=\inf_{c>0}\int\Psi(k,c)d\mu\).
If a density relative to a reference measure lies between m and B,
this formula bounds its entropy by B times the reference entropy;
the gradient energy for the reference measure is at most \(1/m\)
times its own energy. The standard two-dimensional Gaussian LSI,
whose constant is one in the convention above, therefore gives the
LSI constant \(e^{-M_\eta^2/(2\lambda^2)}\) for \(\mu\).

The map \(T(b,w)=(b+G_\eta(w)/\lambda,w)\) pushes \(\mu\) to
\(p_{\eta,\lambda}\) by (21), and its derivative has operator norm
at most \(1+L_\eta/\lambda\). The chain rule applied to a test
composed with T proves the unrestricted LSI lower bound
\(e^{-M_\eta^2/(2\lambda^2)}/(1+L_\eta/\lambda)^2\).
Restricting the test class can only increase the best constant;
the restricted gap is at least the restricted LSI constant as already
proved. This yields the stated lower bounds for both. Boundedness of
\(G_\eta'\) follows directly from the two Gaussian formulas in (7).

## 5. The cutoff changes predictions

Fix eta, lambda, and any cutoff (22). Put
\(m=\int u_s\,dp_{\eta,\lambda}\), so \(0<m<1\). For \(|t|<1\),

\[
 dp_t=(1+t(u_s-m))\,dp_{\eta,\lambda}
 \tag{26}
\]

defines positive, normalized, S-invariant probability laws. The multiplier
is bounded, so all their second moments and risks are finite. Conditioning
on w in (21) shows

\[
 f_{p_t}(x)-f_{p_{\eta,\lambda}}(x)=t V(x),\qquad
 V(x)=\frac1\lambda\int G_\eta(w)
 [v_s(|w|)-m]\sin(wx)\,\nu_{\eta,\lambda}(dw).
 \tag{27}
\]

The signed finite measure

\[
 d\zeta(w)=G_\eta(w)[v_s(|w|)-m]\nu_{\eta,\lambda}(dw)
 \tag{28}
\]

is odd and nonzero. To see the latter, use any open interval inside
\((0,r_\eta-s)\): there \(G_\eta\) is strictly positive,
the cutoff is 1, \(1-m>0\), and the marginal has positive
density. If V vanished identically, its sine-transform representation
in (27) and oddness would give \(\int e^{ixw}d\zeta(w)=0\) for every x;
the cosine transform vanishes by parity.

Here is a direct justification that this forces \(\zeta=0\). For any
\(\tau>0\), the Fourier representation of the Gaussian density gives

\[
 \varphi_\tau(y-w)=\frac1{2\pi}\int_{\mathbb R}
 e^{-\tau^2x^2/2}e^{ix(y-w)}dx.
 \tag{29}
\]

Integrating against the finite measure and using Fubini makes
\(\varphi_\tau*\zeta\) identically zero. For any continuous compactly
supported test j, integrate that convolution against j and then let
\(\tau\downarrow0\). Gaussian convolution tends uniformly to j, by
uniform continuity and its vanishing tails, and finite total variation
permits the limit inside the measure integral. Hence \(\int j\,d\zeta=0\)
for every such j, forcing the measure to be zero, a contradiction.

It follows that V is not identically zero. It is bounded and continuous
by dominated convergence in (27), so \(\|V\|_{L^2(\gamma)}>0\), since
the Gaussian input measure gives positive mass to every open interval.
Expanding the risk along (26),

\[
 R(p_t)=R(p_{\eta,\lambda})
 +t\langle f_{p_{\eta,\lambda}}-\sin,V\rangle
 +\tfrac12t^2\|V\|^2.
 \tag{30}
\]

The positive quadratic coefficient proves nonconstancy. For each
\(0<t<1\), at least one of \(R(p_t),R(p_{-t})\) differs from
\(R(p_{\eta,\lambda})\), because their sum minus twice that risk is
\(t^2\|V\|^2>0\). All these perturbations are already S-invariant;
symmetrization leaves them as they are.

## 6. Scope

At eta zero, the earlier theorem gives a polynomial lower bound on the
restricted proximal gap. For every fixed eta in \((0,1]\), (9) gives
an exponential upper bound with a positive, eta-dependent exponent.
Consequently no fixed positive-KL neighborhood of pi admits a bound
\(\beta_S(p_{\rho,\lambda})\geq c\lambda^k\), uniformly over that
neighborhood and all sufficiently small lambda, for any fixed \(c,k>0\).
This remains false if the neighborhood is restricted to S-invariant laws
with risk strictly below \(R(\pi)\) and uniformly bounded second moments.
The same conclusion applies to a restricted LSI bound.

The limits in eta and lambda are not interchangeable. No positive lower
bound on \(D_\eta\) uniform as eta tends to zero is claimed. The result
also does not show that the nonlinear trajectory enters these laws, that
the bottleneck persists under its evolving drift, or that it obstructs
reaching a prescribed teacher risk. Predictor visibility alone supplies
none of these missing assertions. The polynomial-versus-exponential
unregularized-risk runtime question remains unresolved.
