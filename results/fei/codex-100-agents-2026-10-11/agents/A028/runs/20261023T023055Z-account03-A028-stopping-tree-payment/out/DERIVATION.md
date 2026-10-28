# Prescribed profile reconstruction: candidate proof

All logarithms are base two. Independent physical blocks Y,X; Boolean a(Y),G(X),H(X), c=(1-a)/2, p=Ec, f=(1-c)G+cH. Sources may share all of X. At each physical history let P_g,P_h be the actual squared spectra. Supply normalized R_g,R_h positive on the corresponding true supports; off-support mass is retained.

Set q=(1-p)P_g+pP_h and r=(1-p)R_g+pR_h. The actual joint output spectrum P_f(U,t) has marginal q(t). Define k(U|t)=P_f(U,t)/q(t) when q(t)>0 and k(U|t)=1[U=empty] otherwise. Prescribe R_f(U,t)=r(t)k(U|t). This is an algorithm fixed before the tree; it uses the true structural conditional profile, not a canonical reference supplied externally. D_f=D(P_f||R_f)=D(q||r).

Write W=(1-p)D(P_g||R_g)+pD(P_h||R_h), Z=W-D_f. Log-sum gives Z>=0, including p=0,1. More precisely Z is the q-weighted conditional KL of the hidden source label, whose two joints are ((1-p)P_g,pP_h) and ((1-p)R_g,pR_h).

At a data query i, inherit each source reference through its own actual-phase pair kernel: alpha=g_hat(T), beta=g_hat(T+i), s=alpha^2+beta^2; from either member of this pair send mass to (b,T) with probability (alpha+(-1)^b beta)^2/(2s). For s=0 use probability 1/2. If the reference output has branch masses rho_b, normalize its two child references by rho_b. True output is (1/2)P_{g_b}; rho_b>0. Erasing pair membership costs E_g>=0 and outcome normalization costs O_g=D((1/2,1/2)||rho)>=0. Exact chain rule: D_g=E_g+O_g+(D_{g_0}+D_{g_1})/2. Control queries keep source references fixed and make p harmonic. Thus A_v=W_v-E_v W_child>=0 for all queries (zero for control queries).

Reconstruct the prescribed profile reference at each child from these inherited source references. Put sigma_v=E_v D_{f_child}-D_{f_v}. Then sigma_v=Z_v-E_v Z_child-A_v. For any finite adaptive mixed tree, with actual uniform branch reach weights,

    sum_v reach(v) sigma_v + sum_v reach(v) A_v + E_leaf Z_leaf = Z_root.

Consequently E_leaf D_f <= W_root. Retaining all entropy drops Delta H_v=H(f_v)-E H(f_child),

    sum_v reach(v) Delta H_v + E_leaf CE(P_f,R_f)
      = H(f_root)+E_leaf D_f
      <= H(f_root)+W_root
      = (1-p)CE(P_g,R_g)+p CE(P_h,R_h)+Pi_root,

where Pi_root=H(f_root)-(1-p)H(g)-pH(h)=J_root+L_root is the previously proved signed entropy surcharge. Thus source CE suppliers and the original Pi allowance fund this prescribed reconstruction across every mixed stopping tree, with no renewed source bank.

The actual path cost Delta H_v is nonnegative: erase the queried spectral membership to obtain pair law s, and observe that the average of the two child spectral laws is s. Hence Delta H_v=H(S_i|S_without_i)+[H(s)-average H(P_child)]=B_i+JS_i>=B_i>=0. It is only the decomposed source/structural/reference transactions that need signed accounting. The same bound therefore also pays the nonnegative erasure path cost sum reach*B_i and terminal CE.

Actual reset audit: if R_f is first transported through its own physical pair kernel to inherited references R_f^inh, write E_f,O_f for that kernel's erasure and outcome KL refunds. The raw reset kappa_v=E[D(P_child||R_f^target_child)-D(P_child||R_f^inh_child)] equals sigma_v+E_f+O_f. Only kappa_v-(E_f+O_f)=sigma_v is paid from Z; no bound on raw positive reset charges is asserted. For controls the physical query is on Y; the same identity applies to the full f spectrum. All references, both terminal KL terms, and branch normalizers remain present.

Old-debit rule: if an original earmark U already has unrelated debit b, the displayed payment is usable only when U-b >= H(f_root)+W_root (or its stated source-CE-plus-Pi upper bound). Z is the slack inside that allowance, not additional money on top of W. Positive parts and separately prescribed fresh references are not covered.

First unsupported universal line: providing source CE suppliers and the controller entropy bound at a dimension-independent root influence rate for every Boolean input, or paying a conversion from these profile references to externally required terminal references at that same original rate. This proof does not supply either line.

## Same original JS account: common-root-reference corollary

If R_g=R_h=R at the root, then W_root-D_froot=H(q)-[(1-p)H(P_g)+pH(P_h)]=J_root. Thus Z_root is EXACTLY the original JS bank, not a new descendant source allowance. After data restrictions the two source references generally differ, so this is not a rule to renew J at a descendant. The inherited Z account, rather than a fresh JS at every node, pays the subsequent reconstructions.

In full units, root prescribed CE equals CE(q,R)+L_root=weighted source CE+L_root. The single original target is weighted source CE+J_root+L_root. The signed reset increment after actual erasure/outcome refunds consumes at most the one J_root, minus source contractions and terminal Z. This full equality counts J once, rather than adding the v6 entropy payment to a separately priced reset. Querying all controls and stopping before any data makes A identically zero and terminal Z zero, hence the net reset bound J_root is sharp (whenever J_root>0).

Conditional influence consequence: if supplied source references satisfy CE_g<=L_g I(G), CE_h<=L_h I(H), and the v5 root surcharge premise Pi_root<=M gamma I(a)+(V/2)I(GH) holds, then the complete expected signed entropy path plus terminal profile CE is at most max{M,L_g+2p,L_h+2(1-p)} I(f). Indeed I(f)=gamma I(a)+(1-p)I(G)+pI(H), I(GH)<=I(G)+I(H), and V/2=2p(1-p). In the v5 controller class M=K+3log2(e). This invocation remains conditional on that scoped v5 premise and the actual source CE suppliers; the present KL transport theorem itself is unconditional.
