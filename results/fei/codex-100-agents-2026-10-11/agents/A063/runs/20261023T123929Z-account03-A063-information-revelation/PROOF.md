# Quadratic phases: one original rank account pays every actual reset

All entropies and divergences below use base-two logarithms. Let
f(x)=(-1)^{q(x)+ell.x+c}, x in F_2^n, where q(x)=sum_{i<j} A_ij x_i x_j
and A is symmetric with zero diagonal. Put r=rank(A), m=number of nonzero
rows, and W=r/2. At every reached node use the actual full product of the
spectral marginals as reference. At a physical query transport this reference
by the source-induced kernel, with FAIR extension on every zero-source row,
normalize each outcome, then actually reset both references to their actual
products. Arbitrary adaptive coordinate orders and stopping cuts are allowed.
No new owner is issued at any descendant. The initial reference is this
actual product; arbitrary incoming references are outside the theorem.

## 1. Spectral law, including the affine shift

For h=q+ell.x+c, Fourier autocorrelation gives
p(s)=hat(f)(s)^2=2^{-n} sum_{t in ker A} (-1)^{q(t)+ell.t+s.t}.
Indeed averaging f(x)f(x+t) over x kills every t with At nonzero, and leaves
(-1)^{q(t)+ell.t} otherwise. On ker A the map q is linear, because its
polarization is t^T A u. Thus p is uniform on a nonempty affine coset of
(ker A)^perp=im A, of dimension r. The coset need not be ell+im A.
Consequently H(p)=r. A spectral coordinate is fair precisely when its row
of A is nonzero; otherwise it is fixed to ell_i. Thus M=sum h2(d_i)=m,
TC=M-H=m-r, and physical I=m/2+a, where a counts isolated vertices with
ell_i=1. All restrictions remain quadratic; r is even.

## 2. One query with the actual zero-source extension

For query i let p_0,p_1 be the two child spectral laws on the remaining
coordinates and let qbar=(p_0+p_1)/2 be the erased parent law. Transport
the erased incoming reference Qbar using k_b(t)=p_b(t)/(2qbar(t)) on
qbar(t)>0 and k_b(t)=1/2 otherwise. Its outcome mass is pi_b, and the
normalized predicted child reference is Q_b=Qbar*k_b/pi_b. Define
K=KL(p||Q), K_b=KL(p_b||Q_b), E=K-KL(qbar||Qbar),
O=KL((1/2,1/2)||pi), and the signed actual reset price
sigma=(TC_0+TC_1-K_0-K_1)/2.
The general source identity is K=E+O+(K_0+K_1)/2.

An isolated queried vertex has d_i in {0,1}; the child laws coincide,
pi is fair, and E=O=sigma=0.

For an active vertex write r'=rank(A without i)=r-2s, s in {0,1},
and let k count its neighbors that become isolated upon deletion. Then
m'=m-1-k. The rank alternatives follow by bordered alternating-matrix
elimination: if A' has the same rank as A, the added column is in im A';
otherwise one hyperbolic pair raises the rank by two. Equivalently e_i
lies in im A exactly in the latter case. This also follows from whether
erasing coordinate i has a one-dimensional kernel on im A.

If s=0, erasure of the affine support is injective. Its image has size 2^r.
Each child is uniform on a coset of im A' of size 2^r; since their mean is
qbar, both equal qbar. Hence k_b=1/2 everywhere, INCLUDING reference-only
rows. The incoming product is uniform on an axis-aligned subcube with
m free bits. The erased reference has m-1 free bits; its support contains
both child supports. Thus pi_b=1/2, K_b=m-1-r, E=1, O=0, sigma=-k.

If s=1, erased support has size 2^{r-1}; the two child supports each have
size 2^{r-2} and must be disjoint and partition it (their mean is uniform).
The kernel is deterministic there and fair outside. The erased product is
uniform on its subcube, and the two source supports have equal size inside
that subcube. Therefore the deterministic contributions to pi_b are equal;
the reference-only contribution is split equally. Thus pi_b=1/2 exactly.
On the actual child support Q_b=2 Qbar, whence K_b=m-r, E=O=0 and
sigma=1-k. Reference-only mass is retained throughout this computation.

In both cases the children have the same numerical costs, despite different
affine shifts. The complete formulas for an active query are
  E=1-s, O=0, sigma=s-k, TC_child=m-1-k-r+2s.
Physical revealed information J and spectral-erasure information B both
equal s here; this equality is a property of this class, not an assumption
for general Boolean functions. The spectator marginal-entropy loss is k.

## 3. A single original owner and every stopping cut

