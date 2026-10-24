# ProofNet24 P20 — immutable readback correction / verification

**Canonical report:** `proofnet24/P20-kernel-hard-edge/runs/2026-09-16/2026-09-16_09-08-26__run-report.md`  
**Creation commit:** `e67f9ac81c190e65f85d088ee8ca923d9019a710`  
**Verified report blob:** `3014891261b23b522c8d365d67c0b5eb469a1ce0`

The report was read back from the exact creation commit in contiguous ranges `1-320`, `321-700`, `701-1100`, `1101-1500`, followed by an explicit `1501-1700` read returning empty content. The canonical report is therefore complete through EOF at the exact returned creation SHA.

During adversarial readback I found one proof-line error in Section 4 (`P20-SELECTED-PIVOT-L1-UI-61`). The theorem is correct, but the displayed inequality

```text
E[ K_d 1_{K_d>M} ]
<= E[K_d-(K_d wedge M)]
```

is false: on `{K_d>M}`, the right integrand is `K_d-M`, not `K_d`.

The immutable canonical report is not overwritten. Replace only that proof step by the following correct argument.

Let

```text
X_d=K_d,
X=(chi_4^2)^(-1).
```

P04 plus the audit give

```text
X_d => X,
E X_d -> E X = 1/2.
```

The limit law is continuous. Hence for every fixed `M>0`,

```text
E(X_d wedge M) -> E(X wedge M),
P{X_d>M} -> P{X>M}.
```

Use the exact identity

```text
E[X_d 1_{X_d>M}]
= E X_d - E(X_d wedge M) + M P{X_d>M}.
```

Therefore

```text
lim_{d->infinity} E[X_d 1_{X_d>M}]
= E X - E(X wedge M) + M P{X>M}
= E[X 1_{X>M}].
```

Letting `M->infinity` and using `E X<infinity` gives

```text
boxed{
lim_{M->infinity}
limsup_{d->infinity}
E[X_d 1_{X_d>M}]
=0.
}
```

Thus `K_d` is asymptotically uniformly integrable in `L^1` exactly as claimed.

The same corrected argument applies to

```text
R_d^sel=K_d^(-1),
R_d^sel => chi_4^2,
E R_d^sel -> 4=E chi_4^2,
```

and proves its asymptotic `L^1` uniform integrability.

No other theorem statement, exponent, P04 audit verdict, source SHA, trace/traceless dependence statement, failed-route certificate, dependency status, or next attack changes. In particular:

- `P20-REGULAR-RANK2-PIVOT-TAIL-61` remains **PROVED** with critical exponent `2`;
- `P20-SHARED-FACTOR-PIVOT-TAIL-61` remains **PROVED** with critical exponent `3/2`;
- `P20-RAW-DENOM-CONCENTRATION-NOGO-61` remains **PROVED**;
- Target 4 remains **OPEN**.

No email/Gmail action was used.
