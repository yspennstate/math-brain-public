# Fourier entropy–influence for monotone functions in a fixed Hamming band

Date: 2026-10-02. Status: **complete proof of a restricted theorem; novelty
unconfirmed**. This does not prove FEI for all linear threshold functions or all
monotone functions. It uses the established symmetric-function FEI theorem as
an input. The Gaussian-to-discrete transfer route remains incomplete.

All logarithms below are base 2. On the uniform cube, write

\[
 H(f)=\sum_S\widehat f(S)^2\log\frac1{\widehat f(S)^2},\qquad
 I(u)=\sum_S |S|\widehat u(S)^2.
\]

The second definition applies to arbitrary real-valued functions. For Boolean
functions it is the usual total influence. Let \(r(x)=\#\{i:x_i=+1\}\).
The zero-dimensional case consists only of constants and is immediate; below
\(n\ge1\).

## The theorem

Suppose \(f:\{-1,+1\}^n\to\{-1,+1\}\) is coordinatewise monotone. Suppose
there are integers \(0\le a\le b\le n\) such that

* \(f(x)=-1\) whenever \(r(x)<a\);
* \(f(x)=+1\) whenever \(r(x)>b\).

There are \(k=b-a+1\) potentially nonsymmetric Hamming layers. Then

\[
 \boxed{H(f)\le\bigl(25+64(k+1)^2\bigr) I(f).}\tag{1}
\]

The constant is deliberately generous. Arbitrary assignments within the band
are allowed, subject only to monotonicity. There is no bias restriction.

For a single exceptional layer there is the sharper elementary bound

\[
 \boxed{H(f)\le 62 I(f).}\tag{2}
\]

The only previously established FEI input used in these statements is

\[
 H(g)\le 12.04 I(g)\quad\text{for every symmetric Boolean }g,
\tag{3}
\]

which is Theorem 1 of O'Donnell–Wright–Zhou, *The Fourier Entropy–Influence
Conjecture for certain classes of Boolean functions* (ICALP 2011).

## 1. An entropy comparison for nearby Boolean functions

For any Boolean \(f,g\), let \(\delta=\Pr(f\ne g)\). Then

\[
 H(f)\le 2H(g)+8\delta n+
 2(1+4\delta)h_2\!\left(\frac{4\delta}{1+4\delta}\right).
\tag{4}
\]

In particular, for \(n\ge1\),

\[
 \boxed{H(f)\le 2H(g)+32\delta n.}\tag{5}
\]

Here is a complete proof. Put \(d=f-g\), so \(\|d\|_2^2=4\delta\). Let
\(A_S=\widehat f(S)\), \(B_S=\widehat g(S)\), and
\(C_S=\widehat d(S)\). Thus \(A=B+C\), \(\sum B_S^2=1\), and
\(\sum C_S^2=4\delta\). Set \(M=1+4\delta\) and define probability laws

\[
 Q_S=A_S^2,\qquad P_S=\frac{B_S^2+C_S^2}{M}.
\]

The pointwise inequality \((B_S+C_S)^2\le2(B_S^2+C_S^2)\) says
\(Q_S\le2M P_S\). If probability laws satisfy \(Q\le K P\), \(K>1\),
then \(P=Q/K+(1-1/K)R\) for another probability law \(R\). Entropy
concavity and nonnegativity yield \(H(Q)\le K H(P)\). Applying this with
\(K=2M\), and then the entropy upper bound for a mixture, gives

\[
 \begin{aligned}
 H(f)&\le 2M H(P)\\
 &\le 2H(g)+8\delta H\!\left(\frac{C^2}{4\delta}\right)
       +2M h_2(4\delta/M)\\
 &\le 2H(g)+8\delta n+2M h_2(4\delta/M).
 \end{aligned}
\]

The case \(\delta=0\) is interpreted separately and is immediate. If
\(\delta>0\), the finite cube gives \(\delta\ge2^{-n}\). Also
\(0<\delta\le1\), hence \(M/4\le5/4\). The binary-entropy term satisfies

\[
 \begin{aligned}
 2M h_2(4\delta/M)
 &=2\log M+8\delta\log\frac{M}{4\delta}\\
 &\le8\delta\left(\log e+\log\frac1\delta+\log\frac54\right)\\
 &\le8\delta\left(n+\log e+\log\frac54\right).
 \end{aligned}
\]

Together with \(8\delta n\), this is less than \(32\delta n\), since
\(8(2+\log e+\log(5/4))<32\). This proves (5). This comparison estimate
is elementary; no novelty is claimed for the general entropy principle.

## 2. Random symmetric thresholds reproduce the layer averages

Set

\[
 p_r=2^{-n}\binom nr,\quad
 q_r=\Pr(f=+1\mid r(x)=r),\quad q_{-1}=0,\quad q_{n+1}=1.
\]

Monotonicity gives \(q_{r+1}\ge q_r\). For example, couple a uniformly
random \(r\)-set to a uniformly random \((r+1)\)-set by adding a uniformly
chosen missing coordinate; monotonicity applies pointwise.

For \(-1\le t\le n\), define the symmetric threshold

\[
 g_t(x)=\begin{cases}-1,&r(x)\le t,\\+1,&r(x)>t.\end{cases}
\]

This includes the constants \(g_{-1}=+1\) and \(g_n=-1\). Choose a random
\(T\) with

\[
 \Pr(T=t)=\mu_t=q_{t+1}-q_t.
\]

Then \(\mu\) is a probability law and

\[
 \Pr(g_T=+1\mid r)=q_r.
\tag{6}
\]

Since \(q_r=0\) for \(r<a\) and \(q_r=1\) for \(r>b\), its support is
contained in \(\{a-1,\ldots,b\}\). In particular, every \(d_t=f-g_t\)
with positive \(\mu_t\) is supported on the same \(k\) Hamming layers.

The number of boundary edges from layer \(r\) to layer \(r+1\) is

\[
 (n-r)\binom nr (q_{r+1}-q_r).
\]

To verify this, count edges with a positive upper endpoint and subtract those
with a positive lower endpoint. Monotonicity ensures that their difference
counts exactly the negative-to-positive edges. The identity
\((r+1)\binom n{r+1}=(n-r)\binom nr\) gives the formula. Thus, with
\(c_t=(n-t)p_t\) for \(0\le t<n\) and \(c_{-1}=c_n=0\),

\[
 I(f)=2\sum_{t=-1}^n c_t\mu_t
      =\mathbb E_T I(g_T).
\tag{7}
\]

The quadratic definition of influence and \((u-v)^2\le2u^2+2v^2\) give

\[
 \mathbb E_T I(d_T)\le
 2I(f)+2\mathbb E_T I(g_T)=4I(f).
\tag{8}
\]

## 3. The mean disagreement costs at most a quadratic band-width factor

Write \(\delta_t=\Pr(f\ne g_t)\). We prove

\[
 \boxed{n\mathbb E_T\delta_T\le2(k+1)^2 I(f).}\tag{9}
\]

### Large dimension: a Dirichlet bound on a short band

Let \(u\) be any real function supported on \(k\) consecutive Hamming
layers. Let \(A\) be the cube adjacency operator, and write
\(v_r^2=2^{-n}\sum_{r(x)=r}u(x)^2\). Cauchy–Schwarz on the edges between
two consecutive layers gives

\[
 \langle u,Au\rangle\le
 2\sum_{r=a}^{b-1}\sqrt{(n-r)(r+1)}\,v_rv_{r+1}
 \le(n+1)\sum_{r=a}^{b-1}v_rv_{r+1}.
\]

The path adjacency matrix on \(k\) vertices has top eigenvalue
\(2\cos(\pi/(k+1))\). Hence

\[
 \langle u,Au\rangle\le
 (n+1)\cos\!\left(\frac\pi{k+1}\right)\|u\|_2^2.
\]

Since \(I(u)=\tfrac12(n\|u\|_2^2-\langle u,Au\rangle)\) and
\(1-\cos(\pi/(k+1))\ge2/(k+1)^2\), for \(n\ge(k+1)^2\) this implies

\[
 I(u)\ge\frac{n}{2(k+1)^2}\|u\|_2^2.
\tag{10}
\]

Apply (10) to \(d_T\), use \(\|d_T\|_2^2=4\delta_T\), average, and use
(8). The result is (9).

### Small dimension: average Poincaré instead of a false pointwise claim

For any real function, \(I(u)\ge\operatorname{Var}(u)\). Let \(T,U\) be
independent with law \(\mu\), and put
\(D(T,U)=\Pr(g_T\ne g_U)\). The thresholds are nested, so

\[
 |\mathbb E g_T-\mathbb E g_U|=2D(T,U).
\]

Using (6), at a layer with positive fraction \(q_r\), both average
\(f\)-versus-\(g_T\) disagreement and average \(g_T\)-versus-\(g_U\)
disagreement equal \(2q_r(1-q_r)\). Consequently

\[
 \mathbb E_T\delta_T=\mathbb E_{T,U}D(T,U),\qquad
 \mathbb E_T\mathbb E g_T=\mathbb E f.
\]

It follows that

\[
 \begin{aligned}
 \mathbb E_T\operatorname{Var}(d_T)
 &=4\mathbb E_T\delta_T-
   \operatorname{Var}_T(\mathbb E g_T)\\
 &=4\mathbb E_T\delta_T-2\mathbb E_{T,U}D(T,U)^2\\
 &\ge2\mathbb E_T\delta_T.
 \end{aligned}
\tag{11}
\]

Here we used \(0\le D\le1\). Combining (11), Poincaré, and (8) gives
\(\mathbb E\delta_T\le2I(f)\). If \(n<(k+1)^2\), this again implies
(9). Thus (9) holds in every dimension. It is essential that this argument
averages over \(T\); a uniform pointwise disagreement estimate was not used.

## 4. Finish the band theorem

Apply (5) to each \((f,g_t)\), average over \(T\), then use (3), (7), and
(9):

\[
 \begin{aligned}
 H(f)&\le2\mathbb E H(g_T)+32n\mathbb E\delta_T\\
 &\le24.08 I(f)+64(k+1)^2 I(f)\\
 &\le\bigl(25+64(k+1)^2\bigr)I(f).
 \end{aligned}
\]

This proves (1), including constant functions.

## 5. Sharper single-layer bound

Suppose only layer \(r\) is exceptional, with positive fraction \(q\), and
let \(p=2^{-n}\binom nr\). Its boundary-edge count gives exactly

\[
 I(f)=2p\bigl(rq+(n-r)(1-q)\bigr).
\]

Choose \(g\) by assigning the exceptional layer its majority value. Then
\(\delta=p\min(q,1-q)\le1/2\), and

\[
 \delta n\le\tfrac12 I(f),\qquad I(g)\le2I(f).
\tag{12}
\]

For \(\delta\le1/2\), \(M/4\le3/4<1\), so the argument proving (5)
improves to

\[
 H(f)\le2H(g)+(16+8\log e)\delta n.
\]

Now (3) and (12) give

\[
 H(f)\le\bigl(48.16+8+4\log e\bigr)I(f)<62 I(f),
\]

as claimed. The endpoint layers cause no exception: they contain a single
point and their fraction \(q\) is 0 or 1.

## 6. Weighted thresholds with arbitrary bias

Let \(w_i>0\) and \(f(x)=\operatorname{sgn}(\sum_i w_i x_i-\theta)\), with
either usual convention at equality. Suppose

\[
 A=\sum_{i=1}^n|w_i-1|.
\]

Since
\(\left|\sum_iw_ix_i-\sum_ix_i\right|\le A\), only the unweighted sum
levels in \([\theta-A,\theta+A]\) can be ambiguous. Consecutive levels
have separation 2. There are at most \(\lfloor A\rfloor+1\) such levels.
Outside their consecutive Hamming band the function is respectively −1 and
+1. Thus, if \(A\) is bounded independently of \(n\), (1) proves FEI with

\[
 H(f)\le\left(25+64(\lfloor A\rfloor+2)^2\right)I(f).
\tag{13}
\]

If the interval contains no unweighted sum level, \(f\) is a symmetric
threshold and (3) applies directly. If \(A<1\), there is at most one
ambiguous layer and the bound is 62. This accommodates arbitrary bias
\(\theta\), including thresholds far into the binomial tails. No regularity
or Gaussian approximation is used. The result also tolerates arbitrary
monotone decisions inside the ambiguous band, a larger class than LTFs.

Scaling: replace 1 by any positive common weight \(c\), and take
\(A=\sum_i|w_i/c-1|\). Positivity of the weights is needed only for
monotonicity. For general weights, first delete coordinates with zero weight,
then make the remaining weights positive by changing signs of coordinates;
these operations preserve Fourier entropy and total influence. Apply the
displayed condition to the resulting positive weights.

## 7. Scope and primary-source audit

* Established input: O'Donnell–Wright–Zhou (2011), Theorem 1 gives the
  symmetric FEI constant 12.04; Theorem 2 covers a fixed number of symmetric
  coordinate parts. Primary manuscript:
  <https://www.cs.cmu.edu/~odonnell/papers/fei.pdf>.
* Their fixed-part symmetry condition need not hold for the functions in
  this note. The exceptional layers can use arbitrary coordinate labels.
  This observation distinguishes the hypotheses but is not a novelty proof.
* González–MacManus–Pereyra (2026), v2:
  <https://arxiv.org/html/2606.00246v2> and
  <https://arxiv.org/abs/2606.00246>. Its introduction and class statements
  do not assert the band theorem proved here. A search of primary titles
  and phrases about almost symmetric functions, perturbations, and Hamming
  layers found no explicit matching theorem. That search is not exhaustive.
* Chakraborty–Kulkarni–Lokam–Saurabh's revised *Upper Bounds on Fourier
  Entropy* removes the earlier incorrect proof for all LTFs:
  <https://eccc.weizmann.ac.il/report/2013/052/revision/2/download>.
  Its valid general LTF bound is \(H(f)=O(\sqrt n)\), which alone does not
  give FEI for arbitrary bias. This note is a restricted extension, not a
  correction resolving that whole problem.

The fixed-band result is elementary enough that it may be known or follow
from a previously documented stability principle. Its independent proof
is complete; research novelty has not been established. For weights with
\(\sum_i|w_i/c-1|\) growing with dimension, (13) gives a growing constant.
This is the explicit gap to the full deterministic-LTF problem.

## 8. Relation to the failed Gaussian transfer route

For an unbiased Gaussian halfspace, its Hermite entropy can be bounded by
\(C\|w\|_1/\|w\|_2\), using the \(k^{-3/2}\) degree tail and multinomial
allocation conditional on total degree. This auxiliary calculation is
recorded in the earlier research notes. Low-degree invariance does not by
itself transfer whole Fourier entropy: the unresolved high-degree tail
has an ambient dimension factor. The band theorem bypasses that obstacle
only because a physical perturbation costs \(O(n\delta)\) entropy and the
short-band Dirichlet bound controls \(n\mathbb E\delta\).

No new sufficient condition for all LTFs is claimed. The max-influence and
separator counterexamples in the previously archived notes remain valid;
this proof never uses either selection rule.
