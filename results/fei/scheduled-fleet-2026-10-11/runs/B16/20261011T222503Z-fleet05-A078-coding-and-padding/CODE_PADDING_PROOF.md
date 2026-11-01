# Actual Boolean parity codes and auxiliary payment

All physical inputs are independent fair binary bits, characters are (-1)^{s.x}, outputs are signs, and entropy is in bits. None of the following asserts that an arbitrary spectral probability law is Boolean. Every seed and every substituted gate is an actual Boolean truth table.

## 1. Every full-rank linear code and every output parity

Let f:F2^m->{-1,1}; let A:F2^N->F2^m be surjective, with columns v_1,...,v_N; let b in F2^m and t in F2^N. Construct

    F(x)=(-1)^{t.x} f(Ax+b).

This is Boolean on N bits. A uniform x gives a uniform Ax+b. Expanding f yields coefficient (-1)^{s.b} fhat(s) at the unique label A^T s+t. A^T is injective. Therefore H(F)=H(f). Its mean is zero if t is not in im(A^T); if t=A^T s0 it is (-1)^{s0.b} fhat(s0). In particular t=0 preserves the original mean.

Define q_f(v)=P_z[f(z)!=f(z+v)]. Parseval gives q_f(v)=sum_s fhat(s)^2 1{s.v=1} = (1-E f(z)f(z+v))/2. Flipping physical bit j changes the seed input by v_j and also changes output sign precisely when t_j=1. Hence

    Inf_j(F)=q_f(v_j) if t_j=0, and 1-q_f(v_j) if t_j=1.
    I(F)=sum_j Inf_j(F).

All added physical influence is included. A zero column costs zero without modulation and one with modulation. Input translation b only changes coefficient signs; it changes none of these costs.

For fixed A choose t_j independently to minimize each term. Write d_f(v)=min(q_f(v),1-q_f(v))=(1-|E f(z)f(z+v)|)/2. Define

    M(f)=min_{B a vector-space basis of F2^m} sum_{v in B} d_f(v).

Every spanning multiset of columns contains a basis, and all d_f are nonnegative. Thus I(F)>=M(f) for all N,A,b,t. Equality is attained already at N=m: choose a minimizing basis as columns and choose each output parity bit optimally. Consequently arbitrary redundant parity padding never lowers influence beyond an actual invertible parity change with output modulation. It can lower influence relative to a badly chosen coordinate representation; no universal assertion I(F)>=I(f) is made for nonsystematic codes.

This is a constructive minimum, obtainable by sorting nonzero directions by exact d_f(v) and retaining a direction whenever it increases binary rank. For completeness, at each weight threshold u the retained directions span every direction of weight <=u (a rejected direction was already in the span). Their number is therefore the rank R_f(u) of that sublevel span. Every basis contains at most R_f(u) vectors of cost <=u, so every basis costs at least integral_0^{1/2}(m-R_f(u))du. The greedy basis has equality at every threshold and attains that lower bound. Endpoint ties have zero integration measure; zero-cost directions are allowed.

## 2. Tensor products cannot amplify this optimum

For independent physical blocks and h(z,w)=f(z)g(w), the directional autocorrelation factors exactly:

    rho_h(v,w)=rho_f(v)rho_g(w).
    d_h(v,w)=(1-|rho_f(v)rho_g(w)|)/2 >= max(d_f(v),d_g(w)).

Fix threshold u in [0,1/2]. Every vector in the h sublevel has both components in the corresponding f,g sublevels; conversely (v,0) and (0,w) belong whenever v,w do. Hence its span is exactly the direct sum of those sublevel spans and R_h(u)=R_f(u)+R_g(u). The preceding exact rank integral proves

    M(f tensor g)=M(f)+M(g).

Also H(f tensor g)=H(f)+H(g), since its actual squared Fourier law is the product law. For any full-rank parity code with modulation applied after any disjoint product, its influence is at least sum_j M(f_j) and its entropy is sum_j H(f_j). If H(f_j)<=C_j M(f_j), the result satisfies H<=max_j C_j I. In particular tensoring and mixing blocks by parity codes cannot amplify beyond the largest optimized seed ratio. If M(f)=0, the attaining Boolean transform has zero physical influence and is constant; thus H(f)=0. Such factors create no entropy and are omitted from ratio divisions.

No universal upper bound for H(f)/M(f) is proved. In fact it has exactly the optimal full-FEI constant as an extended-real supremum: for each f the minimizing transform is actual Boolean with equal H and influence M, so FEI implies H<=C M. Conversely M<=I(f), so a universal H<=C M implies FEI. This precise unpaid line cannot be replaced by a formal low-degree spectral law.

## 3. Actual physical peeling and the C019 interface

