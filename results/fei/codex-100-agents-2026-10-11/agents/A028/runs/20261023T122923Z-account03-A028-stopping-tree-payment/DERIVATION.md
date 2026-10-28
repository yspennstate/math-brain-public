# v9: admissible conditional Markov references

All entropy, CE and KL are in bits. All restrictions are physical coordinates of a finite uniform cube. The complete path cost is DeltaH=H(parent)-average H(children)=B_i+JS_i>=B_i>=0. Source references and old debits are retained, not issued again at a descendant.

## 1. General finite-label reference theorem

Let L(Y) take finitely many labels j, independent of the shared data block X, and f(y,x)=g_{L(y)}(x) for arbitrary Boolean g_j. At each physical history let pi_j=Pr(L=j), P_j(t)=ghat_j(t)^2, and retain normalized R_j positive on the true P_j support. Inherit each R_j through its OWN actual source's physical phase-sensitive pair channel for DATA queries, including off-target mass and actual reference branch normalizers; CONTROL queries leave the source references fixed. Set

    q(t)=sum_j pi_j P_j(t), r(t)=sum_j pi_j R_j(t),
    W=sum_j pi_j D(P_j||R_j).

Parseval over Y gives the actual output Fourier marginal q on data sets: sum_U Pf(U,t)=E_Y[ghat_{L(Y)}(t)^2]=q(t). Let k(U|t)=Pf(U,t)/q(t) on positive q. Define true and reference source-label posteriors

    alpha_j(t)=pi_j P_j(t)/q(t), rho_j(t)=pi_j R_j(t)/r(t).

Choose ANY stochastic kernel K_t(U|j), fixed by a declared history rule, satisfying sum_j alpha_j K_t(U|j)=k(U|t). Define ell(U|t)=sum_j rho_j K_t(U|j) and Q(U,t)=r(t)ell(U|t). On q=0 put the entire reference row r(t) at U=empty. This is a precisely delimited family of externally changed conditional references; constant-in-j K=k is the old true-profile reference, and nonconstant K can genuinely change the controller profile.

Apply KL chain rule to the true/reference joint laws alpha_j K(U|j), rho_j K(U|j). The kernel is the SAME in both laws, so

    D(alpha||rho)=D(k||ell)
       + sum_U k(U) D(alpha(j|U)||rho(j|U)).             (1)

Multiply by q(t), sum rows, and use W=D(q||r)+sum_t q D(alpha||rho). Thus

    D(Pf||Q)=D(q||r)+C, C=sum_t q D(k||ell),
    W-D(Pf||Q)=Z-C>=0, Z=sum_t q D(alpha||rho).          (2)

All posterior terms with zero true mass are omitted; source support positivity makes every true-supported reference denominator positive. Reference-only rows are never discarded. Identity(1) proves nonnegativity, not a floating search.

The physical source KL chain is Du_parent=Eu+Ou+average Du_child, where Eu is the pair-erasure loss and Ou=D(fair||actual reference outcome probabilities)>=0. Consequently W is a supermartingale under DATA (weighted sum of source E/O) and harmonic under CONTROL (pi is harmonic). With D=D(Pf||Q), S=W-D>=0 and A=W-average Wchild>=0, every finite adaptive mixed stopping tree, even when its admissible K rules change with history, satisfies

    sum reach*(average Dchild-Dparent)+sum reach*A
       + E_leaf S_leaf=S_root,
    sum reach*DeltaH+E_leaf CE(Pf,Q)
       =Hroot+Wroot-sum reach*A-E_leaf S <=Hroot+Wroot. (3)

Both full terminal CE/KL bills remain. Actual inherited OUTPUT references are obtained by the OUTPUT's own physical channel, not by replacing them with true profiles. If its actual refunds are Ef,Of, raw reconstruction kappa=average(D_target_child-D_inherited_child) equals sigma+Ef+Of, sigma=average Dchild-Dparent. Equation(3) charges sigma, retains the refunds, and is not a positive-part bound.

