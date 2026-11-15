# Referee proofs

The source under review is the expressly permitted `NOTES.md` named in `BRIEF.md`.
These arguments were derived independently. All logarithms are base two. A sum
weighted by a zero Fourier mass omits that summand, even if its displayed ratio
is undefined. No assertion about the current literature in the introduction of
the source was used or independently checked.

## Definitions and boundary conventions

Write `chi_S(x) = product_{i in S} x_i`, and use uniform probability on the cube.
The characters are an orthonormal basis, so Parseval gives

    mu(S) = fhat(S)^2,     sum_S mu(S) = E f^2 = 1.

For a fixed nonempty S of size k, averaging `f chi_S` over its free coordinates
gives `c_S(z)`. Expanding f in characters before taking this average gives

    c_S(z) = sum_{U containing S} fhat(U) chi_{U\S}(z).

Averaging this identity, and then its square, over z proves respectively
`E c_S = fhat(S)` and `E c_S^2 = up(S)`. The same statements hold for S empty:
then `c_empty(z)=f(z)`, `up(empty)=abs1(empty)=p(empty)=1`.

For k >= 1 the sum defining `2^k c_S` is an even integer, since it is the sum
of an even number of signs. Thus each nonzero absolute value is at least
`delta_k=2^(1-k)`. It is at most one, by the triangle inequality. Consequently

    |fhat(S)| <= abs1(S),
    abs1(S)^2 <= up(S) <= abs1(S) <= p(S),
    delta_k p(S) <= abs1(S),     delta_k abs1(S) <= up(S).

The first line holds also for empty S. The second line is used only for k >= 1.
These follow, in order, from triangle, Cauchy-Schwarz, `|c|^2 <= |c|`,
`|c| <= 1_{c!=0}`, and the two pointwise granularity inequalities.

If `up(S)=0`, then `c_S=0` everywhere, `p(S)=abs1(S)=fhat(S)=mu(S)=0`.
Conversely `p(S)=0` implies all these zeros. Such an S contributes zero to
every sum. If `mu(S)>0`, all denominators in A, B, Gamma, P are positive.
In particular these four quantities are finite and nonnegative.

For S equal to the full coordinate set, there is one restriction and
`c_S=fhat(S)`, `up(S)=mu(S)`, `p(S)=1` if it is nonzero; Gamma and B have
zero summands there. Nothing in the proofs requires a remaining coordinate.

Finally, for each positive mass,
`log(1/mu)=log(1/up)+log(up/mu)`, proving `H=A+B`. A constant Boolean f has
only `mu(empty)=1`; H, A, B, I, Var, Gamma, P are all zero. The zero-dimensional
cube is exactly this case. These conventions settle every empty, zero-mass,
zero-containment, constant, and full-set case used below.

## Theorem 1 — PROVED

For a supported nonempty S, with k=|S|, the last granularity bound above yields

    |fhat(S)| <= abs1(S) <= 2^(k-1) up(S).

Taking logarithms of positive numbers and rearranging proves

    log(1/up(S)) <= log(up(S)/mu(S)) + 2(k-1).

For S empty the desired summand inequality is simply `0 <= B_empty`, where
`B_empty = mu(empty) log(1/mu(empty))`, interpreted as zero at mu(empty)=0.
Multiplying by mu and summing, the nonempty degree correction is

    sum_{S nonempty} (|S|-1) mu(S) = I - (1-mu(empty)) = I-Var.

Thus

    A <= B + 2I - 2Var,
    H <= 2B + 2I - 2Var.

The distinction between empty and nonempty S is essential to the proof; one
must not apply the k>=1 granularity formula to S empty.

### Exactly when equality holds

The exact slack is

    B + 2I - 2Var - A
      = B_empty
        + 2 sum_{S nonempty, mu(S)>0}
            mu(S) log(2^(|S|-1) up(S) / |fhat(S)|).

Every term on the right is nonnegative. Therefore equality holds precisely for
constants, or for balanced Boolean f satisfying the following condition:

