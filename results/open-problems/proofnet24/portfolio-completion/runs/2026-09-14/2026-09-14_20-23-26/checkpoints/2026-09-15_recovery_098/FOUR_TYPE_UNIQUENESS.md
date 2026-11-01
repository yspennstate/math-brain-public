# Fixed-point uniqueness for four-type strictly non-Volterra quadratic stochastic operators

Yitzchak Shmalo — research note, 14 September 2026

## Statement and relation to the source problem

Every strictly non-Volterra quadratic stochastic operator on four types has exactly one fixed point. The result holds without positivity of the allowed coefficients, symmetry among the types, or an assumption that the fixed point is interior.

This settles the four-type uniqueness question left open in the current project manuscript. Ganikhodzhaev and Rozikov's [2009 survey, Problem 11](https://arxiv.org/abs/0902.4207) asks whether the three-type theorem, which also concerns attractiveness and cycles, extends to higher dimension. The theorem below addresses its fixed-point uniqueness clause at four types. Jamilov's [2016 publisher abstract](https://doi.org/10.5890/DNC.2016.09.006) reports uniqueness for a symmetric strictly non-Volterra operator on the three-dimensional simplex. The complete hypotheses of that paper have not yet been retrieved, so the precise comparison and worldwide novelty remain provisional. The full cycle question is outside the result established here.

The proof is elementary. A second proof yields a globally convergent averaged iteration, and the same estimates give a quantitative perturbation bound. Original discrete iterates of the quadratic operator need not converge.

## 1. Definitions and a transfer inequality

Write
\[
\Delta_3=\{x\in\mathbb R^4:x_i\ge0,\ \textstyle\sum_i x_i=1\}.
\]
Let
\[
V_k(x)=\sum_{i,j=1}^4P_{ij,k}x_ix_j,
\qquad P_{ij,k}=P_{ji,k}\ge0,
\qquad\sum_kP_{ij,k}=1,
\]
and suppose
\[
P_{ij,k}=0\quad\text{whenever }k\in\{i,j\}.
\tag{1}
\]
These are precisely the strictly non-Volterra coefficient conditions. In particular, the polynomial defining \(V_k\) does not involve its own coordinate \(x_k\). The map preserves the simplex because its coordinates are nonnegative and \(\sum_kV_k(x)=(\sum_i x_i)^2\).

Set
\[
c=\frac{3-\sqrt5}{2}<\frac12.
\tag{2}
\]
At a fixed point,
\[
x_k=V_k(x)\le\sum_{i,j\ne k}x_ix_j=(1-x_k)^2.
\]
Solving this quadratic inequality on \([0,1]\) gives \(x_k\le c\) for every coordinate.

For \(m\in\Delta_3\), define the matrix
\[
A(m)_{rj}=\sum_aP_{aj,r}m_a.
\tag{3}
\]
It is nonnegative, column-stochastic, and has zero diagonal. If \(m=(x+y)/2\), parent symmetry gives the exact polarization identity
\[
V(x)-V(y)=2A(m)(x-y).
\tag{4}
\]
Indeed \(x_ax_b-y_ay_b=m_a(x_b-y_b)+(x_a-y_a)m_b\), and the two resulting sums agree.

**Transfer lemma.** Suppose \(G,H\) partition the four types into two pairs. For \(i\in G\) and \(j\in H\),
\[
\mathbf1_G^{\mathsf T}A(m)(e_i-e_j)\le\max(m_i,m_j).
\tag{5}
\]

**Proof.** Let \(k\) be the other member of \(G\) and \(\ell\) the other member of \(H\). Put
\(p_{ab}=\sum_{r\in G}P_{ab,r}\). Then \(0\le p_{ab}\le1\), \(p_{ab}=p_{ba}\), \(p_{ki}=0\), and \(p_{\ell j}=1\). The last two equalities use both the prohibition (1) and the fact that each part has exactly two members. Consequently
\[
\begin{aligned}
\mathbf1_G^{\mathsf T}A(m)(e_i-e_j)
&=m_i(p_{ii}-p_{ij})+m_j(p_{ij}-p_{jj})
  -m_kp_{kj}+m_\ell(p_{\ell i}-1)\\
&\le m_i(1-p_{ij})+m_jp_{ij}\\
&\le\max(m_i,m_j).
\end{aligned}
\]
No strictly positive coordinate or coefficient is needed. \(\square\)

## 2. Uniqueness

**Theorem 1.** Every operator satisfying (1) has exactly one fixed point in \(\Delta_3\).

**Proof.** Existence follows from Brouwer's theorem. Suppose \(x\ne y\) are fixed points and write \(z=x-y\). A zero-sum nonzero vector has both a positive and a negative coordinate. If \(z_i\) were its only positive coordinate, then \(x_j\le y_j\) for all \(j\ne i\). Since \(V_i\) is a polynomial with nonnegative coefficients in those other coordinates, \(V_i(x)\le V_i(y)\), contradicting \(x_i>y_i\). Interchanging \(x,y\) also rules out exactly one negative coordinate. There are therefore two strictly positive and two strictly negative coordinates.

Let \(G=\{i:z_i>0\}\), \(H=\{j:z_j<0\}\), and \(h=\sum_{i\in G}z_i>0\). Define
\[
\theta_{ij}=\frac{z_i(-z_j)}{h^2},\qquad i\in G,\ j\in H.
\]
Then \(\theta_{ij}\ge0\), \(\sum_{ij}\theta_{ij}=1\), and
\[
z=h\sum_{i\in G,j\in H}\theta_{ij}(e_i-e_j).
\]
Every coordinate of \(m=(x+y)/2\) is at most \(c\). Equations (4) and (5) give
\[
\begin{aligned}
h&=\mathbf1_G^{\mathsf T}(V(x)-V(y))\\
 &=2h\sum_{i\in G,j\in H}\theta_{ij}
       \mathbf1_G^{\mathsf T}A(m)(e_i-e_j)\\
 &\le2ch<h,
\end{aligned}
\]
a contradiction. This proof includes boundary fixed points. \(\square\)

For a separate description of the boundary, the support of any fixed point is an invariant face: for every missing output type, a nonnegative sum over positive input coordinates vanishes, forcing every corresponding coefficient to vanish. A support of size one or two is impossible under (1). A boundary fixed point thus has support of size three; invariance of that triple together with (1) forces the omitted output coordinate to vanish identically. These observations are compatible with Theorem 1 and require no nondegeneracy assumption.

## 3. A constructive proof and a convergent iteration

For \(c\le q<1/2\), put
\[
K_q=\{x\in\Delta_3:\max_i x_i\le q\}.
\]
Let \(0<\lambda\le q\), and consider
\[
T_\lambda(x)=(1-\lambda)x+\lambda V(x).
\tag{6}
\]

**Theorem 2.** The set \(K_q\) is invariant under \(T_\lambda\), and
\[
\|T_\lambda(x)-T_\lambda(y)\|_1
\le L(q,\lambda)\|x-y\|_1,
\quad x,y\in K_q,
\quad L(q,\lambda)=1-\lambda(1-2q)<1.
\tag{7}
\]

**Proof.** For \(s=x_i\in[0,q]\),
\[
(T_\lambda x)_i\le f(s):=(1-\lambda)s+\lambda(1-s)^2.
\]
The function \(f\) is convex, so its maximum on \([0,q]\) occurs at an endpoint. Now \(f(0)=\lambda\le q\), while \(f(q)\le q\) because \(q\ge c\). This proves invariance.

For \(m=(x+y)/2\), equation (4) gives
\[
T_\lambda(x)-T_\lambda(y)=B(m)(x-y),
\quad B(m)=(1-\lambda)I+2\lambda A(m).
\]
All columns of \(B\) have the same sum \(1+\lambda\). For any such matrix, its induced \(\ell^1\) norm on the zero-sum subspace is
\[
\max_{i,j}\frac12\|Be_i-Be_j\|_1
=\max_{G\subseteq\{1,2,3,4\},i,j}
       \mathbf1_G^{\mathsf T}B(e_i-e_j).
\tag{8}
\]
The upper bound in (8) follows by decomposing an arbitrary zero-sum vector into transfers between its positive and negative coordinates; equality follows by taking a vector \(e_i-e_j\). The second equality is the positive-mass formula for a zero-sum vector.

It remains to bound a subset and two distinct column indices. Empty and full subsets give zero.

* If both indices lie in \(G\), or both outside, the identity term cancels and column stochasticity of \(A\) bounds the difference by \(2\lambda\).
* If \(i\notin G\), \(j\in G\), the bound is \(-(1-\lambda)+2\lambda=3\lambda-1\le2\lambda\).
* If \(i\in G\), \(j\notin G\), and \(|G|=1\), the \(A\)-term is \(-A_{ij}\le0\). If \(|G|=3\), it is \(-A_{ji}\le0\). Both cases give at most \(1-\lambda\).
* If \(i\in G\), \(j\notin G\), and \(|G|=2\), the transfer lemma gives at most \(1-\lambda+2\lambda q\).

Finally,
\[
1-\lambda+2\lambda q-2\lambda
=1-\lambda(3-2q)
\ge1-q(3-2q)=(1-q)(1-2q)>0.
\]
Thus (8) is at most the constant in (7). \(\square\)

Banach's theorem gives a unique fixed point of \(T_\lambda\) in \(K_q\). The fixed points of \(T_\lambda\) and \(V\) coincide, and every fixed point of \(V\) lies in \(K_c\), providing a second proof of Theorem 1.

**Corollary 3 (global rational iteration).** For
\[
T(x)=\frac35x+\frac25V(x),
\]
every initial point of \(\Delta_3\) enters \(K_{2/5}\) in at most three iterations. Thereafter the iteration contracts in \(\ell^1\) with factor \(23/25\). In particular, if \(x_{n+1}=T(x_n)\) and \(x^*\) is the unique fixed point, then
\[
\|x_n-x^*\|_1\le2(23/25)^{n-3},\qquad n\ge3.
\tag{9}
\]

**Proof.** Here \(f(s)=2/5-s/5+2s^2/5\). Convexity successively bounds the largest coordinate by
\[
1\longmapsto\frac35\longmapsto\frac{53}{125}\longmapsto\frac25.
\]
For the last step, \(f(0)=2/5\) and \(f(53/125)=30243/78125<2/5\). Invariance and (7) finish the proof; the diameter of the simplex in \(\ell^1\) is two. \(\square\)

There are also a posteriori estimates on \(K_q\):
\[
\|x-x^*\|_1\le\frac{\|T_\lambda x-x\|_1}{1-L(q,\lambda)}
=\frac{\|V(x)-x\|_1}{1-2q}.
\tag{10}
\]
These follow by the triangle inequality and (7). At \(q=2/5\), the final residual multiplier is five. Choosing \(q=\lambda=c\) yields the smaller contraction factor
\[
L(c,c)=\frac{13-5\sqrt5}{2}\approx0.909830.
\tag{11}
\]
This is the minimum of the stated bound over \(c\le q<1/2\), \(0<\lambda\le q\): for fixed \(q\) it is minimized at \(\lambda=q\), and \(1-q+2q^2\) is increasing for \(q\ge c>1/4\). This optimization is within the specified invariant-set argument; it does not assert that no different algorithm has a better rate.

## 4. Quantitative dependence on the coefficients

**Corollary 4.** Let \(P,Q\) be two four-type coefficient arrays satisfying (1), with unique fixed points \(x_P,x_Q\), and define
\[
\eta=\max_{i,j}\sum_k|P_{ij,k}-Q_{ij,k}|.
\]
Then
\[
\|x_P-x_Q\|_1\le\min\{2,(2\sqrt5-1)\eta\}.
\tag{12}
\]

**Proof.** If \(x_P=x_Q\), the conclusion is immediate; assume otherwise. Both fixed points lie in \(K_c\). For any probability vector \(x\),
\[
\|V_P(x)-V_Q(x)\|_1
\le\sum_{i,j}x_ix_j\sum_k|P_{ij,k}-Q_{ij,k}|\le\eta.
\]
Applying (10) already gives the weaker bound \(\eta/(1-2c)=(\sqrt5+2)\eta\). To retain the forced zero perturbations, write \(x=x_P,y=x_Q,z=x-y\), \(G=\{i:z_i>0\}\), and \(h=\|z\|_1/2\). If either sign support is a singleton, interchange \(P,Q\) and \(x,y\), if necessary, to make the positive support the singleton. The monotonicity argument of Theorem 1 bounds the \(P\)-operator group difference by zero. The coefficient contribution to this group is at most \(\eta/2\), giving \(\|z\|_1\le\eta\).

In the remaining case the signs form two pairs, \(G=\{i,k\}\) and \(H=\{j,\ell\}\). The transfer lemma bounds the first term in
\[
h=\sum_{r\in G}[V_{P,r}(x)-V_{P,r}(y)]
  +\sum_{r\in G}[V_{P,r}(y)-V_{Q,r}(y)]
\]
by \(2ch\). The group output probability of each within-pair parental combination \(\{i,k\}\) and \(\{j,\ell\}\) is forced to zero or one for both arrays. Their perturbations therefore vanish. Every other row has group perturbation at most \(\eta/2\), so the second term is at most
\[
\frac\eta2[1-2(y_iy_k+y_jy_\ell)].
\]
Since \(y_a\le c\) and its coordinates sum to one,
\[
0\le(c-y_i)(c-y_k)+(c-y_j)(c-y_\ell)
=2c^2-c+y_iy_k+y_jy_\ell.
\]
Consequently \(y_iy_k+y_jy_\ell\ge c(1-2c)\), and
\[
\|z\|_1\le\left[\frac1{1-2c}-2c\right]\eta
=(2\sqrt5-1)\eta.
\]
The simplex diameter gives the other bound two. This sharper estimate is due to agent013; no optimality is claimed. \(\square\)

The same sign-cut proof also improves (10) for a known approximation \(x\): if \(\|x\|_\infty<1-c\), then
\[
\|x-x^*\|_1\le\frac{\|x-V(x)\|_1}{1-c-\|x\|_\infty}.
\]
Indeed the midpoint with the true fixed point has maximum coordinate at most \((\|x\|_\infty+c)/2\), and summing the fixed-point residual over the positive support gives this bound. Agent013 gives the full argument, including zero coordinates and residual-only variants. The solver in this packet uses the simpler rational multiplier five from (10), which remains valid.

## 5. The determinant question

**Corollary 5.** At a fixed point \(x^*\), put \(J=DV(x^*)=2A(x^*)\), and restrict \(J\) to the tangent space \(E=\{z:\sum_i z_i=0\}\). Every positive real eigenvalue \(\rho\) of \(J|_E\) obeys
\[
\rho\le2\max_i x_i^*\le3-\sqrt5<1.
\tag{13}
\]
In particular,
\[
\det(I-J|_E)>0.
\tag{14}
\]

**Proof.** Take a real eigenvector for \(\rho>0\). Since the ambient matrix \(J\) is nonnegative with zero diagonal, an eigenvector with a single positive coordinate is impossible: at that coordinate \((Jz)_i\le0<\rho z_i\). The same argument rules out a single negative coordinate. Its signs therefore form a two-pair partition. Apply the transfer decomposition used in Theorem 1, now to \(Jz=\rho z\), to obtain (13).

For \(0\le s\le1\), \(I-sJ|_E\) is nonsingular: a singularity for \(s>0\) would give a positive real eigenvalue \(1/s\ge1\), contradicting (13). Its determinant is real and continuous and equals one at \(s=0\), proving (14). \(\square\)

Writing \(e_3(A)\) for the sum of the principal minors of order three, (14) gives the strict inequality asked in the archived manuscript:
\[
3+4e_3(A(x^*))-12\det A(x^*)>0.
\tag{15}
\]
For completeness, \(\operatorname{tr}A=0\), \(1\) is an eigenvalue, and
\(\det(I-A)=1+e_2(A)-e_3(A)+\det A=0\). Thus
\(\det(I-2A)=1+4e_2(A)-8e_3(A)+16\det A=-3-4e_3(A)+12\det A\).
The radial eigenvalue of \(J\) is two, so \(\det(I-J)=-\det(I-J|_E)\), which proves (15).

## 6. Allowing a small probability of parental offspring

The same argument proves uniqueness for a larger class of quadratic stochastic operators. For a stochastic coefficient array on four types, define
\[
\delta=\max_{i,j}\sum_{k\in\{i,j\}}P_{ij,k}.
\tag{16}
\]
The repeated-parent case counts the single coefficient \(P_{ii,i}\) once. Thus (16) bounds the total probability that the offspring belongs to either parental type.

**Theorem 6.** Suppose
\[
0\le\delta<1-\frac{\sqrt3}{2}.
\]
Put
\[
a=1-\delta,\qquad s=\sqrt{1+4a^2},\qquad
q=1-\frac{s-1}{2a},\qquad\kappa=s-2>0.
\]
Then \(V\) has exactly one fixed point, which belongs to \(K_q\). For every \(0<\lambda\le q\), the averaged map \(T_\lambda=(1-\lambda)I+\lambda V\) preserves \(K_q\) and contracts there with factor \(L=1-\lambda\kappa<1\). Its iterates converge to the fixed point from every point of the simplex. More precisely,
\[
\|T_\lambda^n(x)-T_\lambda^n(y)\|_1
\le
\exp\!\left(\frac{2(s-1)}{L(s+1)}\right)L^n\|x-y\|_1,
\quad x,y\in\Delta_3.
\tag{17}
\]
The threshold is a sufficient condition; its optimality is not asserted.

**Proof.** The total weight of parent pairs containing type \(i\) is \(1-(1-x_i)^2\). Therefore
\[
V_i(x)\le\delta+(1-\delta)(1-x_i)^2=:g(x_i).
\]
The strictly decreasing function \(g(u)-u\) has its unique zero in \([0,1]\) at \(q\), so every fixed point lies in \(K_q\). Directly from the displayed definitions,
\[
c\le q<1-1/\sqrt3<1/2,\qquad g(q)=q.
\]
The convex function \(f(u)=(1-\lambda)u+\lambda g(u)\) has \(f(0)=\lambda\le q\) and \(f(q)=q\), proving invariance.

The matrix \(A(m)\) in (3) remains nonnegative and column-stochastic, and now \(A_{ii}\le\delta\). In a two-pair cut, the proof of (5) instead uses \(p_{ki}\le\delta\), \(p_{\ell j}\ge1-\delta\), and gives
\[
\begin{aligned}
\mathbf1_G^{\mathsf T}A(m)(e_i-e_j)
&\le m_i(1-p_{ij})+m_jp_{ij}+\delta(m_k+m_\ell)\\
&\le\delta+(1-\delta)\max_r m_r.
\end{aligned}
\]
For singleton and three-element separating cuts the bound is \(\delta\). The other cases in (8) are unchanged. On \(K_q\), put \(\beta=\delta+aq=(3-s)/2\). The resulting norm bound is
\[
\max\{2\lambda,1-\lambda+2\lambda\beta\}
=1-\lambda(s-2)=L<1.
\]
The second term dominates because \(\beta\ge q\), \(\lambda\le q<1/2\), and the same calculation following (8) applies. Banach's theorem proves existence and uniqueness in \(K_q\); the coordinate bound covers every possible fixed point.

For global convergence, let \(q_0=1\), \(q_{n+1}=f(q_n)\). The identity
\[
1-qs=\frac{2a(s-2a)}{s+1}>0
\]
shows that \(f\) is increasing on \([q,1]\), since \(\lambda\le q\). Convexity gives \(T_\lambda(K_{q_n})\subseteq K_{q_{n+1}}\), and
\[
0\le q_n-q\le(1-q)\rho^n,
\qquad\rho=1-\frac{\lambda(s+1)}2\in(0,1).
\]
Indeed
\[
f(u)-q=(u-q)\{1-\lambda[1+a(2-u-q)]\},
\]
whose bracket on \([q,1]\) is nonnegative and at most \(\rho\). At stage \(n\), the norm bound from the cut argument is at most
\(L+2\lambda a(1-q)\rho^n\). Multiplying these bounds and using \(1+t\le e^t\) gives (17), because
\[
\frac{2\lambda a(1-q)}{L(1-\rho)}
=\frac{2(s-1)}{L(s+1)}.
\]
Taking \(y\) to be the fixed point proves the global convergence assertion. \(\square\)

This extension was derived by the parent, its global bound was developed by agent011, and both arguments were checked independently in agent014's full report. The strict non-Volterra case is exactly \(\delta=0\).

## 7. The half-step endpoint also converges

**Theorem 7.** Suppose \(V\) is strictly non-Volterra and satisfies (1). For \(T=(I+V)/2\), every initial point converges to the unique fixed point. A coefficient-uniform explicit estimate is
\[
\|T^n x-x^*\|_1\le2\left(\frac{7967}{8192}\right)^{n-3},\qquad n\ge3.
\]

The complete proof is in [the half-step note](QSO_HALF_STEP_EXPLICIT.md). Its main extra ingredient is an overlap estimate for every column pair of \(A(m)\) when \(m\) is a midpoint of points in \(T^3(\Delta_3)\). The sharp two-step coordinate cap is \(49/128\). If both tested coordinate masses are at least \(225/8192\), their common parental offspring distribution supplies that much overlap. If one mass is smaller, a preimage in \(T^2(\Delta_3)\) bounds offspring probabilities into that small coordinate and forces overlap on the other two coordinates. The resulting zero-sum norm of \(I/2+A(m)\) is at most \(7967/8192\). Compact invariant-image contraction then proves the theorem. Agent024 independently verified the full argument and its exact constants. This sufficient rate is not claimed optimal.

## 8. Guaranteed rational computation in polynomial bit complexity

Assume throughout this section that every coefficient of the tensor is rational and is supplied by an exact integer numerator and positive integer denominator. The constructive contraction then gives a finite exact algorithm at any positive rational tolerance \(\varepsilon\). This strengthens the stopping guarantee beyond a floating-point search followed by exact certification. The full implementation and bit model are in [report065](agents/065.md); the parent independently checked the proof and code.

Let \(T=3I/5+2V/5\), \(L=23/25\), and choose
\[
N=20\max\{1,\lceil75/\varepsilon\rceil\}.
\]
Starting at \(x_0=(1/4,1/4,1/4,1/4)\), calculate \(T(x_t)\) exactly, round down its four coordinates to multiples of \(1/N\), and give the remaining units to the largest fractional remainders, breaking ties by coordinate order. Call this rounding map \(Q_N\), and put \(x_{t+1}=Q_NT(x_t)\).

The rounded coordinates still sum to one. Because \(2N/5\) is an integer, rounding any coordinate at most \(2/5\) to its floor or ceiling cannot exceed that cap. No zero remainder receives an extra unit: the sum of the fractional remainders is the integer number of units to allocate, and if it is positive there are more positive remainders than units. Therefore every iterate stays in the invariant cap. Each coordinate changes by less than \(1/N\), so the rounding error is at most \(4/N\) in \(\ell^1\).

If \(p\) is the unique fixed point and \(d_t=\|x_t-p\|_1\), contraction gives
\[
d_t\le 2L^t+\frac{50}{N}.
\]
Moreover, \(V\) is globally 2-Lipschitz on the simplex, whence
\[
\|V(x)-x\|_1\le3\|x-p\|_1.
\]
Choose the least nonnegative integer \(k\) with \(2^k\ge60/\varepsilon\). The exact integer inequality \(2\cdot23^9\le25^9\) gives \(L^9\le1/2\). At \(t=9k\), both \(2L^t\) and \(50/N\) are at most \(\varepsilon/30\). Consequently
\[
5\|V(x_{9k})-x_{9k}\|_1
\le15\left(2L^{9k}+\frac{50}{N}\right)
\le\varepsilon.
\]
The residual bound (10) certifies distance at most \(\varepsilon\), so checking this exact residual at each iteration must succeed by the proved horizon.

For implementation, clear the coefficient denominators once to a common integer \(D_0\), and represent each iterate by four counts summing to \(N\). Every quadratic evaluation then uses integers with \(O(b+h)\) bits, where \(b\) is the explicit coefficient encoding length and \(h\) the rational tolerance encoding length. Rounding resets the denominator to \(N\) every time; no grid enumeration or repeated denominator squaring occurs. There are \(O(1+h)\) iterations and a constant number of arithmetic operations per step. Elementary integer arithmetic gives the safe polynomial bound \(O((1+h)(1+b+h)^3)\). This is a finite-accuracy algorithm, not a claim that a fixed rounded grid orbit converges exactly to an irrational fixed point.

## Verification and scope

The elementary proof originated in agent006's report. The transfer inequality and boundary arguments received an independent line-by-line audit in agent007. The constructive proof combines the parent derivation with agent008's independent audit and improvements. Full execution records, later checks, corrections, and exact finite computations accompany this note. Finite checks support the algebra; the universal statements rest on the proofs above. This note makes no claim that the new theorem has been formally checked in Lean or refereed by a human mathematician.

The result establishes uniqueness for every strictly non-Volterra quadratic stochastic operator on four types, and complements the project's existing five-type counterexample, whose tensor and original two-point classification are due to Jamilov2017 as verified in [primary-source audit091](agents/091.md). It does not settle Lyons's determinantal-entropy concavity conjecture, nor the higher-dimensional cycle questions for these stochastic operators. Current literature checks and any remaining retrieval limits are recorded separately; absence of a matching search result is not proof of worldwide novelty.
