# exact target, quantifiers, hypotheses and units

A060 stage 2, B12 composition sharpness. Follow lead v2: determine the
singleton-log sharpness constant, test strict improvement of the monotone
outer-erasure cap when |alpha|<=1-c, and audit tensorization. H/B/L/lambda
are bits; Lambda=(ln2)lambda is nats; I is ordinary total influence.
The singleton inequality is certified on all balanced n<=4 and all odd
n=5 functions, not all dimensions. The cap saturation theorem is
all-dimensional: for every 0<c<1, the supremum L_j(alpha^2)/B_j(g) over
actual disjoint balanced-child compositions with B_j(g)>0 and
|alpha|<=1-c is 1. Complete proof and exact certificates are saved.
Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

Read BOARD at stage start, supervisor snapshot 2026-10-13 21:24 UTC;
B12 STREAM_NOTES v2, 2026-10-11 23:30 UTC; own STATUS/LEARNED and stage-1
proof/results; EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2
read in full. The lead's sharpness direction supersedes my old rolling
control-first-tree NEXT. Other board work is preserved: A056 already has
the biased interface, A057 has a scoped capped activation-bank price,
A058 has the shared-anchor correction, and A059 has the local-gate
deficit ledger and the recharged-bank obstruction. Those baselines are
not restated as new universal progress.

Read the B12 lead CLAIMS.json L1/L2/R1 statements in full. Its L1 proof
pointer REPORT.md is absent from the local lead directory; I independently
reconstruct that elementary lemma in PROOF.md section 3/REVIEW_L1.md.
REVIEW_L2.md also independently accepts the lead's original broader
4+6/e singleton-deficit lemma, while leaving the sharp global coefficient open.
Read A057 stage2 REPORT.md and PROOF.md in full, A087 stage2 REPORT.md
in full, and A058 stage2 REVIEW_A057.md plus out/review_results.json.
A087 accepts both older A057 v1 claims; A058 independently accepts the
new capped activation-bank price at its stated scope (96 fresh tree cases,
1010 exact checks). Thus the lead's older 'A057 two claims go first' review
queue has since progressed. These reviews are consumed locally, not
inferred from a status label or propagated by editing shared indices.

Previously read threshold Proposition 7.1 supplies the disjoint balanced
substitution interface; ERASURE_RIGIDITY sections 2--3 supply the X009
baseline. They are retained source pins from stage 1, not newly claimed
whole-manuscript audits. The cap proof reconstructs the required spectrum
and chi-square algebra directly. No fresh literature-priority claim or
percolation premise is made. Exact file hashes are in out/SOURCES.json.

# complete derivation or exact first unsupported line

PROOF.md contains all analytic steps and the reduction of finite
logarithmic inequalities to integer comparisons. Main conclusions:

1. Lambda/(I-1) has maximum 3ln2 on all balanced n=3,4 and all odd n=5
   functions. The complete n=4 census has 224 equality cases: 32 signed
   Maj3 juntas and 192 signed/permuted variants of a four-input selector
   that returns x3 if x3=x4, otherwise x1 when x3=+1 and x2 otherwise.
   The latter has singleton coefficients (1/4,1/4,1/2,1/2), I=3/2,
   H=3 bits and Lambda=(3/2)ln2. Thus Maj3 is not the unique equality
   function. An independent implementation reconstructs the whole n=4
   census and equality orbit classification. The sharp finite bound
   improves the LOCAL per-gate bank coefficient from 4+6/e to 3ln2 for
   balanced arity<=4 or odd arity=5 gates, retaining the terminal deficit
   reserve. No physical biased-descendant payment is inferred.
2. Let d=2^-m, m even, b quadratic bent, D=1_(y=0) and
   g_m(z,y)=D+z(b-D). This exchanges the selector frequency sectors in
   X009. Its selected outer influence is 1-d, not d. Its packet masses
   are A_T=d^2 and V_T=(sign_T sqrt(d)-d)^2. For 0<x<1,
   0<B_j(g_m)-L_j(x)<=d log2(1/x). For even m>=4, B_j(g_m)>=dm;
   hence L/B>=1-log2(1/x)/m. The ratio tends to 1 at every fixed
   x>0, and even when alpha=2^-ceil(log2 m)->0. The construction
   h(s,w)=s v(w), with Ev=alpha, realizes the coefficient using balanced
   actual Boolean inners; physical queried B_s is exactly L(alpha^2).
   This refutes any uniform strict multiplicative cap improvement based
   only on a fixed singleton gap. At x=1/4,m=100, L/B>=49/50 by an
   analytic exact bound; no large truth table is constructed.
3. The cap coefficient 1 survives outer tensor products, because packet
   homogeneity and Parseval preserve each selected B and L, and sums
   over copies add. A fixed additive term cannot rescue a coefficient
   below 1. In contrast, Lambda of a product of two balanced functions
   is zero: it is not tensor additive. One cannot erase an additive term
   in a singleton-Lambda inequality using ordinary tensor powers.

The first unsupported sharp-singleton line is the inequality
Lambda(h)<=3ln2(I(h)-1) for every balanced h in arbitrary dimension;
even all balanced n=5 remains uncertified. The first unsupported
universal FEI line is a common-reserve payment of current biased outer
packet charges, nonempty inner decrements and terminal entropy. The cap
counterexample has ample data-side influence and does not refute FEI.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before pilot/search. FROZEN_SPEC_V2.json froze
an independent n=4 reproduction, equality orbit check and two dyadic-inner
physical compositions. No dimension was raised automatically. Estimates
were 90 MB and 70 MB; no >300 MB or heavy job, GPU, random sampling or
long-lived process was started.

