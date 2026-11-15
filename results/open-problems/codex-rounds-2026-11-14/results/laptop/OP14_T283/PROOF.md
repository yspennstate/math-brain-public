# Exact independence threshold for random alternating-form graphs

All vector spaces in this note are over F_2. A graph is simple and has labeled vertices. A family is L-wise linearly independent if every subfamily of size at most L is linearly independent.

## Theorem

Let n >= 2 and let v_1,...,v_n be nonzero vectors in F_2^K. Let B be a uniformly random alternating bilinear form on F_2^K, and set X_{ij}=B(v_i,v_j) for i<j. Let g be the smallest size of a linearly dependent subfamily of the v_i, with g=infinity if the whole family is independent.

If g is finite, the smallest number of distinct edge variables having a nonuniform joint distribution is exactly g-1. Equivalently, all marginals on at most g-2 edges are uniform, and some marginal on g-1 edges is nonuniform. If g=infinity, all edge variables are jointly uniform.

Both statements remain true after an independent uniform permutation of the vertices. After independent edge resampling with rate rho<1, the same exact threshold remains true. At rho=1 the entire graph is uniform.

In particular, L-wise linear independence, for L>=2, guarantees uniform marginals on at most L-1 edges. The guarantee is sharp.

## 1. Edge parities and alternating forms

For u,v in F_2^K, write w(u,v) in F_2^{binom(K,2)} for the vector with coordinates

    w(u,v)_{ab}=u_a v_b + u_b v_a,   a<b.

The entries b_{ab}=B(e_a,e_b), a<b, are independent uniform bits, and

    B(u,v)=sum_{a<b} b_{ab} w(u,v)_{ab}.

For a nonempty set F of edges, it follows that

    E_B[(-1)^{sum_{ij in F} X_{ij}}]
      = 1 if sum_{ij in F} w(v_i,v_j)=0,
      = 0 otherwise.                                      (1)

Indeed, a nonzero linear functional of independent uniform bits is uniform, whereas the zero functional is identically zero. A vector of t bits is uniform exactly when all its nonempty parity expectations vanish: expanding a point indicator as

    1_{X=x}=2^{-t} product_j (1+(-1)^{X_j+x_j})

proves both directions by taking expectations. Thus the first nonuniform marginal is the smallest support of an identically zero edge parity.

## 2. A zero edge parity forces a short vector dependence

Suppose F is nonempty, has t edges, and has identically zero parity. Discard vertices not incident to F. Let h be the number of remaining vertices, c the number of connected components, A the h by h adjacency matrix of F, and V the K by h matrix of their vectors.

The off-diagonal (a,b) entry of V A V^T is sum_{ij in F} w(v_i,v_j)_{ab}; its diagonal entries are zero in characteristic two. Hence the zero parity is equivalent to

    V A V^T=0.                                           (2)

Write R for the row space of V, of dimension q. On F_2^h, use the alternating form with matrix A. Equation (2) says that R is totally isotropic.

Here is the dimension bound, including its justification. The radical N=ker A has dimension h-rank(A). On the quotient F_2^h/N the induced form is nondegenerate. The image (R+N)/N is isotropic. For a nondegenerate bilinear form on a d-dimensional space, an isotropic subspace S satisfies S subset S^perp and dim(S^perp)=d-dim(S). Therefore 2 dim(S)<=d. Applying this with d=rank(A) gives

    q <= dim N + rank(A)/2 = h-rank(A)/2.                (3)

Each component of F contains an edge. Its adjacency matrix has the nonsingular principal submatrix [[0,1],[1,0]], so its rank is at least two. The components give diagonal blocks, and consequently

    rank(A)>=2c.                                        (4)

Every connected component on h_j vertices has at least h_j-1 edges, as follows by growing a spanning tree. Summing over components gives

    t>=h-c.                                             (5)

Together (3)--(5) imply

    q<=h-rank(A)/2<=h-c<=t.                              (6)

Also rank(A)>=2, so (3) implies q<h. Choose q independent columns of V spanning its column space. Any additional column is their linear combination. Moving that column to the other side gives a nonempty zero sum on at most q+1<=t+1 original vectors. Thus

    g<=t+1.                                             (7)

No identically zero edge parity can have fewer than g-1 edges. If the original vectors are all independent, (7) rules out every nonempty zero parity.

An independent derivation of the numerical bound (3) uses only rank loss under linear maps. Put k=h-q. Since the image of V^T has codimension k, restricting A to that image loses at most k dimensions of rank. Composing with V then loses at most another k dimensions, because ker V has dimension k. Thus

    rank(V A V^T)>=rank(A)-2k.