Let C be the cumulative GROSS positive reset price along any physical path.
A positive price is exactly one, requires s=1,k=0, and consumes one unit of
the original W=r_root/2 through a rank drop. The final rank drop, if reached,
has child rank zero and child m'=0, so k=m-1>=1; its price is nonpositive.
If that final drop has not been reached, at least one unit of rank remains.
Therefore, when r_root>=2, at EVERY cut and on EVERY path,
  C <= W-1.
This is a pathwise account; taking physical expectations permits adaptive
and randomized policies. No recycling is needed to prove the bound. With
an old absolute debit 0<=omega<=1/4, the same original W pays all positive
resets and retains at least 3/4. Earlier debits remain booked. When r_root=0
there are no reset costs and W=0; a positive old debit is not covered.

The initial full-product KL admission A0=m-r is charged exactly once.
A0+W=m-r/2<=m<=2 I_root, so the initial reference and original reserve can
both be purchased from the SAME original influence bank of capacity 2 I_root.
No supplied arbitrary reference budget is needed within this class.

At any cut, the exact telescoped source account is
  sum E + E_physical K_terminal = A0 + E_physical sum sigma,
as O=0. Here K_terminal is for the actual reset product at that cut.
Also H_terminal<=r_root pathwise. Hence, for r_root>=2,
  sum E + E_physical(K_terminal+H_terminal) + omega + 3/4
    <= A0+C+r_root+1 <= A0+W+r_root
    = m+r_root/2 <= 3 I_root.
The sum E denotes the physical reached-node weighted sum. Both full terminal
entropy and terminal reference KL are retained, as are all previous charges.
This is a reference-history payment theorem for quadratic phases. It is not
a new universal FEI theorem; H=r<=2I for this class is already immediate.

For the stronger OLD RELATIVE QUARTER convention, take one original bank
S=4 I_root, and keep 0<=omega<=S/4 booked forever. It funds A0, all GROSS
positive reset charges (no refund needed), and the stronger terminal-entropy
reservation H_root, all simultaneously. Indeed, when r_root>=2,
  A0+C+H_root+omega <= 3 I_root-1+I_root = S-1.
Thus its residual is at least one unit at every cut, and consequently it also
pays sum E+E_physical(K_terminal+H_terminal)+omega with that residual.
This bank is fixed at the root; all component purchases are debited from it,
and no part of the previously booked old quarter is erased. For r_root=0,
all reference/reset/entropy costs vanish and the residual is at least 3S/4.
The S=4I claim is a safe payment upper bound; no optimality is asserted for
the coefficient four. The sharpness below concerns the separate extra reset
reserve, not the total bank including entropy and previous charges.

## 4. Sharp pending cost before any refund

For k>=1 take m=k+2 data bits z_0,...,z_{m-1}, k additional bits
y_2,...,y_{m-1}, and
  q=z_0(z_1+...+z_{m-1}) + sum_{j=2}^{m-1} y_j z_j.
The n=2k+2 alternating matrix is invertible: a kernel vector first has
z_j=0 for j>=2 from the y rows; then z_0=0 from row z_1; then z_1=0
from row z_0; finally all y_j=0 from the remaining z rows. Thus the root
is bent, its actual product equals its actual law, A0=0 and I_root=W=k+1.
Query all k y bits first, and stop, keeping both outcomes at every step.
Each deletion has s=1,k_new_isolates=0, so E=O=0 and sigma=1.
At the cut the residual star matrix has rank two and all m rows nonzero;
every branch has full terminal H=2 and TC=k. The initial source account was
zero and no E or O was released. Exactly k additional units are necessary
and sufficient for these actual resets. This is a MINIMAL pending reserve,
not merely a gross-billing lower bound. It equals W-1, and k/I_root tends
to one. A coefficient below one multiplying original influence cannot pay
all such prescribed-prefix actual resets, even with a product source root.
Here extra reserve means a reference/outcome reserve beyond initial KL,
without another entropy or outside reserve being supplied to that account.
This does not refute a policy that chooses a different order or full FEI.

## 5. Honest universal boundary

The first unsupported universal step would replace rank/2 by a nonnegative
restriction-stable owner R(f)<=K I(f) that pays every necessary signed
actual reset, retains old debits, and funds initial reference admission for
general Boolean functions. Affine spectral supports, fair reference outcomes,
and the two-unit rank drop have only been proved here for quadratic phases.
Previous A063 dense/sparse selector examples prohibit a general local-query
J, B, or marginal-entropy-drop substitute. No such universal R is supplied.

Independent review requested from A087/A094; finite checking does not replace
that review. All statements here concern exactly the specified fair extension.
