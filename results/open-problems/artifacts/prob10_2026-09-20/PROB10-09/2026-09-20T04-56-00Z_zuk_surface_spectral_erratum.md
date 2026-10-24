# Correction to the 04:53 idea/checker labels

The primary Żuk paper states the safe theorem
\[
\|M_g\|\le g^{-1/2},
\]
not the strict inequality written in the 04:53 idea note and checker comment. For `g=4` the input used below is therefore
\[
\|A_4\|\le 8.
\]
This does **not** change the certificate: the exact check has strict positive slack at the conservative endpoint `Rbar=457297/31250`, so `beta_D(||A||)<z_*` still follows when `||A||<=Rbar`. No numerical value or gap changes. The final report uses only the safe non-strict Żuk theorem.