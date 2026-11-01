# One complete dyadic reference and one rounding account

The dyadic scale approximation has a complete normalized reference with an explicit deficit-paid normalizer. Its rounding errors also telescope through genuine disjoint composition. The dyadic scale cost itself remains unpaid universally; full FEI is open.

All entropy and KL quantities below use natural logarithms. Let f be a Boolean sign on a finite cube with independent interior biases p_i. Put v_i=4p_i(1-p_i), v_S=product_{i in S}v_i, c_S=fhat(S)/sqrt(v_S), P(S)=v_S c_S^2 for nonempty S, and w=Var(f)=sum_{S nonempty}P(S). Define

    Delta=sum_{S nonempty}(|S|-1)P(S),
    R=sum_{|S|>=3}(|S|-2)P(S),
    E=sum_{S nonempty}P(S)ln(v_S/P(S)).

Actual physical mixed derivatives give |c_S|<=1. Zero terms are omitted, not assigned a logarithm. For each t_S=|c_S|>0 choose the unique integer j_S>=0 with 1/2<u_S=2^(j_S)t_S<=1. Thus j_S=floor(log_2(1/t_S)), with dyadic boundary points assigned u=1. Set

    J(f)=2ln2 sum_{S nonempty}P(S)j_S,
    L(f)=E-J(f)=2sum_{S nonempty}P(S)ln(1/u_S)>=0.

## 1. The complete reference and its actual normalizer

Define, on every nonempty label,

    W(S)=v_S 4^(-j_S) if c_S!=0, and W(S)=0 otherwise,
    Z=sum_{S nonempty}W(S).

For w>0 the COMPLETE probability law on all Fourier labels is

    Q(empty)=P(empty)=1-w,
    Q(S)=w W(S)/Z for S nonempty.

Every P-positive label is Q-positive. All P-zero labels are explicitly assigned zero reference mass; no positive off-support mass is dropped. This is an auxiliary reference, not a spectrally conditioned Boolean function. No Boolean admission or physical restriction property is asserted for Q.

Let R_f=P/w and Q_+=W/Z on the nonempty labels. Direct substitution, BEFORE any entropy inequality, gives

    E=J(f)+w ln(Z/w)-w KL(R_f||Q_+),                 (1)
    KL(P||Q)=w KL(R_f||Q_+).

Indeed P(S)/W(S)=u_S^2, so P(S)/Q(S)=u_S^2 Z/w at every occupied nonempty label. The empty atom has ratio one. This proves (1), including the ordinary full-law KL term. The corrected reference cross-entropy is exactly J+w ln(Z/w). For ordinary full entropy, the same Q has the exact full cross-entropy

    H_nats(P,Q)=P(empty)ln(1/P(empty))
                  +J+sum_{S nonempty}P(S)ln(1/v_S)+w ln(Z/w).

Zero empty mass contributes zero. This formula retains the empty atom and the physical-bias correction explicitly; it is not an ordinary biased-FEI theorem with those terms omitted.

The normalizer is paid by the ORIGINAL deficit:

    0<=Z-w<=9Delta-6R,
    0<=w ln(Z/w)<=9Delta-6R<=9Delta.                 (2)

Proof: P<=W<4P, with equality W=P at dyadic points. For |S|>=2,

    sum(W-P)<=3sum_{|S|>=2}P=3(Delta-R).

For a singleton i put D_i=(f(1,X_not_i)-f(0,X_not_i))/2, d_i=E D_i^2 and t_i=|E D_i|. Booleanity gives D_i in {-1,0,1}, so d_i>=t_i and V_i=d_i-t_i^2>=t_i(1-t_i).

If 0<t_i<=1/2 write a=2^(-j_i)<=1/2. Since a/2<t_i<=a and a^2<=a/2<t_i, W(i)-P(i)=v_i(a^2-t_i^2)<=v_i(t_i-t_i^2)<=v_i V_i. At dyadic endpoints the excess is zero; the same bound holds. If t_i>1/2 then j_i=0 and

    W(i)-P(i)=v_i(1-t_i^2)
             <=3v_i t_i(1-t_i)<=3v_i V_i.

At t_i=0 or1 the excess is zero. Actual product Parseval gives

    sum_i v_i V_i=sum_{|S|>=2}|S|P(S)=2Delta-R.

