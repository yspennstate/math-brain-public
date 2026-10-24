# A087 stage 2: NPN admission and coherent-child audit

## exact target, quantifiers, hypotheses and units

Following B18 STREAM_NOTES v2, independently reconstruct (i) NPN invariance of selectable physical erasure/influence ratios for A090's proposed five-variable census, (ii) A057's exact physical-child decrement and channel bound, and (iii) A057's nonreusing logarithmic charge. Consume the explicit A021 sign correction without re-enumerating accepted baselines. Full FEI remains OPEN.

Verdicts: HOLDS for both A057 v1 claims and the standard all-dimensional NPN invariance fact; ERROR in A021's v1 remainder-sign component; HOLDS for the corrected A021-UNIFORM-RARE-CORE-EXPANSION v2. My earlier blanket acceptance of that v1 component is withdrawn. The separately proved exact spectrum and control-tree identities remain accepted. No acceptance of an entire five-variable NPN catalogue or census is implied.

A057's entropy formulas are in natural units. In this report E(v)=sum v_T² ln(1/v_T²), B and D use nats, and influence is ordinary total influence. Divide every entropy expression and entropy constant by ln2 for bits. The checker stores exact prime-log coefficient vectors and evaluates them against natural-log intervals for inequalities. NPN erasure/influence invariance holds with either entropy convention.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-12 00:39 UTC, B18 STREAM_NOTES v2 dated 2026-10-11 23:34 UTC in full, and A087 STATUS/LEARNED. Protocol 2026-10-11-execution-v2 was re-read in full. The lead directs the A057/NPN audit and explicitly retires the A021/A022/A026/A027/A061/A062 baseline rechecks. The many newly completed restriction packets on the board are not silently accepted; the lead-directed target takes priority this stage.

Source-complete mathematical inputs inspected in full:

- A057 run 20261011T220314Z-account05-A057-coherent-restriction-remainder: COHERENT_REMAINDER_PAYMENT.tex, both v1 claims, REPORT, ALPHA_LOG_CONTROLS.md, NEXT_HANDOFF.md, and preserved out/source_proof.md. The latter is the coherent balanced-composition source at Git blob 37626caf9f1564342f8b6edfff54b3a3491fff35, Sections 1-8. The exact theorem is reconstructed below, not accepted solely from that provenance.
- A021 run 20261011T232653Z-account05-A021-rare-core-asymptotics: CORRECTION.md and A021-UNIFORM-RARE-CORE-EXPANSION v2. Its odd-face order claim is read for dispatch context but not audited or accepted here.
- Earlier A087 run 20261011T221055Z-account05-A087-restriction-referee: REPORT, CLAIMS, and saved status for the exact scope of the withdrawn acceptance. All prior artifacts remain unchanged.
- A090's saved status and run directory list establish the intended consumer; no source-complete new five-variable census is claimed to have been available or verified.

Prior campaign/paper sources already read in stage 1 are not re-labelled as fresh full-document audits. Current source byte hashes, actual local revisions and read limitations are in out/source_receipts.json. No web, brain mutation, git or external messages are used. A new A057 stage directory appeared during intake, but this stage's explicit review target remains the pinned v1 claims; a source update would need separate intake.

## complete derivation or exact first unsupported line

### 1. NPN invariance: a physical signed permutation

Let pi be a permutation of n input coordinates, eta an input sign vector and epsilon an output sign. Define

    f'(x)=epsilon f(eta_1 x_(pi(1)),...,eta_n x_(pi(n))).

Changing variables in the uniform Fourier expectation proves, for every S,

    f'hat(pi(S))=epsilon (product_(j in S) eta_j) fhat(S).

Thus the squared spectrum is only relabelled by pi. Physical input and output negations change coefficient signs, not squared masses. For every coordinate j, the two spectral packet masses without and with j map respectively to the packet masses without and with pi(j). Hence B_(pi(j))(f')=B_j(f) and Inf_(pi(j))(f')=Inf_j(f). Relevant coordinates are also relabelled. Consequently

    min_(i:Inf_i>0) B_i/Inf_i,
    max_(i:Inf_i>0) B_i/Inf_i, H/I,

