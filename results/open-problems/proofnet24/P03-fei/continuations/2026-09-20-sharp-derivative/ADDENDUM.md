# Further full-scope attempts: compression and pivotal-curvature rank

20 September 2026. Continuation after the main report was committed. **Full FEI remains unproved here.** This addendum gives an exact counterexample to influence-paid monotone compression, a physical rank resource with an exact arbitrary-gate composition rule, and an all-coordinate obstruction to paying entropy by that resource's one-step decrease. No independent review or publication-priority clearance is claimed.

## 1. Influence-paid compression is false

Let C_i sort the two signs on every physical i-edge into the order (-1,+1), leaving equal pairs unchanged. A proposed reduction to monotone functions would be valid if its lost entropy could be bounded by a constant times its decrease in total influence. The following example refutes that proposed payment for every finite constant.

Index the four-dimensional cube by integers 0,...,15, with coordinate 0 the least significant bit. Set

    f(x)=-1 exactly at {1,6,10,12},
    g(x)=-1 exactly at {0,6,10,12}.

Then g=C_0 f. Their integer Walsh numerators, in label order 0,...,15, are

    16 fhat = (8,-4,0,4,0,4,0,4,0,4,0,4,0,4,-8,-4),
    16 ghat = (8,-8,0,0,0,0,0,0,0,0,0,0,0,0,-8,-8).

Thus f has two masses 1/4 and eight masses 1/16, while g has four masses 1/4. Directly,

\[
H(f)=3,\qquad H(g)=2,\qquad
\operatorname{Inf}_i(f)=\operatorname{Inf}_i(g)=\tfrac12
\quad(0\le i<4).
\]

Consequently

\[
\boxed{H(f)-H(C_0f)=1,\qquad I(f)-I(C_0f)=0.}
\]

No finite C can give H(f)-H(C_i f)<=C[I(f)-I(C_i f)] for every Boolean f. This also rules out payment using only the change in the original-coordinate folded sum J, which is unchanged here. It does not assert that every possible compression argument fails, and it says nothing analogous about the affine minimum M: that quantity need not stay unchanged.

The example explains the lost information. Writing the two restrictions as f_0=A+B and f_1=A-B, the real functions A,B have disjoint supports and satisfy A^2+B^2=1. Compression replaces B by -|B|. A physical boundary cost can fail to see the relative signs on separated components of the support of B, while those signs still affect Fourier interference and entropy. The exact Walsh table above, not this explanation alone, certifies the counterexample.

The exploratory compression search exhausts dimensions one through four and stops at this witness. Its floating-point diagnostics are kept separately; the equalities above are checked by integers and exact entropy signatures in verify_addendum.py.

## 2. A rank resource on pivotal directions

For a Boolean sign f at a physical point x, define its pivotal directions

\[
P_f(x)=\{i:f(x+e_i)\ne f(x)\}.
\]

On this index set form the symmetric zero-diagonal binary matrix

\[
C_f(x)_{ij}=\mathbf1\{f(x+e_i+e_j)\ne f(x)\},\qquad i\ne j.
\]

All matrix operations in this addendum are over F_2. Put

\[
r_f(x)=\operatorname{rank}C_f(x),\qquad
\epsilon_f(x)=\mathbf1\{\mathbf1_{P_f(x)}\notin\operatorname{im}C_f(x)\},
\]
\[
R(f)=\mathbb E_x r_f(x),\qquad
\mathcal Q(f)=\mathbb E_x[r_f(x)+\epsilon_f(x)].
\]

The empty matrix has rank zero and flag zero. These are explicitly defined physical-coordinate quantities, not Fourier rank or minimum affine influence.

**Proposition 2.1.** In every dimension,

\[
\boxed{0\le R(f)\le\mathcal Q(f)\le I(f).}
\]

Indeed r<=|P|. If epsilon=1, the matrix has a nonzero kernel and r<=|P|-1, so r+epsilon<=|P|. Averaging |P| gives I.

Moreover R(f)=0 if and only if f is a character times a constant sign. To see this, an odd-parity two-dimensional face has a unique minority-sign vertex. Both its directions are pivotal there, and their matrix entry is one, forcing rank at least two. Thus R=0 implies that every two-dimensional face has even sign parity. Writing f=(-1)^a, all mixed second differences of a vanish. Each first difference is then independent of all other coordinates, hence constant, and a is affine. Conversely an affine sign has C_f(x)=0 everywhere.

The candidate dimension-free inequality

\[
H(f)\stackrel{?}{\le} C R(f)
\tag{2.1}
\]

would imply full FEI, but it is **unproved**. We have not proved the converse implication from FEI, so this is not asserted to be an equivalent reformulation of FEI.

## 3. Exact physical-restriction monotonicity

Let g be a restriction obtained by fixing coordinate i, and let y correspond to x on that physical slice. The pivotal matrix C_g(y) is exactly the principal submatrix of C_f(x) obtained by deleting i if it was pivotal. Therefore r_g(y)<=r_f(x).

