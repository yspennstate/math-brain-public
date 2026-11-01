Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 same-run correction — threshold argument in Corollary 6.2

This is a narrow correctness correction to the immutable report

`2026-09-20T024819Z__posterior-packing-and-variance-localized-chaining.md`

created at commit `e6b8ed46fec54055fb18b65735492ebf03d5b619`. The predecessor is intentionally not overwritten.

## Correction

Theorem 6.1 in the predecessor is unchanged. In Corollary 6.2, the displayed entropy profile must retain a fixed constant rescaling in the **argument** of the monotone active-set profile. The correct statement is:

> There exist constants `c_r>0` and `C_{r,p}<infinity` such that, for `0<epsilon<=2H_0`,
>
> ```text
> sqrt(log N(B_p^d,d_T,C_r epsilon))
> <= C_{r,p} sqrt(log(2d))
>    [1 + max_{1<=ell<=r}
>       { H_ell(c_r epsilon) / epsilon }^(1/ell)].
> ```

The sentence in the predecessor saying that replacing `H_ell(c_r epsilon)` by `H_ell(epsilon)` “only changes constants” should be deleted. For an arbitrary monotone profile `H_ell(u)`, that replacement is not justified: a fixed multiplicative change in the threshold may cross a genuine jump of the active set.

### Proof with the corrected profile

Take

```text
u := c_r epsilon
```

with `c_r` sufficiently small compared with the covering-radius constant in Theorem 6.1, and choose

```text
s := ceil(C_r [1 + max_ell
                {H_ell(nu)/epsilon}^{2/ell}]).
```

Then

```text
R_s(nu)^2
 <= C_r sum_{ell=1}^r s^(-ell) H_ell(nu)^2
 <= C'_r epsilon^2.
```

Theorem 6.1 covers the inactive set by the origin at radius `nu` and the active set at radius `C'_r epsilon`, while

```text
log N <= C_{r,p} s log(2d).
```

Taking square roots gives the corrected display.

## Effect on the rest of the report

Theorem 7.1 in the predecessor already uses the correct quantity

```text
H_ell(c_r epsilon),
```

in its definition of `Psi(epsilon)`. Therefore the variance-localized Dudley reduction, the exact `ell=0` cancellation, the worst-case `gamma` sanity check, and the dense-dust counterexample are unchanged.

No full-source exponent improvement is claimed: `gamma -> gamma`, target `alpha=1/2-1/p`.
