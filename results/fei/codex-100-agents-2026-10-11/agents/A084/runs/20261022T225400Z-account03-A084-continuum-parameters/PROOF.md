# Heterogeneous second-query curvature, including a vanishing-pivot boundary

Units: bits. An index bit1 denotes a negative input. Gate h is negative on {0,1,2,4,8,16,32,6,17,40}; J(x)=-h(x xor1). Initially F=k(g_0,...,g_5), k in{h,J}, has six disjoint identical nonconstant Boolean cores with negative probability 0<p<=1/16. Reveal any physical coordinate in block k0 and retain EITHER actual child. Its negative probability t belongs to[0,2p]. Then query any remaining physical coordinate in block j. The latter query has core influence d and full influence q_j d. This statement is dimension independent and covers every real attainable bias and singleton shift.

## Statement and full retained account

For heterogeneous biases p_l define q_l as the true outer pivotal probabilities and

    C=H(P_occupied)-sum_l q_l h2(4p_l(1-p_l)).
    H(F)=sum_l q_l H(g_l)+C; I(F)=sum_l q_l I(g_l).

Write Delta C=C_parent-mean C_children using the two true weights1/2. The following entries B satisfy Delta C<=B q_j d:

| second query | h | J directions1,2,3,5 | J direction0 | J direction4 |
| --- | --- | --- | --- | --- |
| different block j!=k0 | 3/4 | 1/8 | 3/4 | 5/4 |
| same block j=k0 | 5/4 | 3/4 | 7/4 | 11/4 |

For J, k0=0,j=4, the distinct-block price is more sharply35/32. Thus all different-block queries cost at most5/4 and every second query costs at most11/4. These are signed upper bounds, not absolute values. The t=0 face, irrelevant coordinates, and constant subsequent children are included. No history of length greater than two is claimed. The first-query theorem@1 and its finer constants remain unchanged.

The exact physical identity is

    Delta H(F)=q_j Delta H(g_j)+Delta C.                  (1)

Other cores' q_l average to their parent values; all their COMPLETE entropy terms cancel only in that average, rather than being dropped. For rate K and inherited debit D, the outgoing mean debit is still D+Delta H(F)-K q_j d. Neither D nor the first-query bill is reset. The theorem pays only the additional composition correction, not the arbitrary-core term in(1).

## Directional curvature, derived with the other laws fixed

Write k=A+y_j D, and let a_T,d_T be the normalized biased coefficients on the other five inputs. At a deterministic other input, remove that input and use the basis on its actual support; equivalently the polynomial mass formulas discard every factor of zero variance. No division by that variance is used. Put q=sum d_T^2. For selected mean x, expanding the two kinds of occupied mass and subtracting q h2(1-x^2) cancels the entire (1-x^2)log(1-x^2) term BEFORE differentiation. Other q_l terms are affine. The remaining function is

    C_j(x)=sum_T ell((a_T+xd_T)^2)
           +(1-x^2)sum_T ell(d_T^2)+q x^2 log2(x^2),
    ell(z)=-z log2 z, ell(0)=0.

Differentiation cancels all constant derivative terms and gives

    C_j''(x)=-2L_j(x),
    L_j(x)=sum_(d_T!=0) d_T^2 log2((a_T+xd_T)^2/(x^2 d_T^2)).

At an isolated numerator zero, ell of a squared affine function is C1 and has a locally integrable logarithmic second derivative. Identical vanishing on an interval with d_T!=0 is impossible. There are finitely many terms. Thus the derivative formula extends by improper integration without losing a positive boundary charge. If m is the selected core mean and b=abs(beta) its actual singleton coefficient, the Green identity is

    Delta C=integral_(-b)^b (b-abs(u)) L_j(m+u) du.       (2)

The nonnegative kernel has mass b^2. Jensen with weights d_T^2/q and Parseval imply, for q>0 and abs(x)>=ell>0,

    L_j(x)<=q log2(1+(1-q)/(ell^2 q)).                 (3)

In deriving this, the norm on active d_T packets is bounded by the full norm sum(a_T+xd_T)^2=1-(1-x^2)q. For a core with negative probability s, Booleanity gives abs(beta)<=d and abs(beta)<=2s, so beta^2/d<=2s when d>0 and the entire child-mean interval lies above1-4s. If d=0 or beta=0, Delta C=0. If q=0 the selected gate input is irrelevant on the support of the other laws and Delta C=0, with no division. Constant selected-child means1 are harmless because cancellation preceded differentiation.

## Different-block query: ordinary directions

Here s=p, ell>=3/4, and beta^2/d<=2p. A pivotal assignment with the previous block positive and r negatives among the remaining four unselected inputs has probability(1-t)p^r(1-p)^(4-r). Exhaustively inspecting the actual64-entry gate tables, with NO direction symmetry reduction, gives r=1 for all30 ordered distinct pairs of h. For J, r=0 for j in{1,2,3,5}, r=1 for j=0, and r=2 for j=4 except when k0=0. The60 witness rows, including that failure, are saved.

By monotonicity of positive factors and the exact endpoint inequalities in the code,

    r=0: q>=(1-2p)(1-p)^4>=2/3,
    r=1: q>=(1-2p)p(1-p)^3>=2p/3,
    r=2: q>=(1-2p)p^2(1-p)^2>=3p^2/4.

