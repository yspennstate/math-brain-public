SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-24T00:48:17Z.
attacking: local-row spectral reserve: allow arbitrary huge added signed modes in q physical row directions while paying only the first unreserved local square-energy singular value; compose with account04/B12 multihub shear.

# B12 handoff — local spectral-leakage reserve

Canonical mathematics: `yspennstate/math-open-problems@9e25f855f8a00cd57febbd63dc029af0836c57a2`

Main path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T004817Z-qform-eigenvalue-r45/REPORT.md`

Later-owner projected-crossing application: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T004817Z-qform-eigenvalue-r45/PROJECTED_CROSSING_ADDENDUM.md`

## Proved

For an ORIGINAL-coordinate bank `H`, let `P_H` be its row selector and write

`A=A_*+sum_j T_j`.

Choose integers `q_j>=0`, put `Q=sum_j q_j`, and define the local packet tails

`tau_j=s_(q_j+1)(P_H T_j)`.

Then, for every `k+Q<=|H|`,

` s_k(P_H A) >= s_(k+Q)(P_H A_*) - sum_j tau_j. `

Equivalently,

` sqrt(lambda_k((A^2)[H,H])) >= sqrt(lambda_(k+Q)((A_*^2)[H,H])) - sum_j tau_j. `

For a symmetric spectral packet `T=sum theta_a v_a v_a^T`,

` tau_q(H,T)^2 = lambda_(q+1)(sum theta_a^2 (P_H v_a)(P_H v_a)^T). `

In particular, if the `H`-projections of all eigenvectors with `|theta_a|>h` span at most `q` dimensions, then

` s_(q+1)(P_H T)<=h. `

Thus arbitrarily many arbitrarily large added eigenvalues of either sign cost only the dimension of their physical footprint; all remaining full-rank small spectrum costs only their magnitude threshold. No added quadratic term is treated as independent noise.

## Designated partner applied

The completed account04/B12 multihub theorem at `math-open-problems@bcb9fd2641440a89d6e4967781d755618e163001` gives

` s_(p+ell)(P_H A_*) >= gamma(||Lambda^(-1)W^T||) min{s_p(Lambda),s_ell(R)}. `

Combining it with the new local reserve theorem: if `p+ell-sum q_j>=6` and the resulting gap `g>0`, the final matrix has

` sqrt(lambda_6((A^2)[H,H]))>=g, `

so the completed six-square-mode compiler gives `||p_(X^TAX)||_(infinity,ess)<=C_m/g`.

Concrete application: `m=8,p=2,ell=6`, `s_2(Lambda)>=4`, `s_6(R)=2`, and slope at most one give baseline

` s_8(P_H A_*) >= sqrt(5)-1. `

Add an arbitrary symmetric packet `T` whose eigenmodes above `1/100` have `H`-projection span dimension at most two; those large eigenvalues have unrestricted number, signs and magnitudes. Then

` s_6(P_H(A_*+T)) >= sqrt(5)-1-1/100 = 1.2260679774997898... `

and

` ||p_(X^TAX)||_(infinity,ess) <= 2243.515238502045... . `

This strictly strengthens the partner's earlier `||P_HT||_op<=1/100` perturbation gate: the first two local singular values of `P_HT` may now be arbitrarily large.

## Later-owner projected-crossing checkpoint applied

The later owner continuation specifically asks B09--B12 to apply the checked arbitrary-rank projected-crossing theorem to an actual physical partition. On original hubs `K={1,2}`, light banks `I={3,...,8}`, `J={9,...,14}`, take

`M_J=2[I_2,0]`,  `A_R[I,J]=2I_6+E`,  `||E||_op<=1/100`.

Then `rank(M_J)=2`, its singular-product is `S=4`, and after projecting off `row(M_J)`,

`Z_1>= (4-sqrt(6)/100)^2`.

Every first-volume row marginal satisfies

`alpha_i <= (2.01)^2/(4-sqrt(6)/100)^2 = 0.2556274480... < 1/2`.

Thus every gate of the grouped projected-crossing theorem is checked on this actual partition, giving the continuous `C_0` density bound

` ||p_Q||_infinity <= 2.125668232876967... `.

At `E=0` this is exactly `3/sqrt(2)=2.1213203435596424...`. Arbitrary internal hub curvature is retained by the theorem's arbitrary hub function; it is not discarded as noise.

The seeded finite checker recorded zero violations in 5,000 threshold tests and 5,000 random two-packet reserve tests; these are sanity checks only.

## Status

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. The unpaid implication is structural: bare `s_3(A)>=1` does not yet force a bounded ORIGINAL-coordinate bank with enough pre-tail reserve and bounded local high-spectrum footprint, nor the quantitative projected-crossing gates above. Failure must be routed into an already-paid grouped-bank, projected-crossing, ridge, hub/common-plane, physical-core, Schur, or Pluecker-volume mechanism.

Continuity is proved for the explicit projected-crossing subbranch above; it is not claimed for the general r45 six-mode branch or the unrestricted conjecture. Memory status remains `WITHOUT_VERIFIED_BRAIN`.
