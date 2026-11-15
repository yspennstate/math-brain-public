# Cancellation in restricted Fourier coefficients

The universal Gamma conjecture is not proved or refuted here. The results below
give an exact composition theorem, the majority asymptotic, the zero set of Gamma,
and explicit obstructions to three proposed proof steps. The normalization includes
the empty set. Logs are base 2 except where `ln` is written.

Write h_S = fhat(S), mu(S) = h_S^2, and a_S = E|c_S|. A summand with h_S = 0 is
defined to be zero. Influences use the usual uniform-cube normalization, so
I_i = Pr[f(x) != f(x with coordinate i flipped)] and I = sum_i I_i.

## 1. What a martingale argument gives, and what it cannot charge locally

Fix S with h_S != 0, and order the coordinates outside S. Let R_t be the first t
of them and

    M_t = E[c_S | x on R_t],       L_t = E|M_t|.

Then M_0 = h_S, M_final = c_S, and Jensen gives

    |h_S| = L_0 <= L_1 <= ... <= L_final = a_S.

Consequently the exact, nonnegative telescoping identity is

    Gamma(f) = sum_S mu(S) sum_t log(L_t/L_(t-1)).                 (1)

All denominators in a contributing term are positive. If the next coordinate is i,
write M_t = A + x_i D, where A and D depend on the previous revealed values. The
identity (|a+b|+|a-b|)/2 = max(|a|,|b|) gives

    L_t - L_(t-1) = E (|D|-|A|)_+.                               (2)

This states precisely where cancellation becomes visible. The logarithm of the
expected absolute values in (1) cannot be replaced with an expected logarithm
without a further inequality.

There is a useful first-reveal bound. Before anything has been exposed, A = h_S
and D = h_(S+i), so the contribution for S not containing i is

    h_S^2 log max(1, |h_(S+i)|/|h_S|).

For fixed b, max_(0<a<=b) a^2 log(b/a) = b^2/(2 e ln 2). Thus the sum for that
first coordinate is at most I_i/(2 e ln 2). This calculation does not extend to
later reveals: the weight is the original h_S^2 while A is now conditional.

### A Boolean family rules out any constant per-coordinate bound on later reveals

Let k be positive and even, and use k bits x, followed by two selector coordinates
r and i. Set

    g(x) = (-1)^(x_1 x_2 + x_3 x_4 + ... + x_(k-1) x_k).

This is a bent function: each of its Fourier coefficients has magnitude 2^(-k/2).
This also follows by tensoring the four-entry Walsh transform of (-1)^(uv).
Define f as follows, where i is written as a sign:

    r = +1: f = g(x);
    r = -1: f = i at x = 0, -i at x = e_1, and +1 elsewhere.

For S contained in the x coordinates and containing coordinate 1, the r=-1
branch's coefficient, averaged in i, is zero. Its i-derivative coefficient is
p = 2^(1-k). The r=+1 branch's coefficient has magnitude b = 2^(-k/2).
Therefore, after revealing r and before revealing i, L = b/2. After revealing i,
L = (b+p)/2. The original coefficient has magnitude b/2.

There are 2^(k-1) such sets S, so just these sets contribute

    Q_k = (1/8) log(1 + 2^(1-k/2))                               (3)

to coordinate i's step of (1). Directly I_i = 2^(-k), since its edges change only
on the r=-1 branch at those two points. Hence

    Q_k / I_i = 2^k/8 log(1 + 2^(1-k/2))
              ~ 2^(k/2)/(4 ln 2) -> infinity.                    (4)

All other martingale charges are nonnegative. Thus no inequality saying that each
coordinate's total reveal charge is at most C I_i can hold with universal C for
this reveal order. The construction is Boolean, not a real-valued surrogate.
It leaves open a charge that transfers cost between coordinates or between sets.

`theory_checks.py` checks (1) on every function through four variables and checks
(3) and the coordinate influence independently from truth tables.

## 2. Two natural superset/coding arguments fail

### Fourier triangle inequality loses an unbounded factor

The valid inequality

    a_S <= V(S) := sum_(U containing S) |h_U|

would give the surrogate T = sum_S mu(S) log(V(S)/|h_S|). Unfortunately T is not
O(I), even on majority. For n = 2m+1 and a_m = binom(2m,m)/4^m, the formulas in
Section 5 give

    V({i}) = a_m sum_(r=0)^m binom(m,r) = a_m 2^m.

The level-one terms alone give T >= n a_m^2 m, while I = n a_m. Thus

    T/I >= m a_m ~ sqrt(n/(2 pi)) -> infinity.                    (5)