## 2. Binary sector changes on the already changed v8 profile

For binary mux f=(1-c)G+cH, keep the original v8 controller reference Ra and source references Rg,Rh. Let p=Ec, V=Var(a), gamma=Pr(G!=H), Da=D(Pa||Ra), beta=1-Ra(empty), B=Ra conditioned nonempty. Actual sector probability at data row t is b=w_t/q_t, w_t=V(Ghat-Hhat)^2/4. True/reference source-G posteriors are alpha=(1-p)Pg/q, rho=(1-p)Rg/r.

Choose binary kernel K(1|G)=u, K(1|H)=v with 0<=u,v<=1 and alpha*u+(1-alpha)*v=b. Its reference sector probability is ell=rho*u+(1-rho)*v. Prescribe Q(empty,t)=r(1-ell), Q(U!=empty,t)=r ell B(U). If beta=0, require ell=0; in the declared coupling rules b=0 implies u=v=0, so this condition is automatic. Zero true rows use the same empty-row completion. Then

    C=sum_t q D(Bern(b)||Bern(ell)) <= Zdata,
    D9=D8+C,
    T=Wdata+gamma Da  (EXACTLY the original v8 account),
    S9=Zdata-C+gamma Cvac>=0,
    Cvac=D(Bern(V)||Bern(beta)), D9=T-S9.              (4)

The T supermartingale and its exact source/controller E/O releases are unchanged from v8. Therefore(3) holds with W replaced by T and S by S9. The same old influence-rate corollary, if genuine initial CE suppliers and the v5 surcharge premise are supplied, has NO extra constant, depth factor or renewed JS/controller liability. Root common source reference plus controller calibration gives S9root=Jroot-Croot. A prior true-odds v8 node has C=0; switching AFTER a DATA query consumes existing conditional-label slack. Later queries transport CURRENT Q9, and each subsequent admissible switch is paid by this same signed identity. No free return to true odds is assumed.

Original admission stays U-old_debit>=Hroot+Troot. Remaining credit at any frontier is exactly U-old_debit-Hroot-Troot+sum prior reach*A+E S9. The controller root liability gamma Da from v8 is still real and is never erased by the new row payment.

## 3. Exact admissibility and constructive genuine changes

For 0<alpha<1, write tau=alpha*u. Then

    max(0,alpha+b-1)<=tau<=min(alpha,b),
    u=tau/alpha, v=(b-tau)/(1-alpha).

Every such tau is valid. The reachable ell interval is the image of this closed interval under rho*tau/alpha+(1-rho)*(b-tau)/(1-alpha); it suffices to take the min/max of its endpoint values. If alpha=0, v=b and u is free in[0,1]; if alpha=1, u=b and v is free. The tests set unused-input u/v to0, and use tau=max(0,alpha+b-1) or min(alpha,b), plus old constant kernel u=v=b. This exact linear feasibility condition is stronger than merely announcing a KL budget. In particular alpha=rho implies ell=b for EVERY admissible kernel.

For general finite labels and output sets, a deterministic quantile coupling between distributions alpha and k supplies a rational joint h(j,U) with these marginals. Set K(U|j)=h(j,U)/alpha_j on positive alpha_j and K=k on zero alpha_j. This constructs admissible references in every finite dimension; it is not a universal initial entropy-price supplier.

## 4. Exact row-odds obstruction and the first unsupported line

Let a on two controls be -1 only at00, G(z,d)=z, H(z,d)=-z. Use exact source references Rg=Rh=Pg=Ph and exact controller reference Ra=Pa=(1/4,1/4,1/4,1/4). Then f=a*z has H=I=2, Wdata=Da=T=Z=0, alpha=rho=3/4 at its unique nonzero data row, and b=3/4. Query dummy DATA d: entropy drop0 and both full source children remain nonconstant. A prescribed target ell=1/2, retaining TRUE nonempty shape B=(1/3,1/3,1/3), costs

    D(Bern(3/4)||Bern(1/2))=(3/4)log2(3)-1
       =(1/4)log2(27/16)>0.

