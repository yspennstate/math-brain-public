# Transfer between two complete dyadic references

All logarithms are natural. The physical inputs are independent Bernoulli variables with interior biases, after deterministic coordinates have contracted. For an actual Boolean sign write P(S)=v_S c_S^2, v_i=4p_i(1-p_i), Delta=sum_nonempty(|S|-1)P(S), and R=sum_|S|>=3(|S|-2)P(S). Empty and zero-probability terms are treated explicitly. The reference laws below need not be Boolean Fourier laws.

## 1. Independent reconstruction of the source dyadic normalizer

Actual alternating Boolean cofactor sums imply |c_S|<=1. For a nonzero coefficient choose the unique j>=0 with1/2<u=2^j|c_S|<=1. Put W(S)=v_S4^(-j), and W(S)=0 on the unoccupied nonempty labels. If w=Var(f)>0, define

    Q_flat(empty)=P(empty),
    Q_flat(S)=w W(S)/Z,   Z=sum_nonempty W(S).

This is normalized and positive on actual support. For w=0 it is the empty point mass. Since P/W=u^2, direct expansion on each nonempty atom gives

    E=J+n-K_flat,   n=w ln(Z/w),
    J=ln4 sum_nonempty P(S)j_S,
    K_flat=KL(P||Q_flat),   L=E-J>=0.

No empty term is lost: the two empty masses agree, so their likelihood ratio is1. For ordinary entropy one must additionally retain P(empty)ln(1/P(empty)) and sum_nonempty P(S)ln(1/v_S).

For |S|>=2, W-P<3P, so the total excess in this sector is at most3(Delta-R). At a singleton, let t=|E D_i|, V=Var(D_i), where D_i is the physical half-difference and takes only values -1,0,1. Thus V>=t(1-t). If0<t<=1/2, dyadic rounding gives W(i)-P(i)<=v_i V; if t>1/2 it gives W(i)-P(i)=v_i(1-t^2)<=3v_i V. At t=0 or1 the excess is0. Exact physical Parseval gives

    sum_i v_i V_i=2Delta-R.

Consequently

    0<=Z-w<=9Delta-6R,
    0<=n<=9Delta-6R,
    0<=K_flat=n-L<=9Delta-6R.                    (1)

The middle bound uses ln x<=x-1; the last also uses nonnegativity of ordinary KL. Every denominator is positive on its stated support. There is no claim that the source-dependent reference pays J.

## 2. Composition uses the complete inherited child laws

Let F=g(f_1,...,f_m) with disjoint physical child blocks. Contract constant children, put w_i=Var(f_i)>0, and evaluate g at the ACTUAL independent child-output biases. A nonempty physical label S decomposes uniquely into occupied block set A and nonempty child labels T_i. Direct expansion yields

    c_F(S)=c_g(A) product_(i in A)c_i(T_i),
    P_F(S)=P_g(A) product_(i in A) P_i(T_i)/w_i.

For complete child references with Q_i(empty)=P_i(empty), set

    Q_tree(empty)=Q_g(empty),
    Q_tree(S)=Q_g(A) product_(i in A) Q_i(T_i)/w_i.

Each conditional child reference has mass1 on its nonempty labels. This proves full normalization of Q_tree and positivity on actual support, retaining every child terminal. Ratios multiply pointwise in the unique decomposition, so taking finite sums of their logarithms gives

    KL(P_F||Q_tree)=KL(P_g||Q_g)+sum_i a_i KL(P_i||Q_i),
    a_i=I_i(g)/w_i>=0.

The same actual sampling experiment gives exact corrected entropy and deficit additivity E(F)=E(g)+sum a_i E(f_i) and Delta(F)=Delta(g)+sum a_i Delta(f_i). No conditional marginal bound is multiplied into a joint bound without this experiment.

For a finite read-once formula with literal leaves let omega_v be the recursively inherited nonnegative gate weights. Then

    K_tree:=KL(P_F||Q_tree)=sum_v omega_v K_v,
    Delta(F)=sum_v omega_v Delta(g_v),
    0<=K_tree<=A_tree:=sum_v omega_v(9Delta(g_v)-6R(g_v))<=9Delta(F).       (2)

