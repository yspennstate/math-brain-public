# A sharper flat-grid subdivision bound for equal masses

Let Q=[0,1]^2, let T=R^2/Z^2 be the unit flat torus, and let dx denote uniform probability on either space. The heat operator is exp(t Delta); thus a free Gaussian increment at time t has covariance 2t I. Let Y_1,...,Y_n be independent uniform points, and put

\[
\nu_n=\frac1n\sum_{i=1}^n\delta_{Y_i},\qquad
t=n^{-5/6},\qquad s=n^{-1}.
\]

For m in {1,2,3}, partition Q into m^2 squares B of side ell=1/m. Identify this grid with a partition of T, retaining its seams when m=1. Let S_t be the direct sum of the Neumann heat operators on these squares, and write S_t nu_n=q dx. For measures with equal mass on B, OT_B denotes the minimum squared Euclidean transport cost of their restrictions, without renormalizing that mass. Set

\[
Z_{n,m}=n\sum_B\operatorname{OT}_B(q\,dx,\nu_n).
\tag{1}
\]

All constants below are independent of n. They may depend on m; since only three values of m occur, one constant suffices for all of them.

Almost surely no sampled point lies on a grid boundary. Work on that probability-one event throughout; all cell assignments and restrictions are then unambiguous.

**Theorem.** For Omega=Q or T and n>=2,

\[
\mathbb E\left|nW_{2,\Omega}^2(P_t^\Omega\nu_n,\nu_n)-Z_{n,m}\right|
\le C n^{-1/60}\log(en)^{11/10}.
\tag{2}
\]

Here P_t^Q is Neumann heat and P_t^T is periodic heat. In particular, if

\[
d_k^Q(a)=k\mathbb E W_{2,Q}^2(P_a^Q\nu_k,\nu_k),\qquad d_0^Q(a)=0,
\]

then, for K distributed as Bin(n,m^(-2)),

\[
\left|d_n^\Omega(n^{-5/6})-\mathbb E d_K^Q(m^2n^{-5/6})\right|
\le C n^{-1/60}\log(en)^{11/10}.
\tag{3}
\]

