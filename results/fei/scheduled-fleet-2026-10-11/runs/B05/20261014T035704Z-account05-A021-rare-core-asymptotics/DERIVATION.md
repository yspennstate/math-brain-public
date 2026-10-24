# A coherent refund at the first three-distinct-core hierarchy

All cubes are uniform, all entropies are in bits. Put c=1/ln2.
The result is a scoped repair to the nested reserve interface, not FEI.

## Exact family and physical accounts

Let m>=4 be even and b any bent Boolean sign on m data bits. Its Fourier
coefficients have magnitude a0=2^(-m/2). Choose distinct vertices u,v.
Write delta=2^-m and let b_u,b_v flip b at u,v respectively. With one
fresh balancing sign z, set g0=z b, g1=z b_u, g2=z b_v. Let A,B be
independent fresh point blocks of positive widths r,s, probabilities
alpha=2^-r, beta=2^-s. Define

    h=g1+B(g2-g1), f=g0+A(h-g0),
    pi=(1-alpha, alpha(1-beta), alpha beta).

Query controls to resolution and stop at the actual three cores. All
terminals are nonconstant and distinct. Denote

    H_T=sum_j pi_j H(gj), D=H(f)-H_T,
    I_C=2r alpha delta+4s alpha beta delta.

These are actual terminal entropy and removed influence. The formula
for I_C follows from gamma01=gamma02=delta and gamma12=2delta.
The terminal influence is sum pi_j I(gj), and I(f)=I_C+I_T.

Let e_adj be one if u,v are Hamming neighbors and zero otherwise.
Point-defect edge counting, including the destroyed internal edge, gives

    I01=I02=2m delta, I12=4(m-e_adj)delta,
    Rstar=2 sum_(i<j) pi_i pi_j Iij.

Define w=1-2beta, and the exact nonempty-control sector masses

    V_A=2alpha(1-alpha)delta(1+w^2),
    V_B=8alpha beta(1-beta)delta, V=V_A+V_B,
    L=V_A(2r-2)+V_B(2r+2s-4)
        +2alpha(1-alpha)delta w^2 log2(1/w^2),

with 0 log(1/0)=0. Then

    V=4delta[alpha(1-alpha)+2alpha^2 beta(1-beta)],
    Rstar=m V-8 e_adj delta pi1 pi2.                       (1)

## Uniform expansion: no order surcharge in the leading term

For EVERY m,r,s,b,u,v as above,

    D=m V+L+3c V+E,
    |E|<=8c sqrt(delta) V.                               (2)

The same error constant works for all joint regimes of the two control
widths and m. More precise one-sided bounds are

    [3c+2log2(1-2sqrt(delta))]V <= D-mV-L
       <=[3c+2log2(1+2sqrt(delta))]V.                     (3)

Consequently a rigorous finite-dimensional payment is

    Rstar <= D <= Rstar+(17/2+6c) I_C < Rstar+18 I_C.     (4)

In particular the coefficient-one symmetric terminal-pair reserve is
sufficient on this family with an absolute control rate. The source's
smaller control rate 11/2 is NOT established here.

## Fourier reconstruction and full proof

Use E0(x)=x^2 log2(1/x^2), extended at zero. The balancing sign means
every nonzero core Fourier label contains z. At such a label T, write
xj=hat(gj)(T). The root coefficients fall into just three selector
frequency sectors:

    empty A,empty B: xbar=sum pi_j xj;
    nonempty A,empty B: alpha[(1-beta)x1+beta x2-x0];
    any A,nonempty B: alpha beta(x2-x1).

Their multiplicities are 1, alpha^-1-1, and
alpha^-1(beta^-1-1). These are actual Fourier coefficients of f;
no terminal mixture is substituted for their coherent sums.

For each T let sigma=x0/a0 in {-1,1},
e1=b(u)chi_T(u), e2=b(v)chi_T(v). Then
x1=x0-2delta e1, x2=x0-2delta e2. Across all 2^m data frequencies,
e1,e2 agree on exactly half and disagree on half. Hence the second
sector has magnitudes 2alpha delta and 2alpha delta|w|, each on half
the frequencies. The third has magnitude 4alpha beta delta on half,
and zero on half. This proves the stated V_A,V_B and exact nonempty
sector entropy 2m V+L. In particular L>=0, since 2alpha<=1 and
4alpha beta<=1.

