# A convex quartic coupling cost and a weak-block extension theorem

Date: 2026-09-15. Root creative work, not an agent execution. This proves a restricted composition theorem, not the full Lyons conjecture. Historical novelty has not been investigated.

## Statement

Partition the ground set into blocks E_1,...,E_m and let D=direct_sum D_a be a strict Hermitian contraction. Suppose the occupation entropy Hessian at each D_a is negative definite on all Hermitian block directions. Singleton blocks are allowed.

There is a finite union of proper complex linear hyperplanes in the space of off-block matrices such that, for every fixed Hermitian off-block V outside that union, the entropy Hessian at D+epsilon V is negative definite in **every Hermitian direction** for all sufficiently small positive epsilon. The proof constructs the excluded hyperplanes explicitly from conditional Fisher features.

Thus proven strict blocks can be connected by sufficiently weak generic correlations, while retaining full-Hessian negativity. This is stronger than the automatic radial fourth-order entropy loss at independence. The key fact is that the entire leading coupling cost is a convex quartic form, with a positive definite Hessian at generic couplings.

## 1. Conditional Fisher information is a positive rank-one frame

Fix an ordering of the sites in a block and reveal its occupation indicators successively. At a history h let pi_h>0 be its probability and q_h in (0,1) the conditional probability of the next site j.

If R is the revealed set and J is its absent subset, put N=D_R-I_J. Conditioning gives

\[
q_h=D_{jj}-D_{jR}N^{-1}D_{Rj}.
\]

For any Hermitian perturbation A, differentiation gives

\[
Dq_h[A]=w_h^*Aw_h,
\qquad w_h|_R=-N^{-1}D_{Rj},\quad (w_h)_j=1,
\]

with zeros on later sites. The score of the joint law is the sum of its conditional Bernoulli scores. Their martingale differences are orthogonal. Therefore the exact Fisher identity is

\[
\mathcal I_D(A)=\sum_h\omega_h(w_h^*Aw_h)^2,
\qquad \omega_h={\pi_h\over q_h(1-q_h)}>0.
\tag{1}
\]

This is a finite identity, not a lower-bound truncation. Selecting one history for each reveal depth gives a triangular set of vectors with diagonal entries one, hence a basis of the block vector space.

## 2. Expand the law around independent blocks

For a block atom S_a, write

\[
N_a(S_a)=D_a-I_{E_a\setminus S_a},\qquad
R_a(S_a)=N_a(S_a)^{-1}.
\]

These matrices are Hermitian and invertible, although they need not be positive. The block atom probability is the signed determinant of N_a. Differentiating the total probability in arbitrary Hermitian directions yields

\[
\mathbb E R_a=0,\qquad
\mathbb E(\operatorname{tr}R_a A)^2=\mathcal I_{D_a}(A).
\tag{2}
\]

Let p_0 be the product of the block laws. For a Hermitian off-block matrix V with blocks V_ab, expansion of the signed determinant gives

\[
{p_{D+\epsilon V}(S)\over p_0(S)}
=1+\epsilon^2 r_2(S)+O(\epsilon^3),
\qquad
r_2(S)=-\sum_{a<b}\operatorname{tr}
\bigl(R_aV_{ab}R_bV_{ab}^*\bigr).
\tag{3}
\]

The first derivative vanishes because V has zero diagonal blocks. Formula (3) follows from det(I+epsilon RV)=1-epsilon^2 tr((RV)^2)/2+O(epsilon^3); the trace sums each unordered block pair twice. The finite atom set and strictness make the expansion uniform in a neighborhood of D.

Every block marginal stays fixed as epsilon varies. Consequently the entropy loss equals the relative entropy to the product law:

\[
\sum_a H(D_a)-H(D+\epsilon V)
=D(p_{D+\epsilon V}\Vert p_0)
={\epsilon^4\over2}\mathbb E r_2^2+O(\epsilon^5).
\tag{4}
\]

The absence of linear and quadratic entropy-loss terms follows from the law expansion and normalization; it is not an assumption of curvature positivity.

## 3. The quartic term is a sum of fourth powers of linear forms

Distinct unordered block-pair summands in r_2 are orthogonal under p_0. Indeed, a block belonging to just one of the two pairs appears linearly in R_a, whose expectation is zero by (2). Thus

\[
\mathbb E r_2^2=\sum_{a<b}
\mathbb E\left[\operatorname{tr}
(R_aV_{ab}R_bV_{ab}^*)\right]^2.
\]

Apply the Fisher identity (1) first in block b to the Hermitian test matrix V_ab^* R_a V_ab, and then in block a to the rank-one matrix V_ab z_g z_g^* V_ab^*. This gives the exact quartic identity

