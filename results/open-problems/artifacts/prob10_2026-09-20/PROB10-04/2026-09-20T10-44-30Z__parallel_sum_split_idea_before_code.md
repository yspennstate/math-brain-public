Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 idea before code — eliminate covariance inverses by a matrix-splitting certificate

Status: **idea / source OPEN**. Source metric remains the published explicit bracket `[3.52,4.4898]`, width `0.9698`; this artifact does not claim endpoint movement.

The preceding run reduced the remaining Diaz outer copy-mass problem to

\[
\nabla^2\Phi(y)=D(y)^{-1}-\Sigma_V(y)^{-1}-\Sigma_C(y)^{-1},
\]

where `y=(u,v,w)`, `D=H_copy^{-1}` is the sign-stratified copy covariance, and `Sigma_V,Sigma_C` are the variable/clause Gibbs covariances. The obstacle is not the identity but making a global/interval certificate without repeatedly inverting interval matrices.

## Three materially different attacks for this run

1. **Scalar collinear split.** Use the parallel-sum variational formula with `z=t x`; this would certify concavity from one scalar `t` and the LMI
   `D >= t^2 Sigma_V + (1-t)^2 Sigma_C`. It is deliberately simple and may be too fragile.

2. **Full matrix split.** Use `z=T x` with a fixed `3x3` matrix. For SPD `A,B`,
   `P=(A^{-1}+B^{-1})^{-1}` satisfies
   \[
   x^T P x=\min_z\{z^TAz+(x-z)^TB(x-z)\}.
   \]
   Hence for every matrix `T`,
   \[
   P\preceq T^TAT+(I-T)^TB(I-T).
   \]
   Therefore the inverse-free sufficient condition
   \[
   \boxed{D-T^T\Sigma_VT-(I-T)^T\Sigma_C(I-T)\succeq0}
   \]
   implies `nabla^2 Phi <= 0`. At one point the optimal split is `T_*=(Sigma_V+Sigma_C)^{-1}Sigma_C`; a nearby rational matrix can be frozen on a whole interval box. This is the main route because it converts an interval inverse problem into polynomial matrix arithmetic.

3. **Support-only covariance domination.** Try to remove Gibbs multipliers as well, by bounding each directional block variance from its finite support (Popoviciu/Bhatia-Davis) and the exact support oracles from the preceding run. If this is too loose, record the quantitative failure and retain the matrix-split theorem as a boxwise compiler.

## Exact missing lemma after this run if attack 2 works

For a finite cover of the source-relevant projected outer feasible polytope by boxes `B_j`, construct one rational split matrix `T_j` per box and outward interval enclosures of `D,Sigma_V,Sigma_C` such that

\[
D(y)-T_j^T\Sigma_V(y)T_j-(I-T_j)^T\Sigma_C(y)(I-T_j)\succeq \eta_j I,
\qquad y\in B_j,
\]

with `eta_j>0`, except possibly boxes already killed by the rescued exponent/support boundary estimate. A successful cover would replace the source's coarse 100^3 outer sweep by a rigorous branch-and-bound concavity certificate.

The mathematical objective of this bounded run is to prove the split theorem, quantify its diagnostic margin at the inherited 4.4898 saddle, and test whether the support-only shortcut is remotely competitive before writing any checker.