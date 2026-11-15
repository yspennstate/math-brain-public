# A symmetry bound and quadratic projection for fair binary LCS

Let X and Y be independent uniform words in {0,1}^n, and put
f(X,Y) = LCS(X,Y). Then, for every integer n >= 1,

\[
\boxed{\operatorname{Var}(f)\leq n/4.}
\]

The proof below is an application of the spectral gap on the cube after removing
odd degrees. It does not establish an asymptotic lower bound, and no claim of
novelty for this upper bound is made.

## 1. Walsh expansion

Write z = (x_1,...,x_n,y_1,...,y_n) in {0,1}^{2n}. For a subset
A of {1,...,2n}, define

\[
\chi_A(z)=(-1)^{\sum_{i\in A}z_i},\qquad
\widehat f(A)=2^{-2n}\sum_z f(z)\chi_A(z).
\]

Under uniform measure these characters are orthonormal. Indeed,
chi_A chi_B = chi_{A symmetric-difference B}; if A differs from B, one
independent fair bit appears to the first power, and its sign has mean zero.
There are 2^{2n} characters, equal to the dimension of the space of functions
on the cube. Consequently they form an orthonormal basis,

\[
f=\sum_A\widehat f(A)\chi_A,\qquad
\operatorname{Var}(f)=\sum_{A\ne\varnothing}\widehat f(A)^2.
\tag{1}
\]

Define the degree masses

\[
W_k=\sum_{|A|=k}\widehat f(A)^2.
\]

## 2. Complementation removes odd degrees

Complement every letter in both words. Every pair of equal letters remains
equal, so the possible common-subsequence index pairs are unchanged. Therefore
f(1-z)=f(z). Changing variable z to 1-z in the defining sum gives

\[
\widehat f(A)=(-1)^{|A|}\widehat f(A).
\]

If |A| is odd, this implies widehat f(A)=0. Thus

\[
\operatorname{Var}(f)=W_2+W_4+\cdots+W_{2n}.
\tag{2}
\]

In particular, every individual-letter covariance is zero. This cancellation
does not remove quadratic covariances.

## 3. One-bit changes and the upper bound

Let z^{(i)} denote z with bit i flipped, and define

\[
D_i f(z)=\frac{f(z)-f(z^{(i)})}{2}.
\]

Flipping bit i negates exactly the characters whose index set contains i.
Hence, by orthonormality,

\[
\mathbb E(D_i f)^2=\sum_{A\ni i}\widehat f(A)^2.
\]

Summing over i proves the exact identity

\[
\mathcal E(f):=\frac14\sum_{i=1}^{2n}
\mathbb E\bigl(f(z)-f(z^{(i)})\bigr)^2
=\sum_{k=1}^{2n}kW_k.
\tag{3}
\]

Changing one letter changes LCS by at most one: take an optimal common
subsequence before the change. If it uses the changed position, removing
that matched letter leaves a common subsequence one shorter after the change;
if it does not, the same subsequence is still valid. This gives
f(z^{(i)}) >= f(z)-1. Applying the same argument in the opposite direction
gives f(z) >= f(z^{(i)})-1. Thus the squared difference in (3) is at most one,
and

\[
\mathcal E(f)\leq (2n)/4=n/2.
\]

Equations (2) and (3) give 2 Var(f) <= mathcal E(f), proving
Var(f) <= n/4. For n=1, f is the indicator that the two bits agree, so its
variance is 1/4 and equality holds. For n=0 the variance is zero.

The exact remainder identity is also useful:

\[
\boxed{\operatorname{Var}(f)
=\frac{\mathcal E(f)}2-
\sum_{\substack{k\geq4\\ k\text{ even}}}\left(\frac k2-1\right)W_k.}
\tag{4}
\]

## 4. An explicit quadratic lower-bound target

Put s_i=(-1)^{X_i} and t_j=(-1)^{Y_j}, and define

\[
a_{ij}=\mathbb E[f s_i s_j]\quad(1\leq i<j\leq n),\qquad
b_{ij}=\mathbb E[f s_i t_j]\quad(1\leq i,j\leq n).
\]

Interchanging the two words preserves f and the joint distribution. Therefore
the coefficients supported on two positions in Y equal the corresponding
a_{ij}. Listing all degree-two subsets gives the exact identity

