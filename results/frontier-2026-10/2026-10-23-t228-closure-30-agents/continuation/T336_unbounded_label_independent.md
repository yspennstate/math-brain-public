# T336: an all-label KL obstruction for finite polynomial/ReLU mean circuits

**Verdict.** The proposed obstruction is true when the predicted Gaussian mean itself is computed by a finite circuit using affine operations, additions, products, and ReLU. It remains true even if the predicted variance is an arbitrary positive finite function. In fact, the result holds for any mean selecting pointwise from a finite collection of bivariate polynomials, without any assumption on how the pieces are selected.

An essential qualification is the Gaussian parameterization: polynomial natural parameters can represent the exact posterior through a decoder that implicitly performs division. Thus this is not a theorem about arbitrary Gaussian-output heads merely because their raw network outputs are polynomial.

Agent 27, 23 October 2026. Independently derived from the stated rank-one model; subsequent coordination with Agent 30 clarified predictive-versus-latent scope. No subagents used. No frozen T228 package files edited.

## 1. Exact model and target distribution

Fix context noise variance \(s>0\). Let
\[
G\sim N(0,1),\qquad f(t)=Gt,\qquad
Y=xG+\varepsilon,\quad \varepsilon\sim N(0,s),
\]
where \(G\) and \(\varepsilon\) are independent and \(x\in[1,2]\). This is a Gaussian process with kernel \(k(t,u)=tu\).

The query input is one. To include both standard target conventions, let the query target be
\[
T=G+\varepsilon_\star,\qquad \varepsilon_\star\sim N(0,\tau),
\]
independent of everything else, where \(\tau\ge0\) is fixed. The noisy predictive target uses \(\tau=s\); the latent posterior uses \(\tau=0\).

Completing the square in
\[
g^2+\frac{(y-xg)^2}{s}
=\frac{x^2+s}{s}
 \left(g-\frac{xy}{x^2+s}\right)^2+\frac{y^2}{x^2+s}
\]
shows that, for every real label \(y\),
\[
P_{x,y}:=\mathcal L(T\mid x,Y=y)
=N\!\left(a(x)y,v_\tau(x)\right),
\quad
a(x)=\frac{x}{x^2+s},
\quad
v_\tau(x)=\tau+\frac{s}{x^2+s}.
\]
In particular,
\[
0<v_{\min}:=\tau+\frac{s}{s+4}
\le v_\tau(x)
\le \tau+\frac{s}{s+1}=:v_{\max}<\infty.
\]
The exact model gives positive label density at every real \(y\), although the statement below concerns pointwise uniform KL, not an expectation over labels.

Let a predictor output
\[
Q_{x,y}=N(m(x,y),w(x,y)),
\qquad 0<w(x,y)<\infty.
\]
Forward KL here means \(D_{\rm KL}(P_{x,y}\Vert Q_{x,y})\), with the exact posterior/predictive law in the first argument.

## 2. Optimizing the predicted variance cannot hide an unbounded mean error

Write \(e=m(x,y)-a(x)y\), \(v=v_\tau(x)>0\), and \(w=w(x,y)>0\). Direct integration of the two Gaussian log densities gives
\[
D_{\rm KL}(N(a(x)y,v)\Vert N(m,w))
=\frac12\left[
\log\frac{w}{v}+\frac{v+e^2}{w}-1
\right].
\tag{1}
\]
For fixed \(v,e\), put \(A=v+e^2\) and \(r=w/A\). Then
\[
\log\frac{w}{v}+\frac{A}{w}-1
=\log\frac{A}{v}+\log r+\frac1r-1.
\]
The last three terms satisfy \(\log r+1/r-1\ge0\) for every \(r>0\): their derivative is \((r-1)/r^2\), so the unique minimum is zero at \(r=1\). Consequently,
\[
\boxed{
\inf_{w>0}D_{\rm KL}(N(a(x)y,v)\Vert N(m,w))
=\frac12\log\left(1+\frac{e^2}{v}\right)
}
\tag{2}
\]
and the minimizing variance is \(w=v+e^2\).

