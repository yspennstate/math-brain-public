# Typographical correction to REPORT.md

In `REPORT.md`, equation (3.4) contains the string `\nu` because a newline and the scalar `u` were accidentally joined in the source. The intended and proved inequality is

\[
\boxed{
\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j
>
u\,(0.4194-170d),
}
\]

where the `u` immediately after `>` is the scalar
\[
u=\min(t,1-t).
\]

Equivalently, without any ambiguous TeX control sequence,
\[
\boxed{
\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j
>
\min(t,1-t)\,(0.4194-170|r_1-r_0|).
}
\]

No mathematical claim, hypothesis, constant, or later equation changes. In particular the stated consequence at `|r_1-r_0|<=1/512` remains
\[
\mathcal R_{\Gamma^\dagger,j}+\mathcal C_j
>{13979\over160000}\min(t,1-t)>0.
\]
