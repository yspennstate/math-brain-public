# Strengthening: the negative point-defect constant is `5/3`

All logarithms are base two.  We retain the notation of the reviewed proof.

## 1. Defect-block payment

For `p=2^{-r}` and `beta=1-2p`, direct spectral summation gives

\[
I(N_r)=2rp,
\qquad U(N_r)=\beta^2\log_2(1/\beta^2)+2rp\beta.
\tag{1}
\]

For `r=2` the ratio is one.  For `r=3` it is

\[
\frac34\left(1+\log_2\frac{16}{9}\right)<\frac32.
\]

At `r=4`,

\[
\frac{U(N_4)}{I(N_4)}
=\frac78+\frac{49}{32}\log_2\frac{64}{49}<\frac32.
\tag{2}
\]

Indeed `7^49>2^137` (for example, `7^45>2^126` from
`7^5>2^14`, and `7^4>2^11`), so
`log_2(64/49)<20/49`, which proves (2).

For `r>=5`, `-ln beta <=2p/beta` and `ln2>2/3` give

\[
\frac{U(N_r)}{I(N_r)}
\le\beta+\frac{2\beta}{r\ln2}
<1+\frac{2}{5\ln2}<\frac85<\frac53.
\tag{3}
\]

Thus every block is paid at coefficient `5/3`.

## 2. Sharpened scalar payment

The independently accepted shape calculation on `[-1,0]` gives

\[
R'''(t)<0,
\]

so `R''` decreases through one zero and `R'` first increases and then
decreases.  Since `R'(-1+)<0<R'(0-)`, `R'` crosses zero once and remains
positive thereafter.  Independently, direct differentiation yields

\[
R'(-1/2)=\frac94-
\frac{\frac34\ln(4/3)+\frac38}{\ln2}>0.
\tag{4}
\]

The last inequality follows from `ln(4/3)<1/3` and `ln2>2/3`.  Consequently
`R` is increasing on `[-1/2,-1/8]`, and hence

\[
R(-s)\le R(-1/8)\qquad(1/8\le s\le1/2).
\tag{5}
\]

At the endpoint,

\[
R(-1/8)=\frac{
49\log_2(256/49)+81\log_2(16/9)+51}{256}.
\tag{6}
\]

The exact comparisons `7^5>2^14` and `3^12>2^19` imply
`log_2 7>14/5` and `log_2 3>19/12`.  Substitution into (6) gives

\[
R(-1/8)<\frac{2361}{2560}<\frac{15}{16}.
\tag{7}
\]

## 3. Endpoint closure

The mean recurrence gives `m_k in [1/4,1/2]`.  Thus, with
`s_k=beta_km_{k-1}`, one has `s_k in [1/8,1/2]`.  At `c=5/3`,

\[
R(-s_k)<\frac{15}{16}
\le\frac53\frac{1+s_k}{2}.
\tag{8}
\]

Combining (1)--(3), (8), and the exact activation recurrence yields

\[
U(F_k)-cI(F_k)
\le\frac12\bigl(U(F_{k-1})-cI(F_{k-1})\bigr).
\]

The balanced first level closes for every `c>=1`.  Induction proves

\[
U(P)\le\frac53I(P)\Longrightarrow
U(F_d)\le\frac53I(F_d).
\]

The same signed endpoint telescope as in the source then gives retained loss
at most `5I(F_d)/3` for every permitted tree and common disjoint terminal
factor.  Finally, `H<=2I+2U` gives `H<=16I/3`.

The coefficient `5/3` is sufficient, not claimed optimal.  This strengthening
requires fresh independent review because B19 supplied it.
