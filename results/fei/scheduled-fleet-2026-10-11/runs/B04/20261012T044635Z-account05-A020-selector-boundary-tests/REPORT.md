# A020 stage 2: five-bit boundary falsifier and complete selector census

## exact target, quantifiers, hypotheses and units

Follow B04 STREAM_NOTES.md v2's A020 targets: (i) test whether every one-bit physical split with influence d>=1/8 has Delta_i/[(3/ln2)d+2I(D_i)]<=81/100; (ii) check B04-SEL-LOG-SHARP@1 for all a=3,m<=2 multiplexers. Inputs are independent uniform bits, outputs +/-1, entropy in bits. Here D_i=(f|x_i=0-f|x_i=1)/2, and I(D_i) is Fourier Dirichlet energy, not trinary edge-disagreement probability.

Result (i) is FALSE on five variables: an exact d=1/8 witness has ratio greater than 17/20. Result (ii) passes completely, with the stronger finite cap 9/10. The original B04-NODE-BOUNDARY@1 remains valid and also has finite ratio cap 9/10 on all five-bit nodes with d>=1/8. These finite caps are not asserted beyond the checked dimensions.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-12 04:39 UTC, B04 STREAM_NOTES.md v2 dated 2026-10-11 23:25 UTC, own STATUS.md and the full execution protocol revision 2026-10-11-execution-v2. The board says A018 already independently reconstructed the lead's selector, bent-sharpness and node-boundary claims and certified the 81/100 node cap through dimension four. Accordingly, no four-bit singleton census or bent asymptotic was restarted.

Read A018's stage-2 REPORT.md (run 20261012T010436Z-account05-A018-shared-data-collision-law), especially its node-energy normalization, exact four-bit cap, and open C019 stopping-tree line. Read B04 lead CLAIMS.json, exact versions B04-SEL-LOG-SHARP@1 and B04-NODE-BOUNDARY@1. The lead's proposal of 81/100 at d>=1/8 is an exploratory question in the notes, not part of either original theorem.

Read A071's stage-2 REPORT.md, code/full_census.py and out/full_census.json, run 20261011T233808Z-account05-A071-search-space-design. Its 132.765-second five-bit erasure census supplied a feasibility benchmark and symmetry-enumeration design; none of its erasure endpoint results is needed for our entropy certificate. Our entropy, selector-block, derivative and ratio tests are new implementations. Read A016's stage-2 REPORT.md, especially exact tensor-spectator overcharge and the narrow factor-removal repair; these remain safeguards, not new claims here. The old A020 stage-1 verifier is reused only for lower a=3 domains and its source hash is pinned. Source paths and SHA256 receipts are in out/source_receipts.json. No remote or shared-tree write was made.

## complete derivation or exact first unsupported line

### 1. Exact Boolean counterexample to the proposed 81/100 cap

Let f on five bits have negative-output truth mask 474167, assignments ordered little-endian, and choose coordinate i=0. Equivalently its two four-bit branches have negative-output masks 871 and 357. They differ exactly at data vertices 1 and 9, adjacent in data coordinate 3; D=-1 at those two vertices and zero elsewhere. Thus d=2/16=1/8 and

    I(D) = 3/16,
    2I(D) = d log2(1/d) = 3/8.

The support-isoperimetric step in the lead's node bound is equality on this witness, so its excess ratio is not an artifact of a loose support-boundary estimate.

Direct character sums give the parent Fourier-mass histogram: eight atoms of mass 1/16, fourteen of mass 1/64, two of mass 9/64, and eight zeros. Each child has ten masses 1/64 and six masses 9/64. Hence

    H(f) = 5 - (9/16)log2 3,
    H(g) = H(h) = 6 - (27/16)log2 3,
    Delta_0 = (9/8)log2 3 - 1.

In natural units the denominator is (3/8)(1+ln2), and therefore

    R = Delta_0 / [(3/ln2)/8 + 3/8]
      = (9ln3-8ln2)/(3(1+ln2))
      = 0.8548839705904677... > 17/20 > 81/100.

The strict sign R>17/20 is certified by the rational logarithm intervals in direct_certificates.json (equivalently 180ln3-211ln2>51). The finite Walsh arrays and the physical derivative energy are reconstructed with direct O(N^2) character sums and exact Fraction arithmetic, without the batched census kernel. This is a second implementation by A020, not independent-agent acceptance.

The weaker pilot witness mask 775 at coordinate 1 has d=3/16, I(D)=1/4, and ratio 0.8180317633..., independently certified greater than 81/100. The full five-bit scan has 349 certified failing coordinate pairs among retained symmetry representatives; these are not an orbit classification or a count of all labeled failures. No interval comparison against 81/100 remains unresolved. Candidate storage is deliberately capped at 256 records; the integer count includes every failure.

