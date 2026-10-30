# A096: source-bound gap ledger and sharp fixed-pair rare-bias coefficient

## exact target, quantifiers, hypotheses and units

Packet A096, B20. Full uniform-cube FEI remains OPEN. The nearest unpaid lemma selected is the sharp one-bit rare-bias tax in B09's section 8, with A046's AND lower-bound work treated as existing work rather than repeated. The final result is the dimension-uniform upper tax J_X-M_X<=h2(r)-h2(1-sqrt(1-r)), r=min(p,1-p), and the sharp universal rare-endpoint coefficient 1/2. Two complete local claims await independent review; no third candidate is opened.

Fix a finite residual cube with any fixed interior product measure, and two actual Boolean sign children G,H. A new independent selector X has Pr(X=1)=p, and F_p equals G at X=1 and H at X=0. All entropies are in bits and residual parameters and children are fixed as p tends to zero. Write a_T=hat G(T), b_T=hat H(T), c=E[GH], D={T:b_T !=0}, A=sum_{T in D}a_T^2. Let M_p=H(S_X|S_residual), and J_p=I(X;T) in the actual physical-child/spectral experiment. Then

    J_p-M_p = kappa(G,H) p log2(1/p) + O_{G,H,measure}(p),
    kappa = 2(c-A),
    -4 <= kappa <= 1/2,
    1/2-kappa = 2 ||P_D a-c b||_2^2 + 2(c-1/2)^2.

Consequently the supremum, over fixed actual finite Boolean child pairs, of the limiting normalized tax is exactly 1/2. Equality holds exactly when c=1/2 and P_D a=b/2. The example H=1 and G=(-1)^{y1 y2} on two uniform residual bits has c=a_empty=1/2 and realizes equality. Multiplying both children by any residual character gives nonconstant common-child examples as well. The claim is a fixed-pair endpoint theorem, not a dimension-uniform remainder bound or a full FEI theorem.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json was read in full, revision 2026-10-11-execution-v2. README.md, CURRENT_STATUS.md, CLAIM_REGISTRY.json, OBSTRUCTION_REGISTRY.json, PACKET_STATUS.json, STREAM_NEXT_ACTIONS.json and the campaign plan were read from the specified read-only tree. Supplemental campaign, claims, counterexamples, seed lemmas, mapping and source notes were ingested with exact SHA256 receipts in out/SOURCE_LEDGER.json. The board dated 2026-10-11 21:55 UTC was read. The requested claude/B20/STREAM_NOTES.md did not exist; no lead instruction was inferred.

Critical originals: B09 run 20261011T195500Z-fleet01-B09-biased-restriction-uncertainty REPORT.md sections 2-3 (exact biased transform), 5(4) (unsupported endpoint necessity inference), 8 (sharp singleton tax target); B05 run 20261011T193057Z-fleet01-B05-rare-restrictions sections 4-7 (local-refund no-go); B19 run 20261011T195038Z-fleet01-B19-independent-review sections 2-4 (independent reconstruction and scope). The B09 source pin is adb671ffcda143fa68347806bb96e8c305621a7d, B05 80cc2e5027efa56d79c4ecdf7d4949759ef2068b, B19 7955d427222392911dc6af2e4ee3aa8aab67ac8c. Local byte hashes, rather than unverified equivalence to repository commits, bind this intake.

threshold_paper_38pp.txt: Proposition 7.1 and Section 8/Proposition 8.1 establish the disjoint composition and orthogonal selector interfaces. Earlier 29-page version lacks the later selector scope. percolation_spectral_pivotal_entropy_30pp.txt introduction/Theorems 1.1-1.3 concerns geometric crossing classes and is not a universal Boolean premise. The other 31-page version has a weaker conditional overlap-exponent conclusion. Neither percolation manuscript is used in the proof here. Source hashes distinguish all four versions.

A046's complete report/claim supplies the already derived AND lower bound 4q(1-2q) and its coefficient-1/2 obstruction to O(p) universal taxes. This report contributes the upper coefficient, its exact projection formula and stability identity for all fixed child pairs. It does not claim the lower-bound witness as new.

## complete derivation or exact first unsupported line

Let r_{0,T}=((1-p)b_T+p a_T)^2 and r_{1,T}=p(1-p)(a_T-b_T)^2. These are the parent squared Fourier masses without and with the selector coordinate. Their sum is

    q_T=(1-p)b_T^2+p a_T^2.

The child's spectral channel has joint probabilities (1-p)b_T^2 and p a_T^2, so its output marginal is the same q_T. Parseval gives sum a_T^2=sum b_T^2=1. Therefore

    J_p=H(q)-(1-p)H(b^2)-p H(a^2),
    M_p=sum_T q_T h2(r_{1,T}/q_T).

The entropy summand e(t)=-t log2 t, extended by e(0)=0, is differentiable at each positive t. On D, q_T=b_T^2+O(p), so these terms of H(q) change by O(p). Outside D, q_T=p a_T^2 and exactly

    e(p a_T^2)=p a_T^2 log2(1/p)+p e(a_T^2).

