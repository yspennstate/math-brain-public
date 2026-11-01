# T228: smooth and strictly decreasing exact tail index

Author/reviewer: A14. Date: 23 October 2026.

Base source: `campaign/proofs/T228_EXPLICIT_CLOSURE.md`, version 2, SHA-256

```text
a1dbdbb1e99a85749143f44dd8b7d7e264fb550d285c5667f69f1a35ff87c38f
```

This supplement proves the learning-rate dependence of the index in the base source. Its analysis of the scalar multiplier is self-contained. Its final stationary-tail comparison uses the base source's exact-tail conclusion with a strictly positive finite constant. It makes no claim about literature priority.

## Statement and scope

Let \(A\sim N(0,1)\), let

\[
 I=[99/100,101/100],\qquad J=(49/50,51/50),
 \qquad \xi_\eta=|1-\eta A^2|,
 \qquad h(\eta,p)=\mathbb E\xi_\eta^p.
\]

For every \(\eta\in J\), there is a unique positive solution \(\alpha(\eta)\) of

\[
h(\eta,\alpha(\eta))=1,
\]

and it belongs to \((1,2)\). The function \(\alpha:J\to(1,2)\) is \(C^\infty\) and satisfies

\[
\boxed{
\alpha'(\eta)
=-\frac{\partial_\eta h(\eta,\alpha(\eta))}
         {\partial_p h(\eta,\alpha(\eta))}<0.
}
\tag{1}
\]

In particular, smoothness on the closed interval \(I\) means restriction of this smooth function on the open neighborhood \(J\), so the endpoint derivatives have an unambiguous extension.

Writing \(\alpha=\alpha(\eta)\), the two partial derivatives in (1) are

\[
\begin{aligned}
N_\eta:=\partial_\eta h(\eta,\alpha)
 &=-\alpha\,\mathbb E\!\left[
 A^2\operatorname{sgn}(1-\eta A^2)
 |1-\eta A^2|^{\alpha-1}\right]>0,\\
m_\eta:=\partial_p h(\eta,\alpha)
 &=\mathbb E\!\left[\xi_\eta^\alpha\log\xi_\eta\right]>0.
\end{aligned}
\tag{2}
\]

All displayed expectations are absolutely convergent. Terms at \(\xi_\eta=0\) can be assigned their continuous value zero; that event also has probability zero. Equivalently,

\[
\alpha'(\eta)
=\frac{\alpha\,\mathbb E[
A^2\operatorname{sgn}(1-\eta A^2)\xi_\eta^{\alpha-1}]}
{\mathbb E[\xi_\eta^\alpha\log\xi_\eta]}.
\tag{3}
\]

The following deliberately coarse, entirely analytic bounds hold on \(I\):

