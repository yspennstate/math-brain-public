# A necessary size bound for finite orbit approximations

Let H be a complex Hilbert space, with inner product linear in the first
argument. Let U be unitary and let g have an orthonormal bilateral orbit
`(U^n g)_{n in Z}`. Completeness of this orbit is not assumed.

## Proposition

Let h belong to H, write

\[
 A=\|h\|>0,\qquad b=\|Uh-h\|,
\]

and suppose that, for a finite set F of integers and complex coefficients,

\[
 \left\|h-\sum_{n\in F}c_nU^ng\right\|\le\varepsilon<A.
\]

Then b is positive and

\[
 \boxed{\quad |F|\ge {A^2-\varepsilon^2\over A b}.\quad} \tag{1}
\]

Zero coefficients may be deleted from F. In particular (1) holds with F
the actual support of a Laurent polynomial. The constant one in the
coefficient estimate used below is optimal among all unitary operators.

### Proof

Set `a_n = <h,U^n g>`. Bessel's inequality gives

\[
 \sum_{n\in\mathbb Z}|a_n|^2\le A^2. \tag{2}
\]

Unitarity gives

\[
 a_{n+1}-a_n=\langle U^{-1}h-h,U^ng\rangle.
\]

The norm of `U^{-1}h-h` is b. A second application of Bessel therefore
gives

\[
 \sum_{n\in\mathbb Z}|a_{n+1}-a_n|^2\le b^2. \tag{3}
\]

For any square-summable bilateral sequence a, put `d_n=a_{n+1}-a_n`.
The sequence tends to zero at both ends. Telescoping from each end to k
and adding the two resulting inequalities gives

\[
 2|a_k|^2
 \le\sum_{n\in\mathbb Z}
       \big||a_{n+1}|^2-|a_n|^2\big|.
\]

The series on the right converges, because

\[
 \begin{aligned}
 \sum_n\big||a_{n+1}|^2-|a_n|^2\big|
 &\le\sum_n|d_n|(|a_{n+1}|+|a_n|)\\
 &\le\|d\|_{\ell^2}
       \big\|(|a_{n+1}|+|a_n|)_n\big\|_{\ell^2}\\
 &\le2\|d\|_{\ell^2}\|a\|_{\ell^2}.
 \end{aligned}
\]

Thus (2) and (3) imply

\[
             |a_k|^2\le A b\qquad(k\in\mathbb Z). \tag{4}
\]

The orthogonal projection of h onto the span of the orbit elements indexed
by F is `sum_{n in F} a_n U^n g`. Its error is at most the error of the
specified approximation. The Pythagorean theorem gives

\[
 A^2-\varepsilon^2
 \le\sum_{n\in F}|a_n|^2
 \le |F|A b. \tag{5}
\]

The left side is positive. Consequently b is positive and division in
(5) proves (1).

### An independent Fourier check of (4)

For the sequence above, let q be its Fourier transform in
`L^2(R/Z)`. Parseval's identity gives

\[
 \int_0^1|q(t)|^2\,dt\le A^2,\qquad
 \int_0^1 4\sin^2(\pi t)|q(t)|^2\,dt\le b^2.
\]

For every lambda>0, weighted Cauchy--Schwarz applied to the kth Fourier
coefficient gives

\[
 |a_k|^2\le(\lambda A^2+b^2)
      \int_0^1{dt\over\lambda+4\sin^2(\pi t)}
   ={\lambda A^2+b^2\over\sqrt{\lambda(\lambda+4)}}. \tag{6}
\]

For the integral, use a period interval `(-1/2,1/2)` and substitute
`x=tan(pi t)`. The integral becomes

\[
 {1\over\pi}\int_{\mathbb R}
       {dx\over\lambda+(\lambda+4)x^2}
 ={1\over\sqrt{\lambda(\lambda+4)}}.
\]

If b>0, choose `lambda=b^2/A^2` in (6). Its right side is

\[
 {2 A b\over\sqrt{4+b^2/A^2}}\le A b,
\]

