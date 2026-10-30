# exact target, quantifiers, hypotheses and units

A003/B01 stage 2, run 20261012T005637Z-fleet05-A003-minimal-target-formulation. Full FEI remains OPEN. The lead now directs A003 to add erasure-fraction and low-influence arrows, identify a quantitatively stronger selection lemma, and test its coordinate cutoff on X003/X009/B05. This supersedes the prior rolling NEXT coding-debt experiment for this stage. No previous implication inventory or known-family argmin was rediscovered.

For every finite uniform Boolean cube, H is squared-Fourier entropy in bits, I=sum_i alpha_i, alpha_i=Inf_i, B_i=H(S_i|S_-i), B=sum B_i, Delta_i=H(f)-average child H, and JS_i=Delta_i-B_i. Constants have H=I=0. Put a=2/ln2. The cutoff uses d=# relevant inputs, not padded ambient dimension: G_c={i:alpha_i>=c I/d}, c in (0,1). This is stronger than the corresponding ambient-n cutoff and removes dummy-padding ambiguity. All inequalities below quantify uniformly over dimension.

The candidate P4 is an explicit OPEN fixed-budget target: every nonconstant f with max_i alpha_i<1/4 has some i in G_(1/2) satisfying B_i<=4alpha_i. It would imply FEI at 4+2/ln2. This stage proves conditional arrows, exact substitution identities and a stronger-rule refutation; it does not prove P4 or a universal erasure-fraction payment.

# sources actually read, revisions and theorem locators

At stage start: BOARD.md supervisor snapshot 2026-10-12 00:49 UTC; claude/B01/STREAM_NOTES.md v1 2026-10-11 22:40 UTC (now present); own STATUS/LEARNED and previous stage. EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was re-read completely. out/SOURCE_MANIFEST.json pins actual bytes, hashes and locators.

New source-bound inputs:

* A001 stage 2, 20261011T231625Z REPORT sections 2-5 and CLAIMS: exact X009 and B05 directed packets, influence types and existing root argmins. A001-LOCAL-ERASURE-AND-DECREMENT-ARGMIN@1 is author-proved pending independent review; its B05 erasure subclaim consumes A089-EXACT-EXISTENTIAL-ERASURE-REPAIR@1, independently accepted by A001 at r=2k. This run does not adopt broader r or A062 claims.
* A002 stage 2 ERASURE_LEDGER: transformation B/H admission obstruction, exact product case and near-erasure bridge. These ledgers are retained, not re-proved. The maximum-selection obstruction below is a new retained-coordinate use of balanced substitution.
* A086 stage 2 JOINT_CODE_REVIEW, 20261011T234041Z: HOLDS at original scope for both A003 v1 claims, with a full independent reconstruction. This is recorded as a local review receipt, not inferred from the board alone. Previous run files and shared indices remain unchanged.
* LOG_ALLOCATION_CURATED sections 2-4: explicit B05/X003 construction and independently archived selector lower bound (1-delta)(k-2). X003 here is the same sparse-activation mechanism as canonical B05, not a third disjoint family. The earlier B05/B19 theorem remains accepted at its all-coordinate scope.
* Source ERASURE_REDUCTION sections 1-4, already pinned in stage 1: actual split and influence identities, JS_i<=a alpha_i. The scalar h2(alpha)<=alpha log2(e/alpha) is proved directly by -(1-alpha)ln(1-alpha)<=alpha. Balanced majority coefficients are derived below; no new external literature premise is needed.

The B02 lead's single-gate-collapse and tribes obstruction notes were read: this stage accordingly avoids another single-order witness calibration. The source notes distinguish known class bounds, pending author claims and universal open payments. The review cap is respected by verifying/refining existing B01 interfaces and producing a scoped refutation, rather than proposing another broad positive universal proof candidate.

# complete derivation or exact first unsupported line

Full source-complete proofs are saved in [DERIVATION.md](DERIVATION.md), sections 1-5. The mathematical delta is summarized here with the decisive arguments.

