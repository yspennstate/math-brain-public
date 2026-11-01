# Checks — translation-curvature invariance

Run: `20260924T110354Z-fleet03-B14-QFORM-auto11`.

## Algebraic recentering

For `S=U+psi(T)`, so `U=S-psi`,

`U^T H U + 2 U^T g + r`

expands to

`S^T H S + 2 S^T (g-H psi) + r + psi^T H psi - 2 psi^T g`.

Therefore the quadratic Hessian in the anchor variable is exactly `H` under arbitrary environment-dependent translations.

## Reflection block

`B_* = I_3 - (2/3) 11^T` equals

```
[ 1/3  -2/3  -2/3 ]
[-2/3   1/3  -2/3 ]
[-2/3  -2/3   1/3 ]
```

and satisfies `B_*^2=I_3`, hence `spec(B_*)={-1,1,1}` and `sigma(B_*)=1`.

For one coordinate from each size-`m` bank in `A_m=U_0 B_* U_0^T`, the physical principal block is `B_*/m`, so its minimum absolute eigenvalue is exactly `1/m`. If a physical triple repeats a bank, its bank-membership matrix has repeated rows and the block is singular.

Thus

`max_{|I|=3} sigma((A_m)_{I,I}) = 1/m`.

## Partner inequality and grouped comparison

Fleet04/B14 r10 gives

`||p_Q||_inf <= 6 sqrt(pi) / sigma(H)`.

For `H=B_*/m`, this is

`||p_Q||_inf <= 6 sqrt(pi) m`.

Numerically:

- `6 sqrt(pi) = 10.634723105433096...`
- `12 sqrt(pi) = 21.269446210866192...`

The completed disjoint-bank compiler gives the same `A_m` family the uniform bound `12 sqrt(pi)`. Hence for `m>=3`, the grouped certificate is strictly stronger than every physical-triple certificate after arbitrary translation/recentering, and the ratio of the partner physical-triple constant to the grouped constant is `m/2`.

No numerical experiment is used as proof; these values only check the exact symbolic identities above.
