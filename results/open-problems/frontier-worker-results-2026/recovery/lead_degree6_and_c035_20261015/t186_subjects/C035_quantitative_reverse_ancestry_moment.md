# C035: quantitative reverse-ancestry moment and history trimming

Status: proof (unaudited), target3, kind bound. Exact rational substitutions
PASS; independent proof audit pending. No finite-graph transfer is claimed.

This quantifies the reverse causal-ancestry construction proposed by the
T186 lead in T186_REVERSE_ANCESTRY_ROUTE.md (15 October2026). The
construction is credited to that note. The argument below supplies
explicit constants using C034's drift witnesses; no novelty claim is made.

## Statement

Assume C009's stationary recursively conditioned Poisson tree with
interior terminal law pi, and its column-parent24-type matrix T. Suppose
there are rational h_i>=1 with h^T T<=h^T-1^T, and bounds

    max_i h_i<=H,  min_a pi_a>=q>0,  c<=C,  H>=1, C>=1.

Let mu_(a,b,d)=pi_a*pi_d for 0<=b<a<=3, and let W_i count all reverse
potential causal paths from type i, with their multiplicities, including
the root. Different lowered values at one physical neighbor can share
the same subtree; independence of those copies is NOT assumed. Set

    eta = q^2/[108 H(C^2+C)],       p=1+eta.

Then

    sum_i mu_i E[W_i^p] <= 12H^2.                         (1)

For the common augmented top-process history refinements of C022, let
mu_t(A,a,b,D)=Q_t(A)Q_t(D), with terminal(A)=a>b and Q_t(A)Q_t(D)>0.
Let r_t be the conditional expected reverse path count given those two
baseline histories. Then, uniformly over history length t,

    sum_i mu_t(i) r_t(i)^p <= 12H^2,                     (2)
    sum_i mu_t(i) r_t(i) 1{r_t(i)>L} <= 12H^2/L^eta.      (3)

The canonical right weights v_t=mu_t*r_t solve
B_t v_t=v_t-mu_t. The product is componentwise. The constants use the
minimum TERMINAL probability q, not the minimum refined-history mass.

## Actual reverse process and its marginal continuation laws

A reverse parent i=(a,b,d) starts with an outgoing potential change a->b
and a fixed incoming reverse boundary d. Sample its other incoming
subtrees conditional on M(N)=a, where N has independent Poisson(c*pi_u)
counts. For each occurrence with label u and each lower value v<u that
makes M(N-e_u+e_v)=b, list an ancestor j=(u,v,z), where
z=M(N-e_u+e_d). Continue in that occurrence's descendant subtree, with
reverse boundary z. This counts paths, even when several v choices use
one subtree. It never treats such copies as independent trees.

Poisson Palm removal gives

 R[j,i] = c*pi_u/pi_a *
   Pr(M(N+e_u)=a, M(N+e_v)=b, M(N+e_d)=z).

Comparison with the displayed C009 T entry proves
R=D_mu T^transpose D_mu^-1. Condition on the complete first-generation
label list including occurrence identities and the root boundary.
Selection of an occurrence, every candidate v, the new reverse boundary
z, and the number K_i of listed ancestors are then fixed. These data
inspect that occurrence's subtree only through its original output u.
The new boundary z uses the OTHER occurrences and d. Its continuation
therefore has the stationary conditional type-j marginal law. Sibling
and duplicate-copy independence is not required to take expectations
of sums of these continuations, even after multiplication by a function
of the known local K_i.

## A quantitative fractional moment

Each physical occurrence supplies at most3 lower values, so K_i<=3N_i.
Conditional on M(N)=a, this gives

 E K_i <=3c/pi_a,       E K_i^2 <=9(c^2+c)/pi_a.

These follow by dividing unconditional Poisson moment bounds by pi_a.
Let K_ji count type-j ancestors, and define

 R_eta[j,i]=E[(1+K_i)^eta K_ji | type i],
 B[j,i]=E[K_i K_ji | type i].

