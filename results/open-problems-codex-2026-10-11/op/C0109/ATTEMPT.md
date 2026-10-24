# C0109 — checked scope and partial lower bound

Date: 2026-10-11. No complete answer to the open problem is claimed.

SECOND-PASS UPDATE: DIRECT_UPPER.md now proves an explicit nonoptimal
upper rate in the source metric, beta=e/(12+4e), e=min(eps,1), with
a log n factor and overwhelming probability. SECOND_ATTEMPT.md proves
unconditional truncation stability. SECOND_APPROACHES.md records the two
new routes. The matching optimal exponent remains unresolved.

## Source and precise interpretation

Tao–Vu, arXiv:0810.2994v3, Section 6, printed/PDF p.22 says:

> Circular Law. A natural question here is to investigate the rate of convergence. In [54], we observed that under the extra assumption that the (2 + ε)-moment of the entries are bounded, we can have rate of convergence of order n−δ, for some positive constant δ depending on ε. The exact dependence between ε and δ is not clear.

The surrounding model is a SINGLE complex (possibly real) entry law x,
iid across entries, with mean zero and unit variance; normalization is
n^(-1/2). The source does not literally ask for an “optimal” exponent in
that paragraph and leaves the metric and rate probability quantifiers
implicit. Its cited [54], Tao–Vu arXiv:0708.2895v5, p.4 explicitly
specifies almost-sure eventual rates in the uniform southwest-rectangle
metric. This identifies the intended interpretation. This attempt uses

    d_K(mu,nu) = sup_{s,t in R}|mu({Re z<=s, Im z<=t})-nu(same set)|.

We also use ball discrepancy D_B, and W_1. These are distinct metrics.
No conclusions about the rate of the mean ESD are inferred from the
almost-sure random-ESD lower bound below.

## Published input (not a solution of C0109)

Götze–Jalowy, arXiv:1807.00489v3, Theorem 7, p.6, gives
d_K <= n^(-1/2+eta) with probability >=1-n^(-Q), for sufficiently
large n, under condition (A) on p.4. In its iid real specialization,
the entries are centered, variance one, and have every absolute moment
finite. We use it only for one fixed all-moments law at each induction
stage. Its threshold can depend on that law, eta, and Q. We do not
assume a threshold uniform across stages. Jalowy, arXiv:2111.03595v3,
Theorem 1, p.2 gives the analogous W_1 bound under all moments.

## Proposition: a fixed-law moment-dependent lower obstruction

For every 0<eps<2/3 there exist a SINGLE real law X with
E X=0, E X^2=1, E|X|^(2+eps)<infinity, and deterministic n_j increasing
to infinity, such that for iid-entry matrices M_n with law X,
almost surely, for EVERY delta>alpha=2eps/(2+eps),

    n_j^delta d_K(mu_{M_{n_j}/sqrt(n_j)},mu_circ) -> infinity.

This holds for any coupling of the matrices across different sizes.
The same assertion holds for D_B and W_1 (proved below).
In particular a universal exponent larger than alpha cannot hold even
with law-dependent finite constants, in probability, almost surely, or
for the expectation of these random distances. This is a lower bound
on possible exponents, not a matching rate theorem or full answer.

### Complete construction and proof

Put p=2+eps and a_j=2^(-jp). Let delta_j=alpha+1/j. Choose real

    max(eps/delta_j,2eps)<b_j<p/2,
    eps/b_j<beta_j<1/2.

These intervals are nonempty: eps/delta_j<p/2 by delta_j>2eps/p,
and 2eps<p/2 is exactly eps<2/3. Consequently
2b_j-p<0, b_j beta_j-eps>0, and b_j delta_j-eps>0.

Let G be a standard real Gaussian. For j>=1 define independent Y_j,
independent of G, with probabilities

    P(Y_j=R_j)=P(Y_j=-R_j)=q_j/2,
    P(Y_j=0)=1-q_j,
    q_j=a_j R_j^(-p),  R_j>=1.

The amplitudes R_j are chosen sequentially. Before choosing R_j,
S_j=G+sum_{k<j}Y_k is a fixed law with all moments finite, mean zero,
and variance s_j=1+sum_{k<j}v_k, where v_k=a_k R_k^(-eps).
Apply the published input to S_j/sqrt(s_j), with eta_j=1/2-beta_j>0
and Q=2. There is a finite N_j such that at every n>=N_j its normalized
matrix ESD nu_{j,n} satisfies

    P(d_K(nu_{j,n},mu_circ)>n^(-beta_j))<=n^(-2).

Choose R_j so large that n_j=floor(R_j^(b_j)) satisfies ALL of

    n_j>=max(N_j,2^j,n_{j-1}+1),
    n_j^(-beta_j)<=v_j/200,
    n_j^(delta_j) v_j>=j,
    n_j^2 q_j<=2^(-j-2),
    q_j<=q_{j-1}/2   (j>1).

