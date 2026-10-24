from pathlib import Path
s=r'''

## 4. Pushing the local theorem to a growing number of rounds

The fixed-t proof admits a genuine uniform extension; this is stronger than the first local special case and still stops well before the critical bottleneck.

**Theorem B (slowly growing rounds).** Let d>=3 and 2<=r<=d be fixed. Let t=t_n>=0 satisfy

  (d-1)^{t_n}=o(log n),                                (C1)

and let deterministic vacancy densities q_n lie in a fixed compact interval [c,1-c], c>0. With h_t and sigma_t defined by the infinite-tree local statistics as above,

  P((H_t-n h_t(q_n))/sqrt(n sigma_t(q_n)^2)<=a | G_n)
       -> Phi(a) in probability over G_n.              (C2)

Independent replicas have independent standard Gaussian limits with this normalization. The graph variance of these conditional CDFs tends to zero. Furthermore

  Var_G(E(H_t|G))=n^{o(1)}=o(n).                        (C3)

Here n^{o(1)} means an upper bound, not an asserted asymptotic equality for a possibly zero variance. Complete occupation by t_n rounds has probability tending to zero, uniformly in q_n in the indicated compact interval. Thus in the critical setting the L1 discrepancy from final occupation still tends to 1/2, even at these growing depths.

Proof, with all uniformity checks. Condition (C1) implies t=O(log log n). The cycle counting proof in Section 1.1 can be made explicit for L=3t. For cycle lengths ell,j<=2L+1, their union is specified by identifications of ell+j cycle positions. There are at most (ell+j)^{ell+j} such identifications. Each consistent union has e>=v, e<=ell+j, at most n^v d^{2e} embeddings/half-edge choices, and specified-pair probability at most (2/(nd))^e for all large n, since e=O(L)=O(log log n). Its expected number is therefore at most (2d)^e. It follows that

  E(C_ell C_j) <= exp(O_d(L log(L+2))).

The O constant is uniform in ell,j,L in this range. Multiplying by S_L^2 and summing at most (2L+1)^2 weighted cycle pairs in (A1) preserves this form. Conditioning on simplicity divides by a probability bounded away from zero. Hence

  E B_{3t}^2 <= exp(O_d(t log(t+2)))=n^{o(1)}.           (C4)

For t=0 this is immediate separately. Equations (A3) and (C4) prove (C3). With probability tending to one B_{3t}<=n^{1/8}. Let D=S_{2t}; (C1) gives D=n^{o(1)} (indeed O((log n)^2)). The universal lower bound on sigma_t from (A6), obtained for every finite t and q in Section 1.2, is

  sigma_t(q_n)^2 >=q_n(1-q_n)q_n^{2(S_t-1)} >= exp(-O_c(S_t)).

Since S_t=O_d((d-1)^t)=o(log n), it follows that n sigma_t(q_n)^2>=n^{1-o(1)}. The same degree-one argument gives the unconditional-on-seeds lower bound Var(H_t|G)>=n^{1-o(1)} on every graph. Therefore (A3) and (A5), on the structural good set, imply respectively

  [E(H_t|G)-n h_t(q_n)]/sqrt(n sigma_t(q_n)^2)->0,
  Var(H_t|G)/[n sigma_t(q_n)^2]->1.                     (C5)

Indeed the numerators are bounded by n^{1/8} and 2D n^{1/8}, respectively, while the two denominators have orders at least n^{1/2-o(1)} and n^{1-o(1)}.

The moment proof in Section 1.3 is also uniform at these depths. For each fixed order m, counting spanning trees of the position components gives an upper bound C_m n^j D^m for tuples with j components; C_m depends only on m, not n,t or q. Odd normalized moments are bounded by

  C_m n^{(m-1)/2}D^m/[Var(H_t|G)]^{m/2}
       =n^{-1/2+o(1)}.

At order m=2j, the exceptional linked-pair and non-pair-component terms are at most C_m n^{j-1}D^m; divided by Var(H_t|G)^j they are n^{-1+o(1)}. Thus all conditional moments, normalized by their conditional variance, converge to the standard Gaussian moments uniformly on the structural good set. The same moment-determinacy and conditional sequence argument as before, followed by (C5), proves (C2). Conditional independence and bounded CDFs prove replica factorization and vanishing graph variance.

Finally, h_t(q_n)>=q_n^{S_t}>=n^{-o(1)} since the entire finite ball may be vacant. On the structural good set E(H_t|G)>=n^{1-o(1)}-n^{1/8}, while Var(H_t|G)<=nD=n^{1+o(1)} by bounded dependence. Chebyshev then gives P(H_t=0|G)<=n^{-1+o(1)} on this good set, and its complement has probability tending to zero by (C4). This proves the no-early-completion assertion. The same estimate works at graph-dependent critical q_G, since it is uniform for vacancy densities in a fixed compact interval and q_G lies in such an interval with probability tending to one. Final occupation is balanced at q_G, or annealed-balanced at p0_n, so the monotonicity identity E|F-F_t|=1/2-P(F_t=1) again proves the discrepancy limit. End proof.

Theorem B establishes an actual growing-round version of the replica concentration mechanism. It does not allow t of order n^(1/4), and it does not factorize final-success indicators. It sharpens, rather than closes, the remaining gap.
'''
p=Path('SECOND_ATTEMPT.md');p.write_text(p.read_text(encoding='utf8')+s,encoding='utf8')
