# The spectral finite part for the unit square

Let Q=[0,1]^2 and use the nonnegative Neumann Laplacian -Delta. Set

\[
F_Q(t)=\sum_{\substack{k,l\geq0\\k+l>0}}
\frac{e^{-\pi^2(k^2+l^2)t}}{\pi^2(k^2+l^2)},\qquad
h_Q=\lim_{t\downarrow0}\left(F_Q(t)-\frac{\log(1/t)}{4\pi}\right).
\]

The following evaluation concerns only this deterministic spectral constant.

## Explicit formula and truncation error

For a>0 define

\[
E_1(a)=\int_a^\infty\frac{e^{-x}}x\,dx,\qquad
A(a)=\int_1^\infty w^{-3/2}e^{-aw}\,dw.
\]

For an integer M>=0 define

\[
\begin{split}
H_M=\frac1{4\pi}\bigg[1-\log\pi
&+\sum_{\substack{|k|,|l|\leq M\\(k,l)\ne(0,0)}}
\left\{E_1(\pi(k^2+l^2))+
\frac{e^{-\pi(k^2+l^2)}}{\pi(k^2+l^2)}\right\}\\
&+4\sum_{m=1}^M\left\{A(\pi m^2)+\frac{e^{-\pi m^2}}{\pi m^2}\right\}\bigg].
\end{split}
\tag{1}
\]

An empty sum is zero. Then h_Q exists and

\[
0\leq h_Q-H_M\leq
\frac{4e^{-\pi(M+1)^2}}
{\pi^2(M+1)^2(1-e^{-\pi})(1-e^{-\pi(2M+3)})}.
\tag{2}
\]

In particular, 0<=h_Q-H_3<10^(-21). Formula (1) thus gives an explicit value with a proved error; it requires no matching simulation. It does not give a decimal value for the full random matching constant.

For evaluation by standard special functions, the second integral is

\[
A(a)=2e^{-a}-2\sqrt{\pi a}\,\operatorname{erfc}(\sqrt a).
\tag{3}
\]

At large a, the integral defining A avoids the subtraction in (3).

## 1. Spectrum and heat trace

In one dimension the Neumann eigenfunctions are 1 and cos(k pi x), k>=1. Their eigenvalues are pi^2 k^2. Taking products gives exactly one eigenfunction for each ordered pair k,l>=0, with eigenvalue pi^2(k^2+l^2). The pair (0,0) is the constant eigenfunction and is excluded from F_Q.

Write

\[
\theta(v)=\sum_{m\in\mathbb Z}e^{-\pi m^2v},\qquad v>0.
\]

Since the one-dimensional Neumann heat trace is (1+theta(pi u))/2, the positive-eigenvalue heat trace on Q is

\[
K_Q(u)=\frac{\theta(\pi u)^2+2\theta(\pi u)-3}{4}.
\tag{4}
\]

The -3 in (4) includes removal of the zero eigenvalue. All eigenvalue summands are nonnegative, so Tonelli's theorem gives

\[
F_Q(t)=\int_t^\infty K_Q(u)\,du
=\frac1{4\pi}\int_{\pi t}^\infty
\{\theta(v)^2+2\theta(v)-3\}\,dv.
\tag{5}
\]

## 2. Gaussian transformation

The Fourier transform of exp(-pi v x^2), with frequency convention exp(-2 pi i x xi), is v^(-1/2)exp(-pi xi^2/v). This follows by scaling the Gaussian integral; alternatively, differentiation in xi gives the differential equation for the transform and the value at xi=0 fixes its normalization.

Periodize exp(-pi v x^2) over integer translates. The function and its differentiated series converge uniformly on compact intervals. Its m-th Fourier coefficient is v^(-1/2)exp(-pi m^2/v). These coefficients are absolutely summable, so evaluating its Fourier series at zero gives

\[
\theta(v)=v^{-1/2}\theta(1/v).
\tag{6}
\]

For 0<v<=1, insert (6) into the integrand of (5):

\[
\begin{split}
\theta(v)^2+2\theta(v)-3
={}&v^{-1}+2v^{-1/2}-3\\
&+v^{-1}\{\theta(1/v)^2-1\}
+2v^{-1/2}\{\theta(1/v)-1\}.
\end{split}
\tag{7}
\]

