# Stage 3 independent reconstructions

Units in the A066 discussion are nats; units in the A096 discussion are bits. These are independent reconstructions of original source claims, not repairs supplied by A100. They do not establish a finite universal FEI constant.

## A066-POSITIVE-RESTRICTION-HEAT-LEDGER v2

For a block B, write the coherent child coefficients as sums over its queried Fourier index U, and let q_T=sum_U p_(U union T). Orthogonality gives E_y p_y(T)=q_T. Finite entropy subtraction gives H_nat(parent)-E H_nat(child)=sum_T[M_T+C_T], where M_T=sum_U p_(UT)ln(q_T/p_(UT)) and C_T=E_y p_y(T)ln(p_y(T)/q_T). M_T is nonnegative conditional entropy; C_T is nonnegative by convexity of x ln x. Removing the empty residual row cancels its channel against the parent/child empty-atom entropies and leaves

2(K(parent)-E K(child))=M_B^++C_B^++ell_B,

where K=(H_nat-p_empty ln(1/p_empty))/2 and ell_B=sum_(nonempty U subset B)p_U ln(1/p_U). The separately accepted heat-entropy identity identifies this K with the finite-cube integral; no new integrability argument is required. Finite adaptive block trees telescope this identity with K at every terminal leaf retained.

For a singleton, row amplitudes a,c have channel cost (a²+c²)g(2ac/(a²+c²)), g(t)=((1+t)ln(1+t)+(1-t)ln(1-t))/2. On [0,1), g'(t)=atanh t <= t/sqrt(1-t²): the right-hand derivative is (1-t²)^(-3/2), which exceeds (atanh t)'=(1-t²)^(-1). Integrating gives g(t)<=1-sqrt(1-t²), with evenness and continuity supplying the endpoints. Hence the channel cost is <=2min(a²,c²). Omitting the empty row spends at most 2(d-x²), where d=Inf_i and x=|fhat({i})|. The Boolean derivative takes values 0,+1,-1, so x<=E|D_i f|=d. Thus

C_i^++ell_i <=2d+2x²(ln(1/x)-1).

For x>=e^-1 the extra term is nonpositive. For 0<x<e^-1, division by d and x<=d bound the extra term by 2x(ln(1/x)-1), whose derivative is -2ln x-4 and maximum is 2e^-2 at x=e^-2. Zero x gives no extra charge. Consequently C_i^++ell_i <=(2+2/e²)d. Physical singleton influence telescopes to I(root)-E I(leaf), so this is a joint, nonreused budget for every finite singleton-query tree. It is not an all-block price. Compared with the old separately paid coefficient, the proved saving is 2/e-2/e²; it does not reduce a proved universal FEI constant, because the erasure residual remains unpaid.

For the empty row, masses u=p_empty, v=x² satisfy phi_nat(u,v)<=v ln(1/v)+v, since u+v<=1 and u ln(1+v/u)<=v. Boolean x<=d and x ln(1/x)<=1/e give this missing erasure <=(1+2/e)d. Summing yields 0<=B_nat-R_nat<=(1+2/e)I. Fresh-character tensor admission F_m=y product_j g_j forces every occupied context for core coordinates to be nonempty. Tensor independence gives R_nat(F_m)=mB_nat(g) and I(F_m)=mI(g)+1; the fresh character has zero erasure. Therefore the two unrestricted optimal constants coincide in the extended reals, by taking m large for each seed and using R_nat<=B_nat for the converse. The conditional FEI implication (A+2)/ln2 is the already checked C018 conversion. No finite A is proved.

This establishes the full repaired v2 at its explicit singleton-tree scope. A088 is a contributor to this version through the scope correction and is not counted as a v2 independent acceptor. The v1 unqualified block-tree clause remains withdrawn; author substitution to v2 is now observed, while canonical adoption remains unverified.

## A096-TERMINAL-KL-REFUND-AUDIT v1

For each relevant physical coordinate i, the laws mu_i(T)=p_(T+i)/e_i and r_i(T)=p_T+p_(T+i) normalize exactly. The joint laws P(i,T)=p_(T+i)/I and Q(i,T)=(e_i/I)r_i(T) share coordinate marginal e_i/I. The KL chain rule gives I D(P||Q)=sum_i e_i D(mu_i||r_i). Direct subtraction gives M=sum_i e_i log2(1/e_i)-I D(P||Q). All support ratios are finite because r_i contains the upper mass. Constants use I D=0.