Adding the two sectors proves the first bound in (2). Apply ln x<=x-1 at x=Z/w>=1 to prove the second. The singleton reserve is used only once. In particular (1)-(2) imply 0<=KL(P||Q)<=9Delta-6R, since L=E-J>=0. They give the complete-reference payment E<=J+9Delta, but do NOT bound J universally.

If w=0, f is constant and Q is the point mass at empty; E=J=Delta=0. No division by w occurs in that case. If Delta=0, all high-degree mass and every v_i V_i vanish, so Z=w and Q=P. Contract deterministic input coordinates before defining the normalized basis; (1)-(2) apply to the remaining interior coordinates without an endpoint division.

## 2. Independent reconstruction of A042's sharper mantissa bound

This section accepts only the mathematical approximation theorem, not the source's checker counts or a universal payment. Set z=(1-u)/(1+u) in [0,1/3),

    L_N(z)=2sum_{k=0}^{N-1}z^(2k+1)/(2k+1),
    E_N=2sum_{S nonempty}P(S)[j_S ln2+L_N(z_S)],
    A_N=(2N+1)9^N.

The positive atanh tail is bounded by 2z^(2N+1)/[(2N+1)(1-z^2)]. Its contribution to E at each label is therefore at most epsilon_N P(S), where epsilon_N=3/(2A_N). High-degree labels sum to epsilon_N(Delta-R).

At a singleton with t<=1/2, P(i)<=v_i V_i, giving the same bound against v_i V_i. At t>1/2 the dyadic scale is zero and u=t. The error divided by v_i t(1-t) is at most

    (1+t)z^(2N)/(2N+1)<=2/A_N=beta_N.

At t=0,1 the error is zero directly. Since beta_N>=epsilon_N, sum_i v_i V_i=2Delta-R gives

    0<=E-E_N<=(11Delta-7R)/(2A_N).                   (3)

All Fourier sums are finite, the logarithm series has a uniform geometric majorant, and no limit over changing dimensions is used. This independently reconstructs A042's theorem at every N>=0. In particular E_0=J, so

    0<=L(f)<=B(f):=(11Delta-7R)/2<=11Delta/2.       (4)

Equation (4) is sharper than the separate 9Delta normalizer bound. In (1) the difference is precisely retained as ordinary KL credit; it is not a second owner budget.

## 3. Exact dyadic carries under genuine composition

Let F=g(f_1,...,f_m) with mutually disjoint physical input blocks. The original input law is a product, and g is evaluated at the actual independent child-output means. Contract constant children. Write w_i=Var(f_i)>0 and a_i=I_i(g)/w_i>=0.

For a nonempty physical output set S, let A be its set of occupied child blocks and T_i=S intersect block i. The unique disjoint-composition Fourier expansion gives

    c_F(S)=c_g(A) product_{i in A}c_(f_i)(T_i).

This uses corrected coefficients and the actual induced biases; the child variance factors cancel exactly. At P_F(S)>0 every factor is nonzero. Writing ell=-log_2 u in [0,1), the dyadic scales satisfy

    j_F(S)=j_g(A)+sum_{i in A}j_(f_i)(T_i)+kappa(S),
    kappa(S)=floor(ell_g(A)+sum_{i in A}ell_(f_i)(T_i))>=0.

Equivalently kappa is the integer difference of the scales. This definition handles exact dyadic boundaries without numerical floor ambiguity. Let C=sum_{S nonempty}P_F(S)kappa(S). Sampling the unique outer label and the actual conditional nonempty child spectra gives

    J(F)=J(g)+sum_i a_i J(f_i)+2ln2 C.              (5)

The exact corrected-entropy and deficit identities give

    E(F)=E(g)+sum_i a_i E(f_i),
    Delta(F)=Delta(g)+sum_i a_i Delta(f_i).

Subtract (5) to obtain the actual signed rounding account

    2ln2 C=L(g)+sum_i a_i L(f_i)-L(F).              (6)

Thus a carry is paid from the SAME mantissa source while retaining the full final terminal L(F). It is not paid anew from each child's influence. Equation (6) is an exact identity, not a conditional-probability multiplication or an independence assumption about spectral bits.

For any finite read-once formula with literal leaves, define node weights recursively by omega_root=1 and omega_child=omega_parent*a_child. Let g_v be each internal gate at its induced law, and C_v the carry expectation for its actual composed subtree. Finite telescoping gives

    Delta(F)=sum_v omega_v Delta(g_v),
    2ln2 sum_v omega_v C_v+L(F)=sum_v omega_v L(g_v)
       <=sum_v omega_v B(g_v)<=11Delta(F)/2.        (7)

