# A006 stage 3: actual forest mass from determinant moments

## exact target, quantifiers, hypotheses and units

Packet A006, stream B02, C020 / PI-J. For every fixed finite nonconstant gate table, positive feasible fractional lambda, covered nonempty set A and eligible ownership assignment tau, I derive the exact surrogate partition mass over DISTINCT ACTUAL source-SCC partition-forest queue events. Entropy and B costs are in bits; gamma=6/5 and the baseline F statistics are in natural logarithms. The formula is b_tau times a factorial-moment evaluation of a rooted Laplacian determinant polynomial. Canonical-order determinants give a computable lower mass, and weighted determinants and e! give computable upper masses, where e is the number of forest edges. Summing over assignments bounds the complete optimized E B-H posterior cost. Parent, root and attachment choices alone do not count every actual run.

I independently accept the WHOLE A008 unequal read-once DNF forest-payment v1 at its original scope, without repair. The new determinant interface is a combinatorial cost calculation for arbitrary references, not a new universal O(I) claim or a new known-class FEI calibration. It is analytically proved and exactly checked, pending independent review. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

At stage start I read BOARD.md (supervisor snapshot 2026-10-13 21:34 UTC), B02 STREAM_NOTES.md v2 (2026-10-11 23:35 UTC), and own STATUS.md. The board's newer results supersede the lead's historical review counts; I do not treat the old counts as proof that current candidates are reviewed. The previous A006 stage had already reconstructed A008's first dictionary claim and followed the lead's majority target. This stage reviews A008's NEW unequal-block claim before the generic calculation, follows the saved determinant NEXT, and consumes A009's full-label error transfer. The protocol was reread in full, revision 2026-10-11-execution-v2. No shared index was changed.

The complete A008 stage-2 REPORT.md, READ_ONCE_DNF.tex and CLAIMS.json were read. The complete A009 stage-2 REPORT.md and FOREST_TRANSFER.tex were read: its sparse affine-plane certificate pays the full residual; its transfer (T) leaves arbitrary-density full-cost error unpaid. A009 is consumed as a source-bound next-target interface, not assumed as an independently accepted theorem or adopted wholesale review. B03/A014's current progress is consumed through the board; their projective-plane calculations are not repeated. Own earlier report/status/progress and the baseline forests.tex generator, eq:forestpacking, eq:forestconditioning, eq:forestcost and thm:posteriorforest were revisited. Earlier campaign/paper reads are retained, not restarted; no new theorem from them is assumed here. out/SOURCES.json pins actual reads and locators. No brain query or external source was needed for the determinant identity because its proof is given directly.

## complete derivation or exact first unsupported line

FOREST_MOMENTS.md gives the complete proof and exact boundary. For a fixed assignment, used gates V form the incidence graph u->v iff A_u intersects R_v. Let c be its number of source SCCs, e=|V|-c, and b_tau=2^(-B_nonroot). Introduce x_(u,j) for each owned coordinate. Edge weight w_uv=sum_(j in A_u intersects R_v)x_(u,j); use the incoming Laplacian L_vv=sum_u w_uv, L_vu=-w_uv. Define

    T_tau(x)=sum_(one root in each source SCC) product_root pi_r * det L_(nonroots,nonroots)(x).

Multilinearity of the rows selects a parent for every nonroot. Cycle choices vanish by linear dependence; acyclic choices have determinant one after parent-first ordering. Expanding each edge weight selects its attachment coordinate. Thus T is the exact attached-forest polynomial with nonnegative coefficients. This proof fixes orientation and root constraints without relying on an external matrix-tree assertion.

An attached forest with h_(u,j) children at one repeated attachment has product h! distinct sequences of child-label draws. Root order and order between different attachment coordinates stay fixed. The resulting BFS event uniquely recovers the assignment, parents, attachment multiset and chronological label sequence, so there is no extra credit for alternative descriptions. Different assignments are disjoint actual run sets. Let M map each monomial product x^h to product h!, equivalently expectation over independent rate-one exponential variables. Then

    S(A)=sum_tau b_tau M(T_tau),
    inf_eta [E B-H(eta)]=-log2 S(A).

