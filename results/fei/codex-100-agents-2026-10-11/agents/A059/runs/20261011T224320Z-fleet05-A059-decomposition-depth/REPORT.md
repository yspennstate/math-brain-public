# exact target, quantifiers, hypotheses and units

A059, B12, decomposition depth. This stage resolves the lead's precise test:
whether sum_c J(c)Lambda(Sub_c)<=K I(F) for every finite balanced disjoint
composition tree, with one depth- and arity-independent K. Here J(c) is the
product of ancestor gate coordinate influences and Lambda is singleton-square
logarithmic entropy. That proposed inequality is FALSE. A source-complete
actual Boolean counterfamily is given below. A local-GATE charge and an exact
first-charge factorization are proved, including any finite stopping frontier.
No bound on formula depth or number of composition steps is assumed.
Lambda uses nats; H in the explicit family's FEI estimate uses bits. Ordinary
influence is dimensionless. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

- EXECUTION_PROTOCOL.json read in full, revision 2026-10-11-execution-v2;
  campaign README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY,
  PACKET_STATUS, STREAM_NEXT_ACTIONS and FEI_100_agent_research_plan.tex,
  especially A059's acceptance test and B12's low-energy obligation. The
  canonical index is an older snapshot than the live board. Earlier B05/B19
  and B09 reports were inspected for scope, not accepted as new premises.
- Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS and
  NATIVE_MAPPING. Relevant sources read: OVERLAPPING_PRODUCT_NOTE.md and
  BLOCK_RESTRICTION_IDENTITY_2026-09-18.md. No overlapping-product
  subadditivity or erasure-certified arbitrary leaf is assumed.
- Threshold paper 38pp, Section 7 Proposition 7.1, Corollary 7.2, and
  Section 8 selector identities; earlier 29pp version's matching composition
  scope. Percolation 30pp and earlier 31pp introductions and entropy
  conventions were inspected as background; no percolation theorem is used.
  PDF text files require cp1252 decoding here. These are focused section
  reads, not an independent audit of both entire manuscripts.
- BOARD.md at stage start (22:37 UTC snapshot), and updated B12 section
  after the 22:47 UTC snapshot. B12 STREAM_NOTES.md was initially absent,
  then appeared as v1 at 22:45 UTC and was read in full. Its A059 direction
  superseded the initial exploratory rare-leaf summability idea. The local
  Lambda<= (4+6/e)delta lemma is credited to the lead and independently
  reconstructed here. The requested whole-subformula bank is refuted, not
  silently replaced by a different assertion.
- A056 REPORT.md and A091 composition audit REPORT.md (A056 v1 accepted
  there); A057 REPORT.md, COHERENT_REMAINDER_PAYMENT.tex, CLAIMS.json,
  and preserved pinned source_proof.md, blob
  37626caf9f1564342f8b6edfff54b3a3491fff35. REVIEW_A057.md independently
  accepts both A057 v1 claims at their stated scopes. This fulfills the
  protocol's review-before-new-candidate requirement at the B12 claim cap.
  No other agent's files or shared claim statuses were changed.

# complete derivation or exact first unsupported line

PROOF.md supplies every all-dimensional step. The central statements are:

1. For balanced Boolean h, Lambda(h)<=(4+6/e)(I(h)-1). Choose the largest
   singleton coefficient a, let u=1-a and s be the other influences.
   The inequalities delta>=s-u and delta>=u(2-u)-(1-u)s imply
   u<=2delta and s<=3delta. The chosen term is <=2u; all other terms
   are <=(2/e)s. This is a proof with constants, not numerical evidence.
2. On a balanced composition tree, the exact stopping-frontier identity is
   delta(F)=sum_internal J(v)delta(g_v)+sum_terminal J(l)delta(Sub_l).
   Thus the local gate log bank is <=(4+6/e)delta(F), less any terminal
   reserve. Arbitrary refinement is monotone for each finite root.
3. If A(v) is the product of ancestor singleton coefficients squared, then
   Lambda(F)=sum_internal A(v)sum_i alpha_vi^2 ln(1/alpha_vi^2)
   W1(Sub_vi)+sum_terminal A(l)Lambda(Sub_l). Each edge introduces its
   logarithm once. A(v)<=J(v) and W1<=1 justify the gate upper bound.
4. Let G_r(x,y,z) select y only on the all-+1 event of r fresh controls,
   otherwise x. Put p=2^-r and F_t=G_r(F_(t-1),y_t,z_t), F_0=x_0.
   Every input block and child output is genuinely independent and balanced.
   I(F_d)=1+r[1-(1-p)^d]. The x_0 singleton coefficient is (1-p)^d.
   For d=2^(2k), r=3k, k>=2, the sum over nonroot continuation nodes is
   at least (1/2)2^k(1-2^(-2k)), while I(F_d)<=5/2 and tends to 1.
   Therefore no finite K pays the whole-subformula bank. These finite
   functions have dimension 1+d(r+1), depth d, and selector energy density
   p tending to zero. Exact logarithm and Bernoulli inequalities prove the
   divergence; no truth table of the exponentially large family is built.
