# A059: new gate charges telescope; whole-subformula charges do not

All entropies in this proof are in nats, unless bits are explicitly stated.
For balanced Boolean h define

    delta(h)=I(h)-1,
    W1(h)=sum_i hat h({i})^2,
    Lambda(h)=sum_i hat h({i})^2 ln(1/hat h({i})^2).

Zero summands are zero. A balanced composition tree means a finite rooted tree
of Boolean gates on independent balanced child outputs, with disjoint physical
child blocks. Every node function, including every gate, is balanced. Literal
leaves are permitted. More generally a stopping frontier may consist of arbitrary
balanced Boolean functions on disjoint blocks. No bound on depth or arity is used.
For a node v, J(v) is the product of the gate coordinate influences on the path
from the root to v; J(root)=1. Sub_v is the actual entire function below v.

## 1. A local deficit inequality, independently reconstructed

For every balanced Boolean h,

    Lambda(h) <= K delta(h),       K=4+6/e.

Proof. If all singleton coefficients vanish the result is immediate. Otherwise
choose i with a=|hat h({i})| maximal; put u=1-a and
s=sum_{j != i} Inf_j(h), delta=I(h)-1. The Boolean half-derivative gives
|hat h({j})| <= Inf_j(h), hence delta >= s-u. Also balanced Parseval gives
delta >= 1-W1(h). Maximality of a implies

    W1(h) <= a^2 + a sum_{j != i}|hat h({j})| <= a^2+a s,
    delta >= u(2-u)-(1-u)s.

Substitute s<=delta+u in the second inequality to get
delta(2-u)>=u, thus u<=2delta and s<=3delta. Since
-a ln a <= 1-a, the chosen coordinate contributes at most 2u<=4delta.
For all 0<=b<=1, b^2 ln(1/b^2)<= (2/e)b (maximize b ln(1/b)).
The other coordinates contribute at most (2/e)s<=6delta/e. Endpoints
a=1 and delta=0 are included. This proof is independent of the lead's derivation,
but the statement and the choice of inequalities were supplied by B12 lead notes v1.

## 2. Deficit stopping theorem and exact first-charge factorization

At each internal node v let g_v be its gate, q_{v,i}=Inf_i(g_v),
and alpha_{v,i}=hat g_v({i}). Balanced disjoint substitution gives

    delta(Sub_v)=delta(g_v)+sum_i q_{v,i} delta(Sub_{vi}).

Therefore for ANY finite stopping frontier L,

    delta(F)=sum_{v internal} J(v)delta(g_v)
             +sum_{l in L} J(l)delta(Sub_l).                    (1)

In particular,

    sum_{v internal} J(v)Lambda(g_v)
        <= K[delta(F)-sum_l J(l)delta(Sub_l)] <= K delta(F).    (2)

This sum charges local GATES, not entire Sub_v. Arbitrary depth causes no
loss. Each term in (1) is nonnegative; for a fixed finite F, refining stopping
frontiers gives monotone charge sums bounded by delta(F). For a sequence of
different roots F_d, (1)-(2) hold for each d. No Fourier limit on an infinite
cube or cross-dimensional interchange is asserted.

There is also an exact factorization of the root singleton logarithm.
Put A(v)=product_{edges above v} alpha_edge^2. Then

    Lambda(F) = sum_{v internal} A(v) sum_i
           alpha_{v,i}^2 ln(1/alpha_{v,i}^2) W1(Sub_{vi})
       + sum_{l in L} A(l)Lambda(Sub_l).                       (3)

To prove (3), a physical singleton coefficient below child i is
alpha_{v,i} times its singleton coefficient in that child. Balancedness ensures
that no other outer sector contributes to that singleton. Expand the logarithm
of this product along its unique path and sum the squared coefficients. The
sum of descendant singleton squares below edge vi is W1(Sub_{vi}). For zero
coefficients take the zero convention or continuity. This proves (3), including
all endpoint/irrelevant-edge cases, without an incoherent mixture approximation.
Since W1<=1, alpha_edge^2<=|alpha_edge|<=q_edge, and A(v)<=J(v), (3) yields

    Lambda(F) <= sum_v J(v)Lambda(g_v)+sum_l J(l)Lambda(Sub_l).

Together with the local deficit inequality this is a complete first-charge
allocation: a logarithm introduced at an edge is charged once. The terminal
cost is present. The gate sum in (2) is the useful compositional statement;
Lambda(F)<=K delta(F) alone is already the local inequality applied to F.

