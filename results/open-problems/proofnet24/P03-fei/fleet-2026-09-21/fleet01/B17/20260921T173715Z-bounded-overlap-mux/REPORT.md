# B17 FEI creative continuation: bounded-overlap MUX toll is O(r)

**Status:** **PARTIAL. Full Friedgut--Kalai Fourier entropy--influence (FEI) remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Primary route:** APPROACH 7, with an information-theoretic ingredient from APPROACH 14.  
**Fresh state:** continued from the one-overlap MUX theorem and the current FEI master/owner handoff.  
**Novelty:** no literature-priority claim is made.

## 1. Result

Let \(Y\) be a shared block of \(r\) Boolean variables, let \(U,V\) be disjoint residual blocks, and let
\[
a=a(Y,U),\qquad b=b(Y,V)
\]
be arbitrary \(\{-1,1\}\)-valued Boolean functions. Let \(z\) be fresh and define
\[
f=\operatorname{MUX}_z(a,b)=\frac{a+b}{2}+z\frac{a-b}{2}.
\]
Put
\[
q=\operatorname{Inf}_z(f)=\Pr[a\ne b].
\]
Then
\[
H(f)=\frac{H(a)+H(b)}2+\Omega
\]
and the new bound is
\[
\boxed{\Omega\le C_r q}
\]
with
\[
\boxed{
C_r=
\max\left\{
r+5+\log_2 e,\;
7+\frac r2+\frac12\log_2 e
\right\}
\le r+8.}
\tag{1.1}
\]

For \(r=2\),
\[
C_2=8.721347520444\ldots<8.722.
\]

Thus the preceding one-overlap theorem has a general fixed-overlap extension. In particular, if a recursive MUX decomposition has at most \(R\) shared variables between the two children at every node, then
\[
\boxed{H(F)\le (R+8)I(F).}
\tag{1.2}
\]
This is dimension-free for every fixed \(R\). It is not full FEI because a general read-twice or arbitrary Boolean function need not admit a bounded-overlap recursive MUX decomposition.

The dependence \(O(r)\) is qualitatively consistent with the previously recorded bent-plus-one-point-flip obstruction, for which the unrestricted shared-block toll/influence ratio grows with the overlap dimension.

## 2. Exact selector-information decomposition

Embed the Fourier vectors of \(a,b\) in the common cube on \(Y\cup U\cup V\), writing them as
\[
\alpha_S=\widehat a(S),\qquad \beta_S=\widehat b(S).
\]
For each base subset \(S\) not containing \(z\),
\[
\widehat f(S)=\frac{\alpha_S+\beta_S}{2},
\qquad
\widehat f(S\cup\{z\})=\frac{\alpha_S-\beta_S}{2}.
\]

Let
\[
p_S=\alpha_S^2,\qquad r_S=\beta_S^2,\qquad
m_S=\frac{p_S+r_S}{2}.
\]
If \(Z\in\{0,1\}\) records whether the spectral sample of \(f\) contains \(z\), then
\[
\Pr[S=s,Z=0]=\frac{(\alpha_s+\beta_s)^2}{4},\qquad
\Pr[S=s,Z=1]=\frac{(\alpha_s-\beta_s)^2}{4}.
\]
Hence the marginal law of the base set is \(m=(p+r)/2\), and
\[
\Pr[Z=1]=
\frac14\sum_S(\alpha_S-\beta_S)^2
=q.
\]
The entropy chain rule therefore gives the exact identity
\[
\boxed{
\Omega=
\operatorname{JS}(p,r)+H(Z\mid S),
}
\tag{2.1}
\]
where JS is Jensen--Shannon divergence in bits.

This splits the MUX toll into a magnitude-mixture term and a selector-location term.

## 3. Universal bound on the JS part