Both expressions in braces decay exponentially as v decreases to zero. Their indicated integrals over (0,1) converge. For example, sum the Gaussian tails using m^2>=m, and use the factor exp(-pi/v) to dominate every inverse power of v. The integrand in (5) also decays exponentially at infinity.

## 3. Taking the finite part

Let epsilon=pi t. The elementary part of (7) integrates to

\[
\int_\epsilon^1(v^{-1}+2v^{-1/2}-3)\,dv
=-\log\epsilon+1-4\sqrt\epsilon+3\epsilon.
\tag{8}
\]

Because log(1/t)=log pi-log epsilon, equations (5), (7), and (8) prove existence and give

\[
\begin{split}
4\pi h_Q=1-\log\pi
&+\int_0^1v^{-1}\{\theta(1/v)^2-1\}\,dv\\
&+2\int_0^1v^{-1/2}\{\theta(1/v)-1\}\,dv\\
&+\int_1^\infty\{\theta(v)^2+2\theta(v)-3\}\,dv.
\end{split}
\tag{9}
\]

Expand the theta functions in (9). Every term in these three integrals is nonnegative, so exchanging sums and integrals is again justified by Tonelli's theorem. For r^2=k^2+l^2>0, substitution x=pi r^2/v gives

\[
\int_0^1v^{-1}e^{-\pi r^2/v}\,dv=E_1(\pi r^2).
\]

For the one-dimensional part, substitution w=1/v gives

\[
\int_0^1v^{-1/2}e^{-\pi m^2/v}\,dv=A(\pi m^2).
\]

The factor 4 in front of the one-dimensional sum in (1) is 2 from (9) times 2 for the two signs of m. Finally,

\[
\int_1^\infty e^{-av}\,dv=\frac{e^{-a}}a.
\]

Thus (9) equals the limit of (1). For completeness, putting y=sqrt(aw) in A(a), followed by integration by parts, gives

\[
A(a)=2\sqrt a\int_{\sqrt a}^\infty\frac{e^{-y^2}}{y^2}\,dy
=2e^{-a}-4\sqrt a\int_{\sqrt a}^\infty e^{-y^2}\,dy,
\]

which proves (3).

## 4. Bounding the omitted terms

For a>0,

\[
0<E_1(a)\leq\frac{e^{-a}}a,\qquad
0<A(a)\leq\frac{e^{-a}}a.
\tag{10}
\]

The first bound uses x>=a in its defining integral; the second uses w^(-3/2)<=1 for w>=1. In each brace in (1), the sum is therefore at most 2e^(-a)/a.

Put q=e^(-pi), p=(M+1)^2, and d=2M+3. The one-dimensional omitted Gaussian tail satisfies

\[
U_M:=\sum_{m=M+1}^\infty q^{m^2}
\leq\frac{q^p}{1-q^d},
\tag{11}
\]

because (M+1+j)^2>=p+dj for j>=0. Also

\[
S:=\sum_{m\in\mathbb Z}q^{m^2}
\leq1+\frac{2q}{1-q}=\frac{1+q}{1-q}.
\tag{12}
\]

Write S_M=sum_{|m|<=M}q^(m^2). The lattice Gaussian mass outside the square |k|,|l|<=M is

\[
S^2-S_M^2=(S-S_M)(S+S_M)\leq4S U_M.
\tag{13}
\]

Every omitted lattice term has k^2+l^2>=p. Using (10) and (13), its total contribution inside the brackets in (1) is at most 8S U_M/(pi p). The one-dimensional omitted contribution, including its factor 4, is at most 8U_M/(pi p). Division by 4 pi yields

\[
0\leq h_Q-H_M\leq\frac{2(S+1)U_M}{\pi^2p}
\leq\frac{4q^p}{\pi^2p(1-q)(1-q^d)},
\]

proving (2).

There is a separate way to check the tail count. The shell max(|k|,|l|)=r contains exactly 8r lattice points. On that shell k^2+l^2>=r^2. Applying (10) shell by shell, and bounding the one-dimensional terms separately, gives the additional valid bound

