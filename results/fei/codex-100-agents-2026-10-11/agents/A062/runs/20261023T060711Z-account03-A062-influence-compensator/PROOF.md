# Blockwise sharp projection, exact physical closure, and the signed coupling obstruction

Information is in bits. Put a=log2(e)<3/2. Full FEI remains OPEN. This strengthens A062-SPARSE-SIGNED-REFERENCE-ENVELOPE@1; it prices an additional reference reserve, not the full terminal entropy or initial reference admission.

## 1. Static projection for arbitrary correlated sources

Partition physical coordinates into disjoint blocks V_1,...,V_b. Let p be ANY law on spectral subsets, p_j its block marginals, d_i=p(i in S), I=sum_i d_i, and q_j the product of these ACTUAL coordinate marginals in block j. Let R=product_j R_j be ONE normalized reference supporting p. For each block either TC(p_j)=0 or assume all its marginals are in (0,1), p_j(empty)>=q_j(empty), and

    R_j(S | S nonempty)=lambda_j^|S| q_j(S)/Z_j,
    0<lambda_j<=1,

with arbitrary supporting empty mass. Different blocks may use different lambda_j. Then

    TC(p)-KL(p||R)
       =sum_j [TC(p_j)-KL(p_j||R_j)] <= a I.            (1)

In particular the positive part is <=aI. Source blocks need NOT be independent. To verify the exact identity, write TC(p)=sum_i h2(d_i)-H(p), and KL(p||R)=-H(p)-sum_j E_(p_j) log2 R_j. The H(p) terms cancel. Each remaining block summand is TC(p_j)-KL(p_j||R_j). Thus all actual cross-block source correlation cancels, rather than being ignored or priced anew.

For completeness the one-block projection used here is reconstructed. Put u=p_j(empty), v=q_j(empty), P=p_j(.|nonempty), and Q_lambda proportional to lambda^rank q_j on nonempty sets. P's rank mean is I_j/(1-u). The finite exponential family satisfies

    d KL(P||Q_lambda)/d ln(lambda)
        =(E_Qlambda rank-I_j/(1-u))/ln2,
    d E_Qlambda rank/d ln(lambda)=Var_Qlambda(rank)>=0.

At lambda1 the rank mean is I_j/(1-v)<=I_j/(1-u). Therefore KL(P||Q_lambda)>=KL(P||Q1). Conditional KL chains, discarding only the nonnegative KL of the reference empty tilt, give

    TC(p_j)-KL(p_j||R_j)<=binaryKL(u||v).

Since u>=v, the binary term on nonemptiness is nonpositive; since u log2 u<=0,

    binaryKL(u||v)<=-u log2 v
       =sum_(i in V_j)u[-log2(1-d_i)]
       <=sum_(i in V_j)(1-d_i)[-log2(1-d_i)]<=a I_j.

The penultimate inequality uses the actual-source relation u<=1-d_i. The last follows from -(1-x)ln(1-x)<=x. All sums/differentiations are finite. The zero-TC blocks give TC-KL<=0 for any supporting reference, including deterministic marginal endpoints. Finally ln2=2(1/3+(1/3)^3/3+...)>2/3 proves a<3/2. No numerical continuum extrapolation occurs.

## 2. Exact reference closure under unequal point-core interleavings

Let F(x)=sigma product_j g_(n_j)(x_(V_j)), sigma in {-1,1}, disjoint blocks n_j>=2, where g_n=1-2*1[x=0]. Its spectrum factors exactly because Fourier amplitudes multiply on disjoint physical coordinates. Supply ONE original R=product_j R_j. Each R_j has arbitrary supporting empty mass r_j in (0,1) and conditional nonempty Bernoulli(delta_j)^n_j law with 0<delta_j<=d_(n_j)=2^(1-n_j). Delta and empty tilt may differ between blocks. This includes arbitrary finite numbers of unequal blocks, not just the enumerated pairs/triple.

For an active point core of remaining m, its actual law is p(empty)=(1-d_m)^2, p(S nonempty)=d_m^2. Its inherited reference has

    R(empty)=r, R(S nonempty)=c delta^|S|(1-delta)^(m-|S|),
    c=(1-r)/(1-(1-delta)^m).

For m>=2, erasing a queried bit gives the active physical kernel1 on nonempty spectators and

    alpha=(1-2d_m)^2/[2((1-d_m)^2+d_m^2)]

on the empty spectator. Write R0=r+c delta(1-delta)^(m-1). Its predicted active reach is pi=1-(1-alpha)R0>0, and the normalized active reference has r'=alpha R0/pi, c'=c/pi. Hence delta is unchanged. The other child is an actual constant with reference concentrated at empty. At m2, alpha0 makes the active child a dictator with zero empty source/reference mass; at m1 both children are constants. Constant coordinates can be omitted: their actual source and reference are concentrated at the empty indicator, every such physical query is fair with zero E,O,Inf and leaves the account unchanged.

