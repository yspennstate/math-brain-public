# MOC4 handoff — account03/B09 odd-twist mass certificate

Run: `20260922T024834Z-account03-B09-moc4-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Scientific report: `proofnet24/collective-MOC4/account03/B09/20260922T024834Z-account03-B09-MOC4-r12/REPORT.md` in `yspennstate/math-open-problems`, first report commit `2f5c6157d73f268cda54740af28f9589f9014b52`. Exact verifier commit `80cd98ac33c0c645d257ce8ef4d7451b858c14ed`; exact verification output commit `1a96bc03d1dc4c590798679791ea1a9a1d21237c`.

## Named partner consumed

The exact named partner result consumed is account04/B07 run `20260922T021038Z-account04-B07-MOC4-r13`, `MOC4-ODD-WEYL-ORIENTATION-v1`. It supplies the Bogoliubov complementary-minor channels `q+ = |m|^2`, `q- = |n|^2`, the structured objective, and the odd-matching overlap inequality. It also leaves the current missing step as orientation-aware weighted suppression.

## New exact theorem

For a genuine exterior-square image `O in SO(6)`, write its Bogoliubov form on the three complementary-pair complex planes as `T(z)=Mz+N zbar`, with `q+_ij=|M_ij|^2`, `q-_ij=|N_ij|^2`.

For any row signs `r_i` and column signs `c_j` with

`(prod_i r_i)(prod_j c_j) = -1`, 

the following global channel-mass inequality holds:

`sum_{i,j} q^{r_i c_j}_{ij} <= 2`.

There are 16 distinct checkerboard sign matrices of this form.

Proof: conjugate exactly the selected input/output complex coordinates. The resulting real orthogonal map is orientation reversing. Its complex-linear part `M'` has squared entry magnitudes exactly the selected `q^{r_i c_j}`. If `M'` were invertible, `Z=M'^{-1}N'` is complex skew-symmetric and the path

`M_t = V(I+t^2 Z Z*)^{-1/2}`, `N_t=M_t(tZ)`

connects the map inside `O(6)` to a unitary orientation-preserving map, contradiction. Thus `rank M'<=2`; also `M'M'^*<=I`, hence `||M'||_F^2<=2`.

This uses the full orthogonality/Bogoliubov compatibility and is stronger than merely bounding the three linear matching masses.

## Exact structured support application

Apply these 16 valid inequalities to the generic structured `(K,X)` datum used by account01/B07 and account04/B07. That datum has

- genuine 24-endpoint maximum `M_even = 13195057/5120000`,
- forbidden 48-state odd maximum `M_odd = 20773731/5120000`,
- naive orientation-forgetting excess `3789337/2560000 > 0`.

An exact rational LP dual using only row/column conservation plus four of the 16 new odd-twist inequalities gives objective exactly

`13195057/5120000 = M_even`.

The active twist multipliers are:

- `r=(+,+,+), c=(-,+,+)`: `2042727/2560000`;
- `r=(+,+,-), c=(-,+,-)`: `133141/256000`;
- `r=(+,-,+), c=(+,+,+)`: `514151/2560000`;
- `r=(+,-,-), c=(-,+,+)`: `98951/2560000`.

Row potentials are `(2302707,1268991,-871389)/5120000`; column potentials are `(-720783/640000,39007/640000,0)`. Fraction arithmetic verifies all 18 channel inequalities; nine are tight and the smallest positive slack is `347/16000`.

Therefore the new compatibility inequalities recover the correct `S4` support bound on an exact generic datum where the previous 48-state relaxation overshoots by about `1.48021`.

## Next implication

Do not return to arbitrary bistochastic or 48-state matching data. The sharpened finite question is whether, for every **structured spectral** coefficient pair `(K,X)` arising from `(a,b,eta)`, row/column conservation plus the 16 odd-twist mass inequalities already have support equal to the 24 even Weyl endpoints. If not, isolate the residual structured cone and combine these mass inequalities with account04/B07's stronger square-root odd-overlap inequality or the remaining phase equations.

This is not yet a full MOC4 proof and is not a target counterexample.
