# The zero-endpoint derivative quadrature

Source: OpenAI, *Subpolynomial query complexity for well-conditioned log-concave sampling*, September 26, 2026. This checks Lemma 6.3, `lem:kernel-endpoint-quadrature`, in [numerics.tex](sources/reopened-round6/numerics.tex), and its time-derivative input from Lemma 5.1 in [centering.tex](sources/reopened-round6/centering.tex).

The result is a local implication. The transported-path jet estimate `eq:path-jet` in [Section 4](sources/preprints/Subpolynomial-query-complexity-for-well-conditioned-log-concave-sampling-September-26-2026/build/sections/divergence.tex) and the exact probability-transport law are inputs. The high-moment tensor-divergence theorem that supplies that jet estimate is not proved here. No conclusion about the complete sampler follows from this check alone.

## 1. Recheck of the preceding harmonic result

For a law proportional to exp(−S) with bounded Hessian, write D*V=−div V+DS·V. Two integrations by parts, first for compactly supported fields and then by cutoff, give

\[
 \|D^*V\|_2^2
 =\mathbb E\sum_{i,j}(\partial_iV_j)(\partial_jV_i)
  +\mathbb E V^T(D^2S)V
 \le \|DV\|_{F,2}^2+\|D^2S\|_{\mathrm{op},\infty}\|V\|_{F,2}^2.
 \tag{1}
\]

This also holds componentwise for tensor output. Let A be the constant harmonic skew matrix, and let L=D*AD. Starting from spatial derivative bounds \(\|D^j\phi\|_{F,2}\le C_j a_0\sqrt d R^{-(j-1)}\), j≥1, induction gives

\[
 \|D^j L^k\phi\|_{F,2}
 \le C_{j,k}a_0\sqrt d R^{-(j+2k-1)},\qquad k\ge1,\ j\ge0.
 \tag{2}
\]

Indeed, set V=AD L^(k−1)φ. At derivative order h its bound has inverse-R exponent h+2k−2, including k=1 by the spatial hypothesis. Commuting j derivatives through D*, the principal divergence term uses V at orders j and j+1 in (1), hence costs at most j+2k−1. A commutator with v≥1 derivatives on the score has exponent (v−1)+(j−v+2k−2)=j+2k−3, using the stated one-slot score bounds. It is smaller because R≤1. There are finitely many terms for fixed j,k. This proves (2). Stationarity then turns (2) into a bound on each fixed-time RMS derivative along the harmonic trajectory.

With ψ=δ^(4t), R=δ^t, the angle-stencil remainder is proportional to ψ^(m−1)R^(−(2m−1))=δ^(2tm−3t); harmonic interpolation gives ψ^m R^(−(2m−1))=δ^(2tm+t). Thus the preceding conditional result holds. This recheck uses no supremum over a random path and no stationarity of approximate states.

## 2. The time-derivative input and its exact scope

Use the paper's notation a=1−ρ², L=λr, l=rL≤1/2. Put

\[
 Y_\rho(y)=T_{\rho\to b_*}^{-1}(y),\quad
 B_\rho(y)=(D_yY_\rho(y))^{-1},\quad b_*=\sqrt{1-R^2}.
\]

Assume the exact transport sends y∼ξ_* to Yρ(y)∼ξρ, and assume the Section 4 estimate, for each fixed j and fixed finite p≥2,

\[
 \bigl\|\|\mathcal D^j U_1\|_{\mathrm{op}}\bigr\|_{L^p(\xi_\rho)}
 \le P_{j,p}(d)L a^{-j},\qquad
 \mathcal D=\partial_\rho-rM_\rho\cdot D.
 \tag{3}
\]

Each P is a fixed power of 1+log d, with constants independent of center, primitive scale and ρ. Assume also the source's spatial bound r‖DMρ‖op≤Cl. The Jacobian equation gives

\[
 B'_\rho=B_\rho C_\rho,\qquad
 C_\rho=rDM_\rho(Y_\rho)=r\rho U_1(\rho,Y_\rho),\qquad B_{b_*}=I.
 \tag{4}
\]

Gronwall on an interval of length at most one gives ‖Bρ‖op≤exp(Cl)≤C, uniformly in y. The multiplication order in (4) follows directly by differentiating Jρ^−1 with Jρ'=−rDMρ Jρ: Bρ'=−Jρ^−1Jρ'Jρ^−1=rBρDMρ.