For nonnegative \(u,v\), define
\[
j(u^2,v^2)=
\phi\!\left(\frac{u^2+v^2}{2}\right)
-\frac{\phi(u^2)+\phi(v^2)}2,
\qquad
\phi(t)=-t\log_2 t.
\]
With
\[
s=u^2+v^2,\qquad t=\frac{u^2}{s},
\]
one has
\[
j(u^2,v^2)=\frac{s}{2}\left(1-h_2(t)\right).
\]
Using the elementary bound
\[
h_2(t)\ge4t(1-t)
\]
and setting \(x=2\sqrt{t(1-t)}\in[0,1]\),
\[
h_2(t)\ge x^2\ge2x-1.
\]
Thus
\[
j(u^2,v^2)
\le s(1-x)
=(u-v)^2.
\]
Applying this coordinatewise to \(u=|\alpha_S|\), \(v=|\beta_S|\),
\[
\operatorname{JS}(p,r)
\le\sum_S(|\alpha_S|-|\beta_S|)^2
\le\sum_S(\alpha_S-\beta_S)^2
=4q.
\tag{3.1}
\]

So only \(H(Z\mid S)\) needs additional structure.

## 4. Shared-core geometry

Let
\[
g(y)=\mathbb E_U a(y,U),\qquad
h(y)=\mathbb E_V b(y,V),
\qquad y\in\{-1,1\}^r.
\]
The spectra of \(a\) and \(b\) can overlap only on subsets of \(Y\). Their common Fourier cores are exactly \(\widehat g\) and \(\widehat h\).

Conditional independence of \(U,V\) given \(Y\) gives
\[
\mathbb E[ab]=\mathbb E_Y[g(Y)h(Y)],
\]
and hence
\[
2q=1-\mathbb E[g h].
\tag{4.1}
\]

Write
\[
R_a=1-\mathbb E g^2,\qquad
R_b=1-\mathbb E h^2.
\]
Outside the shared core, exactly one branch coefficient is nonzero. At every such base spectral atom, \(Z\) is fair. Consequently the off-core contribution to \(H(Z\mid S)\) is exactly
\[
T_{\rm res}=\frac{R_a+R_b}{2}.
\]
Pointwise,
\[
2-g^2-h^2\le2(1-gh),
\]
so by (4.1),
\[
R_a+R_b\le4q,\qquad
\boxed{T_{\rm res}\le2q.}
\tag{4.2}
\]

## 5. Large-selector regime

Let \(m=2^r\). If
\[
q\ge\frac1{2m},
\]
then simply
\[
H(Z\mid S)\le H(Z)=h_2(q)
\le q\log_2\frac{e}{q}
\le q\log_2(2em).
\]
Combining with (3.1),
\[
\boxed{
\Omega\le
\left(4+\log_2(2em)\right)q
=
\left(r+5+\log_2 e\right)q.
}
\tag{5.1}
\]

## 6. Small-selector regime

Assume now
\[
q<\frac1{2m}.
\tag{6.1}
\]
Define on the \(m\) shared physical fibres
\[
\delta(y)=1-g(y)h(y)\ge0.
\]
By (4.1),
\[
\mathbb E\delta=2q.
\]
Because the measure on the \(m\) fibres is uniform,
\[
\max_y\delta(y)\le m\mathbb E\delta=2mq<1.
\]
Therefore \(g(y)h(y)>0\) for every \(y\), so \(g(y)\) and \(h(y)\) have the same sign pointwise. For same-sign numbers \(u,v\in[-1,1]\),
\[
|u-v|\le1-uv,
\]
hence
\[
|g-h|\le\delta.
\tag{6.2}
\]

Let \(x_T=\widehat g(T)\), \(w_T=\widehat h(T)\). The total \(Z=1\) mass lying in the common spectral core is
\[
Q_{\rm core}
=\frac14\sum_{T\subseteq Y}(x_T-w_T)^2
=\frac14\mathbb E(g-h)^2.
\]
By (6.2),
\[
\mathbb E(g-h)^2
\le\mathbb E\delta^2
\le(\max\delta)\mathbb E\delta
\le4mq^2,
\]
so
\[
\boxed{Q_{\rm core}\le mq^2.}
\tag{6.3}
\]

