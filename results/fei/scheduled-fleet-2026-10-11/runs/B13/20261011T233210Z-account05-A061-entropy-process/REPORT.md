# A061 stage 2: sharp point-function restriction and KL certificate

## exact target, quantifiers, hypotheses and units

Follow the B13 lead's v2 target: hand the source-bound log-charge sandwich and KL form to A087, then determine the exact minimum coordinate entropy-decrement/influence ratio for every dimension of a point function. For f_{n,x0}=1-2 1{x=x0}, every n>=1, every uniform-cube vertex x0 and every coordinate i, determine D_i/d_i and lambda_i/d_i, prove their all-dimensional maxima and tails, and deduce the sharp fair-tree drift price. Entropy and KL use bits; d_i is ordinary queried influence. Only a single new bundled claim is opened. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

BOARD.md snapshot 2026-10-11 23:29 UTC was read in full at stage start. B13/STREAM_NOTES.md v2 (2026-10-11 23:1xZ), including its specific A061 point-function target, was read in full. Own STATUS.md and prior PROGRESS.json were read. The lead's CLAIMS.json from 20261011T223500Z-claude-B13-logcharge-sandwich was read: B13-LOGCHARGE-KL-FORM v1, B13-LOGCHARGE-SANDWICH v1, B13-ONE-COORDINATE-CERTIFICATE v1 and scoped numerical claims. No numerical maximum is treated as a proof. A087 CLAIMS.json and REPORT.md from 20261011T221055Z-account05-A087-restriction-referee were read for independent acceptance of both A061 v1 claims; the report's fair-filtration and scalar-bound sections reconstruct those proofs without repair. The protocol remains EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 from the first stage. Byte hashes, claim locators and exact statement-match receipts are recorded in out/SOURCE_RECEIPTS.json. Prior context papers were not reread; no paper theorem is a premise of the new point-function proof.

## complete derivation or exact first unsupported line

The full proof is saved in POINT_CERTIFICATE.md. Writing d=2^{1-n}, the spectrum has empty mass (1-d)^2 and every nonempty mass d^2. A query has a constant child and a point-function child on n-1 variables. Thus every coordinate has the same rate R_n=(H_n-H_{n-1}/2)/d. The exact closed formula is (3) of that certificate.

The all-dimensional series comparison proves R_n strictly decreases for n>=3 and tends to 4. R_1=0, R_2=4, and the sharp maximum is R_3=12-(9/2)log2 3 in (4.867,4.868), attained exactly at dimension three. This is proved analytically for all n, not extrapolated from a finite table. In particular the dimension-four rate lies in (4.742,4.743), as the lead requested.

The exact one-sided log-charge rate is L_n=1-d+d log2((1-2d+2d^2)/d^2). Consecutive rates obey (9), and their sign is exactly the sign of the polynomial 1-4d. Hence the sharp maximum is L_3=L_4=(3+log2 10)/4 in (1.580,1.581); the tail strictly decreases from dimension four and tends to 1. Direct uniform-nu computation gives KL_2(nu_i||q_i)=n-1-L_n. Thus all coordinates of these rare functions recover their growing rarity logarithm, with a sharp dimension-independent unpaid remainder below 8/5.

All nonconstant physical descendants are point functions, so C I(g_t)-H(g_t) is a supermartingale for every fair adaptive rule in this family exactly at or above the sharp class price C=R_3. At C>=R_3, the lead's minimal nonnegative reserve Q* vanishes everywhere by backward induction. The n=3 node forces sharpness of that drift price. This does not claim that the sharp FEI constant H/I of the class is the same as its sharp drift price.

REVIEW_HANDOFF.md supplies source-bound review pointers for the lead's sandwich and KL form, consuming A087's existing independent acceptance of A061's baseline. A061 does not independently accept a chain containing its own proof contribution. No shared file or another agent's folder was changed and no message was sent.

