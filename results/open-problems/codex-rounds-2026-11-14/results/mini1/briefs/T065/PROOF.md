# Two-site polynomial conserved quantities for a quartic chain

Let indices belong to Z/NZ, with N >= 5. Put

\[
 V(r)=\frac{r^2}{2}+\frac{r^4}{4},\qquad F(r)=V'(r)=r+r^3,
\]

and consider the equations

\[
 \dot r_i=p_i-p_{i-1},\qquad
 \dot p_i=F(r_{i+1})-F(r_i).                    \tag{1}
\]

All the r_i and p_i range independently over R. In particle coordinates,
r_i=q_i-q_{i-1}; allowing every total stretch amounts to allowing every
twisted periodic boundary condition. Thus conservation below means conservation
on the union of all total-stretch sectors.

## Theorem

Let f(x,y,u,v) be a real polynomial of total degree at most six. For a fixed
N >= 5, the quantity

\[
 Q_f(r,p)=\sum_{i=0}^{N-1} f(r_i,p_i,r_{i+1},p_{i+1})
\]

is conserved by (1) at every phase point if and only if

\[
 \begin{split}
 f(x,y,u,v)={}&c_0+c_Rx+c_Py
       +c_H\left(\frac{y^2}{2}+\frac{x^2}{2}+\frac{x^4}{4}\right)\\
       &+g(x,y)-g(u,v),                         \tag{2}
 \end{split}
\]

where g is a polynomial of total degree at most six and the c's are real
constants. In particular,

\[
 Q_f=c_0N+c_R\sum_i r_i+c_P\sum_i p_i+c_HH,
 \qquad H=\sum_i\left(\frac{p_i^2}{2}+V(r_i)\right).
\]

This is a computer-assisted finite linear algebra theorem. The full integer
matrix, its kernel vectors, and nonzero minors are in `charge_data.json`.
`verify_certificate.py` checks the certificate without importing the program
that generated it.

## 1. The conservation operator

Let z_i=(r_i,p_i), and let T shift every index by one. The generator is

\[
 L=\sum_i\left[(p_i-p_{i-1})\partial_{r_i}
       +(F(r_{i+1})-F(r_i))\partial_{p_i}\right]. \tag{3}
\]

It commutes with T. If f is placed at sites 0,1, the ordinary chain rule gives

\[
 \begin{split}
 Lf={}& f_x(p_0-p_{-1})
       +f_y(F(r_1)-F(r_0))\\
     &+f_u(p_1-p_0)+f_v(F(r_2)-F(r_1)).          \tag{4}
 \end{split}
\]

Consequently LQ_f = sum_i T^i Lf. Since (1) has a smooth vector field,
conservation for all initial data is equivalent to the polynomial identity
LQ_f=0. The conserved positive energy H bounds all coordinates on each
trajectory, so solutions exist globally; local existence would already suffice
for this equivalence.

There are

\[
 D=\binom{6+4}{4}=210                           \tag{5}
\]

monomials x^a y^b u^c v^d of degree at most six. One way to count them is to add
a fifth nonnegative exponent making the sum exactly six, and apply stars and
bars. These monomials form the column basis of the conservation operator.

## 2. Removing the dependence on N

For a nonconstant monomial in the r_i,p_i, its site support consists of the
indices where at least one exponent is positive. Identify monomials that differ
by an integer translation. A representative is obtained by shifting the smallest
occupied index to zero and listing the exponent pairs up to the largest occupied
index. This representative retains the order of sites; it does not identify
reflections.

Every term of (4) has support in either {-1,0,1} or {0,1,2}. Indeed a single
derivative can introduce site -1 or site 2, but never both. Thus every support
has diameter at most two. The output degree is at most eight because the cubic
force multiplies a derivative of degree at most five. No constant monomial can
be produced: every vector-field term has positive degree.

