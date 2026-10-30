# Positive outer correction does not form a coherent envelope

Full FEI remains OPEN. This refutes the candidate proposed in A089 stage9 NEXT, not A089's conditional coherent-envelope/rerouting theorem.

## Candidate, conventions and exact family

For disjoint physical inner Boolean functions f_j and an outer Boolean gate h, let mu_j=E f_j, v_j=1-mu_j^2, and q_j be the true pivotal probability of h in input j under the other independent inner signs. The exact composition identity is

    H(h(f_0,f_1,f_2))=C(mu)+sum_j q_j H(f_j),
    C(mu)=H(occupied outer spectrum)-sum_j q_j h2(v_j).

At rate K put S_K=K I-H, and let rho_j be the full stopping deficit hull of inner core j. The proposed envelope is

    U_K=(C)_+ + sum_j q_j rho_j.

It majorizes (-S_K)_+, since S_K=sum q_j S_K(f_j)-C and S_K(f_j)+rho_j>=0. Eligibility for A089's theorem additionally requires full-query superharmonicity U(parent)>=mean U(children). That condition is false, even at every real K>=3.

Physical bits are0/1; a Fourier character is (-1)^popcount(x&A), and entropy is in bits. Set g_m(x)=-1 only at the allzero m-bit point, and +1 elsewhere. Let h be +1 precisely when all its three input signs are +1. Its bit truth integer is1, with sign-1 encoded by bit1. Take

    F=h(g_3,g_2,g_2),

on three disjoint blocks of sizes3,2,2. Equivalently F is +1 iff all three physical blocks are nonzero, i.e. AND of OR clauses of sizes3,2,2. Query original physical bit0 in the first block. Answer0 gives h(g_2,g_2,g_2); answer1 gives h(+1,g_2,g_2), the complete four-essential-bit two-clause function, with two pointwise dummy variables still present in its original six-free-bit physical domain. Both outcomes are retained, each at reach1/2.

Every restriction of g_m is a smaller g_r or a constant. H(g_1)=0,I(g_1)=1; H(g_2)=2,I(g_2)=1; H(g_3)=4-(9/8)log2(3),I(g_3)=3/4. The last rate3 slack is positive exactly when3^9>2^14, checked as19683>16384. Constants have H=I=0. Consequently all these inner functions and restrictions have nonnegative S_K for every real K>=3, so ALL inner hulls rho_j are exactly0. The proposed U_K therefore equals C_+, independently of K throughout this entire interval.

## Complete exact calculation

For the literal outer gate, hhat(empty)=-3/4 and hhat(M)=1/4 for every nonempty M. In the centered product basis let

    c_U=sum_(M containing U) hhat(M) prod_(j in M\U)mu_j,
    p_U=c_U^2 prod_(j in U)v_j.

Character orthogonality proves that p_U are the occupied-set masses. Conditional on occupied U, disjoint nonempty core Fourier laws multiply. Shannon's chain rule gives the displayed H identity; weighted physical edges give I=sum q_j I_j. In particular, no product law for the outer occupied subset is assumed.

For the parent, mus=(3/4,1/2,1/2), pivotal probabilities=(9/16,21/32,21/32), and the eight occupied masses, in subset order0..7, are

    (1,567,1323,189,1323,189,441,63)/4096.

For answer0 all mus are1/2. The empty mass is25/1024, each singleton243/1024, each pair81/1024, and the triple27/1024. For answer1, after the constant first core is omitted, the four masses are(1,27,27,9)/64. Substituting in C yields the exact expressions

    C_parent =57/8 -(1431/1024)log2(3) -(3087/2048)log2(7),
    C_0      =53/8 -(1701/512)log2(3) -(25/512)log2(5),
    C_1      =3 -(27/16)log2(3).

All three are strictly positive. Independent integer-power certificates are

    2^14592 > 3^2862 * 7^3087,
    2^3392  > 3^1701 * 5^25,
    2^48    > 3^27.

Therefore clipping does not affect this row, and its superharmonicity failure is

    G=(C_0+C_1)/2-C_parent
      =-37/16 -(567/512)log2(3) -(25/1024)log2(5)
        +(3087/2048)log2(7) >0.

The sign is exactly the finite integer inequality

    7^3087 > 2^4736 * 3^2268 * 5^50.

Python arbitrary-precision integer comparison verifies it, independently of directed-log signs. The separate directed192-bit enclosure gives

    0.107184 < G < 0.107185.

The parent influence is111/64; the two full child influences are27/16 and3/2. Their telescoping difference, and the independently counted queried-bit influence, equal9/64. Thus the modified candidate U_K+lambda I needs at least

    lambda >= (64/9)G,
    0.762198 < (64/9)G < 0.762199,

on this query. This is a necessary LOCAL repair coefficient, not a sufficient bound across other gates, dimensions or histories.

The initial account with credit U_K is locally solvent because U_K majorizes (-S_K)_+. However no mean-conserved allocation starting from exactly U_K(parent) can dominate BOTH child requirements U_K: their mean is larger by G. Reassigning original owner labels or rerouting siblings cannot create that missing conditional mean. A supplied extra reserve G, or a changed potential that releases it, is required if these child requirements are retained. This does not say the Boolean children themselves require positive FEI deficit banks: the candidate may overprotect them. It refutes superharmonicity of this proposed candidate, not feasibility of every possible envelope.

## Frozen family, completeness and executed scope

The declared design has128 outer three-input truth tables modulo output complement; first inner g_m or -g_m for fixed m2..6; each other core g_2,-g_2 or dictator. There are128*10*9=11520 designated first-core query rows and at most10 physical bits. Output complementation preserves every squared spectrum, C and q; no additional unproved quotient is used. The576-row pilot restricts outer integer0..15 and m2..3. It stops at row55 with the witness above; NO exhaustive pass over the full family or the remaining pilot rows is claimed. Once the strict witness and independent reproduction were available, no full search was necessary.

The producer computes exact direct three-bit Walsh-subset occupied masses and full H/I. Its second lane constructs the whole physical truth table, fast integer Walsh, inverse characters and physical edges for parent and both children. The independent author checker imports no producer, uses direct whole-cube character sums and edges, and reconstructs

    C=H(full physical function)-sum_j I(physical block j)*H(g_j)/I(g_j).

Disjointness justifies I(block j)=q_j I(g_j). Constant cores contribute0 and are omitted without deleting the other full terminal. It agrees exactly with every saved C/H/I form. Altered correction and drift values are rejected as positive controls. Finally the closed-form powers certify all essential signs without logarithm approximation. The new result is author checked; independent external acceptance is still pending.

## Universal bridge and first unsupported line

C019/C024 coherent-envelope repair remains valid conditionally. This stage removes the suggested positive-outer-correction candidate from the list of universally coherent envelopes, uniformly for all K>=3, and prices its exact missing one-query mean stock G on an actual seven-bit family. The next unpaid line is to pay the drift of the SIGNED outer correction from unused original influence/variance stock while keeping a full-universe superharmonic envelope and an influence-paid initial account. Merely increasing K leaves this witness's inner hulls0 and does not fix it; replacing the whole correction by its positive part does not preserve the needed drift. A universal envelope, or a Boolean unbounded H/I family, is still unproved.
