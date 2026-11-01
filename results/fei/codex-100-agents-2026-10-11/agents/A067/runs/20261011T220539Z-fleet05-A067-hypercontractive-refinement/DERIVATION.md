# Boolean local granularity, its regime, and its obstruction

All inputs are finite uniform cubes, outputs are signs, and entropy is in bits. Write a_S=hat f(S), q_S=a_S^2, v=1-q_empty, I=sum |S|q_S. For each nonzero nonempty coefficient define

    d_f(S)=max{|T|: T contains S and a_T != 0},
    U(f)=sum_{S != empty} q_S [d_f(S)-|S|].

Zeros are omitted; U(constants)=0. This is a spectral-support parameter, with no logarithm or entropy in its definition. Let c=2-log_2(e)>0.

## 1. The Boolean arithmetic lemma

An integer-valued function h on a cube of real Fourier degree at most m has every Fourier coefficient in 2^{-m} Z. Indeed, put x_i=1-2y_i. The unique multilinear polynomial in the y_i has integer coefficients: its coefficients are finite differences of the integer vertex values. The substitution preserves degree. Each monomial of degree j<=m contributes Fourier coefficients that are multiples of 2^{-j}; their sum is a multiple of 2^{-m}. This proves the assertion in every dimension, including m=0.

For nonempty S of size s, let

    D_S f(x_{S^c})=2^{-s} sum_{z in {-1,1}^S} chi_S(z) f(z,x_{S^c}).

Its values are multiples of 2^{1-s}: a sum of 2^s signs with sign multipliers is even. Its Fourier expansion is sum_{T superset S} a_T chi_{T\S}, of degree exactly d_f(S)-s. Apply the integer lemma to 2^{s-1}D_S f. Its empty coefficient is 2^{s-1}a_S. Consequently

    a_S in 2^{1-d_f(S)} Z,
    a_S != 0 => log_2(1/q_S) <= 2[d_f(S)-1].             (1)

This uses Boolean vertex quantization at precisely the even-sum step. It is not a bound for arbitrary normalized real Fourier vectors.

## 2. Entropy estimate and measurable regime

Summing (1) over nonempty S gives

    sum_{S != empty} q_S log_2(1/q_S) <= 2I-2v+2U.

For x=q_empty, -x ln x <= 1-x=v; the assertion includes x=0 by continuity. Thus

    H(f) <= 2I(f)+2U(f)-c v.                            (2)

In particular U(f)<=K I(f) implies H(f)<=(2+2K)I(f), for every fixed finite K>=0, in all dimensions. When f is balanced, the sharper bound is H(f)<=2I+2U-2. A nonconstant function with nonzero Fourier supports forming an inclusion antichain has no empty coefficient and U=0, so H<=2I-2. This antichain corollary is not claimed as a new FEI class in the literature. The mathematical delta is the coefficient-local d_f(S) estimate and its exact unpaid U term; novelty is unverified.

One simple sufficient condition is d_f(S)<=L|S| for every nonzero nonempty S, with fixed L>=1. Then U<=(L-1)I and H<=2LI-cv. This criterion permits different degrees and amplitudes and is a support test, rather than an entropy hypothesis. The global bounded-degree granularity bound is an older elementary special case and is not claimed as new.

## 3. Why the dimension logarithm disappears, and what remains

For W_k=sum_{|S|=k}q_S and its normalized conditional law P_k, the exact entropy decomposition is H(q)=H(W)+sum_k W_k H(P_k). The general support-count step is

    H(P_k)<=log_2 binom(n,k)<=k log_2(en/k).             (3)

This is where a dimension logarithm enters a level-wise entropy argument. Hypercontractivity estimates the W_k or noise-weighted masses; it does not replace (3) by an upper bound on within-level entropy. For instance T_rho D_i f obeys ||T_rho D_i f||_2^2<=I_i^{2/(1+rho^2)}, because D_i f is ternary. The resulting low-level mass estimate has the rarity scale log(1/I_i). It gives no individual lower bound on a nonzero coefficient. Estimate (1) is such a lower bound and bypasses (3), while keeping U explicitly unpaid.

