# Target 1 working lemma: endpoint Gram martingales

Initialization only; no target-1 convergence claim and no novelty claim.

Let B_i=W_i/sqrt(m) for all layers, including the last. Take a deterministic orthonormal d_x by r basis U for col(X). Set F_0=U, F_i=B_i ... B_1 U (1<=i<=L-1), Q_i=F_i^T F_i, Q_0=I_r. Independently of this notation, expose layers backwards and set S_0=I_(d_y), S_k=B_L ... B_(L-k+1), H_k=S_k S_k^T, 1<=k<=L-1.

For q=r or d_y assume m>q+1 and define rho_q=m/(m-q-1). For any 0<zeta<1, with failure probability <=2zeta the corresponding entire Gram chain obeys

    zeta/[q rho_q^(L-1)] I_q <= Gram_k <= q/zeta I_q

for all 0<=k<=L-1 simultaneously. The forward and backward bounds hold together with probability >=1-4zeta, without needing independence between those two events.

## Proof, including the inverse-Wishart identity

For a full-column-rank m by q preceding feature Z, write Z=V Q^(1/2), V^T V=I_q. Conditional on preceding layers, an independent Gaussian W gives G=WV with iid N(0,1) entries and

    Q_new=Q^(1/2) (G^T G/m) Q^(1/2).

The first rectangular layer satisfies this too. For suffixes use the transpose and expose independent layers in reverse order. All ranks are q almost surely.

Write T=G^T G. For its j-th column vector g_j the Schur complement says

    (T^-1)_(jj)=1/[g_j^T (I-P_(-j)) g_j],

where P_(-j) projects onto the other q-1 columns. Conditional on those columns, the denominator is chi-square with m-q+1 degrees of freedom. Integrating its density gives reciprocal expectation 1/(m-q-1). Column sign symmetry makes off-diagonal inverse expectations zero. They are integrable because |T^-1_ij|<=sqrt(T^-1_ii T^-1_jj) and Cauchy-Schwarz. Hence

    E[(G^T G/m)^-1]=rho_q I_q.

Thus tr(Q_k) and rho_q^(-k) tr(Q_k^-1) are nonnegative martingales, each with initial expectation q. Apply the nonnegative martingale maximal inequality at threshold q/zeta to each: stop at its first threshold crossing, use bounded stopping time and nonnegativity, then Markov. The two failure probabilities are <=zeta each. On their complement use lambda_max(Q)<=tr(Q), lambda_min(Q)>=1/tr(Q^-1) and rho_q^k<=rho_q^(L-1). The identity endpoint Gram is covered too.

If m>=2(q+1), log rho_q<=2(q+1)/m. For m=cL, rho_q^(L-1)<=exp(2(q+1)/c). Thus all bounds depend on c,q,zeta and not L. Integer rounding can be handled using m>=cL/2 eventually. Take zeta=delta/4 for probability 1-delta.

## Initial kernel consequence

Apply the Du-Hu orthogonal right singular-vector reduction to the data and discard the zero-input coordinates (the realizable residual there is zero). In the resulting notation X is d_x by r with rank r, and write X=UR. Here sigma_min(X) is the smallest NONZERO singular value of the original data matrix; all kernel minimum-eigenvalue claims are on this reduced r-column residual space, since the original n-column kernel has a nullspace when n>r. Define a_q=zeta/[q rho_q^(L-1)], b_q=q/zeta. With alpha=(m^(L-1)d_y)^(-1/2), the output kernel is exactly

    P(0)=(1/d_y) sum_(i=1)^L [(R^T Q_(i-1) R) tensor H_(L-i)].

For i=1 use Q_0=I_r and for i=L use H_0=I_(d_y). The normalized powers cancel because alpha^2 m^((i-1)+(L-i))=1/d_y. Therefore

    lambda_min(P(0)) >= (L/d_y) a_r a_(d_y) sigma_min(X)^2,
    lambda_max(P(0)) <= (L/d_y) b_r b_(d_y) ||X||^2.

At width cL these are L times positive c-dependent constants. In the realizable reduced problem ||grad_W loss||_F^2>=2 lambda_min(P(0)) loss.

## Unproved training step

The conditional Gaussian calculation uses an unexposed independent layer. At positive GD times each layer depends on all initial layers and the residual. These martingale identities cannot simply be applied to trained Grams. A smaller step reduces discrete remainders, but by itself does not reduce the integrated movement to reach a fixed loss reduction: the geometric residual sum contributes an inverse step size. Positive initial kernel does not prove a global kernel bound.

This note supplies an initialization component, not a frontier move. Next: inspect Du-Hu Claim 7.2 and quantify its accumulated perturbation budget at m=cL before claiming anything about the trajectory.

Sources: Du-Hu https://arxiv.org/pdf/1901.08572 (kernel and induction); HXP https://arxiv.org/pdf/2001.05992 Eq. (7) (same kernel). Projection identity, inverse chi-square mean, and maximal inequality are derived above.

Review identifier: C004 v1, kind bound, target1; independently submitted at reviewer request. Independently ACCEPTED by an agent; see AUDITS_FROM_REVIEWER.tsv.
