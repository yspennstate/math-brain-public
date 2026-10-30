# r33 exact constant checks

All numerical values below are evaluations of the exact rational/algebraic expressions used in `REPORT.md`; they are regression checks, not substitutes for the analytic inequalities.

- `c3=11907/16384 = 0.72674560546875`.
- `L0=(63/64)c3-1/2048 = 749629/1048576 = 0.7149019241333008`.
- `z0=(1/4096)(L0-1/4096) = 749373/4294967296 = 0.00017447699792683125`.
- `8 sqrt(e) z0^(-1/8) = 38.906302166968054`.
- `Gamma0=sqrt((127/512)z0) = 0.006578637708152956`.
- `Gamma0/2 = 0.003289318854076478`.
- `16 Gamma0 = 0.10525820333044729`.
- `L1=(63/64)c3-3/4096 = 749373/1048576 = 0.7146577835083008`.
- `sqrt(L1) = 0.8453743451917031`.
- `sqrt(L1/2) = 0.5977699321261905`.
- `E_*=961/4096+L1/2 = 1241405/2097152 = 0.5919480323791504`.
- Fifth-volume payment at `E_*`, `delta=1/64`: `5 sqrt(2e) [120/((1/64)^4 E_*^5)]^(1/10) = 129.086423012756 <129.087`.
- Rank-three product floor on strong-top-four `W` with `s3(W)>=1/64`: `sqrt((63/256)E_*)/4096 = 9.318202298444798e-05`.
- Grouped-rank-three payment: `3e Delta3^(-1/3) = 179.87536644726364 <179.876`.
- Nested-cut `L0_*=(63/64)E_*-1/2048 = 78142979/134217728 = 0.5822105631232262`.
- Nested-cut `z_*=(1/4096)(L0_*-1/4096) = 78110211/549755813888 = 0.000142081646117731`.
- `8 sqrt(e) z_*^(-1/8) = 39.91811090469585`.
- `Gamma_*=sqrt((127/512)z_*) = 0.005936573785809375`.
- `Gamma_*/2 = 0.0029682868929046874`.
- `16 Gamma_* = 0.0949851805729500`.

Status: `CHECK_PASS`.
