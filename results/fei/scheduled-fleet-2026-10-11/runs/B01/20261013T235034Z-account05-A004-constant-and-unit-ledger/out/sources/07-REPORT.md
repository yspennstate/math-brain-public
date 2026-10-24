# A026 stage 3: erasure selection survives a first query in other blocks

## exact target, quantifiers, hypotheses and units

C018 asks for a dimension-independent K such that every nonconstant Boolean sign on every uniform finite cube has some relevant i with B_i<=K I_i. That remains open. This stage proves a scoped history-robust prefix statement: for even k>=4, the sparse bent-surgery outer seed of A003, with all 3k background inputs encoded by disjoint odd majority blocks of size M=2k^2 2^(2k+2)+1, admits one physical query per block with every chosen bit satisfying B_i/I_i<55/256 and I_i>I/(2d). This holds at every reached preterminal node, including actual bias in previously queried blocks; d is the relevant residual physical dimension. Any adaptive order among intact blocks is permitted. Entropies are bits. Full terminal entropy is retained.

## sources actually read, revisions and theorem locators

Read EXECUTION_PROTOCOL.json in full (2026-10-11-execution-v2), BOARD.md at stage start and refreshed header 2026-10-13 21:55 UTC, B06 STREAM_NOTES.md v2 (2026-10-11 23:26Z), own STATUS and LEARNED and prior stage artifacts. The lead's transitive-family assignment was completed in stage 2; this stage follows dispatch order by consuming A003's new induced-bias objection and its explicitly named first-restriction target.

Read A003 stage 20261012T005637Z REPORT, DERIVATION sections 1-5 and CLAIMS: the root retained-selector construction, outer influence types, and distinction between maximum-influence selection and G_(1/2) selection. Read A075 stage 20261013T212622Z REPORT, A030 WORKLOG, A057 stage 20261012T003930Z REPORT/CLAIMS, and A063 stage 20261011T222159Z REPORT for current paid banks and unpaid terminals. A056-DISJOINT-COMPOSITION v2 is consumed through A057's reproduced statement and independent acceptance, not through an asserted new review of A056's original files. Source hashes and exact locators are in out/source_receipts.json. Own stage-2 logarithm helper is reused and hash-pinned; no other agent's code is imported. No new literature novelty claim is made.

## complete derivation or exact first unsupported line

PROOF.md gives the analytic argument. For arbitrary actual Boolean rest, write F=A+gD, with A D=0 and delta=E D^2. An intact balanced odd encoder has only its empty/singleton erasure collisions, giving B_i=sum_T Phi(Ahat_T^2,gamma^2 Dhat_T^2). Concavity gives B_i/I_i<=(gamma^2/d_g)log2(e/(gamma^2 delta)). For majority gamma=d_g=rho. This is a consequence of the existing composition formula used on actual physical rest, not a new balanced-composition identity.

After q first queries in distinct blocks, the induced outer density is between (1-rho)^q and (1+rho)^q. The larger encoder choice ensures rho<2^-k/(2k), so q rho<3/32 for every q<=3k. Actual background edge probabilities remain at least p/4, p=2^-2k. Consequently every intact bit has price <55/256. A separate density/influence comparison puts each such bit above the half-average cutoff at every preterminal node. The retained selector remains the unique maximum-influence coordinate, but its divergent erasure price is claimed only at the root, as supplied by A003's B05 input. No bad-selector claim is extrapolated to biased children.

The exact decrement identity is Delta_i H=B_i+J_i, with J_i<=(2/ln2)I_i. The physical influence telescope pays the whole prefix at K0=55/256 for erasure and K0+2/ln2 for entropy decrement. Hence H(root)<=E H(leaf)+(K0+2/ln2)[I(root)-E I(leaf)]. No leaf entropy is omitted. For sliced encoders the exact correction is delta[B_i(h)-Phi(mu^2,gamma^2)] plus the signed shifted empty-row collisions; it is retained in the proof and exact checks.

The first unsupported universal line is paying a second query in touched blocks, or the retained outer-core entropy, from a single conserved influence budget without assuming FEI for the core. The intact-block scalar bound contains log(1/delta), and unrestricted delta has no family-independent lower bound. The universal selection theorem and a complete stopping-tree payment therefore remain unproved.

## executed validation with domain, arithmetic, commands and outputs

