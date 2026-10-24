# Stage-2 derivation checkpoint

The lead's requested positive side can be proved for unequal read-once clause widths, in the ORIGINAL fixed conditioned queue. Let p_l=2^-w_l, q_l=1-p_l, Q0=product q_l, lambda_l=1 and M_l=1. Each nonempty set has a unique partition forest: one root per used disjoint block and zero children. Names are paid once per used gate; attachments and posterior entropy are zero.

The direct Boolean expansion gives mu_l=P(S meets block l)=4p_l Q0 and I_l=2Q0 w_l p_l/q_l. In each used block the selected subset is uniform on its nonempty subsets. D=product(1+p_l)-1, so the root block is v log2 D+sum_l mu_l w_l, exactly, with v=4Q0(1-Q0). Weighted activation gives v log2 D<=v Lambda<=log2(e) I; also sum mu_l w_l<=2I.

For a fixed order on a width-w block, rank sum=log(product selected ranks/|B|!). The initial factorial/concavity bound gives residual <13I/2. It sharpens as follows: conditional on a coordinate of rank r being selected, predecessors are Bin(r-1,1/2), so E[r/(1+Bin)]=2(1-2^-r)<=2. Concavity of log gives E F<=ln2, and the complete rank sum is <=I bits. Therefore the conditioned residual is <=[16/5+log2(e)]I <(47/10)I. This sharper binomial proof is the final claim.

For the ACTUAL once-per-block finite run probability, subset size costs log s(s+1), subset normalizer log Z_s, subset weights (6/5)sum_selected log^+(rank/s), and child count zero costs one bit. The size expectation is <=log2(3) I, normalizers <=log2(6e) I, subset weights <=(6/5)I, and zero-child costs <=I. Combined with the exact root block above, complete nonempty run cross-entropy <=[26/5+2log2(3)+2log2(e)]I; adding h2(v)<=2I gives the complete entropy-reference bound <(67/5)I.

This is a bound on the specified prime-implicant forest reference, not a new FEI-class claim. Need independent exact verification of these identities and the A006 review before proposing acceptance. Shared-variable gates invalidate the unique-owner premise; the universal PI-J label/rank payment is still open.
