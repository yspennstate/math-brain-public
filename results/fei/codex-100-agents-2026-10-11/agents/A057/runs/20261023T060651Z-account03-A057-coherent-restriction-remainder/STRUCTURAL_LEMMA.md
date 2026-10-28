# A physical pair criterion, beyond quadratic gates

The actual sufficient condition used by PAIR_PROOF.md is the following, stated without Fourier-flatness or degree assumptions. Fix a partition of the exterior coordinates into physical pairs. Suppose b is Boolean and:

(a) on EVERY two-bit slice of each pair, after fixing ALL outside exterior bits arbitrarily, the product of its four signs is -1;
(b) b(0)=b(e_i)=+1 for every exterior unit vector e_i.

On a slice in(a), there are an odd number of negative signs, so each coordinate has exactly one disagreeing edge out of its two edges. Thus each untouched pair coordinate has actual influence1/2 after ANY restriction outside that pair. Mixtures over unqueried outside bits preserve1/2. This is a statement about physical derivatives, not a supplied spectral surrogate.

With the point mask C at0, on a surviving-mask history all past exterior values are0. The exceptional edge altered by the point edit has its endpoints among the original0,e_i, where(b) says both b values are+1. The edit therefore adds t(1-Eg) disagreements and cannot cancel an old one. Consequently the untouched-pair influence floor1 holds at EVERY actual history of the splice. The original-owner conversion4I_pair ->2 per open child ->0 is therefore paid by the identical proof, including arbitrary internal interleaving, full terminals, current logarithmic variance reserve, and all old debits. This structural criterion is the exact hypothesis of the new self-contained exterior theorem. The quadratic perfect-matching family is one application.

There are also arbitrary-degree examples. On k pairs (x_j,y_j), let

    b(x,y)=(-1)^(sum_j x_j y_j + P(x)),

where P is ANY Boolean phase on the k first coordinates with P(0)=P(e_j)=0. Each matching pair slice has product -1: the term x_j y_j contributes odd slice parity, while every other phase term depends on at most one coordinate in that pair. Condition(b) also holds. The mean is EXACTLY2^-k: sum over y kills every x except x=0, where P(0)=0. For k>=2 this lies in[c,1/4] with c=2^-2k, so the original source6 condition holds throughout internal histories. This produces the FULL mixed source/internal/exterior stopped inequality at fixed rates6,21,5,4, conditional only on the explicitly imported internal local estimates, for arbitrary P of arbitrarily high degree satisfying the stated origin values.

No FEI reduction for arbitrary b is hidden here. For a general Boolean gate, condition(a) may fail on many conditional slices; without an influence-paid replacement for this physical lower bound, the first-query conversion need not have four incoming bits. The remaining universal step is a representation or block-selection/payment lemma funding such failed slices from original unused physical influence, with no assumed initial entropy price. This is the bridge sought next, rather than enumerating more gates satisfying(a).
