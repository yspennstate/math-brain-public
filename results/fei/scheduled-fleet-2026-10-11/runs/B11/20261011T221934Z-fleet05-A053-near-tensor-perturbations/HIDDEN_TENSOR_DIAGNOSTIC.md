# A053: quantitative surgery and hidden tensors

All entropies are in bits. Encode the uniform cube as {0,1}^n, with characters chi_S(x)=(-1)^(S dot x), and write x^i=x xor e_i. This is equivalent to the sign cube. Let p=2^(-n), f be any Boolean sign, a a vertex, and g=f-2f(a)1_a. The result is an actual Boolean sign differing from f at exactly one point. Statements below are self-contained analytic results; independent review is pending.

## 1. Signed spectrum, influence, and additive derivatives

Write alpha_S=fhat(S). Exactly,

    ghat(S)=alpha_S-2p f(a)chi_S(a),
    P_g(S)=alpha_S^2-4p f(a)alpha_S chi_S(a)+4p^2.

The cross term must be retained. Put r_i=f(a)f(a^i), r_ij=f(a)f(a^i^j). Reversing one vertex toggles only its incident coordinate edges. Each undirected edge has two uniform endpoints, hence

    Inf_i(g)-Inf_i(f)=2p r_i,
    I(g)-I(f)=2p sum_i r_i,
    |I(g)-I(f)|<=2np.

Define D_i f(x)=[f(x)-f(x^i)]/2. For distinct i,j,

    K_ij(f)=E[(D_i D_j f)^2]=sum_(S contains i,j) alpha_S^2.

The squared perturbation contributes 4p^2*2^(n-2)=p. The linear term contributes

    -4p f(a) sum_(S contains i,j) alpha_S chi_S(a)
    =-p[1-r_i-r_j+r_ij].

Thus exactly

    K_ij(g)-K_ij(f)=p(r_i+r_j-r_ij),
    |K_ij(g)-K_ij(f)|<=3p.

In particular the sum over pairs changes by at most 3 binom(n,2)p. This is additive derivative energy, not a tensor nonfactorization criterion. For f=h(x_A)k(x_B), i in A and j in B, K_ij(f)=Inf_i(h)Inf_j(k), potentially large on an exact product.

The centered spectral covariance M_ij=K_ij-Inf_i Inf_j is zero across a product cut. In that case r_ij=r_i r_j and, with u_i=Inf_i(f), u_j=Inf_j(f),

    M_ij(g)=p(r_i+r_j-r_i r_j)
             -2p(r_i u_j+r_j u_i)-4p^2 r_i r_j,
    |M_ij(g)|<=7p+4p^2.

The covariance can have either sign; positivity of raw K_ij does not express failure of product structure. All these bounds are uniform in f, its factor count, dimensions, and a.

## 2. Exact multiplicative curvature and factorization

Define the Boolean plaquette

    sigma_ij^f(x)=f(x)f(x^i)f(x^j)f(x^i^j),
    c_ij(f)=P[sigma_ij^f(X)=-1].

Surgery changes the sign of exactly the one physical two-face containing a; each of that face's four vertices is counted in c_ij. The plaquette sign before surgery is constant across that face. Therefore, for every distinct i,j,

    c_ij(g)-c_ij(f)=4p sigma_ij^f(a).

For an exact product and a pair crossing its factor cut sigma is identically +1, giving c_ij(g)=4p. This is the smallest possible strictly positive plaquette probability in dimension n: every defective face contributes four vertices. A merely positive lower bound of this quantized size is no separation from a tensor.

For any nontrivial partition A,B, f=h(x_A)k(x_B) if and only if c_ij(f)=0 for all i in A,j in B. Necessity is direct cancellation. For sufficiency write f=(-1)^b with b valued in F_2. Vanishing plaquettes say that the discrete derivative of b in every A direction is independent of all B coordinates. Walk in A from 0 to x_A with x_B fixed and with x_B=0: the increments agree, so

    b(x_A,x_B)=b(x_A,0)+b(0,x_B)+b(0,0) mod 2.

Exponentiating gives the factorization. Consequently the graph with edges c_ij>0 is disconnected exactly when a nontrivial coordinate tensor factorization exists. Graph connectivity is qualitative; surgery supplies exponentially small edges across an old factor cut.

## 3. One-point surgery makes every product tensor-prime

Let n>=2 and f=h(x_A)k(x_B) with A,B both nonempty, allowing constant factors. The product of f over the entire cube is

    [product_(x_A) h(x_A)]^(2^|B|)
    [product_(x_B) k(x_B)]^(2^|A|)=+1.

After one flip the whole-cube product is -1. Every nontrivial coordinate tensor product has whole-cube product +1 by the same argument; g is therefore tensor-indecomposable over every partition, not merely the original partition. This is a parity argument, not a circuit picture. Equivalently g has an odd number of negative values.

There is also full Fourier support. The integer Walsh sum W_S=sum_x g(x)chi_S(x) equals sum_x chi_S(x)-2 sum_(g(x)=-1) chi_S(x). For n>=2 the first sum is divisible by four, and the second inner sum is odd. Hence W_S=2 mod 4 for every S, and no coefficient vanishes. In particular every coordinate is essential and every K_ij(g)>0. Full support is only a qualitative admission condition here; arbitrary positive quantitative lower bounds are not inferred.

## 4. Uniform entropy continuity, including zero coefficients

Let P,Q be the squared Fourier laws of f,g, and let delta=TV(P,Q). Set alpha=fhat, beta=ghat, viewed as unit real vectors. Parseval and the one-point difference give

    ||alpha-beta||_2=2 sqrt(p),
    ||alpha+beta||_2=2 sqrt(1-p).

