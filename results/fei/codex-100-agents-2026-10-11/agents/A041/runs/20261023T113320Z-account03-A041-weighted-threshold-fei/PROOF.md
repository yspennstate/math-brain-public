# Units, physical scope and reviewed source

Natural logarithms throughout. For an actual Boolean sign f on an interior independent product cube, put P(S)=fhat(S)^2=v_S c_S^2, v_i=4p_i(1-p_i), Delta=I-Var(f), R=sum_(|S|>=3)(|S|-2)P(S), and H=sum_(|S|>=2)P(S)=Delta-R. Contract deterministic inputs and constant children. Complete references are auxiliary probability laws; they are not claimed Boolean Fourier spectra.

Reviewed source: A043-PAID-SECTOR-COMPLETE-REFERENCE@1, statement hash 502a92f6beccba0801965fe24c8430ba1f45d1258bf4283ea5cf8a2cc42ef451, run20261023T063610Z. Its prime high-scale premise is explicitly OPEN. Sections 1 and 6 below reconstruct its whole stated mathematical interface without a repair. Subsequent sections extend the reference and carry interface. They do not pay the universal prime-gate scale charge.

# 1. Independent reconstruction of the paid-sector reference

Let j_S be the unique integer >=0 satisfying 1/2<u_S=2^j_S|c_S|<=1 for each occupied nonempty S; dyadic boundary points use u=1. Actual alternating Boolean cofactor differences give |c_S|<=1. On the HIGH sector |S|>=2 set W(S)=v_S 4^(-j_S), Z=sum_high W, and preserve the exact actual empty AND singleton masses:

    Q_0(S)=P(S) for |S|<=1,
    Q_0(S)=H W(S)/Z for |S|>=2.

If H=0 use Q_0=P. No actual-support atom is omitted. Write

    E_1=sum_singleton P ln(1/c_S^2),
    J_hi=ln4 sum_high P j_S,
    L_hi=sum_high P ln(1/u_S^2),
    n=H ln(Z/H).

Since P<=W<4P, 0<=n<=ln4 H and 0<=L_hi<=ln4 H. Direct substitution on each label proves

    E=E_1+J_hi+L_hi=E_1+J_hi+n-KL(P||Q_0),
    KL(P||Q_0)=n-L_hi>=0.                         (1)

This is ordinary full KL; its low-sector terms are zero. At zero high mass all four high quantities vanish.

For d_i=(f|i=1-f|i=0)/2 in {-1,0,1}, let rho_i=E d_i^2 and t_i=|E d_i|. Booleanity gives rho_i>=t_i. The scalar -t ln t<=1-t gives

    -2t_i^2 ln t_i <=2t_i(1-t_i)<=2(rho_i-t_i^2).

Physical Parseval gives sum_i v_i(rho_i-t_i^2)=sum_(|S|>=2)|S|P(S)=2Delta-R. Hence

    0<=E_1<=4Delta-2R.                            (2)

With the actual nonnegative refunds S_res=4Delta-2R-E_1 and U=ln4 H-L_hi, equations (1)-(2) give the source exact identity

    E=J_hi+(4+ln4)Delta-(2+ln4)R-S_res-U.           (3)

Comparison with the earlier all-nonempty-rounded reference Q_all is an exact KL chain rule on {empty,singleton,high}. Its within-high conditional law is the same as Q_0. Thus KL(P||Q_all)-KL(P||Q_0) is the sum of the nonnegative singleton-conditional KL (weighted by actual singleton mass) and the nonempty singleton/high Bernoulli-sector KL. Cross-entropies differ by exactly the same amount. If a sector is empty, contract that sector rather than form an undefined conditional law. This rederives the entire source reference/normalizer/refund interface, not only its headline upper bound.

# 2. Actual composition preserves singleton masses globally

Let F=g(f_1,...,f_m) on disjoint physical blocks at actual induced independent child-output biases. Let w_i=Var(f_i)>0 and a_i=I_i(g)/w_i. A physical label decomposes uniquely as occupied block set A and nonempty child labels T_i. Direct expansion in the centered product basis yields

    c_F(S)=c_g(A) product_(i in A)c_i(T_i),
    P_F(S)=P_g(A) product_(i in A)P_i(T_i)/w_i.

