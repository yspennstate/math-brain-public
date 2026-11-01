# exact target, quantifiers, hypotheses and units

A079 / B16 / G-PHASE-COND, stage 20261012T044009Z. Seek actual Boolean correlated auxiliary realizations and retain their full entropy and phase energy. Inputs are disjoint uniform cubes, entropy in bits, Walsh transforms normalized, and B is the true aggregate erasure sum. This stage strengthens the previous arbitrary-seed guard: pairwise distinct bent branches with genuinely dependent spectral marginals retain EVERY arbitrary seed's full H/I using logarithmic rather than linear auxiliary influence. It also closes the flat bent-branch construction as an amplifier of bounded phase-row ratios.

The finite-dimensional identities and all-t proofs are complete; universal FEI and its finite constant remain OPEN. The new result continues/repairs A079's existing packet, together with independent review, rather than opening a new universal-payment candidate while B16's broad-review queue is pending.

# sources actually read, revisions and theorem locators

Read at stage start: BOARD.md snapshot 2026-10-12 04:39 UTC; B16 STREAM_NOTES.md v2, 2026-10-11 23:25Z; own STATUS.md and LEARNED.md. Consulted the B07 lead's v2 row-payment target, A034 STATUS, and A098 learned scope/duplicate notes. The protocol remains 2026-10-11-execution-v2, previously read in full and loaded again for final schema checking. No shared status index is used as a theorem premise.

Source-complete mathematical dependency examined: A034/runs/20261011T223816Z-fleet05-A034-phase-energy-transfer/REPORT.md, CLAIMS.json, CONDITIONAL_PHASE_THEOREM.tex, theorem A034-QUADRATIC-AFFINE-ROW-CONDITIONAL v1. Its later run directory existed but REPORT.md/CLAIMS.json were absent when first inspected; no unsaved result from that directory is assumed. The original A034 version is independently reconstructed at its stated scope in REVIEW_A034.md. The original file is unchanged.

Own previous stage REPORT.md and CONDITIONAL_ENERGY_LEDGER.md were reread to avoid repeating the high-padding point-tag guard. Previous campaign/paper sources remain pinned there; no additional threshold/percolation theorem or unreviewed B16 result is needed for the new proof. Byte hashes of this stage's inputs are in out/source_receipts.json.

# complete derivation or exact first unsupported line

Complete derivation: DERIVATION.md sections 1-8, with a concise standalone mathematical companion CORRELATED_AUXILIARY_CONSTRUCTION.tex.

For k selector bits, m=ceil(log2(k+1)), N=2^m, assign c_b=e_b at k distinct B-values and c_b=0 otherwise. For ANY Boolean seed g define F_g(x,a,b)=(-1)^(a dot b+c_b dot x)g(x). Its signed coefficient is 2^-m(-1)^(s dot t)ghat(v+c_s). Every physical selector branch is bent and distinct even modulo sign. Exact H=2m+H(g), I_Y=m, I_X=I(g)+(k-2I(g))/N, H(S_X|S_Y)=H(g), and H(S_Y|S_X)=2m-I(S_X;S_Y). Marginal q(v)=(1-k/N)p_g(v)+N^-1 sum_i p_g(v+e_i).

For g_t=z product of t disjoint copies of any nonconstant seed f on n bits, k_t=tn+1 and m_t=ceil(log2(k_t+1)), this gives H(F_t)=tH(f)+2m_t, I(F_t)=tI(f)+J_t with m_t<J_t<m_t+2. The added z spectral bit detects its single tag, so I(S_X;S_Y)>=h2(1/N_t)>0. Thus actual full H(F_t)/I(F_t) tends to H(f)/I(f), with an explicit O(log t/t) error bound. The first stage's tags used m>=k+1 and bounded the FULL H/I below 3; this new logarithmic overhead preserves the FULL seed ratio instead. It is not a disproof because the arbitrary seed ratio remains unpaid.

For EVERY bent-branch address selector, the Boolean phase rows sigma_t satisfy H=d+E H(sigma_t), I=d/2+E I(sigma_t). A ratio above any C>=2 descends to a smaller actual Boolean phase-row function. Therefore flat bent magnitudes do not generate a counterexample from bounded-ratio cores. Combined with the explicit strict-dependence embedding, the optimal constant on distinct correlated bent-branch selectors equals the universal optimal constant, possibly infinity.

For arbitrary F=(-1)^(a dot b)h_b(x), aggregate erasure transports as B(F)=m+E B(h_b)+A, A=sum_j H(S_j|V,S_-j) in [0,m]. A physical b-first paired stopping tree spends internal erasure m, JS m and removed influence m, leaving E H(h_b), E B(h_b), E I(h_b) intact. An a-first split instead creates actual two-row cores G_s(x,z)=h_(s,z)(x), with B_a=1-E JS_z(G_s) and JS_a=1-E B_z(G_s). This identifies the precise colliding/nonflat boundary; it does not price a rare core query by a fixed multiple of its influence.

A034's theorem HOLDS at scope. The noncharacter code seeds fail its unit-row assumption because an actual partial row has intermediate magnitude. Character seed corner admission is exactly the affinity of the zero-code support. The earlier point tags have one admitted corner k=1,m=2; other cases fail unit amplitude or affine support. Thus these embeddings do not refute A034's genuinely structural theorem.

