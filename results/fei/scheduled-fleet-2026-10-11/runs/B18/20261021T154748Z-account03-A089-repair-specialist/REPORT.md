# A089 stage 6: the third query requires a sibling transfer

## exact target, quantifiers, hypotheses and units

All functions below are Boolean signs on finite uniform cubes, with entropy in bits. Write S(f)=4I(f)-H(f). Let h on six bits be negative precisely on {0,1,2,4,8,16,32,6,17,40}, let J(x)=-h(x xor 1), and let g on six bits be negative precisely on {0,1,2}. The 36-bit source is F=J(g,g,g,g,g,g), on disjoint physical blocks. Retain the stage-5 root query (block 0, original coordinate 2), its zero child, and the second query at original coordinate 0. The old debit is the actual proportional stage-5 allocation, not a fresh S(g) allowance. This stage handles every active third-query choice in both second-query children: seven alternatives, with no symmetry reduction.

The result is an exact repair of selected-owner continuation. Three alternatives require a strictly positive transfer from the unused OTHER-owner reserve in their constant-core sibling. The least necessary transferred fraction is strictly between 1/4 and 13/50. The other four alternatives need no such transfer. All rates remain 4, both full child functions remain in the ledger, and the original booked debit is preserved. This is a proof with exact finite certificates, pending independent review; full FEI remains OPEN.

## sources actually read, revisions and theorem locators

The execution protocol is fei-execution-protocol/2, revision 2026-10-11-execution-v2. Current BOARD.md, B18 STREAM_NOTES.md v2, and A089 STATUS/WORKLOG/LEARNED were read. The B18 lexicographic/composition directions have already been addressed in the first five substantive stages. Protocol dispatch therefore resumes stage 5's explicit retained-debit NEXT. The ten intervening run directories contain only .final markers; they supply no new mathematical result.

Primary mathematical source: A089 run 20261014T061326Z-account05-A089-repair-specialist, REPORT.md, sections “Exact physical-query decomposition”, “Exact owner rule” and “Carry the SAME booked debit”. Its actual Walsh/edge and rational-log helpers are copied locally, with Python bytecode writes disabled. No other agent's code is executed. Current board reports A072's higher-rate heterogeneous continuation, A071's negative other-owner margins, and A074's requested positive-curvature interface; these are coordination leads, not proof premises. Source hashes and exact locators are recorded in out/SOURCE_INVENTORY.json. No new literature theorem or independent acceptance is asserted by reading an index or a brain card.

## complete derivation or exact first unsupported line

### Failed statement and actual counterexample

The failed continuation is: “After the third active physical query, the other five cores still pay the complete outer correction separately in EACH child, leaving the queried-core S4 bank entirely unused.” The first pilot asserts exactly that sign and fails. For second-query bit 0, any third query at original coordinate 3, 4 or 5 gives the same numerical profile (all three are checked separately). Its zero child has

    U_0 in (0.31708,0.31710),
    M_0 in (-0.18541,-0.18540),
    S(full child)=U_0+M_0 in (0.13168,0.13169).

Here U is the queried-core owner and M is the signed other-owner remainder AFTER its outer correction. Thus the original “M_b>0 persists” line is false. The other child has a constant queried core, U_1=0, but its full function is nonconstant and has M_1 in (0.47566,0.47567). A constant queried core does not erase the other five cores or their entropy.

The related stronger statement “the genuinely unused queried-core owner alone still pays old plus new debit” also fails. Naively averaging raw U would leave a positive margin about 0.03183. That is misleading: U_0 must first pay -M_0. Once this already owed correction is subtracted, mean selected capacity B is about 0.0658424, whereas the preserved old-plus-new debit T is about 0.1267110. The strictly positive shortfall is about 0.0608686. Exact outward endpoints, rather than these decimals, certify each sign in out/REPAIRED_CASES.json.

The earlier failed all-eight root rate-4 assertion remains visible: the actual h(g^6) has S4<0 although S4(g)>0; stage 5's exact countercertificate is retained as a source dependency. Nothing here revives that assertion or changes h's earlier repair to 9/2.

### Definitions and exact surplus transport

For the fixed outer gate and independent cores, let q_l be its biased pivotal probabilities and C the complete composition entropy correction. The actual occupied-block spectrum gives

    H(F)=sum_l q_l H(g_l)+C,
    I(F)=sum_l q_l I(g_l).

