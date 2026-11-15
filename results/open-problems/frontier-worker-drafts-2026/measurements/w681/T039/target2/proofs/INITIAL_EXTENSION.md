# Initial certified extension of the positive three-set simplex range

Status: computer-assisted proof (unaudited). This is an intermediate prefix, not completion of the requested target through 0.42 or 0.43.

Theorem. Let n>=2 and let Omega_1,Omega_2,Omega_3 be a measurable partition of R^n with each cell of standard Gaussian measure 1/3. For every rho in [1/10,803/2000], its Gaussian rho-noise stability is at most that of the standard 120-degree simplex partition (embedded cylindrically when n>2).

Heilman arXiv:2608.00333v1 Theorem A.1 gives [1/10,2/5]. For the extension, its proof uses positive-correlation dimension reduction, circular rearrangement, Corollary A.3 (valid for every a>=0), and (146). Thus it suffices that the same mean-zero weighted operator have norm below 2. CELL_BOUND.md proves a positive radial-cell matrix comparison and a full-complement Hilbert-Schmidt tail bound for this operator. SCALED_KERNEL.md proves the exact rescaling used in this run. ARBITRARY_CENTER.md explains why the slabwise dyadic quartic centers preserve the same mean-zero quadratic form.

The saved centered_checkpoint.json has three adjacent accepted slabs covering [0.4,0.4015]. Every slab has directed finite-matrix Collatz row sums, a complete analytic outside tail, strictly positive dyadic witness and total upper bound below 2. The worst total binary64 upper bound is 1.998371111346653. Its exact hexadecimal representation is 0x1.ff953fc8814aep+0. Since this is an upper bound strictly below 2, (146) is nonpositive and the source reduction proves the theorem.

Reproduce the recorded computation with python -B -X utf8 scripts/run_centered_certificate.py --max-seconds 460, using the pinned cut_bounds source and recorded dependencies. The command is resumable and will continue beyond this prefix; the theorem here uses only the three accepted slabs recorded in logs/initial_extension_validation.json. Numerical quadrature and power iteration only propose centers and positive witnesses; the directed entry, tail and row-sum computations establish their bounds.

This result is not independently checked. It uses radial cells rather than a Laguerre basis. The output validation checks coverage, source and witness identities, and exact final arithmetic; it does not replace source-level independent review of the analytic reduction or enclosure code.
