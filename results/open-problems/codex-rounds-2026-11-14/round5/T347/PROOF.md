# An iid exclusion cap from unstable pattern fields

Let the entries of the N-by-M matrix X be independent uniform signs,
where M=M_N and M/N tends to a fixed alpha>0. Write xi^mu for its columns,
and let

\[
 H(\sigma)=-\frac{1}{2N}\|X^\mathsf T\sigma\|_2^2,
 \qquad J=\frac{XX^\mathsf T}{N}-\frac{M}{N}I.
\]

Thus J has zero diagonal. A single-spin local minimum, with ties allowed,
is precisely a configuration satisfying

\[
 \sigma_i(J\sigma)_i\ge0\quad(1\le i\le N),                 \tag{1}
\]

since the energy cost of flipping i is 2 sigma_i(J sigma)_i.
All distances below are Hamming distances. Define

\[
 L_\alpha=8(1+\alpha)\log9-\alpha,\qquad
 p_\alpha(t)=\Phi\left(-\frac{1+t}{\sqrt\alpha}\right),
 \qquad
 R_\alpha(t)=\frac{t^2p_\alpha(t)}{t^2+4L_\alpha^2},         \tag{2}
\]

where Phi is the standard normal distribution function.

**Theorem.** For every alpha>0, t>0 and 0<=delta<R_alpha(t), and
for any deterministic choice of a stored-pattern label mu=mu_N,

\[
 \mathbb P\{\exists\text{ a single-spin local minimum }\sigma:
                  d(\sigma,\xi^\mu)\le\lfloor\delta N\rfloor\}
 \longrightarrow0.                                      \tag{3}
\]

Moreover, if B_N is the fraction of stored patterns having such a nearby
minimum, then B_N tends to zero in probability. In particular, the
probability that every pattern has such a minimum tends to zero.
At alpha=1/7 the fixed choice delta=10^{-8} satisfies (3).

The bound is small and is not an estimate of the AGS capacity. It proves
an iid obstruction absent from the correlated constructions in the
earlier reports. At every positive extensive load, overlap tending to
one is impossible for a specified pattern, and for all but a fraction
tending to zero of the patterns. A retrieval statement using a fixed,
larger error tolerance is a different question.

## 1. A deterministic stability inequality

Let J be any symmetric zero-diagonal matrix, let x be a sign vector,
and suppose ||J||_op<=L. For t>0 set

\[
 U_t(x)=\{i:x_i(Jx)_i\le-t\},\qquad b_t=|U_t(x)|/N.
\]

If sigma satisfies (1), put D={i:sigma_i!=x_i} and d=|D|. For every
i in U_t(x) outside D, stability and sigma_i=x_i give

\[
 x_i\big(J(\sigma-x)\big)_i
 =x_i(J\sigma)_i-x_i(Jx)_i\ge t.
\]

There are at least (|U_t(x)|-d)_+ such sites. Since ||sigma-x||_2^2=4d,

\[
 t^2(|U_t(x)|-d)_+
 \le\|J(\sigma-x)\|_2^2\le4L^2d.                          \tag{4}
\]

If d<|U_t(x)|, rearrangement gives

\[
 \frac dN\ge\frac{b_t t^2}{t^2+4L^2}.                    \tag{5}
\]

If d>=|U_t(x)|, the same conclusion follows because the right side is
at most b_t. This proves (5) for every local minimum simultaneously,
without a union bound over configurations. It applies to non-strict
minima as well as strict ones. A direct derivation of (4) is to square
the required field corrections at the unchanged unstable sites, then
sum them; errors at changed sites are discarded, not assumed stable
relative to x.

## 2. An elementary matrix norm bound

For every r>0,

\[
 \mathbb P\left\{\|X\|_{\mathrm{op}}^2>
                  8\big((N+M)\log9+r\big)\right\}
 \le2e^{-r}.                                             \tag{6}
\]

Here is a proof with its constant. In dimension d the unit sphere has a
1/4-net with at most 9^d points. Indeed, take a maximal 1/4-separated
subset. The disjoint open balls of radius 1/8 around it lie inside the
ball of radius 9/8. Comparing volumes bounds its size by 9^d; maximality
gives the covering property. Compactness, or this same packing bound,
ensures that a finite maximal set exists.

Take these nets in dimensions N and M. For any fixed unit vectors u,v,
independence and cosh(w)<=exp(w^2/2) give

\[
 \mathbb E e^{s u^\mathsf TXv}
 =\prod_{i,\nu}\cosh(su_iv_\nu)
 \le\exp\left(\frac{s^2}{2}\sum_{i,\nu}u_i^2v_\nu^2\right)
 =e^{s^2/2}.
\]