For the literal leaves Q=P. Both references keep the same final empty atom. There is no assumed additivity for R: in general sum omega_v R(g_v) differs from R(F).

## 3. Exact signed conversion, and its paid scope

Let C_flat^+=sum_nonempty P_F(S)ln(v_S/Q_flat(S)) and define C_tree^+ with Q_tree. Because both references have the same empty atom as P_F,

    C_tree^+-C_flat^+
      =sum_nonempty P_F(S)ln(Q_flat(S)/Q_tree(S))
      =K_tree-K_flat.                             (3)

Thus the full signed reference-change charge satisfies

    -(9Delta(F)-6R(F)) <= C_tree^+-C_flat^+ <= A_tree,
    |C_tree^+-C_flat^+|<=9Delta(F).                 (4)

This is an expected signed likelihood conversion, not a pointwise likelihood-ratio bound or a bound on expected absolute log likelihood. The two KL rebates cannot both be subtracted. If one replaces C_tree^+ by C_flat^+, equation(3) replaces the KL term at the same time. A preexisting debit against Delta remains a debit; (4) does not manufacture a second reserve.

For ordinary full cross-entropy the same conversion holds, since both the empty contribution and the physical-bias correction are identical and cancel. The units and the reference identity are not changed.

## 4. The references are actually different on an admitted nonflat source

Take three independent bits with p_i=1/3 and F=AND2(AND2(X_1,X_2),X_3), with Boolean sign output. The final gate is actual AND3. It has

    P(empty)=625/729,
    P(singleton)=8/729,
    P(pair)=16/729,
    P(triple)=32/729,
    Z_flat=1363/5832.

At singleton {1}, direct construction gives

    Q_flat({1})=104/12267,
    Q_tree({1})=256/10521.

Both are complete normalized references on the SAME final physical label space. The numerical disagreement is an exact rational inequality and does not invalidate either reference. It invalidates identifying them for free. The parent/child gates have Fourier degree at most2 and hence R(g_v)=0, while R(F)=32/729>0; this also demonstrates why their R terms cannot be silently telescoped.

Shared wires violate the hypotheses. At p_X=1/3, AND(X,X)=X has empty Fourier mass1/9. The fictitious independent AND of two inputs with those marginal biases has empty mass49/81. The independent child-output law, unique occupied-block decomposition and equal-empty likelihood proof cannot be used for this repeated-wire gate. This is an actual Boolean control, not a relaxation. It does not exclude a different shared-variable theorem with an explicit coherent collision term.

## 5. Carries and the exact remaining universal line

The source's carry account also reconstructs directly. Products of the actual normalized coefficients give

    j_F=j_g+sum j_i+kappa,
    kappa=floor(-log_2 u_g-sum log_2 u_i)>=0.

The exact scale difference is an integer, so dyadic boundaries require no numerical floor. Taking the actual spectral expectation gives J(F)=J(g)+sum a_i J(f_i)+ln4 E[kappa]. Subtracting this from exact corrected entropy additivity gives

    ln4 E[kappa]=L(g)+sum a_i L(f_i)-L(F).

For completeness the needed N=0 mantissa estimate follows from ln(1/u)<=2z/(1-z^2), z=(1-u)/(1+u)<1/3. High-degree terms cost at most(3/2)(Delta-R). For singleton t<=1/2, P(i)<=v_i V_i and the same3/2 factor applies. For t>1/2, the bound divided by v_i t(1-t) is at most1+t<=2. Summing the actual singleton reserve once gives

    L(f)<=(11Delta-7R)/2<=11Delta/2.

Finite telescoping therefore pays all weighted carries plus the entire final L(F) from sum omega_v L(g_v)<=11Delta(F)/2. Together with (1)-(2), this independently reconstructs the A044 source claim, including its conditional gate-J closure, without a repair. It does not newly certify all-N approximation clauses belonging to A042.

First unsupported universal line: pay J(f)<=KDelta(f), or an appropriate inherited complete-reference version, for every actual Boolean gate at all induced biases. Equations(1)-(4) allow a correctly owned transfer between flat and tree references, but neither pays that scale. Full FEI remains open; there is no new universal entropy constant or FEI counterfamily.
