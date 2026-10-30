# A084 stage5: continuum physical-terminal curvature payment

## exact target, quantifiers, hypotheses and units

Pay the signed heterogeneous terminal correction Delta C at the FIRST actual physical query of six identical disjoint rare Boolean cores, for every finite core dimension and every real minority bias0<p<=1/16. Gates are h negative on{0,1,2,4,8,16,32,6,17,40}, and J=-h(x xor1); one bits denote negative inputs. The child is minority-negative oriented. Entropy is in bits. Both actual child weights are1/2 and complete terminal entropies remain present.

**Author-proved result:** Delta C<=(5/4) Inf_(j,i)(F) for either gate and every selected physical coordinate. The bound improves to1/2 for h,1/8 for J directions1,2,3,5, and3/4 for J direction0; direction4 uses5/4. These are upper bounds on a signed correction, not absolute-value bounds or an absolute FEI theorem. Independent review is pending; full FEI remains OPEN.

## sources actually read, revisions and theorem locators

Read all BOARD.md entries, supervisor snapshot2026-10-14 06:02 UTC, including a second read of the initially truncated B07-B15 section; B17 STREAM_NOTES.md v2 unchanged2026-10-11 23:40; own STATUS.md; and EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2 in full. The lead's AND-map task was finished in stage2 and remains stale. The last-stage NEXT on repeated escape cycles is now closed by other agents, so protocol dispatch consumes the NEW physical-query curvature gap instead. No disagreement with the lead's mathematics is asserted.

Read A075 run20261014T034311Z PROOF and REPORT: output-entropy potential pays arbitrary legal gate words, but leaves the retained arbitrary core unpaid. Read A080 run20261014T034416Z PROOF: repeated escape-episode/common returns have a Var/I budget below40. Read A072 run20261014T044904Z REPORT and NEXT_INTERFACE.md equations(A)-(B): an actual first core query preserves complete terminals but has an additional Delta C, positive in two of its eight source cases. Read that run's CLAIMS metadata for the scoped accepted A080 version. No source code from another agent was imported or executed. The prior paper/campaign consultations remain retained context; no new literature review is claimed.

Some initial source reads used guessed filenames that do not exist (A072 later-run timestamp, its PROOF.md and QUERY_FIXTURES.json, and A089 PROOF.md). Listing the actual A072 directory resolved its timestamp and interface filenames; no mathematical result was inferred from those access failures. Hash receipts bind all successfully read sources. The stage's proof rederives its terminal chain and does not assume the pending general gate-word claims.

## complete derivation or exact first unsupported line

PROOF.md gives the full all-real, all-dimensional proof. Holding the OTHER five output laws fixed, write k=A+y_j D, with normalized other-input coefficients a_T,d_T, D_T=d_T^2 and q=sum D_T. For varying selected mean x, U_T=(a_T+x d_T)^2 and the spectral masses are U_T and(1-x^2)D_T. Expanding entropy and subtracting q h2(1-x^2) BEFORE differentiating cancels the apparent endpoint v log(v) singularity. The remaining non-affine terminal function satisfies

    C_j''(x)=-2 L_j(x),
    L_j(x)=sum D_T log2(U_T/(x^2 D_T)).

This is the logarithmic admission slope from the earlier continuum packet, now taken in the actual physical-query direction. The other five complete core bills cancel only through affine transport of their q_l; they are not discarded. An actual core query changes its mean to m+beta and m-beta, with m=1-2p. The exact nonnegative Green kernel gives

    Delta C=integral_(-|beta|)^|beta| (|beta|-|u|) L_j(m+u) du.

Weighted Jensen and Parseval imply L_j(x)<=q log2[1+(1-q)/(x^2 q)]. Actual Boolean singleton constraints give |beta|<=min(Inf_i,2p), so the entire child-mean segment lies in[3/4,1], including a constant child. Consequently

    Delta C/(q Inf_i)<=2p log2[1+16(1-q)/(9q)].

This analytic integral bound covers ALL real p and singleton shifts; the finite scalar diagnostics do not provide the continuum inference. Gate-specific exact pivotal witnesses give q_h>=3p; four J directions have q>=(1-p)^5; the remaining directions0 and4 have pivotal assignments at respective minimum weights1 and2, giving q>=(3/4)p and q>=(3/4)p^2. Elementary monotonic endpoint bounds yield the stated1/2,1/8,3/4,5/4 prices. The bounds tend to zero as p->0, beta=0 is exact zero, a constant child x=1 is covered after algebraic cancellation, and coefficient zeros produce integrable logarithmic singularities with negative-credit effect. No uncovered grid or singular boundary remains at the theorem's scope.

For every proposed query rate K the complete inherited statement is

    Delta H(F)-K Inf_(j,i)(F)
       <=q_j[Delta H(g)-(K-5/4)Inf_i(g)].

Thus a supplied actual core query at rate K0 transfers to rate K0+5/4 for this first rare composition query, with finer direction prices available. No unused child surplus is postulated.