Commands from A060:

    python -X utf8 runs/20261013T212522Z-fleet05-A060-composition-sharpness/code/check.py --pilot
    python -X utf8 runs/20261013T212522Z-fleet05-A060-composition-sharpness/code/check.py
    python -X utf8 runs/20261013T212522Z-fleet05-A060-composition-sharpness/code/reproduce.py

Final main PASS: 314298 assertions, 4.4586026 seconds. All 78484 Boolean
tables in the frozen census domains are covered. Integer FWHT spectra,
direct physical edge counts, exact rational singleton squares and 97
prime-exponent signature certificates prove the finite inequalities.
The main also checks 12 swapped-bent cap examples m=2,4,6,8 and
x=1/4,1/16,9/16, three Maj3 physical compositions m=2,4,6, and spectator
homogeneity. Cap logarithm signs are positive-integer comparisons after
clearing rational exponents; no floating sign is used.

Independent reproduction PASS: 25765 assertions, 0.3682147 seconds.
It filters all 65536 n=4 masks by popcount 8, then uses direct singleton
character sums and direct edges, with a differently arranged integer
comparison. All 12870 balanced masks and 224 equality masks match the
first implementation. Two independently enumerated NPN orbits have
sizes 32 and 192 and exhaust the equality set. Two actual alpha=1/4
inner compositions m=2,4 use direct character sums, not FWHT.
Final total: 340063 assertions across main and reproduction. Exact
outputs are out/validation.json, out/census.json, out/caps.json,
out/integer_certificates.json and out/reproduction.json.

Two early executions stopped honestly: the first pilot incorrectly
equated a physical singleton coefficient with its influence; the
corrected pilot passed 2468 checks. The first full census had an
unsupported extra assumption that equality implied Maj3; mask 1343
disproved that assumption, not the inequality. The rerun retained and
classified all equality cases. out/PILOT_CORRECTION.md and
out/EQUALITY_DISCOVERY.md preserve these events. The frozen V2 numerical
Maj3 seed label 5951 was a transcription typo; the frozen descriptive
definition and implementation both generated actual mask 5911.
out/SPEC_CLARIFICATION.md preserves that distinction. No failed execution
is counted as a final passing certificate.

# proof dependencies and changed downstream conclusions

The sharp finite bound is proved by exhaustive Boolean enumeration and
exact integer certificates, with a separate full n=4 reproduction.
The all-dimensional cap saturation theorem derives actual spectra,
chi-square, derivative loss, balanced-inner realization and tensor scaling
in PROOF.md. No full FEI or unreviewed biased closure is assumed.
B12 L1 and L2 are independently reconstructed at their existing scopes; the imported
A057 B identity has independent A087 acceptance and is also reconstructed
by sectors. The local gate reserve is obtained by the elementary
balanced-disjoint influence identity, not by treating a physical-tree
reach probability as a formula influence weight.

A056/A057/A059 must not insert a dimension-independent factor below 1
in front of the monotone cap based solely on |alpha|<1. A059 may use the
sharp 3ln2 coefficient only in the certified finite gate library; arbitrary
balanced gates still require the proved broader constant or a new proof.
A091/A090/B20 should preserve the newly found equality family and the
nonadditivity of singleton Lambda. New sharpness claims remain pending
independent external review. No shared ledger was edited.

# one next mathematical action and independent reviewer

Next: on A057/A058's first two-core priority activation with overlapping
controls, compute the actual biased packet imbalance and identify a single
owned terminal/core reserve. Test any proposed cap saving against
g_m=D+z(b-D), which is saturated even at small alpha, and retain both
terminal core entropies. Reviewers A091 and alternate A090 should check
the integer census coverage, orbit classification, all-m loss bound and
tensor distinction. A universal singleton-Lambda proof remains a
separate conditional constant optimization, not a prerequisite for this
physical-tree ownership test.

# actual persistence receipts or precise save blocker

All run artifacts, proofs/review, frozen specifications, correction notes,
code and exact outputs are saved only under A060. Required CLAIMS,
PROGRESS and identical PACKET_DELTA fields are schema checked; the
protocol's descriptive packet_ids suffix is normalized to its actual key.
out/PERSISTENCE.json gives byte counts and SHA256 readback receipts,
including rolling STATUS/WORKLOG/LEARNED. All files are below 20 MB.
Supervisor copy, independent review, shared adoption and mirror
verification remain pending. No git, mail, brain writes or writes to
another agent's folder occurred.

# Universal bridge

This stage moves C019 by sharpening the local gate-log coefficient from
4+6/e to 3ln2 only on the certified balanced arity<=4/odd-arity-5 library,
while proving the monotone outer-erasure coefficient 1 cannot be lowered
even with singleton coefficients separated from one. It also establishes
which of these prices survives tensorization. No universal FEI constant
is reduced: biased physical descendants, nonempty inner charges and
terminal entropy still need one common, nonreused reserve. NEXT attacks
that ownership obligation on the first genuinely overlapping two-core
activation, using the saturated-cap family as a falsifier; another finite
singleton census would leave the universal transport cost unpaid.
