# Local eligibility does not pay reference coupling

All logarithms are base two, a=log2(e). This is a negative interface result with an actual Boolean source, not a counterexample to FEI or to an inherited-product-root policy.

## 1. Sector decomposition

Partition physical coordinates into blocks B_j. For any subset S let Z_j=1[S intersects B_j]. Let p be a finite subset distribution, d_i its actual inclusion marginals, and Q the product of Bernoulli(d_i). Write q for the occupancy law of Q, so q is a product law. Assume positive probabilities for simplicity. Define a supporting reference by

    R(S)=r(Z(S)) Q(S | Z(S)),

where r is an arbitrary positive occupancy law. Its actual block marginal is R_j(S_j)=r_j(Z_j) Q_j(S_j | Z_j). Consequently

    T := TC(p)-KL(p||R) = E_p log(R/Q) = E_{p_Z} log(r/q),
    T_j := TC(p_j)-KL(p_j||R_j) = E_{p_Zj} log(r_j/q_j),
    C_p(R) := E_p log(R/product_j R_j) = E_{p_Z} log(r/product_j r_j),
    T = sum_j T_j + C_p(R).

Choose r=p_Z. Then these identities become EXACTLY

    T = KL(p_Z||q), T_j = KL(p_Zj||q_j), C_p(R)=TC(p_Z).

No assumption about the conditional source law within a sector is needed. In particular, no conditional-source entropy is deleted by these identities.

More generally, allow each occupied-block conditional reference to be Q_j tilted by lambda_j^rank and renormalized, with 0<lambda_j<=1, independently inside the blocks GIVEN Z. Assume each source block has empty dominance. Its conditional source rank mean is I_j/P(Z_j=1), at least I_j/Q(Z_j=1), the conditional rank mean of Q_j. The derivative of the conditional expected log likelihood with respect to log(lambda_j) is this source mean minus the tilted-Q mean; it is nonnegative for lambda_j<=1. The conditional log likelihood is zero at lambda_j=1, hence nonpositive below one. Adding blocks proves the corrected projection bound

    TC(p)-KL(p||R)
       <= KL(p_Z||q)-KL(p_Z||r)
       = TC(p_Z)+sum_j KL(p_Zj||q_j)-KL(p_Z||r)
       <= TC(p_Z)+a I(p)-KL(p_Z||r).

This retains the full occupancy divergence, not merely a clipped coupling. The binary bound in the last line can also be checked directly: if alpha=p_j(empty)>=beta=Q_j(empty), its second binary-KL term is nonpositive, while alpha log(alpha/beta)<=-alpha log(beta)<=sum_{i in B_j} -(1-d_i)log(1-d_i)<=a I_j. Here alpha<=1-d_i. If r is a product law, KL(p_Z||r)=TC(p_Z)+sum_j KL(p_Zj||r_j), recovering the block-product projection bound. The example below shows the occupancy correction cannot in general be omitted.

## 2. Actual Boolean family with every local block eligible

Let k>=2, n=2k, and f_n(x)=1-2*1[x=0] on the uniform binary cube, with the usual Walsh characters. Set d=2^(1-n). The squared spectrum has

    p(empty)=(1-d)^2, p(S)=d^2 for every nonempty S,
    d_i=d, I(f_n)=2kd.

Partition into k consecutive pairs. Write t=3d/2 and rho=2d-d^2. The occupancy law is

    p_Z(0)=(1-d)^2,
    p_Z(z)=d^2 3^|z| for z!=0,
    P(Z_j=1)=t.

The actual coordinate product Q has independent pair occupancy, q_j(0)=(1-d)^2 and q_j(1)=2d-d^2. Use the reference R from section 1 with r=p_Z.

For each block, p_j(empty)=1-t >= (1-d)^2=Q_j(empty), since d<=1/8. Moreover R_j conditional on nonempty is EXACTLY Q_j conditional on nonempty. Thus every local block satisfies the previous empty-dominance/common-odds eligibility with lambda_j=1; its empty tilt is allowed and positive. All source and reference atoms are positive. Neither a source-zero convention nor loss of local eligibility causes this example.

Each local signed projection equals a binary KL and obeys T_j<=a I_j by the previously proved projection inequality. Nevertheless T/I and C_p(R)/I are unbounded.

## 3. Quantitative all-k lower bound

TC(p_Z)=k h2(t)-H(Z). Let A=1[Z!=0]. Because Z=0 is deterministic given A=0 and there are at most 2^k possibilities otherwise,

    H(Z)<=h2(rho)+rho k.

For x in [0,1], -(1-x)log(1-x)<=a x. Also x log(1/x) increases on (0,1/e). Here rho<=2d<=1/4<1/e. Hence, using a<3/2,

    h2(rho)<=2d log(1/(2d))+3d = 2d(2k-1/2) <= 2d(2k+1/2),
    H(Z)<=2d(3k+1/2).

Since h2(t)>=t log(1/t) and log2(3)<2,

    k h2(t) >= (3kd/2)(2k-log2(3)) > 3kd(k-1).

Dividing by I=2kd gives the rigorous bound

    C_p(R)/I = TC(p_Z)/I > (3k/2)-(9/2)-1/(2k).

Furthermore T=TC(p_Z)+sum_j KL(p_Zj||q_j)>=TC(p_Z), so the same lower bound holds for T/I. For every fixed constant c, choose any finite k with this lower bound >c. There is no passage to an infinite distribution and no optional-stopping limit in this argument.

For reference, the entropy used above also has the exact finite formula

    H(Z)=-(1-d)^2 log((1-d)^2)-2 rho log(d)-kt log(3).

## 4. What is refuted and what survives

Refuted: a universal assertion that arbitrary supporting references whose EVERY block marginal meets the empty-dominance/common-odds conditions have [TC(p)-KL(p||R)]_+ <= c I(p) for an absolute c. It fails already for two-coordinate blocks, lambda_j=1, and actual point-function spectra. Thus no rule using only current block eligibility can supply the missing coupling payment. The product-reference theorem remains valid because its coupling is identically zero.

Not refuted: the hereditary claim for references actually obtained by the coherent physical kernel from one specified original product root, retaining its unspent owner. No such root-to-R transport history is supplied here. A087's arbitrary-reference point-source obstruction motivates this test, but the new distinguishing condition is simultaneous eligibility of every nontrivial block. The first unsupported line toward the universal target is a bound on the coupling of ACTUALLY REACHABLE inherited references in terms of the SAME unused original owner (or a certified policy avoiding the costly reference), with all query charges and terminal entropy retained.

The source family itself has bounded H/I: H(f_n)=-(1-d)^2 log((1-d)^2)+(2d-d^2)(2n-2), so H/I<=4+2a/n. Unbounded reset liability is therefore a reference-policy obstruction, not an FEI disproof.

## 5. Scoped independent review consumed this stage

A061 stage20 section 0 (bent-mask reduction), read at its source, independently reconstructs as follows. For F=(-1)^(UV)f and reference R/4, both spectra factor as the core times a uniform four-atom bent factor. Any physical core query made before V transports this factor unchanged, including fair source-zero rows, so core K,E,O agree exactly. Revealing V has E=O=0. On positive source core rows its child fixes the U spectral bit and its reference probability there is exactly R(T); source-zero core rows retain fair reference mass on both U sectors. Therefore the two child KLs equal the core K and the two child total correlations equal the core TC. The finite-tree Bellman reset reserve is identical for policies consisting of a core-only prefix followed by V and an immediate optional product reset/stop. This independently accepts that scoped reduction; it does not accept the full field-family bundle or assert arbitrary post-V core-query equivalence. Retaining the source-zero reference mass is essential.
