# General results, obstructions and open targets

FEIB17, 10 November 2026. PROVED means the argument is given here in arbitrary dimension. CHECKED always names its finite scope. OPEN means no proof was obtained. No general FEI bound or counterexample to FEI was found. Novelty beyond the supplied FLOW and prior reports is not a claim of priority in the literature.

Let mu(S)=fhat(S)^2, I=sum |S|mu(S), H^-=sum_i H(U_i|U_-i), and

    G=sum_{T,i not in T} mu(T+i)log(1+mu(T)/mu(T+i)).

Entropy is measured in bits. All functions in the theorems are real and sign-valued unless stated otherwise. See REFEREE.md for the corrected one-step, KL, pair and witness formulas.

## 1. A bounded-influence reduction for erasure entropy — PROVED

A uniform bound on erasure entropy just for

    1 <= I(f) <= 9/4

already implies FEI. More precisely, if M is an upper bound for H^- throughout that interval, then

    H^-(f) <= 2 M I(f)                         (all Boolean f),
    H(f) <= (2M+2/ln 2)I(f).

This addresses the ambition of the first requested target: a polynomial bound at bounded influence is not an easier quantitative relaxation here.

Proof. First observe tensor additivity. For Boolean f and h on disjoint variables, the product function f h has spectral law mu_f times mu_h. Therefore both I and H^- add. This is immediate for I; for an erasure bit, conditioning on all the other bits of an independent product distribution leaves exactly its original conditional entropy.

Now introduce k fresh selector bits y and one fresh data bit z. Let B be a single point in the selector cube, with density delta=2^-k. Define the Boolean switch

    g(x,y,z)=f(x) on B, and z off B.

Its Fourier expansion is

    g=1_B(y) f(x)+(1-1_B(y))z.

In the sector not containing z, every coefficient is fhat(S) times the corresponding coefficient of 1_B. In the sector containing z, only S=empty occurs. Hence, for every original coordinate i, all nonzero erasure contributions lie in the first sector. Homogeneity of Phi and Parseval for 1_B give the exact identity

    E_i(g)=delta E_i(f),     i an original coordinate.

The z-sector creates no original-coordinate erasure because each of its edges has a zero upper endpoint. All the additional erasures are nonnegative, so

    H^-(g)>=delta H^-(f).                    (SW1)

For influence, original bits contribute delta I(f); z contributes 1-delta. A selector bit is pivotal exactly when all other selectors match B and f(x) differs from z, an event of probability 2delta times 1/2. Thus each selector contributes delta, and

    I(g)=1+delta(I(f)+k-1).                 (SW2)

If I(f)>=1 choose k=max(1,ceil(log I(f))). Then delta^-1<=2I(f). Also 1<=I(g)<=9/4: for k=1 the upper bound is 2; for k>=2 it is 2+(k-1)/2^k<=9/4. Therefore (SW1) yields H^-(f)<=2MI(f).

If 0<I(f)<1, multiply r=ceil(1/I(f)) independent copies. Its influence is r I(f) in [1,2), and its erasure entropy is r H^-(f). Hence H^-(f)<=M/r<=M I(f). Constants have zero erasure and need no division. Finally apply the erasure-to-FEI implication proved in REFEREE (b). This completes the proof.

CHECKED before writing this proof: reductions.py tests (SW1) coordinate by coordinate and (SW2) on every four-variable function at k=1,2,3. Original-coordinate erasure residuals are at most 2.498001805406602e-16 bits; influence residuals are exactly zero in the floating-point calculation. This is 65,536 base functions for each selector size, not an exhaustive census on the enlarged dimensions.

Corollary — PROVED. Any bound H^-<=C I^2 for every Boolean f with I>=1 implies the full linear erasure bound with constant (81/8)C, and then FEI with constant (81/8)C+2/ln 2. Thus the quadratic target, after fixing its small-I defect, remains equivalent to FEI up to constants. Likewise the proposed universal H^-<=C I log(I+2) would imply FEI through this bounded interval; FEI implies that estimate immediately because log(I+2)>=1.

The unqualified quadratic target is false — PROVED. For AND_n, let d=2^(1-n), q=d^2 and p=(1-d)^2. Direct enumeration of coefficient pairs gives

    I=n d,
    H^-=n[Phi(p,q)+(2^(n-1)-1)2q].

The second summand divided by I tends to 2; the exceptional pair divided by I is O(n2^-n). Hence H^-/I ->2 while I ->0, and H^-/I^2 diverges. exact_families.json records the exact-form evaluations. A polynomial statement must include a linear term, restrict I away from zero, or normalize influence; it still would not bypass the switch reduction.