For every nonempty S with fhat(S) nonzero, every restricted coefficient c_S(z)
is either zero or `sign(fhat(S)) 2^(1-|S|)`.

This is a necessary and sufficient characterization, not just a collection of
examples. Necessity follows because equality in triangle requires a common sign
and equality in the granularity inequality requires the smallest nonzero
magnitude. Sufficiency follows by substituting those conditions. There is no
condition on an S with zero Fourier coefficient. A nonconstant biased f cannot
be an equality case, since then `0 < mu(empty) < 1` and `B_empty > 0`.

`census4.log` and the independent `analyze_census.py` audit give 578 equality
functions on four coordinates, including functions with irrelevant coordinates.
Up to input permutations, input sign changes, and output sign changes, the
representatives and orbit sizes in `census_analysis.json` are:

| Truth table | Functions |
| --- | ---: |
| 0x0000 | 2 |
| 0x00ff | 8 |
| 0x017f | 64 |
| 0x01ef | 192 |
| 0x035f | 192 |
| 0x03cf | 96 |
| 0x1bd8 | 24 |

Truth-table bit x set means f(x)=-1, as in the source. This table is a finite
census classification; the restricted-coefficient criterion is valid in every
dimension.

### The coefficient 2 is optimal

Consider the Boolean function

    q(x1,x2,x3,x4)
      = (x1*x2 + x2*x3 + x3*x4 - x1*x4)/2.

Indeed, if x1=x3 it equals x1*x2, and otherwise it equals -x1*x4.
Its four Fourier coefficients have magnitude 1/2, all on pairs. Thus it is
balanced and has `(A,B,I,Var)=(2,0,2,1)`: each supported set has up=mu=1/4.
This alone forces a coefficient at least two if the correction `-2Var` is kept.

Let q_1=q, and obtain q_{r+1} by substituting disjoint copies of q_r into q.
The composition proof below and the analogous calculation for I give

    variables(q_r)=4^r,   I(q_r)=2^r,   B(q_r)=0,
    A(q_r)=2(2^r-1),     Var(q_r)=1.

The recurrence for A is `A(q_{r+1})=2+2 A(q_r)`, with initial value two.
Consequently `(A-B)/I = 2-2^(1-r) -> 2`, and these are exact equality cases.
These algebraic values are saved in `precision_audit.json`.

AND_n is a second, different witness. Let `p=2^-n`, so its exceptional output
has probability p. Then

    mu(empty)=(1-2p)^2,  mu(S)=4p^2 for every nonempty S,
    I=2np,  Var=4p(1-p),  B_empty=-(1-2p)^2 log((1-2p)^2).

Every nonempty supported S has the minimal nonzero restricted magnitude with
a fixed sign. Hence its Theorem 1 inequality is an equality, and

    (A-B)/I = 2 - 2Var/I - B_empty/I -> 2.

Here `Var/I=2(1-p)/n`, and `B_empty/I=O(1/n)` by `log(1-t)=-t/ln(2)+O(t^2)`.
The stable high-precision evaluation is in `precision_audit.py`; it uses log1p
to retain this entropy term at very small p.

## Proposition 4 — PROVED, with stronger bounds

For each positive-mass S, put `m=E c`, `a=E|c|`, `u=E c^2`, `p=Pr(c!=0)`.
Then the exact decomposition is

    log(u/m^2) = log(u/a^2) + 2 log(a/|m|).

For a nonempty S of size k, `u<=a` and `a>=delta_k p`. Therefore

    u/a^2 <= 1/a <= 1/(delta_k p),
    log(u/m^2) <= (k-1) + log(1/p) + 2 log(a/|m|).

For S empty, u=a=p=1, so `log(u/m^2)=2 log(a/|m|)` exactly; no degree
correction is inserted. Sum to obtain

    B <= (I-Var) + P + 2 Gamma.

