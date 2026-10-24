# A045 stage 2: sharp taxes cannot be paid separately by biased deficit

## exact target, quantifiers, hypotheses and units

Audit the B09 lead's proposed gate payment `sum_i tau*(eta_i) <= K delta_eta(g)` on address gates and symmetric thresholds of arity at most six, where `delta=I-Var`, `I` is spectral influence, and `tau*` is the sharp scalar singleton uncertainty tax. Test both the raw input sum and the actual reach-weighted query bill with constant/literal leaves. All gates are genuine Boolean signs on independent product inputs. Entropies and taxes are bits. Biases are the actual gate-input probabilities, not squared-spectrum marginals.

Outcome: the continuum supremum is infinite already for an essential binary AND with equal biases tending to zero. This remains true for the best singleton gate-input query tree stopped at zero-deficit leaves, and even the actual positive Shannon correction `(J-M)_+` cannot be paid separately by root biased deficit. The corrected entropy remains bounded: `Hplus/delta -> 2` on the same family. This refutes a payment mechanism, not FEI. The finite exact search covers 126 threshold and 32 address cases, with certified finite-grid maxima. A separate independent reconstruction accepts A042's existing sharp all-bias binary endpoint claim at its stated scope, reducing the review backlog rather than opening another binary class target.

## sources actually read, revisions and theorem locators

At stage start read BOARD.md, supervisor snapshot 2026-10-13 21:24 UTC; B09 STREAM_NOTES.md v2, 2026-10-11 23:33 UTC; own STATUS.md, LEARNED.md and WORKLOG.md. Re-read EXECUTION_PROTOCOL.json in full, revision 2026-10-11-execution-v2. The B09 lead explicitly assigns the tax-sum versus deficit test and asks for arity trends. A098 stage 2 retires repeated half-tax reviews and directs A045 toward the higher-level normalized erasure frontier. This stage does not recompute or claim the half-tax endpoint coefficient as new; it tests its proposed downstream payment and consumes a binary review dependency.

Critical source originals inspected: B09 lead CLAIMS.json, `B09-CLAUDE-SHARP-ONE-BIT-TAX@1`, including the proof text in its proof_source field (REPORT.md was not written by the lead harness); prior A045 REPORT.md, Section 1, scalar convexity on p<=1/16; A100 REPORT.md tax-tree diagnostic (unsharp A096 tax positive at fair bias); A098 stage-2 REPORT.md retirement and `R_ge2` frontier; A042 stage-2 REPORT.md equations (1)-(9), `A042-SHARP-BINARY-PRIME-ENDPOINT@1`; A024 REPORT.md equations (1)-(7), signed normalization and child law transfer; A050 REPORT.md equal-overlap repair and terminal exclusions; A057 stage-2 REPORT.md capped activation bank and unpaid inner/terminal term; A056 disjoint-composition and physical-scope reports. Threshold 38pp Section 6.1 and Proposition 7.1 are the inherited normalization baseline. No percolation theorem or online source is a premise. Local source receipts distinguish raw files and hashes from repository or mirror verification.

The new obstruction is distinct from A100: A100 prices the weaker `h2(p)-h2(1-sqrt(1-p))`, which is positive at p=1/2; the present sharp tax is exactly zero there, and the obstruction uses interior biases approaching zero. No existing source is edited and no global invalidation is inferred from a helper failure.

## complete derivation or exact first unsupported line

### 1. Exact, realizable input laws and frozen finite domain

Let `p_m=1-(1-2^-m)^2`, for m=5,6,8,10,14, and include the fair bias 1/2. Each p_m<=1/16 has the rational half-angle parameter

    sqrt(1-p_m)=1-2^-m,
    (1-sqrt(1-p_m))/2=2^(-m-1).

The already reconstructed scalar convexity formula therefore gives the exact tax expression

    tau*(p_m)=h2(p_m)-2h2(2^(-m-1)).                 (1)

