# Correlated character tags: exact deficit transport and admission obstruction

All cubes are uniform and physical coordinates are disjoint. H is Shannon entropy in bits of squared normalized Walsh coefficients; I is their mean Hamming weight. B=sum_i H(S_i|S_-i), D=H-B. No finite universal FEI constant is assumed.

## 1. Arbitrary character-tag map

Let g be any Boolean sign on k bits, m>=1, N=2^m, and let c:F_2^m -> F_2^k be ANY map. Set

    F(x,a,b)=(-1)^(a dot b+c_b dot x)g(x).

Summing first over a, then over x, gives

    Fhat(v,s,t)=N^-1 (-1)^(s dot t) ghat(v+c_s).

Equivalently, its spectral law is obtained by drawing independent W~p_g and uniform S,T in F_2^m and setting V=W+c_S. Conditional on S, the law of V is a translate of p_g; T is independent of (V,S). Thus H(F)=H(g)+2m. All physical x-branches are bent. Branch distinctness is NOT assumed in this identity.

Write d_i=Inf_i(g), theta_i=N^-1 #{s:(c_s)_i=1}. Spectral weight, or direct physical flips, gives

    Inf_xi(F)=d_i+theta_i(1-2d_i),
    Inf_aj(F)=Inf_bj(F)=1/2,
    I(F)=I(g)+m+sum_i theta_i(1-2d_i).

Conditioning on all remaining frequency bits fixes S. Translation preserves each seed erasure. Consequently B_xi(F)=B_i(g), B_bj(F)=1.

For each j, average uniformly over s_-j and set

    J_j = E_s_-j JS(p_g(.+c_(s_-j,0)), p_g(.+c_(s_-j,1))),
    J=sum_j J_j.

Here JS(p,q)=H((p+q)/2)-(H(p)+H(q))/2. The fair S_j conditional on s_-j transmits exactly this mutual information to V, so B_aj(F)=1-J_j. In particular

    0<=J_j<=1,
    B(F)=B(g)+2m-J,
    D(F)=D(g)+J.                                            (1)

This sharpens A079's root identity by identifying its missing auxiliary erasure as an explicitly nonnegative JS deficit. Correlated character tagging cannot reduce the ABSOLUTE seed deficit. Equality J=0 holds exactly when p_g is invariant under every adjacent tag difference c_s+c_(s+e_j); equivalently under their generated F_2 subspace. This follows from JS=0 iff the two probability laws coincide. If the tag image contains 0 and all unit vectors, J=0 iff p_g is uniform. In that case spectral groups are independent; branch distinctness alone is insufficient for dependence.

## 2. Independent reconstruction of A079 v1

For c_s=e_s at s<k and c_s=0 otherwise, m=ceil(log2(k+1)), theta_i=1/N. Hence I(F)=I(g)+m+(k-2I(g))/N. The zero tag fixes a relative branch sign; each unit tag then recovers one x bit, so all x-branches are distinct even modulo sign. Dependence holds unless p_g is uniform.

For any nonconstant seed f on n bits, take g_t=z product of t disjoint copies, k=tn+1. Then H(g_t)=tH(f), B(g_t)=tB(f), I(g_t)=tI(f)+1. Its z spectral bit is constantly one and V_z=0 exactly at its single tag, giving I(V;S,T)>=h2(1/N)>0. With m=ceil(log2(tn+2)),

    H(F_t)=tH(f)+2m,
    B(F_t)=tB(f)+2m-J_t,   0<=J_t<=m,
    D(F_t)=tD(f)+J_t,
    I(F_t)=tI(f)+Q_t,     m<Q_t<m+2.                (2)

For rho=H(f)/I(f) and beta=B(f)/I(f),

    |H(F_t)/I(F_t)-rho| <= [2m+rho(m+2)]/[tI(f)],
    |B(F_t)/I(F_t)-beta| <= [2m+beta(m+2)]/[tI(f)].

Since m=O(log t), both limits preserve the original seed. If H(f)>0, B(F_t)/H(F_t)->B(f)/H(f). This consumes A079's new construction instead of repeating activation or independent bent padding. Strict correlated distinct bent branches admit the optimal universal erasure constant K_E as well as the optimal FEI constant: inclusion proves one supremum inequality, and (2) proves the reverse, in the extended reals. No finite value for either constant follows.