Because the finite pair is fixed, summing yields

    J_p = (1-A) p log2(1/p) + O(p).                 (1)

For T in D with a_T != b_T, write t_T=(a_T-b_T)^2>0. Then r_{1,T}=p t_T+O(p^2), q_T=b_T^2+O(p), and

    q_T h2(r_{1,T}/q_T)
      = r_{1,T} log2(q_T/r_{1,T}) + O(r_{1,T})
      = p t_T log2(1/p)+O(p).

Here h2(u)=u log2(1/u)+O(u) as u decreases to zero. The O(p^2 log(1/p)) error is O(p). If a_T=b_T the conditional summand is identically zero. For T outside D with a_T !=0, the two parent masses are p^2 a_T^2 and p(1-p)a_T^2, so the conditional summand is p a_T^2 h2(p)=O(p^2 log(1/p))=O(p). Zero/zero fibers contribute zero. Thus

    M_p = sum_{T in D}(a_T-b_T)^2 p log2(1/p)+O(p). (2)

Subtract (2) from (1), and use sum_D b_T^2=1 and sum_D a_T b_T=c:

    kappa=1-A-(A+1-2c)=2(c-A).                    (3)

The vector b is unit and supported on D. Orthogonal projection yields

    ||P_D a-c b||^2=A-c^2 >=0.

Hence the exact identity

    1/2-kappa=2(A-c^2)+2(c-1/2)^2                 (4)

proves kappa<=1/2, with the claimed equality conditions. Since A<=1 and c>=-1, kappa>=-4; G=-H attains -4. For the upper equality witness, H=1 has only its empty coefficient and G has mean 1/2, so A=1/4,c=1/2. This proves sharpness within actual Boolean pairs.

Additional physical interpretation: d=Pr(G!=H) satisfies c=1-2d, so

    kappa=2(1-2d-A) <= 4d(1-2d).

A positive leading tax requires d<1/2. If kappa>=1/2-epsilon, equation (4) gives |c-1/2|<=sqrt(epsilon/2), |d-1/4|<=sqrt(epsilon/8), and ||P_D a-c b||<=sqrt(epsilon/2). Thus near-maximal leading tax demands physical disagreement near 1/4 and a nearly proportional common-support projection.

At this point the fixed-pair mechanism alone leaves unsupported the exchange

    limsup_{p->0} sup_{dimension, residual biases, G,H}
        (J_p-M_p)/(p log2(1/p)) <= 1/2.

The fixed-pair expansions give no dimension-uniform O(p) remainder. Children and residual biases changing with p can move formerly positive b_T^2 toward zero at the same scale. The following independent two-dimensional uncertainty argument resolves the leading-coefficient exchange without relying on those remainders.

### Uniform singleton tax: the remaining leading-coefficient gap closes

For every finite actual Boolean sign under arbitrary interior product biases and a singleton physical block with bias p, put r=min(p,1-p), delta=1-sqrt(1-r). Then

    J_X-M_X <= tau(r):=h2(r)-h2(delta).             (5)

This holds uniformly in the residual dimension, residual biases and the Boolean function. The displayed tax is positive at r=1/2 and is not claimed sharp there. One may use min{Delta(r),tau(r)}, where Delta(r)=h2(r)+log2(1-r) is B09's existing tax, if its pending theorem is accepted. Our independent result (5) alone is enough for the rare endpoint.

Proof of the needed two-dimensional inequality: let v be any unit real or complex vector in C^2 and U=[[sqrt(1-r),-sqrt(r)],[sqrt(r),sqrt(1-r)]]. Define u=min(|v_0|^2,|v_1|^2) and w=min(|(Uv)_0|^2,|(Uv)_1|^2). Choose the basis vector e which gives the larger entry of v, and the row-basis vector k which gives the larger entry of Uv. Their overlap has magnitude either sqrt(r) or sqrt(1-r), hence at most sqrt(1-r). The sum of their rank-one orthogonal projectors has largest eigenvalue 1+|<e,k>| (diagonalize the span of e,k). Thus

    (1-u)+(1-w) <= 1+sqrt(1-r),
    u+w >= delta.                                 (6)

Here u,w are in [0,1/2] and delta is in [0,1-1/sqrt(2)] subset [0,1/2]. If either u or w is at least delta, monotonicity of h2 on [0,1/2] gives h2(u)+h2(w)>=h2(delta). Otherwise w>=delta-u, so monotonicity and the concavity of h2 give

    h2(u)+h2(w) >= h2(u)+h2(delta-u) >= h2(delta).

The final inequality follows because the concave function h2(s)+h2(delta-s), s in [0,delta], attains its minimum at an endpoint. Therefore

    H(|v|^2)+H(|Uv|^2) >= h2(delta).               (7)

For the actual Boolean function, normalize each residual spectral fiber of the parent by its marginal q_T. The spectral vector (coefficients without/with X) and the posterior physical vector (sqrt(1-p)hat H(T),sqrt(p)hat G(T)) are related by U, up to row/column signs or swaps. Each squared fiber entropy is respectively H(S_X|T) and H(X|T). Averaging (7) yields

    M_X+H(X|T)>=h2(delta),
    J_X=H(X)-H(X|T)<=h2(r)-h2(delta)-M_X.