At p=1/2 the sharp tax is zero. No approximate scalar minimizer is used. These are actual possible induced means from uniform physical children: OR of two AND_m indicators on disjoint uniform blocks has probability p_m. Giving each gate wire its own fresh pair of blocks realizes the independent product law. A fair wire is a fresh literal. This verifies Boolean realizability without enumerating the much larger substituted truth table.

There is a scope distinction: querying a gate input in its product space is a valid gate restriction. Querying the output of a composed child is not automatically a singleton physical restriction of the underlying uniform cube; conditioning a child block on its output can correlate its physical inputs. The present gate-level bill must not be silently promoted to an underlying physical-tree budget.

For a symmetric threshold `2*1{sum X_i>=t}-1`, every truth-table coefficient and squared mass is computed by an exact centered tensor transform. In sign input coordinates, one transform sends a pair (a,b) to `((1-p)a+pb,(b-a)/2)`; a coefficient c_S then has mass `c_S^2 prod_{i in S}4p_i(1-p_i)`. This preserves all signs before squaring and includes the empty coefficient. An independent mixed-difference computation checks every subset coefficient for threshold arity at most four. The larger specified arities are still full actual truth tables, not candidate spectral laws.

### 2. The requested raw tax payment is false, already at arity two

Consider the essential sign conjunction `f_n=2 prod_{i=1}^n X_i-1`, every input independently Bernoulli(p), 0<p<1. Direct pivotal conditioning or the exact Boolean spectrum gives

    I(f_n)=4n p^n(1-p),
    Var(f_n)=4p^n(1-p^n),
    delta(f_n)=4p^n[n(1-p)-1+p^n].                 (2)

For fixed n>=2, the previously established sharp tax asymptotic `tau*(p)=(p/2)log2(1/p)+O(p)` yields

    n tau*(p)/delta(f_n)
       ~ n/[8(n-1)] p^(1-n) log2(1/p).             (3)

Thus the all-interior-bias supremum is infinite for every fixed n>=2. No growth of arity is needed. In particular `delta(AND_2)=4p^2(1-p)^2`, and the ratio is asymptotic to `log2(1/p)/(4p)`. The sequence p_m gives exact rational instances on this path. This is the first failing line in the lead's proposed payment; finite-grid ratios are not promoted to a finite continuum bound.

Unary gates already have delta=0 and positive rare tax, but they are legitimate terminal gates with Hplus=0. The counterexample deliberately uses essential binary gates with strictly positive deficit, so it does not rely on dividing by zero or charging an irrelevant coordinate.

The finite grid's worst threshold at each arity n=3,...,6 is AND_n at m=14. At n=2, OR_2 and AND_2 tie exactly because their deficits and raw numerators are identical at equal bias. The diagnostic ratios (exact rational enclosures in CHECK_OUTPUT.json) are:

| arity | worst raw tax/deficit on the frozen grid |
|---|---:|
| 2 | 25,488.4763517 |
| 3 | 156,596,420.3449 |
| 4 | 1.14031193077e12 |
| 5 | 8.75777379660e15 |
| 6 | 6.88756171192e19 |

Each finite-grid maximum is certified by disjoint rational intervals after grouping exact rational ties. These values describe only the frozen domain. Formula (3) supplies the infinite continuum supremum.

### 3. Sequential exposure does not repair the AND obstruction

Define a gate-query tax bill as the sum over queried singleton nodes of their actual product reach probability times tau*(p_i). Require every terminal restriction to be a constant or signed literal, equivalently delta=Hplus=0. This admits early stopping at affine leaves and retains no uncharged nonaffine leaf.

For AND_2 every admissible deterministic policy must query at least one input: the root has positive deficit. Either query gives a constant child when the input is zero and a literal child when it is one, so exactly one query attains the minimum. Both wires have the same tax. Therefore

    inf_policy bill(AND_2)=tau*(p),
    inf_policy bill/delta ~ log2(1/p)/(8p).        (4)

