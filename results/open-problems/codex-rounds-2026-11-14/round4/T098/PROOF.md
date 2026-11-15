# A first rotation at a diluted Ising barrier

## 1. Statement

Let Lambda be a finite interval with open ends, and let

\[
 H_0=\sum_i h_iZ_i+\sum_i\xi_i g_iX_i
       +\sum_{i,i+1\in\Lambda}J_iZ_iZ_{i+1}.
\]

The indicators are iid Bernoulli(p), with 0<p<1. The longitudinal fields
are iid with density bounded by rho, independently of the indicators and
of g,J. The real coefficients g,J are finite and otherwise unrestricted.
Fix a frozen site f, that is, xi_f=0. All probabilities concerning f below
are conditional on this event. Add a real transverse term
V_f=epsilon_f X_f; epsilon_f is fixed.

Let a,b be the adjacent active-run lengths and m=a+b. Set
C_f=[f-a,f+b], and let I_f be C_f together with its existing frozen
neighbors immediately outside it. For each assignment eta to those at most
two neighbors and each Z_f sector s=+1,-1, let K_s(eta) be the operator on
the m active spins which includes their on-site terms, all their bonds,
and their bonds to the fixed controls s,eta. If a side is empty, its bond
from f to an outer control is included as a scalar. Do not include s h_f.
Write its eigenvalues, with multiplicities, as lambda_u^s(eta).

For delta>0, define the good event

\[
 G_f(\delta)=\left\{
 |2h_f+\lambda_u^+(\eta)-\lambda_v^-(\eta)|\ge\delta
 \text{ for every }\eta,u,v\right\}.
                                                        \tag{1}
\]

Put C_*=sqrt(8/3). On G_f there is an anti-Hermitian A_f, supported in
I_f and diagonal on the outer frozen controls, such that

\[
 [H_0,A_f]=V_f,\qquad
 \{A_f,Z_f\}=0,\qquad
 \|A_f\|\le a_f:=C_*\frac{|\epsilon_f|}{\delta}.       \tag{2}
\]

The constant is independent of m, Lambda, all eigenstate labels, and all
other gaps, including gaps within a fixed Z_f sector. No ordering of the
two sector spectra is assumed. Set A_f=0 off G_f; the norm and support
bounds then hold everywhere, and the commutator identity in (2) holds
with V_f replaced by 1_{G_f} V_f.

On G_f the exact conjugation satisfies

\[
 e^{A_f}(H_0+V_f)e^{-A_f}=H_0+Q_f+T_f,
 \qquad Q_f=\tfrac12[A_f,V_f],                       \tag{3}
\]
\[
 \|Q_f+T_f\|\le a_f|\epsilon_f|,
 \qquad \|T_f\|\le\tfrac43 a_f^2|\epsilon_f|.       \tag{4}
\]

These are local remainder bounds uniform in the chain length, even when
the coefficients outside I_f are large. In addition [Q_f,Z_f]=0.
Consequently the Hermitian involution

\[
 \widetilde Z_f=e^{-A_f}Z_fe^{A_f}
\]

is supported in I_f and, on G_f, obeys

\[
 \|\widetilde Z_f-Z_f\|\le\min(2,2a_f),\qquad
 \|[H_0+V_f,\widetilde Z_f]\|
       \le\tfrac83 a_f^2|\epsilon_f|.               \tag{5}
\]

The probability of failure of these identities is bounded by the earlier
capped resonance estimate

\[
 \mathbb P(G_f^c\mid\xi_f=0)\le F_p(4\rho\delta),
 \quad
 F_p(t)=(1-p)^2\sum_{k\ge0}(k+1)p^k\min(1,t4^k).   \tag{6}
\]

For every integer r>=1 the numerical support envelope has

\[
 \mathbb P\bigl(\max(a,b)+1>r\mid\xi_f=0\bigr)
       \le 2p^r-p^{2r}.                             \tag{7}
\]

Thus with conditional probability at least
1-F_p(4rho delta)-2p^r+p^(2r), (2)--(5) hold and A_f, Q_f, T_f and
the dressed spin are supported within distance r of f. This is a fixed-site assertion, not a
claim that all barriers of an arbitrarily long chain are good.

## 2. Audit of the earlier resonance estimate

Fix the indicators, all fields except h_f, and g,J. Conditional on all frozen
spins, the active blocks are disjoint quantum systems. Their diagonalizers
may be chosen controlled by their frozen boundary spins; any overlap of
two such gates is diagonal on shared controls, so the gates commute.
A flip of f therefore changes only its two adjacent blocks. All spectator
energies cancel. The local energies in its two sectors are

\[
 E_{\rm out}+s h_f+\lambda_u^s(\eta),\quad
 1\le u\le d=2^m.
\]

