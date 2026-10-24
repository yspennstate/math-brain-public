# exact target, quantifiers, hypotheses and units

A053 / B11 stage 2, run 20261012T014744Z-account05-A053-near-tensor-perturbations. Follow the lead's target: quantify proper-block descent phi under one-point surgery, with a uniform explicit remainder. For every Boolean sign f on a named n-coordinate uniform cube, phi(f)=min L_A/I_A over nonempty proper blocks with I_A>0, L_A=H(f)-average H(f_a). Give precise denominator and slack hypotheses, and test the lead's proposed exact own-ratio inheritance. Entropies and logarithms are in bits. The physical cube is encoded by 0/1 coordinates. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read BOARD.md at stage start, snapshot 2026-10-12 01:41 UTC; my STATUS.md and LEARNED.md; complete EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2; B11 STREAM_NOTES.md v2, 2026-10-11 23:3xZ. The stream lead's original REPORT.md and CLAIMS.json in 20261011T230100Z-claude-B11-block-descent-recentring were read, especially R6 exact tensor descent and the A053 target. A055 independently accepted stage 1: original REVIEW_A053.md and EMBEDDING_PROOF.md sections 1--5 were read, including the stronger singleton exclusion and the warning that average deficit tests are weaker than individual descendant tests. A052's new SINGLETON_COLLAPSE.md was read: increasing the block size cannot rescue the same additive recentred certificate. This directs future use toward the full joint channel.

The stage-1 REPORT.md and HIDDEN_TENSOR_DIAGNOSTIC.md provide the accepted entropy continuity baseline; it is reproduced self-contained in the new proof rather than reopened as a novel result. Existing campaign/paper baselines already read last stage were not reread unnecessarily. No unrelated percolation theorem, pending Gross-based channel bound, or external literature premise is used. Exact local source hashes are in out/SOURCE_MANIFEST.json; no remote readback or new novelty search is claimed.

# complete derivation or exact first unsupported line

CONTINUITY_PROOF.md contains the complete analytic derivation, with NEAR_TENSOR_DESCENT.tex as a concise mathematical interface. A one-point flip affects exactly one of a block's 2^a children, giving |delta L_A|<=E_n+2^-a E_(n-a); the physical influence change obeys |delta I_A|<=2a2^-n. The E_m envelope includes dimensions zero and one, where Boolean spectral entropy is always zero, and zero old coefficients. A second continuity bound uses the full actual-query/retained-spectrum channel and common-mixture conditional entropy, with no dimension dependence on the retained spectral alphabet.

If every seed coordinate has influence at least kappa>2^(1-n), the proper-block family is unchanged and the explicit two-sided error is

    |delta phi|<=max_(1<=a<n) [E_n+2^-a E_(n-a)]/[a(kappa-2p)]
                         +4p/[kappa(kappa-2p)], p=2^-n.

The same argument bounds the H/I error. A strict seed slack larger than the sum of these errors transfers phi(surgery)<H(surgery)/I(surgery). A selected cut with I_A>2ap has a one-sided transfer without requiring healthy influence on other coordinates. Denominator assumptions and fixed physical-coordinate conventions are explicit; surgery can otherwise change which blocks are admissible.

The lead's suggested exact inheritance at equality is false. For every n>=2 the tensor parity F_n=chi_[n] has phi=H/I=0, but G_n=chi_[n](1-2*1_0), its actual one-point surgery, has phi(G_n)>H(G_n)/I(G_n). The exact residual at every proper block A is 2(n-|A|)2^-n(R_n-R_(n-|A|))>0, where R_n is the strictly increasing point-defect H/I ratio. Monotonicity is proved analytically by R_n=4-B_n/n, with B_n positive and decreasing; it is not inferred from a finite list. Both phi(G_n) and H/I are asymptotic to 8*2^-n, and 1<phi/(H/I)<=n/(n-1). Continuity holds while the exact inequality stays reversed.

CLAUDE-B11-R6@1 on exact products remains valid. LEAD_SCOPE_CORRECTION.md pins the unversioned inference that needs narrowing, independently reconstructs R6's factor-ratio clause, and distinguishes the correction from refuting R6. This actual Boolean family has defect mass tending to zero and uniformly healthy seed influences; the issue is zero slack, not a denominator pathology. It has bounded vanishing H/I, so neither a fixed positive universal descent constant nor FEI is refuted.

For n>=3 all averaged proper-block tests at C=H(G_n)/I(G_n) pass strictly, yet an edited two-bit physical child has ratio 2 greater than the root ratio. Thus averaging cannot replace the individual child tests of genuine criticality. Entropy-positive fixed cores with a fresh sign have phi=0 and a positive limiting root ratio, so the strict-slack theorem does give eventual exact descent for their surgeries. This retains the original arbitrary-core admission result and A055's criticality exclusion.

First unsupported universal line: every genuine high-threshold dimension-critical source has a quantitative factor-cut slack or another affordable proper block at one fixed finite absolute price, with full individual child/terminal deficits retained. No bound on sup_n K_desc(n), dimension-independent critical-source separation, or universal FEI constant is proved.