This is possible: floor(R^b)/R^b ->1; the three powers controlling
the middle constraints have signs b beta-eps>0,
b delta-eps>0 and 2b-p<0. The last inequality also follows as R->infinity.
N_j and the previous q's have already been fixed. This verifies the
induction without circular dependence on a future law or its constants.

The sum S=G+sum_{j>=1}Y_j exists almost surely, since sum q_j<infinity
and only finitely many Y_j are nonzero almost surely (Borel–Cantelli).
It also converges in L^p: ||Y_j||_p=a_j^(1/p)=2^(-j), and Minkowski
makes the partial sums Cauchy. Their L^p limit is the same almost-sure
sum. Thus E|S|^p<infinity, E S=0, and by L^2 convergence and independence

    s=E S^2=1+sum_j v_j,
    1<=s_j<=s<2,

since sum_j a_j=1/(2^p-1)<1. Define X=S/sqrt(s), once and for all.
It has the required normalization and moment. In fact
||X||_p<=||G||_p+1, so its p-th moment is bounded by
(||G||_p+1)^p, a constant depending only on eps, independently of
the amplitudes and chosen rate thresholds. The obstruction therefore
persists even inside a quantitatively moment-bounded class. Its law
does not vary with n.

At size n_j realize each entry with an independent copy of the whole
sequence (G,Y_1,Y_2,...). Couple the full matrix X to its past-only
counterpart S_j/sqrt(s). They agree entry by entry on E_j, the event
that every Y_k with k>=j is zero in every entry. Union bound gives

    P(E_j^c)<=n_j^2 sum_{k>=j}q_k<=2 n_j^2 q_j<=2^(-j-1),

using the enforced geometric decrease of q_k. No eigenvalue perturbation
estimate is used: the matrices are exactly equal on this event.

Put t_j=s-s_j=sum_{k>=j}v_k>=v_j, and r_j=sqrt(s_j/s).
Then 1/sqrt(2)<=r_j<=1 and

    1-r_j=t_j/[s(1+r_j)]>=t_j/4>=v_j/4.

