# Output-conditional transcript repair of the existing scalar tax

All entropies are in bits. Physical influence under a product law is the unweighted pivotal probability, not biased Fourier expected cardinality. Theorem scope: finite deterministic physical singleton stopping trees, a fixed actual Boolean sign f under independent interior input probabilities, inherited probabilities at each node. Only unqueried coordinates may be queried. Full FEI remains open.

## 1. An unconditional bound sufficient for the path repair

Write r=min(p,1-p), beta=arcsin(sqrt(r)), F_p(t)=h2(sin^2 t)+h2(sin^2(t-beta)), and tau*(p)=h2(p)-min_t F_p(t). First swap children for p>1/2; never change the angle without that swap in the actual pair identity. The angular definition itself is symmetric.

For any normalized two-vector v and its image under the real rotation by beta, let u,w be the smaller entry probabilities in the two bases. Choose the maximal-probability basis vector in each basis. Their overlap modulus is at most sqrt(1-r). The largest eigenvalue of the sum of their rank-one projectors is 1+the overlap modulus (diagonalize their two-dimensional span). Thus (1-u)+(1-w)<=1+sqrt(1-r), giving u+w>=delta=1-sqrt(1-r).

Here 0<=u,w<=1/2 and 0<=delta<=1-1/sqrt(2)<1/2. If either u or w is at least delta, the binary entropy sum is >=h2(delta). Otherwise w>=delta-u; monotonicity and concavity imply h2(u)+h2(w)>=h2(u)+h2(delta-u)>=h2(delta), the last minimum being at an endpoint of [0,delta]. Since delta>=r/2, monotonicity and concavity give h2(delta)>=h2(r/2)>=h2(r)/2. Therefore

    0<=tau*(p)<=h2(p)/2.                              (1)

Nonnegativity follows by evaluating F at a basis vector, for which F=h2(p). This proof is self-contained and needs neither the lead's middle-region interval certificate nor multi-bit optimal-uncertainty additivity. A096/A090's earlier projector argument is credited; the extra half-entropy consequence is reconstructed here for its path payment use. It is weaker than tau*<=Delta/2, which remains separately scoped as the lead's computer-assisted claim.

Evaluate the angular sum at t=beta/2. For p<=1/2 set s=(1-sqrt(1-p))/2. Then

    tau*(p)>=h2(p)-2h2(s),  s=p/4+O(p^2).

Using h2(p)=p log2(1/p)+O(p), this and (1) prove tau*(p)/h2(p)->1/2 as p->0. No exact minimizer or Boolean attainment is needed.

At p=1/2, tau*=0. Indeed h2(x)>=4x(1-x): expand h2((1+z)/2)=1-sum_{k>=1} z^(2k)/[ln(2)*2k(2k-1)], whose positive coefficients sum to one at z=1. Since z^(2k)<=z^2, the lower bound follows. The two probabilities sin^2 t,sin^2(t-pi/4) give lower bounds summing to sin^2(2t)+cos^2(2t)=1, attained at a basis vector.

## 2. One conserved output-entropy account

Let Y=f(X) be the actual physical output, Pi the entire stopped transcript including coordinate choices, and w_v the node reach probability. Choices and stopping are deterministic functions of past outcomes, so no unrecorded choice entropy occurs. At queried node v let p_i be the inherited product bias, and define

    c_v=H(X_i | Y, history=v),
    j_v=I(X_i;Y | history=v)=h2(p_i)-c_v,
    ell_v=h2(p_i)/2-tau*(p_i)>=0.

All three quantities use the ordinary physical product experiment, not the function-specific spectral lift. The chain rules for a finite variable-length transcript give

    H(Pi)=sum_v w_v h2(p_i),
    H(Pi|Y)=sum_v w_v c_v,
    I(Pi;Y)=sum_v w_v j_v.

The exact local tax remainder is

    tau*(p_i)-c_v/2=j_v/2-ell_v.                     (2)

Consequently its positive part is <=j_v/2. The reserve R_v=H(Y|history=v)/2 has drift R_v-E[R_child|v]=j_v/2. Summing on the same physical tree, including the terminal reserve, proves

    sum_v w_v [tau*(p_i)-c_v/2]_+
       <=(H(Y)-E H(Y|Pi))/2=I(Pi;Y)/2.               (3)