Thus a finite uniform KL bound \(D_{\rm KL}(P_{x,y}\Vert Q_{x,y})\le K\) would force
\[
|m(x,y)-a(x)y|
\le \sqrt{v_\tau(x)(e^{2K}-1)}
\le \sqrt{v_{\max}(e^{2K}-1)}
\tag{3}
\]
for all \(x\in[1,2]\) and \(y\in\mathbb R\). This necessity does not assume that \(w\) is polynomial, bounded, label-independent, or computed by the same architecture.

## 3. Finite arithmetic/ReLU circuits have a finite polynomial library

Consider a fixed finite acyclic computation with inputs \(x,y\), real constants (which may depend on fixed \(s,\tau\)), and operations:

- affine combinations;
- additions and products of previously computed scalar coordinates;
- \(z\mapsto\max\{z,0\}\).

Fixed-dimensional vector/matrix versions of these operations are just finitely many scalar operations. Fixed query coordinates, token positions, and sequence-length normalization by a fixed nonzero constant may be absorbed into constants. Input-dependent division and nonpolynomial preprocessing are not allowed.

Every coordinate computed by such a circuit selects, at each input, from a finite set of polynomials in \(x,y\). This follows by induction over the computation:

1. Every input and constant has a one-element polynomial library.
2. An affine combination or product of coordinates has a library consisting of the corresponding combinations of all choices from the finitely many input libraries.
3. ReLU applied to a coordinate with library \(\mathcal P\) has library contained in \(\mathcal P\cup\{0\}\).

The libraries can be large, and some formal choices may never occur, but they remain finite. Therefore the predicted mean has a finite library
\[
\mathcal P=\{P_1,\ldots,P_N\}\subset\mathbb R[x,y],
\qquad
m(x,y)\in\{P_1(x,y),\ldots,P_N(x,y)\}
\tag{4}
\]
at every input.

This covers finite unnormalized ReLU-attention arithmetic, and normalization by a fixed context length, when all input features and the output mean are computed using the listed operations. It does not cover score-dependent row normalization.

## 4. Main obstruction, with a uniform divergence rate

**Theorem.** Fix \(s>0\) and \(\tau\ge0\). Suppose the mean satisfies (4) for finitely many bivariate polynomials, and \(w(x,y)\) is any positive finite function. There exist a closed interval \(J\subset(1,2)\) with nonempty interior and constants \(c>0\), \(Y\ge1\), depending on the finite polynomial library, such that for every \(x\in J\) and every \(y\ge Y\),
\[
|m(x,y)-a(x)y|\ge cy.
\tag{5}
\]
Hence
\[
D_{\rm KL}(P_{x,y}\Vert Q_{x,y})
\ge\frac12\log\left(1+\frac{c^2y^2}{v_{\max}}\right)
\quad (x\in J,\ y\ge Y),
\tag{6}
\]
and in particular
\[
\sup_{x\in[1,2],\,y\in\mathbb R}
D_{\rm KL}(P_{x,y}\Vert Q_{x,y})=\infty.
\tag{7}
\]

**Proof.**
Write
\[
P_i(x,y)=\sum_{j\ge0}p_{ij}(x)y^j
\]
with all \(p_{ij}\in\mathbb R[x]\) and only finitely many nonzero terms. Define
\[
Q_i(x,y)=(x^2+s)P_i(x,y)-xy
=\sum_{j\ge0}q_{ij}(x)y^j.
\]
Its coefficient of \(y\) is
\[
q_{i1}(x)=(x^2+s)p_{i1}(x)-x.
\tag{8}
\]
This is not the zero polynomial. If \(p_{i1}=0\), it equals \(-x\). If \(p_{i1}\ne0\), then \((x^2+s)p_{i1}\) has degree \(\deg p_{i1}+2\ge2\), so it cannot equal the degree-one polynomial \(x\).

