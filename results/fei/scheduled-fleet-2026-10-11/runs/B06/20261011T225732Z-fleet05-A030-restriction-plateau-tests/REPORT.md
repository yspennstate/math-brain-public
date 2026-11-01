# A030 / B06: exact restriction plateaux and terminal ratio amplification

## exact target, quantifiers, hypotheses and units

Resolve A030's coded-plateau interface for every Boolean seed g on every finite uniform cube. Outputs are signs; H is Shannon entropy of squared Fourier coefficients in bits; I is total physical influence. Establish exact all-branch bounded-depth entropy preservation, auxiliary influence cost, and what a global stopping partition retains. Per B06 lead v1, also quantify restriction amplification of H/I. This is an interface derivation, not a new broad FEI candidate. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read execution protocol revision 2026-10-11-execution-v2 in full; canonical README/status/claims/obstructions/packet/stream-action indices; plan A030 contract at lines 696-700 and B06 section; earlier B05, B09, B19 reports; supplemental CAMPAIGN/CLAIMS/COUNTEREXAMPLES/SEED_LEMMAS/NATIVE_MAPPING and source collection. Read BOARD snapshot 2026-10-11 22:57 UTC and B06 STREAM_NOTES v1 22:38Z before work. Exact observed local SHA256 receipts for 34 files are in out/source_manifest.json.

Mathematical precursors actually inspected: ES section 3, pair lift (8)-(9); ISO sections 4-5, isospectral splice and signed-symmetry peeling; seed ledger C015/X001; point-defect formula in SEED_LEMMAS section 3. The general lift is an extension of the known pair lift, not claimed as prior-art novelty. The new packet output is its quantified all-choice lookahead/terminal interface, the nonunate stopping-depth obstruction, and the unbounded general one-step amplification diagnostic.

Inspected all four local paper text files, introductions and relevant restriction/composition/scope passages. Threshold 38pp (11 October 2026), Proposition 7.1 and Corollary 7.3, section 8.3's fresh-sign tensor balancing, and section 8.4's activation reductions provide scope checks. The earlier 29pp version is not substituted for it. Percolation 30pp section 12 explicitly limits its geometric result; the other 31pp version has different overlap-conditional wording. No geometric theorem, biased composition theorem, or version-dependent percolation assertion is used in the proof. Text extracts are cp1252; exact Fourier algebra below bypasses damaged mathematical glyphs.

## complete derivation or exact first unsupported line

Write f=sum_S a_S chi_S. Fix A to rho. The restricted coefficient at T is sum_{S\A=T} a_S chi_{S cap A}(rho). If the projection is injective on occupied support, this sum has one nonzero term; hence the full positive squared-mass multiset is unchanged, H(f_rho)=H(f), and I(f_rho)=sum_S |S\A|a_S^2=I(f)-sum_{i in A}Inf_i(f). Spectral A-membership is determined by the complement, and all physical assignments have the same labelled complement spectrum: both block erasure and channel information vanish. If support distance is >=L, projection collisions require >=L deleted coordinates. Thus every adaptive tree of depth <=L-1 has zero entropy decrement on every branch. No rare-branch qualification is needed.

Construct F_L=g(y), y_i=product_j x_ij, L>=2. The seed label S maps to the union of its L-coordinate blocks. This injective map multiplies sizes and distances by L, so H(F_L)=H(g), Inf_ij(F_L)=Inf_i(g), I(F_L)=L I(g). While each block retains ell_i>=1 coordinates, the residual has H(g) and I=sum_i ell_i Inf_i(g), independently of assignments. Querying L-1 coordinates per block yields a genuine fair tree of depth n(L-1), with 2^[n(L-1)] equally probable coordinate-sign translates of g as leaves. Hence E H_leaf=H(g), E I_leaf=I(g), Pi_H=0, Pi_I=(L-1)I(g), and leaf/root H/I amplification exactly L when H(g)>0. L=2^k gives iterated pair-expansion amplification 2^k, but undoing it requires n(2^k-1) physical queries, not k singleton queries.

For nonconstant g and L>=d+2, every restriction of <=d coordinates retains at least two inputs in every block. In a relevant block, fix other block parity values witnessing a nonzero seed derivative. The derivative in one physical coordinate equals the product of its companion block inputs times that nonzero seed derivative. Flipping a second input reverses the sign. Thus the residual is nonunate, even after arbitrary coordinate sign reversals. No depth-d physical tree can have only C001-regular leaves. This does not exclude longer trees or C004-certified roots.

For amplification at one singleton step take g_r=1-2 indicator_{all+} and G_r,m=g_r product_j z_j. The fresh parity shifts every Fourier label by the fixed spectator set, so H is unchanged and I=I(g_r)+m. Every spectator restriction removes one unit of influence and changes at most the overall sign; both children have the same H and I. With p=2^-r, the core coefficients are 1-2p at the empty set and -2p otherwise, giving I(g_r)=2rp and H(g_r)=(1-2p)^2 log2(1/(1-2p)^2)+8p(1-p)(r-1). Therefore H(g_r)/I(g_r)->4, while H(G_r,1)/I(G_r,1)->0. The amplification equals 1+m2^(r-1)/r and is unbounded already for m=1 on both probability-1/2 branches. This disproves a universal amplification factor, not FEI. B06 lead's at-most-two factor is valid for C015's particular global lift, not arbitrary restrictions. Repeating that particular global lift on its even-supported output adds no further spectral coordinate. Pair expansion is the correct iterated map.

