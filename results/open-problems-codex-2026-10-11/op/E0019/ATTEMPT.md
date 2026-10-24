# E0019: checked partial results

Date: 2026-10-12. Verdict: PARTIAL, not a solution of the general question.

Second-attempt update: FOLLOWUP.md now proves matching finite-L^p bounds for the entire stable controllable common-matrix affine family, closes the source spiral critical boundedness case, and gives a self-contained proof of the known C^k sufficient condition. Section 8 below records the new exact statements and the reduced remaining gap.

## 1. Exact question and scope

Florent Malrieu, *Some simple but challenging Markov processes*, arXiv:1412.7516, PDF p. 13:

> Open question 4. What can be said on the smoothness of the density of the invariant measure of such processes?

Section 4, PDF p. 8, permits finitely many smooth globally forward-complete vector fields on R^d and nonnegative continuous switching rates lambda(x,i,j). Section 4.2 discusses compact state spaces, absolute continuity under additional bracket/accessibility conditions, and singular invariant densities. The question states no universal bracket, rate, or regularity threshold. It is not the assertion that every such invariant measure is smooth or even absolutely continuous.

We work on the exact Example 4.7, not the homogeneous linear model of Section 4.1:

    A = [[-1,-1],[1,-1]], a=(1,0),
    F_0(x)=Ax, F_1(x)=A(x-a), lambda_0,lambda_1>0.

Write mu_i(B)=mu(B x {i}); these are unnormalised subprobabilities. Their densities are rho_i; the spatial marginal density is rho=rho_0+rho_1. Every obstruction proved below for a component also holds for rho because densities are nonnegative.

### What the bare hypotheses alone can guarantee

With no additional bracket or uniqueness hypotheses, *every* probability density can be an invariant spatial density in this class. Indeed, take F_0=F_1=0 on R and constant rates lambda_0=lambda_1=1. For any probability density f, the probability f(x)dx times the uniform probability on {0,1} is invariant: the position never moves and the discrete component is stationary. The zero fields are smooth and globally complete, and the rates are positive and smooth. A compact forward-invariant set may equally well be used.

For an explicit density with no L^p improvement whatsoever, set

    f(x)=1/[x (log(1/x))^2] on 0<x<e^{-1}, and f(x)=0 otherwise.

The substitution t=log(1/x) gives integral f=integral_1^infinity t^{-2}dt=1. For every p>1, integral f^p=integral_1^infinity e^{(p-1)t}t^{-2p}dt=infinity, since the integrand eventually exceeds 1. Thus not even a universal L^{1+epsilon} conclusion follows from the explicit Section 4 setup. This elementary observation does not resolve the intended bracket/accessibility questions and is not presented as a solution of Open question 4.

## 2. Existence, uniqueness and absolute continuity (complete proof)

Put J=[[0,-1],[1,0]], so A=-Id+J and e^{At}=e^{-t}R_t, where R_t is rotation through t. Set b=Aa=(-1,1). The equation is X'=AX-b I. The two-state chain has invariant probabilities pi_0=lambda_1/(lambda_0+lambda_1), pi_1=lambda_0/(lambda_0+lambda_1).

Take a stationary two-sided version of this chain and define

    X_t = - integral_0^infinity e^{Au} b I_{t-u} du.

The integral converges absolutely, since its integrand has norm at most sqrt(2)e^{-u}. In particular |X_t|<=sqrt(2). Splitting the integral at a future time increment gives the variation-of-constants formula, hence this stationary construction solves the PDMP equation and provides an invariant probability.

For uniqueness, couple any two copies of the discrete chain by a common Poisson process of rate lambda_0+lambda_1; at each event resample the state with probabilities (pi_0,pi_1). Ignoring events that preserve the state gives precisely rates lambda_0 and lambda_1. The two states coincide after the first common event, which is finite almost surely. After that time S, the two positions differ by e^{A(t-S)}(X_S-Y_S), whose norm goes to zero. For any two invariant probabilities, start this coupling with those probabilities. Every initial position is finite almost surely; bounded Lipschitz test functions have expectation differences tending to zero by bounded convergence. Invariance makes these differences constant. Such test functions determine probabilities, proving uniqueness without an assumed moment bound.

Here is a direct proof of absolute continuity; it does not infer smoothness from a bracket condition. At a fixed time T=1, conditional on initial (x,i) and exactly N switches, the ordered switching times 0<s_1<...<s_N<T have a density on their simplex. This follows directly by multiplying exponential holding-time densities and the final survival factor. The endpoint is

    X_T=e^{AT}x - integral_0^T e^{A(T-u)}b I_u du.

