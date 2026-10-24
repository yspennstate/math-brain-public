# Old conversion, Boolean refinement, and separating controls

Let q_S=hat f(S)^2, W_k=sum_|S|=k q_S, v=1-q_empty. All logarithms are in bits. The old general level estimate is H(q)<=H(W)+sum_k W_k log2 binom(n,k); the marginal estimate is H(q)<=sum_i h2(I_i). These are estimates for probability laws, not Boolean-specific results.

The refinement is H(f)<=2I+2U-(2-log2(e))v, where U=sum_nonempty q_S(max_{T containing S, q_T>0}|T|-|S|). Its quantization proof is in DERIVATION.md, Sections 1-2. A fixed condition U<=KI, or the sufficient support condition d_f(S)<=L|S|, makes the entropy conversion dimension independent. These hypotheses are exactly measurable; they are not asserted for every source or inherited by its restrictions.

| Family | Old estimate | Local Boolean estimate or obstruction |
| --- | --- | --- |
| Point defect, n variables | Marginal bound / I = n-1+log2(e)+O(2^-n); level-count bound is tight | U/I=1-2^(1-n); H<=4I-(2-log2(e))v; actual H/I->4 |
| Existing addressing baseline, a address variables and 2^a data variables | Generic full-cube level-count bound Theta(a^2), while I=1+a/2 | Every support has d_f(S)=a+1, U=a/2; the refined bound gives exactly H<=2a |
| Boolean Fourier support inclusion antichain | Level counting can carry dimension logarithms | U=0 and H<=2I-2; no novelty claim for this class corollary |
| Real sum n^(-1/2)sum x_i | H=log2 n, I=1 | U=0 but Boolean bound false; verifies use of vertex quantization |
| Normalized real epsilon perturbation of 1 | H/I=h2(epsilon)/epsilon+log2 n; L2 distance to 1 can be small | Refutes an L2-only near-Boolean relaxation, not a bounded approximation theorem |
| One-point dictator flip | Actual H/I->0 | U/I~n; refutes universal payment of raw support excess |
| Majority3 tensor point defect | Actual H=2+o(1), I->3/2 | Every single-character arithmetic envelope >=3n/2; refutes optimized single-anchor payment |

The fixed-order Renyi point-defect obstruction remains intact. The bound concerns Shannon entropy and uses coefficient-specific Boolean quantization; it does not take a fixed Renyi order below one. The empty atom is explicitly paid, and no arbitrary tensor factor is discarded.

Primary locators: the current recovered threshold paper Section 5.1, Lemma 5.3, Eq. (29), and its earlier counterpart; [Han v2](https://arxiv.org/html/2312.08271v2), Section 3, Eqs. (3.13)-(3.15) and Remark 3.2, locates a moment-to-influence rarity logarithm. We do not claim a new general norm inequality or rediscovery of the marginal bound. The elementary local-support refinement's priority is unverified.
