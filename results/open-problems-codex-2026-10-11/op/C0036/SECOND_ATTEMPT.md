# C0036: additional serious attempt

Date: 2026-10-12 local. Status: DONE. Overall verdict: PARTIAL.

The remaining gap in ATTEMPT.md Section 6 is comparison on spatial increasing
events, beyond cardinality or single inclusion cylinders. Full-rest conditional
probabilities reach only the harmonic mean; unrestricted translated-product
averaging is false.

## Two approaches not pursued in the first pass

1. **Pivotal derivatives near a scalar kernel.** Expand the probability of an
   arbitrary increasing event at Q=tI and expand its FK comparator to the same
   order. Use the Russo influence formula and positivity of pivotal events to
   interpret the quadratic difference. The target is full two-sided domination
   for nonexchangeable equivariant perturbations, not just a selected event.
   Investigate zero quadratic directions explicitly, rather than treating a
   positive Hessian on one event as a global theorem.
2. **Eventwise subgroup cover on D4.** Audit the inherited block-Schur reduction,
   enumerate invariant increasing events on the order-eight dihedral group,
   and for each event seek a geometric-mean comparison for a suitable proper
   subgroup-coset product law. This avoids the disproved universal product
   averaging lemma: the subgroup may depend on the event. It could give an
   entire nonabelian finite group, but requires a new exact polynomial certificate
   and a proof of the Schur coupling step.

Approach 1 is selected: its second variation can be derived analytically for
every monotone event and checked independently. Approach 2 remains an untried
alternative in this pass; private S3/D4 leads are not adopted as proved premises.

## Brain consultation

Asked math_recall.py for "determinantal stochastic domination subgroup Schur
complement increasing events" (the actual spatial gap), and for "Russo formula
pivotal influence scalar determinantal perturbation" (the proposed neighbouring
tool). Returned hints and their scope are recorded below.

## Initial derivation (completed proof and review below)

Let E be n sites, 0<t<1, and H a zero-diagonal Hermitian matrix with constant
row sum of squared off-diagonal moduli r. Equivariance under any transitive
permutation action implies this property. For an increasing Boolean event f,
write F(z)=E_(independent Bern(z_i)) f, alpha_i=partial_i F(t,...,t),
beta_ij=partial_i partial_j F(t,...,t), and
b_(i|j0)=E_t[Delta_i f | coordinate j fixed to 0] (the expectation is over
the remaining n-2 coordinates, and Delta_i uses coordinate i fixed to 1/0).

The candidate second-order formula is

    mu_(tI+epsilon H)(f)-nu_((det(tI+epsilon H))^(1/n))(f)
    = epsilon² C_f(H)+O(epsilon³),
    C_f(H)=sum_(i<j) |H_ij|² [b_(i|j0)+b_(j|i0)]/(2t) >= 0.

The determinant expansion gives the kernel term -sum |H_ij|² beta_ij.
The density correction is r/(2t)sum alpha_i. Constant row energy lets it be
redistributed to edges; alpha_i/t-beta_ij=b_(i|j0)/t. No unproved sign of a
mixed influence is assumed.

For an event U, define i~j when i and j have identical membership in every
minimal accepted subset. Nonnegative pivotal probabilities suggest that the
coefficient of |H_ij|² vanishes exactly when i~j. For invariant U this partition
is invariant under the group, and transitivity makes its blocks equally sized.
If a kernel is block diagonal on those blocks, U depends only on block-full
occupancy, and its probability should agree exactly with the FK iid comparator.
Cross-block derivatives of determinant minors vanish at every block diagonal
matrix. These two facts may strengthen the directional expansion to a uniform
open neighborhood theorem. A complete proof and independent checks follow.

## Theorem: the full sharp comparison holds near every finite scalar kernel

Let a finite group G act transitively on a finite set E of n sites. For each
t in (0,1), there is delta>0 such that every G-invariant Hermitian kernel Q
with ||Q-tI||<delta satisfies

    Bern((det Q)^(1/n))^E <=st mu_Q
       <=st Bern(1-(det(I-Q))^(1/n))^E.

Delta can be chosen smaller than min(t,1-t), so Q is automatically a strict
positive contraction. Both densities are optimal. In particular the theorem
applies to every finite Gamma with its regular action, without exchangeability.
The radius depends on the finite action and t; no group-size-independent radius
or arbitrary-distance extension is claimed.

