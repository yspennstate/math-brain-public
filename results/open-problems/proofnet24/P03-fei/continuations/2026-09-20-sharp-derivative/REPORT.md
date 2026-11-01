# FEI continuation: optimal marginal one-step constant and signed cancellation

20 September 2026. Owner-requested continuation by ChatGPT, GPT-6 Astra Pro.

**Full Friedgut–Kalai FEI is NOT proved in this continuation.** This report proves an improved all-dimensional auxiliary bound, not an upper bound of 5.395 for H(f)/I(f). The distinction is essential.

## 1. Quantitative result

For a Boolean sign function on G=F_2^n, with uniform measure, set

\[
p_s=\widehat f(s)^2,\qquad H(f)=-\sum_s p_s\log_2p_s,
\]
\[
f_z(x)=f(x)f(x+z),\qquad
D_\times(f)=2H(f)-\mathbb E_zH(f_z).
\]

Zero masses contribute zero. For a direction v, put

\[
\alpha_f(v)=\Pr[f(x)\ne f(x+v)],\quad
j_f(v)=\min\{\alpha_f(v),1-\alpha_f(v)\},
\]
\[
M(f)=\min_{(v_1,\ldots,v_n)\text{ a basis}}\sum_i j_f(v_i).
\]

Thus M(f)<=J(f)<=I(f), where J and I use the original coordinate directions. Define

\[
\phi(q)=2h_2(q)-h_2(2q(1-q)),\quad
\lambda_*:=\max_{0<q\le1/2}\frac{\phi(q)}q.
\]

**Theorem 1.** For every Boolean f, in every dimension,

\[
\boxed{0\le D_\times(f)\le2\lambda_*M(f)\le
\frac{2697377}{500000}M(f)=5.394754\,M(f).}
\tag{1}
\]

The exact optimal scalar coefficient has the certified bounds

\[
5.3947539099<2\lambda_*<5.3947539100.
\tag{2}
\]

Its unique maximizing q is in

\[
0.19943435135686<q_*<0.19943435135687.
\tag{3}
\]

The previous repository bound was D_cross<=6M. This continuation optimizes its one-coordinate entropy step exactly, improving that all-dimensional upper coefficient. It does not introduce the earlier uncertainty reduction as a new method.

If C_D denotes the best universal coefficient in D_cross<=C_D M, then

\[
\boxed{4\le C_D\le 2\lambda_*<5.394754.}
\tag{4}
\]

The lower endpoint follows from the two-variable phase (-1)^(x_1 x_2): its entropy is 2, every multiplicative derivative is a character or a constant, and M=1. Thus D_cross=4. The value 2 lambda_* is optimal for the scalar estimate used here, **not proved optimal for Boolean functions**. The stronger bound D_cross<=4M remains unproved in this report.

## 2. Reconstructed full proof of the uncertainty reduction

Let S,T be independent samples from p and put U=S+T. Define

\[
b_u(z)=\sum_s\widehat f(s)\widehat f(s+u)(-1)^{s\cdot z},
\qquad q_u=\sum_s p_s p_{s+u}.
\]

The Fourier coefficient of f_z at u differs from b_u(z) by the sign (-1)^(u dot z), so their squares agree. Parseval and Booleanity give

\[
\mathbb E_z b_u(z)^2=q_u,
\qquad \sum_u b_u(z)^2=1\quad\text{for every }z.
\]

Consequently P(U=u,Z=z)=b_u(z)^2/2^n is a probability law with Z uniform and U distributed as S+T. In particular,

\[
\mathbb E_zH(f_z)=H(U\mid Z).
\]

Since (S,T) and (S,U) carry the same information,

\[
\boxed{D_\times(f)=H(S\mid U)+I(U;Z).}
\tag{5}
\]

This proves nonnegativity without a numerical test.

For q_u>0, the real amplitude vector

\[
c_u(s)=\widehat f(s)\widehat f(s+u)/\sqrt{q_u}
\]

