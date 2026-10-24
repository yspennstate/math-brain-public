# C0032 endpoint-deformation artifact — immutable erratum

Parent artifact:

`research7_2026-09-17/R7-06/artifacts/2026-09-19/2026-09-19T030400Z__C0032_endpoint_deformation_struveK_inverse_ode.md`

Creation commit of parent artifact: `8d20074bb0dc98e39cf6469adfaeaf84d1a8080c`.

Exact-SHA readback found one typographical escape loss in equation (2.20).  The token printed as

```text
1+
arepsilon
[ ... ]
```

must read

\[
\boxed{
\frac{d}{ds}M_{1-\varepsilon}
=
1+\varepsilon
\left[
1-\gamma_E+\log(1-s)-\frac{s}{1-s}
\right]
+O(\varepsilon^2).
}
\]

No theorem, coefficient, sign, argument, or conclusion changes.  Equations (2.14), (2.16), (2.18), and (2.19) in the parent artifact already contain the correct `\varepsilon` notation and determine this derivative formula uniquely.  The parent artifact is left immutable as required.