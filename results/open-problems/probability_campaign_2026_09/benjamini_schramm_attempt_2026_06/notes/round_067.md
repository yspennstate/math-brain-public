# Round 067 log

## Goal

Turn the graph-specific finite-state bridge obligation into a clean
path-decomposition template.

## Path-sum transfer certificate

Added Proposition `path-sum-transfer-certificate`.  For endpoints
\(\operatorname{dist}(x,y)=n\), a graph-specific computation may injectively
encode every nonbacktracking bridge trajectory \(\gamma\) from \(x\) to \(y\)
as
\[
  \sigma_0,f_1,\sigma_1,\ldots,f_n,\sigma_n,
\]
where each \(f_r\) is a phase fragment from state \(\sigma_{r-1}\) to
\(\sigma_r\).  If
\[
  s_q^k\mathbb P_x^{\mathrm{NB}}(\gamma)
  \le
  \mu_{x,y}(\sigma_0)\prod_{r=1}^n w_{r,x,y}(f_r)h_{x,y}(\sigma_n)
\]
for a trajectory of length \(n+k\), and if the phase sums define matrices
\[
  K_{r,x,y}(\sigma,\tau)=
  \sum_{f\in\mathcal F_{r,x,y}(\sigma,\tau)}w_{r,x,y}(f)
  \le M(\sigma,\tau),
\]
then summing over all encoded trajectories gives
\[
  B_n^{\mathrm{NB}}(q(D-1))\le a^TM^nb.
\]

## Cleanup

Normalized the nonhomogeneous block certificate to the standard forward
product order \(\mu^TK_1\cdots K_nh\).  The argument is unchanged, but the
notation now matches transfer-matrix computations.
