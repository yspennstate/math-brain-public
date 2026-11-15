# Audit of the uniformization reduction

The conclusion being audited is the theorem and equivalence (A)–(C) in
PROOF.md. It is not a proof of T057.

## Two proofs of the essential analytic step

The main proof subtracts the fiber average and obtains
`(D+M) ||U||∞ <= D ||U||∞`. This forces the mean-zero harmonic part to
vanish. It uses the presence of *all* nonidentity vertical elements.

The central translation lemma at the end of PROOF.md gives a separate
probabilistic proof. Bounded harmonic functions evaluated on a random walk
are bounded martingales; their fixed-length squared increments tend to zero.
Every prescribed central displacement has positive probability in a finite
number of steps. Its harmonic difference must therefore vanish. This proof
does not use the fiber average, the special vertical set, a Fourier expansion,
an entropy criterion, or an aperiodicity hypothesis.

Both arguments give equality of bounded harmonic-function spaces under
pullback, not just equality of their dimensions or Liouville statuses.

## Exact worked example, counted two ways

Take G = Z, in additive notation. Let

- μ1(0) = 1/3 and μ1(1) = μ1(-1) = 1/3;
- μ2(1) = μ2(-1) = 1/6 and μ2(2) = μ2(-2) = 1/3.

The normalized first measure has weights 1/2 at ±1; the second already has
no holding mass. A common denominator is D = 6. The integer weights are

- a1(±1) = 3;
- a2(±1) = 1, a2(±2) = 2.

Thus A = 3, M = 4, K = (Z/2Z)^2, N = 9, and α = 2/3.
Write K = {0,u,v,u+v} in that order.

The first set has the three vertical elements plus
`{(1,0),(1,u),(1,v),(-1,0),(-1,u),(-1,v)}`: 3 + 6 = 9.
The second has the same three vertical elements plus
`{(1,0),(-1,0),(2,0),(2,u),(-2,0),(-2,u)}`: again 3 + 6 = 9.

Independent count from the projected probabilities:

- first projection: 1/3 at 0 and 1/3 at each of ±1;
  with denominator 9 the total multiplicity is 3 + 3 + 3 = 9;
- second projection: 1/3 at 0, 1/9 at each of ±1, 2/9 at each of ±2;
  total multiplicity is 3 + 1 + 1 + 2 + 2 = 9.

They sum to one and agree with α ρi + (1-α) δ0. In the first case the
projection happens to equal the original μ1; it need not equal μi in general.
The averaging contraction uses D/(D+M) = 6/10 = 3/5, distinct from the
nonholding fraction α = 6/9 = 2/3. Moving the vertical term -U to the left
is exactly why the contraction denominator is N+1 = 10 rather than N = 9.

The example is an arithmetic check of the construction, not evidence for a
new Liouville or non-Liouville group.

## Bounds checked independently through the rank

The definition gives `r = max(1, ceil(log2 A))`, where the expression means
the smallest integer with 2^r >= max(2,A), without numerical logarithms.
If A >= 2, minimality implies `2^(r-1) < A <= 2^r`, hence M < 2A.
If A = 1, M = 2. This verifies M <= 2A <= 2D. Substituting into the
disjoint-union count gives N <= 3D-1, so D/N > 1/3. Alternatively, after
projecting, the holding-to-moving ratio is `(M-1)/D < 2`; normalizing
`1 : (M-1)/D` gives the same strict lower bound for α.

## Edge cases and attempted failures

1. **Elements of order two.** They are their own inverses. Every K-element
   is also its own inverse, so every tagged element above such a generator
   is its own inverse. No parity condition on a(g) is needed. An odd-order
   cyclic tagging group would require an extra symmetry check and was not used.
2. **Smallest denominator.** D = 1 means that each normalized measure is
   concentrated at one nonidentity element. Symmetry makes that element an
   involution, and generation forces G = Z/2Z. Here M = 2, N = 2, and the
   construction is the four-cycle on (Z/2Z)^2. It is periodic; both proofs
   still apply. No division by D-1 or assumption D >= 2 occurs.
3. **Holding mass close to one.** Only μ(e) < 1 is needed to remove it.
   Equality μ(e) = 1 is impossible for a generating measure on a nontrivial
   group. Rational normalization is still rational.
4. **A equal to a power of two.** Then M = A when A >= 2. The inequality
   needed is M <= 2A; no strict inequality M > A was used. B_g may equal K.
5. **Different supports.** A common denominator exists for the finite union
   of the rational weights, whether or not the supports intersect. Empty
   fibers are omitted. Both supports separately generate G.
