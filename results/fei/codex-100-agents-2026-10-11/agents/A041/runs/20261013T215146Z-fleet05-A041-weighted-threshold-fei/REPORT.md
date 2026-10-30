# A041 stage 3: coherent pure-sector payment, mixed reference, binary review

## exact target, quantifiers, hypotheses and units

Target: the B09 lead's all-bias, arity-independent corrected FEI+ for two-weight thresholds F=2*1{w sum_A X+sum_B Y>=t}-1, arbitrary finite A,B, real w>0,t, and independent interior input biases. Corrected entropy E uses natural logarithms, v_i=4q_i(1-q_i), P(S)=Fhat_mu(S)^2, and E=sum_nonempty P(S)ln(v_S/P(S)); Hplus=E/ln2. Delta=I-Var=sum_nonempty(|S|-1)P(S). Deterministic inputs are frozen before any division. Full two-weight FEI+, arbitrary weighted FEI+, and full FEI remain OPEN.

Proved scoped replacement: coherent averaging costs at most 3 times coefficient variance, independently of the number or probabilities of the physical slices. It pays the entire pure higher-degree spectrum in both groups by c Delta, c=460+80 ln2, and extends to every partition into equal-weight groups of an arbitrary real-weight threshold. This closes the previously unpaid pure-heavy sector; all genuinely mixed higher-degree entropy remains the precise gap. The extension is vacuous on pure higher-degree sets when all weights are distinct, and is not an arbitrary-weight FEI+ theorem.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage intake (2026-10-13 21:44 UTC snapshot), own STATUS.md and LEARNED.md, B09 STREAM_NOTES.md v2 (2026-10-11 23:33 UTC), and EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2. The lead still assigns the full two-weight target and states that review/repair precedes new broad candidates. This stage consumes that review queue and proves a scoped continuation of the existing slice mechanism; it opens no new broad universal candidate.

Read own stage-2 SLICE_DEFICIT_PAYMENT.tex, CLAIMS.json and checker; their one-exceptional-input result and deficit Gram interface are not recomputed. Re-read the baseline current-threshold-paper.tex theorem bias:strong (lines 1640-1647 in this snapshot), which gives E<=c Delta for every symmetric threshold under every product law. Read the recovered reductions/paper/biased.tex at biasfull:weightedcounter, biasfull:creditremark and biasfull:localTC. These distinguish the coefficient-one pivotal failure and conditional-input TC from spectral entropy/erasure; this stage preserves those distinctions.

Read original A042 stage-2 REPORT.md, CLAIMS.json and code/binary_certificate.py. Independently reconstructed A042-SHARP-BINARY-PRIME-ENDPOINT@1, statement hash e163ebefc916767a00214eea2d54e56e53c9666821565f612f15a7ef4f17d5e8, at its complete claimed binary/read-once scope. The new local review is in REVIEW_BINARY.md. This provides another reconstruction beyond the A045 acceptance recorded on the board; no claim of reviewing A043's bundled census is made. Exact source hashes and locators are saved in out/SOURCE_RECEIPTS.json.

## complete derivation or exact first unsupported line

The complete derivation is PURE_SECTOR_PAYMENT.md, equations (1)-(8). For psi_s(a)=a^2 ln(s/a^2), the function psi_s(a)+3a^2 is convex on |a|<=sqrt(s), including zero by continuous derivative extension. Jensen proves

    psi_s(E a)<=E psi_s(a)+3 Var(a).

This acts on coherent amplitudes; there is no slice-label entropy. For the physical restrictions f_x(B)=F(x,B), Parseval on A identifies Var_A(fhat_x(T)) with sum_{U nonempty}P(U,T). Summing over |T|>=2 and applying the symmetric-threshold baseline pays the pure-B entropy by c D_B plus its corresponding mixed variance. Reversing the groups pays pure A as well. The exact nonnegative ledger is

    Delta=D_A+D_B+M,
    D_A=sum_{U nonempty,T}(|U|-1)P(U,T),
    D_B=sum_{U,T nonempty}(|T|-1)P(U,T),
    M=sum_{U nonempty,T nonempty}P(U,T).

Together the two coherent variance costs are at most 6M, so E_pure,ge2<=c(D_A+D_B)+6M<=c Delta. For k equal-weight groups, write r(S) for occupied-group count. The exact replacement ledger is Delta=sum_j D_j+R, R=sum(r(S)-1)P(S). The summed variance overhead is at most 3r(S)P(S)<=6(r(S)-1)P(S) for every cross-group set. Thus the same pure-sector constant holds for all finite k and real weights after orientation/contraction. The universal singleton contribution is at most 4Delta nats.

The tempting next inequality E_mixed<=K M is FALSE. Actual thresholds with weights 2 on m inputs and 1 on m inputs, threshold 3m, and fair biases are conjunction signs. Every nonempty squared coefficient is 4^(1-2m), and E_mixed/M=2(2m-1)ln2 diverges. This is a route obstruction, not a counterexample to FEI+. Its mixed degree deficit still pays the entropy with asymptotic ratio 4ln2. A mixed reference must retain degree rather than price each mixed atom by mass alone.

For M>0 a complete normalized reference is the product of the mixed spectral marginals p_A/M and p_B/M. The exact identity is E_mixed=E_A^m+E_B^m+M ln M-M TC_spec. Here TC_spec measures the dependence of the two portions of a Fourier set conditioned on being mixed; it is not physical conditional-input TC. No erasure estimate is inferred. At M=0 no conditioning/division is performed.

