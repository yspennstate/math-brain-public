# Measurable drift for unbounded diffusion and L2 initial data

Let \(\mathbb T=\mathbb R/\mathbb Z\) have mass one and put
\(H=L^2(\mathbb T;\mathbb R)\), \(S_t=\exp(t\Delta)\).
Fix a finite horizon \(T>0\), a deterministic \(h\in H\), and
\(0<\beta<1\). Suppose

\[
 |g(z)-g(y)|\le L|z-y|^\beta,\qquad |g(z)|\ge c>0.                 \tag{1}
\]

There is no upper bound on \(g\). Let
\(b:[0,T]\times\mathbb T\times\mathbb R\to\mathbb R\) be Borel with

\[
 |b(t,x,z)|\le B(1+|z|).                                      \tag{2}
\]

For \(v\in H\), write \(b_t(v)(x)=b(t,x,v(x))\). A solution below is
an adapted continuous \(H\)-valued weak mild solution driven by cylindrical
Brownian motion \(W\) on \(H\):

\[
 U_t=S_th+\int_0^t S_{t-s}b_s(U_s)\,ds
             +\int_0^t S_{t-s}M_{g(U_s)}\,dW_s.                \tag{3}
\]

Multiplication by an unbounded spatial function is understood before heat
smoothing; no bounded multiplication operator on \(H\) is assumed.
All laws are state-path laws on \(\mathcal X=C([0,T];H)\).

The input from the previous session is:

**(D)** The drift-free equation with coefficient \(g\), from every
deterministic \(h\in H\), has a weak mild solution with continuous
\(H\) paths and a unique state-path law \(\mu_0\).