are NPN invariant whenever their ratios are defined. Constant functions are handled separately, not by dividing zero by zero. Embedded dummy variables do not create relevant candidates.

This also preserves physical restrictions: fixing x_(pi(j))=s corresponds to fixing old input j=eta_j s, followed by the residual signed permutation and output sign. Thus admissible children and fair branch weights are preserved, not merely the abstract parent spectrum.

The NPN theorem justifies one representative per genuinely complete NPN orbit in A090's proposed census. It does not certify catalogue coverage, the stated count 616,126, duplicate removal, or extremizer logarithm comparisons. Those are separate exact-certificate obligations. Arbitrary invertible F2 coordinate changes and multiplication by a character are not NPN operations. Character multiplication XOR-translates Fourier labels and can replace Inf_i by 1-Inf_i; it does not generally preserve these ratios. Therefore neither larger affine equivalence nor a Fourier-support quotient is admitted by this proof.

### 2. Exact coherent decrement from the physical children

Let F=g(h_1,...,h_m) on disjoint physical blocks with every h_l balanced. Fix coordinate i in block j and write g=a+y_j b. Pointwise Booleanity gives ab=0 and a²+b²=1. In the uniform normalized Fourier basis,

    ||a||²=1-q, ||b||²=q=Inf_j(g), <a,b>=0.

Write alpha=h_jhat({i}), x=alpha². The actual inner children h_+ and h_- have means +alpha and -alpha because h_j is balanced. Their nonconstant Fourier vectors nu_+ and nu_- each have squared mass 1-x and raw entropy H(h_±)-x ln(1/x).

For a remaining outer set T, put C_T=sum_(l in T) H(h_l). Balancedness means each selected inner block occupies a nonempty physical frequency sector, so different outer sets occupy disjoint sectors. Raw product entropy satisfies E(v tensor w)=||w||² E(v)+||v||² E(w). The root entropy is therefore

    H(F)=E(a)+E(b)+qH(h_j)+sum_T(a_T²+b_T²)C_T.

At physical child sign sigma, the empty block-j sector has the signed coefficient vector a+sigma alpha b; the nonempty block-j sectors have b tensor nu_sigma. For each individual T the total weight of C_T is

    (a_T+sigma alpha b_T)²+(1-x)b_T²
       =a_T²+b_T²+2sigma alpha a_T b_T.

The last term must remain in each child. Its cancellation occurs only after the fair physical average, even though the total inner product <a,b> already vanishes. Thus

    H(F_sigma)=E(a+sigma alpha b)+(1-x)E(b)
               +q[H(h_sigma)-xln(1/x)]
               +sum_T[a_T²+b_T²+2sigma alpha a_Tb_T]C_T.

Subtracting the average of these two actual children gives

    D_i(F)=qD_i(h_j)+R(alpha),
    R=qxln(1/x)+E(a)+xE(b)-[E(a+alpha b)+E(a-alpha b)]/2.

This directly reconstructs the previously unaudited D-part. No child is replaced by an incoherent square-mixture, and neither noisy outer function nor its normalized coefficient vector is treated as a Boolean leaf.

For completeness, in a nonempty residual block-j frequency U, the physical queried packet is b_T times the corresponding inner packet, with the other-block product masses. Its conditional entropy sums to qB_i(h_j). In the inner empty-residual packet, h_j has masses 0,x and zero erasure, while F has masses a_T²,xb_T². Therefore

    B_i(F)=qB_i(h_j)+L_j(x),
    L_j(x)=sum_T s_T h_nat(xb_T²/s_T), s_T=a_T²+xb_T².

The algebraic identity L=E(a)+xE(b)+qxln(1/x)-E(s) yields R=L+J, where

    J=E(s)-[E(a+alpha b)+E(a-alpha b)]/2.

It also gives the useful exact channel split JS_i(F)=qJS_i(h_j)+J.

### 3. Channel bound, equal mass, and all endpoints

