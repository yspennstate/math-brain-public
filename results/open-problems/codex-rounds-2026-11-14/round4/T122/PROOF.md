# A regular-graph variational reduction with an explicit temperature error

Fix an integer d>=3. Limits in n are along dn even. Write G_n for the
uniform simple d-regular graph and c_n=E MaxCut(G_n)/n.
All logarithms are natural.

The external input is Theorem 2.7 and equation (2.12) of Amin Coja-Oghlan
and Will Perkins, [Spin systems on Bethe lattices,
arXiv:1808.03440v1](https://arxiv.org/html/1808.03440).
Under their condition POS, the limiting pressure of the regular factor
graph, for both the pairing and simple ensembles, is the minimum of
their functional over laws invariant under every finite cavity
reweighting. Their theorem is used as stated; its proof is not reproduced.

The specialization and bounds below follow from that theorem. They do
not identify its invariant-law minimum with the hierarchical cavity
infimum.

## 1. Scalar kernels and the invariant-law problem

For beta>0 set t=exp(-beta), a=(1+t)/2 and b=(1-t)/(1+t).
Let m:[0,1]^2 -> [-1,1] be measurable, and put

\[
 \mu_{s,x}(\sigma)=\frac{1+\sigma m(s,x)}2,
 \qquad \sigma\in\{-1,1\}.
\]

Use the binary kernel space and its cut-distance quotient from the
external theorem, via this correspondence. Probability laws on that
space are denoted by pi. Thus equality of laws below is equality on
kernel equivalence classes, not equality of chosen representatives.

Define

\[
 D_\beta(\sigma,u)=a(1-b\sigma u),\qquad
 Q_\beta(u,v)=a(1-buv),
\]

\[
 A_\beta(s;X)=\frac12\sum_{\sigma=\pm1}
       \prod_{j=1}^d D_\beta(\sigma,m(s,X_j)),\qquad
 B_\beta(s;Y)=Q_\beta(m(s,Y_1),m(s,Y_2)).
\tag{1}
\]

Here X_1,...,X_d,Y_1,Y_2 are independent uniform variables. Different
factors below use fresh independent variables, independent of m.
For nonnegative integers N,M, reweight Lebesgue measure on the row
coordinate s by

\[
 z(s)=\prod_{i=1}^N A_\beta(s;X^{i})
               \prod_{j=1}^M B_\beta(s;Y^{j}).
\tag{2}
\]

Let F_z(u)=int_0^u z(v)dv / int_0^1 z(v)dv, and define
m^*(s,x)=m(F_z^{-1}(s),x). These definitions are unambiguous up to null
sets: exp(-beta)<=D_beta,Q_beta<=1, hence
exp(-beta d)<=A_beta<=1, and z is bounded above and bounded away from
zero for each fixed N,M,beta.

Let D^*_{d,beta} be the laws pi for which m^* has law pi whenever m
has law pi, for every N,M. This is an explicit specialization of the
external theorem's invariant class. Define

\[
 \mathcal V_{d,\beta}(\pi)
 =\mathbb E\log\int_0^1 A_\beta(s;X)\,ds
       -\frac d2\mathbb E\log\int_0^1 B_\beta(s;Y)\,ds,
 \qquad
 \Phi_d(\beta)=\min_{\pi\in D^*_{d,\beta}}
                         \mathcal V_{d,\beta}(\pi).
\tag{3}
\]

Expectations include the kernel and the independent uniform variables.
Using separate variables for the two terms is legitimate by linearity
of expectation. All logarithms are bounded at fixed d,beta.

## 2. Checking POS and the model hypotheses

Take the uniform spin prior and the deterministic edge weight

\[
 \psi_\beta(\sigma,\tau)
 =\exp[-\beta\boldsymbol1\{\sigma=\tau\}].
\]

The general definition requests weights strictly between zero and one.
To meet this literally, apply its theorem to
tilde psi=psi_beta/2. This is a single symmetric weight function with
values t/2 and 1/2. All required integrability is immediate.

Here is a direct check of POS, including this scaling. For probability
kernels mu,nu put

\[
 q_{\mu,\nu}(x,y)=\int_0^1\sum_{\sigma=\pm1}
                    \mu_{s,x}(\sigma)\nu_{s,y}(\sigma)\,ds.
\]

The quantity inside each power in binary POS is
1/2+(1-t)q_{mu,nu}/2. For any integer j>=1, define, for
s=(s_1,...,s_j) and eta=(eta_1,...,eta_j),

\[
 f_\mu(s,\eta)=\int_0^1\prod_{h=1}^j\mu_{s_h,x}(\eta_h)\,dx.
\]

Expanding the j-th power and using Fubini gives

\[
 \mathbb E_{X,Y}q_{\mu,\nu}(X,Y)^j
 =\int_{[0,1]^j}\sum_{\eta\in\{-1,1\}^j}
                      f_\mu(s,\eta)f_\nu(s,\eta)\,ds.
\]

Therefore

\[
 \mathbb E[q_{\mu,\mu}^j+q_{\nu,\nu}^j-2q_{\mu,\nu}^j]
 =\int\sum_\eta(f_\mu-f_\nu)^2\,ds\geq0.
\tag{4}
\]

The same expression is zero for j=0. The binomial expansion of
(1/2+(1-t)q/2)^ell has nonnegative coefficients for every ell>=1.
Equation (4), applied term by term, is precisely binary POS.
This proof allows arbitrary kernels; no spin-flip symmetry or
zero-mean condition is imposed on their messages.

Averaging psi_beta over an incoming spin of mean u gives
D_beta(sigma,u). Averaging over two independent incoming spins of
means u,v gives Q_beta(u,v). These identities follow either by summing
the two or four possible spins, or from

\[
 \psi_\beta(\sigma,\tau)
      =a(1-b\sigma\tau).
\tag{5}
\]

For tilde psi the site factor is 2^{-d}A_beta and the edge factor is
B_beta/2. Consequently its cavity tilt differs from (2) by the
constant 2^{-dN-M}, which cancels from F_z. Its invariant class is
exactly D^*_{d,beta}, and its functional is
V_{d,beta}-(d/2)log 2.

Every d-regular graph has dn/2 edges. Thus dividing each edge weight
by two shifts its pressure by exactly -(d/2)log 2. Applying the
external theorem and cancelling this shift proves

\[
 \lim_{n\to\infty}\frac1n\mathbb E\log Z_n^-(\beta)
       =\Phi_d(\beta),\qquad
 Z_n^-(\beta)=2^{-n}\sum_\sigma
                    e^{-\beta U_{G_n}(\sigma)},
\tag{6}
\]

where U_G counts uncut edges. The same equality holds for the pairing
ensemble. The sign in (3) is the minus sign in general equation (2.12).

## 3. Ground state and a uniform error bound

Write h(G)=min_sigma U_G(sigma) and e_n=E h(G_n)/n.
The largest term of the sum in (6), and the upper bound by 2^n copies
of that term, give

\[
 -\beta h(G)-n\log2\leq\log Z_n^-(\beta)
                                  \leq-\beta h(G).
\]

Thus, for each beta>0,

\[
 -\frac{\Phi_d(\beta)}\beta-\frac{\log2}\beta
 \leq\liminf_n e_n\leq\limsup_n e_n
 \leq-\frac{\Phi_d(\beta)}\beta.
\]

Since 0<=e_n<=d/2, letting beta tend to infinity shows that e_n has a
limit e_d. In particular c_n converges to c_d=d/2-e_d, and

\[
 c_d=\frac d2+\lim_{\beta\to\infty}\frac{\Phi_d(\beta)}\beta,
 \qquad
 0\leq c_d-\left(\frac d2+\frac{\Phi_d(\beta)}\beta\right)
                      \leq\frac{\log2}\beta.
\tag{7}
\]

There is also an explicit error bound for the finite differences used
in the source's Corollary 7.7. For any finite graph let S_beta be the
entropy of the Gibbs distribution proportional to exp(-beta U_G).
The identity

\[
 S_\beta=\log\sum_\sigma e^{-\beta U_G(\sigma)}
                           +\beta\langle U_G\rangle_\beta
\]

and the largest-summand lower bound show

\[
 0\leq\langle U_G\rangle_\beta-h(G)
                         \leq\frac{n\log2}\beta.
\tag{8}
\]

Indeed S_beta<=n log2, and log sum exp(-beta U)>=-beta h.
For any L>0, integrate (8) from beta to beta+L, using
-partial_beta log Z_n^-=<U_G>_beta. Taking expectations and n limits
at the two endpoints, which is justified by (6), gives

\[
 e_d\leq\frac{\Phi_d(\beta)-\Phi_d(\beta+L)}L
 \leq e_d+\frac{\log2}{L}\log\left(1+\frac L\beta\right).
\]

Equivalently, the fully specified invariant-law variational problems
at two temperatures obey

\[
 0\leq c_d-
 \left[\frac d2+\frac{\Phi_d(\beta+L)-\Phi_d(\beta)}L\right]
 \leq\frac{\log2}{L}\log\left(1+\frac L\beta\right)
 \leq\frac{\log2}\beta.
\tag{9}
\]

No differentiability of the limiting pressure is required. The
optimization classes at beta and beta+L may differ.

For completeness, concentration upgrades the expectation limit to
convergence in probability. Generate a pairing of dn stubs by revealing
one partner at a time. Conditional completions for two possible
partners can be put in bijection by switching two pairs. A switch
replaces two edges by two edges; each spin assignment's cut changes
by at most two, and so does its maximum. The Doob martingale therefore
has at most dn/2 increments bounded by two. Azuma gives, for the
pairing graph H_n,

\[
 \mathbb P\{|\operatorname{MaxCut}(H_n)
            -\mathbb E\operatorname{MaxCut}(H_n)|\geq u\}
                  \leq2\exp[-u^2/(4dn)].
\]

The pairing-ensemble expectation has the same limit by (6) and (7).
The probability of simplicity is bounded away from zero at fixed d
(Fact 2.2 of the source). Conditioning this concentration statement on
simplicity proves MaxCut(G_n)/n -> c_d in probability. Conditioned
pairings produce uniform simple d-regular graphs, since each such
graph has the same number of labelled-stub realizations.

## 4. Normalization and sign checks

Directly, U_G=dn/2-Cut_G, so

\[
 \sum_\sigma e^{\beta\operatorname{Cut}_G(\sigma)}
 =2^n e^{\beta dn/2}Z_n^-(\beta).
\tag{10}
\]

This independently recovers the d/2 and log 2 shifts in (7).
It also follows from Cut_G=(dn/2-sum_e sigma_u sigma_v)/2
and U_G=(dn/2+sum_e sigma_u sigma_v)/2.

At the constant zero kernel, A_beta=a^d, B_beta=a, and
V_{d,beta}=(d/2)log a. Its derivative at beta=0 is -d/4.
On any simple d-regular graph, differentiation of (6)'s finite-graph
expression at beta=0 gives -E_uniform U_G/n=-d/4 as well.
Replacing the minus in (3) by plus instead gives -3d/4 for this
trial. The displayed Potts specialization in the opened HTML has this
inconsistent plus sign; the general equation (2.12) gives (3).
The argument above uses only the general theorem's functional.

There is a check independent of the zero-kernel interpretation.
Multiplying every edge weight by a constant kappa>0 must shift the
pressure by (d/2)log kappa. A site factor acquires kappa^d and an
edge factor acquires kappa. Thus the minus-sign functional shifts by
(d-d/2)log kappa, exactly as required. A plus-sign functional would
shift by (d+d/2)log kappa. The row reweighting class is unchanged under
this scaling, so optimizing cannot repair the latter discrepancy.

A second check of POS uses m in place of spin probabilities. Put
R_{m,n}(x,y)=int m(s,x)n(s,y)ds. Then q=(1+R)/2. For j>=1,
the corresponding moment difference of the R's equals

\[
 \int_{[0,1]^j}\left[
   \int_0^1\prod_{h=1}^j m(s_h,x)dx
   -\int_0^1\prod_{h=1}^j n(s_h,x)dx\right]^2 ds.
\]

Expanding q^ell by the binomial theorem gives another sum of
nonnegative terms, independently verifying (4).

For (8), a second derivation uses convexity. The function
g(beta)=log sum_sigma exp[-beta(U_G(sigma)-h(G))] is convex,
nonincreasing, and belongs to [0,n log 2], with g(0)=n log 2.
Its tangent at beta lies below g(0), giving
g'(beta)>=(g(beta)-g(0))/beta>=-n log 2/beta. Since
-g'(beta)=<U_G>_beta-h(G), this proves (8) again. Integrating the
derivative bound independently gives the logarithmic error in (9).

## 5. The remaining hierarchical question

Define C_beta(u,v)=exp(beta)Q_beta(u,v). Choose r>=1, parameters
0<zeta_0<...<zeta_{r-1}<1, normalized Ruelle cascade weights V_alpha
on leaves alpha in N^r, and a measurable h:[0,1]^r -> [-1,1].
For each input label j take independent uniform variables U_gamma^j
at all nonroot tree vertices gamma, independent also of the weights,
and set m_alpha^j=h(U_{alpha|1}^j,...,U_{alpha|r}^j). These are the
trial objects used in round 3 and in Section 2.2 of Dmitry Panchenko,
[The Mézard-Parisi formula, arXiv:2610.39545v1](https://arxiv.org/html/2610.39545v1).
The candidate regular hierarchical value is the infimum of

\[
 \log2+\mathbb E\log\sum_\alpha V_\alpha
       \frac12\sum_{\sigma=\pm1}\prod_{j=1}^d
                               C_\beta(m_\alpha^j,\sigma)
 -\frac d2\mathbb E\log\sum_\alpha V_\alpha
                               C_\beta(m_\alpha^1,m_\alpha^2)
\tag{11}
\]

over finite depths, cascade parameters and measurable message
functions. Equation (11) has exactly d site inputs and one edge term
multiplied by d/2; it is not the Poisson functional.

What remains is to equate that infimum with
log 2+beta d/2+Phi_d(beta), or to prove a sufficient zero-temperature
version of that comparison. The invariant laws in (3) have not been
shown to admit the restricted cascade representation. Arbitrary
cascade trial laws also must not be declared invariant under (2)
without proof. Thus simple inclusion of trial spaces is not a
justification of equality. The Poisson upper bound used in round 3
does not, by itself, supply a regular-ensemble interpolation bound.

Equations (7) and (9) settle the temperature passage once a suitable
comparison of the variational problems is proved. They do not settle
that comparison. No fixed-degree hierarchical cavity equality is
claimed here.
