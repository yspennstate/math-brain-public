# fleet04/B16 — exact n=18 first-cell rescue for the committed h96 baseline

**Run:** `b16-20260922t071429z-fei`  
**Status:** `PARTIAL_PROVED_BASELINE_POINT_SAFE / AND_EXTREMALITY_ALREADY_FALSIFIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Full unrestricted uniform-cube FEI remains **OPEN / NOT PROVED**.

## 0. Control precedence and scope

\[
D_\Gamma(G;p)=
\sum_i {\operatorname{It}_i(G;p)\over V_{p_i}}
 [\Gamma(p_i)+h_2(V_{p_i})]
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\]
and for a quadratic lift \(\Gamma\mapsto \Gamma+a\,z(1-z)\),
\[
D_{\Gamma+a z(1-z)}=D_\Gamma+aW,\qquad
W={I(G;p)\over4}-p_{\rm out}(1-p_{\rm out})\ge0.
\]
Thus the comparable gate margin is
\[
c_G(p)=-D_\Gamma(G;p)/W.
\]

This run attacks the fresh composition-prime \(n=18\) obstruction in exactly those units.  It does not revive the old unsigned-current route.

## 1. Required inherited signed sources preserved

I re-read, without spending their ledgers:

1. fleet02/B16,
`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`,
creation revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`.
After same-syndrome **signed** aggregation it gives the authentic parent weights
\[
\mu_j=\sum_{R:j\ {\rm doubled}}{\varepsilon_{q_R,k_R}\over r_R}b_R^2,
\qquad
\sum_j\mu_j=E_{\rm cen}\le {11\over192}W.
\]
Nonnegativity is only legitimate after signed aggregation.

2. fleet03/B18,
`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`,
creation revision `4843e50690013fd18b85dd8763b53bdc75da79e8`.
Its authentic oriented sink is
\[
\kappa_i^K=p_i+4o_i^K,
\]
with the opposite-sign overlap \(o_i^K\) essential.

Original-coordinate orientation, opposite-sign overlap, dual-code multiplicity, negative credits, live-window/R16 terms and terminal payment remain live at their proved scopes.  None is re-spent in the scalar gate calculation below.

## 2. Fresh peer obstruction reduced to two source secants

I consume fleet02/B16's exact certified output
`20260922T063230Z-n18-exact-entropy-two-secant/check_exact_entropy_two_secant.out`.

For the composition-prime \(18\)-input gate \(F\), bias all nine core inputs by
\[
u={1\over5000},\qquad p_{x_i}={1\over2}+u,
\]
and leave the nine host inputs unbiased.  The peer checker reduces the lifted defect exactly to
\[
D_*(u)=B_0+A_1m_1+A_{12}m_{12},
\tag{2.1}
\]
where \(m_1,m_{12}\) are the two source secant slopes of \(G\) in
\(\Gamma_{\rm RO}(z)=sG(\log_2(1/s))\), \(s=\min(z,1-z)\).

It rigorously certifies
\[
A_1+A_{12}>0
\]
and, when \(m_1=m_{12}=m\), the unique sign threshold
\[
12.619835562701958406899771738309\ldots
<m_{\rm crit}<
12.619835562701958406899771738333\ldots .
\tag{2.2}
\]
It also certifies
\[
D_*(u)\big|_{m=30}>
2.0158864838143015\times10^{-6}.
\tag{2.3}
\]

The exact source arguments are
\[
r_1={2499\over5000}=0.4998,
\]
and
\[
r_2=1-p_{\rm out}
=0.499599218802499996040000115199999488.
\tag{2.4}
\]

## 3. New first-cell theorem for the committed baseline h96 source

The committed baseline certificate source is
`proofnet24/P03-fei/continuations/2026-09-21-readonce-certificate/data/cert_vi_h96k40.npz`,
Git blob `1e2a1a5c293fa7b6ec9885b7a410910d6589be80`.

The source grid constructor `fei_cert_vi.py` puts the first small-side cell at
\[
\left[{1023\over2048},{1\over2}\right]
=[0.49951171875,0.5].
\tag{3.1}
\]
By (2.4),
\[
{1023\over2048}<r_2<r_1<{1\over2}.
\tag{3.2}
\]
Therefore **both source secants lie in the same first affine h96 cell**, so
\[
m_1=m_{12}=m_{\rm base}.
\tag{3.3}
\]