The previous proof derives (D) from bounded-start uniqueness by scalar
comparison of Lipschitz approximations. Its external uniqueness input is
Yi Han, *Weak uniqueness for the stochastic heat equation with
nondegenerate diffusion: the full Hölder regime*,
[arXiv:2611.07310v1, Proposition 8.1](https://arxiv.org/html/2611.07310v1).
That external theorem's main argument is not proved here.

**Theorem.** Assume (1), (2), and (D). Equation (3) has a weak solution
and a unique state-path law \(\mu_b\). The laws \(\mu_b\) and \(\mu_0\)
are equivalent. There is a Borel function \(J:\mathcal X\to\mathbb R\)
such that

\[
 \frac{d\mu_b}{d\mu_0}(\omega)
     =D(\omega):=\exp\{J(\omega)-A(\omega)/2\},\qquad
 A(\omega)=\int_0^T\left\|\frac{b_s(\omega_s)}{g(\omega_s)}
                    \right\|_2^2\,ds.                       \tag{4}
\]

The two relative entropies are finite and satisfy

\[
 \operatorname{Ent}(\mu_b\mid\mu_0)=\tfrac12 E_{\mu_b}A,
 \qquad
 \operatorname{Ent}(\mu_0\mid\mu_b)=\tfrac12 E_{\mu_0}A.         \tag{5}
\]

In particular each is at most

\[
 c^{-2}B^2T\,C_T(1+\|h\|_2^2),                               \tag{6}
\]

where one permissible explicit constant is

\[
 \begin{split}
 G&=|g(0)|+L,\\
 a_1&=6(TB^2+G^2),\qquad a_2=6G^2/\sqrt{8\pi},\\
 \lambda&=1+4a_1+16\pi a_2^2,\qquad C_T=6e^{\lambda T}.
 \end{split}                                                 \tag{7}
\]

The extension beyond the previous session is the inclusion of (2) for
unbounded diffusion and arbitrary \(L^2\) initial data. The Girsanov
transfer method itself is already in Han's Section 8.2, Proposition 8.5.
The proof below supplies its estimates and the state-law identification
for this initial-data class. Formula (5) also checks the density's sign
and normalization quantitatively.

## 1. Check of the drift-free input

Here is the independently checked mechanism behind the previous proof.
Mollify \(g\) to globally Lipschitz \(g_n\) with
\(\|g_n-g\|_\infty\le Ln^{-\beta}\) and uniform sublinear growth.
For bounded \(v,w\), couple their approximating solutions between the
solutions started from \(v\wedge w\) and \(v\vee w\), using common noise.
Classical scalar comparison gives a nonnegative enclosing gap \(D_n(t)\).
Testing its weak equation against the constant function \(1\) gives

\[
 E\|D_n(t)\|_1=E\int D_n(t,x)\,dx
     =\int[(v\vee w)-(v\wedge w)]\,dx=\|v-w\|_1.              \tag{8}
\]

The mass martingale is a true martingale: its bracket has expectation
at most \(2\int_0^T E(\|g_n(U_s^+)\|_2^2+
\|g_n(U_s^-)\|_2^2)ds<\infty\), by the uniform moment bounds.
Thus
\(E\|U_n^v(t)-U_n^w(t)\|_1\le\|v-w\|_1\).
For constant diffusion and constant positive displacement, equality holds.
The constant one and the use of absolute initial mass therefore check.

The approximation limit does not assume pathwise uniqueness for \(g\).
Uniform moment bounds and heat factorization make the marginal laws tight
in \(C([0,T];H)\). Under a Skorokhod representation, uniform \(H\) path
convergence yields

\[
 \|g_n(U_n)-g(U)\|_2
 \le Ln^{-\beta}+L\|U_n-U\|_2^\beta\longrightarrow0.            \tag{9}
\]

The inequality \(\|a^2-d^2\|_1\le(\|a\|_2+\|d\|_2)\|a-d\|_2\)
then identifies brackets. Higher moment bounds allow passage in the
martingale and product-minus-bracket identities. Bounded-start uniqueness
identifies each marginal limit. Only marginal identification is needed
when passing (8) to bounded \(L^1\)-Lipschitz observables.

For any rough-start solution, the prior estimates give
\(U_\delta\in L^\infty\) at positive times and
\(E\|U_\delta-S_\delta h\|_2^2\le C\sqrt\delta\).
The factorization inequalities are
\(2\eta+(1+\beta)/2<1\) and \(\eta>3/(2p)\), compatible for every
\(\beta<1\). Restart at \(\delta\), apply (8), and compare to
\(S_\delta h\). The error for a bounded \(L^1\)-Lipschitz test is
at most its Lipschitz constant times \(C^{1/2}\delta^{1/4}\).
Real and imaginary parts of Fourier characteristic functions are such
tests and determine \(H\)-valued laws. Restart then determines all
positive-time joint laws and continuous path laws. This verifies the
previous extension mechanism; the complete comparison and compactness
proof remains in the read-only previous PROOF.md.

## 2. Measurability and energy

All coefficient expressions below are defined on \(L^2\) equivalence
classes. One explicit jointly Borel representative of \(v\in H\) is the
finite limit of \(S_{1/n}v(x)\) when it exists, with value zero otherwise.
Heat approximation at Lebesgue points shows that this equals \(v(x)\)
for almost every \(x\). The maps \((v,x)\mapsto S_{1/n}v(x)\) are Borel.
Composition with \(b\), followed by integration against a countable
orthonormal basis, shows that \((t,v)\mapsto b_t(v)\) is Borel into \(H\).
Indeed all its scalar coordinates are Borel by measurable integration;
coordinates generate the Borel sigma field of separable \(H\), and
(2) ensures that the image lies in \(H\).

The same argument applies to quotients by \(g\) or \(g^2\). A continuous
adapted \(H\)-valued process is predictable. Composing the predictable
map \((t,\omega)\mapsto(t,U_t(\omega))\) with these Borel maps gives
predictable coefficient processes. For their spatial representatives,
the same construction gives joint predictability in \((t,\omega)\)
and measurability in \(x\).

Since \(|z|^\beta\le1+|z|\),

\[
 |g(z)|\le G(1+|z|),\quad
 \|g(v)\|_2^2\le2G^2(1+\|v\|_2^2),\quad
 \|b_t(v)\|_2^2\le2B^2(1+\|v\|_2^2).                         \tag{10}
\]

Define the noise direction \(\theta_t(v)=b_t(v)/g(v)\). Ellipticity gives

\[
 \|\theta_t(v)\|_2^2\le 2c^{-2}B^2(1+\|v\|_2^2).              \tag{11}
\]

For every \(\omega\in\mathcal X\), continuity makes
\(\sup_{t\le T}\|\omega_t\|_2<\infty\), so \(A(\omega)<\infty\).
Measurable integration shows that \(A\) is Borel. No spatial bound on
\(h\) or \(\omega_t\) is used in this step.

## 3. A moment bound uniform under stopped changes of measure

Consider any continuous-\(H\) mild solution with drift
\(\kappa_s b_s(U_s)\), where \(\kappa\) is predictable and
\(0\le\kappa_s\le1\). Its driving cylindrical Brownian motion may live
under any probability measure. We prove

\[
 \sup_{t\le T} E(1+\|U_t\|_2^2)
       \le C_T(1+\|h\|_2^2),                                \tag{12}
\]

with (7), independently of \(\kappa\) and the probability space.

First the precise heat bound is

\[
 \|S_rM_k\|_{\mathrm{HS}}^2=p_{2r}(0)\|k\|_2^2,
 \qquad p_{2r}(0)\le1+(8\pi r)^{-1/2}.                        \tag{13}
\]

For the identity integrate \(p_r(x-y)^2\) over \(x\), then \(y\).
For the bound use the real Fourier expansion
\(p_{2r}(0)=1+2\sum_{j\ge1}e^{-8\pi^2j^2r}\).
A decreasing nonnegative function obeys
\(\sum_{j\ge1}f(j)\le\int_0^\infty f(y)dy\); the Gaussian integral
is \(1/\sqrt{8\pi r}\) after multiplying by two.

Moment estimates must first be localized. For \(R>\|h\|_2\), let
\(\sigma_R=\inf\{t:\|U_t\|_2\ge R\}\) and set, on the entire
interval \([0,T]\),

\[
 U_t^{[R]}=S_th+\int_0^t1_{s\le\sigma_R}S_{t-s}\kappa_s b_s(U_s)ds
       +\int_0^t1_{s\le\sigma_R}S_{t-s}M_{g(U_s)}dW_s.         \tag{14}
\]

Before the stop this equals \(U\). The integrands have bounded \(H\)
norm after localization. In particular
\(1_{s\le\sigma_R}(1+\|U_s\|_2^2)\le1+\|U_s^{[R]}\|_2^2\).
We stop integrands rather than assert a mild equation for
\(U_{t\wedge\sigma_R}\).

Let \(F_R(t)=E\|U_t^{[R]}\|_2^2\). Heat contraction, Cauchy--Schwarz
for the drift integral, stochastic isometry, (10), and (13) give

\[
 F_R(t)\le3\|h\|_2^2
  +6TB^2\int_0^t(1+F_R(s))ds
  +6G^2\int_0^t[1+(8\pi(t-s))^{-1/2}](1+F_R(s))ds.           \tag{15}
\]

Every term is finite and uniformly bounded in \(t\) for each fixed
\(R\), before any absorption. Setting \(Y_R=1+F_R\), this reads

\[
 Y_R(t)\le1+3\|h\|_2^2
  +\int_0^t[a_1+a_2(t-s)^{-1/2}]Y_R(s)ds.                    \tag{16}
\]

Put \(N_R=\sup_{t\le T}e^{-\lambda t}Y_R(t)<\infty\). Multiplying
(16) by \(e^{-\lambda t}\), and enlarging the kernel integral to
\((0,\infty)\), yields

\[
 N_R\le1+3\|h\|_2^2+
       [a_1/\lambda+a_2\sqrt\pi/\sqrt\lambda]N_R.              \tag{17}
\]

The definition in (7) gives \(\lambda\ge4a_1\) and
\(\lambda\ge16\pi a_2^2\), so the coefficient is at most \(1/2\).
Hence \(Y_R(t)\le2(1+3\|h\|_2^2)e^{\lambda T}
\le C_T(1+\|h\|_2^2)\). Continuous paths are bounded in \(H\) on
\([0,T]\), so eventually \(\sigma_R>T\) on each path. Fatou's lemma
proves (12). Integrating (11) consequently gives

\[
 E A(U)\le K_T(1+\|h\|_2^2),\qquad
 K_T=2c^{-2}B^2T C_T.                                       \tag{18}
\]

This estimate holds for every multiplier \(\kappa\in[0,1]\).

## 4. Removing the energy stops

We use the usual cylindrical Girsanov theorem for a predictable direction
\(\theta\in L^2([0,T];H)\). The following argument checks that its full
stochastic exponential has expectation one, without an exponential-moment
assumption on \(U\).

Write \(A_t=\int_0^t\|\theta_s\|_2^2ds\), assume \(A_T<\infty\)
almost surely, and let

\[
 R_t=\exp\{\int_0^t\langle\theta_s,dW_s\rangle-A_t/2\},\quad
 \tau_n=\inf\{t:A_t\ge n\},\quad
 dQ_n=R_{T\wedge\tau_n}\,dP.                                 \tag{19}
\]

At the stop the bracket is at most \(n\). Novikov therefore applies
to the stopped exponential, whose expectation is one. Suppose
\(E_{Q_n}A_T\le K\) uniformly in \(n\). On \(\{A_T<n\}\), the
stopped and full exponentials agree. The full exponential is a
nonnegative local martingale, hence a supermartingale. Therefore

\[
 1\ge E_PR_T\ge E_P[R_T1_{A_T<n}]
       =Q_n(A_T<n)\ge1-K/n.                                 \tag{20}
\]

Letting \(n\to\infty\) proves \(E_PR_T=1\). The supermartingale
inequalities then imply constant expectation at every time. For \(s<t\)
the nonnegative variable \(R_s-E[R_t\mid\mathcal F_s]\) has zero
expectation, so it vanishes. Thus \(R\) is a martingale. The full
Girsanov change is justified. Since \(A_T<\infty\), its terminal
density is finite and strictly positive.

There is a second integrability check. Under \(Q_n\), put
\(W^n=W-\int_0^{\cdot\wedge\tau_n}\theta_sds\). Then

\[
 E_P[R_{T\wedge\tau_n}\log R_{T\wedge\tau_n}]
       =\tfrac12 E_{Q_n} A_{T\wedge\tau_n}\le K/2.             \tag{21}
\]

The stochastic integral against \(W^n\) has mean zero since its
bracket is at most \(n\). Because \(x\log x\ge-1/e\), (21) bounds
the positive part uniformly. The bound
\(x1_{x>M}\le (x\log x)^+/\log M\), for \(M>1\), proves uniform
integrability of the stopped densities. Their almost sure convergence
to \(R_T\) gives the same normalization independently of (20).

Direct use of Novikov without stopping is not available under the
hypotheses. Take \(g\equiv1\), \(h=0\), and \(b(z)=kz\). Under the
drift-free law the spatial mass \(Z_s=\langle X_s,1\rangle\) is standard
Brownian motion. Therefore

\[
 A=k^2\int_0^T\|X_s\|_2^2ds
       \ge k^2\int_0^T Z_s^2ds
       \ge\frac{k^2}{T}\left(\int_0^T Z_sds\right)^2.          \tag{21a}
\]

The first inequality uses \(\|1\|_2=1\), and the second is
Cauchy--Schwarz in time. The centered Gaussian
\(Y=\int_0^T Z_sds=\int_0^T(T-r)dZ_r\) has variance
\(\int_0^T(T-r)^2dr=T^3/3\). Independently its covariance formula
gives \(\int_0^T\int_0^T\min(s,t)dsdt=T^3/3\).
For a centered Gaussian of variance \(v>0\), direct integration of its
density shows \(E e^{aY^2}=\infty\) when \(2av\ge1\).
Consequently \(E_{\mu_0}e^{A/2}=\infty\) whenever \(k^2T^2\ge3\).
This is a sufficient divergence condition, not a sharp threshold.
It does not contradict Section 4: normalization follows from changed-
measure second moments, even when the usual sufficient Novikov condition
fails for the full exponential.

## 5. Existence with drift and drift removal

Take a drift-free solution \((X,W)\) with law \(\mu_0\) under \(P\).
Use (19) with \(\theta_s=\theta_s(X_s)\). Under \(Q_n\), Girsanov
makes \(W^n=W-\int_0^{\cdot\wedge\tau_n}\theta_s(X_s)ds\)
cylindrical Brownian motion. The weak equation for \(X\) becomes

\[
 dX=\Delta X\,dt+1_{t\le\tau_n}b_t(X_t)dt+M_{g(X_t)}dW^n_t.  \tag{22}
\]

This follows first for smooth tests from \(g\theta=b\). To obtain
the mild form without assuming moments in advance, localize at the
first \(H\)-norm hit of \(R\). The localized coefficients have bounded
\(H\) norm, and (13) makes stochastic Fubini and variation of constants
valid. Letting \(R\) increase gives the mild identity, because continuous
\(H\) paths have bounded norm on this horizon. The drift belongs to
\(L^1([0,T];H)\) pathwise. Section 3 now applies to that mild equation.
Since the multiplier in (22) belongs to
\([0,1]\), (18) yields \(\sup_nE_{Q_n}A_T\le K_T(1+\|h\|_2^2)\).
Section 4 proves that \(R_T\) has expectation one. Under
\(dQ=R_TdP\),
\(W^b=W-\int_0^\cdot\theta_s(X_s)ds\) is Brownian and \(X\)
solves (3). This proves weak existence. The two underlying measures
are equivalent, so their state laws are equivalent as well.

Now take any drifted solution \((U,W)\) under a probability \(P\).
Use the reverse exponential

\[
 \widehat R_t=\exp\{-\int_0^t\langle\theta_s(U_s),dW_s\rangle
                              -A_t(U)/2\}.                  \tag{23}
\]

Under its stopped measure, \(W+\int_0^{\cdot\wedge\tau_n}\theta_sds\)
is Brownian and the drift of \(U\) is
\(1_{s>\tau_n}b_s(U_s)\). This multiplier also lies in \([0,1]\),
so (18) applies under every stopped reverse measure. Section 4, now
with direction \(-\theta\), proves \(E_P\widehat R_T=1\).
Under \(d\widehat Q=\widehat R_TdP\),

\[
 \widehat W=W+\int_0^\cdot\theta_s(U_s)ds                     \tag{24}
\]

is Brownian and \(U\) is drift-free. By (D), its state law under
\(\widehat Q\) is \(\mu_0\).

This alone does not identify the original law under \(P\). The next
section checks that the inverse density is a function of the state path,
using no uniqueness assumption for the joint state and noise.

## 6. A density determined by the state path

On canonical space with law \(\mu_0\), let \(X_t(\omega)=\omega_t\).
For real smooth periodic \(\varphi\), define the Borel path function

\[
 M_t(\varphi)=\langle X_t-h,\varphi\rangle
                     -\int_0^t\langle X_s,\Delta\varphi\rangle ds.
                                                                    \tag{25}
\]

These are continuous square-integrable martingales in the natural state
filtration. This follows from any drift-free realization by conditioning
its martingale identities on the state history. Their brackets are

\[
 [M(\varphi),M(\psi)]_t
       =\int_0^t\!\int_{\mathbb T}g(X_s(x))^2\varphi(x)\psi(x)dxds.
                                                                    \tag{26}
\]

For bounded canonical \(\mathcal F_r\)-measurable Borel \(\eta\),
form the predictable elementary spatial functions
\(v(s,x)=\eta1_{(r,t]}(s)\varphi(x)\) and finite sums of these.
Define their integrals as Borel functions of the path by

\[
 I(v)=\eta[M_t(\varphi)-M_r(\varphi)],                         \tag{27}
\]

and extend linearly. The bracket formula gives the isometry

\[
 E_{\mu_0}|I(v)-I(w)|^2
    =E_{\mu_0}\int_0^T\!\int g(X_s)^2|v-w|^2 dxds.            \tag{28}
\]

For clarity, density in this norm does not require a bound on \(g\).
The measure \(dm=g(X_s(x))^2d\mu_0dsdx\) is finite, by (10), (12).
Predictable rectangles \(A\times(r,t]\), \(A\in\mathcal F_r\),
together with spatial Borel sets generate the relevant product sigma
field (time zero has zero measure). Their finite linear combinations
are dense in \(L^2(m)\) by the monotone-class theorem. For any such
predictable rectangle, its induced finite measure in \(x\) is a Borel
measure on the compact torus. Continuous functions are dense in its
\(L^2\), and smooth periodic functions are uniformly dense in continuous
functions. Thus smooth spatial factors in (27) suffice. Completion of
the filtration adds only null sets and does not change this density.
Coefficients can first be clipped to be bounded.

The target predictable integrand is

\[
 q_s(X)(x)=\frac{b(s,x,X_s(x))}{g(X_s(x))^2}.                  \tag{29}
\]

Its squared norm in (28) is exactly \(E_{\mu_0}A<\infty\),
since \(gq=\theta\). Choose elementary \(v_m\) converging to
\(q\) in that weighted norm. Then \(I(v_m)\) converges in
\(L^2(\mu_0)\). Take a subsequence that also converges
\(\mu_0\)-almost surely and define \(J\) as its finite pointwise
limit, with value zero off the Borel convergence set. This defines a
Borel real function on all of \(\mathcal X\).

On any drift-free realization with state law \(\mu_0\), the same
path functions satisfy
\(I(v_m)(X)=\int_0^T\langle g(X_s)v_m(s),dW_s\rangle\).
The weighted approximation and stochastic isometry make these converge
in \(L^2\) to \(\int\langle\theta_s(X_s),dW_s\rangle\).
The chosen subsequence also converges almost surely to \(J(X)\),
because its state law is \(\mu_0\). Uniqueness of limits in probability
gives the realization-independent identity

\[
 J(X)=\int_0^T\langle\theta_s(X_s),dW_s\rangle.                \tag{30}
\]

Consequently the forward density in Section 5 is exactly \(D(X)\)
from (4), and \(\int Dd\mu_0=1\).

For an arbitrary drifted solution, use \(\widehat Q,\widehat W\)
from (23)--(24). Under \(\widehat Q\), (30) gives
\(J(U)=\int\langle\theta_s(U_s),d\widehat W_s\rangle\).
Substitution of \(dW=d\widehat W-\theta ds\) into (23) yields

\[
 \widehat R_T^{-1}
   =\exp\{\int_0^T\langle\theta_s(U_s),d\widehat W_s\rangle
                                              -A(U)/2\}
   =D(U).                                                    \tag{31}
\]

The substitution holds up to each energy stop and then on the entire
horizon, since \(A(U)<\infty\). For bounded Borel \(F:\mathcal X\to\mathbb R\),

\[
 E_PF(U)=E_{\widehat Q}[F(U)\widehat R_T^{-1}]
              =\int F(\omega)D(\omega)\mu_0(d\omega).         \tag{32}
\]

This identifies every drifted state-path law as \(D\mu_0\), proving
uniqueness. Since \(D\) is positive and finite \(\mu_0\)-almost surely,
the two path laws are mutually absolutely continuous.

## 7. Entropy and sign checks

Under \(\mu_0\), (30) is a square-integrable mean-zero integral.
By (18), \(A\) is integrable. Thus \(\log D=J-A/2\) is integrable,
and

\[
 E_{\mu_0}\log(1/D)=\tfrac12E_{\mu_0}A.                       \tag{33}
\]

Under a drifted realization with law \(\mu_b\), equivalence of measures
and (24), (30) imply

\[
 J(U)=\int_0^T\langle\theta_s(U_s),dW_s\rangle+A(U).           \tag{34}
\]

One can verify this change of integrator first at finite energy stops.
Stochastic integrals are limits in probability of predictable elementary
integrals; equivalent measures preserve convergence in probability.
Their finite-variation correction is \(\int\|\theta\|_2^2ds=A\).
This proves (34) without assuming a joint-law uniqueness theorem.

The stochastic integral in (34) is square integrable by (18), so has
mean zero under the drifted probability. Hence

\[
 E_{\mu_b}\log D=\tfrac12E_{\mu_b}A.                          \tag{35}
\]

Equations (33), (35) are precisely (5), with the definition
\(\operatorname{Ent}(\nu\mid\mu)=\int\log(d\nu/d\mu)d\nu\).
The bound (6) follows by halving (18) under each law.

For a direct normalization and sign check, take \(g\equiv\sigma\ne0\)
and \(b\equiv d\). The spatial mass under the drift-free law satisfies
\(\langle X_T-h,1\rangle=\sigma W_T(1)\). Then

\[
 J=\frac{d}{\sigma^2}\langle X_T-h,1\rangle,
 \quad A=\frac{d^2T}{\sigma^2},\quad
 D=\exp\{\tfrac d\sigma W_T(1)-\tfrac{d^2T}{2\sigma^2}\}.    \tag{36}
\]

The exponential tilts the mass mean upward by \(dT\), as required by
(3), and each entropy is \(d^2T/(2\sigma^2)\). This independently
checks the sign and factor \(1/2\) in (4), (5), and (31).

## 8. Scope and remaining questions

No exponential moment of \(\|U\|_2^2\) is needed: stopped changes of
measure have a uniform second-moment estimate and hence controlled energy.
No uniform spatial bound on initial data or on diffusion enters (10)--(35).
The only inverse coefficient bounds used are \(1/|g|\le1/c\) and
\(1/g^2\le1/c^2\). The sign of \(g\) is immaterial.

A merely Borel drift, including a discontinuous function of the state, is
covered. No contraction or order property for the drifted equation is
claimed; order was used only for the drift-free input in the previous
session. In particular no pathwise uniqueness conclusion follows.

The unbounded, globally Hölder example
\(g(z)=1+|z|^\beta\), together with
\(h(x)=\operatorname{dist}(x,0)^{-a}\) near zero, \(0<a<1/2\),
and \(b(t,x,z)=z+1_{z\ge0}\), satisfies all assumptions. The value of
\(h\) at zero can be assigned arbitrarily. This tests simultaneously
unbounded diffusion, unbounded initial spatial norm, and discontinuous
linear-growth drift. Here \(h\in H\), \(g\ge1\),
\([g]_\beta\le1\), and \(|b|\le1+|z|\).

If ellipticity is removed, (11) and (29) can fail, as can the drift-free
uniqueness input. Nothing here applies to the degenerate nonuniqueness
examples. The endpoint \(\beta=0\) is not treated. A scalar globally
Lipschitz elliptic coefficient can be handled by the same transfer, using
the classical drift-free theory instead of (D).

The conclusion remains conditional on the bounded-start uniqueness theorem
used to obtain (D); it is not an independent proof of the main
full-positive-Hölder uniqueness result. The next unresolved direction after
this extension is to audit that theorem's core cancellation estimates or
to obtain an initial-data modulus for drifted laws. The latter does not
follow from mere equivalence of measures or from the drift-free L1 bound.
