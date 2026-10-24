# r23 finite algebra checks

These are arithmetic/symbolic checks only; the proof is in `REPORT.md`.

Let

`h_* = 1 - pi^(1/4) e^(1/8)/(Gamma(1/4) cos(pi/8))`.

Numerically:

- `h_* = 0.5496212850267048...`.
- Heavy quarter-Riesz constant at crossover: `C_* = 4*2^(1/8) h_*^(-1/8) = 4.700897674324740...`.
- Old r22 crossover-at-1/2 constant: `4*2^(1/4) = 4.756828460010884...`.
- New global weighted time constant: `2 Gamma(1/4) cos(pi/8) C_* = 31.492505546446097...`.
- Old r22 weighted time constant: `31.867200062359164...`.
- New quarter-pair transducer scalar: `3*2^(4/3) C_*^(2/3) = 21.213636077138162...`.
- Old r22 scalar: `3*2^(17/6) = 21.38156923536814...`.
- Partner r23 concentrated-row scalar: `8 sqrt(3) 2^(1/8) = 15.11051839218372...`.
- Sharpened concentrated-row scalar: `2^(29/8) = 12.337686603263526...`.
- Ratio sharpened/partner: `sqrt(2/3)`.
- Sharpened concentrated-row quarter-weighted time scalar: `8*2^(1/8)Gamma(1/4)cos(pi/8) = 29.222351302795506...`.

Crossover identity check for `h>1/2`:

`C_diff(h)=8(2pi)^(1/4)(e/(2h))^(1/8)/[(2-2h)Gamma(1/4)cos(pi/8)]`.

Setting this equal to `C_heavy(h)=4*2^(1/8)h^(-1/8)` and cancelling `4h^(-1/8)` gives

`1-h = pi^(1/4)e^(1/8)/(Gamma(1/4)cos(pi/8))`,

which is exactly the displayed `h_*`.