For j≥1, differentiating C along this path gives exactly

\[
 C_\rho^{(j)}
 =r\rho(\mathcal D^jU_1)(\rho,Y_\rho)
   +rj(\mathcal D^{j-1}U_1)(\rho,Y_\rho).
 \tag{5}
\]

For j=0 there is only the first term. Therefore (3), the marginal identity, and a≤1 imply

\[
 \bigl\|\|C_\rho^{(j)}\|_{\mathrm{op}}\bigr\|_{L^p(y\sim\xi_*)}
 \le P_{j,p}(d)l a^{-j}.
 \tag{6}
\]

Repeated differentiation of (4), without commuting matrices, expresses Bρ^(m), m≥1, as a finite sum of ordered words

\[
 c\,B_\rho C_\rho^{(j_1)}\cdots C_\rho^{(j_k)},\qquad
 k\ge1,\quad j_i\ge0,\quad \sum_i j_i=m-k.
 \tag{7}
\]

This description follows by induction: differentiating B inserts C^(0) immediately after B; differentiating another factor increases one j by one. Both operations increase m by one and preserve the displayed identity. The coefficients and the finite number of words depend only on m. Hölder at moment order kp and (6) bound each word by P(d)l^k a^(−(m−k)). Since l≤1 and a≤1, it follows that

\[
 \bigl\|\|B_\rho^{(m)}\|_{\mathrm{op}}\bigr\|_{L^p(\xi_*)}
 \le P_{m,p}(d)l a^{-(m-1)}
 \le P_{m,p}(d)l a^{-m}.
 \tag{8}
\]

This derives Lemma 5.1's conservative time estimate from its actual stated input, with an additional unused power a. It does not prove input (3).

Now draw G∼N(0,I_d) independently of y, and set F(ρ)=(Bρ(y)−I)G, viewed as a vector in the Hilbert space H=L²(y,G;R^d). Gaussian conditioning gives, for every matrix A(y),

\[
 \mathbb E_{y,G}|A(y)G|^2
 =\mathbb E_y\|A(y)\|_F^2
 \le d\,\mathbb E_y\|A(y)\|_{\mathrm{op}}^2.
 \tag{9}
\]

Thus (8) with p=2 implies ‖F^(m)(ρ)‖H≤K(1−ρ²)^−m, where K=P_m(d)l√d. Also F'(0)=0 exactly, from (4) and its factor ρ. Smoothness on every compact interval below one follows from the source's Gaussian conditional-integral regularity. Its polynomial growth and Gaussian tails justify these fixed-order Hilbert-space differentiations. No bound on the size of the uncentered gradient is inserted in (8)–(9).

## 3. A Hilbert-space quadrature statement

Fix m≥3 and 0<h≤1/4. Let b∈(0,1), T=−log(1−b), and suppose T≥h. Set n=ceil(T/h), Δ=T/n, and mesh endpoints

\[
 x_j=1-e^{-j\Delta},\qquad 0\le j\le n.
\]

Then h/2≤Δ≤h. For a cell [a_c,b_c] with length ℓc,

\[
 \ell_c=(e^\Delta-1)(1-b_c),\qquad
 c h(1-\rho)\le\ell_c\le 2h(1-b_c)
 \quad(a_c\le\rho\le b_c),\qquad
 c h\le\ell_0\le h.
 \tag{10}
\]

Here c>0 is absolute. To check the lower inequalities, use e^Δ−1≥Δ≥h/2, 1−ρ≤e^Δ(1−b_c), and 1−e^−Δ≥Δe^−Δ. The upper inequalities use e^h−1≤2h and 1−e^−Δ≤Δ. In the source b=√(1−R²) with R→0, so T≥h for sufficiently large dimension. A zero interval has zero quadrature and zero error.

Let F:[0,b]→H be C^m, with

\[
 F'(0)=0,\qquad \|F^{(m)}(\rho)\|_H\le K(1-\rho^2)^{-m}.
 \tag{11}
\]

On each ordinary cell interpolate F at m equally spaced value nodes including both endpoints, to degree at most m−1. On the first cell use m−1 equally spaced value nodes including both endpoints and impose the additional condition (IF)'(0)=0. Write IF for the resulting piecewise interpolant. The m first-cell conditions are unisolvent: a homogeneous polynomial would have a double zero at zero and the m−2 other distinct value zeros, exceeding its allowed degree unless it vanishes.

