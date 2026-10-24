# Exact-rank-three finite-hub reduction for arbitrary affine terms

**Status:** Rigorous structural reduction, not a full dimension-uniform proof. The unresolved branch retains a spectral direction concentrated on a finite set of physical coordinates.

Let (X_i) be independent with densities bounded by one. Let (A=U\Lambda U^T) be symmetric of **exact rank three**, (U^TU=I_3), and (|\lambda_j(\Lambda)|\ge\sigma>0). Write (u_i^T) for row (i) of (U), and define
\[
 H=\{i:\|u_i\|^2\ge1/144\},\qquad R=[n]\setminus H,\qquad G_R=U_R^TU_R.
\]
Then (|H|\le432), since (\sum_i\|u_i\|^2=3).

## Proposition

If (\lambda_{\min}(G_R)\ge1/12), then for all affine (b,c),
\[
 \|p_{X^TAX+b^TX+c}\|_\infty\le288/\sigma.
\]
Consequently every exact-rank-three frame satisfies a dichotomy: this density bound holds, or there is a unit vector (v\in\mathbb R^3) such that
\[
 \sum_{i\in H}(u_i\cdot v)^2>11/12,
\]
where (H) consists of at most (432) **original physical coordinates**.

## Proof

Condition on (X_H). The remaining coordinates stay independent with density caps one. Their conditional quadratic matrix is (A_{RR}=U_R\Lambda U_R^T), with arbitrary conditional affine terms. When (G_R\succeq I/12), the columns of (\widetilde U=U_R G_R^{-1/2}) are orthonormal. Every row satisfies
\[
 \|\widetilde u_i\|^2=u_i^TG_R^{-1}u_i
 \le12\|u_i\|^2<1/12
 \qquad(i\in R).
\]
The nonzero eigenvalues of (A_{RR}) are those of (G_R^{1/2}\Lambda G_R^{1/2}), whose smallest absolute value is at least (\sigma\lambda_{\min}(G_R)\ge\sigma/12), as follows by inverting the latter product. Thus the diffuse exact-rank-three theorem with leverage at most (1/12), valid for arbitrary affine coefficients, bounds each conditional density by (24/(\sigma/12)=288/\sigma). Averaging conditional interval probabilities proves the first assertion.

If (\lambda_{\min}(G_R)<1/12), choose a unit eigenvector (v) with (v^TG_Rv<1/12). Since (U^TU=I_3), (\sum_{i\in H}(u_i\cdot v)^2=1-v^TG_Rv>11/12). This is the stated alternative.

The diffuse theorem and its complete Plancherel proof are at https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T193700Z-diffuse-rank-three-fourier/REPORT.md . The finite-hub alternative includes near-coloop configurations and remains unresolved by this reduction.


## Second finite-hub branch: all three directions on heavy coordinates

Suppose in addition that $m=|H|\ge3$ and $G_H=U_H^TU_H\succeq c_0 I_3$ for a fixed $c_0>0$. Then, without assuming anything about $G_R$,
\[
 \|p_{X^TAX+b^TX+c}\|_\infty
 < \frac{51(m-2)}{c_0\sigma}.
\]
Indeed, $W=U_H G_H^{-1/2}$ has three orthonormal columns. The volume-sampled triple identity proved in the [exact-rank-three arbitrary-affine report](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T193238Z-exact-rank-three-affine/REPORT.md) supplies a three-element physical subset $I\subset H$ with
\[
 s_{\min}(W_I)^2\ge\frac1{3(m-2)}.
\]
Since $U_I=W_I G_H^{1/2}$, we have $s_{\min}(U_I)^2\ge c_0/[3(m-2)]$. The inverse factorization of $A_{II}=U_I\Lambda U_I^T$ gives $s_{\min}(A_{II})\ge c_0\sigma/[3(m-2)]$, valid also for indefinite $\Lambda$. Condition on all coordinates outside $I$ and apply the three-physical-coordinate density bound $<17/s_{\min}(A_{II})$ uniformly in the conditional affine term.

For a fully numerical dichotomy, take $c_0=1/12$. If $G_R\succeq I_3/12$, the bound is $288/\sigma$. Otherwise, if $G_H\succeq I_3/12$, the bound is at most $51\cdot430\cdot12/\sigma=263160/\sigma$. The remaining branch has **both** $\lambda_{\min}(G_R)<1/12$ and $\lambda_{\min}(G_H)<1/12$: some direction is concentrated on the at most 432 heavy coordinates, while another direction is concentrated on the diffuse complement. This is the mixed heavy/diffuse geometry containing the near-coloop leakage problem. It is not solved here.

Technical detail for the first branch: diagonalize the symmetric matrix $G_R^{1/2}\Lambda G_R^{1/2}$ after whitening $U_R$. The corresponding orthogonal rotation of the whitened frame preserves every row norm and therefore the leverage threshold.
