# Every Boolean core occurs in a genuine positive-private signed-core CNF

This is an exact universality reduction for C020, not a proof or disproof of FEI. All cubes are uniform, all logarithms base two. The core clauses below use SIGNED literals. This is broader than A015's all-positive core-anchor subclass; no equivalence for that narrower subclass is asserted.

Fix ANY nonconstant g:{-1,1}^s->{-1,1}, s>=1, and let V={v:g(v)=-1}, q=|V|/2^s. For each v in V let a_v(z) be the OR of the s signed core literals that is false exactly at z=v. For each v create L>=1 fresh PRIVATE positive variables x_(v,l), l=1,...,L, all disjoint and independent. Define the indicator and sign function

    U_L(z,x)=product_{v in V,l=1..L} [a_v(z) OR x_(v,l)],
    F_L=2U_L-1, epsilon=2^-L.                             (1)

Every clause has s core literals and exactly ONE private positive variable. There are L|V| clauses and s+L|V| actual physical bits. No dummy private variables, clone approximation or nonuniform core conditioning is involved. Every private variable is relevant: condition the core to its v and all its sibling private bits to true.

Moreover the displayed CNF is IRREDUNDANT and every displayed clause is a PRIME IMPLICATE. For irredundancy, fix core v, set its sibling private bits true and its chosen private bit false: exactly this clause fails. To show that its private literal cannot be deleted, fix core v and set ALL its private bits true; the function is true but the shortened core clause is false. To show that any chosen core literal cannot be deleted, flip just its core bit from v to v'; keep the chosen v-private bit false. If v' is a false core point, set every private bit in its DISTINCT group true; if v' is true, no private group is needed. In both cases the function is true, but the shortened clause is false. These explicit actual assignments certify minimality of every literal. This does NOT assert that the displayed clauses exhaust all prime implicates; resolution may produce additional ones.

## Exact physical spectrum and influence

When g(z)=1, all clauses are true and F_L=1. When g(z)=-1, exactly the v=z group of L clauses remains, so U_L is the AND of its L private bits. Therefore

    E_x F_L(z,x)=(1-epsilon)g(z)+epsilon.

For EVERY nonempty core S, with ALL private Fourier coordinates empty,

    Fhat_L(S,empty)=(1-epsilon) ghat(S).                    (2)

The empty coefficient is (1-epsilon) ghat(empty)+epsilon. In particular the total nonempty core-only spectral mass is exactly (1-epsilon)^2 Var(g). This is a signed Walsh identity, not a pushforward of independent squared spectra.

There is also an EXACT full private-sector description. Write delta_v for the core point indicator and A_v for its private AND. Then F_L=g+2 sum_v delta_v A_v. A nonempty private Fourier set must lie entirely inside ONE v-group; otherwise its coefficient is zero. For each such private set and EVERY core set S, its coefficient has magnitude 2^(1-s)epsilon, since delta_v has all Fourier magnitudes 2^-s and the private AND has all magnitudes epsilon. There are |V|2^s(2^L-1) such distinct coefficients. Consequently the private-sector mass is M=4qepsilon(1-epsilon), and its ENTIRE entropy is

    H_private=M(2s+2L-2).                                (2a)

Thus H(F_L) equals the entropy contribution of the affine core coefficients above plus (2a). This proves H(F_L)->H(g), despite the growing physical dimension; dimension-dependent continuity is not assumed. The private entropy vanishes because L2^-L->0. The exact entropy formula supplies a guard against misreporting this family as an FEI counterexample.

The exact PHYSICAL influence is

    I(F_L)=(1-epsilon)^2 I(g)
                  +2q epsilon [s(1-epsilon)+L].            (3)

Proof: private influence conditioned on a false core point is 2L epsilon, and is zero on a true point, giving 2qL epsilon. For a core edge with one true endpoint, disagreement has probability 1-epsilon. For a false/false edge the two endpoint groups are DISTINCT and independent, so disagreement is 2epsilon(1-epsilon). Summing over oriented uniform core edges, the true/false crossing count is I(g), while the false/false count is s q-I(g)/2. This gives I_core=(1-epsilon)I(g)+2epsilon(1-epsilon)[sq-I(g)/2]=(1-epsilon)^2 I(g)+2sqepsilon(1-epsilon). Adding the private term proves (3). Independence is used only between the two disjoint actual private groups after fixing a false/false edge.