For any alternating matrix C and vector u, elementary elimination gives

\[
\operatorname{rank}\begin{pmatrix}C&u\\u^T&0\end{pmatrix}
=\operatorname{rank}C+2\mathbf1\{u\notin\operatorname{im}C\}.
\tag{3.1}
\]

If u=Cw, changing the last basis vector by w eliminates the off-diagonal column, because w^TCw=0. If u is not in the image, it is nonzero on the kernel of C, and its pairing with the new last coordinate creates one additional nondegenerate two-dimensional block. This proves (3.1).

Apply (3.1) with u the all-ones vector. The quantity r+epsilon is the average of the rank of C and the rank of its bordered matrix. Both restricted matrices are principal submatrices of their parents. Hence

\[
r_g(y)+\epsilon_g(y)\le r_f(x)+\epsilon_f(x).
\]

Averaging over the uniform assignments gives the universal monotonicity

\[
\boxed{\mathbb E_bR(f_{i=b})\le R(f),\qquad
\mathbb E_b\mathcal Q(f_{i=b})\le\mathcal Q(f).}
\tag{3.2}
\]

These decreases telescope on any finite physical restriction tree. This is an actual bounded resource, unlike the nonsummable derivative-chain sum of M. Nevertheless Section 6 shows that entropy cannot be charged locally to these decreases with a universal constant, even by choosing the most favorable coordinate.

## 4. Exact composition theorem for arbitrary Boolean gates

Let F be any Boolean sign on m input bits. Let g_j be Boolean signs on disjoint physical groups. Encode their outputs as bits b_j=1_{g_j(x_j)=-1}; the composed function is f(x)=F(b).

At the fixed point x let

\[
J=\{j:F(b+e_j)\ne F(b)\},\qquad
A=\{j\in J:\epsilon_{g_j}(x_j)=1\}.
\]

Let C be the outer pivotal matrix at b restricted to A. Then

\[
\boxed{r_f(x)=\sum_{j\in J}r_{g_j}(x_j)+\operatorname{rank}C,}
\tag{4.1}
\]
\[
\boxed{\epsilon_f(x)=\mathbf1\{\mathbf1_A\notin\operatorname{im}C\}.}
\tag{4.2}
\]

This covers arbitrary outer truth tables, unequal and biased children, and all dimensions; it is not confined to NAND or symmetric gates. It requires disjoint physical input groups.

### Proof of the matrix structure

A physical direction in child j is pivotal for f exactly when j is pivotal for F and that direction is pivotal for g_j. Within such a group the root matrix equals B_j=C_{g_j}(x_j). Between groups j,l it is the constant block C_F(b)_{jl} u_j u_l^T, where u_j is the all-ones vector on the child pivotal set. Thus the root matrix is a block diagonal alternating matrix plus these rank-one cross blocks.

### Proof by computing its kernel

For a vector v=(v_j), write s_j=u_j^T v_j and a_j=sum_l C_F(b)_{jl}s_l. The kernel equation on block j is

\[
B_jv_j=a_j u_j.
\tag{4.3}
\]

For an inactive block j not in A, choose w_j with B_jw_j=u_j. Since B_j is alternating, u_j^Tw_j=w_j^TB_jw_j=0. Also u_j annihilates ker B_j. Hence every solution v_j=a_jw_j+k_j has s_j=0, and its free dimension is dim ker B_j.

For an active block j in A, u_j is not in the image, so (4.3) requires a_j=0 and v_j belongs to ker B_j. The functional u_j is nonzero on that kernel, so every prescribed bit s_j is attainable, with a solution fiber of dimension dim ker B_j-1.

It follows that the only remaining equations are C s_A=0. The kernel dimension is therefore

\[
\sum_j\dim\ker B_j-|A|+\dim\ker C
=\sum_j\dim\ker B_j-\operatorname{rank}C,
\]

proving (4.1). The all-ones functional on the full vector is sum_j s_j=sum_{j in A}s_j. It annihilates the root kernel if and only if the all-ones functional on A annihilates ker C, equivalently if and only if 1_A belongs to im C. This proves (4.2).

### Expected rank and influence

Let w_j be the probability that the other child outputs make outer coordinate j pivotal. For a Boolean outer gate this event does not depend on its own j-th input bit. Independence of the physical groups therefore gives

\[
\boxed{R(f)=\sum_jw_jR(g_j)+\mathbb E\operatorname{rank}C,\qquad
I(f)=\sum_jw_jI(g_j).}
\tag{4.4}
\]

The expected rank increment is nonnegative. The flag law (4.2) retains the extra state needed to compute further compositions. No entropy inequality is assumed or proved by (4.1)-(4.4).

## 5. Tensor products and the bounded flag correction

