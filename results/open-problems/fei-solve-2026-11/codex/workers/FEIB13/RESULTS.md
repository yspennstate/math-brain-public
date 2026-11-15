# FEIB13 results

PROVED correction to FLOW 3b: the read-once zero-cancellation statement needs the empty-set qualification. AND₂, truth table `0x8`, has H=2 bits but 2P+2(I−Var)=1.5 bits; the missing 0.5 bit is its empty Fourier entropy. General FLOW formulas retaining Gamma are unaffected. See PROOFS.md, opening paragraph.

General containment P≤CI is OPEN. The original W and both untruncated candidate budgets are disproved below. Every finite table is CHECKED within its stated scope.

Logs are base 2. P, A, H and reference costs are in bits; I and Var are dimensionless. Entries below are divided by I unless stated otherwise. Census outputs: census.json; literal families: structured.json; analytic families: families.json; large MUX: mux.json. Scripts are independent of the shared FEI check scripts.

## 1. Sparse split

CHECKED: complete NPN orbits for every n≤5, plus 5,120 functions each at n=6,7. The sample seed is 20261110, with equal allocations to uniform, balanced, sparse-output, and random threshold functions. NPN generation scans all output-complement classes; it does not sample them.

| scope | count | max P/I | max A/I | max Sp1/I | max Sp2/I | max Sp3/I | max Sp4/I | max Sp6/I |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| npn1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| npn2 | 4 | 0.5 | 1 | 0 | 0 | 0 | 0 | 0 |
| npn3 | 14 | 0.75 | 1.5833333 | 0.5 | 0 | 0 | 0 | 0 |
| npn4 | 222 | 0.875 | 1.9375 | 0.5306391 | 0.375 | 0 | 0 | 0 |
| npn5 | 616126 | 0.9375 | 2.1625 | 0.625 | 0.4159433 | 0.25 | 0 | 0 |
| sample6 | 5120 | 0.9732814 | 2.3125 | 0.6681995 | 0.3055556 | 0.2967441 | 0.15625 | 0 |
| sample7 | 5120 | 1.0062458 | 2.4174107 | 0.640625 | 0.328125 | 0.1936367 | 0.1936367 | 0 |

CHECKED n=5 sparse extrema (bit x set means f(x)=−1):

| K | Sp_K/I | truth table |
| --- | --- | --- |
| 1 | 0.625 | 0x2 |
| 2 | 0.4159433 | 0xe |
| 3 | 0.25 | 0x2 |
| 4 | 0 | 0x2 |
| 6 | 0 | 0x2 |

Every census extremum, including all moments and references, is in extremal_truth_tables.csv. Full finite-function witnesses are hexadecimal there; very large analytic families are specified by their parameters, because their truth tables cannot be materialized within the disk limit.

CHECKED maxima across every tested function and analytic parameter choice:

| K | max Sp_K/I | function |
| --- | --- | --- |
| 1 | 1.3552891 | tribes_w3_m32 |
| 2 | 0.505692 | tribes_w3_m3 |
| 3 | 0.3624738 | tribes_w4_m2 |
| 4 | 0.2161381 | majority_255 |
| 6 | 0.0546875 | tribes_w1_m8 |

Thus K=2 with C=0.5056921 covers everything tried; this is a finite numerical bound, not a universal theorem. K=6 with C=0.0546876 also covers everything tried. PROVED for all equal-width tribes, Sp_K≤P≤2I for every K. General sparse containment is OPEN.

The actual sets are in carriers.json. In tribes, a set hitting r blocks in s coordinates contributes exactly when rw−s−(m−r)log b>K s; its weight depends only on (r,s). Large costs are concentrated on unusually small selections inside the hit blocks. The global K=2 and K=3 witnesses have their full sets and degree breakdown in that file. For majority₂₅₅, the K=4 cost is carried by singletons: Inf_i log(1/Inf_i)=0.2161381 after division by I. The K=6 record is the eight singleton sets of OR₈, equivalent to AND₈.