Distinct such infinite-chain translation classes remain distinct on a ring
of N >= 5 sites. To see this, take a support with at least two occupied sites,
contained in an integer interval of diameter d <= 2. In cyclic order, the gap
from its last occupied site to its first has length N-d >= 3. All other gaps
have length at most d <= 2. This is the unique largest gap. The support and
the r,p exponents can therefore be lifted uniquely to the line, up to translation,
by cutting at this gap. A one-site support plainly has the same uniqueness.
The same argument shows that every nonconstant monomial here has a cyclic orbit
of size N: a rotation fixing the monomial must preserve the unique gap and hence
its endpoints, or fix the single occupied site.

For a column monomial m, expand Lm from (4), translate each output monomial
to its representative, and add its integer coefficients. Call the resulting
coefficient of representative w the entry M_(w,m). For N >= 5, in
sum_i T^i Lm the coefficient of each individual monomial in the orbit of w is
exactly M_(w,m). This follows because each term with representative w visits
each of the N distinct orbit members once. Distinct w have disjoint orbits.
Therefore, if a is the column of coefficients of f,

\[
 LQ_f=0 \quad\Longleftrightarrow\quad Ma=0,      \tag{6}
\]

for every fixed N >= 5, with the same matrix M.

## 3. The explicit integer matrix

The following rule specifies every entry without any dynamical approximation.
For alpha=(a,b,c,d), start with the exponent list

\[
 e=(0,0,a,b,c,d,0,0)
\]

at sites -1,0,1,2, in the order r,p at each site. For each nonzero exponent k
of a variable at site j=0 or 1, decrease that exponent by one and do the
following:

* For an r_j derivative, add one to the p_j exponent with coefficient k,
  and one to the p_(j-1) exponent with coefficient -k.
* For a p_j derivative, add one or three to the r_(j+1) exponent with
  coefficient k, and one or three to the r_j exponent with coefficient -k.

Trim zero exponent pairs at both ends of each resulting list and add
coefficients for identical lists. This is exactly (4) on a monomial.
Zero rows may be dropped. Lexicographic order of the 210 alpha's and of the
remaining exponent lists gives the matrix stored in `charge_data.json`:

\[
 M\in\mathbb Z^{631\times210}.                 \tag{7}
\]

The JSON fields `column_exponents` and `row_monomials_interleaved_r_p` record
these orders. `sparse_matrix_rows` lists each nonzero column index and integer
entry for each row. Indices are zero based.

As a separate check of this rule, the verifier first forms Q_m on a five-site
ring in all ten variables and differentiates that full polynomial. It also
expands each saved matrix row into the sum of its five translates. These full
polynomials agree coefficient by coefficient for all 210 columns. No
translation reduction is used in that comparison.

## 4. The kernel and rank certificate

For each a,b >= 0 with 1 <= a+b <= 6, the density

\[
 x^a y^b-u^a v^b                                \tag{8}
\]

has identically zero sum. There are

\[
 \binom{6+2}{2}-1=27                            \tag{9}
\]

such densities. Also, 1,x,y and

\[
 h(x,y)=\frac{y^2}{2}+\frac{x^2}{2}+\frac{x^4}{4}
\]

give conserved sums. For stretch and momentum this follows by telescoping (1).
For energy, directly,

\[
 \begin{split}
 LH&=\sum_i\left[p_i(F(r_{i+1})-F(r_i))
                      +F(r_i)(p_i-p_{i-1})\right]\\
   &=\sum_i[p_iF(r_{i+1})-p_{i-1}F(r_i)]=0.     \tag{10}
 \end{split}
\]

These 31 densities are linearly independent as polynomials. In a linear
relation, the coefficient of each nonconstant monomial u^a v^b forces the
corresponding coefficient in (8) to vanish. The relation then contains only
1,x,y,h. Its x^4 coefficient first forces the h coefficient to vanish, and
then its constant, x, and y coefficients vanish separately. Thus

\[
 \dim\ker M\geq31,\qquad \operatorname{rank}M\leq179. \tag{11}
\]

For the reverse inequality, the certificate gives lists I,J of 179 distinct
row and column indices. Their selected minor has the following determinant
residues. The two certificates are checked separately; each alone suffices.

