# Independent joint-code reconstruction

A086, stage 3. All entropy, cross entropy and KL quantities use log base two. Cross entropy against a subprobability includes its missing-mass penalty. These are finite fixed references, not unproved termination claims. Integer word rounding is separate.

## A012-CONTROL-FIRST-POSTERIOR-REPAIR@1: HOLDS

Let g be any balanced Boolean core, r>=1, p=2^-r, and F=1+A_r(g-1), with independent controls and point event A_r. Expanding the point event gives squared masses (1-p)^2 at the vacuum, p^2 at each nonempty control-only set, and p^2 P_g(T) at every (U,T) with T nonempty. These sum to one. Replacing only P_g by the prescribed complete nonempty subprobability R gives mass 1-p+p sum R and cost

CE(P_F,Q)=p CE(P_g,R)+a_r,
a_r=2rp(2-p)-(1-p)^2 log2((1-p)^2).

The actual expectation uses P_F, including all 2^r control choices in every data fiber. Thus CE-H=p(CE_g-H_g), and I(F)=p(I(g)+r). Failure mass is exactly p(1-sum R). Successful draws specify unique physical subsets (U,T); distinct latent stopping witnesses for the same set are not transmitted. A decoder reads the fixed subset output, with a block prefix/arithmetic code approaching CE or a single Shannon word costing less than CE+1. This proof never removes that additive one from a single output word.

The selector coefficient c_r=a_r/(rp) is at most 4+2/(r ln2), using -(1-p)ln(1-p)<=p. Since ln2>2/3, r>=6 gives c_r<4.5. Our outward rational log certificates prove c_3>4.5, c_3>c_1,c_2,c_4,c_5 and 4.536<c_3<4.537. Substitution yields c_3=15/4+(49/12)log2(8/7). This finite certificate plus the analytic tail proves the unique maximum over ALL integers r. For exact core R=P_g, Gibbs' inequality CE>=H forces every activation transfer constant to be at least c_3; the displayed construction attains it. This is sharpness of this transfer, not of universal FEI.

We reconstruct the original physical witness, rather than inferring its law from Q. At a selector node, let u,v be the two actual child Fourier coefficients at a residual set T. Choose the physical child fairly, sample its actual residual witness, then include the selector with probability (u-v)^2/[2(u^2+v^2)]. The residual mixture probability is (u^2+v^2)/2, producing output probabilities (u+v)^2/4 and (u-v)^2/4. Zero residual packets are omitted, so every operation has finite support. This signed construction gives the true parent spectrum.

The retained witness is exactly W=(J,S): leaf data equals the data part of S, and the queried membership bits plus zeros on unqueried positions are determined by J and S. J stops at position j with mass 2^-j or reaches the core with mass p. Its entropy is D=2(1-p). For a k-control suffix the only non-fair residual packet is empty, with m_k=1-2^-(k-1), q_k=(1+m_k^2)/2, epsilon_k=(1-m_k)^2/[2(1+m_k^2)]. Its membership entropy contribution is B_k=q_k h2(epsilon_k)+(1-m_k^2)/2. Conditioning down the physical tree gives

H(W)=D+pH(g)+sum_k 2^(-(r-k)) B_k,
H(W|S)=D+sum_k 2^(-(r-k)) B_k-a_r.

Our implementation independently recurses that sampler and compares its entire rational joint law with A012's stopping-index closed formula, then compares its marginal with a truth-table FWHT. Repeated stopping witnesses are summed only for the output marginal, never counted twice in a success law. This verifies the posterior identity without subtracting a latent posterior from an actual transmitted word. Since H(W|S)=H(J|S)<=D and the nonnegative weighted B term gives H(W|S)>=D-a_r, its limit is two bits. The complete core bill persists in disjoint products and in fresh-character permutations; arbitrary shared controls are excluded. No substantive repair to the source is needed.

## A011-COMB-PHASE-REFERENCE-TRANSFER@1: HOLDS

For a scalar first-positive sign comb with a selectors and sign labels s_1,...,s_(a+1), let m_(a+1)=s_(a+1), m_j=(s_j+m_(j+1))/2, r_j=(1-s_j m_(j+1))/2. The coefficient at a nonempty selector set with maximum index j is 2^(1-j)s_j r_j (-1)^(|U|-1). There are 2^(j-1) such sets. Thus v_j=2^(1-j)r_j^2, V=sum v_j=1-m_1^2, and spectral influence is I=one half sum(j+1)v_j. Physical conditioning also gives I=sum 2^(1-j)r_j.

Writing L(t)=-t log2 t, exact entropy is
H=L(m_1^2)+sum_j v_j[2(j-1)+2log2(1/r_j)].
Use L(1-V)<=V/ln2<2V, sum 2(j-1)v_j=4I-4V, and r log2(1/r)<=1/(e ln2). Then
H<=[4+2/(e ln2)]I-2V<=C_* I.
Zero terms have continuous endpoint values. The elementary bounds e>8/3 and ln2>2/3 imply C_*<41/8. This proves every comb length; our scalar finite cases verify the stronger rational coefficient inequality H<=(41/8)I-2V.

For actual Boolean leaves with common entire squared spectrum P, each nonzero data row has labels s_j(T)=ghat_j(T)/sqrt(P(T)) in {-1,1}. By linearity, Fhat(U,T)=sqrt(P(T))*shat_T(U). Hence K_T(U)=shat_T(U)^2 is a normalized Boolean spectral row. Fixing Q(U,T)=R(T)K_T(U) gives mass sum R, cost c+sum P(T)H(K_T), and deficit CE-H=c-H(P). Reference mass on a zero true fiber uses a normalized empty-selector point kernel. True supported outputs therefore all have positive Q. No stopping label is charged or erased in this output reference. Each row's maximum-index/subset alternatives have already been summed into its spectral probabilities; decoding a physical subset needs no latent witness. The supplied core cost c, including its subprobability normalizer, remains once in the final expectation. I_data=sum |T|P(T), I_sel=sum P(T)I(s_T); the scalar lemma pays precisely that latter sum. The terminal leaf is included in the row labels and probabilities. The one-word rounding bill remains +1. Translates and sign changes of a core preserve squared coefficients, so are admitted even with total physical data overlap.