The inequality `p>=u` gives `P<=A`, proving the second upper bound in the
proposition. Cauchy-Schwarz, `a^2<=u`, gives pointwise
`log(a/|m|)<=log(u/m^2)/2`, proving `Gamma<=B/2`. The boundary conventions
above apply throughout, including S empty and S full.

### A simpler, stronger upper bound

The inequality `u<=a` also implies `u/a^2 <= 1/u`. In the same exact
decomposition this gives, including S empty,

    B <= A + 2 Gamma.                                      (P4+)

Thus the proposition's upper bound `(I-Var)+A+2Gamma` is not optimal.
This improvement was also checked over the entire census and random suite
by `referee.cpp`; it is an all-dimension theorem by the argument just given.

Conditional Cauchy-Schwarz on the event c!=0 gives `a^2<=p u`, and hence
another useful universal inequality:

    P + 2 Gamma <= B.

It does not reverse the proposition; it bounds the remaining dispersion
between two quantities.

### A sharper version of the first upper bound

For a nonempty S, condition on c!=0 and set V=|c|, delta=2^(1-|S|).
Then delta<=V<=1. Pointwise `(V-delta)(V-1)<=0`, so, writing t=E V,

    E V^2 <= (1+delta)t-delta,
    E V^2 / t^2 <= (1+delta)^2/(4delta).

The last inequality follows either by maximizing the quadratic expression
in 1/t or from `((1+delta)t-2delta)^2>=0`. Since
`u p/a^2 = E V^2/(E V)^2`, this proves

    B <= P + 2Gamma
         + sum_{S nonempty} mu(S)
             log((1+2^(1-|S|))^2 / (4*2^(1-|S|))).            (P4 refined)

For |S|=1 the logarithm is zero; for |S|>=2 it is strictly less than |S|-1.
Thus the first upper bound is also strictly improvable whenever f has a
nonzero Fourier coefficient of degree at least two.

For clarity about what is and is not sharp: the optimal local bound for a
fixed S under only delta<=V<=1 is this refined bound. Equality in the
continuous probability optimization puts mass `delta/(1+delta)` at one and
the remaining mass at delta. It can be approximated by dyadic probabilities
using Boolean restrictions that are parity or a suitably signed AND. As
|S| grows, the refined logarithm is `|S|-3+o(1)`, so its ratio to |S|-1
tends to one. This local observation does not prove that the coefficient
of I-Var in the summed inequality is globally optimal. Its optimal universal
value is not determined here. The census optimum for that coefficient is
recorded separately below.

### Equality and sharpness of the other parts

Equality in the original first upper bound requires `u=a` and `a=delta_k p`
at every supported nonempty S. If f has highest degree d>=2 and a supported
set S of that size, c_S is the constant fhat(S). Equality in `u=a` forces
its magnitude to be one. Parseval then forces f to be a character; equality
in `a=delta_d p` would force delta_d=1, a contradiction. Hence equality is
possible only for degree at most one. A Boolean polynomial of degree at
most one is a constant or a signed dictator: squaring it, its nonconstant
coefficients give `a_i a_j=0` for i!=j and `a_0 a_i=0`, while Parseval gives
unit norm. Conversely all these functions are equality cases. There are
ten such four-coordinate functions, agreeing with `census4.log`.

For `P=A`, equality requires `p=u` on every supported S, or `|c_S|` taking
only zero and one there. Applying this to a highest-degree supported S
forces `|fhat(S)|=1`, so Parseval forces f to be a signed character. Every
signed character does give equality, with P=A=0. Positive values can
approach the same ratio one; the majority argument below proves that the
coefficient one in P<=A cannot be reduced.

The coefficient one-half in `Gamma<=B/2` is attained with positive B. Take

    r(x,y,z) = (1 - x*y + x*z + y*z)/2.

If x=y it equals x*z; otherwise it equals one, so it is Boolean. Its four
Fourier masses are 1/4 at empty and at three pairs. Thus B=1/2 entirely
from the empty set, and Gamma=1/4 entirely from the empty set. P=0,
I=3/2, Var=3/4, A=3/2. This is truth table 0x03c0 on four coordinates
with one irrelevant coordinate; `precision_audit.json` verifies its exact
spectrum and metrics. In particular the half cannot be improved even
when both sides are positive.

