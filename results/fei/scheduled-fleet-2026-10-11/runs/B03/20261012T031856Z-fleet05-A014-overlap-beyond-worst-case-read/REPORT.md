# A014 stage 2 — bounded intersections, complete sparse payment, and local blocking repair

## exact target, quantifiers, hypotheses and units

Run `20261012T031856Z-fleet05-A014-overlap-beyond-worst-case-read`, B03/A014. Uniform finite cube, Boolean +/-1 outputs, Fourier entropy and code costs in bits, ordinary total influence. Full FEI and the unrestricted linear-hypergraph target remain OPEN. This stage extends and repairs the previous A014 interference mechanism rather than opening another unrelated broad candidate.

The new complete theorem is: for an OR of distinct nonempty positive conjunctions with widths w_l<=W and pairwise support intersections <=t, t>=1, define mu=sum_l 2^(-w_l), theta=2^t mu. If theta W<=1/16, then **H(f)<71 I(f)**, independently of worst read, gate count and dimension. A common global coordinate reversal preserves the statement. Arbitrary mixed literal orientations are not asserted. The condition uses incidence and gate activation data, not H or an assumed FEI inequality.

The local rank theorem is separate: after factoring all nonincident gates disjoint from the incident residual support into a common outside factor C_j, the local pressure theta_j in DERIVATION.md suffices for **R<47I** when theta_j W_j<=1/16 at every relevant coordinate. This has no global-density hypothesis, but does not pay the complete whole-set reference. Its coordinatewise-minimum assignment differs from the single whole-set owner in the complete sparse theorem.

Explicit unbounded-read example: the q^2 nonvertical affine-line conjunctions on F_q^2, for every prime q>=19, have width q and read q, with 2q^3 2^(-q)<=1/16. The theorem gives 71 against the original bound 41+7log2 q. We do not re-enumerate or reprove the lead's separate projective-plane result.

## sources actually read, revisions and theorem locators

Read BOARD snapshot 2026-10-12 03:24 UTC (relevant B02/B03 and review updates), B03 STREAM_NOTES v2 (23:2xZ), own STATUS and LEARNED, and execution protocol `fei-execution-protocol/2`, revision `2026-10-11-execution-v2`. Read A009 LEARNED: affine-plane coordinatewise pressure is an obstruction to that separate metric, not to a paid whole-set description.

Read the lead run `claude/B03/runs/20261011T223500Z-claude-B03-pp-congestion/CLAIMS.json`. Its complete PP proof cites REPORT sections 3.2-3.4 and Lemmas O/G, but REPORT.md was absent. Its claims and scalar evidence therefore guide dispatch only; we do not consume the full PP constant as a source-complete accepted premise. The registry-writing helper was checked for an alternate persisted report payload. No lead artifact was modified.

Mathematical baseline actually used: `research_pushes/2026-10-11-full-fei-100-agents/baseline/current-threshold-paper.tex`, Section 5: signed rank tail (`lem:ranktail`), fixed-noise rarity (`union:rare` / `union:raretail`), subset normalizer (`union:normalizer`), source-component forest (`union:forestcount`), and K0/E0 (`union:K0`, `union:E0`). Re-read the queue and forest passages directly, retaining the square root in B_*=sqrt(2e). Previous A014 v1's generic ideal-piece proof and complete root-normalizer accounting are retained; the present derivation replaces its PP-specific use with a general bounded-intersection argument.

## complete derivation or exact first unsupported line

The full source-complete proof is saved immediately in [DERIVATION.md](DERIVATION.md), hash-bound in CLAIMS/receipts. Its dependency chain is:

1. For any Fourier decomposition d=sum_l u_l+r, projected Young's inequality retains the exact signed cross sum:

       ||P_E d||^2 <=(1+eta)[sum_l||P_Eu_l||^2+sum_{l!=m}<P_Eu_l,P_Eu_m>]
                        +(1+1/eta)||P_Er||^2.

   The same holds for a nonnegative Fourier-cost multiplier. No cross term is discarded for an arbitrary union.

