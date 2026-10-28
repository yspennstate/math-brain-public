# P0174: candidate sharp diameter threshold for free Brownian unimodality

Scope: a complete argument for Problem 3.3 of Hasebe and Ueda. The literature search behind it is incomplete; see analyses/.

Source: Hasebe and Ueda, *Large time unimodality for classical and free Brownian motions with initial distributions*, ALEA 15 (2018), 353–374, Problem 3.3; archived arXiv1710.08240v2, PDF p.6. The PDF carries the arXiv revision date14 September2018 and a manuscript header4 November2021; retain that discrepancy. Primary links: https://arxiv.org/abs/1710.08240 and https://alea.math.cnrs.fr/articles/v15/15-15.pdf . The source defines S(0,t) to have variance t, and D_mu to be support diameter.

The source proves the sufficient constant4 and asks for the optimal universal C in t>=C D_mu^2. Its paragraph says the symmetric Bernoulli law on{-1,1} has threshold t=4 and diameter2, then prints2<=C<=4. Those preceding numbers imply the lower bound C>=1. The candidate upper bound below is a separate argument, not a conclusion drawn from that arithmetic inconsistency.

## Candidate theorem

If mu is a compactly supported probability measure on R with support diameter D, then mu free-convolved with the centered semicircle law of variance t is unimodal whenever t>=D^2. The optimal universal constant in the source's normalization is therefore C=1.

When D=0 the measure is a point mass and the assertion is immediate. Henceforth D>0. No symmetry, density, or non-atomicity of mu is assumed.

## An elementary moment inequality

Let Q be a probability law of a centered real variable X supported in an interval of length D. Write a=E_Q X^2 and b=E_Q X^4. Then

\[
 a\le D^2/4,\qquad b+3a^2\le D^2a.
\]