This proves (5), with zero fibers omitted. It reconstructs the singleton transform and does not use the pending B09 uncertainty theorem. At exactly r=1/2 the stronger direct fact H(|v|^2)+H(|Uv|^2)>=1 is the usual mutually unbiased two-dimensional entropy inequality; we do not independently reprove that sharper endpoint in this run and do not need it for (5).

Since delta=r/2+O(r^2), elementary binary-entropy expansion gives

    tau(r) = (r/2)log2(1/r) + ((log2(e)-1)/2)r
             + O(r^2 log(1/r)).                    (8)

The scalar upper tax in (5) is uniform. The actual H=1, E G=1/2 witness from the fixed-pair theorem gives the matching lower coefficient. Consequently

    lim_{p->0} sup_{all finite actual Boolean signs,
                  all interior residual product biases}
       (J_X-M_X)/(p log2(1/p)) = 1/2.              (9)

The upper bound follows from (5)-(8) before taking the supremum, and the lower bound from one fixed actual Boolean pair. This closes the leading-coefficient exchange that the earlier fixed-pair mechanism could not justify. The first remaining unsupported line is a nonreusing physical influence/composition payment of M_X plus this tax, or an exact all-p optimal tax; neither is proved here.

## executed validation with domain, arithmetic, commands and outputs

The frozen spec precedes execution in FROZEN_SPEC.json. Command: python -X utf8 runs/20261011T215017Z-fleet05-A096-live-gap-ledger/code/check_endpoint.py. All 276 ordered pairs on n=0,1,2 were checked without symmetry reduction, using integer Walsh transforms and Fraction arithmetic. At p=1/8 and p=1/32, 552 complete parent mass checks verified normalization, nonnegativity and the physical-child marginal identity. Exact projection coefficient, physical Hamming-distance formula, the 1/2 bound and equality cases were checked. Result: 6,758 assertions passed, zero failed; observed checker runtime 0.0707044 seconds. out/ENDPOINT_CHECK.json is the exact output. No floating entropy comparison is used as proof. Equations (1)-(4) provide the all-dimensional fixed-pair theorem.

For the second mechanism, FROZEN_UNCERTAINTY_SPEC.json was saved before executing python -X utf8 runs/20261011T215017Z-fleet05-A096-live-gap-ledger/code/check_uncertainty.py. Thirty-nine rational unit-vector/rotation cases checked (6), with Fraction arithmetic and no logarithmic numerical claims. Result: 81 assertions passed, zero failed; runtime 0.0014934 seconds. out/UNCERTAINTY_CHECK.json stores the rational cases. Combined total: 6,839 exact assertions. The analytic projection and concavity argument (5)-(9) establishes the uniform result.

## proof dependencies and changed downstream conclusions

The proof reconstructs the biased transform and chain-rule definitions directly and uses only finite Parseval, an elementary scalar entropy expansion and orthogonal projection. It does not assume B09's pending Maassen-Uffink theorem or A046's pending claim. External proof dependencies are empty; A046 is an acknowledged parallel lower-bound source. The second claim records the first A096 claim as its versioned dependency for the matching lower endpoint coefficient; the uniform upper bound itself is independently reconstructed in (5)-(8).

The source-bound adoption delta in out/GAP_MAP.json covers canonical claims, every observed packet, local claim versions, exact original report hashes, completion caveats, objections and intended consumers. Shared indices and other agents' folders remain read-only. Four-file presence is recorded as a completeness signal, never as mathematical acceptance. Pending local author claims retain their review status. The reviewed B05 no-go blocks only its universal all-coordinate fixed-price helper; existential coordinate/block choice and nonlocal transport remain open. B09's O(p)-impossibility claim is repairable by A046's proof, but the source upper-tax asymptotic alone was not evidence. Exact aligned tensor additivity is distinct from arbitrary composition. The second new A096 claim now proves a dimension-uniform singleton upper tax and settles the optimal leading coefficient, closing A046's section 'one next mathematical action' at the endpoint level.

## one next mathematical action and independent reviewer

Next mathematical action: transport the sharper uniform singleton tax through an actual restriction/composition ledger without reusing influence; retain the actual conditional cost M_X and terminal entropy. Independent reviewer: A087 for the asymptotic and both projection reconstructions; A094 for quantifier scope and dependency audit. Intended consumers: A042, A046, A050, A057, A084 and B09/B10/B20 leads. A046's AND necessity work should be adopted rather than rerun.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, frozen spec, code, exact checker output, SOURCE_LEDGER.json and GAP_MAP.json are saved inside the assigned run. out/PERSISTENCE_RECEIPT.json records their SHA256 hashes and schema checks after writing. STATUS.md is exactly two lines; WORKLOG.md and LEARNED.md carry the durable result and remaining gap. No repository or Brain write, mirror verification, independent acceptance or downstream use is claimed. Supervisor copying remains outstanding.
