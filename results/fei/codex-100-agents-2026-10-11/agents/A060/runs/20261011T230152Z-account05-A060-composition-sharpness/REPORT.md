# exact target, quantifiers, hypotheses and units

A060, B12 composition sharpness. Resolve the lead's two specified controls:
exact rare-switch chain H/I/B and relaxed-root loss, and an a-bit selector
cell containing a quadratic-bent point defect. H and B are in bits;
Lambda and repeated root-log D are in nats. The analytic statements apply
to every integer r,d>=1 for chains, and every integer a>=1/even m>=2 for
the bent example. Tensorization conclusions explicitly require tensor-closed
classes and a fixed additive term. Full FEI remains OPEN.

# sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json read in full, revision 2026-10-11-execution-v2.
Read campaign README/CURRENT_STATUS, claim/obstruction registries, packet
matrix and stream actions, and plan introduction plus B12/A060 contract.
The canonical indices are older than the live BOARD, which was read at
stage start (23:09 UTC snapshot). B12 lead notes v1, 22:45 UTC, read in
full and followed. Supplemental CAMPAIGN, CLAIMS, COUNTEREXAMPLES,
SEED_LEMMAS and NATIVE_MAPPING were consulted, with X004/X005/X009 scope
guards retained. Relevant original sources ERASURE_RIGIDITY.md sections
1--4 and BLOCK_RESTRICTION_IDENTITY sections 1--5 were read. Earlier
B05/B09/B19 REPORT openings were inspected for provenance and scope;
their full mathematical packages were not independently audited here.

Read threshold 38pp Section 7 Proposition 7.1/Corollaries 7.2--7.4 and
Section 8 shared-data Proposition 8.6/Corollaries 8.7--8.8; corresponding
composition/selector sections in the 29pp text were inspected. Read
percolation 30pp and 31pp variant introductions and conventions only;
no percolation result is used. These are focused section reads, not
whole-manuscript audits. Local files are hashed in out/SOURCES.json.

Read A057 REPORT.md in full for the exact root concavity relaxation and
A059 REPORT.md/PROOF.md in full. A059 had already closed the repeated
subformula divergence: I do not claim novelty for that obstruction.
REVIEW_A059.md records a scoped independent reconstruction. A059 also
independently reviewed A057, addressing B12's review-before-new-candidate
cap; this run opens only one bundled sharpness record.

# complete derivation or exact first unsupported line

PROOF.md supplies complete analytic proofs and COMPOSITION_SHARPNESS.tex
is the compact mathematical deliverable. New sharpness detail:

* For p=2^-r, q=1-p, Q=q^2 log2(1/q^2)+2rp(2-p),
  b_r=phi(q^2,p^2)+2p-2p^2, the chain has
  H=Q(1-q^d)/p, I=1+r(1-q^d), B=r b_r(1-q^d)/p.
  The continuation outer-erasure residual L is exactly zero; a concavity
  relaxation nevertheless adds D=sum q^(d-t)Lambda(F_t).
  D>=p d(d-1)q^(2d). With r=3k,d=2^(2k), actual H,B tend to zero,
  I tends to one, while D diverges. The informal epsilon diagnostic needs
  a factor-r qualification: deficit epsilon=rp gives D~epsilon d^2/r,
  H~4epsilon d; switch probability epsilon=p gives D~epsilon d^2,
  H~4r epsilon d. A059's explicit formulas already distinguish them.
* For selector probability p=2^-a and bent-point probability delta=2^-m,
  exact coefficients, H, means, correlations, B_W, influence split and
  selector/data chi-square are given in PROOF.md (7)--(8).
  The all-parameter rigorous enclosure is
  L-32p delta/(a ln2)<=B_W/I_W<=L,
  L=2(1-p)[m+2a-2+1/ln2]/a.
  This proves fixed-a divergence and quantifies its disappearance when
  a grows faster than m. The a=1 chi-square is exactly X009's value.
  I_data=m(1/2+2p delta) is retained; the example does not refute FEI.
* Fixed additive overhead is erased on a tensor-closed class. Per-factor
  overhead and a class lacking tensor closure require different claims.

The first unsupported universal line is a map from physical-query,
recentered biased-descendant remainder and terminal entropy into one
conserved data-side/edge-deficit reserve. No such line is proved here.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before running code; FROZEN_SPEC_V2.json froze
the added individual-erasure, root-ledger and tensor checks before rerun.
Command from A060:

    python -X utf8 runs/20261011T230152Z-account05-A060-composition-sharpness/code/check.py

V1 passed 792 assertions in 1.7083274 seconds. V2 passed 839 assertions
in 0.2076975 seconds; exact output is recorded in out/validation.json.
Domain: six rare-switch tables (r,d)=(1,1),(1,2),(1,3),(2,1),(2,2),(3,1);
eight bent-splice tables (a,m)=(1,2),(2,2),(3,2),(1,4),(2,4),(3,4),(1,6),(2,6);
two disjoint tensor-square controls; seven rational scale checks k=2,...,8.
Largest actual table has 8 bits. No exhaustive optimum is claimed.

Integer FWHT and Fraction arithmetic verify amplitudes, influences,
Parseval, chi-square, individual/aggregate erasure, entropy recurrences,
relaxed-root recurrence and tensor additivity. Entropies are exact rational
linear combinations of prime logarithms, compared coefficientwise.
All infinite inequalities and asymptotics follow from PROOF.md; finite
computations are not substitutes for these proofs. Estimated memory 40 MB;
no heavy job, GPU, random search or automatic dimension increase occurred.

# proof dependencies and changed downstream conclusions

The proofs derive the needed family spectra directly. The imported
interfaces are threshold Proposition 7.1 and the A057 root relaxation;
ERASURE_RIGIDITY supplies the a=1 baseline, independently recovered here.
No FEI premise, product-biased weighted-LTF conjecture, overlapping-product
subadditivity or real-wavefunction Boolean admission is used.

A059's rare-switch obstruction and H/I controls are independently accepted
locally at their stated scope, not the entirety of its bundled claim.
The A060 sharpness bundle is author-proved and pending A091/A090 review.
A019/A058 must reserve data-side influence before claiming low-selector
closure. A056/A057/A059 should test physical-tree transport against the
exact-zero continuation residual and factor-r depth diagnostic. No shared
indices or other agents' files were changed.

# one next mathematical action and independent reviewer

Next: on the rare-switch chain's control-first physical restriction tree,
evaluate the recentered biased-descendant outer residual and terminal entropy,
and test whether each is assigned once to A059's local gate deficit reserve.
This is a concrete admissibility check on the remaining universal transport.
Independent reviewer A091, alternate A090. Handoff consumers A019/A056/A057/
A058/A059/A097/B20.

# actual persistence receipts or precise save blocker

All required files, code, exact output, frozen specs, mathematical deliverables
and rolling files are saved inside A060. out/SCHEMA_CHECK.json validates
exact protocol fields; out/PERSISTENCE.json records file hashes and sizes.
Supervisor copy, central adoption, external review and mirror verification
remain pending. No git, mail, brain writes or writes outside A060 occurred.

# Universal bridge

This stage sharpens C019 stopping-tree payment and the lead's low-selector
collision target by independently confirming the divergent redundant log
ledger, adding exact actual B for that chain, and quantifying precisely when
the multi-bit selector-only payment fails. It pays no new universal residual;
the remaining gap is a source-valid physical-tree transfer with biased
descendants, data-side influence and terminal entropy charged once. NEXT
tests that transfer on a family where the exact continuation residual is
zero, so it is the shortest check of the missing universal mechanism rather
than another isolated class entropy bound.