The second identity is the already-established finite variational baseline, not a new claim. The new content computes its correct actual-run mass. This is a SURROGATE B mass, not exact queue probabilities, whose subset/count normalizers remain covered by the source K_ref I overhead.

Put T_can=T(1) and D_(u,j)=number of possible child gates at group (u,j). With rational a_D=(D+1)/2 for D>=1 (a_0=1), define T_up=T(a_D). Integer AM-GM proves h!<=a_D^h for h<=D; the multinomial coefficient proves product h!<=e!. Therefore

    T_can <= M(T) <= min(e! T_can,T_up).

Sharper rational enclosures a_D>=(D!)^(1/D) also work. For rational pi all determinant bounds are exactly rational. b_tau is generally algebraic at gamma=6/5 and is kept separate; it can be enclosed outward for numeric entropy bounds. Summation of b_tau times the lower and upper masses gives reversed -log bounds on the full optimized posterior cost. A fixed-assignment canonical posterior already attains the upper cost -log2(b_tau T_can). Bounds coincide when all D<=1. The factorial gap is sharp on actual sunflower prime tables, with e! distinct child sequences at a forced star.

SCC block triangularity gives a product of grounded non-source SCC determinants and source SCC sums of rarity-weighted principal cofactors. This computes T_can/T_up in polynomially many exact determinant operations at a fixed assignment, avoiding root-set enumeration. It does not remove the assignment sum or make polynomial factorial-moment evaluation generally cheap. Expectation cannot be factored across SCCs: a three-gate actual prime-table star has T=pi_1*x_(1,0)^2, moment 2pi_1, while multiplying SCC-factor expectations gives pi_1. The new exact boundary avoids that false shortcut.

REVIEW_A008.md reconstructs all of A008's residual <47I/10, actual nonempty cost <=[26/5+2log2(3)+2log2(e)]I, and entropy split <67I/5. Physical spectra, root odds, unique partition events and the all-width conditional-binomial payment are reconstructed independently; no repair is supplied.

The first unsupported UNIVERSAL line remains: for one globally fixed feasible prime-table reference chosen from every arbitrary Boolean f,

    v log2[product_l(1+lambda_l*pi_l)-1]
       - E_P log2[sum_tau b_tau M(T_tau)] <= K I(f)

with dimension-independent K. The exact mass calculation does not prove this expectation bound, and log2(e!) cannot be uniformly bounded by a constant times set size. No universal FEI conclusion is inferred from the finite certificates or the arbitrary-reference identity.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded execution. Pilot: every nonempty distinct conjunction-support table on two coordinates, 7 tables, 4 exact prime tables, 26 ownership cases and 26 actual queue traces. It passed 281 assertions in 0.009341 seconds. Full: every such table on three coordinates, 127 tables, including all 18 nonempty monotone nonconstant prime tables, every covered nonempty A and all eligible assignments. It checked 3,904 ownership cases and 5,264 distinct actual traces. Zero Fourier-mass sets are included for a stronger combinatorial identity. No symmetry reduction or repeated gate table is used in these tests.

Each actual Boolean truth table is transformed by integer FWHT; Parseval and independent physical influence edge counts are checked exactly. For each assignment an independent parent-map/attachment/chronological-queue enumeration is compared with exact rational determinant polynomial expansion, its factorial moment and its separate SCC-product polynomial. Actual traces are deduplicated within assignments; the proof shows assignment disjointness. Canonical lower, rational AM-GM upper, e! upper and D<=1 equality are checked. This tests the mass, not floating-point entropy signs.

The same full job independently checks the 29 read-once width partitions of n=1,...,6 against exact spectrum/hit/influence/root-odds formulas and every reciprocal rank identity used. Seven fixed sunflower forced-star certificates (e=1,...,7) verify e! chronological traces, positive Boolean Fourier mass and the explicit failed expectation-factorization witness. These are count sharpness witnesses, not another claimed FEI class result.

