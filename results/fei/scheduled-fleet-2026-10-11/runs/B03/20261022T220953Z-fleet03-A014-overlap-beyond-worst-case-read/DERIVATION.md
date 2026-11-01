# Non-separating row transport with the complete inherited reference

All logarithms are base two. No bound on maximum read or separator hypothesis is used.

Let C(x,y) be any indicator on a finite uniform cube, s=E C in (0,1), f=1-2C,
v=Var(f)=4s(1-s). Write c_b(T) for the normalized Walsh coefficients of C(b,y),
b in {0,1}. Thus c_b(0)=a_b=E C(b,y), and a_0+a_1=2s. The bit label is
arbitrary; neither nesting nor disjoint private supports is needed.

Define the probability law on (T,xi)

    R(T,xi) = [c_0(T)^2+c_1(T)^2]/(4s).

Parseval gives sum R=1. Its empty atom is

    r = (a_0^2+a_1^2)/(4s),          s/2 <= r <= 1/2.                 (1)

The actual normalized blocker spectrum is

    P_C(T,xi) = [c_0(T)+(-1)^xi c_1(T)]^2/(4s) <= 2R(T,xi).        (2)

Here (1) uses (a_0-a_1)^2>=0 and a_b^2<=a_b. Equation (2) is equivalent
to (c_0(T)-(-1)^xi c_1(T))^2>=0. Shared variables do not affect either step.

Condition both laws on the nonempty Fourier set. Put

    P=P_C(.|nonempty),  R*=R(.|nonempty),
    L=2(1-r)/(1-s).

Then 1/(1-s)<=L<=(2-s)/(1-s), so L>1, and P<=L R*. P is also the output spectrum of f
conditioned nonempty: p_f(A)/v=P(A) for nonempty A.

Fix ANY probability q on nonempty sets, strictly positive on the support of R*.
The reference is fixed before the comparison; it is not chosen by the sampled set.
Set S=(LR*-P)/(L-1), a nonnegative probability law. With alpha=1/L,
R*=alpha P+(1-alpha)S. Expanding each KL term, including zeros with 0 log 0=0,
gives the exact identity

 D(P||q) = L D(R*||q) -(L-1)D(S||q) + L JS_alpha(P,S).            (3)

JS_alpha(P,S) is the mutual information of a Bernoulli-alpha mixture label
and its sample, so 0<=JS_alpha<=h2(alpha). This also follows by the classical
KL chain rule and the nonnegative conditional entropy of that label. Since
D(S||q)>=0 (Jensen applied to -log, or the log-sum inequality),

    D(P||q) <= L D(R*||q)+L h2(1/L).                             (4)

For a complete occupation subprobability M(A)>0 on nonempty sets, let
Z=sum M in (0,1] and q(A)=M(A)/Z. The full output reference is
Q(empty)=1-v and Q(A)=v q(A), including Q(empty)=0 if v=1. Constants s=0,1
instead use the empty point mass. Its complete excess, with the output's
actual empty mass fixed, is

 CE(p_f,Q)-H(f) = v D(P||q)
              <=8s(1-r)D(R*||q)+v L h2(1/L).                    (5)

This keeps the normalizer: CE(p_f,Q)=h2(v)+sum_{A!=empty}p_f(A)log(1/M(A))
+v log Z. In particular the signed log Z term and every row/reference debt
remain. Formula (3) also keeps the possible negative complementary debt.

The additive term in (5) is paid by the SAME physical total influence:

    v L h2(1/L) <= (3+log2(e)) I(f) < (9/2) I(f).                (6)

Proof: put t=1-s. For every L>1,
L h2(1/L)=log L+(L-1)log(1+1/(L-1)) <=log L+log e.
Since L<=2/t, the left side of (6) is at most
v[1+log e+log(1/t)]. Poincare gives v<=I(f). Edge isoperimetry for the
indicator 1-C gives I(f)>=2t log(1/t). Therefore v log(1/t)<=2s I(f)<=2I(f),
proving the non-strict bound. log2(e)<3/2 follows from ln 2>2/3: expanding
ln 2=2[1/3+(1/3)^3/3+...] has strictly positive remaining terms.

For completeness, the edge inequality needs no external theorem: induct on
dimension for an indicator of mean t. If the child means are a>=b and m=a+b,
the queried coordinate influence is at least a-b. The child induction bounds
the other influence by a log(1/a)+b log(1/b). Their sum minus
m log(2/m) is m[h2(a/m)+2a/m-2]>=0, by the chord bound
h2(p)>=2(1-p) on [1/2,1]. The empty m=0 and constant-dimensional base are
immediate. This proof also handles nonnested rows. Poincare follows directly
from sum_{A!=empty}p_f(A)<=sum_A |A|p_f(A).

Checks that can fail: normalization uses s>0; conditioning uses s<1 and r<1;
division by L-1 uses L>1; all reference atoms must cover R*, not merely P;
the two rows must be Walsh-transformed on the SAME remaining cube; and the
occupation mass must be normalized by its own full nonempty Z. All these
conditions are explicitly checked on the finite graph domain. Constant and
zero rows are allowed. Constant outputs are handled separately.

This is a proof with exact finite checks, pending independent review. The Lean
attempt on the scalar square inequality was held by compute admission before
compilation; the result is not Lean-checked. No claim of novelty is made for
the classical mixture identity (3).

## First unpaid line

For a useful prescribed occupation reference, establish
8s(1-r)D(R*||q), together with all inherited terminal costs, <=K times the
genuinely UNUSED part of the original influence bank. Formula (5) alone cannot
be iterated with fresh 9I/2 allowances at every node. It bounds conversion,
not the construction cost of the reference. Neither full FEI nor an arbitrary
linear-hypergraph FEI bound follows here.

## A relevant-query obstruction to carrying row KL at coefficient one

The factor multiplying inherited KL is necessary for arbitrary complete
references, even for a graph blocker with a relevant query and nested rows.
Take the independent-set blocker of the triangle, with all three bits uniform,
and query x. Its two row means are 3/4 and 1/4. Thus s=1/2, r=5/16,
v=1, I(f)=3/2, and L=11/4. The true nonempty output spectrum P has four
atoms of mass 1/4 (the three singletons and the triple); R* has mass 5/11
at {x} and mass 1/11 at the six other nonempty sets. In particular, at
A={y}, P(A)=1/4 and R*(A)=1/11, so the domination coefficient L is attained.

For epsilon in (0,1), define a complete, fixed reference by
q_epsilon(A)=epsilon and q_epsilon(B)=(1-epsilon)R*(B)/(10/11) for B!=A.
All atoms are positive. Expanding the finite KL sums gives

 D(P||q_epsilon)=(1/4)log(1/epsilon)+O(1),
 D(R*||q_epsilon)=(1/11)log(1/epsilon)+O(1), as epsilon decreases to zero.

The O(1) remainders are bounded on 0<epsilon<=1/2: the remaining fixed
atoms only contribute constants and multiples of log(1/(1-epsilon))<=1.
Consequently, for ANY c<11/4 and ANY finite K, some epsilon has
D(P||q_epsilon)>c D(R*||q_epsilon)+K I(f). Every Boolean side condition
is preserved, and the query influence is 1/2. This refutes an arbitrary-reference
coefficient-one transport repair. It does not refute the frozen occupation
reference or FEI, and says nothing about whether a specially constructed
occupation q can pay its debt from unused influence.