Define

\[
 \mathcal Q_hF=\sum_c\int_{a_c}^{b_c}(IF)'(\rho)\,\frac{d\rho}{\rho}.
\]

Then

\[
 \left\|\int_0^bF'(\rho)\,\frac{d\rho}{\rho}-\mathcal Q_hF\right\|_H
 \le C_m K h^{m-1}.
 \tag{12}
\]

The constant is independent of b. In particular, it needs no additional logarithm of R or h. The integral itself exists at zero since F'(0)=0 and F'' is continuous there.

## 4. Proof of the quadrature error

First consider an ordinary cell I=[a_c,b_c]. Subtract the Taylor polynomial P of degree m−1 at a_c. The integral remainder and (11) give

\[
 \|F(v)-P(v)\|_H
 \le C_m K\ell_c^m(1-b_c^2)^{-m},\qquad v\in I.
\]

The scaled Lagrange basis has bounded absolute value sum depending only on m. Interpolation reproduces P, so the error E=F−IF satisfies

\[
 \|E(v)\|_H
 \le C_m K\ell_c^m(1-b_c^2)^{-m}
 \le C_m K h^m.
 \tag{13}
\]

The last inequality is (10) and 1−b_c²≥1−b_c. Both cell endpoints are value nodes, so E(a_c)=E(b_c)=0. Hilbert-space integration by parts therefore yields