This also explains why the KKLMS concentration theorem is not a proof of the requested target. The [authors' primary paper, Theorem 1.3](https://www.ias.edu/sites/default/files/math/csdm/19-20/KelmanKiLiMiSa-Towards.pdf) controls entropy by a weighted degree logarithm. It does not state a bound purely by I log(I+2) for all spectral mass. I used that source only to check the scope of the requested comparison, not as an input to a proof. In particular, I did not turn concentration of most mass into a Shannon-entropy bound on the remainder.

## 2. A Boolean edge budget that fails for complex unimodular functions — PROVED, limited scope

For every i choose nonnegative weights w_i(T), T not containing i, with sum_T w_i(T)<=1. Then

    sum_i sum_T w_i(T) b_T^2 log(1+a_T^2/b_T^2)
       <= [2/(e ln 2)] I(f).                                  (EB)

The weights may depend arbitrarily on the whole function. In particular one can choose, in each direction, its most expensive edge. Equivalently,

    sum_i max_{T not containing i}
       fhat(T+i)^2 log(1+fhat(T)^2/fhat(T+i)^2)
       <= [2/(e ln 2)] I(f).

The same conclusion holds with a multiplicative factor K when each direction's weights sum to at most K. Another corollary is the fully summed but collision-weighted bound

    sum_{T,i not in T} mu(T) mu(T+i)log(1+mu(T)/mu(T+i))
       <= [2/(e ln 2)] I(f).

Proof. Real Booleanity gives D_i f in {-1,0,1}, with support density delta_i=Inf_i. For every T not containing i,

    |b_T|=|E[D_i f chi_T]|<=E|D_i f|=delta_i.       (B1)

Also a_T^2+b_T^2<=1 by Parseval. With q=b_T^2,

    q log(1+a_T^2/q) <= q log(1/q).

Writing r=sqrt(q), elementary calculus gives

    q log(1/q)=2r^2 log(1/r)
             <= [2/(e ln 2)]r
             <= [2/(e ln 2)]delta_i.

The scalar maximum uses r ln(1/r)<=1/e. Multiply by the weights and sum over T and i. For collision weights take w_i(T)=mu(T), whose sum is at most one. This proves every stated form.

This is genuinely a consequence of the real Boolean pair relations: f_0 f_1=0 and f_0^2+f_1^2=1 imply f_1 is a signed indicator, so its L1 norm equals its squared L2 norm. It uses that fact for every coordinate at once. The complex product with n=1 has a=sqrt(1-p), b=i sqrt(p), unit modulus, and weighted edge cost p log(1/p), while I=p. It violates (EB) with any fixed constant as p tends to zero. Thus (EB) distinguishes the real and complex classes.

The limitation is explicit: the full G has an unbounded number of unweighted edges in each direction. We have bounded their maximum or a normalized average, not their sum. No deduction G<=CI follows from (EB). The missing statement would have to control how many expensive edges coexist in each direction, using further cross-coordinate relations.

CHECKED before the proof: edge_budget.py checks the directional-maximum and collision-weighted forms on all four-variable functions and a separate mixed bank of 3,000 functions at each of n=6,7,8. It finds no violation. edge_budget.json records the finite maxima.

Singleton consequence — PROVED. Set T=empty in (EB). The contribution to G of all singleton upper endpoints is at most [2/(e ln 2)]I. The corresponding contribution to H^- is at most [(1+2/e)/ln 2]I, using the absence term from REFEREE (c). Therefore an erasure witness with unbounded G/I must obtain its unbounded cost from levels at least two. witnesses.json separately tests the singleton bound on the supplied five-variable representative file.

## 3. The convolution conditions — PROVED; the full desired inequality is OPEN

For every i, f=f_0+x_i f_1 is Boolean exactly when f_0+f_1 and f_0-f_1 are sign-valued. Squaring them and adding/subtracting gives

    f_0 f_1=0,     f_0^2+f_1^2=1.

The Fourier coefficient of a product is symmetric-difference convolution, so for a=f_0hat and b=f_1hat,

    a*b=0,     a*a+b*b=delta_empty.

Conversely inverse transformation gives the pointwise identities, which imply (f_0 plus or minus f_1)^2=1 for real f_0,f_1. Thus there is no lost assumption at the level of a complete coordinate pair. Requiring these identities for all coordinates expresses the simultaneous Boolean consistency that scalar coefficient ratios omit.

The full f^2=1 condition also gives, for every nonempty W,

    sum_S fhat(S)fhat(S symmetric_difference W)=0.

Grouping the two orientations of each pair shows that the largest absolute unoriented pair product cannot exceed the sum of the others. This is a necessary cancellation constraint on every difference W. It was already identified in FEIB10; I do not claim it as new or sufficient to prove FEI. Complex unimodularity instead gives a conjugated autocorrelation identity, whose two orientations can cancel by imaginary phases. The n=1 complex example has only one unoriented edge and illustrates the distinction.

CHECKED: extra_checks.py computes the two pair convolutions explicitly, rather than only inverse-transforming pointwise products. It checks all four-variable functions and 128 mixed functions at each of n=6,7,8, for every coordinate and every convolution displacement. Both residuals are exactly zero on this dyadic bank.

OPEN: an inequality on the entire unweighted G that exploits all these identities and gives CI or CI log(I+2). The proved weighted budget above does not supply it. The bounded-influence theorem explains why even an apparently weak dimension-free polynomial estimate would be a major result.

## 4. A vertex LP and a general obstruction to its correction term — CHECKED / PROVED

The candidate fixed before this census was, for a Boolean g with mean b!=0 and A any subset of its coordinates,

    F_A(g):=sum_{i in A} rho_i log(1+1/rho_i)
       <= c sum_{i in A}rho_i + k I(g) + l Var(g),
    rho_i=(ghat(i)/b)^2.                                      (V)

Why these correction terms were worth testing: for g_T=f chi_T,

    I(g_T)=I(f)+|T|-2 sum_{i in T}Inf_i(f),
    E_{T~mu} I(g_T)=2 sum_i delta_i(1-delta_i)<=2I(f),
    E_{T~mu} Var(g_T)=1-sum_T mu(T)^2<=2 Var(f)<=2I(f).

The variance inequality follows from sum mu^2>=mu(empty)^2 and 1-mu(empty)^2<=2(1-mu(empty)). Moreover

    E_mu sum_{i not in T}rho_i <= I(f),

because the expectation is the sum of upper masses on edges with a supported lower endpoint. Therefore a universal (V), with A the coordinates outside T, would imply G<=(c+2k+2l)I. These are actual O(I) correction budgets, not terms whose expectation is merely hoped to be small.

CHECKED finite LP. vertex_lp.py multiplies (V) by b^2, uses nonnegative c,k,l, and minimizes c+2k+2l. It scans the 616,126 representatives in FEIB11/npn5.txt for every coordinate subset A. Input and output negations preserve squared coefficients, and coordinate permutations relabel A, so the candidate is NPN invariant. This project did not regenerate or independently prove coverage of that supplied representative file; the exact file hash is in vertex_lp.json. Padded lower-dimensional functions are included through this representation.

The cutting-plane LP returns

    c=1.5421769659005276, k=0.8421145787053088, l=0,
    c+2k+2l=3.226406123311145.

A final scan finds no positive violation at the recorded floating-point tolerance. The constraints, final coefficients, worst scan witnesses and objective are saved in vertex_lp.json. These decimals are a finite numerical fit, not a rational or universal certificate.

The candidate fails outside the census. At n=256, the symmetric threshold positive when the number of positive inputs is at least 132 gives

    F=26.81734217721384,
    fitted right side=16.88218195148726.

The remaining threshold rows are independent holdouts, not constraints used for fitting.

In fact no fixed c,k,l can make (V) true — PROVED. Take even n along n=16^j, and let g_n be negative iff Binomial input weight is at least n/2+n^(1/4). Its mean and singleton coefficient are

    b_n=1-2 P[Bin(n,1/2)>=n/2+n^(1/4)],
    alpha_n=P[Bin(n-1,1/2)=n/2+n^(1/4)-1].

The equality ghat(i)=alpha_n follows from monotonicity and the pivotal indicator. Stirling's formula, uniformly for displacement o(sqrt(n)), gives

    b_n ~ 2 sqrt(2/pi)n^(-1/4),
    alpha_n ~ sqrt(2/pi)n^(-1/2).

For completeness, b_n is twice the mass between the median and that threshold, up to one central atom: there are n^(1/4)+O(1) atoms, each sqrt(2/(pi n))(1+o(1)). This proves the mean asymptotic directly without needing a quantitative central limit theorem. The singleton asymptotic is the same local Stirling estimate at the last threshold atom.

Consequently, with A all coordinates,

    I(g_n) ~ sqrt(2/pi)sqrt(n),
    sum_i rho_i ~ sqrt(n)/4,
    Var(g_n) ->1,
    F_A(g_n) ~ [sqrt(n)/8]log n.

The right side of (V) is O(sqrt(n)) for any fixed coefficients, while its left side has an extra log n. This proves failure for all constants, not just failure of the fitted LP. The binomial formulas are evaluated without allocating truth tables through n=16,777,216 in vertex_lp.json.

This no-go result does not refute FEI: (V) demanded a bound at every vertex separately. For the threshold example the bad empty vertex has spectral weight b_n^2 of order n^-1/2; its weighted cost is only of order log n, below I of order sqrt(n). An eventual correction must use how often such vertices occur, or borrow a more structured budget from other vertices. A correction proportional only to I(g_T) and Var(g_T), with a constant coefficient, cannot do the job pointwise.

OPEN: the requested correction term with an O(I) spectral average. The LP identified an attractive false candidate, and the holdout plus proof rule out the entire stated three-feature family. I have not promoted small-dimensional feasibility to a theorem.

## 5. Necessary structure of an erasure obstruction — PROVED constraints; existence OPEN

I do not have evidence that FEI is false. The following constraints describe what an unbounded erasure ratio would require. The distinction between an erasure witness and an arbitrary high H/I function matters: by the path reduction a hypothetical FEI counterexample has restrictions exposing a large erasure ratio, but its original H^-/I need not itself be large.

Choose a restriction witnessing large G/I and draw a down edge from P(e)=mu(top)/I. Set

    Z(e)=log(1+mu(bottom)/mu(top)).

Then exactly

    G/I=E_P Z=integral_0^infinity P[mu(bottom)/mu(top)>2^t-1] dt.   (ST)

Edges with zero upper mass have no P weight. This is the layer-cake formula for a nonnegative finite random variable. Edges of lower/upper ratio at most 2^t contribute at most (t+1)I in total. Thus a growing mean requires an unbounded area under the steep-edge tail; the existence of one steep edge alone proves nothing.

The edge-law identity further forces

    KL(P||Q)=log(n/I)-G/I>=0,
    G/I<=log(n/I).

In particular an unbounded ratio needs n/I to grow. Singleton upper endpoints have the uniformly bounded budget proved in section 2, so the excess must come from higher levels. A fixed supported edge costs at most [2/(e ln 2)]Inf_i, and any bounded number of edges in each coordinate direction has the same bounded aggregate budget. Therefore an obstruction also needs expensive edges spread across an increasing effective multiplicity of locations per direction; no single chosen edge in each direction can carry its growing ratio.

For every nonempty R and integer k>=0, hypercontractivity and Boolean granularity give the already-proved FEIB10 constraint

    mu{U contains R, |U-R|<=k}
       <=3^k 2^(|R|-1) up(R)^(3/2).

The proof is: sum_low Fourier mass of D_R f <=3^k ||D_R f||_(4/3)^2; Holder on its support bounds that by 3^k up(R)sqrt(p(R)); granularity gives p(R)<=4^(|R|-1)up(R). In particular a rare derivative's spectral mass cannot all sit just above R. The full signed convolution cancellations from section 3 hold at every displacement at once. A sparse independent product spectrum violates these real-Boolean constraints; complex phases evade them.

None of these constraints proves that the steep-edge tail in (ST) is uniformly integrable. That uniform integrability, or an equivalent collective budget, is the remaining obstacle. No unproved assertion about how many levels must be steep is made: the constraints establish a higher-level source and multiplicity requirement, not a particular level distribution.

## 6. What was and was not completed

PROVED: the bounded-influence switch reduction; failure of the unqualified small-I quadratic target; the Boolean weighted edge budget and singleton bound; failure of every pointwise vertex correction in the stated I(g), Var(g), rho family; the corrected mixture KL identities and improved pair approximation constant; the exact bent composition and corrected block witness; steep-tail necessary conditions.

CHECKED: the exhaustive and sample results in the JSON outputs, including the provided five-variable representative census. All numerical candidates were tested before being written here as theorems. Finite checks were used to reject (V), not to prove it.

OPEN: the requested general G<=CI or H^-<=CI log(I+2), their equivalent polynomial relaxation away from zero influence, a useful pointwise vertex correction whose spectral average is O(I), and a Boolean FEI counterexample. These are mathematical open ends of this task, not an environmental block.
