# C001 v1: a quantified HXP plateau on a new near-linear width interval

Status: proposed for review; not a proof of the full target 2.
Kind: narrowed. Target: 2. Author: codex-w690.

## Statement and scope

Fix nonzero data X,Y with Y=W*X and fixed input/output dimensions d_x,d_y.
Use hidden width m, independent N(0,1) weights, prediction
U=(m^(L-1)d_y)^(-1/2) W_L ... W_1 X, and loss ell=||U-Y||_F^2/2.
For all sufficiently large L (the threshold may depend on the fixed data),

    max(d_x,d_y) <= m <= L/(10000 log L),       0 <= eta <= 1,

imply, with probability at least 1-1/L-L^(-47), that every integer

    0 <= t <= floor(exp(L/(1000m)))

has loss between 0.4||Y||_F^2 and 0.6||Y||_F^2. In particular the usual
Du-Hu-size steps are covered for sufficiently large L, and a tolerance below
0.4||Y||_F^2 cannot be reached during this interval.

The constants are deliberately loose. The result leaves
L/(10000 log L) < m <= L/log L unresolved. It is not labeled a solution of
target 2. Its new range includes widths of order L/log L with a sufficiently
small fixed coefficient, and widths L/(log L)^p for fixed p>1; those widths
are not eventually bounded by L^(1-gamma) for any fixed gamma>0.

## Normalization and reused input

Write d_0=d_x, d_1=...=d_(L-1)=m, d_L=d_y and A_i=W_i/sqrt(d_i).
Then U=A_L...A_1 X exactly: the normalization beta in HXP is 1.
All norms on products below are operator norms. Empty products are identities.
Set

    q=L/m,  a=1/200,  b=3/1000,  K=L^2,  delta=exp(-b q).

The only probabilistic input reused from the published proof is its elementary
chi-square first-moment bound. For a fixed vector independent of a layer with
output dimension d,

    E ||A v|| / ||v|| = E sqrt(chi_d^2/d) <= 1-1/(10d).

This is the gamma-ratio estimate displayed in HXP Lemma 5.3, PDF page 7
(zero-based page 6), arXiv:2001.05992. Iterating conditional expectation,
since all d_i<=m, a product of k layers satisfies

    E ||A_(j:i)(0) v|| <= exp(-k/(10m)) ||v||.             (1)

The new argument below retains all dimension and depth factors instead of
absorbing them into exp(Omega(L^gamma)). No variable gamma is substituted
into HXP's published theorem.

## Initialization event, including its probability

For each block, E||A_(j:i)(0)||_F^2=d_(i-1)<=m. Markov followed by a union
over at most L^2 blocks gives

    Pr[some block has norm > K] <= L^2 m/K^2 <= 1/L.       (2)

For a block of length k with j-i>=L/10, use
||P|| <= ||P||_F <= sum_h ||P e_h|| and (1) to obtain

    E||P|| <= m exp(-q/100).

Consequently

    Pr[||P|| > exp(-a q)] <= m exp(-q/200).

Union over long blocks and use m<=L, q>=10000 log L:

    Pr[some long block violates this bound]
       <= L^3 exp(-q/200) <= L^(-47).                    (3)

Condition on the event E in which every block is bounded by K and every
block with j-i>=L/10 is bounded by exp(-a q). Equations (2),(3) give
Pr(E)>=1-1/L-L^(-47). No independence between block events is assumed.

## Deterministic neighborhood, with every polynomial retained

Suppose ||A_i-A_i(0)||<=delta for every i. Put Delta_i=A_i-A_i(0), and
z=L K delta. Since q>=10000 log L,

    delta<=L^(-30),      z<=L^(-27).

Expand each block as a sum indexed by the perturbed layers. A term with
s perturbations has s+1 unperturbed gaps, so its norm is at most
delta^s K^(s+1), including empty gaps. Thus every perturbed block obeys

    ||A_(j:i)|| <= K sum_(s>=0) z^s <= 2K.               (4)

Now let j-i>=L/4 and take L>=40. In a term with exactly one perturbation,
the two unperturbed gaps have total length at least L/4. One gap therefore
has length at least L/8, hence index difference at least L/10. That gap
has norm at most exp(-a q). Summing these terms costs at most

    L K delta exp(-a q) = z exp(-a q) <= exp(-a q).

All terms with s>=2 together cost at most

    K z^2/(1-z) <= 2 L^8 exp(-2b q)
                 <= exp(-a q),                         (5)

because (2b-a)q=q/1000>=10 log L and 2L^(-2)<=1.
The unperturbed term costs at most exp(-a q). Therefore

    ||A_(j:i)|| <= 3 exp(-a q) whenever j-i>=L/4.        (6)

This verifies the robustness step directly, rather than presuming a
uniform extension of HXP Lemma 5.4 at the logarithmic boundary.

## Loss and gradient inside this neighborhood

By (6), ||U||_F <= 3 exp(-a q)||X||_F. For sufficiently large L this is
at most ||Y||_F/20, because exp(-a q)<=L^(-50). Hence

    (0.95)^2 ||Y||_F^2/2 <= ell <= (1.05)^2 ||Y||_F^2/2,

which lies strictly inside the claimed [0.4,0.6] interval. In particular
||U-Y||_F<=1.05||Y||_F.

Differentiating with respect to the original W_i, not A_i, gives

    grad_(W_i) ell
       = d_i^(-1/2) A_(L:i+1)^T (U-Y) (A_(i-1:1)X)^T.

Of the two products flanking the residual, at least one has length at
least (L-1)/2, so (6) applies to it for all sufficiently large L. Bound
the other by (4); an empty product has norm 1<=2K. With

    G=7 ||X||_F ||Y||_F,

we obtain

    ||grad_(W_i) ell|| <= d_i^(-1/2) G K exp(-a q).

The update in A_i is divided by sqrt(d_i) once more. Thus

    ||A_i(t+1)-A_i(t)|| <= eta G K exp(-a q)/d_i
                         <= eta G K exp(-a q).          (7)

No hidden sqrt(m) factor or change of learning-rate convention is used.

## GD induction and the escape time

Let N=floor(exp(q/1000)). Assume inductively that all earlier iterates
remain within delta of initialization. Sum (7), using eta<=1:

    ||A_i(t)-A_i(0)||
       <= N G L^2 exp(-q/200)
       <= G L^2 exp(-q/250)
       = delta [G L^2 exp(-q/1000)]
       <= delta G L^(-8) <= delta/2,                    (8)

once L is large enough that G L^(-8)<=1/2. This is a strict improvement
of the inductive hypothesis, so induction establishes it for all t<=N.
The loss interval therefore holds for all those iterates. Together with
(2),(3), this proves the statement.

The lower bound is conditional on the explicit nonzero-data/tolerance
assumptions, as in HXP's plateau statement. Zero targets or tolerances
already above the initial plateau do not satisfy this conclusion.

## Checks and remaining work

The numerical companion checks the exponent bookkeeping and the exact
rank-one product formula for C002. It is not evidence replacing (1)-(8).
No width/depth simulation from the settled target 3 was repeated.

The remaining strip has q between about log L and 10000 log L. The proof
above gives no result there. A genuinely better robustness argument, with
appropriate initialization information, is needed to cover that strip.

Source locators: HXP https://arxiv.org/pdf/2001.05992, Section 5.1 and
Appendix B (PDF pp. 6-8,16); Du-Hu https://arxiv.org/pdf/1901.08572,
Theorem 4.1. These papers supply the setting and the indicated reused
moment bound; the explicit interval and constants above are this claim.
