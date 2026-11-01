# C0036 research record

Date: 2026-10-12 (Asia/Jerusalem; API timestamps may be 2026-10-11 UTC).

## Exact question and present outcome

Let Gamma be a discrete countable group, Q a bounded Gamma-equivariant self-adjoint
operator on ell²(Gamma), and 0 <= Q <= I. The determinantal law mu_Q is defined by
mu_Q[A subset X] = det Q_A for every finite A. With the normalized group trace
tau(T)=<T delta_e,delta_e>, put FK(Q)=exp(tau(log Q)), interpreting exp(-infinity)=0.
The question is whether

    Bern(FK(Q))^Gamma <=st mu_Q <=st Bern(1-FK(I-Q))^Gamma

and whether these parameters are optimal for each Q. This is exactly Lyons 2014,
Conjecture 5.7, printed p.23, not merely an operator-order comparison. On a finite
group of size n, FK(Q)=(det Q)^(1/n).

No complete proof or counterexample to that statement has been obtained here.
The literature search has not identified a matching published solution, and
rate limits prevent a conclusive citation search. The results below are partial.

## 1. Finite optimality is necessary, with no equivariance assumption

For any positive contraction Q on n>=1 sites, if mu_Q dominates iid density p,
the increasing event that every site is present gives det Q >= p^n. Hence
p <= (det Q)^(1/n). Complementing all coordinates turns mu_Q into mu_(I-Q),
because its finite absence probabilities are det(I-Q)_A (inclusion-exclusion
or the determinant expansion). If mu_Q is dominated by iid density q, this
gives (1-q)^n <= det(I-Q), hence q >= 1-(det(I-Q))^(1/n).
Thus once finite sufficiency is proved, optimality follows automatically.
This is necessity only; it is not the conjecture's sufficiency.

## 2. Full geometric-mean comparison of cardinalities

### Lemma: pair smoothing

If u,v in [0,1] and r=sqrt(uv), then

    Bern(u)+Bern(v) >=st Bin(2,r).

Proof: the only nontrivial thresholds of these integer-valued random variables
are 1 and 2. The probabilities at threshold 2 are both uv=r². At threshold 1,
they are u+v-uv and 2r-r²; their difference is u+v-2sqrt(uv)>=0, since
(sqrt(u)-sqrt(v))²>=0. Thresholds outside {1,2} are immediate.
Adding an independent integer-valued variable preserves stochastic order:
for every threshold k condition on its value z and compare thresholds k-z.

### Theorem: geometric-mean binomial bounds for any finite DPP

Let lambda_1,...,lambda_n be the eigenvalues of Q, p=(product lambda_i)^(1/n),
and h=(product (1-lambda_i))^(1/n). Then

    Bin(n,p) <=st |X| <=st Bin(n,1-h), X~mu_Q.

Proof of the spectral count identity: for z real,
z^|X|=product_i(1+(z-1)1_{i in X}). Taking expectations, expanding the product,
and using the defining inclusion probabilities gives
E z^|X|=sum_A (z-1)^|A| det Q_A=det(I+(z-1)Q)
=product_i (1-lambda_i+lambda_i z). This is the probability-generating
polynomial of the sum of independent Bern(lambda_i) variables, so the laws agree.

If any lambda_i=0 then p=0 and the lower comparison is immediate. Otherwise
write x_i=log lambda_i<=0. Repeatedly replace a largest and a smallest x_i by
their arithmetic mean, equivalently replace their Bernoulli parameters by
their geometric mean. Each step lowers the count law in stochastic order by
the pair lemma, and preserves sum x_i. For completeness, this sequence converges
to the constant vector: let xbar=(sum x_i)/n and V=sum_i(x_i-xbar)². A step
decreases V by (max x_i-min x_i)²/2. Since xbar lies between the extremes,
V<=n(max x_i-min x_i)², so V_new <= (1-1/(2n))V. For n=1 no steps are needed.
Thus V tends to zero, every parameter tends to p, and each of the finitely many
tail probabilities converges by polynomial continuity. The initial law therefore
dominates Bin(n,p). Apply this result to I-Q and to n-|X| to get the upper bound.
This proof includes lambda_i=1, and no group hypothesis was used.

