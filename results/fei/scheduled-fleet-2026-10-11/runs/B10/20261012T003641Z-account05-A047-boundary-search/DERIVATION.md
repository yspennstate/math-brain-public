# Exact sharp supremum for real children

Fix 0<p<1/2, b=arcsin(sqrt(p)), and phi(t)=h2(sin^2(t)). Set

    F_p(t)=phi(t)+phi(t-b), m_p=min_t F_p(t), tau_p=h2(p)-m_p.

The minimum exists by continuity and period pi/2. No evaluation or uniqueness of its minimizer is assumed.

For any two unit real child coefficient vectors G,H, write

    (sqrt(1-p)G_T,sqrt(p)H_T)=sqrt(q_T)(cos(t_T),sin(t_T)).

Then q_T=(1-p)G_T^2+pH_T^2 and sum q_T=1. Exact normalization also gives sum q_T sin^2(t_T)=p. The physical posterior entropy is sum q_T phi(t_T); the spectral selector conditional entropy is sum q_T phi(t_T-b). Thus

    J-M=h2(p)-sum_T q_T F_p(t_T).

Conversely any finite distribution (q_T,t_T) with those two normalization constraints defines two unit vectors by the displayed equation. Therefore the supremum over real children is h2(p) minus the lower convex envelope of the curve (sin^2(t),F_p(t)) evaluated at p.

The envelope value is EXACTLY m_p, not merely at least m_p. Choose any minimizer t0 and put x=sin^2(t0). Since F_p(0)=h2(p), m_p<=h2(p). Also F_p(t0)>=h2(x). If p<x<1-p then h2(x)>h2(p), a contradiction. Thus x<=p or x>=1-p. The symmetry t->t+pi/2 preserves F_p and complements x, so take a minimizing representative with x<=p. Its companion t1=t0+pi/2 has abscissa 1-x and the same minimum value. Mix the two with

    lambda=(1-x-p)/(1-2x), 1-lambda=(p-x)/(1-2x).

Because 0<=x<=p<1/2, these are nonnegative and sum to one, and their averaged abscissa is p. Their averaged ordinate is m_p. This proves the envelope assertion and exact real supremum tau_p. A two-label coefficient space suffices; equivalently real children on ONE uniform residual data bit attain it. Explicit coefficients are

    G=(sqrt(lambda)cos(t0),sqrt(1-lambda)cos(t1))/sqrt(1-p),
    H=(sqrt(lambda)sin(t0),sqrt(1-lambda)sin(t1))/sqrt(p).

They have norm one by the mixture identity. Their inverse Walsh transforms need not be sign-valued. This last distinction is the Boolean realizability obligation, not a defect in the real supremum theorem. For p>1/2 exchange the two physical children. The p=1/2 envelope case can be obtained directly: if a minimizing x differs from 1/2 the complementary pair mixes with weights 1/2; if x=1/2 the single minimizer already meets the constraint.

# Certified real witnesses without solving the trigonometric minimum

For any rational 0<=x<=p, take t=arcsin(sqrt(x)) and its orthogonal companion t+pi/2. The mixture above satisfies the normalization constraint exactly. The second measurement probability is

    y=sin^2(t-b)=p+(1-2p)x-2sqrt(p(1-p)x(1-x)).

Here 0<=y<=p<1/2. The attained real debt is

    h2(p)-h2(x)-h2(y).

Rational bisection encloses the sole square root. Since h2 is increasing on [0,1/2], endpoint evaluation encloses h2(y). This supplies a rigorous real lower bound. Comparison against the exhaustive Boolean upper bound proves a strict gap if its exact rational lower endpoint is positive. It does not evaluate m_p or prove a continuum minimizer formula.

# Finite Boolean supremum certificate

On uniform n-bit data, every Boolean child coefficient is an integer Walsh coefficient divided by N=2^n. For every ordered pair of sign tables and each frozen bias, compute the exact rational parent masses

    a=((1-p)G+pH)^2, b=p(1-p)(H-G)^2, q=a+b.

Let eta(s)=-s log2(s), eta(0)=0. The debt is the sum over residual labels of

    2eta(q)-eta(a)-eta(b)-(1-p)eta(G^2)-p eta(H^2).

The code certifies each distinct fiber value once, rounding outwards to the dyadic lattice 2^-100. Integer sums then enclose every pair debt. The maximum of lower endpoints and the maximum of upper endpoints enclose the supremum over the entire finite family. The stored witness attains at least the certified global lower endpoint; noncandidate separation is also exact. The final checker additionally expands every remaining candidate debt into a rational prime-log coefficient vector and verifies that all vectors equal the witness vector. All remaining candidates are therefore exact ties, and the finite supremum equals the exact witness expression. Equality of coefficient vectors is sufficient; no independence or converse statement about prime logarithms is used.

For x=2^k r with 1<=r<2, z=(r-1)/(r+1) lies in [0,1/3). The 40-term rational sum 2 sum_{j=0}^{39} z^(2j+1)/(2j+1) underestimates ln(r), with remainder at most 2z^81/(81(1-z^2)). The identical calculation for ln(2) has z=1/3 and positive denominator. Division of nonnegative intervals followed by the exact shift k gives log2(x) intervals without signed-denominator inversion. Negative entropy multiplication reverses endpoints before outward dyadic rounding. Cache reuse and integer aggregation change none of these inequalities.

First unsupported line: extending the small uniform-data Boolean supremum to all dimensions or variable residual biases. The exact real theorem pays no tree tax and supplies no Boolean realization of its minimizing coefficient vectors. Neither the finite census nor its strict real/Boolean gap proves a smaller tax for all Boolean children, or the C019 whole-tree payment.