Equality in P4+ is also only for signed characters: it requires `u=a`
on every supported set, and the highest-degree argument just given applies.
This equality statement does not claim that its two coefficients are
jointly optimal over all dimensions.

### Why P/A approaches one for odd majority

Here is a proof, rather than an extrapolation of the numerical experiments.
Let n=2m+1 and f be the sign of the sum of n coordinates, with either overall
sign. Put `t=binom(2m,m)/4^m`, the influence of each coordinate, and `L=log(1/t)`.
For each nonempty S of size k, the alternating sum of the majority threshold
on its k free coordinates is, in absolute value,

    2^(1-k) binom(k-1,m-j)

when the outside assignment has j negative coordinates and `0<=m-j<=k-1`,
and is zero otherwise. This follows from the partial alternating-binomial
identity `sum_{a=0}^q (-1)^a binom(k,a)=(-1)^q binom(k-1,q)`.
Vandermonde's identity now gives `abs1(S)=t`, for every nonempty S.
Thus `up(S)<=t<=p(S)` and conditional Cauchy gives `up(S)>=t^2/p(S)`.
Because majority is balanced, its full spectral mass is on nonempty sets.
Averaging these inequalities gives

    A>=L,    P<=L,    A<=2L-P.

The event c_S!=0 uses at most k possible outside Hamming weights. The largest
atom of a binomial on ell coordinates is at most `sqrt(2/(ell+1))`.
The elementary central-binomial bounds give `t>=1/sqrt(2n)` for n>=3.
For k<=n/2 these facts give `p(S)<=2k/sqrt(n)<=3kt`; for k>n/2 the same
bound follows from p<=1. The case n=1 is direct. Therefore

    P >= L-log(3)-E_mu log |S|.

It remains to bound the last expectation uniformly in n. The Fourier
coefficients at even levels vanish, while at level k=2r+1 they have magnitude

    t binom(m,r)/binom(2m,2r).

For example, differentiate in one coordinate: its derivative is the indicator
that the other 2m coordinates tie. The alternating sum on that middle slice
is the coefficient of z^(2r) in `(1-z^2)^m`, divided by binom(2m,2r).
This proves the displayed coefficient formula. Writing
`c_j=binom(2j,j)/4^j`, the total spectral mass on level 2r+1 is exactly

    w_(2r+1) = (2m+1)/(2r+1) * c_m * c_r * c_(m-r).

The elementary bounds `1/(2 sqrt(j))<=c_j<=1/sqrt(j+1)` for j>=1,
with c_0=1, follow by induction from `c_(j+1)/c_j=(2j+1)/(2j+2)`.
For r<=m/2 this bounds the level mass by a fixed constant times
`(r+1)^(-3/2)`. For r>m/2 it bounds the level mass by a fixed constant
times `1/((m+1) sqrt(m-r+1))`. Hence

    sum_r w_(2r+1) log(2r+1) = O(1):

the first range is a convergent logarithm-weighted p-series; the second
is `O(log(m+1)/sqrt(m+1))`. All constants here are absolute. It follows
that `P>=L-O(1)` and `A<=L+O(1)`, while L grows like one-half log n.
Thus `P/A -> 1`. `majority_levels.json` is an independent exact-coefficient
finite check, not the justification of this limit.

## Lemma 2 (coding) — PROVED

Fix 0<lambda<1 and define

    nu(S)=(1-lambda)^|S|
          sum_{U containing S} lambda^|U\S| mu(U).

Its mass is exactly one, since after swapping the finite sums its contribution
from each U is

    mu(U) sum_{S subset U} (1-lambda)^|S| lambda^|U\S| = mu(U).