For a query in block 0, q_0 is unchanged in both children and the remaining q_l average to their parent values. Define

    U_b=q_0 S(g_0^b),
    M_b=sum_(l!=0) q_l^b S(g_l)-C_b.

Consequently S(F^b)=U_b+M_b, with every full terminal included. If e=H(F)-average H(F^b)-4 Inf_i(F), then

    e=average S(F^b)-S(F).

The old debit D arrives at the current parent. The required outgoing mean booked debit is T=D+e, not e alone. These are exact identities; subtraction of interval enclosures is only a diagnostic check, not their proof.

### Strongest correct replacement for the prescribed two owners

Let w_b be fixed nonnegative child probabilities summing to one. Suppose the certified raw selected owner U_b>=0 and the signed remainder M_b give nonnegative corrected selected capacity

    V_b=U_b-max(0,-M_b)>=0,
    W_b=max(0,M_b).

Then V_b+W_b=U_b+M_b=S(F^b). Negative M has already been paid; W is the genuinely unused other owner. Put B=sum w_b V_b and W=sum w_b W_b. For any nonnegative required debit T, a payment from these two capacities exists if and only if

    T<=B+W.

Among such payments, the least possible mean draw on the other owner is exactly

    tau=max(0,T-B).

Necessity: selected draws total at most B, so other draws total at least T-B and are nonnegative. Sufficiency: spend s=min(T,B) from the selected owner and tau=T-s from the other owner. If B>0, book s V_b/B; when B=0 take all selected draws zero. If W>0, book tau W_b/W; when W=0 feasibility forces tau=0. Both coefficients lie in [0,1], so no child capacity is exceeded, and the conditional average booked debit is precisely T. This proof uses no independence or multiplication of conditional estimates. It is an exact deterministic allocation theorem. It also handles B=0, W=0, T=0 and equality T=B+W. If some V_b<0, this particular theorem is inapplicable; a negative owner cannot be silently clipped away.

### Carrying the actual old debit into the seven third-query alternatives

Let e1 be the root rate-4 excess. Its nonconstant queried-core child receives D0=2e1; the root's constant-core child, of reach 1/2, receives zero selected debit and is retained unchanged. Let e2 be the second-query full excess, let U^(2)_b be its two queried-core banks, and B2=(U^(2)_0+U^(2)_1)/2. Stage 5 establishes 0<D0+e2<(3/5)B2. The incoming debit at second child b is therefore

    D_b=(D0+e2) U^(2)_b/B2.

This is the SAME stage-5 allocation. It is computed anew from the exact source, not reconstructed from rounded saved decimals. For each active third query, calculate its full e3, then T_b=D_b+e3 and the corrected V,W above. In all seven cases D_b>0 and e3>0. To preserve the old and new labels separately, split each outgoing total debit d_c as (D_b/T_b)d_c and (e3/T_b)d_c. Their conditional means are exactly D_b and e3; no old label is erased when its owner changes.

For second bit 0, the active original coordinates are 3,4,5 (coordinate 1 is dummy). All three have tau>0 and

    1/4 < tau/W < 13/50.

The zero child has W_0=0 and V_0>0; the one child has V_1=0 and W_1>0. Spend V_0 in full in the zero child and book 2tau in the one child. The mean debit is B+tau=T. Thus the old debit crosses into the constant-core sibling's OTHER-core reserve; pretending it stayed solely in the selected core would be false. The zero child has zero remaining full surplus, the one child strictly positive remaining full surplus, and the mean remainder exceeds 0.1769. All full H and I remain present.

For second bit 1, all four original coordinates 1,3,4,5 are active. Both M children are positive, and 0<T<B. Book T V_b/B in each child; no W is spent. Both full remaining child banks are strictly positive.

Every new third-query terminal has unconditional reach 1/8. The root's unchanged branch keeps reach 1/2, and the untouched opposite second-query branch keeps reach 1/4 and its original debit. The seven alternatives are choices at their respective nodes; they are not seven simultaneous charges against one reserve.

### Honest first unsupported universal line

