# An `s_8` endpoint reduction: two completion hubs and determinant amplification

Run: `20260924T152240Z-fleet01-B20-fixedmult-r11`
Parent source: nine-eigenvalue paper blob `19fb119877426b640b2c0dae19ec2f78a399fe11`.
Status: **proved structural improvement below nine; NOT an eight-eigenvalue density theorem**.

Use the normalized constants of the nine-eigenvalue manuscript

\[
d=\frac3{40},\qquad p=\frac1{400},\qquad h=\frac2{25},\qquad
\kappa=h^2=\frac4{625}.
\]

Assume throughout that `A=A^T` has **no scalar or pair pivot** in the manuscript sense and
\[
s_8(A)\ge1.
\]
The no-pivot entry bounds are
\[
 |A_{ii}|<d,\qquad |A_{ij}|<\frac1{11}\quad(i\ne j).
\]
The already-proved order-two spectral-to-volume theorem gives
\[
V_2(A)\ge\kappa^2.
\]
If `V_3(A)>=kappa^3`, the existing order-three/random-cut/marginal-free receiver already pays a bounded density. The only endpoint considered here is therefore
\[
V_3(A)<\kappa^3. \tag{1}
\]

## Theorem: favorable seed with two amplifying physical arms

Under the assumptions above, there exist pairwise disjoint two-sets `S,T,H` with `H={h_1,h_2}`, with
\[
B=A_{S,T}\quad\text{invertible},
\]
such that, for the interpolation matrix
\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot},
\]
one has
\[
 |P_{h_ah_a}|>\frac{137}{200}\quad(a=1,2), \tag{2}
\]
\[
 |P_{h_1h_2}|,|P_{h_2h_1}|<\frac{91}{275}, \tag{3}
\]
and consequently
\[
 |\det P_{H,H}|>
 q_*:=\left(\frac{137}{200}\right)^2-
       \left(\frac{91}{275}\right)^2
 =\frac{348213}{968000}
 =0.3597241735\ldots . \tag{4}
\]
In particular both literal original-coordinate arms
\[
U=A_{S,H},\qquad C=A_{H,T}
\]
are invertible and satisfy
\[
 |\det U\,\det C|>q_*|\det B|. \tag{5}
\]
Since every entry of `U` and `C` has modulus `<1/11`,
\[
 |\det U|,|\det C|<\frac2{121}.
\]
Therefore **each arm individually amplifies the seed determinant**:
\[
\boxed{
 |\det U|,|\det C|>
 \gamma_*|\det B|,
 \qquad
 \gamma_*:=\frac{121q_*}{2}
 =\frac{348213}{16000}
 =21.7633125.
} \tag{6}
\]
Moreover the two same-index bordered minors obey
\[
 \left|\det A_{S\cup\{h_a\},\,T\cup\{h_a\}}\right|
 >\frac{19}{25}|\det B|,
 \qquad a=1,2. \tag{7}
\]
Thus the unpaid `s_8` endpoint contains not just aggregate overlap mass: one favorable volume-sampled seed has **two distinct exterior completion hubs**, and each creates a much stronger disjoint physical two-seed on either side.

### Proof

Apply the manuscript's volume-sampled interpolation lemma at `r=2`. Because `V_2>=kappa^2` and (1), some nonsingular disjoint seed `S,T` satisfies
\[
 \|E\|_F\le3\sqrt{V_3/V_2}<3\sqrt\kappa=3h=\frac6{25}, \tag{8}
\]
with decomposition
\[
 A=D+R+E,
\]
where `D` is diagonal and vanishes on `S union T`, `E` has zero diagonal, `rank R<=6`, and on `L=[n]\(S union T)` one has `R_{L,L}=P_{L,L}` and `rank P_{L,L}<=2`.

Weyl and the global rank bound give
\[
 s_8(D+R)=s_8(A-E)>1-\frac6{25}=\frac{19}{25},
\]
and then
\[
 s_2(D)\ge s_8(D+R)>\frac{19}{25}. \tag{9}
\]
Hence there are two coordinates `h_1,h_2 in L` with
\[
 |D_{h_ah_a}|>\frac{19}{25}. \tag{10}
\]
On `L`, by construction,
\[
 D_{ii}=A_{ii}-P_{ii},\qquad
 E_{ij}=A_{ij}-P_{ij}\quad(i\ne j).
\]
The no-pivot bounds and (8) therefore give
\[
 |P_{h_ah_a}|
 \ge |D_{h_ah_a}|-|A_{h_ah_a}|
 >\frac{19}{25}-\frac3{40}=\frac{137}{200},
\]
and
\[
 |P_{h_1h_2}|,|P_{h_2h_1}|
 <\frac1{11}+\frac6{25}=\frac{91}{275}.
\]
This proves (2)–(3). The determinant bound (4) follows from
\[
 |ad-bc|\ge |a||d|-|b||c|.
\]

