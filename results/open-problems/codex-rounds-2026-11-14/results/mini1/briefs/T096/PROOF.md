# External fields can slow a frustrated triangle

For K≥0 and b∈R, let

\[
 \mu_{K,b}(x)=Z_{K,b}^{-1}
 \exp\{-K(x_1x_2+x_1x_3+x_2x_3)+b(x_1+x_2+x_3)\},
 \qquad x\in\{-1,1\}^3.
\]

Both K and b are coefficients in the log density. In a convention with an inverse temperature multiplying the entire Hamiltonian, these coefficients already include that factor.

Let P_i be conditional expectation given the other two coordinates, and let
L=∑_{i=1}^3(P_i−I). This is heat-bath dynamics with rate one at each site. Write γ(K,b) for the smallest positive eigenvalue of −L. A discrete step choosing a site uniformly has transition operator P=(P_1+P_2+P_3)/3 and gap γ(K,b)/3.

**Theorem.** For every finite K≥0,

\[
 \gamma(K,0)=1-\tfrac12\tanh(2K)\geq\tfrac12.
 \tag{1}
\]

Put

\[
 u=\tanh K,\quad v=\tanh(3K),\quad
 A=(u+v)/4,\quad C=(v-3u)/4.
\]

Then

\[
 \gamma(K,K)=
 \frac{3-2A-\sqrt{1+4C(-A+2C)}}2.
 \tag{2}
\]

In particular, at K=log 2,

\[
 \gamma(K,0)=\frac{19}{34},\qquad
 \gamma(K,K)=\frac{72-\sqrt{1765}}{65}
 <\frac6{13}<\frac{19}{34}.
 \tag{3}
\]

There is also the elementary bound

\[
 \gamma(K,K)<\frac{9}{2(1+e^{2K})}.
 \tag{4}
\]

Consequently, no universal positive constant c can satisfy
γ(J,h)≥cγ(J,0) for every finite Ising interaction matrix J and every external field h, even for three spins and a nonnegative uniform field. In fact, for this family,

\[
 \frac{\gamma(K,K)}{\gamma(K,0)}<9e^{-2K}.
 \tag{5}
\]

## 1. Reversibility and the polynomial basis

Each P_i is an orthogonal projection in L²(μ_{K,b}): conditioning twice gives P_i²=P_i, and conditioning the product shows
⟨f,P_i g⟩=⟨P_i f,g⟩. Thus −L is self-adjoint and nonnegative. All single-spin flip rates are positive for finite K,b, so the chain is irreducible and the zero eigenvalue is simple.

The eight monomials 1, x_1,x_2,x_3, x_1x_2,x_1x_3,x_2x_3, x_1x_2x_3 form a basis of all functions on the cube. It therefore suffices to compute the action on these functions.

## 2. Complete zero-field spectrum

Set a=½tanh(2K). At b=0 the conditional mean at site i, with other sites j,k, is

\[
 E[x_i\mid x_j,x_k]=\tanh[-K(x_j+x_k)]=-a(x_j+x_k).
\]

This holds when the other spins agree, by the definition of a, and when they disagree, because both sides vanish. Therefore

\[
 Lx_i=-x_i-a(x_j+x_k).
 \tag{6}
\]

On the three-dimensional space of linear functions, the sum x_1+x_2+x_3 has eigenvalue −(1+2a), and the two-dimensional subspace whose coefficients sum to zero has eigenvalue −(1−a).

For distinct i,j,k, updating the two coordinates in x_ix_j gives

\[
 L(x_ix_j)=-2x_ix_j-a(2+x_ix_k+x_jx_k).
 \tag{7}
\]

Modulo constants, the quadratic sum has eigenvalue −(2+2a), and the two-dimensional space of quadratic coefficient differences has eigenvalue −(2−a). Constants contribute eigenvalue zero. These conclusions give the eigenvalues on the entire even subspace: the constant terms in (7) make the matrix block triangular and do not change its diagonal-block eigenvalues.

Finally, with r=x_1x_2x_3,

\[
 Lr=-3r-2a(x_1+x_2+x_3).
 \tag{8}
\]

The odd subspace is also block triangular, contributing the linear eigenvalues already found and eigenvalue −3. Counting multiplicities, the complete spectrum of −L is

\[
 0,\quad 1+2a,\quad (1-a)^{[2]},\quad
 2+2a,\quad (2-a)^{[2]},\quad 3.
 \tag{9}
\]

Here [2] denotes multiplicity two. Since 0≤a<½, the smallest positive value is 1−a, proving (1).

## 3. Complete spectrum at field b=K

For j,k distinct from i, write the conditional mean as

\[
 E[x_i\mid x_j,x_k]=\tanh[K-K(x_j+x_k)]
 =A+B(x_j+x_k)+Cx_jx_k.
 \tag{10}
\]

For (x_j,x_k) equal to (+,+), (+,−), and (−,−), the left side is respectively −u,u,v. Solving the three equations yields

\[
 A=(u+v)/4,\qquad B=-(u+v)/4=-A,\qquad C=(v-3u)/4.
 \tag{11}
\]

The monomial actions are consequently

\[
 \begin{aligned}
 Lx_i&=-x_i+A+B(x_j+x_k)+Cx_jx_k,\\
 L(x_ix_j)&=-2x_ix_j+A(x_i+x_j)
       +B(2+x_ix_k+x_jx_k)+2Cx_k.
 \end{aligned}
 \tag{12}
\]

For d=x_1−x_2 and e=x_3(x_1−x_2), subtraction gives

