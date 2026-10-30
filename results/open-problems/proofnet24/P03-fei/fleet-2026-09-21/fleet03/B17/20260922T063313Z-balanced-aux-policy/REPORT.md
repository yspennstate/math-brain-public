# B17 — every balanced auxiliary restriction of the nine-host seed makes the physical core selector cheaper

**Classification:** `ESSENTIAL_STEP_APPLIED / SOURCE-RESTRICTION-POLICY-STRENGTHENED`.  
**Full unrestricted FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact candidate and peer results consumed

The live all-gate target is the exact gate inequality `(G)`.  I do not reopen its proof here.

The named compatible cross-account result consumed substantively is fleet04/B18,

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B18/20260922T031308Z-global-shared-core-invariant/REPORT.md`,

which fixes the sharpened shared-core center and quadratic lift

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(p)=\Gamma_{\rm RO}(p)+a^\dagger p(1-p),
\qquad a^\dagger=0.268204856.
\tag{1.1}
\]

I apply that center to a different source-valid object: **physical restrictions of the external 18-input nine-host seed itself**.  These restrictions need not remain an exact instance of the abstract transform to which the fleet04/B18 theorem applies.

The physical policy under attack is fleet01/B14's `SIGNED-SHARED-CORE-9`: reveal the nine genuine outer-core coordinates.  B14 proves price `<6.528` for an exact nine-host transform with arbitrary balanced Boolean source and signed singleton.  The old missing implication for this run is whether asymmetric fixing of the auxiliary host coordinates can produce a balanced physical descendant on which the same nine-core reveal becomes more expensive, in particular expensive enough to cross the much sharper center (1.1).

## 2. The complete balanced auxiliary-restriction lattice

Use the exact recovered Numaro seed representation.  There are nine core coordinates `x_0,...,x_8` and nine auxiliary host coordinates `y_0,...,y_8`.  The core truth table has signed sum `18`.  Each auxiliary host changes exactly two core cells from `+1` to `-1`; the nine pairs are disjoint.

Keep all nine core coordinates free.  Let

- `F` be the set of free auxiliary coordinates, `r=|F|`;
- `O` be the fixed auxiliary coordinates set to one, `m=|O|`;
- every remaining auxiliary coordinate is fixed to zero.

A fixed-one host lowers the core signed sum by `4`.  A free host lowers the signed sum averaged over its two states by `2`.  Hence the resulting gate is balanced exactly when

\[
18-4m-2r=0,
\qquad\text{i.e.}\qquad r+2m=9.
\tag{2.1}
\]

Thus necessarily

\[
r\in\{1,3,5,7,9\},\qquad m={9-r\over2}.
\]

The complete number of balanced restrictions is therefore

\[
\sum_{r\in\{1,3,5,7,9\}}
\binom9r\binom{9-r}{(9-r)/2}
=630+1680+756+72+1
=\boxed{3139}.
\tag{2.2}
\]

This is the full class, not a sampled battery.

## 3. Exact influence formula

The nine host pairs have a useful geometry.  Within each host pair the two cells are adjacent in the nine-cube; there are no adjacency edges between distinct host pairs.  For each pair, among the sixteen external incident edges, exactly eight go to `+1` core cells and eight to `-1` core cells.  Therefore flipping either complete host pair from `+1,+1` to `-1,-1` leaves the core edge boundary unchanged.

The unreduced core boundary is exactly `513`, so every fixed auxiliary pattern has core total influence

\[
I_{\rm core}={513\over256}.
\tag{3.1}
\]

Each free auxiliary coordinate disagrees on exactly its two host cells, hence has influence `2/512=1/256`.  Averaging over the other free auxiliaries does not change (3.1).  Consequently every balanced restriction with `r` free auxiliaries has the exact total influence

\[
\boxed{I_r={513+r\over256}},
\qquad
\boxed{I_r-1={257+r\over256}}.
\tag{3.2}
\]

No numerical Fourier estimate is used for (3.2).

## 4. The B14 core-block price collapses exactly to the balanced gate ratio

Reveal the nine physical core coordinates `X={x_0,...,x_8}`.  At a fixed core point, the remaining gate on the free auxiliaries is either

1. a constant, or
2. a single unbiased auxiliary literal, if that core point is one of the two cells of a free host.

Both kinds of residual have spectral entropy zero and Poincare quantity

\[
P(g)={I(g)\over4}-p_g(1-p_g)=0.
\]

Hence for every balanced restriction in (2.2), the exact B14 block drop satisfies

\[
L_X(F)=H(F),\qquad
4Q_X(F)=I(F)-1,
\]
so its physical block price is

\[
\boxed{
\rho_X(F)={L_X(F)\over4Q_X(F)}
={H(F)\over I(F)-1}.
}
\tag{4.1}
\]

There is no terminal exception payment to estimate on this lattice: it vanishes identically after the physical core reveal.

## 5. New exact transition theorem

The finite certificate computes the integer Walsh transform of every one of the 3139 gates, checks Parseval exactly, and encloses every logarithm by a rational positive-remainder atanh series.  The widest ratio interval is below `1.46e-23`.

There is a natural balance-preserving upward move in the restriction lattice.  At any node with `r<9`, choose one fixed-one auxiliary `j` and one fixed-zero auxiliary `k` and make **both** free.  Then `r` increases by two and `m` decreases by one, so (2.1) remains true.

There are exactly

\[
630(4^2)+1680(3^2)+756(2^2)+72(1^2)
=\boxed{28296}
\tag{5.1}
\]

such directed moves.  The exact interval checker proves, for every one of them,

\[
\boxed{
{H(F')\over I(F')-1}>{H(F)\over I(F)-1}.
}
\tag{5.2}
\]

The smallest certified increase is

\[
\boxed{
R(F')-R(F)>0.01478999088202595837.
}
\tag{5.3}
\]

Every nonterminal balanced restriction has at least one fixed-one and one fixed-zero auxiliary, so it has at least one move of this form.  Iterating (5.2) reaches the unique node with all nine auxiliaries free: the original 18-input seed.

Therefore:

### Theorem 5.1 — auxiliary restrictions cannot worsen the core selector

Among **all 3139 balanced restrictions obtained by fixing only auxiliary host coordinates and keeping all nine physical core coordinates free**, the original unrestricted 18-input seed uniquely maximizes both the block price (4.1) and the balanced center requirement.

The exact interval maxima by number `r` of free auxiliaries are:

| `r` | count | certified maximum of `H/(I-1)` |
|---:|---:|---:|
| 1 | 630 | `< 6.459372281637856` |
| 3 | 1680 | `< 6.475438356724385` |
| 5 | 756 | `< 6.491595306028880` |
| 7 | 72 | `< 6.506724016198907` |
| 9 | 1 | `< 6.521845710923047` |

For the unique top node the rigorous interval is

\[
6.52184571092304657565812962830536
< R_{18} <
6.52184571092304657565814422591013.
\tag{5.4}
\]

The recovered source truth-table SHA-256 is independently reproduced as
`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

