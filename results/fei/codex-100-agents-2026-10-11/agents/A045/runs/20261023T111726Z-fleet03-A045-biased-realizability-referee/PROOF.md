# A045: independent activation review and multiselector realizability audit

All logarithms are natural. This is a reconstruction of A042's exact activation
claim and a finite-depth corollary, not an arbitrary-seed FEI supplier.

## 1. Conventions and admission

Let g be a Boolean sign on an independent finite product cube. Contract all
deterministic coordinates before normalized Fourier coefficients are formed.
For nonempty T put v_T=product_{i in T}4p_i(1-p_i), c_T=E[g product(X_i-p_i)]/
product_{i in T}2p_i(1-p_i), and P_T=v_T c_T^2. Write a=(1-Eg)/2,
V=4a(1-a), I=sum |T|P_T, Delta=I-V. For occupied T choose j_T>=0 with
1/2<2^j_T|c_T|<=1, W_T=v_T4^-j_T, Z=sum W_T, and
J=ln4 sum P_T j_T. The complete reference has Q(empty)=P(empty),
Q(T)=VW_T/Z. K=KL(P||Q) is FULL ordinary KL. E=sum P_T ln(1/c_T^2),
n=V ln(Z/V), so E=J+n-K. Constants are handled without dividing by V.

## 2. Independent reconstruction of A042@1

For independent X~Bernoulli epsilon=2^-k, k>=1, F=1-X+Xg,
direct centered differences give c_F(T)=epsilon c_T,
c_F(XT)=c_T/2, c_F(X)=-a. Hence the actual masses are
epsilon^2 P_T, epsilon(1-epsilon)P_T, and4epsilon(1-epsilon)a^2;
the empty mass is (1-2a epsilon)^2. These sum to one, without a reset.
Thus I_F=epsilon I+4a epsilon(1-epsilon),
Delta_F=epsilon Delta+epsilon(1-epsilon)V.

The scale cells are respectively k+j_T,1+j_T,j_a, where
1/2<2^j_a a<=1. There is zero carry, including boundary a=1/2 where j_a=1.
For B=V+4a^2 j_a this gives
J_F=epsilon J+ln4[epsilon(1-epsilon)B+epsilon^2 kV].
For j_a>=1, j_a a<=j_a2^-j_a<=1-2^-j_a<=1-a;
for j_a=0 the term is zero. Therefore V<=B<=2V. Also
k/(2^k-1)<=1, so the OUTER gate satisfies
J_outer<=3ln4 Delta_outer, sharply at a=epsilon=1/2.
This uses only the outer portion epsilon(1-epsilon)V, not a renewed seed bank.
The exact error in J_F/epsilon-J-ln4 B is ln4 epsilon(kV-B), whose
absolute value is at most ln4 epsilon(k+2)V. In particular epsilon J
does not disappear relative to the inherited epsilon I.

Taking logs of the three actual sectors gives
E_F=epsilon E+epsilon(1-epsilon)V ln4+2epsilon^2 V ln(1/epsilon)
    +4epsilon(1-epsilon)a^2 ln(1/a^2).
This identity does not require dyadic epsilon; the cell claims do.

Put b=4^-j_a and w=4a epsilon(1-a epsilon). Complete flat reference weights
give Z_F=epsilon Z+4epsilon(1-epsilon)b and
Z_o=epsilon V+4epsilon(1-epsilon)b for the actual outer gate.
In the nonempty law the singleton-selector sector has physical probability
s=4epsilon(1-epsilon)a^2/w, and reference probability
t=4epsilon(1-epsilon)b/Z_F. In the complementary seed sector BOTH laws
have the same placement probabilities epsilon,1-epsilon; the remaining
likelihood is P_T/V against W_T/Z. The empty ratio is one. Therefore
K_F=epsilon K+w d_Bern(s||t).
For the complete outer-gate/seed reference replace t by t_o with Z_o;
K_tree=epsilon K+w d_Bern(s||t_o), n_tree=n_o+epsilon n.
Consequently the signed conversion is exactly
K_F-K_tree=w ln(Z_F/Z_o)-epsilon V ln(Z/V).
Both KLs refer to complete laws; they replace each other when references change.
Since b>=a^2 and Z>=V, Z_o>=w and ln x<=x-1 gives
0<=w ln(Z_F/Z_o)<=epsilon(Z-V). This is the inherited seed allocation
once, even if an external theorem bounds Z-V by a multiple of Delta.

For fixed 0<a<1, s->a and t->4b/(Z+4b), both interior, so the exact full
endpoint is K_F/epsilon->K+4a d_Bern(a||4b/(Z+4b)).
At a=0 the function is constant. At a=1 and one selector it is a signed
literal and all corrected costs vanish. epsilon=0 or1 is contracted
physically. Reflecting X preserves squared coefficients and yields the
probability-one-coordinate endpoint stated by A042, without pretending
that activation probability tends to one in the k>=1 formulas.