## Added arrows and the constant loss of a coordinate cutoff

```mermaid
flowchart TD
 AF[Restriction-closed: B <= lambda H + K I] -->|C=(K+2/ln2)/(1-lambda)| FEI[FEI C]
 WL[Weak regime: exists i, B_i <= lambda H/I + K times alpha_i] -->|C=max log2(e/tau)+2/ln2, (K+2/ln2)/(1-lambda)| FEI
 WLG[Same weak rule; i must lie in G_c] -->|same forward C| FEI
 FEI -->|lambda=0; K=C/(1-c)| WLG
 BF[Weak regime: B_G <= lambda H + K I; lambda<1-c] -->|C=max log2(e/tau)+2/ln2, (K+(2/ln2)(1-c))/(1-c-lambda)| FEI
 P4[OPEN: c=1/2, tau=1/4, K=4, lambda=0] -->|C=4+2/ln2| FEI
 MAX[Fixed-price maximum-influence coordinate] --> BAD[REFUTED by majority-diluted B05]
```

All lambda in the first three arrows lie in [0,1); K>=0; tau in (0,1). In the restricted-bucket arrow lambda in [0,1-c). All quantified source classes must contain every reached restriction needed by the induction, or be all Boolean functions. A root-only property is not a class theorem.

Proof strategy: if H>CI, choose a violating function with least relevant dimension and write delta=H-CI>0. Each actual child satisfies the C bound, giving Delta_i>=C alpha_i+delta and B_i>= (C-a)alpha_i+delta for every relevant i. Summing contradicts B<=lambda H+KI at C=(K+a)/(1-lambda). For a weak coordinate satisfying the local fraction inequality, Delta_i<=(lambda C+K+a)alpha_i+lambda delta alpha_i/I; the displayed C makes it strictly smaller than C alpha_i+delta. Outside the weak regime a maximum influence at least tau has B_i<=alpha_i log2(e/tau), which supplies the strong-coordinate constant. This proves the lead's arrows without a circular assumed bound on H/I at the current node.

The high-bucket fraction beta=I_G/I is at least 1-c+c/d>1-c. Weighted averaging gives a cutoff coordinate at price B_G/(beta I). Therefore FEI(C) already implies high-cutoff selection at K=C/(1-c). Adding that cutoff with an unspecified finite K is FEI-equivalent in finiteness, not a genuinely stronger finiteness theorem. This is an explicit qualification of the lead's proposed example. At a prescribed budget it is a stronger operational requirement; P4 freezes that budget rather than hiding an unknown FEI constant. No canonical smallest lemma exists over all conceivable formulations. The exact first stronger claim in this frozen route is P4 itself.

For P4, the strong branch costs 2+3/ln2, below 4+2/ln2 because ln2>1/2, and the weak branch costs 4+2/ln2. Hence its forward universal constant is exactly the stated sufficient value. The diagram does not supply P4 from FEI at that value with the same K=4.

## Tests consume known minima and add eligibility

With delta=2^-k,p=delta^2,s=sqrt(delta), u=1/2+delta,A=1-s+delta, canonical B05 has alpha_data=pu, alpha_control=pA, alpha_selector=pdelta and I=p[k u+2kA+delta] on 3k+1 relevant coordinates. Data eligibility at c=1/2 is the strictly positive identity

    2(3k+1)u-[k u+2kA+delta]
      =k(1/2+2s+3delta)+1+delta>0.

Controls are larger and eligible. The already-computed erasure minimizer (data for k=4, control for even k>=6) is therefore always eligible and has price below 2+7/1024<4. All root influences are below 1/4. This passes P4 at those roots, not at unexamined descendants. X009's data coordinates are eligible with price below 2, but their influence exceeds 1/2: that root is outside the weak regime and is labelled accordingly.

## New retained-coordinate identity and maximum-rule obstruction