\[
h_Q-H_M\leq
\frac{4(M+1)+2}{\pi^2(M+1)^2}
\frac{q^{(M+1)^2}}{1-q^{2M+3}}.
\tag{13a}
\]

Indeed the two contributions are at most (4/pi^2)sum_{r>M}q^(r^2)/r and (2/pi^2)sum_{r>M}q^(r^2)/r^2. Bounding their denominators by M+1 and (M+1)^2, respectively, and applying (11) proves (13a). This independent shell count is weaker than (2) when M>=1 but also gives error below 10^(-21) at M=3 using q<1/20.

Here is a rational check of the stated M=3 accuracy. The elementary inequalities pi>3 and e^3>20 give q<1/20. The second inequality follows already from summing the terms through degree 8 of the positive exponential series at 3: that sum is 806769/40320>20. With p=16 and d=9, (2) is strictly less than

\[
\frac{4\,20^{-16}}{9\cdot16\cdot(19/20)^2}
=\frac{1600}{51984\cdot20^{16}}<10^{-21}.
\tag{14}
\]

The last inequality can be checked without floating point: 20^16=655360000000000000000, and multiplying this integer by 51984 is larger than 1600 times 10^21.

## 5. Independent check using spectral zeta regularization

For real s>1 define Z_Q(s)=sum_{k,l>=0,k+l>0}[pi^2(k^2+l^2)]^(-s). Mellin integration of (4) gives

\[
Z_Q(s)=\frac1{4\pi^s\Gamma(s)}
\int_0^\infty v^{s-1}\{\theta(v)^2+2\theta(v)-3\}\,dv.
\tag{15}
\]

Define the entire function

\[
\begin{split}
J(s)={}&\int_0^1v^{s-1}\left[v^{-1}\{\theta(1/v)^2-1\}
+2v^{-1/2}\{\theta(1/v)-1\}\right]dv\\
&+\int_1^\infty v^{s-1}\{\theta(v)^2+2\theta(v)-3\}\,dv.
\end{split}
\]

Exponential decay at both endpoints, locally uniformly in s and with any power of log v, justifies holomorphy and differentiation under the integrals. Splitting (15) at 1 and using (7) gives the meromorphic continuation

\[
Z_Q(s)=\frac1{4\pi^s\Gamma(s)}
\left[\frac1{s-1}+\frac2{s-1/2}-\frac3s+J(s)\right].
\tag{16}
\]

In particular, with gamma=-Gamma'(1), expansion at s=1 gives

\[
Z_Q(s)=\frac1{4\pi(s-1)}
+\frac{1+J(1)+\gamma-\log\pi}{4\pi}+O(s-1).
\tag{17}
\]

The relation between the zeta finite part B and the heat finite part is B=h_Q+gamma/(4 pi). To verify its sign directly, use

\[
\Gamma(s)Z_Q(s)=\int_0^\infty u^{s-1}K_Q(u)\,du.
\]

Subtract 1/(4 pi u) only over (0,1). The remaining integral at s=1 is

\[
\int_0^1\left(K_Q(u)-\frac1{4\pi u}\right)du+
\int_1^\infty K_Q(u)du=h_Q,
\]

as follows also by integrating K_Q from t to infinity. The left side has finite part B-gamma/(4 pi), because Gamma(s)=1-gamma(s-1)+O((s-1)^2). This proves the relation. Substituting (17) recovers (9) exactly. In particular, using the Laurent finite part itself as h_Q would introduce an erroneous gamma/(4 pi).

## 6. Check of boundary multiplicities and spatial scaling

Let F_T be the corresponding spectral sum on the unit flat torus, with eigenvalues 4 pi^2(k^2+l^2), k,l in Z, excluding zero. Let

\[
I(t)=\sum_{k,l\geq1}\frac{e^{-\pi^2(k^2+l^2)t}}{\pi^2(k^2+l^2)},\qquad
B(t)=\sum_{m\geq1}\frac{e^{-\pi^2m^2t}}{\pi^2m^2}.
\]

Directly counting signs and the two axes gives

