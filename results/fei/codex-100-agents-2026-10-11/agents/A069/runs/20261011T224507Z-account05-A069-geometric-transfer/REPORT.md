# A069 / B14: stable transfer of the percolation mask decoder

Full FEI remains OPEN. This is a complete local derivation for a proper family and an abstract perturbation interface; independent acceptance and supervisor copying are pending. All entropy is in bits.

## exact target, quantifiers, hypotheses and units

Let g_d be complete depth-d ternary recursive majority on n=3^d independent uniform sign bits, d>=1. For any N>=n, pad g_d with N-n unused bits. For an arbitrary deterministic edit set D in the N-cube, let f=g_d off D and f=-g_d on D, and rho=|D|/2^N. The target proved here is a complete, injective prefix code for every spectral subset, including the empty subset, with:

* H(f)<=E_{S_f} L_T(S_f)<=12 I(f) whenever N rho<=1/8.
* For a single edited input, H(f)<=E_{S_f} L_T(S_f)<=25 I(f), uniformly in d,N and edit location; the constant 12 applies for N>=6.
* Its cost is stable under padding followed by one point flip: for fixed d, the cost difference from the padded base code tends to zero as N tends to infinity.

The abstract hypothesis is a fixed rooted partition tree T with singleton leaves, at most three children per internal vertex, and a paid spectral occupancy sum. Its coordinates and child order are fixed before the sample is drawn. No spatial estimate is assumed. Tree choice may depend on the function, but not on the realized Fourier set.

## sources actually read, revisions and theorem locators

Execution protocol: fei-execution-protocol/2, revision 2026-10-11-execution-v2, all rules read. Campaign README, current status, claim/obstruction registries, A069 packet entry, stream actions, campaign plan B14/A069 acceptance contract, supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING were consulted. BOARD.md snapshot 2026-10-11 22:37 UTC and B14 STREAM_NOTES.md v1, 2026-10-11 22:48 UTC supplied the nonduplication and padding-flip directions.

Primary local mathematical texts: percolation_spectral_pivotal_entropy_30pp.txt, Lemma 2.1 (refinement decoder), Lemma 4.1 (block variance), Proposition 4.3 (occupancy payment), Theorem 4.4 (arm criterion). The 31-page other version was compared at its abstract and corresponding lemma/theorem locators. threshold_paper_38pp.txt, Section 7, Proposition 7.1 and Corollaries 7.2-7.3 give disjoint composition and the existing read-once baseline; the earlier 29-page version was compared at its introduction and Section 7 locators. Supplemental BLOCK_RESTRICTION_IDENTITY_2026-09-18.md and prior B05/B19 reports were consulted for scope. Source hashes and precise paths are in out/source_manifest.json. No web literature/priority search or new prior-art claim is made.

The source does NOT say that a spectral sample is a deterministic function of a pivotal set, or of a few arms. It decodes the sample from occupied-cell masks. Arm events bound block oscillation probabilities, which bound spectral occupancy. These two steps must be distinguished.

## complete derivation or exact first unsupported line

### 1. Abstract all-set decoder and complete cost

For each internal vertex v, let C_v be its cell and b_v its number of children, with 2<=b_v<=3. Encode the empty set by the one-bit word 0. Encode a nonempty set by 1 and, in preorder, encode every occupied internal vertex's nonempty child mask using b_v bits. Number masks 1,...,2^{b_v}-1 and write mask-1 in b_v bits. One word is unused at each vertex. Unoccupied vertices are skipped. At singleton leaves, occupation already identifies the coordinate, so no further bits are needed.

The decoder knows which occupied vertices remain from previously decoded masks. It stops precisely when this list is empty. This proves unique decoding, termination, and prefix freedom. Every subset has a word. Thus Q_T(S)=2^{-L_T(S)} has total mass <=1 by Kraft, with

    L_T(S)=1 + sum_{v internal} b_v 1{S intersects C_v}.