Replace background inputs of any Boolean f(y,x) by disjoint balanced Boolean encoder blocks and retain y. Every encoded spectral frequency determines its outer label by whether each block is nonempty. Its two y-sector coefficients share the same encoder multiplier. Binary edge entropy is homogeneous, so summing squared multipliers by Parseval proves B_y, alpha_y, Delta_y and JS_y are EXACTLY unchanged. Background influence multiplies by its encoder bit's influence. This is a genuine Boolean composition, not a real normalized mixture.

For odd Majority_M, every nonzero spectral set is odd. Adjacent internal frequencies can both be occupied only when they are empty and singleton. With rho=binom(2R,R)/2^(2R), M=2R+1, each inner influence and singleton coefficient equals rho. Therefore

    B_inner=sum_(T not containing j) Phi(p_T,rho^2p_(T+j)),
    alpha_inner=rho alpha_j,
    B_inner/alpha_inner
      <=rho[log2(1/alpha_j)+2log2(1/rho)+2/ln2].

The bound follows from Phi(u,tv)<=tv/ln2+tv[log2(1/t)+log2(1+u/v)], then L_j<=B_j<=h2(alpha_j). All other outer coordinates, including y, stay in the sum.

Now retain B05's selector and replace all 3k backgrounds with Majority_M for R=2^(2k+2), M=2^(2k+3)+1. Induction from the central-binomial recurrence proves rho<=1/sqrt(R+1)<delta/2; also M rho>=1. Original background influences lie in [p/2,p]. Thus the selector has unchanged alpha=pdelta, every other alpha is strictly less than pdelta/2, and the selector is the unique maximum-influence input. Its ratio remains at least (1-delta)(k-2), diverging. All influences tend to zero; total I also tends to zero by the upper bound in DERIVATION section 4. This analytically refutes, for every fixed finite K and every tau>0, the proposal that a maximum-influence coordinate of every weak function can satisfy B_i<=K alpha_i. It also refutes the same fixed-price maximum rule for Delta_i. It does not refute a lambda H/I allowance or FEI.

On that SAME family every encoded background lies above I/(2D), D=3kM+1, since M rho k(5u-2A)+2u rho>=k/2>delta. The new inner bound gives every background ratio <=(4k+3+2/ln2)/2^(k+1)<1. Thus P4 has many eligible cheap coordinates while its unique largest input is arbitrarily expensive. This is a checked all-parameter separation, not a floating search pattern.

The first unsupported line is P4 for arbitrary weak Boolean functions and their reached restrictions. Balanced encoder blocks cease to be balanced after one inner input is physically restricted; their induced mean is +/-rho, so the root invariants above cannot be silently reused. No universal high-bucket fraction or full C018 payment is proved. Stage 1's C020 coding-debt inequality remains open and is not claimed advanced by this localization.

# executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was written before the pilot; FROZEN_SPEC_V2.json records a serialization-only repair before replay. V1 completed and saved all 276 source substitution cases, then raw Fraction string conversion exceeded Python's 4,300-digit limit. V2 uses exactly checked outward rational rounding to denominator 10^12 for displayed certificate bounds, retaining the same internal arithmetic, dimension domain and 48-term interval precision. Its replay hit the 60-second guard during the already-completed substitution loop. FROZEN_SPEC_V3.json reuses that completed V1 checkpoint and runs only the remaining family certificates, caching repeated interval expressions. Both failures are preserved in out/; neither is a failed mathematical inequality.

Commands executed: python -X utf8 runs/20261012T005637Z-fleet05-A003-minimal-target-formulation/code/check.py (V1,V2); python -X utf8 runs/20261012T005637Z-fleet05-A003-minimal-target-formulation/code/check.py --families-only (V3); python -X utf8 runs/20261012T005637Z-fleet05-A003-minimal-target-formulation/code/finalize.py. The final accumulated validation has 12,556 exact assertions PASS, with V3 family runtime 0.877 seconds rounded upward; the original substitution runtime is recorded separately in out/SUBSTITUTION.json. The check uses integer Walsh transforms, Fraction masses, exact log2-prime expressions for substitution identities, and rational atanh-series enclosures for family inequalities. After power-of-two reduction, the 48-term ln remainder is bounded by 2|z|^97/[97(1-z^2)], |z|<=1/3. No decimal or float sign is a certificate.

