# Compatible calibrated references are closed under physical Bayes transport

All costs are bits. W,S,X,Y are independent uniform coordinate blocks. Let c(W) be a Boolean indicator and G(S,X),H(S,Y) Boolean signs. Set F=cG+(1-c)H, p=Ec. Supply normalized positive-support seed references on each branch's remaining data cube. Calibrate EACH shared-only Fourier atom to its true squared coefficient, rescaling the complement to its true total mass; denote the resulting references R_G,R_H. Constants and empty blocks are included.

## 1. Specify the off-support completion before querying

For a data set T, let g_T,h_T be embedded branch coefficients. If T is shared-only, define Q(U,T)=Fhat(U,T)^2 for every controller subset U. If T contains private X coordinates (and no Y coordinates), define

    Q(U,T)=chat(U)^2 R_G(T).

For private Y sets define Q(U,T)=(1-c)hat(U)^2 R_H(T). All other sets have zero mass. This is the mixture-compatible root reference of stage4 on true support. On a zero-probability exclusive branch fiber, use the SAME branch controller law, rather than assigning all reference mass to U=empty. Shared-only zero-probability fibers have zero reference mass by calibration. Thus the completion is fully specified once, before sampling or querying.

Normalization follows from sum_U chat(U)^2=p and sum_U (1-c)hat(U)^2=1-p, together with exact shared-only root masses. On shared-only sets Q=P_F; on exclusive branch sets Q/P_F=R_j/P_j whenever the true mass is nonzero. Hence

    D(P_F||Q)=p D(P_G||R_G)+(1-p)D(P_H||R_H).             (A)

Changing the zero-fiber completion changes neither this KL nor CE(P_F,Q), but it does change possible future physical reference projections. This is a scope refinement, not a refutation of stage4's local cost identities.

## 2. Physical Bayes projection and inherited reference

Fix any physical query i. For residual Fourier set A write a_A=Fhat(A), b_A=Fhat(A+i), q_A=a_A^2+b_A^2. The true child probability is P_sigma(A)=(a_A+sigma b_A)^2, sigma=+/-1; the joint law is P_sigma/2. For q_A>0 set

    K(sigma|A)=P_sigma(A)/(2q_A).

Apply K to Q_marg(A)=Q(A)+Q(A+i), obtaining a normalized joint reference L(sigma,A)=Q_marg(A)K(sigma|A). Let z_sigma=sum_A L(sigma,A)>0 and Qbar_sigma=L(sigma,.)/z_sigma. For q_A=0 choose the structural kernel below. Positive support ensures z_sigma>0 because each true child is a normalized Boolean spectrum.

At exclusive branch residual sets, a data query uses that branch's actual physical coherence kernel, with the fair extension if its coefficient pair is zero. A controller query uses its indicator's coherence kernel: for branch G use (chat(A_W)+sigma chat(A_W+i))^2/[2(chat(A_W)^2+chat(A_W+i)^2)], similarly 1-c for H. If that denominator is zero the reference fiber is also zero, so extend fairly. This controller rule applies EVEN WHEN the branch data coefficient is zero. At residual sets becoming shared-only, any normalized zero-fiber extension suffices, since those atoms will be calibrated individually below. Residual sets with both private blocks have zero reference mass.

The usual exact KL disintegration gives

    D(P_F||Q)=E_i+O_i+(1/2)sum_sigma D(P_sigma||Qbar_sigma), (B)

where E_i=sum_A q_A D(P(S_i|A)||Q(S_i|A)) and O_i=D(fair||z). All terms are nonnegative. Formula (B) is the established physical Bayes ledger consumed from A039, not claimed as a new chain rule.

## 3. The rebuilt mux reference is a categorical calibration of Qbar

After fixing sigma, rebuild the SAME composition with the actual remaining blocks. For a data query transport each affected branch seed reference by its own actual coherence kernel and normalize at its reference outcome probability; an unaffected seed stays fixed. For a controller query keep both branch seed references fixed. Then calibrate every shared-only atom of the reached branch spectra, including those newly exposed by removal of a private coordinate. Build Qnew_sigma by Section1 with the actual restricted controller (so p_sigma may change).

Partition the reached root Fourier universe into the following cells: singleton (U,T) for every shared-only data T and controller U; one cell C_G containing all private-G data sets and all controller subsets; one cell C_H similarly; and a zero-true-mass remainder if needed. Set each singleton reference mass to P_sigma(U,T) and each exclusive-cell total to its true mass, preserving its internal reference conditional distribution. This is categorical calibration of Qbar_sigma.

We show it gives EXACTLY Qnew_sigma, including reference-only support:

