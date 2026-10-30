# A084 stage 4: complete the unpaid moderate-prefix entropy bill

## exact target, quantifiers, hypotheses and units

For every actual nonconstant uniform Boolean core of any finite dimension, and every finite depth of the specified six-bit matching-gate policy, bound the complete signed change of H/I independently of bias, depth and dimension. The gate is negative on {0,1,2,4,8,16,32,6,17,40}. Substitute six disjoint identical copies, choosing their minority-negative orientation when minority s<=7/32 and its complement otherwise; orient the resulting output to its minority. Entropies are bits and physical total influence is unchanged by output complement. Full FEI remains OPEN.

**Author-proved result:** the moderate prefix has normalized entropy correction in [-314/21,200/3]. Including its absorbing rare tail, every finite depth d satisfies

    -2074/105 <= H(g_d)/I(g_d)-H(g_0)/I(g_0) <=248/3.

These endpoints are strictly within [-20,83]. The entire starting H(g_0)/I(g_0) survives. Independent review of this new bound is pending. No absolute erasure or FEI constant follows from an additive bound relative to the arbitrary starting core.

## sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot 2026-10-14 02:53 UTC, own STATUS.md, and B17 STREAM_NOTES v2 (2026-10-11 23:40 UTC). The lead still requests the AND sign map already completed in stage2; there is no mathematical disagreement, but that assignment is stale. Re-read EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 in full. Protocol dispatch consumes A075's explicit new unpaid moderate-prefix dependency, rather than repeating the completed AND map or stage3 interval admission. Our earlier report and exact checker were consulted for the signed terminal interface.

Read A075 run20261014T005346Z REPORT.md, PROOF.md and CLAIMS.json: Section2 independently accepts A084-F6-CONTINUUM-ADMISSION@1; Section4 supplies the bias dynamics; Section5 retains and pays the rare-tail entropy but explicitly leaves the moderate-prefix bill unbounded by any proved estimate. Read A080 run20261014T005622Z REPORT.md: an actual 1296-bit rare high-E core refutes the attempted high-E rare-core exclusion and both-common-sign monotonic extension. Read A072 run20261014T020611Z REPORT.md: the different one-flipped-block rare escape retains its entropy bill but leaves terminal admission and repeated excursions open. Read A089 rolling STATUS.md; its new stage directory was in progress, so no unfinished result was inferred. A first read attempted a run-local A089 STATUS.md that does not exist; reading the actual rolling file resolved this access-only error.

Source receipts pin all actual read inputs. No other agent's code was imported or executed. Original campaign and paper consultations remain earlier-stage context; no new manuscript or literature review is claimed here.

## complete derivation or exact first unsupported line

PROOF.md reconstructs the complete chain. Exact disjoint composition gives

    H_next=Q H_core+C(p), I_next=Q I_core,
    Q=12p(1-p)^3(2-p), C=H_p(h)-Q h2(4p(1-p)).

Thus every signed correction is C/(Q I_core), counted once in a normalized telescope. The six outer spectral membership marginals are vq, with v=4p(1-p), q=Q/6. Spectral subadditivity and the independently derived concave scalar thinning inequality h2(vq)<=q h2(v)+v h2(q) give

    -h2(v)/I <= C/(Q I) <=(v/I)h2(q)/q.

On the low-moderate band [1/16,7/32], an exact continuum certificate proves Q>=19/16; q>=19/96 and e<3 imply h2(q)/q<4. Actual edge isoperimetry, proved by section induction, gives I>=1/2 at the beginning of such a run. Its subsequent influences grow geometrically, hence sum_low 1/I<=38/3. Therefore arbitrarily many low-moderate levels cost at most152/3 above and38/3 below, rather than an unbounded charge per level near the irrational fixed bias.

On a complemented step, Q(1-s)>=1/9, q>=1/54 and I>=v give upper correction<8. Edge isoperimetry gives I>=7/8, hence lower correction>=-8/7. The increasing bias maps tau(s)=12s^2-28s^3+27s^4-12s^5+2s^6 and b(s)=s^4(3-2s^2) satisfy tau(7/32)<3/8, b(1/2)=5/32, and b(3/8)=7047/131072<1/16. Consequently the complete stated policy has at most one low-moderate run and at most two complemented steps before entering the absorbing rare band. Combining their signed bills proves [-314/21,200/3]. No uniform moderate escape time is needed.

PROOF Section4 reconstructs the source's rare entropy calculation without using its unreviewed theorem: exact raw-coefficient expansion cancels log(v), yielding -144p^2<=C<=360p^2 and the sharper lower C>=-Qv/ln2. With r=I/p, Poincare gives r_0>=15/4 and the actual bias/influence identities give r_next>=(3/2)r. Every finite rare-tail correction lies in [-24/5,16]. Adding this to the newly proved moderate interval gives the complete theorem. Every boundary p=1/16, s=7/32, s=1/2 and the rare limit p->0 is covered analytically or by exact compact polynomial bounds; a bias grid is not used as a continuum proof.

**First unsupported universal line:** an absolute selectable-erasure or entropy/influence bound for the retained arbitrary-dimensional rare terminal core. The theorem pays the policy's complete signed composition correction relative to the starting ratio, which remains unknown. It does not pay a physical restriction-tree query ledger or repeated cycles alternating this policy with A072's DIFFERENT one-flipped-block escape. Those cycles need an independently owned terminal reserve or actual cancellation. No rare-core exclusion or full FEI claim is made.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before the pilot. The fixed helper uses integer Walsh transforms, Fraction arithmetic, exact polynomial Bernstein coefficients, and rational entropy intervals. Memory was estimated at100MB; no job was expected above300MB, so no memok gate was triggered. Jobs were serial, without GPU, detached process or automatic dimension/depth growth.

