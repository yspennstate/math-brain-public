# Critical extinction does not imply convergence of radius conditioning

## Proposition

There is an infinite locally finite tree T, with a distinguished vertex o and maximum degree three, such that Bernoulli bond percolation satisfies

\[
p_c(T)=\tfrac12,\qquad \mathbb P_{1/2}(\text{there is an infinite open cluster})=0,
\]

but the laws

\[
\mathbb P_{1/2}(\,\cdot\mid o\leftrightarrow S_T(o,n))
\]

do not converge on cylinder events. Here S_T(o,n) is the graph-distance sphere. For a specified edge e incident to o, its conditional opening probability has subsequential limits 1/2 and 1.

This proposition concerns a nontransitive tree. It does not answer the existence question on the cubic lattice. It rules out a general implication from bounded degree and critical extinction alone.

## 1. Survival estimates for a spherically symmetric tree

Let b_i in {1,2} be the number of children of every vertex in generation i−1. Write Z_n for the number of vertices of generation n connected to the root, Z_0=1, and

\[
m_i=p b_i,\qquad M_0=1,\qquad M_n=\prod_{i=1}^n m_i.
\]

Conditional on Z_(i−1), the variable Z_i has the binomial distribution with b_i Z_(i−1) trials and success probability p. Consequently

\[
\mathbb E Z_n=M_n
\]

and

\[
\mathbb E[Z_i^2\mid Z_{i-1}]
=m_i^2 Z_{i-1}^2+b_i p(1-p)Z_{i-1}.
\]

After taking expectations and dividing by M_i^2, this gives

\[
\frac{\mathbb E Z_i^2}{M_i^2}
=\frac{\mathbb E Z_{i-1}^2}{M_{i-1}^2}+\frac{1-p}{M_i}.
\]

Iteration yields the exact identity

\[
\frac{\mathbb E Z_n^2}{M_n^2}
=1+(1-p)\sum_{i=1}^n M_i^{-1}.                 \tag{1}
\]

Cauchy–Schwarz, applied to Z_n times the indicator of {Z_n>0}, implies

\[
q(n):=\mathbb P_p(Z_n>0)
\geq \frac{(\mathbb E Z_n)^2}{\mathbb E Z_n^2}
=\left(1+(1-p)\sum_{i=1}^n M_i^{-1}\right)^{-1}. \tag{2}
\]

At p=1/2, put

\[
D(n)=\#\{i\leq n:b_i=1\}.
\]

Then M_n=2^(−D(n)) is nonincreasing and at most one. From (2),

\[
q(n)\geq\frac{M_n}{M_n+n/2}\geq\frac{M_n}{n+1}. \tag{3}
\]

There is also a useful upper bound when the last L generations are binary. Let s_L be the critical survival probability for L generations of the full binary tree. Independence of the two descendant subtrees gives

\[
s_0=1,\qquad s_{L+1}=s_L-s_L^2/4.
\]

For any 0<s<=1,

\[
\frac1{s-s^2/4}-\frac1s=\frac1{4(1-s/4)}\geq\frac14.
\]

Thus s_L<=4/(L+4). Conditional on the open generation at level n−L, a union bound over its vertices gives

\[
q(n)\leq M_{n-L}s_L
\leq\frac{4M_n}{L+4},                         \tag{4}
\]

where M_(n−L)=M_n because all the last L offspring means equal one. In particular, if L>=n/2,

\[
\frac{M_n}{n+1}\leq q(n)\leq\frac{8M_n}{n}.    \tag{5}
\]

All these statements concern a finite number of generations and require no assumption about an infinite cluster.

## 2. Definition of the two branches

Set

\[
N_0=0,\qquad N_k=2^{k^2+10}\quad(k\geq1),
\]

and define the finite intervals of positive integers

\[
I_k=\{N_{k-1}+1,\ldots,N_{k-1}+2k-1\}.
\]

For branch A, set b_i=1 on I_k when k is odd, and b_i=2 elsewhere. For branch B, set b_i=1 on I_k when k is even, and b_i=2 elsewhere. These prescriptions define two infinite rooted spherically symmetric trees. Attach their roots a and b to a new vertex o by edges e_A and e_B. The resulting tree T has maximum degree three.