Let \(d_i\ge1\) be the degree of \(Q_i\) in \(y\), and let \(q_{i,d_i}\) be its nonzero leading coefficient polynomial in \(x\). Each of these finitely many leading coefficients has only finitely many real roots. Choose a closed interval \(J\subset(1,2)\) with nonempty interior avoiding every such root. Define
\[
b_i:=\min_{x\in J}|q_{i,d_i}(x)|>0,
\qquad
B_i:=\sum_{j<d_i}\max_{x\in J}|q_{ij}(x)|<\infty.
\]
Choose
\[
Y\ge \max\left(1,\max_i\frac{2B_i}{b_i}\right).
\]
For all \(x\in J\), \(y\ge Y\), and every \(i\),
\[
\begin{aligned}
|Q_i(x,y)|
&\ge b_i y^{d_i}-B_i y^{d_i-1}\\
&\ge \frac{b_i}{2}y^{d_i}
\ge \frac{b_i}{2}y.
\end{aligned}
\]
Since \(x^2+s\le4+s\),
\[
\left|P_i(x,y)-\frac{xy}{x^2+s}\right|
=\frac{|Q_i(x,y)|}{x^2+s}
\ge\frac{b_i}{2(s+4)}y.
\]
Set \(c=\min_i b_i/[2(s+4)]>0\). The estimate holds for every library member simultaneously, so it holds for whichever member the predictor selects at each input. This proves (5). Equation (2), together with \(v_\tau(x)\le v_{\max}\), proves (6) and (7). \(\square\)

This proof does not need eventual gate stabilization or semialgebraic geometry. In particular, pathological switching between the finitely many branches cannot rescue the mean. It yields divergence at least \(\log y+O(1)\) uniformly over a nontrivial input interval, even after optimizing the variance separately at every point.

The interval and constants depend on the particular predictor. No single interval uniform over all possible networks is claimed.

## 5. The proposed stable-branch argument is also valid

For completeness, the specific gate-stabilization mechanism in the question can be proved directly.

**Stable-strip lemma.** For a finite circuit as in Section 3, there exist a nonempty open interval \(I\subset(1,2)\), a finite \(Y\), and a single polynomial \(P(x,y)\) such that \(m(x,y)=P(x,y)\) for every \(x\in I\), \(y>Y\). All ReLU gates have fixed sign behavior on that strip, allowing an identically zero preactivation.

**Proof.** Process the gates in topological order while maintaining a nonempty input interval and a sufficiently high label threshold on which all earlier gates have fixed branches. Before a ReLU, its preactivation is then one polynomial \(H(x,y)\).

If \(H\) is identically zero, fix the zero branch. Otherwise, write \(H=\sum_{j=0}^d h_j(x)y^j\) with \(h_d\) a nonzero polynomial. Choose a smaller closed interval with nonempty interior, compactly contained in the current interval, that avoids the finitely many roots of \(h_d\). On it, the leading coefficient has a fixed sign and its absolute value has a positive minimum, while all lower coefficients are uniformly bounded. For sufficiently large positive \(y\), the leading term controls the sign of \(H\) uniformly on that interval. Restrict to the interval's interior and increase the threshold if necessary. The ReLU now has a fixed branch. Affine and product gates require no branch decision.

There are only finitely many ReLUs, so finitely many such interval restrictions and threshold increases leave a nonempty interval and a finite threshold. The resulting mean is one polynomial there. \(\square\)

If finite uniform KL were possible, (3) would hold on this strip. For each fixed \(x\in I\), the polynomial
\[
y\longmapsto P(x,y)-a(x)y
\]
would remain bounded as \(y\to+\infty\), so it would be constant in \(y\). Thus all coefficients of powers \(y^j\), \(j\ge2\), vanish on \(I\), and the coefficient \(p_1(x)\) of \(y\) must satisfy
\[
p_1(x)=\frac{x}{x^2+s}\qquad(x\in I).
\]
The polynomial \((x^2+s)p_1(x)-x\) would vanish on an interval and hence identically, contradicting the degree argument in (8). This proves the requested version of the contradiction.

## 6. Necessary limits on the conclusion

### 6.1 Polynomial natural parameters are an escape route if decoding may divide

The theorem requires the predicted mean itself to satisfy (4). It is false that every Gaussian family with polynomial raw parameters is obstructed.