**First unsupported universal line:** pay/select the inherited arbitrary-core decrement noncircularly from a genuinely unused actual child surplus, then transport the correction after another query when the blocks have heterogeneous biases. The source's eight complete decrements remain above rate4, even when Delta C is negative, because their inherited core bill also matters. This theorem pays the additive curvature only, without an absolute C018 erasure bound or C019 stopping-tree payment.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes computation:12 directional pivotal profiles,108 scalar diagnostics and8 fixed source-bound physical queries,16 children, estimated100MB memory,55-second pilot/120-second full caps, no dimension/depth escalation. Commands from A084:

    python -X utf8 runs/20261014T061132Z-fleet05-A084-continuum-parameters/code/verify.py --pilot
    python -X utf8 runs/20261014T061132Z-fleet05-A084-continuum-parameters/code/verify.py
    python -X utf8 runs/20261014T061132Z-fleet05-A084-continuum-parameters/code/finalize.py

The first pilot FAILED an actual truth-table hypothesis: both nondominant J directions were assumed to have a single-negative pivotal witness. Direction4 instead starts at weight2. out/FAILED_SINGLE_NEGATIVE_WITNESS.json preserves all exact counts and the failed assumption; the proposed uniform3/4 envelope was withdrawn BEFORE claim filing and replaced by the proved5/4 envelope. This is a substantive hypothesis correction, not a hidden numerical miss. A failed diagnostic save also exposed the absent out directory, which was created in the helper; that filesystem issue has no mathematical content.

Corrected pilot passed315 assertions in1.3816 seconds. The final full run passed2506 exact or rigorous-interval assertions in8.3613 seconds: twelve directional pivotal counts,108 fixed scalar diagnostics, direct core/child Walsh inverse/Parseval/influences, biased outer normalization and all64 sign-valued inverses even at a constant-child endpoint, all directional spectral-vs-edge marginals, affine q transport, independently weighted physical edge enumeration, and complete parent/both-child entropy and influence ledgers. The actual36-bit cases are compressed exact disjoint expansions, not full truth-table enumeration. There are two positive and six negative Delta C signs, and every full decrement remains strictly above4 times physical influence, independently reproducing the stated finite source pattern.

The full run was repeated only after adding complete parent/both-child terminal readback checks (24 additional assertions), not to broaden the search. All finished cases were saved immediately. Logs use Fraction arithmetic with24 positive atanh terms, explicit49th-power remainder,80-bit outward argument brackets and64-bit outward log2 rounding. Narrow zero-containing identity residuals are implementation diagnostics; the analytic coefficient decomposition proves equality. Float runtime fields are timing only. All successful jobs were below the frozen caps and30-minute limit, serial, without GPU or detached process. No job expected above300MB was started, so memok was not triggered; estimated memory is not a measured peak.

## proof dependencies and changed downstream conclusions

The new theorem has no unreviewed claim premise: exact signed block expansion, Shannon entropy chain rule, Boolean derivative bounds, Jensen, the central-difference integral and finite pivotal witnesses are reconstructed. This completes the specifically identified continuum bound for A072's first-query Delta C, rather than opening a new broad FEI candidate. A075/A080's gate-word theorems are source context and were not independently accepted here. A072's eight finite signs are reproduced with distinct centered-section and heterogeneous full-terminal representations; no independent full review of its accepted A080 chain is claimed.

A072/A075/A089 can now charge positive Delta C to the actual queried physical influence at the proved local rates, rather than request an unspecified terminal owner for that additive term. Their warnings about the inherited arbitrary core and later physical history remain valid. The earlier stage4 normalized common-policy theorem and stage3 independently accepted continuum admission remain unchanged. No correctly scoped existing claim is refuted; our failed preliminary weight-one assumption is explicitly archived.

## one next mathematical action and independent reviewer

Extend the signed Green-kernel price through ONE subsequent query of the already exposed non-flat core, carrying its actual child bias, all other block laws and the exact remaining physical influence, then determine whether any inherited child surplus is unused after the first debit. Start from the constant-child and two-nonconstant-child source fixtures; do not renew a root account. If the local heterogeneous envelope grows, record its exact dependency rather than assume the first-query5/4 rate is hereditary.

A072/A089/A075 should reconstruct the fixed-other-law curvature identity and Green kernel; A074/A092 should verify direction4's weight-two witness, all constant-child boundaries and complete terminal transport. A087/A094 can consume the scoped physical payment in the stopping-tree ledger. New independent acceptance remains pending. No external message or write to another agent is made.

## actual persistence receipts or precise save blocker

The four required protocol files, PROOF.md, frozen specification, standalone helper, failure witness, exact scalar and physical outputs are saved in this requested run. STATUS.md has two current lines; WORKLOG.md and LEARNED.md are appended. out/RECEIPTS.json binds all hashes and sizes, schema fields, canonical statement/hypotheses digest, progress compatibility equality, all12 witness directions,108 diagnostics and8 complete physical fixtures. Every artifact is below20MB. Independent review, supervisor copying, registry adoption and mirror verification remain pending; none is inferred from local save. No shared source, other agent folder, git or brain was written.

**Universal bridge:** This stage moves the B15/B17 retained-terminal interface adjacent to C019 by paying the previously unpriced FIRST physical-query curvature over the whole rare continuum: Delta C<=5Inf/4 for h/J, with1/2,1/8 and3/4 direction refinements, every actual core dimension and all singleton shifts including constant children. It pays no unknown inherited core entropy and supplies no absolute C018 or FEI constant. The exact remaining lines are an unused actual surplus for the inherited decrement and transport through the next heterogeneous physical query. NEXT tests that one carried child account because another legal-word cycle is already bounded and cannot remove the arbitrary terminal bill; the new curvature identity supplies a concrete local quantity that can be debited once toward the universal stopping-tree payment.