The equality uses the binomial theorem. For supported S, the U=S term shows
nu(S)>0. For any probability measures mu,nu, relative entropy
`D(mu||nu)=sum mu log(mu/nu)` is nonnegative. One direct proof uses
`ln t<=t-1`: applying it to nu(S)/mu(S) and summing over supported S gives
`sum mu ln(nu/mu) <= sum_{mu>0} nu - 1 <= 0`. A zero nu at positive mu
instead gives infinite D, which also satisfies nonnegativity.

Apply this to the nu just constructed and rearrange:

    D(mu||nu)
      = B_lambda + I log(1/(1-lambda)) - B >= 0.

This proves the lemma with exactly the constants in the source. Its displayed
conditional expectation is just `up_lambda/up`, by conditioning U on containing S.
At S empty it remains meaningful and contributes no degree correction. At
S full, up_lambda=up=mu, so its contribution to B_lambda is zero. Constants
have nu concentrated at empty and all quantities zero. The endpoints lambda=0
and lambda=1 are outside the stated range and are not silently substituted.

For the more general kernel, define `nu(S)=sum_{U containing S} mu(U)r(U,S)`.
The hypothesis on each column of r makes nu a probability measure. On any
supported S with nu(S)>0,

    log(1/E[r(U,S)|U contains S]) = log(up(S)/nu(S)).

Its mu-average is `B+D(mu||nu)`, which proves the claimed bound. If nu(S)=0
at positive mu(S), the right side is infinite and the inequality is still
valid. This also handles kernels with many zero entries. Taking
`r(U,S)=1_{S=U}` gives nu=mu and equality for every f, so the general-kernel
statement has no missing additive term.

### The informal Jensen sentence

The source's sentence “Jensen on B_lam is false by sqrt(n) on majority” does
not specify an inequality, a choice of lambda, or what is compared. It is
not a precise additional statement that can be given a theorem verdict.
The following Jensen upper bound is valid, with D=|U\S|:

    -log E[lambda^D | U contains S]
       <= log(1/lambda) E[D | U contains S].

Indeed `x -> lambda^x` is convex, so its expectation is at least its value
at the mean. A Jensen estimate here may be loose; it is not false with this
direction. `precision_audit.py` evaluates both sides at lambda=1/2 for odd
majority using exact integer coefficients. The ratios are saved in
`majority_levels.json`. No asymptotic theorem about the ambiguous sentence
is asserted in this report.

## Lemma 3 (recursion) — PROVED under the unnormalized quadratic definition

For real-valued g, define `mu_g(S)=ghat(S)^2`, `up_g(S)=sum_{U containing S} mu_g(U)`,
and `B(g)=sum mu_g(S) log(up_g(S)/mu_g(S))`. Do not renormalize mu_g to a
probability measure. This extension is necessary to give the stated recursion
its meaning, since a and d need not be Boolean and their squared norms need
not be one. In particular `B(tg)=t^2 B(g)` and B(0)=0.

Write `g=a+x_i d`, where a,d do not depend on coordinate i. Comparing Fourier
coefficients gives

    ghat(S)=ahat(S),       ghat(S union {i})=dhat(S)  (i not in S).

Partitioning the supersets of S according to whether they contain i proves
exactly

    up_g(S)=up_a(S)+up_d(S),
    up_g(S union {i})=up_d(S).

Partition the sum defining B(g) in the same way. The containing-i part is
exactly B(d). If ahat(S)!=0, its remaining summand satisfies

    ahat(S)^2 log((up_a(S)+up_d(S))/ahat(S)^2)
      = ahat(S)^2 log(up_a(S)/ahat(S)^2)
        + ahat(S)^2 log(1+up_d(S)/up_a(S)).

Here up_a(S)>=ahat(S)^2>0, so division is legitimate. If ahat(S)=0,
both its B(a) and J contributions are defined as zero, even if up_a(S)=0.
Summing proves `B(g)=B(a)+B(d)+J_i(g)`. This covers zero a, zero d, zero g,
S empty, and the full set of coordinates other than i. The original cube
with no coordinate i has no recursion to assert.