## 3. Full sharp bounds for exchangeable DPPs

### Theorem

If mu_Q is invariant under every permutation of its n sites, then it satisfies
the full two-sided conjectured product bounds, including optimality.

Proof: by exchangeability, conditional on |X|=k, X is uniform on the k-subsets
(if that count has positive probability). The preceding theorem compares
the cardinality laws. Couple a binomial count M and a DPP count N so M<=N:
take a uniform U on (0,1), and for each count law use its generalized inverse
distribution function at U. The stochastic tail order implies the stated
inverse inequality, since the larger law has the smaller distribution function.
Independently take a uniform random permutation pi of the sites, and set
Y={pi(1),...,pi(M)} and X={pi(1),...,pi(N)}. These sets have the correct laws:
uniform subsets conditional on their counts; the binomial/uniform mixture is
exactly iid Bern(p). Also Y subset X. The analogous count coupling with the
upper binomial law gives the upper bound. Section 1 proves optimality.

In particular, Q=aI+b11* with real a,b and eigenvalues a (multiplicity n-1)
and a+nb in [0,1] is invariant under all permutations, so this theorem applies.
This gives kernels on every finite group, including nonabelian groups, but is
only a special family of equivariant kernels.

Every equivariant kernel on groups of order <=3 also gives an exchangeable law.
For order 2 the two singleton minors agree. For order 3 the three singleton
minors agree and the group acts transitively on the three unordered pairs,
so all equal-size principal minors agree. The determinant for size 3 is unique.
The inclusion-exclusion formula
mu_Q[X=S]=sum_(T subset E\S) (-1)^|T| det Q_(S union T)
then depends only on |S|, proving exchangeability. Order 1 is immediate.
These small cases and the cardinality theorem are also present in earlier private
work; they are independently reconstructed here, with no novelty claim.

## 4. Rechecked harmonic-mean lower bound (finite groups)

Assume first 0<Q<I, and put J=Q(I-Q)^(-1)>0. The exact-set law is
mu_Q[X=B]=det(I-Q)det J_B. One can prove this by expanding the generating
polynomial det(I-Q+QZ), factoring I-Q, and comparing coefficients of
product_(i in B) z_i; Q and I-Q commute. For e outside B,

    P(e in X | X\{e}=B) = s_B/(1+s_B),
    s_B = J_ee-J_eB J_B^(-1)J_Be.

The Schur complement equals the minimum of (delta_e+v)*J(delta_e+v) over v
supported in B (complete the square). Enlarging B enlarges the minimization
domain, so s_B decreases. At B=E\{e}, the block inverse formula gives
s_min=1/(J^(-1))_ee. Since J^(-1)=Q^(-1)-I, the minimum probability is
1/(Q^(-1))_ee, not s_min. Equivariance makes the diagonal of Q^(-1) constant,
so this probability equals HM(Q)=n/(sum_i 1/lambda_i).

Enumerate the sites. Every conditional probability given previous coordinates
is an average of full-rest conditional probabilities, hence is at least HM(Q).
Sample sequentially with independent uniform variables U_i: set X_i=1 iff
U_i<=P(X_i=1 | previous X), and Y_i=1 iff U_i<=HM(Q). Then X has law mu_Q,
Y is iid Bern(HM(Q)), and Y subset X coordinatewise. Complementation gives
the upper density 1-HM(I-Q). Endpoint cases follow by replacing Q by
epsilon I+(1-2epsilon)Q and passing to a convergent subsequence of the finite
coupling simplex; take HM=0 when an eigenvalue is zero.

