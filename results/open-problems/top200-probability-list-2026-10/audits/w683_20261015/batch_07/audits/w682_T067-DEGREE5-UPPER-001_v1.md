# T067-DEGREE5-UPPER-001 v1: PASS

Kind: audit. Target: T067 regular degree5 critical case.
Exact proof SHA256: `e0e8f87ccad0e886a0253e9c8b234e84920d3038e1650403f2a56f3969dd18b2`.
Audit time: 2026-10-15T16:47:54.220818+03:00.

## Scope and verdict

PASS: the finite canonical depth25 signal for the uniform-prior three-state ferromagnetic Potts process on the regular5-ary tree at eta=161/360 is at most927866518931/19791209299968, strictly below217/4500. This is a finite experiment upper bound, not the infinite-tree assertion by itself. No priority finding is made.

## Full mathematical check

Read the entire frozen proof. For two calibrated conditionally independent experiments, conditional root densities are3p_i and3r_i relative to each unconditional observation law. Passing an edge gives1-t+3tp_i, so multiplication gives exactly z_i and the unconditional tuple density sum(z)/3. All factors here are positive because eta<1, including a prefix paired with a child; a prefix may have zero coordinates but the child factors are positive.

The three floor/residual cases have nonnegative barycentric weights, sum1, and posterior barycenter z/sum(z). For a split label j, the root-conditional kernel w_j v_ji/p_i sums to1 on every positive-probability root coordinate. Coordinates with p_i=0 force each positive-weight v_ji=0 and have zero conditional probability. Forgetting the label is therefore exactly the old experiment. Rounding the total mass of each permutation orbit downward and revealing all removed mass is also an upgrade: the decision depends on the old observation orbit, then the root is revealed. By color invariance each revealed color has equal total mass. This accounts for every rounding unit; it is not a numerical error estimate.

Conditional independent upgraded child experiments continue to dominate the old children. Each depth uses the OLD child law for all five branches, with four fusions: two eta edges, then three merges using prefix strength1 and another OLD eta child. Every intermediate split and rounding is accounted for. There is no replacement of the old children by the newly formed prefix.

## Independent evaluator, complete replay and precision

Created checks/t067_degree5_own.cs from the proof and our own earlier evaluator design; imported no solver code, tables, executable or intermediate masses. It independently constructs all334153 triangular first rows and667489 ordered merge rows, asserting exact nonnegative row normalization. For each fixed left representative, distinct right permutations suffice by simultaneous color relabeling invariance. With the raw integer likelihood ((360-161)N+3*161*k), the tuple density denominator is3*(360*N)^2 for the first fusion and3*360*N^2 for later fusions. The integer multiplier36/(right orbit size) gives the common108 denominators printed in the proof. Each barycentric residual cancels the tuple-sum denominator exactly.

All table numerators and local likelihood products fit checked UInt64. The accumulation uses checked exact unsigned128-bit arithmetic, explicit low-word carry and overflow rejection; BigInteger is used for exact final floor division by S*tableDen. Since every row sums to its denominator and both masses sumS, the sum over ALL destination accumulators is S^2*tableDen. This bounds every individual accumulator below2^128, even with the triangular factor2, with S=2^32. Exact source-level expansion of the32-bit limb multiplication and carry formula checks the arithmetic. Automatic BigInteger controls include S*S=2^64, maximal limbs, nonzero low accumulator, expected overflow rejections and the actual table denominators. No float participates in masses or bounds; elapsed-time display is operational only.

The separate checks/t067_degree5_control_own.py uses Fraction and BOTH complete left/right orientations, unlike the native relative-orientation method. It compares all28 first rows and49 ordered merge rows on N6, all7 masses and signals at each of4 depths, and all16 intermediate revelations. Every comparison passes. Native exact controls also pass on N96.

On N96 the independent updater started at the pure orbit, completed25 depths, and checkpointed every full depth. The separate comparator recomputed all25 signals directly from the817 exact checkpoint masses, checked each totalS, and compared all100 intermediate rounding revelations to the frozen artifact. All817 FINAL masses and all817 orbit keys match exactly. The replay did not merely compare the final scalar or sample table rows. See checks/t067_degree5_compare_own.json for exact hashes of the independent source, controls and all50 trajectory files.

Final signal=927866518931/19791209299968; exact positive gap to217/4500=3313696747321/2473901162496000. The comparison channel is strictly stronger than critical since5*(161/360)^2-1=1/25920>0. Larger precision cannot change this verdict because every operation is exact integer/rational arithmetic. Native runs exited after the N6 control, N96 pilot and approximately46-second remaining trajectory. No owned evaluator remains running.

The source artifact SHA256 is bec3329f2968b0b58fee6306d2e2d96b6237a9da72fb9ecdb4be22913755484f. The solver's separate full Python replay was marked pending in the frozen entry record; this audit supplies its own complete independently written trajectory and does not treat that pending replay as evidence.

## Literature and admission scope

This is an audit of a submitted exact case, not a claim of priority. The existing primary-source search and source records for T067 include Sly arXiv:0811.1208, Mossel-Sly-Sohn arXiv:2212.03362, Gu-Polyanskiy arXiv:2303.14688 and the recent Potts metadata search checks/t067_recent_literature_own.json. Their contextual general and asymptotic results are not used as a theorem substituting for this finite degree-five argument. This report establishes the proof's validity, while novelty remains unjudged. Another required independent exact-content review and the authorized ledger decision are still required before admission; neither this PASS nor an audit on the same account substitutes for them.