\[
\frac1{50}<m_\eta<16,
\qquad
\frac{25}{101}<N_\eta<\frac{303}{50},
\qquad
\boxed{\frac{25}{1616}<-\alpha'(\eta)<303.}
\tag{4}
\]

For the nonlinear SGD model of the base source, let \(\pi_\eta\) be its invariant law and \(C_\eta\in(0,\infty)\) its exact absolute-tail constant. For every fixed pair \(\eta_1<\eta_2\) in \(I\),

\[
\frac{\pi_{\eta_2}(|x|>t)}{\pi_{\eta_1}(|x|>t)}
\sim \frac{C_{\eta_2}}{C_{\eta_1}}
t^{\alpha(\eta_1)-\alpha(\eta_2)}
\longrightarrow\infty.
\tag{5}
\]

This is a precise asymptotic sense in which increasing the stepsize makes the stationary tails heavier. It is not a claim that \(C_\eta\) is monotone, that the whole distribution is stochastically ordered at every threshold, or that the convergence in (5) is uniform over pairs of stepsizes.

## 1. The unique positive root on an open neighborhood

Writing \(\varphi\) for the standard normal density, the identities
\(\mathbb E(1-A^2)=0\) and \((a\varphi(a))'=(1-a^2)\varphi(a)\) give
\(\mathbb E|1-A^2|=4\int_0^1(1-a^2)\varphi(a)\,da=4\varphi(1)\).
The rational estimates \(\pi>3.14\) and \(e>2.718\) then give the same elementary bound as the base source:

\[
\mathbb E|1-A^2|=\frac4{\sqrt{2\pi e}}<\frac{97}{100}.
\]

Consequently, since \(\mathbb EA^2=1\),

\[
h(\eta,1)
\le\mathbb E|1-A^2|+|\eta-1|
<\frac{99}{100}<1
\quad(\eta\in J),
\tag{6}
\]

and the stronger bound \(h(\eta,1)<49/50\) holds on \(I\). Also

\[
h(\eta,0)=1,
\qquad h(\eta,2)=1-2\eta+3\eta^2>1
\quad(\eta\in J),
\tag{7}
\]

because \(\eta>49/50>2/3\).

For fixed \(\eta>0\), all nonnegative moments of \(\xi_\eta\) are finite. The distribution of \(\log\xi_\eta\) is nonconstant, so \(p\mapsto h(\eta,p)\) is strictly convex; this also follows from the strictly positive second derivative justified below. Equations (6)–(7), continuity, and strict convexity give a root in \((1,2)\). They give uniqueness among all positive \(p\): the function lies strictly below 1 between 0 and its positive root, and its derivative at that root is positive, after which convexity makes it strictly increasing above 1. No invariant-law assertion outside \(I\) is needed for this extension of the index.

## 2. Integrability and smoothness despite the moving zero

The variable \(A^2\) has density \(x^{-1/2}e^{-x/2}/\sqrt{2\pi}\) for \(x>0\). The change of variables \(y=\eta x\) gives

\[
h(\eta,p)
=\frac1{\sqrt{2\pi}}
\int_0^\infty
|1-y|^p y^{-1/2}\eta^{-1/2}e^{-y/(2\eta)}\,dy.
\tag{8}
\]

This integral is finite throughout

\[
\mathcal D=\{(\eta,p):\eta>0,\ p>-1\}.
\]

The only interior singularity in (8) is now fixed at \(y=1\). For any nonnegative integers \(r,s\), differentiation \(r\) times in \(\eta\) and \(s\) times in \(p\) gives the formal integrand

\[
|1-y|^p(\log|1-y|)^s y^{-1/2}
\partial_\eta^r\!\left(\eta^{-1/2}e^{-y/(2\eta)}\right).
\tag{9}
\]

These derivatives can all be integrated. To justify this locally uniformly, fix a compact rectangle

\[
[a,b]\times[p_0,p_1]\subset\mathcal D,
\quad a>0,\quad p_0>-1.
\]

Every \(\eta\)-derivative of the density factor is the same exponential factor multiplied by a polynomial in \(y\) whose coefficients are uniformly bounded on \([a,b]\). An integrable envelope for (9) is obtained on three regions:

* Near \(y=0\), the factors involving \(1-y\) and its logarithm are bounded, and the remaining possible singularity is \(y^{-1/2}\).
* Near \(y=1\), all density derivatives are bounded, and an envelope is a constant times \(|1-y|^{p_0}(1+|\log|1-y||^s)\).
* For large \(y\), a fixed polynomial in \(y\), times a fixed power of \(\log y\), times \(e^{-y/(2b)}\), is an integrable envelope.

The middle envelope is integrable because, for every \(q>-1\), every finite \(s\ge0\), and \(0<\varepsilon<1\),

\[
\int_0^\varepsilon u^q|\log u|^s\,du
=\int_{-\log\varepsilon}^{\infty}
e^{-(q+1)v}v^s\,dv<\infty.
\tag{10}
\]

Dominated differentiation, iterated on arbitrary compact rectangles, therefore proves

\[
h\in C^\infty(\mathcal D).
\tag{11}
\]

In particular, \(\mathbb E[\xi_\eta^p|\log\xi_\eta|^s]<\infty\) for \(p>-1\), including \(\mathbb E|\log\xi_\eta|<\infty\). In the original Gaussian variable, the same logarithmic fact follows because the zeros \(A=\pm\eta^{-1/2}\) are simple: \(|1-\eta A^2|\) is comparable to distance from the relevant zero in a sufficiently small neighborhood, and the Gaussian density is bounded there. Thus these are ordinary integrable logarithmic singularities, not excluded exceptional neighborhoods.

The change of variables in (8) matters for the all-orders assertion. Repeatedly differentiating \(|1-\eta A^2|^p\) directly in \(\eta\) would eventually produce nonintegrable pointwise derivatives for \(1<p<2\); that procedure does not justify (11). Moving the scale dependence into the density avoids it.

## 3. First derivative formulas and positivity of the denominator

Differentiation in \(p\), justified by Section 2, yields

\[
\partial_p h(\eta,p)
=\mathbb E[\xi_\eta^p\log\xi_\eta],
\qquad
\partial_{pp}h(\eta,p)
=\mathbb E[\xi_\eta^p(\log\xi_\eta)^2]>0.
\tag{12}
\]

For \(p>1\), a direct first differentiation in \(\eta\) is also justified. The scalar function \(v\mapsto|v|^p\) is continuously differentiable, including at zero. On a compact parameter set with \(p\in[p_0,p_1]\subset(1,\infty)\) and \(\eta\in[a,b]\subset(0,\infty)\), the absolute value of its derivative is bounded by

\[
p_1 A^2\left[1+(1+bA^2)^{p_1-1}\right],
\]

which is Gaussian-integrable. Hence

\[
\partial_\eta h(\eta,p)
=-p\,\mathbb E[A^2\operatorname{sgn}(1-\eta A^2)
\xi_\eta^{p-1}].
\tag{13}
\]

An alternative, nonsingular expression follows by differentiating (8):

\[
\partial_\eta h(\eta,p)
=\frac{\mathbb E[A^2\xi_\eta^p]-h(\eta,p)}{2\eta}.
\tag{14}
\]

This last identity holds on all of \(\mathcal D\). At the root its numerator is \(\mathbb E[A^2\xi_\eta^\alpha]-1\).

Strict convexity in \(p\), applied between 1 and \(\alpha\), gives

\[
m_\eta
>\frac{h(\eta,\alpha)-h(\eta,1)}{\alpha-1}
=\frac{1-h(\eta,1)}{\alpha-1}>0.
\tag{15}
\]

On \(I\), \(1-h(\eta,1)>1/50\) and \(0<\alpha-1<1\), proving \(m_\eta>1/50\).

## 4. Strict positivity of the stepsize partial derivative

Fix a root \((\eta,\alpha)\) with \(\eta\in J\), and hold \(p=\alpha>1\) fixed. The function

\[
g(u)=\mathbb E|1-uA^2|^p,\qquad u\in\mathbb R,
\]

is strictly convex. Indeed, \(v\mapsto|v|^p\) is strictly convex, and for any two distinct \(u\)'s their affine arguments are distinct whenever \(A^2>0\), which holds almost surely. Expectations preserve the resulting strict inequality. The function is differentiable by the same domination as in Section 3.

Here \(g(0)=g(\eta)=1\). The strict supporting-line inequality at \(u=\eta\) is

\[
g(0)>g(\eta)-\eta g'(\eta).
\]

Therefore \(\eta g'(\eta)>0\), and \(\eta>0\) gives

\[
N_\eta=g'(\eta)>0.
\tag{16}
\]

The positivity is not an assertion that \(|1-\eta A^2|\) increases pointwise with \(\eta\); that is false for some samples. It comes from strict convexity at the positive return of the moment curve to its value at zero.

## 5. Smooth root and strict decrease

At every \((\eta,\alpha(\eta))\) with \(\eta\in J\), (11) and (15) verify the hypotheses of the smooth implicit-function theorem for \(h(\eta,p)-1=0\). It supplies a smooth root function near that point. Uniqueness of the positive root makes these local functions agree on overlaps, producing \(\alpha\in C^\infty(J)\).

Differentiating the defining identity gives

\[
0=\partial_\eta h(\eta,\alpha(\eta))
+\partial_p h(\eta,\alpha(\eta))\alpha'(\eta).
\]

Equations (15)–(16) prove (1)–(3) and strict decrease throughout \(J\).

## 6. Exact rational bounds on the stated interval

Only Gaussian moments and elementary convexity are needed for (4). First, put \(u=\eta/2\). On \(I\),

\[
\mathbb E|1-uA^2|^2
=1-2u+3u^2
\le\frac{30203}{40000}<\frac{49}{64}.
\tag{17}
\]

The quadratic increases for \(u>1/3\), so its maximum here is attained at \(u=101/200\), giving the displayed fraction. Since \(1<\alpha<2\), the moment inequality yields

\[
g(\eta/2)
\le\left(\mathbb E|1-(\eta/2)A^2|^2\right)^{\alpha/2}
\le\left(\frac{30203}{40000}\right)^{\alpha/2}
<\frac78.
\tag{18}
\]

The last step uses that the base is below 1 and \(\alpha/2>1/2\). A convex secant ending at \(\eta\), together with \(g(\eta)=1\), now gives

\[
N_\eta\ge\frac{g(\eta)-g(\eta/2)}{\eta/2}
>\frac1{4\eta}\ge\frac{25}{101}.
\tag{19}
\]

For the upper bound in (13), discard its nonpositive contribution from \(\eta A^2<1\). On the remaining event put \(r=\eta A^2>1\). Since \(0<\alpha-1<1\),

\[
(r-1)^{\alpha-1}<r^{\alpha-1}<r.
\]

Therefore, using \(\mathbb EA^4=3\),

\[
0<N_\eta
\le\alpha\,\mathbb E[A^2(\eta A^2-1)^{\alpha-1};\eta A^2>1]
<2\eta\,\mathbb EA^4
=6\eta\le\frac{303}{50}.
\tag{20}
\]

For the denominator, discard the nonpositive contribution from \(\xi_\eta\le1\). On \(\xi_\eta>1\), one has \(\xi_\eta=\eta A^2-1<\eta A^2\), while \(\alpha<2\) and \(\log t\le t\) for \(t\ge1\). Thus, using \(\mathbb EA^6=15\),

\[
0<m_\eta
\le\mathbb E[\xi_\eta^\alpha\log\xi_\eta;\xi_\eta>1]
\le\mathbb E[\xi_\eta^3;\xi_\eta>1]
<15\eta^3
\le15(101/100)^3<16.
\tag{21}
\]

Together with (15), (19), and (20), this proves all of (4). These bounds certify a nonzero sensitivity and finiteness; they are not numerical approximations to the actual derivative. Integration also gives, for \(\eta_1<\eta_2\) in \(I\),

\[
\frac{25}{1616}(\eta_2-\eta_1)
<\alpha(\eta_1)-\alpha(\eta_2)
<303(\eta_2-\eta_1).
\tag{22}
\]

## 7. Consequences for the nonlinear stationary law

The base source considers the genuinely nonlinear activation \(s(z)=z+10^{-3}\tanh z\), fresh independent \(A,E\sim N(0,1)\), and

\[
X_{k+1}=X_k-\eta A_k s'(A_kX_k)(s(A_kX_k)-E_k).
\]

For each fixed \(\eta\in I\), it establishes a unique invariant law \(\pi_\eta\) and

\[
\pi_\eta(|x|>t)=C_\eta t^{-\alpha(\eta)}(1+o(1)),
\qquad 0<C_\eta<\infty.
\tag{23}
\]

For a fixed pair \(\eta_1<\eta_2\), division of their two asymptotics is legitimate because both constants are positive. Since \(\alpha(\eta_1)>\alpha(\eta_2)\), it proves (5). In particular, the larger-stepsize absolute tail eventually exceeds the smaller-stepsize tail at all sufficiently large thresholds. Symmetry gives the identical ratio conclusion separately for the positive and negative tails, with each constant divided by two.

The moment threshold also changes strictly: every

\[
p\in[\alpha(\eta_2),\alpha(\eta_1))
\]

has a finite \(p\)-th absolute moment under \(\pi_{\eta_1}\) and an infinite one under \(\pi_{\eta_2}\). This includes divergence at the larger-stepsize critical exponent itself. No ordering, differentiability, or uniform positive lower bound in \(\eta\) for \(C_\eta\) is needed for any of these conclusions. No derivative of the stationary tail asymptotic, and no exchange of a stepsize derivative with \(t\to\infty\), has been taken.

The conclusion concerns this fixed batch-one family. It does not by itself establish a monotonicity theorem for changing batch sizes, unrelated nonlinear models, or a joint large-threshold and varying-stepsize limit.
