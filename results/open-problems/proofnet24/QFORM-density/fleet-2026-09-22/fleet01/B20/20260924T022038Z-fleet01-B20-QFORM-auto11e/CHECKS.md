# Exact and numerical checks — fleet01/B20 auto11e

Run: `20260924T022038Z-fleet01-B20-QFORM-auto11e`.

These checks support the constants in `REPORT.md`; the proofs there are analytic and do not depend on floating-point experiments.

Let

`c0=((sqrt(766)-4sqrt(3))^2)/16384`,

`pstar=sqrt((63/256)c0)/64`,

`C3=3*2^(4/3)*e^(1/3)`,

`Zstar=(3pstar/4096)^2`,

`qstar=27pstar/256`,

`Zcross=qstar^2/2^24`.

Numerically:

- `c0 = 0.026275654659752182...`;
- `pstar = 0.0012564554392151157...`;
- `Zstar = 8.468700907587555e-13`;
- `C3 = 10.550168831164775...`;
- `C3*Zstar^(-1/6) = 1084.6508070708749...`;
- `qstar = 0.00013251678460471925...`;
- `Zcross = 1.0466991783364748e-15`;
- `C3*Zcross^(-1/6) = 3310.9739388026574...`;
- `3/4096 = 0.000732421875`;
- `21/4096 = 0.005126953125`;
- `sqrt(3)/4096 = 0.0004228639666916204...`;
- `1/(256sqrt(2))-3/4096 = 0.002029713989009951... > 1/512 = 0.001953125`.

The last strict inequality has the exact reduction

`1/(256sqrt(2))-3/4096 > 1/512`

iff

`8sqrt(2)>11`,

and this holds because `128>121`.

## Symbolic constant flow

From the fleet02/B20 packet,

`s1^2>(63/256)c0`, `s2>=1/64`,

so

`p=s1s2>pstar`.

If `E3(M)<Zstar`, then the exact inclusion of the `x1*x2*xk` terms in `e3` gives

`E3(M)>=p^2 T`,

where `T=sum_(k>=3)sk^2`. Thus

`sqrt(T)<sqrt(Zstar)/pstar=3/4096`.

For the diffuse physical paving, `g=3/8`. Hence each quadrant satisfies

`s2(C)>g/64-3/4096=3/512-3/4096=21/4096`.

Also

`p sqrt(T)<sqrt(Zstar)=3pstar/4096`,

`s1+s2<=2s1=2p/s2<=128p`,

and therefore

`g sqrt(T)(s1+s2)<(3/8)*128*(3pstar/4096)=9pstar/256`.

The rank-two core product is at least

`g^2 p>9pstar/64=36pstar/256`,

so the actual quadrant product is strictly larger than

`(36-9)pstar/256=27pstar/256=qstar`.

For the crossed cut `B`, `e2(B)>qstar^2`. If `e3(B)<qstar^2/2^24`, the exact exterior-volume inequality

`T2 e2<=3e3`

gives

`T2<3/2^24`,

hence

`dist_F(B,rank<=2)<sqrt(3)/4096`.
