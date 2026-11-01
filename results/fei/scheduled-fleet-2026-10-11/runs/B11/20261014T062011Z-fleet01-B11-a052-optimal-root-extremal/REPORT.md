# B11 / A052 — optimal root-KL payment on the true extremal class

**Status:** PROVED sharp root-row theorem and a strictly smaller sufficient
GU aggregate; independent review pending. The aggregate itself, universal GU,
and full FEI remain **OPEN**.

## Frozen candidate and mechanism change

- Primary packet: **A052 (critical-source structure)**.
- Stable gap: `G-GU-SIGNED-KL`.
- Attempt: `A052-OPTIMAL-ROOT-EXTREMAL-6`.
- Claim version: `B11-A052-OPTIMAL-ROOT-EXTREMAL-v1`.
- Frozen GU pair: `(a,b)=(4,3/4)`.

The preceding B11 attempt refuted every fixed unqualified tensor-prime
good-coordinate curvature bound using even quadratic phases. This run changes
mechanism: it uses signed Boolean convolution to remove the root KL rows, and
uses minimal-counterexample structure only to restrict the remaining
aggregate to tensor-prime functions with positive frozen residual.

## Sharp root theorem

For the root row of the exact identity

\[
\Delta_iU=B_i-\Gamma_i+K_i,
\]

write `a=fhat(empty)`, `b=fhat({i})`, and `m=a^2+b^2`. Boolean convolution
forces the root posterior asymmetry to zero, hence

\[
K_i^{(0)}=m\left[1-h_2\left(\frac{1+2ab/m}{2}\right)\right].
\]

The new sharp scalar estimate is

\[
\boxed{K_i^{(0)}\le\frac{2}{\ln2}\min\{a^2,b^2\}.}
\]

It follows by integrating
`atanh(x) <= x/sqrt(1-x^2)` after setting
`x=2 sqrt(r(1-r))`, `r=min(a^2,b^2)/m`. The coefficient is optimal because
the ratio tends to `2/ln2` as the smaller Fourier coefficient tends to zero.

Define

\[
M_1(f)=\sum_i\min\{p(\varnothing),p(\{i\})\}
\]

and let `D_+` be the complete signed contribution

\[
D_+=\sum_i(B_i-\Gamma_i)+\sum_iK_i^{(+)},
\]

where `K_i^(+)` contains exactly the nonempty upper-set rows. Then

\[
\boxed{G(f)\le D_+(f)+\frac{2}{\ln2}M_1(f).}
\]

## Smaller sufficient GU endpoint

Let

\[
R(f)=G(f)-4I(f)-\frac34U(f).
\]

Residual additivity shows that a counterexample has a tensor-prime factor
with `R>0`; no all-dimensional optimizer is assumed. Therefore it now
suffices to prove only on tensor-prime Boolean functions with `R>0` that

\[
\boxed{
D_+(f)+\frac{2}{\ln2}M_1(f)
\le4I(f)+\frac34U(f).
}
\tag{E}
\]

This implies `G<=4I+3U/4`, hence the source-reviewed reduction gives

\[
U\le16I,\qquad H\le34I.
\]

The previous coefficient-four root payment consumed the entire `4I` budget
and left `D_+<=3U/4`. The new endpoint permits

\[
D_+\le4I+\frac34U-\frac{2}{\ln2}M_1.
\]

Since `M_1<=I`, this adds at least
`(4-2/ln2)I = 1.114609918... I` of allowance, while retaining the exact
bias-sensitive singleton reserve.

## Verification and scope

The checker reconstructs the signed rows from literal Walsh coefficients and
physical restrictions for all **32,906** Boolean signs modulo global output
sign through dimension four. It verifies the exact local identity, the sharp
root payment, and zero violations of (E) in that finite domain. Point defects
approach the optimal constant `2/ln2`.

Finite checks do not prove (E) in all dimensions. The even quadratic phases
from the previous run have negative frozen residual and are correctly outside
the quantified critical class. This is not an exception and does not prove
that a positive-residual function exists.

## Before / after / next unpaid step

- **Before:** the unqualified curvature route was refuted, while B07's root
  payment used coefficient four and left no influence for nonempty rows.
- **After:** the root coefficient is sharp, bias-sensitive, and the remaining
  obligation is (E) only on positive-residual tensor-prime sources.
- **Still unpaid:** bound the nonempty signed KL rows together with
  `sum(B_i-Gamma_i)`; arbitrary spectral laws are outside scope.
- **Next action:** expand the first nonempty rows `|A|=1` under the full
  convolution identities and test whether their aggregate is paid by
  `4I-(2/ln2)M_1` without reusing singleton mass.

Requested independent reviewers: **A090 and A094**. No independent
acceptance or native Brain ingestion is claimed.
