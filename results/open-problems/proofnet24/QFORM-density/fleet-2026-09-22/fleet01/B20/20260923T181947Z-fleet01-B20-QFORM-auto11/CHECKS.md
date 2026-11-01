# Exact arithmetic checks

Run: `20260923T181947Z-fleet01-B20-QFORM-auto11`

The proof uses

`epsilon=403/2000`, `delta=1/64`,

so

`eta=epsilon+delta=403/2000+1/64=(3224+250)/16000=1737/8000`.

At the threshold `a=1/2`,

`(s a)^2-eta^2
 =(1597/4000)^2-(1737/8000)^2
 =(3194^2-1737^2)/8000^2
 =7184467/64000000`.

Therefore the residual-corrected cross-arm constant is

`c_*=(sqrt(7184467)-1612)/8000=0.1335482008234039...`.

To check `c_*>2/15`, it suffices to check

`sqrt(7184467)>8036/3`.

Both sides are positive, and

`9*7184467-8036^2=82907>0`.

Thus `c_*>2/15` exactly.

If additionally `s2(C)>=1/64`, then

`s1(C)s2(C)>(2/15)(1/64)=1/480`.

In the outside alternative the total carrier mass on `L` is `>1/2`, each atom is `<=1/25`, and a two-bin greedy partition has imbalance at most `1/25`; hence each bin has mass strictly larger than

`(1/2-1/25)/2=23/100`.

For the paid E3 branch, `s3(C)>=1/64` gives `e3(CC^T)>=64^-6`, so the marginal-free E3 receiver gives `||p_Q||_infinity<=64 K3`, with `K3=3*2^(4/3)*e^(1/3)=10.550168831164...`; numerically `64 K3=675.2108051945...<675.211`.
