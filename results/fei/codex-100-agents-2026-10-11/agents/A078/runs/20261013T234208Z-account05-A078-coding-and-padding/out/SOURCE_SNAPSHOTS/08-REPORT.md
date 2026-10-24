# A077 stage 3 — one shared data bit has a paid signed collision

## exact target, quantifiers, hypotheses and units

For every Boolean pair G(s,X),H(s,Y) with at most one common data bit s, disjoint private inputs X,Y and fresh fair selector z, put F=(G+H)/2+z(G-H)/2. All original inputs are independent uniform signs; entropy, Phi and logarithms are bits. Every finite adaptive data-only prefix, z unqueried and arbitrary stopping leaves, satisfies

    B_i(F)=[B_i(G)+B_i(H)]/2+D_i, |D_i|<=2Inf_i(F),
    B_T(F)=half both inherited core tree bills+D_T,
    sum_v w_v |D_i|<=2[I(F)-E I(F_leaf)].

The factor two is sharp; D may be negative. Exact terminal entropy is half both core entropies plus a two-frequency potential R. Its prefix drop has absolute value <=K consumed-data-influence, K=2+2/ln2<5; its remaining selector price is <=K remaining-data-influence. Prefix and suffix split one outer-potential reserve, while both inherited core costs stay explicit. Full FEI is OPEN.

This extends this packet's saved derivative-profile target, not the completed scalar-overcharge tests. It covers a shared DATA bit, not A091's three-output priority shared-activation-control gate.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start, supervisor snapshot 2026-10-13 22:15 UTC; B16 STREAM_NOTES.md v2 (still 2026-10-11 23:25Z); own STATUS.md; and the complete EXECUTION_PROTOCOL.json v2. The lead's majority target is already completed in our previous stage and is not repeated. New productive dependencies were consumed: A076 stage-3 REPORT, complete SHIFTED_ROW_PROOF and CLAIMS; A086 stage-3 REPORT's disjoint-child reference interface and first common-data gap; A091 stage-3 REPORT's priority-event ownership and terminal scope. A078's latest source-complete REPORT (stage 1) was read; its stage 2 is active without a new report. These sources prevent conflating shared data, priority shared controls and prescribed-reference payment.

Prior-stage conventions retained: ERASURE_REDUCTION Sections 1-2, LOG_ALLOCATION Sections 2 and 5 and ISOSPECTRAL_SPLICING Sections 2-3. The proof reconstructs all needed scalar and JS bounds, without a pending universal premise. out/SOURCE_RECEIPTS.json records paths, SHA256 and read scopes. No Brain or web query was needed and no novelty/priority claim is made.

## complete derivation or exact first unsupported line

PROOF.md Sections 1-6 is the full all-dimensional proof. Its symmetric-shift comparison is

    -Phi(u^2,d^2)/2 <= S(u,d;v) <= Phi(v^2,d^2)/2,
    S=[Phi((u+v)^2,d^2)+Phi((u-v)^2,d^2)]/4-Phi(u^2,d^2)/2.

The integral of log(1+u^2/t) reduces the upper bound to an exact comparison of two quadratic products. At a private query the only colliding rows are empty and {s}. Their comparison bills are summed jointly; the Fourier l1 norm of a bounded one-bit conditional mean is <=1, and each derivative coefficient is <=the actual queried physical influence. At the shared query, the exact four-amplitude row gives the same price by Phi(a^2,b^2)<=2|ab|. Its averaged influence is counted once.

Sharp Boolean fixture: G=-1,H=s gives D_s=1, Inf_s(F)=1/2 and zero inherited erasure. Signed fixture: G(s,x),H(s,y) each +1 only at its zero vertex, queried at x, gives D=-3/2+(5/8)log2(5)<0 by 5^5<2^12; wrapper influence is 1/4. Every cross term is kept; common-frequency additivity is not assumed.

The exact influence identity Inf_i(F)=[Inf_i(G)+Inf_i(H)]/2 and physical telescope pay sum w|D| at two consumed influences. Direct Fourier counting gives H(F)=half[H(G)+H(H)]+R, with both exact terminal core entropies. The JS node bound pays |Delta R| at K Inf_i(F). A complete data-first continuation has R=0 at constant/character wrapper leaves, so R<=K I_data. A partial prefix splits the same reserve between consumed and remaining data influence; an optional selector suffix uses only the remaining part. Neither the inherited core erasure nor their terminal entropies are paid by the outer bank.

REVIEW_A076.md independently reconstructs the stage-3 equations (1)-(8) of both A076 v3 bundles: HOLDS at those locators, without repair. It does not accept their earlier bundled claims. The reconstruction uses the new integral route and independent truth-table/prime-log code, not the author's checker.

