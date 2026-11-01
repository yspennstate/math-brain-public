# A011 / B03 stage 2: repair the low-boundary comb output cost

## exact target, quantifiers, hypotheses and units

For every a>=1, every first-positive selector comb with arbitrary stopping
and terminal labels in {chi_A,chi_B}, and every distinct nonempty data
character supports A,B on an independent uniform data cube, construct
a complete fixed output reference and bound its entire description cost
without the previous condition I_sel>=gamma D. Labels may repeat without
bound and A,B may share data coordinates. Entropy and costs are in bits;
influence is the ordinary uniform physical edge-flip sum.

Result: a normalized reference Q_F computed from physical suffix means
satisfies CE(P_F,Q_F)=H(F)<=C_* I_sel(F), where
C_*=4+2/(e ln 2)<41/8. A physical OUTPUT prefix code has expected length
<CE+1<=(41/8) I(F), with zero-length deterministic output allowed. This
is an output code and does not decode a physical leaf history.

The same fixed conjunction/parity gate cover is constructive for every
comb label string; singleton data characters give ordinary conjunctions.
This is a repair of the accepted first-stage transcript, consuming the
specific A012 objection and B03 lead target, not an unrelated new broad
candidate under the pending-claim cap. The original general transcript
remains valid at its original scope. Current repair: AUTHOR_PROVED,
independent review pending. Full FEI and universal paid representation
existence remain OPEN; literature novelty is not asserted.

Do not interpret this as a new FEI class or a better total H/I bound:
the old comb code already has 2D<4 and I_data>=1, hence cost<=4 I(F)
without boundary admission. The mathematical advance is the stronger
complete IDEAL output cost paid solely by selector influence and tending
to zero with its boundary, leaving data influence available for a later
shared-data transfer. Integer output rounding is kept separate.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start: supervisor snapshot 2026-10-11 23:19 UTC,
and B03 STREAM_NOTES.md v2, 2026-10-11 23:2xZ. The lead assigns A011
"a class with REPEATED variables where I_sel >= gamma D is proved, or the
posterior-erased code on the comb." This run follows the second target.
The lead's projective-plane result was not repeated or used as a premise;
A014 owns its linear-hypergraph extension and A012 owns the constant/core
point-activation repair. STATUS.md, LEARNED.md, WORKLOG.md and the prior
A011 claim/report were consumed. Protocol v2 was reread in full.

New dependencies/objections consumed from their originals:

* A086 run 20261011T214823Z-fleet05-A086-joint-code-referee: REPORT,
  CLAIMS, and A011 reconstruction in JOINT_CODE_REVIEW.md. It independently
  accepts A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT@1 at stated scope.
  This review is now recorded in the local handoff; old immutable files
  were not rewritten. Its acceptance does not cover the present repair.
* A012 run 20261011T215648Z-fleet05-A012-sparse-activation-accounting:
  REPORT, CLAIMS and LEARNED. Its raw activated-literal code-cost and
  physical-label posterior lower bound are independently reconstructed
  below and accepted only as that specified subclaim. The hereditary
  admission/read-once package was not independently audited here.
* A008 run 20261011T221357Z-fleet05-A008-gate-label-compression:
  REPORT's complete generator/quotient distinction. Its sunflower theorem
  is context only. Marginalizing a reference is distinct from transmitting
  a raw record and subtracting its entropy afterwards.
* A097 run 20261011T221240Z-fleet05-A097-cross-route-transfer:
  REPORT and CROSS_ROUTE_SUBSTITUTION.tex, especially exact compatible
  reference transfer and terminal debt. Choosing exact character leaf
  laws gives no free kappa credit. Its algebra is explanatory context;
  the new comb bound is derived directly without assuming its candidate.

Earlier primary threshold selector/activation/coding interfaces remain
the pinned local 38-page source, particularly Sections 5.6 and 8.1--8.4;
the quadratic probability correction is reproduced analytically here.
Stage 1's literature check already established that expected-depth
entropy bounds and decision-tree coding have prior art. No new priority
claim or fresh survey is made. out/SOURCE_ARTIFACTS.json binds actual
source bytes and read scopes. No percolation theorem is a premise.

## complete derivation or exact first unsupported line

POSTERIOR_REPAIR.tex supplies the complete all-dimensional proof;
COMB_QUOTIENT.md records the result as soon as derived; COVER_COST.md
is the full reference ledger. The key equations follow.

Let sigma_j encode the two data labels. Define suffix means
m_(a+1)=sigma_(a+1), m_j=(sigma_j+m_(j+1))/2 and disagreement probability
r_j=(1-sigma_j m_(j+1))/2. Set p=(1+m_1)/2, q=1-p. These are fixed
physical probabilities, computable before sampling any Fourier set.