\[
F_Q(t)=I(t)+2B(t),\qquad F_T(t/4)=I(t)+B(t).
\tag{18}
\]

The torus heat trace, or the same Gaussian transformation, shows that its leading heat singularity is 1/(4 pi u) with an integrable remainder near zero. Hence its heat finite part h_T exists. Dominated convergence gives B(t)->1/6. One way to verify the value without a spectral multiplicity convention is Parseval applied to x on (-pi,pi): its sine coefficients are 2(-1)^(m+1)/m, so 2 pi^2/3=4 sum_{m>=1}m^(-2), and sum m^(-2)=pi^2/6. Now (18) gives

\[
h_Q-h_T=\frac16+\frac{\log4}{4\pi}
=\frac16+\frac{\log2}{2\pi}.
\tag{19}
\]

The plus sign of the logarithm comes from evaluating F_T at t/4. This agrees with a separate count of the omitted and included axis modes. It checks both the Neumann boundary contribution and the heat-time normalization in (1).

## 7. Direct heat-sum check

A second finite approximation, useful for checking (1), uses the original quadrant sum. For t>0 and N>=0 let

\[
C_N(t)=\sum_{\substack{0\leq k,l\leq N\\k+l>0}}
\frac{e^{-\pi^2(k^2+l^2)t}}{\pi^2(k^2+l^2)}
-\frac{\log(1/t)}{4\pi}+\sqrt{t/\pi}-\frac{3t}{4}.
\]

Put r=N+1, alpha=pi^2 t and z=exp(-1/t). Then

\[
\begin{split}
0\leq h_Q-C_N(t)\leq{}&
\left(\frac2{\pi^2r}+\frac1{\pi^2r^2}\right)
\frac{e^{-\alpha r^2}}{1-e^{-\alpha(2r+1)}}\\
&+z\left\{\frac{t}{\pi(1-z)^2}
+\frac{t^{3/2}}{\sqrt\pi(1-z)}\right\}.
\end{split}
\tag{20}
\]

Here is a direct derivation. Applying (6) to (4) gives

\[
K_Q(u)=\frac1{4\pi u}+\frac1{2\sqrt{\pi u}}-\frac34+R(u),
\]

where R(u)>=0. Integrating from 0 to t after subtracting the area term yields

\[
h_Q=F_Q(t)-\frac{\log(1/t)}{4\pi}+\sqrt{t/\pi}
-\frac{3t}{4}+\int_0^tR(u)\,du.
\]

For 0<u<=t, the Gaussian tail estimates used in (11)–(12) give

\[
R(u)\leq\frac{e^{-1/u}}{\pi u(1-z)^2}
+\frac{e^{-1/u}}{\sqrt{\pi u}(1-z)}.
\]

Substitution x=1/u shows that the integral of e^(-1/u)/u is E1(1/t)<=tz. Also u^(-1/2)<=sqrt(t)/u, so the other integral is at most t^(3/2)z. This proves the second line of (20). To bound the omitted part of F_Q(t), note that the quadrant shell max(k,l)=j contains exactly 2j+1 points. Their denominators are at least pi^2 j^2. Sum the shell bounds and the geometric majorant starting at j=r. This proves the first line of (20).

The supplied verifier compares H_3 and H_5 with C_40(1/100). Its numerical assertions allow for rounding, and its analytic errors are (2) and (20). It refuses to compute unless the requested thread environment and process niceness are in force.

## Relation to random matching

The earlier report invokes Corollary 2 of Yunzong Xu, *Random Matching Between Distinct Distributions in Two Dimensions*, [arXiv:2610.40509v1](https://arxiv.org/abs/2610.40509v1). In that preprint's convention its square specialization states c_square=beta_sd+h_Q. Combining that statement with (1)–(2) gives

\[
\beta_{\rm sd}+H_M\leq c_{\square}\leq
\beta_{\rm sd}+H_M+
\frac{4e^{-\pi(M+1)^2}}
{\pi^2(M+1)^2(1-e^{-\pi})(1-e^{-\pi(2M+3)})}.
\]

This last assertion uses the preprint's matching theorem. The spectral evaluation above does not. No value for beta_sd is asserted.
