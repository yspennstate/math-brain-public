# First-step denominator bounds at a diluted Ising barrier

## 1. Assumptions and statement

On a finite interval Lambda with open ends let

\[
 H_0=\sum_i h_iZ_i+\sum_i\xi_i g_iX_i
       +\sum_{i,i+1\in\Lambda}J_iZ_iZ_{i+1}.
\]

The xi_i are iid Bernoulli(p), 0<p<1. The h_i are iid with a density bounded
by rho<infinity, independent of xi and of the finite real coefficients g,J.
The coefficients g,J can be deterministic or random, independently of h and
xi. No bound on their sizes is needed. All probabilities below at a specified
site f are conditional on xi_f=0.

Let a and b be the numbers of consecutive active sites immediately left and
right of f, stopping at a frozen site or the physical end. Put m=a+b. In the
controlled block eigenbasis of H_0, consider every pair of local block
eigenstates in the two Z_f sectors, with the same outer frozen assignment.
Define R_f(delta) to mean that at least one difference (9) has absolute value
less than delta. This conservative event includes pairs with zero X_f matrix
element and covers every actual transition caused by X_f. For delta>0,

\[
 \mathbb P(R_f(\delta)\mid \xi,\{h_i:i\ne f\},g,J)
 \le \min\{1,4\rho\delta\,4^m\}.                    \tag{1}
\]

The conditioning includes xi_f=0. This is a bound for all relevant local
state pairs, not for a fixed chosen eigenstate and not for all spacings of H_0.

For t>0 define

\[
 F_p(t)=(1-p)^2\sum_{k=0}^\infty(k+1)p^k\min\{1,t4^k\}.
                                                               \tag{2}
\]

Uniformly in Lambda and f,

\[
 \mathbb P(R_f(\delta)\mid\xi_f=0)\le F_p(4\rho\delta).
                                                               \tag{3}
\]

If 0<t<1 and K=floor(log(1/t)/log 4), this majorant has the exact formula

\[
 F_p(t)=(1-p)^2t\sum_{k=0}^{K}(k+1)(4p)^k
       +p^{K+1}\big[(K+2)-(K+1)p\big].              \tag{4}
\]

For t>=1 it equals 1. In particular,

\[
 F_p(t)\le t\left(\frac{1-p}{1-4p}\right)^2
       \quad(0<p<1/4),                            \tag{5}
\]

and, for every 0<q<=1 satisfying p4^q<1,

\[
 F_p(t)\le t^q\left(\frac{1-p}{1-p4^q}\right)^2.   \tag{6}
\]

Thus for every fixed p<1 the first-step all-state resonance probability tends
to zero with delta, uniformly in chain length. More precisely, as t decreases
to zero,

\[
 F_p(t)=
 \begin{cases}
 O_p(t),&p<1/4,\\
 O(t[1+\log(1/t)]^2),&p=1/4,\\
 O_p(t^\alpha[1+\log(1/t)]),&p>1/4,
 \end{cases}
 \qquad \alpha=\dfrac{\log(1/p)}{\log4}.             \tag{7}
\]

These estimates concern the first denominators at the exact-barrier model.
They assert neither a convergent diagonalization after adding transverse
terms at all barriers nor independence of different resonance events.

## 2. The local Hilbert space and the spectators

The adjacent active intervals are B_-=[f-a,f-1] and B_+=[f+1,f+b], omitting
empty intervals. Let C=[f-a,f+b]. A site immediately outside C, when it
exists, is frozen. There are at most two such sites. Write eta for their
Z-spin values; at most four assignments occur. All other frozen spins and
all active blocks outside C will be called spectators.

For fixed eta and Z_f=s in {+1,-1}, define K_s(eta) on the m active spins
B_- union B_+. Include the on-site and transverse terms of these spins,
their internal bonds, and their bonds to f with Z_f replaced by s. Include
their bonds to eta. If a=0, include the scalar s J_{f-1} eta_{f-1} when
f-1 exists. If b=0, include s J_f eta_{f+1} when f+1 exists. These last
rules account for bonds from f directly to a frozen neighbor. Omit missing
bonds at physical boundaries. For m=0 the active space is \(\mathbb C\) and K_s is
a scalar. Do not include h_f s in K_s.

In the sector of all frozen spins the Hamiltonian therefore has the form

\[
 E_{\rm out}+s h_f+K_s(\eta),                       \tag{8}
\]

where the spectator operator or spectator eigenvalue E_out is unchanged by
flipping f. In particular K_s does not depend on h_f.

To justify which states are connected, choose the earlier controlled
diagonalizer U as a product of gates, one on each active block and its frozen
boundary controls. Those gates commute: distinct target intervals are
disjoint and shared controls are diagonal projectors. Every gate except
those on B_- and B_+ commutes with X_f. Commuting gates can be cancelled
in U*X_f U. The remaining two gates preserve every frozen spin, and X_f
flips only f. Consequently U*X_f U changes only f and the active labels in
B_- and B_+, preserves eta, and preserves all spectators. This also holds
when one or both adjacent intervals are empty.

Let lambda_u^s(eta), 1<=u<=d=2^m, be the eigenvalues of K_s, counted with
multiplicity. Choose the eigenvectors independently of h_f, possible since
K_s is independent of h_f. Every energy difference for a flip from s=-1
to s=+1 is

\[
 D_{\eta,u,v}=2h_f+\lambda_u^+(\eta)-\lambda_v^-(\eta).
                                                               \tag{9}
\]