For h=chi_Z product_(b=1..m)f_b with ell>=2 fresh parity bits, both laws of a core derivative factor with the same complete laws of the other blocks. Thus D_i(h)=D_i(f) and M(h)=mM(f). A parity derivative has mu=r and contributes zero divergence and oriented erasure. J=I(h)=mI(f)+ell. Its Fourier support contains Z; its mean and singleton coefficients vanish.

Activate on k fresh controls: F=1+A_k(h-1), q=2^-k. Its empty coefficient is 1-q, every other pure-control coefficient has magnitude q, and each h coefficient appears with amplitude q in every control slice. Direct physical edges, or Parseval, give I(F)=q(J+k).

For a core derivative, mu_F is mu_h times the uniform control-subset law, while its residual law on that support is q times r_h times the same law. The exceptional constant endpoint is absent from derivative support because h has no singleton coefficients. Each likelihood ratio therefore gains exactly 1/q: D_i(F)=D_i(h)+k, and M_i(F)=qM_i(h).

For a control derivative, the exceptional atom has derivative mass q and residual mass d=(1-q)²+q². All other atoms have ratio 1/(2q) and total derivative probability 1-q. Therefore D_c=(1-q)(k-1)+q log2(q/d), and M_c=q(1-q)+q²log2(d/q²). Summing with the actual influence weights gives

I(F)D_F=q[mI(f)D_f+kJ+kD_c],
M(F)=qmM(f)+k[q(1-q)+q²log2(d/q²)].

In the |T|>=2 tail, all positive core costs survive. For each control, nonempty core rows supply q/2; eligible pure-control rows supply q²[2^(k-1)-k]. Hence M_ge2(F)=qmM(f)+kq(1-kq). This differs by a factor two in the control term from the corresponding symmetric erasure formula. The refund cancels wrapper rarity but retains the arbitrary seed divergence. No terminal-core payment is created.

For any fixed ell>=2 and finite nonnegative s(N)=o(N), let eta_m=sup_(N>=mn)s(N)/N. It is finite and tends to zero. Set k_m=ceil(4(n+1)m sqrt(eta_m)+2sqrt(m)). Then k_m=o(m), N_m=mn+ell+k_m<=(n+2)m eventually, and k_m-s(N_m)>=2sqrt(m)>log2(mI(f)+ell+k_m). Thus F_m lies in the cutoff class and M_geell(F_m)/I(F_m)>=mM(f)/(mI(f)+ell+k_m), tending to the seed ratio. The reverse inequality is M_geell<=M. Apply this to each finite seed ratio if the unrestricted supremum is infinite; no interchange with an infinite supremum is required. Constant seeds do not affect the supremum and satisfy the finite identities by the stated convention.

This reconstructs the entire stated refund audit. The first unsupported universal line is D(P_f||Q_f)>=sum_i(e_i/I)log2(1/e_i)-K for a finite absolute K and every Boolean seed. That is a C018 obligation, not a solved low-influence case. The already independently reviewed parity-tail theorem puts every fixed-degree remainder at this same universal strength; moving the starting level alone cannot weaken the problem.

## Release scope guards

A081's complete finite-tree reconstruction accepts A097-COMPATIBLE-LEAF-REFERENCE-TRANSFER v1; A094's newest receipt accepts only its one-node clause. These are compatible review scopes, not conflicting verdicts. Neither pays the universal hypothesis sum pi(B-kappa)<=K I_removed or the terminal CE. The recent one-shared-data transfer has A094's full stated-scope review but retains seed/reference costs and an l1 admission hypothesis for larger blocks.

A099's aggregate low-influence v2 is reviewed as a fragment by A090 and A081. A090's full fixed-tail theorem has A096, A081 and A099 scoped acceptances. A096's normalized refund audit has A073/A099 source receipts, augmented by this independent reconstruction. These do not confer acceptance on the entire assembled manuscript, the new shared-bit transfer, or a universal terminal-KL payment. A001's influence-vector-only prior obstruction is accepted by A098 at that slice and rules out a route to complete CE, not FEI itself. Its permitted alternative is a function-specific conditional-edge reference with a paid signed refund and one cross-degree influence budget.