Its derivative with respect to s_j is e^{A(T-s_j)}b Delta_j, where Delta_j is the jump of I at s_j, equal to +1 or -1. For N>=2 the first two derivative columns have determinant

    Delta_1 Delta_2 |b|^2 e^{-(2T-s_1-s_2)} sin(s_1-s_2).

Its sign is immaterial. Since 0<s_2-s_1<1<pi, it is nonzero. Holding the remaining times fixed, the inverse function theorem gives local diffeomorphisms in (s_1,s_2). A countable covering by such neighborhoods shows that the preimage of any planar Lebesgue-null set has two-dimensional Lebesgue measure zero. Fubini then gives zero probability for such a set. Integrating over arbitrary initial distributions retains this conclusion. Thus paths with at least two switches in a unit block give an absolutely continuous endpoint law.

Every subsequent transition preserves absolute continuity: conditional on a switching path, the map from the initial position is affine with invertible linear part e^{At}, and the switching-path law depends only on the discrete state. A null set therefore still has probability zero.

Let m=min(lambda_0,lambda_1)>0. In any unit block, from either state, the probability that each of the first two holding times is less than 1/2 is at least h=(1-e^{-m/2})^2>0. Such a block has at least two switches. Conditional block by block, the probability that none of n blocks has this property is at most (1-h)^n. For any null B, the stationary probability mu(B x {0,1}) is at most (1-h)^n: once a good block has occurred, the endpoint has an absolutely continuous law, and later transitions preserve it. Let n tend to infinity. This proves absolute continuity of both mu_i.

## 3. Persistence lemma and the endpoint L^p obstruction

**Lemma.** Suppose a stationary switched process on R^d has a mode i with constant exit rate lambda>0 and flow phi_t(x)=c+e^{-kappa t}O_t(x-c), where kappa>0 and O_t is orthogonal. Suppose mu_i has a density and mu_i(R^d)>0. If 0<lambda<d kappa, then, in every neighborhood of c,

    rho_i not in L^p for every finite p >= d kappa/(d kappa-lambda),

and rho_i is not essentially bounded.

**Proof.** No switching for time t has probability e^{-lambda t}, independent of the starting location. Stationarity consequently gives, for every Borel E,

    mu_i(phi_t(E)) >= e^{-lambda t} mu_i(E).             (3.1)

Absolute continuity and positive mode mass imply that some annulus E={r<|x-c|<R}, with 0<r<R<infinity, has mass M>0. Choose T with e^{-kappa T}R<r and set E_n=phi_{nT}(E). These annuli are pairwise disjoint, eventually lie in any prescribed neighborhood of c, and have volume V_n=V e^{-d kappa nT}, where V=vol(E)>0. Equation (3.1) gives mu_i(E_n)>=M e^{-lambda nT}.

For finite p>1, Holder's inequality on E_n yields

    integral_{E_n} rho_i^p >= M^p V^{1-p}
                              exp((d kappa(p-1)-lambda p)nT).

If p>=d kappa/(d kappa-lambda), the exponent is nonnegative. Summing over the disjoint annuli, including at equality, diverges. If rho_i<=C almost everywhere near c, then M e^{-lambda nT}<=C V e^{-d kappa nT} for all sufficiently large n, impossible when lambda<d kappa. This proves both assertions. No pointwise choice of density is used. QED.

Applying the lemma to Example 4.7 gives, for i=0 when 0<lambda_0<2,

    rho_0, rho not in L^p_loc at 0 for p>=2/(2-lambda_0).

At a, the same result holds with i=1 and lambda_1. In particular lambda_i=1 excludes local L^2, including the endpoint, and lambda_i=1/2 excludes local L^{4/3}. At lambda_i=2 the lemma does not decide boundedness or continuity.

## 4. Propagation along the other flow

**Theorem.** In Example 4.7, if lambda_0<1, both rho_1 and rho are essentially unbounded in every neighborhood of every y_s=phi^1_s(0), s>0. More precisely, for each fixed s>0 there exist C_s>0 and r_s>0 such that

    mu_1(B(y_s,r)) >= C_s r^{lambda_0+1}, 0<r<r_s.    (4.1)

Along any fixed compact nontrivial segment of this curve, rho_1 fails local L^p for p>=1/(1-lambda_0), including the endpoint exponent.

**Proof.** Choose R=sqrt(2), or any larger radius, containing the support of the stationary spatial law. Since mu_0 has total mass pi_0, (3.1), with t=log(R/r), gives

    mu_0(B(0,r)) >= pi_0 (r/R)^{lambda_0}, 0<r<R,    (4.2)