## 6. Apply the current fixed center and report the requested margin

From (5.4) and (1.1), every gate in this entire restriction lattice satisfies the strict center reserve

\[
C^\dagger-R(F)
> C^\dagger-R_{18}
>\boxed{5.50307695342434\times10^{-6}}.
\tag{6.1}
\]

In the owner's gate-margin units relative to the old read-once center `C_0=6.4548`, a balanced gate has

\[
c_G=4\left({H(G)\over I(G)-1}-C_0\right).
\]

Thus the worst member of the whole restriction lattice satisfies

\[
\boxed{c_G<0.268182843692187},
\tag{6.2}
\]

whereas the live quadratic lift is `a^dagger=0.268204856`.  The certified lift reserve is therefore

\[
\boxed{a^\dagger-c_G>2.20123078137\times10^{-5}}.
\tag{6.3}
\]

So the attempted adversarial bridge is **REFUTED**:

> fixing auxiliary hosts asymmetrically can make the physical nine-core selector more expensive than the original source, or can turn this source geometry into a counterexample to `C^dagger`.

It cannot.  Every balance-preserving removal of auxiliary freedom moves strictly *away* from the dangerous center.

## 7. What changes and what remains open

**Exact candidate version tested:** `C^dagger=6.521851214`, `a^dagger=0.268204856`.

**Old missing implication:** B14's exact nine-core selector theorem controls an exact shared-core transform at `<6.528`, but did not cover the asymmetric physical descendants formed by fixing host auxiliaries, nor certify them at the sharper `C^dagger` center.

**New proved implication:** the entire balanced auxiliary-restriction lattice has an exact monotone block-price orientation toward the original source, and the original source itself remains strictly below `C^dagger`.  The same physical nine-core block therefore closes every one of these descendants at the sharper center, with zero terminal exception payment.

**Consumed peer artifact:** fleet04/B18 `20260922T031308Z-global-shared-core-invariant/REPORT.md`, applied to the fixed center being adversarially tested; fleet01/B14 supplies the physical nine-core selector being challenged.

**Replacement obligation:** an adversarial descendant of this source must now either fix at least one core coordinate, change the host/core geometry, or move to a genuinely nonuniform product-bias point.  Auxiliary-only balance-preserving restrictions are exhausted by Theorem 5.1.  The next useful source-valid attack is a core-coordinate restriction/nonuniform-bias deformation, not another auxiliary restriction sweep.

**Next recipient:** fleet01/B14 for physical-policy integration and fleet04/B18 for the fixed-center candidate state.

**Implication to full FEI:** this closes one exact restriction lattice and strengthens one physical selector.  It does **not** prove `(G)` for arbitrary composition-prime gates or arbitrary product biases.  Full uniform-cube FEI remains **OPEN / NOT PROVED**.
