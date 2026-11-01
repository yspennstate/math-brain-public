# A043: exact disjoint prime decomposition and its FEI endpoint

## exact target, quantifiers, hypotheses and units

For every finite-dimensional Boolean sign function, remove irrelevant physical coordinates and factor under genuine disjoint one-bit substitution. Define the remaining essential primes exactly, including the convention that constants and unary literals are terminal rather than prime, every essential binary gate is prime, and parity of arity at least three decomposes. Prove termination, inheritance of induced product laws, and the implication of a dimension-independent corrected FEI+ theorem for all primes at all interior product biases. Entropies are in bits; biased influence is spectral influence, not unweighted pivotal probability.

Completed result: the universal corrected product-biased FEI+ endpoint is equivalent, with the same constant, to that endpoint on the precisely defined prime class. Either endpoint with constant C implies ordinary uniform FEI with constant max{C,log2(e)}. This is a proved conditional implication; its antecedent remains OPEN. No proof or disproof of full FEI is claimed. The supporting definitions and complete proofs are in PRIME_GATE_DEFINITION.tex and PRIME_ENDPOINT_IMPLICATION.md.

## sources actually read, revisions and theorem locators

Execution protocol revision 2026-10-11-execution-v2 was read in full. README, CURRENT_STATUS, claim/obstruction/packet registries, STREAM_NEXT_ACTIONS, the campaign plan, and the A043 assignment contract were inspected. CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING, the twelve supplemental source notes, and the earlier B05/B09/B19 reports were loaded and inspected for relevant routes and scope guards. out/source_manifest.json pins all 35 files actually loaded; out/source_excerpts.txt records targeted locators. Loading entire text is not a claim of reconstructing every theorem in those sources.

The 38-page threshold text Section 6.1 defines the corrected product entropy; Section 7 Proposition 7.1, equations (67)-(70), supplies the exact composition identities, and Corollary 7.2 gives constant-preserving closure. The same passage was read from baseline/current-threshold-paper.tex at labels comp:identities, comp:eq-6-1 through comp:eq-6-4, and comp:closure to remove PDF-extraction ambiguity. Its Section 7.2 full-entropy conclusion agrees with the elementary empty-atom argument reconstructed here. The earlier 29-page threshold version and both percolation versions were inspected for product-basis conventions and relevant passages; no geometric percolation theorem is a premise. Legacy text decoding is cp1252 when UTF-8 fails.

BOARD.md was read at stage start and again while collecting sources. It initially showed A043 unstarted and A056's composition baseline complete. A056's original REPORT.md was read and used as a normalization cross-check, not as an assumed new unreviewed theorem: its product identities are independently reconstructed here from the primary local manuscript. The later board reports A091's acceptance of A056, but that acceptance is not needed in this proof. claude/B09/STREAM_NOTES.md was absent; no lead direction could be consumed. The B09 physical-uncertainty claim and its tax-optimality assertions are not used.

## complete derivation or exact first unsupported line

For an essential n-input function and a proper block B with 2<=|B|<=n-1, list the cofactor row r_a=(f(a,b):b on B-complement) for every assignment a to B. A factorization f=g(h(x_B),x_Bc) exists exactly when these rows have two distinct values. Necessity is the binary range of h and exclusion of irrelevant block variables. Sufficiency labels the two rows and makes h their label. Both factors are essential: an irrelevant h input would be irrelevant in f; the new g wire is essential because the rows differ; the other g inputs remain essential by surjectivity of h.

Splitting a block of size k produces arities k and n-k+1, each strictly below n. Induction produces a formula with distinct physical leaves and prime internal gates. The new wire in the outer factor occurs once by induction and is replaced by the inner formula; this preserves disjoint physical support at every internal node. There are at most n-1 nonunary internal nodes and depth at most n-1, but the entropy reduction below needs no factor depending on depth. No canonical or unique factorization is asserted. Any nontrivial simultaneous disjoint substitution yields such a block, so the criterion covers the intended general notion, not just a special binary outer gate.