Verdict: HOLDS for A042-DYADIC-ACTIVATION-ENDPOINT-CERTIFICATE@1 as stated,
including its explicit OPEN arbitrary-seed obligation. No source repair supplied.
Its optional A044 normalizer bound was already independently reconstructed in
A045 stage8 and is not counted as a fresh independent review here.

## 3. Full physical spectrum of several independent selector wires

Let m>=1, X_j independent Bernoulli epsilon_j=2^-k_j, k_j>=1, on blocks
disjoint from g and from each other. Define epsilon=product epsilon_j,
A=product X_j, F=1-A+Ag, K_sel=sum k_j,
D_sel=sum_j[(1-epsilon_j)+epsilon_j k_j], and
L_sel=sum_j(1-epsilon_j). Let nu(U)=product_{j in U}(1-epsilon_j)
product_{j notin U}epsilon_j, a genuine probability law on selector subsets.
For nonempty seed T and any selector subset U,

 c_F(U,T)=c_T 2^-|U| product_{j notin U}epsilon_j,
 P_F(U,T)=epsilon nu(U)P_T,
 j_F(U,T)=j_T+|U|+sum_{j notin U}k_j.

For T empty and U nonempty,

 c_F(U,empty)=-a 2^(1-|U|)product_{j notin U}epsilon_j,
 P_F(U,empty)=4a^2 epsilon nu(U),
 j_F(U,empty)=j_a+|U|-1+sum_{j notin U}k_j.

Every displayed shift is a nonnegative integer where it is used. This is
an exact Boolean spectrum, not a freely chosen spectral product law. The empty
mass is (1-2a epsilon)^2, and nu(empty)=epsilon. Summing these masses yields

 I_F=epsilon I+4a epsilon L_sel,
 Delta_F=epsilon Delta+epsilon[4a L_sel-4a^2(1-epsilon)],
 J_F=epsilon J+ln4 epsilon[4a D_sel+4a^2(j_a-1)(1-epsilon)
                              -4a^2 epsilon K_sel].             (M)

The bracket is exactly J_outer/(epsilon ln4), for the actual (m+1)-input
gate on the selectors and a literal Y of mean1-2a. Its Delta is the bracket
in the preceding Delta identity. Iterating the independently reconstructed
one-selector bound, starting with Y of J=Delta=0, proves
J_outer<=3ln4 Delta_outer for all m and all these labeled laws. It also proves
J_F<=max(K,3ln4)Delta_F CONDITIONALLY on J_g<=KDelta_g. The constant is sharp
already at m=1; no arbitrary-seed premise is supplied by this corollary.

The complete flat reference retains the same full empty mass and has

 Z_F=epsilon Z+4b epsilon(1-epsilon),
 Z_o=epsilon V+4b epsilon(1-epsilon),
 K_F=epsilon K+w d_Bern(s||t),
 s=4a^2 epsilon(1-epsilon)/w, t=4b epsilon(1-epsilon)/Z_F.

These last quantities depend on the selector biases only through their product.
Indeed, conditional on being in the pure-selector sector, both actual and
reference laws have selector label nu(U)/(1-epsilon), U nonempty. In the seed
sector both have placement nu(U), and the seed likelihood is unchanged.
For the complete reference composed from this actual (m+1)-input outer gate
and Q_g, K_tree=K_outer+epsilon K_g. The signed conversion and positive
transfer bound from Section2 hold verbatim. This composition is not asserted
to equal every reference produced by a sequence of binary decompositions.

Corrected entropy has the exact additional identity
E_F=epsilon E+ln4 epsilon[4a D_sel-4a^2(1-epsilon)-4a^2 epsilon K_sel]
                    +4a^2 epsilon(1-epsilon)ln(1/a^2).
Consequently the mantissa remainder is
L_F=epsilon L_g+4a^2 epsilon(1-epsilon)ln(b/a^2), also independent of
selector shape at fixed product. J and I generally retain selector shape.

## 4. Adversarial admission and first unpaid line

Independence is essential. For a fair signed-literal seed and selector
probability p=1/3, reusing the same physical selector twice gives mean1-p=2/3
and empty mass4/9. Inventing two independent copies gives mean1-p^2=8/9
and empty mass64/81. Their different physical functions cannot be interchanged.
Spectral selector absence is not restriction X=0: fair AND2 conditioned on
absence has empty/surviving-singleton masses1/2,1/2; physical X=0 is constant.
Deterministic zero and one selectors contract to a constant and to g,
respectively. A negative constant seed with MULTIPLE selectors is generally
an AND sign, not a signed literal; the single-selector zero-deficit statement
must not be extrapolated to that case.

The first unsupported line toward full FEI is still an influence-priced
supplier for the arbitrary inherited seed J (or its complete reference bill)
from the SAME unused original capacity after all earlier debits. Equations(M)
and the full ordinary-KL chain preserve, rather than solve, that obligation.
Independent review of the multiselector corollary is pending. Finite checks
verify the identities and admission controls; the all-depth assertions rest
on the derivation and induction, not an extrapolation of those checks.
