# Exact checks

Local symbolic/high-precision execution of `CHECK.py` returned:

```text
QFORM_B17_INF_TARRAY_MIXED_FRAME_CHECK_PASS
R0BR0T = Matrix([[-15/28, -5/28, 1/4, 17/28], [-5/28, 17/28, -1/4, 15/28], [1/4, -1/4, 3/4, 1/4], [17/28, 15/28, 1/4, 5/28]])
C0 = 4.242640687119285146405066172629094235709
C1 = 2.903648694229720197573962315226727857944
C9 = 2.918523551643464541665013978187152809970
Ctet = 2.942775602943224786624343258228361753633
```

Checked exactly: `R0^T R0=I_3`; `B^2=I_3`; `charpoly(B)=(lambda-1)^2(lambda+1)`; every entry of `R0 B R0^T` is nonzero; its largest absolute entry is `3/4`; every row of `R0` has squared norm `3/4`. The strict numerical chain is `Ctet < pi < 3sqrt(2)`.

The checker verifies the explicit algebra/constants only. The infinitesimal-triangular-array Gaussian-floor theorem is proved analytically in `REPORT.md`; the finite-stage Fourier majorant and the random-location Gaussian inequality are source-pinned dependencies there.
