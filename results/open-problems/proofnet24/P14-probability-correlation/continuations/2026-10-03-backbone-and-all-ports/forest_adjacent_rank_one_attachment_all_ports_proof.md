# Adjacent marked edges in a rank-one three-vertex attachment: any number of ports

2 October 2026. Complete analytic derivation, awaiting a fresh independent
audit. It removes the three-port bound from the earlier adjacent theorem by
reversing the roles of the attachment and backbone, and using a credited
scalar graphic-matroid log-concavity theorem. Historical novelty remains
unverified. This is a restricted configuration, not the general forest
correlation conjecture.

## Theorem

Let H be any finite weighted graph with nonnegative activities. Assign each
vertex j of H a nonnegative profile weight beta_j. Add three new vertices
u,v,w with spoke activities respectively `a beta_j`, `b beta_j`, `c beta_j`
to vertex j, where a,b,c>=0. Add marked edges e=uv and f=vw of arbitrary
positive activities. One may also add an unmarked edge g=uw of arbitrary
activity rho>=0. There are no other edges incident to u,v,w.

Then e,f are negatively correlated in the ordinary weighted unrooted-forest
measure. The inequality is strict precisely when either rho>0, or
`a c>0` and `sum_j beta_j>0`. It holds after arbitrary positive-probability
conditioning of H-edge indicators and under arbitrary positive fields on
H and on the three new mutual edges. Rank-one changes of the spoke rows
or profile weights are allowed; independent spoke fields are not asserted.

There is no bound on the number of nonzero profile weights, on the vertex
count of H, or on its topology. The earlier three-common-port adjacent
path theorem is a special case with rho=0 and only three nonzero beta_j.

## 1. Exact component reduction of the arbitrary backbone

Write `s=a+b+c` and initially suppose s>0. For each forest A of H, let
its components have profile sums

    x_C=sum_(j in C) beta_j.

Contracting its selected edges makes the component a single terminal with
spoke activities `a x_C,b x_C,c x_C` to u,v,w. Two selected spokes to the
same new vertex from one H component are a cycle and forbidden. Parallel
spoke choices therefore aggregate to exactly x_C. This component reduction
is an exact forest bijection with multiplicities, not an independence
assumption about the components of a random H forest.

Use u,v,w as a three-vertex core, with column factors a,b,c and each
component as a terminal of row factor x_C. On the five core partitions,
the terminal transfer is

    T(x)=d(x)I+x^2 P+x^3 Q,
    d(x)=1+s x,
    P^2=2sQ,   PQ=QP=Q^2=0.

With

    alpha(x)=x^2/d(x),   gamma(x)=x^3/d(x)^2,

this is `T(x)=d(x) exp[alpha(x)P+gamma(x)Q]`. Thus define

    D_A=product_C d(x_C),
    U_A=sum_C alpha(x_C),   G_A=sum_C gamma(x_C),
    D=sum_(A forest in H) weight(A) D_A>0.

Normalize the finite weights `weight(A)D_A` to a probability nu_s and put

    U=E U_A,
    Gamma=E G_A+s Var(U_A).                         (1)

The commuting truncated exponential gives exactly

    sum_A weight(A) product_C T(x_C)
        =D exp[U P+Gamma Q].                        (2)

Indeed the Q coefficient on the left after normalization is
`E G_A+s E U_A^2`, and on the right it is `Gamma+sU^2`. The variance in
(1) is essential. In particular U,Gamma>=0, and U>0 exactly when some
profile weight is positive.

## 2. Credited scalar log-concavity bounds the mixture variance

