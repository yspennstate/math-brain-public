# F0084: the requested upper bound is already proved in the literature

## Outcome and scope

Holroyd, Pemantle, Peres and Schramm, *Poisson Matching*, explicitly extend their polynomial upper-tail theorem to the critical stable allocation of Lebesgue measure to a unit-intensity Poisson process. The relevant statement is Theorem 6(ii), **printed p.269**, together with the explicitly stated extension on **printed p.270** and the proof-adaptation remark on **printed p.286** of the 2009 journal paper. The corresponding locations in arXiv:0712.1867v3 are PDF p.6, pp.7–8, and p.34. Both PDFs were retrieved and independently inspected. This answers the request for **any quantitative upper bound in every d>=2**. It does not determine the sharp asymptotic tail, which remains a different question.

The first attempt missed this explicit extension and incorrectly left the upper-bound question unresolved. Its small-distance result and conditional comparison remain valid, but its literature-status conclusion is superseded. The complete exact quotations and hypothesis mapping are in LITERATURE.md.

## Independent complete proof of a weaker explicit bound

For d>=2 let v_d be the volume of the Euclidean unit ball. We prove, for every r>0,

P(X>r) <= K_d r^(-1/(4d)),

where K_d = max{1, 21*2^(d/2)/(10*sqrt(v_d))}.

This is a deliberately weaker exponent than the published s(d). The proof below uses only stationarity, stability, critical full allocation/satedness, Poisson count variance, and elementary integration. It independently checks the decisive allocation transfer instead of relying on point-to-point matching by analogy.

### 1. Site–centre tail-mass identity

Work with the almost surely unique translation-equivariant stable allocation psi. By the critical phase theorem, almost every site is claimed and every centre has territory of volume 1. For t>=0 put p(t)=P(X>t), and for a centre xi put

T_t(xi)=volume{x:psi(x)=xi, |x-xi|>t}.

Then 0<=T_t(xi)<=1 and E^0 T_t(0)=p(t), where E^0 is expectation under the Palm law of the Poisson centres, with the allocation included as background.

Here is a full mass-transport proof. For half-open unit cubes Q_u=u+[0,1)^d, u in Z^d, let

m(u,v)=integral_{Q_u} 1{psi(x) in Q_v, |x-psi(x)|>t} dx.

All quantities are nonnegative. Integer translation covariance gives E m(0,v)=E m(-v,0). Summing over v and applying Tonelli gives E sum_v m(0,v)=E sum_u m(u,0). The first side is the expected volume of distance>t sites in Q_0, equal to p(t) by stationarity. The second side is E sum_{xi in Pi intersect Q_0} T_t(xi), equal by Campbell–Palm at intensity 1 to E^0 T_t(0). This proves the identity. It involves weighted territory volume, not the probability that a centre's maximum radius exceeds t.

Consequently, for every deterministic nonnegative measurable threshold h on a bounded B,

E sum_{xi in Pi intersect B} T_{h(xi)}(xi) = integral_B p(h(y)) dy.       (1)

Indeed Campbell–Palm first gives integral_B E^0 T_{h(y)}(0) dy, and the fixed-t identity applies to each deterministic h(y). Joint measurability follows directly from the measurable allocation and its tail integrals; Tonelli allows every exchange. At a deterministic site the exceptional allocation set has probability zero by stationarity and Fubini.

### 2. Stability excludes two opposite deep outgoing masses

Fix R>0 and B=B(0,R). Define

A = volume{x in B: |x-psi(x)|>R+|x|},
D = sum_{xi in Pi intersect B} T_{R+|xi|}(xi),
Q_out = volume{x in B: psi(x) outside B},
Q_in = sum_{xi in Pi intersect B} volume{x outside B:psi(x)=xi},
Z = volume(B)-N(B), where N(B)=#(Pi intersect B).