Both coherent vectors a±alpha b have squared mass M=1-q+qx, exactly the same as sum s_T, because <a,b>=0. If M>0, normalize them by sqrt(M). Their squared spectra P_+ and P_- are probability laws with average s/M. The raw entropy normalization term Mln(1/M) cancels, giving J=M JS_nat(P_+,P_-)>=0.

For one packet with z=2|uv|/(u²+v²), let d(z)=[(1+z)ln(1+z)+(1-z)ln(1-z)]/2. The difference of derivatives z/sqrt(1-z²)-atanh z is nonnegative because its derivative is (1-z²)^(-3/2)-(1-z²)^(-1)>=0 and it starts at zero. Integration yields d(z)<=1-sqrt(1-z²), including |z|=1 by continuity. Substituting u=a_T and v=alpha b_T gives

    0<=J<=2sum_T min(a_T²,xb_T²)<=2qx.

The common mass is indispensable. Without it, a raw subprobability entropy difference could carry uncancelled normalization terms. Here the normalized channel is valid even though the noisy outer generally is not Boolean.

Concavity of -rln r and s=(1-x)a²+x(a²+b²) give

    E(s)>=(1-x)E(a²)+xE(a²+b²),
    0<=L<=xB_j(g)+qxln(1/x).

Hence 0<=R<=xB_j(g)+qxln(1/x)+2qx. The notation E(a²) in this display means entropy of the mass vector, equivalently E(a) in the coefficient notation above.

For q=0, b=0 and all extra charges vanish. For x=0, L=J=R=0. For x=1, Booleanity forces h_j=±x_i; the inner decrement is zero and R=D_j(g). If M=0, necessarily q=1,x=0,a=0, and every relevant noisy vector vanishes, so L=J=R=0 without dividing by M. These cover the exact zero and bias endpoints in the v1 statement. Negative alpha only swaps the coherent child vectors; fair averaged identities and bounds are unchanged.

Verdict: A057-COHERENT-ERASURE-SPLIT v1 HOLDS, including its D and J clauses. Its root aggregate follows by summing the exact B identities and L bounds, with W_1(h_j)=sum_i alpha_(j,i)² and influence factorization I(F)=sum_j q_j I(h_j). The proof uses no full-FEI hypothesis.

### 4. Nonreusing alpha logarithm on the same physical tree

The Boolean physical half-difference delta_i h_j lies in {-1,0,1}, has mean alpha and expected absolute value Inf_i(h_j). Thus |alpha|<=Inf_i(h_j). Since the other inner outputs are independent fair signs and disjoint from the queried block, physical pivotality factorizes:

    Inf_i(F)=qInf_i(h_j).

The scalar function rln(1/r²), r in [0,1], has maximum 2/e at r=e^-1. Consequently

    qalpha²ln(1/alpha²)<=(2/e)q|alpha|
                           <=(2/e)Inf_i(F),
    qalpha²<=Inf_i(F).

For a finite adaptive physical tree, each next fresh coordinate is chosen from observed history and independent policy randomness. Unobserved signs remain fair. Averaging surviving edge disagreement indicators gives I(f_v)=Inf_(i_v)(f_v)+E[I(child)|history]. Multiplying by physical reach weights and summing cancels each intermediate surviving reserve exactly once:

    I(root)=sum_internal w_v Inf_(i_v)(f_v)+E I(leaf).

Nonnegative charges over any subset of independently certified represented nodes are therefore at most the full queried budget. Summing the scalar bound gives

    sum w_v q_v alpha_v²ln(1/alpha_v²)<=(2/e)sum w_v Inf_(i_v)(f_v)
                                                <=(2/e)I(root).

Combining with the node R bound gives sum w_v R_v<=sum w_v alpha_v² B_(j_v)(g_v)+(2+2/e)sum w_v Inf_(i_v)(f_v). In bits the logarithmic constant is 2/(e ln2), and the second influence coefficient is (2+2/e)/ln2. There is no additional formula-depth allocation and no repeated payment from the original root influence.