Here tensor reference transport is PROVED, not assumed. For a query in block j, the erased source is p_j^-i times the product of the other source laws, and the actual positive-row physical kernel depends only on the queried block spectator. The erased reference factors in the same way. In this point-core invariant the reference and source have identical support at every history: full support for m>=2, the same singleton at m1, the same empty singleton after deactivation. Thus any global source-zero erased row also has zero erased reference mass. A fair zero-row convention cannot introduce a reference-only coupling. Normalizing therefore changes only R_j, exactly as above, and the other original reference factors stay untouched. This support argument is essential; arbitrary product references with extra mass on source-zero rows are not silently covered.

Every active m>=3 has p_j(empty)>=q_j(empty), and its local attenuation is

    lambda_j=[delta_j/(1-delta_j)]/[d_m/(1-d_m)]<=1.

At m<=2 TC=0 or the same projection applies. Thus (1) holds at every reached history under ANY adaptive physical interleaving, including unequal reveal depths, inactive cores, stopping and arbitrary remaining-coordinate permutations. No reference is reset during this transport.

The result strictly enlarges the old single-lambda interface. Start widths3,4 with the actual coordinate-product reference, and query a width3 coordinate, active outcome. Within the resulting width2 block, adding a second coordinate to a nonempty set changes R/q odds by1/3; adding an untouched width4 coordinate changes them by1. Both comparisons use nonempty sets and positive masses. A single global conditional nonempty tilt would require the SAME lambda for both ratios, impossible since1/3!=1. Local eligibility and factorization nevertheless remain exact.

## 3. Finite stopping account; original owner is never renewed

Use the normalized actual physical kernel and actual fair reaches. At every node the finite KL chain is

    K_parent=E_i+O_i+mean K_child,
    E_i=K_parent-KL(p^-i||R^-i)>=0,
    O_i=KL(fair||predicted physical reaches)>=0.

Influence conservation is I_parent=Inf_i+mean I_child. These established identities are used here, not claimed as new results. Put P=K+aI. Its exact drift is E_i+O_i+aInf_i. By (1), a terminal keeping R has target K<=P, and a terminal converting ONCE to its actual coordinate-product reference has target TC<=P. Conversion is terminal, with no post-conversion continuation asserted. Finite-tree summation gives

    E K_terminal + E sum O_i + a E sum Inf_i
          <=K_initial+a I_initial,                    (2)

where K_terminal is inherited KL or actual product KL according to the terminal choice. Add E H_terminal to BOTH sides for the full terminal cross entropy. It remains a separate explicit bill.

Equivalently the least pending reserve obeys

    B=max(0,TC-K,max_i(mean B_child-E_i))<=aI.           (3)

For point products, E_i and O_i are exactly those of the queried factor; all other original factors and old debits remain. Backward induction or (2) proves (3). The actual simultaneous-conversion obstacle is the positive part of the SUM of block signed obstacles, not a sum of their positive parts; replacing the latter by the former can save credit, never cost it. The validation computes this global Bellman recursion rather than simply checking a sum of local caps.

One ORIGINAL aI_initial reserve, or the rational cap3I_initial/2, is allocated once. Already spent unrelated omega stays spent. An existing pending theta for a nested policy class may be topped up only by cap-theta when admissible; no descent renews the owner. Independently randomized policies follow by conditioning. Fixed dimension has bounded depth. The separately conditional a.s.-finite unbounded-tree result of the previous proof also applies whenever nonnegative local P, drift, finite initial expectation and terminal domination are supplied: truncate at tau wedge N and use Fatou on accumulated costs plus terminal target (P_N on unstopped paths). No UI, varying-dimension limit or infinite-stopping event is silently assumed.

Sharpness is inherited constructively by taking just one block, delta=d_n and r=p_n(empty). Then TC-K=binaryKL((1-d_n)^2||(1-d_n)^n). Dividing by n d_n, the first term tends to a by a<=-log2(1-d_n)/d_n<=a/(1-d_n), and the other lies in [-2log2(n)/n,0]. Thus the reserve coefficient a cannot be reduced in this larger theorem either.

## 4. The exact signed term when reference factorization fails

For ANY supporting normalized R, let R_j be its actual block marginal laws; these are an ANALYTIC comparison, not an executed reset or a newly admitted reference. Always

    TC(p)-KL(p||R)
       =sum_j [TC(p_j)-KL(p_j||R_j)] + C_p(R),
    C_p(R)=E_p log2[R(S)/product_j R_j(S_j)].            (4)