Here B is only an auxiliary moment matrix, distinct from the history
offspring matrix B_t. Since 0<eta<=1, concavity of x^eta on [1,infinity)
gives (1+K)^eta<=1+eta K. Thus R_eta<=R+eta B.

Put g=D_mu h. The original drift gives Rg<=g-mu. For any row j,

 (Bg)_j <=9(C^2+C) sum_i mu_i h_i/pi_(a_i)
        <=54H(C^2+C).

The last inequality uses the six pairs a>b and sum_d pi_d=1. Therefore
eta(Bg)_j<=q^2/2<=mu_j/2, and

 R_eta g <=g-mu/2 <=(1-1/(2H))g.                        (4)

Also b_i=E(1+K_i)^eta<=1+3eta C/q<=2; indeed
3eta C/q=q/[36H(C+1)]<=1. No numerical real-power evaluation is used.

Let W_i^(r) be reverse path count to depth r on the actual shared tree,
and m_r(i)=E[(W_i^(r))^p]. Convexity of x^p gives pointwise

 (1+sum_children X)^p
 <=(1+K)^(p-1) [1+sum_children X^p].

The conditional marginal law established above yields
m_(r+1)<=b+R_eta^transpose m_r. Multiply by g and use (4). As
sum_i mu_i=sum_a a*pi_a<=3 and g_i=mu_i h_i,

 g^T m_(r+1) <=6H+(1-1/(2H))g^T m_r.

Initially m_0=1 and g^T m_0<=3H. Induction gives
g^T m_r<=12H^2 for every r. Monotone convergence proves (1), since
g>=mu. In particular every W_i is finite almost surely. This argument
allows all dependencies caused by shared continuation subtrees.

## Common histories and canonical right densities

Use the actual finite top-process trace together with its limiting
terminal message on one stationary tree. The root outgoing history A
and its opposite cavity boundary history D come from independent cavity
trees before conditioning, with joint mass Q_t(A)Q_t(D). The terminal
reverse path multiset uses A and D only through their limiting terminal
values and the same descendant tree. Conditional Jensen and summation
over these histories give

 sum_(A,b,D) Q_t(A)Q_t(D) E[W|A,D]^p
 <= sum_(a,b,d) pi_a*pi_d E[W_(a,b,d)^p].

This proves (2) with a bound independent of t. Choosing an unrelated
stationary law separately for each t would not justify this comparison.
At each fixed t, condition on complete local histories for the reverse
Palm construction, as in C022. A selected subtree is seen only through
its outgoing history; its new reverse history is computed outside it.
The reverse history mean is consequently
R_t=D_(mu_t) B_t^transpose D_(mu_t)^-1. The root decomposition of total
path expectation gives R_t^transpose r_t=r_t-1, hence
B_t(mu_t*r_t)=mu_t*r_t-mu_t. Finite moments ensure all terms are finite;
C022's rho(B_t)<1 identifies the right resolvent uniquely. Finally
r*1{r>L}<=r^(1+eta)/L^eta proves (3).

## Scope

The stationary conditional subtree laws and common augmented histories
are essential. These weights are latent conditional expectations, not
predictable observations in a finite graph. Neither their uniform
moment nor their tail bound proves relative class depletion or a sparse
budget for genuine two-coordinate hits. They therefore do not establish
a new circumference cutoff or finite giant strong-core threshold.

## Exact numerical substitutions

At k4 c=11, C034 gives H=91 and q=1/1024. Therefore eta=1/1360313450496 and the weighted moment bound is99372. At c=12, H=89 and q=1/2048 give eta=1/6289241407488 and bound95052. These exponents are deliberately crude and extremely close to zero. They are not useful practical cutoff estimates without further improvements.

The exact Fraction substitutions and coefficient checks are in logs/t3_reverse_moment_constants.json, from scripts/target3_reverse_moment_constants.py. The recorded contraction181/182 or177/178 concerns R_eta, the reverse moment matrix, NOT the red/blue component kernel of C006. No ordinary floating-point arithmetic or numerical evaluation of real powers is used.