5. The same family has H(F_d)=Q_r[1-(1-p)^d]/p in bits, with
   Q_r=(1-p)^2 log2(1/(1-p)^2)+2rp(2-p)<=6rp.
   Thus H(F_d)<=6(I(F_d)-1), uniformly in depth. This is a calibration
   of the repaired charge, not a new claim of generic read-once closure.

The exact first unsupported universal line is replacing A057's actual-query
log/outer-erasure bank by the LOCAL gate bank under physical restriction,
with recentered biased descendants and the same influence reserve. Formula
ancestor multipliers J and physical reach probabilities w are not identical.
No assertion that the new gate bank already upper-bounds that physical bank
is made. The counterfamily is a failed-helper certificate, not an FEI disproof.

# executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before either computation. No symmetry reduction,
random sampling, automatic dimension escalation, GPU, heavy job or memory-gated
job was used. Estimated memory was 40 MB. The pilot limit was 60 seconds;
observed Python time was 0.0017 seconds. Main time was 0.0201 seconds.

Commands from agents/A059:

    python -X utf8 runs/20261011T224320Z-fleet05-A059-decomposition-depth/code/check.py --pilot
    python -X utf8 runs/20261011T224320Z-fleet05-A059-decomposition-depth/code/check.py

Pilot: 31 assertions PASS. Main: 252 assertions PASS, all 78 balanced truth
tables on n<=3, five rare-switch gates r=1,...,5, five chain tables at
(r,d)=(1,1),(1,2),(1,3),(2,1),(2,2), and eleven exact symbolic lower bounds
at k=2,...,12. Largest full truth table has 7 bits. Integer Walsh transforms
and Fraction arithmetic verify influences, singleton coefficients, the exact
entropy recurrence and first-charge factorization. Entropy identities are
compared as exact rational coefficients of prime logarithms. Inequalities use
40-term rational atanh-series intervals with an explicit geometric tail.
The finite local-Lambda checks certify the weaker 7delta bound; the sharp
4+6/e coefficient follows from the analytic proof. out/validation.json and
out/pilot.json contain actual outputs. No Decimal or floating entropy is used
as proof. Timing measurements are ordinary floating wall times only.

# proof dependencies and changed downstream conclusions

The new claim uses the exact balanced disjoint coefficient/influence identities
from threshold Proposition 7.1 and reviewed A056 v1, plus elementary finite
Fourier and logarithm inequalities. PROOF.md also derives the particular
coefficient/influence relations used, so it has no dependence on a pending
weighted biased-threshold theorem, arbitrary-selector leaf certification, or
universal FEI. The local Lambda lemma was contributed by the B12 lead.

A057's two v1 claims are independently accepted locally at scope; see
REVIEW_A057.md and out/REVIEWS.json. A059's new bundled claim remains pending
A091/A090 review. A057/A060 must not use sum J Lambda(Sub) as a depth budget:
it fails even when I tends to 1 and actual H tends to zero. A056/A057/A097
can consume the first-charge identity, but must prove its admissibility for
their actual physical-query remainder. The common leaf reserve in the
stopping identity is retained, not charged again at every ancestor.

# one next mathematical action and independent reviewer

Next: use the signed recentered A056/A057 descendant interface to attempt an
actual-query charging rule into the NEW local edge/gate charges in PROOF.md
(3), preserving terminal entropy and influence. Use the explicit rare-switch
chain as a mandatory no-double-counting test before any general claim.
Independent reviewer: A091; alternate A090. A060 can independently reproduce
the whole-subformula divergence without repeating the baseline closure.

# actual persistence receipts or precise save blocker

All required artifacts are inside the authorized A059 run directory, with
rolling STATUS.md, WORKLOG.md and LEARNED.md in A059. out/PERSISTENCE.json
records byte counts and SHA256 readback receipts; out/SCHEMA_CHECK.json checks
the exact protocol claim/progress field sets and compatibility copy. Every
file is below 20 MB. Supervisor copy, mirror verification, central adoption
and downstream use remain pending. No local save blocker exists. No git,
mail, brain writes, other-agent writes or shared-index writes were performed.

## Universal bridge

This stage moves C019 by settling the composition-depth logarithm accounting
test: a universal balanced local gate charge is paid by the exact deficit
reserve with 4+6/e nats, while the proposed whole-subformula charge is
rigorously refuted by a Boolean growing-depth family with bounded influence.
The unpaid part is the transfer of physical-query, recentered biased-child
remainders and terminal entropy to those single-use gate charges. NEXT is
that exact admissibility test, because it attacks the missing universal
transport after removing a false depth ledger; another isolated formula-class
bound would leave this obstruction unchanged.
