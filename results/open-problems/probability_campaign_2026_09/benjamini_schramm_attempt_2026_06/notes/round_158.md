# Round 158 log

Added `cor:volume-sensitive-uniform-deterministic-gate-incidence-obstruction`.

Round 157 produced a deterministic anchored incidence obstruction with

```tex
kappa_j^vol(p)
  = p^{2r_p} (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 4 theta log_Delta omega}.
```

Using the bounded-degree lower bound `p_c >= 1/Delta`, choose the near-critical
window so that `p >= 1/Delta`.  Then

```tex
p^{2r_p} >= Delta^{-2r_p} >= chiBar_p^{-2 theta}.
```

Thus the uniform deterministic threshold is

```tex
hat{kappa}_j^vol(p)
  = (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 2 theta - 4 theta log_Delta omega}.
```

The deterministic lower bounds become

```tex
|Z^sharp| >= hat{kappa}_j^vol(p),

|{ y in K : d(y,a_z) in I_gate }| >= hat{kappa}_j^vol(p)
  for every z in Z^sharp.
```

The useful parameter range is now

```tex
theta < B,
1 - 2 theta - 4 theta log_Delta omega > 0.
```