Since
\[
 P_{H,H}=A_{H,T}B^{-1}A_{S,H}=CB^{-1}U,
\]
(4) implies invertibility of all three two-by-two factors and
\[
 \det P_{H,H}=\frac{\det C\det U}{\det B},
\]
which is (5). A two-by-two matrix with all entries `<1/11` in modulus has determinant modulus `<2/121`; dividing (5) by that upper bound proves both inequalities in (6).

Finally the same-index bordered determinant formula from the manuscript is
\[
 \det A_{S\cup\{h\},T\cup\{h\}}=\pm\det(B)D_{hh}.
\]
Together with (10) this gives (7). QED.

## Exact aligned obstruction to a tempting shortcut

The theorem above does **not** imply that the three two-by-two arms automatically create a disjoint order-three crossing. There is an exact product-coordinate algebraic obstruction.

Take six original coordinates in three two-coordinate banks `S,T,H`, and for `0<epsilon<p` set all within-bank blocks to zero and
\[
 A_{S,T}=\epsilon I_2,\qquad
 A_{S,H}=\sqrt\epsilon I_2,\qquad
 A_{H,T}=\sqrt\epsilon I_2,
\]
with transpose blocks imposed by symmetry. Then the matrix is the direct sum, across the two channels, of
\[
 \begin{pmatrix}
 0&\epsilon&\sqrt\epsilon\\
 \epsilon&0&\sqrt\epsilon\\
 \sqrt\epsilon&\sqrt\epsilon&0
 \end{pmatrix}.
\]
It has rank six. Relative to the seed `B=epsilon I_2`,
\[
 P_{H,H}=I_2,\qquad D_{H,H}=-I_2,
\]
and both arm determinants are `epsilon`, compared with `det B=epsilon^2`. Nevertheless **every disjoint three-by-three crossing minor on these six coordinates vanishes**, so `V_3=0` for this block. Thus the implication

> two invertible arms + a large completion diagonal ⇒ physical order-three crossing

is false without using the extra ambient spectral information.

This is a counterexample only to that intermediate shortcut, not to the `s_8` density theorem: a six-dimensional rank-six block has no eighth singular direction.

## Cycle-transversality identity for the next step

The exact `E=0` alignment equations expose a useful deterministic defect. Write
\[
U=A_{S,H},\qquad C=A_{H,T},\qquad B=A_{S,T}.
\]
For `k` outside `S union T union H`, put row vectors
\[
r_s=A_{k,S},\qquad r_t=A_{k,T}.
\]
Symmetry of the actual `L×L` block together with `A_{L,L}=P_{L,L}` gives
\[
 r_tB^{-1}U=r_sB^{-T}C^T.
\]
Since `U,C,B` are invertible,
\[
 r_s=r_tL_*,\qquad
 L_*:=B^{-1}UC^{-T}B^T. \tag{11}
\]
Hence the linear combination of the physical columns `S,T` with coefficients `(c,-L_*c)` vanishes on every row outside `S union T union H`. Its remaining `H`-component is governed by the two-by-two **cycle-transversality defect**
\[
 K_*:=U^T-CB^{-1}UC^{-T}B^T. \tag{12}
\]
For the aligned obstruction above, `K_*=0` exactly.

With nonzero interpolation error `E`, (11) becomes an approximate relation with an error controlled by the corresponding rows of `E`. A plausible route to `s_8` is therefore a dichotomy: quantitative `K_*` transversality should create a payably new physical direction, while small `K_*` forces the extra two target-scale singular directions to live outside the six-dimensional aligned carrier and should be exploitable by another physical cut. This last implication is **not proved here**.

## Remaining obligation for eight

The new endpoint is sharper but still unpaid. One must consume either the determinant-amplification structure (6) or the transversality defect (12) in a product-preserving analytic estimate. A direct iteration of (6) is not currently justified because the amplified arm seed need not inherit the volume-sampled small interpolation error. Any proof that ignores that distinction would repeat the already-known failure of the maximum-determinant-seed shortcut.

Therefore:

- nine eigenvalues: supported by the current candidate, subject to the independent-review gate;
- eight eigenvalues: **OPEN**;
- three eigenvalues: **OPEN**.