PILOT_SPEC.json, MAIN_SPEC.json and SYMBOLIC_SPEC.json were saved before their respective executions. Pilot: all 16 Boolean outer functions f(y,z), Maj3 encoder in untouched/first-bit-plus/first-bit-minus states, 48 cases, 112 coordinate identities, 12 relevant scalar checks PASS in 0.018720 seconds. Main: all 256 Boolean outer functions f(y,z1,z2), all 9 corresponding states of two disjoint Maj3 blocks, 2304 cases, 10752 coordinate identities, 1440 relevant intact scalar checks PASS in 30.373610 seconds. No sign reduction or random sampling; fixing the representative first bit uses majority permutation symmetry. Every remaining physical inner coordinate is checked.

Commands from A026: `python -X utf8 runs/20261013T214810Z-account05-A026-good-coordinate-erasure/code/check.py 1`, then the same with `2`; `python -X utf8 runs/20261013T214810Z-account05-A026-good-coordinate-erasure/code/symbolic.py`. Integer Walsh transforms and Fraction probabilities verify actual physical/spectral influences and induced product-bias derivative masses. Canonical rational prime-log equality proves erasure identities. Forty-eight-term atanh expansions with proved tails and outward dyadic rounding at 2^-140 certify scalar signs. The smallest main scalar margin is saved as an exact rational in out/main_summary.json. Logs are evaluated only for sign certificates; no floating-point decision enters.

Symbolic checks: 3193 (k,q) pairs, even k=4,...,64 and q=0,...,3k, plus 257 central-binomial recurrence checks, PASS in 0.233255 seconds. These finite checks corroborate algebra; PROOF.md's recurrence, density and monotonicity arguments establish all even k>=4 separately. Encoder dimensions are analytic, never instantiated as huge truth tables. No dimension escalation, GPU, background process or job over 300 MB was used. Frozen memory estimates are 60/100/20 MB. The helper is named A026-biased-history-v1 in outputs; the frozen specs' A026-biased-rest-v1 label denotes the same initial helper, not a restarted or modified search domain.

## proof dependencies and changed downstream conclusions

The prefix theorem can be stated abstractly for any Boolean outer source with the listed influence types; its new density and price proof is self-contained. A003's root identities and source B05 construction instantiate those hypotheses. A003-MAXIMUM-INFLUENCE-SELECTION-NOGO v1 is pending independent review, so the specific-family interpretation is explicitly source-conditional pending that review; this run does not assert independent acceptance of its entire chain. The biased packet correction agrees with A056-DISJOINT-COMPOSITION v2, locally independently accepted by A057. B06 R2 supplies the established physical telescope and JS price. No FEI premise is used for the actual rest.

A003 can replace its root-only cheap-coordinate bound by a bound through every first query in distinct blocks, with actual bias and G_(1/2) eligibility certified. A057/A056 can use the exact sliced-majority correction as the first unpaid inner term. This is one narrow prefix/transport claim, not another broad universal candidate or a new complete FEI class theorem. Universal C018 and C019 are still open; all-coordinate and maximum-coordinate claims are expressly distinguished from the existential target.

## one next mathematical action and independent reviewer

Derive a signed reserve for a second physical query in a previously touched majority block, using the inherited erasure minus empty-row credit and retaining terminal outer-core entropy; test the reserve against an arbitrary Boolean outer seed. A003 is the direct mathematical consumer; A087 or A094 should independently reconstruct the density comparison, half-average cutoff and all-k constant. Review has not occurred in this run.

## actual persistence receipts or precise save blocker

All run files, code, frozen specs, exact outputs and rolling files are saved only inside A026. out/persistence_receipts.json records sizes and SHA256 hashes after schema/readback validation. PROGRESS.json and PACKET_DELTA.json are byte-identical, and claims/progress use exactly the protocol's field names. No file exceeds 20 MB. Independent review, supervisor copying and mirror verification remain pending; no external registry or brain store was modified.

## Universal bridge

This stage moves C018 selection and C019 stopping-tree payment from a balanced root to an entire adaptive first-query-per-block prefix: every intact bit has B_i/I_i<55/256 and lies in G_(1/2) despite all induced output biases, and cumulative prefix entropy decrement costs at most (55/256+2/ln2) times consumed influence. It gains no universal FEI constant because terminal biased blocks and outer-core entropy remain unpaid. NEXT examines the first second-query charge with the exact signed correction on an arbitrary outer seed; this is the shortest continuation because it addresses precisely where the reusable selection proof stops, rather than establishing another isolated root class.
