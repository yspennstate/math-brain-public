# Every essential Boolean core has a prime selector completion

All entropies below use natural logarithms. The result concerns genuine disjoint Boolean-wire composition, not affine or overlapping composition. Full FEI remains open.

## Prime completion theorem

Let f:{0,1}^n->{-1,1} depend essentially on all n coordinates, n>=3. There is an input-reflected threshold q(x)=T_2^n(x xor sigma), where T_2^n is positive exactly when at least two bits are one, such that

    G(x,z) = f(x) if z=0, and q(x) if z=1

is essential and prime on n+1 coordinates. In particular an arbitrary essential core is a deterministic face of a prime gate with only one extra coordinate. The completion is fixed independently of the physical input biases.

First T_2^n is prime. For each proper block B with 2<=|B|<=n-1, use assignments in B with zero, one and two ones. On outside assignments with zero and one ones their rows are (--),(-+),(++). Thus there are at least three cofactor rows. A Boolean wire admits at most two rows. Input reflections preserve this property.

There are 2^n distinct input reflections of T_2^n. Indeed each coordinate is essential and increasing before reflection, and its monotonicity orientation is reversed exactly when reflected. A function cannot be both increasing and decreasing in an essential coordinate. This proves freeness of the reflection action, without a symmetry quotient assertion.

Exclude q=f, q=-f and q=f with coordinate i reflected, for each i. There are at most n+2 excluded functions. Since 2^n>n+2 for n>=3, at least one reflection remains. Use any such q.

All x coordinates of G are essential on the f face. The selector is essential because q!=f. Suppose a proper block B, 2<=|B|<=n, has at most two cofactor rows.

1. If z is not in B and B is a proper subset of x, restricting the outside selector to 1 leaves a one-wire decomposition of q through B, contradicting primality of q. More explicitly, restricting columns cannot increase row count, whereas q has at least three rows.
2. If z is not in B and B is all x, the rows are pairs (f(x),q(x)). Since both components are nonconstant, two possible pairs force f=q or f=-q. Both were excluded.
3. If z is in B, let A=B minus {z}. If 2<=|A|<=n-1, restrict the inside selector to 1. The remaining rows include the rows of q through A, again at least three. The proper-block condition ensures A is a proper subset of x.
4. The only remaining possibility is B={z,x_i}. The two rows q|xi=0 and q|xi=1 are distinct, by essentiality of q. The two f rows are distinct, by essentiality of f. If the four rows have at most two values, the f pair must equal the q pair either in the same order or in the reverse order. Hence f=q or f is q with coordinate i reflected, both excluded.

Every possible proper block is covered. Therefore G is prime. The theorem does not assume that f is itself prime, monotone, balanced or threshold.

Essentiality cannot be dropped with the same selection rule: if f ignores xi and equals q|xi=0 as a function of the other variables, the block {z,xi} can have only two rows despite q not being f, -f, or a single-coordinate reflection of f. Dummy coordinates must be contracted before applying the theorem. The cases n<=2 need no completion for localization: essential binary functions are already prime and unary functions are literal leaves.

## Exact product-law boundary transfer

Fix any interior product law on x, p_i in (0,1), and independently let Pr(z=1)=epsilon in (0,1). Write v_i=4p_i(1-p_i), v_S=product_(i in S)v_i. Expand f and q in the basis product_(i in S)(X_i-E X_i), X_i=2x_i-1, with coefficients a_S and b_S, including the empty coefficient. These are physical centered coefficients; Boolean mixed differences give |a_S|,|b_S|<=1.

With z represented by Z=2z-1, the exact coefficients of G are

    c_S(G) = (1-epsilon)a_S+epsilon b_S,
    c_(S union {z})(G) = (b_S-a_S)/2.                 (1)

The second coefficient is independent of epsilon, and its spectral mass is

    epsilon(1-epsilon) v_S (b_S-a_S)^2.              (2)

Both formulas include S=empty where appropriate. They follow by writing G=f+z(q-f) and z=epsilon+(Z-E Z)/2. No conditioning of the spectral law is used.

For h(t)=t^2 ln(1/t^2), with h(0)=0, define corrected entropy

    E_p(f)=sum_(S nonempty) v_S h(a_S),
    Delta_p(f)=sum_(S nonempty)(|S|-1)v_S a_S^2.

There are only finitely many sets for this fixed n. The continuous extension h(0)=0 and (1)-(2) imply

    E_(p,epsilon)(G) -> E_p(f),
    Delta_(p,epsilon)(G) -> Delta_p(f),
    I_(p,epsilon)(G) -> I_p(f),
    H_(p,epsilon)(G) -> H_p(f).                       (3)

