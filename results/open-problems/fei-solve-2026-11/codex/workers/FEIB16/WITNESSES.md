# Coordinate witnesses

PROVED: every sufficient statistic described below is a function of the erased sample T=U\{i}, and reconstructs P[i in U | T]. Erasure is its resulting conditional entropy. Coarse block indicators give upper bounds when stated.

## PM(K33) and its towers

PROVED: use a block/level witness recursively. At a composition node targeting child j, check whether T meets the target child's block away from i. If it does, recurse into that child: both spectral endpoints have the common outer factor K_{B+j}, which cancels in their ratio. If it does not, retain the active pattern B of the other children and stop. The conditional inclusion probability is

    K_{B+j}² c_i(inner)² / [K_B² + K_{B+j}² c_i(inner)²].

It suffices to retain the selected level and the amplitude-pair class (|K_B|,|K_{B+j}|), rather than the whole pattern B. This is an explicit finite block/level statistic, not a claim that spectral inclusion is determined with zero error. For the balanced PM tower, K is the fixed base Fourier table and c_i(inner) is the product of the core/coin singleton coefficients along the inner path. pm_witness_histograms.csv lists the exact dyadic pair classes and counts.

CHECKED: pm_orbits_depth6.csv and pm_orbits_depth10.csv give E_i/Inf_i and D_i/Inf_i for each of 64 and 1,024 coordinate type words. Each word has multiplicity 9^depth. For depth 20 or 50, FORMULAS.md Section 6 gives each orbit explicitly by its word in {C,K}^depth; expanding the exponential orbit list would add no information. tower.json groups words by their number of core letters only for aggregated averages and minima. It does not mistake that aggregation for a single orbit.

## Tribes and regular AND/OR trees

PROVED: for a coordinate in a width-w tribe, the three cells are: T meets the rest of its own tribe; T misses that tribe but is nonempty; T is empty. In the first cell the inclusion probability is 1/2. In the second it is delta²/(a²+delta²), where delta=2^-w and a=1-delta. In the empty cell it is d²/(b²+d²), with b=2a^s-1 and d=2delta a^(s-1). These cells give the exact E_i formula. The single indicator "T meets the rest of its tribe" gives the coarser upper bound in FLOW 10(d).

PROVED: in a recursive AND/OR tree retain the first level where the remainder of the target child is empty, and whether the other children have any active block. At an AND node all nonempty outside patterns have the same amplitude ratio 2p/c_i(inner); only the entirely empty pattern is exceptional. This recursive block/level statistic gives the stable formulas in FORMULAS.md Section 4. Each regular tree is transitive, so its one orbit has E_i/Inf_i=H^-/I and D_i/Inf_i=R. stable_readonce.json contains these ratios, including very small-influence cases in logarithmic form.

## Other families

PROVED: odd majority and its recursive compositions use the parity of |T|; the spectral support has one degree parity, so E_i=D_i=0. The odd-dimensional complete quadratic has an affine parity constraint on its support and uses the same witness. Even-dimensional complete quadratics, every bent function, and every Maiorana–McFarland bent function have uniform spectra: inclusion is an independent fair bit, E_i/Inf_i=2 and D_i/Inf_i=4.

PROVED: for an address function, a data coordinate is present precisely when no other data coordinate is in T. Thus every data coordinate has zero erasure. For an address coordinate, conditional inclusion remains a fair bit, giving E_i/Inf_i=2 and D_i/Inf_i=4. The data coordinates force R=0.

PROVED: for a patched bent function, a fresh coordinate is absent if another fresh coordinate appears in T. Otherwise its conditional inclusion probability is delta²/(a_T²+delta²). On an inner-product bent subspace patch, the amplitude class is determined by the quadratic parity on the fixed core pairs, so this is a concrete two-class statistic in the no-fresh layer. For a core coordinate, retain whether a fresh coordinate is selected, the paired core bit, and the quadratic parity of the other fixed core pairs. The sums are implemented in families.py:bent_subspace and bent_patch.

CHECKED: the best scanned constructions use the PM block/level witness, rather than a global degree parity. OPEN: a uniformly bounded-cost witness scheme for arbitrary Boolean functions.
