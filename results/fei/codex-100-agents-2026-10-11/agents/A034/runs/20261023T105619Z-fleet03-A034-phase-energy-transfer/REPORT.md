# A034 stage19: proper four-cell fibers paid by ternary phase encoding

## Exact target, quantifiers, hypotheses and units

Advance G-PHASE-COND on actual Boolean signs on disjoint independent uniform physical X,Y cubes, retaining FULL H(S_Y|S_X), entropy bits and original physical I_Y. Repair/strengthen the existing candidate to version2; no third broad candidate is opened while two earlier author proofs await independent review. For ANY complete affine partition with maximum cell codimension k and quadratic cell phases, with ANY repeated X-frequency labels, prove Hcond<=(k+1+log2(e)) I_Y and full H<=(k+3+log2(e)) I_Y at every mixed physical restriction. Optional integer X-degree d>=1 is retained and absent from the constant. At most m cells imply k<=m-1. Thus EIGHT cells have full coefficient10+log2(e)<23/2; FOUR have6+log2(e)<15/2, improving old24. Rational-rate inequalities use <=, including zero-energy states.

## Sources actually read, revisions and theorem locators

Current BOARD.md supervisor10:53 UTC, B07 STREAM_NOTES.md v2 (2026-10-11 23:45), own STATUS.md, full execution protocol revision2026-10-11-execution-v2, and stage18 PROOF.md sections1-6/first unsupported line plus its claims/progress/check helper. The earlier required papers and campaign baseline remain previously consumed sources; this proof imports no unquoted theorem from them. Machine-wide rules were consulted; task-specific read-only/no-git/output scope prevails. Board reveals no independent acceptance of A034 stage18. Source hashes are in out/source_receipts.json. Current user campaign deadline14:49 UTC supersedes older protocol dates.

## Complete derivation or exact first unsupported line

Complete self-contained proof is PROOF.md. A collided row u in {0,+1,-1} has support bit a and negative bit b, with INTEGER identity u=a-2b. Disjoint affine supports imply deg_F2 a<=k, deg_F2 b<=k+2. On a coordinate with nonzero support derivative, the boundary has weight>=2^(-(k-1)) and row influence>=2^(-(k+1)). If the support derivative vanishes identically, row influence is exactly the weight of the negative-bit derivative, whose degree<=k+1 gives the SAME gap. This avoids the false comparison between component energy and collided energy.

Shannon subadditivity bounds mu H(P_u) by sum_i mu h2(p_i/mu); the gap and h2(t)<=t log2(e/t) pay this by (k+1+log2(e)) E(u). The exact support edge-isoperimetry induction gives mu log2(1/mu)<=2E(1_support)<=2E(u). These two payments share one coefficient on the SAME original row energy. Summing complete row bills gives exact full H(F), and summing row energies gives exact I_Y(F). No spectral independence, omitted terminal, or fresh per-query budget appears.

Restrictions preserve the cell representation and never increase codimension. A dyadic mass merge induction proves k<=m-1. Fixing old inputs bounds every admitted fresh Boolean tensor factor's F2 degree by k+2, or m+1. Nested eight-cell quadratic gluing admits the degree9 monomial; degree10 is excluded. The three-bit defect passes, while normalized non-Boolean psi_N fails every fixed-k rate for large N and violates the unit-phase hypotheses.

The genuinely new collision witness has proper row masses85/128 and43/128. Both numerators have binary popcount4, so neither support can be represented by two disjoint affine cells. Their eight-cell complete source now pays every restriction. The first unsupported line is a codimension-independent bound for a proper FOUR-cell signed quadratic row without a bounded-size affine completion. The absolute gap still depends on k; arbitrary singleton partitions would require k=n. Removing this dependence generally would imply full FEI. No universal erasure/history/reference conversion is claimed.

## Executed validation with domain, arithmetic, commands and outputs