using open balls and R>sqrt(2) if necessary.

The stationary last-entry formula is

    mu_1(D)=lambda_0 integral_0^infinity e^{-lambda_1 u}
                         mu_0((phi^1_u)^{-1}(D)) du. (4.3)

To justify it, look back a finite time L in the stationary process. Paths with no switch in mode 1 contribute e^{-lambda_1 L}(phi^1_L)_*mu_1. Every other path has a unique last 0-to-1 switch at a time u in (0,L) before observation. Its entry-location intensity is lambda_0 mu_0(dx)du by stationarity and the constant jump intensity, and its subsequent survival probability is e^{-lambda_1 u}. This gives the formula truncated at L plus the no-switch term. The latter has total mass pi_1 e^{-lambda_1 L} and tends to zero. Monotone convergence gives (4.3).

Fix s>0. The curve y_u=a-e^{Au}a has speed |y'_u|=sqrt(2)e^{-u}<=sqrt(2). Also |phi^1_u(x)-y_u|=e^{-u}|x|<=|x| for u>=0. Put delta=r/(4 sqrt(2)). For r small enough that [s-delta,s+delta] lies in (0,infinity), any |x|<r/2 and any u in that interval satisfy

    |phi^1_u(x)-y_s| <= r/2 + sqrt(2)delta < r.

Restrict (4.3) to this interval and use (4.2) with r/2. Its length is 2delta; e^{-lambda_1 u} has a fixed positive lower bound for all small r. This proves (4.1). If rho_1 were essentially bounded on some neighborhood of y_s, its ball mass would be at most C pi r^2. This contradicts (4.1) when lambda_0+1<2.

For the L^p assertion, fix 0<u<v<infinity and let Gamma={y_s:u<=s<=v}. If |x|<r, then phi^1_s(x) lies in its r-neighborhood N_r(Gamma) for s in [u,v]. Equations (4.2)-(4.3) give mu_1(N_r(Gamma))>=c r^{lambda_0}. The smooth curve has finite length L_Gamma; covering it by at most 1+ceil(L_Gamma/r) balls of radius 2r gives vol(N_r(Gamma))<=C r for 0<r<1. If rho_1 belongs to L^p on a neighborhood of Gamma, Holder gives

    c r^{lambda_0} <= ||rho_1||_{L^p(N_r(Gamma))} (C r)^{1-1/p}.

The local norm on the right tends to zero: rho_1^p is integrable on the assumed fixed neighborhood, and vol(N_r(Gamma)) tends to zero, so absolute continuity of its Lebesgue integral applies. Dividing by r^{1-1/p}, the left side is bounded below by c for every 0<r<1 whenever lambda_0<=1-1/p. This is impossible, including at equality. Equivalently, p>=1/(1-lambda_0) is excluded. The same proof applies to any subsegment, and so rules out L^p in a neighborhood of any interior point of such a segment. For p=infinity use the volume bound directly. QED.

The reflected assertion at a and along phi^0_s(a) follows by x -> a-x and exchanging the mode labels. The calculations above do not assert a particular pointwise value rho_i(y_s), because densities are defined only almost everywhere. They assert the stronger version-independent failure of essential boundedness in every neighborhood.

## 5. Algebra and the earlier-attempt error

Using the convention [F_0,F_1]=DF_1 F_0-DF_0 F_1, the bracket is the constant A^2 a=(0,-2). The difference F_0-F_1=Aa=(-1,1). Their determinant is 2, so they span R^2 at every point. The opposite bracket convention gives determinant -2, with the same rank conclusion. The original drift determinant is det(F_0(x),F_1(x))=2 x_2, and it vanishes on the horizontal axis. Thus failure of transversality does not imply failure of the bracket condition. Indeed the whole-plane bracket condition here coexists with the singularities proved above.

The earlier intake attempt conflated these notions and also transcribed the Section 4.1 determinant incorrectly. The source's actual homogeneous-matrix formula, PDF p. 12, is Q(y,z)=alpha y^2-yz-alpha z^2. It concerns a different model and does not prove smoothness off its zero set. No such inherited claim is used here.

## 6. Later literature and the precise remaining gap

Benaim--Bichard (2024), Theorem 2.2, PDF p. 8, treats stable common-matrix affine flows F_0(x)=Ax, F_1(x)=A(x-p), with the controllability assumption span(p,Ap,...,A^{d-1}p)=R^d. If Lambda_j are the real parts of the eigenvalues and

    min(lambda_0,lambda_1)>-[sum_j Lambda_j+k Lambda_1],