For r=0, the log argument in(3) is at most17/9<2, giving price<=2p<=1/8. For r=1 it is at most1+8/(3p)<=4/p, giving price<=2p[log2(1/p)+2]<=3/4. For r=2 it is at most1+64/(27p^2)<=4/p^2, giving price<=2p[2log2(1/p)+2]<=5/4. Every endpoint reduction is uniform on the FULL real interval: the derivative of p[r log2(1/p)+c] is r(log2(1/p)-log2(e))+c>0 since log2(1/p)>=4 and log2(e)<2. The envelopes vanish as p tends to zero.

## Exceptional vanishing pivot: failed premise and repair

For J,k0=0,j=4 no previous-positive pivotal witness exists: that section is independent of target4. The previous-negative section has a weight1 witness among the other four inputs. Consequently q=t q1, where q1>=p(1-p)^3>=3p/4. A t-independent positive lower bound on q is FALSE, and applying(3) alone leaves an unbounded log(1/t). The failed premise is retained in out/FAILED_UNIFORM_POSITIVE_WITNESS.json.

Let f0(z) be the previous-positive section, independent of selected y. Write the previous-negative section as A1(z)+yD1(z). On the four other inputs let their coefficient vectors be a0,a1,d1, and b1(x)=a1+xd1; q1=sum d1^2. The coefficient pairs on the previous variable are, up to common harmless signs,

    a+xd: ((1-t)a0+t b1(x), sqrt(t(1-t))(a0-b1(x))),
    d:    (t d1,             -sqrt(t(1-t))d1).

Since f0 and A1+xD1 are pointwise in[-1,1] for abs(x)<=1, Parseval gives norm-squared bounds1 and4 on(1-t)a0+t b1(x) and a0-b1(x), respectively. Apply Jensen SEPARATELY to the two groups, omitting zero d1 coefficients and bounding active norms by full norms. For0<t<=1/8,x>=ell=3/4,

    L/q <= t log2(1/(x^2 t^2 q1))
           +(1-t)log2(4/(x^2 q1))
         = log2(1/(x^2 q1))+2t log2(1/t)+2(1-t)
         <= log2(1/p)+2+3/4+2
         = log2(1/p)+19/4.

Here1/(ell^2 q1)<=64/(27p)<4/p, and t log2(1/t)<=3/8 on[0,1/8], by its derivative and continuity. Using(2), beta^2/d<=2p, and endpoint monotonicity proves

    Delta C/(q d)<=2p[log2(1/p)+19/4]<=35/32<5/4.

All used denominators are positive: p>0,q1>=3p/4,t>0,x>=3/4. At t=0 the selected gate input is irrelevant and both Delta C and qd vanish EXACTLY. Numerator zeros use the finite integrable-curvature argument above. Thus the missing face is analytically covered, not left to a grid.

## Same-block second query

The selected restricted core now has s=t<=2p and the other five laws are still p. For t>0, ell>=1-4t>=1-8p>=1/2 and beta^2/d<=4p. Equations(2)--(3) give price at most4p log2(4/q). For h the exact polynomial pivot formula is q=2p(1-p)^3(2-p)>=3p, so4/q<=2/p and the endpoint price is5/4. The lower bound follows from2(15/16)^3(31/16)>3. For J dominant directions q>=(1-p)^5>=1/2, giving price<=12p<=3/4. For J0, q>=p(1-p)^4>=3p/4; for J4, q>=p^2(1-p)^3>=3p^2/4. In these cases4/q<=8/p^r, so the endpoint prices are7/4 and11/4. The same derivative argument proves uniformity. At t=0 the selected core is constant, so no physical debt occurs.

## Independent saturation-account reconstruction, and what remains unpaid

For S=K I-H and e=Delta H-K Inf_query, exact influence telescoping gives mean S_child=S+e. An inherited debit D, with unused R=S-D, and outgoing debits satisfying mean d_child=D+e therefore satisfy

    mean(S_child-d_child)=R.                          (4)

This is a real algebraic identity, independent of bias and signs. If both child unused reserves are nonnegative and R=0, both reserves vanish. Inductively every positive-reach descendant of a saturated parent in such a continuation stays saturated. Positive components in a saturated child are expenditure, not a fresh donor. Positivity is necessary: reserves1 and-1 average0 without vanishing. Exact zero mean is necessary: reserves2 and0 do not vanish. Signed negative e is allowed.

The local engine independently reconstructs one actual A072 parent: J(g^6), g negative on{0,1,2} on6bits, block0 prefix original coordinates2=0,0=0,3=0; then both children for original block1 coordinate0. Direct character sums, integer FWHT, direct physical edges, rational occupied spectra and the exact profile equality agree. This accepts A072's accounting/saturation substatement ONLY; it does not accept all60 optimizer cases or general child eligibility. No source engine beyond the pinned logarithm helper is imported.

The repaired second-query correction bound does NOT imply a nonnegative remaining bank. The first unsupported universal line is paying q_j Delta H(g_j), after all old debits, from a genuinely unused source with both complete terminal entropies. Histories with several unrelated bias changes require a further argument; neither the one-special-variable grouping nor the constants here permit unlimited iteration. Full FEI remains OPEN. The result is an analytic proof with finite exact validation, pending independent review; a Lean attempt is recorded separately and cannot certify the Fourier argument unless its precise target actually passes.
