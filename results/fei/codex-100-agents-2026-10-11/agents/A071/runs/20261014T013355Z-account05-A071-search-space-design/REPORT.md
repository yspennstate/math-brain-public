# A071 stage 4: complete independent-block-sign admission test

## exact target, quantifiers, hypotheses and units

Test the remaining independent-sign repair of h-admission on A080's actual high-erasure rare core. The fixed six-bit gate h is negative exactly on {0,1,2,4,8,16,32,6,17,40}. Define g0=h, g1=h(g0^6), g2=h((-g1)^6), g3=h(g2^6), always on disjoint identical physical blocks. The target family is F_e=h((-1)^e_0 g3,...,(-1)^e_5 g3), all64 e in {0,1}^6. Each target is an actual7776-bit Boolean circuit. E(f)=min relevant_i B_i(f)/Inf_i(f), B_i=H(S_i|S without i); all entropies are bits.

The result separates two proposed repairs. Independent signs DO rescue A080's old threshold669/200: one flipped block gives E=3.348285089821851...>3.345. But this is the maximum over all64 choices and is below33483/10000=3.3483, whereas E(g3)=3.34838725650...>3.3483. Thus no independent block-sign choice preserves E(g3), and fixed-threshold admission still fails at the new rational threshold. These are candidate admission hypotheses, not false statements attributed to A080's correctly scoped common-sign result. Full FEI is OPEN.

## sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot2026-10-14 01:30 UTC, B15 STREAM_NOTES.md v2 (still2026-10-11 23:25 UTC), own STATUS, and the full EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2. The lead's original n=5 census is complete and independently reconstructed; this dispatch continues the productive biased-admission dependency rather than repeating that search.

Read A075's20261014T005346Z REPORT (rare-core localization with loss<0.914, retained rare-tail entropy and remaining localized supremum); A080's20261014T005622Z REPORT, exact CERTIFICATE_SUMMARY, VALIDATION state schema and code/check.py (read-only, never imported/executed); A089's20261014T000812Z REPORT (sharp geometric criterion, grid-safe orientation, and terminal identity). The A080 high-E rare core replaces the previous stage's hypothetical high-E exclusion. Earlier A071, campaign and manuscript consultations are retained background; no new literature or manuscript audit is claimed. out/source_manifest.json pins the current files read. The updated board also reports A074's matching closure acceptance and A075's independent acceptance of A084's continuum band; neither is used as an unreviewed mathematical premise here.

## complete derivation or exact first unsupported line

PROOF.md derives all identities, symmetry coverage, circuit transitivity, the logarithm remainder, and the one-flipped-block bias map. With core mean m, variance v, singleton square t and physical influence d, set p_j=p or1-p according to the block sign. Let s_T be the normalized biased squared outer Fourier coefficients. For each block j,

    q_j=sum_(T containing j) s_T/v,
    R_j=sum_(T excluding j) Phi(s_T,t s_(T+j)/v)-q_j Phi(m^2,t),
    E_(j,i)(F_e)=E(g3)+R_j/(q_j d).

No global physical transitivity is assumed after mixed signs. All six block types are retained, and the minimum over these types is the actual minimum over all7776 physical coordinates. Each block's1296 coordinates are transitive, as proved inductively for the actual circuit. Direct pivotal enumeration checks every q_j. The complete terminal identity is

    H(F_e)=(sum_j q_j) H(g3)+C_e,
    C_e=H_p(h)-(sum_j q_j) h2(v),
    I(F_e)=(sum_j q_j) I(g3).

All outputs retain the whole starting H(g3). No terminal term is dropped or paid by repeatedly charging a core bank.

The48 actual automorphisms permute the three matched pairs and swap within each pair. Sign colorings are classified by counts of00,01,11 pairs, giving ten orbits. The implementation verifies all48 permutations on all64 gate inputs, explicitly lists all64 sign colorings once, and computes all six block ratios for each representative. The representative minima are displayed below; exact rational endpoints are the certificates, not these decimals.

| Sign mask representative | E(F_e), displayed |
|---:|---:|
|0|3.344736180290|
|1|3.348285089822|
|3|3.348040200939|
|6|3.338742725166|
|7|3.338675993301|
|11|3.341604461443|
|15|3.338484381670|
|23|3.338665558998|
|31|3.338243018747|
|63|3.338222225318|

One flipped block is the unique maximizing orbit. For representative1, the selected block and its matched partner have ratios3.350947277... and3.351065675..., while the four unmatched blocks each have the minimum3.3482850898... . Choosing the best single coordinate would therefore have produced the wrong admission conclusion. The exact best minimum lies between334828508/100000000 and334828510/100000000, strictly below33483/10000. The original frozen diagnostic K=669/200 is rescued; K=33483/10000 is a source-visible follow-up separator verified against the same already frozen cases, not a new search or a retroactively changed original threshold.

The one-flip bias map changes the mechanism. For any current core oriented to minority probability0<p<=1/16, the negative gate vertices have distances0,1,2,3 from its dominant unit input with counts1,2,5,2. Hence the composed minority probability is exactly

    sigma(p)=4p-10p^2+18p^3-19p^4+10p^5-2p^6,
    3p<sigma(p)<4p<=1/4.

PROOF.md gives explicit rational coefficient bounds proving both inequalities on the whole real interval. Repeating this particular mixed-sign operation with minority reorientation must exit the rare band in finitely many steps. On the actual g3 it produces minority probability0.0843323290061...>1/16 from0.0222749348296... . This does not contradict A080's absorbing theorem, which quantifies only common signs. It also does not prove a nonnegative erasure reserve or an all-depth entropy payment.

