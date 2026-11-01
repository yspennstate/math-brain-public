# C0101: second serious attempt, 2026-10-12

## Two approaches not tried in the first attempt

1. **Contact-point rigidity near the trace ceiling.** Work directly with the integer majorant from local stabilization, rather than assume periodicity or bounded growth error. Minimize its difference from a slightly penalized quadratic. When the trace deficit is small, the sum of the nonnegative nearest-neighbor contact errors is small. Propagate this estimate to distance two, where integer second differences determine the diagonal and mixed Hessian entries. Target: classify the entire trace-ceiling face, and obtain quantitative bounds for nearby matrices.

2. **Partial-infimum / Schur-complement reduction.** Subtract an integer quadratic in selected coordinates and minimize over those integer coordinates. At a minimizing fiber the eliminated-direction Laplacian is nonnegative; hence the resulting lower-dimensional integer function has a reduced Laplacian budget. When the quadratic in the eliminated directions is positive definite, its real minimum gives a Schur-complement lower bound. Combine with the planar classification to restrict maximal extensions of the explicit half-integral A_3. Main anticipated difficulty: a positive-semidefinite increment can have zero Schur complement while increasing only the eliminated directions, so planar maximality need not exclude it.

Approach 1 is selected because it applies to all stabilizing majorants and their closure, not just special cocycles. The first attempt's trace bound supplies its necessary normalization. The precise open gap remains rationality and isolation of maximal elements whose trace is strictly below 2d-1.

## Local contact estimate

Fix d≥1 and K=2d-1. Let B belong to S_d, and take integer g≥ceil(q_B), Δg≤K, as in ATTEMPT.md Lemma 1. For ε>0 let

    H(x)=g(x)-q_B(x)+ε|x|²,
    δ_ε=K-tr B+2dε.

H≥ε|x|² attains a global minimum at x_0. Set h(x)=H(x_0+x)-H(x_0). Then h≥0, h(0)=0 and Δh≤δ_ε. In particular δ_ε≥0 and

    sum_{y~0} h(y)≤δ_ε.

Thus 0≤h(±e_i)≤δ_ε. At e_i,

    sum_{y~e_i} h(y)≤2d h(e_i)+δ_ε≤(2d+1)δ_ε,

so 0≤h(e_i+e_j)≤(2d+1)δ_ε. No upper growth bound on g was used.

Define an integer symmetric matrix M from local differences of g at x_0:

    M_ii=g(x_0+e_i)+g(x_0-e_i)-2g(x_0),
    M_ij=g(x_0+e_i+e_j)-g(x_0+e_i)-g(x_0+e_j)+g(x_0) (i<j),
    M_ji=M_ij.

Quadratic second differences are independent of x_0. Therefore

    M_ii-B_ii+2ε=h(e_i)+h(-e_i),
    M_ij-B_ij=h(e_i+e_j)-h(e_i)-h(e_j).

The diagonal errors are nonnegative, each at most δ_ε, and their sum is at most δ_ε. The off-diagonal errors initially lie between -2δ_ε and (2d+1)δ_ε. They admit a sharper estimate. Write a=h(e_i), b=h(e_j), c=h(e_i+e_j). We have a+b≤δ_ε, and applying the neighbor estimate at both e_i and e_j gives c≤2d a+δ_ε and c≤2d b+δ_ε. Thus

    c-a-b≥-δ_ε,
    2(c-a-b)≤(2d-2)(a+b)+2δ_ε≤2dδ_ε.

Consequently -δ_ε≤M_ij-B_ij≤dδ_ε. Also tr M=Δg(x_0)≤K. If δ_ε<1 then

    tr M≥tr B-2dε=K-δ_ε>K-1,

so the integer trace tr M equals K. This establishes the finite local step; further consequences and checks are to be recorded below.

## The trace-ceiling face is completely classified

**Theorem 11.** For every d≥1,

    {A∈Γ_d: tr A=2d-1}
      = {symmetric integer matrices M: tr M=2d-1}.