6. **Full generation is essential.** Merely attaching distinct tags to
   generators can leave a proper subgroup of G×K. The construction avoids
   this by containing every (g,0) in the support and the complete vertical
   set. Removing the vertical set and using only (g,0) would leave arbitrary
   functions of k harmonic. This is a failure of that proposed shortcut.
7. **Infinite G.** A bounded function need not attain its supremum. The main
   proof takes a supremum of a pointwise bound and never assumes a maximum
   exists. The martingale proof works from each starting point.
8. **Symmetry and sidedness.** All walks use right multiplication. The
   difference d_zf commutes with the Markov operator specifically because z
   is central. The central lemma assumes semigroup generation; symmetric
   generating supports meet this assumption.
9. **Trivial G.** Normalizing δe would divide by zero. It is explicitly
   excluded from the construction and treated separately in the equivalence.
10. **Irrational weights.** Finite uniform sets have rational projected atom
    weights, so this construction cannot directly encode irrational weights.
    Approximation was not used and would require an additional argument
    about preservation of Liouville status.
11. **Finite versus infinite support.** No truncation of the 2026 infinite-
    support counterexamples was claimed. Those examples do not give an input
    pair for this finite-support construction.
12. **Universal versus fixed-group statement.** The output group is G×K,
    rather than G. This proves equivalence of universal assertions; it does
    not prove weight independence for a fixed group from that group's
    generating-set independence alone.

No numerical program or finite simulation was needed for these checks.

## Constant-overhead cyclic refinement

The last theorem in PROOF.md uses an odd cyclic kernel with order M equal
to the least odd integer at least max(3,A). It needs only the two vertical
generators ±1, and has degree D+2. Its analytic proof uses the central
translation lemma. The following spectral calculation checks the same
analytic step independently.

Let ζ = exp(2πi/M), let F be a bounded harmonic function of this lifted
walk, and define, for j = 0,...,M-1,

    f_j(x) = (1/M) sum_{k=0}^{M-1} F(x,k) ζ^(-jk).

In the harmonic equation, summing a translate F(x,k+b) against ζ^(-jk)
and substituting h=k+b multiplies f_j(x) by ζ^(jb). Thus, with
`c_g(j) = sum_{b in B_g} ζ^(jb)`, the equation becomes

    (D+2 - 2 cos(2πj/M)) f_j(x) = sum_g c_g(j) f_j(xg).

The triangle inequality gives `sum_g |c_g(j)| <= sum_g a(g) = D`.
For j != 0 modulo M, `cos(2πj/M) < 1`. Taking supremum norms therefore
forces f_j = 0, since its positive left coefficient is strictly greater
than D. For completeness, the finite geometric sum
`sum_{j=0}^{M-1} ζ^(j(k-h))` is M if k=h modulo M and zero otherwise;
substitution in the definition of f_j gives Fourier inversion
`F(x,k)=sum_j f_j(x)ζ^(jk)`. Hence F(x,k)=f_0(x) is constant on fibers.
This proves the descent without the martingale argument.

For the earlier Z example, D=6 and A=3 now give M=3 and degree 8.
Choose B1,1=B1,-1=C3, B2,1=B2,-1={0}, and
B2,2={0,1}, B2,-2={0,-1}. Both sets have two vertical elements and six
horizontal elements. The first projection has masses 1/4 at 0 and 3/8
at each of ±1. The second has masses 1/4 at 0, 1/8 at each of ±1,
and 1/4 at each of ±2. Counting denominators gives respectively
`2+3+3=8` and `2+1+1+2+2=8`. Both equal
`(3/4)ρi + (1/4)δ0`, as required.

The odd-order choice is essential to this particular all-cardinalities
recipe for inverse-invariant tag sets. Check the extreme sizes directly:
an odd size M uses all C_M; the maximal even size M-1 uses every nonzero
residue. Neither creates the identity in the lifted generating set because
the corresponding first coordinate g is nonidentity. If a tag set omits 0,
the full cyclic vertical subgroup still supplies (g,0), as proved explicitly.

Bounds rechecked by cases: A=1 gives M=3; even A>=2 gives M=A+1;
odd A>=3 gives M=A. Thus M<=A+2<=D+2 and degree is exactly D+2,
independently of M. The projected moving fraction D/(D+2) is at least
1/3. Equality occurs for D=1, which is allowed; a strict bound here would
be false. When D=1, the output is G×C3=C2×C3 with three generators,
so this case also checks that ±1 are counted as two distinct vertical moves.
