# Root audit of the strengthened LTF and composition theorem

2 October 2026. I read the complete longer candidate and both independent
audits, and independently reconstructed the shorter argument below.
Analytic verdict: PASS, conditional on the completed largest-weight LTF
split theorem. Historical novelty and external peer review remain unverified.

For a split unate in its chosen coordinate, normalize its direction so
f=A+zB with B in {0,1}, A in {-1,0,1}, A^2+B^2=1. Put alpha=E B and
delta=1-alpha. The exact split identity bounds the entropy increment by
twice the conditional spectral component-bit entropy C.

When alpha>1/2, the empty pair has mass at least alpha^2, while |E A|<=delta.
Thus the nonempty pairs contribute at most 1-alpha^2<=2delta to C. At the
empty pair put x=(E A)^2<=delta^2, y=alpha^2. Since x+y<=1,

    x log2((x+y)/x)+y log2((x+y)/y)
       <=x log2(1/x)+x log2 e
       <=2delta^2 log2(1/delta)+delta^2 log2 e.

Here x log(1/x) increases up to 1/e, and delta^2<1/4<1/e. For zero x
the inequality is interpreted by continuity. Dividing this last upper bound
by delta and using delta log2(1/delta)<=log2(e)/e and delta<=1/2 gives

    Delta H <= [4+4log2(e)/e+log2(e)] delta <8delta.

This is a lemma for every unate split, without any threshold geometry in
the remaining coordinates. If alpha=1, f=z exactly; if alpha=0 the split
increment is zero. There is no missing zero-degree entropy atom.

For an LTF's largest defining weight, combine this with the already proved
Delta H<=C_* alpha. With K=max(C_*,8), in both alpha regimes

    Delta H <=2K alpha(1-alpha).

The restricted means are E A plus/minus alpha, so the exact variance
decrement is alpha^2. The exact influence decrement is alpha. Therefore
the potential I-Var has decrement alpha(1-alpha). Constants have zero
potential and entropy, and restrictions remain LTFs. Dimension induction
proves H(f)<=2K[I(f)-Var(f)] for every uniform-cube LTF. Input and output
sign changes preserve all relevant quantities. The Fourier expression
I-Var=sum_(S nonempty)(|S|-1) fhat(S)^2 checks its nonnegativity and the
dictator endpoint.

For disjoint balanced children f_i, the selected child spectral sets are
nonempty, so their occupied blocks recover the outer Fourier set uniquely.
There is no coefficient collision. Thus for F=g(f_1,...,f_m), exactly,

    H(F)=H(g)+sum_i I_i(g)H(f_i),
    I(F)=sum_i I_i(g)I(f_i), Var(F)=Var(g).

The child outputs are independent uniform signs, hence Var(f_i)=1 and
the parent gate uses its uniform-input Fourier coefficients. If all gates
and children satisfy the strong bound with constant C, its right-hand side
telescopes to

    C[I(g)-Var(g)+sum_i I_i(g)(I(f_i)-1)]
       =C[I(F)-Var(F)].

This proves the same constant for arbitrary-depth read-once LTF-gate
formulas with balanced nonroot outputs and mutually disjoint leaf blocks.
The root may be biased. Balanced leaves have H=0 and I=Var=1. The argument
does not extend to shared-input circuits or unbalanced children as stated.

I also checked the longer complementary KL route: the signed rare A
component has squared mass delta and empty normalized atom at most delta;
hypercontractivity uses its L_(3/2) norm, not indicator positivity. The
pair tail is the sum of the two rare halfspace tails with the factor1/4
from indicator normalization. The generalized dyadic zero-atom inequality
has the correct direction. This provides an independent corroborating
route, although the elementary unate lemma makes those extra inputs
unnecessary for the strengthened theorem.
