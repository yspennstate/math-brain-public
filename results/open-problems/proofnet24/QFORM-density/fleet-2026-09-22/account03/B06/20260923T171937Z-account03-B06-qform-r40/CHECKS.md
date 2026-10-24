# r40 exact arithmetic checks

`check_r40.py` is a finite arithmetic sanity checker for the constants in `REPORT.md`; it is not the proof.

Expected/verified output from the same exact formulas:

```text
QFORM_B06_R40_CHECK_PASS
T0/E0 = 0.00013861381749322618
tail/top2 ratio majorant = 0.009438462146148782 < 1/64
pair-law endpoint excess = 0.011046142578125
top-plane leverage floor = 0.59375
cross-star norm floor = 0.08211131956518221
small-mutual-edge residual-star norm floor = 0.07593224809483434
small-mutual-edge residual-star product floor = 0.005765706300735474
Z2 absolute floor = 0.007994596888238448
same-anchor cofactor bank floor = 0.0015989193776476895
same-anchor cofactor Frobenius norm floor = 0.03998648993907429
large-mutual-edge density bound = 546.8943841424625
```

Exact identities checked:

- `T0/E0 = 6316/45565443 < 1/7000`.
- `(2048/31)(1/7000+1/(2*7000^2)) = 224016/23734375 < 1/64`.
- At `(C,m)=(1/256,3/5)`, `F(C,m)-1/256 = 9049/819200 > 0`.
- `(11907/1048576)(19/32)=226233/33554432`.
- `226233/33554432-1/1024=193465/33554432`.
- `(31/2048)(11907/16384)^2=4395076119/549755813888`.
- One-fifth of the preceding quantity is `4395076119/2748779069440`.

The proof itself is symbolic and appears in `REPORT.md`; no Monte Carlo or histogram is used.