The cosh inequality follows by integrating tanh(w)<=w for w>=0
and using evenness. Exponential Markov with s=a and s=-a gives
P(|u^T Xv|>a)<=2exp(-a^2/2).

Approximate maximizing unit vectors by net points u_0,v_0. The identity

\[
 u^\mathsf TXv-u_0^\mathsf TXv_0
 =(u-u_0)^\mathsf TXv+u_0^\mathsf TX(v-v_0)
\]

bounds the difference by ||X||_op/2. Thus ||X||_op is at most twice the
largest absolute bilinear form on the two nets. A union bound over at
most 9^{N+M} pairs with a^2=2((N+M)log9+r) proves (6).

Put a_N=M/N. The eigenvalues of J lie between -a_N and
||X||_op^2/N-a_N. On the complementary event in (6), therefore,

\[
 \|J\|_{\mathrm{op}}
 \le L_N(r):=8(1+a_N)\log9-a_N+8r/N.                      \tag{7}
\]

To justify the upper bound on the absolute eigenvalues, its right side
exceeds a_N: log9>1 and 8(1+a_N)-a_N>a_N. Taking r=sqrt(N) proves
that ||J||_op<=L_N(sqrt(N)) with probability at least 1-2e^{-sqrt(N)},
and this deterministic upper bound tends to L_alpha. No assertion of
sharpness is made for this matrix norm estimate.

## 3. Empirical local fields at one iid pattern

By exchangeability it suffices to take mu=1. Gauge by x=xi^1: set
eta_i^nu=xi_i^1 xi_i^nu for nu>=2. Conditional on xi^1, all these eta
are independent uniform signs, with a conditional law independent of
xi^1. The signed zero-diagonal field at x is

\[
 g_i:=x_i(Jx)_i
 =1-\frac1N+\frac1N\sum_{\nu=2}^{M}V_{\nu,i},
 \qquad
 V_{\nu,i}=\eta_i^\nu\sum_{j\ne i}\eta_j^\nu.             \tag{8}
\]

For one column suppress nu. Independence and symmetry give

\[
 \mathbb EV_i=0,\quad \mathbb EV_i^2=N-1,
 \quad \mathbb EV_i^4=3(N-1)^2-2(N-1).                    \tag{9}
\]

For the fourth moment, eta_i is independent of the sum and has fourth
power one. In the fourth power of a sum of n=N-1 independent signs,
only terms with all four indices equal, or with two pairs, survive.
Their total is n+6 binom(n,2)=3n^2-2n.

For i!=j,

\[
 \mathbb E[V_iV_j]=1.                                    \tag{10}
\]

One way to see this is to write R=sum_{k notin {i,j}} eta_k. Then
V_i=eta_i eta_j+eta_i R and V_j=eta_i eta_j+eta_j R.
The first product has expectation one, the two cross terms vanish,
and E[eta_i eta_j R^2]=0. Thus for fixed real a,b,

\[
 \operatorname{Var}\left(\frac1N\sum_{\nu=2}^{M}
                 (aV_{\nu,i}+bV_{\nu,j})\right)
 =\frac{M-1}{N^2}\big((a^2+b^2)(N-1)+2ab\big)
 \longrightarrow\alpha(a^2+b^2).                         \tag{11}
\]

The columns are independent. For (a,b)!=(0,0), their fourth moments
verify the Lyapunov condition: using
|u+v|^4<=8(|u|^4+|v|^4) and (9),

\[
 \sum_{\nu=2}^{M}\mathbb E
 \left|\frac{aV_{\nu,i}+bV_{\nu,j}}N\right|^4
 \le\frac{24(M-1)(a^4+b^4)(N-1)^2}{N^4}
 =O(N^{-1})\longrightarrow0.                             \tag{12}
\]

The variance in (11) tends to a positive number, so division by its
square preserves convergence to zero in (12). The triangular-array
Lyapunov central limit theorem and the Cramer-Wold criterion yield

\[
 (g_i,g_j)\ \Rightarrow\ (1+\sqrt\alpha Z_1,
                           1+\sqrt\alpha Z_2),            \tag{13}
\]

where Z_1,Z_2 are independent standard normals. The corresponding
one-dimensional convergence follows from the same calculation, or by
taking b=0. Only these standard central limit theorems are used here;
the needed independence, variance limit and moment condition have all
been checked explicitly.

Let I_i=1_{g_i<=-t}. The limiting one- and two-dimensional distributions
give no mass to the threshold boundaries. Hence

\[
 \mathbb EI_i\longrightarrow p_\alpha(t),\qquad
 \mathbb EI_iI_j\longrightarrow p_\alpha(t)^2\quad(i\ne j).
\]

The sites are exchangeable, so