On an injective restriction of d coordinates with H>0, amplification is exactly 1+sum_{i in A}Inf_i(f)/I(f_rho)<=1+d/I(f_rho). If the residual is balanced, Parseval gives I(f_rho)>=1, so amplification<=d+1. The unbounded example has an unbalanced terminal and therefore does not violate this narrower bound.

Full proof is in RESTRICTION_PLATEAUX.tex. The first unsupported universal inference would be: 'zero paid path entropy, or zero lookahead erasure, certifies terminal H(g)<=K I(g) for arbitrary g.' That is unpaid FEI, not a consequence of these identities. A valid ratio-certified root stopping rule is not refuted; only inheritance of root ratio certification by descendants and bounded-depth C001 admission are excluded.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs precede each run. v1 stopped at the internal 59-second guard during the larger point-defect cases with no failed mathematical assertion; original source and domain are preserved. v2 reduced only the fixed verification range, from r<=12 to r<=8; no automatic dimension increase, randomization, GPU or heavy job was used. Estimated memory <30 MB, so no >300 MB allocation was planned.

Command: python -X utf8 runs/20261011T225732Z-fleet05-A030-restriction-plateau-tests/code/verify.py

Result: PASS, 28,049 exact assertions, 5.965 seconds. Exhaust all 276 seed truth tables n=1..3; 296 replicated parents (L=2 for n<=3,L=3 for n<=2); every <=L-1 restriction, 4,736 shallow nodes; all 2,392 compression leaves; 552 spectator parents with 2,760 prefix nodes; point defects r=2..8,m=1..3,21 parents and175 prefix nodes. Integer Walsh/Fraction spectra are checked against the signed label map. Entropy equalities are proved computationally by exact positive squared-mass multiset equality, with no numerical logarithms. Influences are independently computed from physical edges. out/validation.json preserves all records and the checker SHA256. The v2 frozen spec mistakenly predicted 3,744 compression leaves; that bookkeeping count is corrected by the independently enumerated 2,392 (2,120 for L=2 plus272 for L=3). All declared compression leaves were exhausted; the domain did not change.

Command: python -X utf8 runs/20261011T225732Z-fleet05-A030-restriction-plateau-tests/code/verify_terminals.py

Result: PASS, 466 exact nonunate nodes,0.0523 seconds. All nonconstant seeds in the same replicated domain, all <=L-2 restrictions, checked by integer derivative signs in each physical coordinate. out/terminal_validation.json preserves the result. This is self-validation, not independent review. Infinite parameter claims follow from the symbolic proofs, not the finite census. No certificate of a logarithmic numerical sign is needed.

## proof dependencies and changed downstream conclusions

The new claim is self-contained in the uniform Walsh expansion and physical influence definition; C001 is used only through its definition requiring unateness. B06 R2 is respected but not re-proved: the compression payment also follows directly from identical leaf H/I. C015/ES pair lift and ISO symmetry peeling are credited precursors. No unreviewed campaign theorem is a mathematical premise. One narrow bundled interface claim is recorded, with pending independent review; no new broad FEI candidate is opened against the B06 review cap.

For C019, D_K(F_L)=D_K(g)+K(L-1)I(g) exactly. The entire terminal spectrum remains. Short-path entropy-drop observations are all zero but local influence vectors still reveal Inf_i(g); no impossibility for arbitrary local information, computational hardness, or all global policies is asserted. Global code compression sees the actual arbitrary core and a changed terminal influence budget. Neither ample root influence nor a free path is a license to discard the terminal reserve.

## one next mathematical action and independent reviewer

Have A065/A064 substitute this exact compression family into an actual proposed stopping predicate/reserve, including tie-breaking and terminal class. Demonstrate where H(g) is certified or which distinct unused influence bank pays it after zero-cost peeling. Reviewers A087 and A094 should independently reconstruct the signed projection, the derivative-sign obstruction, and the all-branch quantifiers. A026/A027/A028/B06/B20 are downstream consumers.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, proof/diagnostic files, frozen specifications, code, timeout record, source hashes and PASS outputs are saved locally in this run. out/PERSISTENCE_RECEIPTS.json records byte sizes and SHA256 values after writing and verifies exact schema field sets, progress compatibility and the 20 MB ceiling. The agent rolling STATUS/WORKLOG/LEARNED files are current. Supervisor copy, GitHub mirror, independent review, registry adoption and downstream mathematical use are pending and are not inferred from local saves.

## Universal bridge

This stage moves C019 stopping-tree payment and G-R-MISMATCH by closing the exact separated-support plateau interface, demonstrating all-branch unbounded one-step ratio amplification, and forcing depth beyond fixed lookahead for C001 terminal admission. It pays no new universal entropy term: after compression the residual is exactly H(g), for arbitrary g. The shortest next route to full FEI is to test a concrete single-use terminal reserve on this paid-zero-path interface, keeping the arbitrary core in the same ledger, rather than prove another isolated parity/formula-class FEI bound already covered by the paper.
