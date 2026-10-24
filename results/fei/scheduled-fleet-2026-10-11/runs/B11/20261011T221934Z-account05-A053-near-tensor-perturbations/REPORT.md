# exact target, quantifiers, hypotheses and units

A053 / B11, run 20261011T221934Z-account05-A053-near-tensor-perturbations. For every actual Boolean sign and every one-point flip, quantify the signed Fourier perturbation, physical influence, additive second-derivative energy, centered spectral covariance and multiplicative plaquette curvature. For every fixed nonconstant tensor core prove uniform, dimension-explicit entropy and influence errors and determine whether qualitative tensor primitivity controls hidden tensor structure. Entropy and logarithms are in bits, with {0,1} physical input encoding equivalent to the sign cube. Exact statements and hypotheses are in CLAIMS.json and HIDDEN_TENSOR_DIAGNOSTIC.md. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

The complete EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was read first. README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS and STREAM_NEXT_ACTIONS were inspected, along with the campaign plan's universal frontier and A022/A051--A055 execution contracts. BOARD.md was read at stage start, snapshot 2026-10-11 22:16 UTC. claude/B11/STREAM_NOTES.md is absent. Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and NATIVE_MAPPING were loaded and relevant scopes inspected. Source notes consulted include ERASURE_REDUCTION sections 1--4, ERASURE_RIGIDITY sections 1--2, ADDENDUM_11_26 and ADDENDUM_11_44, plus the route map and overlapping-product guard. No component-pruning result is assumed.

A022's original REPORT.md was read, particularly the signed one-point identities and uniform tensor-support logarithm classification. Its sharper selector bill is not rederived or claimed anew. A051's REPORT.md, CLAIMS.json and full EXISTENCE_AND_LIMITS.md were read and independently reconstructed in REVIEW_A051.md. Its two exact statements receive a source-bound analytic ACCEPT_AT_STATED_SCOPE verdict; adoption is pending, and its executable was not rerun. This review addresses B11's existing two-claim queue before handoff of one bundled A053 diagnostic.

Earlier shared B05 and B19 reports were read at their original run paths, including the all-even-k local refund obstruction and its accepted scope; B09 was inspected as background only and is not a premise. Protocol pins are B05 commit 80cc2e5027efa56d79c4ecdf7d4949759ef2068b and B19 7955d427222392911dc6af2e4ee3aa8aab67ac8c. The supplemental source pin is bfb1d10b25cb5cb2e09112357cd24b21b5b1fe5e.

All four supplied paper texts were loaded; relevant current/earlier introductions were inspected. Threshold 38pp sections 8.3--8.4, Proposition 8.9/Corollary 8.10 and Proposition 7.1 locate the existing balanced-tensor, activation and disjoint-composition baselines. Percolation 30pp/31pp introductory spectral/pivotal definitions were inspected for scope; no percolation theorem is used here. Some texts require cp1252 decoding. out/SOURCE_MANIFEST.json pins actual local bytes and distinguishes full-file loading from relevant excerpts analyzed; no exhaustive study of unrelated paper sections or remote readback is claimed.

# complete derivation or exact first unsupported line

HIDDEN_TENSOR_DIAGNOSTIC.md sections 1--7 contains the complete proof; NEAR_TENSOR_PERTURBATIONS.tex is the requested concise mathematical interface. With p=2^-n and g=f-2f(a)1_a, the exact influence change is 2p sum_i f(a)f(a^i). Additive mixed derivative energy changes by p(r_i+r_j-r_ij), while multiplicative plaquette probability changes by 4p sigma_ij(a). Across a product cut the latter is exactly 4p and centered spectral covariance has absolute value <=7p+4p^2. Raw additive mixed-derivative positivity is not a nonfactorization statistic.

Vanishing cross-cut plaquettes are equivalent to coordinate tensor factorization. A one-point flip of a nontrivial product changes the whole-cube product from +1 to -1, ruling out every nontrivial coordinate factorization. All integer Walsh sums are then 2 mod4, proving full support. These are exact conditions, not visual circuit connectedness.

Parseval and Cauchy-Schwarz bound spectral TV by 2sqrt(p(1-p)). A self-contained maximal-coupling proof gives the entropy continuity bound. For n>=4, |H(g)-H(f)|<=h2(u_n)+n u_n, u_n=2^(1-floor(n/2)); influence error is <=2np. Both estimates are uniform in tensor count, core dimensions and point location and include zero old coefficients.

For any fixed nonconstant d-bit core h, balanced powers F_t=z*h^tensor t have H=tH(h), I=tI(h)+1. Their one-point surgeries G_t are tensor-prime, full-support, all-essential and have connected plaquette graphs, yet H(G_t)/I(G_t) tends to H(h)/I(h). Across the fresh-sign cut the total plaquette curvature is 4td*2^(-td-1), tending to zero, and the corresponding summed absolute covariance also tends to zero. The simultaneous qualitative class therefore has the same extended optimal FEI constant as unrestricted Boolean signs. This is an admission equivalence, not an actual unbounded-ratio family.