\[
 \operatorname{Var}\left(\frac1N\sum_i I_i\right)
 =\frac1N\operatorname{Var}(I_1)
   +\frac{N-1}{N}\operatorname{Cov}(I_1,I_2)
 \longrightarrow0.
\]

Consequently

\[
 b_t(\xi^1)=\frac1N\#\{i:g_i\le-t\}
 \longrightarrow p_\alpha(t)\quad\text{in probability}.    \tag{14}
\]

This argument uses asymptotic pair independence, not exact independence
of the local fields. In fact their finite-N covariance is (M-1)/N^2.

## 4. Conclusion and pattern quantifiers

On the norm event (7), every local minimum obeys (5). By (14) and
L_N(sqrt(N))->L_alpha, the right side of (5), evaluated at xi^1 and
this deterministic norm bound, tends in probability to R_alpha(t).
For delta<R_alpha(t), with probability tending to one it exceeds delta.
No local minimum can then have distance at most floor(delta N).
Adding the vanishing probability of failure of the norm event proves
(3). Exchangeability proves it also for every deterministic label mu_N.

For each label let A_mu be the event of a minimum in that cap. Define
B_N=M^{-1}sum_mu 1_{A_mu}. Then E B_N=P(A_1)->0. Markov's inequality
gives P(B_N>epsilon)<=E B_N/epsilon->0 for every epsilon>0. Further,
the event that all patterns have such minima is a subset of A_1, whose
probability tends to zero. The proof does not show that no stored
pattern has a close minimum: the pairwise-CLT variance argument gives
no rate permitting a union bound over M labels.

In particular R_alpha(t)>0 at every alpha,t>0. Fixing any such t proves
that no sequence of minima with d(xi^mu,sigma)/N tending to zero can
exist with nonvanishing probability for a specified pattern. This is
the meaning of the overlap-tending-to-one assertion in the theorem.

## 5. A rationally certified numerical cap at alpha=1/7

Take t=1/5 and z=(6/5)sqrt(7). Then 3<z<16/5.
For every z>0, writing phi(z)=exp(-z^2/2)/sqrt(2pi), integration by
parts gives

\[
 \int_z^\infty\phi(u)\,du
 =\frac{\phi(z)}z-\int_z^\infty\frac{\phi(u)}{u^2}\,du
 >\frac{\phi(z)}z-\frac1{z^2}\int_z^\infty\phi(u)\,du.
\]

Thus Phi(-z)>phi(z)z/(z^2+1). Both phi(z) and z/(z^2+1) decrease
for z>=1. Using z<16/5 gives

\[
 p_{1/7}(1/5)>
 \frac{80}{281}\frac{e^{-128/25}}{\sqrt{2\pi}}
 >\frac{80}{281\cdot540}>\frac1{2000}.                   \tag{15}
\]

For completeness, the second inequality uses sqrt(2pi)<3 and
exp(128/25)<180. The latter follows from e<11/4 and
exp(3/25)<=1/(1-3/25)=25/22:

\[
 e^{128/25}=e^5 e^{3/25}
 <(11/4)^5\,(25/22)<180.
\]

The exponential inequality follows termwise from 1/n!<=1. Also
e=sum_{n>=0}1/n!<5/2+(1/6)sum_{k>=0}3^{-k}=11/4.
The elementary bound pi<4 implies sqrt(2pi)<3.

The exponential series through degree five at 9/4 has sum greater than
9, so log9<9/4. It follows that

\[
 L_{1/7}=\frac{64\log9-1}{7}<\frac{143}{7}<21.
\]

Substitution in (2) now gives the entirely rational lower bound

\[
 R_{1/7}(1/5)
 >\frac{(1/2000)(1/25)}{1/25+4\cdot21^2}
 =\frac1{88\,202\,000}>10^{-8}.                          \tag{16}
\]

This proves the stated explicit cap without depending on decimal normal
tail evaluation. It concerns asymptotically large N, not a useful
finite-network error count at typical simulation sizes.

## 6. Scope

The round-4 correlated construction has load tending to 1/7 and the
stored reference itself is a strict local minimum. The theorem above
excludes that behavior in the iid ensemble, even after allowing a small
fixed error fraction. It supplies one probabilistic stability condition
that a deterministic profile argument cannot supply.

No exclusion at an AGS-sized error tolerance, simultaneous exclusion
around every stored pattern, threshold at 0.138, or replica-symmetric
free-energy formula follows. The constant in (2) was chosen to make the
norm estimate elementary; the result is not claimed to improve published
restitution-error lower bounds. The open problem's phrase “close to 1”
must refer to a specified fixed tolerance or a load-dependent limiting
overlap; interpreting it as overlap tending to 1 at fixed positive load
is ruled out by (3).
