# Conditional trace identities for derivative-dependent orthogonal layers

Finite-width conditional trace identities yield joint-limit empirical concentration after an explicit scalar normalization. No full spectral density or isometry theorem at fixed critical initialization is asserted. All matrices and vectors are real.

## 1. The conditional model

Let n >= 3, let X be a fixed symmetric positive semidefinite n by n matrix, and let e be a fixed unit vector. Let O be Haar on O(n), put u=Oe, and let A=A(u) be any measurable nonnegative diagonal matrix. Define

\[
 B=OXO^\top,\qquad X'=A^{1/2}BA^{1/2}.
\]

All formulas below hold whenever the displayed expectations are finite; bounded A suffices. A deterministic multiplicative gain is included in A.

This is the conditional law of an actual orthogonal tanh layer. If the previous activation h is nonzero, set e=h/\|h\|, let the weight matrix be gO, and put q=g^2\|h\|^2/n. Then the preactivation is \(\sqrt{nq}\,u\), the layer Jacobian is \(g\operatorname{diag}(\operatorname{sech}^2(\sqrt{nq}\,u_i))O\), and

\[
 A_{ii}=g^2\operatorname{sech}^4(\sqrt{nq}\,u_i).
\]

Condition on the entire previous network, so X is its Jacobian Gram matrix and O is fresh. There is no independence assumption between A and O. One may also condition on an independent bias vector and allow A to depend on that vector. The small-q results below concern zero bias.

Use the invariants

\[
 T=\operatorname{Tr}X,\quad Q=\operatorname{Tr}X^2,\quad
 \alpha=e^\top Xe,\quad \gamma=e^\top X^2e,\quad
 \beta=\gamma-\alpha^2,\quad m=n-1,
\]

\[
 T_0=T-\alpha,\qquad Q_0=Q-\alpha^2-2\beta.
\]

Define

\[
 c=\frac{(m+1)T_0^2-2Q_0}{m(m-1)(m+2)},\qquad
 d=\frac{mQ_0-T_0^2}{m(m-1)(m+2)}.                 \tag{1}
\]

For each u and its gate A, write

\[
 k=\operatorname{Tr}A,\quad h=\operatorname{Tr}A^2,\quad
 s=u^\top Au,\quad r=u^\top A^2u,
\]

\[
 p=k-s,\qquad w=h-2r+s^2,\qquad z=r-s^2.          \tag{2}
\]

The letter z here is a one-layer scalar, not a preactivation or the earlier report's distortion.

**Theorem 1.** Conditional on u, expectation over the residual Haar randomness gives exactly

