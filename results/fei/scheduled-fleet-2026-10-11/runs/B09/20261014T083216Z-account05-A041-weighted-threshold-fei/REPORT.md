# A041 stage 5: complete two-direction quadratic reference

## exact target, quantifiers, hypotheses and units

Continue B09's corrected FEI+ target for all two-weight thresholds F=2*1{w N_A+N_B>=t}-1, arbitrary finite groups, real w>0,t and all independent interior physical biases. P is the squared orthonormal product Fourier spectrum, v_i=4p_i(1-p_i), E=sum_nonempty P ln(v_S/P) in nats, Hplus=E/ln2 in bits, root Delta=I-Var. Mixed mass M and deficit D=sum_mixed(|U|+|T|-1)P are nonnegative. Deterministic inputs contract; M=0 involves no conditional law.

New scoped result: take the pointwise larger of the two physical quadratic tail references, then normalize on the complete mixed label space. Its normalizer is at most D+M, and its positive mass tax is at most2D/e<3D/4. The direction can depend on the whole Fourier set with its full normalizer paid. This repairs the previously uncontrolled one-direction cost on the source's actual control. The selected cross-entropy remains unproved universally; full two-weight and full FEI remain OPEN.

## sources actually read, revisions and theorem locators

Read own STATUS, updated BOARD including B09/B20 stage-5 summaries, B09 STREAM_NOTES v2 still dated2026-10-11 23:33UTC, and the execution-v2 protocol in full. The lead's two-weight target and review-first cap remain current. Read A045 run20261014T033253Z REPORT.md and CLAIMS.json: it independently accepts A041's full signed-profile/absolute-budget obstruction, and proves the new quadratic reference. Its source finalizer was read solely to verify the statement-only hash convention, avoiding the prior save assumption. Independent acceptance of our prior claim is consumed at original compound hash46a8f1202df911c49b24b18ae3eddc4e0c106c512fc043db2397ac8533ba4404.

Read A044 run20261014T055346Z REPORT.md and PROOF.md and A045 run20261014T063646Z REPORT.md. They prove the local integer-profile payment and mean-only all-pairs congestion obstruction. Those source results are context/adversarial constraints, not premises of the new two-weight reference; they are not re-exhausted. The A045 band/parity selector is explicitly treated as a different Boolean class, not misidentified as a weighted threshold. Re-read recovered paper/biased.tex at biasfull:mixture and weightedcounter for exact guard parameters. Source hashes/locators are saved in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

Complete proof is TWO_DIRECTION_REFERENCE.md. Independently reconstruct A045's K_A, where normalized physical B-coefficient profiles are expanded in signed A count tails. Distinct tails have disjoint physical derivative supports, giving sum|U|K_A=J_A=sum_mixed|U|P and Z_A<=J_A. Reverse the groups to get K_B, Z_B<=J_B. Neither reference marginal is presumed Boolean. The exact mixed ledger is J_A+J_B=D+M, so those energies are not two independent root reserves.

Set K_*=max(K_A,K_B), Z_*=sum K_*, Q_*=K_*/Z_* and R=P/M. Both references are positive on actual mixed support, bounded by v_Uv_T, and include off-support labels. Thus Q_* is complete, normalized and C_*=sum_mixed P ln(v_Uv_T/K_*)>=0. Since Z_*<=Z_A+Z_B<=D+M<=2D, exact logarithmic expansion and x ln(1/x)<=1/e give

    E_mixed=C_*+M ln(Z_*/M)-M KL(R||Q_*),
    E_mixed<=C_*+2D/e-M KL(R||Q_*).

The negative KL uses the original mixed law R; degree tilting retains its harmonic factor. No physical conditional-input TC, spectral-TC conversion or coordinate erasure is silently exchanged. The max choice avoids a separate direction label charge; its full normalizer accounts for choosing different directions on different complete sets.

The source's proposed stronger payment by one direction alone is rigorously false. On its actual family of two fair heavy inputs and n=4r+1 fair majority light inputs, J_A=1/2 for all r, whereas E_mixed=[E(g)+ln4]/4 and C_A=[E(g)+ln8]/4. Elementary central-binomial induction gives singleton mass at least1/2 and entropy E(g)>=(1/2)ln(2r+1). Therefore E_mixed/J_A and C_A/J_A diverge. This excludes the unregistered J_A-only strengthening, not A045's valid energy/reference theorem or root-Delta FEI+.

On the same control K_B=P_mixed, so K_* equals actual P on actual support, while retaining positive off-support A singleton labels. Exactly Z_*=1/2, C_*=E_mixed, KL(R||Q_*)=ln2, and the mass taxln2/4 cancels its KL rebate. This is a diagnostic of the new complete reference, not another isolated class theorem.

Recovered weighted controls survive analytically: their single exceptional physical input gives K_A=P_mixed for every label, hence C_*<=E_mixed. Their actual OR(X0,AND_lights) disjoint composition is paid by the accepted all-bias symmetric baseline at actual induced biases, so C_*<=cDelta for all m,q,eta in the recovered families, c=460+80ln2. Finite rational members corroborate the new reference; no conditional-input TC claim is used. The coefficient-one pivotal-credit failure retains that exact scope.

On A045's distinct band/parity-selector congestion fixture, the one-bit selector direction also gives K_C=P_mixed universally for arbitrary Boolean branches. This selects one complete label owner rather than repeated local pair owners. No normalization or KL tax remains, but the FULL mixed terminal spectrum still costs E_mixed. Its existing physical parity reserve gives I>=n/2 and H<=n+1, hence E_mixed<=3ln2 Delta for n=16r^2>=16. This uses the full root and terminal cost, not selector energy alone, and is not a universal selector theorem.

