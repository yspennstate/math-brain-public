# A bent child does not need an inherited reference cone

All logarithms are base two. Status: analytic proof, author checked;
independent reconstruction pending. Full FEI remains OPEN.

## 1. Arbitrary inherited reference, one first reset

Let g be a quadratic Boolean phase on even n>=2 variables with nonsingular alternating
matrix A. Its spectral law is uniform on the whole cube, H(g)=n. Start with
ANY normalized reference R positive on that cube, and retain its actual
source-induced transport until an optionally selected first actual product
reset. Use fair extension on zero-source rows. Subsequently allow arbitrary
adaptive queries, product resets, and stopping. No root admission is renewed.
Write K0=KL(p_g||R). At a reached node let E be the conditional erasure KL,
O=KL(fair||predicted reference outcome), and K its actual source/reference KL.
Both E and O are nonnegative. Let sigma=TC(new product)-K(predicted) at each
exercised reset; C is the sum of positive parts of these sigma on a path.

At EVERY stopping cut, with current alternating rank r,

    C + H(current function) <= n.                         (1)

Proof. Before the first reset, C=0 and H=r<=n. Let d be the number of rank
drops before that first reset (each lowers rank by two). If a queries were
active when made, the number of active rows remaining is at most n-a:
deleting an active row removes at least that row, and never creates activity.
Since d<=a, the current product TC=m-r satisfies

    TC <= (n-a)-(n-2d) = 2d-a <= d.

Thus the positive first reset costs at most d, regardless of R, because
K(predicted)>=0. Following that reset the actual product is a uniform affine
superspace containing the actual spectral support. The prior stage's interval
lemma applies: each later positive reset costs at most the number of rank
drops since the preceding reset, including ordinary query prefixes. Consequently
C<=D at every cut, where D is the TOTAL number of rank drops from the original
bent root. Hence C+H <=D+(n-2D)=n-D<=n. This also proves C<=n/2-1: if the final
rank drop has occurred, its reset interval ends with TC=0 and has no positive
charge, while before it at least one rank unit remains. No cone assumption is
made on R before its first reset. A reference outside the cone is permitted.

For completeness the interval lemma after a product reset uses the following
facts. Actual transported references are mixtures of uniform affine superspaces
containing the actual support. Outcomes are fair. Rank-drop queries release
E=0; other queries release at most one bit. Over an interval starting at a
product, with t start-active coordinates queried, u newly isolated unqueried
coordinates and d rank drops, TC_end-TC_start=-t-u+2d and sum E<=t-d. Therefore
sigma=TC_end-TC_start+sum E<=d-u<=d. Start-isolated coordinates release zero;
newly isolated coordinates must be included among the t queries. The last
rank drop leaves TC=0. The superspace-mixture transport proof and fair
zero-source convention are pinned by the prior PROOF_PREFIX.md.

At a physical query the exact source chain rule is

    K_parent = E + O + average K_predicted_children.      (2)

Indeed erasure first subtracts conditional KL E, then applying the same
outcome kernel to source and reference preserves the residual joint KL;
disintegrating that joint law into its fair physical outcome and conditional
spectral reference gives O and the average child KL. A reset adds sigma to K.
Telescoping (2), keeping O rather than calling it physical information J,
gives at every adaptive stopping cut

    sum_reached(E+O) + expected(K_terminal+H_terminal)
       = K0 + expected(sum sigma + H_terminal)
       <= K0+n.                                         (3)

The expectation uses physical reach probabilities, not reference branch
probabilities. Finite-dimensional trees have at most n queries, so there is
no optional-stopping limit or integrability issue. Positivity of R on actual
source support ensures positive reference outcome mass at every reached node.
Randomized policies are covered by conditioning on their independent seed.

## 2. Crossing the actual cubic selector with the SAME original account

Let n=2s>=4 and N=2^n. The selector's physical children are

    dense(u,v)=(-1)^(sum_j u_j v_j),
    sparse(u,v)=(-1)^((sum_j u_j)(sum_j v_j)).

Start the original (n+1)-variable Boolean selector with its ACTUAL full product
reference. Query the selector first, without resetting. On the dense outcome
allow ALL ordinary prefixes, optional actual product resets and stopping rules
from section 1. On the sparse outcome permit arbitrary queries and stopping,
but KEEP the inherited reference and never reset it to the product. This is an
eligible selected policy, not a claim that every policy has cheap admission.

Both children have all data influences 1/2. Dense has rank n and sparse rank
2. The erased original reference is uniform on N masks. Direct kernel transport
gives pi_dense=N/(N+4), pi_sparse=4/(N+4), and the ACTUAL inherited references

    R_dense(t)=4/N^2 on L, (N+4)/N^2 outside L,
    R_sparse=p_sparse=uniform on L,
    L={0,U,V,U+V}.

R_dense is positive and is outside the old unweighted cone. Section 1 applies
without repairing that cone. On the sparse branch, reference equals source;
the common kernel keeps them equal. Thus E=O=K=0 throughout that subtree
(including reference-only extensions, which have zero mass here), while H<=2.
Its n-2 product-admission gap is never incurred. This is a substantive policy
change, not a new bank, an erased debit, or a claim that the gap vanishes.

Let H0,I0,K0 denote ORIGINAL root quantities. Let M0=sum_i h2(Inf_i).
K0=M0-H0, M0<=n+1, I0=n/2+Inf_selector>=n/2. The ordinary entropy query
identity H0-average H(children)=B+J>=0 implies H0>=n/2+1.
The source chain at the selector pays its actual E and O and both inherited
child KLs from K0. Applying (3) on the dense subtree and the zero-K sparse
subtree gives, at EVERY cut after the selector,

    L := sum_reached(E+O)+expected(K_terminal+H_terminal)
       <= K0+n/2+1
       <= M0 <= n+1.                                    (4)

At the root cut L=K0+H0=M0, so the same bound covers stopping before the
selector and randomized mixtures of stopping there and continuing.
One fixed original S=4I0 account, with an already-booked debit
0<=omega<=S/4=I0, therefore retains

    S-omega-L >=3I0-(n+1)>=n/2-1>=1.                    (5)

No child rank owner or source admission is issued. The exact signed sum,
full terminal entropy and KL, and all accumulated E/O stay in L. (4) is an
expectation account at physical cuts, not an assertion of equal branch cash.
For asynchronous branch stopping, each conditional subtree inequality applies
to its own stopping rule, giving the same root-weighted bound.

## 3. Boundary and the first unpaid universal step

The inherited dense reference needs no repair; full original support supplies
the finite first-reset rank bound. The sparse inherited reference needs no
product admission under the selected policy. This closes the exact one-selector
boundary fixture of the prior stage from the SAME rate-four original account.
It does not close arbitrary selectors between quadratic phases: an inherited
rank-deficient child can have TC already large before any rank drop, while an
unfunded product reset would charge that inherited gap. The first unsupported
line is a noncircular original influence-priced choice of retained reference
and eligible reset cuts for such arbitrary children, and then arbitrary
Boolean cores. Physical J is not substituted for E, O, B, or a source invoice.
