# exact target, quantifiers, hypotheses and units

A054 / B11, run 20261011T224200Z-account05-A054-connectedness-alternatives.
For every finite-cube indicator and every component-isolating physical
block, prove raw Fourier entropy is at most the sum of actual-component
raw entropies plus an independently defined interface. Pay this interface
on the stated class of disjoint subcube-cylinder components fixing at
least half the coordinates of a proper selector block. Derive exclusions
for physical raw-ratio-critical sources and actual Boolean signs critical
under every proper physical restriction. All new entropy statements use
bits. Historical raw counterexamples use natural logarithms, explicitly
retained by the checker. Indicator Dirichlet energy E and sign influence
I=4E are distinct. Constants are excluded from ratios.

# sources actually read, revisions and theorem locators

Read the entire EXECUTION_PROTOCOL.json, revision
2026-10-11-execution-v2, then README, CURRENT_STATUS, CLAIM_REGISTRY,
OBSTRUCTION_REGISTRY, PACKET_STATUS, STREAM_NEXT_ACTIONS, A054 assignment
and the plan's B11 execution contract (lines 830--860). Earlier shared
B05/B09/B19 reports were inspected; their results are background guards,
not premises. BOARD.md was read at stage start (22:37 UTC snapshot) and
again during validation. claude/B11/STREAM_NOTES.md was absent, so no
direction from it is asserted or overridden.

Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and
NATIVE_MAPPING were read, with source notes ADDENDUM_11_44 and
BLOCK_RESTRICTION_IDENTITY sections 1--3 analyzed in detail. Remaining
source notes were loaded and hashed for navigation; no exhaustive reading
of unrelated routes is claimed. Both threshold versions and both
percolation versions were loaded; introductory scope and theorem excerpts
were inspected. Current threshold Proposition 7.1, Proposition 8.9 and
Corollary 8.10 provide composition/activation calibration; percolation
Theorems 1.1--1.2 concern different geometric criticality and are not
premises. out/READ_EXCERPTS.txt records relevant local excerpts and
out/SOURCE_MANIFEST.json pins local bytes and decoding.

Read A051/A052/A053 REPORTs; A052 CRITICAL_SOURCE_STRUCTURE.tex and
CLAIMS.json were independently reconstructed in REVIEW_A052.md, with
ACCEPT_AT_STATED_SCOPE verdict without repair. This addresses the B11
two-candidate review cap before creating one bundled A054 candidate.
Source review/adoption and independent review of A054 remain separate.
The seven-bit original component report was read from A052's saved
out/COMPONENT_RATIO_SOURCE.md, whose remote source pin is
31c201a0a8caef323c65abe964ff8ed4b702fc81, blob
978c180155e1a25d4d8f34988b5216269c7b83c3. The nine-bit source is the
supplement's ADDENDUM_11_44, pin 1517573ec0b37bd7aeb6a285562a6763059c5a20.
These are existing controls, not newly discovered counterexamples.

# complete derivation or exact first unsupported line

CRITICAL_INTERFACE_PAYMENT.md sections 1--5 contains the complete proof;
COMPONENT_EXCESS.tex supplies the concise theorem interface. The exact
raw block drop is B_A+(1/ln2)sum_t Ent(v_t²), where B_A is the mass-weighted
conditional selector spectral entropy. Unlike Boolean signs, indicators
have child-mass tilt, and their normalized channel includes
D(P_X||Uniform) in addition to mutual information. This term is retained.
Cube logarithmic Sobolev pays the squared-amplitude entropy by
(2/ln2)E_A, with a self-contained two-point proof and tensorization.

When each physical selector fiber meets at most one actual component,
the child raw entropies sum exactly. This gives the component comparison
with Gamma=[B_A+kappa E_A-sum_k Lambda_A(g_k)]_+, where the component
credits are explicit partial-Fourier quantities. No entropy gap defines
Gamma. For selector subcube cylinders, Lambda_A(g_k)=2d_k p_k=4E_A(g_k).
If d_k>=|A|/2 then E_A>=|A|p/4 and Gamma<=kappa E_A. Energy additivity
gives a corresponding ratio-max bound WITH its interface retained.

The exact criticality line is Rraw E_A<=Lambda_A; it gives
Rraw<=4+2/ln2 on the thin-cylinder critical class. For actual sign
criticality, R I_A<=H(f)-average H(children)<=|A|+kappa I_A and
I_A>=|A|p. Hence R<=kappa+1/p0 when p>=p0; in particular
H<=(4+2/ln2)I on the stated critical class with 1/4<=p<=1/2.
Threshold-critical witnesses at K>=kappa+1/p0 are likewise excluded.

First unsupported universal line: every prospective dimension-minimal
violating sign admits this separator geometry with uniformly positive
support density, or another affordable proper-block descent. Rare
support, non-subcube components and unrestricted terminal cores remain
unpaid. The geometric class can admit arbitrary data cores, but their
criticality is not inherited or asserted. Full FEI remains OPEN.