There are at most four eta assignments and d^2 forward differences per
assignment. Reverse differences only change the sign. Each forbidden
inequality |2h_f+c|<delta specifies an interval of length delta in h_f.
Its probability is at most rho delta. The union bound gives
min(1,4rho delta 4^m); this also covers zero matrix elements conservatively.

On the infinite line, a and b are independent with law (1-p)p^j, j>=0.
Their sum has law (k+1)(1-p)^2p^k. At finite ends the observed lengths
are truncated versions of independent infinite runs. Since the conditional
majorant increases in m, this proves (6) uniformly in Lambda.
For 0<t<1 and K=floor(log_4(1/t)), summing the capped tail gives

\[
 F_p(t)=(1-p)^2t\sum_{k=0}^{K}(k+1)(4p)^k
       +p^{K+1}[(K+2)-(K+1)p].                     \tag{8}
\]

Indeed sum_{k>=n}(k+1)(1-p)^2p^k=p^n[(n+1)-np], obtained by
differentiating the geometric series. This reproduces the earlier formula.
For any 0<q<=1 with p4^q<1, min(1,x)<=x^q gives

\[
 F_p(t)\le t^q\left(\frac{1-p}{1-p4^q}\right)^2,
\]

so (6) tends to zero with delta for every fixed p<1. Splitting (8) also
recovers O_p(t), O(t log^2(1/t)), and O_p(t^alpha log(1/t)) for p<1/4,
p=1/4, and p>1/4 respectively, with alpha=log(1/p)/log 4.
Neither a physical threshold at p=1/4 nor spatial independence follows.

## 3. An operator-norm inverse for the commutator

Define the continuous odd function

\[
 f(x)=\begin{cases}x,&|x|\le1,\\1/x,&|x|>1.\end{cases}
\]

Its weak derivative is 1 on (-1,1) and -1/x^2 outside. There are no delta
terms at +/-1 because f is continuous there. Direct integration gives

\[
 \|f\|_2^2=2(1/3+1)=8/3,\qquad
 \|f'\|_2^2=2(1+1/3)=8/3.                          \tag{9}
\]

Use the Fourier convention
hat f(t)=(2pi)^(-1) integral f(x)e^(-itx) dx in the L2 sense.
Plancherel and the weak derivative identity give