## 2. Label-time flow and budgets

CHECKED supremum of T_t/I within each scope:

| scope | t=1/4 | t=1/2 | t=3/4 | t=1 |
| --- | --- | --- | --- | --- |
| npn1 | 0 | 0 | 0 | 0 |
| npn2 | 0.21875 | 0.375 | 0.46875 | 0.5 |
| npn3 | 0.4101562 | 0.65625 | 0.7617188 | 0.75 |
| npn4 | 0.5776367 | 0.8671875 | 0.9448242 | 0.875 |
| npn5 | 0.7241821 | 1.0253906 | 1.0592651 | 0.9375 |
| sample6 | 0.8524094 | 1.144043 | 1.1307907 | 0.9732814 |
| sample7 | 0.9646082 | 1.2330322 | 1.1754942 | 1.0062458 |
| all tested families | 1.8105426 | 1.672019 | 1.5906383 | 1.524102 |

PROVED generally T_t≤P+(1−t)I. PROVED for all equal-width tribes T_t≤(3−t)I. AND_n forces any universal T_(1/2) constant to be at least 1.5. General T_(1/2) and its relative-increment form remain OPEN.

PROVED stronger noise bound: F_R(1/2)≤up(R)p(R)^(1/3). This does not repair the missing cross-level budget. Both untruncated candidates fail on balanced tribes; even a single AND with increasing width disproves a uniform logarithmic budget after division by its very small I.

CHECKED candidate budgets at t=1/2. Entries are the largest log₂(count)/I found. The cutoff means up_M(R)=Σ_{U⊇R,|U|≤M}mu(U); it is on U.

| theta | up count, no cutoff | up, M=ceil(2I) | up, M=ceil(4I) | tau inverse-p moment |
| --- | --- | --- | --- | --- |
| 0.1 | 5.537878e+13 | 1.3672376 | 2.6925767 | 17.6892442 |
| 0.25 | 2.74195e+18 | 1.9307902 | 3.829635 | 473613.2 |
| 0.5 | 2.818065e+26 | 3.1632695 | 6.2506376 | 1.895151e+13 |

PROVED: no fixed positive theta makes the untruncated tau moment ≤2^(CI); the up count fails even at theta=0. OPEN: a universal cutoff estimate with M=aI for fixed a. The finite maxima for both tested cutoffs are compatible with such an estimate.

## 3. W and the weaker exponent

PROVED: original W (theta=1) is false for every finite c,K. For balanced tribes of width w, log₂ W_(1,c) grows like (1+2/c)^w, while I grows linearly in w.

CHECKED balanced-tribes obstruction at c=4. The last two columns are the minimal log₂ K required by W≤Var K^(I/Var); negative values are allowed.

| w | I | P/I | A/I | theta=1, c=4 | theta=1/2, c=2+sqrt(2) |
| --- | --- | --- | --- | --- | --- |
| 4 | 2.8845326 | 1.1863241 | 2.4931628 | 0.9262399 | -0.3363232 |
| 8 | 5.5550906 | 1.1706959 | 2.8106658 | 4.0583375 | -0.1123323 |
| 16 | 11.0904585 | 1.0901348 | 2.9097996 | 58.7522614 | -0.0457876 |
| 32 | 22.1807098 | 1.0450842 | 2.9549158 | 19450.0635736 | -0.0225435 |
| 64 | 44.3614196 | 1.0225421 | 2.9774579 | 4.195997e+09 | -0.0112711 |

PROVED sharp tribes discount threshold for every 0<theta<1: c≥2^theta/(2^(1−theta)−1) suffices, with K=2^(4−2theta). Every smaller c fails on balanced tribes. At theta=1/2, c=2+sqrt(2), K=8. Jensen gives A≤9.5431066 I and P≤the same bound; the direct tribes proof is stronger: P≤2I, A≤4I−2Var. A weakened W for all Boolean functions is OPEN.