First unsupported universal line: extend the smaller-Boolean-phase payment to nonflat branch amplitudes, whose normalized selector rows can be zero or have multiple magnitudes, while retaining their entire conditional and terminal entropy. Alternatively asserting a finite absolute phase-core payment at the leaves is simply full FEI.

# executed validation with domain, arithmetic, commands and outputs

Three bounded helpers, each with a frozen specification before execution and each estimated below 60 MB. No >300 MB job, memok-required job, GPU, dimension escalation, git or background process was started.

1. python -X utf8 runs\20261012T044009Z-fleet05-A079-correlated-auxiliaries\code\check_transport.py: 370 root fixtures, 14932 exact assertions, 1.1085848999999826 seconds. Exhausted arbitrary phase tables (k,m)=(1,1),(2,1), plus fixed two-pair tables, all k=2 rare-tag seeds, admitted A034 controls and two small admission corners. Validated root erasure, b-first and a-first complementary identities and full physical paired trees, with actual terminal H/B/I.
2. python -X utf8 runs\20261012T044009Z-fleet05-A079-correlated-auxiliaries\code\check_basis_tags.py: final v2, same frozen domain as v1 plus admission checks, 320 fixtures, 92372 exact assertions, 0.4180057000000943 seconds. Exhausted every k<=3 seed and checked 44 specified balanced-tensor lifts. 312 fixtures were spectrally dependent, eight intentionally independent bent-seed controls. A034 admission: 44 character-affine fixtures admitted, 268 excluded by intermediate magnitude, eight by non-affine character-cell support. v1 output is preserved and not added again to totals.
3. python -X utf8 runs\20261012T044009Z-fleet05-A079-correlated-auxiliaries\code\check_a034_review.py: 1920 fixtures, 31232 exact assertions, 0.5342968999999584 seconds. All degree<=2 phases on three Y bits, all nonzero hyperplane normals/cosets and full-cell rows. Separate GF(2) polar-rank/coordinate-energy checks support the independent all-dimensional reconstruction.

Final helpers total 2610 fixture executions and 138536 exact assertions. These are not claimed to be 2610 distinct Boolean functions. Integer signed Walsh transforms, Fraction probability laws and prime-log entropy expressions certify identities without floating logarithms. Full lifted spectra were compared with the closed signed coefficients, and direct physical selector edges independently verify phase energy on tensor lifts. The largest truth table has 8192 signs. Finite checks do not replace the analytic all-t proof. Outputs and all specs are listed in PROGRESS.json and out/combined_validation.json.

# proof dependencies and changed downstream conclusions

The new reduction is self-contained: Fourier orthogonality/Parseval, character shifts, finite entropy/erasure chain rules, tensorization, the entropy bound H<=k, and the elementary log(t)/t limit. It has no unreviewed campaign theorem premise. A034 v1 is separately accepted at scope by independent signed-translation/frequency-orbit proof; A079 supplied no repair or original-version contribution.

A080 can use the logarithmic-overhead family as an exact full-ratio admission guard: a result for distinct, correlated bent branches has universal FEI scope, rather than merely forcing a conditional constant. An alleged unbounded H/I family in that class must already supply unbounded Boolean phase-row ratios. A034/A088 should retain the unit-affine-row exclusion and test the next colliding-row step rather than assuming all X restrictions remain admitted. C018/C019 consumers have exact root/paired-tree ledgers and cannot discard the terminal seed entropy or reuse the paired data influence there.

# one next mathematical action and independent reviewer

Move beyond flat bent marginals at the first a-restriction: consume A034's source-complete colliding-row hypothesis and test whether it pays the cores G_s in the complementary split identity after their amplitudes become nonflat, including their normalized conditional entropy and terminal costs against one physical influence budget. The flat mechanism is now closed as a free amplifier and should not receive another bounded-ratio scan. Independent reviewers of the new A079 lemma: A092 and A088. They should reconstruct the character-tag influence correction, the strict-dependence z event, the all-t limit and the exact paired erasure/JS split.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and byte-identical PACKET_DELTA.json are saved locally with protocol fields. DERIVATION.md, REVIEW_A034.md, the mathematical TeX companion, three helpers, frozen specs, validation outputs, checkpoints and source hashes are in this run. STATUS.md, WORKLOG.md and LEARNED.md are current. out/schema_validation.json and out/PERSISTENCE_RECEIPT.json provide final field checks and artifact SHA256/byte receipts. No save blocker. All writes stayed within A079. Original A034 and shared registry files are unchanged; supervisor mirrors, GitHub persistence and independent acceptance of the new A079 lemma are unverified.

**Universal bridge:** This stage moves G-PHASE-COND from a conditional arbitrary-seed guard with linear padding energy to a full-H/I hardness-preserving correlated Boolean realization with only O(log t) auxiliary influence, and closes flat bent marginals as an amplifier by exact descent to smaller Boolean phase cores. It also supplies C018 root erasure and C019 paired stopping transport with two bits paid per unit of removed influence and the full core entropy retained. Full FEI still needs a payment for arbitrary cores or for the first nonflat/colliding amplitude rows. Testing the source-complete A034 collision hypothesis on those exact a-restriction cores is the shortest next route: it attacks the first place the proved Boolean phase descent ceases to apply, rather than adding another flat-spectrum class certificate.
