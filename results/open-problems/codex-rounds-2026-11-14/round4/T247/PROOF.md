# Removing the scalar normalization at a vanishing-variance critical initialization

Consider a real, constant-width, zero-bias network

\[
h_l=\tanh(gO_lh_{l-1}),\qquad
J_l=g\operatorname{diag}(\operatorname{sech}^2(gO_lh_{l-1}))O_lJ_{l-1},
\qquad J_0=I_n,
\tag{1}
\]

where the matrices \(O_l\) are independent Haar matrices on \(O(n)\). The gain \(g>0\) is deterministic and is the same at every layer. The hyperbolic tangent acts coordinatewise. The input is deterministic and nonzero.

For \(q\geq0\), define

\[
\mu_n(q)=\mathbb E_{u\in S^{n-1}}
  \operatorname{sech}^4(\sqrt{nq}\,u_1),\qquad
\mu_G(q)=\mathbb E_{G\sim N(0,1)}
  \operatorname{sech}^4(\sqrt q\,G).
\tag{2}
\]

Both expectations use probability measures. Set

\[
q_l=\frac{g^2\|h_{l-1}\|^2}{n},\qquad
S_L=\prod_{l=1}^L g^2\mu_n(q_l),\qquad
\nu_L=\frac1n\sum_{i=1}^n\delta_{s_i(J_L)^2}.
\tag{3}
\]

Every radius and every scalar factor in (3) is positive. The quantity \(S_L\) is evaluated on (1); it does not change the network or its Jacobian.

**Theorem.** Let \(n\to\infty\), \(L=L(n)\to\infty\), and \(a=a_n>0\). Suppose

\[
L a^2+\frac{La}{n}\longrightarrow0.
\tag{4}
\]

Choose the gain and input so that

\[
|\log(g^2)-2a|\leq15a^2,\qquad
\frac{g^2\|h_0\|^2}{n}=a.
\tag{5}
\]

Then

\[
\max_{1\leq l\leq L+1}|\log(q_l/a)|\xrightarrow{\mathbb P}0,
\qquad S_L\xrightarrow{\mathbb P}1,
\qquad W_2(\nu_L,\delta_1)\xrightarrow{\mathbb P}0.
\tag{6}
\]

In particular, (5) holds for either of the deterministic choices

\[
g^2=\mu_G(a)^{-1}\quad\hbox{or}\quad g^2=\mu_n(a)^{-1}
\tag{7}
\]

for all sufficiently large \(n\). The first is the conventional Gaussian derivative-critical gain at target variance \(a\). The second uses the exact spherical derivative mean. Neither gain is adapted to the observed forward radii.

This is an empirical isometry theorem for a vanishing-variance sequence. It does not assert stationarity at a fixed positive variance, include biases, give a full limiting density, or control the extreme singular values. For example, \(a=n^{-2}\) and \(L=\lfloor n^{5/2}\rfloor\) satisfy (4), while \(La\to\infty\).

## 1. Global scalar inequalities

For \(x\geq0\),

\[
\frac{x}{1+x^2}\leq\tanh x\leq x.
\tag{8}
\]

