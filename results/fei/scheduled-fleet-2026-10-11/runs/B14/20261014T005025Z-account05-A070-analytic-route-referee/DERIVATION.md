# Independent mask-refund audit

## 1. Source theorem reconstruction

Fix a singleton-leaf tree, internal cells C and arities b_C. Let L(S)=1+sum_C b_C 1{S meets C}, Gamma(u)=sum uhat(S)^2 L(S). For a Boolean sign u write W(u)=Gamma(u)-1. Conditional expectation P_C removes precisely the Fourier sets meeting C. Consequently E Var(u|outside C)=sum_{S meets C} uhat(S)^2. Independent conditional copies of a sign disagree with probability one half of that variance, giving W(u)=2 sum_C b_C P(D_C(u)). This includes constant signs and the empty Fourier atom.

Boolean multiplication makes disagreement XOR, pointwise on each resampling pair. For two signs, D(uw)=D(u)+D(w)-2D(u)D(w). Hence W(uw)=W(u)+W(w)-R_T(u,w), R_T=4 sum_C b_C P(D(u)D(w)). For three signs the sum of three disagreement bits minus their parity is twice the indicator of at least two bits. This proves the simultaneous R3 identity. The events {D(q1)=D(q2)=1} and {D(g)=D(q1q2)=1} are disjoint and their union is the simultaneous refund event. Thus no projected Fourier cross term has been dropped.

For a codimension-k subcube A of density rho, its sign mask has coefficient update -2rho chi_S(a) on subsets of the fixed coordinates. Summing its squared coefficients over sets meeting E gives 4rho(1-2^{-|E intersect fixed|}). A binary tree joining Y,(C,(U,V)) has at most three joins occupied by either compatible mask and r+s-2 (or r+t-2) occupied block-internal cells. Thus W(q1)<=8rho1(r+s+1)<=6I(q1), and likewise q2, using I(q1)=2(r+s)rho1 and r+s>=2.

With c=2^-r,a=2^-s,b=2^-t, exclusive-coordinate pivots are 2c(sa+tb), common-coordinate pivots are 2cr(a+b-2ab). Therefore I(q)=2c[sa+tb+r(a+b-2ab)], whereas the input sum has common term 2cr(a+b). As a,b<=1/2, 2ab<=(a+b)/2; the input sum is at most twice I(q). Subadditivity gives Gamma(gq)<=Gamma(g)+12I(q) for arbitrary Boolean g. It retains Gamma(g) unchanged. For g=h(Y), Gamma_T(g)=Gamma_Y(h)+2Var(h), I(gq)=I(h)+I(q), and Var(h)<=I(h). A paid core code Gamma_Y(h)<=K I(h) gives max(K+2,12) final payment. Constants do not satisfy this root-bit paid-code hypothesis and are not silently admitted.

Verdict: A069-BOOLEAN-MASK-REFUND@1 HOLDS at the exact stated scope, without repair. Its earlier complete decoder is the independently accepted A069-STABLE-HIERARCHY-EDIT-PAYMENT@1; no entropy subadditivity for overlapping products is asserted.

## 2. Indispensable Boolean hypothesis: a normalized real obstruction

On two bits use the root tree L(empty)=1,L(nonempty)=3 and u=(12+5x1)/13. E u^2=1 and W(u)=50/169. Squaring and renormalizing gives v=u^2/||u^2||_2=(169+120x1)/sqrt(42961), also norm one. W(v)=28800/42961 > 100/169 =2W(u), because 28800*169-100*42961=571100>0. Thus even the subadditive inequality fails for products renormalized to have unit L2 norm. This is a genuine normalized-real spectrum control, not a Boolean counterexample. The first invalid real-extension step is E Var(u|outside C)=2P(u(X)!=u(X^C)); XOR of sign disagreements also ceases to describe real multiplication. Norm-one Parseval alone cannot provide either step.

The earlier degree-one singleton control remains H=log2 n and spectral influence 1; the current theorem does not claim its code cost is bounded by influence. No unrecovered historical cyclic-law certificate is used or claimed replayed.

## 3. Exact conversion ledger and retained-core obstruction

For Boolean g,q let R_I(g,q)=2 sum_i P(g differs on the i-edge AND q differs on that edge). Physical XOR gives I(gq)=I(g)+I(q)-R_I. Combine this with the proved cost refund: for any K,

    K I(gq)-Gamma(gq)
      = [K I(g)-Gamma(g)] + [K I(q)-W(q)]
        + R_T(g,q)-K R_I(g,q).

This is an accounting identity, not a new payment. A mask bank K I(q)-W(q)>=0 does not make the final conversion term nonnegative.

Explicit nonconstant-core compatible-overlap witness: four coordinates c,u,v,y; common and exclusive blocks have one bit each. Events are A={c=+,u=+}, B={c=+,v=+}; q=(1-c)/2+(1+c)uv/2. Tree T=(y,(c,(u,v))) has binary cells all four, {c,u,v}, {u,v}. Put g=q*y and f=gq=y. Direct Fourier coefficients give I(q)=3/2, I(g)=5/2, I(f)=1; W(q)=4, Gamma(g)=11/2, Gamma(f)=3, R_T=13/2 and R_I=3. At K=12, R_T-K R_I=-59/2. Nevertheless the complete banks are 49/2,14,-59/2, summing to 9=12I(f)-Gamma(f). The source slack and mask bank cannot be discarded and the complete final core y remains present. This refutes only the proposed shortcut R_T>=12R_I, not A069's theorem or FEI.

First unsupported universal line: prove nonnegative total source-slack plus mask-bank plus signed conversion on a selected source-compatible reference while paying every actual conditional core terminal once. The resampling refund is not physical restriction-tree ownership. Unequal conditional core references require a specified common output reference; independently choosing references for the two branches cannot be inserted into this fixed-tree identity.