This is the exact failing step of the plain absolute-Fourier-superset argument;
the true Gamma/I of majority stays bounded.

### A tempting sub-probability measure cannot be normalized at fixed cost per set

For fixed 0<t<1, consider

    nu_t(S) = t^|S| |h_S| a_S,       Z_t = sum_S nu_t(S).

If Z_t <= 1, the log-sum inequality (or Gibbs' inequality after normalization)
would prove

    Gamma <= I log(1/t).

Indeed log(a_S/|h_S|) = log(nu_t(S)/mu(S)) + |S| log(1/t), and
sum mu log(nu_t/mu) <= log Z_t. This argument itself is valid; its proposed
normalization is false.

For odd majority the exact value is

    Z_t = n a_m^2 sum_(r=0)^m binom(m,r) t^(2r+1)/(2r+1)
        = n a_m^2 integral_0^t (1+x^2)^m dx.                     (6)

For every fixed t>0 it tends to infinity: the integral is at least
(t/2)(1+t^2/4)^m and n a_m^2 tends to 2/pi. Thus no fixed exponential penalty
t^|S| makes these particular nu_t into sub-probabilities. A cost bounded by C|S|
in this same pointwise construction is also impossible, since its total mass is
bounded below by Z_(2^-C). This obstruction does not exclude more elaborate
coding kernels that spread mass from supersets differently.

Equation (6) and the triangle lower bound (5) are evaluated in theory_checks.json.
The general Gibbs/superset program remains unresolved.

## 3. Hypercontractivity does not control the missing mean

For k>=2 choose S to be k coordinates and one further sign coordinate z. Let the
z=+1 restriction be parity chi_S. Let the z=-1 restriction be -chi_S except at a
single input, where its output is flipped. Its S-coefficient is
-1+2^(1-k). Consequently

    c_S(+1)=1,       c_S(-1)=-1+2^(1-k),
    E c_S=2^-k,     E|c_S|=1-2^-k,
    a_S/|h_S|=2^k-1.                                             (7)

As a function of outside coordinates c_S has degree one, is bounded by one, and
has exactly the required 2^(1-k) granularity. Its Lp norms for any fixed p>=1 tend
to one, while its mean tends to zero. Thus neither bounded degree in the outside
variables, the lattice condition, nor ordinary hypercontractive norm comparison
can give log(a_S/|h_S|) <= C times the outside degree. This fails by (7).

This example does not disprove a weighted aggregate hypercontractive argument:
mu(S)=4^-k is tiny, and the top superset carries most of the spectral weight.
Cauchy-Schwarz gives Gamma <= B/2, as in the shared notes, but replacing that
dispersion term with O(I) is precisely the missing aggregate step.

## 4. Exactly when Gamma is zero

Triangle inequality gives a_S>=|h_S|, so every contributing term is nonnegative.
Equality E|X|=|EX| for a real random variable with nonzero mean holds if and only
if X has the sign of its mean almost surely. On the finite cube this proves

    Gamma(f)=0 iff, for every S with h_S != 0,
                      h_S c_S(z) >= 0 for every outside assignment z.            (8)

The empty set matters: c_empty(z)=f(z) and a_empty=1. Hence a nonconstant
zero-Gamma function must be balanced. Equivalently the zero set consists of the
two constants and the balanced Boolean functions satisfying the nonempty part
of (8). Derivatives with h_S=0 need not have a constant sign.

This corrects two possible readings of the brief. Constant signs for every
nonempty derivative do not by themselves give Gamma=0 for a biased function:
AND_2 has Gamma=1/4, entirely from its bias of magnitude 1/2. Conversely constant
signs for all derivatives are not necessary: majority on three variables has
Gamma=0, while D_{1,2} Maj_3 is a nonzero multiple of the third variable.
Requiring a constant sign also for D_empty=f permits only constants.

Input sign changes, output sign changes, and permutations preserve Gamma, since
they preserve |h_S| and a_S up to reindexing. In particular unateness contributes
no new obstruction beyond monotonicity. For a monotone function D_i f has fixed
sign, so every singleton term is zero; higher-order terms need not vanish.
Balanced Maj_5 is a concrete monotone example with positive Gamma.

Useful inclusions and exclusions follow from (8):

* Every nonconstant Boolean function whose Fourier support is an inclusion
  antichain has Gamma=0. At an active S there is no active strict superset, so
  c_S=h_S is constant. This includes homogeneous Boolean functions and parities.
  These antichain functions themselves satisfy H<=2(I-1): at a maximal active
  nonempty S, Boolean granularity gives |h_S|>=2^(1-|S|), so
  log(1/mu(S))<=2(|S|-1), and summation proves the claim.
* Balanced, disjoint compositions of zero-Gamma functions again have Gamma=0,
  by Section 6. This includes arbitrary recursive compositions of Maj_3 and
  parity. Fixed bounded-arity read-once formulas are a known FEI class, so these
  are an explicit zero-Gamma subclass of it.
* All read-once AND/OR/NOT formulas have constant-sign nonempty derivatives, but
  generally have positive Gamma equal to their empty-set term. For completeness,
  write a formula's 0/1 output at an AND root as F_1 F_2. A mixed derivative
  factors into the derivatives on the active children, times unchanged 0/1
  children; at an OR root use 1-(1-F_1)(1-F_2). A derivative touching both
  children gains a fixed minus sign at OR. Induction from possibly negated
  leaves proves the assertion. Thus

        Gamma = b^2 log(1/|b|),       b=E f,                       (9)

  with the zero convention. For a nonconstant essential read-once AND/OR formula
  with n leaves, its 0/1 output probability has an odd numerator over 2^n:
  AND multiplies odd numerators and OR multiplies the complementary odd
  numerators. Hence such a formula is balanced only when n=1. The full read-once
  AND/OR class is therefore not contained in the zero set.
* Neither the monotone/unate class nor the full symmetric class is contained in
  the zero set, as Maj_5 shows. Flat Fourier magnitude (bentness) does not imply
  zero Gamma either; Section 7 supplies examples.

The FEI references for read-once decision trees, symmetric functions, and general
bounded-arity read-once composition are O'Donnell--Wright--Zhou,
[The Fourier Entropy--Influence Conjecture for certain classes of Boolean functions](https://yuanz.web.illinois.edu/papers/fei-icalp.pdf),
and O'Donnell--Tan,
[A composition theorem for the Fourier Entropy-Influence conjecture](https://www.cs.cmu.edu/~odonnell/papers/fei-composition.pdf).
These citations concern the known FEI classes; the elementary Gamma statements
above are proved here, without a claim of literature priority.

Two elementary quantitative bounds are sometimes useful. For b=E f,

    Gamma_empty = -(b^2 ln b^2)/(2 ln 2)
                <= (1-b^2)/(2 ln 2) <= I/(2 ln 2).                (10)

Here -t ln t<=1-t and Var(f)<=I. For singleton S={i}, c_i is 0 or +/-1, so
a_i=I_i and |h_i|<=I_i. Maximizing a^2 log(I_i/a) gives the sharper version of
the brief's singleton estimate:

    Gamma_{i} <= I_i^2/(2 e ln 2) <= I_i/(2 e ln 2).               (11)

For monotone and unate functions the singleton terms are exactly zero, as above.

## 5. Odd majority: exact formula and the asymptotic constant

Let n=2m+1 and f(x)=+1 when the number of 1-bits is at most m, and -1 otherwise.
Set a_j=binom(2j,j)/4^j. For |S|=k>=1 and outside Hamming weight t, the kth
finite difference of this step function is

    c_S(t) = 2^(1-k) (-1)^(m-t) binom(k-1,m-t),                  (12)

where a binomial coefficient outside its range is zero. This follows by summing
the alternating binomial coefficients up to m-t; the identity is
sum_(j=0)^u (-1)^j binom(k,j)=(-1)^u binom(k-1,u).
Taking absolute values and applying Vandermonde gives, for every nonempty S,

    a_S = 2^(1-n) sum_t binom(n-k,t) binom(k-1,m-t)
        = 2^(1-n) binom(n-1,m) = a_m.                            (13)

Symmetry under global sign flip kills the even Fourier levels. For k=2r+1,

    h_k = (-1)^r a_m binom(m,r)/binom(2m,2r).                    (14)

Here is a derivation of (14), to fix its normalization. D_i f is the indicator
that the other 2m coordinates have exactly m 1-bits. On that middle layer the
average product of a fixed 2r coordinates is
(-1)^r binom(m,r)/binom(2m,2r): expand
product_j(1+t x_j)=(1-t^2)^m and compare the coefficient of t^(2r).
Multiplying that average by the middle-layer probability a_m proves (14).

Since f is balanced, Parseval and (13) give the exact identity

    Gamma(Maj_n) = H(Maj_n)/2 + log a_m,
    I(Maj_n) = n a_m.                                           (15)

For a proof of the limiting constant, the mass W_k at k=2r+1 can be rewritten as

    W_k = binom(n,k) h_k^2 = (n/k) a_m a_r a_(m-r).              (16)

On compact subintervals 0<alpha=k/n<1, Wallis/Stirling estimates give uniformly

    W_k = (2/pi)^(3/2) n^(-3/2)
          alpha^(-3/2) (1-alpha)^(-1/2) (1+o(1)).                (17)

Uniformly in k, log(1/h_k^2)=n h_2(k/n)+O(log n): use
binom(n,k) between 2^(n h_2(k/n))/(n+1) and 2^(n h_2(k/n)), together with
(16) and the two-sided bounds a_j comparable to (j+1)^(-1/2). Summing the
O(log n) error against the probability masses contributes only O(log n).

For clarity, endpoint control in the resulting Riemann sum is not assumed.
Equation (16) gives W_k<=C k^(-3/2) for k<=n/2 and
W_k<=C/[n sqrt(n-k+1)] for k>=n/2. Using
h_2(x)<=C x log(e/x) near zero, the contribution to H/sqrt(n) from k<=epsilon n
is at most C sqrt(epsilon) log(e/epsilon)+o(1). The contribution from
k>=(1-epsilon)n is at most C epsilon^(3/2) log(e/epsilon)+o(1).
Both vanish as epsilon decreases to zero. Thus (17), with spacing 2/n, yields

    lim H/sqrt(n) = (1/2)(2/pi)^(3/2) J,
    J = integral_0^1 h_2(x)/[x^(3/2) sqrt(1-x)] dx.

To evaluate J, use natural entropy h(x)=-x ln x-(1-x)ln(1-x). An antiderivative
of x^(-3/2)(1-x)^(-1/2) is -2 sqrt((1-x)/x), and the boundary terms vanish.
Integration by parts gives

    (ln 2) J = 2 integral_0^1 x^(-1/2)(1-x)^(1/2)
                                  ln((1-x)/x) dx
             = 2 B(1/2,3/2) [psi(3/2)-psi(1/2)] = 2 pi.

In the last step B(1/2,3/2)=pi/2 and psi(u+1)-psi(u)=1/u; alternatively these
identities follow by differentiating the elementary beta integral.
As I/sqrt(n)->sqrt(2/pi), (15) finally proves

    lim Gamma(Maj_n)/I(Maj_n) = 1/ln 2,
    Gamma(Maj_n) ~ [sqrt(2/pi)/ln 2] sqrt(n).                     (18)

The balanced ratio Gamma/(I-1) has the same limit. Therefore any universal C in
the Gamma conjecture must be at least 1/ln 2. The numerical script uses a stable
central-binomial recurrence and independently compares it with exact-integer
finite differences at smaller n; it also checks the integral by quadrature.

## 6. Exact composition, and what amplification can establish

Let F=f(g_1,...,g_m), with disjoint blocks and every g_i balanced. Write a subset
U of the input coordinates as block subsets U_i and T={i: U_i is nonempty}.
Fourier expansion, using E g_i=0, gives

    Fhat(U)=fhat(T) product_(i in T) ghat_i(U_i).                 (19)

Under a restriction outside U, differentiation in its free coordinates gives

    c_U^F(z) = c_T^f(y) product_(i in T) c_(U_i)^(g_i)(z_i),     (20)

where y_j=g_j(z_j) for the wholly fixed blocks j not in T. Those y_j are
independent uniform signs, independent of all the displayed derivative factors.
Taking absolute values and expectations in (20) therefore gives

    abs1_F(U)=abs1_f(T) product_(i in T) abs1_(g_i)(U_i).         (21)

Equations (19)--(21) include U=empty: abs1_F(empty)=abs1_f(empty)=1. For each
contributing coefficient, the cancellation logarithm is a sum of the outer
logarithm and the active inner logarithms. Sum against the squared coefficient.
For each balanced g_i its nonempty spectral mass sums to 1. The outer term sums
to Gamma(f), and an inner term's weight is Pr_(T~mu_f)[i in T]=I_i(f). Hence

    Gamma(F)=Gamma(f)+sum_i I_i(f) Gamma(g_i),
    I(F)=sum_i I_i(f) I(g_i).                                   (22)

In particular for a common inner g this is exactly the law asked in the brief:

    Gamma(f o g)=Gamma(f)+I(f) Gamma(g).

Balancedness is used both for the Fourier factorization and for the uniform law
of the wholly fixed blocks. Formula (22) is not asserted for biased g_i.

For a balanced f with I(f)>1, depth-d repeated self-composition satisfies

    I_d=I(f)^d,
    Gamma_d=Gamma(f) [I(f)^d-1]/[I(f)-1].

Thus Gamma_d/I_d tends to Gamma(f)/(I(f)-1), and the balanced ratio
Gamma_d/(I_d-1) stays exactly Gamma(f)/(I(f)-1). More generally balanced
composition's ratio Gamma/(I-1) is a weighted average of the constituent balanced
ratios: I(F)-1=(I(f)-1)+sum_i I_i(f)(I(g_i)-1).
It cannot increase that ratio above the largest constituent ratio. Thus
composition amplifies a single balanced witness into a lower bound on the
unrestricted universal C; it cannot on its own create divergence from bounded
balanced building-block ratios.

There is also a product identity without a balancedness assumption. If
F(x,y)=f(x)g(y), all coefficients and all restricted coefficients factor. By
Parseval, Gamma(F)=Gamma(f)+Gamma(g), and I(F)=I(f)+I(g). Thus tensor products
have Gamma/I between their factors' ratios.

These identities also prove an exact equivalence, with the same best constant:

    Gamma(f)<=C I(f) for every Boolean f
    iff Gamma(f)<=C (I(f)-1) for every balanced Boolean f.         (25)

The forward implication follows by self-composing any balanced f with I(f)>1
and taking the limit in (22). If I(f)=1, all its spectral mass is on singletons,
so it has Gamma=0. For the reverse implication, for arbitrary f multiply by a
fresh dictator t. The product is balanced, has Gamma(t f)=Gamma(f) and
I(t f)=I(f)+1. Apply the balanced bound. This explains why the balanced
Gamma/(I-1) search measures exactly the universal constant relevant to the brief,
without a loss from the empty-set convention.

## 7. Quadratic bent functions give another exact benchmark

Let f(x)=(-1)^q(x) on an even number n of bits, where q is quadratic over F_2
and its alternating polar matrix A is nonsingular. Its full Walsh spectrum is
flat: mu(S)=2^-n and I=n/2. For k=|S| write r_S=rank_F2(A restricted to S).

The Walsh transform of a k-variable quadratic polynomial of polar rank r has
constant nonzero magnitude 2^(-r/2), supported on an affine subspace of dimension
r. One proof is to square its character sum and translate: the sum over a shift
vanishes unless the shift is in the radical; the surviving radical characters
are either all aligned or cancel. Equivalently an invertible change of basis
splits the polynomial into r/2 two-bit products and k-r linear coordinates.

As the outside variables vary, the linear term on S varies by A_(S,outside) z.
It maps onto the quotient by im A_S: otherwise a nonzero vector v supported on S
would annihilate both A_S and A_(S,outside), contradicting nonsingularity of A.
Therefore the chance of lying in the required affine support is 2^(-(k-r_S)),
and

    abs1(S)=2^(-k+r_S/2).

Substitution and averaging over uniform S give

    Gamma = (1/2) E_S r_S,
    Gamma/I = E_S r_S/n <= 1/2.                                 (23)

Every alternating matrix has even rank, so in fact
E r_S <= E[k-(k mod 2)]=n/2-1/2. The complete-graph matrix (zero diagonal,
ones off diagonal) is nonsingular for even n and every principal submatrix has
rank k when k is even and k-1 when k is odd. Thus it attains the exact largest
Gamma among quadratic bent functions:

    Gamma=n/4-1/4,       Gamma/I=1/2-1/(2n).                     (24)

For a perfect matching A, the product-of-two-bit-gates family instead has
Gamma=n/8 and Gamma/I=1/4. These benchmarks reach all even dimensions in the
brief; multiplying by a fresh dictator gives balanced odd-dimensional examples
using the product identity. They do not suggest an unbounded quadratic family.

## Verdicts

(a) The martingale telescope and first-reveal charge are proved. Any fixed charge
of each later reveal to its own coordinate influence is false by (3)--(4).
An aggregate redistribution argument is still open.

(b) Absolute superset summation and the fixed exponential sub-probability ansatz
fail on majority, by (5) and (6). No replacement Gibbs kernel proving the general
bound was found.

(c) Hypercontractivity based only on outside degree, boundedness and granularity
cannot compare L1 to the mean, by the Boolean degree-one family (7). A weighted
aggregate argument remains open.

(d) The zero set is exactly (8), with the empty-set correction above. Sign
invariance, antichain inclusion, read-once AND/OR formula (9), and closure under
balanced zero-Gamma composition are proved.

The composition law is proved. Odd majority's constant is exactly 1/ln 2 relative
to influence. No counterexample to a universal Gamma<=C I was found. The general
conjecture and any sharp universal upper constant remain open.
