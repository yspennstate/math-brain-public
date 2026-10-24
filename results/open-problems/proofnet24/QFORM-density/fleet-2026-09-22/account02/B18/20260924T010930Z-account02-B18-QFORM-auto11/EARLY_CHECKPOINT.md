# account02/B18 — early checkpoint: zero-self-bank spectral funnel

Full QFORM remains OPEN.

Let the ORIGINAL coordinates split as `I disjoint J` and write

`A = [[0,B],[B^T,C]]`.

Let `s_3(A)` be the third largest singular value (equivalently the third largest absolute eigenvalue because `A` is symmetric), and let `beta_2(B)` be the second singular value of `B` (zero if `rank B<2`). Then

` s_3(A) <= ||C||_op + beta_2(B). `

Indeed, let `B_1` be a best rank-one approximation, so `||B-B_1||_op=beta_2(B)`. Put

`A_0=[[0,B_1],[B_1^T,C]] = diag(0,C)+R`, with `rank R<=2`.

A rank-two perturbation satisfies `s_3(A_0)<=s_1(diag(0,C))=||C||_op`, while singular values are 1-Lipschitz in operator norm and

`||A-A_0||_op = ||B-B_1||_op = beta_2(B)`.

Hence the claim.

Therefore if `s_3(A)>=s` and `||C||_op<=c<s`, then `beta_2(B)>=s-c`. The newest completed account03/B18 theorem `QFORM-ONE-SIDED-CROSS-NEGATIVE-MOMENT-v1` then gives, for arbitrary independent cap-one inputs,

`||p_{X^TAX}||_infinity <= 2 sqrt(pi) [beta_1(B) beta_2(B)]^(-1/2) <= 2 sqrt(pi)/(s-c).`

In particular, at the owner normalization `s=1`, every such branch with `||C||_op<=1/2` is paid by `4 sqrt(pi)=7.0898154036...`; the pure bipartite case `C=0` is paid by `2 sqrt(pi)=3.5449077018...`.

This is an exact original-coordinate result. It does not rotate the independent inputs, discard small curvature, or infer that such a zero-self bank is forced in an arbitrary target matrix.