If gate erasures satisfy B(g_v)<=K_B delta(g_v), their LOCAL bank
sum_v J(v)B(g_v) obeys the analogous bound by (1). This does NOT identify
that bank with a physical-query remainder bank using biased descendant
representations. That identification is the remaining C019 transport problem.

## 3. Exact counterfamily to whole-subformula charging

For r>=1 let A_r(z) be the all-+1 event on r fresh sign bits, p=2^-r,
and define the balanced gate

    G_r(x,y,z)=(1-A_r(z))x+A_r(z)y.

Its child outputs x,y,z_1,...,z_r are balanced. The actual Fourier coefficients
are: singleton x: 1-p; singleton y: p; all other x-containing control sectors:
-p; all other y-containing control sectors: p. In particular

    Inf_x=1-p, Inf_y=p, Inf_{z_i}=p,
    I(G_r)=1+rp, delta(G_r)=rp,
    Lambda(G_r)=(1-p)^2 ln(1/(1-p)^2)+p^2 ln(1/p^2).

Let F_0=x_0 and F_t=G_r(F_{t-1},y_t,z_t), with fresh y_t and r fresh controls
at each t. This is an actual Boolean balanced read-once tree. Direct influence
conservation and singleton multiplication give

    I(F_t)=1+r[1-(1-p)^t],
    hat F_t({x_0})=(1-p)^t,
    hat F_t({y_s})=p(1-p)^(t-s), 1<=s<=t,
    all control singleton coefficients =0.                    (4)

The continuation node F_t has J(F_t)=(1-p)^(d-t) in F_d. The putative bank
sum over nonroot child nodes J(c)Lambda(Sub_c) is at least

    S_d=sum_{t=1}^{d-1}(1-p)^(d-t)Lambda(F_t).

From just the x_0 singleton, -ln(1-p)>=p yields

    Lambda(F_t)>=2tp(1-p)^(2t),
    S_d>=p d(d-1)(1-p)^(2d).                                 (5)

Set d=2^(2k), r=3k, p=2^(-3k), k>=2. Bernoulli's inequality gives
(1-p)^(2d)>=1-2dp=1-2^(1-k)>=1/2. Also

    I(F_d)<=1+3k 2^-k <=5/2,
    S_d>= (1/2) 2^k (1-2^(-2k)),
    S_d/I(F_d)>= (1/5)2^k(1-2^(-2k)) -> infinity.             (6)

Thus NO finite K bounds the whole-subformula bank by K I(F), even on these
balanced trees. Omitting the root does not repair it. The counterexample is
to an accounting helper, not FEI. Its dimension is 1+d(r+1), its tree depth
is d, and the selector energy density at a gate is p->0. No existing fixed
positive-selector-energy assumption covers this representation uniformly.

## 4. The same growing-depth family is covered by the repaired theorem

Disjoint x,y sectors give the exact gate entropy in bits

    Q_r=(1-p)^2 log2(1/(1-p)^2)+2rp(2-p).

For r=1, Q_1=2<=6rp. For r>=2, -ln(1-p)<=p/(1-p) and ln2>1/2
give the first term <=4p(1-p)<=2rp, while 2rp(2-p)<=4rp.
Therefore Q_r<=6rp=6delta(G_r) for all r. No finite search is needed
for this all-r inequality. Balanced composition gives

    H(F_d)=Q_r [1-(1-p)^d]/p,
    H(F_d)<=6[I(F_d)-1].                                    (7)

Equation (7) explicitly pays every level and proves a depth-uniform FEI
bound for the counterfamily. It is included as a test of the repaired ledger,
not advertised as a new read-once closure theorem. The new obstruction is
(6), and the remedy is distinguishing a local gate charge from a repeatedly
charged subformula. With k->infinity, I(F_d)->1 and H(F_d)->0, while S_d
diverges. This isolates spurious overhead accumulation very sharply.

## 5. Exact remaining bridge

The gate logarithm bank is deficit-paid with 4+6/e nats, or
(4+6/e)/ln2 bits, without depth or arity assumptions. The whole-subformula
substitute fails by (6). What remains is a source-valid map from A057's
actual-query remainder, after recentering biased children, into the local
gate bank (2) and a single terminal reserve. Formula weights J and physical
restriction probabilities are different measures and cannot be substituted.
No universal FEI conclusion follows from (1)-(7).