This improves the power in the corresponding equal-mass subdivision estimate, Lemma 4.1 of Yunzong Xu, *Random Matching Between Distinct Distributions in Two Dimensions*, [arXiv:2610.40509v1](https://arxiv.org/html/2610.40509v1#S4.SS1). The proof below develops the flat-grid repair construction with a smaller density tolerance. Neither a matching constant nor an asymptotic matching theorem is assumed.

## 1. Cell estimates and a transport bound

On a cell B=[a,a+ell] x [b,b+ell], an orthonormal Neumann basis in L^2(B,dx) is

\[
\psi_{k,l}(x)=\ell^{-1}c_kc_l
\cos\frac{\pi k(x_1-a)}\ell\cos\frac{\pi l(x_2-b)}\ell,
\quad c_0=1,\quad c_j=\sqrt2\ (j>0).
\]

Its eigenvalues are lambda_{k,l}=pi^2(k^2+l^2)/ell^2. The zero eigenfunction is omitted in every norm below. In particular, |psi_{k,l}|<=2/ell. Counting the 2r+1 quadrant pairs with max(k,l)=r gives, for s=1/n and all sufficiently large n,

\[
\sup_{B,x\in B}\sum_{j>0}\frac{e^{-2s\lambda_{B,j}}}{\lambda_{B,j}}
\psi_{B,j}(x)^2\le C\log(en).
\tag{4}
\]

Indeed, the sum is bounded by a constant times sum_{r>=1} e^(-c s r^2/ell^2)/r. Split at r=ell/sqrt(s); the lower part is a harmonic sum and the upper part is bounded by its Gaussian integral plus a constant. Integrating (4) also bounds the corresponding trace, summed over the finitely many cells.

Reflection of x+G, with G a centered Gaussian of covariance 2a I, realizes the cell heat kernel at time a. The folding function on an interval is 1-Lipschitz. Consequently

\[
\int_B|x-y|^2p_a^B(x,y)\,dy\le4a.
\tag{5}
\]

For completeness, the one-dimensional kernel is the sum over integer j of

\[
g_a(x-y+2j\ell)+g_a(x+y-2a_B+2j\ell),
\quad g_a(z)=(4\pi a)^{-1/2}e^{-z^2/(4a)},
\]

where a_B is the left endpoint. Its two-dimensional product, and the derivative of that product, satisfy

\[
\sup p_t^B\le C/t,\qquad \sup|\nabla_xp_t^B|\le C/t^{3/2}
\quad(0<t\le\ell^2).
\tag{6}
\]

These bounds follow by differentiating the Gaussian and summing its images: at spacing 2ell and t<=ell^2 the image tails are uniformly bounded Gaussian series.

If a signed measure f has zero mass on every cell, define

\[
\|f\|_{-1,\mathcal B}^2
=\sum_B\sum_{j>0}\frac{|f(\psi_{B,j})|^2}{\lambda_{B,j}}.
\]

Suppose h dx and q dx have the same masses in every cell, h>=0, and q>=a_0>0. Then

\[
\sum_B\operatorname{OT}_B(h\,dx,q\,dx)
\le\frac4{a_0}\|(h-q)dx\|_{-1,\mathcal B}^2.
\tag{7}
\]

To see this, solve -Delta u=h-q in each cell with zero mean and Neumann boundary condition. For 0<=theta<1 put A(theta)=1-(1-theta)^2,

\[
\rho_\theta=q+A(\theta)(h-q),\qquad J_\theta=A'(\theta)\nabla u.
\]

Then partial_theta rho_theta+div J_theta=0, J has zero normal flux, and rho_theta>=a_0(1-theta)^2. Its transport action is at most

\[
\int_0^1\int\frac{|J_\theta|^2}{\rho_\theta}
\le\frac4{a_0}\int|\nabla u|^2
=\frac4{a_0}\|(h-q)dx\|_{-1,\mathcal B}^2.
\]

The dynamic upper bound for squared transport cost proves (7), cell by cell. Smooth positive approximations, followed by lower semicontinuity, give the same bound for nonnegative L^2 densities. All applications below have L^2 densities. This use of the dynamic action inequality, cyclical monotonicity, and existence of semidiscrete optimal potentials are standard basic facts about quadratic transport.

## 2. Concentration and a rough cost estimate

Fix a sufficiently large constant A, independent of n, and set

\[
\delta^2=\frac{A\log(en)}{nt},\qquad
E=\{\|q-1\|_\infty\le\delta\}.
\tag{8}
\]

For sufficiently large n, delta<=1/2. Kernels are taken relative to dx on each cell, not relative to its normalized probability measure. Extend p_t^B(x,.) by zero outside B. Its mean under uniform sampling on Q is 1, its supremum is at most C/t, and its second moment is at most C/t. Thus Bernstein's inequality gives, for a fixed x in B and 0<delta<=1/2,

\[
\mathbb P(|q(x)-1|>\delta/2)\le2e^{-c nt\delta^2}.
\]

By (6), q is C t^(-3/2)-Lipschitz within each closed cell. Use a net of mesh c delta t^(3/2) separately in each cell, with at most C delta^(-2)t^(-3) points in total. Its union bound yields

\[
\mathbb P(E^c)\le C\delta^{-2}t^{-3}e^{-c nt\delta^2}\le Cn^{-10}.
\tag{9}
\]

The last inequality holds by taking A large: delta^(-2)t^(-3)<=C n^(8/3), while exp(-c nt delta^2)=(en)^(-cA). A choice with cA>13 is sufficient after adjusting constants. Piecewise jumps at cell boundaries cause no problem because the nets and the supremum are cellwise. Values on boundaries are irrelevant to transport; the estimates hold for each one-sided continuous representative.

The following bound is needed without assuming any matching asymptotic:

\[
\mathbb E Z_{n,m}\le C\log(en).
\tag{10}
\]

On E compare nu_n first with S_s nu_n and then with q dx, always within cells. By (5), the first squared cost is at most 4s. For the second use (7) with a_0=1/2. The square root of the sum of squared cell costs obeys the triangle inequality: glue couplings separately in each cell and apply Minkowski to their disjoint union. This gives

\[
Z_{n,m}/n\le8s+16\|S_s\nu_n-S_t\nu_n\|_{-1,\mathcal B}^2
\quad\hbox{on }E.
\]

For any deterministic f of global mean zero, equal-weight independence gives

\[
n\mathbb E\nu_n(f)^2=\|f\|_2^2.
\tag{11}
\]

Every positive cell eigenfunction, extended by zero, has global mean zero and L^2 norm 1. Since s<=t,

\[
\begin{split}
n\mathbb E\|S_s\nu_n-S_t\nu_n\|_{-1,\mathcal B}^2
&=\sum_{B,j>0}\frac{(e^{-s\lambda_{B,j}}-e^{-t\lambda_{B,j}})^2}{\lambda_{B,j}}\\
&\le\sum_{B,j>0}\frac{e^{-2s\lambda_{B,j}}}{\lambda_{B,j}}
\le C\log(en).
\end{split}
\]

This controls the expectation restricted to E as well. On E^c, each cell can couple its own two restrictions at squared cost at most 2ell^2 times its mass, so Z_{n,m}<=2n. Equation (9) proves (10). This also handles empty cells.

## 3. The torus optimal potential

Regard q dx and nu_n as measures on T. Write

\[
D=W_{2,T}^2(q\,dx,\nu_n).
\]

The heat coupling and (5) give D<=4t deterministically. Cellwise transport is feasible on T, so nD<=Z_{n,m} and, by (10), n E D<=C log(en).

On E let T_0(x)=x+v(x) modulo Z^2 be the optimal map, where v=grad phi, phi is periodic, and integral phi dx=0. Choose the shortest displacement. Put

\[
L=\|v\|_\infty,\qquad V=\|\phi\|_2^2,
\qquad D=\int q|v|^2dx.
\]

The elementary displacement bound is

\[
L^4\le CD,\qquad L^2\le C\sqrt t\quad\hbox{on }E.
\tag{12}
\]

Here is a direct proof of the first inequality. Take a support pair (x_0,y_0) of length R>0. On a shortest geodesic from y_0 to x_0 place nine centers at distances iR/10, i=1,...,9. Balls of radius epsilon R with epsilon=1/100 are disjoint. Each has q dx mass at least (pi/2)epsilon^2 R^2 on E. If D<(pi/2)epsilon^4 R^4, each ball contains a support pair (x_i,y_i) with distance less than epsilon R; otherwise that ball alone contributes at least this much to D. Cyclically reassign the ten targets, moving x_1 to y_0, x_i to y_{i-1}, and x_0 to y_9. All new lengths are at most R/10+3epsilon R. Their total squared cost is at most

\[
10(1/10+3/100)^2R^2=(169/1000)R^2<R^2.
\]

The original cost of these pairs is at least R^2, contradicting cyclical monotonicity. Thus D>=c R^4 for every support pair, proving (12). Torus balls here have radius below its injectivity radius, even before L is known to be small. The second bound in (12) follows from D<=4t.

For a zero-mass signed measure zeta on T define

\[
\|\zeta\|_{-2,T}^2=\sum_{j>0}\frac{|\zeta(e_j)|^2}{\lambda_j^2},
\]

using a real orthonormal torus eigenbasis. Then

\[
V\le C\{\|\nu_n-qdx\|_{-2,T}^2+(\delta^2+L^2)D\}
\quad\hbox{on }E.
\tag{13}
\]

To prove this estimate, set h=(-Delta)^(-1)phi on T. Fourier series gives ||h||_{H^2}<=C sqrt(V). For all sufficiently large n, (12) makes L smaller than a fixed fraction of the torus injectivity radius. On a piece assigned to a target y, lift the short edges to R^2. The interpolation

\[
F_u(x)=x+uv(x)=(1-u)x+uy,\qquad 0\le u<1,
\]

has Jacobian (1-u)^2. Images of different pieces are disjoint almost everywhere. Indeed, if two edges meet at the same u in (0,1), lift at their common meeting point. All four endpoints then lie within a small Euclidean chart. Cyclical monotonicity implies (x-x') dot (y-y')>=0. The meeting identity gives

\[
x-x'=-u(v-v'),\qquad y-y'=(1-u)(v-v'),
\]