For a constructed F choose m linearly independent physical columns J. Query every column outside J, in any order, stopping with J unqueried. At every partial history the remaining map still has rank m. Each history only changes b and a global output sign. Coefficient magnitudes and all remaining physical influences stay the same. Both children of each auxiliary query are therefore isospectral, their entropy drop is exactly zero, and so are the erasure and channel terms separately. Leaves are actual m-bit invertible parity transforms with the original entropy. Precisely,

    H(F_leaf)=H(f),
    I(F)=I(F_leaf)+sum_{j outside J} Inf_j(F).

The weighted query influence equals that last sum because every level's history probabilities sum to one and its queried influence is unchanged. This is a conserved physical budget, not spectral conditioning. This verifies and sharpens the already known signed-symmetry peeling interface: linear padding leaves all universal difficulty at an actual Boolean core. Terminal influence is always at least M(f).

## 4. Systematic coding and explicit high-distance examples

For a binary r by m matrix B use

    F(x,z)=f(x+B^T z).

Its spectral support is (s,Bs), H(F)=H(f), mean is unchanged, and

    I(F)=I(f)+sum_{j=1}^r q_f(B_j) <= I(f)+r Var(f).

This systematic baseline is already in reductions/paper/main.tex, lem:coding, independently reconstructed by A002. It is not new here. If every nonzero systematic codeword has Hamming weight at least D, then I(F)>=D Var(f). Adding distance cannot discard its degree payment.

Take the full simplex construction, with one physical column for each nonzero v in F2^m, N=2^m-1. For nonzero s exactly 2^{m-1} columns satisfy s.v=1. Thus, for every Boolean f, without modulation,

    I(F)=2^{m-1} Var(f), H(F)=H(f), EF=Ef.

Distinct occupied labels are separated by 2^{m-1}. This realizes enormous spectral distance with an explicit influence bill. For bent seeds H=m and Var=1, so H/I=m/2^{m-1}. For a point defect f_m=1-2*1{z=0}, m>=2, let p=2^{-m}. Its nonzero directional autocorrelation is 1-4p; all nonzero q=d=2p. Hence M(f_m)=2mp=I(f_m). Every unmodulated full-rank code costs 2p times its number of nonzero columns; folded modulation cannot improve this. The simplex costs 2(1-p), while preserving H(f_m) tending to zero.

For disjoint point-defect tensors with each m_j>=2, M=sum_j 2m_j2^{-m_j}. Their H<=4M by the point-defect entropy bound in the independently accepted A077 ledger. Thus every full-rank parity code, every output modulation, every number of auxiliary bits and every tensor count in this family satisfy H<=4I. This closes this entire counterfamily mechanism, not all Boolean seeds.

## 5. Nonlinear auxiliary substitution with the full entropy bill

Let an actual Boolean outer F_0 have coordinate influences c_j. Replace any chosen coordinate j by an independent balanced Boolean gadget g_j on disjoint new blocks, leaving other coordinates alone. Its nonzero gadget spectrum contains no empty atom. The outer support is recoverable from the occupied blocks, so expansion has no collisions. This gives exact identities

    H(F)=H(F_0)+sum_{j replaced} c_j H(g_j),
    I(F)=I(F_0)+sum_{j replaced} c_j (I(g_j)-1),
    EF=EF_0.

These are the already known balanced-composition identities, derived here to avoid assuming an unreviewed result. In particular ordinary gadget H/I is insufficient to assert a preserved strong constant: a sufficient condition is H(g_j)<=C(I(g_j)-1), in addition to H(F_0)<=C I(F_0). Every balanced Boolean gadget has I>=1 by spectral nonemptiness. Tensor padding by an independent Boolean factor instead simply adds H and I and obeys the ratio-weighted-average law.

Concrete actual padding: systematically add r nonzero parity auxiliaries to a point defect on m>=2 bits, then replace each auxiliary by a majority-three gate on fresh blocks. Majority-three has four spectral masses 1/4, entropy two, and influence 3/2. Host influence is c_j=2p for every nonzero auxiliary mask, including repeated masks. Dimension is m+3r and

    H(F)=H(f_m)+4rp,
    I(F)=2mp+3rp,
    EF=1-2p.

Since H(f_m)<=8mp, the family satisfies H(F)<=4I(F) for every m,r and every choice of nonzero masks. For fixed m as r grows, H/I tends to 4/3. A zero auxiliary mask would have c_j=0 and create irrelevant gadget bits; it is excluded in this displayed cost count. This gives an actual Boolean nonlinear padding family, with its entire auxiliary entropy counted, rather than a distributional completion.

The next unsupported universal line is a payment for newly created conditional entropy under auxiliary constructions outside the injective affine code or balanced disjoint-gadget laws. Every claim of such a payment must retain the actual truth table, all physical influence, and the complete conditional spectrum.
