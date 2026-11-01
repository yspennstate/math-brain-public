# Point-defect coordinate-tree release

All information is in bits. Write L=log2(e). Let f_n=1-2*1_{x=0} on n uniform physical bits, n>=2. Query any unqueried coordinate at every nonconstant node and stop at constants. Choices may depend on physical history. Every active k-bit state is a translated point defect; there is only one active child, with conditional probability 1/2. Permutation/translation invariance makes every such singleton tree have the same ledger. Put d_k=2^(1-k), w_k=2^(k-n), and d=d_n. Thus w_k d_k=d and sum_{k=1}^n w_k d_k=nd=I(f_n).

The k=1 state is a character and has zero entropy, TC, Gamma, JS, mutual-information credit and erasure. Constant leaves have these values zero. Point-defect K_occ is zero at every active state; therefore Delta_k=TC_k. The last stage established this source-exactly; we do not renew its collision target.

## Local quantities, k>=2

Let h=h_2, phi(t)=h(t)-h(2t)/2, and
q0_k=(1-d_k)^2+d_k^2,
beta_k=2d_k(1-d_k).
The exact squared spectrum is (1-d_k)^2 on empty and d_k^2 on each nonempty set. Thus
H_k=-2(1-d_k)^2 log2(1-d_k)+4d_k(1-d_k/2)(k-1),
M_k=k h(d_k), Delta_k=M_k-H_k.

One child is constant; the other is f_(k-1), with every surviving influence 2d_k. Hence
Gamma_k=(k-1)phi(d_k).

Erasing the queried bit leaves mass q0_k at empty and 2d_k^2 at each other residual subset. The total nonempty residual mass is beta_k, NOT d_k-2d_k^2. There are 2^(k-1)-1 such fibers, so the exact erasure is
B_k=q0_k h(d_k^2/q0_k)+beta_k.
The bit is fair in every nonempty residual fiber. The occupancy mutual-information credit is
C_k=h(d_k)-B_k>=0.

Conditional on nonempty residual frequency, the mixture and the nonconstant child's law are both uniform. Child nonempty probability is 2 beta_k. Thus their uniform-mask entropy terms cancel in JS, giving
J_k=phi(beta_k).

These actual signed children give the exact local identities
H_k=B_k+J_k+H_(k-1)/2,
Delta_k=C_k+Gamma_k-J_k+Delta_(k-1)/2.
They independently specialize A039's compensated coherent projection identity.

## Full-tree release and a closed reset sum

Put G_n=sum w_k Gamma_k, C_n=sum w_k C_k, J_n=sum w_k J_k,
B_n^tree=sum w_k B_k, S_n=sum w_k h(d_k).
There is no terminal TC or terminal entropy. Multiplying the preceding identities by visit weights and telescoping gives
Delta_n+J_n=G_n+C_n,
H_n=B_n^tree+J_n,
C_n=S_n-H_n+J_n.

The Gamma sum has a closed formula:
G_n=n h(d_n)-S_n=M_n-S_n.
To see this, substitute phi into sum_{k=2}^n w_k(k-1)[h(d_k)-h(d_(k-1))/2]. Since w_k/2=w_(k-1), every intermediate h(d_k) coefficient becomes -w_k, leaving (n-1)h(d_n)-sum_{k<n}w_k h(d_k). Add and subtract h(d_n).

The exact normalized finite answer can also be written
G_n/Delta_n=[n h(d_n)-S_n]/[n h(d_n)-H_n],
C_n/Delta_n=[S_n-H_n+J_n]/[n h(d_n)-H_n].
Use these ratios only when Delta_n>0, i.e. n>=3. Delta_2=0 but G_2=J_2=1 and C_2=0. Thus the root is not split into two independent nonnegative reserves at finite n: physical-mixture JS is an explicit injection.

## Explicit all-n bounds and release fractions

For 0<t<=1, including the continuous endpoint t=1, write
h(t)/t=log2(1/t)+L+e(t),
-L t<=e(t)<=0.
For t<1 this follows from
t<=-ln(1-t)<=t/(1-t),
so (1-t)L<=[(1-t)/t]log2(1/(1-t))<=L.
At t=1 the formula gives e(1)=-L. Since sum_{k=1}^n d_k<2,
S_n/d_n=n(n-1)/2+n L+E_n, with -2L<=E_n<=0.
Combining the closed Gamma formula with e(d_n)<=0 gives
G_n/d_n<=n(n-1)/2+2L.
For the sharper lower bound, phi'(t)=1+log2[(1-t)/(1-2t)]>=1 on 0<t<1/2 and phi(0)=0, so phi(t)>=t up to the endpoint 1/2. Therefore
n(n-1)/2 <= G_n/d_n <= n(n-1)/2+2L.                 (A)

For the JS sum, k=2 gives beta_2=1/2 and J_2/d_2=2. For k>=3, beta_k<=3/8. The same derivative calculation gives phi(x)=x+eta(x), eta>=0. Using ln(1+u)<=u,
eta(x)<=L x^2/[2(1-2x)]<=2L x^2 for 0<=x<=3/8.
Consequently
2-2d_k <= J_k/d_k <= 2+(8L-2)d_k.
Summing k=3,...,n and using sum_{k>=3}d_k=1/2 gives, for every n>=2,
2(n-1)-1 <= J_n/d_n <= 2(n-1)+4L-1.                (B)
The n=2 inequalities include its exact endpoint, so no limit exception is hidden.

