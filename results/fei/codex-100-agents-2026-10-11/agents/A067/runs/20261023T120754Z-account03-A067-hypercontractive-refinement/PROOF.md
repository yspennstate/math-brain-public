# Arbitrary adaptive refinement inside all retained clean exits

Uniform finite Boolean signs, physical uniform restrictions, full Fourier
labels, base-two entropy and normalized squared spectra are used throughout.

## 1. Sharp local stopping price

Let g=epsilon*(product over l distinct character coordinates)*b_k on k
disjoint canonical quadratic pairs, with any additional dummy coordinates.
All coordinates in these three groups are disjoint. Its Fourier law is
uniform on 4^k labels, so H(g)=2k and I(g)=k+l.
Restrictions remain in this class, including global signs and constants.

For any physical query j the complete actual entropy debit at rate3 is
e_H(j)=H(g)-(H(g_0)+H(g_1))/2-3 Inf_j(g). There are exactly three cases:

* Intact quadratic coordinate: Inf=1/2; both children have k-1 intact
  pairs. The partner becomes a dummy on outcome0 and a character on
  outcome1. The actual entropy drop is2, hence e_H=1/2.
* Character: Inf=1, entropy drop0, hence e_H=-3.
* Dummy: Inf=0, entropy drop0, hence e_H=0.

For EVERY finite adaptive physical stopping tree, including decisions based
on all preceding outcomes, its root-relative expected signed debit is at
most k/2. Indeed along each path at most k distinct pairs can be hit for
the first time. Each such hit contributes1/2, while all other contributions
are nonpositive. Averaging this pathwise bound requires no independence
of the adaptive choices. Equivalently V(g)=k/2 is a Bellman super-solution:
e_H(j)+E V(g_child)<=V(g) in every case. Stop contributes0.

The bound is attained: query exactly one coordinate from each initial pair
and then stop, retaining ALL outcome branches. This has expected debit k/2.
Thus the exact supremum over all adaptive stopping trees is k/2, not merely
a dimension-dependent upper estimate. More generally at fixed rate C>=0
the exact optimum is k*max(0,2-C/2); this follows from the same three cases.
Only C=3 is used in the inherited payment below.

### Extension to every quadratic Boolean phase

The upper bound does not require disjoint quadratic pairs. Let
g(x)=(-1)^q(x) for ANY degree-at-most-two polynomial over F2, with arbitrary
linear and constant terms. Let M be its alternating polar matrix and r its
rank over F2. Then EVERY adaptive stopping tree has total expected actual
rate3 debit at most r/4. Matching phases attain this bound, although a
particular overlapping quadratic need not attain it.

Here is a self-contained entropy calculation. The autocorrelation
E_x g(x)g(x+h) vanishes unless h is in ker M; on ker M it equals
(-1)^(q(h)+q(0)), a character of that subspace. Fourier inversion therefore
makes the squared spectrum uniform with mass2^-r on one affine coset of
(ker M)^perp, of size2^r. Thus H(g)=r. Fixing a coordinate deletes its row
and column from M; the rank drops by0 or2, independently of the fixed bit.
An alternating matrix has even rank and this deletion changes rank by at
most2. If the deleted row is nonzero, the physical derivative is a
nonconstant affine sign, so Inf=1/2. Its rate3 actual debit is respectively
-3/2 or1/2. If the row is zero, the coordinate is a character or dummy,
with debit-3 or0. Hence V(g)=r/4 is a Bellman super-solution for every
coordinate and both actual children. This proves the all-dimensional
upper bound, including all adaptive choices, without any assumption on
the inherited reference. In particular there is no logarithmic dimension
or degree factor in this quadratic stopping payment.

## 2. Inherited reference and the FULL KL change

Let Q_L be any inherited probability law supporting the actual spectrum
P_L on a clean leaf L. It may vanish off that support. Every
descendant uses ONLY its marginal over the physically queried coordinates;
both physical children are retained. Write K_L=KL(P_L||Q_L).
The physical square-sum identity ensures continued support domination:
if a marginal Q row vanishes, both actual child coefficients there vanish.
The complete source debit E_Q(L) and actual debit E_H(L) of a continuation
tree satisfy the exact identity

 E_H(L)=E_Q(L)+sum_descendant reach_from_L*K_descendant-K_L.