\[
 \mathbb E[\operatorname{Tr}X'\mid u]
 =\alpha s+\frac{T_0}{m}p,                       \tag{3}
\]

\[
 \mathbb E[\operatorname{Tr}((X')^2)\mid u]
 =\alpha^2s^2+\frac{2}{m}\{(\beta+\alpha T_0)z+\beta sp\}
 +(c+d)w+dp^2,                                  \tag{4}
\]

\[
 \mathbb E[(\operatorname{Tr}X')^2\mid u]
 =\alpha^2s^2+\frac{2\alpha T_0}{m}sp
 +\frac{4\beta}{m}z+cp^2+2dw.                    \tag{5}
\]

Equation (4) is the trace of the matrix square; (5) is the square of the trace. Averaging (3)–(5) over uniform u gives the full conditional-on-the-past identities for the network. In particular, only T,Q,alpha,gamma from the previous layer are needed, in addition to the forward radius specifying the gate.

## 2. Proof of Theorem 1

Choose an orthonormal basis whose first vector is e, and write

\[
 X=\begin{pmatrix}\alpha&b^\top\\b&H\end{pmatrix}.
\]

Then \(\|b\|^2=\beta\), \(\operatorname{Tr}H=T_0\), and \(\operatorname{Tr}H^2=Q_0\), by multiplying this block matrix and taking its trace.

For a fixed u let F be any orthonormal frame for u-perpendicular, and set P=I-uu^top=FF^top. Conditional on Oe=u, O in these input and output frames is \(\operatorname{diag}(1,R)\) with R Haar on O(m). This follows from Haar invariance under the stabilizer of e: multiplying on the right by any orthogonal map fixing e preserves the conditional law and acts transitively on the remaining frames. Consequently

\[
 B=\alpha uu^\top+uv^\top+vu^\top+C,\qquad
 v=FRb,\quad C=FRHR^\top F^\top.                 \tag{6}
\]

Rotational invariance and the fixed norm of v imply

\[
 \mathbb E v=0,\quad \mathbb E vv^\top=(\beta/m)P,
 \quad \mathbb E C=(T_0/m)P.                     \tag{7}
\]

The transformation R to -R preserves Haar measure, changes v to -v and leaves C unchanged. Hence every expectation with one v and one C vanishes, including each coordinate \(\mathbb E v_i C_{jk}\).

For completeness, the second moment of C is

\[
 \mathbb E C_{ij}C_{kl}
 =cP_{ij}P_{kl}+d(P_{ik}P_{jl}+P_{il}P_{jk}).      \tag{8}
\]

To derive it, work in the F frame, where P is the identity. Coordinate sign changes force a second-moment entry to vanish unless every index occurs an even number of times. Coordinate permutations leave three possible values: a diagonal square, a product of distinct diagonal entries, and an off-diagonal square. A 45-degree rotation in the plane of two coordinates shows that the first equals the second plus twice the third. Thus the tensor has the stated form, with coefficients c and d. Contracting respectively to the square of the trace and the trace of the square gives

\[
 T_0^2=m^2c+2md,\qquad Q_0=mc+m(m+1)d.
\]

Subtracting the first identity from m times the second gives \(mQ_0-T_0^2=m(m-1)(m+2)d\); substitution gives (1). The denominator is nonzero for n >= 3.

The definitions (2) also give

\[
 \operatorname{Tr}(AP)=p,\quad
 \operatorname{Tr}(APAP)=w,\quad u^\top APAu=z.
\]

Taking the trace of A times (6), and using (7), proves (3). For the square of that trace, the nonzero contributions are

\[
 \alpha^2s^2,\quad 2\alpha s\,\mathbb E\operatorname{Tr}(AC)
 =2\alpha sT_0p/m,
\]

\[
 4\mathbb E(u^\top Av)^2=4\beta z/m,
 \qquad \mathbb E(\operatorname{Tr}AC)^2=cp^2+2dw.
\]

Terms linear in v vanish, including the cross term with C, by the sign symmetry above. Their sum proves (5).

For the trace of the matrix square, use \(\operatorname{Tr}((X')^2)=\operatorname{Tr}(ABAB)\) and expand (6). The scalar block contributes alpha^2 s^2. The two cross terms between that block and C contribute \(2\alpha T_0 z/m\). If K=uv^top+vu^top, direct multiplication gives

\[
 \operatorname{Tr}(AKAK)
 =2(u^\top Av)^2+2s(v^\top Av).
\]

Its expectation is \(2\beta(z+sp)/m\). Finally, contraction of (8) gives

\[
 \mathbb E\operatorname{Tr}(ACAC)=(c+d)w+dp^2.
\]

All remaining cross terms contain an odd v and vanish. Summing proves (4).

## 3. A normalized tanh gate and its dependence correction

Let q >= 0 and define the spherical marginal mean

\[
 \mu_n(q)=\mathbb E_u\operatorname{sech}^4(\sqrt{nq}\,u_1),
 \qquad A_{ii}(q,u)=\frac{\operatorname{sech}^4(\sqrt{nq}\,u_i)}{\mu_n(q)}.
                                                               \tag{9}
\]

This normalization is a conditional reference calculation, not a claim that the forward network uses an adaptive gain. For an actual gain g, its A is exactly \(g^2\mu_n(q)\) times (9); multiply the right side of (3) by that scalar and those of (4),(5) by its square. The conditional radius q itself remains \(g^2\|h\|^2/n\).

**Theorem 2.** For 0 <= q <= 1/4, the normalized gate (9) obeys

\[
 \mathbb E\operatorname{Tr}X'
 =T-\frac{4q}{n+2}(n\alpha-T)+R_1,
 \qquad |R_1|\leq\frac{72q^2}{n+2}|n\alpha-T|,       \tag{10}
\]

\[
 \mathbb E\operatorname{Tr}((X')^2)
 =Q-\frac{8q}{n+2}(n\gamma-Q)+R_2,
 \qquad |R_2|\leq1344q^2 Q,                         \tag{11}
\]

\[
 \mathbb E(\operatorname{Tr}X')^2
 =T^2-\frac{8qT}{n+2}(n\alpha-T)+R_3,
 \qquad |R_3|\leq1344q^2 T^2.                       \tag{12}
\]

There is also the exact first-trace identity

\[
 \mathbb E\operatorname{Tr}X'=T-\kappa_n(q)(n\alpha-T),
 \quad
 \kappa_n(q)=\frac{4q}{(n-1)\mu_n(q)}
 \mathbb E\left[y(1-y/n)\,
 \operatorname{sech}^4(\sqrt{qy})
 \frac{\tanh(\sqrt{qy})}{\sqrt{qy}}\right],          \tag{13}
\]

where y=nu_1^2 and the ratio at zero equals 1. In particular kappa_n(q) >= 0, and for 0 <= q <= 1/4,

\[
 0\leq\kappa_n(q)\leq\frac{8q}{n+2}.              \tag{14}
\]

For q>0 the coefficient is positive. The first-trace equality \(\mathbb E\operatorname{Tr}X'=T\) therefore holds exactly when \(\alpha=T/n\). A fixed Gaussian critical gain does not in general preserve this conditional mean, even after correcting the scalar spherical/Gaussian mismatch.

### Spherical moment facts

For a uniform row vector r on the unit sphere, the moment of a monomial with powers 2a_i is

\[
 \mathbb E\prod_i r_i^{2a_i}
 =\frac{\prod_i(2a_i-1)!!}{n(n+2)\cdots(n+2\sum_i a_i-2)}.       \tag{15}
\]

An empty factor is 1. To see this, write a standard Gaussian vector as its independent radius times its uniform direction, integrate each Gaussian even moment by parts, and use the chi-square radial moments \(\mathbb E\|G\|^{2k}=n(n+2)\cdots(n+2k-2)\), also obtained by integration by parts. Odd coordinate powers vanish by symmetry.

Rotating e to the first coordinate and using (15), for any symmetric Y one gets

\[
 \mathbb E(r\cdot e)^2(r^\top Yr)
 =\frac{\operatorname{Tr}Y+2e^\top Ye}{n(n+2)},      \tag{16}
\]

\[
 \mathbb E(r\cdot e)^4(r^\top Yr)
 =\frac{3\operatorname{Tr}Y+12e^\top Ye}{n(n+2)(n+4)}.           \tag{17}
\]

Indeed only the diagonal of Y survives sign symmetry; its first entry has fourth- or sixth-power coefficient 3 or 15, and each other diagonal entry has coefficient 1 or 3, respectively.

### Proof of (13), (14), and (10)

Put y=nu_1^2 and b_q(y)=sech^4(sqrt(qy)). Then E y=1,

\[
 \mathbb E y^2=\frac{3n}{n+2},\qquad
 \mathbb E y^3=\frac{15n^2}{(n+2)(n+4)}.             \tag{18}
\]

Since E k=n in (3), and \(\mathbb E s=\mathbb E[y b_q(y)]/\mu_n(q)\), subtracting T from (3) gives

\[
 \mathbb E\operatorname{Tr}X'-T
 =\frac{n\alpha-T}{n-1}
   \frac{\mathbb E[(y-1)b_q(y)]}{\mu_n(q)}.          \tag{19}
\]

The variable y/n has density proportional to \(t^{-1/2}(1-t)^{(n-3)/2}\), for 0<t<1. This follows by slicing the sphere, or by the Gaussian representation used for (15). Integration by parts, with the boundary factor \(y^{1/2}(1-y/n)^{(n-1)/2}\) zero at both endpoints, yields

\[
 \mathbb E[(y-1)f(y)]
 =2\mathbb E[y(1-y/n)f'(y)].                       \tag{20}
\]

For f=b_q, \(f'(y)=-2q K(\sqrt{qy})\), where

\[
 K(x)=\operatorname{sech}^4(x)\tanh(x)/x,\quad K(0)=1.
\]

Equation (19) now proves (13). Since 0<K<=1 and

\[
 \mathbb E[y(1-y/n)]=\frac{n-1}{n+2},              \tag{21}
\]

it remains to control the normalizer. The inequalities |tanh x|<=|x| and \(1-\operatorname{sech}^4x=2\tanh^2x-\tanh^4x\) give \(1-2q\leq\mu_n(q)\leq1\). Thus mu_n >= 1/2 in the stated range, proving (14).

For the sharper expansion, \(0\leq x-\tanh x\leq x^3/3\) for x>=0 follows by integrating tanh^2 t<=t^2. Hence

\[
 0\leq1-K(x)\leq(7/3)x^2.
\]

Also \(1/\mu_n-1\leq4q\), and (18) implies

\[
 \mathbb E[y^2(1-y/n)]
 =\frac{3n(n-1)}{(n+2)(n+4)}.                     \tag{22}
\]

Using these facts in (13) gives

\[
 \left|\kappa_n(q)-\frac{4q}{n+2}\right|
 \leq\frac{4q}{n-1}
 \left\{\frac{14q}{3}\mathbb E[y^2(1-y/n)]
             +4q\mathbb E[y(1-y/n)]\right\}
 \leq\frac{72q^2}{n+2}.
\]

Combining this with (13) proves (10).

### Proof of (11), (12), and their uniform remainders

Write y_i=nu_i^2. For all real x,

\[
 0\leq\operatorname{sech}^4x-1+2x^2\leq(7/3)x^4.   \tag{23}
\]

The lower bound follows from the tanh identity above. For the upper bound, \(0\leq x^2-\tanh^2x\leq(2/3)x^4\), using the integral estimate for x-tanh x, and \(\tanh^4x\leq x^4\). Adding \(2(x^2-\tanh^2x)+\tanh^4x\) proves (23).

Let \(\Delta=A-I\), \(C_1=\operatorname{diag}(2(1-y_i))\), and \(R=A-I-qC_1\). Using (23), E y_i^2<=3, mu_n>=1/2, and 1-mu_n<=2q gives the pointwise bounds

\[
 |\Delta_{ii}|\leq4q(1+y_i),\qquad
 |R_{ii}|\leq26q^2(1+y_i^2),\qquad
 |\Delta_{ii}|^2\leq32q^2(1+y_i^2).               \tag{24}
\]

To check the middle constant explicitly, write b_q(y)=1-2qy+epsilon(y), with \(0\leq\epsilon(y)\leq(7/3)q^2y^2\). Then

\[
 R_{ii}=\frac{2q(1-y_i)(1-\mu_n)+\epsilon(y_i)-\mathbb E\epsilon(y)}{\mu_n}.
\]

Its absolute value is at most \(q^2(22+8y_i+(14/3)y_i^2)\), which is bounded by \(26q^2(1+y_i^2)\) because \(8y_i\leq4+4y_i^2\). The first bound in (24) follows from \(|b_q(y_i)-\mu_n|\leq2q(y_i+1)\); the third follows from the first and \((1+y_i)^2\leq2(1+y_i^2)\).

For any fixed positive semidefinite Y, applying (17) to each row of O yields

\[
 \mathbb E\sum_i y_i^2(OYO^\top)_{ii}
 =\frac{n^2(3\operatorname{Tr}Y+12e^\top Ye)}{(n+2)(n+4)}
 \leq15\operatorname{Tr}Y.                       \tag{25}
\]

Here \(e^\top Ye\leq\operatorname{Tr}Y\). Adding the zeroth-power term gives a bound of \(16\operatorname{Tr}Y\).

Expand the second trace:

\[
 \operatorname{Tr}(ABAB)=Q+2q\operatorname{Tr}(C_1B^2)
                         +2\operatorname{Tr}(RB^2)
                         +\operatorname{Tr}(\Delta B\Delta B).
\]

Because B is symmetric,

\[
 |\operatorname{Tr}(\Delta B\Delta B)|
 \leq\sum_{ij}|\Delta_{ii}\Delta_{jj}|B_{ij}^2
 \leq\sum_i|\Delta_{ii}|^2(B^2)_{ii},
\]

by \(2|ab|\leq a^2+b^2\). Equations (24),(25), with Y=X^2, bound the expected remainder by

\[
 (2\cdot26+32)q^2\cdot16Q=1344q^2Q.              \tag{26}
\]

Since \(B^2=OX^2O^\top\), applying (16) to each row gives

\[
 \mathbb E\operatorname{Tr}(C_1B^2)
 =2Q-\frac{2n}{n+2}(Q+2\gamma)
 =-\frac4{n+2}(n\gamma-Q).
\]

Together with (26), this proves (11).

For the square of the trace, expand

\[
 (\operatorname{Tr}AB)^2
 =T^2+2qT\operatorname{Tr}(C_1B)
       +2T\operatorname{Tr}(RB)+(\operatorname{Tr}\Delta B)^2.
\]

Since B is positive semidefinite, B_ii>=0, and the weighted Cauchy–Schwarz inequality gives

\[
 (\operatorname{Tr}\Delta B)^2\leq T\sum_i\Delta_{ii}^2B_{ii}.
\]

Thus (24),(25), now with Y=X, bound the remainder by \(1344q^2T^2\). Equation (16) gives \(\mathbb E\operatorname{Tr}(C_1B)=-4(n\alpha-T)/(n+2)\), proving (12).

## 4. What the correction means and what it does not prove

For comparison, independent gates with the same one-coordinate marginal as (9) have mean 1 and variance v_n(q). The earlier report gives

\[
 \mathbb E T'_{\rm ind}=T,\quad
 \mathbb E Q'_{\rm ind}=Q+v_n(q)\frac{T^2+2Q}{n+2},\quad
 \mathbb E (T'_{\rm ind})^2=T^2+v_n(q)\frac{T^2+2Q}{n+2}.        \tag{27}
\]

At fixed n, (23),(24) imply by dominated convergence

\[
 v_n(q)=\frac{8(n-1)}{n+2}q^2+o(q^2),\qquad q\downarrow0.      \tag{28}
\]

Indeed \((A_{11}-1)/q\to2(1-y)\) in L^2 (y is bounded at fixed n), and \(\operatorname{Var}y=2(n-1)/(n+2)\). Uniformly for n>=3 and q<=1/4, v_n(q)<=32q^2: b_q is 2q-Lipschitz as a function of y, so its variance is at most \(4q^2\operatorname{Var}y\), using an independent copy of y; multiplication by 1/mu_n^2<=4 proves the bound.

Equations (10)–(12) therefore show dependence corrections linear in q, before the independent-gate spread of order q^2. The linear terms depend on the input direction through alpha and gamma. For example, with X=ee^top, T=Q=alpha=gamma=1, so

\[
 \mathbb E\operatorname{Tr}X'=1-\frac{4(n-1)}{n+2}q+O(q^2),
\]

\[
 \mathbb E\operatorname{Tr}((X')^2)
 =1-\frac{8(n-1)}{n+2}q+O(q^2).
\]

This example is a test of the conditional lemma, not a claim that this X arises typically in a tanh network.

After division by n, the linear corrections in the first and second trace are respectively

\[
 -\frac{4q}{n+2}(\alpha-T/n),\qquad
 -\frac{8q}{n+2}(\gamma-Q/n).
\]

They are small when the directional energies are controlled, but the identities do not supply that control over many layers. The remainders in (11),(12) are intentionally coarse and cannot identify a second-order accumulated spectral limit. Forward-radius drift and sharper control of alpha and gamma remain open here. The next section obtains a sufficient accumulated distortion bound by combining the two linear corrections, without separate directional estimates. No freeness theorem, limiting density, edge bound, or full dynamical-isometry theorem is asserted.

## 5. Accumulated bound for the actual Jacobian after a scalar normalization

The preceding one-layer estimates yield a joint-limit statement without assuming independent gates. The scalar normalization in this statement is explicit and generally random.

Consider a zero-bias tanh network at a fixed nonzero deterministic input h_0, with independent Haar O_l and deterministic positive gains g_l:

\[
 h_l=\tanh(g_lO_lh_{l-1}),\qquad
 J_l=g_l\operatorname{diag}(\operatorname{sech}^2(g_lO_lh_{l-1}))O_lJ_{l-1},
 \quad J_0=I.
\]

Every h_l is nonzero: each preceding orthogonal image is nonzero, and tanh vanishes only at zero in each coordinate. Put

\[
 q_l=\frac{g_l^2\|h_{l-1}\|^2}{n},\quad
 c_l=g_l^2\mu_n(q_l)>0,\quad S_l=\prod_{j=1}^l c_j,
\]

\[
 \widehat X_l=\frac{J_lJ_l^\top}{S_l},\qquad
 \widehat Z_l=\frac1n\operatorname{Tr}(\widehat X_l-I)^2.
\]

All these definitions are evaluated on the ordinary network; no derivative of a normalization is inserted into J_l.

**Theorem 3.** Suppose deterministic numbers \(0\leq\varepsilon_l\leq1/4\) satisfy \(q_l\leq\varepsilon_l\) almost surely, for each 1<=l<=L. Define

\[
 A_L=\sum_{l=1}^L\left(\frac{12\varepsilon_l}{n+2}+2760\varepsilon_l^2\right),\qquad
 B_L=\sum_{l=1}^L\left(\frac{6\varepsilon_l}{n+2}+2904\varepsilon_l^2\right).
\]

Then at every finite n>=3 and L,

\[
 \mathbb E\widehat Z_L\leq B_L e^{A_L}.             \tag{29}
\]

Consequently, for any triangular sequence n,L(n)->infinity with such envelopes satisfying

\[
 \sum_{l=1}^{L(n)}\varepsilon_l^2
 +\frac1n\sum_{l=1}^{L(n)}\varepsilon_l\longrightarrow0,       \tag{30}
\]

the empirical measure of the eigenvalues of \(\widehat X_L\) converges to delta_1 in W_2 in probability. If also \(S_L\to1\) in probability, the same is true for the unnormalized Gram matrix \(J_LJ_L^\top\). There is no operator-norm conclusion.

For a constant envelope epsilon_l=epsilon_n, (30) reads \(L\varepsilon_n^2\to0\) and \(L\varepsilon_n/n\to0\). This is a sufficient condition; necessity is not asserted.

### Proof

Condition on all layers before l. The quantities q_l and c_l are then fixed. Dividing the ordinary Gram recursion by S_l gives exactly the model of Theorem 2, with X=\widehat X_{l-1}, e=h_{l-1}/\|h_{l-1}\| and the normalized gate (9). This assertion uses only the independence of the fresh Haar matrix.

Let Z=Tr(X-I)^2/n and let E=X-I. Combining (10),(11) gives

\[
 \mathbb E[\widehat Z_l\mid\text{past}]
 =Z+\frac{8q_l}{n+2}\left\{\frac{Q-T}{n}-(\gamma-\alpha)\right\}
       +\frac{R_2-2R_1}{n}.                      \tag{31}
\]

The directional term can be bounded without estimating alpha or gamma separately:

\[
 \gamma-\alpha=e^\top(E^2+E)e
 =\|(E+\tfrac12I)e\|^2-\tfrac14\geq-\tfrac14.
\]

Moreover \((Q-T)/n=Z+\operatorname{Tr}E/n\leq Z+\sqrt Z\), by Cauchy–Schwarz on the eigenvalues. Thus the linear term in (31) is at most

\[
 \frac{8q_l}{n+2}(Z+\sqrt Z+\tfrac14)
 \leq\frac{q_l}{n+2}(12Z+6),                     \tag{32}
\]

using \(\sqrt Z\leq(Z+1)/2\).

Since X is positive semidefinite, \(0\leq\alpha\leq T\) and \(|n\alpha-T|\leq(n-1)T\). Therefore (10),(11) imply

\[
 \frac{|R_2-2R_1|}{n}
 \leq q_l^2\left(1344\frac Qn+144\frac Tn\right).
\]

The triangle inequality for the Frobenius norm gives \(Q/n\leq2+2Z\), and \(T/n\leq1+\sqrt Z\leq3/2+Z/2\). Substitution yields

\[
 \frac{|R_2-2R_1|}{n}\leq q_l^2(2760Z+2904).       \tag{33}
\]

Here \(2760=2\cdot1344+144/2\) and \(2904=2\cdot1344+3\cdot144/2\). Combining (31)–(33) and replacing q_l by its deterministic upper bound gives

\[
 \mathbb E[\widehat Z_l\mid\text{past}]
 \leq(1+a_l)\widehat Z_{l-1}+b_l,
\]

where \(a_l=12\varepsilon_l/(n+2)+2760\varepsilon_l^2\) and \(b_l=6\varepsilon_l/(n+2)+2904\varepsilon_l^2\). All moments involved are finite: the normalized gates are bounded by 2 under the envelope, and the depth is finite. Take expectations and iterate from \(\widehat Z_0=0\):

\[
 \mathbb E\widehat Z_L
 \leq\sum_{j=1}^L b_j\prod_{k=j+1}^L(1+a_k)
 \leq\left(\sum_j b_j\right)\exp\left(\sum_k a_k\right).
\]

This proves (29). Under (30), both A_L and B_L tend to zero. If \(\widehat\nu_L\) is the empirical squared-singular-value measure of \(J_L/\sqrt{S_L}\), its only coupling with delta_1 gives

\[
 W_2(\widehat\nu_L,\delta_1)^2=\widehat Z_L.
\]

Markov's inequality proves the asserted convergence. Finally, the Frobenius triangle inequality gives, sample by sample,

\[
 \left[\frac1n\operatorname{Tr}(J_LJ_L^\top-I)^2\right]^{1/2}
 \leq S_L\sqrt{\widehat Z_L}+|S_L-1|.
\]

If S_L tends to 1 in probability, the right side tends to zero in probability. This proves the last assertion.

The deterministic envelope is a substantive hypothesis. One sufficient, sometimes conservative, envelope follows directly from |tanh x|<=|x|:

\[
 q_l\leq\frac{\|h_0\|^2}{n}\prod_{j=1}^l g_j^2.
\]

For g_j=1, the constant envelope \(\varepsilon_n=\|h_0\|^2/n\) therefore applies. The normalized-spectrum conclusion is then unconditional under the stated scaling. In that example S_L need not tend to 1: (30) alone must not be presented as isometry of the original Jacobian. Establishing S_L->1 and sharper forward-radius envelopes at fixed critical initialization remains unfinished.