For every T, the weighted variance of x0,x1,x2 equals their nonempty
control Fourier mass. All three amplitudes and xbar have the same sign
and absolute values in [a0(1-q),a0(1+q)], q=2sqrt(delta)<=1/2.
Now E0''(x)=2m-6c-4c ln(|x|/a0) on this interval. Taylor expansion
at xbar, followed by summation with the REAL weights pi, cancels the
linear terms and gives

    E0(xbar)-sum_j pi_j E0(xj)=-m Var_pi(xj)+epsilon_T,
    [3c+2log2(1-q)]Var_pi <=epsilon_T
       <=[3c+2log2(1+q)]Var_pi.

Sum over T, add 2mV+L, and obtain (3). Since
max(|ln(1-q)|,|ln(1+q)|)<=q/(1-q)<=4sqrt(delta), (2) follows.
This step is precisely the coherent Jensen refund omitted when two
independent entropy upper bounds are merely added.

To prove (4), note c>1, so 3c+2log2(1-q)>=3c-2>0.
Thus D>=mV>=Rstar. For the upper bound, epsilon<= (3c+2)V.
Moreover V<=4alpha delta<=2 I_C. Rewrite

    L=2r V+2s V_B-2V_A-4V_B+M,
    M=2alpha(1-alpha)delta w^2 log2(1/w^2)<=V_A.

The latter uses x log2(1/x)<=c/e<1 for x in [0,1]. Therefore
0<=L<=2r V+2s V_B<=4 I_C. The edge correction satisfies
8 e_adj delta pi1 pi2 / I_C <=4alpha beta(1-beta)/r<=1/2.
Combine these bounds and c<3/2 to get (4), with every control and
terminal kept in its original physical account.

## Exact comparison with the reviewed hierarchical reserve

A029's expansion of the two A023 whole-block reserves gives

    Rdata=2alpha(1-alpha)[(1-beta)I01+beta I02]
                 +2alpha beta(1-beta)I12,
    Rfuture=2alpha(1-alpha) I_B, I_B=4s beta delta,
    Rdata-Rstar=2alpha(1-alpha)beta(1-beta) I12.           (5)

These identities are independently reconstructed in REVIEW_A029.md.
For r=s=1, the hierarchy surplus and query influence satisfy

    (Rdata-Rstar)/I_C=(m-e_adj)/4.

It diverges on three genuinely different NONCONSTANT shared cores;
there is no constant-failure flattening of their terminal labels.
Nonetheless (4) pays the actual decrement with Rstar and an absolute
control rate. Thus the divergent extra sufficient-ledger debit is not
an actual leading entropy obligation. This is not a refutation of
A023's once-owned one-block theorem or of A029's correct sufficient bound.

For fixed r,s, Rstar/I_C tends to infinity linearly in m, while
D/Rstar tends to one by (2). Hence any proposed scalar payment
D<=lambda Rstar+K I_C for all these actual functions, with fixed finite
K, necessarily has lambda>=1. Coefficient one is also sufficient by
(4). The optimal coefficient of this data reserve is therefore exactly
one in the large-contrast limit; a zero reserve or a positive fixed
underrefund cannot be concealed in an absolute control price.

## Exact finite certificate compression

The four sign alignments r1=sigma e1,r2=sigma e2 have multiplicities

    N_(r1,r2)=2^m/4+2^(m/2)(r1+r2)/4.

Indeed E r1=E r2=2^(-m/2) by Fourier inversion at u,v, and E r1r2=0
because u!=v. A two-sign distribution is determined by these moments.
Thus the COMPLETE entropy formula can be checked with four constant
sector entries and three nonempty-sector magnitudes for any m; it is
independent of the bent seed or edit distance. The distance affects the
physical reserve through its explicit destroyed-edge correction in (1).
Direct full-cube checks use quadratic b and both adjacent and nonadjacent
edits, without assuming their derivative edges survive.

## Exact first unsupported universal line

No proof extends this coefficient-one reserve to arbitrary non-flat
three-core spectra, arbitrary overlapping controller grammars, or all
nested depths. Even the same coefficient at the source control rate
11/2 is not asserted. The proof crucially uses a common flat Fourier
reference and uniformly small perturbations in its nonzero rows. A
general history rule must replace that curvature control by one certified
signed child/reference surplus, retaining the original terminal laws.
The exact expansion above closes the first common-reference two-edit
refund, rather than the full C019/C024 bridge or full FEI.