Exact first unsupported line: an absolute bound C_*<=KD, or an appropriate signed bound C_*-M KL<=KD, for every actual two-weight threshold under every product law. Direction selection, energy and normalization are now explicit; complete-set cross-entropy is still unpaid. If that bound holds, the previously paid pure sectors/singletons and the present mass tax give Hplus<=(c+4+K+2/e)Delta/ln2. The additive constants explicitly account for any reuse of the root upper bound. No universal constant is claimed here.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json before v1 execution; out/FROZEN_SPEC_V1_1.json freezes12 recovered-guard members before the amended runs. No automatic dimension increase. Commands from A041:

    python -X utf8 runs/20261014T083216Z-account05-A041-weighted-threshold-fei/code/check_stage.py --pilot
    python -X utf8 runs/20261014T083216Z-account05-A041-weighted-threshold-fei/code/check_stage.py

Final pilot:6,171 assertions in0.167s; main:61,804 assertions in1.990s. Main domain386 actual two-weight fixtures on frozen group sizes1+2,2+2,2+3,3+2,3+3, weights1/2,2,3, every half-integer threshold cell and two labeled actual product-bias profiles. Also two complete7-/11-bit majority-control truth tables,12 rational recovered weighted guards, six fixed count-compressed central-binomial growth records, and four fixed band/parity-selector count records with up to1024 data inputs. Large count records use exact binomial symmetry formulas, never large truth tables. Source helpers were not executed/copied.

Fraction arithmetic independently constructs complete signed physical spectra and both canonical quadratic references. Checks include both orientation energies, exact J_A+J_B=D+M, support/caps, full Q normalization with off-support labels, pointwise exact multiplicative log identities, positive mass-tax bounds, source control constants and recovered K_A=P. Entropy/KL signs use20-term rational atanh bounds with tail2z^41/[41(1-z^2)], power-of-two range reduction and outward2^-80 exports. Algebra, not interval overlap, proves logarithmic equalities. The finite maximum C_*/D upper enclosure is1725219018707061379188067/604462909807314587353088 nats in this domain only; it is not a continuum bound.

All pilots/main runs stay under the frozen60-second cap; estimated memory120MB, peak unmeasured. No>300MB/heavy job, GPU, background task, git or external write. Initial v1 main output is preserved separately; final count61,804 excludes earlier repeated assertions. No mathematical or implementation failure occurred.

## proof dependencies and changed downstream conclusions

REVIEW_QUADRATIC.md independently reconstructs and accepts A045-QUADRATIC-TAIL-ENERGY-NORMALIZED-REFERENCE@1 at its exact source statement-only hashb8364330c7795e63389748f38d6389fca6f69b6074c304f08194b342f9bb36d3, with no repair. A041 authored an earlier declared profile dependency, so this is scoped reconstruction of the new quadratic ownership/reference clauses, not a claim of wholly independent re-certification of the complete prior dependency chain. The new two-direction result is downstream work, not a repair supplied to that version. A045's source-bound review of our prior obstruction is consumed without rewriting prior runs or shared registries.

The new normalized max-reference proof uses actual coefficient profiles, physical Parseval, signed tail decomposition and elementary maximization. The one-direction lower bound uses exact majority coefficients and central-binomial induction. Recovered guard payment uses the source-complete symmetric baseline and already reconstructed genuine disjoint composition; neither new conjectural prime FEI+ nor all-pairs local funding is a premise.

B09/A045/A044 can retain one complete per-set best-direction reference with a paid mass-normalizer tax. One-direction energy cannot fund the other group's inherited entropy; summing exact mean-only local pair prices would also reintroduce the source's congestion failure. The normalized reference remains valid even where its conditional marginals are not Boolean. No registered valid theorem is refuted, and no universal erasure/tree/history-transfer theorem is closed.

## one next mathematical action and independent reviewer

NEXT: pay the selected C_* or signed C_*-M KL from the same mixed deficit, using the physical coefficient profiles in both directions and preserving the complete off-support reference. Start with a degree-rich actual two-weight gate whose preferred direction changes across Fourier labels; do not retune a single-direction scalar price or sum every local pair bill. A090/A091/A085 should reconstruct the max normalizer and all-r one-direction lower bound; A045/A044 should consume the corrected ownership scope and recovered guard tests. The complete-owner diagnostic on A045's fixture must retain the terminal spectrum rather than count it as a free refund.

## actual persistence receipts or precise save blocker

Required four protocol files, proof, review, code, frozen specifications, exact outputs and source/persistence receipts are saved only in this A041 run. STATUS.md has two lines, WORKLOG.md appended, LEARNED.md updated. Saver validates exact schema fields, both source hash conventions, original review hashes, progress-copy bytes, report fields/final bridge and file sizes below20MB. Prior runs and every read-only source are preserved. Local delivery is complete; new reference review, shared-registry adoption, supervisor copying/brain ingestion and mirror verification remain pending. No local save blocker exists.

**Universal bridge:** This stage moves B09's G-BIASED-LTF target toward C020 whole-set reference cost by constructing a complete pointwise-best two-direction quadratic reference with Z_*<=D+M and positive mass tax at most2D/e<3D/4, consuming the prior obstruction's independent acceptance and reviewing the source quadratic theorem. It closes the false one-direction-only continuation with an all-r actual Boolean lower bound, preserves all recovered weighted guards, and supplies one complete owner on the specified local-congestion control with full terminal cost retained. It gains no universal FEI constant: the selected complete cross-entropy or its signed KL remainder still needs an absolute mixed-deficit payment. NEXT attacks that single now-normalized two-direction charge, the shortest surviving route to full FEI rather than another isolated class or scalar-price grid.
