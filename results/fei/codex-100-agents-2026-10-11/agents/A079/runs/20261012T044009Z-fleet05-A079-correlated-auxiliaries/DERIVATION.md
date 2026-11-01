# Exact correlated bent-branch transport with logarithmic overhead

Physical cubes are disjoint and uniformly distributed; bit values are in F_2, signs in {-1,1}. Entropy is in bits, transforms are normalized, and influence is the expected spectral Hamming weight. All statements below have direct proofs. Full FEI remains open. No novelty assertion is made.

## 1. The flat bent-branch mechanism has a smaller Boolean phase core

Let F(x,y)=g_x(y), with k selector bits and d>0 even data bits, and every g_x bent. Write

    ghat_x(t)=2^(-d/2) sigma_t(x),   sigma_t(x) in {-1,1}.

Partial Walsh expansion gives

    P(S_X=v,S_Y=t)=2^(-d) sigmahat_t(v)^2,
    H(F)=d+E_t H(sigma_t),
    I_Y=d/2,   I_X=E_t I(sigma_t),
    B_X=H(S_X|S_Y)=E_t H(sigma_t),
    H(S_Y|S_X)=d-I(S_X;S_Y)<=2I_Y.

For a constant phase row, H=I=0. Thus H(F)/I(F) is a weighted average of 2 and the nonconstant row ratios H(sigma_t)/I(sigma_t), weighted by their influence contributions. In particular

    H(F)/I(F) <= max(2, max_(nonconstant t) H(sigma_t)/I(sigma_t)).       (1)

If C>=2 and F violates FEI(C), then E_t[H(sigma_t)-C I(sigma_t)]>(C/2-1)d>=0; one actual Boolean sigma_t violates FEI(C) on the strictly smaller k-bit cube. No independent-padding hypothesis or spectral independence is used. This is a dimension-reducing obstruction to extracting a new high-ratio mechanism solely from flat bent data magnitudes.

There is no loophole in the phase realization cost: (1/4) sum_(i in X) E_x sum_t(ghat_x(t)-ghat_(x+e_i)(t))^2 equals I_X by Parseval. The corresponding magnitude energy is zero. Both orientations of conditional entropy remain in the ledger.

## 2. An explicit basis-character tag code

Let g be ANY Boolean sign on k>=1 bits, choose m=ceil(log2(k+1)), and N=2^m. Assign one distinct B-value to every unit vector e_i, i=0,...,k-1, and assign the zero vector to the remaining N-k B-values. Concretely c_b=e_b for 0<=b<k and c_b=0 otherwise. Define

    h_b(x)=g(x)(-1)^(c_b dot x),
    F_g(x,a,b)=(-1)^(a dot b) h_b(x),   a,b in F_2^m.

This is an actual Boolean function. Directly summing first over a gives the signed coefficient formula

    Fhat_g(v,s,t)=2^(-m)(-1)^(s dot t) ghat(v+c_s).                     (2)

All physical x-branches are bent. They are pairwise distinct even modulo a global sign: at a B-value with c_b=0 their relative sign is fixed, and the B-values with c_b=e_i recover every bit x_i. Their squared spectra all coincide, but their signs implement the tag code.

For p_g(v)=ghat(v)^2, the exact marginal is

    q(v):=P(S_X=v)=(1-k/N)p_g(v)+(1/N) sum_i p_g(v+e_i).              (3)

Every phase row is a character times g. Character multiplication translates the spectral vector, preserving entropy and every coordinate erasure entropy. Hence

    H(F_g)=2m+H(g),     B_X=H(g),
    I_Y=m,             I_X=I(g)+(k-2I(g))/N,                          (4)
    H(S_Y|S_X)=2m+H(g)-H(q)=2m-I(S_X;S_Y).                           (5)

Equation (4) also follows directly from physical selector edges. At the B-tag for coordinate i, multiplication by x_i complements the seed's disagreement in that direction; all other B-values keep it. Thus Inf_i(F_g)=(1-2/N)Inf_i(g)+1/N. The added signed phase energy differs from I(g) by less than one because k/N<1. The data energy is m; it cannot be omitted.

Spectral dependence is present exactly when p_g is not uniform: S_X conditional on B-frequency s has law p_g translated by c_s. The zero tag is present, and invariance under all unit translations is equivalent to uniformity on the entire k-cube. A bent selector seed is therefore an intentional independence control; distinct branches alone need not imply spectral dependence.

## 3. Guaranteed dependence and preservation of the full seed ratio