`composition_real.cpp` verifies this from independently restricted rational
truth tables; it does not just substitute spectral identities into themselves.
If one were instead to normalize each real function's spectrum before defining
B, this would be a different statement and the displayed recursion would
require norm weights. The verdict here uses the natural unnormalized
extension explicitly specified above.

## Balanced disjoint-block composition — PROVED

Let f be Boolean on m outer inputs, and let each of m disjoint blocks carry
the same balanced Boolean g. Both its mean and its empty Fourier coefficient
are zero. Expand f in characters and each g in its block characters. A global
subset W of block coordinates has nonempty pieces W_j in precisely the set
T of active blocks. Balance means that exactly the outer Fourier term T
can contribute to this coefficient. Thus

    mu_(f o g)(W) = mu_f(T) product_{j in T} mu_g(W_j).

There is no interference between outer terms. Equivalently, sample T from
mu_f and, for each active block, sample a nonempty subset from mu_g; these
independent choices give the full composed spectral distribution.

For a given W with active block set T, a spectral superset may activate any
outer superset V of T. In active blocks its pieces must contain W_j, and
in additional active blocks their total probability is one. Therefore

    up_(f o g)(W) = up_f(T) product_{j in T} up_g(W_j).

On positive mass take the ratio of the last two displays and its logarithm.
Average over the generative distribution: the outer contribution is B(f),
and the inner contribution is `E|T| B(g)=I(f)B(g)`. This proves

    B(f o g)=B(f)+I(f)B(g).

The identical calculation for `-log mu` gives the stated entropy law, and
averaging sizes gives `I(f o g)=I(f)I(g)`. Consequently A has the same
composition law too. The proof includes T empty: all block products are
one and the corresponding probabilities are mu_f(empty) and up_f(empty)=1.
Zero coefficients contribute zero; constant outer f gives both sides zero.
Balanced Boolean g cannot itself be constant, so that purported edge case
is outside the assumptions. All full-block and full-coordinate subsets are
included without exception.

For unequal balanced inner functions g_j the same proof gives

    B(f o (g_j)) = B(f) + sum_j I_j(f) B(g_j).

The balance assumption cannot be dropped. In the truth-table convention
of the source, outer AND_2 and inner AND_2 compose to AND_4, for which
`B=0.7324877755992936` bits. The unbalanced substitution into the claimed
formula would give two bits, since AND_2 has B=I=1. This is an explicit
counterexample to the unbalanced extension, not to the balanced statement.
The direct-table computation is in `composition_real.log`.

## Exact FEI equivalences and constants

Every assertion in this section quantifies over every dimension and every
Boolean function, using constants independent of both. I=0 forces constant
f, whose relevant quantities vanish; thus division by I is unnecessary.

If FEI holds as `H<=C I`, nonnegativity gives

    B<=C I,   A<=C I,   Gamma<=B/2<=C I/2.

If `B<=K I` holds universally, Theorem 1 gives

    H<= (2K+2) I - 2Var <= (2K+2) I.

Hence FEI is equivalent to a universal B bound, with maps
`C -> K=C` and `K -> C=2K+2` (and the stated negative variance correction).

If instead `A<=alpha I` and `Gamma<=gamma I` both hold universally, P4+
gives

    H=A+B<=2A+2Gamma<= (2alpha+2gamma) I.

Conversely FEI gives the pair `(alpha,gamma)=(C,C/2)`. In the source's
same-constant formulation, `A<=K I` and `Gamma<=K I` imply FEI with C=4K,
and FEI with constant C implies the same-constant pair with K=C. Using
only the source's Proposition 4, without P4+, gives the weaker converse
`C=1+2alpha+2gamma`, or `1+4K`; the variance correction is `-Var`.
All these are sufficient transformations of constants, not assertions
that the best possible constants must achieve each transformation.

## Best coefficient tradeoffs from the four-variable census

There is no unique “best” tuple without fixing a tradeoff or objective.
Here is the full feasible region, with the natural restriction that the
displayed coefficients are nonnegative. For unrestricted real coefficients
the same finite-max formulas remain valid, without truncation at zero.