For general bent data branches g_x(y), d even, write ghat_x(t)=2^(-d/2)sigma_t(x) with Boolean sigma_t. Then H=d+E H(sigma_t), I=d/2+E I(sigma_t). A violation at C>=2 descends to a smaller Boolean phase row. For arbitrary F=(-1)^(a dot b)h_b(x), conditioning gives B=m+E B(h_b)+sum_j H(S_j|V,S_-j). In a physical b-first paired tree, querying b_j removes two entropy bits, B_b=JS_b=1, at influence 1/2; then a_j has zero entropy charge and average influence 1/2. Each pair pays two entropy bits for one influence; terminal rows h_b retain their full H/B/I. These reconstruct the remaining clauses of A079-CORRELATED-BENT-HARDNESS-TRANSPORT@1 without repairs. Neither descent nor pairing pays arbitrary terminal rows.

## 3. General correlated-tag no-go above ratio two

Normalize a seed f by multiplying by a character so each d_i<=1/2: its H,B,D stay unchanged, its influence decreases to I_*=sum_i min(d_i,1-d_i). This is an actual Boolean sign, not a change of physical basis. Use this normalized seed below. Assume I_*>0, R=H(f)/I_*>2, eta=D(f)/H(f)>0. The eta>0 condition is explicit; no product rigidity theorem is needed for the argument.

Let g=chi_Z times t disjoint copies of f, with any number of fresh parity coordinates, and use ANY character-tag map, ANY m>=1. On seed coordinates each term theta_i(1-2d_i) is nonnegative. Fresh parity coordinates contribute nonnegative FINAL influence, even if tags cancel them. Therefore

    H(F)=tH(f)+2m,  D(F)>=tD(f),  I(F)>=tI_*+m.              (3)

Put epsilon=D(F)/H(F). If 0<epsilon<=eta, (3) forces

    m >= tH(f)(eta/epsilon-1)/2.

Because (tH+2m)/(tI_*+m) decreases with m for R>2, we obtain the finite tradeoff

    H(F)/I(F)
       <= 2/[1+(2/R-1)epsilon/eta].                         (4)

As epsilon->0, limsup H(F)/I(F)<=2, even if branches are distinct and spectrally dependent. Conversely, if H(F)/I(F)->R>2 then m/t->0, since

    H(F)/I(F) <= 2+(R-2)tI_*/(tI_*+m).

Equation (3) then gives liminf D(F)/H(F)>=eta. Thus no tag map in this entire correlated character family provides the requested high-ratio near-erasure admission. The same tradeoff that blocked independent bent padding survives correlations, because the new deficit is nonnegative and canonical seed influence cannot be removed for free.

For an unnormalized seed, the same physical influence lower bound holds with I_* directly: d_i+theta_i(1-2d_i)>=min(d_i,1-d_i). No actual preliminary normalization is necessary. Thus (3)-(4) hold with R_*=H/I_*, and epsilon->0 still forces limsup ratio<=2. In particular no original seed of ratio H/I>2 and D>0 can preserve that original ratio while approaching near-erasure. The converse statement that preserving R forces m/t->0 refers specifically to R_*, and is not asserted at a smaller unnormalized seed ratio.

## 4. Child certification audit and first unsupported line

A005's new signed slack identity is independently checked algebraically. For delta=H-CI, sigma_i=E_s[CI(f_i,s)-H(f_i,s)], physical influence recursion gives Delta_iH=C Inf_i+delta+sigma_i. Since Delta_iH=B_i+JS_i,

    D+(n-1)delta+sum_i sigma_i=sum_i JS_i.

Under average child certification sigma_i>=0 and delta>0, the proved scalar bound JS_i<=(2/ln2)Inf_i gives n<=1+(2/ln2)/(H/I-C). Thus fixed positive-gap admission into the child-certified endpoint at growing relevant dimension is impossible. Negative slack cannot be used as reserve. This accepts the stated admission obstruction without proposing a new payment.

The first unsupported universal line remains: prove H<=C_epsilon I for one fixed near-erasure fraction, or exclude genuinely minimal C-violators with their SAME-C certified children. Equations (1)-(4) pay no arbitrary core. Their outcome retires correlated character tagging as a third near-erasure inflation mechanism; it preserves hardness with logarithmic overhead but cannot erase the seed deficit. NEXT must attack signed child-certified payment, retaining all child slacks and terminal entropy, rather than add further tag scans or another isolated flat-spectrum class.
