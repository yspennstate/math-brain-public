# Source correction to REPORT.md equation (3.2)

The intermediate strict-sign display in `REPORT.md` equation (3.2) should be read as

\[
R_{\rm wit}(\psi)\le \kappa\,\mathcal K(\eta)
\le 0.069645\,\mathcal K(\eta),
\]

not with a strict `<` in the second comparison. The distinction matters only at the endpoint `\mathcal K(\eta)=0`: from `\kappa<0.069645` one cannot infer `\kappa\mathcal K<0.069645\mathcal K` when `\mathcal K=0`.

The stated repair-frontier theorem is unchanged. Indeed the source witness has `d>d_0`, so

\[
d\le {1078193\over1048576}E+R_{\rm wit}(\psi)
\le {1078193\over1048576}E+0.069645\mathcal K(\eta)
\]

implies the strict conclusion

\[
{1078193\over1048576}E+0.069645\mathcal K(\eta)>d_0.
\]

All numerical frontier values, the zero-AND-loss center threshold, and the joint shape/AND barrier therefore remain exactly as reported. This correction preserves the immutable original report and fixes only the endpoint comparison sign.
