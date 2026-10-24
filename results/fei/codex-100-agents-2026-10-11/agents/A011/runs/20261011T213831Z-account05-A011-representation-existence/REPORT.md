# A011 / B03: representation existence

## exact target, quantifiers, hypotheses and units

For every finite selector decision tree on an independent uniform selector
cube, querying each selector coordinate at most once along each path,
and every collection of Boolean leaves on a common uniform data cube,
construct a gate cover and a complete whole-spectrum witness. Shared
variables, repeated leaf functions and colliding Fourier supports are
allowed. Entropy and code lengths are in bits; influence is the usual
uniform physical edge-flip probability summed over coordinates.

Let d_ell be leaf depth, p_ell=2^-d_ell, and D=sum p_ell d_ell. If each leaf
has a complete spectral witness code with expected length c_ell, the
constructed full code has expected length exactly

    2D + sum p_ell c_ell.

If I_sel(F)>=gamma D and c_ell<=K I(g_ell), its cost is at most
max(2/gamma,K) I(F). This is a genuinely explicit admission condition.
For unsigned nonempty character leaves, c_ell=0. Defining B as the expected
number of selector flips changing the character label gives I_sel=B/2.
The named class B>=beta D has a fully paid cost <=(4/beta) I(F).

For singleton characters the positive event is a union of ordinary
conjunction gates. The alternating two-label comb has beta=1/2,
unbounded worst-case read, repeated data labels, and I_sel/a tending to
zero. Its complete cost is <=8 I_sel and hence <=8 I(F).

Artifact completion: COMPLETE_LOCAL. Restricted mathematical claims:
AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW. Full representation existence
for every Boolean function with an absolute paid constant: OPEN.
Full FEI: OPEN. Novelty and public-release status: NOT CLAIMED.

## sources actually read, revisions and theorem locators

The initial board was the supervisor's 2026-10-11 21:38 UTC snapshot;
the 21:45 UTC board was reread during the stage. B03 STREAM_NOTES.md was
absent. No directions were overridden. A006's sunflower result was used
only to avoid duplicating that family, not as a proof dependency.

Campaign protocol EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2,
was read in full. README, CURRENT_STATUS, claim/obstruction registries,
the A011/B03 packet statuses and stream actions, the full A011 assignment
contract, and relevant B03/reviewer portions of the plan were read.
Earlier B05, B09 and B19 reports were consulted for the obstruction and
acceptance scopes; those no-go results are not premises of the theorem.

Supplement intake: CAMPAIGN.md, CLAIMS.md, COUNTEREXAMPLES.md,
SEED_LEMMAS.md and NATIVE_MAPPING.md, plus relevant source notes
OVERLAPPING_PRODUCT_NOTE.md and ERASURE_REDUCTION.md. C009/C011 already
cover ordinary addressing and distinct-character affine cells. C035
already supplies the positive-selector-energy shared-data closure. The
initial distinct-label subcube idea was therefore retired as baseline.
X004/X005/X013 were specifically consumed: physical disjointness does
not justify discarding spectral collisions or arbitrary-core entropy.

Primary local threshold source: context/threshold_paper_38pp.txt,
Sections 5.2, 5.6--5.8, 8.1--8.4 and 9; baseline/current-threshold-paper.tex,
labels prop:joint-witness, prop:selector-identities, cor:affine-selectors,
sec:shared-multiplexers and prop:shared-data-collision. The earlier 29-page
threshold version's introduction/constants were checked as historical
context; its weaker constants were not imported. The percolation 30-page
and earlier 31-page introductions/Theorems 1.1--1.3 were read to delimit
the geometric setting; no percolation theorem is used here. The changed
overlap-exponent claim between those versions is unrelated to this proof.