The root bit, all child choices, and all physical coordinate locations are paid: locations are specified by the fixed tree and the decoded masks. There are no latent witnesses, unrevealed leaves, sample-dependent geometry choices, or omitted reference normalizers. The fixed decoder is available for all sets, including those absent from g's spectrum. Gibbs' inequality for the subprobability Q_T gives

    H(f)<=Gamma_T(f):=sum_S fhat(S)^2 L_T(S)
         =1+sum_v b_v P(S_f intersects C_v).                 (1)

Indeed normalize Q_T by its mass Z<=1, use KL>=0, and note that adding log2 Z<=0 can only reduce the cross-entropy bound. This is the integral-bit version of percolation Lemma 2.1. Its abstract influence hypothesis is Gamma_T(f)<=K I(f). Decoding alone never proves that hypothesis.

A tree without unary vertices has at most N-1 internal vertices, since sum_v(b_v-1)=N-1. Therefore

    max_S L_T(S)<=1+3(N-1)=3N-2.                           (2)

### 2. Perturbation transfer, valid without spatial or Boolean spectral assumptions

For Boolean f,g on the same uniform N-cube, put delta=f-g and rho=P(f!=g), so ||delta||_2^2=4rho. For any fixed nonnegative finite cost L, weighted Euclidean Minkowski gives

    sqrt(Gamma_L(f)) <= sqrt(Gamma_L(g))
                        +sqrt(sum_S deltahat(S)^2 L(S))
                     <= sqrt(Gamma_L(g))+2 sqrt(rho max L). (3)

Equivalently, |Gamma_L(f)-Gamma_L(g)| is at most

    4 sqrt(rho max L Gamma_L(g)) + 4rho max L.              (4)

For linear payment one may use (a+b)^2<=2a^2+2b^2 coefficientwise:

    Gamma_T(f)<=2Gamma_T(g)+8rho(3N-2).                    (5)

This retains coherent cross terms; it does not treat squared spectra as an incoherent mixture. The only Boolean input here is ||f-g||_2^2=4rho. The weighted triangle statement itself holds for arbitrary real vectors.

The physical edge events for f and g can differ only if x or x with coordinate i flipped lies in D. Thus

    |Inf_i(f)-Inf_i(g)|<=2rho,
    |I(f)-I(g)|<=2N rho.                                  (6)

For a one-point edit at x0, deltahat(S)=-2g(x0)2^{-N} chi_S(x0) for every S. In particular, for any cell C,

    sum_{S intersects C} deltahat(S)^2
       =4*2^{-N}(1-2^{-|C|}),
    P(S_f intersects C)<=2P(S_g intersects C)
                         +8*2^{-N}(1-2^{-|C|}).           (7)

This directly exhibits stability of the occupancy sum itself, even though the edited Fourier support can become dense.

### 3. Direct nongeometric payment for recursive majority

The three-bit majority gate has the exact Boolean expansion

    Maj3(y1,y2,y3)=(y1+y2+y3-y1*y2*y3)/2.

Its spectral child mask is one of {1},{2},{3},{1,2,3}, each with probability 1/4. At every composition node the child functions are balanced and use disjoint physical blocks. Consequently any output Fourier set has a unique decomposition into its occupied child blocks; substitution multiplies their coefficients with no interference. Conditional on the child mask, their nonempty spectral samples are independent copies of the child law. This follows directly from the expansion and agrees with threshold Proposition 7.1.

An individual child is selected with probability 1/2. Thus any main-tree cell at depth j is occupied with probability 2^{-j}. There are 3^j such cells, so the expected number occupied at that level is (3/2)^j. Singleton leaves yield

    I(g_d)=(3/2)^d,
    E(number of occupied main internal nodes)
       =sum_{j=0}^{d-1}(3/2)^j=2(I(g_d)-1).               (8)