The honest first unsupported line is now an amortized bound for the negative signed reserves AND the retained C_e along such a mixed-sign bias-escape policy, from one legitimate physical influence account. The finite maximum being below E(g3) rules out monotone admission here; it does not rule out a paid small loss, a different gate, nonidentical child cores, or overlapping constructions. A075's localized-supremum reduction remains a separate source-owned theorem; this stage supplies no bound on that supremum and no unbounded H/I family.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was written before the pilot and full search. It freezes the actual circuit, all64 sign choices,10 orbits,6 block types per representative, integer/Fraction arithmetic,96-bit rigorous logarithms, memory estimate140MB, pilot55seconds and full600seconds. The full family has384 block-coordinate types before symmetry, with every1296-coordinate core block covered by its proved transitivity. There is no dimension escalation or n=6 truth-table census.

Commands from A071 use python -X utf8 with the full run prefix:

- code/search.py --pilot: actual six-bit seed, masks0,1,5,63; all24 block types passed in0.2179 seconds.
- code/search.py: seed and three fixed core reconstructions, then all10 representatives/all60 block types; measured computation375.827 seconds; completed normally. Each completed core and orbit was saved immediately. Exact state intervals independently overlap A080's earlier80-bit intervals, with p,d,t,I matching as rationals.
- code/verify.py: independent uniform-Walsh reexpansion at all10 biased sign vectors; matches all64 squared outer coefficients for every case exactly, checks all60 q_j and all packet inputs, recomputes15 decisive coordinate reserves (all6 in the maximizing orbit plus an upper witness in each other orbit), and checks the full terminal accounting. Final assertions and runtime are in out/verification.json. It verifies all64 failure at the follow-up threshold and the maximizing orbit's rescue of the original threshold. External independent review is still pending.

The96-bit enclosures use a proved48-term positive atanh remainder at natural scale2^160 and outward128-bit normalized-argument brackets. All comparisons use exact rational endpoints. The independent coefficient expansion is derived from the gate's uniform Walsh table, rather than the search's centered-bit transform. Both implementations reside in this run; this internal reconstruction is distinguished from acceptance by another agent.

Two full packet JSON files serialize to about33MB each. After the search completed, the verifier moved those exact completed files into out/big, preserving their bytes and recording SHA256 plus regeneration command in out/big_manifest.json. All other files remain below20MB. Detailed packet output serialization adds wall time beyond the helper's recorded computation timer; no concurrent heavy job was started. The final receipts record actual sizes. Expected memory stayed below300MB (140MB search,200MB verifier estimates, not measured peaks), so no memok-triggering job was planned. No GPU, detached process, shared write, or external code execution occurred.

## proof dependencies and changed downstream conclusions

Consumes A080's explicit high-E circuit and reconstructs its seed and three actual common-sign steps independently. Its exact saved states are comparison certificates, not unquestioned premises. A089's biased split and the earlier A056/A071 interface are rederived in PROOF.md. No A075/A084 universal theorem is required for the bounded result. Their reports guide dispatch and identify the universal frontier.

A080's common-sign fixed-K obstruction and absorption proof remain intact. Its explicitly open independent-block-sign loophole is now settled at this core: it rescues the previous K but still cannot preserve the full E. A071 stage3's unguarded low-E obstruction is strengthened to a high-E core and all64 block signs. A075/A084/A089 can use the exact mixed-sign escape fixture, with a small but genuine erasure loss and the full C_e, rather than assume either that sign choices are irrelevant or that all admission fails. No dependent universal theorem is declared refuted.

## one next mathematical action and independent reviewer

NEXT: A075/A089 should price the one-flipped-block bias-escape operation on0<p<=1/16, retaining its four minimum-ratio physical blocks, the other two blocks' influences, the full starting H(g), and C_e in one exclusive ledger. Use the exact g3 fixture to reject zero-loss claims; do not rerun this64-case family or extend the common-sign orbit by more levels. A074 or A092 should independently reconstruct the48-permutation quotient and the15 decisive reserve certificates; A080 should consume the mixed-sign scope change. This is saved for supervisor routing; no message was sent.

## actual persistence receipts or precise save blocker

The four protocol files, PROOF.md, code, frozen specs and exact outputs are saved under this run. Rolling STATUS.md is exactly two lines, and WORKLOG/LEARNED are appended in A071 only. out/receipts.json and out/schema_validation.json record local artifact hashes, field-set checks, matching progress/delta bytes, and large-file handling. Independent review, supervisor copy, mirror verification and downstream use are pending, separate from local completion. No shared registry, another agent folder, brain or git tree was written.

## Universal bridge

This stage moves B15's signed arbitrary-core admission bridge adjacent to C018: it settles all64 independent block signs on the existing1296-bit high-E rare core, proves that none preserves threshold3.3483, and identifies a one-flip operation that rescues threshold3.345 and escapes the rare band by the exact universal bias factor3-to4. It adds no universal FEI constant and pays no terminal entropy. The remaining line is an owned signed-reserve plus C_e payment for that escape policy. NEXT targets this operation because its complete finite obstruction forbids a zero-loss shortcut while its analytic bias expansion opens a mechanism unavailable to common signs; pricing it attacks the actual universal transfer gap rather than another isolated class or a larger raw iteration.
