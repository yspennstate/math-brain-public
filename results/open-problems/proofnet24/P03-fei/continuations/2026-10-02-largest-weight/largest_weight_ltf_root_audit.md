# Independent root derivation of the largest-weight LTF argument

2 October 2026. Audited `largest_weight_ltf_candidate.md` in full. At this
checkpoint the argument passes my analytic check; independent reviewers and
the current prior-art review are still pending. This note is not a claim
that unrestricted Boolean FEI is solved.

## Independent reconstruction of the two spectral estimates

Fix a largest positive input weight w, remaining variance sigma^2, and let
B be the indicator of the pivotal slab of half-width w. Put alpha=E B,
R=sigma^2/w^2, p=min output probability, L=ln(1/p), M=max(1,R,L).

The conditional resampling-mask argument is sound. The random mask is
independent of X and therefore of B(X). After conditioning on the mask and
on X, the refreshed signs remain unbiased and independent; their weighted
sum only changes the center of the same slab. An interval bound uniform in
the center can thus be multiplied by B(X). The bad-mask probability retains
the factor alpha, even for extremely rare B. No conditioning on the mask's
variance removes this factor.

The triangular Fourier kernel in the draft gives a direct atom-safe bound
Pr(|sum b_j X_j-t|<=w)<3w/(sum b_j^2)^(1/2) when |b_j|<=w. Its identity is
correct: the integral of (1-w|u|) on [-1/w,1/w], multiplied by w, is
(sin(t/(2w))/(t/(2w)))^2. Its lower bound on the interval and the cosine
upper bound on the integration range are both valid. The weighted Bernoulli
Chernoff exponent (1-e^-1)-1/2 is greater than 1/8. Also
sup_mu sqrt(mu) exp(-mu/8)=2exp(-1/2), so the resulting stability constant
6 is sufficient.

It follows that the normalized slab Fourier law Q has
Q(K<=k)<=18sqrt(k/R), k>=1. Hypercontractivity at correlation 1/2 gives
Q(K<=k)<=2^k alpha^(1/3). Since alpha<=2p, the elementary two-regime
argument gives Q(K<=k)<=3sqrt(k/L). Taking the largest defining scale gives

    Q(K<=k)<=18sqrt(k/M),  Q(K=0)=alpha.

All-zero remaining weights cause R=0 and are covered by the bias bound and
the trivial bound when M=1. Endpoint ties are removed by a threshold-only
perturbation on the finite cube; alternatively the interval estimate covers
closed slabs. Nonconstant functions have alpha>0 because a largest weight
has maximal physical influence.

The split-pair law P_S=Ahat(S)^2+Bhat(S)^2 is the marginal of the full
spectral set after deleting the pivot. Its positive-degree tail is bounded
by the full spectral-degree tail. The established KOS relative noise bound
therefore gives P(K>=u)<=A0 p sqrt(L/u) for every u>0. The established
Keller--Klein lower maximal-influence theorem gives
alpha>=c p min(1,sqrt(L/(R+1))). The pivot's maximal influence equals this
maximum, and R+1<=2M in the needed case. Thus

    P(K>=u)<=Gamma alpha sqrt(M/u)

with an absolute Gamma>=1. The definitions of p, normalized input weight,
noise correlation, and physical influence agree with the primary theorems.

## A different KL proof: an exponential test function

This independently avoids the draft's fixed geometric reference law.
Coarse-grain positive degrees into J=floor(log2(K/M)), and retain degree
zero as star. Then P_j<=Gamma alpha 2^(-j/2), while

    E_Q[|J| 1_(J<0)]<=Cminus
      =18sqrt(2) sum_(m>=1) m 2^(-m/2).

Define a test function g on the coarse atoms by

    g(star)=0,
    g(j)=log2(1/alpha)+j/4 for j>=0,
    g(j)=log2(1/alpha)+j   for j<0.

Its exponential moment under P is bounded by the absolute number

    E_P 2^g <= Ztest
      :=1+Gamma[1/(1-2^(-1/4))+1/(sqrt(2)-1)].

The Gibbs variational inequality, which follows directly from nonnegativity
of D(Q || P 2^g/E_P2^g), gives

    D(Q||P)>=E_Q g-log2 Ztest
      >=(1-alpha)log2(1/alpha)-Cminus-log2 Ztest
      >=log2(1/alpha)-[(log2 e)/e+Cminus+log2 Ztest].

Every law has finite support in a fixed input dimension, so the positive
tail of g causes no integrability issue. Empty bins can be omitted. Since
P_S>=alpha Q_S, all relevant P denominators are positive. Data processing
transfers this lower bound to the full subset laws in the correct direction.
This alternative proof confirms the draft's essential KL conclusion with
a different absolute constant and no assumption on Q's upper degree tail.

## Spectral inclusion entropy and induction

For q_S=Bhat(S)^2/P_S, the included-pivot entropy contribution is exactly
alpha[log2(1/alpha)-D(Q||P)]. The excluded-pivot contribution is at most
alpha log2 e by ln(1+t)<=t, including limiting zero coefficients. Hence the
conditional spectral inclusion entropy is at most an absolute constant
times alpha.

The full entropy split has the interference correction:

    Delta_i H=sum_S P_S[1+h2(q_S)-h2(r_S)],
    r_S=(Ahat(S)+Bhat(S))^2/(2P_S).

It cannot be replaced by inclusion entropy alone. But
(2r_S-1)^2=4q_S(1-q_S) and h2(t)>=4t(1-t), so its correction is at most
h2(q_S). Thus Delta_i H<=2 sum_S P_S h2(q_S)<=C alpha.

Restrictions of an LTF are LTFs. Output complementation and coordinate sign
flips preserve the entropy split and influence, so at every induction node
the rare output and positive-weight conventions can be reimposed. Deleting
zero weights or taking a constant restriction is harmless. Finally
I(f)=I_i(f)+(I(f+)+I(f-))/2 closes dimension induction with the same
absolute constant.

I found no mathematical gap in this derivation. The result it would establish
is FEI for all deterministic LTFs on the uniform cube, with arbitrary bias
and input weights. It establishes neither unrestricted Boolean FEI nor
biased-input-product FEI. Promotion to a final theorem awaits the remaining
independent written audits and a bounded primary-source priority check.