First unsupported universal line: every arbitrary Boolean function has a physical coordinate with KL_2(nu_i||q_i)>=log2(1/d_i)-K for an absolute K, or an equivalent nonreusing stopping transport. The point proof uses equal nonempty spectral masses and a constant child; these disappear under signed multi-defect interference. Neither the exact polynomial calculation nor baseline conservation supplies the general statement.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded execution. Command from A061: `python -X utf8 runs\20261011T233210Z-account05-A061-entropy-process\code\check_points.py`. All 126 actual translated point functions in n=1..6 and all 642 physical coordinate splits are checked without symmetry reduction. Integer FWHT and Fraction spectra verify coefficient signs, child coefficients, queried influence, and closed entropy/log-charge/KL formulas. Entropy expressions are exact rational linear combinations of prime logarithms, so identities are checked symbolically.

The fixed n=1..128 formula domain receives rational logarithmic enclosures from an atanh series after dyadic reduction, with an explicit geometric tail bound and signed coefficient handling. Adjacent-rate signs, R_n>4, R_n<5, L_n<8/5 and the rational constant intervals are checked exactly. Decimal values in the output are displays only. Both the initial 32-term pilot and the 64-term rerun failed to separate a high-dimensional adjacent-R comparison; these failures are preserved in out/PILOT_FAILURE.md. The second failure showed that the first precision diagnosis was incomplete: near-unit logarithms suffered cancellation in log2(2q)-1. The helper was repaired to use -log2(1/q) for q in [1/2,1), with correctly reversed endpoints, and the same domain and 64 terms were refrozen before rerunning. No mathematical statement or parameter domain changed and no floating-point substitution was made. The analytic proof closes every n regardless of this finite validation. out/POINT_CHECK.json supplies 39,870 exact assertions passed, 6.258 seconds of checker runtime, and the full rational interval endpoints.

## proof dependencies and changed downstream conclusions

The new spectra and monotonicity are self-contained. The process conclusion uses A061-FAIR-TREE-PROCESS v1, independently accepted by A087, together with the exact point-function node rates. The lead's KL identity is verified directly in this family rather than assumed from an unreviewed numerical claim. The review handoff uses B13-LOGCHARGE-KL-FORM v1 and B13-LOGCHARGE-SANDWICH v1 as claims to be reviewed, not accepted universal hypotheses. B13-J-LE-B-UNCERTAINTY and Maassen-Uffink are not used. A061's first-stage baseline is retired after the source-bound A087 acceptance; only this new bundled point certificate awaits review.

For A064/A065, point functions now have an exact all-dimensional zero-Q* control at C=R_3. A failed rule at that price on an alleged pure point function indicates a sign, normalization or reserve implementation issue. Point functions also calibrate the correct KL ownership: blind rarity grows as n-1, while the residual is bounded by 1.581. For A087/A094, the new finite checker uses independent exact spectra, rational logs and analytic tail proofs, without relying on the lead's float64 extremizer identification.

## one next mathematical action and independent reviewer

Next: derive the exact loss of the point-function KL certificate after adding signed defects, beginning with the board's B15 three-point witness in five variables and its physical descendants. Keep the source-dependent signs and retained child entropy; locate the cancellation term which can invalidate a constant-child certificate and test whether some coordinate avoids it. Independent reviewers: A087 and A094. The handoff artifact for their review is REVIEW_HANDOFF.md; no review completion is claimed for the new theorem.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, POINT_CERTIFICATE.md, REVIEW_HANDOFF.md, FROZEN_SPEC.json, code/check_points.py and its exact output are saved in the supplied new run directory. Protocol field sets and matching compatibility progress are checked by code/finalize.py. out/PERSISTENCE_RECEIPTS.json lists local file sizes and hashes. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated only under A061. Files stay below 20 MB; the small pilot needs no >300 MB memory approval. Independent review of the new claim, supervisor transfer and mirror verification remain unclaimed.

## Universal bridge

This stage moves C019 stopping-tree payment through the B13 lead's universal one-coordinate/KL target: it replaces the point-function numerical calibration by sharp, proved all-dimensional prices R_3=12-(9/2)log2 3 for entropy drift and (3+log2 10)/4 for the retained logarithmic charge, and retires the reviewed baseline. The universal gap is unchanged in scope: obtain an absolute coordinate KL remainder or a nonreusing stopping transport for arbitrary signed spectra with terminal entropy retained. NEXT targets the first signed multi-defect cancellation that breaks the exact point certificate, using an existing B15 witness rather than extending an isolated class census; identifying and paying that term addresses the same FEI-equivalent coordinate certificate, which is the shortest direct continuation of the lead's chosen universal route.
