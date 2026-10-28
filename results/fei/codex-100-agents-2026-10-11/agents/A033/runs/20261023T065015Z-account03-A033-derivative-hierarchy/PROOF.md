# Fixed-strength profile conversion has no universal local influence price

Units: entropy, CE and KL in bits; influences are on original physical
uniform bits. This refutes a local reset supplier, NOT FEI. Both tag
children, both seed children, full terminal references and old debits remain.

## 1. Actual Boolean family and exact current state

Let g_m be majority of 2m+1 bits, m>=1. On disjoint blocks of width L>=3
put h(x)=g_m(product of the bits in each block). Let a,b be the ORIGINAL
A079 four-controller mask, b=1-a^2, beta=E b^2=3/8. At each of the two
actual physical tag children use G_sigma=a+sigma b h, sigma=+/-1.
The seed is balanced. Supply the reference R=P_h. Its true full
initial price is retained; it is not assumed influence-priced for free.

Query one physical bit from any block, leaving at least two bits in
that block. The preceding A033 run20261023T063507Z PROOF sections1--3
gives the exact Fourier injection: a core monomial is supported on
the union of its remaining blocks, and exposed bits change only signs.
At the queried fiber at most one actual/reference atom is occupied.
Hence BOTH children have the same full squared spectrum as the inherited
marginal, with B=JS=occupancy KL=0. Their ACTUAL signed vacuum atoms
are unchanged, and their FULL controller-vacuum-plus-tail calibration
refund is also0. With this TRUE-spectrum incoming reference, this
includes every nonempty sign-bin refinement or ANY other partition:
the inherited wrapper reference is the actual child law, so its relative
entropy is zero before any partition is chosen. Thus A097's new
nonisospectral phase refund does not bypass this example. For arbitrary
nonflat calibrated R the preceding stage still proves zero occupancy
and vacuum/tail coarse refund, but finer nonempty calibration MAY release
prepaid source KL. That stored liability is not a new physical phase
refund, and its absence is asserted here only at R=P_h.

At a remaining singleton frequency in the still-multibit queried block,
the inherited seed reference and true law are both zero. Prescribe that
nonempty frequency as target S. Reset the CURRENT conditional seed tail
to N=(1-epsilon)R_tail+epsilon S, 0<epsilon<1, preserving every actual
signed vacuum atom. This is a genuinely changed profile. Every old true
tail likelihood is multiplied by EXACTLY 1-epsilon; every reference-only
atom retains its old1-epsilon component. Consequently the reset cost,
including complete terminals, is EXACTLY

  z=beta log2(1/(1-epsilon)).                             (1)

The erasure and every current query refund are0, so this is also the
complete erasure-plus-mean-child-CE increment at either tag child.

## 2. All finite local rates fail at fixed strength

For majority the original influence of one encoded physical bit is

  Inf_v(G_sigma)=beta a_m,
  a_m=binom(2m,m)/4^m.                                  (2)

Indeed flipping that bit flips the corresponding block product; majority
changes iff the other2m core bits tie, independently of all block signs.
Both restrictions retain all the other core randomness; no conditional
core or spectator is discarded.

For EVERY m>=0,

  a_m^2<=1/(3m+1).                                      (3)

Proof: a_0=1, a_(m+1)/a_m=(2m+1)/(2m+2), and the EXACT polynomial
identity (3m+1)(2m+2)^2-(3m+4)(2m+1)^2=m>=0 proves the inductive step.
For epsilon=1/64, let ell=log2(64/63). Integrating1/x on(63,64)
gives ln(64/63)>1/64; dividing by ln2<1 shows ell>1/64.
For ANY finite real K>=0 choose integer m>=1 such that

  3m+1>4096K^2.

Then K a_m<1/64<ell and (1)--(2) imply the STRICT local underpayment

  B_v+mean CE_child_new-CE_parent > K Inf_v(G_sigma).      (4)

This holds at BOTH tag parents, even after adding ALL zero current
occupancy/phase/coarse refunds. Rates K=2,4,17,100 have finite rational
parameter certificates in out/validation.json. The all-K theorem follows
from (3) and the displayed choice of m, not a floating sweep.

The stronger quantitative statement is that the required ratio is
ell/a_m>=ell sqrt(3m+1), hence diverges. Equivalently ANY local rule
that pays this disjoint target by K Inf MUST choose strength satisfying

  log2(1/(1-epsilon_m))<=K a_m,                          (5)

so epsilon_m necessarily tends to0. Merely replacing the zero refund
by a fixed constant-strength local influence allowance cannot be universal.

## 3. Necessity guard: the positive conversion is prescribed, not inevitable

This does NOT prove that an eventual FEI proof must make this wasteful
off-image conversion. Before block completion every actual spectral law
stays on the same quotient image (up to physical labels). The original
finite core reference can simply be transported through the ENTIRE
window at constant full CE; all adaptive transcripts are independent
of the still-unrevealed block products. To see the latter directly,
condition on a transcript that leaves at least one bit in every block:
each remaining block product is independent uniform, so their vector
is uniform whatever the exposed bits and query choices. This explains
why adaptive finite lookahead cannot consume the core entropy.

An off-image target is therefore not intrinsically necessary within
this window. More generally, for any normalized reference Q after such
a history, let q=Q(image)>0. For true p supported on the image,

  CE(p,Q)=CE(p,Q|image)-log2(q).                         (6)

Thus mass outside the current attainable image has the exact positive
normalization bill -log2(q). It may be retained by an independently
prescribed future reference, but cannot be called a needed local
calibration without an argument. Removing it is an EXPLICIT reset
with (6)'s accounted refund, not a free change of reference.

The correct next bottleneck is consequently a NECESSARY profile change
at a block-completion or genuinely changed-spectrum frontier, with a
global original ancestor bank. Our counterfamily leaves that possibility
open. A096's d^2-funded and A097's nonisospectral rules remain valid;
they correctly authorize zero energy here. No initial universal source,
new high-degree Booleanity payment or full FEI theorem is supplied.

## 4. Completion boundary and full hierarchy

For g=[-1,1,1,1] with width2 blocks, expose one physical bit of its first
block, then query the last bit of that block. Before that last query
H=2; its two actual children have H=0, marginal spectral entropy1,
conditional erasure1 and JS1. The zero-window theorem must stop at
block completion. The independent checker reconstructs this from truth
tables and direct characters, giving a positive control for that boundary.

All our functions are actual Boolean formulas and satisfy ALL signed
convolutions sum_S fhat(S)fhat(S xor U)=1{U=empty}, on every physical
restriction, and all complete derivative split identities AB=0,
A^2+B^2=1. The nonempty derivative grids alone are insufficient admission.
The established fixed-order dyadic G_(K,w) and distinct atom-cap-prefix
no-go directions are retained, not retried; the latter's original explicit
construction/checker remains missing locally, so import is summary-only.

The first unsupported universal line is a theorem selecting which
conversions are necessary and paying their full signed cost from the
SAME unused original influence through a completion/selection tree,
without assuming that the arbitrary core's initial source was cheap.
That is still OPEN. The generic probability identity (6) is not a
new Booleanity-specific inequality excluding nonBoolean controls.
