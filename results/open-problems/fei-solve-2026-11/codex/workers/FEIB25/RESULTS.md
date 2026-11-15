# FEIB25 results

The paper was opened at https://arxiv.org/html/1911.10579 (v2, 7 May 2020). Theorem 1.3 includes an additive K I[f] term and uses {0,1}-valued functions. Conversion to the brief's {-1,1} convention will be explicit.

The journal page https://link.springer.com/article/10.1007/s00039-020-00544-2 identifies GAFA 30, 1097–1138 (2020). Only its abstract/metadata are accessible; journal theorem statements have not been compared.

Brain recall found the provisional erasure-equivalence note and led back to FLOW 7. It helped with orientation, not independent verification. Math recall reports `math store not found`.

## Lower-level-only bounds fail — PROVED (full proof in preparation)

Let m=2r+1, M_m be majority, b=binom(2r,r)/4^r, and let h(z,y) equal 1 when z=1 and M_m(y) when z=-1. For f=parity_{d-1} h,

    W_{d-1}=1/4, W_d=(1+m b^2)/4,
    A_d=1/4 + (m b^2/4) log2(1+1/b^2).

The elementary bounds 1/(4r)<=b^2<=1/(r+1) give A_d>=1/4+(1/8)log2(r+2). Thus no fixed finite coefficients on W_0,...,W_d can bound A_d, even for Boolean f. This rules out L1 with any universal constant, and L2 with any fixed set of lower-level weights. It is not a counterexample to FEI: I(f)=d-1/2+m b/2 grows with m.

## Exhaustive and finite searches — CHECKED NUMERICALLY

`python3 levels.py census` generates census_n*.npz from locally regenerated NPN representatives. There are 2, 4, 14, 222 and 616126 representatives for n=1,...,5 (npn*.log / census_summary.json). W numerators are integers over 4^n; A is evaluated in binary64 from exact dyadic masses.

For n=5, max_{d>=2} A_d/[d W_d+(d-1)W_{d-1}] = 1.160964047443681 at d=2, truth table 0x71356 (bit x means f(x)=-1). The same maximum holds for denominator d W_d+W_{d-1}. Adding every lower level with coefficient 1 still permits ratio 1.1326478511645668 at 0x11717bc.

`python3 search.py` found L1 ratio 1.7369482829826224 at n=16; L2 ratio 1.7375990459866377. These are lower bounds from short searches, not maxima. Witness truth tables and full profiles are in hill.json and hill_n*.npz.

`python3 levels.py audit` checked 96 cases against direct Walsh sums, direct edge sums and truth-table pivotal influences. Maximum absolute discrepancy was 7.771561172376096e-16 (audit.json). Initial subprocesses inherited nice=10; attempts to add niceness were denied by the sandbox. Later runs retain the verified inherited priority and use one numerical thread.

## Low levels — PROVED

PROOFS.md proves A_1≤sqrt(W_0)I/ln 2 and A_2≤(I²−Σ_i Inf_i²)/ln 2≤(I²−W_1)/ln 2. The latter uses |f̂(S)|≤Inf_i for i∈S, from D_i f∈{−1,0,1}. A normalized real degree-two polynomial with W_1=W_2=1/2 has A_2=log2((n+1)/2), proving ordinary hypercontractivity alone cannot give this inequality. The quadratic influence term does not resolve FEI.

## Final computations — CHECKED NUMERICALLY

The four ordinary disjoint-block towers of the perfect-matching K33 host have n=9,81,729,6561. Their G/I values are approximately 1.673279240157, 2.811821689664, 3.173804996308, 3.228290742787; depth 4 has L1 ratio approximately 3.891790410901 at d=2 (towers_decimal_50.json). These are spectral recurrences, not truth tables of the large functions. A biased small-host composition agrees with its nine-variable truth table to 2.7755575615628914e-17 (tower_audit.json).

The initial towers.json is retained as a superseded binary64 diagnostic: it underflows in tiny tails at depths 3 and 4. The primary profiles are towers_decimal_50.json and level_profiles.csv.gz. Their smallest positive level mass is 3.0651863901862839364689027927032557015346182672382e-3950. Runs at 40 and 50 decimal digits agree at every W/A coefficient to relative difference at most 1.73513147368429293470066782141408808150568383645527422653474e-37, with maximum mass error 1e-50 (tower_precision_audit.json). No tail-level maximizer is discarded by a small-mass threshold in these primary tower results.

The selector-majority formula was checked against truth tables through m=13 to 2.220446049250313e-16. At m=65535 it gives A_2=2.9001851134665304 bits, W_1=0.25, W_2=0.40915615737090827 and I=103.62883419143917 for parity times selector-majority (selector_majority.json). Complete analytic level profiles are also saved at n=1024,1025,1026.

`python3 final_audit.py` rechecked all 616368 saved NPN representatives against pivotal influences and the proved A_1/A_2 inequalities, Han's inequality and the directed sandwich. It found no positive inequality residual beyond tolerance, maximum identity/NPN transformation discrepancy 1.1102230246251565e-16, and exact agreement on all 30 stored hill witnesses. Burnside's lemma independently gives the same orbit counts and local representative files match the earlier FEIB13 files byte for byte (analytic.py, coverage_audit.json).

The data comprise 91 truth-table family instances, 4 towers, 30 hill-search instances and 3 full analytic large profiles. Among these profiles, the candidate A_d≤dW_d+(d−1)W_{d−1}+Σ_{k>d}kW_k survives for d≥2; its largest ratio is 0.7817865759096007 at PM_K33, d=2 (numerical_summary.json). It is unproved and summing it would reuse tail mass too often. The finite data do not determine a weakest tail weight.

The final measured largest truth-table case used 513376256 resident bytes at inherited nice 10 and one numerical thread (resources.json); the generator's seen bitset is 268435456 bytes. All data remain inside the brief's disk limit.