The labels out/in refer to flow out of the site ball and flow into its centres from sites outside. A<=Q_out: if psi(x) were a centre inside B, its distance would be less than R+|x|. Similarly D<=Q_in, since |x-xi|>R+|xi| implies x lies outside B.

We have A=0 or D=0. Otherwise choose a nonexceptional x in the positive-volume set defining A and a centre xi in B with T_{R+|xi|}(xi)>0. Such a centre exists because the sum has finitely many terms. There is a site y in its territory with |y-xi|>R+|xi|. Now |x-xi|<=|x|+|xi|<R+|x|<|x-psi(x)|, so x desires xi. Also |x-xi|<R+|xi|<|y-xi|, so xi covets x. This is a blocking pair, contradicting stability. Thus both positive masses cannot coexist.

Let H be the volume of sites in B allocated to centres in B. Since sites are claimed almost everywhere, Q_out=volume(B)-H. Since every centre in B is sated to volume 1, Q_in=N(B)-H. Hence Q_out=Q_in+Z. If A=0, then A+D<=Q_in. If D=0, then A+D=A<=Q_out=Q_in+Z. In either case,

A+D <= Q_in+Z_+, where Z_+=max(Z,0).                                 (2)

This is the exact allocation counterpart of inequality (23) in the published proof.

### 3. An integral recurrence for the critical site tail

Stationarity and (1) give

E A = E D = I_R := integral_B p(R+|y|) dy.

For each centre xi in B, every site outside B in its territory is at distance strictly greater than R-|xi| from xi. Therefore

E Q_in <= J_R := integral_B p(R-|y|) dy.

This implication uses the triangle inequality and the open ball; boundary sites have zero Lebesgue measure and centres on its sphere have zero Poisson probability. Taking expectations in (2) yields 2 I_R<=J_R+E Z_+.

N(B) is Poisson with mean V=v_d R^d, so E Z=0 and E Z^2=V. Cauchy–Schwarz gives E Z_+<=E|Z|<=sqrt(V). Since p is decreasing, I_R>=V p(2R). If U is uniform in B and W=1-|U|/R, then J_R/V=E p(RW). We obtain

p(2R) <= (1/2) E p(RW) + [1/(2 sqrt(v_d))] R^(-d/2).                 (3)

The distribution of W has density d(1-w)^(d-1) on (0,1). No independence of allocation and centres or of these outgoing sets was assumed, and rotational invariance of the allocation is not needed for (3).

### 4. A uniform contraction with an explicit exponent

Put s=1/(4d). Since P(W<=t)=1-(1-t)^d<=dt for 0<=t<=1, W stochastically dominates U_0/d, where U_0 is uniform on (0,1). For completeness, the inequality follows from (1-t)^d>=1-dt: its difference has value zero at t=0 and derivative d[1-(1-t)^(d-1)]>=0. An explicit coupling avoids needing a stochastic-order theorem: the variable W'=1-(1-U_0)^(1/d) has the law of W. Bernoulli's inequality with t=U_0/d gives (1-U_0/d)^d>=1-U_0, hence W'>=U_0/d. Therefore (W')^(-s)<=(U_0/d)^(-s) pointwise, and integration gives

E W^(-s) <= d^s integral_0^1 u^(-s) du = d^s/(1-s).

Thus a := 2^(s-1) E W^(-s) <= (2d)^s/[2(1-s)] <= 16/21 < 1. To verify the numerical bound without approximation: for d>=2, log(2d)<=d. The function x-log(2x) is increasing for x>=2, and 2-log 4>0 (e^2>4, for example from its first three series terms). Therefore (2d)^s<=exp(1/4)<=4/3. The last inequality follows term by term from exp(x)=sum x^n/n!<=sum x^n=1/(1-x) for 0<=x<1. Finally s<=1/8, so 2(1-s)>=7/4, and (4/3)/(7/4)=16/21.

Define F(L)=sup_{0<t<=L} t^s p(t). This is finite, since p<=1, and F(1)<=1. For r>0, using R=r/2 in (3) and RW<=r/2 gives