\[
\boxed{W_2=2\sum_{i<j}a_{ij}^2+\sum_{i,j}b_{ij}^2
\leq\operatorname{Var}(f).}
\tag{5}
\]

Thus a bound W_2 >= c n would suffice for the missing lower bound. Equation
(5) is a sufficient route, not an equivalence: higher degrees could carry
linear variance even if W_2 were sublinear.

There is a one-parameter version involving adjacent positions. For n >= 2 set

\[
S=\sum_{i=1}^{n-1}s_i s_{i+1}
 +\sum_{j=1}^{n-1}t_j t_{j+1}.
\]

Every summand is a different nonconstant Walsh character. Orthonormality gives
E S=0 and Var(S)=2(n-1), even though neighboring summands share a bit. Word
exchange gives

\[
\mathbb E[fS]=2\sum_{i=1}^{n-1}a_{i,i+1}.
\]

Cauchy–Schwarz, applied to (f-E f) and S, yields

\[
\boxed{\operatorname{Var}(f)\geq
\frac{2}{n-1}\left(\sum_{i=1}^{n-1}a_{i,i+1}\right)^2.}
\tag{6}
\]

This can be expressed as a derivative of an expected LCS. For -1 < theta < 1,
let each word independently be a stationary symmetric binary Markov chain with
P(next letter = current letter) = (1+theta)/2, and uniform initial letter.
Relative to uniform iid words, its joint density for the two words is

\[
p_\theta(z)=
\prod_{i=1}^{n-1}(1+\theta s_i s_{i+1})
\prod_{j=1}^{n-1}(1+\theta t_j t_{j+1}).
\]

To check the density, the probability of one word is its initial factor 1/2
times its n-1 transition factors (1+theta s_i s_{i+1})/2; dividing by 2^{-n}
leaves the stated product. Define F_n(theta)=E[f p_theta], the expected LCS
under these Markov words. This is a finite polynomial, so differentiation
term by term at zero is valid and gives

\[
F_n'(0)=\mathbb E[fS]=2\sum_{i=1}^{n-1}a_{i,i+1}.
\]

Consequently (6) is precisely

\[
\boxed{\operatorname{Var}(L_n)\geq
\frac{F_n'(0)^2}{2(n-1)}.}
\tag{7}
\]

A bound |F_n'(0)| >= delta n for every sufficiently large n, with fixed
delta>0, would prove the conjectured lower bound. No such derivative estimate
is proved here. In particular, no differentiation of an infinite-n limit is
used or justified.

## 5. Conditional-word projection used in the data audit

Let mu=E f, g(X)=E[f|X]-mu and h(Y)=E[f|Y]-mu. These functions have mean zero.
Independence gives E[gh]=0. Write r=f-mu-g-h. Conditioning on X gives
E[r|X]=0: the conditional mean of f-mu is g, and that of h is E h=0.
Likewise E[r|Y]=0. It follows that E[rg]=E[rh]=0. Expanding the square yields

\[
\operatorname{Var}(f)=\mathbb E g^2+\mathbb E h^2+\mathbb E r^2
\geq 2\operatorname{Var}(\mathbb E[f\mid X]),
\tag{8}
\]

where the factor two uses exchangeability of the words. The Walsh expansion
of E[f|X] contains exactly the coefficients supported entirely in X. Thus
2 sum_{i<j} a_{ij}^2 is at most the right-hand side of (8).

For exact arithmetic let m=2^n, M=m^2, H_k be the number of ordered pairs
with LCS k, and R_x=sum_y f(x,y). Let c_A=sum_z f(z) chi_A(z)=M widehat f(A).
Then the quantities in the data files are obtained from

\[
\mu=\frac{\sum_k kH_k}{M},\qquad
\operatorname{Var}(f)=\frac{\sum_k k^2H_k}{M}-\mu^2,
\qquad W_k=\frac{\sum_{|A|=k}c_A^2}{M^2},
\]

and

\[
2\operatorname{Var}(\mathbb E[f\mid X])
=2\left(\frac{\sum_x R_x^2}{m^3}-\mu^2\right).
\]

If B is the sum of squared score differences over undirected one-bit cube
edges, every such edge contributes twice to the directed sum in (3). Hence
mathcal E(f)=B/(2M). These formulas account for all normalizations used in
the exact audit.