This is strictly weaker than geometric-mean domination. For example,
Q=[[1/2,1/4],[1/4,1/2]] has minimal full-rest conditional probability 3/8,
whereas FK(Q)=sqrt(3)/4>3/8. A full-rest conditional test cannot prove FK
even in a case where the desired stochastic order holds.

## 5. Failed route: group averaging of heterogeneous product laws

For any ordering of a finite invertible Q, put A_i={first i sites} and
d_i=det Q_(A_i)/det Q_(A_(i-1)). All these numbers lie in (0,1], with product
det Q. The Schur complement gives the inclusion probability of site i
conditioned on all previous sites being present. More generally, conditioning
some previous sites absent increases the conditional kernel relative to having
all of them present. Here are the conditioning identities in detail. Conditioning
B present replaces Q on the remaining sites by its Schur complement K: the
identity P(A present | B present)=det Q_(A union B)/det Q_B=det K_A proves this
for each finite A. For a further disjoint set C conditioned absent and A outside C,
inclusion-exclusion gives the numerator sum_(T subset C)(-1)^|T|det K_(A union T).
Expansion in the C columns identifies this sum with

    det [[K_A,K_AC],[-K_CA,I_C-K_C]].

Indeed, choosing identity columns at C\T leaves the principal block A union T,
with a factor -1 in each remaining C row, producing exactly (-1)^|T|det K_(A union T).
Schur complementation at the invertible block I_C-K_C expresses the same
determinant as det(I_C-K_C)det(K_A+K_AC(I_C-K_C)^(-1)K_CA). Dividing by the
absence probability det(I_C-K_C) proves the conditional-kernel formula.
In particular its diagonal at i is K_ii+K_iC(I-K_C)^(-1)K_Ci>=K_ii.
Conditioning C present instead gives K_ii-K_iC K_C^(-1)K_Ci<=K_ii.
The inverses exist in the strict finite case; all added/subtracted terms are
nonnegative quadratic forms.
Thus for 0<Q<I every sequential conditional probability is at least d_i.
The uniform-variable construction gives mu_Q >=st product_i Bern(d_i).
For equivariant Q, translating that comparator and averaging preserves this
domination. An attractive missing step would say that the translation average
of ANY heterogeneous product law dominates iid density (product d_i)^(1/n).
That proposed universal lemma is false; the exact certificate is recorded below.
It does not refute Lyons: attainable pivot vectors from equivariant Q have
additional constraints that were not tested by this product-law counterexample.

## 6. Computational scope and the remaining gap

`finite_search.py` constructs genuinely equivariant complex Hermitian kernels
on C6, S3 and D4 by Q_(g,h)=f(g^(-1)h), symmetrizes, and applies a spectral
affine map into (0,1). Since all these operations commute with left translations,
the result is a valid equivariant positive contraction. Exact-set probabilities
are obtained by Boolean Mobius inversion of inclusion determinants, independently
of the L-ensemble formula. For both Q and I-Q the comparator density is the
geometric mean of the computed eigenvalues.

For each comparison the LP minimizes sum_S (mu_Q(S)-nu_p(S)) y_S, subject to
0<=y_S<=1 and y_S<=y_(S union {i}). Its vertices are upper-set indicators:
if y is feasible then y_S=integral_0^1 1_{y_S>=t}dt, and each level set is upper.
Thus a negative optimum witnesses a violated increasing event. This is an exact
reduction, but the numerical solves and determinants are floating point.

190 kernels (30 on C6, 100 on S3, 60 on D4), 380 comparisons, produced no
violation beyond roundoff (worst rounded gap about -4.44e-16). This is numerical
evidence only, not a proof. The largest LP uses 256 variables and 1024 cover
constraints; the run took about 19 seconds after initialization and used far
less than 1GB. `finite_results.json` preserves all results and RNG seed is in
the script. Nonempty/nonfull upper sets may have strict gaps; the LP's trivial
empty set makes a zero optimum unsurprising when the domination holds.