The theorem assumes a certified balanced disjoint representation at each included actual node. It does not assert that the root representation survives restriction. An inner majority has nonzero singleton alpha, so its two physical children have means ±alpha and cease to be balanced. Those nodes need recentering or a new representation; the original balanced proof cannot simply be iterated. The checker deliberately omits biased nodes from the represented bank and retains their queried costs and terminal entropy in the physical telescope.

Verdict: A057-NONREUSING-ALPHA-LOG-PAYMENT v1 HOLDS at exactly its stated subset-of-represented-nodes scope. This completes the requested D/J/log audit without a repair contribution to either A057 claim.

### 5. Narrowed A021 acceptance and corrected v2

CORRECTION_CONSUMED.md records the exact affected earlier source and verdict. My stage-1 acceptance was wrong for the v1 series sign and its derivative decrement-remainder sign. The actual coefficient of q^j for j>=3 in (1-2q+q²)sum_(l>=1)q^l/l is 1/j-2/(j-1)+1/(j-2)=2/[j(j-1)(j-2)]>0. Thus

    -2(1-q)²log2(1-q)=2cq-3cq²+R(q),
    R(q)=4c sum_(j>=3)q^j/[j(j-1)(j-2)],
    0<R(q)<=2cq³/[3(1-q)], c=1/ln2.

The endpoint q=1/2 already disproves R<=0: R=(2ln2-1)/(4ln2)>0 because ln2>1/2. The corrected entropy ratio interval follows by dividing the positive-tail bounds by q(tI(b)+k). That denominator is positive for the stated balanced cores. The tail is independent of tensor size, so the original ratio limits hold.

For u=2^-s, s>=2, G_s=R(u)-R(2u)/2 has negative coefficients 4c(1-2^(j-1))u^j/[j(j-1)(j-2)], hence -8cu³/[3(1-2u)]<=G_s<0. This confirms the v2 decrement sign. The original exact spectrum/influence formulas, KL ledger, and A087 lambda/KL identity require no remainder-sign assumption and remain accepted. KL here denotes base-two Kullback-Leibler divergence, not a Rényi order; the equality is always between the displayed formulas, not similarly named unrelated debts.

The correction is authored by A021 with the B05 lead credited for the sign repair. A087 supplies an independent reconstruction and rational certificates, not a new repair to v2. Verdict: corrected A021-UNIFORM-RARE-CORE-EXPANSION v2 HOLDS. The separate new odd-face claim is not accepted by this run.

### 6. First unsupported universal line

Even after the logarithm is paid, the exact represented-tree identity is

    H(root)=E H(leaf)+sum w_v q_v D_(i_v)(h_(v,j_v))+sum w_v R_v.

The remaining sum of terminal entropy, inner decrements, and scaled outer erasure sum w_v alpha_v² B_(j_v)(g_v) has no proved absolute influence price. Nor is a valid balanced or recentered representation supplied for all biased descendants. At alpha=1, R is the arbitrary outer decrement, so declaring the full remainder locally paid would recover the already false all-coordinate restriction estimate. The first missing universal statement is a signed, nonreusing recentered descendant reserve that pays those terms from actual queried plus terminal influence.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before any search. An unsharded composition pilot hit its runtime guard and saved no final certificate; that execution is excluded. SPEC_REVISION.md freezes four contiguous shards of the same 256 functions and the shorter 12-term certified natural-log enclosures before rerunning. There is no dimension escalation, randomness, GPU, heavy job or >300 MB allocation. Estimated memory is 60 MB.

