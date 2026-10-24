# R15 idea before validation — n=30 one-heavy boundary exclusion

Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.

Date: 2026-09-20 UTC. Retained screen only: Talagrand F0111, k=2, PENDING / SELF_CHECK_ONLY / NOT CLAIMED. Native I0076 remains RETIRED-HANDOFF and is not reopened.

Methods used in this idea: #8 DISCRETIZE, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT. Historical R15 work has already used all 30 numbered moves at least once, so there is no literally never-before-used number left; this triple is different from the preceding #15/#18/#29 and is applied to a new object.

## Carried boundary system

Continue from `runs/R15/20260920_0106Z_successor_screen_f0111_heterogeneous_oneheavy_j95r.md`. On the z=1+epsilon branch, after the one-heavy theorem, write

- a=1+delta, b=1-delta, D=delta+3,
- r_*=1-c epsilon+o(epsilon),
- r_i=epsilon u_i+o(epsilon) on light J,
- r_j=epsilon v_j+o(epsilon) on K,
- sum_K v_j=nu=a^2/(2bD),
- sum_light u_i=c+xi with xi=(delta^2+4delta+7)/(2aD),
- kappa=4/(abD), and n=30 so every finite limiting coordinate mass obeys u_i,v_j >= kappa/29.

The projective rank-one downdate has a scaled PSD residual Gram representation. Put

rho=3/D, gamma=12D/a^2, theta=6/a.

There are vectors w0 (heavy), w_i (light J), y_j (K) with

||w0||^2=c-rho,
||w_i||^2=u_i,
||y_j||^2=v_j(1-gamma v_j),

a(w0+sum_i w_i)=b sum_j y_j.

The limiting pair coefficients are

p_i=b_{*i}=u_i+<w0,w_i>,
s_il=b_{il}=<w_i,w_l>,
t_ij=b_{ij}=<w_i,y_j>,
q_j=b_{*j}=(1+theta)v_j+<w0,y_j>,

and all are nonnegative. The limiting null-flow equations imply

a P-b Q=1,
 b T=a(P+2S),

where P=sum p_i, Q=sum q_j, S=sum_{i<l}s_il, T=sum_{i,j}t_ij. Hence P>=1/a and T>=1/b.

## New lower bound from residual geometry

Let Y=sum_j y_j and W=sum_i w_i. Residual nullity gives W=(b/a)Y-w0, while T=<W,Y>. Since each v_j<=1/gamma and sum v_j=nu,

||Y||^2 <= N sum_j ||y_j||^2
 <= N(nu-gamma nu^2/N)=nu(N-L),

where L=gamma nu=6/b. Put E^2=nu(N-L). Then

1/b <= T <= (sqrt(c-rho)+(b/a)E)E.

If E=0, contradiction immediately. Otherwise

c >= C_N(delta):=rho + [1/b-(b/a)E^2]^2/E^2.

At n=30, full-support positivity and the projective K cap give

L=6/b <= N <= U=29 a^3/8.

The global feasibility condition L<=U forces 2/5<delta<3/5; hence N is an integer in {11,12,13,14}. I expect C_N(delta)>26 on every feasible interval. This is now a finite exact rational-polynomial claim.

## New upper bound from exact value contact

The same Gram representation gives

P=xi+rho+(b/a)<w0,Y>,
Q=(1+6/a)nu+<w0,Y>.

The exact leading value-contact identity from the previous report is

c=sum_light p_i log(A u_i)+sum_K q_j log(A v_j),
A=29/kappa.

Using u_i<=c+xi and v_j<=1/gamma,

c <= P log(A(c+xi))+Q log(A/gamma).

On every n=30 feasible boundary configuration, coarse uniform inequalities should be enough:

xi<1, rho<1,
(b/a)E<1/4,
E<1,
(1+6/a)nu<4,
A<21,
A/gamma<=261/256<51/50.

Therefore any such contact must obey

c < Psi(c):=(2+sqrt(c)/4) log(21(c+1)) +(4+sqrt(c))/50.

For c>=26, log(21(c+1))<2sqrt(c); Psi'(c)<1, while at c=26 the elementary bounds sqrt(26)<6 and log(567)<7 give Psi(26)<24.7<26. Hence Psi(c)<c for all c>=26.

If the finite exact check confirms C_N(delta)>26 for N=11,12,13,14 on their feasible intervals, the one-heavy z->1+ limiting system is impossible in dimension 30 for every delta, not just the earlier block-constant or saturation cases. This would show the sharp scalar dimension-barrier boundary n=30 cannot actually be attained by any heterogeneous exact quadratic certificate through this Hessian-null mechanism.