For nonempty selector T with max(T)=j, the Boolean label selector g has

    ghat(T)=2^(1-j) sigma_j r_j (-1)^(|T|-1).

Since F=(1+g)chi_A/2+(1-g)chi_B/2, the empty-selector output masses are
p^2,q^2. Every max-index-j group has 2^j atoms, each of mass
2^(-2j) r_j^2, giving total v_j=2^-j r_j^2. The complete reference first
chooses the empty atom or group j with these exact masses; within j,
choose one fair data label and a uniform subset of j-1 known predecessors.
The highest coordinate j is included. Its normalization is exactly
p^2+q^2+sum v_j=1. Zeros are treated continuously and unsampled.

No physical stopping leaf is transmitted. This is an explicit coherent
output reference calculated from signed suffix coefficients; it is not
an arbitrary spectral prior substituted without a cost proof. Its true
law agrees with P_F by the displayed Fourier calculation.

Two exact expressions for J=I_sel(F) pay the cost:

    J=sum_j 2^-j r_j=(1/2)sum_j(j+1)v_j.

The first is physical boundary counting; the second is the mean size
of the group-uniform selector subsets. With V=sum v_j=2pq, the full cost
is L(p^2)+L(q^2)+2sum jv_j+2sum v_j log2(1/r_j), where L(z)=z log2(1/z).
The binary correction L(p^2)+L(q^2)<=4pq=2V cancels the negative -2V
in 2sum jv_j=4J-2V. Finally r log2(1/r)<=1/(e ln 2) bounds the remaining
rarity expectation by 2J/(e ln 2). Thus CE<=C_*J. The binary correction
is proved by a complete one-variable derivative sign argument in the
standalone proof. The strict rational constant follows from e>8/3 and
ln 2>2/3, giving 2/(e ln 2)<9/8.

For finite positive output masses, lengths ceil(log2(1/Q_F(S))) obey
Kraft and admit a canonical prefix trie. One TOTAL rounding bit suffices;
I_data=p|A|+q|B|>=1 pays it. Empty-selector atoms, both data labels,
support choices, amplitude rarity, and the global normalizer are all
included. There is no paid-prior choice or hidden surviving leaf label.

Precise failed repair, preserved: passively push forward the old
uniform-mask Kraft law and suppress its leaf record. On the terminal-only
switch its common data atom has reference mass (1-4^-a)/3 but true mass
(1-2^-a)^2. Hence its cross-entropy is at least
(1-2^-a)^2 log2[3/(1-4^-a)] -> log2 3 while J=a2^-a ->0.
Even that output quotient fails selector payment. The repaired generator
must use signed/coherent physical suffix amplitudes, not old uniform
Kraft weights. This does not refute a universal infimum over all codes.

Independent reconstruction of A012's subclaim: for the separate
F_r=1+A_r(y-1), p=2^-r, the control-first tree has D=2(1-p), raw cost 2D,
and actual I=p(r+1). Its raw cost/I is 4(2^r-1)/(r+1) -> infinity.
The Fourier constant is 1-p and all other occupied coefficients have
magnitude p, giving H=2rp(2-p)+L((1-p)^2)<=4rp+2p log2(e). Any exact
witness retaining physical leaf L satisfies
H(W|S)>=H(L|S)>=D-H(F)>=2(1-p)-4rp-2p log2(e) ->2.
This reconstructed objection is accepted at exactly that scope;
REVIEW_DELTA.json records the subclaim, not blanket A012 acceptance.
Our theorem uses two nonempty character labels and is not substituted
for A012's separate constant/Boolean-core activation target.

Arbitrary seed guard: for any Boolean h on disjoint coordinates and
complete fixed Q_h (including empty mass and subprobability cost),
Q_F tensor Q_h is a complete reference for F*h with exact cost
CE_F+CE(P_h,Q_h) and influence I(F)+I(h). For h^t the seed terms are
t CE_h and t I(h). The repaired physical-label cost does not erase that
terminal cost, and no seed FEI bound is assumed.

First unsupported universal line: for a general Boolean selector g,
replace the comb's uniform predecessor law in each max-index group by
a complete conditional reference with a dimension-independent physical
influence payment. Indeed the exact two-character formula is
H(F_g)=L(p^2)+L(q^2)+Var(g)+H_nonempty(g)/2, I_sel(F_g)=I(g)/2.
For balanced g this is 2+H(g)/2. Thus unrestricted two-label selection
retains full-FEI strength. Neither cheap output label names nor physical
disjoint cells pay its missing conditional spectral entropy.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before the pilot. No symmetry reduction:
all 1,020 strings of a+1 two-character labels for a=1..8, including
complementary strings and constants. Each actual Boolean table was
reconstructed directly and transformed by integer FWHT; exact Fraction
coefficients and masses were compared with the signed suffix formula.
Physical edge counts, selector/data influences, group masses,
normalization and the integer-ceiling output code/Kraft sum were checked.