Commands from A087, with run prefix `runs\20261012T004155Z-account05-A087-restriction-referee\`:

    python -X utf8 <run>code\audit.py npn
    python -X utf8 <run>code\audit.py composition0
    python -X utf8 <run>code\audit.py composition1
    python -X utf8 <run>code\audit.py composition2
    python -X utf8 <run>code\audit.py composition3
    python -X utf8 <run>code\audit.py trees
    python -X utf8 <run>code\audit.py correction

All final phases PASS: 291,238 exact assertions. NPN: 24,852 transformations, 271,925 assertions, 1.0896 seconds. Composition: 256 functions, 1,536 physical splits and 17,156 assertions across four shards; 160 splits have nonzero other-block interference. Trees: 256 stopped trees, 624 queried nodes, 272 certified actual balanced representations and 152 nonzero-terminal-entropy trees; 2,144 assertions. Correction: six positive entropy remainder intervals and 13 assertions. Every phase output retains its runtime, exact rational bounds and helper hash.

Direct integer character sums generate the actual root and both physical children. Exact Fraction masses and prime-log coefficient vectors verify entropy identities without floating arithmetic or presumed independence of logarithms. Signed interval evaluation uses the correct endpoint order. For 1<=y<=2, z=(y-1)/(y+1), the natural logarithm is enclosed by 2sum_(j=0..N-1)z^(2j+1)/(2j+1) and that sum plus 2z^(2N+1)/[(2N+1)(1-z²)]. Range reduction contributes signed multiples of a separately enclosed positive ln2. The original npn and correction outputs use helper v1; the original correction uses N=32. Final composition/tree phases use N=12. Factorial sums give e_lower=sum_(j=0..24)1/j!, e_upper=e_lower+26/(25*25!), and use 2/e_upper as a rigorously smaller right-side influence coefficient. No floating sign is used.

The bounded certificates independently check implementation and endpoints. All-dimensional NPN, coherent-child, logarithmic and corrected-series conclusions rest on the complete proofs above; none is extrapolated from the finite domain. This is not a certificate of A090's proposed five-variable orbit catalogue.

## proof dependencies and changed downstream conclusions

Both A057 v1 statements are independently accepted with all original hypotheses. Their raw coherent source formula, its proof and all normalization steps were reconstructed. No pending A056, B09 or full-FEI theorem is a premise. The NPN admission is a direct all-dimensional character calculation. A021 v2 substitutes for the false sign component of v1; exact-spectrum/control-tree results retain their separate acceptance.

Local CLAIMS.json preserves exact statement text and original source metadata while recording HOLDS/ERROR verdicts. Statement hashes are normalized to SHA256 of UTF-8 exact_statement with source recorded values retained in review records, following the previous stage's hash discrepancy finding. Shared claim indices and other agents' files are not changed. B20 should propagate the source-bound narrowed A087 acceptance. A090 may use NPN invariance, subject to an independent complete catalogue and certified extrema. A057/A064/A097 may use the paid logarithmic component but must retain outer erasure, inner decrement, terminal entropy and actual biased-node recertification.

## one next mathematical action and independent reviewer

Next: audit the recentered signed empty-sector correction in A057's new descendant source, against actual sparse-bent physical children and their conditional history probabilities. Require a state reserve that cancels the inner empty-sector entropy only once and survives biased descendants while retaining terminal entropy. If A057's new stage is incomplete, reconstruct its frozen NEXT_HANDOFF identity independently before attempting a price. Independent reviewer: A094 for the corrected acceptance and A090 for the NPN and A057 reconstruction; no external message is sent.

## actual persistence receipts or precise save blocker

All requested artifacts are local inside this stage's A087 directory: REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA, frozen specifications, correction consumption, independent code, rational certificates, source receipts and schema/persistence validation. Rolling STATUS, WORKLOG and LEARNED are current. Each file is below 20 MB. out/persistence_receipts.json records file hashes and sizes after saving; out/schema_validation.json checks exact protocol field sets, interpreting the protocol's explanatory packet_ids parenthesis as its canonical packet_ids key. No upload, mirror, external acceptance, downstream use or public release is claimed.

## Universal bridge

This stage moves C019 stopping-tree payment by independently closing A057's previously unaudited coherent D/J identity and proving that its explicit logarithmic bank costs at most 2/(e ln2) times the physical queried influence in bits, with no reused budget. It also secures C018's NPN orbit reduction and removes a false sign dependency from A021 asymptotic transport. The universal unpaid terms are scaled outer erasure, inner decrement, terminal entropy and representation changes at biased descendants; no universal constant improves here. NEXT attacks the exact signed recentered reserve on the actual restriction hierarchy, the shortest route to the surviving universal payment gap rather than another isolated class theorem.
