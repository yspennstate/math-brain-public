# Setup and source review

Natural logarithms and normalized product Fourier coefficients throughout. For an actual Boolean sign f at interior independent physical biases, set P(S)=v_S c_S^2, v_i=4p_i(1-p_i), w=Var(f), Delta=sum_(S nonempty)(|S|-1)P(S), and R=sum_(|S|>=3)(|S|-2)P(S). Contract deterministic inputs and constant children. References below are probability laws, not asserted Boolean spectra.

The reviewed source is A045-FLAT-TREE-DYADIC-SIGNED-REFERENCE-TRANSFER@1, original statement/hypotheses hash be44bc9e8e30330b7fee1efe1aa51f76c436f019d6dff57fe3f09e1588519d1f, proof hash 6ed696b896f9c532a3855e15570f89267b19a7441e89ad7b3dd1ba9f2c84d178. It restricts itself to signed conversion. The new bounds below require the additional actual dyadic structure, not an inference from signed expectation to expected absolute value.

# 1. Independent reconstruction of the source premises

For each occupied nonempty label choose the unique integer j>=0 with 1/2<u=2^j|c_S|<=1 and set W(S)=v_S 4^(-j). Let Z=sum_nonempty W. The complete flat reference is Q_0(empty)=P(empty), Q_0(S)=w W(S)/Z; use the empty point mass if w=0. Actual alternating Boolean differences give |c_S|<=1. Define J=ln4 sum Pj, L=sum P ln(1/u^2), and n=w ln(Z/w). Direct expansion gives E=J+L=J+n-KL(P||Q_0), where E=sum_nonempty P ln(v_S/P), so 0<=KL=n-L<=n.

For singleton i, t_i=|E d_i| and V_i=Var(d_i), with d_i in {-1,0,1}. The integer derivative inequality E d_i^2>=|E d_i| gives V_i>=t_i(1-t_i). If 0<t_i<=1/2, W(i)-P(i)<=v_i V_i: W<4v_i t_i^2 and the largest step occurs just above a dyadic boundary; more explicitly j>=1, W/v_i=4^-j and t_i>2^(-j-1), so W/v_i-t_i^2 <=t_i(1-t_i), equivalent to 4^-j<=t_i, which holds because 4^-j<=2^(-j-1)<t_i for j>=1. If t_i>1/2, j=0 and (1-t_i^2)/(t_i(1-t_i))=(1+t_i)/t_i<=3. The endpoints t_i=0,1 have zero excess. Physical Parseval gives sum_i v_i V_i=sum_S |S|1{|S|>=2}P=2Delta-R. The nonsingleton mass is Delta-R; its rounding excess is at most three times its mass. Consequently

    0<=Z-w<=B_0:=9Delta-6R,
    0<=n<=B_0,  0<=KL(P||Q_0)<=B_0.             (1)

For completeness L<=(11Delta-7R)/2: every nonsingleton has log(1/u^2)<=3/2 (since ln4<3/2). If t<=1/2, P(i)<=v_i V_i and the same factor 3/2 works. If t>1/2, j=0 and -2 t^2 ln t<=2t(1-t)<=2V_i, using -t ln t<=1-t. Thus singleton contributions cost at most 2 sum v_i V_i, and nonsingletons at most (3/2)(Delta-R), proving the bound. No finite enumeration is used to assert these all-dimensional facts.

For f=g(f_1,...,f_m) on DISJOINT physical child blocks at their actual independent output biases, a nonempty physical label has a unique occupied-block set A and labels T_i. Direct expansion gives

    c_f(S)=c_g(A) product_(i in A)c_i(T_i),
    P_f(S)=P_g(A) product_(i in A)P_i(T_i)/w_i,
    Q_tree(S)=Q_g(A) product_(i in A)Q_i(T_i)/w_i,

where w_i=Var(f_i)>0 and every complete Q_i has Q_i(empty)=1-w_i. The experiment first samples A, then a nonempty label in each occupied child. This proves normalization and the ordinary KL chain rule with a_i=I_i(g)/w_i. Corrected entropy and Delta have the same exact additive weights. For a finite literal-leaf read-once formula put omega_v equal to its inherited nonnegative gate weights and R_tree=sum_v omega_v R(g_v), which is NOT assumed equal to R_f. Then

    Delta(f)=sum_v omega_v Delta(g_v),
    KL(P_f||Q_tree)<=B_tree:=9Delta(f)-6R_tree.

The source signed equality C_tree^+-C_flat^+=KL_tree-KL_flat and bounds -B_0<=C_tree^+-C_flat^+<=B_tree now follow by subtracting log densities. This is a different derivation of the critical source steps; no source repair is needed. The source's universal J premise remains unaccepted. The AND3 at p_i=1/3 and repeated-wire countercontrol are checked separately by direct finite product sums.

# 2. New total-variation reserve with actual root ownership

Use TV(A,B)=(1/2)sum |A(S)-B(S)|. Write W=P+e on nonempty labels, with e>=0 and sum e=Z-w. Since Q_0=w(P+e)/Z on that sector,

    TV(P,Q_0)<=w(Z-w)/Z<=Z-w<=B_0.              (2)

