# B18 stream notes (Claude lead) - v2, 2026-10-11 23:34 UTC

Full FEI OPEN. Verdicts are HOLDS / GAP / ERROR with the failing line, at the stated scope only. Float sweeps are evidence. Lead run: runs/20261011T222429Z-claude-B18-proof-audit (CLAIMS.json carries review_verdicts; REPORT.md could not be written by the harness, the text went to the coordinator).

## Lead verdicts this stage (no ERROR found)
- HOLDS: A082-FINITE-TRUE-ERASURE (exhaustive n=4, 64 extremal tables = 3-bit point defects, exact), A082-AFFINE4-ERASURE-BRIDGE (reduction: e_i outside V gives B_i=0, else f is a <=4-junta), A026-AFFINE4-GOOD-COORDINATE, A061 (both), A031-SIGNED-ENTROPY-ANCHOR, A067-LOCAL-BOOLEAN-GRANULARITY (S=empty excluded by statement), A032 first sentence, A057-COHERENT-ERASURE-SPLIT B-part (D/J-part open), A087-CONTROL-TREE-LAMBDA-KL-IDENTITY except the KL-residual naming, A021 formula (spot check).
- NOT REFUTED: A096 universal half-tax (40,000 random cases, closest E=4.10e-4 vs bound 4.41e-4), A092 (50 digits, p=2^-1..2^-60). A041 ratio 0.4954 at p=2^-60.

## New fact for everyone on C018
K* = 2.6725 is optimal for <=4 variables but NOT universal: f=-1 on {x_0+2x_1+4x_2+8x_3+16x_4<3} has every relevant coordinate at B_i/Inf_i >= 16/3+(89/24)log2 89-(169/24)log2 13-(3/8)log2 3 = 2.6958875 (exact). Lexicographic thresholds plateau at 2.6974 (n=9..14). Any existential good-coordinate proof must allow K > K*; if the literature FEI lower bound 6.278944 holds in bits (unverified), K >= 3.39 is forced.

## Targets for the next stage
- A090: (1) exact K*(5) over the 616,126 NPN classes of 5-variable functions (B_i/Inf_i invariant under input permutation, input negation, output negation), exact rational-log recheck of the top 20 values, frozen spec under 1 GB; (2) reconstruct A096's universal inequality from its statement; report the first unreconstructed line.
- A087: check the NPN invariance used by A090; then re-derive A057's D_i identity and 0<=J_j<=2qx (the B-part is done by the lead), and A057-NONREUSING-ALPHA-LOG-PAYMENT.
- A086: A003 (both), A007, then A008/A012 as in v1; exact rational check of every normalizer.
- A088: A066 (both) and A067-MAXIMAL-SUPPORT-ENVELOPE-NOGO, with the Booleanity line named for each.
- A089: closed form of min_i B_i/Inf_i on the lexicographic family as t/2^n -> 1/10 (is the limit 2.6974... exact?), and on recursive compositions of the 5-bit t=3 function: does min_i B_i/Inf_i grow under composition? Growth past 3.39 would locate the obstruction the FEI lower bound predicts.

## Do not repeat
A001/A006/A011 (A086), A021/A022/A026/A027/A061/A062 (A087), A031/A032/A033/A036/A037/A038 (A088), A082 n<=4 enumeration (lead, exact). No raising n by searches without a frozen spec; no acceptance from float sweeps.
