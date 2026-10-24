# A061 stage 3: arbitrary-core padding/edit information certificate

## exact target, quantifiers, hypotheses and units

For every Boolean sign g on r>=0 uniform bits, pad by q>=4 dummy bits and flip one physical vertex. Determine the exact entropy-drift D_i/d_i, erasure B_i/d_i and one-sided log-charge lambda_i/d_i introduced at newly relevant coordinates, the old-coordinate continuity, and the retained terminal cost. This follows the prior NEXT's signed-edit admission gap while consuming the team's newer sparse-family results. Entropies and KL are in bits; influence is ordinary uniform-cube influence. The new result is a single bundled arbitrary-core theorem, not a new class census or a solution to FEI.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-13 21:55 UTC, B13 STREAM_NOTES.md v2 (still dated 2026-10-11 23:1xZ), own STATUS.md, and own earlier proof/state. The lead's point-function target was completed in stage 2 and is not repeated. The board's B13/B14 passages were re-read after the initial combined output was truncated.

Read A075 stage-2 REPORT.md, run 20261013T212622Z-account05-A075-search-to-theorem-bridge: its complete matching closure, graph/path quarantine, and biased signed-collision next target. Read A071 stage-2 REPORT.md, run 20261011T233808Z-account05-A071-search-space-design, for finite f5/f6 scope. Read A089 stage-2 REPORT.md, run 20261012T044049Z-account05-A089-repair-specialist: binary conditional-entropy continuity, newly relevant lex-tail obstruction, and raw f5 recursion. Those newer results make repeating the sparse matching or raw f5 calculations inappropriate. The f5/f6 spectra in validation are reconstructed from actual truth tables, not assumed from another agent's calculation.

Read A002 first-stage REPORT.md, run 20261011T215124Z-account05-A002-hardness-preserving-transformations, especially its full-support point-edit admission. Inspected A002 second-stage source locators for its child-certified/erasure transport boundary. A guessed stage-2 path was absent; rg found the actual 20261011T234442Z run. Full support and H/I continuity are existing baselines, not new claims here. A087's source-bound independent acceptance of A061 v1 was consumed in stage 2; this stage does not rederive that baseline. Protocol remains fei-execution-protocol/2, revision 2026-10-11-execution-v2. Source hashes and exact consultation scopes are in out/SOURCE_RECEIPTS.json. No web source, new paper theorem, Brain write or shared-ledger change is a premise.

## complete derivation or exact first unsupported line

PADDING_EDIT_PROOF.md contains the complete proof. For n=r+q, delta=2^-n and d=2delta, every newly relevant coordinate has influence d. Its exact paired packets are a_T=s d(u_T-1), b_T=-s d, where u_T is the signed old coefficient divided by d. Only K=|supp(ghat)| residual labels are occupied; all remaining labels have u=0. Thus the local ratios are baseline (lambda,B,D)=(1,2,4) plus explicitly signed occupied-packet corrections. Every formerly irrelevant coordinate has the same packet multiset.

The corrections are positive and bounded using Kd<=2^(1-q). In the notation of the proof,

    1 <= lambda_i/d <= 1+2Kd(n+1),
    2 <= B_i/d      <= 2+Kd(2n+4),
    4 <= D_i/d      <= 4+Kd(2n+7).

They tend to (1,2,4) for every fixed arbitrary core. The corresponding exact KL remainder is n-1-lambda_i/d. The new proof includes dimension-independent continuity of the one-sided conditional entropy lambda_i: its perspective is concave, and its Jensen gap is bounded by the binary mixture-label entropy. This complements the earlier B_i continuity and proves old lambda_i ratios converge as well. D_i continuity follows from the two binary conditional entropies B_i and J_i. Influences of old relevant coordinates change by at most 2delta, so their normalized ratios converge with an explicit denominator cutoff.

Consequently the edit operator acts on the three minimum relevant-coordinate ratios by the exact limits

    min_i B_i/d_i      -> min(2, min_old B_i(g)/d_i(g)),
    min_i lambda_i/d_i -> min(1, min_old lambda_i(g)/d_i(g)),
    min_i D_i/d_i      -> min(4, min_old D_i(g)/d_i(g)).

An empty old minimum is interpreted as +infinity. The conclusions are uniform in the choice of edited vertex at fixed core. The edited function has full Fourier support and H/I converges to the original core's H/I when I(g)>0. Thus the operation preserves the full-FEI hardness endpoint but cannot preserve an existential local witness above its respective cap. This generalizes A089's specific newly relevant coordinate warning to every Boolean core and adds the exact log-charge and entropy-drift operator limits; it is not a repeat of A002's full-support proof.

The all-added-coordinate stopping tree has exactly spent influence qd and terminal entropy (1-2^-q)H(g)+2^-q H(g^v), with the analogous terminal influence. The possible core deficit survives almost intact. This is why no root-only min-ratio admission proves the complete C019 bound.