* On shared-only singleton cells, both definitions are the actual child root spectrum.
* For a data query, on residual private-G sets the parent Fourier pair and reference pair factor as controller coefficient times branch coefficient/reference pair. Thus L(sigma,U,T)=chat(U)^2 L_G(sigma,T), where L_G is the branch's unnormalized physical reference joint. Dividing by z_sigma preserves this factorization. Calibrating the total cell to p V_G,sigma leaves conditional controller law chat(U)^2/p and the transported seed complement conditional law. Branch outcome normalization cancels within that complement. This is Qnew's exclusive-G formula. The H formula is identical, including an irrelevant private query, where its branch kernel is fair.
* For a controller query, the structural zero-fiber rule and actual kernel yield L(sigma,U,T)=chat_sigma(U)^2 R_G(T)/2 on exclusive-G sets, including zero actual data coefficients. Calibrating the cell total to p_sigma V_G gives precisely the rebuilt formula. The same holds for H.
* A cell of zero true mass is set to zero. If its true mass is positive its inherited reference mass is positive by support, so every division is legitimate. Endpoint p_sigma=0 or1 discards only the absent branch cell.

Therefore the calibration chain rule identifies the actual reset savings

    C_sigma=D(P_cells,sigma||Qbar_cells,sigma)>=0,
    D(P_sigma||Qbar_sigma)=C_sigma+D(P_sigma||Qnew_sigma).  (C)

Both terminal conditional debts are retained. This is not a free arbitrary product/occupancy reset: the two exclusive complement conditional laws MUST be transported from the owned references. A fresh conditional seed distribution could carry an additional KL conversion price.

## 4. Exact one-history reserve identity

Combining (A)-(C) yields the new source-compatible history identity

    D(P_F||Q)=E_i+O_i+(1/2)sum_sigma C_sigma
                  +(1/2)sum_sigma D(P_sigma||Qnew_sigma). (H)

The rebuilt references can be used at the next actual physical query. Every reached transcript is a product subcube; its partition and references satisfy the same construction. Hence for any finite adaptive stopping tree,

    D(P_root||Q_root)
      =sum_internal w_v [E_v+O_v+average_sigma C_v,sigma]
                      +E_leaf D(P_leaf||Qnew_leaf).      (T)

All weights are actual fair physical reach probabilities. One original KL bank pays its own released conditional, outcome and categorical calibration terms once; the remainder stays in actual terminal references. This closes the inherited-reference calibration compatibility gap for this composition family under arbitrary DATA/CONTROL interleaving, arbitrary current controller bias and any shared width. It does not pay the root entropy overhead of arbitrary shared profiles.

At a CONTROLLER query the statement is sharper: E_i=O_i=C_+=C_-=0. On shared data fibers P=Q, and on exclusive data fibers the reference/true ratio is constant across all controller subsets, so conditional erasure KL is zero. The unnormalized projected reference is P_child/2 on shared fibers and chat_child(U)^2 R_G(T)/2 (or the H formula) on exclusive fibers. Their total is exactly1/2 because the calibrated seed complements have their true masses. Thus reference outcome weights are fair, and each normalized child already is Qnew. Equivalently pD_G+(1-p)D_H is harmonic when only selector probabilities change. Reference calibration releases NO resource for the actual controller entropy decrement; its funding remains a distinct obligation.

## 5. Sharp limitation and the first unsupported line

The arbitrary empty-controller kernel at zero branch Fourier fibers from stage4 has the same root CE, but need not obey the factorization in Section3. Thus it does not justify (H) without specifying the completion. The code records an actual Boolean witness where direct sector calibration of that old physical projection differs from the rebuilt branch reference. The existing local stage4 theorem stays valid.

Explicit witness in binary truth-table order: c=(1,0), G=(1,-1,-1,1) on (s,x), H=(-1,-1,1,1) on (s,y), and uniform branch references calibrated at the two shared atoms. Query the ESSENTIAL shared s, whose actual root influence is 1/2. For the old empty-controller completion, initial KL is1, its physical erasure release is (1/2)log2(3), its reference outcome release is0 and its two child categorical savings are0. Each inherited child has probabilities 3/8 at the two selector-absent private branch atoms and1/8 at the two selector-present atoms. The rebuilt compatible reference has1/4 at all four atoms and is the true child spectrum. Remaining inherited KL is1-(1/2)log2(3)>0, since3<4. Thus categorical-only equality fails. This does not prove an unavoidable positive reset: an additional conditional-controller KL calibration could repair that old completion. Our theorem uses the branch-compatible completion from the start and needs no such additional repair.

The first unsupported universal line is paying the signed entropy/CE overhead of the compatible references, including the initial coherent collision excess, using a NONREUSED certified child/core surplus on one physical influence ledger. Identity (T) conserves reference KL; it does not establish a bound for H(P_root), initial seed costs, or the mixed shared-data entropy decrement. In particular the unbounded selector-only bent/point-flip obstruction is not removed, and unrelated product-projection reset no-go results of A038/A039 remain valid.
