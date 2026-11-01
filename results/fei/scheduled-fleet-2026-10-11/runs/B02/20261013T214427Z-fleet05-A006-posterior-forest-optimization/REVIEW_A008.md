# Independent review: A008 unequal read-once forest payment v1

Verdict: HOLDS AT ORIGINAL STATED SCOPE; no substantive repair. The reviewed whole claim is B02-A008-UNEQUAL-READONCE-DNF-FOREST-PAYMENT@1, original statement hash d20b46b85cf1295d2501ffa585e32d5880bf50cf69b11c5b7d556649b60d62d7. Its all-width residual, actual finite-run cost and empty/nonempty split are all reconstructed below. This is local independent acceptance; no shared registry or author artifact is edited. The author's earlier A006 review is not a premise, and this review does not adopt every other claim mentioned in their report.

Sources read: the complete A008 REPORT.md, READ_ONCE_DNF.tex and CLAIMS.json in runs/20261012T005959Z-fleet05-A008-gate-label-compression, together with the baseline original forests.tex generator and normalizer proof. I did not execute or import A008's code. The source byte hashes are in out/SOURCES.json. Independent exact checks in code/check.py use physical truth tables and integer FWHT on the 29 width partitions of n=1,...,6; rational physical edge influences, conditional root odds and reciprocal rank identities are checked separately from the claimed formulas.

## Reconstruction of the complete chain

Literal signs can be changed by physical input flips. For disjoint positive clauses of widths w_l, put p_l=2^-w_l, q_l=1-p_l, Q0=product q_l. Direct expansion f=1-2product(1-b_l), with b_l the clause indicator, gives for every nonempty A

    P(A)=4 product_(A hits block l) p_l^2 product_(A misses block l) q_l^2.

Summing local subsets, using (2^w_l-1)p_l^2=p_l q_l and q_l^2+p_l q_l=q_l, gives hit mass mu_l=4p_l Q0 and Var f=4Q0(1-Q0). Conditional on a coordinate being selected, all other coordinates in its block are independent fair selections; this remains true after summing other blocks. A physical coordinate is pivotal with probability 2p_l Q0/q_l, so I_l=2Q0 w_l p_l/q_l, also the spectral mean local size. These identities hold for every finite positive width tuple, not just the checker domain.

If an implicant contains no full clause, choose one unfixed literal in every disjoint block and set it false. The resulting false completion proves that the clauses are exactly the prime implicants. Unique ownership makes every used gate an isolated source SCC. The fixed initial-root order gives one root set and one once-per-block zero-child partition event, with no root permutations or child entropy. Generic successful runs with repeated self-visits are not partition forests and are not used to assert uniqueness. A touched block's selected subset is forced by A, so s=kappa, M=1, lambda=1.

For D=product(1+p_l)-1, the actual root experiment conditional on being nonempty has root-set mass product_used p_l / D, including every absent-root factor. Thus the full residual is

    R=v log2 D + sum_l mu_l w_l + gamma E sum_(j in A) log2[r(j)/(1+selected predecessors)].

Rarity is <=2I because q_l<=1. Let S=sum p_l and T=sum w_l p_l/q_l. For integer w>=1, w/q>=2: equality at w=1, and w>=2 otherwise. Hence T>=2S. Since log2 D<=log2 product(1+p_l)<=S log2 e and v=4Q0(1-Q0), the signed normalizer term is <=log2(e) I; a negative log2 D is valid in the same inequality.

For selected rank r, X~Bin(r-1,1/2) and the exact reciprocal identity is E[r/(1+X)]=2(1-2^-r)<=2. Concavity of log2 gives expected rank cost <=1 per selected coordinate, hence the rank bill <=gamma I. This reconstructs R<=(16/5+log2 e)I<47I/10; ln2>2/3 follows from the positive atanh series, so log2 e<3/2.

The actual finite queue event additionally pays every subset size, symmetric normalizer, subset weight and zero-child probability. With the original theta_s and Z_s=e_s(theta_s), its probability is

    q_pf(A)=D^-1 product_used [(p_l/2)/(s_l(s_l+1))*product_(j in A_l)theta_s(j)/Z_s].

The zero-child attachment multiset is empty and has probability one. These are disjoint terminating events of the same globally fixed generator; sum q_pf<=1. Roots cost <=(2+log2 e)I, zero-child choices <=I because every used block owns a selected coordinate, sizes <=log2(3)I since s(s+1)<=3^s, and subset normalizers <=log2(6e)I by the source's integral tail and elementary symmetric bound. Finally -log2 theta_s(j)=gamma log2^+(r/s) is <=gamma log2[r/(1+selected predecessors)] because the denominator is <=s. The same conditional-binomial payment covers the actual subset weights.

Therefore the complete nonempty spectral cross-entropy is <=[26/5+2log2(3)+2log2(e)]I. The source estimate h2(v)<=2I, together with Gibbs for the reference having masses 1-v and v*q_pf(A), proves the entropy-reference bound <67I/5. The constant comparisons are exact: 3^5<2^8 and ln2>2/3. The proof includes root names, rarity and all original probability factors; it imports no optional prefix rounding or selector for free. The fixed table/lambda/orders are chosen from f once, not sampled A.

## Checks and boundary

out/A008_REVIEW_CHECK.json records all 29 independently constructed physical functions and exact v/I/D values; the complete stage checker records 50,295 assertions including the forest calculation and seven separate sunflower sharpness cases. These finite checks validate identities; the analytic reconstruction above supplies the all-width quantifier and cost inequalities. No first unsupported line remains within A008's reviewed statement. The universal line is still influence payment for overlapping ownership, with no uniform local predecessor law available from Booleanity alone. FEI and universal PI-J remain OPEN.