Randomized policies are mixtures and have the same lower bound. A full computing policy, rather than affine-leaf stopping, pays tau*(p)(1+p). Additional queries cannot lower the nonnegative tax bill. The obstruction is therefore not only an unconditional input-sum overcharge.

For AND_n, until a zero is found or one input remains, all surviving restrictions are AND gates on the remaining wires. Every adaptive choice has the same state transition at equal independent bias. Consequently the exact best affine-leaf bill is

    tau*(p) sum_{j=0}^{n-2}p^j.                    (5)

Its ratio diverges as `[8(n-1)]^-1 p^(1-n)log2(1/p)`. The checker evaluates all symmetric threshold stopping policies via the exact state recurrence `Q(n,t)=1+(1-p)Q(n-1,t)+pQ(n-1,t-1)`, with Q=0 at constants/literals. The order independence here follows from symmetry and independence; it is not claimed for general gates. Allowing a nonaffine terminal root with separately paid Hplus could bypass the tax bill; that is a different mechanism, not refuted by (4).

### 4. Address gates expose the distinction between raw input sum and a stopped policy

Let a=1 or 2 address bits choose among N=2^a independent data bits, all address bits of bias r and all data bits of bias s; output is the chosen data sign. Then

    Var=4s(1-s),
    delta=8a r(1-r)s(1-s),
    raw tax=a tau*(r)+N tau*(s).                   (6)

To verify the deficit, data influences sum to 4s(1-s). Flipping a selector replaces one independent data bit by another; their disagreement probability is 2s(1-s), so each selector spectral influence is `8r(1-r)s(1-s)`. This uses the actual product law and accounts for all data labels.

Querying only addresses, then stopping at the selected literal, has bill `a tau*(r)`. If r=1/2 this is zero even for rare data, while the raw input bill divided by deficit diverges as `N/(4a)log2(1/s)`. Moreover in this fair-selector/common-data-bias case the exact corrected entropy is `Hplus=2a Var=4 delta`. Thus the raw input sum can count unnecessary data queries even on a well-paid address gate.

If data are fair but selectors tend to zero, the address-first bill divided by deficit is asymptotic to `log2(1/r)/4`; if r=s=p tends to zero, that bill/deficit is asymptotic to `log2(1/p)/(16p)`. We do not claim that address-first is optimal among all address-gate query orders. The AND obstruction already settles the best-policy universal failure. The search covers the three specified address regimes and retains all actual data labels.

### 5. Even the actual positive Shannon correction cannot be paid separately by delta

The blind scalar tax might seem merely inefficient. On AND_2 with both biases p, the actual correction has a separate obstruction. In order empty, X, Y, XY, its exact squared spectrum is

    P=((1-2p^2)^2,4p^3(1-p),4p^3(1-p),4p^2(1-p)^2).

Let v=4p(1-p). The physical X=0 child is constant and X=1 is the Y literal, with nonempty spectral mass v. The residual parent spectral bit has inclusion probability pv. Thus

    J=h2(pv)-p h2(v),
    M=H(P)-h2(pv),
    J-M=2h2(pv)-H(P)-p h2(v).                     (7)

These are physical-child/spectral mixture quantities. Spectral event conditioning is never substituted for those children. A direct simultaneous-bias expansion of the four explicit masses gives, with L=log2(1/p),

    h2(pv)=8p^2 L+(4log2(e)-8)p^2+O(p^3 L),
    H(P)=8p^2 L+(4log2(e)-8)p^2+O(p^3 L),
    p h2(v)=4p^2 L+(4log2(e)-8)p^2+O(p^3 L).

The leading constants cancel in (7), hence

    (J-M)/delta(AND_2)=log2(1/p)+O(p log2(1/p)).    (8)