\[
 Ld=-(1+B)d-Ce,\qquad
 Le=(A-2C)d-(2+B)e.
 \tag{13}
\]

Thus the matrix of −L on span{d,e}, with columns recording images of basis functions, is

\[
 \begin{pmatrix}1-A&-A+2C\\C&2-A\end{pmatrix}.
 \tag{14}
\]

Its eigenvalues are

\[
 \lambda_\pm=
 \frac{3-2A\pm\sqrt{1+4C(-A+2C)}}2.
 \tag{15}
\]

The corresponding differences x_2−x_3 and x_1(x_2−x_3) give another copy of this matrix. The four functions so obtained are linearly independent: the two linear coefficient differences are independent, the two quadratic coefficient differences are independent, and monomials of different degrees are independent. Each λ_± therefore occurs twice.

For completeness, consider the remaining four-dimensional subspace with basis

\[
 1,\qquad m=x_1+x_2+x_3,\qquad
 s=x_1x_2+x_1x_3+x_2x_3,\qquad r=x_1x_2x_3.
\]

Summing (12) and updating r gives

\[
 \begin{aligned}
 Lm&=3A-(1-2B)m+Cs,\\
 Ls&=6B+2(A+C)m-(2-2B)s,\\
 Lr&=3C+2Bm+As-3r.
 \end{aligned}
 \tag{16}
\]

The eigenvalues of −L on this subspace are 0,3 and

\[
 \nu_\pm=
 \frac{3+4A\pm\sqrt{1+8C(A+C)}}2.
 \tag{17}
\]

Indeed, modulo constants the matrix on span{m,s} has diagonal entries 1−2B,2−2B and off-diagonal entries −2(A+C),−C; r contributes the final diagonal-block value 3.

It remains to identify the least positive eigenvalue. Since tanh is increasing, v≥u≥0. The triple-angle identity gives

\[
 v=\frac{3u+u^3}{1+3u^2}\leq3u.
\]

Hence C≤0, A≥0, and A+C=(v−u)/2≥0. Also A≤½. Therefore C(−A+2C)≥0, and (15) gives λ_−≤1−A≤1. The square root in (17) is real because it comes from the restriction of the self-adjoint operator −L to an invariant subspace. Since C(A+C)≤0, that square root is at most 1, giving ν_−≥1+2A≥1. The other eigenvalues λ_+,ν_+,3 are no smaller than λ_−. Irreducibility makes λ_− positive for finite K. The eight-dimensional decomposition is complete, so γ(K,K)=λ_−, proving (2).

At K=log 2, u=3/5, v=63/65, A=51/130 and C=−27/130. Substitution into (15) gives (72−√1765)/65. The zero-field value follows from tanh(2log 2)=15/17. Since √1765>42, the field gap is less than 30/65=6/13, which is less than 19/34. This proves (3) using exact arithmetic.

## 4. An independent bottleneck bound

At b=K, the four possible magnetizations m=3,1,−1,−3 have log weights 0,2K,0,−6K, with multiplicities 1,3,3,1. Thus

\[
 Z_{K,K}=3e^{2K}+4+e^{-6K}.
 \tag{18}
\]

Let z=(1,1,−1), and let p=μ_{K,K}(z)=e^{2K}/Z_{K,K}. In particular 0<p<1/3. Each of the three neighboring configurations of z has log weight zero, whereas z has log weight 2K. The heat-bath flip rate along each of these edges is therefore 1/(1+e^{2K}), and the total exit rate is

\[
 q_z=\frac{3}{1+e^{2K}}.
 \tag{19}
\]

For f=1_{\{z\}}, its variance is p(1−p), and its Dirichlet form −⟨f,Lf⟩ is pq_z. The variational formula for the gap gives

\[
 \gamma(K,K)\leq\frac{q_z}{1-p}
 <\frac{9}{2(1+e^{2K})}.
 \tag{20}
\]

This proves (4), and dividing by (1) proves (5). This argument uses no diagonalization.

There is also a direct worst-start mixing obstruction. Starting from z, the probability that no actual jump has occurred by time t is e^{−q_z t}. Thus

\[
 \|\mathcal L_z(X_t)-\mu_{K,K}\|_{\rm TV}
 \geq e^{-q_z t}-p.
\]

Since p<1/3, the distance exceeds 1/4 at t=log(12/7)/q_z. In particular

\[
 t_{\rm mix}(1/4)>\frac{1+e^{2K}}3\log(12/7)
\]

in rate-one-per-site time. For the discrete uniform-site chain, the probability of staying at z for k steps is (1−1/(1+e^{2K}))^k, so the same conclusion has a direct discrete-time formulation.

## 5. Scope for Gaussian SK

For n=3 and any fixed β>0, the SK log density β∑_{i<j}g_{ij}x_ix_j/√3 contains this interaction matrix at g_{12}=g_{13}=g_{23}=−√3K/β. The exact point has Gaussian probability zero. However, all finite heat-bath rates and stationary probabilities vary continuously with the couplings and fields. The symmetric matrix representing −L does too, so its ordered eigenvalues are continuous. The strict gap inequality in (3) therefore persists on a nonempty open neighborhood of the couplings, with field held at b=log 2. Independent Gaussians give that neighborhood positive probability.

This is a finite-dimensional obstruction to a deterministic field comparison. The limit K→∞ varies the interaction strength in a fixed three-spin system; it is not the limit n→∞ at fixed β in SK. The theorem gives no failure probability bounded away from zero in that latter limit and does not refute rapid mixing for typical SK disorder. It also does not rule out a comparison whose constant depends on an interaction norm, or a comparison restricted to a high-probability set of SK matrices.