so -u(1-u)|v-v'|^2>=0. Thus the edges coincide. It follows that the density of F_{u#}(qdx) is at most (3/2)(1-u)^(-2).

For smooth h, Taylor's formula along these edges and Cauchy–Schwarz give

\[
(\nu_n-qdx)(h)=\int qv\cdot\nabla h\,dx+R_h,
\qquad |R_h|\le CL\sqrt D\,\|h\|_{H^2}.
\tag{14}
\]

In detail, at time u the absolute integrated quadratic term is at most

\[
L\sqrt D\left(\int q|\nabla^2 h(F_u(x))|^2dx\right)^{1/2}
\le CL\sqrt D(1-u)^{-1}\|\nabla^2h\|_2.
\]

The Taylor weight is 1-u, so its integral over u is bounded. Smooth approximation in H^2 passes (14) to our h: H^2(T) embeds in C^0(T), so the atomic evaluations converge too.

The weak equation -Delta h=phi gives integral v dot grad h dx=V. The part involving q-1 is bounded by C delta sqrt(DV). Fourier duality gives |(nu_n-qdx)(h)|<=||nu_n-qdx||_{-2,T} sqrt(V). Equation (14) now implies

\[
V\le\sqrt V\{\|\nu_n-qdx\|_{-2,T}+C(\delta+L)\sqrt D\},
\]