AND and address functions also have exact moment formulas in PROOFS.md. They satisfy the original W for suitable constants, showing why testing them alone misses the tribes obstruction.

## 4. Reference measures

PROVED: tau_(1/2) and the uniform mixture over rho are probabilities, each ≤up(S), with cross entropy between H and H+I. Thus their universal O(I) cost is equivalent to FEI. Their costs are ≤7I on all equal-width tribes; a general bound is OPEN. Their ratios stay bounded over the tested tribes and majority ranges together.

The proposed conditional-product Markov reference telescopes to up(R), regardless of ordering. It is not normalized. Its normalization costs log₂ E 2^|U|, which is unbounded relative to I on tribes. The independent-product reference also grows with tribes width and majority dimension.

| function | P/I | A/I | tau₁/₂ cost/I | uniform mixture/I | product/I | normalized Markov/I |
| --- | --- | --- | --- | --- | --- | --- |
| AND_127 | 1 | 2.9685039 | 4.406261 | 4.0365223 | 127.442695 | 5.247962e+20 |
| tribes_w16_m45426 | 1.0901348 | 2.9097996 | 4.4140875 | 4.1466443 | 17.4426676 | 61.8423962 |
| tribes_w64_m12786308645202655232 | 1.0225421 | 2.9774579 | 4.4150375 | 4.0582953 | 65.442695 | 4.195997e+09 |
| majority_33 | 0.436817 | 0.7729769 | 3.0296035 | 2.810751 | 4.1872892 | 6.7400841 |
| majority_255 | 0.254955 | 0.4083465 | 3.1162551 | 2.8795127 | 5.7292872 | 19.7413652 |
| address_3 | 0.6 | 1.8 | 3.0490225 | 2.8937493 | 3.045715 | 2.901955 |
| PM_K33 | 1.0876859 | 2.0899467 | 3.6763794 | 3.6404309 | 3.4696508 | 3.4130338 |
| MUX_L16_k7_m458752 | 0.0380002 | 0.319607 | 1.4289745 | 0.6880084 | 12.3813493 | 43819.9714824 |

## 5. Checks, scope, and reproduction

CHECKED by audit.py: 65,536 four-variable truth tables using direct restriction sums; 350 saved extremal witnesses independently reconstructed; exact agreement for mu, up and p; maximum inequality residual 2.220446e-16. The strengthened noise bound also passed 1000 six-variable random checks.

The tribes, symmetric and MUX formulas agree with independent small truth-table calculations. The largest discrepancies are 2.664535e-15, 2.664535e-15, 8.881784e-16 respectively. The 64/128-node uniform-mixture quadrature audit and omitted spectral masses are recorded in audit.json.

For very biased AND functions, ordinary floating point loses counts differing from 1 by 2^-n. highprecision.py recomputes all AND rows in families.json at 160 decimal digits. No rounded-to-one double-precision budget values are used in these tables. Large majority uses exact integer restriction sums before conversion to floating point. The analytic tribes cutoff ceiling rounds back one upward floating-point ulp at an integer.

Run `python3 run.py` from this folder. It compiles the orbit generator, runs every census and family calculation, audits the output, and rebuilds these tables. It sets one numerical thread and nice≥10. resources.json records each child’s measured maximum resident size and elapsed seconds. The n=5 bitset is 268,435,456 bytes. No external files are written.

Brain recall provided orientation and a warning about prior FEI claims, but no applicable cross-level proof. math_recall.py reported that its store was missing. Fleet instructions forbid shared-memory/mesh writes, so the durable corrections are left here for the launching session.
CHECKED measured reproduction: peak resident size 270,745,600 bytes (258.203125 MiB); sum of child elapsed times 58.029360 seconds; every child exited 0 at nice 10. Source: resources.json. The runner completed with REPRODUCTION PASS and the independent audit with AUDIT PASS.


Task: “uniform-in-level containment” — brief read 2026-11-10 02:59 +04.