Fix any nonconstant Boolean f on n bits. For each t>=1 take disjoint copies and the balanced seed

    g_t(x,z)=z product_(j=1)^t f(x^(j)),
    k_t=tn+1,   m_t=ceil(log2(k_t+1)),   N_t=2^m_t.

Here z denotes a sign bit, so in binary notation it is (-1)^z. Its squared spectrum has the z-coordinate constantly one. Entropy and influence tensorize exactly:

    H(g_t)=tH(f),     I(g_t)=tI(f)+1.

Apply the code in section 2. Every physical selector branch is bent and pairwise distinct, and the spectral marginals are genuinely dependent. Indeed the z spectral coordinate becomes zero if and only if s equals the tag assigned to z. Therefore

    I(S_X;S_Y) >= H(S_{X,z})=h2(1/N_t)>0.                            (6)

The conditional row entropy is still exactly tH(f). For the actual complete Boolean function F_t,

    H(F_t)=tH(f)+2m_t,
    I(F_t)=tI(f)+J_t,
    J_t=m_t+1+[k_t-2(tI(f)+1)]/N_t,
    m_t<J_t<m_t+2.                                                  (7)

The last inequalities use 0<=I(g_t)<=k_t and k_t/N_t<1. For rho=H(f)/I(f),

    |H(F_t)/I(F_t)-rho|
       <= [2m_t+rho(m_t+2)]/[t I(f)] -> 0.                          (8)

No floating-point extrapolation is used: m_t=O(log t) for fixed n and I(f)>0. There are only 2m_t auxiliary physical data bits. The first stage's point-specific tags required m>=k+1 and paid linear-in-k data influence, which buried the seed in the full H/I. The new character tags use logarithmic data influence while retaining branch distinctness and strict spectral dependence. This changes the FULL ratio statement, not merely a conditional ratio.

The optimal FEI constant on actual Boolean address selectors with pairwise distinct bent branches and dependent spectral marginals equals the universal optimal constant, allowing infinity. One direction is inclusion in all Boolean functions. The reverse direction follows from (8) for each arbitrary nonconstant seed. Thus a claimed finite universal constant for this apparently restricted class would solve full FEI. This is a scope reduction, not a proof of the finite constant.

## 4. This code preserves difficulty; it does not amplify a seed ratio

For every g in section 2,

    H(F_g)/I(F_g) <= max(2,H(g)/I(g))                                (9)

when I(g)>0, and the ratio is less than two for a constant seed. To prove (9), if I(g)<=k/2 the correction in (4) is nonnegative, and the numerator 2m+H(g) is bounded by max(2,H(g)/I(g))(m+I(g)). If I(g)>=k/2, use H(g)<=k:

    2I(F_g)-H(F_g)
       >= (2I(g)-k)(1-2/N) >= 0.

The broader obstruction is (1): any divergent actual FEI ratio in a bent-branch family already requires divergent Boolean phase-row ratios. An unbounded conditional entropy divided by a selected phase energy is insufficient. Our result gives explicit low-cost realizability of all seed ratios, not an unbounded-ratio Boolean family from bounded-ratio seeds.

## 5. Exact C018 root erasure and C019 paired stopping transport

The following holds for arbitrary h_b, not only character tags. Let

    F(x,a,b)=(-1)^(a dot b)h_b(x),
    P(V=v,S=s,T=t)=2^(-2m)hhat_s(v)^2.

T is independent and uniform. V conditional on S=s has the squared spectrum of h_s. For aggregate erasure B(f)=sum_i H(S_i|S_-i),

    B(F)=m+E_s B(h_s)+A,
    A=sum_j H(S_j|V,S_-j),       0<=A<=m.                           (10)

Every X coordinate transports exactly: B_i(F)=E_s B_i(h_s), Inf_i(F)=E_s Inf_i(h_s). Every b-coordinate has B_b=1 and Inf_b=1/2, because its spectral T-bit is independent and fair. For basis tags, E_s B(h_s)=B(g) exactly.

Consequently for K>=2,

    KI(F)-B(F)
       =E_s[KI(h_s)-B(h_s)]+(K-1)m-A
       >=E_s[KI(h_s)-B(h_s)]+(K-2)m.                             (11)

This is a conditional C018 transfer if the actual phase cores have paid erasure. It does not bound their erasure using an unpaid premise.

There is a physical paired stopping tree: query b_j first, then a_j, for each matched pair. Before a b query, the unmatched data remain in the same displayed form. Restricting b_j to beta introduces only the character (-1)^(beta a_j) and restricts the family of h rows. Hence at every first query,

    B_b=1,    JS_b=1,    Delta_b H=2,    Inf_b=1/2.