### A <= a B + b I

Let

    beta = 7/8 + (49/16) log(8/7)
         = 1.4649755511985874... .

This is B/I for AND_4, with A/I=31/16. The census-optimal tradeoff is

    b_4(a) = max(1, 31/16 - beta*a),   a>=0.

The breakpoint is `15/(16 beta)=0.6399424203584647...`. AND_4 enforces the
second term, and the balanced homogeneous function represented by 0x1bd8
enforces the first. `precision_audit.py` rederives the coefficients of
all 212 distinct normalized census triples using exact integers and
80-digit logs, and checks the supporting line and the A/I and B/I maxima.
The exact-log formula above is supported by exhaustive finite verification;
it is not an analytic proof for arbitrary dimensions.

For arbitrary dimensions, the proved sufficient pair is `(a,b)=(1,2)`;
every a>=1 works with b=2. The iterated q family proves that b>=2 is
necessary for every fixed a, so b=2 is globally optimal when a>=1.
For a<1 the four-variable curve is only a finite-dimensional observation.
In fact balanced iterations of a function with `(A,B,I)=(2,1,3/2)` force
the necessary condition `b>=4-2a`. Such a function is census representative
0x035f, whose spectrum and metrics are saved in `precision_audit.json`.
The all-dimension frontier for a<1 is not determined here.

### B <= a' A + b' I + c' Gamma

For each nonconstant census function put
`x=A/I, y=Gamma/I, z=B/I`. Then the exact census answer is

    b'_4(a',c') = max(0, max_f [ z_f-a'*x_f-c'*y_f ]),
    a'>=0, c'>=0.

Every underlying mass and restricted coefficient is rational. The exact
values x,y,z are specified by the truth table and the definitions, not by
the rounding of a printed decimal. `coefficient_constraints.json` gives
representatives for all 212 distinct normalized triples, and
`coefficient_frontiers.json` compresses the upper surface to 15 active
constraints found by hull and linear-program checks. The full 212-constraint
formula is the authoritative region; compression is not needed to use it.

For a directly usable compressed formula, take the maximum of zero and
`z-a'*x-c'*y` over these rows. Decimals in this table are rounded; the JSON
files identify the truth tables that specify their exact-log values.
The compression is additionally checked by expressing each census point
as dominated, for this objective, by a convex combination of these rows.

| Truth table | x=A/I | y=Gamma/I | z=B/I |
| --- | ---: | ---: | ---: |
| 0x0001 | 1.937500000 | 0.294987776 | 1.464975551 |
| 0x0003 | 1.583333333 | 0.311278124 | 1.372556249 |
| 0x0007 | 1.550093945 | 0.264871838 | 1.298587621 |
| 0x0016 | 0.825368166 | 0.374701538 | 1.073752878 |
| 0x0017 | 1.300000000 | 0.200000000 | 1.100000000 |
| 0x00ff | 0 | 0 | 0 |
| 0x0116 | 0.584758988 | 0.375000000 | 0.915241012 |
| 0x0117 | 1.058484766 | 0.297760026 | 1.158432420 |
| 0x011e | 0.696277408 | 0.332713350 | 0.966410482 |
| 0x0196 | 0.376375835 | 0.336649096 | 0.763096791 |
| 0x033c | 0.298611200 | 0.319715972 | 0.686685327 |
| 0x033f | 0.833333333 | 0 | 0.500000000 |
| 0x0357 | 1.420958593 | 0.031250000 | 0.795958593 |
| 0x035f | 1.333333333 | 0 | 0.666666667 |
| 0x1669 | 0.102105959 | 0.188852540 | 0.383961977 |

Some census-optimal slices from `census_analysis.json` are:

| a' | c' | smallest nonnegative b' | Witness |
| ---: | ---: | ---: | --- |
| 0 | 0 | 1.464975551198587 | 0x0001 |
| 0 | 2 | 0.875 | 0x0001 |
| 1 | 0 | 0.388074127406442 | 0x033c |
| 1/2 | 1 | 0.331430010996065 | 0x0117 |
| 1 | 2 | 0 | dictator |
| 2 | 0 | 0.179750057999188 | 0x1669 |

