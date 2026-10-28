# Rare activation survives affine minimum-basis reduction

All cubes are finite and uniform F_2 cubes; Boolean outputs are signs.
Entropy H is Shannon entropy of the squared normalized Walsh coefficients,
in bits. Write d_i=Inf_i and I=sum d_i. For a sign h define

    w_h(v)=sum_{s:v dot s=1} hhat(s)^2
          =Pr_x[h(x)!=h(x+v)].

The second equality is Parseval applied to a translate. In particular
w_h(e_i)=d_i. An affine-minimum-basis sign is one whose squared spectral
law minimizes I under every invertible affine relabeling s -> Ms+b.
A051's characterization is

    d_i<=1/2; min(w_h(v),1-w_h(v))>=max_{i:v_i=1} d_i.        (A)

Every assertion below concerns an explicit root, not a critical witness.

## 1. Exact activation criterion

Fix k>=2, p=2^-k, mu=E h, delta=1-mu. Let a(z) indicate z=0^k, and set

    F(x,z)=1+a(z)(h(x)-1).

The root is Boolean. For data displacement u and control displacement v,

    w_F(u,0)=p w_h(u),
    w_F(u,v)=p delta                    if v!=0.            (1)

For v=0, only the active slice contributes. For v!=0, the two control
events z=0 and z+v=0 are disjoint. On each, the two signs disagree with
probability Pr[h=-1]=delta/2 (translation does not change this probability).
Their total contribution is 2p(delta/2)=p delta.

Thus the data influences are p d_i; every control influence is p delta;
I(F)=p(I(h)+k delta). Every value in (1) is <=1/2: p<=1/4,
0<=w_h<=1 and 0<=delta<=2. The minority in criterion (A) is therefore
the value itself, including equality at 1/2. Consequently F satisfies (A)
if and only if

    w_h(u)>=max_{i:u_i=1} d_i for every u!=0, and
    delta>=max_i d_i.                                      (2)

An empty data-coordinate maximum imposes no condition. The second
condition always holds for Boolean h: the disagreement event
{h(x)!=h(x+e_i)} lies in {h(x)=-1} union {h(x+e_i)=-1}, so d_i<=delta.
The exact criterion therefore reduces to the first condition in (2).
This uses pointwise Booleanity, not L2 normalization alone.

In particular an affine-minimum-basis seed satisfies (2), and so does its
activation. No balancing bit is required; a deterministic balancing
coordinate can in fact break affine minimality through mixed parities.

The restriction k>=2 ensures that no complement branch is omitted. For
k=1, p delta can exceed 1/2; for example h=-1 gives a control dictator,
which is not affine-minimal. Constants and zero influences are permitted
in (1)--(2). They are excluded only where H/I is formed below.

## 2. Tensors preserve all affine minimum-basis constraints

Let g be an affine-minimum-basis sign. For h=g^{tensor t}, every spectral
block is independent with the law of g. For u=(u_1,...,u_t),

    1-2w_h(u)=product_b (1-2w_g(u_b)),
    min(w_h(u),1-w_h(u))
      =(1-product_b |1-2w_g(u_b)|)/2
      >=min(w_g(u_b),1-w_g(u_b))

for every used block b. All factors lie in [0,1]. For each coordinate
used by u, (A) in its block bounds this last quantity below by its original
d_i. Tensor coordinate influences equal the corresponding g influence,
which is <=1/2. Thus h again satisfies (A), including zero blocks and ties.
Also H(h)=tH(g), I(h)=tI(g), and E h=mu_g^t.

## 3. Full affine span and the entropy ledger

Write c_s=hhat(s). The Fourier coefficients of F are exactly

    Fhat(0,0)=1-p delta,
    Fhat(0,z)= -p delta                    (z!=0),
    Fhat(s,z)=p c_s                       (s!=0, every z). (3)

If h has full affine spectral span in its n data bits and n>0, it is
nonconstant and delta>0. Its nonzero data spectral labels span F_2^n:
the full affine span of its support implies its full linear span. Equation
(3) has a nonzero root (1-p delta>=1/2), every pure control unit label,
and each nonzero data label in the seed support. Hence the support of F
has full affine span n+k. No absent coefficient is presumed nonzero.
Tensor products preserve full affine span by taking independent support
differences in each block.

More precisely, for any nonconstant h the affine spectral dimension of F
is k plus the linear dimension of the span of the nonzero labels in the
support of h, by the same nonzero-root/control-unit argument. Thus
activation can repair affine rank as well as minority-basis minimality:
majority3 itself has affine rank two and fails (A), whereas its activated
root has full affine rank five and satisfies (A). Its raw w(u) values
are 1/2 for nonzero u other than 111, and w(111)=1, so (2) holds.
In contrast parity2 has w(11)=0<d_1=d_2=1 and its activation fails (A).

Let q_s=c_s^2 and v=1-mu^2. Using 0 log 0=0, the exact ledger is

 H(F)= -(1-p delta)^2 log2((1-p delta)^2)
       +p H(h)+p mu^2 log2(mu^2)
       +2k p v+(p-p^2)delta^2(2k-log2(delta^2)).            (4)

