# QFORM fixed-multiplicity improvement — account04/B08

Run: \`20260924T141600Z-account04-B08-fixedmult-improvement-r1\`

Status: **ESSENTIAL_STEP_APPLIED**. This is a rigorous constant improvement for the already independently reviewed nine-eigenvalue theorem. It does **not** solve the unrestricted three-eigenvalue conjecture.

## Source pins

- baseline fixed-multiplicity manuscript: commit \`7c0d6e60946b19423e6400a12d34b473cf0591e2\`, blob \`183ccd294763214e6a707e8d4749ff9a8cf7006d\`;
- nine-eigenvalue proof candidate: commit \`8ff490c177d0cd7d6f33130f1431785e312a9d10\`;
- consolidated source reconstruction: commit \`18c0707d32a6b405f159f690f17a8df5365b2755\`;
- independent end-to-end PASS: account01/B16, commit \`54ec2a651d854563f8db0d92c4c3426f76551786\`;
- independent audit and prior \(2582\) sharpening: account03/B14, commit \`9861ed55f7865b2a67346a66bc178eb7f81df190\`;
- continuity audit: account03/B15, commit \`f5fdb10a327aa665f10e2cb9e0c9c264e5d95964\`.

## The sharpened theorem

Let \(X_1,\dots,X_n\) be independent real random variables with densities bounded by \(K\). Let \(A=A^\top\), \(b\in\mathbb R^n\), \(c\in\mathbb R\), and write \(s_j(A)\) for the \(j\)-th singular value. Then

\[
s_9(A)\ge s>0
\quad\Longrightarrow\quad
\operatorname*{ess\,sup}_{t\in\mathbb R}
p_{X^\top A X+b^\top X+c}(t)
<
\frac{2514K^2}{s}.
\]

The structural proof is the independently reviewed \(s_9\) compiler cited above. The only new work here is an exact rational sharpening of its scalar-pivot bottleneck.

## Exact quarter-potential constant

The audited proof uses

\[
C_q
=
2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8).
\]

I certify

\[
\Gamma(3/8)<\frac{1187}{500}=2.374.
\]

For \(x\in[0,1]\), the degree-eight even alternating Taylor truncation gives

\[
e^{-x}\le
\sum_{k=0}^{8}\frac{(-x)^k}{k!},
\]

hence

\[
\int_0^1 x^{-5/8}e^{-x}\,dx
\le
\sum_{k=0}^{8}\frac{(-1)^k}{k!}\frac{8}{8k+3}.
\]

On \([1,8]\), partition into intervals of length \(1/16\). On \([a,b]\), choose a rational \(u_a\) with \(u_a^8a^5\ge1\), so \(x^{-5/8}\le u_a\). With

\[
L_{60}(x)=\sum_{k=0}^{60}\frac{x^k}{k!}
\]

and the positive geometric tail bound

\[
U_{60}(x)
=
L_{60}(x)+
\frac{x^{61}/61!}{1-x/62},
\qquad 0\le x\le8,
\]

we have \(L_{60}(x)<e^x<U_{60}(x)\), and therefore

\[
\int_a^b x^{-5/8}e^{-x}\,dx
\le
u_a\left(\frac1{L_{60}(a)}-\frac1{U_{60}(b)}\right).
\]

Finally,

\[
\int_8^\infty x^{-5/8}e^{-x}\,dx
\le
u_8e^{-8}
<
\frac{u_8}{L_{60}(8)}.
\]

The exact rational sum is

\[
<2.37376387429124<\frac{1187}{500}.
\]

All interval inequalities, including every \(u_a^8a^5\ge1\), are checked in \`verify.py\`.

The remaining elementary rational bounds are

\[
2^{5/8}<\frac{1543}{1000},
\qquad
\pi^{-1/4}<\frac{3759}{5000},
\qquad
e^{3/8}<\frac{182}{125}.
\]

They follow respectively by raising to the eighth or fourth power, using \(\pi>3.14\), and using \(e<68/25\) together with

\[
\left(\frac{68}{25}\right)^3
<
\left(\frac{182}{125}\right)^8.
\]

Thus

\[
C_q
<
\frac{1543}{1000}
\frac{3759}{5000}
\frac{182}{125}
\frac{1187}{500}
=
4.0096857493056
<
\frac{401}{100}.
\]

## Scalar-pivot ledger

The audited scalar-pivot branch gives the truncated half-potential

\[
H_{\mathrm{sc,tr}}
<
10\left[
\pi+4\log2+2L_{\log}
\right],
\qquad
L_{\log}<4+4\log C_q.
\]

Exact positive Taylor sums certify

\[
\log2<\frac{347}{500},
\qquad
\log\frac{401}{100}<\frac{139}{100}.
\]

Therefore

\[
L_{\log}
<
4+4\frac{139}{100}
=
\frac{239}{25},
\]

and, using \(\pi<22/7\),

\[
H_{\mathrm{sc,tr}}
<
10\left[
\frac{22}{7}
+4\frac{347}{500}
+2\frac{239}{25}
\right]
=
250.388571428572.
\]

The normalized tail contributes \(<1\), so

\[
H_{\mathrm{sc}}<251.388571428572.
\]

The scalar pivot normalization has \(\eta=10^{-2}\), hence its outer factor is \(\eta^{-1/2}=10\). Consequently,

\[
\|p_Q\|_\infty
<
10H_{\mathrm{sc}}
<
2513.88571428572
<
2514
\]

in the scalar-pivot branch.

## Branch comparison on the same proof compiler

The other independently audited branches remain below this value:

\[
C_{\mathrm{no\ pivot}}<2371,
\qquad
C_{\mathrm{definite}}<32,
\qquad
C_{\mathrm{indefinite}}<251.
\]

Hence the scalar branch remains the maximum, and the universal compiler constant is \(2514\).

## Scope boundary

This proves a stronger fixed-multiplicity theorem at \(s_9(A)\). It does not reduce the spectral threshold from nine to three. In particular, the original assertion with only three singular values at least one remains open; no rotation of the independent coordinates and no unproved conditional-density cap is used here.