\[
 \int_{a_c}^{b_c}\frac{E'(\rho)}\rho\,d\rho
 =\left[\frac{E(\rho)}\rho\right]_{a_c}^{b_c}
   +\int_{a_c}^{b_c}\frac{E(\rho)}{\rho^2}\,d\rho
 =\int_{a_c}^{b_c}\frac{E(\rho)}{\rho^2}\,d\rho.
 \tag{14}
\]

Sum (14) over the ordinary cells and use Minkowski, (13), and x₁=ℓ₀≥ch:

\[
 \left\|\sum_{c\ge1}\int_{a_c}^{b_c}\frac{E'}\rho\,d\rho\right\|_H
 \le C_m K h^m\int_{x_1}^{b}\rho^{-2}\,d\rho
 \le C_m K h^m/x_1
 \le C_m K h^{m-1}.
 \tag{15}
\]

With no ordinary cells the left side is zero. The boundary cancellation is essential: estimating the derivative error directly would instead produce logarithms.

On the first cell [0,ℓ₀], subtract the degree-(m−1) Taylor polynomial P at zero. It satisfies P'(0)=0. Since ℓ₀≤h≤1/4, (11) bounds F^(m) there by C_mK. For V=F−P, Taylor's formula gives ‖V‖H≤C_mKℓ₀^m and ‖V''‖H≤C_mKℓ₀^(m−2), uniformly on the cell. The Hermite interpolant of V has derivative zero at zero. Scaling its fixed value bases to the unit cell shows

\[
 \|(IV)''\|_H\le C_m\ell_0^{-2}\max_{\rm nodes}\|V\|_H
 \le C_mK\ell_0^{m-2}.
\]

Thus E=V−IV obeys E(0)=E'(0)=0 and

\[
 \|E''(v)\|_H\le C_mK\ell_0^{m-2},\qquad
 \|E'(\rho)\|_H\le C_mK\rho\ell_0^{m-2}.
\]

Consequently

\[
 \left\|\int_0^{\ell_0}\frac{E'(\rho)}\rho\,d\rho\right\|_H
 \le C_mK\ell_0^{m-1}\le C_mK h^{m-1}.
 \tag{16}
\]

Equivalently, E(ρ)/ρ→0 at zero and E(ℓ₀)=0, so (14) also applies on this cell. Equations (15)–(16) prove (12). The argument uses deterministic bounds on RMS norms; it never takes a supremum of a random path.

## 5. Weight norm and arbitrary approximate values

The quadrature is a linear combination of values, \(\mathcal Q_hF=\sum_iq_i F(\rho_i)\). On an ordinary cell, derivatives of the scaled value bases have absolute sum at most C_m/ℓc. Hence (10) gives the weight bound

\[
 \sum_{\rm ordinary}|q_i|
 \le C_mh^{-1}\int_{x_1}^{b}\frac{d\rho}{\rho(1-\rho)}.
\]

For b=√(1−R²), use 1−b=R²/(1+b), x₁≥ch, and the antiderivative log ρ−log(1−ρ). The right side is at most C_mh^−1(1+|log R|+|log h|). On the first cell each unit-cell Hermite value basis H_i has H_i'(0)=0, so H_i'(u)/u is a polynomial. Its integrated weight is

\[
 q_i=\ell_0^{-1}\int_0^1 H_i'(u)\,\frac{du}{u}.
\]

There are only m−1 such bases and their coefficients depend only on m. Their absolute weights sum to at most C_m/ℓ₀≤C_m/h. Combining the two parts reproduces the source's weight norm.

For arbitrary approximate values \(\widehat F_i=F(\rho_i)+e_i\), including separately labeled copies of a shared endpoint,

\[
 \left\|\sum_iq_i e_i\right\|_H
 \le\sum_i|q_i|\|e_i\|_H.
 \tag{17}
\]

No independence or endpoint consistency of these errors is required. The interpolating polynomial imposes its derivative condition exactly. An ordinary first-cell interpolant with a nonzero derivative at zero would have a divergent weighted derivative integral, even if its derivative error were arbitrarily small. The sharper *exact-value* truncation bound (12) does not remove the h^−1 amplification of arbitrary nodal errors.

## 6. Failure checks and the attainable abstract order

Both endpoints are used on every ordinary cell. If an endpoint is omitted, its E/ρ boundary term in (14) must be retained and the proof of (12) no longer applies. Likewise F'(0)=0 is needed for the exact integral, and the identical zero slope of its Hermite interpolant is needed for the approximate integral. These conditions are present in the source.

The h^(m−1) order cannot in general be improved under (11) alone. Let u_i=i/(m−2), 0≤i≤m−2, be the first-cell value nodes in unit coordinates, and put

\[
 q(u)=u^{m+1}(1-u)^{m+1}\prod_{i=1}^{m-3}(u-u_i)^2,\qquad
 F_h(\rho)=
 \begin{cases}
  \ell_0^m q(\rho/\ell_0),&0\le\rho\le\ell_0,\\
  0,&\ell_0<\rho\le b.
 \end{cases}
 \tag{18}
\]

The empty product for m=3 is one. At both cell endpoints q vanishes to order m+1, so F_h is C^m when extended by zero. Its mth derivative is bounded by a constant K_m independent of h, satisfying (11) with K=K_m. Its first derivative vanishes at zero. Every sampled value on the entire mesh is zero, including the first-cell internal nodes, so its quadrature is zero. However, integration by parts gives

\[
 \int_0^b\frac{F_h'(\rho)}\rho\,d\rho
 =\ell_0^{m-1}\int_0^1\frac{q'(u)}u\,du
 =\ell_0^{m-1}\int_0^1\frac{q(u)}{u^2}\,du
 =c_m\ell_0^{m-1}>0.
 \tag{19}
\]

Positivity follows since q≥0 and is positive away from finitely many zeros in (0,1). As ℓ₀≥ch, (19) rules out a uniform o(h^(m−1)) estimate on this derivative-bounded class. This is an abstract quadrature example; it is not asserted to arise from the sampler's Bρ. It neither disproves nor certifies any sampling theorem.

## 7. Consequence for Lemma 6.3

Taking H=L²(y,G;R^d), F=(Bρ−I)G and K=P_m(d)l√d in (12) proves

\[
 \left\|\int_0^{b_*}B_\rho'(y)G\,\frac{d\rho}{\rho}
             -\sum_iq_i(B_{\rho_i}(y)-I)G\right\|_2
 \le C_m P_m(d)l\sqrt d\,h_0^{m-1}.
 \tag{20}
\]

This improves the displayed h₀^(m−2) in Lemma 6.3 by one factor h₀, conditional on (3) and the exact transport/spatial inputs. The weaker source bound follows because h₀≤1. In the kernel velocity, division by rs changes this exact quadrature term to at most C_mP_m(d)(L/σ)√d h₀^(m−1), since l=rL and s=σ/2. The value-error weight norm and all other numerical and compiler errors retain their own estimates. No final query exponent, general condition-number result, or accuracy tradeoff is established here.