### Proof, step 1: multilinear determinant representation

Every f:{0,1}^E->R has a unique multilinear expansion

    f(x)=sum_(S subset E) c_S product_(i in S)x_i,
    c_S=sum_(T subset S)(-1)^(|S|-|T|) f(1_T).

Indeed, evaluating the first expression at 1_A and substituting the second
leaves sum_(T subset A) f(1_T) sum_(T subset S subset A)(-1)^(|S|-|T|),
whose inner sum is 0 unless T=A and is then 1. Hence it equals f(1_A).
Taking DPP expectations gives mu_Q(f)=sum_S c_S det Q_S. Taking independent
Bernoulli expectations gives F(z)=sum_S c_S product_(i in S) z_i. Thus DPP
event probabilities are polynomials in the real and imaginary matrix entries,
and F and all its partial derivatives can be computed without applying a
product-measure derivative formula to a dependent DPP.

### Proof, step 2: exact second variation

Let H be zero-diagonal, Hermitian, and invariant under the transitive action.
The numbers r_i=sum_(j != i)|H_ij|² are constant: a permutation carrying i to
i' carries its row entries bijectively to those at i'. Write their value as r.
For any S, the identity permutation in det(tI_S+epsilon H_S) contributes t^|S|.
A nonidentity permutation with exactly two moved coordinates is a transposition
(i j), contributing -epsilon² |H_ij|² t^(|S|-2). There is no one-moved-coordinate
permutation, and all others contribute order >=3. Therefore

    mu_(tI+epsilon H)(f)
      =F(t,...,t)-epsilon² sum_(i<j)|H_ij|² beta_ij+O(epsilon³),
    beta_ij=partial_i partial_j F(t,...,t).

For the full determinant the pair sum is nr/2, so

    det(tI+epsilon H)
      =t^n[1-epsilon² nr/(2t²)+O(epsilon³)],
    p(epsilon)=(det(tI+epsilon H))^(1/n)
      =t-epsilon² r/(2t)+O(epsilon³).

The scalar power function is smooth because t>0. Taylor expansion of F along
the diagonal gives the FK-comparator correction
-epsilon² r/(2t)sum_i alpha_i, where alpha_i=partial_i F(t,...,t).

For i != j, let a0=b_(i|j0) and a1=b_(i|j1) be expected finite differences
Delta_i f with j fixed. Directly differentiating the multilinear product law
or conditioning on coordinate j proves

    alpha_i=(1-t)a0+t a1,  beta_ij=a1-a0,
    alpha_i-t beta_ij=a0.

This is the finite Russo identity in elementary form. For increasing f,
a0,a1>=0. Using r constant,

    r sum_i alpha_i = sum_(i<j)|H_ij|²(alpha_i+alpha_j).

Consequently the coefficient of epsilon² in the DPP-minus-comparator gap is

    C_f(H)=sum_(i<j)|H_ij|² gamma_ij,
    gamma_ij=[b_(i|j0)+b_(j|i0)]/(2t)>=0.                 (1)

The second derivative is 2C_f(H). This formula holds for all increasing f,
even ones not invariant under the group. A general mixed derivative beta_ij
can have either sign; no sign assumption about beta_ij was used.

### Proof, step 3: classify all zero coefficients for invariant events

It suffices first to consider invariant increasing events U, with f=1_U.
The empty and full events have identically zero gaps and can be discarded.
Let M(U) be the finite collection of inclusion-minimal accepted subsets. Each
accepted configuration contains one of these sets: repeatedly remove sites
while acceptance remains true. Define i~j iff for every M in M(U),

    i in M iff j in M.

Equality of the finite membership vectors is an equivalence relation. Every
minimal M is a union of its equivalence classes. Thus U is determined by
which of those classes are wholly present: it occurs iff the collection of
wholly present classes contains the classes of at least one minimal M.

We claim gamma_ij=0 iff i~j. All configurations of the n-2 remaining coordinates
have strictly positive probability since 0<t<1. For increasing f, Delta_i f is
0 or 1. Hence b_(i|j0)>0 iff some configuration S excluding i,j obeys
f(S)=0 and f(S union {i})=1. Such a configuration has a minimal accepted
M subset S union {i}; i must belong to M (otherwise f(S)=1), and j does not.
Conversely, if a minimal M contains i and excludes j, choose S=M\{i}; by
minimality f(S)=0 and f(S union {i})=1. Thus

    b_(i|j0)>0 iff some minimal M contains i but not j.

