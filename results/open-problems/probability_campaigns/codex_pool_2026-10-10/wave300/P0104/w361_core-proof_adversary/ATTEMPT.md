# P0104 adversary attempt

## Source and scope

The recovered intake points to Auffinger--Damron--Hanson, *50 years of first passage percolation*, Questions 13 and 15. In the currently fetched November 8, 2015 PDF these are on printed page 37 (zero-based PDF page 36); the intake's page 34/40 locators do not identify the questions in this version. Section 3.1 expressly leaves several meanings of variance scaling possible.

Question 13 asks for chi<1/2 in dimensions d>=2 under suitable distributional conditions and chi=1/3 in dimension two. Question 15 asks for positivity in suitable dimensions. The source does not specify one complete universal hypothesis package. Source: https://www.math.northwestern.edu/~auffing/FPPSurvey.pdf, Section 3.1, equation (3.1), and Questions 13/15.

For a precise slice, use w360's working model: iid Uniform[1,2] weights on undirected nearest-neighbour Z^2, T_n=T(0,n e1), with target Var(T_n)=n^(2/3+o(1)). This logarithmic variance-exponent statement is one of the scaling interpretations discussed by the source. It does not include the full generality of Question 13 or fix an exponent in every dimension.

The April 2026 polynomial variance theorem concerns an isotropic Riemannian field on R^2: https://arxiv.org/html/2604.01214v1, Theorem 1. Current October openness remains UNKNOWN; no novelty or full-target solution is claimed.

## Independent result before the paired proof

INDEPENDENT_OBSTRUCTION.md was saved before reading w360's proof. It gives a finite square counterexample to independent selected costs, the exact rank-one selection-likelihood premise that would repair that inference, and a continuous tie-free control. All 16 discrete environments passed exact verification. This obstruction does not attack a valid product-space resampling argument.

## Independent derivation of the replacement-threshold kernel

Let a finite connected graph have independent Uniform[1,2] weights and fixed distinct terminals. Paths are simple; positive weights justify this. For edge e and the other coordinates eta, let A_e be the minimum cost over terminal paths avoiding e and B_e the minimum cost of a terminal path containing e after omitting e's own weight. Empty minima are +infinity. If B_e is infinite the passage time is constant in this coordinate. Otherwise

T(u,eta)=min(A_e(eta),B_e(eta)+u).

Let a_e(eta)=clip(A_e-B_e-1,0,1), with a=0 when B_e is infinite and a=1 when A_e is infinite. The centered coordinate projection D_e T=T-E_e T is therefore h_a(u-1)-E h_a(V), where V is Uniform[0,1] and h_a(v)=min(v,a).

For 0<=a<=b<=1, direct integration gives

K(a,b)=Cov(h_a(V),h_b(V))=a^2[b(2-b)/4-a/6].