Compose complete paid-sector references by

    Q_T(empty)=P_g(empty),
    Q_T(S)=Q_g(A) product_(i in A)Q_i(T_i)/w_i.

The conditional child reference has total nonempty mass one because its actual empty mass is retained. Thus this experiment defines a normalized complete law and preserves every actual-support label. For a physical singleton, A is a singleton and its unique child label is a singleton. All those factors are EXACT actual masses. By induction through any finite literal-leaf formula,

    Q_T(S)=P_F(S) for every |S|<=1.                (4)

This is stronger than just equality of empty atoms. In particular BOTH the final flat reference Q_0 and composed Q_T put exactly H_F=Delta(F)-R_F on the high sector.

The same unique sampling experiment proves ordinary KL additivity, corrected entropy additivity, and Delta additivity with weights a_i. For inherited gate weights omega_v and literal leaves, set R_T=sum_v omega_v R(g_v) and H_T=sum_v omega_v H(g_v)=Delta(F)-R_T. R_T is not assumed equal to R_F. Then

    KL(P_F||Q_T)=sum_v omega_v KL(P_gv||Q_v)<=ln4 H_T,
    Delta(F)=sum_v omega_v Delta(g_v),
    E(F)=sum_v omega_v E(g_v).                    (5)

Repeated wires do not have this unique disjoint decomposition. They remain excluded, rather than being treated as independent child outputs.

# 3. New whole-label adaptive selection cost: H_F ln2

On the final high sector define K(S)=max(Q_0(S),Q_T(S)); freeze the low sector at actual P_F. Let Z_max=sum_high K. Since each reference has total high mass H_F,

    H_F<=Z_max=H_F+TV(Q_0,Q_T)<=2H_F,

where TV is total variation on the complete law (all low differences are zero). Define the complete maximum reference by Q_max=P_F on |S|<=1 and Q_max(S)=H_F K(S)/Z_max on the high sector. At H_F=0 use Q_max=P_F. Its EXACT normalization cost is

    0<=H_F ln(Z_max/H_F)<=H_F ln2=(Delta(F)-R_F)ln2.       (6)

Thus one may select the larger reference AFTER observing the entire Fourier label. The corrected cross-entropy obeys

    C_max^+<=min(C_0^+,C_T^+)+H_F ln2,
    E(F)=C_max^+-KL(P_F||Q_max).                   (7)

The KL in (7) REPLACES the old KL; no second rebate is available. An arbitrary binary selector has the same upper bound on its positive normalization cost but must retain its own raw cross-entropy. An m-reference maximum costs at most H_F ln m; no count-free infinite-menu assertion is made. This proof in fact applies to ANY two complete references that preserve all actual low-sector masses, not just dyadic ones.

The previous18Delta payment applied to references that preserved only the empty atom and normalized the whole nonempty sector. Equation (6) uses the NEW singleton-preserving class and normalizes only its high sector. It does not silently sharpen the old reference's bound or modify the old theorem.

# 4. New expected absolute conversion bound

For the flat high sector log(P_F/Q_0)=c_0-lambda_0, where c_0=ln(Z/H_F)>=0, lambda_0=ln(1/u_F^2)>=0, and both are zero on low labels. Their expectations are n_0 and L_0, each <=ln4 H_F. For Q_T the log ratio is the sum of the occupied local high-sector c_v-lambda_v; local singleton terms are exactly zero. The actual sampling experiment gives expected nonnegative sums n_T and L_T, each <=ln4 H_T. Triangle inequality therefore proves

    E_P |ln(Q_0/Q_T)|
       <=n_0+L_0+n_T+L_T
       <=2ln4(H_F+H_T)
       =2ln4(2Delta(F)-R_F-R_T)<=4ln4 Delta(F).    (8)