For unequal magnitudes, Parseval gives q(T)=sum_j w_j P_j(T). Given complete leaf subprobabilities R_j, put r(T)=sum_j w_j R_j(T), and Q=rK with actual conditional selector K. Define posterior k_P(j|T)=w_j P_j(T)/q(T), k_R(j|T)=w_j R_j(T)/r(T). Direct expansion of log ratios, including missing masses, gives
sum_j w_j KL(P_j||R_j)=KL(q||r)+kappa,
kappa=sum_T q(T) KL(k_P(.|T)||k_R(.|T)).
Subtracting the entropy identity H(q)=sum w H(P_j)+JS yields
CE(P_F,Q)=H(U|T)+sum_j w_j c_j+JS-kappa.

The sign of JS is positive. Our independent implementation checks actual Fourier coefficients, this identity, and the mass normalizer for arbitrary two-bit leaves and deficient reference mixtures. Common P and common R set JS=kappa=0, recovering the accepted theorem. The first unsupported generalization is applying the sign-comb lemma to ghat_j(T)/sqrt(q(T)) when these labels have varying magnitudes: those rows are real, not Boolean. No source repair was necessary. The extension to arbitrary such rows, with a nonreused payment reserve and full terminal cost, remains open.

## Disjoint-child prescribed-reference interface (author proof; independent review pending)

Let G(X),H(Y) be arbitrary Boolean signs on disjoint uniform blocks, and z a fresh selector. Set F=(G+H)/2+z(G-H)/2, mu=EG, nu=EH, and d=I_z(F)=(1-mu nu)/2. Given normalized complete finite-cost references R_G,R_H, calibrate their empty atom to mu^2,nu^2 respectively, multiplying each nonempty sector by (1-mu^2)/(1-R_G(empty)) or its H analogue. For a constant child use the empty point reference. Write the results R_G^0,R_H^0 and costs c_G^0,c_H^0. The cross-entropy decrease is the binary KL divergence between the true empty/nonempty masses and the original reference sector masses, so c_j^0<=c_j. All endpoint cases are covered by finite-cost support positivity.

Embed each reference in its physical data block, form r=(R_G^0+R_H^0)/2, and use the actual conditional selector kernel K at its data set. At zero true data fibers use the empty-selector point kernel. Q=rK has mass one and finite complete support. On every nonempty supported data set the child is uniquely identified because the blocks are disjoint. On the empty data set the child posterior under r agrees with the true posterior because both empty atoms were calibrated. Consequently kappa=0, including the zero-empty-variance limit, and

CE(P_F,Q)-H(F)=[KL(P_G||R_G^0)+KL(P_H||R_H^0)]/2,
CE(P_F,Q)=(c_G^0+c_H^0)/2+Delta_z,
Delta_z=H(F)-[H(G)+H(H)]/2=B_z+JS_z.

Here is an all-dimensional payment of Delta_z with no reference charge omitted. Every nonempty G or H data packet has equal selector-sector masses P_G(T)/4 or P_H(T)/4, giving
B_nonempty=[(1-mu^2)+(1-nu^2)]/2<=2d.
The empty packet has masses A=(mu+nu)^2/4 and B=(mu-nu)^2/4. For nonnegative A,B, Shannon entropy of the normalized binary packet is at most its order-one-half Renyi entropy: Jensen applied to sqrt(1/p) gives H(p)<=2log2(sum sqrt p). Thus its unnormalized entropy is at most
(A+B)log2(1+2sqrt(AB)/(A+B))<=2 sqrt(AB)/ln2.
Since |mu-nu|<=1-mu nu (square difference (1-mu^2)(1-nu^2)>=0) and |mu+nu|<=2, sqrt(AB)=|mu^2-nu^2|/4<=d. Hence B_z<=2d+2d/ln2.

For completeness, the universal JS scalar estimate used here has its own proof. At a selector spectral packet u,v, let m=u^2+v^2 and t=2|uv|/m. The JS contribution is m D(t)/ln2, with D(t)=[(1+t)ln(1+t)+(1-t)ln(1-t)]/2. The function D(t) has derivative atanh(t), bounded by t/sqrt(1-t^2): their difference starts at zero and its derivative is (1-t^2)^(-3/2)-(1-t^2)^(-1)>=0. Integrating gives D(t)<=1-sqrt(1-t^2). Thus each contribution is <=2min(u^2,v^2)/ln2. Summing gives JS_z<=2d/ln2. Together,

Delta_z<=C_dis d, C_dis=2+4/ln2,
CE(P_F,Q)<=(c_G^0+c_H^0)/2+C_dis d.

Physical influence is I(F)=[I(G)+I(H)]/2+d. Conditional child bounds c_j<=K_j I(j) therefore transfer with constant max(K_G,K_H,C_dis). The exact deficit identity is stronger than the estimate: it specifies the retained conditional core debt rather than declaring it paid. This is a reference-interface extraction using standard disjoint composition, with no novelty claim. It makes no assertion for overlapping child data. In that case nonempty T no longer identifies a child, kappa may remain, and the nonempty conditional selector packets are not all fair. The next source-compatible test introduces one shared coordinate and changes one leaf magnitude; neither the common-magnitude theorem nor the disjoint theorem applies automatically.