the density is C^k on all of R^d. For the exact spiral example, Lambda_1=Lambda_2=-1 and det(a,Aa)=1, so this gives C^k whenever min(lambda_0,lambda_1)>k+2. This is a cited sufficient theorem, not a new full proof supplied by this attempt. The authors explicitly name Malrieu's Open question 4 in Example 1.3, PDF p. 5. The additional parameter assumptions prevent classifying it as a solution of the source's entire question under the user's criterion.

At the end of the first attempt, we had necessary integrability bounds and singularity propagation but lacked matching positive L^p bounds and the lambda_i=2 critical case. FOLLOWUP.md now closes those two gaps for the source spiral and proves an exact finite-p theorem for all stable controllable common-matrix affine systems. Higher differentiability classification and arbitrary nonlinear/state-dependent switched flows remain unresolved. This is still not a SOLVED or SOLVED_IN_LITERATURE verdict.

## 7. Referee checklist and checks

- Invariant-law existence is proved by an absolutely convergent stationary convolution, not assumed from compactness alone.
- The discrete-state coupling is a resampling construction with the correct off-diagonal rates; it does not use identical holding times for different states.
- Absolute continuity is proved from two switch-time derivatives at fixed total observation time. Their nonzero determinant is independent of the starting position, including the equilibria.
- Singularity proofs use unnormalised mode measures, whose positive masses are pi_i. No conditional-mode normalisation is silently omitted.
- All L^p and unboundedness conclusions are invariant under changes of density on null sets.
- The critical equilibrium L^p endpoint is handled by infinitely many disjoint annuli. A Holder bound with a fixed neighborhood norm would not exclude equality; disjoint shells or absolute continuity of a shrinking local Lp integral are needed.
- Propagation uses a time interval of length proportional to r, contributing the extra power of r in (4.1). Ignoring this would give an incorrect threshold of 2 for singularity along the curve.
- The propagated finite L^p endpoint follows from absolute continuity of the local L^p integral on shrinking tubes. FOLLOWUP.md now supplies matching global finite-Lp bounds; a full higher-differentiability classification at intermediate rates remains unproved.
- Kernel-checked algebra and reproducible symbolic/numerical checks are recorded in CHECKS.md after execution. These checks cover algebra, not the analytical proof as a whole.


## 8. Serious second attempt: new exact results and remaining gap

The complete new proofs are in FOLLOWUP.md, Theorems A and B and Corollary C. Two previously untried approaches, the reason for selection, the brain queries, and the hostile-referee checklist are written there.

**Exact finite-p theorem.** If A is any real Hurwitz matrix, a,Aa,...,A^(d-1)a span R^d, and F_0(x)=Ax, F_1(x)=A(x-a) have constant positive exit rates, set D=-tr(A). For every finite p>1, the unique invariant density belongs to L^p if and only if min(lambda_0,lambda_1)>D(1-1/p). Equality is excluded. The obstruction is local at the equilibrium of an offending mode. This covers anisotropic and nonnormal matrices as well as the rotating source example. The proof uses a fixed-time smooth switch-time cutoff kernel, an exact affine Lp pushforward factor, a small-remainder series, and disjoint nested ellipsoid shells.

**Exact boundedness/continuity for Example 4.7.** For the source spiral, a bounded version exists if and only if min(lambda_0,lambda_1)>2. The same inequality characterizes a continuous version on all of R^2. If lambda_0=2, rho_0(x)>=c log(delta/|x|) almost everywhere near 0, for some c,delta>0; there is a reflected statement when lambda_1=2. At min(lambda_0,lambda_1)=2, the density lies in every finite Lp but is essentially unbounded. Three positive switching pulses and a two-switch subkernel supply the needed uniform density lower bound near the equilibrium; support membership alone would not supply it. These are lower bounds, not exact singularity asymptotics.

**Positive C^k condition with a complete proof.** The same decomposition proves C^k whenever min(lambda_0,lambda_1)>-tr(A)-k Lambda_min, where Lambda_min is the smallest real part of an eigenvalue. This reproduces the already cited Benaim--Bichard sufficient condition by a fixed-time argument. It is not claimed to be necessary.

**Remaining gap, precisely.** No classification of higher derivatives at all rate pairs, no complete propagated singularity set or smoothness theorem away from it, and no general theorem for arbitrary smooth nonlinear switched flows with merely continuous spatial switching rates. In particular, the exact finite-p classification and the exact source-spiral C0 classification are solved special cases within E0019, while E0019 itself retains the PARTIAL verdict.
