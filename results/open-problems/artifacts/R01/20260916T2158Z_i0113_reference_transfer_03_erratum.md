# R01 I0113 run 20260916T2158Z — notation erratum

This is a typographical correction to `runs/R01/20260916T2158Z_i0113_reference_transfer_03.md`; it does not change any claim or argument.

In the proof of `R01-I0113-C003`, immediately after (3.3), the displayed identity should read

\[
u_i^{\pi}(x)-u_i^{\nu}(x)=d_i(x),
\]

where `u_i^mu(x)=log r_i^mu(x)` was defined just above. The run report accidentally rendered the left-hand first symbol as `nu_i^pi`.

Also, the scalar function in the path-KL integrand is intended as

\[
F(z)=z e^z-e^z+1=\int_0^z v e^v\,dv.
\]

The subsequent bound `0 <= F(z) <= (1/2)e^{|z|}z^2` and all downstream estimates use this intended expression.