Proof. The right-to-left inclusion was proved in ATTEMPT.md Theorem 4. For the converse take A∈Γ_d of trace K, and choose B_n∈S_d with B_n→A. Choose any ε_n>0 tending to zero. The trace bound gives K-tr B_n≥0, so δ_n=K-tr B_n+2dε_n→0. Use the local contact construction to produce symmetric integer M_n. Its diagonal entries obey |(M_n)_ii-(B_n)_ii|≤δ_n+2ε_n. Its mixed entries obey |(M_n)_ij-(B_n)_ij|≤dδ_n. Therefore M_n→A entrywise. Every convergent sequence of integers has an integer limit: if a real limit were not integer, its positive distance to the closed set Z would contradict convergence. Applying this to each entry shows A is integer. Its trace is already K. □

In particular all maximal elements on the trace ceiling have integer entries, without a periodicity assumption. These elements form a discrete set on that face. This is not isolation relative to maximal elements below that face.

## Quantitative rigidity in a strip below the ceiling

**Theorem 12.** If A∈Γ_d has trace deficit δ=K-tr A with 0≤δ<1, then there is a symmetric integer matrix M of trace K with

    0≤M_ii-A_ii≤δ,
    -δ≤M_ij-A_ij≤dδ  (i≠j).

In particular M is a maximal matrix by ATTEMPT.md Theorem 4, and ||M-A||_max≤dδ. This is approximation, not necessarily Loewner domination.

Proof. Choose B_n∈S_d tending to A and ε_n>0 tending to zero, so δ_n=K-tr B_n+2dε_n tends to δ<1. For sufficiently large n the local construction gives integer M_n of trace K. The displayed contact bounds show that their entries are bounded uniformly in n. A bounded family of integer matrices is finite, so pass to an infinite subsequence on which M_n equals a fixed M. For diagonal entries,

    0≤(M_n)_ii-(B_n)_ii+2ε_n≤δ_n.

Taking limits gives the claimed diagonal bounds. The mixed bounds pass to the limit in the same way. The integer matrix M has trace K. □

**Corollary 13.** For d≥2, if 0≤δ<1/(2d), at most one symmetric integer trace-K matrix can satisfy these bounds for A.

Proof. Two such matrices differ entrywise by at most 2dδ<1, by the max-norm bound. Their entry differences are integers, hence zero. □

The contact matrices need not dominate A: positivity of each diagonal error and a small bound on mixed errors do not imply positive semidefiniteness. Theorem 12 cannot be promoted to a classification by simply asserting domination.

## A genuine trace gap for extensions of the half-integral example

**Theorem 14.** Let d≥3 and let A_d be the matrix in ATTEMPT.md Theorem 10, with diagonal (1,1,2,...,2) and A_12=A_21=1/2. Every B∈Γ_d with B≥A_d satisfies

    tr B≤2d-1-1/(2d).

Consequently there is a noninteger maximal B≥A_d with trace in [2d-2, 2d-1-1/(2d)].

Proof. Write K=2d-1 and δ=K-tr B≥0. If δ≥1, the stated bound holds. Otherwise Theorem 12 supplies an integer symmetric matrix M of trace K with M_ii≥B_ii≥(A_d)_ii. Thus M_ii-(A_d)_ii are nonnegative integers summing to K-tr A_d=1. At least one of M_11-1, M_22-1 equals zero. Suppose M_11=1; the other case is symmetric. Then 1≤B_11≤M_11=1, so (B-A_d)_11=0. A zero diagonal entry of a positive-semidefinite matrix forces its entire corresponding row to vanish, hence B_12=(A_d)_12=1/2. Since M_12 is integer, |M_12-B_12|≥1/2. Theorem 12 bounds this by dδ, giving δ≥1/(2d). This proves the bound in all cases. A maximal extension exists by ATTEMPT.md Theorem 7; Theorem 10 proves it noninteger; B≥A_d gives tr B≥2d-2. □

This is a proved gap for the upper section above A_d, not a uniform trace gap for every noninteger maximal matrix. No periodicity assumption is used.