This closes the supplied third-query interface with a sharp finite transfer requirement. It does not prove that arbitrary deeper histories or arbitrary Boolean cores provide nonnegative V and enough untouched W, nor that a chosen sibling reserve is still unused after another query in one of the OTHER cores. One must carry the now explicitly spent other-owner amount 2tau; the full M of that sibling is no longer fresh. Uniform selection and admissibility of those signed capacities is the unpaid universal line. Full FEI remains OPEN.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json fixes the actual source, both surviving second children, at most eight third-query candidates, no symmetry, Fraction arithmetic with 192-bit outward logarithm bounds, 80 positive atanh terms and a proved geometric remainder, <=100 MB estimated memory, and a 55-second cap. The first pilot fails the persisted M_b>0 assumption and is preserved in out/FIRST_FAILURE.md. The audited enumeration handles all seven active choices, with 475 structural predicates. REPAIR_SPEC.json precedes the seven-case corrected allocation certificate, which records 108 exact mathematical predicates. An independent direct-DFT A+gB representation checks the full entropy, influence and required transfer without the mixed-bias outer helper; its result is in out/INDEPENDENT_REPRODUCTION.json: 848 exact predicates, seven cases, 0.013 seconds. The scalar boundary grid checks 2860 feasible rational cases and 14301 exact predicates, including zero capacities and equality. The scalar minimum-transfer step was submitted to Lean; the helper returns RUNTIME_UNVERIFIED after 124.7 seconds, with source hash and actual outcome in out/LEAN_ATTEMPT.json. No Lean certification is claimed. A Lean check of the scalar statement does not certify the Fourier derivation or the complete report.

Commands (from the A089 folder):

    python -B -X utf8 runs/20261021T154748Z-account03-A089-repair-specialist/code/third_query.py
    python -B -X utf8 runs/20261021T154748Z-account03-A089-repair-specialist/code/repair.py
    python -B -X utf8 runs/20261021T154748Z-account03-A089-repair-specialist/code/reproduce.py
    python -B -X utf8 runs/20261021T154748Z-account03-A089-repair-specialist/code/persist.py

No floating-point sign is used. Floats in summaries are displays only. No job is expected above 300 MB, so no >300 MB admission is needed; no dimension escalation, GPU, remote compute, detached process or background search is used. Current compute state reports status ok, 22.7 GB available RAM, 3.2 GB disk free and no interventions in the last hour. Slow shell startup motivates fewer process starts. No running work is stopped or throttled.

## proof dependencies and changed downstream conclusions

The physical composition identities and stage-5 incoming allocation are rederived locally. No unchecked universal lemma or external theorem is a mathematical premise. The elementary owner-allocation theorem now explicitly subtracts each negative other-owner correction before calling selected slack unused. A072/A074/A075 should replace any continuation using raw selected U by corrected V, and may use the explicit third-query sibling transfer at fixed rate 4. A071's warnings about negative other-owner margins are realized in an actual continuation, rather than left as a root sign count. New mathematics remains pending independent review; same-agent independent implementation is not independent reviewer acceptance.

## one next mathematical action and independent reviewer

NEXT: query one of the five OTHER cores in the sibling that has just spent 2tau. Retain that exact spent amount, the zero-remainder nonconstant sibling, the other reach-1/4 branch and the reach-1/2 root branch. Derive signed child eligibility against this heterogeneous account; do not restart from its full unspent M. A072/A074 should independently reconstruct the full terminal packet spectra and incoming labels; A092/A075 should challenge the necessity and sufficiency of tau and all reach weights.

## actual persistence receipts or precise save blocker

All outputs belong to this A089 run. The four required protocol files, local helpers, two frozen specifications, exact case records, failure and independent reproduction are saved locally, with hashes/sizes and schema checks in out/RECEIPTS.json. STATUS.md has two lines; WORKLOG.md and LEARNED.md record the signed-margin failure and the repaired third-query transfer. Shared registry adoption, independent review, supervisor copy and remote mirror verification remain pending. No git, external messaging or research write into the brain/shared campaign trees is performed.

## Universal bridge

This stage moves C019's stopping-tree payment bridge through the next unpaid active query at the original rate 4: all seven third-query alternatives are funded with the SAME inherited debit and complete terminals, while three refute selected-core-only continuation after the outer correction is honestly paid. The exact repair spends between 1/4 and 13/50 of a genuinely unused sibling other-owner reserve, with no bank renewal. It supplies no dimension-independent FEI constant. What remains is uniform signed eligibility after a reserve has crossed between owners and been spent. NEXT tests that already spent heterogeneous sibling account under an actual other-core query, which attacks the missing universal transport mechanism rather than producing another isolated root bound.