For the lower bound, differentiate
\(f(x)=(1+x^2)\sinh x-x\cosh x\). Its derivative is
\(x\sinh x+x^2\cosh x\geq0\), and \(f(0)=0\). Division by \((1+x^2)\cosh x\) proves it. The upper bound follows by integrating \(\tanh'(x)=\operatorname{sech}^2x\leq1\).

Put \(t=x-\tanh x\). Integrating \(\tanh^2s\leq s^2\) gives \(0\leq t\leq x^3/3\). Therefore
\(0\leq x^2-\tanh^2x=(x-\tanh x)(x+\tanh x)\leq(2/3)x^4\).
Integrating this last inequality gives

\[
0\leq\frac{x^3}{3}-t
=\int_0^x(s^2-\tanh^2s)\,ds\leq\frac{2x^5}{15}.
\]

Expanding \((x-t)^2\) now proves, for every real \(x\),

\[
0\leq\tanh^2x-x^2+\frac23x^4\leq\frac{17}{45}x^6.
\tag{9}
\]

Indeed the expression is \(2x(x^3/3-t)+t^2\), whose upper bound is
\((4/15+1/9)x^6=(17/45)x^6\). Evenness extends the proof to negative \(x\).

The identity \(\operatorname{sech}^4x=(1-\tanh^2x)^2\), together with the bounds above, gives

\[
0\leq\operatorname{sech}^4x-1+2x^2\leq\frac73x^4.
\tag{10}
\]

For the upper bound, write the expression as
\(2(x^2-\tanh^2x)+\tanh^4x\); for the lower bound both terms are nonnegative.

Let \(Y\geq0\) have \(\mathbb EY=1\) and \(\mathbb EY^2\leq3\), and write
\(\mu(q)=\mathbb E\operatorname{sech}^4(\sqrt{qY})\). By (10),

\[
1-2q\leq\mu(q)\leq1,\qquad
0\leq\mu(q)-1+2q\leq7q^2.
\tag{11}
\]

For \(0\leq q\leq1/4\), let \(s=-\log\mu(q)\). Then \(0\leq s\leq4q\). Since
\(0\leq s-(1-e^{-s})\leq s^2/2\), it follows that

\[
|\log\mu(q)+2q|\leq15q^2.
\tag{12}
\]

The auxiliary inequality follows by integrating \(1-e^{-t}\leq t\) from zero to \(s\). In (2), take respectively \(Y=nu_1^2\) and \(Y=G^2\). Their fourth-coordinate moments give \(\mathbb EY^2\leq3\), so (12) proves (5) for both choices (7).

## 2. The forward radial increment

For a unit vector \(u\), define

\[
F(q,u)=\frac1{nq}\sum_{i=1}^n\tanh^2(\sqrt{nq}\,u_i),
\quad M_4(u)=n\sum_i u_i^4,\quad M_6(u)=n^2\sum_i u_i^6.
\tag{13}
\]

At \(q=0\), use \(F(0,u)=1\). For \(q>0\), \(0<F(q,u)\leq1\). Applying (8) with weights \(u_i^2\), then Jensen's inequality for the convex function \(v\mapsto(1+v)^{-2}\), gives

\[
F(q,u)\geq\sum_i\frac{u_i^2}{(1+nqu_i^2)^2}
\geq(1+qM_4(u))^{-2}.
\]

Consequently

\[
0\leq-\log F(q,u)\leq2qM_4(u).
\tag{14}
\]

Summing (9) gives

\[
F(q,u)=1-\frac23qM_4(u)+R_F,
\qquad0\leq R_F\leq\frac{17}{45}q^2M_6(u).
\tag{15}
\]

Apply \(0\leq s-(1-e^{-s})\leq s^2/2\) with \(s=-\log F\) and use (14). Combining with (15) yields

\[
\left|\log F(q,u)+\frac23qM_4(u)\right|
\leq q^2\left(\frac{17}{45}M_6(u)+2M_4(u)^2\right).
\tag{16}
\]

These inequalities are global in the coordinates; no bound on \(nq\) is imposed.

For uniform \(u\), its even coordinate moments are

\[
\mathbb E\prod_i u_i^{2k_i}
=\frac{\prod_i(2k_i-1)!!}{n(n+2)\cdots(n+2\sum_i k_i-2)}.
\tag{17}
\]

To derive this, write a standard Gaussian vector as its independent uniform direction times its radius. The one-dimensional Gaussian moments follow by integration by parts, as do the radial moments \(\mathbb E\|G\|^{2k}=n(n+2)\cdots(n+2k-2)\). Dividing the coordinate-moment identity by the radial moment gives (17).

In particular,

\[
\mathbb EM_4=\frac{3n}{n+2},\qquad
\mathbb EM_6=\frac{15n^2}{(n+2)(n+4)}\leq15,
\]

\[
\mathbb EM_4^2
=\frac{n^2(9n+96)}{(n+2)(n+4)(n+6)}\leq9.
\tag{18}
\]

For the last equality, separate the \(n\) terms \(u_i^8\), whose numerator is 105, from the \(n(n-1)\) terms \(u_i^4u_j^4\), whose numerator is 9. The inequality follows because the difference between nine times the denominator and the numerator is \(12n^2+396n+432>0\).

Let \(m_n(q)=\mathbb E\log F(q,u)\) and \(c_n=2n/(n+2)\). Equations (14), (16), (18) imply

\[
m_n(q)=-c_nq+\rho_n(q),\quad |\rho_n(q)|\leq24q^2,
\qquad \operatorname{Var}(\log F(q,u))\leq36q^2.
\tag{19}
\]

The remainder constant is valid since \((17/45)15+2\cdot9=71/3<24\). The variance bound follows from \(\operatorname{Var}(Z)\leq\mathbb EZ^2\) and (14).

## 3. A uniform forward-radius estimate

For explicit finite-size bounds, assume from now on

\[
n\geq64,\qquad0<a\leq1/4096,
\tag{20}
\]

and (5). These restrictions hold eventually under (4). Given all preceding layers, \(u_l=O_lh_{l-1}/\|h_{l-1}\|\) is uniform on the sphere. Thus the exact recursion is

\[
q_{l+1}=g^2q_lF(q_l,u_l).
\tag{21}
\]

Write \(x_k=\log(q_{k+1}/a)\), so \(x_0=0\). The conditional mean increment at radius \(q\) is
\(b(q)=\log(g^2)+m_n(q)\). For \(q\in[a/2,2a]\), (5), (19) give

\[
b(q)=2a-c_nq+\eta(q),\qquad |\eta(q)|\leq111a^2.
\tag{22}
\]

Also \(|b(q)|\leq16a\): (11)–(12) and (5) imply \(|\log g^2|\leq4a\), and (14), (18) give \(|m_n(q)|\leq6q\leq12a\).

Put \(r=8/n+222a\). Under (20), \(r<1/4\). If \(q\geq ae^r\) remains in the interval, (22) and \(e^r\geq1+r\) give

\[
b(q)\leq a\{4/(n+2)-c_nr+111a\}\leq0.
\tag{23}
\]

Here \(c_n\geq1\) and \(r\geq8/n+222a\). If \(q\leq ae^{-r}\), use \(e^{-r}\leq1-r/2\), valid for \(0\leq r\leq1\), to obtain

\[
b(q)\geq a\{4/(n+2)+c_nr/2-111a\}\geq0.
\tag{24}
\]

Stop \(x_k\) at its first exit \(\tau\) from \((-\log2,\log2)\), and freeze it afterwards. Its stopped increments can be written

\[
\bar x_{k+1}-\bar x_k=\bar b_k+\Delta M_{k+1},
\]

where before exit \(\bar b_k=b(q_{k+1})\) and
\(\Delta M_{k+1}=\log F(q_{k+1},u_{k+1})-m_n(q_{k+1})\); after exit both are zero. The indicator of an active step is known before drawing the fresh Haar matrix, so \(M_k\) is a martingale. By (19) and \(q\leq2a\) before exit,

\[
\mathbb EM_L^2\leq144La^2,\qquad
\mathbb P\{\max_{k\leq L}|M_k|>\delta\}
\leq\frac{144La^2}{\delta^2}.
\tag{25}
\]

Orthogonality of martingale differences gives the first inequality. For the second, stop at the first crossing of \(|M_k|>\delta\). Conditional variance is nonnegative, so the expectation of \(M_L^2\) dominates that of its stopped square, which is at least \(\delta^2\) times the crossing probability.

The restoring signs (23)–(24) and the increment bound imply, pathwise,

\[
\max_{k\leq L}|\bar x_k|\leq r+16a+2\max_{k\leq L}|M_k|.
\tag{26}
\]

Here is the discrete crossing argument. If \(\bar x_k>r\), take the last \(j<k\) with \(\bar x_j\leq r\). Its existence follows from \(\bar x_0=0\). The first subsequent drift is at most \(16a\); every later drift up to time \(k\) is nonpositive by (23), or zero after freezing. Hence
\(\bar x_k\leq r+16a+M_k-M_j\). If \(\bar x_k<-r\), take the last \(j<k\) with \(\bar x_j\geq-r\); use the lower drift bound \(-16a\) at the first step and (24) afterwards. This proves (26), including the exit step itself.

For \(0<\delta\leq1/8\), (20) gives \(r+16a+2\delta<\log2\). Thus on the event \(\max|M_k|\leq\delta\), (26) prevents exit, and

\[
\max_{1\leq l\leq L+1}|\log(q_l/a)|
\leq\frac8n+238a+2\delta.
\tag{27}
\]

The exceptional probability is at most the right side of (25).

## 4. Comparing the scalar gain with the radius

By (12) and (19), whenever \(q\leq1/4\),

\[
d_n(q):=\log\mu_n(q)-m_n(q),\qquad
|d_n(q)|\leq\frac{4q}{n+2}+39q^2.
\tag{28}
\]

The coefficient is \(2-c_n=4/(n+2)\); the remainder bound is \(15+24=39\). On the event in (27), all \(L\) steps are active. Subtract the logarithm of (21), summed over the layers, from the logarithm of (3):

\[
\log S_L-x_L
=\sum_{l=1}^L\{\log\mu_n(q_l)-\log F(q_l,u_l)\}
=\sum_{l=1}^Ld_n(q_l)-M_L.
\tag{29}
\]

Since \(q_l\leq2a\), equations (27)–(29) prove

\[
|\log S_L|\leq H+3\delta,\qquad
H=\frac8n+238a+\frac{8La}{n+2}+156La^2,
\tag{30}
\]

with exceptional probability at most \(144La^2/\delta^2\). Thus the forward-radius and scalar assertions in (6) already follow from (4), by taking \(\delta=(La^2)^{1/4}\), eventually at most \(1/8\).

## 5. The dependent-gate distortion estimate

The needed finite-width estimate is the accumulated bound from the preceding round. Its proof is included to specify its hypotheses and the stopping operation.

Condition on the past, let \(X\succeq0\) be the preceding normalized Gram matrix, and set \(e=h/\|h\|\), \(B=OXO^\top\), \(y_i=n(Oe)_i^2\). Write

\[
A_{ii}=\frac{\operatorname{sech}^4(\sqrt{qy_i})}{\mu_n(q)},
\quad X'=A^{1/2}BA^{1/2},\quad
T=\operatorname{Tr}X,\ Q=\operatorname{Tr}X^2,
\quad\alpha=e^\top Xe,\ \gamma=e^\top X^2e.
\]

For \(q\leq1/4\), the one-layer estimates are

\[
\mathbb E\operatorname{Tr}X'
=T-\frac{4q}{n+2}(n\alpha-T)+R_1,
\quad |R_1|\leq\frac{72q^2}{n+2}|n\alpha-T|,
\tag{31}
\]

\[
\mathbb E\operatorname{Tr}(X'^2)
=Q-\frac{8q}{n+2}(n\gamma-Q)+R_2,
\quad |R_2|\leq1344q^2Q.
\tag{32}
\]

For (31), condition on \(u=Oe\). The conditional mean of \(B\) is
\(\alpha uu^\top+(T-\alpha)(I-uu^\top)/(n-1)\), by invariance under the stabilizer of \(e\). Thus, with \(Y=nu_1^2\) and \(b_q(Y)=\operatorname{sech}^4(\sqrt{qY})\),

\[
\mathbb E\operatorname{Tr}X'-T
=\frac{n\alpha-T}{(n-1)\mu_n(q)}\mathbb E[(Y-1)b_q(Y)].
\]

The beta density of \(Y/n\) is proportional to
\(t^{-1/2}(1-t)^{(n-3)/2}\). Integrating its derivative gives
\(\mathbb E[(Y-1)f(Y)]=2\mathbb E[Y(1-Y/n)f'(Y)]\); the boundary term vanishes. Since
\(b_q'(Y)=-2qK(\sqrt{qY})\), where \(K(x)=\operatorname{sech}^4x\,\tanh x/x\), the correction is \(-\kappa(n\alpha-T)\), with

\[
\kappa=\frac{4q}{(n-1)\mu_n(q)}\mathbb E[Y(1-Y/n)K(\sqrt{qY})].
\]

The bounds \(0\leq1-K(x)\leq(7/3)x^2\), \(\mu_n(q)^{-1}\leq2\) and \(\mu_n(q)^{-1}-1\leq4q\) follow from (8), (10), (11). Formula (17) gives
\(\mathbb E[Y(1-Y/n)]=(n-1)/(n+2)\) and
\(\mathbb E[Y^2(1-Y/n)]=3n(n-1)/((n+2)(n+4))\). Therefore

\[
\left|\kappa-\frac{4q}{n+2}\right|
\leq\frac{4q}{n-1}\left\{\frac{14q}{3}\frac{3n(n-1)}{(n+2)(n+4)}
+4q\frac{n-1}{n+2}\right\}
\leq\frac{72q^2}{n+2},
\]

which proves (31).

For (32), put \(\Delta=A-I\), \(C_{ii}=2(1-y_i)\), and \(R=A-I-qC\). Directly from (10), (11),

\[
|\Delta_{ii}|\leq4q(1+y_i),\quad
|R_{ii}|\leq26q^2(1+y_i^2),\quad
\Delta_{ii}^2\leq32q^2(1+y_i^2).
\tag{33}
\]

For the middle constant, write \(b_q(y)=1-2qy+\epsilon(y)\) with
\(0\leq\epsilon(y)\leq(7/3)q^2y^2\). Then
\(R_{ii}=[2q(1-y_i)(1-\mu_n)+\epsilon(y_i)-\mathbb E\epsilon(Y)]/\mu_n\).
Its absolute value is at most \(q^2(22+8y_i+(14/3)y_i^2)\), bounded by \(26q^2(1+y_i^2)\). The other two bounds follow from \(|b_q(y)-\mu_n|\leq2q(y+1)\) and \((1+y)^2\leq2(1+y^2)\).

For any fixed \(Y_0\succeq0\), the fourth and sixth coordinate moments (17) imply

\[
\mathbb E\sum_i y_i(OY_0O^\top)_{ii}
=\frac{n}{n+2}(\operatorname{Tr}Y_0+2e^\top Y_0e),
\]

\[
\mathbb E\sum_i(1+y_i^2)(OY_0O^\top)_{ii}
=\operatorname{Tr}Y_0+
\frac{n^2(3\operatorname{Tr}Y_0+12e^\top Y_0e)}{(n+2)(n+4)}
\leq16\operatorname{Tr}Y_0.
\tag{34}
\]

Indeed rotate \(e\) to the first coordinate in each row moment; the coefficient of the first diagonal entry is 3 rather than 1 at fourth order, and 15 rather than 3 at sixth order. Odd terms vanish by coordinate sign symmetry.

Expand
\(\operatorname{Tr}(ABAB)=Q+2q\operatorname{Tr}(CB^2)+2\operatorname{Tr}(RB^2)+\operatorname{Tr}(\Delta B\Delta B)\).
The first equation of (34), with \(Y_0=X^2\), gives
\(\mathbb E\operatorname{Tr}(CB^2)=-4(n\gamma-Q)/(n+2)\).
Also \(|\operatorname{Tr}(\Delta B\Delta B)|\leq\sum_i\Delta_{ii}^2(B^2)_{ii}\), by symmetry of \(B\) and \(2|ab|\leq a^2+b^2\). Equations (33)–(34) bound the expected remainder by
\((2\cdot26+32)16q^2Q=1344q^2Q\), proving (32).

Let \(Z=\operatorname{Tr}(X-I)^2/n\). Combining (31)–(32), the linear correction to \(\mathbb EZ\) is

\[
\frac{8q}{n+2}\left\{\frac{Q-T}{n}-(\gamma-\alpha)\right\}.
\]

Write \(E=X-I\). Completing the square gives
\(\gamma-\alpha=e^\top(E^2+E)e\geq-1/4\), while
\((Q-T)/n=Z+\operatorname{Tr}E/n\leq Z+\sqrt Z\).
Using \(\sqrt Z\leq(Z+1)/2\), the linear correction is at most \(q(12Z+6)/(n+2)\).
Since \(\alpha\leq T\), the remainder divided by \(n\) is at most
\(q^2(1344Q/n+144T/n)\). Finally \(Q/n\leq2Z+2\) and
\(T/n\leq1+\sqrt Z\leq3/2+Z/2\). Hence

\[
\mathbb E[Z'\mid\mathrm{past}]
\leq\left(1+\frac{12q}{n+2}+2760q^2\right)Z
+\frac{6q}{n+2}+2904q^2.
\tag{35}
\]

No independence of gates and weights has been used.

Freeze the normalized Gram process just before any step whose input radius has already exited \([a/2,2a]\). Equivalently, apply its normalized gate only while the stopped radius process in Section 3 is active, and apply an identity step afterwards. Call its distortion \(Z_L^{\mathrm{stop}}\). The choice of an active step is measurable with respect to the past. On active steps use (35) with \(q\leq2a\); on frozen steps \(Z'=Z\), which also satisfies the same upper bound. Iteration from \(Z_0=0\) yields

\[
\mathbb EZ_L^{\mathrm{stop}}\leq Be^A,
\quad A=\frac{24La}{n+2}+11040La^2,
\quad B=\frac{12La}{n+2}+11616La^2.
\tag{36}
\]

To see the iteration explicitly, write the fixed upper coefficients in (35) as \(1+\alpha_0\), \(\beta_0\). Then
\(\mathbb EZ_L^{\mathrm{stop}}\leq\beta_0\sum_{j=0}^{L-1}(1+\alpha_0)^j\leq L\beta_0e^{L\alpha_0}\), which is (36). All stopped-process moments are finite at finite depth because the active normalized gate entries are at most 2.

## 6. Completion and a finite probability bound

On the event in (27), the stopped process agrees with \(J_LJ_L^\top/S_L\). For \(t>0\), Markov's inequality and (36) bound the probability that its distortion exceeds \(t\) by \(Be^A/t\). On the intersection of the two good events, the Frobenius triangle inequality and (30) imply

\[
W_2(\nu_L,\delta_1)
=\left[\frac1n\operatorname{Tr}(J_LJ_L^\top-I)^2\right]^{1/2}
\leq e^{H+3\delta}\sqrt t+e^{H+3\delta}-1.
\]

The equality holds because coupling an empirical measure with a point mass is unique. Consequently, for (20), (5), \(0<\delta\leq1/8\), and \(t>0\),

\[
\mathbb P\left\{W_2(\nu_L,\delta_1)>
e^{H+3\delta}\sqrt t+e^{H+3\delta}-1\right\}
\leq\frac{144La^2}{\delta^2}+\frac{Be^A}{t}.
\tag{37}
\]

Under (4), \(a\to0\), \(A,B,H\to0\). Choose
\(\delta=(La^2)^{1/4}\) and \(t=(Be^A)^{1/2}\). Both the right side of (37) and its displayed threshold tend to zero. Equations (27), (30), (37) prove (6). The singular values themselves also converge empirically to 1, since \(|\sqrt\lambda-1|\leq|\lambda-1|\) for \(\lambda\geq0\).
