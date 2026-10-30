# Reference-error occupation, and the expected-depth boundary

Finite uniform Boolean signs, entropy in bits, K>=0. All trees below
query one current coordinate per node, may use branch-dependent invertible
affine input maps and output characters, and retain all complete leaves.

## 1. Fixed reference error survives a changed chart

Choose ANY signed character c at the root and let Z={f!=c}, e=P(Z).
Transport c through exactly the same affine input maps and output
character multiplications as f. On an actual restriction it remains a
signed character. The original error event is unchanged by any such
reset. At node v of reach w_v, let q_v=P(Z|v). Both actual daughters
have conditional probability1/2 and their q's average to q_v. This is
a martingale for the fixed original error event, not a newly chosen
error event in each chart. The best-character error at v is at most
min(q_v,1-q_v). Comparing translated endpoints with this reference
shows the directional minority m_v<=min(2q_v,1/2).

Use the established one-query entropy inequality and symmetrize by
the queried character, as in A005 DERIVATION Sections1--2:

 L_v=H(f_v)-E H(child)<=phi(m_v),
 phi(x)=h2(x)+(2/ln2)x, 0<=x<=1/2.

Phi is concave and increasing. Thus psi(q)=phi(min(2q,1/2)) is concave
and increasing on[0,1]. Complete child entropies are unchanged by resets.

## 2. Occupation theorem: expected stopping time with the right measure

Let tau be the total number of queries on a path of ANY finite tree;
zero-query leaves and early stopped leaves are allowed. Put

 dbar=E tau=sum_internal w_v,
 a=E[1_Z tau]=sum_internal w_v q_v.                       (1)

The second equality follows by summing the indicators that each node
is visited, multiplied by the SAME root event Z. It does not assert
independence between stopping time and the error event. If dbar>0,
Jensen over the finite measure assigning mass w_v to each internal
node and entropy telescoping give

 H(f)-E H(leaves) <= dbar phi(min(2a/dbar,1/2)).           (2)

If dbar=0 both sides are zero. Resets need not decrease I for (2).
For nonincreasing actual-I resets, E I(leaves)<=I(f), so

E D_K(leaves)>=D_K(f)-dbar phi(min(2a/dbar,1/2)).         (3)

More precisely, write Q+R=I(f)-E I(leaves) for the SAME original
expected queried influence plus actual reset release, and write
S_leaf=E[K I(leaves)-H(leaves)]. Then the full signed bank satisfies

 D_K(f)+S_leaf+K(Q+R)=H(f)-E H(leaves)
                      <=dbar phi(min(2a/dbar,1/2)).       (3a)

This is the stronger critical admission test when S_leaf>=0. No
root-influence increase, old debit, or reset is granted a new bank.

In particular, if every complete terminal is K-nonviolating, then
D_K(f)<=dbar phi(min(2a/dbar,1/2)). On a genuine least-dimensional
K-witness this is applicable to any frontier whose leaves have actually
smaller dimension, including their affine images. No signed terminal
debt is discarded. The query influence/reset release ledger remains
the SAME original ledger; (2) only upper-bounds its entropy decrement.

For a tree of maximum depth r, (1) implies a<=r e. At each fixed
padded level Jensen also yields A005's sharper simple bound
H(f)-E H(leaves)<=r phi(min(2e,1/2)). We do not claim that substituting
a<=r e into (2) gives exactly that sharper expression. Both are valid;
the occupation statement requires no maximum-depth parameter and keeps
the correlation that an expected-depth substitution would lose.

## 3. An actual bounded-expected-depth frontier clears arbitrary seed debt

Fix any canonical nonconstant d-bit seed g, with full affine span,
H0,I0>0, mu=Eg. Let t=2^k,p=2^-k,k>=2, h=g^tensor(t),
F=1-A+A h, where A is the event that the first k controls are zero.
This is the actual Boolean escape family from A051 COMPACTNESS.
Its complete entropy and influence satisfy

 |H(F)-H0|<=p(10k+15), I(F)=I0+kp(1-mu^t).

Use this ORIGINAL physical-coordinate tree, with no input resets:
query controls in order until the first1, then stop at constant+1.
If all k controls are0, query ALL dt data coordinates (even if a
constant was reached sooner) and stop. All terminal functions are
constants, so every complete terminal has H=I=D_K=0. Direct counting
gives

 dbar=sum_{j=0}^{k-1}2^-j+pdt=d+2(1-p)<=d+2,             (4)
 e=P(F!=1)=p(1-mu^t)/2,
 a=E[1_{F!=1} tau]=e(k+dt).                             (5)

The root's largest absolute Fourier coefficient is its empty one:
1-p(1-mu^t)>=1-2p>=1/2, whereas each other coefficient has magnitude
at most2p<=1/2. Hence the constant predictor attains best-character
error e, including possible ties. The reference is therefore also
eligible for A005's root best-error convention.

Although e->0 and dbar stays bounded, a->d/2. The rare error paths
are precisely paths of length k+dt. One cannot replace the MAXIMUM
depth r in A005's theorem by E tau, or assume a=e E tau. The tree
does not preserve any positive seed deficit in its leaves. It contains
unpaid local bills whenever the root violates K; neither (4) nor zero
terminal deficit declares those bills paid. The physical query-cost
telescope still spends exactly I(F), once.

The same tree works for ANY finite seed ratio and every K. Any claim
that a bounded-expected-depth frontier retains arbitrary seed deficit
is false, even on full-span affine-minimal roots. This does not refute
A002/A005, whose stated hypotheses concern MAXIMUM depth.

## 4. Finite rational negative arm and exact scope

Take g(x,y)=(-1)^(xy), H0=2,I0=1,mu=1/2 and k=10,t=1024.
The 2058-bit root is specified by its Boolean formula, not enumerated.
Its actual tree has dbar=2047/512<4 and all terminals constant.
The seed-profile bound gives H(F)>=1933/1024.
The elementary h2(x)<=x log2(euler_e/x) gives, using ln2>2/3,

 phi(min(2e,1/2))<=phi(2p)
   <=2p[k+3/ln2]<29/1024.

Therefore the false expected-depth substitution would give entropy
loss <116/1024, whereas the actual loss is at least1933/1024.
The same root has D_1(F)>=889/1024>0 and terminal D_1=0, so the
false expected-depth DEFICIT-retention claim also fails strictly.
Equation(5), retained in the correct occupation theorem, prevents
this contradiction. All displayed separations are rational; the
negative arm uses an actual finite Boolean family, not a free spectral law.

## 5. Independent review and universal unpaid line

A005 DERIVATION Sections1--3: HOLDS unchanged, without repair, for
the affine-invariant best-character error, physical supermartingale,
one-query symmetrization, padded-level Jensen maximum-depth bound and
nonincreasing-I terminal-deficit bound, including activation insertion.
The source depth64 point8 certificate and source census are not newly
independently accepted here. This review retains the crucial distinction
between maximum depth and expectation, and between expected debt and
positivity of every leaf. A002's original-data-only conclusion is read
context and is not extended to control frontiers.

FIRST UNSUPPORTED UNIVERSAL LINE: force a paid ORIGINAL proper pair
of every genuine finite least-dimensional high-K witness from independent
cheap-parity rank and SAME unused NONNEGATIVE smaller-affine-child
reserves, with mixed interaction and all complete terminals. No uniform
bound selecting such a pair is proved. The new occupation bound supplies
a stopping-time admission constraint, not payment of that pair. FEI OPEN.