The last inequality uses B(g_v)<=11Delta(g_v)/2 at each gate and telescopes only Delta. No composition additivity for R or B is assumed.

Consequently, if every allowed gate satisfies J(g)<=KDelta(g) under every induced product law, then

    E(F)<= (K+11/2)Delta(F),
    Hplus(F)<= (K+11/2)Delta(F)/ln2.                 (8)

There is ONE additive natural constant11/2, independent of depth and fan-in. This is a conditional composition corollary, not an assertion that the required gate-scale theorem holds on all gates. It also follows from ordinary exact composition and (4); the carry derivation makes its source and final terminal explicit.

## 4. Compose the COMPLETE references, including both child laws

The reference itself composes without requiring it to be Boolean. Let Q_g and Q_i be the complete laws in section1, or recursively composed laws with the same empty atoms as the corresponding actual spectra. On the unique occupied-block decomposition define

    Q_tree(empty)=Q_g(empty),
    Q_tree(S)=Q_g(A) product_{i in A}[Q_i(T_i)/w_i].

Each conditional nonempty child law is normalized because Q_i(empty)=P_i(empty)=1-w_i. Therefore Q_tree is one complete normalized law on the FINAL physical label space. It retains every child terminal and the outer empty atom. If PF(S)>0, all its factors are positive. No mixture of incompatible physical laws is asserted.

Pointwise actual/reference likelihood ratios multiply on this disjoint representation. Taking their logs and expectations gives the ordinary KL identity

    KL(P_F||Q_tree)=KL(P_g||Q_g)
                          +sum_i a_i KL(P_i||Q_i).           (9)

This is a genuine product experiment conditional on the outer label, not a product bound inferred from marginal conditional probabilities. The corrected complete cross-entropy also decomposes with these weights. For literal leaves and dyadic references at each internal gate,

    C_tree^+=sum_v omega_v[J(g_v)+n(g_v)],
    n(g)=Var(g)ln(Z_g/Var(g)),
    E(F)=C_tree^+-KL(P_F||Q_tree),
    sum_v omega_v n(g_v)<=9Delta(F).                         (10)

Thus the conditional gate premise J(g)<=KDelta(g) pays the WHOLE reference bill C_tree^+<=(K+9)Delta(F), at all depths and fan-ins. Retaining its exact KL credit gives the sharper entropy constant(K+11/2) from (8). These are different quantities, not two revisions of one constant:9 pays the complete reference cross-entropy, while11/2 pays entropy after ordinary KL credit. The original physical deficit is used once through its exact telescope; neither a fresh root bank nor deletion of a child terminal appears.

For ordinary full entropy, append the SAME final empty-atom term and physical-bias term from section1 to both sides of the corrected cross-entropy identity. They have not vanished. On a uniform physical cube the bias term is zero; the empty term remains explicit.

## 5. Failure tests and exact unpaid step

The previous bent-tensor obstruction has all |c_S|=2^(-r). Hence W=P, Z=w, Q=P, L=0 and J=E=2r ln2(1-4^(-r)). The complete full entropy is2r ln2; the empty atom supplies2r ln2*4^(-r). There is no exponential local approximation error in this reference.

Booleanity cannot be dropped from (2)-(4). The real-valued fair one-bit f=(4+3(2x-1))/5 has squared masses16/25 and9/25, norm one, and Delta=0. Its singleton coefficient is3/5, so j=0, W=1, Z-w=16/25>0 and L=(9/25)ln(25/9)>0. Its derivative has d=9/25<t=3/5 and fails exactly the integer-admission line. Independence/disjointness is used exactly at the unique Fourier factorization and the inherited product-output law. Shared physical wires do not satisfy those hypotheses.

First unsupported universal line: J(f)<=KDelta(f) for every Boolean gate at all product biases, or a selected complete-reference version that pays this same dyadic scale cost from an unused original source. Equations (1)-(10) supply normalization, ordinary KL, endpoint admission, complete composition references and depth-independent carry bookkeeping. They do not pay J or solve full FEI. The source-dependent reference Q is permitted as a reference but does not make the scale-payment theorem easier by itself. No novelty or independent external acceptance is asserted.