The zero at `(a',c')=(1,2)` is proved in every dimension by P4+ and is
optimal in b': a dictator has I>0 and A=B=Gamma=0, forcing b'>=0 even if
one allows negative b'. Thus this particular census optimum is also a
global theorem. The original source's `(1,1,2)` is strictly improvable
to `(1,0,2)`. All other numerical frontier values in this subsection are
census observations, not proposed universal inequalities.

The census also gives

    max (B-P-2Gamma)/(I-Var) = 0.13657007572574492...

over positive denominators, at 0x0796, rather than the coefficient one
in the source's first upper bound. A zero denominator occurs only for
constants or dictators, where its numerator is zero. This is another
finite-census sharpness result; no dimension-independent replacement
of that coefficient is claimed here.

## Verification scope and arithmetic

`referee.cpp` computes integer Walsh numerators h_S and exact integer
containment energies `sum_{U containing S} h_U^2`. It separately differentiates
truth tables on every face; for S of size k, the face numerator is `2^k c_S`.
It checks the exact identity

    sum_z (2^k c_S(z))^2 * 2^(n-k) = sum_{U containing S} h_U^2.

It also checks the integer triangle, granularity, boundedness, Cauchy,
support-count, and coding-normalization inequalities. Only logarithms
and final aggregate comparisons use floating point, with absolute tolerance
2e-10 in their weighted bit units. The independent Python matrix audit
uses a different, direct subcube enumeration and exact integer arithmetic
before taking logs. The high-precision audit uses 80 decimal digits.

The exhaustive census is all 65,536 truth tables on four coordinates,
including all lower-dimensional functions by embedding. It checks every
recursion coordinate, three rational lambda choices (1/4, 1/2, 3/4),
and a general kernel that first picks a cardinality uniformly from
0 through |U| and then a subset uniformly at that cardinality.

The random suite is 1,200,000 independent draws with replacement: 100,000
in each of the twelve (n,p) cells, n=5,6,7,8 and p=0.5,0.2,0.05 for
negative outputs. Seed and generator are in the source. This is not a
claim of that many distinct truth tables. Every draw checks the theorem,
proposition, strengthened inequalities, lambda=1/2 coding, one rotating
recursion coordinate, and composition with the balanced three-variable mux.
Exact local face inequalities are checked at every subset.

For the million-draw composition checks, `composition_check` expands the
composed Fourier distribution in groups rather than allocating a full
3n-coordinate truth table. The mux has two singleton Fourier sets and
two pair Fourier sets, all with mass 1/4. For each outer supported T of
size k and each c from zero through k, the group with c singleton pieces
has multiplicity `2^k binom(k,c)`. With common denominator `2^(6n)`, each
set in that group has squared-coefficient numerator
`h_T^2 2^(4n-2k)` and containment numerator
`up_integer(T) 2^(4n-2k+c)`. The code evaluates the logarithmic sums across
these groups and checks exact total probability one. It then compares
with the composition law. This checks the entire grouped expanded spectrum,
using the disjoint-block coefficient and containment factorization; it is
not a million independent truth-table transforms of 3n-coordinate functions.
That factorization itself is independently tested by the full-table suite.

`composition_real.cpp` instead checks composition by explicit truth tables
for every four-variable outer function with a balanced three-variable mux
inner function; every balanced four-variable inner function with mux as
outer; and every four-variable outer with unequal balanced blocks. It
also checks rational real-valued recursion independently by restricting
truth tables. Its small real suite includes the zero function and zero
a or d cases. `structured.csv` includes AND, OR, strict majority (tie to
the positive output), parity, tribes, address functions, parity times AND,
and quadratic bent functions on four and six variables, as well as constants.

The suite is intended to find counterexamples and arithmetic mistakes.
The proofs above, rather than random testing, justify the universal verdicts.