Decoding the first two binary64 \(G\)-values from the exact committed NPZ blob gives
\[
G_0=\texttt{0x1.9d1b71758e219p+3},
\qquad
G_1=\texttt{0x1.9e76c3a5f50bcp+3}.
\tag{3.4}
\]
The node spacing in \(x=\log_2(1/s)\) is
\[
\Delta x=\log_2(1024/1023).
\]
A rational atanh-series enclosure, using the exact binary64 rationals in (3.4), certifies
\[
\boxed{
30.0783796336058879347644507621723
<m_{\rm base}<
30.0783796336058879347644507621724 .
}
\tag{3.5}
\]
In particular
\[
m_{\rm base}>30>m_{\rm crit}.
\]

Substituting the peer-certified coefficient intervals into (2.1) gives
\[
\boxed{
2.0249775625876039710013645554248\times10^{-6}
<
D_{\Gamma_{\rm base}+a_*z(1-z)}(F;p(u))
<
2.0249775625876039710013645554277\times10^{-6}
}
\tag{3.6}
\]
for \(a_*=0.268204856\).

Hence the exact \(u=1/5000\) coherent-core bias point **does not falsify the lifted committed baseline h96 potential**.

## 4. The gate margin, in the owner's requested units

For this point the peer exact currency is
\[
W=
0.259765502969375869532068437164660027266399033856017326079882035200262144.
\]
Therefore
\[
c_F(u)=a_*-{D_*(u)\over W}
\]
satisfies
\[
\boxed{
0.268197060593991734416322212779035229
<
c_F(u)
<
0.268197060593991734416322212779035240 .
}
\tag{4.1}
\]

The certified central value from the same source gate obeys
\[
c_F(0)<0.268182843692186302632575891794314.
\tag{4.2}
\]
Thus the coherent bias really **raises** the requested gate margin, exactly as the zero-mode birth calculation predicted, but at \(u=1/5000\) the committed baseline still has reserve
\[
a_*-c_F(u)>7.7954060082\times10^{-6}.
\tag{4.3}
\]

This is also a decisive correction to the proposed finite-falsification shortcut: the singular leading term by itself is not enough at this point.  The regular first-cell source slope repairs the defect.

## 5. What this settles and what it does not

### Settled

For every source potential whose two arguments in (2.4) lie in one affine cell with common slope \(m\), the exact peer reduction gives
\[
D_*(u)=B_0+(A_1+A_{12})m,
\]
with \(A_1+A_{12}>0\).  Consequently the point is decided by **one scalar**:
\[
m>m_{\rm crit}\Longrightarrow D_*(u)>0,\qquad
m<m_{\rm crit}\Longrightarrow D_*(u)<0,
\tag{5.1}
\]
with the certified \(m_{\rm crit}\) interval in (2.2).

The committed baseline h96 slope is far on the safe side by (3.5).

Also, the owner's original decomposable/AND-extremality subtarget for the unlifted read-once potential is already falsified by this same composition-prime gate: fleet02/B16 certifies the central requested margin
\[
c_F(0)>0.26818284369218,
\]
whereas the current read-once AND floor is about \(4.4\times10^{-3}\).  This falsifies that **potential/extremality claim**, not FEI.

### Not settled

The canonical all-gate report names a newer rough source file
`cert_vi_h96k40_f4.npz`, but those bytes are not present in the authorized repository path available in this run.  I therefore do **not** transfer (3.5)--(4.3) to `f4`.

For the missing `f4` shape, the entire \(u=1/5000\) test is now compressed to one datum if it uses the same first affine cell:
its first-cell slope \(m_{\rm f4}\).
The certified decision boundary is (2.2).

Full FEI remains open.

## 6. Verification

`check_b16_n18_first_cell_baseline.py` uses only the Python standard library.  It:

- checks the exact first-cell containment (3.2);
- binds the decoded source values by exact binary64 hex/bytes;
- proves (3.5) with rational atanh-series bounds for both \(\ln(1024/1023)\) and \(\ln2\);
- imports the peer's rigorous decimal intervals as exact rationals;
- checks \(m_{\rm base}>30>m_{\rm crit}\);
- derives the positive defect interval (3.6);
- derives the gate-margin interval (4.1);
- verifies the margin rose from the center but remains below \(a_*\).

No paid/remote compute, workflow dispatch, email/Drive, benchmark gold, mocks, unrelated private data, scheduler mutation, or notification enabling was used.
