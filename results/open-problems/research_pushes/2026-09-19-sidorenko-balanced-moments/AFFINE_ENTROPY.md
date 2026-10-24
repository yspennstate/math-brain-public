# An affine-channel obstruction to a common-latent entropy shortcut

19 September 2026. This note tests an entropy extension of the transfer
argument. It proves a counterexample to that extension, not to Sidorenko.
The finite-field mechanism uses elementary character orthogonality and matrix
rank counts; no priority claim or independent audit is made.

## 1. The proposed sufficient inequality

For a nonnegative symmetric 1-regular kernel W on (Omega,p), let

    C_k(x_1,...,x_k) = E_u product_{i=1}^k W(u,x_i),
    D_k = E_{p^k}[C_k log C_k].

C_k is a probability density, realized by first sampling u with law p and
then sampling the x_i conditionally independently with transition density
W(u,x_i). Let nu_5 have density C_5. Its five cyclic triple marginals all
have density C_3. The variational/Jensen lower bound gives

    log t_H(W) >= 5D_3-D_5.                         (1.1)

For strictly positive W, this follows directly by rewriting the target
integral under nu_5 and applying Jensen to its logarithm. If W has zeros,
restrict the integral to the support of nu_5. On that support every cyclic
C_3 factor is positive; deleting the complement only lowers the integral.
The same Jensen argument proves (1.1). Finite-dimensional limiting arguments
also suffice. Thus D_5<=5D_3 would prove the target using this particular
trial distribution. It is false.

## 2. A symmetric regular affine channel

Let q be prime, d>=1, and Omega=F_q^d times F_q with uniform measure. Put

    W((a,b),(u,c)) = q * 1_{a dot u=b+c}.             (2.1)

This is symmetric and nonnegative. For fixed (u,c), exactly q^d of the
q^(d+1) possible (a,b) satisfy the equation, so every weighted row sum is
one. No directed/nonregular relaxation has been used.

A latent state (U,C) is uniform. Given it, an output consists of a uniform
A in F_q^d and the deterministic label B=A dot U-C. For k independent
conditional outputs, fix the feature rows A_1,...,A_k. The label vector is
uniform on the image of the linear map whose rows are (A_i,-1). Its entropy
is therefore the rank of that matrix times log q. Since each output is
uniform on Omega,

    D_k = [k-E rank((A_i,-1)_{i=1}^k)] log q
        = delta_(k-1,d) log q,                      (2.2)

where delta_(r,d) is the expected row nullity of a uniform r by d matrix
over F_q. For the second equality, subtract the first row from all others;
the differences A_i-A_1 are independent uniform vectors and the first
row's last coordinate is -1. Hence the rank is one plus their rank.

## 3. Exact 81-state counterexample

Take q=3,d=3. The exact rank counts give

    D_3/log 3 = 106/729,
    D_5/log 3 = 614644/531441,
    (D_5-5D_3)/log 3 = 228274/531441 > 0.            (3.1)

There is no numerical logarithm comparison: log 3 is positive and all
coefficients are rational. The kernel has 81 states and entries zero or
three, and is exactly symmetric and 1-regular.

For completeness, the number of rank-s matrices of size r by d is

    product_{i=0}^{s-1} [(q^r-q^i)(q^d-q^i)/(q^s-q^i)].

This follows by counting full-column-rank r by s factors and full-row-rank
s by d factors and dividing by the number of invertible s by s changes of
basis. The expected nullity can independently be computed row by row:
from rank s a new uniform row stays in the row span with probability q^(s-d)
and otherwise raises the rank by one. The checker verifies both calculations
and exhaustively counts all 729 smaller 2 by 3 matrices.

## 4. No uniform constant can repair this trial-distribution strategy

For fixed q and r and d tending to infinity,

    delta_(r,d) = [(q^r-1)/(q-1)] q^(-d) + O_(q,r)(q^(-2d)).

Indeed each projective nonzero coefficient vector is a left relation with
probability q^(-d). Two distinct projective relations are linearly independent,
so their joint probability is q^(-2d). Except on the union of these two-relation
events, the row nullity and the number of projective relations are both zero
or both one. There are finitely many such relation pairs for fixed q,r.
It follows from (2.2) that

    D_5/D_3 -> (q^4-1)/(q^2-1) = q^2+1.

Letting q grow shows that no constant independent of the kernel can give
D_5<=C D_3 on all bounded symmetric nonnegative regular kernels. Each kernel
is bounded, but there is no common entrywise bound across all q. The explicit
q=3 example already invalidates the needed coefficient five.

## 5. These kernels nevertheless satisfy Sidorenko for every bipartite graph

The failure is in the entropy shortcut, not in the desired graph inequality.
For a finite bipartite graph F=(L,R,E), expand each factor using

    q * 1_{v=0} = sum_{t in F_q} exp(2 pi i t v/q).

Averaging the label b at each vertex forces the sum of its incident edge
labels t_e to be zero. For each such flow t, form the L by R matrix M_t
whose entry is t_e on an edge and zero otherwise. Averaging the feature
vectors, coordinate by coordinate and first on the left side, gives

    t_F(W) = sum_{t: sum_{e incident v}t_e=0 for every v}
                   q^(-d rank(M_t)) >= 1.           (5.1)

Every term is nonnegative; the zero flow contributes one. This proof is
character orthogonality, not a claimed new general Fourier principle.

For H at q=3 the flow space has dimension six. Enumeration of all 729
flows gives rank multiplicities

    rank 0: 1; rank 1: 10; rank 2: 80;
    rank 3: 410; rank 4: 228.

At d=3 this yields exactly

    t_H(W)=265963/177147 > 1.

The checker verifies the entire flow space, every incidence constraint,
and every finite-field rank. Thus the counterexample to the entropy bound
comes with a separate exact positive evaluation of the target itself.

## 6. Consequence for the continuation

The common-latent trial distribution is not sufficiently flexible. A useful
entropy proof would need a different coupling or a comparison retaining more
than the triple relative entropy. This does not invalidate the earlier
stationary-pair-chain Perron bound or BALANCED_MOMENTS.md, neither of which
uses D_5<=5D_3. No assertion about the sign of the universal fifth-trace
remainder has been established here.

Run python check_affine_entropy.py. All accepted decisions use integers and
fractions. The analytic entropy and Fourier implications are proved above,
not supplied by the finite enumeration.