For the product f(x)g(y) on disjoint variables, the outer gate is parity, whose pivotal matrix is zero. Equations (4.1)-(4.2) give

\[
R(fg)=R(f)+R(g),\qquad
\epsilon_{fg}(x,y)=\epsilon_f(x)\lor\epsilon_g(y).
\]

Thus, writing p=Pr(epsilon_f=1),

\[
\mathcal Q(f^{\otimes k})=kR(f)+1-(1-p)^k,
\qquad H(f^{\otimes k})=kH(f).
\]

Consequently a universal bound H<=C Q would imply H<=CR with the same constant, by dividing the k-fold tensor bound by k and taking k to infinity. The reverse follows from R<=Q. This is an equivalence between the two **unproved rank-budget inequalities**, not a claimed equivalence with FEI. The bounded flag correction alone cannot repair a failure of a global H/R bound.

For the one-point defect on n variables, only the exceptional point has nonzero pivotal rank. Its matrix is the complete-graph alternating matrix, with rank n for even n and n-1 for odd n. Hence

\[
R(1-2\mathbf1_{x=0})=2^{-n}(n-\mathbf1_{n\text{ odd}}).
\]

Its H/R tends to eight; the five-variable ratio is approximately 9.059351. These observations set constraints on (2.1), not a universal upper bound.

## 6. All-coordinate obstruction to local rank-budget payment

Take the symmetric four-variable sign

\[
f(x)=-1\quad\Longleftrightarrow\quad |x|=1.
\]

Its exact values are

\[
H(f)=3,\quad R(f)=\tfrac12,\quad \mathcal Q(f)=\tfrac{19}{16}.
\]

By symmetry all coordinates give the same two restrictions. Their values are

\[
R(f_{i=0})=\tfrac34,\quad R(f_{i=1})=\tfrac14,
\]
\[
\mathcal Q(f_{i=0})=\tfrac{13}{8},\quad
\mathcal Q(f_{i=1})=\tfrac34,
\]
\[
H(f_{i=0})=H(f_{i=1})=4-\tfrac98\log_2 3.
\]

The entropy formula follows from one Fourier mass 9/16 and seven masses 1/16 for each restriction. Therefore, at **every** coordinate,

\[
R(f)-\mathbb E_bR(f_{i=b})=0,
\quad\mathcal Q(f)-\mathbb E_b\mathcal Q(f_{i=b})=0,
\]
\[
\boxed{H(f)-\mathbb E_bH(f_{i=b})
=\tfrac98\log_2 3-1>\tfrac{783}{1000}.}
\]

Neither R nor Q can pay this entropy decrement by any finite multiple of its own one-step decrease. Coordinate selection and coordinate averaging cannot repair this example. This does **not** refute (2.1) or a global amortized rank estimate; it refutes the proposed local induction mechanism. The exact checker verifies every coordinate separately.

## 7. Executed checks and remaining task

`python3 verify_addendum.py --output addendum_verification.json` uses only the Python standard library and the included standard-library `verify_continuation.py`. It was executed after adding the all-coordinate witness and produced PASS. It verifies:

- the exact influence-preserving compression witness;
- all four rank-budget obstruction coordinates, including the rational lower bound on their entropy decrement;
- 278 Boolean tables in dimensions zero through three for R=0 iff character, R<=Q<=I, and 6,280 pointwise restriction-monotonicity comparisons;
- 22,760 composition parameter cases and 269,824 pointwise rank-and-flag identities. The binary-gate families with one- or two-bit children and the ternary-gate family with one-bit children are exhaustive as specified in the JSON; the additional 1,000 ternary/two-bit-child cases are reproducible samples, not exhaustive.

`explore_curvature.py` separately exhausts truth tables modulo global negation through dimension four and samples 500 functions per dimension five through seven. It uses floating entropy and exact ranks. Its largest observed H/R was the five-variable one-point value above; it provides no universal bound.

`explore_rank_restriction.py` found the symmetric all-coordinate counterexample after 417 parameter cases, before reaching its planned larger dimensions. Its `Infinity` output is a diagnostic for a positive entropy loss divided by exactly zero rank decrease, not a claim that a Boolean function has infinite entropy. The subsequent exact certificate is authoritative.

The useful surviving results are the exact matrix composition law and bounded monotone physical resources. The missing step is a global entropy estimate, or a nonlocal allocation theorem that can use later rank decreases to pay earlier entropy losses. No such estimate is established here. The main report's improved derivative bound also still lacks the necessary summable allocation. Thus neither route is being represented as a completed proof of full FEI.

The broad physical restriction framework is already present in Gonzalez--MacManus--Pereyra, arXiv:2606.00246v2, and in the repository's hereditary-erasure work. The rank definitions and identities above are supplied with proofs, but a bounded search did not establish publication priority. They are not to be conflated with previously studied global Fourier rank. No older valid theorem, schedule, ownership record, or native finite-dimension metric was changed.