Full observed checker: 50,295 assertions PASS in 5.220846 seconds. Including the pilot, 50,576 assertions passed. Code/check.py uses integers, Fraction and finite polynomial dictionaries; no approximate arithmetic supplies a mathematical sign. The frozen 90 MB estimate is below the 300 MB memok threshold, no heavy job is launched, and no automatic dimension escalation, GPU, background process or window is used. Exact formulas supply the arbitrary finite-table theorem; the finite test domain is not extrapolated.

Commands from A006:

    python -X utf8 runs/20261013T214427Z-fleet05-A006-posterior-forest-optimization/code/check.py --pilot
    python -X utf8 runs/20261013T214427Z-fleet05-A006-posterior-forest-optimization/code/check.py

out/PILOT_SUMMARY.json, out/CHECK_SUMMARY.json, out/FOREST_CHECK_2.json, out/FOREST_CHECK_3.json, out/A008_REVIEW_CHECK.json and out/STAR_CERTIFICATES.json preserve the exact checks. Each completed table was also checkpointed immediately. No failed computation or floating-point optimum is represented as a proof.

## proof dependencies and changed downstream conclusions

Only the complete original forests.tex interface and finite entropy/log-sum principles are premises for interpreting B and its posterior objective. The determinant formula, factorial multiplicity, rational upper bounds and SCC factorization are proved here from row multilinearity and actual generator events. A008 is independently reviewed at its unchanged statement/version/hash; A009 motivates the next application but is not a theorem premise. Review status, artifact completion, local persistence and supervisor adoption are recorded separately.

The resulting interface applies to arbitrary support tables, including arbitrary Boolean prime tables. It replaces abstract-forest counting with exact actual-run mass and bounded determinant calculations. The SCC-expectation shortcut is explicitly false even on a positive-mass Boolean sunflower set. The e! worst-case gap is real, so determinant bounds must be used with a spectral/assignment-sensitive argument rather than assumed to produce O(I). No improved universal constant is claimed. This finishes the prior determinant NEXT and adds a whole independent review before further exploration, consistent with the review-first direction. Neither another class calibration nor another broad FEI-payment candidate is opened.

## one next mathematical action and independent reviewer

Next: replace A009 transfer (T)'s off-support worst-case B_max charge by the assignment-sensitive upper cost from canonical/weighted determinant mass, retaining the signed normalizer and all label/rank/subset terms. Seek an influence-paid expected error cost at density N*2^-w comparable to one; avoid assuming the indicator-sum approximation is small or factoring SCC expectations. The immediate deliverable should be one error-cost inequality or its first explicit counterexample for the same full ledger, not another affine-plane FEI computation. A008/A086 should reconstruct the actual child-slot bijection and source-SCC determinant formula; A094 should challenge the upper-bound orientation, expectation counterexample and universal-gap statement. No messages were sent.

## actual persistence receipts or precise save blocker

The run contains all four protocol files, FOREST_MOMENTS.md, REVIEW_A008.md, FROZEN_SPEC.json, code and exact out files. out/SOURCES.json records source byte hashes; out/RECEIPTS.json records local artifact sizes and SHA256 and exact protocol-field validation. STATUS.md, WORKLOG.md and LEARNED.md are current only in A006. All artifacts are below 20 MB. Shared trees, another agent's folder, Brain and git were not modified. Independent review of the new determinant interface, supervisor copying and mirror verification are unobserved and remain pending; no persistence blocker occurred.

## Universal bridge

C020 / PI-J moves by an exact arbitrary-reference actual-forest mass formula and computable determinant bounds, with no claimed improvement to the unknown universal K; A008's complete unequal-block cost chain also receives an independent unchanged-scope acceptance. The unresolved line is still the influence-paid spectral expectation of the joint label/rank/subset cost under one fixed prime table, particularly the arbitrary-density error sector where a raw indicator-sum approximation is inaccurate. NEXT substitutes the newly certified mass-based cost into A009's existing complete error ledger at that exact gap, preserving posterior entropy and every normalization term; this is a shorter route toward universal FEI than repeating a known class or optimizing the already refuted coordinatewise pressure.