For the latent target \(\tau=0\), use precision and information parameter
\[
\lambda(x,y)=\frac{x^2+s}{s},
\qquad
h(x,y)=\frac{xy}{s}.
\]
These are polynomial functions of the inputs, with constants allowed to depend on fixed \(s\), and \(\lambda>0\). The Gaussian represented in natural form by
\[
q(g)\ \propto\ \exp\left(hg-\frac{\lambda g^2}{2}\right)
\]
has mean \(h/\lambda=xy/(x^2+s)\) and variance \(1/\lambda=s/(x^2+s)\). It is exactly the posterior.

Thus a Gaussian head that interprets polynomial raw outputs as natural parameters has implicitly supplied the missing input-dependent division. Similarly, a decoder may parameterize a Gaussian by unnormalized quantities \(A>0,H,B>0\) and interpret them as mean \(H/A\), variance \(B/A\). Taking
\[
A=x^2+s,\qquad H=xy,\qquad B=\tau(x^2+s)+s
\]
represents the exact noisy or latent target using polynomial raw outputs. Such a decoder lies outside the no-division mean-circuit assumption.

In contrast, allowing only the variance head to use an arbitrary positive transformation does not defeat the theorem if the final mean still has a finite polynomial library.

### 6.2 Softmax, layer normalization, and rational attention are outside this result

Softmax contains exponentials and input-dependent normalization. Layer normalization includes input-dependent division and square roots. Row-normalized positive ReLU attention includes input-dependent division. General nonpolynomial feature maps can also invalidate (4). No conclusion about any of these architectures follows from the finite-polynomial proof.

Adding an operation that computes division by the positive denominator \(x^2+s\) immediately permits the exact mean. The noisy or latent variance is then also obtained by elementary arithmetic and division. This exhibits why the excluded operation is substantive, rather than a cosmetic modeling choice.

### 6.3 The obstruction is specifically uniform over unbounded labels

It does not contradict compact-label approximation. For example, with \(D=s+4\),
\[
\frac1{x^2+s}
=\frac1D\sum_{j=0}^{\infty}
\left(\frac{4-x^2}{D}\right)^j
\quad(x\in[1,2]),
\]
and the ratio lies in \([0,3/(s+4)]\subset[0,1)\). Finite truncations are polynomials that converge uniformly in \(x\). Multiplying by \(xy\) gives uniform mean approximation on any fixed bounded-label rectangle, but not over all real labels.

It also does not rule out finite prior-averaged KL. Set \(W=\tau+1\) and use the constant prior-predictive output \(Q=N(0,W)\), which is available to the restricted architecture. Under the true conditional law of the context label,
\[
Y\mid x\sim N(0,x^2+s),\qquad
\mathbb E_Y[a(x)^2Y^2]=\frac{x^2}{x^2+s}=W-v_\tau(x).
\]
Taking expectations in (1) gives the exact identity
\[
\mathbb E_{Y\mid x}
D_{\rm KL}(P_{x,Y}\Vert N(0,W))
=\frac12\log\frac{W}{v_\tau(x)}
\le\frac12\log\frac{\tau+1}{\tau+s/(s+4)}<\infty.
\]
Thus worst-case all-label divergence and finite uniformly-in-input expected KL coexist in this example. The theorem does not by itself obstruct convergence in an average-risk objective.

## 7. Conclusion for the T336 obstruction

For a direct Gaussian mean produced by a fixed finite affine/product/ReLU arithmetic circuit, the all-label uniform forward-KL target fails already for one observation from the continuous rank-one GP \(k(t,u)=tu\), one query at one, and any fixed positive context noise variance. Allowing unrestricted positive predicted variance does not repair it.

The proof covers both the noisy predictive variance \(s+s/(x^2+s)\) and the latent posterior variance \(s/(x^2+s)\). It does not cover general softmax/layer-normalized transformers, input-dependent normalization, rational Gaussian decoders, or arbitrary Gaussian natural-parameter heads. A final architecture-specific impossibility statement must specify the final mean computation and the Gaussian head, rather than only the operations used to produce unspecified raw parameters.