Commands from the A084 directory:

    python -X utf8 runs/20261014T030826Z-fleet05-A084-continuum-parameters/code/verify.py --pilot
    python -X utf8 runs/20261014T030826Z-fleet05-A084-continuum-parameters/code/verify.py
    python -X utf8 runs/20261014T030826Z-fleet05-A084-continuum-parameters/code/finalize.py

The pilot passed336 exact assertions in0.0609 seconds. The full checker passed8864 assertions, including8192 exact signed Fourier coefficients from two actual12-bit composed truth tables. It also checks inverses, Parseval, all physical edge influences, all six biased gate marginal/pivotal identities, four thinning fixtures, and three fixed three-step actual-core bias/influence trajectories. Entropy-identity fixtures use narrow rigorous intervals containing zero as implementation checks; exact equality follows from the analytic derivation. No narrow interval is promoted into an exact identity certificate.

Five fixed polynomial certificates each use32 rational subintervals, totaling160 boxes: low-moderate Q>=19/16, complemented Q>=1/9, rare q>=3p, rare q<=4p, and rare tau<=12p^2. Their Bernstein coefficients and exact adjacent endpoints are saved immediately. Positive Bernstein coefficients prove every real point in the respective compact domains; zeros on the rare p=0 endpoint are allowed only for non-strict bounds. The rare endpoint and scalar entropy bounds are then treated analytically. Rational log intervals use24 atanh terms, exact range reduction,80-bit outward argument brackets,64-bit outward output bounds and a proved remainder. Floating runtime fields are timing only.

The full helper was rerun after replacing an irrelevant representation sanity assertion with the genuine exact seed-degree identity sum|T|hhat(T)^2=Q(1/2); no domain or case-count increase occurred. The final successful run took0.7419 seconds, recorded in out/VALIDATION.json. All jobs stayed below the frozen55-second pilot/120-second full budgets and the30-minute limit. Estimated memory is not a measured peak. No failed mathematical assertion occurred. The initial finalizer halted on a source-hash convention assumption: A075 stores a statement-only digest for its new claim, while its copied A084 claim uses statement-plus-hypotheses canonical JSON. Reading the source hash-convention lines verified this difference. out/SOURCE_HASH_CONVENTIONS.json preserves the source digest and supplies an additional hypotheses binding; no source claim or mathematical statement was changed.

## proof dependencies and changed downstream conclusions

The new entropy-budget theorem has no unreviewed claim dependency: its disjoint entropy identity, scalar thinning, edge isoperimetry, compact polynomial estimates, rare raw-coefficient bounds and infinite geometric ledgers are reconstructed. A075@1 is the source-bound precursor; this is completion of its explicitly unpaid moderate-prefix bill, not a new broad conjecture candidate. A084's earlier moderate-erasure theorem is not needed for the entropy inequalities.

A075's unchanged external independent acceptance of A084-F6-CONTINUUM-ADMISSION@1 is consumed with its statement hash and copied provenance in this run's CLAIMS.json. Old immutable runs are not rewritten. REVIEW.md records that the rare-tail entropy subchain holds at its stated scope; no independent full acceptance of A075's localization is claimed because A084 authored its moderate-erasure premise and did not reproduce its full erasure-loss certificate this stage. An integrated extension using this new budget would list A084 as a contributor.

A075/A071/A072/A089 can now retain a uniform full H/I correction for the stated common-sign localization, including arbitrary residence near the fixed bias. The actual A080 rare counterfixture still survives. No correctly scoped existing claim is refuted. The repeated-excursion bill for a different mixed policy and the absolute hard terminal-core bound remain explicit.

## one next mathematical action and independent reviewer

Next derive a signed cancellation or exclusive retained-core slack for one complete cycle consisting of A072's one-flipped-block rare escape followed by the common-sign localization. Keep its actual returning core and both signed terminal corrections; a constant cost per cycle cannot be summed over arbitrarily many cycles. Alternatively an absolute bound on the localized rare-core E supremum would close the universal erasure route directly. This continues the same exact unpaid admission/ownership gap rather than repeating an already bounded prefix.

A075/A074/A092/A089 should reconstruct the complete prefix decomposition, Bernstein coverage, thinning inequality and terminal telescope independently. A075 may accept this new claim independently if it supplies no substantive repair; its authorship of the source rare calculation does not itself establish a review of our added moderate-prefix theorem. No external message or write to another agent is made.

## actual persistence receipts or precise save blocker

The four protocol files, PROOF.md, REVIEW.md, frozen specification, code, polynomial certificates and exact outputs are saved locally in the requested run. STATUS.md has exactly two current lines; WORKLOG.md and LEARNED.md are appended. out/RECEIPTS.json binds hashes and sizes, exact protocol field sets, statement hashes, compatibility-copy equality and final successful checks; every file is below20MB. Local durable save and artifact completeness are established. Independent acceptance of the new theorem, supervisor copy, registry adoption and mirror verification remain pending. No shared source, other agent folder, git repository or brain was modified.

**Universal bridge:** This stage moves the B15/B17 signed-admission route adjacent to C018 and the terminal-ownership obstacle adjacent to C019 by closing A075's previously unpaid moderate-prefix entropy bill: [-314/21,200/3] at every prefix and [-2074/105,248/3] including the entire rare tail, uniformly in all real biases, actual core dimensions and finite depths. It improves no absolute FEI constant and is a composition ledger, not a restriction-tree payment. The exact remaining lines are an absolute bound on the retained hard rare core and single-use ownership of repeated mixed-policy excursions. NEXT tests one actual signed escape/localization cycle with both complete terminal corrections because the now-bounded common-sign prefix cannot by itself price repeated cycles; another finite census or bias grid would not address that universal obstruction.