This is an expected absolute conversion, not a pointwise bound. It is derived from the actual local density factors, not from a bound on signed expectation. The signed conversion remains KL_T-KL_0. Both terminal laws are kept, even when some actual coefficient vanishes.

# 5. New nonnegative HIGH-scale carries and their single all-depth bank

For a final occupied physical label S, sum j_A only over the occupied local GATE LABELS of degree at least two in its unique formula derivation. Call this sum b_T(S). If |S|=1 every local label is a singleton, so b_T(S)=0. If |S|>=2, coefficient multiplication and |c_v|<=1 imply

    j_F(S)=floor(log_2(1/|c_F(S)|))
       >=sum_all occupied local j_v >= b_T(S).

Consequently kappa_hi(S)=j_F(S)-b_T(S)>=0 is an integer on high labels and is zero on low labels. Its actual expectation is the exact all-depth carry

    A_hi:=ln4 E_P kappa_hi
         =J_hi(F)-sum_v omega_v J_hi(g_v)>=0.     (9)

Unlike the fully rounded reference, omitting singleton scales DOES NOT make (9) a pure mantissa refund. Corrected entropy additivity gives the exact identity

    A_hi+E_1(F)+L_hi(F)
       =sum_v omega_v[E_1(g_v)+L_hi(g_v)]
       <=(4+ln4)Delta(F)-(2+ln4)R_T.              (10)

Thus the nonnegative carries, the full final singleton entropy AND the final high mantissa share ONE original bank. Finite telescoping of the nonnegative one-step carries gives exactly A_hi, with no depth surcharge. Old debits against that bank stay debited; (10) cannot also be booked as a new reserve elsewhere. The prime-gate J_hi terms on the right of (9) are STILL UNPAID.

An exact actual control prevents loss of E_1 in (10). Let F=AND3 on fair bits, decomposed as AND2(AND2(X1,X2),X3). The root is evaluated at actual biases (1/4,1/2); its child weight is1/2. All relevant normalized coefficients are dyadic, so all high mantissas and both reference normalizers/KL terms are zero, and Q_0=Q_T=P_F. Nevertheless

    J_hi(F)/ln4=1/2,
    sum omega_v J_hi(g_v)/ln4=5/16,
    A_hi/ln4=3/16,
    E_1(F)/ln4=3/8,
    sum omega_v E_1(g_v)/ln4=9/16.

Hence the proposed mantissa-only carry identity would incorrectly give zero. The actual carry is paid by the SINGLETON transfer of3ln4/16; no reference normalization or KL can pay this example. The same control is an actual weighted-threshold function. This is an obstruction to that proof shortcut, not a counterexample to FEI.

# 6. Reviewed prime localization and exact remaining line

For an essential k-input gate, a proper block of size2 through k-1 factors through a Boolean child precisely when its cofactors have exactly two distinct rows. One row would mean dummy coordinates; two rows define the child and quotient gate. Repeated proper factorizations reduce arity and terminate in a finite literal-leaf prime decomposition on disjoint physical blocks. All induced child laws are the actual independent product laws. A common prime bound J_hi(g)<=K Delta(g), over EVERY arity and induced law, together with (5), (2) and L_hi<=ln4 H gives E(F)<=(K+4+ln4)Delta(F). Conversely J_hi<=E since |c_S|<=1. At uniform physical inputs, -P(empty)ln P(empty)<=Var(F), so corrected FEI+ implies uniform bit FEI with constant max(K+4+ln4,1)/ln2. These steps reconstruct A043's full stated conditional localization, without supplying its premise.

The exact first unsupported line remains an arity-independent payment of the ACTUAL prime/weighted-threshold high-degree dyadic scale J_hi from the SAME unused original deficit, or its sharper refund-inclusive inequality. Equations (6), (8), (9)-(10) pay adaptive reference normalization, absolute conversion and composition carries, respectively; they do not pay that supplier. Normalizer-zero AND3 already shows why scale and mantissa cannot be identified. The original conditional-input TC controls remain separate from spectral good-coordinate erasure, and the pivotal-credit refutation remains coefficient-one only. Full FEI remains OPEN.
