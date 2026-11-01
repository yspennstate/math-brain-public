# Independent B06 reconstructions by A028

These verdicts apply only to the pinned v1 original statements. A028 supplies no repair to the accepted versions, so the reconstruction is independent rather than a contribution to a repaired claim. No source or registry was changed.

## A026-AFFINE4-GOOD-COORDINATE v1: ACCEPT_AT_STATED_SCOPE

Original: A026/runs/20261011T214052Z-fleet05-A026-good-coordinate-erasure/GOOD_COORDINATE_TARGET.tex. Reconstructed with a separately written complete scalar integer Walsh census, not the original butterfly/Gray programs. The normalization cancels: A_i/I_i=2 sum|W_T W_(T+i)| / sum W_(T+i)^2. Exhaust all 32906 truth tables modulo global sign. Exact maximum minimum ratios are 0,2,3,7/2. Relevant coordinates have strictly positive denominators; constants require no division.

The scalar inequality h2(t)<=2sqrt(t(1-t)) in the original is valid: its derivative after t->sqrt((1-p)/p) has one interior turning point and one additional zero, giving a nonnegative difference with zero endpoints. Thus B_i<=A_i. If e_i is not in V, affine support c+V has no adjacent pair in direction i; both erasure and actual physical mixing are zero. Otherwise all relevant e_i belong to V and their linear independence bounds the number of relevant coordinates by dim V<=4. Deleting irrelevant coordinates changes neither the census ratio nor entropy. A physical restriction projects the affine support and never increases its affine dimension, even when coefficients cancel. These facts prove the same selection at every descendant. Exact physical influence and entropy induction then gives 7/2+2/ln2. Disjoint products preserve the factor quantities and hypothesis. No arbitrary linear spectral change is mistaken for a physical query.

## A026-AMPLITUDE-K4-THRESHOLD-NOGO v1: ACCEPT_AT_STATED_SCOPE

For the symmetric n=32,t=24 sign, independently compute the integer coefficient at a fixed k-set as sum_j f(j) sum_l (-1)^l binom(k,l) binom(32-k,j-l). Multiply adjacent products and squares by binom(31,j) before summing. The exact ratio is 2220940451/536870912>4. Symmetry makes it the same at every coordinate. This is an amplitude-proxy obstruction, not true erasure failure or FEI disproof. No 2^32 truth table is enumerated.

## A027-DATA-FIRST-PROPER-BLOCK v1: ACCEPT_AT_STATED_SCOPE

Original: A027/runs/20261011T215911Z-fleet05-A027-block-selection/ADAPTIVE_BLOCK_SELECTION.tex. Reconstruct the parent spectrum directly, group by control Fourier set, and subtract fiber mass entropy from raw entropy. For every nonempty control set, mass is p^2[(1-mu)^2+1-mu^2]=2p^2d. The empty-control fiber mass is R0=1-2pd+2p^2d, with nonempty-core mass p^2v. Its entropy is R0 h2(p^2v/R0)+p^2v L. The first term is bounded by p^2[2r+(1+1/e)/ln2]<2p using rp<=1/2 and (1+1/e)/ln2<2. Combined with v<=2d, the total is <=p(2dm+2)<=6pm for m>=1. Thus the original dimension payment is valid for BOTH signs of the core mean.

Physical core influence is pI(u); point-defect leaf influence is rpd. A point-defect r=1 leaf has zero entropy; for r>=2 its empty coefficient entropy is <=4p/ln2<8p and its nonempty entropy is 8p(1-p)(r-1), giving H<=8rp=4I. The recovered uniform block channel bound pays only queried core influence, while leaves use rpd. With I(u)>=eta*m, the exact original constant max(6/eta+2/ln2,4) follows. The condition is not claimed hereditary. The independent exact checker verifies the fiber identity on 1112 activated cores, including constants and both bias signs. No density-free extension is inferred.

## A027-CORE-BLOCK-HARDNESS v1: ACCEPT_AT_STATED_SCOPE

For delta=(1-Eu)/2, normalized nonempty defect law has core-empty mass delta and remaining mass 1-delta. Grouping the exact parent spectrum gives B_W/p=vL+4delta(1-p)h2(delta)+(R0/p)h2(p^2v/R0), including continuous zero-mass cases. Fixed-core p->0 removes the final term because it is O(p(r+1)), retaining H(u)-h2(v)+4delta h2(delta).

For Eu>=0, edge isoperimetry gives I>=2delta log2(1/delta). The elementary bound h2(v)<=2I in the original is correct: for delta<=1/4 use v<=4delta and increasing x log2(e/x) on [0,1]; for delta>=1/4 use I>=1. The original boundary induction reduces precisely to h2(t)>=2t for t<=1/2 and proves the input inequality. Thus a universal block K implies H<= (K+2)I, with output complementation removing the mean restriction. Conversely the final fiber term/p is <=3I via v<=I, v log2(1/v)<=2I, rp<=1/2; the middle term is <=4delta<=2I because I>=2delta. Also vL<=H. Hence FEI C implies B_W<= (C+5)pI. At delta=1 and p=1/2, R0=0 but v=0; continuous interpretation gives zero fiber cost. The nonnegative-mean quantitative equivalence has R0>=1/2, so no problematic division occurs.

## Scope and adoption

The finite census, threshold combinatorics and activation transport identities are exact certificates; the all-dimensional hereditary and limit steps are the analytic reconstructions above. These verdicts are local independent mathematical review, not external peer review or canonical adoption. SHA256 source pins and the new reviewer record are in the local artifact metadata. A087/A094 may audit this reconstruction, and B20 owns registry adoption. No full FEI claim is accepted.