which proves (13), including the case V=0.

## 4. Cancellation of the sample and its cellwise smoothing

Set zeta=nu_n-S_t nu_n. For deterministic h in L^2(T), self-adjointness and preservation of dx give

\[
\zeta(h)=\nu_n((I-S_t)h),\qquad
n\mathbb E\zeta(h)^2=\|(I-S_t)h\|_2^2.
\tag{15}
\]

The direct-sum Neumann form has domain consisting of functions that are H^1 within each cell. For globally H^1 functions its energy is exactly integral |grad h|^2 dx. Spectral calculus in each cell gives

\[
\|(I-S_t)h\|_2^2\le\min\{\|h\|_2^2,t\|\nabla h\|_2^2\}.
\]

Apply this to the global eigenfunctions in (15). The torus eigenvalues are 4pi^2|k|^2, k in Z^2 except zero. Tonelli's theorem and lattice-shell counting yield

\[
n\mathbb E\|\zeta\|_{-2,T}^2
\le\sum_{j>0}\frac{\min(1,t\lambda_j)}{\lambda_j^2}
\le Ct\log(e/t).
\tag{16}
\]

For the last inequality split the lattice at |k|=t^(-1/2). The inner shells contribute at most Ct sum_{r<=t^(-1/2)}1/r; the outer shells contribute at most C sum_{r>t^(-1/2)}r^(-3)<=Ct.

Combining (10), (12), (13), and (16) gives

\[
n\mathbb E[V1_E]
\le C\{t\log(e/t)+(\delta^2+\sqrt t)\log(en)\}
\le C\delta^2\log(en).
\tag{17}
\]

Here sqrt(t)=n^(-5/12) is smaller than delta^2=A n^(-1/6)log(en), and t log(e/t)<=C delta^2 log(en). No covariance formula has been conditioned on E: (15)–(16) are unconditional, and only inequalities are restricted to E.

## 5. Repairing transport near the grid

Choose

\[
r=(\delta^2)^{1/5}=A^{1/5}n^{-1/30}\log(en)^{1/5}.
\tag{18}
\]

For sufficiently large n, r is smaller than ell/16, and (12) implies L<r/2 on E. Let eta be a smooth periodic function, equal to 1 within distance r of the grid and zero beyond distance 2r, with 0<=eta<=1. Products of one-dimensional cutoffs along the finitely many vertical and horizontal grid lines give

\[
\kappa:=|\operatorname{supp}\eta|\le Cr,\qquad
|\nabla\eta|\le C/r,\qquad |\nabla^2\eta|\le C/r^2.
\tag{19}
\]

The seams at the physical square boundary are included. In particular this construction applies when m=1.

Put xi=1-eta and omega=xi composed with T_0. Work on E for the following construction. Reverse the optimal torus allocation, returning the fraction xi(y) at target y to its original source points. Since xi(y)>0 only when y is more than r from the grid and L<r/2, every retained edge stays in the same Euclidean cell. The retained reverse transport ends at

\[
\sigma_0=\eta\nu_n+\omega qdx.
\]

Its cost is at most D, and its mass in every cell is nu_n(B). Smooth just the remaining atomic mass at time s:

\[
\sigma_s=S_s(\eta\nu_n)+\omega qdx.
\]

This second transport stays within cells and costs at most 4s nu_n(eta), by (5). Both sigma_s and qdx have mass nu_n(B) in every cell. Apply (7) to their final transport, obtaining

