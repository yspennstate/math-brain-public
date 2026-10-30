# Enlargement: the joint MUX tube has the same `q^2/8192` radius in address and data

The source-robust argument in `SOURCE_ROBUSTNESS_ADDENDUM.md` has enough reserve to enlarge the data-asymmetry radius by a factor `32`.

Keep
\[
0<q\le\frac12,
\qquad
q_0=q,
\qquad
q_1=1-q+\eta,
\qquad
\left|t-\frac12\right|\le{q^2\over8192},
\]
but now assume only
\[
\boxed{|\eta|\le {q^2\over8192}.}
\tag{E.1}
\]
This still implies `|eta|<q`, so every bias remains interior.

The exact six-mass variation estimates are unchanged:
\[
\delta_{TV}<5|\eta|,
\qquad
|\Delta H|<5|\eta|\log_2{3\over|\eta|}.
\tag{E.2}
\]
The source-robust non-spectral estimate is also unchanged:
\[
|\Delta D|_{\rm nonspectral}<(18L+105)|\eta|,
\qquad L=\log_2(1/q).
\tag{E.3}
\]
At the enlarged endpoint `|eta|=q^2/2^13`, equations (E.2)-(E.3) give total loss at most
\[
{q^2\over8192}
\left[28L+170+5\log_2 3\right].
\tag{E.4}
\]
Using
\[
qL\le1,
\qquad q\le\frac12,
\qquad \log_2 3<{8\over5},
\]
we get the clean bound
\[
\boxed{
|\Delta D|<{117\over8192}q.}
\tag{E.5}
\]

The newest fleet01/B18 complementary-data address theorem supplies at the same `t,q`
\[
D_{\Gamma^\dagger}(M;t,q,1-q)>{89\over4096}q={178\over8192}q.
\]
Therefore throughout (E.1)
\[
D_{\Gamma^\dagger}(M;t,q,1-q+\eta)
>{61\over8192}q.
\tag{E.6}
\]
Since
\[
{61\over8192}-{1\over135}
={43\over1105920}>0,
\]
we obtain the enlarged theorem
\[
\boxed{
D_{\Gamma^\dagger}(M;t,q,1-q+\eta)>{q\over135}>0
}
\tag{E.7}
\]
whenever both the address displacement and the complementary-data defect are at most `q^2/8192`.

The exact Poincare currency remains
\[
W_M={V_t(V_0+V_1)\over16}<{9q\over16},
\]
so the requested gate margin relative to the base `Gamma_0` satisfies
\[
\boxed{
c_M<a^\dagger-{16\over1215}
=0.2550361317201646\ldots<a^\dagger.}
\tag{E.8}
\]

Thus the current fixed candidate is proved on a genuinely unequal-data, off-center MUX tube with the **same quadratic radius** `q^2/8192` in the address and data-asymmetry directions. This is still not the full unequal-data MUX theorem and not full FEI.