It also gives the signed bill inequality

    A_T-(1/2)H(Pi|Y)<=I(Pi;Y)/2,
    A_T=sum_v w_v tau*(p_i).                         (4)

This is a payment after a declared output-conditional transcript refund, not a proof that an external spectral reference supplies that refund. It applies to non-computing stopping trees; E H(Y|Pi) must then remain. A randomized policy can be handled conditional on an independent recorded seed, but this stage's theorem and validation are deterministic.

## 3. Root reserve is bounded by actual physical influence

For a fixed coordinate order, H(Y)=I(Y;X)=sum_i I(Y;X_i|X_<i). Adding the later coordinates to the first argument increases mutual information. Independence gives

    I(Y;X_i|X_<i)<=I(Y,X_>i;X_i|X_<i)
                       =I(Y;X_i|X_-i)=H(Y|X_-i).

On a fixed other-coordinate fiber f is either constant or a nonconstant Boolean function of X_i. Its output entropy is respectively zero or h2(p_i). Hence

    H(Y)<=sum_i h2(p_i) Inf_i^phys(f)<=I_phys(f).

Together with (3)-(4), this proves the unconditional scoped repair

    sum_v w_v [tau*(p_i)-c_v/2]_+<=I_phys(f)/2,
    A_T<=I_phys(f)/2+H(Pi|Y)/2.                      (5)

The influence comparison is at the original product law; it is not a comparison with biased spectral energy. For each coordinate the physical pivotal probabilities average under restriction, so ordinary physical influence also has its usual same-tree removal identity. The output account in (3) is sharper than merely restarting a root influence bound at every node.

## 4. The refund coefficient 1/2 is optimal in this bank family

Consider claims of the form A_T<=C I_phys(f)+lambda H(Pi|f), universally over all Boolean functions, independent interior biases and essential exact computing singleton trees, for fixed finite C and nonnegative lambda. Formula (5) proves the claim with lambda=1/2 and C=1/2. If lambda<1/2, the limit in section 1 allows a fixed q in (0,1/2) with tau*(q)>lambda h2(q). Take an r-bit q-biased point defect f_r=1-2 product X_i. Every essential computing policy short-circuits along the all-one path; any ordering has

    E queries=(1-q^r)/(1-q),
    A_T=tau*(q)(1-q^r)/(1-q),
    H(Pi)=h2(q)(1-q^r)/(1-q),
    H(Pi|f_r)=H(Pi)-h2(q^r),
    I_phys(f_r)=r q^(r-1).

Thus A_T-lambda H(Pi|f_r) tends to the strictly positive constant [tau*(q)-lambda h2(q)]/(1-q), whereas influence tends to zero. No finite C works. The weakest coefficient in this explicit ordered scalar-bank family is therefore exactly 1/2. This is not a globally weakest repair among all possible structural hypotheses or compatible references.

This family and the failure of tax payment without a refund are prior A048 results; this stage contributes the all-tree positive-part payment and the exact threshold coefficient for the proposed conditional-output history bank. No new FEI counterfamily is claimed.

## 5. The exact C019 remainder after spending the output account once

For an actual singleton pair at v, write M_v for parent queried spectral-label conditional entropy and J_v for physical-child/spectral mixture information. The exact two-basis calculation gives E_v=J_v-M_v<=tau*(p_i). Define the actual nonnegative uncertainty defect D_v=tau*(p_i)-E_v. Then L_v=2M_v+tau*(p_i)-D_v. Let M_T=sum_v w_v M_v and S_T=sum_v w_v(ell_v+D_v). Physical entropy telescoping and (2) yield the identity

    H_hat(f)=E H_hat(f_leaf)+2M_T+(1/2)H(Pi|Y)
                                  +(1/2)I(Pi;Y)-S_T.          (6)

All histories, posterior entropies and defects refer to this same physical tree. Thus only I(Pi;Y)/2 is now influence-paid. The remaining exact signed target is

    2M_T+(1/2)H(Pi|Y)-S_T+E H_hat(f_leaf).             (7)

