---
name: jgshg_lemma16_needs_square_g_depth4_full_rank_2026_11_16
description: "[VERIFIED] Jacot et al. 2021 Lemma 16 (L=3 nonzero critical points strict) fails when n0!=n3: (0,0,W3), G^T W3=0 has zero Hessian; a.s. L=3 still holds via two vanishing layers; T232 Thm 5.1 extended to every full-rank G"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T03:47:52+02:00
  status: verified
  evidence: "rect_depth4_check.py"
---

Jacot, Ged, Simsek, Hongler and Gabriel (arXiv 2106.15933), Lemma 16 claims that at depth L=3, for G of rank min{n0,n3}, every nonzero critical point of H(theta)=Tr(G^T W3 W2 W1) (an "escape direction with speed 0") has a direction of negative curvature. When n0 != n3 this does not hold.

Counterexample (smallest): n0=n1=n2=1, n3=2, G=(1,0)^T, theta=(0,0,W3) with W3=(0,1)^T. Then G^T W3=0. The gradient is zero, and every Hessian block is G^T W3, W2 or W1, all zero, so the Hessian is zero. Their proof breaks where it uses the top singular value of G^T W3 (theirs: W3 G), which is 0 here.

The almost-sure conclusion at L=3 still holds for every G of full rank. Proposition 3.1(b) of our T232 paper says a zero Hessian forces W2=0, G^T W3=0 and W1 G^T=0. If n0<=n3, G^T is onto, so W1=0; otherwise G^T is injective, so W3=0. Either way two layers vanish, and the conserved imbalances exclude that almost surely (|W_i|^2-|W_j|^2 is conserved, so it would be a nonzero polynomial equation in theta0).

The same algebra extends Theorem 5.1 of the T232 paper (depth four, hidden layers of a common width) from invertible G to every G of rank min{n0,n4}. By reversal (W_l -> W_{L+1-l}^T, G -> G^T, D_l -> -D_{L-l}) assume n4<=n0, so G^T is injective. Then W2!=0 forces W4=0 and W3 invertible, a contradiction; and W2=0 forces W3 invertible, hence W4=0. The leftover points have W2=W4=0 and are null.

Evidence: rect_depth4_check.py (n0=3, n4=1, w=1: leftover point has gradient 0, Hessian 4e-17, all D_l invertible). Paper: the T232 manuscript, Remark 3.2 and Theorem 5.1.

How to apply: when citing Lemma 16 of JGSHG, state it for n0=nL only. When a paper's lemma is stated for "rank min" matrices, test the non-square case with the smallest dimensions before relying on it.

