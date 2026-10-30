# An admissible influence tolerance under actual reductions

Uniform finite Boolean signs, normalized Walsh coefficients, H in bits,
D_K=H-KI, K>=0. Every tree is finite; all original reaches and complete
terminal functions are retained. Queries may be blocks in the current
chart; following affine/character resets preserve H and do not increase I.
An initial cubic-phase critical normal form is a separate finite selection,
not an entropy-preserving reset or inherited descendant stationarity.

## 1. Charge the influence spent, not the influence still present

At internal node v let g_v be the actual function, let q_v be the sum
of influences of the coordinates queried there, and let rho_v be the
conditional average actual influence released by its child resets.
Write c_v=q_v+rho_v>=0 and

 L_v=H(g_v)-E[H(next child)|v], b_v=L_v-K c_v.

For original node reaches w_v, leaves ell with reaches w_ell, exact
restriction accounting and reset entropy preservation give

 sum_internal w_v c_v + sum_leaf w_ell I(g_ell)=I(g_root), (1)
 D_K(root)=sum_internal w_v b_v+sum_leaf w_ell D_K(g_ell). (2)

Thus ANY nonnegative certified allowances e_v,e_ell satisfying
b_v<=e_v and D_K(g_ell)<=e_ell prove D_K(root)<=sum w e.
In particular, if epsilon>=0 and

 b_v<=epsilon c_v at EVERY internal node,
 D_K(g_ell)<=epsilon I(g_ell) at EVERY complete leaf,     (3)

then H(root)<=(K+epsilon)I(root), with NO depth factor. More generally,
different node/leaf tolerances may be used whenever their weighted
influence allocation is at most epsilon I(root). Each allowance has an
owner in the SAME original influence ledger. Negative signed bills may
be kept; replacing them by positive parts is only an upper relaxation.
Zero spend requires b_v<=0; zero-influence Boolean leaves have H=0.

This certificate is stable under grafting any certified child subtree,
branch-dependent affine charts, grouping consecutive levels into a
larger actual reduction, early stopping with the stated leaf certificate,
and independent tensor products using sequential component trees.
The reason is (1): grafted influence allocations sum to precisely the
former terminal allocation. Tensor H,I and independent reaches add.
No fresh bank is created when the chart changes. Grouping only discards
interior cancellations; it does not assume a common original chart.

## 2. Finite critical selection with a nonzero tolerance

Fix K,epsilon>=0 and put C=K+epsilon. If FEI(C) fails on finite cubes,
choose the least essential dimension n of a positive D_C witness.
There are finitely many n-bit Boolean tables, so choose a maximizer
of D_C there. This also maximizes over any finite joint affine/cubic-
phase orbit and is affine-influence minimal when C>0. Its positivity
forces essential dimension n. No optimizer over unbounded dimensions
or compactness is used. Support-affine compression cannot lower its
dimension either: that would give a smaller positive D_C witness with
the same H and no larger I. ALL smaller Boolean functions, including every
affine image of a proper actual child, satisfy D_K<=epsilon I.

Consequently a SINGLE proper actual block with

 L_A<=C(I_A+rho_A),                                     (4)

and all complete transformed children would imply D_C(root)<=0 by
(1)--(3), a contradiction. A universal selector of (4) on this exact
finite critical class suffices for FEI(C). Approximate local funding
at baseline K is admissible precisely as b_A<=epsilon c_A, not an
unscaled absolute error or a repeatedly renewed remaining-I allowance.
This is a sufficient reduction-stable tolerance convention, not a claim
that all other possible conventions are logically impossible.

An epsilon_a-near finite D_C maximum, where C>0, also satisfies
I(root)-a(root)<=epsilon_a/C by testing its finite entropy-preserving
affine minimizer. A near-maximal table does NOT itself license exact
nonnegative smaller-child reserves; that conclusion uses the separate
least-dimension threshold selection above. Absolute variational error
epsilon_a and per-spent-influence error epsilon have different units
and must never be substituted for each other.

## 3. Remaining-influence allowances can overcharge without bound

Let g(x,y)=(-1)^(xy). On two bits it has H=2,I=1, full affine spectral
span and minimum affine influence. Let h be t independent copies.
Query its pairs in order, first x then y, with identity resets, until
all data bits are fixed. At the beginning of a pair with j factors left,
expected current influence is j; after its first query it is j-1/2.
Therefore this complete physical tree has

 sum_internal reach*I(current)=sum_{j=1}^t (2j-1/2)
                             =t^2+t/2,                 (5)
 sum_internal reach*queried_influence=I(h)=t.            (6)

The latter is the resource actually spent. Equation(5) is a repeated
occupation of influence which will be queried later, not a new release.

The failure remains inside bounded-I affine-minimal full-span roots.
Set p=2^-k,t=2^k,mu=2^-t, k>=2 and F=1-A+A h, with k zero controls.
Query controls until the first1 (then stop), and on activation query
all data pairs as above. Every complete terminal is constant. Its
expected query count is 4-2p and

 I(F)=p[t+k(1-mu)]->1,
 Omega:=sum_internal reach*I(current)
       =p[k t+(1-mu)k(k+1)/2+t^2+t/2]>=t.                (7)

For each control node with j previous zeros, conditional activation
probability is2^{-(k-j)}, so its weighted influence is
p[t+(k-j)(1-mu)]; this proves the first two terms in(7).
The data subtree contributes p(t^2+t/2) by(5).
Thus Omega/I(F) tends to infinity, even though mean depth<4 and root
influence tends1. Full span and affine minimality are those of the
reviewed actual activation family; no free spectral law is used.

At k=10,t=1024 the root is an actual2058-bit Boolean formula with
I(F)<=517/512, Omega>=1024, hence Omega/I(F)>1000.
A putative allowance epsilon I(current) at each node could therefore
budget over1000 epsilon I(root), whereas epsilon c_v telescopes to
exactly epsilon I(root). This disproves that proposed error-accounting
inference. It does NOT claim the actual local bills saturate such an
allowance, and is not a counterexample to FEI.

## 4. Independent reconstruction and universal unpaid line

A002 STOPPING_REVIEW Section3 sharp depth-law envelope independently
HOLDS without repair: for T>=0 and an error event Z of probability e,
E[T1_Z]<=L e+E(T-L)_+ for every L>=0. On a finite uniform input space,
choose the largest e-fraction of depths and split only a tied threshold
to attain the bound; e must be an admissible atom fraction for an
actual event. The threshold is an exact primal/dual witness. Uniform
integrability of T plus e->0 forces the envelope to vanish, and
Cauchy--Schwarz gives E[T1_Z]<=sqrt(e E T^2). This accepts the sharp
occupation admission theorem and stated limits, not source census.
The last-stage A051 stopping theorem's independent A002 acceptance is
consumed at its reported Sections1--4 scope.

FIRST UNSUPPORTED UNIVERSAL LINE: force (4) at some ORIGINAL proper
pair of a genuine finite high-C critical witness using independent
cheap-parity rank, signed cubic alignment, SAME unused complete child
reserve, mixed entropy interaction and every terminal. The new tolerance
rule can transport such an approximate payment without depth loss; it
does not establish that payment or any dimension-independent C. FEI OPEN.
