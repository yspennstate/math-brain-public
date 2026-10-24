# Round 159 log

Added `cor:volume-sensitive-localized-anchored-incidence-obstruction`.

Round 158 gave a deterministic anchored gate-incidence obstruction with

```tex
hat{kappa}_j^vol(p)
  = (sigma_j^3/(16 C_vol^3))
    chiBar_p^{1 - 2 theta - 4 theta log_Delta omega}.
```

Set

```tex
A = {a_z : z in Z^sharp}
Y = union_z { y in K : d(y,a_z) in I_gate }.
```

The anchor separation and `d(a_z,z)=r_p` make `z -> a_z` injective, so

```tex
|A| = |Z^sharp| >= hat{kappa}_j^vol(p).
```

The pointwise incidence lower bound for any selected gate gives

```tex
|Y| >= hat{kappa}_j^vol(p).
```

Every `y in Y` is localized around the root because

```tex
d(x,y) <= d(x,a_z) + d(a_z,y) <= 2^{j+2} + 2 r_p.
```

The resulting obstruction no longer contains the ambient witness set `K`; it
has separated anchors `Z`, selected gates `A`, and a localized incident set
`Y subset B(x,2^{j+2}+2r_p)`.