Remaining gap: for a general equivariant Q, compare arbitrary increasing events
that depend on the arrangement of occupied sites, not only their number.
The cardinality law does not determine these probabilities. Exchangeability is
not implied by regular group equivariance on larger groups. The false averaging
lemma cannot bridge the gap. No assertion here establishes optimality on arbitrary
infinite nonamenable groups either. These are precisely unproved parts of the
original question; this attempt remains PARTIAL.

## 7. Exact obstruction to group averaging

The proposed universal product-law averaging lemma in Section 5 is false.
Index six coordinates by Z/6Z. Use independent presence probabilities

    r=(11/50,4/5,5/8,19/20,5/16,85766121/133760000).

Their product is (21/40)^6: the first five have product 209/6400, and the last
is (21/40)^6 divided by that number. All six probabilities lie strictly between
zero and one. Let U contain all configurations with at least five present sites,
and the four-site configurations whose two absent sites have cyclic distance
1 or 3. Adding a site to an accepted four-site configuration gives five sites,
so U is increasing. Cyclic distance is preserved under translation, so U is
translation invariant. With bit i denoting site i, its complete mask list is

    15,27,30,31,39,45,47,51,54,55,57,59,60,61,62,63.

For the heterogeneous product law eta, summing the sixteen rational terms
product_i(r_i if bit i of s is 1, else 1-r_i) gives exactly

    eta(U) = 1225976459083/4280320000000,
    Bern(21/40)^6(U) = 295805601/1024000000,
    difference = -10490953097/4280320000000 < 0.

The iid expression can also be obtained as
9 p^4(1-p)^2+6 p^5(1-p)+p^6, p=21/40: nine admissible four-site sets,
six five-site sets, and one six-site set. Translation invariance implies
(g eta)(U)=eta(U), so averaging all six translates keeps the same violation.
`exact_symmetrization_obstruction.json` stores this exact certificate, and
`verify_results.py` independently checks the mask closure, invariance and sums.
This does not refute Lyons: no representation by an equivariant determinantal
kernel or its Schur-pivot vector has been asserted.

## 8. Inclusion and absence cylinders for arbitrary countable groups

For every equivariant positive contraction Q and finite A,

    det Q_A >= FK(Q)^|A|,
    det (I-Q)_A >= FK(I-Q)^|A|.

Proof: first Q>=delta I>0. Let P project onto ell²(A). For a strictly positive
bounded T, completing the square around T^(-1)v proves

    <v,T^(-1)v> = sup_w [2 Re<v,w> - <w,Tw>].

For v in ran P, restricting the supremum to w in ran P proves
(PTP)^(-1)<=PT^(-1)P, as operators on ran P. Apply this to Q+tI and integrate
the scalar resolvent formula for log via functional calculus:

    log Q_A - P(log Q)P
    = integral_0^infinity [P(Q+tI)^(-1)P-(Q_A+tI_A)^(-1)] dt >= 0.

Near zero the integrand is bounded using delta; at infinity its leading 1/t
terms cancel and it is O(t^(-2)), so the difference integral converges in norm.
Taking the ordinary trace on the finite-dimensional space ran P gives
log det Q_A >= sum_(g in A)<delta_g,log Q delta_g>=|A|tau(log Q).
The equality uses equivariance of functional calculus. Exponentiate.
For a general Q use Q_epsilon=(Q+epsilon I)/(1+epsilon). Finite determinants
converge. The spectral measure of Q at delta_e is a probability measure on
[0,1], and log(t+epsilon) decreases to log t. Monotone convergence after
subtracting a fixed upper bound proves convergence of its integral, including
minus infinity. Subtracting log(1+epsilon) does not change the limit. Hence
FK(Q_epsilon) tends to FK(Q), proving the first inequality by passage to the
limit. Apply it to I-Q for the second. A empty gives the equality 1=1.

Thus every all-present cylinder satisfies the proposed lower comparison,
and every all-absent cylinder satisfies the complementary lower comparison.
Unions involve alternating inclusion-exclusion coefficients; these comparisons
alone do not imply stochastic domination. This standard compression-of-log
consequence is not claimed as a novel theorem.

