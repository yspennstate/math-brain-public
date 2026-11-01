# Independent audit of the fixed-Hamming-band FEI theorem

2 October 2026. The proof in `hamming_band_fei.md` passes independent
mathematical audit. Its conclusion is restricted to monotone functions
with a fixed number of potentially nonsymmetric Hamming layers. It does
not settle FEI for all monotone functions or all linear threshold
functions. Novelty has not been established.

## Established input

I independently opened the author-hosted primary manuscript
https://www.cs.cmu.edu/~odonnell/papers/fei.pdf . Theorem1 states the
symmetric Boolean FEI constant C=12.04, and the definitions use binary
logarithms. This is exactly the input used by the new argument. The
input covers constant symmetric functions as well, whose entropy and
influence are zero.

## Entropy comparison and its uniform constant

For Boolean f,g, let delta=P(f!=g) and d=f-g. Parseval gives
||d||_2^2=4delta. With spectral probability laws Q=fhat^2 and
P=(ghat^2+dhat^2)/(1+4delta), the pointwise inequality Q<=2(1+4delta)P
is correct, including all spectral signs. If Q<=KP then
P=Q/K+(1-1/K)R with R a probability law. Entropy concavity and its
nonnegativity give H(Q)<=K H(P). Applying the mixture entropy upper
bound then gives exactly

    H(f)<=2H(g)+8delta n
       +2(1+4delta)h2(4delta/(1+4delta)).

For delta>0, Boolean truth-table discreteness gives delta>=2^-n.
Writing M=1+4delta, the binary entropy term is

    2log M+8delta log(M/(4delta)).

Using log M<=4delta log e and M/4<=5/4 bounds this by
8delta[n+log e+log(5/4)]. For n>=1 the total is below32delta n,
because8[2+log e+log(5/4)]<32. The comparison constant is therefore
uniform even for rare disagreement in highly biased layers. The case
delta=0 is immediate. The zero-dimensional cube consists only of
constants and is handled separately.

## Layer randomization and influence

The monotone layer averages q_r are nondecreasing by the uniform
set-inclusion coupling. The threshold distribution
mu_t=q_(t+1)-q_t, with q_-1=0 and q_(n+1)=1, is a probability law.
It reproduces the positive fraction q_r in every layer, and its support
lies in a-1,...,b. Thus every selected difference f-g_t is supported
on the same k=b-a+1 layers, including bands touching the endpoint
layers and thresholds that are constant functions.

The exact number of changing edges between layers r and r+1 is
(n-r)binom(n,r)(q_(r+1)-q_r). This follows by subtracting edges with a
positive lower endpoint from those with a positive upper endpoint;
monotonicity is essential. Undirected edge normalization for influence
is2/2^n. Therefore

    I(f)=E_T I(g_T).

The quadratic influence inequality gives E I(f-g_T)<=4I(f), with the
correct factor four. No equality between arbitrary nonsymmetric
individual layers is assumed.

## Band adjacency estimate

For a real function u supported on k consecutive layers, edge
Cauchy-Schwarz gives

    <u,Au><=2 sum_r sqrt((n-r)(r+1))v_r v_(r+1)
            <=(n+1)sum_r v_r v_(r+1).

Here v_r^2 is the uniformly normalized squared mass on layer r.
The path adjacency norm is2cos(pi/(k+1)), so the upper bound is
(n+1)cos(pi/(k+1))||u||_2^2. Also

    I(u)=(n||u||_2^2-<u,Au>)/2.

With s=(k+1)^2 and n>=s, the inequality1-cos(pi/(k+1))>=2/s gives
n-(n+1)cos(pi/(k+1))>=n/s. Hence

    I(u)>=n||u||_2^2/(2s).

The argument uses an upper bound on adjacency, so sign-changing u causes
no problem. For k=1 its internal adjacency is zero, consistently with
the formula. Applying it to u=f-g_T gives
nE delta_T<=2s I(f), including the factors ||f-g_T||^2=4delta_T.

## Small dimensions

The averaged Poincare argument is correct and avoids an invalid
pointwise bound. For two independent thresholds let D(T,U) be their
disagreement probability. Nested thresholds give
|E g_T-E g_U|=2D(T,U), while layer averaging gives E D=E delta_T.
Therefore

    E Var(f-g_T)=4E delta_T-2E D(T,U)^2>=2E delta_T.

Poincare and the quadratic influence bound yield E delta_T<=2I(f).
For n<(k+1)^2 this proves the same required nE delta estimate. Thus
the argument has no missing small-n regime.

## Final constants and one exceptional layer

Averaging the entropy comparison, using symmetric FEI and the exact
influence identity, yields

    H(f)<=24.08I(f)+64(k+1)^2I(f)
         <=[25+64(k+1)^2]I(f).

For one exceptional layer, its boundary count gives
I(f)=2p[rq+(n-r)(1-q)]. Assigning the layer its majority value gives
delta n<=I(f)/2 and I(g)<=2I(f). The improved entropy comparison for
delta<=1/2 gives total constant
48.16+8+4log e=61.930780...<62. The endpoint-layer cases have q=0 or1
because there is only one point, so they create no exception.

## Weighted-threshold consequence and scope

For positive weights, A=sum_i|w_i-1| bounds the difference between
weighted and unweighted sums. Only sum levels in the closed interval
[theta-A,theta+A] can be ambiguous. Their spacing is two, so there
are at most floor(A)+1. Equality conventions at the threshold do not
alter the outside-band conclusions. This proves the stated bounded-A
corollary for arbitrary bias, and the sharper62 constant when A<1.

Signed nonzero weights can be made positive by coordinate sign flips,
preserving Fourier entropy and total influence. If zero weights are
allowed, first delete those irrelevant coordinates; sign flipping does
not itself make zero weights positive. The theorem itself assumes
strictly positive weights, so this is a wording clarification rather
than a gap in the proved statement.

When A grows with dimension, the constant grows too. No argument here
removes that dependence or establishes full LTF or monotone FEI.

## Independent exact finite checks

`independent_hamming_band_check.py` separately enumerates every monotone
Boolean function in dimensions1 through5: respectively3,6,20,168,7581
functions. It checks exact Fraction identities for Fourier influence,
random-threshold expected influence, support in the chosen minimal
band, average disagreement, quadratic influence, averaged variance,
Poincare, and the mean-disagreement bound. Large-dimension one-layer
instances are also checked directly. All checks pass.

Walsh transforms use integer coefficients. Entropy itself is evaluated
in floating point only as an additional numerical check; the analytic
proof above establishes its inequalities. Results are recorded in
`independent_hamming_band_checks.json`. The main inequalities are not
claimed as exact-log computational certificates.

Final verdict: the restricted fixed-band theorem and its stated
consequences are internally correct. The familiar symmetric theorem is
an explicit input. Novelty, full FEI, and broader LTF claims remain
unestablished.