For t>=2 fixing another copy away from its surgery coordinates removes the defect and leaves +/-h as a proper physical descendant. Thus a strict violating core makes these admitted embeddings fail dimension-criticality. A051's stronger all-descendant tests remain distinct and useful.

First unsupported universal line: all dimension-critical violating witnesses have quantitative separation from near-products sufficient to pay a proper-block entropy erasure or the remaining full conditional witness cost. Neither that separation nor an absolute FEI constant is proved. No refutation of dimension-critical structure is asserted.

# executed validation with domain, arithmetic, commands and outputs

Both the initial and revised search specifications were saved before their respective runs. The initial unreduced pilot was manually interrupted after slow progress; it produced no completed certificate, and its elapsed helper runtime was not captured. The revised specification out/FROZEN_SPEC_V2.json makes input-translation symmetry explicit: moving a flip to zero permutes each fully enumerated sign family, including each two-factor product family. It does not claim extra symmetry coverage for the fixed balanced tensor fixtures.

Executed from A053:

    python -X utf8 runs\20261011T221934Z-account05-A053-near-tensor-perturbations\code\check_near_tensor.py

Final result in out/EXACT_CHECK.json: PASS, 592 cases, 35,957 exact assertions, 3,132 cut rank checks and 36 rigorous entropy-interval checks; measured helper runtime 0.37773290008772165 seconds. The domains are every sign for n=1,2,3 at zero (276 cases), every product of two arbitrary two-bit signs at zero (256), and balanced powers of all one-/two-bit signs at t=1,2,3 at zero (60). No automatic dimension increase, randomness, GPU or heavy job was used. Frozen memory estimate is 25 MB; actual peak memory was not measured. The v2 helper enforces an internal 55-second stopping boundary within a 60-second pilot allowance. Shell/tool overhead is separate from helper runtime.

Walsh sums and factor-cut minors are integers; edge probabilities, plaquette probabilities, spectrum identities, covariance and TV inequalities use Fraction. Physical second differences independently reproduce spectral second moments. Entropy comparisons use 40-term rational atanh-series intervals with an explicit tail and exact range reduction. Only selected finite continuity checks need logarithms; all-dimensional results have analytic proofs. The code and exact output provide a reproducible certificate, not numerical support substituted for proof.

# proof dependencies and changed downstream conclusions

The bundled A053 result is self-contained: Walsh linearity, orthogonality, physical edge/face counting, parity of truth-table negative count, F_2 discrete differences, and the elementary coupling argument. No pending campaign theorem is a required premise. The existing tensor/balancing baseline is reproduced as a calibrated identity, without a novelty claim. A051's two claims are analytically independently accepted in REVIEW_A051.md without supplying substantive repairs; their field-level registry records remain untouched for supervisor adoption.

A054/A055 should reject qualitative primitivity, positive raw mixed energy and graph connectivity as arbitrary-core exclusion conditions. A052/A051 can retain genuine all-descendant deficit constraints: the explicit restriction above is exactly where the near-tensor embedding fails them. A022 receives the cross-cut mixed-derivative/covariance ledger and should retain its sharper local logarithm formulas. A090/A094 should review the full bundled A053 proof independently.

# one next mathematical action and independent reviewer

Next: apply A051's all-proper-descendant deficit inequalities to a quantitative near-product separation condition, locating either one paid proper-block erasure on a prospective critical witness or an actual critical counterexample to the proposed separation. Independent reviewers: A090 and A094. The needed check is on a minimal violating source, not another arbitrary seed family. Source-bound handoff is via the saved run for supervisor collection; no tool messages were sent to other agents.

# actual persistence receipts or precise save blocker

Saved locally: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, both requested mathematical deliverables, REVIEW_A051.md, code/check_near_tensor.py, code/save_records.py, both frozen specifications, exact checker output, source manifest and persistence receipts. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE_RECEIPTS.json records byte lengths, SHA256 hashes, and exact protocol field-set validation. No shared indices, another agent's files or read-only trees were modified. Supervisor adoption, remote mirrors and independent review of A053 remain pending.

**Universal bridge:** This stage moves C018 erasure B<=KI by removing qualitative primitivity and connectedness as unjustified substitutes for quantitative critical-source control, while preserving the genuine minimal-witness distinction; it supplies exact near-tensor cross-cut ledgers rather than an influence payment. No reduction in the universal constant or unpaid B term is established. The remaining step is to use all-descendant criticality at the specified failed-restriction line to obtain a quantitative structure forcing a paid erasure. That is the shortest next route to full FEI because the qualitative class has just been shown to retain the unrestricted optimal constant; another FEI bound on arbitrary near-tensor fixtures would not close the universal obstruction.