First unsupported universal line: a dimension-independent source-owned correction for multiple shared-frequency bits, whose common-mean Fourier l1 norm need not be <=1, together with paid inherited terminal core costs. Reusing this one-wrapper outer reserve along a selector hierarchy without ownership accounting is also unproved.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded the pilot. Pilot: 16 labelled shared-literal core pairs, 48 prefixes, 277 exact assertions, 0.00713 helper seconds. Full domain: all labelled private widths (0,0),(0,1),(1,0),(1,1),(2,0),(0,2), 2,448 roots, plus 36 fixed (2,2) fixtures, totaling 2,484 roots and 7,452 trees. Policies: complete first, complete last and one-query maximum current wrapper influence, first-coordinate tie break. No symmetry quotient. Biased/constant cores and irrelevant shared bits remain included. REVIEW_FROZEN_SPEC.json preceded the additional potential checks on this same domain.

Final main result: 282,333 exact assertions PASS in 7.84118 helper seconds. The initial erasure-only run passed 206,789 in 5.31212 seconds before potential checks were added. Independent A076 review: all 278 cores through n=3, both signs, 556 wrappers, 1,668 trees, 71,988 exact assertions PASS in 1.74991 seconds. Total final main plus review: 354,321 checks. No mathematical failure occurred.

Commands from the agent root:

    python -X utf8 runs\20261013T222235Z-account05-A077-sparse-defect-towers\code\check.py pilot
    python -X utf8 runs\20261013T222235Z-account05-A077-sparse-defect-towers\code\check.py full
    python -X utf8 runs\20261013T222235Z-account05-A077-sparse-defect-towers\code\review_a076.py

Integer FWHT and physical pivotal counts reconstruct Boolean spectra/influence. Exact rational prime-log dictionaries certify equalities; rational intervals certify signs, with exact symbolic zeros at boundaries. Log-prime intervals use dyadic reduction, positive 32-term atanh series, tail 2t^65/[65(1-t^2)], positive ln2 interval division and outward 2^100 rounding. Potential tests use the valid rational upper price 5; the analytic bound is K=2+2/ln2<5. Runtime is the only floating metadata. Estimated memory: main 120 MB, review 80 MB, below the 300 MB memok trigger; no peak measurement is claimed. Every job ran below 60 seconds; no GPU, background worker, automatic dimension expansion or other-agent write. The infinite-domain result rests on the proof.

## proof dependencies and changed downstream conclusions

The new theorem is self-contained, reconstructing its envelope and JS bound. A076's stage-3 shift is consumed and independently reviewed only at the exact new locators. No unreviewed universal claim is used. This finishes the packet's current narrow transport extension and supplies a scoped independent review before one new application; retired point-defect and majority tests stay retired.

A076/A078 receive the sharp actual paired-row price; A086 the first common-data-bit erasure/entropy interface, without payment of its prescribed-reference deficit; A091 the three-output scope guard; A064/A097 the single-use outer prefix/suffix reserve with both terminal core costs retained. No dependent universal theorem or shared-index adoption is claimed.

## one next mathematical action and independent reviewer

NEXT: test a two-bit shared conditional-mean profile, especially bent means against a rare physical derivative, using the exact Phi comparison rows and both inherited core bills. Prove a linear exclusive reserve or construct an actual Boolean prefix falsifying the one-bit l1-payment extension. Independent reviewers: A092, alternate A088; A076 can challenge signed prefix ownership and A086 terminal normalization.

## actual persistence receipts or precise save blocker

All four protocol files, proof and TeX summary, main/review frozen specs, scoped review with original statement hashes, code, exact outputs and MULTISCALE_COST_LEDGER.json are saved in this run. STATUS.md is two lines; WORKLOG.md appended; LEARNED.md updated. out/ARTIFACT_MANIFEST.json records local hashes/bytes after protocol field and compatibility-copy checks. Files are below 20 MB. Independent acceptance of the new theorem, supervisor copying, B20 adoption and remote mirror verification are not claimed. Shared trees remain read-only.

## Universal bridge

This stage moves C018/C019 past the completed one-control shift to the first shared-data collision: arbitrary two-core wrappers with one common physical bit admit an exact signed correction paid at the sharp factor two along every adaptive data prefix, and a terminal-inclusive outer-potential reserve K=2+2/ln2<5 split once between consumed and remaining data influence. The inherited erasure and both arbitrary core entropies remain unpaid, and multiple shared frequencies can invalidate the key l1 step. NEXT tests that first two-bit profile with a rare derivative because it directly decides whether this retained-profile ownership extends toward the universal bridge, rather than improve another closed class constant.
