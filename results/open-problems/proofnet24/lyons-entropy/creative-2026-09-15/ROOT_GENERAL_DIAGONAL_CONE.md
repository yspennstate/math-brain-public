# C020's completion extends to arbitrary three-site diagonals

Date: 2026-09-15. Root creative corollary, not an agent execution. This strengthens the scope of C020's completed equal-diagonal theorem; it does not prove unrestricted three-site concavity or the full Lyons conjecture.

## The theorem

Let K be Hermitian 3-by-3 with diagonal d_i in (0,1), and put

\[
\mu=\min_i\{d_i,1-d_i\}>0.
\]

The diagonal entries need not agree. If

\[
\boxed{\max_{i<j}|K_{ij}|\le {2\over7}\mu,}
\tag{1}
\]

then 0<K<I and, in every Hermitian direction A,

\[
\boxed{D^2H(K)[A,A]
\le-{2\over19}\sum_i A_{ii}^2
-{3\over7}\sum_{\{i,j,k\}=[3]}M_{ii}|A_{jk}|^2\le0.}
\tag{2}
\]

There are three complementary-edge terms in the sum. Here M=diag(c_23,c_13,c_12)+tau K is the usual three-site frozen-log matrix. If K is connected, M_ii>0 and (2) is strict for nonzero A. Missing edges are allowed; no lower bound or comparability condition on nonzero edges is used.

Unlike the equal-diagonal slice, (1) defines a full-dimensional convex region in the entire Hermitian matrix space. Entropy is concave on its closure.

## Proof with all changed estimates explicit

Retain C020's coefficient convention c_jk>=0 and c_jk+tau>=0, and set eta=2/7. Put m_i=M_ii. The two decompositions

\[
M=\operatorname{diag}(c_{23},c_{13},c_{12})+\tau K,
\]
\[
M=\operatorname{diag}(c_{23}+\tau,c_{13}+\tau,c_{12}+\tau)
+|\tau|(I-K)\quad(\tau<0)
\]

give m_i>=|tau|mu for **each** i, whether or not the d_i are equal. If all six conditional pair coefficients are bounded by C, then

\[
m_i=(1-d_i)c_{jk}+d_i(c_{jk}+\tau)\le C,
\qquad |\tau|\le C.
\tag{3}
\]

Thus the two off-diagonal estimates needed in C020 are unchanged:

\[
|M_{jk}|\le\eta\sqrt{m_jm_k},\qquad
{|M_{jk}|^2\over m_i}\le |\tau|\eta^2\mu.
\tag{4}
\]

Zero denominators correspond to zero numerators and those terms are omitted. C020's adjugate expansion and completion of all off-diagonal squares therefore give, without any equal-diagonal hypothesis,

\[
2\operatorname{tr}(M\operatorname{adj}A)
\le C\left(2+{4\eta^2\mu\over1-2\eta}\right)\sum_i A_{ii}^2
-(1-2\eta)\sum_i m_i|A_{jk}|^2.
\tag{5}
\]

For the uniform logarithm bound compare the atoms to the product law with the actual means d_i, not a common mean. In the signed determinant set q_i=d_i-1_{i absent}, so |q_i|>=mu. The same three pair terms and one cycle term yield

\[
\left|{p_S\over\prod_{i\in S}d_i\prod_{i\notin S}(1-d_i)}-1\right|
\le3\eta^2+2\eta^3={100\over343}.
\]

The product log weight is modular even with unequal means. Every conditional pair coefficient is consequently bounded by

\[
C=4\log(343/243)<7/5.
\tag{6}
\]

C020 supplies the rational odd-series proof of this scalar inequality; it depends on no diagonal parameter. Applying mu<=1/2 in (5) gives the same bound as there:

\[
2\operatorname{tr}(M\operatorname{adj}A)
\le {10\over3}\sum_i A_{ii}^2
-{3\over7}\sum_i m_i|A_{jk}|^2.
\tag{7}
\]

The occupation covariance now has Sigma_ii=d_i(1-d_i)<=1/4 and Sigma_ij=-|K_ij|^2. Absolute row sums imply

\[
\lambda_{\max}(\Sigma)\le {1\over4}+2\eta^2\mu^2
\le {57\over196}.
\]

Score projection onto occupation indicators therefore gives

\[
\mathcal I_K(A)\ge {196\over57}\sum_i A_{ii}^2.
\tag{8}
\]

Subtract (8) from (7) in H''=-I+2tr(M adj A). Since 196/57-10/3=2/19, this proves (2).

Finally the off-diagonal operator norm is at most 2eta mu<mu, establishing strict contraction directly. Connectedness implies m_i>0 by the same equality argument in C020: if tau=0 and a pair coefficient vanishes, unconditional and conditional Schur determinant equalities force the remaining two-edge path to vanish, disconnecting L and hence K. If tau!=0, m_i>=|tau|mu>0 already.

## Convexity and boundary

Condition (1) is equivalent to the simultaneous convex constraints

\[
|K_{ij}|\le(2/7)d_k,\qquad
|K_{ij}|\le(2/7)(1-d_k)
\quad\text{for every edge }ij\text{ and every }k.
\]

It thus defines a convex set. It has nonempty full-dimensional interior, for example around any diagonal matrix with all means strictly between zero and one and sufficiently small strict edge bounds. Integrating (2) along its affine segments proves entropy concavity in the interior. The regularization K -> (1-2epsilon)K+epsilon I preserves these constraints and proves the closure statement by continuity. No boundary Hessian is asserted.

The extension uses the exact mechanism already proved by C020; its new observation is that every estimate survives unequal diagonals after taking their common minimum distance to the boundary. The general large-edge region remains outside this proof.