## 9. Source context and earlier private work

Section 5.2 of the source opens by taking Gamma sofic; Conjecture 5.7 itself
says "For all Gamma-equivariant positive contractions" without restating that
restriction. The intake explicitly requests all groups, which is the formulation
worked on here. Nothing here solves either that formulation or its sofic restriction.
Read-only repository material contains much more than the supplied harmonic-mean
hint: private candidate proofs on cyclic groups through C6 and on S3, including
finite symbolic event certificates and a proposed subgroup-cover method. These
are leads, not published resolutions and not adopted here as established proofs.
In particular, the S3 note labels its full proof candidate pending independent
review. The count theorem is already present in that earlier work. Its proof
above is self-contained and independently checked. See LITERATURE.md for paths.

## 10. Additional endpoint validation

`boundary_checks.py` checked all increasing events by order-polytope LP for
40 exchangeable kernels on n=2,3,5,7,8 sites, including eigenvalues exactly
0 or 1. Both sides passed in all 80 comparisons. A separate direct convolution
check compared 600 Poisson-binomial count laws (including endpoints) with the
geometric-mean binomial law on n=2,3,6,12,20 sites. Worst tail difference was
about -1.44e-15, numerical roundoff. These checks corroborate the written
proofs; they do not replace them. Saved in boundary_results.json and
count_boundary_results.json.

## 11. Formal algebra check and final verdict

`PairBalancing.lean` was checked from ~/lean_verify by
`lake env lean ~/brain_workers/TRIO_1011/op/C0036/PairBalancing.lean`.
The final corrected run exited 0. It imports only the Linarith tactic module and
Real.Basic, uses kernel-checked tactic proofs, and has no sorry or native_decide.
It proves u+v>=2p from nonnegativity and p²=uv, then proves the threshold-one
inequality and threshold-two equality used in the pair-smoothing proof. It does
not formalize a determinantal process, a coupling, or the full conjecture.
The earlier import/instance failures and final harmless linter warning are
recorded in LEAN_CHECK.txt. All substantive remaining gaps are in Section 6.

This research pass is complete with verdict PARTIAL, not SOLVED. A concrete next
mathematical step, if resumed, is to independently audit the earlier private
subgroup-cover certificate on S3 and test whether analogous eventwise subgroup
covers exist for D4. That is a lead toward a general finite-group induction,
not an existing proof of such an induction or of the infinite-group problem.

## 12. Additional serious attempt requested before closure

The full follow-up is in SECOND_ATTEMPT.md, with an independent self-review in
REFEREE_SECOND.md. Two previously unpursued approaches were recorded: scalar
pivotal-derivative analysis and an eventwise D4 subgroup-cover audit. The former
was pursued and led to a stronger proved special case:

For every finite transitive group action on n sites and t in (0,1), every
invariant kernel in an explicitly bounded operator-norm neighborhood of tI
satisfies both optimal geometric-mean iid product bounds. For the regular action
of any finite group, these are precisely the conjectured FK bounds. The proof
handles zero quadratic directions by classifying sites with identical membership
in all minimal accepted sets, obtaining exact block-diagonal equality, and then
controlling the cross-block Hessian uniformly. Formula (7) in SECOND_ATTEMPT.md
gives a conservative radius depending only on n and t.

The result also lifts to countable groups for kernels supported on cosets of
a finite subgroup whose restricted kernel is in the proved neighborhood.
Exact and high-precision checks passed, including 168 monotone-event coefficient
checks, 144 D4 near-flat spatial comparisons, and 1008 all-event comparisons
strictly inside the explicit radius. A nearby nontransitive counterexample
shows why constant row energy cannot replace full transitive symmetry.

The global gap remains: arbitrary equivariant kernels outside these scalar
neighborhoods are not covered, and the radius deteriorates with n, so no general
infinite-group theorem follows by approximation. Overall verdict remains PARTIAL.