The class has unbounded arity. Signed parity, AND and OR split off pairs above arity two. Conversely every symmetric threshold at 2<=t<=n-1 is prime: for a block of size k and complement size d, the possible cofactor thresholds t-j, j=0,...,k, clipped to [0,d+1], occupy at least three distinct integer positions. The exact interval calculation U-L>=2 is given in the definition file. Factoring does not leave a fixed finite gate basis.

Under any interior product physical law, every nonconstant child has both output signs with positive probability. Disjoint supports imply independence, so a parent inherits the product law with precisely those means. Nonconstant child variances v_i are positive. This law generally differs from the uniform law, even when the original physical inputs were uniform. The literal/constant conventions prevent zero-variance divisions.

Write Hplus_mu=sum_{S nonempty} fhat_mu(S)^2 log2(sigma_S^2/fhat_mu(S)^2), with sigma_S^2 the product of physical variances, and delta_mu=I_mu-Var_mu. For F=g(f_i), centered child expansions and disjoint blocks give the unique union coefficient formula in PRIME_ENDPOINT_IMPLICATION.md. With alpha_i=I_i^eta(g)/v_i it yields

    Hplus_mu(F)=Hplus_eta(g)+sum_i alpha_i Hplus_mu_i(f_i),
    delta_mu(F)=delta_eta(g)+sum_i alpha_i delta_mu_i(f_i).

All alpha_i and deficits are nonnegative. A single constant C valid for all primes and all induced interior product laws therefore propagates from literals to the root. Conversely all-function corrected FEI+ includes the prime class, proving the endpoint equivalence. On the uniform physical cube, H=Hplus+h0 and h0<=log2(e) Var, so H<=max{C,log2(e)} I. The required scalar inequality follows from -t ln t<=1-t for t in [0,1].

For residual D_C=Hplus-C delta, the exact same identity shows that a positive corrected deficit somewhere in a formula has a positive prime descendant under its actual induced product law. This is a localization statement, not an entropy payment and not a uniform FEI counterfamily. The exact remaining unsupported mathematical assertion is the existence of one finite C for all prime arities and all interior biases.

Uniform-only gate estimates cannot be substituted into this proof. The prime root in majority_3(AND_2(x1,x2),x3,x4) receives biases (1/4,1/2,1/2) from uniform physical inputs. The first unsupported step is applying a uniform prime estimate at that nonuniform root law. Ordinary H<=CI bounds also omit the deficit cancellation needed to prevent a charge accumulating at every gate. This report proves failure of those proof substitutions; it does not claim impossibility of every other abstract reduction from ordinary uniform prime FEI.

## executed validation with domain, arithmetic, commands and outputs

Each search specification was saved before execution. out/FROZEN_SPEC.json records the initial helper, out/FROZEN_SPEC_V2.json the optimized bounded helper, and out/FROZEN_SPEC_INDEPENDENT.json the alternate finite reconstruction. All finite checks use exact integers and truth-table equality. No floating entropy computation or numerical sign claim is used.

The first helper did not return promptly and was stopped through its own exec session with Ctrl-C. It saved no census; no result is inferred from it. Its end-of-dimension runtime check was insufficiently frequent. Version 2 precomputes index layouts, caches only small certificates, rejects a candidate block upon its third row, checks time every 256 truth tables with a 50-second stopping threshold, and saves each completed dimension. That change is recorded as an implementation failure and correction, not three mathematical failures of the same mechanism.

From the A043 folder, the commands were:

    python -X utf8 runs/20261011T221757Z-fleet05-A043-prime-gate-decomposition/code/check_primes_v2.py 3
    python -X utf8 runs/20261011T221757Z-fleet05-A043-prime-gate-decomposition/code/check_primes_v2.py 4
    python -X utf8 runs/20261011T221757Z-fleet05-A043-prime-gate-decomposition/code/check_independent.py

