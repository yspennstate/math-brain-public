# Proof: rank-two posterior and three-defect GU closure

All logarithms are base two.  Write

\[
 f_{A,E}(x)=\chi_A(x)(1-2\mathbf 1_E(x)),\qquad |E|=3.
\]

Global signs do not affect `p`, `U`, `G`, or `I`.  Translation lets us put
`E={0,u,v}` with `u,v` nonzero and distinct.

## 1. Exact rank-two Fourier and upper-set law

Let `N=2^n`, `H={T:T dot u=T dot v=0}`,

\[
 p_0=(1-6/N)^2,\qquad q=4/N^2.
\]

The unmasked nonconstant Fourier coefficient is

\[
 -\frac2N(1+\chi_T(u)+\chi_T(v)).
\]

It has squared magnitude `9q` on `H` and `q` off `H`.  Multiplication by
`chi_A` translates the indices.  Therefore

\[
 p_f(A)=p_0,\quad p_f(T)=
 \begin{cases}
 9q,&T\ne A,\ T\triangle A\in H,\\
 q,&T\triangle A\notin H.
 \end{cases}                                      \tag{1}
\]

Since `|H|=N/4`, (1) is normalized exactly:

\[
 p_0+(N/4-1)9q+(3N/4)q=1.                         \tag{2}
\]

For `S subseteq [n]`, let

\[
 C_{A,u,v}(S)=|\{T\supseteq S:(T\triangle A)\cdot u
 =(T\triangle A)\cdot v=0\}|.
\]

Equivalently, solve the two parity equations on the coordinates outside
`S`.  If the resulting affine system is consistent and its free-column
matrix has rank `r_S`, then
`C=2^(n-|S|-r_S)`; otherwise `C=0`.  The exact upper mass is

\[
 \pi_f(S)=q2^{n-|S|}+8qC_{A,u,v}(S)
 +(p_0-9q)\mathbf1_{S\subseteq A}.                 \tag{3}
\]

Thus the reused-variable posterior is rank two, including the heavy-atom
correction.  It is not replaced by an independent selector law.

## 2. Actual physical restriction recursion

Delete coordinates on which all three points agree; they are genuine dummy
coordinates in the unmasked case and contribute zero to both `G` and `I`.
On each remaining coordinate one physical sign contains one exceptional
point and the companion sign contains the other two.  If `P_{n-1}` is the
one-defect `U` and `V_{n-1,d_i}` the two-defect `U` at the surviving Hamming
separation `d_i`, then

\[
 G(f)=nU(f)-\frac12\sum_{i=1}^n
       (P_{n-1}+V_{n-1,d_i}).                      \tag{4}
\]

Both signs in (4) are retained.  Neither child is declared terminal.  With
a parity mask, deleting coordinate `i` also deletes its mask bit; each child
is exactly a masked one-, two-, or three-defect factor (or a character).

## 3. Unmasked three-defect estimate

Let `e` be the number of cube edges induced by `{0,u,v}`.  The cube is
bipartite, hence `e<=2`, and the edge boundary gives

\[
 I(f)=\frac{2(3n-2e)}N\ge\frac{2(3n-4)}N.          \tag{5}
\]

For nonempty `T`, the heavy atom is not an upper superset.  Equation (3)
gives `pi(T)<=9q2^(n-|T|)`.  Thus a high atom contributes at most
`9q(n-|T|)` and a low atom at most
`q(n-|T|+log_2 9)`.

The annihilator `H` has dimension `n-2`.  A coordinate is identically zero
on `H` exactly when its unit vector lies in `span{u,v}`.  The number of such
coordinates is precisely `e`.  Consequently

\[
 \sum_{T\in H}(n-|T|)=\frac{(n+e)N}{8}.
\]

Summing the preceding atomwise bound, and removing the empty set from the
high sum, yields

\[
 U(f)\le B_{n,e}:=\phi(6/N)
 +\frac{6n+4e+3\log_2 9}{N}-\frac{36n}{N^2},       \tag{6}
\]

where `phi(r)=(1-r)^2 log_2(1/(1-r)^2)`.

For `m=n-1`, the exact one-defect formula and the minimum of the exact
two-defect formulas from the preceding B12 packet give