At the subsequent a query, B_a=JS_a=Delta_a H=0; its influence is beta, averaging to 1/2. Each complete pair therefore removes exactly two bits of entropy and one unit of influence. Leaves are precisely h_b (with repetitions and irrelevant/global signs), with the fair uniform B-assignment. The full, terminal-inclusive ledger is

    sum_internal w B=m,     sum_internal w JS=m,
    I_removed=m,
    H(F)=2m+E_b H(h_b),      I(F)=m+E_b I(h_b).                    (12)

Every queried influence is used once. The terminal phase-core entropy is retained. The construction gives no route to discard it as an auxiliary normalization credit. The matched-pair structure remains valid after any X restriction, because the restricted h_b are still actual Boolean signs. If a data a-coordinate is restricted first, a different core appears, and the next identity specifies it exactly.

## 6. A-first collisions exchange the two conditional charges

Fix one pair j and the other B-values s. Let G_s(x,z)=h_(s,z)(x), an actual Boolean one-bit selector of two phase cores. Write B_z(G_s), JS_z(G_s), and L_z(G_s)=B_z+JS_z for its ordinary physical split quantities. Averaging uniformly over s,

    B_(a_j)(F)=1-E_s JS_z(G_s),
    JS_(a_j)(F)=1-E_s B_z(G_s),
    Delta_(a_j)H(F)=2-E_s L_z(G_s).                            (13)

For a derivation, the parent conditional law of the B-index z given the core Fourier label v has entropy 1-JS_z(G_s): the physical index z is fair and its spectral law is the child law. This is B_(a_j)(F). After fixing a_j, the residual core is G_s or its z-character shift. Both have entropy H(G_s). Their mixture has the z spectral bit independent and fair with core marginal q_v=(hhat_0(v)^2+hhat_1(v)^2)/2. Its entropy minus H(G_s) is 1-B_z(G_s), giving the JS formula. The same formulas follow by the signed two-point Walsh transform before squaring.

The subsequent b_j query in either a-child costs E_s L_z(G_s) in entropy; together the pair still costs two bits. But the b query's influences in those two children can be d and 1-d, where d is the physical phase-core disagreement. Equation (13) pays the pair on average and retains the collided core; it does not assert a fixed-price bound on the small-influence child query. Such an assertion would revive the known all-coordinate rare-log obstruction.

## 7. Test of A034's genuinely structural admission

The source-complete version A034-QUADRATIC-AFFINE-ROW-CONDITIONAL v1 requires each partial X Fourier row to be a unit sign on one affine Y partition cell with quadratic phase. It is not a condition just on marginal spectra. For a character-tag root its actual partial row is

    u_v(a,b)=(-1)^(a dot b) ghat(v+c_b).

If g is not a character, some nonzero coefficient has magnitude strictly between zero and one. At any zero-code B-value this is an actual intermediate partial-row magnitude, contradicting unit-row admission. Thus all noncharacter seed embeddings are excluded by the stated algebraic hypothesis; they are not counterexamples to A034's bound.

For the standard code and a character g, the cells have B-fibers of size one at each unit tag, and size N-k for the zero code. The latter is affine if and only if N-k is a power of two (then the final binary interval [k,N) is an affine subcube). The row phases are restrictions of the quadratic a dot b. Therefore in this character corner A034 admission holds exactly when N-k is a power of two. Non-affine zero-code support explains exclusion otherwise.

For the earlier point-specific rare tags, k>=2 always fails unit-row admission: either a noncharacter seed has an intermediate coefficient on untagged B-values or a character seed gets an off-character coefficient of magnitude 2^(1-k) at a tagged value. For k=1, m=2, both supports are two-point B-affine cells and admission holds; for k=1,m>=3 the complementary B-support has size 2^m-2, not a power of two. These checks identify the actual hypothesis excluding the arbitrary seed and cover the small admitted corner.

## 8. Exact first unsupported universal line and mechanism change

No bound is missing inside the paired or basis-tag identities. The unsupported universal inference is to pay every arbitrary phase core at one absolute constant, or to extend the smaller-Boolean-phase descent to nonflat branch amplitudes without a new payment. Full FEI is exactly the former obligation. In a nonflat/plateaued branch family, the normalized selector rows can be zero or have multiple magnitudes, so they cease to be Boolean signs; equation (1) cannot simply apply FEI to them.

The next nonduplicate target is this first nonflat boundary: a single physical a restriction produces the two-row selector cores G_s in (13). Consume A034's exact colliding-row hypothesis when its next report is source-complete, and check whether it pays those normalized cores and their terminal entropies using one physical influence budget. The present flat mechanism is closed as an amplifier and remains an exact hardness-preserving guard for that next step.
