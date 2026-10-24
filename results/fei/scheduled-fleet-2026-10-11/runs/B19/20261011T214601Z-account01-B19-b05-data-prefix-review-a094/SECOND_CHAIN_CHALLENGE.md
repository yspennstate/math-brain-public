# A094 second-chain challenge verdict

Target: `B05-A023-BENT-DATA-PREFIX-TELESCOPE-v1` at open-problems commit `8ffa3a930c849135d366d10d8d4f2e8afd0da67c`.

## Accepted chain

The restricted bent support size, sign counts, one-point Fourier shift, affine formula

\[
L_m=A_L-2\delta+2^m\rho(B_L+2\rho),
\]

constant nonnegative raw `L` credit, geometric telescope, single application of the activation probability, and terminal `L_h,Q_h` estimates were independently reconstructed and are correct for the declared family.

## Precisely located gap

The displayed `Gamma_m=L_m-L_(m+1)/2` is only the conditional-entropy component of the physical selector/data order-swap interaction. The full physical term is

\[
(L_m+Q_m)-\tfrac12(L_{m+1}+Q_{m+1}).
\]

B05 did not derive or sign the missing phase-prefix difference. Therefore its exact `L` telescope is accepted, but the unqualified physical-node interpretation was not independently proved by the submitted chain.

## Repair (contributor result; fresh review required)

With `j(t)=1-h_2(1/2+sqrt(t(1-t)))` and `R_\pm`, `A_Q`, `B_Q` defined as in `REPORT.md`, the same support count gives

\[
Q_m=A_Q-2\delta+2^m\rho(B_Q+2\rho),
\qquad
\Gamma_m^Q=(A_Q-2\delta)/2.
\]

The scalar inequality `h_2(r)<=2sqrt(r(1-r))` implies `j(t)>=2t` for `t<=1/2`; hence `Gamma_m^Q>=0`. Thus the complete physical raw credit is `Gamma_m^L+Gamma_m^Q>=0`, and the exact `L+Q` prefix telescope follows. Because this review supplies the missing step, the strengthened claim is `PROVED_PENDING_FRESH_INDEPENDENT_REVIEW`, not accepted by this same reviewer.

Full FEI remains open.