For the other order exchange a,b. Indeed E h_a=a-a^2/2 and E(h_a h_b)=ab-ab^2/2-a^3/6. Subtracting the product of means gives the displayed formula. K is nonnegative by the covariance identity with an independent V': 2K=E[(h_a(V)-h_a(V'))(h_b(V)-h_b(V'))]. Cauchy--Schwarz gives K<=1/12 because Var h_a<=Var V=1/12 (the same identity and the 1-Lipschitz property give this bound). K(a,0)=0 and K(1,1)=1/12.

This calculation is independent of geodesic selection and agrees with off-edge thresholds. It is a standard finite-product calculation, author proved, pending referee w362. It needs the paths to use e at most once; defining B_e using unrestricted repeated-edge walks would invalidate that representation.

## Most important normalization audit

Let E_e be averaging over coordinate e, D_e=I-E_e, and P_t the semigroup in which every coordinate is independently retained with probability exp(-t) and otherwise replaced by an independent sample. In a coupling of eta and eta^t, only the other coordinates are resampled. Then

E[D_e T(X) D_e T(X^t)]=exp(-t) E K(a_e(eta),a_e(eta^t)).

Reason: conditional on the off-edge pair, if coordinate e is retained it is the same uniform variable in both centered factors and yields K. If replaced the two factors have independent centered uniform inputs and yield zero. The retention flag is independent of the off-edge coupling. This is a derived joint structure, not an assumption about costs on a selected path.

Consequently the finite-product variance identity is

Var(T)=integral_0^infinity exp(-t) sum_e E K(a_e(eta),a_e(eta^t)) dt.

To verify the identity without informal differentiation, decompose T into its finitely many orthogonal Hoeffding projections T_S. The semigroup multiplies T_S by exp(-|S|t). Thus sum_e E[D_e T P_t D_e T]=sum_{S nonempty}|S| exp(-|S|t)||T_S||_2^2. Integration gives sum_{S nonempty}||T_S||_2^2=Var(T). All sums are finite, and T is bounded; no limiting graph or interchange issue is hidden here.

Minimal failure control: a graph with one edge has T=U, a_e=1, K=1/12. Omitting the exp(-t) factor makes the proposed infinite-time integral infinite, whereas Var(T)=1/12. Using resampling probability p=1-exp(-t) as the integration variable absorbs the factor into dp; it must not be counted twice. This is an audit control, not a claim that w360 has omitted the factor.

## Single hardest missing lemma and attempted route

For the precise Uniform[1,2] lattice slice, w360's exact finite-box reduction is valid: paths of more than 2n edges cost more than the direct route, and leaving [-2n,2n]^2 takes at least 2n+1 edges. This removes the infinite-volume technical issue.

Set H_n(t)=sum_e E K(a_e(eta),a_e(eta^t)) on that finite graph. The required input is a quantified, two-sided estimate for the integrated correlated thresholds:

for every epsilon>0 there are c_epsilon,C_epsilon>0 and n_epsilon such that, for all integer n>=n_epsilon,

c_epsilon n^(2/3-epsilon) <= integral_0^infinity exp(-t) H_n(t) dt <= C_epsilon n^(2/3+epsilon).

This estimate is equivalent to the variance-exponent target under the proved identity, so renaming it is not progress on the open input. One normalization trap is important: H_n(t) need not tend to zero. Its limit is the first-order Hoeffding energy L_n=sum_e ||T_{n,{e}}||_2^2. The exact decomposition is

H_n(t)=L_n+sum_{|S|>=2}|S| exp(-(|S|-1)t)||T_{n,S}||_2^2,

so R_n(t)=H_n(t)-L_n is nonnegative. The variance identity becomes Var(T_n)=L_n+integral_0^infinity exp(-t)R_n(t)dt. In the binary square verification L=1/4 and R(t)=(3/16)exp(-t)+(1/16)exp(-3t); the resulting variance is 1/4+3/32+1/64=23/64. Any bound H_n(t)<=C n F(n^(1/3)t) for ALL t with integrable F and a positive floor L_n is impossible. I corrected that proposed sufficient input before submission.

A correctly stated sufficient stronger route is: L_n<=C n^(2/3); R_n(t)<=C n F(n^(1/3)t) for all t>=0 for a nonnegative integrable F; and H_n(t)>=c n for 0<=t<=c' n^(-1/3). Substitution gives the upper bound C n^(2/3)(1+integral F) and the lower bound c c' exp(-c') n^(2/3). Constants must be uniform in n. These are unproved inputs, and the lower persistence estimate is indispensable. The first-order estimate itself asks for a quantitative bound on the squared edge influences; it is not supplied by product independence.

The threshold kernel itself supplies only 0<=K<=1/12. Without geometry the finite box has O(n^2) edges; charging pivotal edges to a geodesic can recover an O(n) scale, but gives no n^(-1/3) decorrelation time. Qualitative decay as t grows cannot furnish an n-dependent power. A lower bound only on H_n(0) also has zero integration measure and needs a proved persistence interval. The straight one-edge/series control has no threshold decorrelation at all. These are concrete obstructions to deriving the missing scaling from product structure alone.

The prior variance-growth scar shows why a bootstrap using an unproved fine-to-coarse variance ratio is circular. The prior gap/overlap scar shows why an avoidance-gap estimate can merely rename the needed chaos event. Neither scar is promoted to an impossibility result for every route.

## Paired-proof verdict at the received checkpoint

At the first received checkpoint w360 supplied only C1 and a statement of the remaining resampling gap. C1 survives the boundary, positivity, and quantifier checks. No corridor independence is asserted. The next packet must include the retention normalization, treatment of empty path classes, and the actual quantitative H_n estimates. No full-target proof is present at that checkpoint.

NEXT: Audit w360's completed kernel identity against the retention factor, then have w362 check the finite counterexamples and independent kernel derivation.