The input is Anari, Liu, Oveis Gharan and Vinzant,
*Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for
Independent Sets of Matroids*, [arXiv:1811.01600v1](https://arxiv.org/pdf/1811.01600).
Theorem 4.1 concerns the coefficient-one homogeneous independent-set
polynomial `sum_I y^(n-|I|) product_(i in I)z_i`; there is no factorial
normalization. Lemma 2.2 permits affine orthant-preserving specialization.
Setting y=1 gives exactly the ordinary graphic-matroid unrooted-forest
polynomial used here.

The scalar function D(s) above is the ordinary forest partition sum of H
with one new apex, whose spoke to vertex j has activity `s beta_j`.
For each fixed H forest, one may choose at most one apex spoke from each
component; zero or one choices have total weight `1+s x_C`. This proves
the stated apex identity. The credited theorem, after fixing the H-edge
activities and specializing those spokes affinely, therefore gives

    (log D)''(s)<=0.                                 (3)

Here is the exact closure consequence, including the variance term. Let
`A_0=sum_j beta_j`, independent of the H forest, and put
`W_A=sum_C x_C/d(x_C)`. Termwise identities give

    U_A=(A_0-W_A)/s,
    U_A/s-G_A=sum_C x_C^2/[s d(x_C)^2].

Differentiating the actual finite sum D gives

    (log D)''=-E sum_C x_C^2/d(x_C)^2+Var(W_A).

Since `Var(U_A)=Var(W_A)/s^2`, equation (1) yields the exact identity

    U/s-Gamma=-(log D)''/s>=0.                      (4)

The prior theorem supplies only (3); the component identity, normalization,
and equality (4) have all been shown for the actual forest polynomial.
No off-diagonal logarithmic-Hessian sign is assumed.

## 3. The four marked coefficients and a one-line positive difference

Put `l=ab+ac+bc` and `j=abc`. Starting with the three new vertices as an
empty core gives core partition weights `1,l,j` on `1,P1,Q1`. Selecting
the outer edge g changes the first two to `1+rho` and `l+rho b(a+c)`,
while the Q weight remains j because g joins two core ports. Selecting e
or f joins its pair and leaves only the two-spoke choices to the third
vertex. Selecting both marked edges connects all three, and then g would
make a cycle. Consequently the exact marked partition is

    Z(w_e,w_f)=A+E w_e+F w_f+C w_e w_f,

    A=D[1+rho+(l+rho b(a+c))U+j Gamma+s j U^2],
    E=D[1+rho+c(a+b)U],
    F=D[1+rho+a(b+c)U],
    C=D.                                           (5)

One can also obtain these coefficients by direct deletion/contraction of
the three core edges followed by (2). Expanding the two products gives
the exact Rayleigh difference

    R=E F-A C
      =D^2 {rho(1+rho)
          +ac[(1+2rho)U+ac U^2-b Gamma]}.            (6)

By (4), `b Gamma<=b U/s`. Hence

    R>=D^2 {rho(1+rho)
           +ac[((a+c)/s+2rho)U+ac U^2]}>=0.         (7)

For every positive marked activity, their covariance is
`-w_e w_f R/Z(w_e,w_f)^2`, so (7) proves the asserted negative correlation.
If rho>0 the first term is strict. If rho=0, strictness is exactly `ac>0`
and U>0, equivalently the criterion in the theorem. When neither condition
holds, (6) is zero. If s=0, all spokes vanish and the three new vertices
form only a weighted triangle; directly `R=D^2 rho(1+rho)`, so the same
criterion and conclusion hold.

## 4. Conditioning, fields, verification and scope

Conditioning H edges present contracts their acyclic required components
and sums the beta_j of each component; conditioning them absent deletes
them. The resulting graph is another arbitrary backbone with the same
rank-one attachment. Loop and parallel-edge conventions are the ordinary
graphic-matroid conventions. Positive H-edge fields change its weights;
positive fields on e,f,g change the permitted three core activities. Thus
the proof covers the stated closures. Conditioning g absent sets rho=0;
conditioning g present makes e,f parallel after contraction, so their
simultaneous occurrence is forbidden and their correlation inequality is
immediate. This optional conditioning also preserves the conclusion.

The exact checker `forest_adjacent_rank_one_attachment_all_ports_exact.py`
computes (1)-(7) from literal H forests, independently checks D,D',D'' by
enumerating the actual apex graph, and computes the four coefficients by
direct three-spoke subset transitions. Small cases additionally enumerate
the full original graph including marked subsets, without component
contraction. Its report includes four or more nonzero common-neighbor
profile weights, extra backbone vertices, rational activities, zero middle
rows, zero outer rows, zero profiles, and positive rho.

The scalar graphic-matroid log-concavity result is established prior work,
and the component transfer and variance closure were used in the preceding
arbitrary-unmatched-background theorem. The new conclusion is the all-port
adjacent marked-pair application and its simple difference (6). Its
historical novelty and external review are unverified.

The three new vertices must have proportional spoke profiles and no other
edges except their mutual triangle. This does not cover arbitrary marked
positions, nonproportional profiles, or arbitrary forest indicators. It
does not solve the general all-graph forest pair-correlation conjecture.
