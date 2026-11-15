# Potentials for the E/D recursion

All logarithms are base two. The definitions here apply to a real function g with squared Fourier coefficients mu, mass m=sum mu, and containment sums up. Put

Hbar(g)=sum mu(S) log(m/mu(S)),
Abar(g)=sum mu(S) log(m/up(S)),
N(g)=m log(1/m).

Thus Hbar=Abar+B, while the unnormalised H and A requested in the brief are Hbar+N and Abar+N. Zero terms have their continuous value zero. Hbar, Abar, B are homogeneous of degree two. N is not; its scaling defect is additive in mass and therefore cancels in the E/D difference.

## 1. Every bounded dyadic real function occurs in the specified node class

Suppose h:{-1,1}^r -> [-1,1] has dyadic values. Choose q so that 2^q(1+h(x))/2 is an integer for every x. Define a Boolean F(x,z) which is +1 at exactly that many of the 2^q assignments z and -1 at the others. Then E_z F(x,z)=h(x), pointwise. Averaging those q coordinates one at a time makes h an iterated E image of a Boolean function. No claim about its other E/D branches is needed. Consequently an inequality required at every node in the brief must hold for all bounded dyadic h.

## 2. Exact classification for unweighted entropy potentials

Consider fixed real coefficients t,s,u and

Phi(g)=t Abar(g)+s B(g)+u N(g).

Assume the leaf condition holds on the entire node class, and ask whether some finite C>=0 makes (*) hold with some choice of coordinate at every non-scalar node. This is possible if and only if

u>=0, t>=u, s>=t+1.

When these inequalities hold, C=0 already works for every coordinate. At a Boolean root Phi(f)>=B(f), so every such solution carries the original B bound in its root condition.

Proof. Write a=E_i g, d=D_i g, m_a=||a||^2, m_d=||d||^2, m=m_a+m_d. Let

T_i(g)=m h_2(m_d/m),

where h_2 is binary entropy and T=0 for zero mass. Directly splitting the coefficient sum gives Delta Hbar=T. Mass additivity gives Delta N=-T. Lemma 3 gives Delta B=J, so Delta Abar=T-J. Therefore (*) is exactly

(1-s+t) J_i <= C m_d + (t-u) T_i.                 (1)

At a scalar leaf Abar=B=0. There are scalar nodes of any dyadic value in (0,1), where N>0, so the leaf condition forces u>=0.

For a growing family take M=4^k, k>=1, kappa=1/(2 sqrt(M)), and

g_M(x_0,...,x_M)=kappa [M^(-1/2) sum_{j=1}^M x_j + x_0 product_{j=1}^M x_j].

Its maximum absolute value is at most (sqrt(M)+1)/(2 sqrt(M))<=1 and all values are dyadic. The first construction places it in the required node class. There are M singleton coefficients of square kappa^2/M, and one full-set coefficient of square kappa^2. At coordinate 0,

J_0/||D_0 g_M||^2=log(1+M), T_0/||D_0 g_M||^2=2.

At every coordinate j>=1,

J_j/||D_j g_M||^2=((M-1)/(M+1)) log(1+M),
T_j/||D_j g_M||^2=2 h_2((M+1)/(2M))/(1+1/M)<=2.

The J ratios diverge simultaneously at every coordinate, while the T ratios remain bounded. Equation (1) forces 1-s+t<=0, including for an adaptive best-coordinate rule.

Next take the one-coordinate dyadic function h_epsilon(x)=(1+epsilon x)/2, epsilon=2^(-q). It is bounded and hence belongs to the same node class. Its only coordinate has

J/||D h_epsilon||^2=epsilon^(-2) log(1+epsilon^2) -> 1/ln(2),
T/||D h_epsilon||^2=((1+epsilon^2)/epsilon^2) h_2(epsilon^2/(1+epsilon^2)) -> infinity.

If t-u<0, the right side of (1), divided by ||D h_epsilon||^2, tends to minus infinity, whereas the left side stays finite. Thus t>=u is necessary. Conversely the three stated conditions make the left side of (1) nonpositive and its right side nonnegative at C=0. This proves sufficiency. Finally Abar,B>=0, m=1 and N=0 at a Boolean root. Since t>=0 and s>=1, Phi(f)>=B(f). QED.

Consequences: no multiple of Abar plus an admissible N correction works universally. Neither the entropy potential Hbar nor its negative repairs this E/D induction. A positive B potential works only by carrying B at the root. For the sign used in (*), +B is the identity at C=0; -B requires 2J<=C||d||^2. The brief's warning about -B has the opposite sign.

There is another instructive excluded identity: raw H has zero E/D difference, hence raw A has difference -J. Phi=-A_raw would pay J exactly, but its scalar leaves equal -N<0 whenever their mass lies strictly between zero and one. The leaf condition is essential.