Let mu_r be uniform on the disk of radius r. Scaling both coordinates
of every southwest rectangle by r shows that

    d_K((z->r z)_#nu,mu_r)=d_K(nu,mu_circ).

Thus on E_j and the all-moments good event, the full ESD mu_j has
d_K(mu_j,mu_{r_j})<=n_j^(-beta_j)<=v_j/200.

Use the FIXED rectangle Q_0={Re z<=1/2, Im z<=2}. For every r in
[1/sqrt(2),1], the upper imaginary bound includes the whole disk.
If H(u) is the real marginal CDF of mu_circ, then

    mu_r(Q_0)-mu_circ(Q_0)=H(1/(2r))-H(1/2).

The density is H'(u)=(2/pi)sqrt(1-u^2) for |u|<1, by integration of
the vertical chord of the disk. On [1/2,1/(2r)] subset [1/2,3/4],
this density is at least 1/4 (pi<4 and sqrt(1-u^2)>=sqrt(7)/4>1/2).
Consequently

    mu_r(Q_0)-mu_circ(Q_0)
      >= (1/8)(1/r-1) >= (1-r)/8 >= t_j/32.

On both good events the empirical mass of Q_0 therefore exceeds its
circular-law mass by at least v_j/32-v_j/200>=v_j/64. Hence

    P(d_K(mu_j,mu_circ)>=v_j/64)
      >=1-2^(-j-1)-n_j^(-2).

The failure probabilities are summable. Borel–Cantelli needs no
independence across j, so this inequality holds eventually almost surely
under every coupling across sizes. For any delta>alpha, eventually
delta>=delta_j and n_j^delta v_j>=n_j^delta_j v_j>=j. Multiplication
proves the assertion, simultaneously for every such real delta.

If n^delta d_K were tight, its subsequence could not tend to infinity
in probability. Almost-sure O(n^(-delta)) is likewise contradicted.
For expected random distance, E d_K>= (v_j/64)(1-o(1)), giving the
same divergence after multiplication. These conclusions allow constants
depending arbitrarily on the fixed law.

### Ball discrepancy and W_1 versions

Apply Jalowy's W_1 theorem to each past law in the induction instead
(or require both published bounds when choosing N_j). Scaling has
W_1((r z)_#nu,mu_r)=r W_1(nu,mu_circ)<=W_1(nu,mu_circ).
The fixed test f(z)=min(|z|,1) is bounded by one and 1-Lipschitz.
Under mu_r its integral is 2r/3, whereas under mu_circ it is 2/3,
by the radial density 2u on [0,1]. Thus, on both good events,

    |int f d(mu_j-mu_circ)|
       >= (2/3)(1-r_j)-v_j/200 >= v_j/6-v_j/200 >= v_j/8.

Any coupling proves W_1>=the absolute difference of integrals of this
test. Also f(z)=int_0^1 1_{|z|>u} du. Fubini implies the same absolute
difference is at most D_B, since complementary centered disks have the
same signed mass discrepancy as centered disks. Open/closed disks only
differ at a countable set of radii for a finite measure, which does not
affect the integral. The construction with both thresholds gives all
three metric assertions for the SAME fixed law and same subsequence.
The test also proves the analogous bounded-Lipschitz obstruction (up to
the convention-dependent factor two in its norm).

## Hostile referee checks

1. No n-dependent law: the recursive choices define one infinite sequence
   and one final variance; matrices at all sizes use the same X.
2. Tail absence concerns n^2 entries, not n entries. It forces b<p/2;
   ignoring this would produce the unsupported exponent eps/(2+eps).
3. Finite p-moment follows from the summable L^p norms, not merely from
   summability of variances or probabilities.
4. The all-moments law used in stage j is fixed BEFORE R_j is chosen.
   Its rate threshold may be arbitrarily large; the construction absorbs it.
5. The finite-past law is normalized by its OWN variance to apply the
   published input. Only afterwards is it rescaled by r_j.
6. All-moments thresholds for both metrics can be satisfied together by
   taking their maximum. The good-event failures add at most 2n_j^-2,
   still summable; replace the single failure term above by this when
   requiring the simultaneous three-metric statement.
7. A positive pointwise bias on one event does not establish a bias for
   E mu_n: bad-event cancellation could exceed the deficit. Only the
   expectation of the nonnegative random distance is claimed.
8. eps=2/3 is NOT covered: b>2eps and b<p/2 become incompatible.
   No endpoint assertion is made.
9. A scalar truncation upper estimate is NOT an optimality theorem.
   This argument adds exact entrywise coupling and an actual separating
   spectral statistic; it does not repair any claimed upper bound.

## Other checked special case and remaining gap

### Boundary eps=0: no positive universal exponent under finite variance

There is a single centered variance-one real law with finite second
moment for which n_j^delta d_K tends to infinity almost surely along
one subsequence, for every delta>0. Moreover this law has no finite
(2+eta)-moment for any eta>0.

Here is the complete adaptation. Set a_j=4^(-j), b_j=1/2,
beta_j=1/4, delta_j=1/j, q_j=a_j/R_j^2, v_j=a_j. Choose R_j
recursively using the fixed-past all-moments threshold and exactly the
five constraints of the earlier construction, and additionally
R_j>=2^(j^2). Such choices exist because as R->infinity,
n=floor(sqrt(R)) tends to infinity, n^-1/4/v_j tends to zero,
n^(1/j)v_j tends to infinity, and n^2 q_j<=a_j/R tends to zero.
The geometric decrease of q_j can also be enforced. Define independent
Gaussian G and the same sparse symmetric Y_j, and S=G+sum Y_j.
The L^2 norms of Y_j are 2^-j, hence their sum converges in L^2;
sum q_j<infinity gives the same almost-sure sum. Its mean is zero and
variance s=1+sum v_j=4/3. Normalize X=S/sqrt(s).

The whole-matrix tail-absence probability is again at least
1-2^(-j-1), the past-law rectangle discrepancy is at most v_j/200
except on an event of probability n_j^-2, and the disk radius satisfies
1-r_j>=v_j/4. The identical fixed-rectangle integration therefore gives
d_K>=v_j/64 except for summable failures. Borel–Cantelli and
n_j^(1/j)v_j>=j prove divergence for every delta>0, as delta>=1/j
eventually. This completes the finite-second-moment lower-bound proof.

For any eta>0, if E|S|^(2+eta) were finite, conditional Jensen given
Y_j would give E|S|^(2+eta)>=E|Y_j|^(2+eta), since S-Y_j is independent
of Y_j, integrable, and centered. The latter expectation equals
4^-j R_j^eta >=2^(-2j+eta j^2), which is unbounded as j->infinity.
This contradicts the assumed finite value. Dividing by sqrt(s) does
not change this failure of higher moments. Thus this boundary law
does not satisfy the positive-eps hypothesis and is not a counterexample
to a positive-eps polynomial-rate theorem.

For any empirical measure on at most n complex points, W_1 to mu_circ
is >=2/(3sqrt(n)). Indeed if A is its support, every coupling costs
at least int dist(z,A) dmu_circ(z). The union of n disks of radius u
has mu_circ mass <=n u^2. Layer cake, integrated from 0 to 1/sqrt(n),
gives int_0^(1/sqrt(n))(1-nu^2)du=2/(3sqrt(n)). This is solely a
Wasserstein geometric lower bound, not a Kolmogorov one. Together with
Jalowy Theorem 3, it confirms exponent 1/2 in expected W_1 for complex
Ginibre. It does not answer the weak-moment dependence.

The full question remains unresolved here: the second pass proves the
nonoptimal upper rate in DIRECT_UPPER.md, but no MATCHING upper rate for
all iid laws under a finite (2+eps)-moment has been proved, and no proof
that 2eps/(2+eps) is the sharp exponent for eps<2/3 is available. Nor is
there a matching weak-moment rate at eps>=2/3. The cited original paper
identifies the metric and probability quantifiers as above; the remaining
gap is mathematical. The numerical/formal checks below
verify only auxiliary steps, never the full stochastic theorem.