# executed validation with domain, arithmetic, commands and outputs

Frozen specification: out/FROZEN_SPEC.json. Its table/block count was
corrected from a clerical 1814 to 1844; this changed no helper, family,
dimension, arithmetic or runtime limit. Executed from A054:

    python -X utf8 runs\20261011T224200Z-account05-A054-connectedness-alternatives\code\read_sources.py
    python -X utf8 runs\20261011T224200Z-account05-A054-connectedness-alternatives\code\check_components.py --pilot
    python -X utf8 runs\20261011T224200Z-account05-A054-connectedness-alternatives\code\check_components.py

Pilot PASS: 22 indicators through n=2, 52 block cases, one thin-cylinder
fixture, 948 assertions, helper runtime 0.035489 seconds. Full PASS:
278 indicators through n=3, all 1844 nonempty table/block cases plus two
historical block controls, 1702 component-isolating cases, 507 thin-cylinder
fixtures, 48,045 assertions, helper runtime 7.742993 seconds. Tool/shell
latency is separate from helper runtime. Full results: out/EXACT_CHECK.json.

No symmetry reduction for the truth-table census. The thin fixtures
are all 13² ordered pairs of connected nonempty two-bit data supports at
selector (r,d)=(2,2),(3,2),(4,2), with fixed separated selector subcubes;
no exhaustive claim for all cylinder geometries. Historical supports have
sizes (40,1) and (96,1); energies independently recover 103/256 and
329/1024. The nine-bit natural raw excess is certified >1/5000. The
seven-bit raw ratio failure is certified by independent integer-power
comparisons 3^45*5^25>2^128 and
2^23552>3^1620*23^2645*41^1681.

Walsh sums use integers, direct transforms independently match FWHT;
physical edges, energies, masses and spectra use Fraction. Entropy
identities compare exact rational prime-log vectors. Inequalities use
24-term rational atanh-series enclosures with range reduction and tail
2z^(2m+1)/((2m+1)(1-z²)), z<=1/3; signed interval combinations respect
coefficient signs. No floating entropy sign is a certificate. Runtime is
floating metadata only. Frozen memory estimate was 90 MB; actual peak
RAM was not measured. No heavy job, dimension escalation, GPU or process
intended to outlive its command was used. Analytic proofs supply all
dimensions and criticality consequences; finite checks alone do not.

# proof dependencies and changed downstream conclusions

The new bundled A054 theorem is self-contained, using raw entropy
expansion, the supplied elementary cube log Sobolev proof, subcube
Fourier coefficients and physical criticality averaging. A052 v1 is
independently analytically reviewed as a related stronger syndrome
interface, but is not required as an unreviewed premise. No paper or
pending agent result is needed to establish the new statement.

A052 receives an explicit component interface and a proved critical
class payment; zero-interface component pruning remains refuted. A055
should attack universal admission of the geometric/density hypotheses
and preserve all proper-child tests. A026/A028 can use the direct
threshold-critical separator descent exclusion, retaining terminal
entropy outside this class. A090/A094 are nominated independent reviewers;
neither acceptance nor supervisor registry adoption is asserted.

# one next mathematical action and independent reviewer

Next mathematical action: use the all-proper-descendant inequalities to
test whether a high-ratio minimal sign witness with non-subcube selector
components has a proper separator whose explicit component Lambda
credits still pay Gamma, retaining the support-mass tilt. A090 should
independently reconstruct the raw block ledger and cylinder credit;
A094 should challenge criticality, density admission and unit conversion.
Do not enlarge the completed small-cube census absent a new dependency.

# actual persistence receipts or precise save blocker

All artifacts are saved only in A054: REPORT.md, CLAIMS.json, PROGRESS.json,
PACKET_DELTA.json, the two assigned mathematical deliverables, REVIEW_A052.md,
code, frozen spec, source manifest/excerpts and exact outputs. Rolling
STATUS.md, WORKLOG.md and LEARNED.md are current. out/RECEIPTS.json records
byte sizes and SHA256s after final generation. Shared indices, source
trees, other agents, brain stores and trading directories were not
modified; no git or outbound messages were used. Supervisor copying,
mirror verification, adoption and A054 independent acceptance are pending.

# Universal bridge

This stage advances C018 erasure payment toward C019 stopping-tree
payment: it turns arbitrary component deletion into a physical-block
ledger, retains mass-tilt and conditional spectral entropy, and pays the
interface at kappa E_A on thin selector cylinders. At K>=4+kappa it
excludes actual threshold-critical signs in the stated density range.
What remains is universal admission or a broader separator with enough
explicit component credit, followed by nonreusing tree payment including
terminal entropy. Testing those credits against all-descendant criticality
is the shortest next route to full FEI because it directly targets the
missing universal proper-block selection, rather than adding another
unrelated class or reviving false component pruning.