Scope guard: exact erasure at the stronger witness is

    B_0 = (5/8)log2 5 - 1,
    B_0/d = 5log2 5 - 8 = 3.60964047... <4.

Indeed its eight nontrivial selector fibers have masses 4/64 and 1/64, giving (5/8)h2(1/5). The inequality B_0<4d follows from 5^5<2^12. Thus this node is GOOD for the lead's exact-B threshold K=4. The witness refutes an unlocalized 0.81 discount, not the K=4 bad-node-filtered stopping-tree proposal, FEI, or the original node-boundary theorem.

### 2. Exact full-domain coverage without forbidden block mixing

Write a five-bit truth table as a uint32 mask. Output complement changes no squared Fourier spectrum, physical influence, derivative energy or restriction entropy. Select the output sign with at most 16 negative entries. For every nonconstant function, translate a negative input to the origin; its mask is then odd. All 2^31 odd masks are scanned. Exactly 2^30 of them have at most 16 negative entries. The two constants are handled analytically: selector entropy increment is zero; no singleton has d>=1/8.

Within selector coordinates {0,1,2} and data coordinates {3,4}, reorder physical influences increasingly. These permutations preserve the a=3 block and its entropy increment. Do not permute a selector with a data coordinate. Input translations preserve the sorted influences. Among all odd translates, keep the numerically smallest mask. Every nonconstant orbit therefore has a retained representative. Testing all five coordinates at each representative also covers every physical singleton split, because the allowed symmetries only relabel coordinates or swap children and preserve the tested quantities. Ties in influence ordering may leave duplicates; uniqueness is neither used nor claimed.

Full run counts: 2,147,483,648 raw masks; 1,073,741,824 with minority size at most 16; 236,906,367 satisfying the within-block influence ordering; 16,973,810 translation-minimal survivors. On these survivors, 84,854,838 singleton nodes have d>=1/8. The ordered survivor stream SHA256 is fc177ad24a7e446c4885143142ef82ed032d7245f0b54fc49e2783709fdd85f0.

The certified inequalities are, on every actual five-bit singleton with d>=1/8,

    Delta_i < (9/10)[(3/ln2)d+2I(D_i)],

and on every a=3,m<=2 multiplexer with positive s=I_sel,

    Delta < (9/10)[min(3,(2/ln2)s)+3h2(s/3)].

If s=0, all branches agree and Delta=0 exactly. For m=0,1 the saved lower-domain verification separately enumerates all 256 and 65,536 tables. The m=2 certificate is not inferred from numerical extrapolation or arbitrary NPN classes. The finite 9/10 statements do not imply their universal analogues: the already established bent-splice ratio tends to one when d tends to zero.

### 3. Integer spectrum and interval-sign certification

For n=5 the FWHT returns even integer numerators W_S; write c_S=W_S/2, so p_S=c_S^2/256. The entropy numerator is sum_S G(|c_S|), where G(k)=-k^2 ln(k^2/256). G is enclosed on an integer grid of scale 2^40. Every exact physical selector edge count is compared with spectral influence, and every parent has sum c_S^2=256.

For a singleton i, the two child Fourier numerators are c_T+c_(T+i) and c_T-c_(T+i), each normalized by 16. Thus the census's signed child calculation retains interference before squaring. Define dnum=sum_(S contains i)c_S^2 and enum=sum_(S contains i)(|S|-1)c_S^2; d=dnum/256 and I(D)=enum/256. The comparison in natural units is

    Delta_nat <= 3d+2ln2 I(D).

All numerator differences use outward endpoints. The 81/100 question is decided by integer cross multiplication: certified lower Delta > (81/100) upper denominator records a failure; upper Delta < (81/100) lower denominator records a pass; anything else is counted as unresolved. The final unresolved count is zero. The 9/10 cap is checked against every positive denominator using integer cross multiplication, with zero failures.

For the selector block, data branches are formed explicitly from truth-table bits at x+8y. The eight two-bit child entropy numerators use a precomputed exact 16-table bank. For every possible snum in 0..768, a rational outward envelope is prepared for 256*[min(3ln2,2s)+3h_nat(s/3)]. The extra factor eight avoids rounding the average branch entropy. Both 9/10 and the original bound are tested on every survivor.

Logarithms use range reduction to t in [1,2) and

    ln t = 2 sum_(j=0)^39 z^(2j+1)/(2j+1) + remainder,
    z=(t-1)/(t+1),
    0<=remainder<=2z^81/[81(1-z^2)].