The intervals I_k are disjoint. Indeed,

\[
N_{k-1}+2k-1\leq N_k/2.                       \tag{6}
\]

For k=1 this is 1<=1024. For k>=2, N_k/N_(k−1)=2^(2k−1)>=8, so N_(k−1)<=N_k/8. Also 2k−1<=N_k/8: for example, 2^(k^2+7)>=2^k>=2k−1 for k>=2, the last inequality following by induction. Summing these two bounds proves the stronger inequality N_(k−1)+2k−1<=N_k/4 for k>=2. In particular, after I_k both branches have at least N_k/2 consecutive binary generations before level N_k.

Write D_A and D_B for the suppressed-level counts. At n=N_k,

\[
D_A(N_k)+D_B(N_k)=\sum_{j=1}^k(2j-1)=k^2
\]

and

\[
D_A(N_k)-D_B(N_k)
=\sum_{j=1}^k(-1)^{j+1}(2j-1)=(-1)^{k+1}k.    \tag{7}
\]

For the second identity, the alternating sum is 1 at k=1; adding the next signed odd number changes (−1)^(k+1)k into (−1)^(k+2)(k+1). Equivalently,

\[
D_A(N_k)=\frac{k^2+(-1)^{k+1}k}{2},\qquad
D_B(N_k)=\frac{k^2-(-1)^{k+1}k}{2}.             \tag{8}
\]

For N_(k−1)<n<=N_k, each suppressed-level count is at most k^2. For k>=2,

\[
0\leq\frac{D_s(n)}n
\leq\frac{k^2}{2^{(k-1)^2+10}}\longrightarrow0,
\qquad s\in\{A,B\}.                          \tag{9}
\]

Both counts tend to infinity, since each branch receives infinitely many nonempty intervals.

## 3. Critical parameter and extinction

For p<=1/2, the generation mean in either branch is

\[
M_n(p)=(2p)^n2^{-D_s(n)}\leq2^{-D_s(n)}\longrightarrow0.
\]

Markov's inequality gives q_s(n)<=M_n(p), so the probability that a branch root has an infinite open descendant path is zero. The same conclusion holds for a vertex at any fixed generation j: its descendant generation mean at level n is M_n(p)/M_j(p), which tends to zero for p>0. At p=0 extinction is immediate.

If an open component of T is infinite, its vertex closest to o exists and has an infinite descendant component. Each generation is finite. An infinite descendant component therefore reaches arbitrarily deep generations. The probability of this for any specified vertex is zero by the preceding paragraph. A countable union over vertices proves absence of any infinite open cluster at p<=1/2.

For p>1/2, (9) implies

\[
\log M_n(p)=n\log(2p)-D_s(n)\log2.
\]

Hence M_n(p)>=exp(c_p n) for all sufficiently large n, for some c_p>0. The series sum_(n>=1) M_n(p)^(−1) converges. By (2), q_s(n) is bounded below by a positive constant independent of n. The events {Z_n>0} decrease, so continuity of probability gives positive probability of connection to arbitrarily large generations. On a locally finite tree this is equivalent to an infinite open descendant path: recursively choose a child with descendants at arbitrarily large depths. At each choice at least one such child exists because there are finitely many children.

The root o therefore percolates with positive probability for every p>1/2, since its edge to either branch is open with probability p>0 independently of that branch. Together with extinction at p<=1/2, this proves p_c(T)=1/2 and theta_T(1/2)=0, as well as absence of every infinite open cluster at criticality.

## 4. Oscillation of a cylinder probability

All probabilities in this section are at p=1/2. Write q_A(n) and q_B(n) for the branch-root survival probabilities to generation n. At n=N_k, (5), (6), and (7) imply, for odd k,

\[
\frac{q_A(N_k)}{q_B(N_k)}
\leq 8\frac{N_k+1}{N_k}\,2^{D_B(N_k)-D_A(N_k)}
\leq16\,2^{-k}.                              \tag{10}
\]