This is the required occupancy growth/payment replacing percolation's arm estimates. It is proved from the named Boolean family, not imported from spatial geometry. The four-mask two-bit code on the unedited support also gives the known identity H(g_d)=4(I(g_d)-1). That support-only code is NOT used after editing.

To code all subsets, use the three-bit masks of section 1. If there are padding bits, attach the main ternary tree and an arbitrary binary tree on all padding bits to a new binary root. Under g_d the main branch is always occupied and the padding branch never is. Write Ig=I(g_d). Exactly,

    Gamma_T(g_d)=1+6(Ig-1)+2*1{N>3^d} <=6Ig-3.            (9)

Combining (5), (6), and (9), for every edit set D,

    H(f)<=Gamma_T(f)
         <=12Ig-6+8rho(3N-2)
         <=12I(f)-6+48N rho-16rho.                        (10)

Hence N rho<=1/8 implies Gamma_T(f)<=12I(f). This proves the sparse-edit theorem for arbitrary edit sets, including highly irregular, nonmonotone edits and all choices of signs inherited from g_d.

For a single point, rho=2^{-N}, N>=3. Since N/2^N<=3/8, (10) gives Gamma_T(f)<=12I(f)+12. Balance of g_d gives Ef=+-2^{1-N}, hence Var(f)=1-4*2^{-2N}>=15/16. Parseval gives I(f)>=Var(f), and consequently

    Gamma_T(f)<= (12+12/(15/16))I(f)
              =(124/5)I(f)<25I(f).                       (11)

For N>=6, N/2^N<=1/8, so the sharper constant 12 follows from (10). No floating-point logarithmic estimate supplies any of these signs.

### 4. Padding stability and scope controls

For fixed d, Gamma_T(g_d) is constant for N>3^d by (9). By (2) and (4), a one-point edit changes that paid cost by at most

    4 sqrt(2^{-N}(3N-2)Gamma_T(g_d))
       +4*2^{-N}(3N-2),                                  (12)

which tends to zero. Influence convergence follows from (6). For completeness, spectral total variation tau<=2 sqrt(2^{-N}) follows by Cauchy-Schwarz applied to (fhat-ghat)(fhat+ghat). A maximal coupling and the conditional entropy chain rule give |H(f)-H(g_d)|<=h2(tau)+tau log2(2^N-1), which also tends to zero. Thus this functional passes the B14 perturbation test in its actual paid domain.

The base recursive-majority family is already covered by read-once composition (threshold Corollary 7.3 and the cited composition literature). Reproving its FEI is NOT a new class advance. The additional deliverable is an all-set hierarchy that remains paid after arbitrary sparse truth-table edits; edits are not assumed to preserve the original read-once representation. We do not claim that this neighborhood theorem has no prior literature overlap. For example, changing Maj3 at the all-positive input makes it non-unate: from that input a single negative input changes output -1 to +1, whereas elsewhere the same coordinate has the original positive majority direction. This edited example lies outside the unate/desirability hypothesis of C001. We make no assertion that every edited member is outside every structured FEI theorem.

The normalized non-Boolean control a(x)=N^{-1/2} sum_i x_i has spectrum uniform on singleton sets and I(a)=1. At N=3^d, the same complete ternary tree has one expected occupied vertex at each internal depth, giving Gamma_T(a)=1+3d. This diverges. The decoder and stability lemmas remain valid; the Boolean-family occupancy payment (8) is the indispensable extra step. There is no extension of (8) from normalization alone. An arbitrary tensor factor is not allowed as an unpaid terminal in the family theorem.

First unsupported universal line: for every Boolean f, choose a bounded-arity fixed partition tree, or a fixed-prior collection of complete tree references, whose full expected code cost is <=K I(f) for one absolute K. This report proves that choice/payment only for the recursive-majority neighborhood above. It neither proves nor disproves that universal statement.

## executed validation with domain, arithmetic, commands and outputs