The frozen checks cover all 276 labelled source functions on 1..3 inputs with retained coordinate 0 and Majority_3 on all other inputs; all new inner-coordinate erasure formulas, selector Delta/B/alpha identities, X009 k=4,6,8,10, B05 k=4,6,8,10,12,14,16, and full B05 k=4 spectra on 13 physical bits. The enormous majority-diluted F_k is proved symbolically for all even k>=4; its full truth table is not enumerated. out/VALIDATION.json records actual assertion counts, runtime and rigorous rational bounds. out/SUBSTITUTION.json was saved immediately after the substitution subjob. All computation is under the frozen 120 MB estimate; no job over 300 MB, GPU, dimension escalation or window-opening command was used.

# proof dependencies and changed downstream conclusions

The erasure/JS identities are source-established; the new localization arrows are proved in DERIVATION without assuming universal FEI. Existing A001/A089 family ordering is consumed and credited, with finite signs independently checked here only at the declared domain. The all-k maximum obstruction uses the independently archived B05 selector lower bound, an exact balanced-substitution invariant and an elementary central-binomial recurrence. Its proof dependencies are acyclic. A086's prior A003 reviews are carried as local records, not a new shared-registry adoption.

B01/A005 should distinguish high-average eligibility with freely adjustable constants from a fixed-budget lemma. B06/A026/A028 must avoid maximum-influence fixed-price selection even when total influence vanishes; full terminal entropy remains essential. A001's cheapest known coordinate is above the half-average cutoff, so its root minima can be consumed without relaxing the cutoff. A088 can independently reconstruct the odd-encoder internal spectral-edge formula. Nothing here requires withdrawing good-coordinate C018, stopping-tree C019, or the lead's fraction localization.

# one next mathematical action and independent reviewer

Next: derive the high-bucket erasure transport after one physical Majority_M encoder input is restricted, retaining the induced encoder mean +/-rho, the coherent empty/singleton rows and full child/terminal entropy. The root-level counterexample and eligible alternatives are now exact; the shortest remaining gap is heredity of a paid selection policy, not another root family. Independent reviewers: A087 for the low-influence constants and all-k maximum-rule obstruction; A088 for balanced/odd-encoder spectral pair identities; A094 for the distinction between fixed-budget P4 and finiteness equivalence.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, DERIVATION.md, IMPLICATION_DELTA.json, frozen specs, code/ and out/ are saved only in this run. Rolling STATUS/WORKLOG/LEARNED are updated in A003 only. out/SCHEMA_VALIDATION.json checks exact field sets (normalizing the protocol's explanatory packet_ids annotation to its required machine key); out/ARTIFACT_RECEIPTS.json hashes every artifact except itself. No shared index, other agent file, brain store, external service, git repository or protected trading folder was changed. Supervisor mirror copying and independent acceptance of this stage are pending. No save blocker remains.

**Universal bridge:** This stage moves C018's formulation by proving the erasure-fraction/low-influence arrows with explicit constants and the exact cutoff loss C/(1-c); it shows why a free-constant cutoff still restates FEI, while freezing the open price-4, half-average weak-coordinate target with sufficient FEI constant 4+2/ln2. It also rigorously retires maximum-influence fixed-price selection on an actual all-weak, vanishing-I Boolean family, while preserving many eligible price-below-one alternatives. No universal bound on B/I or H/I is gained. What remains is the fixed-budget eligible-coordinate lemma on all reached restrictions. NEXT attacks the first loss of balance after a real query, with coherent child spectra and terminal entropy intact, so it tests the universal hereditary bridge rather than closing another isolated class.