No bound on (7) is proved. The terminal Fourier entropy is separate from terminal output entropy in (3). They cannot be interchanged: a balanced high-entropy Boolean leaf has output entropy one but potentially much larger Fourier entropy. At uniform physical biases tau*=0, so ell_v=1/2 and the transcript term cancels its matching ell sum exactly; one obtains the original unbiased C019 ledger, with no fictitious positive tax.

For exact finite checking it is unnecessary to optimize tau*. Set the surrogate tax bar_tau=h2(p)/2 and bar_D=bar_tau-(J-M)=ell+D>=0. Then (6) has exactly the same S_T=sum w bar_D, proving that the meaningful residual does not depend on the internal allocation between scalar tax slack and actual uncertainty defect. This avoids numerical optimization of a sharp tax and prevents charging its slack twice.

## 6. C024 compatibility is an additional hypothesis, not free credit

For a fair complete tree, A037's coherent spectral lift supplies a joint root Fourier set S0 and a transcript Pi with the correct physical transcript marginal, and I(S0;Pi)=sum w J_v. Attach Y as the actual Boolean value of the full physical transcript. The refund used in (5)-(6) is H(Pi|Y); a spectral witness ledger often instead contains H(Pi|S0). Their exact difference is

For completeness, reconstruct that lift: at a node with parent coefficient squares P(R union T), queried label R in {empty,{i}}, q_T=sum_R P(R union T), and child coefficient C_b(T), choose physical b from the kernel C_b(T)^2/(2q_T), then discard R. Summing R gives the joint probability C_b(T)^2/2; Boolean child Parseval gives physical marginal 1/2 and the actual normalized child spectrum. The kernel depends only on the retained T, so root removed labels are conditionally independent of the next outcome given T and history. Consequently the node's root-spectral information release is precisely J_v; chain rules give the asserted root-information identity. Zero-q fibers are unreachable. This is a self-contained reconstruction of A037's existing lift, not a new lift or a free output-bank compatibility theorem.

    H(Pi|Y)-H(Pi|S0)=I(S0;Pi)-I(Y;Pi).

There is no universally valid ordering. For the fair one-bit character f=(-1)^X, S0 is deterministic and Pi=Y, so H(Pi|Y)=0 but H(Pi|S0)=1. For the fair two-bit bent AND sign f=(-1)^(X1 X2), the forward essential computing tree has H(Pi)=3/2, H(Y)=h2(1/4), and J_tree=1. Thus H(Pi|Y)=3/2-h2(1/4)>1/2=H(Pi|S0), with a rigorously certified gap 1-h2(1/4)>0. These explicit controls forbid using one conditional entropy as an automatic substitute for the other.

The honest first unsupported line is an actual normalized common-space reference showing that the output-conditional refund in (5) is supplied once, with any side-information/channel reset correction retained, while also paying the signed erasure/uncertainty residual (7) and terminal Fourier entropy. Essential contraction and singleton optimality alone do not establish it.

## 7. Applications and operations

The tax refund theorem applies to every declared finite deterministic physical singleton tree under a product law, including adaptive choices, partial stopping, point defects, and overlapping-control functions. It is not limited to OI children. If two overlapping control events use the same physical bit, a single physical tree queries it once; (3) automatically has one output-information account. This gives the tax component's ownership, not a complete two-core spectral payment.

Common independent factors remain in the full actual output Y and in all terminal Fourier entropies; replacing Y by a factor's output is a different bank requiring its own declared conditioning. Disjoint processing gives additive factorwise versions with separate factor outputs and separate terminal costs, provided the banks correspond to actual independent factors. Collapsed logical masks are not physical coordinates: their influence must be converted to the original control budget. Neither (5) nor half-tax sharpness licenses ignoring that conversion.

Prior OI fair-selector repair remains valid and unchanged, but the current path-refund result does not assert OI survives arbitrary restriction. Blocks may be processed sequentially with inherited singleton costs; identifying the sum of those M_v with root-block M_A requires a separate transport proof. The sharp root-block sum tau* statement remains conditional on the lead's multi-bit optimal-uncertainty additivity premise; no block theorem is accepted here.
