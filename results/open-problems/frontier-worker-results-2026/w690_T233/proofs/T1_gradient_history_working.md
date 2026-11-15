# Target 1: gradient history and Gaussian innovations — WORKING

No new convergence result is claimed here. C009 is separately submitted for
its deterministic mixed-time Gram comparison. All routes below were F-checked.

## Exact history, not an arbitrary span

In original units, Delta W_i(t)=-sum_(s<t) eta_s alpha
C_i(s)^T E_s A_i(s)^T, with A_i=W_(i-1)...W_1 X and C_i=W_L...W_(i+1).
In normalized units this is C009 (9.3). Per-layer column/row query-history
ranks are at most d_y times the number of times and r times that number.
The residuals and positive step sizes are coupled across ALL layers.

An arbitrary matrix with column/row spaces in a large union of history
spans is a much weaker restriction than this update identity. Nearly
dependent query histories also make unweighted span bounds misleading.
C008's structured constant-loss paths fail the update identity already
at their initial tangent: initial hidden gradients are -k^2 E_21.

## A standard noncentral inverse-Wishart inequality, re-derived

Let G be d by q iid N(0,1), M fixed, d>q+1. Then
    E[((G+M)^T(G+M))^-1] <= I/(d-q-1)                 (W.1)
in Loewner order, with no bound on M.

For any unit v in R^q rotate the columns to put v first. Conditional
on the other q-1 columns, the Schur-complement reciprocal for the first
diagonal entry is 1/Z, where Z has a noncentral chi-square law with
d-q+1 degrees of freedom. Independence of the Gaussian columns is used
AFTER the fixed column rotation. For lambda>=0 and a=d-q+1>2,
    E[1/Z]=integral_0^infinity
      (1+2t)^(-a/2) exp(-lambda*t/(1+2t)) dt
      <=1/(a-2).
Trace integrability follows from the diagonal bounds, and the same
argument for every v gives (W.1). No assertion that the noncentral
inverse mean is a scalar matrix is made.

More generally let Pi be an orthogonal projection of rank d in R^m,
let G be m by q iid N(0,1), and Y=M+Pi G Q^(1/2)/sqrt(m),
with Q positive definite. Projecting Y onto range(Pi) drops a PSD
term from Y^T Y; inverse order and (W.1) give
    E[(Y^T Y)^-1] <= m/(d-q-1) Q^-1.                (W.2)
This remains true conditionally if M,Pi,Q are measurable BEFORE
the fresh independent G is exposed.

For a depth-adapted recursion with Q_k=Y_k^T Y_k and d_k>=m-s,
rho=m/(m-s-q-1), the process rho^(-k)tr(Q_k^-1) is a nonnegative
supermartingale. Ville yields simultaneous Gram lower bounds
zeta/[tr(Q_0^-1)rho^n] through n layers with failure <=zeta.
For fixed s,q and m=cL, rho^L is bounded by a c-dependent constant.

## Essential application gap

Do NOT substitute raw trained prefixes into (W.2). Their input is
adaptive to the same initial Gaussian matrix. Under deferred linear
queries, the remaining Gaussian acts only on the input component
orthogonal to previously queried rows, and only outside already queried
left directions. An old query has no such fresh innovation. Ignoring
this would be a false proof.

For one Gaussian matrix with observed W V and W^T U, the familiar
orthogonal decomposition is
    W = W P_V + P_U W - P_U W P_V
        +(I-P_U) Z (I-P_V),
where the last block is fresh Gaussian conditional on a predictable
sequence of linear queries. A simultaneous-network argument must prove
the required predictability by ordering the forward/backward oracle
queries and using the known low-rank update history. It must also
control query-Gram degeneracies. Merely declaring the final random
subspaces fixed is insufficient.

C009 improves the deterministic drift part: stitched outputs imply
cross-time suffix/prefix inner products O(m^-1/2), and exact gradient
form converts this to a local Gram correction O(A_t/m). What remains
is a lower bound for the adaptive base image B_i(0)F_(i-1)(t), with
valid innovation conditioning, and a no-exit estimate. No claim is
filed for applying (W.2) to GD.