Equation (2) gives rank(A)<=2(h-q), or q<=h-rank(A)/2, exactly as in (3). This route does not use the isotropic quotient dimension argument.

## 3. A smallest vector circuit attains the bound

Suppose g is finite, and choose a dependent subfamily indexed by C of size g. Minimality and the fact that the field is F_2 imply

    sum_{i in C} v_i=0.

Since no vector is zero, g>=2. Choose a vertex a in C and take the star F={ai : i in C, i!=a}. It has exactly g-1 distinct edges, and for every alternating B,

    sum_{i in C, i!=a} B(v_a,v_i)
       =B(v_a,sum_{i in C, i!=a} v_i)
       =B(v_a,v_a)=0.                                   (8)

Its parity expectation is one, so its joint law is nonuniform. Combining (7) and (8) proves the threshold before permutation.

For sharpness of the L-wise guarantee, use K=L and the L+1 vectors

    e_1,...,e_L, e_1+...+e_L.

Their smallest dependence has size L+1: an expression involving the last vector requires all L basis vectors, and a subfamily of basis vectors is independent. Their edge law is uniform through L-1 edges and fails at L edges.

## 4. Permutations, noise, and random evaluation seeds

For a uniform independent permutation pi, a fixed observed edge set F satisfies

    E[(-1)^{sum_{e in F} X_e}]
      =Pr_pi{sum_{ij in pi^{-1}(F)} w(v_i,v_j)=0}.        (9)

This follows by conditioning on pi and applying (1). In particular every parity expectation is nonnegative. If |F|<g-1, it is zero for every pi by (7). A fixed observed star of g-1 edges has positive probability of being mapped onto the circuit star in (8). Its expectation is therefore positive. Thus permutation averaging preserves the exact threshold, even though it may reduce the size of the nonzero expectation.

Under independent resampling at rate rho, conditioning on the replacement set shows that any replaced edge in a parity makes its conditional expectation zero. If none is replaced the expectation is unchanged. Therefore every nonempty F satisfies

    E[(-1)^{sum_{e in F} Y_e}]
      =(1-rho)^{|F|} E[(-1)^{sum_{e in F} X_e}].         (10)

For rho<1 the multiplier is positive. This proves the assertion about noise, including preservation of failure at the first nonuniform degree.

There is a useful exactness consequence. Let V now be random, independent of the uniform B and the uniform pi, and assume its columns are nonzero almost surely. For any integer 1<=D<=binom(n,2), the resulting graph law is exactly D-wise uniform if and only if

    Pr{g(V)>=D+2}=1,                                    (11)

where infinity satisfies every such inequality. Sufficiency follows by conditioning on V. For necessity, if Pr{g(V)<=D+1}>0, some integer k between 2 and D+1 has Pr{g(V)=k}>0. Necessarily k<=n. Use a fixed observed star on k vertices. Given every such V, some permutation maps this star to a smallest circuit star, so its parity expectation is at least 1/n! on that event. All other conditional expectations are nonnegative by (1). Its unconditional expectation is positive, contradicting exact D-wise uniformity. This also holds at every rho<1 by (10).

If zero columns are allowed, exact uniformity even for single edges requires their absence almost surely: conditional on a zero column, a fixed observed edge has positive probability to meet it, making that edge's functional zero. Again no cancellation is possible in (9). Thus for n>=2 and D>=1, the unrestricted version of (11) adds the condition that every column is nonzero almost surely.

## 5. Consequence for T283 and limits

In Mao's construction, retaining the same evaluation vectors and random alternating form, L-wise independent evaluation vectors suffice for exact uniformity through L-1 edges. This replaces the sufficient bound floor(L/2) in Proposition 2.6. In terms of a target degree D, it suffices that the evaluation-vector code have no nonempty dependence of size at most D+1; the earlier sufficient requirement was independence through 2D vectors. For this construction the new requirement is also necessary, by (11).

Consequently, an unconditioned mixture over candidate seeds cannot repair failures of exact uniformity: each bad seed contributes nonnegative Fourier coefficients. Even a very small positive probability of a circuit of size at most D+1 is incompatible with the exact requirement. This is a limitation of the independent uniform alternating-form construction, not of every possible planted graph sampler.

This note neither constructs a uniform polynomial-time sampler nor changes the noise-robust distinguishing analysis. T283 remains open. No replacement of a general conjecture or change to an integrator's problem record is made here.

Reference: Songtao Mao, *The Polynomial-Time Low-Degree Conjecture is False*, arXiv:2607.20318v2, Proposition 2.6 and Section 4. https://arxiv.org/html/2607.20318v2
