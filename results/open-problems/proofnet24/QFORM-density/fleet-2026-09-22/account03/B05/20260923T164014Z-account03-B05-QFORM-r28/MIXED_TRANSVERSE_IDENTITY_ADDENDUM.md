# r28 addendum — exact mixed-transverse Gram identity

This addendum continues the same actual-hour run `20260923T164014Z-account03-B05-QFORM-r28`. It does not alter the full-QFORM status: the conjecture and full continuity remain OPEN.

## Setup

Use the ratio-packet notation from `REPORT.md` and `LATE_SOURCE_REFRESH_ADDENDUM.md`:

\[
B=\begin{pmatrix}a&c\\ c&d\end{pmatrix},\qquad \Delta=\det B<0,
\]
\[
P=\begin{pmatrix}\alpha&\beta\\ r&s\end{pmatrix},\qquad q=(r,s)^T,
\]
\[
C=P B^{-1}P^T+\begin{pmatrix}L&0\\0&0\end{pmatrix},
\qquad \tau:=\det P=\alpha s-\beta r.
\]
The already-recorded transverse currencies are
\[
T_Y=Lr^2+\frac{a}{\Delta}\tau^2,
\qquad
T_Z=Ls^2+\frac{d}{\Delta}\tau^2.
\]
They arise from the vectors
\[
u:=J(\alpha,r)^T=(-r,\alpha)^T,
\qquad
v:=J(\beta,s)^T=(-s,\beta)^T,
\]
namely `T_Y=u^T C u` and `T_Z=v^T C v`.

## Lemma — `QFORM-MIXED-TRANSVERSE-GRAM-IDENTITY-v1`

Define the mixed transverse entry
\[
U:=u^T C v.
\]
Then
\[
\boxed{U=Lrs+\frac{c}{\Delta}\tau^2.}
\tag{1}
\]
Moreover the full transverse Gram matrix
\[
K:=\begin{pmatrix}T_Y&U\\U&T_Z\end{pmatrix}
=[u\ v]^T C [u\ v]
\]
satisfies the exact determinant identity
\[
\boxed{T_YT_Z-U^2=\tau^2\det C.}
\tag{2}
\]
Finally
\[
\boxed{\det C=\frac{\tau^2}{\Delta}+L\,q^TB^{-1}q,}
\tag{3}
\]
so that
\[
\boxed{
T_YT_Z-U^2
=\tau^2\left(\frac{\tau^2}{\Delta}+L\,q^TB^{-1}q\right).
}
\tag{4}
\]

### Proof

Because
\[
P^Tu=(0,\tau)^T,\qquad P^Tv=(-\tau,0)^T,
\]
and
\[
B^{-1}=\frac1\Delta\begin{pmatrix}d&-c\\-c&a\end{pmatrix},
\]
we obtain
\[
u^T P B^{-1}P^Tv=\frac{c}{\Delta}\tau^2.
\]
The rank-one Schur term contributes `L(-r)(-s)=Lrs`, proving (1).

Also `det[u v]=\alpha s-\beta r=\tau`. Therefore
\[
\det K=\det([u\ v])^2\det C=\tau^2\det C,
\]
which is exactly (2).

For (3), first
\[
\det(PB^{-1}P^T)=\frac{(\det P)^2}{\det B}=\frac{\tau^2}{\Delta}.
\]
Adding `L e_1e_1^T` to a symmetric `2 x 2` matrix changes its determinant by `L` times the `(2,2)` entry. The `(2,2)` entry of `PB^{-1}P^T` is `q^TB^{-1}q`, giving (3). Substitution proves (4). QED.

## Quantitative consequence for the live cancellation chamber

The late source refresh showed that the source-matching near-null scalar/dependent-pair theorem pays every state with
\[
\Psi:=\max(|T_Y|z_2^2,|T_Z|z_1^2)
\]
quantitative, while the fresh-square atlas pays quantitative
\[
\chi:=\max(|d|z_1^2,|a|z_2^2).
\]
Equations (1)--(4) identify what is left when both diagonal transverse currencies cancel.

For any nonzero `tau`,
\[
U^2= T_YT_Z-\tau^2\det C,
\]
hence by the reverse triangle inequality
\[
\boxed{
U^2\ge \bigl||\tau|^2|\det C|-|T_YT_Z|\bigr|.
}
\tag{5}
\]
In particular, if
\[
|T_YT_Z|\le \tfrac12 |\tau|^2|\det C|,
\]
then
\[
\boxed{|U|\ge 2^{-1/2}|\tau|\sqrt{|\det C|}.}
\tag{6}
\]
Thus a simultaneous cancellation of `T_Y` and `T_Z` cannot erase the entire transverse quadratic geometry whenever `|tau|^2 |det C|` remains quantitative: it forces the missing curvature into the **off-diagonal transverse entry** `U`.

This is not yet a density theorem. The vectors `u,v` live inside the same two-dimensional projection `(S,R)` of one original product bank, so treating them as independent coordinates would be invalid. The next analytic receiver must spend a quantitative `U` jointly with that bank's original product provenance before taking a reciprocal coarea factor. If instead `|tau|^2|det C|` is also small, then (2) shows that the entire transverse `2 x 2` Gram determinant is genuinely small; the third resource must then be sought in the escaped-curvature/structural branch rather than in another reparametrization of `T_Y,T_Z`.

Accordingly the refined unpaid implication is:

`QFORM-MIXED-OFFDIAGONAL-TRANSVERSE-COAREA-v1`: in the live ratio packet, after the `chi` and `Psi` exits fail, prove a product-preserving interval/coarea bound from a quantitative off-diagonal transverse currency `U`, or else use the exact smallness of `tau^2 det C` to force a different original-coordinate curvature aggregate.

No Gaussianity, moment, support, log-concavity, connected-support, post-rotation independence, conditional projection-density cap, or pointwise law-uniform oscillatory decay is used in this identity.