\[
\boxed{
Q(V):=\mathbb E r_2^2
=\sum_{a<b}\sum_{h,g}
\omega_{a,h}\omega_{b,g}
|w_{a,h}^*V_{ab}w_{b,g}|^4.}
\tag{5}
\]

Every coefficient is positive. In particular Q is convex as a real function of all complex off-block entries. This conclusion would not follow just from its being a squared norm of quadratic functions; the rank-one Fisher representation is essential.

For z,u in C,

\[
D^2\left({|z|^4\over2}\right)[u,u]
=2|z|^2|u|^2+4\{\operatorname{Re}(\bar z u)\}^2.
\tag{6}
\]

Choose basis histories w_a,1,...,w_a,n_a in each block as in Section 1. For each a<b require

\[
w_{a,r}^*V_{ab}w_{b,s}\ne0
\quad\text{for every selected }r,s.
\tag{7}
\]

Each forbidden equality is a proper complex linear hyperplane. Their finite union has empty interior and Lebesgue measure zero. These are the promised explicit genericity conditions.

Since the two basis matrices are invertible, the selected linear map V_ab -> (w_a,r^* V_ab w_b,s)_rs is invertible. Equations (5)--(7) therefore imply a constant c(V,D)>0 with

\[
D^2(Q/2)(V)[W,W]\ge c\|W\|_F^2
\tag{8}
\]

for all Hermitian off-block W. For an explicit choice let W_a have the selected vectors as columns, s_a=sigma_min(W_a)>0, and

\[
c=\min_{a<b}\left[
s_a^2s_b^2\min_{r,s}
\omega_{a,r}\omega_{b,s}|w_{a,r}^*V_{ab}w_{b,s}|^2\right].
\]

The Frobenius norm on Hermitian off-block matrices counts each rectangular pair twice, matching this constant in (6).

## 4. Full-Hessian control, including perturbations within the blocks

Permit the diagonal blocks to vary in a small neighborhood U of D. Their atom laws and all coefficients above are real analytic, because every atom stays positive. Writing C for the collection of off-block entries, the block mutual information has a convergent local Taylor expansion

\[
I(U,C)={1\over2}Q_U(C)+O(\|C\|^5).
\tag{9}
\]

The remainder has the corresponding differentiated bounds: its second C derivative is O(||C||^3), mixed U,C derivative is O(||C||^4), and second U derivative is O(||C||^5). The leading quartic contributes O(||C||^2), O(||C||^3), and O(||C||^4), respectively. These follow termwise from the convergent analytic Taylor series on a smaller neighborhood.

By the assumed strictness of the component entropy Hessians there is gamma>0 such that their sum has curvature at most -gamma||T||_F^2 for diagonal-block T. At C=epsilon V, (8)--(9) and H(U,C)=sum H(U_a)-I(U,C) yield

\[
\begin{aligned}
D^2H(D+\epsilon V)[T+W,T+W]
\le{}&(-\gamma+O(\epsilon^4))\|T\|_F^2\\
&+O(\epsilon^3)\|T\|_F\|W\|_F\\
&+(-c\epsilon^2+O(\epsilon^3))\|W\|_F^2.
\end{aligned}
\tag{10}
\]

Young's inequality absorbs the mixed term into gamma||T||^2/4 plus O(epsilon^6)||W||^2. For sufficiently small positive epsilon, (10) is at most

\[
-{\gamma\over2}\|T\|_F^2
-{c\epsilon^2\over2}\|W\|_F^2<0
\]

unless T=W=0. Strict contraction also persists for small epsilon by spectral continuity. This proves the theorem.

## Consequences and limits

- Taking all blocks to be singletons recovers a weak dense-correlation region around any interior product kernel. Here Q(V)=sum_{i<j}|V_ij|^4/[d_i(1-d_i)d_j(1-d_j)]. C018 is independently developing this product case and quantitative corridors.
- Any already proved connected strict three-site bases from C008, C010, or other reports can be used as blocks, producing families in arbitrarily large dimension with substantial internal correlations and weak generic links.
- For pure off-block lines, (4)--(5) also gives local radial strict concavity for every nonzero V, even without (7). The basis features ensure Q(V)>0. This radial statement is weaker than the all-direction conclusion, which here uses (7) and strict component Hessians.
- No universal size for epsilon is claimed by the analytic argument. A quantitative remainder bound, degenerate feature couplings, or extension to large coupling requires further work. Independent blocks themselves have cross-block Hessian null directions; no unjustified strictness is assigned there.