The H limit is ordinary entropy of the full squared Fourier law, including empty. Every old spectral atom converges to its f mass, every selector-containing atom vanishes, and -t ln t is continuous at zero. No uniform-in-n convergence rate or interchange of an infinite sum is asserted.

Consequently, a constant K valid in E<=K Delta for all such PRIME selector completions at all interior product laws implies E<=K Delta for every essential f of arity n>=3 at every interior product law. Define the test class precisely as these completions TOGETHER WITH all essential binary gates. A uniform K theorem on this class, combined with the literal/constant identities E=Delta=0 and contraction of dummy coordinates, gives the usual all-function corrected endpoint with the same K. Conversely an all-function theorem plainly covers this test class. At Delta(f)=0 use the undivided inequalities and (3), never a ratio limit. Combined with the previously established disjoint-composition localization, the ordinary uniform FEI implication is max{K/ln2,log2(e)} when K is in nats.

This sharpens the location of the universal obligation: even prime gates with one rare selector and a signed threshold on the other face retain arbitrary Boolean core entropy. A theorem paying only the selector or only the threshold face has not supplied the f-face cost. The fixed-n limiting argument proves the implication for every finite n, so it does not need a uniform continuity modulus.

## Dyadic scale boundary guard

The corrected entropy in (3) is continuous. The rounded scale charge J_hi need not be continuous: the upper dyadic convention assigns j=k at |a|=2^-k, whereas an approach from above assigns k-1. It would be incorrect to substitute exact J_hi(G)->J_hi(f) into a core transfer without checking this boundary.

This happens in an actual prime completion. Let f be positive only at x=000 on three fair bits (truth-table mask1), and let q=T_2^3. This q is not among the five excluded functions. Every nonempty f coefficient has magnitude1/4; its triple coefficient is -1/4, whereas q's triple coefficient is -1/2 and its pair coefficients vanish. Thus J_hi(f)/ln4=1/2. For 0<epsilon<1/2, the old triple coefficient is -(1+epsilon)/4 and has scale1, while the three old pair coefficients have magnitude (1-epsilon)/4 and scale2. Their total old high charge divided by ln4 is [6(1-epsilon)^2+(1+epsilon)^2]/16. Selector-containing high charges vanish in the limit, giving lim J_hi(G)/ln4=7/16, strictly below1/2. The lost ln4/16 is a rounding jump, not disappeared entropy.

Let M_p(f)=sum_(|S|>=2)v_S a_S^2. For occupied coefficients j(t) is the unique nonnegative integer with 1/2<2^j |t|<=1. From (1), termwise inspection gives

    J_hi(f)-ln4 M_p(f) <= liminf_(epsilon->0) J_hi(G)
      <= limsup_(epsilon->0) J_hi(G) <= J_hi(f).       (4)

At a nonzero nondyadic a_S the scale is eventually constant. At an interior dyadic a_S it can drop by at most one. At |a_S|=1 it cannot approach from above since coefficients remain in [-1,1]. At zero, t^2 j(t)->0, because j(t)<=log2(1/|t|). Selector-containing terms vanish by their epsilon factor; their normalized coefficients in (1) are fixed, including possible zero. Sum these finitely many bounds with nonnegative v_S. The bound deliberately allows all old high dyadic atoms to lose one scale. This is a guard for the reference ledger, not a payment of its high charge. Complete terminal KL laws, singleton imports, carries and old mantissa commitments retain their owners.

## Validation and remaining gap

The finite checker enumerates all 218 essential ternary cores, constructs an allowed reflected threshold for each, and checks every proper block of the resulting four-bit gate directly by distinct rows. It also checks all 256 ternary masks for essentiality, excludes inadmissible dummy-core use, and verifies exact centered-coefficient formulas on sixteen rational product-law fixtures and the actual dyadic jump on four fair-core fixtures. A second construction forms the completed truth table directly from selector faces. The separate proof, rather than these finite examples, supplies all n.

The first unpaid line remains a dimension-independent original-influence payment for arbitrary core high-sector entropy, retaining existing singleton/mantissa/import/carry debits and both complete terminal laws. The theorem exposes that obligation inside a narrow prime subclass; it does not prove that payment or disprove FEI. Mathematical rung: analytic proof with exact finite validation, pending independent review; any separate Lean check covers only its explicitly stated finite row-pair lemma.