\[
 P_m=\phi(4/N)+\frac{4(n-1)}N-\frac{16(n-1)}{N^2},\tag{7}
\]

\[
 V_{m,d}\ge Q_m:=\phi(8/N)+\frac{8(n-3)}N
                     -\frac{64(n-2)}{N^2}.         \tag{8}
\]

For separation one the omitted term is positive; for separation at least
two, (8) is the exact minimum over the parity correction.

Insert (6)--(8) into (4), discard only the nonnegative child heavy terms,
and use `phi(r)<=2r/ln 2`:

\[
 G(f)\le \frac nN\left(
 \frac{12}{\ln2}+14+4e+3\log_2 9
 +\frac{4(n-18)}N\right).                          \tag{9}
\]

Use the exact elementary bounds `ln 2>2/3` and
`log_2 9<13/4` (the latter is `9^4<2^13`).  For `8<=n<=18`, the last term
in (9) is nonpositive and the parenthesis is below `49.75`, whereas

\[
 10I(f)\ge\frac nN(60-80/n)\ge\frac{50n}N.
\]

For `n>=19`, the last term is below one while
`60-80/n>55`.  Hence `G<=10I` for every `n>=8`.

The remaining `n=2,...,7` comprise 98 coordinate-permutation types
`(a,b,c)`, where `a,b,c` count the coordinate columns `(1,0),(0,1),(1,1)`.
`CERTIFY.py` uses exact rational Walsh arithmetic and rigorous logarithm
intervals from the 80-term atanh series, including an exact tail bound.  It
certifies `G<=10I` for all 98 types.  Therefore

\[
 \boxed{G(f_{\varnothing,E})\le10I(f_{\varnothing,E})}
 \quad\text{for every three-point }E.              \tag{10}
\]

## 4. Arbitrary nonempty same-variable parity mask

Assume `A` is nonempty.  The heavy atom in (1) contributes `|A|p_0` to
influence, so `I>=p_0`.  Since every child `U` is nonnegative,

\[
 G\le nU\le nH(p_f).                               \tag{11}
\]

Put `rho=6/N`.  From (1), for `n>=4`,

\[
\begin{aligned}
H(p_f)
&\le 3\rho+3\rho(n-\log_2 6)+\rho(n-1)\\
&\le \rho(4n-5).                                  \tag{12}
\end{aligned}
\]

The first term pays the heavy atom using
`-p_0 log_2 p_0 <= (1-p_0)/ln2 <=3rho`; the other two terms are the exact
counts of the `9q` and `q` sectors.  The sequence
`6n(4n-5)/2^n` decreases for `n>=4` and begins at `16.5`, while
`64p_0>=25`.  Equations (11)--(12) imply `G<=64I`.

For `n<=3`, any nonconstant Boolean function has
`I>=n/2^(n-1)` by the edge isoperimetric minimum and
`G<=nH<=n^2`; this is again below `64I`.  Constants have `G=I=0`.
Combining with (10),

\[
 \boxed{G(f_{A,E})\le64I(f_{A,E})}
 \quad(|E|=3,\text{ arbitrary }A).                 \tag{13}
\]

## 5. Closure and GU implication

The earlier B12 packets proved `(16,0)` and `(32,0)` for arbitrary masked
one- and two-defect factors.  Restrictions of a masked three-defect factor
are masked factors with at most three defects or characters, and disjoint
products add `U`, `G`, and `I` exactly.  Hence the restriction-closed class
generated by arbitrary same-block parity-masked factors with at most three
exceptional points satisfies the single pair

\[
 (a,b)=(64,0).                                     \tag{14}
\]

The reviewed GU reduction therefore gives, on this class,

\[
 U\le64I,\qquad H\le(2+2\cdot64)I=130I.            \tag{15}
\]

This is a proper-class theorem, not universal GU.  The remaining hypothesis
is the bounded defect count per irreducible factor.

## 6. Preserved falsifier

The stronger coordinatewise coefficient-two claim is false.  For
`n=5,(a,b,c)=(4,1,0)`, the singleton coordinate of the second type has
rigorously certified

\[
 \Delta_iU/I_i>2.8867058064550006.
\]

The aggregate ratio is smaller because the other coordinate types carry the
companion reserve.  This is exactly why (4) is summed before payment.