2. For positive AND gates at coordinate j, let S_j count satisfied incident residual clauses and B_j the event of a satisfied nonincident clause. Then d_jf=1[S_j>0]1[not B_j]. Writing a_j=sum_incident 2p_l, pairwise intersection estimates yield

       C_j=E[S_j(S_j-1)]<=2^(t-1)a_j^2,
       E[S_j 1[B_j]]<=2^t a_j(mu-a_j/2),
       ||d_jf-S_j||^2<=theta a_j,
       Inf_j(f)>=(1-theta)a_j.

   Thus Q=sum_j a_j=2sum_l w_l p_l and I>=(1-theta)Q. The ideal cross spectrum is nonnegative and has exact total mass C_j. Nonnegative products, rather than nonnegative individual FWHT amplitudes in every bit convention, are the required property.

3. A good Fourier set A is contained in some gate. Assign it wholly to the gate minimizing SUM_j G_jl(A). Its ideal diagonal weights (2p_l)^2 are identical across j in A, so the minimizing owner's total cost is at most the weighted average over owners. For a bad set all ideal derivative amplitudes vanish. With Gmax<=(11/5)W, the published piece tails and multiplier lemma give

       R<=[2E0+(44/5)theta W]Q,
       E_p[|A|1[bad]]<=theta Q.

   This averaged whole-set argument is not a claim that one owner minimizes each coordinate separately.

4. Use one fixed queue with root odds p_l and child-gate prior p_l/sum_incident p_m. Root normalization is Lambda=sum_l log2(1+p_l)<=mu log2 e. A child name costs <=w_l<=W, because mu<1. Good sets need one root and no child/subset congestion. Bad sets cost <=(11/5)W|A| in additional names and subset allocation, using log2 N<=W. Dense root rarity and sparse root rarity are paid in the original forest manner; all elementary costs contribute K0 I. Consequently

       H<=h2(v)+v Lambda+K0 I+L+S+R,
       L+S<=(11/5)theta W Q.

   Gibbs uses Q(empty)=1-v and Q(A)=v Q1(A). The term is v Lambda, not Lambda erased or an independently optimized normalizer.

5. Use h2(v)<=2I, v<=4mu, Q>=2mu, K0<22, E0<108/5. The exact final expression is

       H/I <24+[2E0+11theta W+3mu]/(1-theta)
            <24+[216/5+11/16+3/32]*(16/15)
            =10637/150<71.

6. The raw approximation has an exact dense read-one obstruction: on m disjoint width-w clauses,

       ||d_jf-u_j||^2/Inf_j=(1-2^(-w))^(-(m-1))-1 -> infinity.

   These functions already satisfy C003 with k=1. This refutes a density-free normalized raw-remainder helper, not FEI. Factor distant false-clause constraints into C_j. Its independence from the incident residual variables and decreasing/increasing covariance induction pay only nearby blockers. The exact local pressure theta_j in DERIVATION yields

       E_nu_j G_j <=[2E0+4theta_j Gmax_j]/(1-theta_j),
       R<(140/3)I<47I if all theta_j W_j<=1/16.

**First unsupported line for the lead's unrestricted target:** a whole-set reference can pay the spectra of these common outside factors and shared blocking once, together with actual roots/labels/subset costs, when global pressure 2^t mu W is unbounded. Neither the complete sparse theorem nor the local rank theorem establishes that line. A dimension-independent O(t) intersection payment beyond the present 2^t activation condition is also unproved. No FEI disproof or unconditional all-linear-hypergraph theorem is claimed.

## executed validation with domain, arithmetic, commands and outputs

Frozen domains precede computation in FROZEN_SPEC.json and LOCAL_FROZEN_SPEC.json. Pilot v1 exposed a character-convention mismatch: integer FWHT uses (-1)^bit, while positive conjunctions use 2bit-1. At odd indices all ideal amplitudes share a negative sign in FWHT convention, but their cross products are still positive. Fixed the sign assertion before rerun; preserved failure in out/pilot_failure.txt. No mathematical hypothesis or domain changed.

Pilot v1.1: all **166 labelled nonconstant monotone antichain DNFs on n=4**, no symmetry reduction; **40,639 assertions PASS**, **37.31487 seconds**. Rational atanh-series intervals certify H<=4I on that finite domain. The small truth-table domain has no cover satisfying the infinite theorem's sparsity condition; these checks validate the structural identities and finite class certificates, not an inference from small n to the sparse theorem.

FULL_VALIDATION_PENDING