\[
\sqrt{Z_{n,m}/n}\le\sqrt D+2\sqrt{s\nu_n(\eta)}
+\sqrt8\|\sigma_s-qdx\|_{-1,\mathcal B}.
\tag{20}
\]

It remains to control the last norm. Define cellwise centering by

\[
(\mathcal Z f)|_B=f|_B-\frac{f(B)}{|B|}dx|_B.
\]

The sum sigma_s-qdx is already centered in each cell. Its decomposition is

\[
\sigma_s-qdx=U+W+\mathcal Z[q(\omega-\xi)dx],
\quad U=\mathcal Z S_s[\eta(\nu_n-qdx)],\quad
W=(S_s-I)(\eta q)dx.
\tag{21}
\]

Indeed, before centering the first two terms sum to S_s(eta nu_n)-eta qdx, and adding q(omega-xi)dx gives sigma_s-qdx. Heat preserves cell mass, so W already has zero cell masses.

For the first term, (15) applied to eta psi_{B,j}, extended by zero, gives the unconditional identity

\[
n\mathbb E\|U\|_{-1,\mathcal B}^2
=\sum_{B,j>0}\frac{e^{-2s\lambda_{B,j}}}{\lambda_{B,j}}
\|(I-S_t)(\eta\psi_{B,j})\|_2^2.
\]

The operator I-S_t is an L^2 contraction. Equation (4) therefore implies

\[
n\mathbb E\|U\|_{-1,\mathcal B}^2\le C\kappa\log(en).
\tag{22}
\]

For the second term, (1-e^(-s lambda))^2/lambda<=s gives

\[
n\mathbb E[\|W\|_{-1,\mathcal B}^2 1_E]
\le ns\mathbb E[\|\eta q\|_2^2 1_E]\le C\kappa.
\tag{23}
\]

For the last term, Taylor expansion of xi along the short edges yields

\[
q(\omega-\xi)=\operatorname{div}(\phi\nabla\xi)-\phi\Delta\xi
+(q-1)\nabla\xi\cdot v+qR,
\qquad |R|\le Cr^{-2}|v|^2.
\tag{24}
\]

The vector field phi grad xi vanishes near every cell boundary. Integration by parts bounds its divergence in the cellwise H^(-1) norm by ||phi grad xi||_2. For an L^2 density g, cellwise centering satisfies ||Z(gdx)||_{-1,B}<=C||g||_2 by the cell Poincaré inequality. Apply these facts to the four terms of (24). Since q lies in [1/2,3/2] on E and r<=1, they give

\[
\|\mathcal Z[q(\omega-\xi)dx]\|_{-1,\mathcal B}^2
\le C\{r^{-4}V+\delta^2r^{-2}D+r^{-4}L^2D\}.
\tag{25}
\]

For example, the squared L^2 norm of qR is at most C r^(-4)L^2 D. The divergence term gives C r^(-2)V, which is bounded by C r^(-4)V. Thus no differentiability of q or of v across allocation interfaces is needed in (24)–(25).

Using (10), (12), and (17) in (22)–(25), and using sqrt(t)<=delta^2, gives

\[
n\mathbb E[\|\sigma_s-qdx\|_{-1,\mathcal B}^2 1_E]
\le C\{\kappa+r^{-4}\delta^2\}\log(en)
\le Cr\log(en).
\tag{26}
\]

The last step uses r^5=delta^2. Also E nu_n(eta)=integral eta dx<=kappa, so ns E nu_n(eta)<=kappa<=Cr.

Write A_n=2 sqrt(s nu_n(eta))+sqrt(8)||sigma_s-qdx||_{-1,B} on E. Squaring (20) gives

\[
0\le Z_{n,m}-nD\le2n\sqrt D A_n+nA_n^2\quad\hbox{on }E.
\]

The lower bound holds because every cellwise plan is feasible on T. Equations (10) and (26), followed by Cauchy–Schwarz, show that the expectation of the right side restricted to E is at most

\[
C\sqrt r\log(en)+Cr\log(en)\le C\sqrt r\log(en).
\]

On E^c use 0<=Z_{n,m}-nD<=2n and (9). We have proved

