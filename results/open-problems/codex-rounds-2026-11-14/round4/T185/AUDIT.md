# Audit of the sampled-drift lemma

## The earlier result

For gradient g at the through axis, the two limiting drift vectors are
rho-e_1 and rho-e_2. Their average is (1/5,0,0), so their mean pairing
with g is g_0/5. Homogeneity gives g_0=dF(e_0)>0. Equivalently the two
values are g_0/5 plus and minus (g_1-g_2)/2. This rederives the old
obstruction without importing its polynomial calculation. The explicit
two-route allocation follows from the single tight common-link constraint
and its KKT equation. The old main claim holds under its stated boundary
smoothness assumptions.

The original session's certificate is consistent with this calculation:
normalized aggregate service below one makes every link slack, contradicting
Pareto efficiency; a route alone attains one. The example has total route
load 6/5 and individual link loads 7/10, so it falls outside that certificate's
region. Nothing in the new lemma relies on a scalar comparison queue being
stable at total load 6/5.

## Independent checks on the new constants

With equal weights, alpha=1, and horizon four, the expected clearing-time
upper bound can be calculated directly before collecting powers of N:

    N^-4 [N + E A_0(4) + 2 N^3 + 2 E(A_1(4)+A_2(4))]
      = N^-4 [N + 4/5 + 2 N^3 + 8]
      = 2/N + 1/N^3 + 44/(5N^4).

The subsequent service-loss bound has expectation
2*4*E(A_1(4)+A_2(4))/N=32/N. Adding gives
34/N+1/N^3+44/(5N^4), as in PROOF.md. At N=200 its terms are
0.17, 0.000000125, and 0.0000000055. Their sum is 0.1700001305.
Subtracting 0.2 gives -0.0299998695. The script separately checks the
fractions 340000261/2000000000 and -59999739/2000000000.

For the limiting sign, workload balance gives expected through change
T/5-T=-4T/5. The unserved new local work is max(P_1,P_2), with mean
T/2+E|P_1-P_2|/2. Their sum is -3T/10+E|P_1-P_2|/2. Independently,
the difference is a rate-one symmetric random walk observed at time T;
its second moment is T, recovering the same Cauchy bound. Negativity of
-3T/10+sqrt(T)/2 is equivalent to 3sqrt(T)>5, or T>25/9.

## Exact Poisson calculation, with two representations

The exact script encloses d(4) in

    [-0.428494478548, -0.428494478547].

No floating-point exponential is used. For exp(4), sum the positive power
series through order 80. Its remaining terms are bounded by the first
omitted term times 1/(1-4/82), since all subsequent ratios are at most
4/82. Inverting the resulting positive bounds encloses exp(-4).

First calculation: condition on the total number of local arrivals,
Z~Poisson(4). Given Z=n, their difference is S_n, an n-step symmetric
random walk. Direct binomial enumeration gives q_n=E|S_n| exactly. The
independent recurrence q_(n+1)-q_n=P(S_n=0) checks each q_n. Sum
exp(-4) sum_(n=0)^70 4^n q_n/n!. Since q_n<=n, its unnormalized omitted
tail is at most

    4*(4^70/70!)/(1-4/71).

This bounds E|P_1-P_2| and hence d(4).

Second calculation: independently sum max(m,n) against the two Poisson(2)
mass functions for 0<=m,n<=40. Off that square use max(X,Y)<=X+Y and
the union bound. The omitted expectation is at most

    4*[P(Poisson(2)>=40)+P(Poisson(2)>=41)].

Bound each probability by its unnormalized positive series, using a
geometric bound on the successive ratios. This gives a second enclosure
of E max(P_1,P_2), and subtraction of 16/5 gives d(4). The intervals
overlap and separately give the displayed outward-rounded enclosure.
The simple theorem uses only d(4)<=-1/5; this calculation checks the
scale and sign more sharply without being needed for the proof.

## Attempts to break the clearing and balance arguments

1. **New arrivals before clearing.** Equation (9) of PROOF.md uses all
   terminal arrival counts in its denominator. It remains valid during
   arbitrary early arrival bursts. The deterministic cohort checks include
   arrivals at N^-6, well before the nominal N^-1 clearing scale.

2. **Unequal original residuals or locals on both links.** The service lower
   bound applies to each surviving original file individually and uses only
   its upper residual bound. As some files depart the denominator bound
   remains valid. No simultaneous departure assumption enters the proof.
   Both kinds of perturbation are covered symbolically and tested by cohorts.

3. **Weights that make clearing slower than T.** In this case the argument
   uses I_N(T)<=T<=D_N, not a false assertion that the originals have already
   gone. The convergence is for each fixed set of positive weights and fixed
   alpha; no weight-uniform convergence is claimed. Cohort checks include
   weights (1,1/100,100).