For the first inequality, if the supporting interval is[l,h], then E[(X-l)(h-X)]>=0 gives a<=-lh, and -lh<=D^2/4 because l+h has a real square. For the second, let X' be an independent copy. Pointwise, (X-X')^4<=D^2(X-X')^2. Taking expectations and using E X=0 gives2b+6a^2<=2D^2a. This derivation checks both the coefficient3 and the use of the diameter rather than radius.

Equality a=D^2/4 forces l=-D/2,h=D/2 and Q to put equal mass on the two endpoints: equality in E[(X-l)(h-X)]>=0 forces endpoint support, and centering fixes the weights.

## Cauchy-profile lemma

For R>0 define

\[
 F_R(u)=\int\frac{d\mu(x)}{(x-u)^2+R^2}.
\]

Claim: F_R has no local minimum with value at most1/D^2.

Take any stationary point u of F_R with F_R''(u)>=0. Put y=R^2>0 and

\[
 Z=\int ((x-u)^2+y)^{-2}\,d\mu(x),\qquad
 dQ(x)=Z^{-1}((x-u)^2+y)^{-2}\,d\mu(x).
\]

Differentiation under the integral is justified by R>0 and compact support. Stationarity says E_Q(X-u)=0. With a=E_Q(X-u)^2 and b=E_Q(X-u)^4, the preceding moment inequalities apply. The second derivative is

\[
 \frac{F_R''(u)}{2Z}
 =E_Q\frac{3(X-u)^2-y}{(X-u)^2+y}
 =3-4y E_Q\frac1{(X-u)^2+y}.
\]

Jensen's inequality and F_R''(u)>=0 imply

\[
 \frac1{a+y}\le E_Q\frac1{(X-u)^2+y}\le\frac3{4y},
 \qquad y\le3a.
\]

The normalization of Q gives an exact reciprocal-profile identity:

\[
 \frac1{F_R(u)}
 =\frac{E_Q[((X-u)^2+y)^2]}{E_Q[(X-u)^2+y]}
 =\frac{b+2ay+y^2}{a+y}.
\]

Consequently

\[
 \begin{aligned}
 \frac1{F_R(u)}-D^2
 &\le\frac{y^2+2ay-3a^2-D^2y}{a+y}\\
 &=\frac{(y-3a)(y+a)+(4a-D^2)y}{a+y}\le0.
 \end{aligned}
\]

The first inequality uses b<=D^2a-3a^2; the final two summands are nonpositive because y<=3a and4a<=D^2. In particular, F_R(u)>=1/D^2.

The equality case matters for the endpoint t=D^2. If F_R(u)=1/D^2 and F_R''(u)>=0, then the two final nonpositive terms both vanish: y=3a and4a=D^2, since y>0. Equality in the variance bound forces Q to be symmetric Bernoulli on u plus/minus D/2. On these two points the reweighting denominator is equal, so mu is the same symmetric Bernoulli law. Writing c=D/2 and s for displacement from its midpoint, with R^2=3c^2, gives

\[
 F_R(u+s)=\frac{s^2+4c^2}{s^4+4c^2s^2+16c^4},
 \qquad
 F_R(u+s)-\frac1{4c^2}
 =-\frac{s^4}{4c^2(s^4+4c^2s^2+16c^4)}<0\quad(s\ne0).
\]

Thus the only possible equality point is a strict maximum, not a local minimum. Every local minimum therefore has value strictly greater than1/D^2, proving the claim including equality.

## Unimodality via Biane's density parametrization

For fixed t>=D^2 and fixed R>0, the equation F_R(u)=1/t has at most two solutions. Indeed, if there were three solutions u1<u2<u3, then either F_R dips below1/t somewhere in[u1,u3], producing an interior local minimum below that level, or F_R>=1/t throughout that interval, making u2 a local minimum at that level. Both alternatives contradict the Cauchy-profile lemma because1/t<=1/D^2. The analytic function cannot be identically constant on an interval, since F_R tends to0 at infinity.

Now use exactly the density framework stated in source Section2.2 and Lemma3.1. Define v_t(u)>=0 by

\[
 \int\frac{d\mu(x)}{(x-u)^2+v_t(u)^2}=\frac1t
\]

where its positive solution exists, setting v_t=0 elsewhere. Biane's real homeomorphism psi_t satisfies

\[
 p_t(\psi_t(u))=\frac{v_t(u)}{\pi t},
\]

where p_t is the continuous density of mu free-convolved with S(0,t), analytic wherever positive. Each positive density level p_t=a corresponds to F_(pi*a*t)(u)=1/t, and therefore has at most two points. Source Lemma2.2, equivalently Lemma3.1, now gives unimodality. All source assumptions match: mu is compactly supported, t>0, and the semicircle parameter is variance.

## Sharpness

Let mu be symmetric Bernoulli on{-c,c}, c>0, so D=2c. For c^2<t<4c^2, the positive solution at the symmetry center has v_t(0)^2=t-c^2. Implicit differentiation at0 yields

\[
 v_t''(0)=\frac{3c^2-v_t(0)^2}{v_t(0)(c^2+v_t(0)^2)}
 =\frac{4c^2-t}{t\sqrt{t-c^2}}>0.
\]

Thus v_t has a positive strict local minimum at0, and the density under the homeomorphism psi_t does as well. It is not unimodal. For any proposed C<1, choose t strictly between max(C,1/4)D^2 and D^2. Then t>=CD^2 but unimodality fails. This proves the lower bound C>=1 independently of the source's printed inequality.

## Second analytic check and remaining review obligations

The same moment computation can be applied directly at critical points of v_t. At such a point, the profile's first derivative vanishes and the sign of v_t'' equals the sign of F_v-fixed''. The calculation above says a nonnegative second derivative would force t<=D^2. Hence for t>D^2 every critical point of v_t is a strict maximum, giving the same threshold. The equality analysis in the Cauchy-profile proof closes the boundary without appealing to weak closure of unimodal laws.

The load-bearing points to challenge are the Q-normalization identity, the centered fourth-moment inequality, the direction of Jensen, and the equality case at t=D^2. Each is written explicitly. Later literature might already contain this sharp threshold or the same argument.