The first unsupported line is precisely an absolute bound on E_mixed by the root Delta, equivalently a sufficient marginal-reference payment retaining the favorable spectral TC cancellation. The squared-energy Gram identity alone does not prove it. Root deficits in these formulas are explicit partitions, not extra reserves. If E_mixed<=K Delta is later proved, the displayed estimates yield Hplus<=(c+4+K)Delta/ln2; the sum of constants makes every reuse explicit. Nothing enlarges the coefficient-one pivotal-credit refutation to a larger multiplier.

The independent A042 review found no unsupported line within its exact binary claim. Direct spectra yield corner ratio 2+2[A(u)+A(v)]/ln2 and parity ratio [A(1-a)+A(1-b)]/ln2, A(z)=z ln(1/z)/(1-z), a=4p(1-p), b=4q(1-q). Strict increase and endpoint continuity prove the sharp suprema; disjoint centered-product composition propagates them exactly. REVIEW_BINARY.md gives the independent continuum reconstruction and scope exclusions.

## executed validation with domain, arithmetic, commands and outputs

Frozen before each execution: out/FROZEN_SPEC.json, its same-domain v1.1 amendment out/FROZEN_SPEC_V1_1.json, and out/FROZEN_GROUP_SPEC.json. All pilots estimated below 100 MB and capped at 60 seconds; no >300 MB job, heavy search, automatic dimension increase, GPU or background process was used. Peak memory was not measured.

Executed `python -X utf8 runs/20261013T215146Z-fleet05-A041-weighted-threshold-fei/code/check_stage.py`. Version 1.1 passed 29,006 assertions in 2.152 seconds: 400 binary cases (all 16 tables at 25 rational bias pairs), 80 genuine four-input binary compositions, 196 scalar Jensen cases, 212 actual two-weight threshold cases at all half-integer threshold cells in the frozen domain, and six conjunction formula certificates. The v1 output with 15,497 checks is preserved; v1.1 adds the exact mixed-marginal reference identity and normalization, without enlarging the domain. Rational centered finite-difference spectra independently reconstruct A042's centered-moment result. Corrected entropy identities use rational prime-log coefficient equality. Entropy inequalities use 20-term range-reduced rational atanh bounds with a proved positive remainder; equality is checked symbolically. No floating sign is a proof premise.

Executed `python -X utf8 runs/20261013T215146Z-fleet05-A041-weighted-threshold-fei/code/check_group_partition.py`. Passed 2,307 assertions in 0.133 seconds: 42 actual three-weight thresholds on group sizes (2,2,1) and (2,2,2), weights (1,2,3), every attained integer threshold, two frozen bias profiles, plus 1,092 occupation patterns. Exact outputs are out/EXACT_CHECKS.json and out/GROUP_PARTITION_CHECKS.json. Total final assertion count is 31,313; earlier v1 assertions are not added again. Finite checks corroborate the analytic proofs, and do not establish their unbounded quantifiers by extrapolation.

## proof dependencies and changed downstream conclusions

The new scoped pure-sector theorem depends only on the source-complete symmetric-threshold baseline, Parseval and the proved scalar convexity inequality. The new normalized mixed-reference identity is algebraic. The stage-2 unreviewed rank and one-heavy-input theorem are context, not premises. The conjunction obstruction follows from the actual complete Boolean family analytically, not a numerical search.

A042@1 is locally independently accepted at its original statement hash, with no repair and no contributor conflict. Only the local claim copy records this review; supervisor adoption of shared registries is pending. B09/A045 can remove pure-heavy and pure-light logarithmic payment from the two-weight open frontier and target the mixed coefficient process. A045/A090/A091 should preserve the normalized spectral marginal reference and its TC rebate, rather than import physical conditional-TC failure into a spectral conclusion. General weighted FEI+ remains open even though its pure-group contribution is now uniformly paid.

## one next mathematical action and independent reviewer

NEXT: construct a degree-weighted normalized reference for the mixed marginal coefficient process of the two-weight threshold, targeting E_A^m+E_B^m+M ln M-M TC_spec<=K Delta with one absolute K. Start from the disjoint pivotal-boundary slice Gram matrix and charge the degree-weighted mixed reserve; the conjunction obstruction rules out M-only pricing before another search. A090/A091 should independently reconstruct the convex Jensen step and the sum_j D_j+R partition; A045 should consume the reference identity with the signed bias/empty-sector conventions intact. No further binary or AND bias grid is needed.

## actual persistence receipts or precise save blocker

All four protocol files, proofs, code, frozen specifications, exact outputs and receipts are written only inside the current A041 run directory. STATUS.md has two lines; WORKLOG.md is appended and LEARNED.md records durable statements and scope limits. The saver checks exact claim/progress field sets, statement hashes, byte-identical PROGRESS/PACKET_DELTA, and every artifact size below 20 MB. out/PERSISTENCE_RECEIPTS.json records local hashes; out/VALIDATION.json records schema and receipt verification. Previous runs are preserved. Independent review of the new pure-sector lemma, supervisor copying, brain ingestion and mirror verification remain pending. No local save blocker exists.

**Universal bridge:** This stage moves the B09 lead's G-BIASED-LTF corrected prime/weighted-threshold bridge by paying both pure higher-degree Fourier sectors for every two-weight gate, and all pure equal-weight-group sectors for arbitrary real-weight thresholds, with c=460+80ln2 nats per root deficit independent of arity, bias and weight ratios. It also supplies an independent acceptance of the complete sharp binary base case and a normalized mixed-spectrum reference with an exact TC rebate. What remains is exactly the cross-group mixed-set logarithmic payment; neither full FEI nor C018 erasure is closed. NEXT targets that single conserved mixed deficit/reference obligation, whose M-only shortcut is now rigorously excluded, rather than another isolated class theorem or endpoint search.