It follows directly by grouping (3): one exceptional root, 2^k-1 pure
control coefficients, and 2^k copies of each nonzero data coefficient.
This proves (4) even at mu=0 or delta=0 by continuity of x log x.

## 4. Simultaneous rare, weak, full-span affine-minimal hardness

Given any seed f with H(f)>0, use A051's finite affine compression and
orbit minimization to obtain a sign g on d<=n coordinates with full affine
spectral span, satisfying (A), H(g)=H(f), and 0<I(g)<=I(f).
This step is independently reconstructed in Section5 below. In particular
g is neither constant nor a character, and |mu_g|<1.

For every positive integer t take h_t=g^{tensor t}, k_t=ceil(sqrt(t)),
using max(2,k_t) to include the first few t, p_t=2^-k_t, and activate as
above. Sections1--3 prove that F_t is an actual Boolean sign of dimension
N_t=td+k_t, full affine spectral span, and affine minimum-basis influence.
Moreover

    E F_t=1-p_t(1-mu_g^t) ->1,
    I(F_t)=p_t(tI(g)+k_t(1-mu_g^t)) ->0,
    max_i Inf_i(F_t)<=2p_t ->0,
    H(F_t)/I(F_t) -> H(g)/I(g) >= H(f)/I(f).              (5)

For the entropy limit, divide (4) by p_t t. Its core term becomes H(g).
The term mu^2 log(mu^2)/t is uniformly O(1/t). Also
delta^2 log(delta^2) is uniformly bounded for 0<=delta<=2, and k_t/t->0.
For the root term use -x log2 x <= (1-x)/ln2 on [0,1]; with
x=(1-p delta)^2 its contribution after division is <=4/(t ln2).
Thus the limit uses finite uniform bounds, not an interchange of an
infinite entropy sum. I(g)>0 is fixed, so the limiting denominator is
nonzero. Polynomial t times 2^-ceil(sqrt(t)) tends to zero.

Let R be the class with (A), full affine spectral span, E F>=1-eta,
I(F)<=epsilon, and max_i Inf_i<=tau, for any fixed positive eta,epsilon,tau.
For every K>=0,

    H<=K I on R  iff  H<=K I on every Boolean sign.         (6)

The backward direction is inclusion. For the forward direction, if a seed
has H>K I, then g has at least that ratio and (5) supplies an actual F_t
in R with H(F_t)>K I(F_t) for all sufficiently large t. Constants have H=0
and need no admission. There is no rate uniform over all seeds claimed.

## 5. Independent reconstruction of the A051 premise

If A is the nonempty Fourier support, choose a in A and let V=span(A+a)
have dimension d. Select d original coordinate projections J independent
on V. Their restriction maps V bijectively onto F_2^d. There is a unique
point a0 in a+V whose selected coordinates are chosen majority values of
the corresponding squared spectral marginals. Modulate by character a0
and choose an invertible Fourier linear map whose first d forms restrict
to J on V and whose remaining forms annihilate V. The resulting sign
depends on d inputs, has unchanged entropy, full affine spectral span,
and influence sum_{j in J}min(d_j,1-d_j)<=I(f).

Minimize influence in its finite affine spectral orbit. Flipping a label
coordinate gives d_i<=1/2. Replacing identity row i by any u with u_i=1
is invertible; choose its translation to make its marginal the minority.
Nondecrease of influence yields min(w(u),1-w(u))>=d_i, proving (A).
Conversely, under (A) every linear form of minority cost <r is supported
on coordinates with d_i<r. Independent such forms number at most those
coordinates. Sorting costs therefore shows that every basis has its
j-th cost at least the j-th coordinate cost. Translation cannot improve
below minority cost. This proves the whole-orbit characterization,
including ties and d=0. Fourier relabeling is implemented by invertible
input linear substitution and character multiplication, preserving signs.

This reconstruction accepts this scoped A051 premise only; it does not
accept a critical pair-payment theorem or identify transformed physical
children with original children.

## 6. The precise unpaid universal step

No F_t above is certified as a least-dimensional violator or as a maximum
of D_K among all signs of its dimension. In fact restriction to the active
controls recovers h_t, and restriction of its other blocks to fixed inputs
recovers a sign of g. Therefore when g violates K, a proper lower-dimensional
child also violates K. These roots explicitly fail minimal-witness child
eligibility. Their root affine-minimality does not repair that failure.

The SAME physical bank remains

    D_K(F)+S_A=H(F)-E H(F|A)-K I_A,
    S_A=-E D_K(F|A).

Neither the affine inequalities nor the activation limit supplies a bound
on the signed S_A or forces a paid physical pair. FIRST UNSUPPORTED LINE:
use actual finite maximality AND lower-dimensional nonviolation to select
a proper physical pair whose full entropy loss is <=K I_A, spending this
one bank with complete terminals. Equation(6) rules out obtaining that
payment merely from affine minimum-basis inequalities plus rare/weak
root thresholds. This advances the hardness map at the new A051 endpoint;
it gives no universal constant improvement and no disproof of FEI.
