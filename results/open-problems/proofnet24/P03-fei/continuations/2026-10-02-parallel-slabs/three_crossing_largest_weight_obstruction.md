# Three crossings obstruct a universal largest-weight entropy split

Date: 2026-10-02. This is a local-method obstruction, not a counterexample
to FEI for stripe functions or for general Boolean functions.

There are Boolean functions of one weighted linear form with exactly three
threshold crossings for which
\[
 \frac{H(f)-\tfrac12[H(f^+)+H(f^-)]}{I_z(f)}\longrightarrow\infty,
\]
even though \(z\) has the unique largest input weight. Thus the all-LTF
largest-weight proof cannot simply be extended to arbitrary three-crossing
functions. The unrestricted two-crossing parallel-slab theorem is consistent
with this obstruction.

## Construction

Let \(N=2d+1\ge3\), \(x\in\{-1,1\}^N\), and
\[
 g(x)=\operatorname{sign}\Bigl(\sum_{j=1}^Nx_j\Bigr),\qquad
 D(x)=\mathbf1\{x_1=\cdots=x_N=-1\},\qquad \alpha=2^{-N}.
\]
Define the two restrictions
\(f^-=g\), \(f^+=g+2D\). The latter flips the single all-minus value
from \(-1\) to \(+1\), so both restrictions are Boolean. Then
\[
 f=A+zB,\qquad A=g+D,\quad B=D,
 \qquad I_z(f)=\mathbb ED=\alpha.
\tag{1}
\]

Set \(w=N+1\), \(s=wz+\sum_jx_j\), and define a three-crossing rule
\[
 F(s)=
 \begin{cases}
 -1,&s<-w,\\
 +1,&-w<s<2,\\
 -1,&2<s<w,\\
 +1,&s>w.
 \end{cases}
\tag{2}
\]
All attained scores are odd, while the three crossings \(-w,2,w\)
are even, so there are no ties. For \(z=-1\), the score range is
\([-2N-1,-1]\) and (2) gives majority. For \(z=+1\), the scores start
at 1, then 3, and continue through \(2N+1\): the value at 1 is flipped,
while the other values give majority. Thus \(f(x,z)=F(s)\), exactly.
The pivot weight \(w=N+1\) strictly exceeds every other weight, which is 1.

## A lower bound on majority's nonzero Fourier coefficients

Majority is odd, so its coefficients vanish at every even subset size.
For \(|S|=2\ell+1\), its coefficient is
\[
 \widehat g(S)=(-1)^\ell\frac{\binom{2d}{d}}{4^d}
                  \frac{\binom d\ell}{\binom{2d}{2\ell}}.
\tag{3}
\]
For a direct derivation choose \(i\in S\). Majority's discrete derivative
in coordinate \(i\) is the central-layer indicator on the other \(2d\)
bits. The generating polynomial for the degree-\(j\) character average on
that layer is \((1+t)^d(1-t)^d=(1-t^2)^d\). This gives the numerator
\((-1)^\ell\binom d\ell\), and dividing by the number
\(\binom{2d}{2\ell}\) of subsets gives (3).

The central coefficient obeys
\(\binom{2d}{d}/4^d\ge1/(2d+1)\). Vandermonde and log-concavity of
the binomial row give
\[
 \binom{2d}{2\ell}
 =\sum_j\binom d j\binom d{2\ell-j}
 \le(d+1)\binom d\ell^2.
\]
Each product is bounded by the centered product by log-concavity; terms
outside the row are zero. Since \(\binom d\ell\le2^d\), all odd-size
coefficients satisfy
\[
 |\widehat g(S)|\ge\frac{2^{-d}}{(2d+1)(d+1)}
 =\frac{2^{-(N-1)/2}}{N(N+1)/2}.
\tag{4}
\]
For \(N\ge15\), this is at least \(2\alpha\): the ratio to
\(\alpha\) is \(2^{d+1}/[(2d+1)(d+1)]\), already above 2 at \(d=7\)
and increasing thereafter.

## Entropy split grows relative to its influence

Write \(a_S=\widehat A(S)\), \(b_S=\widehat B(S)\),
\(P_S=a_S^2+b_S^2\), \(q_S=b_S^2/P_S\), and
\(r_S=(a_S+b_S)^2/(2P_S)\). The exact split identity is
\[
 \Delta_zH(f)=\sum_S P_S[1+h_2(q_S)-h_2(r_S)].
\tag{5}
\]
Here \(b_S=\alpha(-1)^{|S|}\) and \(a_S=\widehat g(S)+b_S\).

For every even-size subset, \(\widehat g(S)=0\), so \(a_S=b_S\),
\(P_S=2\alpha^2\), \(q_S=1/2\), \(r_S=1\). Each such set contributes
\(4\alpha^2\) to (5). Their number is \(2^{N-1}\), giving total
\(2\alpha\).

For every odd-size subset and \(N\ge15\), (4) gives
\(|a_S|\ge|\widehat g(S)|/2\). Since \(1-h_2(r_S)\ge0\),
its contribution is at least
\[
 P_Sh_2(q_S)\ge\alpha^2\log_2(P_S/\alpha^2)
 \ge\alpha^2\left[N-1-2\log_2\frac{N(N+1)}2\right].
\]
There are \(2^{N-1}\) odd-size subsets. Combining both parities gives
\[
 \boxed{\frac{\Delta_zH(f)}{\alpha}
 \ge\frac{N+3}{2}-\log_2\frac{N(N+1)}2
 \xrightarrow[N\to\infty]{}\infty.}
\tag{6}
\]

For completeness the general conditional-bit-entropy upper bound is
\(\mathcal C\le\alpha[\log_2(1/\alpha)+\log_2e]\), using KL
nonnegativity and \(\ln(1+t)\le t\). Together with
\(\Delta H\le2\mathcal C\), this gives
\[
 \Delta_zH(f)\le2\alpha(N+\log_2e).
\]
Thus the split increment is \(\Theta(N2^{-N})\), whereas the largest
weight's influence is \(2^{-N}\).

The whole function still contains a majority background with much larger
total influence. This construction obstructs this particular local
largest-weight induction criterion; it establishes no failure of FEI.