which independently proves (4). If b=0, (3) says that a is constant;
square summability forces a=0, so no approximation with error below A
exists.

### Optimality of the constant in (4)

Take the bilateral shift on `ell^2(Z)`, g equal to the vector at index
zero, and h with coordinates `a_n=r^{|n|}`, where `0<r<1`. Direct geometric
summation gives

\[
 \|a\|_{\ell^2}^2={1+r^2\over1-r^2},\qquad
 \|a_{n+1}-a_n\|_{\ell^2}^2
       ={2(1-r)\over1+r}.
\]

Indeed the first sum is `1+2 sum_{n>=1} r^{2n}`. For the second,
each half-line contributes `(1-r)^2 sum_{n>=0} r^{2n}`. Since `a_0=1`,

\[
 {|a_0|^2\over\|a\|_{\ell^2}\|a_{n+1}-a_n\|_{\ell^2}}
     ={1+r\over\sqrt{2(1+r^2)}}\longrightarrow1
 \quad(r\uparrow1).
\]

The second sum also follows from

\[
 \|a_{n+1}-a_n\|_2^2
  =2\|a\|_2^2-2\sum_na_{n+1}a_n,
 \qquad \sum_na_{n+1}a_n={2r\over1-r^2}.
\]

Thus no smaller universal constant can replace one in (4). This
optimality statement concerns (4); it does not assert optimality of (1)
for each prescribed approximation error.

## Application to perturbations of a twist

Let M be a compact metric probability space, let S and R be invertible
probability-preserving maps, and let h be a real Lipschitz function with
`h o S=h`. Suppose that its Lipschitz constant is L and

\[
           \sup_{x\in M}d(Rx,Sx)\le\delta.
\]

Pointwise,

\[
 |h(Rx)-h(x)|=|h(Rx)-h(Sx)|\le L\delta,
\]

so `||h o R-h||_2 <= L delta`. If g has an orthonormal bilateral
Koopman orbit for R and `||h-P(U_R)g||_2 <= epsilon < A=||h||_2`,
the proposition gives

\[
 \#\operatorname{supp}P\ge
              {A^2-\varepsilon^2\over A L\delta} \tag{7}
\]

when `L delta>0`. If the actual residual is zero there is no such
approximation. Only the forward maps enter this estimate.

For an explicit test on the standard volume three-torus, use the maximum
of the three circle distances and put

\[
 S(\theta,u,a)=(\theta+\phi(u),u,a),\qquad
 h(\theta,u,a)=\sin(2\pi u).
\]

This test is real, centered, smooth, and bounded by one. It is fixed by S.
Its norm is `A=1/sqrt(2)` and its Lipschitz constant is at most `2 pi`.
The norm follows both from `sin^2 t=(1-cos(2t))/2` and from the two
orthogonal Fourier coefficients of modulus `1/2`.

For error `epsilon=A/2=1/(2 sqrt(2))`, equation (7) becomes

\[
 \boxed{\quad \#\operatorname{supp}P\ge
                {3\over8\sqrt2\,\pi\delta}.\quad} \tag{8}
\]

The numerator in (7) is `1/2-1/8=3/8`, and its denominator is
`(1/sqrt(2)) 2 pi delta = sqrt(2) pi delta`.
Equivalently, normalize the target to `sqrt(2) sin(2 pi u)`: its norm
is one, its error is `1/2`, and its Lipschitz constant is `2 sqrt(2) pi`.
This gives `(1-1/4)/(2 sqrt(2) pi delta)`, the same expression.

If P has all exponents in `[-d,d]`, then

\[
       2d+1\ge {3\over8\sqrt2\,\pi\delta}.
\]

In any fixed smooth volume-preserving chart the same argument applies
to the corresponding physical observable, with its physical Lipschitz
constant. That constant need not be uniform over changing charts.

The finite-stage construction under audit allows its polynomial to
depend on the perturbation tolerance. Equations (7) and (8) give a
necessary growth condition, not an obstruction to that quantifier.