All 16 two-bit Boolean seeds were tensored with every label string for
a=1..3: 448 independent full-FWHT comparisons. A subprobability seed
reference P_seed/2 verifies its mass and explicit factorization; its
normalization penalty is retained, not silently reset. Terminal-only
switch recurrences for a=1..64 were checked rationally, without any
truth-table dimension escalation. Five fixed entropy/cost fixtures have
outward rational log certificates, including a constant-label endpoint.

Command from this run directory:

    python -X utf8 code/check_comb.py

out/EXACT_RESULTS.json reports 711,791 exact assertions, zero failures,
1,020 comb cases, 448 tensor cases, 64 recurrence instances, five log
certificates, observed helper runtime 24.0823129999917 seconds. Estimated
memory was 100 MB; no >300 MB or heavy job was started, so no memok gate
was required. No GPU, randomness, background process or window.

Log certification uses power-of-two range reduction to [1,2] followed by
the 48-term positive atanh expansion with remainder
2 t^(2N+1)/[(2N+1)(1-t^2)], t=(z-1)/(z+1). Division by the positive ln2
interval is outward. Bounds are exact Fractions in out/LOG_CERTIFICATES.json.
The universal-in-a proof is analytic; the finite pilot is not used as
a finite-to-infinite extrapolation. No Lean certification or independent
review of this new repair is claimed.

## proof dependencies and changed downstream conclusions

The repair uses the explicit Boolean Fourier expansion, Parseval,
uniform boundary counting, elementary calculus/Kraft, and disjoint
tensor factorization, all derived here. No pending broad FEI helper is
assumed. The prior transcript and A086 acceptance are source-bound
context and continuity; neither an unproved A008/A097 cost nor the B03
projective-plane theorem is a premise.

Changed A011 conclusion: I_sel>=gamma D is no longer needed for any
two-character comb label string; on the old terminal-only bad family
raw cost/J=4(2^a-1)/a diverges, whereas full repaired cost/J<41/8
uniformly. Output prefix rounding is separately paid by data influence.
A012/A008 can consume the distinction between true-witness posterior
erasure and passive uniform-Kraft quotient; A097/A013 can use the exact
remaining seed cost and conditional-row obstruction. None is claimed
to have adopted or reviewed this repair yet. The original queue
(L)+(S)+(R) infimum is not bounded by this separate reference.

## one next mathematical action and independent reviewer

Primary reviewer A086, alternate A094: independently reconstruct the
signed highest-index masses, the empty-sector cancellation, the code
normalizer, and the difference from passive marginalization. Also
challenge the arbitrary-seed tensor guard. Neither reviewer contributed
to this repaired version; A011 does not accept its own new theorem.

NEXT: derive the exact output-reference transfer for a selector node
with two colliding nonconstant child spectra, retaining the conditional
predecessor-set law and complete terminal references. Test whether the
comb's empty-sector cancellation gives a physical influence payment
there; a failure must identify the retained conditional entropy rather
than erase it. This is the next recursive interface needed to leave
the comb, not a larger census of the same solved label strings.

## actual persistence receipts or precise save blocker

Required REPORT, CLAIMS, PROGRESS and identical PACKET_DELTA are saved
with POSTERIOR_REPAIR.tex, COMB_QUOTIENT.md, COVER_COST.md, review delta,
frozen spec, checker, exact results, and rational certificates. Rolling
STATUS.md, WORKLOG.md and LEARNED.md are current. out/PERSISTENCE_RECEIPTS.json
records sizes and SHA256 after schema/content checks; sources are pinned
separately. No file exceeds 20 MB and no write outside A011 occurred.
No shared registry, earlier immutable run, other agent's folder, brain,
git, mail, protected tree, public upload or mirror was modified. Local
persistence is distinct from supervisor adoption, mirror verification
and independent acceptance, all pending for the repair.

## Universal bridge

This stage moves C020 whole-set witness cost by repairing the exact selector-only low-boundary failure of the accepted A011 transcript: the entire coherent ideal output cost for every repeated two-label comb is now <(41/8) I_sel with no boundary admission, compared with the old terminal-switch cost/J=4(2^a-1)/a, and even passive uniform-Kraft marginalization is proved insufficient. The comb was already a cheap total-FEI class (raw cost<4<=4I); no class H/I constant, universal FEI constant or original queue infimum is improved. What remains is a complete influence-paid conditional spectral reference inside general selector rows; the exact arbitrary-selector/tensor formulas retain H_nonempty(g)/2 and the full terminal seed cost. NEXT targets the first two-child collision transfer with those terms present because that is the recursive step a universal cover must survive without reusing data influence to pay physical labels; another isolated class estimate or larger comb census would leave the same universal conditional-entropy obligation untouched.