This is a direct contamination calculation, not Pinsker's square-root bound and not a consequence of the signed KL estimate alone. It retains the actual empty atom.

There is a composition inequality with ACTUAL spectral weights:

    TV(P_f,Q_tree)<=TV(P_g,Q_g)+sum_i a_i TV(P_i,Q_i).      (3)

To prove it, first replace only the root law while leaving the same complete conditional child-Q kernel; total variation contracts under a Markov kernel. Then replace the children under the ACTUAL root law P_g. For fixed A, the product-TV inequality is at most sum_(i in A) TV(P_i/w_i,Q_i/w_i). The nonempty conditional child distance is TV(P_i,Q_i)/w_i because the empty masses agree. Its probability of occupation is sum_(A contains i)P_g(A)=I_i(g). This proves (3); no conditional marginal bounds are multiplied into a joint claim. Applying (2) at the gates and telescoping over the finite tree yields

    TV(P_f,Q_tree)<=B_tree,
    TV(Q_flat,Q_tree)<=B_0+B_tree
      =18Delta(f)-6(R_f+R_tree)<=18Delta(f).      (4)

These are one original deficit calculation with inherited weights. If an old debit exists it is not refunded or forgotten: the displayed amount is an additional explicit bill within that original allowance, not a fresh reserve at each depth.

# 3. New complete adaptive-selector reference

For the two references on the SAME final labels let K(S)=max(Q_flat(S),Q_tree(S)) for nonempty S. Both have the same actual empty atom and actual support. The exact identity for maxima is

    Z_max:=sum_nonempty K=w+TV(Q_flat,Q_tree).

Define Q_max(empty)=P(empty), Q_max(S)=w K(S)/Z_max, with the empty-point convention at w=0. This is a complete normalized reference. Its normalization tax obeys

    0<=w ln(Z_max/w)<=Z_max-w
       <=B_0+B_tree<=18Delta.                  (5)

The reference can choose which law is larger AFTER seeing the entire label. Since K dominates either law pointwise, the corrected cross-entropy satisfies

    C_max^+ <= min(C_flat^+,C_tree^+) + B_0+B_tree.          (6)

Ordinary full cross-entropies have the same comparison after retaining the identical empty and physical-bias contributions. More generally any deterministic selector K_sigma(S) in {Q_flat(S),Q_tree(S)} is normalized on the full nonempty sector in the same manner. Its positive normalization tax is at most B_0+B_tree; its selected raw cross-entropy must still be retained. Equation (6) requires the maximum selector. Neither reference is being admitted as a Boolean function. No uniform pointwise P<=c Q, conditional-input TC payment, or good-coordinate erasure estimate is inferred.

The exact entropy identity after selection is E=C_max^+-KL(P||Q_max). This is the ordinary full KL with respect to the new complete reference. Replacing the reference replaces its KL term; neither old KL rebate can also be subtracted.

# 4. New absolute likelihood conversion

At a complete formula label let lambda_tree be the sum of the local -ln u_v^2 and c_tree the sum of the local ln(Z_v/w_v) on its unique occupied derivation. Both are nonnegative. Then log(P/Q_tree)=c_tree-lambda_tree and E_P c_tree=n_tree=sum omega_v n_v. For the flat reference, log(P/Q_flat)=c_0-lambda_0 on nonempty labels, with E_P c_0=n_0.

Coefficient multiplication implies j_flat=sum occupied j_v+kappa(S), with integer kappa>=0; exact dyadic boundary convention gives kappa=floor(sum occupied -log_2 u_v). Thus lambda_tree-lambda_0=ln4*kappa>=0. Consequently

    log(Q_flat/Q_tree)=c_tree-c_0-ln4*kappa,
    E_P |log(Q_flat/Q_tree)|
      <= n_tree+n_0+L_tree-L_0
      = n_tree+L_tree+KL_flat
      <= (47/2)Delta -6R_f -(19/2)R_tree.        (7)

Here L_tree=sum omega_v L_v<=(11Delta-7R_tree)/2 and n_tree<=9Delta-6R_tree; equation (1) bounds KL_flat. Empty atoms give log ratio zero. Formula (7) uses more than the source signed theorem; in particular it retains the nonnegative integer carry. It is not a pointwise bound. The finite formula's full terminal laws and the single original Delta are retained throughout.

# 5. Exact unpaid line and why this changes the mechanism

The universal dyadic-scale expectation J(f)<=K Delta(f) for actual gates at all induced product biases is STILL UNPROVED, as is the arbitrary-real-weight biased threshold FEI+ estimate. Equations (4)-(7) pay a different, previously unbounded interface: whole-set adaptive selection and expected absolute conversion between the two complete dyadic references, with constants independent of depth and arity. They permit changing reference without a raw Var(f) ln2 near-dictator tax. They do not authorize spending an old paid source twice or subtracting two KL rebates.

The next useful step is to price the actual weighted-threshold scale charge J in whichever of these two admitted REFERENCES is cheaper, using (5) once from the same unused owner. The prior count-tail quadratic reference and its unbounded pointwise coherence are not silently identified with either dyadic reference. The recovered conditional-input normalization/TC counterfamilies remain controls; the pivotal-credit failure remains coefficient-one only. Full FEI remains OPEN.