Derive (4) by adding and subtracting E_p log2(product_j R_j); no assumptions on p's dependence are needed. All denominators are positive on source support. C_p(R) is signed, not a KL in general. It vanishes if R factors. If R=p, it equals the nonnegative actual block total correlation, which can be large relative to influence. A universal bound on C for arbitrary incoming R cannot be assumed.

If all local block projection hypotheses survive, (4) gives TC-K<=aI+C_p(R). If they fail, their local defects must ALSO be retained. Thus the first unpaid universal line is a hereditary payment for BOTH the new reference-coupling term and any local eligibility defect from the same unused original owner, net of actual E credits and all old debits. There is no proved such payment here.

The frozen one-point perturbations of disjoint point products are actual coupled Boolean guards. Their R is transported through the ACTUAL physical kernel with fair source-zero rows. Outputs retain the actual source, actual inherited R, complete H/K/TC, local signed obstacles and the exact coupling interval. There are positive and negative C rows. Consequently deleting the signed term, or replacing it by a nonnegative KL without a proof, is false. Some rows also lose local empty dominance/common attenuation; the report explicitly separates those defects and does not call them counterexamples to a fully eligible dependent-source theorem.

In particular flip the all-zero point of g2*g3. This actual5-bit function is -1 precisely when either block is all zero. Start the product of block references whose empty masses equal the actual block empty masses and whose conditional nonempty laws equal their actual marginal products conditioned nonempty (lambda1). This root is eligible. Query the first width3 coordinate, outcome0. The actual inherited-reference coupling exceeds20011/65536 bits, the global TC-K exceeds1/32 bit, while the sum of the two local signed TC-K terms is less than-1/4 bit. These strict rational inequalities are rechecked in code/extract.py and the full source/reference laws are in out/SELECTED_WITNESSES.json. The child fails some local reference eligibility as separately recorded; this is not a pure counterexample with every eligibility hypothesis preserved. A negative witness has coupling less than-1409/65536 bit, proving that this term is genuinely signed.

There is a FINITE positive payment beyond the invariant class. For each of the24 frozen coupled source/original-reference pairs, allow root inherited/product stop or one arbitrary physical coordinate query, then independent inherited/product stops in BOTH children. Write t=(TC-K), and use actual E_i. The exact original-owner requirement, INCLUDING the query's influence expenditure, is

    B1=max(0,t_root,max_i[a Inf_i+mean_b (t_child_b)_+-E_i]). (7)

Indeed actual O_i+mean K_child_i=K_root-E_i, so subtracting the separately retained K_root proves (7). The full H is retained by adding expected terminal H to both sides; it is not part of this new reserve payment. The finite outward certificates prove

    (3/4)a I_root-B1 > (39357/65536) I_root >0.         (8)

Thus the SAME original aI owner still pays after unrelated prior consumption omega<=aI/4, with neither renewal nor refund of that consumption. E is reconstructed from the proved KL chain and recorded actual K/O; its lower endpoint is clamped only by proved E>=0. Reciprocal enclosures of natural ln2 bound the actual coefficient a on BOTH sides, rather than charging a lower approximation. Equation (8) is certified only for the frozen finite cases; it does not prove an all-width coupled-family theorem. The universal hereditary coupling/local-defect payment remains the first unpaid line.

## 5. Scoped independent reconstruction of A061's affine pivot

A061 20261023T051706Z PROOF sections1-3 is reconstructed independently as a two-child marginal-entropy argument. For an arbitrary protected physical pivot v, let its actual Boolean children be f0,f1 on the other physical coordinates. Before v use K+M(f0)+M(f1), where M=sum h2(actual Inf). A query of another coordinate restricts BOTH child functions; for each child physical-edge averaging and entropy concavity make its M a supermartingale. Hence this potential pays actual O with no reference symmetry. At v allocate K_child+2M(child); its mean allocation equals the parent potential apart from actual E+O. After an actual product reset the continuation potential is TC(child)+M(child)=2M(child)-H(child), and the drop is K_child+H(child)>=0. Later K+M pays arbitrary physical continuation and a final conversion-and-stop. This reconstructs the claimed finite tree payment.

For A061's affine phase, f0=g and f1=chi_A g have identical H and M, so this is exactly its2M(g) allocation. Without affinity, the valid sum M(f0)+M(f1) may exceed2M(g); no influence price for that difference is provided. The actual guard F=(-1)^(v*y0*y1*y2), g=1, Q=p_F has zero initial K+2M(g) but positive expected immediate product-reset cost 1-(9/16)log2(3)>0, exactly because2^16>3^9. Thus the non-affine extension is indeed false. This review accepts the generic affine theorem at that scope; A061's separate field edge-count/source cap and its entire proof dependency bundle are not independently accepted by this review.