The exact H formula, retained from the source rather than offered as a new class FEI bound, gives
H_n/d_n=4(n-1)+2L+E_H,n,
-[2(n-1)+4L]d_n <= E_H,n <=0.
Indeed its empty contribution divided by d_n lies between 2L(1-d_n)^2 and 2L(1-d_n), and the nonempty contribution is 4(n-1)-2(n-1)d_n.

Equations (A),(B) and this explicit error imply
Delta_n/I_n=n-5+L+o(1),
G_n/I_n=(n-1)/2+O(1/n),
C_n/I_n=(n-1)/2+L-2+O(1/n),
J_n/I_n=2+O(1/n),
B_n^tree/I_n=2+O(1/n).
The exponentially small d_n terms also fit O(1/n) for n>=2. In particular,
G_n/Delta_n -> 1/2,
C_n/Delta_n -> 1/2,
J_n/Delta_n -> 0.

A useful explicit credit bound follows from the same errors:
d_n[A_n+(n-2)L-2(n-1)-(1+3L)]
 <= C_n
 <= d_n[A_n+(n-2)L-2(n-1)+6L],
where A_n=n(n-1)/2.
For the lower bound use n d_n<=1, E_n>=-2L and (B); for the upper bound use (n-1)d_n<=1/2, d_n<=1/2 and the upper errors. C_n itself is nonnegative, so the lower bound may be replaced by its positive part. These are explicit quantitative statements, not floating asymptotics.

Thus accumulated Gamma is not O(I) even after optimizing over every full physical singleton coordinate tree of these sources:
G_n/I_n >=(n-1)/2.
This is a full-tree extension of the already known local Gamma obstruction, not a disproof of FEI or a claim about proper-block trees or trees stopped at paid nonconstant leaves.

## Bayes-compatible signed reset: source kernel and all-tree bound

Use A039's actual coherent kernel k(y|T)=P_child_y(T)/(2P_residual(T)) under both P and the parent residual product Q. Point defects have no zero residual fibers for k>=2, so no arbitrary extension is needed. Let y=c label the constant child. For T nonempty, k(c|T)=0; for T empty,
k(c|empty)=1/(2q0_k).
The residual product puts mass (1-d_k)^(k-1) on empty. Therefore its constant-child outcome probability is
q_k=(1-d_k)^(k-1)/(2q0_k).
P's outcome is fair. The output divergence is
O_k=D_2(Bern(1/2)||Bern(q_k))
   =-1/2 log2[4q_k(1-q_k)].
At k=1,2, O_k=0.

Let Q_y be the Bayes-predicted child reference and R_y its newly optimized product; let rho_k=E_y E_{P_child_y} log2(Q_y/R_y), interpreted on actual child support. Applying one common kernel, with no channel injection, gives A039's exact signed correction
rho_k=O_k+J_k-Gamma_k.
We independently reconstruct this equality in the exact finite node checker.

The total output divergence O_n=sum w_k O_k satisfies an explicit uniform bound
0<=O_n<=8L d_n.                                    (C)
Proof: for k>=3, q0_k>=5/8 and (k-1)d_k<=1/2. Bernoulli gives q_k>=1/4. Also (1-d_k)^(k-1)<=(1-d_k)^2<=q0_k, so q_k<=1/2. Write epsilon_k=1-2q_k in [0,1/2]. Its numerator is at most (k-3)d_k+2d_k^2<=(k-2)d_k, hence epsilon_k<=2(k-2)d_k. Then
O_k=-(L/2)ln(1-epsilon_k^2)
 <=(2L/3)epsilon_k^2
 <=(8L/3)(k-2)^2 d_k^2.
Since w_k d_k^2=d_n d_k and sum_{k>=3}(k-2)^2 d_k=3, (C) follows. The geometric-series sum is exact and all terms are nonnegative.

The cumulative SIGNED reset is R_n=sum w_k rho_k, so
R_n=O_n+J_n-G_n,
R_n/Delta_n -> -1/2.
In particular O_n/I_n<=8L/n tends to zero while G_n/I_n diverges. The reset is a large negative correction, not an extra positive root reserve. From (A)-(C), R_n<0 for every n>=9. No term can be discarded just because its standalone sign is attractive.

## What this does and does not pay

The net erased-label debt is S_n-C_n=B_n^tree=H_n-J_n. On this exact family its ratio tends to 2, even though root Delta, cumulative Gamma and cumulative mutual-information credit have ratios to influence growing linearly in n. Reference transfers and credits cancel at a much larger scale than the remaining entropy debt.

The first unsupported universal line is extending a compatible, net erasure-plus-terminal payment to overlapping activated cores or arbitrary Boolean sources with one nonreused physical influence budget. Neither the half-release fractions nor the signed-reset identity implies that universal inequality. The point-defect family is calibration for the demonstrated cancellation, not a new isolated FEI class result.

