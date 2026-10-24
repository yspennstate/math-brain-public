# Tensorization of the moment certificate

19 September 2026. For a product kernel W tensor V with product measure,
the triple kernel, transfer matrix, and self-adjoint realization factor as
tensor products after permuting pair coordinates. Thus

    tau_j(W^tensor m)=tau_j(W)^m,
    t_H(W^tensor m)=t_H(W)^m.

If z is a positive gauge, its product gauge satisfies

    q(z^tensor m)=q(z)^m.

A certified Perron lower bound beta becomes beta^m. Therefore the bound
in BALANCED_MOMENTS.md applied to W^tensor m is evaluated without building
an exponentially sized matrix: replace tau_j by tau_j^m, beta by beta^m,
and a by q(z)^m/2. In particular a is NOT replaced by a^m. A positive
lower bound L_m gives t_H(W)>=L_m^(1/m).

This is a valid extension, but fixed-parameter tensor amplification does
not automatically strengthen the certificate. For the normalized complete
triangle host, p=(1/3,1/3,1/3), W_ij=(3/2)1_{i!=j}, use beta=9/8 and q=3/2.
Its moments are

    tau_2=81/32, tau_3=567/256,
    tau_4=4617/2048, tau_5=37179/16384.

The one-copy optimized bound is 397305/180224>2. At the fifth tensor power,
with the product gauge and beta^5, the optimized bound is negative. All
powers one through six are checked exactly by check_tensorization.py;
none improves on the original bound after taking the appropriate root.
The target densities are positive and exceed one. This is not a Sidorenko
counterexample and does not rule out adaptive gauge/Perron choices or
other tensor arguments. It rules out treating this simple amplification
as a finished global step.
