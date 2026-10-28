# Independent A015 review: fixed-polarity mixture obstruction

Source: A008 run20261023T062437Z-account03-A008-gate-label-compression,
MIXTURE_OBSTRUCTION.md and its version1 CLAIMS.json. Exact claim:
A008-RARE-CHILD-MOMENT-AND-FIXED-POLARITY-MIXTURE-OBSTRUCTION@1,
statement hash8665cf2638011cb0dffa64b7c0cad0b347746eeb92dc2541e4bbc262ce55e6e5.
Verdict: HOLDS at the complete stated scope, without repair. This review
does not accept unrelated claims merely because they occur in the source
CLAIMS.json. The new joint dictionary in this run is a separate subsequent
construction, not a repair supplied to the reviewed proof.

## Reconstruction of the probability argument

For the exact offspring law p_c=1/[(c+1)(c+2)], its tail from17 has mass1/18.
Thus at t=17/20, the first17 terms plus t^17/18 bound the PGF from above.
Independent Fraction arithmetic gives
20606392695229053324830943/26240614400000000000000000 <4/5.
No finite mean is asserted. If the height-h descendant functions are bounded
by4/5, any attachment row contributes at most(4/5)(1+zt)<=17/20, by packing.
Conditional multiset probabilities are normalized even when child labels
repeat: independent descendant contributions still multiply, so averaging
them preserves this upper bound. Size/subset choices have total mass<=1.
Induction from the zero height gives the same4/5 bound at every finite
height. Monotone convergence includes all finite successful runs and keeps
infinite/failed mass absent rather than conditioning it away.

Root-set summation, done jointly after the descendant bound, is exactly
[prod(1+(4/5)zx_e)-1]/(zD). Set u_e=(4/5)zx_e. Since sum u<=1/20, product
expansion gives prod(1+u)-1<=sum u/(1-sum u). With D>=A0 this proves16/19.
The z^(-1) is essential because R>=1 and the moment weights R-1, not R.
Neither absent roots nor D are dropped in this derivation.

## Reconstruction on the actual Boolean family

Disjoint AND factors require two positive certificates, and disjoint OR
factors require one complete certificate. Minimality gives precisely the
positive X-transversal plus Y-clause primes and the negative X-clause or
Y-transversal primes. The independent checker enumerates every signed
face on16 mixed-width toy pairs and checks equality of both complete tables;
the general classification follows the preceding completion argument.

On a fixed X clause, summing packing rows bounds all positive lambda by w.
At least r/2 Y clauses therefore have marked-name mass<=2w/r. Their A0 is
at most w/r, so z=1/[16(t_D+A0)]>=r/(48w). The exact integer inequality
(48w)^2<=2^w holds at32 and propagates: the next ratio is
2[w/(w+1)]^2>1 for w>=32. Thus z>=2^(w/2), including arbitrarily tiny
positive weights. The proof does not presume uniform weights or orders.

For a target contained in one clause per block, an X-coordinate can change
along a tree edge only at a Y attachment, whose child is marked by D.
Consequently k_X<=R+M_D, even with repeated names/overlapping subsets.
This NECESSARY condition on every successful output run, rather than one
chosen forest, bounds the full Q_+ by z^[-(k_X-1)]. In the negative table,
the Y coordinates lie in distinct components and the X component is
separate. Summing the necessary root event gives D_X prod D_i/D_-;
D_->=D_X cancels it without a free-root normalization. Packing and the
rarity2^-r bound each remaining D_i by2^(1-r). Thus the full Q_- is at most
2^[-(r-1)k_Y], independently of its own weights and orders.

For k_X>=ceil(w/2), k_X-1>=w/4, while r-1>=w^2/8. Both outputs have mass
at most2^-w^2/8 on the same targets. Every fixed alpha-mixture has this
same bound, including alpha0 or1; posterior selection cannot create mass
outside the full output laws already summed.

## Actual spectral mass, physical influence, entropy guard

One-clause nonempty indicator coefficients have magnitude epsilon p^(r-1).
The joint F coefficient is twice the product, giving squared mass
4epsilon^4 p^[4(r-1)]. At least r*r/2*r/2*r/2 distinct targets qualify,
so their total mass exceeds1/162. Indeed p^(r-1)>1/3 follows directly by
binomial comparison of(1+1/(r-1))^(r-1) with sum1/j!<3. Pivotal counting
gives I(g)=2w p^(r-1); exact disjoint AND composition gives the same I(F),
since the two activation probabilities add to1. Therefore full nonempty
cost/I>w/2592, without assuming FEI or any entropy estimate.

For the entropy guard only, the indicator's normalized square law is a
product of per-clause activation epsilon and a uniform nonempty subset.
Its entropy is bounded by2w+log(e)<2w+3/2. Empty/nonempty decomposition gives
H(g)<=1+4a(2w+3/2), hence H(g)/I(g)<4+9/(2w)<6. The four sectors of F
have entropy<=2 and the combined local normalized-entropy coefficient v0,
so H(F)<=2+H(g)<8I(F), using I(F)>2w/3>1. These are explicit product
calculations, not applications of the general FEI conjecture.

## Validation and limits

code/check.py is a fresh implementation, importing no A008 helper. It
certifies the rational PGF bound;97 parameter inequalities;12 independently
defined marked-tree fixtures through height3 (offspring above6 fails);
all16 small signed-prime tables; and direct physical Walsh/influence
identities, including a16-variable table. Those finite checks do not replace
the analytic height/parameter arguments above. out/exact_checks.json pins
the executed helper. Verdict unchanged: the entire version1 statement
holds, including arbitrary positive feasible packing, all finite output
runs, and fixed normalized mixtures. Arbitrary richer mixtures or new
joint whole-set codes remain outside this refutation, exactly as stated.