Main fixed job: all 2,109 nonempty labelled uniform hypergraph families on n=5, widths 1 through 5, plus the 166 pilot covers, total 2,275. Exact integer truth tables/FWHT, Fraction physical remainder/influence/cross bounds, exact rational whole-owner objectives, bad-set payment, and rational H<=4I signs. Pilot cap 60 seconds; full cap frozen at 1,200 seconds after the observed pilot, below the 30-minute limit. Estimated memory <100 MB; no job expected over 300 MB. Stored entropy intervals are rounded OUTWARD to a rational 1e-6 grid; decisive comparisons remain exact internally.

Local job is sequential after the main job: 166 n=4 antichains plus disjoint width-two clauses at m=1,2,3 (fixed cubes n=2,4,6), and 192 symbolic disjoint-clause ratios. It checks covariance, conditioned cross spectra, influence and residual bounds. No automatic dimension escalation or parallel compute jobs.

Commands:

    python -X utf8 runs/20261012T031856Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py --pilot --out runs/20261012T031856Z-fleet05-A014-overlap-beyond-worst-case-read/out/pilot.json
    python -X utf8 runs/20261012T031856Z-fleet05-A014-overlap-beyond-worst-case-read/code/check.py --out runs/20261012T031856Z-fleet05-A014-overlap-beyond-worst-case-read/out/check.json
    python -X utf8 runs/20261012T031856Z-fleet05-A014-overlap-beyond-worst-case-read/code/local_check.py

The logarithm kernel sums 28 rational terms of 2atanh((x-1)/(x+1)) after scaling to [1,2), with explicit omitted tail 2z^57/[57(1-z^2)], and divides using rational ln2 endpoints. No floating-point mathematical sign is used. The full proof supplies the arbitrary-dimension theorem. Affine-net incidence certificates at the fixed primes q=19,23 use exact point sets, not large Boolean truth tables.

## proof dependencies and changed downstream conclusions

Dependencies are C003's published signed rank/rarity and finite queue/forest facts, and elementary Fourier/physical identities, Young's inequality, and a proved covariance induction. No unreviewed full PP theorem, generic coherent entropy subadditivity, or asserted universal FEI premise is used. The previous A014 version remains valid and is extended by version 2, with its immutable source retained.

B03 can now replace all three read bills in the complete sparse bounded-intersection regime, including unequal widths. A009's coordinatewise affine pressure obstruction remains intact: the present description pays labels per used whole gate, and suppresses bad-frame bills with the actual spectral residual. A011/A012/A013 can consume the local outside-factor cancellation as a rank-payment interface; they must retain its assignment and whole-set normalization gap. Independent reviewers A086/A094 should reconstruct the owner SUM averaging, covariance sign and all queue odds, rather than merely checking the scalar constant. No independent acceptance of the present version is claimed.

## one next mathematical action and independent reviewer

Next: build a joint whole-set witness for the local ideal derivatives C_j u_jl, assigning the outside-factor spectrum and shared blockers once, and compare its actual label/subset cost with the local-pressure rank budget. This addresses the exact dense-regime failure exhibited by read-one clauses and avoids repeating known read-once or plane calculations. Reviewers: A086 and A094; none has reviewed this version. The unrestricted linear-hypergraph and O(t) targets remain explicit open obligations.

## actual persistence receipts or precise save blocker

All edits are confined to A014. REPORT, DERIVATION, CLAIMS, PROGRESS, PACKET_DELTA, frozen specs, code and exact outputs are saved in this run; rolling STATUS/WORKLOG/LEARNED are current. out/receipts.json records SHA256 and sizes and validates protocol field sets, including the compatibility key packet_ids. Finalization checks every artifact below 20 MB and equality of PROGRESS/PACKET_DELTA. Supervisor copies, GitHub/Brain mirrors, independent review, adoption and downstream use are not claimed. No git, messaging, Brain writes, peer-folder edits, deletion, GPU, window or background helper was used.

**Universal bridge:** This stage moves C020 whole-set witness cost from a PP-specific rank repair to a complete sparse bounded-intersection theorem with every root, gate label, subset, rank and normalizer cost paid by less than 71I, despite unbounded read. It also repairs the raw residual's dense read-one failure through common outside factors, paying the local rank term by less than 47I without global sparsity. What remains is one whole-set code charging outside-factor spectra and shared blockers once in the dense regime, plus a noncircular O(t) intersection refinement. The next joint ownership calculation attacks the only unpaid bills left by the repaired derivative representation, which is the shortest route toward the stream's universal cover payment rather than another isolated known-class FEI bound.