The recovered threshold paper, Section 5.1, Lemma 5.3 and Eq. (29), applies hypercontractivity to a ternary pivotal fiber d_z. Its displayed noise-square norm bound is at most support_density^{8/5}. After normalizing and comparing the noise weight on the event of low cardinality, it obtains a rare-gate low-cardinality probability bound. That norm inequality is a general real-valued hypercontractive estimate specialized to a ternary alphabet. The later gate-rank and piece-count payments must not be called a sharpened hypercontractivity constant. We improve the entropy conversion on a stated Boolean regime, not the Bonami--Beckner theorem for general functions.

For a second exact primary locator, Han's arXiv:2312.08271v2 (10 December 2025), Section 3, Eqs. (3.13)-(3.15), replaces packet moments by an influence-only extremum; differentiating at zero in Eq. (3.4) leaves a rarity logarithm. Remark 3.2, Eqs. (3.16)-(3.17), identifies the unpaid packet logarithmic ratio. This is background scope, not a new bound in this stage; no priority claim is made.

## 4. Explicit strict gain: one-point defects

Let p=2^{-n}, n>=2, and f_n=1-2 indicator{x=all +}. Then a_empty=1-2p, a_S=-2p for every nonempty S, and d_f(S)=n. Exact quantities are

    v=4p(1-p), I=2np,
    U=n v-I=2np-4np^2 <= I,
    H=(1-2p)^2 log_2(1/(1-2p)^2)+8p(1-p)(n-1).

Equation (2) therefore yields H<=4I-cv. In contrast, the generic marginal bound sum_i h_2(I_i)=n h_2(2p) has ratio to I equal to n-1+log_2(e)+O(p), tending to infinity. The generic level-count bound is tight on this family: its conditional law within each nonzero level is uniform, so it already gives a constant ratio. The new bound has constant ratio and H/I tends to 4. This family and its FEI limit are baseline controls, not new counterfamilies.

For a strict gain over the level-count step itself, use the existing addressing baseline on a address variables and 2^a data variables. Its nonzero Fourier supports are {data_j} union T, for every address j and every subset T of the address variables; each coefficient has magnitude 2^{-a}. Thus d_f(S)=a+1 for every nonzero support, v=1, I=1+a/2, U=a/2, and our balanced bound gives exactly H<=2a, the known exact entropy. No addressing baseline theorem is claimed as new. The old full-cube level-count bound uses n=a+2^a and W_{t+1}=binom(a,t)/2^a. Its sum W_k log2 binom(n,k) is Theta(a^2): for a>=8, Chebyshev gives probability at least 1/2 that t>=a/4; using binom(n,k)>=(n/k)^k then gives the lower bound (a/8)[a-log2(a+1)], and the standard binomial upper bound gives O(a^2). Dividing by I loses a factor Theta(a). This comparison retains all relevant data variables and is not dummy-variable padding.

For any fixed alpha in (0,1), the exact Renyi moment is (1-2p)^{2alpha}+4^alpha(1-p)p^{2alpha-1}. Its entropy/influence ratio diverges, as derived in SEED_LEMMAS Section 3. Equation (2) makes no fixed-order Renyi assertion.

## 5. Non-Boolean and near-Boolean guards

For real degree-one g_n=n^{-1/2}sum_i x_i, the normalized Fourier law is uniform on n singletons, I=1, and H=log_2 n. Its support is an antichain, so U=0. Thus (1)-(2) would be false without the Boolean quantization hypothesis.

Even L2-nearness alone does not repair this. For 0<epsilon<1, the normalized real function

    g_{n,epsilon}=sqrt(1-epsilon)+sqrt(epsilon/n)sum_i x_i