The completed pilot took 0.007010200060904026 computation seconds and passed 1,487 assertions. The completed main census took 39.017291600001045 computation seconds and passed 205,811 assertions, covering all 65,812 labeled tables in dimensions one through four, with no symmetry reduction. For essential functions it certifies: n=1 has two terminal literals and zero primes; n=2 has 10 primes and zero decomposables; n=3 has 104 primes and 114 decomposables out of 218 essential functions; n=4 has 57,240 primes and 7,354 decomposables out of 64,594 essential functions. Every selected split was reconstructed for every input and both essential factors recursively checked. Threshold prime/decomposable classification was verified throughout this tested range. The outputs are out/pilot_census.json and out/main_census.json.

The independent finite reconstruction generates all 768 labeled three-variable binary substitutions instead of relying on the row criterion, and compares the generated essential truth tables against the criterion on all 218 essential three-variable tables. Its saved counts and assertions are in out/independent.json. This is a different implementation by the same agent, not independent reviewer acceptance. All searches are fixed at n<=4, with memory estimates below 30 MB. No heavy job, GPU, or dimension escalation was used. Finite verification corroborates the analytic proof and is not an inference to arbitrary dimension.

## proof dependencies and changed downstream conclusions

Only elementary essentiality and truth-table arguments, normalized product Fourier expansion, Parseval, and the source-complete composition identities are used. The local proof reconstructs those identities, so no unresolved campaign candidate is a mathematical premise. Exact primary source bytes and theorem locators are pinned in out/source_manifest.json. One bundled claim records the factorization and conditional endpoint rather than claiming a newly solved universal bound.

A044 receives an explicit cofactor test and an unbounded prime family. A059 receives terminating decomposition, disjointness, inherited means, and transport without a depth penalty. A091/A090 receive the full bias quantifiers, literal/parity conventions, and an exact test domain. B20 can adopt this as the A043 packet artifact once reviewed. The broad all-prime corrected theorem is as strong as the all-function corrected theorem; it is not advertised as an easier solved input or as a converse equivalence with ordinary uniform FEI.

## one next mathematical action and independent reviewer

Next mathematical action: A044 should take a proposed non-symmetric gate family, apply the exact cofactor criterion, and target a bias-uniform corrected entropy estimate on its surviving prime members; any full prime theorem must retain all arities and all induced biases. This consumes the finished reduction instead of repeating composition identities or enumerating larger truth-table dimensions. Independent reviewers are A091 (primary) and A090 (alternate). A091 should reconstruct the cofactor criterion and the product-entropy cancellation, and check that uniform-only hypotheses are not imported into biased nodes. No message was sent to another agent or shared index modified.

## actual persistence receipts or precise save blocker

All proof, specifications, code, exact outputs, and protocol-shaped records are saved inside the assigned A043 run directory. STATUS.md, WORKLOG.md, and LEARNED.md are saved only at the A043 root. out/receipts.json contains local sizes and SHA256 hashes, and out/schema_check.json records required-field and census checks. No git operation, brain write, shared-index edit, or modification to another agent's folder occurred. Independent review, supervisor copying, remote mirror verification, and downstream mathematical use remain pending; the receipts establish local persistence only.

**Universal bridge:** This stage moves B09's assigned prime-gate endpoint by completing its structural reduction and quantifier audit: all-function corrected product FEI+ is reduced exactly to essential primes with all biases and arities, with no entropy overhead, and implies ordinary full FEI with constant max{C,log2(e)}. It pays none of C018/C019/C020/C024's open entropy costs and proves no finite prime constant. What remains is a genuinely new prime entropy payment; the prime class already has unbounded arity and comprises 57,240 of the 64,594 essential four-input functions. The shortest next route is to prove or obstruct a bias-uniform payment on surviving prime structure using A044, retaining the all-prime endpoint as the precise full-theorem obligation, rather than repeat isolated balanced composition or larger finite censuses.