For completeness, the remainders are justified by `-(1-x)ln(1-x)=x-R(x)`, where `0<=R(x)<=x^2/[2(1-x)]`, obtained by the convergent series `R=sum_{k>=2}x^k/[k(k-1)]`. Write each small mass as a fixed power of p times a nonvanishing polynomial and use `|ln(1-p)|<=p/(1-p)`. These estimates are uniform for 0<p<=1/16. This is a direct finite-polynomial path calculation, not an application of a fixed-child O(p) expansion while the residual bias moves. Equation (8) proves eventual positivity and a divergent ratio for the actual positive correction.

Five exact interval certificates have `(J-M)/delta` about 3.35394, 4.59188, 6.85328, 8.95179, 12.99553; their ratios to log2(1/p_m) are about .83375, .91630, .97865, .99457, .99965. At m=14 the certificate gives `12.99552 < (J-M)/delta < 12.99554`. The analytic calculation proves the limit; the intervals corroborate it.

### 6. Preserve corrected normalization before charging: the large logarithm cancels

For any finite Boolean sign under independent interior product biases, write `P0=(E f)^2`, `e(z)=z log2(1/z)`, `v_i=4p_i(1-p_i)`. The definition gives exactly

    Hplus(f)=H(P)-e(P0)+sum_i I_i(f)log2(v_i).     (9)

At a physical singleton query i, let Delta be parent minus actual biased average of its two children. Residual spectral marginals equal physical averages, so for j!=i, `Delta I_j=0`. The complete one-node ledgers are

    Delta Hplus=M_i+J_i+I_i log2(v_i)-Delta e(P0),
    Delta delta=I_i-P({i})
               =sum_{T nonempty}P(T union {i}).    (10)

The second equation uses `Delta Var=Var(E[f|X_i])=P({i})`. Both terms are nonnegative in the deficit decrement. These are the elementary corrected-entropy/variance chain rules; they specialize the existing A024 normalization interface rather than claiming a new class theorem.

For every actual gate restriction tree, telescoping (10) preserves the terminal terms:

    Hplus(root)=E Hplus(leaves)+sum_v reach_v[complete bracket in (10)],
    delta(root)=E delta(leaves)+sum_v reach_v[I_i-P({i})].

This is an identity, not a universal payment. Terminal Hplus and deficit cannot be omitted except at proved zero-deficit leaves.

On the same AND_2 family, actual children are constant/literal and their corrected entropies vanish. Direct normalized Fourier calculation gives

    Hplus/delta=2+[4p/(1-p)]log2(1/p) -> 2.         (11)

Thus the unbounded Shannon correction in (8) is canceled by the signed bias and empty-sector terms before payment. Charging tau* or `(J-M)_+` separately throws away precisely that cancellation. Neither obstruction disproves corrected product-biased FEI+, nor ordinary uniform FEI for the actual substituted Boolean family. The underlying disjoint AND/OR realization lies in the already paid binary read-once class.

**First unsupported line:** for higher prime gates or actual composed physical trees, pay the entire signed corrected bracket / recentered outer residual against one owned deficit or influence budget, together with all retained inner and terminal entropy. Equations (9)-(10) do not give that bound by themselves. A bound on scalar taxes alone is now rigorously excluded as that missing premise.

### 7. Independent review of A042's queued binary endpoint: HOLDS at stated scope

All essential binary tables are eight exceptional-corner gates and two parity gates. Output negation and input reflection with the corresponding bias reflection preserve each normalized squared mass and its input variance. Put `A(x)=x ln(1/x)/(1-x)`, with A(0)=0, A(1)=1. The inequality `ln y<=y-1` gives 0<A(x)<1, and `A'(x)=(-ln x-1+x)/(1-x)^2>0` proves strict monotonicity.