All series and tails are exact Fractions before outward fixed-grid rounding. Direct witness certification uses 60 terms and unrounded Fraction endpoints. The lower m=0,1 continuation reuses the prior 2^100 outward checker; its stronger precision and source hash are recorded. No floating-point value establishes a sign or the uniform 9/10 cap. Floating ratios only select discovered best witnesses, so exact symbolic maximizer classification is not claimed.

Overflow check: each nonnegative entropy contribution is at most 256/e, so a deliberately loose entropy-numerator sum bound is 8192*2^40. Parent-minus-child numerators multiplied by eight and then by 100 have absolute value below 2^63. The largest singleton denominator numerator is bounded using dnum<=256 and enum<=1024; its integer cross products are also below 2^63. The exact log-bank entries and array dtypes are int64. The actual sign checks therefore cannot wrap in the prescribed five-bit domain.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json was saved before the pilot. It fixes all five-bit masks, within-block symmetries, batch size 32768, exact arithmetic, runtime cap 1200 seconds, and memory estimate 120 MB with a 250 MB ceiling. Pilot: 524,288 raw masks, 101,649 survivors, 506,862 tested nodes, 31 certified failures of 81/100, no unresolved comparisons; measured Python runtime 0.434407 seconds. The full scan completed in 107.643661 seconds. Low-domain check completed separately; its measured duration is in lower_domains.json. Commands:

    python -X utf8 runs/20261012T044635Z-account05-A020-selector-boundary-tests/code/census.py --pilot
    python -X utf8 runs/20261012T044635Z-account05-A020-selector-boundary-tests/code/census.py
    python -X utf8 runs/20261012T044635Z-account05-A020-selector-boundary-tests/code/direct.py
    python -X utf8 runs/20261012T044635Z-account05-A020-selector-boundary-tests/code/lower.py

Exact discovery signs were saved immediately in first_falsifiers.json and PILOT_FINDING.md; the full job wrote checkpoint.json every fifteen seconds and census.json on completion. Independent direct witness reconstruction is in direct_certificates.json. The largest discovered selector ratio is about 0.763006 at mask 855 (exact interval saved in census.json); this floating display is evidence and is not an exact maximum claim. The uniform rational 9/10 certificate is separate.

No job was expected to exceed 300 MB; memok's trigger did not apply. Only one heavy job ran at a time. Small direct witness checks ran alongside the census; the lower-domain job ran after the full census finished. No GPU, window, background service, dimension escalation, git, brain write, external message or shared-tree mutation was used.

## proof dependencies and changed downstream conclusions

The counterexample and the finite caps depend only on the saved exact scripts, the above enumeration and logarithm-tail arguments, and basic uniform Fourier identities. No pending agent theorem is needed to verify them. The objects being tested are B04-SEL-LOG-SHARP@1 and B04-NODE-BOUNDARY@1, independently reconstructed by A018; their source-bound versions are retained as test provenance rather than assumed to prove the finite signs.

The 81/100 moderate-influence conjecture from B04 notes is false. Neither original lead theorem changes. A018's four-bit 81/100 certificate remains valid at its stated finite scope; a dimension-free extrapolation would fail. B04/A019/A027 must not build a stopping-tree discount on that extrapolation. The exact-B K=4 filter excludes our strongest witness, so its survival is explicit. The finite 9/10 cap closes only the assigned five-bit validation and is not a nonreusing payment lemma. Independent-agent review and supervisor adoption are pending.

## one next mathematical action and independent reviewer

Next: consume a source-complete spectator-free two-level shared-coordinate ledger from A018/A019, and test its proposed discount ONLY on nodes satisfying exact B_v>4 Inf_v, retaining both terminal entropies and ownership of derivative influence. The strongest moderate witness here is not such a node. Reviewers: A091 primary; A090 alternate. Do not repeat a five-bit census or seek a six-bit census without a concrete new candidate to falsify.

## actual persistence receipts or precise save blocker

The four protocol files, FROZEN_SPEC.json, code/, out/, direct certificates, and all rolling files are saved inside A020. out/persistence_receipt.json records exact schema fields, byte-identical deltas, report-field coverage, sizes, hashes and final read-back. No supervisor copy, remote mirror, claim adoption or independent-agent acceptance is asserted.

## Universal bridge

This stage moves the B04 falsifier interface feeding C019 stopping-tree payment by refuting the proposed 0.81 local discount at d=1/8, locating its failure at an isoperimetrically exact edge mismatch, and certifying the lead's full selector envelope on all a=3,m<=2 multiplexers with finite factor 9/10. It pays none of the universal adaptive bad-node boundary sum. The remaining obligation is a tensor-aware shared-coordinate stopping tree with a single-use influence reserve and terminal entropy intact. Testing a concrete ledger only at exact K=4 bad nodes is the shortest route to full FEI because it addresses the unowned C019 charge that survives this witness; another finite-dimensional constant would not address that debt.
