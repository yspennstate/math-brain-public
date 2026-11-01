# P0282 route pivot before archival checker — Gessel/Toeplitz seam instead of 17M hook-length shapes

Date: 2026-09-18 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282`

The preceding idea note reduced row 85 to the low-LIS seam `k<=19`. A local scratch implementation of the most literal realization — enumerate all 17,240,952 partitions of 85 with first row at most 19 and apply the hook-length formula — exceeded a 180-second local execution window and produced no certificate. That is not mathematical progress and is not archived as a claim.

Rather than spend the run optimizing the same brute-force route, switch languages.

For

`u_k(n) = #{sigma in S_n : LIS(sigma) <= k}`,

Gessel's classical Bessel/Toeplitz identity gives

`sum_{n>=0} u_k(n) x^(2n)/(n!)^2 = det(I_{|i-j|}(2x))_{1<=i,j<=k}`,

where

`I_d(2x) = sum_{r>=0} x^(2r+d)/(r!(r+d)!)`.

The low-seam source counts are then `ell_{85,k}=u_k(85)-u_{k-1}(85)` for `k<=19`. Because every matrix entry has a fixed parity, formal Gaussian elimination can be done in `t=x^2` series of degree only 85. Run the calculation modulo enough distinct primes that their product exceeds `2*85!`, reconstruct each `u_k(85)` by CRT, and multiply the determinant coefficient by `(85!)^2` modulo the CRT modulus. Since `0<=u_k(85)<=85!`, the reconstructed integer is unique.

Three independent safeguards will be built into the archival checker:

1. reconstruct Gessel coefficients for `n<=10` and compare them exactly against direct RSK/hook enumeration;
2. at `k=2,n=85`, verify `u_2(85)=Catalan(85)` exactly;
3. independently reconstruct the high-LIS side `j<=66` at `n=85` with the already proved Kauers-Wang fixed-defect recurrence plus exact finite Plancherel-tail correction, and require its overlapping count at `k=19` to equal the Gessel/CRT count.

If those checks pass and all 17 low-seam Turan margins are positive, then every row-85 inequality has an exact certificate: `k=2..18` from Gessel/CRT and `k>=19` from the independent fixed-defect/tail calculation. Chaining with archived rows through 84 moves the frozen metric `N_exact: 84 -> 85` without altering its definition.

This pivot is the substantive #19 algorithmic change for the run: exploit the theorem-induced seam first, then use a generating-function determinant whose complexity depends on the cutoff 19 rather than on the number of partitions of 85.