\[
 \int(1+t^2)|\widehat f(t)|^2dt
       =\frac{\|f\|_2^2+\|f'\|_2^2}{2\pi}
       =\frac8{3\pi}.
\]

Cauchy--Schwarz, using integral (1+t^2)^(-1)dt=pi, yields

\[
 \|\widehat f\|_1\le\sqrt{8/3}=C_*.                \tag{10}
\]

The inverse integral is consequently continuous and equals f almost
everywhere by L2 inversion. Since f is continuous it equals f everywhere.
For f_delta(x)=delta^(-1)f(x/delta), scaling gives
hat f_delta(t)=hat f(delta t), hence
||hat f_delta||_1<=C_*/delta. Also f_delta(x)=1/x when |x|>=delta.

For finite-dimensional Hermitian K and arbitrary B, define the norm-convergent
integral

\[
 \Phi_{\delta,K}(B)=\int_{\mathbb R}\widehat f(\delta t)
                           e^{itK}B e^{-itK}\,dt.
\]

Unitary invariance and (10) prove

\[
 \|\Phi_{\delta,K}(B)\|\le(C_*/\delta)\|B\|.        \tag{11}
\]

In an eigenbasis of K with eigenvalues E_u its entries are
f_delta(E_u-E_v) B_uv, by the inverse formula. If B is Hermitian then
Phi(B) is anti-Hermitian, because f_delta is real and odd. Whenever
B_uv=0 or |E_u-E_v|>=delta for each pair, multiplication by E_u-E_v
shows [K,Phi(B)]=B. A diagonal entry of B must be zero in that assertion.
This argument allows degeneracies and interlaced spectra. It does not
replace a bound on individual entries by a dimension-dependent matrix norm.

## 4. Local construction

For fixed eta, define the operator on C_f

\[
 L_f(\eta)=\bigoplus_{s=+1,-1}\bigl(s h_f+K_s(\eta)\bigr).
\]

The two blocks refer to the physical Z_f sectors; the active coordinates
have the same product basis in both. The operator epsilon_f X_f connects
only opposite sectors. On G_f, define

\[
 A_f(\eta)=\Phi_{\delta,L_f(\eta)}(\epsilon_f X_f),
 \qquad
 A_f=\sum_\eta P_\eta A_f(\eta),                   \tag{12}
\]

where P_eta are the mutually orthogonal projectors onto the outer controls.
This sum acts only on I_f. Each summand is diagonal on the outer controls,
and (11) bounds its norm by a_f. The norm of the controlled direct sum is
the maximum, so there is no factor four in the operator norm.

Let H_c=sum_eta P_eta L_f(eta). Every term of H_0 not in H_c is either
outside I_f or acts on its outer controls only through Z. Such a term
commutes with A_f. In particular, an active spectator touching an outer
control causes no difficulty. Thus [H_0,A_f]=[H_c,A_f]=V_f by Section 3.
Evolution by each L_f preserves Z_f; since X_f flips Z_f, (12) anticommutes
with Z_f. This proves (2), including the empty-block and missing-boundary
cases. Set A_f=0 if (1) fails. All these choices are measurable finite-matrix
functions of the parameters on I_f and the indicator run lengths.

For the infinite-run dominating lengths, max(a,b)+1>r means a>=r or b>=r.
These independent events have probability p^r each. Finite ends only shorten
the lengths, proving (7). I_f is contained within radius max(a,b)+1 even
when an outer control is absent. The union bound proves the joint statement.

## 5. Exact remainder and an approximately conserved spin

Write A=A_f, V=V_f and assume G_f. Since [A,H_0]=-V, differentiation of
unitary conjugation, followed by the fundamental theorem of calculus, gives

\[
 e^A H_0e^{-A}=H_0-\int_0^1 e^{tA}Ve^{-tA}dt.
\]

Subtract this integral from e^AVe^(-A) and integrate the derivative of
e^(tA)Ve^(-tA). Interchanging two integrals over 0<=t<=u<=1 gives

\[
 R_f:=e^A(H_0+V)e^{-A}-H_0
       =\int_0^1 t\,e^{tA}[A,V]e^{-tA}dt.           \tag{13}
\]

The integrand is supported on I_f. Unitary conjugation is isometric, so
||R_f||<=||[A,V]||/2<=||A||||V||<=a_f|epsilon_f|.
Subtract Q_f=[A,V]/2 in (13). For any B,

\[
 e^{tA}Be^{-tA}-B=\int_0^t e^{uA}[A,B]e^{-uA}du,
\]

whose norm is at most t||[A,B]||. Taking B=[A,V] gives

\[
 \|T_f\|\le\int_0^1 t^2dt\,\|[A,[A,V]]\|
       \le\tfrac43\|A\|^2\|V\|.
\]

This proves (3)--(4) without requiring a_f<1. Their usefulness as a small
perturbation does require small a_f. Both A and V anticommute with Z_f,
so AV and VA commute with Z_f. Therefore [Q_f,Z_f]=0. Also [H_0,Z_f]=0.
Conjugating the commutator with the dressed spin reduces it to [T_f,Z_f],
of norm at most 2||T_f||. This proves the second bound in (5).
The first follows by integrating the derivative of e^(-tA)Z_fe^(tA),
bounded in norm by 2||A||, and by the triangle bound 2 for two norm-one
operators. Conjugation preserves Hermiticity and the equation Z_f^2=I.

The factors in these remainder estimates can be checked independently on
one spin. Take H_0=Z, V=2aX with a>0, and
A=a[[0,1],[-1,0]], so ||A||=a and ||V||=2a. Direct multiplication of
the two-by-two rotation matrix gives

\[
 R=(\cos(2a)-1+2a\sin(2a))Z
       +(2a\cos(2a)-\sin(2a))X,\qquad Q=2a^2Z.
\]

The X coefficient of T=R-Q is -(8/3)a^3+O(a^5), while its Z coefficient
is O(a^4). Therefore ||T||/(||A||^2||V||) tends to 4/3. Since only the
X coefficient contributes to [T,Z], the dressed-spin commutator divided
by ||A||^2||V|| tends to 8/3. Thus these two factors cannot be decreased
in estimates formulated in terms of the actual norm ||A||. This does not
assert optimality of the separate multiplier constant C_*.

For a specified f with |epsilon_f|<=epsilon, choose any delta tending to
zero with epsilon while epsilon/delta tends to zero. Equations (5)--(7)
then give a small local rotation and a small commutator outside an event
of probability tending to zero, together with the geometric spatial tail.
This concerns H_0+epsilon_f X_f only. Other transverse perturbations produce
additional commutators, described next.

## 6. What the first rotation produces at order two

For a finite collection of perturbed frozen sites, let V=sum_f V_f. Construct
A_f by (12) on G_f and set it to zero otherwise. At a fixed realization put
A=sum_f A_f, V_G=sum_{f:G_f}V_f, V_B=V-V_G. Then [H_0,A]=V_G.
The finite-volume analytic expansion in a real parameter t is

\[
 e^{tA}(H_0+tV)e^{-tA}
   =H_0+tV_B+t^2\left(\tfrac12[A,V_G]+[A,V_B]\right)+O_\Lambda(t^3).
                                                               \tag{14}
\]

To verify the coefficient, expand through degree two. The degree-one term
is V+[A,H_0]=V_B. The degree-two term is
[A,V]+[A,[A,H_0]]/2=[A,V]-[A,V_G]/2, which is the stated expression.
The remainder in (14) is only a finite-volume Taylor remainder; no
volume-uniform bound for the sum A is asserted.

If only good sites are perturbed, the order-two term is

\[
 Q=\sum_f Q_{ff}+\sum_{f<g}Q_{fg},\quad
 Q_{ff}=\tfrac12[A_f,V_f],\quad
 Q_{fg}=\tfrac12([A_f,V_g]+[A_g,V_f]).               \tag{15}
\]

Let thresholds be delta_f,delta_g, and define a_f=C_*|epsilon_f|/delta_f.
The norm estimates are

\[
 \|Q_{ff}\|\le C_*\epsilon_f^2/\delta_f,
 \qquad
 \|Q_{fg}\|\le C_*|\epsilon_f\epsilon_g|
                    (\delta_f^{-1}+\delta_g^{-1}). \tag{16}
\]

These follow from ||[B,C]||<=2||B||||C||. They do not depend on block size.
I_f contains no frozen sites other than f and its immediate predecessor
and successor in the ordered list of frozen sites. If f,g are not consecutive
in that list, g is outside I_f and f outside I_g. Both commutators in Q_fg
then vanish. For consecutive f,g, Q_fg is supported on I_f union I_g and
flips both frozen spins. Q_ff preserves all frozen spins but may change
active-block eigenstate labels; it need not be diagonal in an H_0 eigenbasis.

To see the denominators explicitly, choose the controlled eigenbasis of H_0
and write its energies E_alpha. On a nonzero transition of V_f at a good f,

\[
 (A_f)_{\alpha\kappa}
       =\frac{(V_f)_{\alpha\kappa}}{E_\alpha-E_\kappa}.
\]

For Q= [A,V]/2 with only good sites perturbed,

\[
 Q_{\alpha\beta}
 =\frac12\sum_\kappa V_{\alpha\kappa}V_{\kappa\beta}
       \left(\frac1{E_\alpha-E_\kappa}
                    +\frac1{E_\beta-E_\kappa}\right).           \tag{17}
\]

The sum is over paths with both matrix elements nonzero. This restriction
avoids assigning meaning to unused zero denominators. Formula (17) follows
by expanding AV-VA and replacing -(E_kappa-E_beta)^(-1) by
(E_beta-E_kappa)^(-1). The intermediate denominators are the first-flip
ones already controlled by (1). Solving away an off-diagonal Q_alpha,beta
would introduce a new endpoint denominator E_alpha-E_beta.

For a two-distinct-barrier path, let the endpoint alpha have frozen values
s_f,s_g and beta the opposite values, with all other frozen spins fixed.
The endpoint denominator in the original H_0 basis has the form

\[
 E_\alpha-E_\beta=2s_fh_f+2s_gh_g+c,                \tag{18}
\]

where c is independent of h_f,h_g. Indeed these fields occur only as frozen
on-site scalars, while the active spectra depend on the frozen signs and
the other fields. Spectator labels unchanged by the path cancel.
For a twice-at-the-same-barrier path, the frozen signs at the endpoints
are identical. All frozen on-site fields cancel; the new endpoint gap
is between active-block states and is independent of h_f. The estimate
from Section 2 at f therefore gives no control of that gap.

Even (18) does not justify iterating (6) with unchanged constants: the
path amplitudes and good events already depend on these fields, and
renormalized energies acquire field-dependent corrections. For the
one-spin example H_0=hZ, V=epsilon X, h!=0, direct multiplication gives

\[
 A=\begin{pmatrix}0&\epsilon/(2h)\\-\epsilon/(2h)&0\end{pmatrix},
 \qquad Q=\frac{\epsilon^2}{2h}Z.
\]

The signed sector-energy difference of H_0+Q is 2h+epsilon^2/h, already
a nonlinear function of h.
Equations (14)--(18) identify the next obstruction, without a level-spacing
or resonance-probability assertion for the renormalized Hamiltonian.

## 7. Scope

The result is a first local rotation and its quantitative remainder at a
formerly exact barrier. It preserves the all-state quantifier and the
volume-independent fixed-site probability bound of the earlier work.
It does not construct mutually commuting exact integrals for a chain with
nonzero transverse terms at every site, control repeated denominators, or
establish a full-spectrum localized phase. No optimality or literature
novelty is claimed for the constant C_* or the first-rotation identities.
