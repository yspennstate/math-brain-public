Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# Inverse-free parallel-sum certificate for the remaining Diaz outer Hessian

This note is a self-contained algebraic theorem used by PROB10-04. It is **auxiliary progress only**: it does not improve the published random-3-SAT threshold endpoint by itself.

## 1. Parallel-sum variational identity

Let `A,B` be real symmetric positive-definite `d x d` matrices and put

\[
P:=(A^{-1}+B^{-1})^{-1}.
\]

For every `x in R^d`,

\[
\boxed{
x^TPx=\min_{z\in\mathbb R^d}\bigl[z^TAz+(x-z)^TB(x-z)\bigr].
}
\tag{1.1}
\]

### Proof

Set

\[
T_*=(A+B)^{-1}B.
\]

The gradient of the bracketed quadratic with respect to `z` is

\[
2Az-2B(x-z)=2(A+B)z-2Bx,
\]

so its unique minimizer is `z=T_*x`. Completing the square gives

\[
z^TAz+(x-z)^TB(x-z)
=(z-T_*x)^T(A+B)(z-T_*x)+x^T\bigl[B-B(A+B)^{-1}B\bigr]x.
\]

It remains to identify the last matrix. Multiplying on the left by `A^{-1}+B^{-1}` gives

\[
(A^{-1}+B^{-1})\bigl[B-B(A+B)^{-1}B\bigr]
=I,
\]

so

\[
B-B(A+B)^{-1}B=(A^{-1}+B^{-1})^{-1}=P.
\]

This proves (1.1). QED.

## 2. Matrix-splitting upper envelope

For an arbitrary real `d x d` matrix `T`, evaluate (1.1) at `z=Tx`. Then for every `x`,

\[
x^TPx\le x^T\Bigl[T^TAT+(I-T)^TB(I-T)\Bigr]x.
\]

Hence

\[
\boxed{
P\preceq R_T:=T^TAT+(I-T)^TB(I-T).
}
\tag{2.1}
\]

Equality holds for `T=T_*=(A+B)^{-1}B`.

The scalar-collinear certificate is the special case `T=tI`:

\[
P\preceq t^2A+(1-t)^2B.
\tag{2.2}
\]

This explains why a one-dimensional split can work locally but can be much less robust than a full matrix split.

## 3. Inverse-free strict-concavity theorem

Let `D` also be symmetric positive definite. Suppose there are `T`, `eta>0` such that

\[
\boxed{
D-R_T\succeq \eta I.
}
\tag{3.1}
\]

Then by (2.1),

\[
D\succeq P+\eta I.
\]

Since inversion reverses Loewner order on the positive cone,

\[
D^{-1}\preceq(P+\eta I)^{-1}.
\]

Therefore

\[
D^{-1}-A^{-1}-B^{-1}
=D^{-1}-P^{-1}
\preceq (P+\eta I)^{-1}-P^{-1}\prec0.
\tag{3.2}
\]

Thus the single LMI (3.1), containing **no matrix inverse of `A` or `B`**, certifies strict negative definiteness of the target Hessian.

A quantitative version follows. If additionally `R_T\preceq L I`, then `P\preceq L I`, and the eigenvalues of

\[
P^{-1}-(P+\eta I)^{-1}
\]

are `eta/[lambda(lambda+eta)]` with `lambda` ranging over the eigenvalues of `P`. Since this expression decreases in `lambda`,

\[
\boxed{
D^{-1}-A^{-1}-B^{-1}
\preceq-\frac{\eta}{L(L+\eta)}I.
}
\tag{3.3}
\]

This is useful for interval boxes: a lower LMI gap `eta` and an upper bound `L` on the split envelope immediately give a Hessian margin without interval matrix inversion.

## 4. Application to the Diaz outer problem

For the inherited outer macrostate `y=(u,v,w)` from PROB10-04 run 11, let

- `A=Sigma_V(y)`, the variable-side Gibbs covariance;
- `B=Sigma_C(y)`, the clause-side Gibbs covariance;
- `D=H_copy(y)^{-1}`, the copy covariance.

Run 11 proved exactly

\[
\nabla^2\Phi(y)=D^{-1}-A^{-1}-B^{-1}.
\]

Hence any rational matrix `T` for which outward interval arithmetic proves

\[
D-T^T\Sigma_VT-(I-T)^T\Sigma_C(I-T)\succeq\eta I
\]

on an outer box gives a rigorous concavity certificate on that box. This is strictly more interval-friendly than directly enclosing `Sigma_V^{-1}` and `Sigma_C^{-1}`.

At a point, the ideal split is

\[
T_*=(\Sigma_V+\Sigma_C)^{-1}\Sigma_C.
\]

One should compute it only to **choose** a nearby rational matrix and then verify the rational matrix directly by (3.1); the proof certificate does not depend on trusting the floating inverse used to propose `T`.

## 5. Finite-cover compiler

Let the projected feasible outer region be covered by finitely many boxes `B_j`. For each box choose a rational matrix `T_j`. If rigorous interval evaluation proves

\[
D(y)-T_j^T\Sigma_V(y)T_j-(I-T_j)^T\Sigma_C(y)(I-T_j)\succeq\eta_j I
\quad\forall y\in B_j,
\]

with `eta_j>0`, then `Phi` is strictly concave on every such box. Boxes on which the rescued exponent/support bounds are already negative need no curvature certificate. Consequently a branch-and-bound proof may alternate two tests:

1. **rescue/support kill:** upper bound the rescued exponent below the target level;
2. **split-concavity kill:** certify (3.1) and use a stationary-point/face bound.

This is an exact reduction. The unresolved source-level obligation is to implement outward interval enclosures for the covariance maps over the surviving boxes and close the global cover.

## 6. Why this is genuinely different from the failed one-side KL route

The failed shortcut in run 11 asked one endpoint distribution to pay the full copy Bregman cost; coherent degree-`D` states make that false. The parallel sum instead optimally **splits each test direction between the variable and clause sides**. The minimizing split is matrix-valued, not a fixed scalar fraction, and uses both covariance structures. Thus the theorem survives the specific high-degree obstruction that killed the one-side argument; it does not assert that the global boxwise LMI will hold automatically.