This follows by CE=H+KL at every node, with the interior KL terms cancelling.
It does NOT say the source debit has the same sign as the actual debit.
In particular the old K_L is subtracted, never deleted or reissued as an
independent budget. Dummy queries can have positive CE debit with zero
actual entropy debit; their compensating inherited KL release is retained.

The new result here is the sharp positive-cost bound from section1. The
CE/H/KL identity is standard background accounting, not a new payment.

## 3. Apply to the same diminished A088 source, without renewal

Use EXACTLY A088 run20261023T105519Z PROOF sections1--5. For each m>=2,
take its original G_m with unchanged old z debit D, original Q_c, original
rate3 chosen once, r>4^-m/8 and I_X=m+(2m+1)4^-m/2.
At every paid cut 0<=H<=T<=m, w is queried once after H completed edited
pairs and T-H further pairs are completed on w=0. The cut retains EVERY
earlier clean exit, original clean b_m sibling, and the active edited leaf.
Its entire actual signed debit satisfies E_old<71/96, and its remaining
ORIGINAL account is R_old=r+I_X-E_old>m-71/96.

Every retained clean leaf has the class in section1. This includes the
original b_m, the w=1 bent exit, first-one exits with a character, and
second-one bent exits before and after w. Assign any finite adaptive clean
continuation tree independently to each such retained leaf. The choice of
tree may depend on the full inherited history. The active edited leaf is
left at the same paid cut. A constant leaf is also clean with k=0.

Let a_L be each original G reach and k_L its number of intact pairs.
Since sum_clean a_L<=1 and k_L<=m, the ADDED complete actual debit obeys

 F=sum_clean a_L E_H(L) <= (1/2)sum_clean a_L k_L <=m/2.

Consequently, after ALL such continuations, the SAME original remaining
reserve, with no replenishment, satisfies

 R_new=R_old-F=r+I_X-(E_old+F)
      >m/2-71/96 >=25/96>0.

This pays every adaptive clean continuation, including one actual data query
inside every retained clean exit simultaneously. A single intact query in
leaf L has exact added actual debit a_L/2. It need not have nonpositive
source debit, and its full two-child KL conversion is never suppressed.

For explicit bookkeeping let K_old be the full KL bill at the paid cut,
and K_new the full bill at the refined cut, with active edited leaf unchanged.
Then E_new,Q=E_old,Q+sum_clean a_L E_Q(L) and
K_new-K_old=sum_clean a_L*(sum_desc reach_from_L K_desc-K_L).
Thus E_new,H=E_old,H+F=E_new,Q+K_new, since the original references were
actual spectra and originally had KL0. The complete signed banks obey
S_new,H-(D+E_new,H)=r+I_X exactly. Negative inherited banks remain signed.

The legacy rate-two invoices also remain explicit. If J_old is A088's
already booked removed influence and J_clean the actual root-weighted
influence removed by these new queries, then
E_new,H,rate2=E_new,H,rate3+J_old+J_clean. The same relation holds for CE.
No claim that J_clean<1/2 is made: querying all remaining clean coordinates
can make it large. The old bound J_old<1/2 is not reused for new queries.

## 4. Dependency reconstruction and the actual universal gap

The analytic source allowance71/96 is an existing A088 result, not claimed
as new here. Its complete derivation is independently reconstructed in
DEPENDENCY_REVIEW.md and literal old frontiers are checked directly from
the original Boolean truth tables, full references and all terminal bills.
The new clean Bellman price does not assume flatness of the inherited Q.

The sharp clean stopping bound is Boolean and restriction-structural, not
a general real-valued entropy-versus-mean-degree inequality. An untouched
pair phase filter can still imitate proper prefixes, as A088 noted, but
once that pair is queried the real filter need not preserve child norms or
these three Boolean cases. No universal Boolean convolution estimate is
claimed. Standard one-coordinate influence charging remains false in general.

The first unsupported line is now a supplier of comparable residual/phase
control for a noncanonical EDITED Boolean core, or a bound of this Bellman
kind beyond quadratic phases. The quadratic extension closes clean leaves
with overlapping interactions, but supplies no such edited ancestor bank.
All adaptive clean refinements of the supplied canonical paid frontier are
closed; generic transport alone and another isolated class H/I estimate are
not the next step. Full FEI remains OPEN.