r^s p(r) <= a F(r/2) + B_d r^(s-d/2),

where B_d=2^(d/2)/(2 sqrt(v_d)). The inequality p(RW)<=(RW)^(-s)F(r/2) holds for W>0, which occurs almost surely; its expectation is finite by the preceding negative-moment estimate.

Let K=max{1,21 B_d/5}. We prove F(2^n)<=K by induction on n. It holds at n=0. If it holds at n, then for every r in (2^n,2^(n+1)], r/2<=2^n and r>=1. As s<d/2, the displayed recurrence gives

r^s p(r) <= aK+B_d <= (16/21)K+(5/21)K=K.

For 0<r<=2^n the induction hypothesis gives the same bound. Taking the supremum proves F(2^(n+1))<=K. For every r>0 there exists n with r<=2^n; hence r^s p(r)<=K. Since 21 B_d/5=21*2^(d/2)/(10 sqrt(v_d)), this proves the stated explicit bound for all r>0.

## Hostile-referee checklist

- The central exclusion is a consequence of strict blocking-pair inequalities, not an independence assumption.
- Counts on the centre side are replaced by *volumes of long portions of territories*. This is crucial; maximum territory radii have a different distribution.
- Every site is claimed a.e. and every centre sated exactly at criticality. These facts justify both flow equalities. Without them, an extra missing-mass term appears.
- The centre weighted-tail law equals the site tail by mass transport at intensity 1. Varying deterministic radial thresholds are then handled by Campbell–Palm; direct site/centre law identification would be wrong.
- Cauchy–Schwarz uses the exact Poisson count variance V; no claim about independent residual processes is needed.
- The induction uses F(r/2), not F(r), so it is not circular. Negative moments are integrable because s<1.
- This answers the explicitly requested upper-bound portion. It does not prove a sharp exponent or an asymptotic equivalence.

### Numerical checks completed

`check_second.py`, seed 84002, checked 30 finite critical torus allocations (256 sites of mass 1/16 and 16 centres of appetite 1), with 20 independently sampled origins and six radii each. All 3,600 origin/radius combinations passed the exact integer versions of A<=Q_out, D<=Q_in, A=0 or D=0, Q_out=Q_in+Z, and A+D<=Q_in+Z_+. There were 1,821 cases with A>0, 840 with D>0, and 939 with both zero, so the test exercised both nontrivial branches. The distance matrix occupied 32,768 bytes and numerical work took about 35 seconds. This is a finite algebra/stability check, not a proof that a finite discretization approximates the infinite tail.

Numerical quadrature separately checked the negative moment and contraction for d=2,3,4,10,50,100. The contractions were approximately 0.66469, 0.62024, 0.59646, 0.54766, 0.51316, 0.50741, respectively, each below its analytic bound and below 16/21. These floating-point computations are diagnostic; the elementary analytic proof of the uniform bound is given above. Full results are saved in `second_checks.json`.

On 2026-10-12, `lake env lean ~/brain_workers/TRIO_1011/op/F0084/FlowCheck.lean`, run from `~/lean_verify`, completed with exit code 0 and no Lean errors. The shared-machine wrapper waited 420 seconds for slot 0 before running. The earlier session handle was unavailable after continuation, with no result observed, so the command was resubmitted once. The checked file explicitly imports only `Mathlib.Data.Real.Basic` and `Mathlib.Tactic.Linarith`; it contains no `sorry`, `native_decide`, or custom axiom.

The two kernel-checked lemmas are `exclusive_flow_bound` (the real-valued weighted-flow inequality) and `dyadic_contraction_bound` (the finite induction). The continuum stability, mass-transport and probability arguments are the complete prose proof above, not claims of Lean formalization. Final record validation also passed. There is no remaining gap for the stated upper bound; the sharp asymptotic tail is outside what is proved here.