For a corner gate, let u,v be the two actual probabilities of its exceptional input values. The masses are `(2uv-1)^2,4u(1-u)v^2,4v(1-v)u^2,4u(1-u)v(1-v)`. Dividing its corrected entropy by its pair deficit gives `2+2[A(u)+A(v)]/ln2`. Its sharp supremum is 2+4/ln2, approached precisely when u,v both tend to one, with independently arbitrary rates. For parity, put a=4p(1-p), b=4q(1-q); the ratio is `[A(1-a)+A(1-b)]/ln2`, with sharp supremum 2/ln2 as both variances tend to zero. Fair zero singleton packets are omitted correctly; the fair unit pair still has positive deficit. Deterministic contracted gates have Hplus=delta=0 and no defined ratio.

The earlier independently reconstructed disjoint composition law has nonnegative weights alpha_i and exact `Hplus(F)=Hplus(g)+sum alpha_i Hplus(f_i)`, `delta(F)=delta(g)+sum alpha_i delta(f_i)` at actual induced means. Induction therefore transfers the sharp common binary constant through a genuine disjoint binary read-once tree, with constants contracted. On uniform physical inputs, `e((E F)^2)<=Var(F)/ln2` turns the corrected bound into ordinary `H<= [2+4/ln2] I`. No fixed bias relation, depth penalty or unpaid deterministic division is introduced.

This reconstructs every assertion in `A042-SHARP-BINARY-PRIME-ENDPOINT@1`, without the source checker and without supplying a substantive repair. The independent finite check covers all 16 tables at 25 rational bias pairs (400 cases): 200 corner, 50 parity, 150 constant/literal cases. Exact prime-log coefficient equality verifies both formulas, including signs and zero packets. The source's extra quantitative remainder inequalities are not part of that exact claim statement and are not separately certified here. The review does not extend the binary constant to higher primes.

## executed validation with domain, arithmetic, commands and outputs

Frozen before pilot: out/FROZEN_SPEC.json. The first implementation's exact interval denominators exceeded Python's integer serialization limit; no mathematical assertion failed. Version 2.1 freezes outward rounding of log2 enclosures to rational multiples of 10^-24 and stored endpoints to 10^-18, with unchanged family/domain. A diagnostic strict-max assertion then correctly exposed the exact AND/OR arity-two tie; ties are now grouped by equal rational deficit and numerator before comparing other interval groups. Both events are preserved in out/PILOT_FAILURE.json and out/PILOT_TIE_CORRECTION.json; neither is counted as stagnation of the mathematical mechanism.

Commands from A045:

    python -X utf8 runs/20261013T212421Z-account05-A045-biased-realizability-referee/code/check.py --pilot
    python -X utf8 runs/20261013T212421Z-account05-A045-biased-realizability-referee/code/check.py
    python -X utf8 runs/20261013T212421Z-account05-A045-biased-realizability-referee/code/binary_review.py

Pilot PASS: 359 assertions, 18 threshold and 14 address cases in 0.1312 computation seconds. Before the main run, exact formal-log equality checks of (10) were added without changing the frozen search domain. Main PASS: 1,348 assertions, 126 thresholds, 32 address gates, five endpoint certificates, 36 normalized physical node ledgers, 1.6583 computation seconds. Independent binary review PASS: 1,200 assertions, 400 tables/bias fixtures, 0.0454 seconds. Total final main/review assertions: 2,548. out/CHECK_OUTPUT.json and out/BINARY_REVIEW_CHECK.json store exact outputs; bias checkpoints were saved as the search progressed.

The log enclosure reduces x=2^k u to 1<=u<=2, sets z=(u-1)/(u+1), and uses the first N=32 terms of `ln u=2sum z^(2j+1)/(2j+1)`, with omitted tail at most `2z^(2N+1)/[(2N+1)(1-z^2)]`. Signed scaling reverses endpoints and division checks every rational corner. All rounding is outward. Stored decimal midpoints are diagnostics only. Finite signs/maxima follow from rational disjoint intervals; identities in (10) use exact rational coefficient dictionaries of formal log arguments after expanding product logarithms, not mere interval intersection. The binary formulas use exact prime-log coefficient equality. No inference from log-prime independence is needed: coefficient equality is a sufficient proof of equality.