## 3. Finite polynomial level-mass potentials also cannot work

Let Phi(g)=v V(g)+sum_{ell=1}^L a_ell M_ell(g)+u N(g), where V=m-mu(empty), M_ell=sum |S|^ell mu(S), and all coefficients are fixed across dimensions. Suppose (*) holds on the whole node class with finite C and Phi(f)<=Cprime I(f) on every Boolean root with finite Cprime. Then no such potential exists.

Proof. Apply the root bound to the Boolean parity on k coordinates. Its potential is v+P(k), with P(k)=sum a_ell k^ell, so v+P(k)<=Cprime k. For the same parity, each coordinate has J=0 and ||d||^2=1. For k>=2, Delta V=0 and Delta N=0, hence (*) requires P(k)-P(k-1)>=-C. Summing gives a linear lower bound on P(k). A real polynomial bounded above and below by linear functions on the positive integers has degree at most one. Therefore a_ell=0 for ell>=2.

The M_1 term is I; Delta I=||d||^2, so it only replaces C by C+a_1. Scalar leaves force u>=0. In the g_M family above, Delta V equals the square of the constant Fourier coefficient of d. This is zero at coordinate 0 and kappa^2/M at each other coordinate. Dividing by ||d||^2 bounds Delta V/||d||^2 by 1/(M+1). Also Delta N=-T<=0. The potential contribution cannot pay the J ratios that diverge at every coordinate. This contradicts finite C+a_1. QED.

## 4. The quadratic level-weighted B family cannot work either

Let B_j(g)=sum |S|^j mu(S) log(up(S)/mu(S)). No fixed Phi=b_1 B_1+b_2 B_2+u N satisfies both the local inequality and a universal root budget.

Proof. For even r, a product of r/2 Boolean AND_2 gates has uniform squared spectrum on all r bits. Its spectral degree is Binomial(r,1/2). Direct evaluation gives

B_1=r(r-1)/4, B_2=r^2(r-1)/8, I=r/2.

The root condition bounds b_1(r-1)/2+b_2 r(r-1)/4 above uniformly. It forces b_2<=0 and, if b_2=0, b_1<=0. Each coordinate of the same function has ||d||^2=1/2 and J=1/2; both children have mass 1/2 and uniform squared spectrum on r-1 bits. Therefore

Delta B_1=(r-1)/2,
Delta B_2=(3r^2-5r+2)/8,
Delta N=-1.

If b_2<0, the right side of (*) tends to minus infinity along this family, for every coordinate. Thus b_2=0. If b_1<0 the same contradiction follows linearly in r, so b_1=0. Leaves require u>=0. The remaining uN has nonpositive drop and is killed by g_M from section 2. QED.

## 5. Level-profile and marginal entropy cannot supply the potential

Let L(g) be mass times the entropy of the spectral degree distribution, and Q(g)=m sum_i h_2(I_i(g)/m) the sum of marginal spectral entropies. No fixed Phi=aL+bQ+uN satisfies both conditions.

Proof. For Boolean AND_n, put p=2^{1-n}. Its coordinate influences are p and I=np. Thus Q/I=h_2(p)/p>=log(1/p)=n-1. Its nonconstant spectral mass is v=2p-p^2, and its degree distribution has one mass 1-v at zero and v spread over at most n positive degrees. Consequently

L <= h_2(v)+v log n,
L/I <= 2+o(1).

The second estimate follows from v=2p-p^2, h_2(v)=v log(1/v)+O(v), and log(1/p)=n-1. A universal root bound therefore forces b<=0 regardless of a. Leaves require u>=0.

For any squared-spectrum distribution, splitting bit i gives

Delta Q=m h_2(Pr[i in S])+m sum_{j!=i} MutualInformation(1_{i in S};1_{j in S})>=0.

This follows by subtracting the weighted child marginal entropies, which are the conditional entropies given bit i. In the g_M family of section 2, the parent has equal spectral mass at degrees 1 and M+1, hence L(g_M)=2kappa^2. At coordinate 0 both children have a single degree, so Delta L=2kappa^2. At every other coordinate, E_i g_M has a single degree; D_i g_M has at most two degrees and mass kappa^2(1+1/M). Its level entropy lies between zero and that mass. Therefore 0<=Delta L/||d||^2<=2 at every coordinate. Since b<=0, u>=0, Delta Q>=0, and Delta N<=0, we have

Delta Phi/||d||^2 <= 2 max(a,0).

The J/||d||^2 ratios diverge simultaneously at all coordinates. No finite C works. QED.

These are obstructions for the specified families, not a proof of FEI or an obstruction to arbitrary potentials. Numerical checks and explicit finite examples are in proof_checks.json, produced by proof_checks.py. The exact constructions establish membership; no claim is made that their potentially large Boolean lifts were exhaustively materialised.