The reverse flip gives the negatives of these same numbers, so does not
double their count. Degeneracies within K_s do not affect (9). States with
the same spectator labels have the spectator energy cancel exactly. There
are at most 4d^2=4*4^m numbers in (9). The count has no factor depending on
the spectator Hilbert-space dimension.

## 3. Conditional spectral averaging

Condition on xi, all fields except h_f, and the coefficients. Every offset
c=lambda_u^+(eta)-lambda_v^-(eta) in (9) is now fixed. The inequality
|2h_f+c|<delta restricts h_f to an interval of length delta, since its
endpoints are (-c-delta)/2 and (-c+delta)/2. The conditional density bound
therefore gives

\[
 \mathbb P(|2h_f+c|<\delta\mid\hbox{conditioned data})\le\rho\delta.
                                                               \tag{10}
\]

A union bound over the at most 4*4^m intervals, capped at one, proves (1).
No assertion about independence among these intervals is used.

An alternative way to count the same intervals is to regard
K_+(eta) tensor I - I tensor K_-(eta)^T as a d^2-dimensional Hermitian
matrix. Its eigenvalues are all the differences lambda_u^+-lambda_v^-.
The union of the h_f intervals centered at minus half these eigenvalues,
over eta, has total length at most 4d^2 delta. Integrating its indicator
against the density gives the same constant in (1).

## 4. Averaging the two adjacent lengths

Conditioning on xi_f=0 leaves the indicators on the two sides independent.
On the infinite line, the adjacent lengths A and B have

\[
 \mathbb P(A=n)=\mathbb P(B=n)=(1-p)p^n,\quad n>=0.
\]

Indeed a run of length n specifies n active sites followed by a frozen
site. The two runs use disjoint sets of indicators. Hence

\[
 \mathbb P(A+B=k)=(k+1)(1-p)^2p^k.                  \tag{11}
\]

For a finite chain, extend its indicators independently beyond each physical
end. Its observed a,b are the corresponding infinite run lengths truncated
at the ends. Therefore a+b<=A+B under this coupling. The right side of (1)
is increasing in m. Averaging (1), then using (11), proves (2)--(3), including
sites at the physical ends and volumes containing no other frozen site.

For 0<t<1, t4^k<=1 exactly when k<=K. Splitting (2) at K yields (4), since
for any n>=0,

\[
 \begin{split}
 (1-p)^2\sum_{k=n}^\infty(k+1)p^k
 &=p^n(1-p)^2\sum_{j=0}^\infty(j+n+1)p^j\\
 &=p^n[(n+1)-np].
 \end{split}                                                   \tag{12}
\]

Here sum p^j=1/(1-p) and sum j p^j=p/(1-p)^2; the second follows by
termwise differentiation of the absolutely convergent geometric series.
Setting n=K+1 in (12) gives the tail in (4). If p<1/4, replacing
min{1,t4^k} by t4^k in (2) and summing gives (5).

For 0<q<=1 and x>=0, min{1,x}<=x^q: for x<=1, x<=x^q, and for x>=1,
1<=x^q. Apply this to (2). The resulting geometric derivative sum converges
when p4^q<1 and equals (6). For every p<1 there is a positive such q.

For completeness, (7) follows directly from (4). At p=1/4 the finite sum
is (K+1)(K+2)/2; the tail is at most t(K+2), because
p^{K+1}=4^{-(K+1)}<=t and (K+2)-(K+1)p<=K+2. If p>1/4, put r=4p>1.
Then

\[
 \sum_{k=0}^{K}(k+1)r^k
 \le (K+1)\frac{r^{K+1}}{r-1}.
\]

Since 4^K<=1/t<4^{K+1}, one has t4^{K+1}<=4. The finite part in (4)
is at most 4(1-p)^2(K+1)p^{K+1}/(4p-1). The tail is at most
(K+2)p^{K+1}. Writing p=4^(-alpha), the strict inequality 1/t<4^{K+1}
gives p^{K+1}<=t^alpha. Finally K+2 is at most
2+log(1/t)/log4. This proves (7); the p<1/4 case is (5).

## 5. Spatial extent and the limitation of the estimate

All these denominators are determined by h_f, the two adjacent active
blocks, and at most their two outer frozen controls. Their support is
contained in the interval obtained by padding C by one site on each side,
intersected with Lambda. Its radius about f is at most max(a,b)+1. For every
integer r>=1,

\[
 \mathbb P(\max(a,b)+1>r\mid\xi_f=0)
 \le 2p^r-p^{2r},                                  \tag{13}
\]

because A>=r and B>=r have probability p^r and are independent. The bound
is an equality for this numerical envelope on the infinite chain; physical
support can be smaller at the ends. In particular, the union of R_f(delta)
and this exceptional-radius event has probability at most
F_p(4rho delta)+2p^r-p^{2r}. This is a fixed-site bound. Requiring no
resonance at any barrier of a volume can introduce a factor proportional
to its length.

Formula (5) shows that the direct first moment of the pair count is finite
when p<1/4. Its divergence for p>=1/4 is a failure of that uncapped bound,
not a localization threshold: (4) and (6) still tend to zero for every p<1.
Repeated rotations change the denominators and may remove their affine
dependence on an unused independent field. Neighboring resonance events
also share blocks and fields. No estimate here controls those later steps,
their correlations, or the norm of a full diagonalizing transformation.