The same argument with i,j reversed proves the claim about gamma_ij.

The equivalence relation is group invariant. Indeed, if i~j and g is in G,
every minimal M has g^(-1)M minimal (invariance and preservation of inclusion),
so gi,gj have identical membership in M. Transitivity on E implies transitivity
on the classes: an element sending any chosen member of one class to a member
of another sends the entire first class onto the second. All classes therefore
have the same size m, with n=km. If there is only one class, the nonconstant
event is precisely {E}, and its gap is det Q-p(Q)^n=0 for every Q.

### Proof, step 4: exact equality on the whole zero-direction subspace

Fix U with at least two equivalence classes. Decompose an invariant Hermitian
perturbation Q-tI=A+B, where A has the entries within the classes (including
the diagonal) and B has the entries between different classes. The group
preserves the partition, so A and B remain invariant. They belong to real
finite-dimensional linear spaces V_in and V_cross, respectively.

If B=0, the kernel Q0=tI+A is block diagonal. The DPP on those blocks is a
product: for any finite prescribed inclusion set S, its determinant factors
over the blocks; these inclusion probabilities determine all exact-set
probabilities by inclusion-exclusion. Thus the block configurations are independent.
The invariant kernel's blocks are related by coordinate permutations induced
by G, so each has the same determinant d. The indicators Z_l that the l-th
block is wholly present are consequently independent Bern(d) variables.

Since det Q0=d^k and n=km, p(Q0)=(det Q0)^(1/n)=d^(1/m). Under iid Bern(p(Q0))
the same block-full indicators are independent Bern(p(Q0)^m)=Bern(d).
Step 3 showed that U is a function of those indicators, so its two probabilities
are exactly equal for every sufficiently small A:

    g_U(A,0):=mu_(tI+A)(U)-nu_(p(tI+A))(U)=0.           (2)

This is equality on a subspace, not an inference from a vanishing Hessian.

### Proof, step 5: cross derivatives vanish along that equality subspace

For any block diagonal positive definite Q0 and any cross-block B, the first
derivative of each principal determinant is zero. To see this, Q0_S is itself
block diagonal, its inverse is block diagonal, and B_S has zero within-block
entries. The determinant derivative is

    D det(Q0_S)[B_S]=det Q0_S Tr(Q0_S^(-1)B_S)=0.

This derivative formula follows by factoring det Q0_S and expanding
det(I+s Q0_S^(-1)B_S)=1+s Tr(Q0_S^(-1)B_S)+O(s²).
For S empty it is the derivative of the constant 1. Step 1 implies that the
first derivative of the DPP event probability is zero. The same statement for
the full determinant, followed by the chain rule for its positive nth root,
implies that the first derivative of the iid comparator is zero too. Thus

    D_B g_U(A,0)=0                                      (3)

for every small A. Positive definiteness is ensured by staying near tI.

### Proof, step 6: a uniform neighborhood for all directions

The function g_U(A,B) is real analytic near (0,0): DPP event probabilities are
polynomials, the determinant is positive there, and the positive nth root is
analytic on (0,infinity). On V_cross, B is zero-diagonal and invariant, so (1)
applies. Each cross-class gamma_ij is strictly positive by step 3. Let

    gamma_* = min_(i,j in distinct classes) gamma_ij > 0.

With Frobenius norm ||B||_F²=2 sum_(i<j)|B_ij|², equation (1) gives

    D_B² g_U(0,0)[B,B]=2C_f(B)>=gamma_* ||B||_F².       (4)

Continuity of the Hessian on the finite-dimensional space, in the operator
norm for quadratic forms, supplies rho_U>0 such that whenever
||A||_F+||B||_F<rho_U,

    D_B² g_U(A,B)[D,D] >= (gamma_*/2)||D||_F²
    for every D in V_cross.                            (5)

Explicitly, choose the neighborhood where the Hessian differs from its value
at (0,0) by operator norm less than gamma_*/2. Along s->g_U(A,sB), (2), (3)
and the integral Taylor formula yield

    g_U(A,B)=integral_0^1 (1-s)D_B² g_U(A,sB)[B,B] ds
             >= (gamma_*/4)||B||_F² >= 0.              (6)