For even k the same estimate holds with A and B interchanged. Thus A is the less likely surviving branch at odd stages, and B at even stages.

Let E_(n+1)={o connects to S_T(o,n+1)}, and put

\[
u=\tfrac12 q_A(n),\qquad v=\tfrac12 q_B(n).
\]

The two branch-success events use disjoint edges, so they are independent and

\[
\mathbb P(E_{n+1})=u+v-uv.
\]

The event that e_A is closed and E_(n+1) occurs requires the B branch to succeed; its probability is v/2. Therefore the exact cylinder probability is

\[
H(n):=\mathbb P(e_A\text{ open}\mid E_{n+1})
=1-\frac{v/2}{u+v-uv}.                        \tag{11}
\]

For odd k, set r=u/v. By (10), 0<r<=16*2^(−k), and 0<=u<=r, since v<=1. Equation (11) gives

\[
H(N_k)-\tfrac12
=\frac{r-u}{2(1+r-u)}.
\]

Consequently

\[
\tfrac12\leq H(N_k)\leq\tfrac12+8\,2^{-k}
\quad(k\text{ odd}).                         \tag{12}
\]

For even k, put t=v/u<=16*2^(−k). Since u<=1, one has t>=v. Again by (11),

\[
0\leq1-H(N_k)=\frac{t}{2(1+t-v)}\leq8\,2^{-k}.
                                                               \tag{13}
\]

It follows that

\[
\lim_{j\to\infty}H(N_{2j-1})=\tfrac12,
\qquad
\lim_{j\to\infty}H(N_{2j})=1.
\]

The conditioning radii are N_(2j−1)+1 and N_(2j)+1. Both tend to infinity, and {e_A is open} depends on one edge. Thus the conditional laws fail to converge on cylinder events.

## 5. A second derivation of the survival bounds

Fix n and let t_i be the probability that a specified vertex of generation i connects to generation n through descendants; thus t_n=1. At p=1/2,

\[
t_{i-1}=t_i/2\quad(b_i=1),\qquad
t_{i-1}=t_i-t_i^2/4\quad(b_i=2).
\]

Writing r_i=1/t_i, the corresponding identities are

\[
r_{i-1}=r_i/m_i+c_i,
\]

where c_i=0 for b_i=1, while

\[
c_i=\frac1{4(1-t_i/4)}\in[1/4,1/3]
\quad(b_i=2).
\]

Successive substitution gives the exact formula

\[
\frac1{q(n)}=\frac1{M_n}+\sum_{i=1}^n\frac{c_i}{M_{i-1}}.       \tag{14}
\]

Because M_(i−1)>=M_n and c_i<=1/3, (14) implies

\[
q(n)\geq\frac{M_n}{1+n/3}\geq\frac{M_n}{n+1}.
\]

If the last L>=n/2 generations are binary, their terms in (14) contribute at least L/(4M_n). Thus q(n)<=4M_n/L<=8M_n/n. This proves the same estimates (5) without using the second-moment lower bound or the union-bound upper bound.

## Relation to the lattice problem

The example shows that critical extinction and bounded degree do not prevent different arms from dominating at different radii. A proof of the cubic-lattice IIC limit needs additional information that excludes such oscillation. This tree lacks transitivity and the uniqueness hypothesis in a supercritical interval used by Basu and Sapozhnikov. To see the latter failure, fix 1/2<p<1 and take the two children of the root of branch B (its first generation is binary). Each child has positive probability of an infinite open descendant path by the argument in Section 3 applied after that finite initial segment. Closing the two edges to their parent and requiring both descendant subtrees to survive gives two distinct infinite open clusters with positive probability, by independence. The proposition therefore does not contradict their theorem. The conditioning uses graph-distance spheres, not cubic boxes, and the tree is not a nearest-neighbor subgraph of the cubic lattice: a branch has 2^{n-D_s(n)} vertices at generation n, which grows exponentially by (9), whereas a cubic-lattice ball contains only (2n+1)^3 vertices. No claim of novelty for this obstruction is made.
