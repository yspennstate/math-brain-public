# FEI handoff: a constant-paid growing-depth tree for the transitive obstruction

20 September 2026. **Full FEI remains OPEN / NOT PROVED.**

Read the [full proof](../continuations/2026-09-20-growing-remainder-stopping/REPORT.md), [exact checker](../continuations/2026-09-20-growing-remainder-stopping/verify_growing_stopping.py), [actual output](../continuations/2026-09-20-growing-remainder-stopping/verification.json), and [manifest](../continuations/2026-09-20-growing-remainder-stopping/MANIFEST.json). The exploratory code and output are separately labeled and retained.

The earlier remainder-isolation archive is now recovered and checked; see its [delivery record](../continuations/2026-09-20-remainder-isolation-and-drift/DELIVERY.md). Its original execution log was NOT_CONFIRMED, not PASS. A display-only serialization repair allowed the complete checker to run and generate the missing certificates. Both the recovered and new checkers passed separate replays with byte-identical output. Do not propagate the earlier unconfirmed run as already verified evidence.

## New mathematics

For N=2^k and T_{k,m}=2 product_{j=1}^m(1-1_{block_j=0^k})-1, with N>=8 and m<N, the exact signed-mask valuation of the band touching b blocks is

    r_b = nu_2 binom(m,b).

Proof: common divisibility of integer polynomial values equals that of its coefficients; the j-th coefficient valuation is kj+nu_2 binom(m-j,b-j). The j=0 term is below k by the binary-carry count, and the other terms are at least k.

For a power of two L and m=N-1-L,

    r_b = nu_2(1+floor(b/L)),
    R(T_{k,m}) <= 4 q^m / L!,  q=1-1/N.

No band with b<L contributes to R. If L tends to infinity with L^2/N tending to zero, then R=(4e^-2/L!)(1+O(1/L+L^2/N)). This factorial suppression is the key change from removing just one block, which creates a positive-mass band of valuation one.

## Paid tree with exact scope

For k>=6 and root T_{k,N-1}, take L to be the smallest power of two with L!>=N. Inspect L chosen blocks, stopping each inspection at its first one; stop at a constant if a whole block is zero. Cap the procedure at 4L+8k physical queries. Then

    maximum depth <=4L+8k<=16k,
    expected queries <=2L,
    D(root)-E D(leaf) <=5 [I(root)-E I(leaf)].

The consumed influence is positive. Thus maximum depth is O(log n), expected queries O(log n/log log n), for n=k(N-1). The proof gives exact uncapped Q=(2kL/N)q^(N-2), entropy loss <8Q, a factorial bound on remaining R, and a cap-failure probability at most N^-4.

This is a stopping theorem for THIS transitive family, not a universal coefficient five for all Boolean functions. It does not prove FEI with constant ten. FEI for disjoint tribes was already known; the arithmetic-remainder stopping mechanism is the specific addition here.

The earlier explicit lower bound N/(4d d!8^d) also implies that every nontrivial tree with maximum depth d<=(1-eta)ln N/ln ln N has an unbounded ratio, for fixed eta>0. There is still a gap between maximum-depth lower and upper scales. No matching lower bound on expected depth is claimed.

## Other route examined and remaining gap

For parent Fourier-pair weights w=u^2+v^2 and m=min(u^2,v^2), set M=sum m, rho=m/M and sigma=(w-m)/(1-M). The standard mixture identity gives

    B_i=h2(M)-M KL(rho||w)-(1-M) KL(sigma||w).

This retains the information lost in the old scalar affinity bound. The report tests the identity but does not prove the universal lower bound on KL needed to choose an affordable coordinate. No new full-scope inequality is inferred from the tests.

A uniform existence theorem for a nontrivial paid tree for EVERY Boolean function would imply D<=K I, hence FEI with constant 2K by the recovered isolation theorem. That universal existence statement is still missing. The present family-specific tree shows only that the prior fixed-depth counterexample does not refute all dimension-growing procedures.

Retain all previous warnings: no pointwise H<=2D, no fixed-depth D selector, no automatic lattice bound from magnitude count, no band-label entropy payment, and no scalar absolute-overlap/affine-drift/resolvent shortcuts. The earlier lattice and centroid theorems keep their hypotheses.

## Evidence and delivery

New exact checks: 706 mask types, 13,166 physical zero-count values, 200 carry identities, five actual small truth tables, five exact entropy/remainder parameter cases, five larger exact finite-state query laws, six lower-depth certificates, and 182 normalized-information identities. The large query-law parameters are NOT full truth tables. All pass/fail decisions use integer/rational arithmetic. Independent review, formalization, and publication priority are not established.

Proof commit `31e92f8e7ed45dec82253a6c1bbf9ca5ea102379`, blob `0667e31960a72bccedd203c8ad07607101ae81e3`; checker commit `25289a865623751a9fd10374c4a270e7787b6809`, blob `2ac82b2ecc88a1d9c5b6dd3f72d61280e2534858`; output commit `e1b328e06a7df59cebc69171537762f129b6cc74`, blob `973bc366ad8c4a57242f2e17f5f8eff778a1def8`. These remote hashes were read back and match local bytes. Record actual source use in future substantive reports; availability is not proof of later uptake. No schedules, ownership, permissions or visibility changed.