Primary literature opened during this stage:
[Wan--Wright--Wu, arXiv:1312.3003](https://arxiv.org/abs/1312.3003),
abstract and [Shalev, arXiv:1806.03646v2](https://arxiv.org/html/1806.03646v2),
introduction and prior-work discussion. Whole-spectrum coding and
decision-tree FEI are prior art; Shalev also records earlier O(average
depth) entropy bounds. A theorem-level exhaustive novelty search was not
performed, so no new-to-literature assertion is made. Local hashes of
the actual files are in out/SOURCE_ARTIFACTS.json.

## complete derivation or exact first unsupported line

The complete standalone derivation is STRUCTURED_COVER.tex. Its critical
steps are reproduced here for reviewers.

At a selector node with actual Boolean children G,H and residual Fourier
coefficients u_T,v_T, set q_T=(u_T^2+v_T^2)/2 and
theta_T=(u_T-v_T)^2/(4q_T). Choose a fair physical child, then its recursive
spectral witness with decoded set T, then a Bernoulli spectral bit Z with
parameter theta_T. The decoded parent probabilities are exactly

    q_T(1-theta_T)=(u_T+v_T)^2/4,
    q_T theta_T=(u_T-v_T)^2/4.

Both are the actual squared parent Fourier coefficients. The Bernoulli
law is valid by (u-v)^2<=2(u^2+v^2). Zero-q packets are never sampled.
This recursive construction retains the signs and all coherent cross
terms. It does not replace the Boolean children by normalized real
mixture components or use a false entropy-subadditivity claim.

The physical leaf path has probability 2^-d. Encode that prefix (d bits),
the complete leaf witness prefix, then exactly d selector-frequency bits
along the known queried path. Its Kraft sum is

    sum_ell 2^-d_ell [sum_w 2^-L_leaf(w)] 2^d_ell 2^-d_ell <= 1.

It is prefix-free and uniquely decodes the witness: physical paths are
prefixes ending at leaves; each leaf dictionary is prefix-free; the final
block length is fixed by the decoded path. Output spectral coordinates
are recovered from the leaf set and final membership bits. The true law
need not have uniform spectral bits, and their entire cost is still paid
at one bit each. Conditional physical leaf witnesses retain the original
leaf law because all later spectral innovations sum to one.

Let W be this exact witness and S its decoded output. Then
H(S)<=H(W)<=E L(W)=2D+sum p c. Pushing Kraft masses through the decoder
gives a complete subprobability reference Q(S); for every sampled w,
-log2 Q(S(w))<=L(w). Thus the full cross-entropy is also paid. Multiple
witnesses decoding to the same S are summed, not discarded or counted
as distinct output states. Their posterior entropy is present in
H(S)=H(W)-H(W|S).

The explicit cover is C_ell AND [g_ell=1], where C_ell is the conjunction
of the path literals. For character leaves, parity is itself a Boolean
combination of coordinate regular gates; singleton characters give
ordinary conjunction gates immediately. Finite truth tables provide an
algorithm for all child coefficients and witness transitions. Neither
efficient construction nor a short encoding of the static function's
dictionary is claimed or required by the reference interface.

Conditioning on selectors gives I_data=sum p I(leaf). The admission
I_sel>=gamma D pays the selector transcript, and the leaf codes pay only
data influence; the budget is never reused. Distinct unsigned characters
disagree with probability 1/2, proving I_sel=B/2 for that specialization.
Coordinates not fixed by the reached leaf stay in the same cell under
a flip, so B<=D. The condition B>=beta D is exact, physical, and checkable.

For the alternating-label comb, query j is reached with probability
2^-(j-1), so D=2(1-2^-a). Its continuation disagreement probabilities obey
r_a=1 and r_j=1-r_(j+1)/2, giving 1/2<=r_j<=1 and
B=sum 2^-(j-1)r_j>=D/2. Thus I_sel=B/2<1 while a grows. The cover has a+1
gates, each using x1, and the two data literals repeat without bound.

First unsupported universal line: an arbitrary Boolean selector with
shared/colliding leaf spectra need not have any representation with
I_sel>=gamma D for an absolute positive gamma. This line is not used in
the restricted theorem. For example, the first-positive comb with every
stopping leaf y1 and only its terminal leaf y2 has
D=2(1-2^-a) but B=a*2^-(a-1), so B/D tends to zero. The code can be
wasteful on a perfectly valid easy FEI function. Optimizing that cost
universally is a remaining obligation, not an inferred no-go for FEI.

This is a new complete reference interface in this run, not a claimed
bound on the original queue's variational minimum. Distinct-character
affine selectors are included as calibration only. Repeated labels and
low average selector energy are the stated extension of those baseline
hypotheses. Literature novelty remains unverified.

## executed validation with domain, arithmetic, commands and outputs

Frozen before searching: out/FROZEN_SPEC.json. No symmetry reduction;
all 1,446 fixed-order prunable depth-three trees with leaves y1 or y2
were retained, including duplicate functions and repeated labels. The
five-variable Boolean tables were checked by integer FWHT. Recursive
signed coefficients, transcript probabilities, spectral marginals,
physical leaf masses, expected depths, and physical/spectral influence
identities were compared with exact Fraction arithmetic.

Command, from this run directory:

    python -X utf8 code/validate.py

Result in out/EXACT_RESULTS.json: 50,089 exact assertions, zero failures;
1,446 tree representations; 828 nontrivial representations meeting
B>=D/2; 64 alternating-comb rational recurrence cases (a=1..64); six
independent comb truth-table reconstructions (a=1..6). Maximum sampled
witness count among depth-three trees: 40. Observed Python checker time
0.9666288000298664 seconds. Memory estimate 80 MB; no >300 MB job,
automatic dimension escalation, GPU, background helper or heavy job.

No floating logarithm is a proof premise. The all-dimensional inequality
is the analytic prefix-code/Kraft proof; the finite checks validate the
implementation and local identities, not a finite-to-infinite search
extrapolation. This is author verification with a separately implemented
FWHT comparison, not independent mathematical review or Lean certification.

## proof dependencies and changed downstream conclusions

The proof is self-contained from Fourier restriction algebra, Parseval,
uniform physical conditioning and the elementary prefix/Kraft entropy
inequality (also reconstructed by the Q-reference argument). No
unreviewed campaign claim is assumed. The original threshold selector
and queue identities are scope/notation calibration, not essential proof
dependencies. The two types of witness law (true Fourier-law coupling
versus prefix/Kraft reference) are kept distinct.

Downstream A008/A009/A013/A014 can use a constructive repeated-label
cover and its complete reference cost under explicit boundary admission.
A012/A015 should retain the small-boundary counterexample above and the
arbitrary-selector admission gap. A019/A058 can replace a crude declared
selector dimension by expected tree depth when their physical family
has a proof of the admission condition. None of these substitutions has
yet been made by those agents or accepted in a shared index.

## one next mathematical action and independent reviewer

Primary reviewer A086 should independently reconstruct the transcript
coupling and decode its codebook, checking zero packets, duplicates,
physical leaf law and Kraft normalization. Alternate/second reviewer:
A094. No messages were sent; this is a source-bound saved handoff.

Next mathematical action: compute the conditional spectral-bit entropy
along low-boundary combs, retaining H(W|S), to replace the present d-bit
support block by an influence-paid coherent reference beyond B>=beta D.
The first prospective inequality requiring proof is the full joint
cost (including the physical leaf label), not just the Bernoulli terms.

## actual persistence receipts or precise save blocker

All writes are inside the assigned A011 folder. Required report, claims,
progress and compatibility delta, both named mathematical deliverables,
frozen specification, checker and exact output are present. Final hashes
and byte sizes are in out/PERSISTENCE_RECEIPTS.json, produced after the
files were written and parsed against protocol field names. Rolling
STATUS.md, WORKLOG.md and LEARNED.md are updated separately.

No shared registry, other agent folder or read-only source was modified;
no git, brain write, email, public upload or mirror action was performed.
Supervisor adoption, mirror verification and independent review are
pending and are not inferred from local persistence.