## Reference extraction: retain the negative normalization

Let R be ANY normalized nonempty output reference on all physical subsets, or a subprobability law with total mass<=1, which covers every Fourier-supported target of F_L. It must be fixed before sampling. Let

    Z_c=sum_{S nonempty core} R(S,empty),
    r_c(S)=R(S,empty)/Z_c.

The function g is nonconstant, so supported nonempty core coefficients exist; coverage ensures 0<Z_c<=1. The extracted reference is normalized and may be image-supported. Put C_g(r)=sum_{S nonempty} ghat(S)^2 log(1/r(S)). Then the EXACT core-sector extraction identity is

    C_g(r_c) = C_core(F_L;R)/(1-epsilon)^2
                              +Var(g) log Z_c.            (4)

The signed log Z_c is NONPOSITIVE and is the conditioning refund. It cancels all raw core-sector rarity whenever that rarity is just a common multiplicative scale. It must be retained before assessing payment. Other output costs are nonnegative because R(A)<=1, so only AFTER (4) is established may we infer

    C_g(r_c)<=C(F_L;R)/(1-epsilon)^2.                      (5)

For example, if R is uniform on all 2^N-1 nonempty physical subsets, then Z_c=(2^s-1)/(2^N-1); the negative Var(g) log Z_c cancels the ENTIRE extraneous private-label length, leaving exactly Var(g)log(2^s-1). This is genuine cancellation, not an argument that the remaining uniform core code is influence-paid. Majority already refutes such a uniform-core claim.

The core-only event is fixed from the supplied representation BEFORE the target Fourier set. Formula (4) constructs a reference for the DIFFERENT function g; it does not authorize resetting a spent reference along an adaptive restriction history of F_L.

## Finite quantitative reduction and exact FEI equivalence

Choose the explicit FINITE L=4s+4. Any nonconstant g has I(g)>=2^(1-s), since at least one physical edge changes sign. Since epsilon<=1/256, (1-epsilon)^-2<4, q<=1 and s+L=5s+4,

    2qepsilon[s(1-epsilon)+L]/(1-epsilon)^2
       <=8(5s+4)2^(-4s-4)
        =(5s+4)2^(-4s-1) <=2^(1-s)<=I(g).                (6)

The scalar sign 5s+4<=2^(3s+2) holds at s=1; increasing s adds5 on the left and multiplies the right by8, so it holds inductively. Equations (3),(5),(6) show: if a supplied reference for THIS finite F_L has complete nonempty cost<=K I(F_L), its conditioned core reference has complete nonempty cost<=2K I(g). This is a quantitative general Boolean-core reduction, with its exact conditioning refund, not just a limiting example. Finding the supplied physical reference remains the original hard problem.

There is also an exact SAME-CONSTANT FEI equivalence. For any fixed C, FEI H<=C I for every function in family (1), for all g,s,L, implies FEI with the SAME C for EVERY Boolean g. Indeed (3) gives I(F_L)->I(g), and (2a) plus continuity of -t log t on the finitely many core probabilities gives H(F_L)->H(g). Therefore H(g)<=C I(g). Conversely the full conjecture applies because F_L is an actual Boolean function. In fact H(F_L)/I(F_L)->H(g)/I(g), and the supremum ratio over this positive-private SIGNED-core clause family equals the supremum over ALL Boolean functions. No entropy bound for g is assumed in this implication. This does not construct any FEI counterexample.

Consequently a dimension-independent influence-paid whole-set dictionary for arbitrary signed-core positive-private clauses is already a route to FULL FEI. Bounded cores, one common anchor and injective private-parity lifts are useful restricted interfaces; they do not bypass this universality. The first unsupported line is a fixed core-sensitive dictionary whose complete signed fusion/reference cost is paid by the SAME physical influence account for arbitrary g, rather than assuming that a visible core has a cheap uniform or individual-anchor description.