has squared coordinates distributed as S conditional on U=u. The normalized Walsh transform of c_u has squared coordinates distributed as Z conditional on U=u. Walsh entropic uncertainty therefore gives

\[
H(S\mid U=u)+H(Z\mid U=u)\ge n.
\]

Averaging and using H(Z)=n gives I(U;Z)<=H(S|U), and hence

\[
\boxed{D_\times(f)\le2H(S\mid S+T).}
\tag{6}
\]

For completeness, Walsh entropic uncertainty follows by interpolating the normalized Walsh operator's l_1-to-l_infinity norm 2^(-n/2) with its l_2 norm 1, obtaining

\[
\|Wc\|_{p'}\le2^{n(1/2-1/p)}\|c\|_p,
\quad1\le p\le2,\quad p'=p/(p-1).
\]

For a unit l_2 vector, differentiate the logarithms at p=2 from the left. The derivatives of log||c||_p and log||Wc||_(p') are respectively -H_nat(c^2)/4 and +H_nat((Wc)^2)/4. Since the inequality has equality at p=2, its left derivative yields H_nat(c^2)+H_nat((Wc)^2)>=n ln 2. Zero coordinates are handled by continuity. This is the standard entropic-uncertainty argument already used in the repository.

## 3. Affine minimization and the scalar problem

Invertible linear input changes permute Fourier labels and uniform shifts. Multiplication by an output character translates the Fourier spectrum and changes each f_z only by a constant sign. Thus both H and D_cross are invariant under these operations.

Choose a basis attaining M. An output character can complement precisely those directional influences above 1/2. In the resulting coordinates, q_i=Pr(S_i=1) lies in [0,1/2] and sum_i q_i=M(f). Conditional entropy subadditivity and reduction under conditioning give

\[
H(S\mid U)\le\sum_iH(S_i\mid U)\le\sum_iH(S_i\mid U_i).
\]

Because S_i,T_i are independent Bernoulli(q_i),

\[
H(S_i\mid S_i+T_i)=2h_2(q_i)-h_2(2q_i(1-q_i))=\phi(q_i).
\]

Combining this with (6) proves D_cross<=2 lambda_* M. When M=0, all derivatives along a basis are constant signs; integrating those signs along the basis shows that f is a character times a constant. Then D_cross=H=M=0.

The scalar inequality phi(q)<=lambda_* q is sharp as a scalar inequality. Independent Bernoulli(q_*) coordinates also make the conditional-entropy subadditivity exact. Such a general product probability law must not be silently assumed to be a squared Boolean spectrum. In particular, these observations do not certify the sharp Boolean coefficient C_D.

## 4. Unique scalar maximizer and certified coefficient

Use natural-log entropy h temporarily and write

\[
\Phi(q)=2h(q)-h(r),\qquad r=2q(1-q).
\]

Then

\[
\Phi'(q)=2\ln\frac{1-q}{q}-2(1-2q)\ln\frac{1-r}{r},
\]
\[
\boxed{\Phi''(q)=4\left(\ln\frac{1-r}{r}-\frac1{1-r}\right).}
\tag{7}
\]

The bracket is strictly decreasing in r: its derivative is

\[
-\frac1{1-r}-\frac1r-\frac1{(1-r)^2}<0.
\]

Since r increases from 0 to 1/2, Phi'' changes sign exactly once, from positive to negative. It tends to positive infinity at q=0 and equals -8 at q=1/2.

Let G(q)=q Phi'(q)-Phi(q). Then G'(q)=q Phi''(q), G(0+)=0, and G(1/2)=-ln2. Thus G first increases from zero and then decreases, crossing zero exactly once in (0,1/2). Since

\[
\frac{d}{dq}\frac{\Phi(q)}q=\frac{G(q)}{q^2},
\]

the ratio has precisely one maximum, at q_*. Also Phi(q)/q tends to 2 ln2 at zero and has that same value at q=1/2.

The accompanying standard-library checker certifies G(a)>0 and G(b)<0 for the rational endpoints a,b in (3). This brackets the unique maximum; it is not a grid-based guess. Equation (7) is already negative at q=1/6, and the checker certifies that sign. Therefore Phi' is decreasing throughout [a,b]. At the maximizer Phi(q_*)/q_*=Phi'(q_*), so

\[
\frac{2\Phi'(b)}{\ln2}\le2\lambda_*\le
\frac{2\Phi'(a)}{\ln2}.
\]

Rational logarithm enclosures give (2), and the rational corollary in (1) follows.

All logarithms in the checker are enclosed using range reduction and

\[
\ln x=2\sum_{j=0}^{L-1}\frac{z^{2j+1}}{2j+1}+R_L,
\quad z=\frac{x-1}{x+1},\quad1\le x\le2,
\]
\[
0\le R_L\le\frac{2z^{2L+1}}{(2L+1)(1-z^2)}.
\]

It uses L=60, exact fractions, and no floating-point acceptance tolerance.

## 5. A signed identity retained from the archive, and a translated-square consequence

The attempt also pursued an all-Boolean-function expansion rather than another symmetric subclass. The underlying entropy coefficient formula was recovered in the older repository report `runs/2026-09-16/2026-09-16_13-31-31__run-report.md`, Section 1.3, where it is credited to the September 13 R32 archive. **That coefficient formula and its alternating signs are inherited results, not new discoveries of this continuation.** The derivation below makes the normalization explicit and records consequences used in this attempt.

Set N=2^n. Regard H itself as a function on the 2^N possible sign truth tables. For a subset A of physical points define

\[
\chi_A(f)=\prod_{x\in A}f(x).
\]

Its truth-table Fourier coefficient vanishes unless |A| is even and the XOR of all points in A is zero. No nonempty two-point set has zero XOR. For even k>=4, the coefficient at any zero-XOR k-set is

\[
\boxed{w_{N,k}=
\frac{4(-1)^{k/2+1}}{N\ln2}
\int_0^\infty\frac{\sin^k t\cos^{N-k}t}{t^3}\,dt.}
\tag{8}
\]

The integral is positive. Thus orders 0 mod 4 have negative coefficients, and orders 2 mod 4 have positive coefficients, whenever such sets exist.

A derivation: write psi(u)=-u^2 log_2(u^2), expand psi(N^-1 sum_x f(x)) in the truth-table characters, and sum over the original Fourier labels. Orthogonality gives the factor N times the zero-XOR indicator. To derive its k-th coefficient, use

\[
F(u)=\int_0^\infty
\frac{\cos(tu)-1+(tu)^2\mathbf1_{t\le1}/2}{t^3}\,dt.
\]

Scaling gives F(u)=u^2 F(1)+(u^2/2)ln|u|. The constant and quadratic terms vanish in a k-th truth-table coefficient for k>=4. The remaining cosine coefficient is (-1)^(k/2)sin^k(t/N)cos^(N-k)(t/N). This yields (8). Convergence near zero follows from k>=4; convergence at infinity follows from t^-3. The case u=0 follows by continuity.

Since H(1)=0, the entire entropy has the exact finite expansion

\[
H(f)=-\sum_{\substack{\varnothing\ne A\subseteq G\\|A|\text{ even},\ \oplus A=0}}
 w_{N,|A|}\,[1-\chi_A(f)].
\tag{9}
\]

Let m_A(f)=E_z chi_(A+z)(f), the average over physical translations. Summing (9) over translation orbits gives H(f)=-sum_A w_(N,|A|)[1-m_A(f)]. Moreover,

\[
\chi_A(f_z)=\chi_A(f)\chi_{A+z}(f).
\]

The coefficients are constant on translation orbits, so summing first over each orbit proves

\[
\boxed{D_\times(f)=-\sum_Aw_{N,|A|}[1-m_A(f)]^2.}
\tag{10}
\]

This is an exact signed expression for the universal quantity in Theorem 1. Positive coefficients at orders 2 mod 4 remain negative credits in (10). They cannot be discarded without an additional estimate. The report does not claim a comprehensive archive search establishing that the translated-square packaging has no antecedent.

## 6. The unsigned fourth-order contribution is exponentially too large

Here is an explicit all-dimensional obstruction to paying the positive summands of (10) separately. Let n>=2 be even and take

\[
f(x)=(-1)^{x_1x_2+x_3x_4+\cdots+x_{n-1}x_n}.
\]

The two-variable factors have flat four-point Fourier spectra, so H(f)=n. Every derivative is a character or constant; the polar form is nondegenerate, so j_f(v)=1/2 for every nonzero direction. Therefore

\[
D_\times(f)=2n,\qquad M(f)=n/2,\qquad D_\times(f)/M(f)=4.
\]

A four-point zero-XOR set is an affine plane A={x,x+u,x+v,x+u+v}. Its product under f equals (-1)^(B(u,v)), independent of x. Nondegeneracy gives exactly N/2 choices of v with B(u,v)=1 for every u!=0. Dividing the N(N-1)N/2 ordered choices (x,u,v) by the 24 parametrizations of one plane gives

\[
\#\{A:m_A(f)=-1\}=N^2(N-1)/48.
\tag{11}
\]

Write beta_N=-w_(N,4)>0. The fourth-order contribution to D_cross alone equals

\[
D^{(4)}_\times(f)=4\beta_N\,N^2(N-1)/48.
\]

For 0<=t<=1/sqrt(N)<=1/2, sin t>=t(1-t^2/6)>=(23/24)t, so sin^4 t>=t^4/2. Also cos t>=1-t^2/2 and Bernoulli's inequality gives cos^(N-4)t>=1/2 on that interval. Hence

\[
\int_0^\infty\frac{\sin^4t\cos^{N-4}t}{t^3}\,dt
\ge\frac1{8N},\qquad
\beta_N\ge\frac1{2(\ln2)N^2}.
\]

Consequently,

\[
\boxed{\frac{D^{(4)}_\times(f)}{M(f)}
\ge\frac{2^n-1}{12(\ln2)n}\longrightarrow\infty,}
\tag{12}
\]

even though the complete signed ratio is exactly 4. This is not an FEI counterexample. It is a precise obstruction to an unsigned or separately charged fourth-order proof. Earlier R32 work already emphasized retaining signs; (11)-(12) give the explicit quadratic-family obstruction used in this continuation.

Exact coefficient calculations give fourth-order ratios approximately 4, 4.1584, 10.4324 and 30.9012 in dimensions 2,4,6,8, while the complete ratio remains exactly 4. Only the coefficient formula is evaluated for N=64,256; no collection of all 2^64 or 2^256 truth tables is enumerated.

## 7. A concrete failure of the negative-type entropy-kernel approach

For n=4, the physical six-set A={0,1,2,4,8,15} has zero XOR. Its truth-table Fourier coefficient is exactly

\[
\widehat H(A)=
\frac{48-81\log_2 3+125\log_2 5-49\log_2 7}{16384}.
\tag{13}
\]

The checker proves

\[
0.004412759895<\widehat H(A)<0.004412759896.
\]

Thus the kernel K(f,g)=H(fg), on the finite group of Boolean truth tables under pointwise multiplication, is **not conditionally negative definite**. Indeed, choose real weights c_f=chi_A(f). They sum to zero, while character orthogonality gives

\[
\sum_{f,g}c_fc_gH(fg)=2^{2N}\widehat H(A)>0,
\]

contrary to the defining nonpositivity of a conditionally negative definite kernel. This rules out the attempted direct negative-type/Hilbert-distance argument. It does not rule out all two-function entropy inequalities or all uses of signed kernel decompositions.

## 8. Why the improved one-step bound still does not close FEI

For successive independent uniform multiplicative derivatives f_k, algebraic degree over F_2 eventually falls to zero. Therefore

\[
H(f)=\frac12\sum_{k\ge0}2^{-k}\mathbb E D_\times(f_k).
\tag{14}
\]

A universal estimate for the discounted sum of M would allow Theorem 1 to be summed, but that estimate is false. This obstruction was already proved in the preceding one-step report; it is retained, not offered as new progress.

For w_n=1-2 1_{x=0}, M(w_n)=n2^(1-n). After k linearly independent shifts the derivative is the sign of their k-dimensional span; dependent shifts make it constant. For 0<=k<=n-2 its affine minimum is (n-k)2^(k+1-n), conditional on independence, whose probability is

\[
P_{n,k}=\prod_{j=0}^{k-1}(1-2^{j-n}).
\]

Thus

\[
\frac{\sum_k2^{-k}\mathbb E M((w_n)_k)}{M(w_n)}
=\frac1n\sum_{k=0}^{n-2}(n-k)P_{n,k}\sim n/2.
\tag{15}
\]

Replacing 6 by 5.394754, or even proving the candidate 4, does not remove this divergence. The remaining full-scope task is a genuinely summable signed allocation estimate, or the live universal hereditary-erasure bound, not another application of (1).

The attempted negative-type shortcut fails by (13), and discarding signs fails by (12). Any continuation using (10) must control the signed aggregate, not its positive terms separately. No such universal aggregate bound has been proved here.

## 9. Checks, failed stronger route, and provenance

Run `python3 verify_continuation.py --output verification.json`. The committed output is actual output of this included standard-library checker. It establishes the scalar bracket and exact logarithmic certificates above, and verifies both (9) and (10) as exact rational linear forms in logarithms of primes on all 278 Boolean truth tables in dimensions 0--3 and 64 distinct selected tables in dimension 4. All 342 cases also pass the new bound. They also pass the tentative coefficient 4, but this is explicitly finite evidence only.

The exploratory scripts separately exhaust 32,906 truth tables modulo global negation through dimension four and sample 150 cases per dimension from five through nine. Floating-point logs in those experiments do not supply universal or exact optimality certificates. The largest observed D/M was 4.

A proposed extension of the candidate coefficient 4 to arbitrary real Fourier amplitudes is false. Let the two amplitudes be sqrt(119/120), sqrt(1/120), put q=1/120 and t=4q(1-q). In the normalized two-copy output construction the first output-bit probability is z0=(1+t)/2, and

\[
D_{\rm real}=2h_2(q)-z_0 h_2(t/(1+t)).
\]

Its influence is q, and the checker proves

\[
D_{\rm real}-4q>48014467/250000000000>0.
\]

This function is not Boolean; this is a counterexample to the relaxation, not to FEI or the Boolean coefficient-4 candidate. Booleanity's uniform-Z property in Section 2 must not be removed.

### Actual source consumption

- `proofnet24/P03-fei/README.md`, blob `9201da45afcf21156ae078cc505d37b57a1ae4b7`, read in full. Preserves the live universal gap and retired shortcuts.
- `proofnet24/P03-fei/scheduled-continuation/runs/2026-09-19/2026-09-19T18-46-55Z__report.md`, blob `2bee28b73ccddc731c5b16022412981b7e0a94f7`, lines 1--95 and 70--230 retrieved. The uncertainty method, affine reduction and nonsummability obstruction are credited to that work. Its later-refuted potential proposals are not reused.
- `proofnet24/P03-fei/runs/2026-09-16/2026-09-16_13-31-31__run-report.md`, Section 1.3 read in the returned opening text. It records the R32 truth-table coefficient formula in nats. This report converts it to bits and does not claim to have reread the entire R32 archive.
- Gonzalez--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, June 9, 2026. Current primary-source introduction and restriction discussion consulted: <https://arxiv.org/html/2606.00246v2>. It describes partial classes and an unresolved unrestricted induction estimate, not a full FEI proof.

Superseded targets checked: no use of the false pointwise erasure converse, Han's refuted absolute-overlap selector, retired full-resolvent bounds, universal fixed-coefficient affine-drift payments, or unsigned replacement of R32 credits.

No independent audit, formal verification, exhaustive publication-priority review, new schedule, email, Drive upload, or external paid computation is claimed. The mathematical contribution is separate from GitHub delivery and later worker uptake.