The split A,B is orthogonal for the Frobenius inner product, so
||A||_F+||B||_F<=sqrt(2)||Q-tI||_F<=sqrt(2n)||Q-tI||.
It follows that (6) holds for ||Q-tI||<rho_U/sqrt(2n). The equality/constant
events already have zero gap. There are finitely many invariant increasing
events on finite E, so the minimum of their positive radii and a radius
ensuring 0<Q<I is positive. This proves all invariant-event lower comparisons
on one neighborhood, independently of the direction of Q-tI.

To get all increasing events, average the indicator of an arbitrary increasing
event W over the finite permutation group. The average fbar is invariant,
increasing, and takes finitely many values in [0,1]. Its upper-level events
{fbar>=s} are invariant increasing events. Integrating their comparisons in s
gives E_mu_Q fbar>=E_nu_p fbar. Both measures are invariant, so their expectations
of fbar equal their probabilities of W. This proves full stochastic domination.

### Proof, step 7: upper bound and optimality

Apply the lower theorem around (1-t)I to I-Q, shrinking the radius to the
minimum of the two lower radii. Complementing configurations reverses stochastic
order and sends mu_(I-Q) to mu_Q, so the stated upper bound follows. The event
that all n sites are present implies any lower iid density b must satisfy
b^n<=det Q; the same argument on I-Q implies any upper density c must satisfy
(1-c)^n<=det(I-Q). Thus both parameters are optimal. This completes the proof.

## Corollary: subgroup-supported kernels on arbitrary countable groups

Let Gamma be any countable group, H<=Gamma a finite subgroup, and Q a
Gamma-equivariant kernel with Q_(g,h)=0 whenever gH != hH. Its restriction K
to H is H-equivariant, and all left-coset blocks are its permuted copies. If
K is in the scalar neighborhood just proved, the full sharp conjectured
comparison holds for Q on Gamma.

Proof: Q is a direct sum of copies of K, hence mu_Q is the independent product
of their DPP laws (factor all finite inclusion determinants). Functional
calculus preserves these blocks, and the H-equivariance of log K makes its
diagonal constant. Therefore

    tau_Gamma(log Q)=<delta_e,log K delta_e>
                    =Tr(log K)/|H|,
    FK_Gamma(Q)=(det K)^(1/|H|),

and similarly for I-Q. Take independent copies of the finite monotone couplings
over the countably many cosets; their product is a monotone coupling with the
correct iid marginal on Gamma. The all-present event on a single coset proves
optimality of the lower density, and the all-absent event proves the upper one.
This is an infinite-group special family, not general infinite-group sufficiency.

## An explicit, conservative radius

The neighborhood theorem can be made quantitative without enumerating events.
For n>=2, set

    a=min(t,1-t), c=a/2, T=max(t,1-t),
    L=3^n [n^3+(n^3+6n^2+6n)/c^3],
    delta(n,t)=min(a/2, a^(n-2)/(4 T L))/sqrt(n).        (7)

Every invariant Q with ||Q-tI||<delta(n,t) satisfies both sharp bounds. This
radius is deliberately crude and can be extremely small. No claim of optimal
radius is made. For n=1 all kernels are scalar and the full bounds are trivial.

### Derivation of the uniform third-derivative bound

Work on the Frobenius ball ||Q-tI||_F<a/2, where all eigenvalues are in (c,1).
Let g_U(Q)=mu_Q(U)-F_U(p(Q)), with p(Q)=(det Q)^(1/n). Each coefficient of the
multilinear indicator satisfies |c_S|<=2^|S|, by its explicit alternating sum.
In a third mixed derivative of det Q_S, the derivative directions must enter
three different columns. There are at most |S|^3 assignments. The unchanged
columns have Euclidean norm <=1, since ||Q||<=1; a column of a derivative
direction D has norm <=||D||_F. Hadamard's determinant inequality bounds each
term by the product of the three direction norms. Since sum_S 2^|S|=3^n,

    ||D^3 mu_Q(U)|| <=3^n n^3.

Here and below the derivative norm is the real multilinear operator norm on
Hermitian directions with their Frobenius norms. For the iid polynomial
F_U(x)=sum_S c_S x^|S| and 0<x<1, the same coefficient bound gives
|F_U^(j)(x)|<=3^n n^j for j=1,2,3.

