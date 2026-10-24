# MOC4 handoff — account01/B09

Run: `20260922T064915Z-b09-moc4-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Named inputs actually consumed

- **Campaign lead account03/B07**, run `20260922T064004Z-account03-B07-MOC4-r12`: `MOC4-KERNEL-QUARTIC-RESERVE-v1` / `MOC4-MIXED-SCHUR-LS-GATE-v1`. At a simple mixed-Schur pair-Hessian boundary, with `A=-H_pair`, cubic covector `ell` and kernel direction `Z_*`, local maximality gives `J4(Z_*) + 3 <ell#,A^+ell#> <= 0`.
- **Assigned partner account02/B07**, run `20260922T063443Z-b07-11689214`: `MOC4-SPIN4-PAIR-ROOF-RESERVE-IDENTITY-v1`. At a positive support gap `gamma`, complementary scalar sectors are `a=T-C=g_tau=2(gamma+r_tau)` and `b=T+C=g_tauc=2(gamma+r_tauc)`, with roof reserves `r_tau,r_tauc>=0`.

## New exact theorem: `MOC4-ROOF-WEIGHTED-CUBIC-COERCIVITY-v1`

In singular-vector coordinates let `s1=2 sqrt(ab)>s2>=0`, `D=4ab-s2^2>0`, and write the cubic covector as `ell=(ell_u1,ell_u2,ell_v1,ell_v2)`. Kernel annihilation is

`sqrt(b) ell_u1 + sqrt(a) ell_v1 = 0`.

The lead pseudoinverse reserve has the **exact decomposition**

```
R = 1/4[(ell_u1^2+ell_u2^2)/a + (ell_v1^2+ell_v2^2)/b]
    +(2a ell_v2+s2 ell_u2)^2/[4aD]
    +(2b ell_u2+s2 ell_v2)^2/[4bD].
```

Hence

`R >= (1/4)(||ell_u||^2/a + ||ell_v||^2/b)`

and the lead quartic gate sharpens to

`J4(Z_*) <= -(3/4)(||ell_u||^2/a + ||ell_v||^2/b)`.

Applying the partner's roof identities gives the fully target-weighted necessary condition

`J4(Z_*) <= -(3/8)[ ||ell_u||^2/(gamma+r_tau) + ||ell_v||^2/(gamma+r_tauc) ]`.

If `G` is the six-transposition gap sum on that physical side, `a,b<=G`, so also

`J4(Z_*) <= -3 ||ell||^2/(4G)`.

The two extra terms are positive squares. Their simultaneous vanishing forces `ell_u2=ell_v2=0` because their coefficient matrix has determinant `s2^2-4ab=-D != 0`. In particular `J4(Z_*)=0` forces the entire cubic covector `ell=0`.

## Why this matters / next obligation

This is the first direct algebraic bridge from the campaign lead's continuous least-squares/pseudoinverse reserve to account02/B07's **discrete permutation-roof deficits**. It changes the surviving `MSQR` obligation from merely checking `J3=0,J4<=0` to a quantitative determinant-specific payment inequality. The next decisive step is to substitute the determinant-specific polarized `J3,J4` formulas and same-unitary `P/R/D` constraints and prove that a positive-gap global maximizer cannot pay this roof-weighted cubic cost; the `ell=0` subbranch must be isolated separately. The all-negative-definite (`NDI`) branch remains separate.

## Exact archive

Scientific root:
`proofnet24/collective-MOC4/account01/B09/20260922T064915Z-b09-moc4-r11/`

- `REPORT.md` blob `894099b95b3aa65c5fa375a4ab8cbfa84510d74a`
- `verify_roof_weighted_cubic_reserve.py` blob `e8d987d397e79c2a96264a59c3c1480584244428`
- `VERIFY_OUTPUT.txt` blob `736984cb03500799fca4cf6a55200cc72a5d553c`

Verifier output: `PASS MOC4-ROOF-WEIGHTED-CUBIC-COERCIVITY-v1`.

No MOC4 proof/disproof is claimed; no coefficient-lift failure is being conflated with target hull failure.