Cauchy-Schwarz gives

    delta=(1/2)sum |alpha_S-beta_S||alpha_S+beta_S|
          <=2 sqrt(p(1-p))<=2 sqrt(p).

No lower bound on old coefficients is needed. For a probability law on N labels, the elementary coupling bound is

    |H(P)-H(Q)|<=h2(delta)+delta log2(N-1).

To prove it, maximally couple X,Y with P[X!=Y]=delta by matching the common mass min(P_s,Q_s). Given Y, the mismatch indicator costs at most h2(delta), and on a mismatch X has at most N-1 possibilities. Thus H(X|Y)<=h2(delta)+delta log2(N-1); reverse X,Y and use H(X)-H(Y)=H(X|Y)-H(Y|X). This proves the bound without invoking a literature theorem.

For n>=4 put u_n=2^(1-floor(n/2)), so delta<=u_n<=1/2. Since h2 is increasing on [0,1/2],

    |H(g)-H(f)|<=E_n:=h2(u_n)+n u_n.

This is a dimension-explicit uniform remainder, E_n=O(n*2^(-n/2)). For example - (1-u)log2(1-u)<=u/ln2, so E_n<=u_n[log2(1/u_n)+log2(e)+n]. Entropy changes need not be O(p); this continuity estimate deliberately retains an exponentially small but larger uniform envelope. It does not replace A022's sharper support-dependent selector logarithm classification.

## 5. Arbitrary hard core admission with all costs

Fix any nonconstant Boolean sign h on d>=1 coordinates. For t>=1 form

    F_t(x^(1),...,x^(t),z)=(-1)^z product_(r=1)^t h(x^(r)),
    n_t=td+1, p_t=2^(-n_t),
    G_t=F_t-2F_t(a)1_a,

at any chosen vertex a. Tensor Fourier multiplication gives, exactly,

    H(F_t)=tH(h), I(F_t)=tI(h)+1.

By sections 1--4,

    |H(G_t)-tH(h)|<=E_(n_t),
    |I(G_t)-(tI(h)+1)|<=2n_t p_t.

All factor-count and point-defect parameters appear explicitly. For n_t>=4 and J_t=tI(h)+1,

    |H(G_t)/I(G_t)-tH(h)/J_t|
    <=[E_(n_t)+(tH(h)/J_t)*2n_t p_t]/[J_t-2n_t p_t].

The denominator is positive. Since I(h)>0 and both errors vanish exponentially, H(G_t)/I(G_t) tends to H(h)/I(h). Every G_t is tensor-prime, has full Fourier support, has all coordinates essential, and has a connected multiplicative-curvature graph. The fresh z is connected to each other coordinate by c_iz(G_t)=4p_t. Across the old split {z},rest,

    sum_(i != z) c_iz(G_t)=4(n_t-1)p_t ->0,
    sum_(i != z) |M_iz(G_t)|<=(n_t-1)(7p_t+4p_t^2)->0.

At least one formerly exact cut is therefore quantitatively arbitrarily close to tensor structure despite qualitative primitivity. G_t is also at physical Hamming distance p_t from the explicit product F_t. Its Fourier law is at TV distance <=2sqrt(p_t) from the product Fourier law. Any fixed positive bound on Hamming distance from all products, all cut-plaquette sums, or analogous cut-covariance cannot be inferred from primitivity alone.

It follows that the supremum of H/I over the simultaneous class of tensor-prime, full-support, all-essential Boolean signs with connected multiplicative-curvature graph equals the unrestricted supremum, including the possibility of +infinity. Inclusion gives one direction. For each arbitrary fixed h, the sequence G_t gives the reverse direction by the preceding limit. This is an admission equivalence, not an FEI counterfamily: the core ratio remains unknown in general.

## 6. Where dimension-criticality actually fails

These embeddings preserve a fixed violated threshold C after sufficiently large t if H(h)>C I(h). They do not preserve minimal dimension at that threshold. To see an explicit smaller physical descendant for t>=2, fix z and every copy except copy 1 to constants, choosing fixed values in copy 2 unequal to its surgery coordinates. The surgery point is thereby excluded. The surviving sign is +h or -h on copy 1, so it retains the original violating ratio. A dimension-critical witness in A051's sense cannot contain this smaller violating physical descendant. The failure occurs at that specified restriction, not at an unproved assumption about criticality inheritance. For arbitrary h with a strict violation, t can be taken >=2 and large enough to admit G_t.

Thus stronger all-descendant deficit tests remain a meaningful possible route. Neither tensor primitivity, positive mixed derivatives, nor graph connectedness substitutes for those tests. The first unsupported universal line is that every dimension-critical violating witness has a dimension-independent quantitative separation from near-products sufficient to pay a proper-block entropy erasure or the remaining conditional witness cost. This packet establishes no such separation.

## 7. Validation and review scope

code/check_near_tensor.py uses independent physical-edge and physical-second-derivative counts, integer Walsh transforms, rational plaquette probabilities, and cutwise rank-one minors. The v2 frozen spec exploits only bijective input translations on fully enumerated seed families. Exact rational logarithm bounds use ln(y)=2 sum_(k>=0) z^(2k+1)/(2k+1), z=(y-1)/(y+1), with omitted tail bounded by 2z^(2m+1)/[(2m+1)(1-z^2)] after range reduction to 1<=y<2. ln2 is bounded likewise and all divisions are between nonnegative intervals. Selected entropy continuity checks compare rigorous upper differences with a rigorous lower bound on E_n. The finite tests validate identities; the preceding derivations prove all dimensions. A090/A094 should independently reconstruct the factorization criterion, covariance signs, continuity coupling, ratio limit, and the failed-criticality restriction.