4. **A through departure that invalidates n_0>=N.** Before the first original
   departure its individual rate is at most 1/N. The strict inequality
   T/N<1-N^-8 rules that departure out. Merely knowing that W_0 is large
   would not justify this argument. Horizon T is fixed before N increases.

5. **An absent local route.** Its service is zero, not 1-Lambda_0. The
   proof uses equality only on occupied local routes and the inequality
   0<=Lambda_j<=1-Lambda_0 for the balance sandwich. With no locals H=0
   and through service is exactly one.

6. **Small alpha and very unequal counts.** The bound H<=b(n_1+n_2) uses
   only monotonicity of a positive power. No norm triangle inequality for
   alpha<1 is invoked. Allocation formula (6) follows directly from the
   objective for every alpha>0; its symbolic derivation is essential because
   the rational cohort checks test alpha=1 only.

7. **Replacing input by its mean too early.** The balance sandwich retains
   every unit arrival. In the limit it retains a random max(P_1,P_2), not
   the maximum of their mean values. In particular the absolute-difference
   correction is nonzero and cannot be dropped.

8. **A stronger convergence assertion than the estimates support.** The
   proof bounds the expectation of I_N(T) explicitly. It does not rely on
   an unstated uniform-integrability step. The error sandwich bounds the
   absolute error by max(m,I_N(T)); hence it also gives L1 approximation
   under a common arrival coupling for each deterministic sequence of states.

9. **A sign or missing factor in the workload sandwich.** The local endpoint
   maximum is between Q-I_N and Q+m; adding the through increment
   A_0-T+I_N and subtracting the initial local maximum m gives exactly
   [-m,I_N]. The cumulative loss appears once, not twice. The 360 exact
   cohort paths check this against both workload balance and the independent
   identity that M drains at rate one between arrivals.

10. **Extrapolating to stability.** The sets C_N do not exhaust the large
    states. In particular the proof does not cover a few through files with
    substantial residuals or macroscopic initial local work. A negative drift
    only on C_N cannot prove recurrence. There is no uniform estimate here
    over a diverging horizon T_N, and no renewal or general-arriving-file
    extension is claimed.

No mathematical failure was found in the new lemma. Its restricted initial
state class is the principal limitation.

## Stronger service accounting estimate

Section 7 of PROOF.md removes the initial count and individual local-residual
restrictions. Its extra assumption is only that every residual is at most
one, as in the deterministic-unit-file model. In particular
n_0(t)>=W_0(t)>=W_0(0)-T, even if many original through files depart.

The crucial charging inequality is pointwise: the loss of through service
is at most the total service to original local files plus
c*(number of new local files)/(a_0*R). If only one local route is occupied,
the uncharged fraction is its new-file fraction. If both are occupied, the
positive uncharged fraction is

    theta=(new_1/n_1 + new_2/n_2 - 1)^+.

It is bounded by each new-file fraction, so theta*n_j<=new_j in both
coordinates. The explicit H is coordinatewise increasing and homogeneous
of degree one for every alpha>0. Thus theta*H(n)<=H(new). This does not
use convexity or a norm inequality. When original-file fractions sum to
more than one, the total service to originals already exceeds the loss,
and there is no positive amount to charge to new files.

After integrating, original local service is at most its initial work w.
At time s there are at most A_1(s)+A_2(s) new local files, with mean s.
Consequently the mean arrival-count area is T^2/2. Independently, conditional
on K total local arrivals up to T their times are uniform, so their mean
total area is K*T/2. Taking E K=T gives the same T^2/2. The terminal-count
bound in the initial log is valid but can be sharpened by this factor two.

For equal weights and alpha=1, H=n_1+n_2, so c=1 is valid (the earlier
clearing proof's b=2 remains a valid looser bound). If W_0>=N-1 and local
total work<=1/N, the new upper error at T=4 is

    1/N + 8/(N-5).

At N=100, subtracting 1/5 gives

    -1/5 + 1/100 + 8/95
      =(-380+19+160)/1900=-201/1900.

This rederives the final constant independently of the script's Fraction
identity. Both positive terms decrease with N, so the bound holds for all
N>=100. This wider family includes the old accessible sets because their
through workload is at least N-N^-7>=N-1.

The final 504 exact cohort paths also check the pointwise charging inequality
and its integrated form. Added paths contain N^3 tiny original through
files that depart during the horizon, and a single original local file
of residual 1/N, which is larger than the old N^-4 restriction. The old
clearing bound is not applied to this latter case. These are independent
stress tests of the wider initial-state statement, not evidence for general
file-size or renewal stability.