Before execution FROZEN_SPEC.json fixed dimensions, counts, arithmetic, memory80MB and per-job55-second cap. No >300MB job or compiler was started, so memok admission was unnecessary. Commands are `python -B -X utf8 code/check.py MODE` from this run directory (MODE below). No dimension escalation or detached work.

| MODE | Exact domain | Assertions | Seconds |
|---|---|---:|---:|
| ternary | All 6654 ternary rows on nY=0..3 | 118518 | 3.615 |
| fixture7 | ALL59049 mixed restrictions of actual Boolean nX3/nY7 eight-cell fixture | 885378 | 37.547 |
| fixture9 | 4401 states: all27 X restrictions times163 Y restrictions fixing at most2 of9 coordinates | 149458 | 35.993 |
| masses | Dyadic profiles through8 cells, degree9 guard, direct proper-support character sums | 95 | 0.161 |
| direct | Independent full-F Walsh decomposition at all27 X restrictions;8 gap-sharp rows k0..7 | 34349 | 0.941 |


All 1,187,798 assertions PASS. Integer Walsh transforms, physical difference sums, exact Fraction comparisons and ANF degree calculations are used. Entropies have rational upper intervals from14 positive atanh terms with a proved geometric remainder; dyadic logs are exact. Physical and Fourier I_Y agree. The direct full-F lane checks each Walsh coefficient against row assembly, including label collisions, so the complete ledger is independently verified rather than inferred from a marginal test. Finite tests support, and do not replace, the all-dimensional proof. Max observed job time 37.547s. Output receipts are JSON, each under20MB.

## Proof dependencies and changed downstream conclusions

Version2 has no external proof dependency: polynomial weight, row encoding, dyadic cover, restriction closure, entropy chain rule and mass payment are proved here. It strengthens A034-AFFINE-PLANE-HEREDITARY-PHASE@1 and replaces its missing rank-three intermediate fiber step when the source has eight cells. Old sharper rank-specific subcases remain valid. No withdrawal of the old two-cell theorem is required, but the new proof needs neither it nor a false component-energy comparison. The general class has a changed guard: fixed eight-cell degree<=9, while the smaller four-cell guard remains degree<=5. Full FEI OPEN; author proof awaits independent reconstruction, not accepted merely by these checks.

## One next mathematical action and independent reviewer

A079/A033: reconstruct the negative-bit support-invariant case and normalization of the full entropy ledger. A088/A094: audit zero energy, same original influence, arbitrary X labels, restriction closure and tensor guard. Next mathematical action: bound the COMPLETE bill of a proper signed FOUR-cell quadratic row independently of its cell codimensions when no bounded-size affine completion exists; replace the absolute minimum-influence cutoff by a signed geometric entropy payment. This is a source-bound handoff, with no message sent or other-agent file modified.

## Actual persistence receipts or precise save blocker

PROOF.md, frozen spec, code, all five PASS outputs, four protocol files and rolling STATUS/WORKLOG/LEARNED saved locally in A034. out/protocol_validation.json checks exact schema fields and byte-identical PACKET_DELTA/PROGRESS. out/artifact_receipts.json records sizes/SHA256 of completed run artifacts excluding itself. Supervisor copying, independent review, downstream acceptance and public release are unverified. No mathematical job remains running. Brain self-care remains degraded/unverified: owner model97.4h, state-of-mind82.0h and dream32.7h at wake; those stale personal notes are not proof dependencies.

## Universal bridge

G-PHASE-COND advances from four labels with rate24 to ANY eight-cell affine partition with full coefficient10+log2(e)<11.5 through ALL physical restrictions, paying the previously unpaid proper nonaffine noncoarsenable four-cell fibers from the SAME original I_Y and retaining full H(S_Y|S_X). The general maximum-codimension-k payment exposes the remaining loss precisely at the absolute derivative cutoff2^(-(k+1)). Full universal C018 erasure/C019 history conversion is not obtained. The shortest next route is to remove that codimension loss for proper four-cell rows without bounded completion; this directly addresses the phase-payment obstruction needed by arbitrary-core sources, rather than opening another unrelated class.