| Prime p | Size of M[I,J] | det M[I,J] modulo p |
| --- | --- | --- |
| 1000003 | 179 by 179 | 310877 |
| 1000033 | 179 by 179 | 810340 |

The index lists are the `pivot_rows` and `pivot_columns` fields in
`modular_certificates`. Trial division verifies that the displayed moduli are
prime. Gaussian elimination in the corresponding finite field gives the
displayed nonzero residues. Since the determinant is an integer, a nonzero
residue implies a nonzero determinant over Q and over R. Hence

\[
 \operatorname{rank}_{\mathbb Q}M
 =\operatorname{rank}_{\mathbb R}M=179,
 \qquad \dim\ker M=210-179=31.                 \tag{12}
\]

The 31 independent densities already displayed therefore span the kernel.
Combining this with (6) proves (2). Conversely every density in (2) has a
conserved sum by (8) and (10), completing both directions of the theorem.

The verifier also checks M times every candidate kernel vector with integer
arithmetic. It uses 4h in place of h to keep coefficients integral. An
independent check of linear independence gives Gram determinant 994494 modulo
1000003 for these 31 vectors. Exact rational elimination, without modular
arithmetic, gives the same rank 179.

## 5. Rescaled potentials

The same classification holds, with the corresponding energy density, for

\[
 V_{a,b,c,d}(r)=\frac a2r^2+\frac b4r^4+cr+d,
 \qquad a>0,\ b>0.                            \tag{13}
\]

Indeed the constant c in V' cancels between adjacent forces; d has no force.
Let s=sqrt(a/b) and substitute

\[
 r_i=sx_i,\qquad p_i=s\sqrt a\,y_i,
 \qquad \tau=\sqrt a\,t.
\]

Then (1), for force ar+br^3, becomes

\[
 \frac{dx_i}{d\tau}=y_i-y_{i-1},\qquad
 \frac{dy_i}{d\tau}=x_{i+1}+x_{i+1}^3-x_i-x_i^3.
\]

The substitution is invertible, preserves two-site support, and preserves the
space of polynomials of degree at most six. The energy without its affine
terms becomes s^2 a times the normalized energy. Adding cr+d changes its sum
only by c times total stretch plus dN. Thus the four-dimensional span of charges
is exactly the same. These potentials are smooth and uniformly convex since
V''=a+3br^2 >= a.

## 6. Scope and a harmonic control

Setting the cubic part of the force to zero gives a useful distinction. In
addition to the four displayed charges, the harmonic chain conserves

\[
 J=\sum_i p_i(r_i+r_{i+1}),\qquad
 K=\sum_i(p_i p_{i+1}+r_i r_{i+1}).
\]

For J, differentiating and summing cancels the momentum terms and yields

\[
 \dot J=\sum_i\left[r_iF(r_{i+1})-F(r_i)r_{i+1}\right]. \tag{14}
\]

This is zero for F(r)=r. For F(r)=r+r^3 it is

\[
 \sum_i(r_i r_{i+1}^3-r_i^3r_{i+1}),            \tag{15}
\]

a nonzero polynomial: its two monomials belong to distinct translation
classes for N >= 5. For example, r_0=1, r_1=2 and all other stretches zero
gives (15)=6. For K in the harmonic case, its derivative is the sum of

\[
 (r_{i+1}-r_i)p_{i+1}
 +p_i(r_{i+2}-r_{i+1})
 +(p_i-p_{i-1})r_{i+1}
 +r_i(p_{i+1}-p_i),
\]

whose terms cancel after shifting indices. The exact harmonic matrix has
nullity 33, in agreement with these two additional independent densities and
the 31 above (using harmonic energy in place of quartic energy).

The theorem excludes only extra additive, translation-invariant, two-site
polynomial charges of the specified degree. It says nothing about densities
with larger support or degree, nonpolynomial charges, nonlocal integrals,
ergodicity, or relaxation. It assumes a charge is valid on every total-stretch
sector. It does not prove nonintegrability, the absence of all invariant
measures beyond Gibbs states, or the Euler hydrodynamic limit.
