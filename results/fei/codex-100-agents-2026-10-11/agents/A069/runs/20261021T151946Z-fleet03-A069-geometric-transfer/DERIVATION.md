# One inherited terminal bank for an adaptive core history

Status: author proof with exact side certificates (1150 assertions PASS), independent
review pending. Lean allocation check returned RUNTIME_UNVERIFIED; no formal
certification is claimed.

Use the stage5 normalized five-cell law without changing its cell weights. Fix
F=q2 G, q2=-1 exactly when c=0 and Z=0, |Z|=m>=1. In frequency/truth-table
order c+2u the four cores are (Maj3,y0,-y0,-Maj3). Core frequencies initially
have common law R=(8/13,2/13,1/26,1/26,1/26,1/26,1/26,1/26).
At every core restriction carry R by frequency marginalization, identically
for all four cores and both physical children. Keep the same five control
cells. Only the actual empty/nonempty flag prior is updated. All units bits.

For a partial core assignment let a=Maj3 restricted, b=y0 restricted,
d=Pr(a!=b), A=(I(a)+I(b))/2, rho=2^-m, beta=2rho(1-rho),
B=(C_R(a)+C_R(b))/2. Opposite-sign cores have identical Fourier squares.
The four cores sum to zero pointwise and their c=0 average is (a-b)/2.
Consequently the actual complete output reference cost and influence are

 C=B+h2(d rho^2)+2+2(1-2d)rho
       +beta[ m+log2(1-rho)+log2(20/7) ],                 (1)
 I=A+1+(m+1-2d)rho.                                    (2)

Derivation: alpha=Pr(S_controls nonempty)=1-d rho^2. Influence in c is
d+(1-2d)rho; influence in u is 1-d; each Z bit has influence rho.
Every tail cell is flat; total nonempty-Z mass is beta, with half of that
mass containing c. Singleton costs equal twice degree, while tail costs
are twice u-degree plus log2[2(2^m-1)]+log2(20/7).
Thus their combined bill is 2I_cu+beta[log2((1-rho)/rho)+log2(20/7)].
This is an exact full cross entropy, including B and the actual flag.

For a physical unqueried Y bit i, write D_i=C-E C_child and j_i=Inf_i(F).
The nonflag control bill averages exactly over children, hence

 D_i=(B-E B_child)+J_i,
 J_i=h2(rho^2 d)-E h2(rho^2 d_child).                    (3)

Here d=E d_child. Bernoulli thinning proves 0<=J_i<=rho^2<=1/4:
take a fair child label X and conditional B0~Bernoulli(d_X), then an
independent gate E~Bernoulli(rho^2), and output W=E B0.
I(X;W)<=I(X;(E,E B0))=rho^2 I(X;B0)<=rho^2. This is an
auxiliary information identity, not a new physical influence account.
If j_i=0 both actual a,b are independent of i, so d_child=d and J_i=0.

The finite 27-pattern core certificate must establish
 B-E B_child<=4j_i when j_i>0,
 B-E B_child<1/4 when j_i=0.                            (4)
Thus e_i=max(0,D_i-4j_i)<=1/4 for every core query, all m.
This includes irrelevant queries; no positive decrement is called income.

After all three Y coordinates have been fixed, A=B=0 and d is 0 or1.
Let s_leaf=4I_leaf-C_leaf. For m=1,2 certify s_leaf>1 directly for both d.
For m>=3, use h2<=1, log2(1-rho)<=0, log2(20/7)<8/5, beta<=2rho:

 s_leaf>=1+rho(2m+2-4d-16/5)>=1+4rho/5>1.              (5)

Every terminal is nonconstant: its c,u influence is 1+(1-2d)rho>=1-rho>0.
The terminal reference is the inherited law (core law has marginalized to1),
not an entropy-optimal reset. Boundary d=0 has zero flag cost, not a division
by d; rho>0 and 1-rho>0 for all allowed finite m.

For ANY adaptive physical tree querying distinct Y bits, complete it to
three Y queries on each path if necessary, allowing irrelevant queries.
There are at most three charges e_i on a root-to-leaf path. Allocate each
charge to the final descendants of that node with their actual conditional
probabilities. Each final leaf receives at most 3/4 conditional debit from
all ancestors together, against its ONE s_leaf>1 bank. No terminal's slack
is renewed at a child; at least 1/4 remains. Nonnegative query prices
4j_i-D_i may simply be retained, never spent twice.

The exact telescope is
 4I_root-C_root=E s_leaf+E sum_path(4j_i-D_i).
Dropping positive query prices, the allocated negative prices consume at
most3/4 of each full terminal surplus. Therefore 4I_root-C_root>1/4,
and every partial adaptive subtree has both actual terminal bills retained
by first completing its leaves. In particular H(F)<=C_root<4I_root.
This is a statement about a fixed small shared core and an unbounded
private block, and about its actual inherited-reference histories. It is
not a new priority claim for the Boolean family or a universal FEI proof.

The universal missing step remains a common reference with a dimension-free
bound on cumulative signed query excess relative to ONE unused terminal
bank. Here the depth3 bound and the 27-pattern majority/literal certificate
provide that information explicitly. Arbitrary cores need not satisfy (4)
or have depth3; arbitrary source dependence on Z need not satisfy (1).