Put ell(Q)=(1/n)log det Q, so p=exp ell. Writing R=Q^(-1), the determinant
derivative formula and D R[D]=-RDR give

    D ell[D]=(1/n)Tr(RD),
    D^2 ell[D1,D2]=-(1/n)Tr(RD1RD2),
    D^3 ell[D1,D2,D3]=(1/n)Tr(RD1RD2RD3+RD1RD3RD2).

The last formula follows by differentiating the second one and using cyclicity
of the trace. Since ||R||<=1/c, Hilbert-Schmidt Cauchy-Schwarz and
||D||<=||D||_F give the derivative bounds

    ||D ell||<=1/(sqrt(n)c),
    ||D^2 ell||<=1/(n c^2),
    ||D^3 ell||<=2/(n c^3).

For example a trace of three R/D pairs is bounded by c^(-3) product ||Di||_F:
use |Tr AB|<=||A||_F||B||_F with A=RD1RD2 and B=RD3, and the product norm
bound ||RD1RD2||_F<=c^(-2)||D1||_F||D2||. Also 0<p<=1. The chain rule gives

    ||Dp||<=1/c,
    ||D^2p||<=2/c^2,
    ||D^3p||<=(4/n^(3/2)+2/n)/c^3<=6/c^3.

The third derivative of F_U(p(Q)) consists of F_U''' times three first
derivatives of p, three terms F_U'' times a second and a first derivative,
and F_U' times the third derivative. Consequently

    ||D^3 g_U(Q)||
      <=3^n n^3+3^n(n^3+6n^2+6n)/c^3=L.              (8)

All bounds are uniform over events U and over the indicated ball.

### Derivation of (7)

For any cross-class pair, step 3 supplies at least one pivotal configuration
on n-2 sites. Its Bernoulli(t) weight is at least a^(n-2). Hence
gamma_*>=a^(n-2)/(2t)>=a^(n-2)/(2T).
The fundamental theorem of calculus and (8) imply

    ||D^2g_U(Q)-D^2g_U(tI)|| <= L ||Q-tI||_F.

For Q=tI+A+B, orthogonality of the split gives ||A+sB||_F<=||A+B||_F for
0<=s<=1. Thus if ||Q-tI||_F<min(a/2,a^(n-2)/(4TL)), the cross-block Hessian
along every point tI+A+sB differs from its scalar value by less than gamma_*/2.
Equations (2), (3) and the integral Taylor formula then prove (6), uniformly
over all invariant events. The same estimate at scalar 1-t gives the upper
bound, because a,c,T,L are unchanged. Finally ||Q-tI||_F<=sqrt(n)||Q-tI||
proves the operator-norm radius (7).

This quantitative version removes any dependence on a particular perturbation
direction and explains why it supplies no immediate infinite-group theorem:
the displayed guaranteed radius deteriorates rapidly with n.

## Brain hints actually used, and current proof boundary

The gap query returned the standard definitions of increasing events and
stochastic order, the Schur complement lemma, and the earlier harmonic-mean
card, without a resolution of spatial-event comparison. The second query
returned Russo/pivotal cards, including
claim_ce028eff08f7ef08cc636b492788f905d03b4c3fa8e4ee1b14f0bc0ea2dcd3a1.
Read claim_569ccbdb68319948c30d7d0358dc8c699ed1907ce85a36c356879bd884bd847d
in full. Its warning that the product Russo formula must not be applied directly
to a dependent process was respected: the DPP derivative was computed by
determinants and only the iid polynomial F was differentiated by influences.
These were hints, not proof certificates. The scalar-neighborhood theorem and
its quantitative radius were derived here; no novelty claim is made relative
to the full published literature or earlier uninspected private work.

The remaining gap is now narrower but still substantive. We have a full sharp
comparison for every finite group's equivariant kernels in a guaranteed open
neighborhood of every scalar tI. We have not proved comparison for an arbitrary
equivariant Q outside those neighborhoods. In the proof this would require
control of the cross-block Hessian beyond its scalar neighborhood, or a different
global argument. Nonnegative second variation at scalar does not supply that.
The quantitative radius tends rapidly to zero with n, so finite approximation
cannot be used here to obtain arbitrary infinite-group bounds or their optimality.
The subgroup-supported corollary is an explicitly limited infinite family.
No counterexample to Lyons's conjecture or matching published resolution has
been produced. The honest overall verdict remains PARTIAL.

## Hostile boundary test: row-energy symmetry alone is insufficient

The nonnegative second-variation formula uses only constant row energy. It is
tempting to weaken transitive equivariance to that condition. This extension
is false arbitrarily close to scalar, and gives a useful test of the zero-direction
argument. On five sites let H be the direct sum of the unweighted triangle
adjacency and [[0,sqrt(2)],[sqrt(2),0]]. All diagonals are zero, every row energy
is 2, and its eigenvalues are 2,-1,-1,sqrt(2),-sqrt(2). For 0<t<1 and
0<epsilon<min(t/4,(1-t)/2), Q=tI+epsilon H is a strict positive contraction.

The determinants of the three-site and two-site blocks are

    d3=t^3-3t epsilon^2+2 epsilon^3,
    d2=t^2-2 epsilon^2>0.

For the increasing event that both sites in the two-site block are present,
the DPP probability is d2, whereas iid density (det Q)^(1/5) gives probability
(d3 d2)^(2/5). The latter is greater precisely when d3^2>d2^3. Direct expansion
gives

    d3^2-d2^3=epsilon^3(4t^3-3t^2 epsilon-12t epsilon^2+12epsilon^3)>0.

For epsilon<t/4, the bracket is at least
(4-3/4-12/16)t^3=(5/2)t^3>0, by dropping the last positive term. Thus the
lower product bound fails for this nontransitive family, despite nonnegative
quadratic variation for every increasing event. The relevant gap has zero
quadratic term and a negative cubic term. Its inseparability classes have sizes
three and two, so they cannot be permuted transitively and their normalized
block determinants differ. This is exactly the feature excluded by proof steps
3 and 4, not a counterexample to the equivariant conjecture.

For an even simpler diagnostic, an isolated off-diagonal pair in tI on four
sites gives a constant-diagonal kernel with event probability t^2-epsilon^2,
below the FK-product comparison t sqrt(t^2-epsilon^2). Equal diagonal alone
therefore does not justify the transitive-neighborhood theorem either.

## Verification results

1. `pivotal_checks.py` independently expanded complex Hermitian principal
   determinants and checked the pivotal coefficient on all 168 monotone events
   on four sites. All passed exactly, as did the minimal-set zero classification.
   For all eight C4-invariant events it also checked the invariant equal-size
   partition, equal block determinants, exact block-diagonal event equality,
   and every principal determinant's vanishing first cross derivative.
2. `near_flat_checks.py` passed 144 spatial comparisons on D4 using 80-digit
   arithmetic. The events concern full cosets of C4 or a nonnormal C2 subgroup;
   kernels have multiple internal strengths and signed cross strengths from
   10^-2 down to 10^-7. The least gap/cross-strength² was about 0.94159.
   These are stress tests, not claimed certified-radius instances.
3. `certified_radius_checks.py` passed 1,008 all-event comparisons at 80 digits
   on C4, with centres 1/5,1/2,4/5 and both perturbation signs. A rigorous norm
   upper bound put each kernel strictly inside (7). The certified radius at
   t=1/2,n=4 is 1/15344640; at t=1/5 or 4/5 it is 1/2385469440. Exact-equality
   events had numerical errors of order 10^-82; every other event had positive
   computed gap, with the smallest about 1.37*10^-22.
4. `boundary_extension_check.py` checks the exact symbolic determinants and
   positive power-comparison margin of the five-site row-energy counterexample.
   It passed exactly, with positive power margin 61489/125000000000 at t=1/2, epsilon=1/100.
5. `PivotalIdentity.lean` covers only the scaled pivotal identities and their
   nonnegative numerator. The initial direct nlinarith invocation could not
   multiply a defining equality by t; explicit rewriting and ring normalization
   replace it. The corrected run passed kernel checking, exit code 0. No
   full probabilistic or neighborhood theorem is called Lean verified.

All new checks and output artifacts stay in the problem folder. The full
written proof is reviewed separately in REFEREE_SECOND.md. The numerical
checks support it and do not replace the analytic uniform-Hessian argument.

Final formal-algebra check: PASS (exit 0; no compiler output). See LEAN_SECOND_CHECK.txt for scope and command. The completed additional pass remains PARTIAL on C0036.
