# Quantitative edit distance forced by genuine criticality

Finite uniform cubes, Boolean signs, normalized Walsh coefficients, entropy in bits. Let n>=3, p=2^-n. Let F have Fourier support with minimum Hamming distance at least three. Let G differ from F on exactly R physical vertices. No factorization, parity of R, sign pattern, connectivity, or symmetry hypothesis is imposed on the edit set.

For every coordinate i, write L_i=H(G)-[H(G|i=0)+H(G|i=1)]/2. If R>=1, then

    L_i < [10R+(17/2)R^2]p.                         (1)

For every relevant coordinate Inf_i(G)>=2p. Therefore every such coordinate is strictly paid at

    K_R=5R+(17/4)R^2,   L_i<K_R Inf_i(G).        (2)

The unused original bank identity is exact:

    E[D_K(child)]-D_K(G)=K Inf_i(G)-L_i.

Every complete child, including constant and inessential children, retains its reach 1/2. At the simpler rate K=10R^2 the gain is greater than (3/2)R^2 p. For R=0 the loss L_i is exactly zero; the ratio at an irrelevant coordinate is never divided by zero.

Consequently, if G is a least-essential-dimension positive K-witness, H(G)-KI(G)>0, with K>=0, then it cannot be such a seed itself, and for EVERY such seed at edit distance R>=1 it necessarily satisfies

    K < 5R+(17/4)R^2.                            (3)

Equivalently R>(2/17)(sqrt(25+17K)-5). This is a necessary condition on a hypothetical critical witness, not a proof that a violating witness exists. The earlier sharper one-edit all-policy two-query rate9 remains available; the current constants trade sharpness for arbitrary edit sets.

This is a root-local admission theorem. A restriction can destroy the seed's distance-three packing property. It does not grant a fresh bank after a query or justify applying the displayed rate to the inherited third-query collision. The previous stage's all-policy third-query counterfamily remains compatible with this theorem.

## 1. Exact row decomposition and a proved curvature bound

For fixed i, pair the actual signed coefficients a_T=Ghat(T), b_T=Ghat(T+i), with T not containing i. Let q_T=a_T^2+b_T^2. They sum to one. The two actual restricted coefficients are a_T+b_T and a_T-b_T; their squared distributions are normalized because the restrictions are Boolean.

Let B=sum_T q_T h2(b_T^2/q_T), ignoring zero rows. Let J be the Jensen-Shannon divergence of those two complete child spectral distributions. Entropy grouping gives L_i=B+J exactly. In row form, with z=2ab/q,

    J_T=(q/ln2)*psi(z),
    psi(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2.

We use the sharp elementary curvature bound

    0<=J_T<=2 min(a^2,b^2)/ln2.                 (4)

Here is a proof, including the endpoints by continuity. For 0<=z<1, psi'(z)=atanh(z). Since both functions vanish at zero and

    (atanh z)'=1/(1-z^2) <= 1/(1-z^2)^(3/2)
                              =(z/sqrt(1-z^2))',

we have atanh(z)<=z/sqrt(1-z^2). Integrating once more gives psi(z)<=1-sqrt(1-z^2). Both sides are even. Finally q[1-sqrt(1-z^2)]=2min(a^2,b^2). Thus no independent-row assumption is used.

## 2. Surgery energy and occupied-row liability

Put e=G-F=-2F 1_E. Parseval gives sum ehat^2=4Rp and the triangle inequality gives |ehat(S)|<=2Rp for every label. Radius-one Hamming balls about the seed support are disjoint, so its cardinality s satisfies

    s(n+1)<=2^n.

Each i-row contains at most one seed coefficient. Call rows with one seed coefficient occupied; orient their anchor as a. There are exactly s occupied rows. In such a row b=ehat(off-anchor label). Let beta be the sum of b^2 over occupied rows. Then

    beta<=s(2Rp)^2<=4R^2 p/(n+1).              (5)

Empty rows have both coefficients equal to those of e; their total mass M is at most 4Rp. Since binary entropy is at most one and (4) is at most q/ln2 on each empty row,

    B_empty+J_empty<=M(1+1/ln2)<10Rp.         (6)

The strict numerical bound uses ln2>2/3, obtained from ln2=2[1/3+(1/3)^3/3+...]. In particular no dimension factor is charged to empty rows.

For occupied rows, the anchor entropy term obeys

    a^2 log2(1+b^2/a^2)<=b^2/ln2,

with the zero-anchor endpoint interpreted continuously. The other terms aggregate by the log-sum inequality:

    sum b^2 log2(q/b^2)<=beta log2((sum q)/beta)
                                     <=beta log2(1/beta).

Hence

    B_occupied+J_occupied
        <=beta log2(1/beta)+3beta/ln2.         (7)

No premise about independence or a product of row probabilities occurs here.

## 3. Boolean granularity removes the residual logarithm

Every normalized coefficient of an n-bit Boolean sign is an even integer times p. Thus if beta>0, one of its summands is at least 4p^2. Consequently log2(1/beta)<=2n-2. Combining (5)--(7) gives

    L_i <10Rp+(2n+5/2)*[4R^2 p/(n+1)]
        =[10R+(8+2/(n+1))R^2]p
        <=[10R+(17/2)R^2]p.

When beta=0 the same conclusion follows directly from (6). No smallness assumption on R or beta is used: beta<=1 automatically, and the bound uses its actual positive lower granularity rather than a monotonicity assumption about binary entropy.

If i is relevant, at least one unoriented cube edge crosses the sign boundary. Each such edge contributes 2/2^n to influence, proving Inf_i>=2p. This proves (2) without assuming an odd negative count. At K=10R^2, subtraction yields gain greater than [(23/2)R^2-10R]p>=(3/2)R^2p.

If R=0, each signed row has only one nonzero coefficient. The actual children have the same squared coefficients as the root, so B=J=L_i=0.

## 4. Genuine criticality and exact eligibility

In a least-essential-dimension positive K-witness all coordinates are relevant after deleting unused coordinates. Every physical child has smaller essential dimension, so each has D_K<=0. Therefore the exact complete physical bank satisfies

    L_i-K Inf_i=D_K(G)+E[-D_K(child)]>0.

This contradicts (2) whenever K>=K_R. For R=0 it contradicts L_i=0. This proves (3). The argument does not use a transformed child or claim affine preprocessing supplies free funding. It also applies to the stronger least-dimensional selector that licenses every affine child image.

## First unsupported universal line

Neither criticality nor primitivity is shown to force a uniformly bounded edit distance to a distance-three seed. Nor is the signed bill of the residual far-from-every-code critical class controlled. The next unpaid line is to select an original proper block with enough independent UNUSED child release on that residual class, retaining its SAME deficit and complete terminal bank. The necessary radius bound above is a quantitative structural exclusion, not that selection theorem and not full FEI.