# executed validation with domain, arithmetic, commands and outputs

The initial specification was frozen in out/FROZEN_SPEC.json before execution. It covered 256 products of arbitrary two-bit signs, all 14 proper blocks, and parity-surgery cardinality orbits n=2,...,12. The helper also contained six fixed scalar strict-slack checks t=3,...,8 that were omitted from that prose specification; this omission is disclosed and corrected in out/FROZEN_SPEC_FINAL.json before the repeat. They are analytic inequality evaluations, not a truth-table dimension escalation or an adaptive search. No initial spec was overwritten.

Completed command, from A053:

    python -X utf8 runs\20261012T014744Z-account05-A053-near-tensor-perturbations\code\check_descent.py

The completed pilot in out/EXACT_CHECK.json passed 28,936 exact assertions, 256 product cases, 3,584 proper-block checks, 11 parity dimensions / 66 block-cardinality orbits, 28 direct physical parity-child replays and six strict-slack certificates. Measured helper runtime was 6.291945700068027 seconds, under the 60-second pilot allowance. Integer FWHT and direct physical boundaries supply independent influence calculations. Fraction arithmetic checks the spectral/actual-child marginal identity, TV, weighted child errors, denominator-aware quotient bounds and every all-essential product's phi error. The parity orbit residuals are rigorously positive by outward rational base-two logarithm bounds using 48-term atanh series with a proved tail. Exact rational endpoints are persisted in out/PARITY_CERTIFICATES.json; decimal displays are illustrative only.

A repeat of the unchanged helper after final accounting reached its internal 55-second wall-time guard and exited without completing; out/TIMEOUT.json records its partial counts. It did not overwrite the completed certificate or rational endpoints. No mathematical assertion failed on the repeat. Its cause is not measured, so no resource diagnosis is claimed. The completed pilot and unchanged helper establish the finite validation reported here; the all-dimensional statements rest on the analytic proof. out/VALIDATION_RECEIPT.json binds the helper hash to the completed output and records both executions honestly.

The frozen memory estimate is 40 MB; actual peak memory was not measured. No >300 MB job, heavy search, automatic dimension increase, GPU, background helper, or process intended to outlive its command was started.

# proof dependencies and changed downstream conclusions

The stage is self-contained: Walsh linearity, Parseval, common-mass coupling, conditional entropy chain rules, physical edge counting, exact tensor entropy additivity and an elementary logarithm derivative. Earlier accepted A053 continuity and the lead's R6 are provenance, with the needed pieces rederived; no unreviewed channel theorem is assumed. One bundled scoped extension is saved rather than opening a new broad universal candidate. Stage-1 A053 acceptance by A055 is preserved, not represented as review of this new result.

B11 lead should replace exact surgery inheritance at equality with the error/slack formulation. A051/A055 should retain the explicit individual-descendant requirement: every averaged test can pass on an edited parity near-tensor. A052 may use the full joint-channel TV continuity bound on exact cut channels, avoiding its already refuted additive beta pricing as a route to larger blocks. A090/A094 should reconstruct quotient denominators, point-defect monotonicity and the exact positive residual independently. No shared claim status or downstream version was modified.

# one next mathematical action and independent reviewer

Next: at a fixed positive descent price K, test a quantitative factor-cut slack or healthy-denominator condition on the existing higher-ratio NAND witnesses, retaining the additive surgery error and individual child deficits and using the full joint channel J_A rather than summed beta pricing. This targets the live critical-source gap; the low-ratio parity boundary is closed and should not be scanned further. Independent reviewers: A090 and A094; immediate consumer: B11 lead.

# actual persistence receipts or precise save blocker

Saved locally in the requested run: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, CONTINUITY_PROOF.md, NEAR_TENSOR_DESCENT.tex, LEAD_SCOPE_CORRECTION.md, code/check_descent.py and code/save_records.py, both frozen specifications, completed exact output, rational parity certificates, repeat timeout, source manifest, validation receipt and persistence receipt. Rolling STATUS.md, WORKLOG.md and LEARNED.md are current. Exact protocol field sets, file sizes and SHA256 hashes are checked by code/save_records.py and recorded in out/PERSISTENCE_RECEIPTS.json. Independent review of stage 2, supervisor adoption and remote mirroring remain pending. No read-only source tree, another agent folder, shared index or brain store was modified, and no tool message was sent to other agents.

**Universal bridge:** This stage moves the lead's C019 proper-block descent route by closing its requested continuity calculation with explicit block weighting, influence denominators and strict slack, and by supplying an exact all-dimensional counterexample to the overstrong own-ratio inheritance inference at equality. It pays no universal stopping-tree residual and gives no new absolute FEI constant. The remaining step is a quantitative cut or joint-channel bound on genuine high-threshold critical sources, with individual terminal deficits retained. That is the shortest next route because qualitative near-tensor admission and its equality boundary are now resolved; a further scan of parity defects would repeat a low-ratio mechanism rather than address the missing fixed-price descent theorem.
