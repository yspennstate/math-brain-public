from pathlib import Path
with Path('ATTEMPT.md').open('a',encoding='utf8') as out:out.write('''

## Lemma E (proved: forward filling from a dominated law to the invariant law)

Let (E,P) be a standard Borel probability space and theta an invertible measurable P-preserving ergodic transformation with measurable inverse. Let Q=fP be any probability measure, where f>=0 and integral f dP=1. For Z with law Q, on an extension carrying an auxiliary uniform random variable there is an a.s. finite nonnegative integer N such that theta^N Z has law P. N may depend on the entire state Z and is not asserted to be a stopping time. Neither equivalence Q~P nor a finite mean for N is asserted or needed.

### Full proof

Choose measurable versions of all densities. Let a_0=f, b_0=1. Recursively define

    h_n = min(a_n,b_n),
    a_{n+1} = (a_n-h_n) composed with theta^{-1},
    b_{n+1} = b_n-h_n.

Every density is nonnegative and integrable. The measures h_n P are the mass accepted at step n, expressed at its destination. Preservation of P gives

    integral a_{n+1} dP = integral a_n dP - integral h_n dP,
    integral b_{n+1} dP = integral b_n dP - integral h_n dP.

Thus integral a_n = integral b_n for all n. The b_n decrease pointwise to b_infty, with 0<=b_n<=1.

Pull remaining source mass back to its original location: s_n(x)=a_n(theta^n x). The recursion gives

    s_{n+1}(x)=s_n(x)-h_n(theta^n x).

Therefore 0<=s_n<=f, s_n decreases to s_infty, and

    sum_{n>=0} h_n(theta^n x)=f(x)-s_infty(x).

These identities hold simultaneously off a P-null set, which can be enlarged by its countably many theta-translates so that every required orbit evaluation is valid. Dominated convergence, using f for s_n and 1 for b_n, and preservation of P show

    integral s_infty dP = integral b_infty dP.

Suppose b_infty is not zero P-a.e. Choose epsilon>0 with P(D)>0 for D={b_infty>=epsilon}. By the pointwise ergodic theorem for 1_D, for P-a.e. x the orbit theta^n x visits D infinitely often (indeed with limiting frequency P(D)>0). At any such x with s_infty(x)>0,

    h_n(theta^n x)
       = min(a_n(theta^n x),b_n(theta^n x))
       >= min(s_infty(x),epsilon) * 1_D(theta^n x).

The right side sums to infinity over n, whereas the preceding telescoping identity bounds the sum of the left side by the finite number f(x). Contradiction. Hence s_infty=0 P-a.e., which implies integral b_infty=0 and contradicts the supposition. We conclude that b_infty=s_infty=0 P-a.e.

For x with f(x)>0 define

    p_n(x)=h_n(theta^n x)/f(x).

These are nonnegative measurable functions summing to one for Q-a.e. x. At the irrelevant remaining x assign p_0=1 and p_n=0 for n>0. With an independent U uniform on [0,1), set N to the first n with U < sum_{j=0}^n p_j(Z). This is measurable and finite a.s. For every measurable A,

    P_Q(theta^N Z in A)
       = sum_n integral 1_A(theta^n x) p_n(x) f(x) P(dx)
       = sum_n integral_A h_n(y) P(dy)
       = integral_A (1-b_infty(y)) P(dy)
       = P(A).

Tonelli justifies the nonnegative sum and change of variables uses P preservation. This proves the lemma. QED.

The lemma is a classical filling/shift-coupling mechanism, with a new application here rather than a claim of a new ergodic-theory theorem. The brain's recalled lemma had the opposite source/target direction; that recalled statement was not used as a proof of this one.

## Corollary F (proved: full-law absolute continuity is sufficient)

Let W be centered two-sided Wiener law on C_0(R), and theta w(t)=w(t+1)-w(1). If a centered continuous process has full path law Q<<W, then on a probability-space extension it becomes standard two-sided Brownian motion after an a.s. finite nonnegative integer shift.

Proof of the required ergodicity. Under W, the unit increment paths w(k+u)-w(k), 0<=u<=1, k in Z, are independent and identically distributed standard Wiener segments. They determine w uniquely, including negative times, and theta shifts their indices. This is the bilateral i.i.d. shift. To verify ergodicity explicitly, let A be invariant and approximate A in probability by a finite-coordinate cylinder C with P(A symmetric_difference C)<delta; such approximations exist because finite-coordinate cylinders generate the product sigma field. For a sufficiently large integer m, C and theta^{-m} C use disjoint coordinates, hence are independent. Invariance of A yields

    |P(A)-P(A)^2|
       <= |P(A intersection theta^{-m} A)-P(C intersection theta^{-m} C)|
          + |P(C)^2-P(A)^2|
       <= 2 delta + 2 delta = 4 delta.

Let delta tend to zero. Thus P(A) is 0 or 1. The map theta and its inverse are measurable and preserve W. Lemma E applies and gives the required exact shift. QED.

A more general stability statement follows. If a continuous centered path law mu is absolutely continuous with respect to a path law nu that already admits a finite random shift to W, then mu also admits such a shift on an extension. Indeed, take a joint law of (x,R) witnessing nu's shift to W and disintegrate R given x, obtaining a probability kernel K(x,dR). The joint law mu(dx)K(x,dR) is absolutely continuous with respect to nu(dx)K(x,dR): a joint null set has K-section measure zero nu-a.e., hence mu-a.e. Its shifted-path image has law lambda<<W. Apply Corollary F to that image, with integer shift N. The combined real shift R+N is finite and gives W exactly. The cocycle identity theta_N(theta_R x)=theta_{R+N}x verifies that this is a shift of the original path, not a change to the trajectory.

Scope convention: these statements explicitly allow auxiliary randomness on an extension. They do not claim that the integer shift is a deterministic function of the canonical path. The source uses distributional random-shift constructions; regardless of its underlying-space convention, no inference to the full Problems 7.1–7.3 is made from this added absolute-continuity condition.

## Lemma G (proved: one-way Kakutani product domination)

Let P_0 be a probability law on a standard Borel space E, and let Q_j=f_j P_0, j>=1, be probability laws. Define rho_j=integral sqrt(f_j) dP_0. If sum_j (1-rho_j)<infinity, then product_j Q_j << product_j P_0.

### Full proof

By Cauchy-Schwarz, 0<rho_j<=1. Positivity follows because f_j>=0 integrates to 1. Work on the reference product P. Put F_n=product_{j=1}^n f_j(x_j), and H_n=sqrt(F_n). Independence gives integral H_n^2 dP=1. For m>n,

    integral H_n H_m dP = product_{j=n+1}^m rho_j,
    ||H_m-H_n||_2^2 = 2(1-product_{j=n+1}^m rho_j)
                       <= 2 sum_{j=n+1}^m (1-rho_j).

The finite product inequality follows by induction from 1-ab=(1-a)+a(1-b)<= (1-a)+(1-b) when a,b in [0,1]. The summability hypothesis makes H_n Cauchy in L^2. Let H be its L^2 limit. Passing to an a.e. convergent subsequence ensures H>=0. Norm continuity gives ||H||_2=1. By Cauchy-Schwarz,

    ||F_n-H^2||_1
       <= ||H_n-H||_2 (||H_n||_2+||H||_2)
       = 2 ||H_n-H||_2 -> 0.

Thus F=H^2 is a probability density with respect to P. For any event C depending on the first r coordinates, for n>=r independence gives

    integral_C F_n dP = (product_{j=1}^r Q_j)(C).

L^1 convergence gives the same identity with F in place of F_n. Consequently FP and product_j Q_j agree on every finite-coordinate cylinder; the pi-lambda theorem makes them equal on the product sigma field. Hence product Q_j=FP<<P. QED.

This is the sufficient one-way direction of Kakutani's product-measure result, proved here without assuming every coordinate law is equivalent. We need domination, not reverse domination.

## Theorem H (proved special case: summably perturbed stopped-piece laws)

Let P_0 be the law of a Brownian stopped piece (T,B stopped at T) with 0<E_{P_0} T<infinity and an a.s. finite nonnegative stopping time for a normal filtration. Let the actual decomposable process be constructed from independent stopped Brownian pieces with laws Q_k, k in Z. Assume

    Q_k << P_0 for every k,
    sum_{k in Z} [1-integral sqrt(dQ_k/dP_0) dP_0] < infinity.

Then, in the distributional sense allowing a probability-space extension, the actual process is 2BM after a finite random shift. BBM need not be separately assumed. The Q_k need not be identical, and their stopping rules may depend on their Brownian paths.

### Full proof

Represent a stopped piece as (T,b), with b(t)=B(t min T), in [0,infinity) times C_0([0,infinity)); the consistency condition b(t)=b(T) for t>=T is Borel, so this is a standard Borel piece space. Enumerate Z by 0,1,-1,2,-2,... and apply Lemma G. The actual product of piece laws Q is absolutely continuous with respect to the i.i.d. reference product P=product_{k in Z} P_0.

Under P, the durations sum to infinity in both directions a.s. For example choose epsilon>0 with P_0(T>=epsilon)>0, which exists because E T>0. In each direction independent trials give infinitely many such durations by the second Borel-Cantelli lemma. This a.s. event also holds under Q by domination. Thus both concatenations are defined on all of R. The concatenation map Phi from the piece sequence to a centered continuous path is measurable: joining times are finite sums of coordinate durations; at any fixed rational time a countable Borel partition selects its containing index, and evaluation of that coordinate's continuous path at the corresponding measurable offset is measurable. Continuity and rational evaluations then give path-valued measurability. On the null set of nondivergent clocks choose an arbitrary fixed continuous path.

The reference process is strongly decomposable and has finite mean durations; source Theorem 5.1 (pp.18–19) gives a joint law of reference pieces and a finite real shift R_0 such that theta_{R_0} Phi has law W. Disintegrate the shift given the entire reference piece sequence to obtain a kernel K. Put the same kernel on the actual product Q. The resulting joint actual law is absolutely continuous with respect to the joint reference law, as proved in Corollary F. Hence the actual shifted path Y=theta_{R_0} Phi has some law lambda<<W. Corollary F gives a further finite nonnegative integer shift N with theta_N Y law W. Therefore R_0+N is a finite centering time of the original concatenated path and witnesses 2BM. If the original decomposition itself required a shift U, add U to this combined shift. QED.

Only source Theorem 5.1 is imported in this proof; all product-domination and tilt-correction steps are proved above. No claim of originality is made for combining these classical tools.
''')
print('saved Lemmas E,G; Corollary F; Theorem H')