It lies outside the admissible interval {3/4} and exceeds the tight old quota2. This is different from v8's shape-only excess (2-log2(3))/4: here ONLY binary row odds change, with shape and original controller reference unchanged. The integer27>16 is a strict certificate. Dummy padding preserves the witness with H/I=1. Neither reference-payment obstruction is a FEI counterexample.

The first unsupported universal line is an influence-priced initial reference supplier for every Boolean input, or funding a necessary external target OUTSIDE the admissible posterior-channel image from genuinely unused original capacity. A fixed-quota reset theorem or abstract conservation identity alone does not supply that price.

## 5. Physical channel and original-account proof, without a reset premise

For any real Boolean Fourier coefficients hhat(T)=s, hhat(T+i)=t, restriction xi=b gives child coefficient s+(-1)^b t. Put v_T=s^2+t^2. The channel from EITHER member of this input pair to (b,T) is (s+(-1)^b t)^2/(2v_T). If v_T=0 take the two branch probabilities to be 1/2. This channel is stochastic. Applied to true P it gives joint law Pchild_b(T)/2. Applied to a normalized reference R it gives a joint law with branch masses rho_b; divide each branch by its OWN rho_b to obtain Rchild_b. Support positivity ensures rho_b>0. Chain rule and data processing give

    D(P||R)=E+O+(D(Pchild_0||Rchild_0)+D(Pchild_1||Rchild_1))/2,
    E>=0, O=D((1/2,1/2)||(rho_0,rho_1))>=0.

The true branch law is fair because each restricted Boolean function has squared Fourier mass 1. The erased-pair conditional KL is E. No child reference is silently normalized by 1/2.

For binary output write z_t=(1-p)Ghat_t+p Hhat_t and d_t=(Ghat_t-Hhat_t)/2. Its empty-controller coefficient is z_t, and each nonempty controller coefficient is ahat(U)d_t (up to an irrelevant sign). Hence q_t=z_t^2+V d_t^2 and w_t=V d_t^2. Moreover sum_t d_t^2=Pr(G!=H)=gamma by Parseval. The actual nonempty controller shape is A=Pa conditioned nonempty, independent of t. The v8 reference has the true sector probability b_t and reference shape B. Chain rule therefore gives

    D8=D(q||r)+gamma V D(A||B),
    Da=Cvac+V D(A||B),
    T-D8=Wdata-D(q||r)+gamma Cvac=Zdata+gamma Cvac.

Changing only b_t to ell_t adds exactly sum q_t D(Bern(b_t)||Bern(ell_t)); this proves (4), including its compatibility with the already changed shape B. DATA restrictions keep Da fixed while gamma is harmonic; source KLs lose their own E/O amounts. CONTROL restrictions keep gamma and source references fixed, make pi harmonic, and contract Da by its controller E/O. Thus T-E Tchild is nonnegative on both kinds of physical query, even after arbitrary earlier admissible changes. Applying the OUTPUT channel above to CURRENT Q proves the stated raw-reset/refund identity directly.

Finally, entropy accounting uses no terminal relaxation: along any finite binary physical tree the sum of reach-weighted Hparent-average Hchildren equals Hroot-E Hleaf. Adding each leaf's full CE=Hleaf+Dleaf gives Hroot+E Dleaf. Substitute Dleaf=Tleaf-Sleaf and telescope T. This proves (3) and its binary extension for every finite adaptive stopping rule, including rules that stop in recovered regular, bounded-overlap or threshold-formula classes. To conclude a constant times root influence one must additionally prove the original admission Hroot+Troot+old_debit<=C Iroot; this stage does not assert that missing universal admission.
