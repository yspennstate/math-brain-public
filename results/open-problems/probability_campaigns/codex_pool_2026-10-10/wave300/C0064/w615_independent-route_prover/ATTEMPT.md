# C0064 independent route — w615

Route registered on 2026-10-10 before reading any peer's proposed proof.

Target: independent nearest-neighbour bond percolation on Z^d, for each integer d>6. Set tau_p(x)=P_p(0<->x), chi(p)=sum_x tau_p(x), and Dhat(k)=d^{-1} sum_i cos(k_i). Seek finite dimension-dependent constants A1,A2 with tauhat_p(k)<=A1/[chi(p)^{-1}+p(1-Dhat(k))] and tauhat_p(k)<=A2/(1-Dhat(k)), uniformly up to pc, with the critical Fourier transform given an explicit interpretation. The missing dimensions in the dated intake are 7,8,9,10. Fitzner–van der Hofstad, Theorem 1.1, is the recovered primary template; it proves this for d>=11.

Independent method: view tau as the covariance of independently signed percolation clusters, prove a uniform strictly positive spectral floor in the finite-susceptibility regime, then study the Fourier inverse A_p of 1/tauhat_p. Derive a sufficient coercivity condition from the nearest-neighbour part of the signed direct kernel J_p(x)=-A_p(x) (x!=0) and a weighted bound on its negative tail. This uses cluster covariance and inverse convolution, not a re-evaluation of the non-backtracking lace coefficients or a dimension-7 numerical bootstrap. No peer proof has been read. Prior-route digest follows after targeted source recovery.

Single hardest gap at registration: a positive, p-uniform lower bound for 2d*J_p(e1)-sum_{x!=0, |x|_1!=1} J_p(x)^- |x|_1^2, near pc in dimensions 7..10. A finite-volume fit, positivity of tauhat, or a source hash does not prove this gap.

Saved result L0: the elementary path-counting susceptibility estimate is in CLAIMS.jsonl. It applies only below 1/(2d-1), and makes no critical-regime claim.

NEXT: Prove the signed-cluster spectral floor and inverse-kernel criterion; identify which hypotheses can actually be verified.