The first unsupported universal line is a paid signed child/terminal reserve preserving a high local witness or carrying its residual core deficit after newly relevant coordinates are queried. Neither old-coordinate continuity nor the presence of full spectral support supplies that reserve. The exact terminal identity records the outstanding term rather than dropping it.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before execution. The first pilot found a meaningful normalization error at the r=0 constant core: the positive-dimensional 2^(1-r) granularity was applied there. It was corrected to the universal 2^-r grid before the unchanged-domain rerun. The full-domain rerun passed its mathematical checks but exceeded the original 60-second estimate and failed the runtime assertion before saving success. Both corrections are recorded in out/PILOT_CORRECTION.md; no mathematical sign failure or domain escalation was hidden.

Exact sums of log enclosures with unrelated denominators were the avoidable cost. The repaired helper rounds each proved log enclosure outward to the dyadic grid 2^-192, preserving the certificate and controlling denominator growth. A separately frozen pilot covers 16 roots/76 splits and runs below 60 seconds. The full job is frozen at 600 seconds, under 80 MB, with no >300 MB memory gate required. The domain remains 352 roots/2348 coordinate splits and 12 compressed profiles; no larger search was initiated.

Commands from A061:

    python -X utf8 runs\20261013T215821Z-account05-A061-entropy-process\code\check_admission.py --pilot
    python -X utf8 runs\20261013T215821Z-account05-A061-entropy-process\code\check_admission.py
    python -X utf8 runs\20261013T215821Z-account05-A061-entropy-process\code\finalize.py

All 278 Boolean cores r=0..3 are checked at edited old vertex zero; all 74 core/vertex pairs r=0..2 are additionally checked, including intentional duplicate cases. Four dummy bits are added. Every physical coordinate is checked with integer FWHT and Fraction probabilities, including direct child truth-table Fourier transforms. The signed local formula is reconciled with exact prime-log entropy expressions. Rigorous 64-term atanh-series logarithm intervals plus outward dyadic rounding check the analytic inequalities and old-coordinate continuity. The pilot and full certificates are saved separately as out/PILOT_CHECK.json and out/FINITE_CHECK.json.

Compressed point3, f5 and f6 support profiles at q=4,8,16,32 traverse only the original spectra (at most 64 entries), never a padded truth table. The f5 support is {0,e0,e0+e1}, physically translated/permuted from the team's path witness; f6 uses a perfect matching of the six coordinate labels. out/COMPRESSED_PROFILES.json retains full rational endpoints; decimal displays establish no sign. The all-dimensional claims follow from the proof, not these finite cases. The full job passed 35,293 exact assertions in 60.296 seconds; the compressed profiles added 48 exact assertions in 1.488 seconds, for 35,341 primary checks. The separate bounded pilot passed 1,189 checks in 0.159 seconds.

## proof dependencies and changed downstream conclusions

The new packet expansion, concavity/continuity argument, operator limits and exact terminal assignment law are proved on the page. The only mathematical campaign dependency is the independently accepted A061 v1 scalar log/JS compensation for a convenient upper bound; it can be replaced by the self-contained scalar derivation in the original report. No current unreviewed sparse-family theorem is a required premise. A002 admission and A089 continuity are prior context with the exact scope retained.

A002/A005/A075/A089 receive a universal same-operation witness-preservation obstruction with exact caps, rather than another root-spectrum check. A064 receives the arbitrary-core terminal deficit which must be owned after the cheap reveals. The stage-2 point certificate remains pending review, and the first-stage baseline remains independently accepted; no status is upgraded by this stage's algebra. The new bundled claim awaits A087/A094 independent reconstruction.

## one next mathematical action and independent reviewer

Next: use a child-certified high-ratio witness to price the terminal deficit under the exact two-child pair g and g^v after a fresh-coordinate query. A valid admission or stopping payment must keep both signed child slacks and pay the reserve once against the queried-coordinate account; root continuity alone is now ruled out. This consumes the lead's FEI-equivalent coordinate target and A064's debt interface, rather than repeating matching, point or padding censuses. Independent reviewers A087 and A094 should reconstruct the partial-conditional-entropy concavity argument, the signed G monotonicity, and the retained terminal deficit.

## actual persistence receipts or precise save blocker

The requested REPORT.md, CLAIMS.json, PROGRESS.json and matching PACKET_DELTA.json are saved in this stage's supplied run directory with code/ and out/. PADDING_EDIT_PROOF.md and FROZEN_SPEC.json were saved before final validation; successful certificates are saved as each job completes. code/finalize.py checks protocol field sets, compatibility equality, statement hash and file sizes, then saves out/PERSISTENCE_RECEIPTS.json. STATUS.md, WORKLOG.md and LEARNED.md are updated only within A061. Independent review of the new theorem, supervisor adoption and remote mirror transfer remain unclaimed.

## Universal bridge

This stage moves C019 and the B13 one-coordinate KL certificate by closing the arbitrary-core single-edit admission gap exactly: the local minimum operators have proved caps (B,lambda,D)=(2,1,4), while the same operation preserves the arbitrary core's full-FEI entropy ratio and leaves its terminal deficit with weight 1-2^-q. The advance is a universal obstruction and a dimension-independent one-sided-entropy continuity lemma, not a bound on arbitrary complete-tree cost. What remains is a signed child/terminal reserve with one owned physical influence account; NEXT isolates that surviving deficit on a child-certified witness, the shortest route to a valid universal bridge because root-only hardness admission and further sparse-class censuses cannot pay it.