Both specs were saved before their runs. FROZEN_SPEC.json fixes depth 1, N=3..8 and depth 2, N=9..10, every edit location (2,040 cases), no symmetry reduction. Command: `python -X utf8 code/validate.py`. Actual result: PASS, 1,437,082 exact assertions, 3.958 seconds measured within the Python process. Output: out/validation.json.

Checks construct actual Boolean truth tables, compare each changed integer FWHT coefficient to the independent rank-one update, compare physical edge influences with spectral influence, verify every-subset prefix decoding and Kraft, and check all code/occupancy inequalities using integers and Fraction. They do not numerically evaluate entropy: the prefix/Gibbs proof supplies the entropy bound.

FROZEN_PAIRS_SPEC.json separately fixes Maj3 padded to N=7 and every unordered two-point edit, 8,128 cases, N rho=7/64<=1/8. Command: `python -X utf8 code/validate_pairs.py`. Actual result: PASS, 1,072,896 exact assertions, 3.006 seconds measured within Python, saved in out/pairs_validation.json. Together the checkers cover 10,168 cases and 2,509,978 exact assertions. The second checker uses a full truth-table FWHT and the independently computed rank-two coefficient update. It tests arbitrary same-sign and opposite-sign edited vertices. No heavy search, GPU, dimension escalation, or external persistent process was used; estimated memory was 12 MB per checker.

Finite checks validate implementation and the identities at the frozen dimensions. The all-dimensional conclusions rest on equations (1)-(12), not on extrapolation from the finite checks.

## proof dependencies and changed downstream conclusions

No unreviewed campaign claim is assumed. The proof independently reconstructs the refinement/Kraft argument and the balanced Maj3 substitution from explicit expansions; the primary source locators are provenance and baseline comparison. The perturbed class proof uses standard finite Parseval, weighted Euclidean triangle, and the elementary physical edit bound. One bundled authored claim is saved in CLAIMS.json; review acceptance is not inferred from author checking.

A067/A070 can use equation (3) as a perturbation-stability test for any proposed complete finite-cost code. A008/A011/B02 can use this all-set code as a complete witness endpoint with root, mask, and terminal charges explicit. B20 can record restricted C020 payment, not a universal FEI advance in quantifier scope. The inherited read-once case is retired as a baseline.

## one next mathematical action and independent reviewer

Next mathematical action: replace the crude edit tax rho*N by the exact weighted edit-spectrum term E_delta=sum_S deltahat(S)^2 L_T(S), and pay E_delta by physical boundary on a union of disjoint subcube edits, retaining the Fourier entropy of each restricted core rather than hiding it in a leaf. This is a concrete test of the obstruction to transporting the generic stability interface beyond vanishing-density neighborhoods. Independent reviewers: A088 and A094; A070 should apply the non-Boolean and padding controls. No messages were sent to other agents.

## actual persistence receipts or precise save blocker

Local required files, two family-proof deliverables, frozen specs, code, exact outputs, source hashes, and rolling files are saved under A069. out/receipts.json lists actual byte sizes and SHA256 hashes, generated only after schema and output verification. Local save is complete; supervisor copy, GitHub/brain mirror verification, independent acceptance, and downstream use have NOT been observed. No access blocker occurred.

## Universal bridge

This stage moves C020 whole-set witness cost: it supplies a complete geometric-free decoder, a generic weighted-L2 transfer inequality, and full payment on arbitrary sparse edits of recursive majority (12I for N rho<=1/8; 25I for every padded one-point edit). The inherited unedited case is already known. What remains is a universal tree/reference selection and payment theorem, with no arbitrary uncharged terminal entropy. Replacing rho*N by the exact edit-spectrum cost is the shortest next route because the transfer lemma applies to any already paid reference, and the edit cost identifies the missing budget for broader sources; merely proving another unperturbed read-once class would not move this interface. Full FEI remains OPEN.