For each core atom put
\[
M_T=\frac{x_T^2+w_T^2}{2},\qquad
A_T=\frac{(x_T-w_T)^2}{4}.
\]
The core conditional entropy equals
\[
T_{\rm core}
=\sum_T M_T h_2(A_T/M_T).
\]
By concavity of binary entropy,
\[
T_{\rm core}
\le M_{\rm core}\,
h_2(Q_{\rm core}/M_{\rm core}),
\qquad
M_{\rm core}=\sum_T M_T\le1.
\]
For fixed \(Q\), the function \(M\mapsto M h_2(Q/M)\) is increasing on \(Q\le M\le1\). Therefore
\[
T_{\rm core}\le h_2(Q_{\rm core}).
\]
Under (6.1), \(Q_{\rm core}\le mq^2<1/(4m)\le1/4\), so \(h_2\) is increasing and
\[
T_{\rm core}
\le h_2(mq^2)
\le mq^2\log_2\frac{e}{mq^2}.
\]
Put \(t=mq<1/2\). Dividing by \(q\),
\[
\frac{T_{\rm core}}q
\le t\log_2\frac{em}{t^2}.
\]
The right-hand side is increasing for \(0<t\le1/2\), because its natural-log derivative is
\[
\log\frac{m}{e t^2}>0.
\]
Hence
\[
\boxed{
T_{\rm core}\le
\frac q2\log_2(4em).
}
\tag{6.4}
\]

Combining (3.1), (4.2), and (6.4),
\[
\boxed{
\Omega
\le
\left(
6+\frac12\log_2(4em)
\right)q
=
\left(
7+\frac r2+\frac12\log_2 e
\right)q.
}
\tag{6.5}
\]

Equations (5.1) and (6.5) prove (1.1).

## 7. Recursive bounded-overlap MUX class

Suppose a Boolean function is built recursively from literals/constants by fresh-selector MUX gates, and at every internal gate the two child variable sets overlap in at most \(R\) coordinates.

If both children satisfy \(H\le C I\), then from the exact influence identity
\[
I(f)=\frac{I(a)+I(b)}2+q
\]
and (1.1),
\[
H(f)
\le
\frac{C(I(a)+I(b))}{2}+C_Rq
\le C I(f)
\]
whenever \(C\ge C_R\). Since \(C_R\le R+8\), induction gives (1.2).

This is a genuine enlargement of the one-overlap class and proves the previously proposed qualitative target \(C_r=O(r)\) for fixed overlap size.

## 8. Stress tests for r=2

A deterministic finite checker enumerated every pair
\[
(g,h)\in\{-1,0,1\}^4\times\{-1,0,1\}^4,
\]
i.e. all \(3^8=6561\) four-fibre conditional-mean pairs obtainable from branches with one unbiased residual bit per fibre. It verified the rigorous bound \(C_2\) on every pair. The largest observed toll ratio was
\[
\frac{\Omega}{q}
=
5.921783780331385,
\]
at, up to symmetries,
\[
g=(-1,-1,-1,0),\qquad h=(-1,-1,-1,1),
\]
with
\[
q=\frac18,\qquad
\Omega=0.7402229725414231.
\]

Separately, a continuous differential-evolution search over the full box
\[
(g,h)\in[-1,1]^4\times[-1,1]^4
\]
found
\[
\frac{\Omega}{q}\approx5.927489895933067.
\]
A representative optimizer was
\[
g=(1,-1,1,1),\qquad
h=(1,-1,1,-0.071243\ldots).
\]
This numerical search is exploratory, not a proof of a sharp constant. It suggests that the true two-overlap toll constant may still be \(6\), but no such claim is made here.

## 9. What this changes and what remains

The previous one-overlap proof relied on a two-dimensional Fourier diamond and did not extend visibly to \(r=2\). The present argument bypasses the \(2^r\)-dimensional coefficient geometry by separating the entropy toll into:

1. a JS term paid universally by \(4q\);
2. off-core selector entropy paid by \(2q\);
3. a core selector entropy which becomes rare when \(q\ll2^{-r}\), because small disagreement forces all shared physical fibres to have matched signs.

This yields a clean \(O(r)\) toll for every fixed overlap dimension.

The remaining universal gap is structural, not local: a general Boolean function/read-twice representation can have growing overlap. A next B17 step should therefore be one of:

- prove the conjectured sharper \(C_2=6\) from the four-point physical box, then identify whether \(C_r\) can remain bounded for special overlap geometries;
- construct an explicit Boolean family showing a lower bound \(\Omega/q\ge c r\), which would prove the linear dependence is unavoidable for unrestricted shared blocks;
- find a read-twice decomposition in which the sum of overlap tolls is charged to influence so that the local \(O(r)\) factor is globally summable.

Until such a universal charging/decomposition theorem exists, full FEI remains OPEN.