Dimensions and domains never escalate. Memory estimate is 70 MB for the search, 30 MB for binary review, not measured peak memory; no job was expected to exceed 300 MB, so memok was not required. No heavy job, GPU, foreign write, git or background process was used. The all-bias obstructions and binary suprema follow from the analytic derivations, not extrapolation from the fixed finite grid.

## proof dependencies and changed downstream conclusions

The sharp tax formula on p<=1/16 is inherited from prior A045's complete scalar convexity reconstruction; the already established rare coefficient is used for the payment obstruction, not reopened as a new target. The lead source claim now exists and is pinned, but its larger p0 numerical threshold/AND-attainment statement is outside this stage's review. A042's binary claim is independently accepted at its exact original statement and hash. Product Fourier inversion, Parseval, entropy/variance chain rules and elementary scalar logarithm estimates give the remaining self-contained derivations.

The precise refuted candidates are: a finite K paying every raw input tax sum by gate deficit; a finite K paying the best affine-leaf query tax bill by root gate deficit; and a finite K paying every positive actual singleton Shannon correction by gate deficit. Their essential Boolean witness is equal-bias AND_2. There is no dependency invalidation of the lead's valid upper-tax statement, A024's signed interface, A057's capped activation bank, or A042's corrected binary theorem. A100's different tax-tree diagnostic remains true at its stated scope.

B09 should replace the unpayable scalar-tax-sum target with the full signed corrected normalization charge. A050/A057 can use the explicit gate-input/underlying-physical distinction when inserting a budget into a composed tree. A098's higher-level frontier remains unpaid: `R_ge2=sum_{|S|>=2}sum_{i notin S}Phi(P(S),P(S+i))<=K I` still needs one normalized derivative reference, not a new tax calibration or repeated full-I charge at each Fourier level. No shared status index is changed.

## one next mathematical action and independent reviewer

NEXT: consume A041's exact two-group normalized coefficient/deficit Gram interface and A024's signed recentering formula to build one complete reference for its mixed higher-degree sector. Test the reference on an actual biased prime boundary while retaining every bias normalization, empty-sector subtraction and terminal inner entropy. This follows B09's live gate target and A098's requested higher-level reference rather than repeat a refuted scalar payment. A091 is primary independent reviewer; A085 should check the rational interval maxima and simultaneous-bias remainder; A090 should challenge the best-policy quantifiers and original physical-cube scope. A042 receives its source-bound binary acceptance record. No message is sent to another agent.

## actual persistence receipts or precise save blocker

This run's REPORT.md, CLAIMS.json, PROGRESS.json, identical PACKET_DELTA.json, code and out specifications/failures/checkpoints/certificates/review records are written only inside A045's assigned run. STATUS.md is exactly two lines; WORKLOG.md is appended and LEARNED.md updated under A045 only. out/SOURCE_RECEIPTS.json pins files actually read and out/PERSISTENCE_RECEIPTS.json records local byte sizes/hashes. The finalizer checks exact protocol field sets, unchanged source statement hash for the review, progress-copy equality, report fields and the 20 MB cap. Supervisor adoption/copy, mirror verification, downstream use and independent review of the new payment obstruction remain pending. There is no local save blocker.

**Universal bridge:** This stage moves B09's C025/G-BIASED-LTF prime-gate interface and the C019 transfer audit by conclusively excluding separate sharp-tax and even separate actual-Shannon-correction payment by root spectral deficit, already at an essential binary gate with realizable product laws; it independently accepts the sharp corrected binary endpoint and pinpoints the signed bias/empty-sector cancellation that any viable payment must preserve. It improves no universal FEI constant and does not refute corrected product FEI+. The remaining higher-prime mixed-sector / actual physical-tree charge plus retained inner and terminal entropy needs one normalized reference and one owned influence budget. NEXT builds that reference from A041/A024's exact interfaces, the shortest route past the now-settled scalar-payment obstruction rather than another isolated gate census or repeated half-tax calculation.