has I=epsilon and H=h_2(epsilon)+epsilon log_2 n. Its L2 distance squared to the constant sign 1 is 2-2sqrt(1-epsilon), tending to zero with epsilon, yet H/I can be arbitrarily large at fixed epsilon as n grows. Its nonempty supports have U=0. It is not bounded in magnitude by one, so this only refutes an L2-only relaxation; no bounded near-Boolean stability statement is claimed or refuted.

## 6. Universal payment of U fails on an actual Boolean family

Let g_n=x_1-2 indicator{x=all +}, n>=2. This flips just one value of a dictator. Its coefficients are a_{1}=1-2p and a_S=-2p at every other S, including empty; all coefficients are nonzero. Thus

    I(g_n)=1+(2n-4)p,
    v(g_n)=1-4p^2,
    U(g_n)=n-1-(2n-4)p-4np^2.

Hence U/I tends to infinity. Its entropy is exactly that of f_n because g_n=x_1 f_n, so H/I tends to zero. This disproves U<=K I universally, not FEI. Sparse nonzero top-degree tails can make d_f(S) large at a heavy low-degree coefficient.

## 7. A single optimized character anchor still cannot pay the cost

For any A subset [n], define h=f chi_A, J_A=I(h), v_A=1-q_A, U_A=U(h), and

    E_A=(log_2 e)v_A+2sum_{R != empty} hat h(R)^2[d_h(R)-1]
       =2J_A+2U_A-cv_A.

Entropy is invariant under character multiplication, so H(f)<=E_A for every A. On the dictator surgery A={1} cures the preceding U obstruction. However min_A E_A<=K I(f) is also false universally.

Take F_n(z,y)=Maj_3(z) f_n(y), with disjoint variables and n>=2. Maj_3=(z_1+z_2+z_3-z_1z_2z_3)/2 has four nonzero Fourier coefficients of squared mass 1/4. Its entropy is 2 and influence is 3/2. The point defect f_n has full Fourier support, so

    I(F_n)=3/2+2n2^{-n}<=5/2,
    H(F_n)=2+H(f_n),

which is bounded. Fix any anchor A=(A_z,A_y), including anchors with zero coefficient. The shifted majority support has four distinct sets, at most one of which is empty. At least 3/4 of the full spectral mass therefore has nonempty z-support R_z. For each such coefficient R=(R_z,R_y), the support contains (R_z,all y) because the shifted point-defect factor has full support. Hence d_{F_n chi_A}(R)>=|R_z|+n>=n+1. The coefficient is nonempty, and its contribution to the sum in E_A is at least 2n times its mass. Consequently

    E_A>=3n/2 for every A,
    min_A E_A/I(F_n)>=3n/5 -> infinity.                 (4)

This rules out both a fixed and an optimized single-anchor maximal-support-degree envelope. It does not rule out a complete paid partition or a tail-stable arithmetic bound. It also checks the arbitrary-tensor-factor obstruction explicitly.

## 8. Stopping-tree interface and exact gap

At each leaf h of an actual fair physical restriction tree, (2) yields H(h)<=2I(h)+2U(h)-c Var(h). If the visited-node entropy decrement is <=a times its queried influence in expectation, and E_leaf U<=b E_leaf I, the usual exact influence telescope gives

    H(root)<=max(a,2+2b) I(root).

Both node payment and leaf-U payment are hypotheses, not results of this note. U is not asserted to be hereditary under restriction. For balanced disjoint factors U is additive (d on product support is additive); for biased factors empty-support cross terms prevent that claim. The shortest next mathematical action is a tail-stable replacement of d_f(S) for a heavy coefficient, or a completely paid finite partition into sources with controlled U. Merely searching for a universal bound on U or min_A E_A is ruled out by Sections 6-7.

The first unsupported universal line is: every Boolean source admits a tail-stable arithmetic/partition charge bounded by O(I), including the cost of selecting its pieces and the terminal entropy. No universal FEI proof or disproof is supplied.