\[
0\le\mathbb E(Z_{n,m}-nD)
\le C n^{-1/60}\log(en)^{11/10}.
\tag{27}
\]

For the square cost with the same q, the pointwise sandwich

\[
D\le W_{2,Q}^2(qdx,\nu_n)\le Z_{n,m}/n
\tag{28}
\]

gives the identical expected repair bound.

## 6. Replacing cellwise heat by global heat

Couple the two heat kernels starting at x by the same free Gaussian increment G of covariance 2t I, folding within the cell for S_t and folding globally or reducing periodically for P_t^Omega. The endpoints coincide whenever x+G stays in the cell. If b(x) is the distance from x to the grid, their squared separation is therefore at most

\[
4|G|^2 1_{\{|G|\ge b(x)\}}.
\]

The bound holds because each folded endpoint is within |G| of x in its respective metric; for Omega=Q the global folding map is 1-Lipschitz, and for Omega=T use torus distance. Gaussian integration bounds the expected separation by Ct exp(-c b(x)^2/t). The grid has bounded total length, so

\[
\int_Qe^{-c b(x)^2/t}dx\le C\sqrt t.
\]

Average over the uniform target positions and use the resulting mixture as a transport coupling. Then

\[
\Delta:=n\mathbb E W_{2,\Omega}^2(P_t^\Omega\nu_n,qdx)
\le Cnt^{3/2}=Cn^{-1/4}.
\tag{29}
\]

If a=W_{2,Omega}(P_t^Omega nu_n,nu_n), b=W_{2,Omega}(qdx,nu_n), and c=W_{2,Omega}(P_t^Omega nu_n,qdx), the triangle inequality implies |a^2-b^2|<=c^2+2bc. Since nb^2<=Z_{n,m}, Cauchy–Schwarz and (10) give

\[
n\mathbb E|a^2-b^2|\le\Delta+2\sqrt{\Delta\mathbb E Z_{n,m}}
\le Cn^{-1/8}\log(en)^{1/2}.
\tag{30}
\]

This is smaller than the right side of (27). Combining (27)–(30) proves (2) for sufficiently large n. For the finitely many other n>=2, both costs are bounded by 2n, so increasing C proves (2) as stated.

## 7. Rescaling and checks of the rate

Conditional on K_B=k>0, the sites in B are independent uniform there, each with its original mass 1/n. The cell mass is k/n. Scaling B to Q multiplies squared distances by ell^(-2) and heat time by ell^(-2). Its conditional expected contribution to Z_{n,m} is consequently

\[
n(k/n)\ell^2\frac{d_k^Q(t/\ell^2)}k
=\ell^2d_k^Q(m^2t).
\]

For k=0 it is zero. Summing over m^2 identically distributed cells proves E Z_{n,m}=E d_K^Q(m^2t). Equation (3) follows from (2) and |E X|<=E|X|.

There are two ways to check the dominant rate. Direct substitution in (26) gives r^(-4)delta^2=r, so (27) is sqrt(r)log(en)=A^(1/10)n^(-1/60)log(en)^(11/10). Alternatively, ignore the smaller sqrt(t) term and put r=n^(-b)log(en)^c. The two terms in the squared repair error have orders

\[
r=n^{-b}\log(en)^c,\qquad
r^{-4}\delta^2=A n^{4b-1/6}\log(en)^{1-4c}.
\]

Balancing powers gives b=1/30 and c=1/5; taking the square root and multiplying by log(en) recovers 1/60 and 11/10. The second check does not use the substitution r^5=delta^2.

Other necessary inequalities have strict power margins: sqrt(t)=n^(-5/12)=o(delta^2); L=O(n^(-5/24))=o(r); and the global heat comparison has power 1/8>1/60. The concentration prefactor has power 8/3 and is dominated by (en)^(-cA). The auxiliary time is s=1/n<=t. Corners and grid intersections are covered by smooth products in (19); no boundary flux occurs in (25). The construction preserves cell masses before applying the H^(-1) estimate. In particular, it does not replace cell masses by their means, condition a covariance identity on E, or substitute a two-sample covariance factor.

The theorem proves a sharper subdivision estimate. To infer a full second-order matching formula one still needs a valid semidiscrete-to-smoothing reduction and the sample-size/time comparison. Those separate arguments are not asserted here as independently verified theorems. No numerical value of the universal equal-mass constant is obtained.
