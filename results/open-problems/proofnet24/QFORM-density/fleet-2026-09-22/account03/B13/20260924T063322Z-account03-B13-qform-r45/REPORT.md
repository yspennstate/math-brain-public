SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-24T06:33:22Z.
attacking: rank-one-plus-four-diagonal survivor; first strengthen the exact diffuse-rank-two receiver by spending two literal physical squares simultaneously, then apply account04/B13's newest physical-star alternative without deleting the residual mode.

# account03/B13 r45 — two-square Strichartz receiver and rho^{-7/3} determinant collapse

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T063322Z-account03-B13-qform-r45`  
Role: extremal product laws / quantitative inequalities and rigorous computations  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING CONTINUOUS-DENSITY THEOREM + STRONGER HIGH-DENSITY NORMAL FORM / FULL QFORM OPEN**.

All random variables below are the original independent physical coordinates. A two-dimensional rotation is used only to diagonalize the latent rank-two coefficient matrix; it never rotates the independent random variables. No moment, compact-support, connected-support, log-concavity, centered-uniform, interval-extremality, pointwise law-uniform van der Corput estimate, fiber supremum, or deletion of a coefficient-small random quadratic term is used.

## 1. Source-pinned inputs

Fresh control is OWNER CONTROL revision `2026-09-22.15`, QFORM-only and unpaused. The full conjecture and full-target continuity remain open.

The previous B13 run is

- `yspennstate/math-open-problems@57ccfc48fbd392d6b1948c288308c9e3db05e69b`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260924T053240Z-account03-B13-qform-r44/REPORT.md`.

It proves the one-physical-square theorem for
\[
A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad \max_i c_i\le1/3,\quad c_i=\|u_i\|^2,
\]
namely a continuous-density bound
\[
\|p_Q\|_\infty\le C_{\rm sq}(1+|\det\Lambda|^{-6/13})
\]
when one original coordinate has `|d_k|>=1`. Its analytic inputs include the rank-two Fresnel identity, geometric Brascamp--Lieb, sharp Hausdorff--Young, and the one-dimensional parabola mixed estimate
\[
\|T_df\|_{L_t^rL_s^q}\le S_*|d|^{-1/r}\|f\|_2,
\qquad {2\over r}+{1\over q}={1\over2},\quad 2\le q\le\infty.
\tag{1.1}
\]

The designated partner `account04/B13` supplies three completed inputs.

1. Optimizer-free slab dichotomy, `math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`: in the diffuse exact-rank-two chamber with `s_3(A)>=1`, there is a physical `k` with `|d_k|>=1`, and every slab ratio `rho` satisfies
\[
|A_{kk}\det\Lambda|\le1536e^2\rho^{-4}.
\tag{1.2}
\]
The previous r44 run uses this to close the determinant-lower branch and shows that every sufficiently high-ratio survivor satisfies
\[
D_\Lambda:=|\det\Lambda|\le H\rho^{-2},\qquad
H:=\sqrt{1536e^2}=106.534455308869\ldots .
\tag{1.3}
\]

2. Fifth-diagonal sparsification, `math-open-problems@635da12cb1c19b27c455c662be800eb1113dd845`:
\[
d_{(5)}\le C_5\rho^{-1},\qquad C_5=2\sqrt{30\pi}=19.416259125557\ldots .
\tag{1.4}
\]
The same partner line proves the optimizer-free cap-one-product reduction, with no interval, common-diameter, or fixed-fragment conclusion.

3. Newest partner result, `math-open-problems@8b90908a934588442491cf1a41c7db12ece290bf`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260924T061740Z-account04-B13-nearnull-star-r3/REPORT.md`: for `k` chosen with `|d_k|=||D||op>=1`, every slab witness obeys
\[
\boxed{
D_\Lambda<3072e^2\rho^{-4}
\quad\text{or}\quad
\|A_{-k,k}\|_2\ge2^{-1/2}.
}
\tag{1.5}
\]
If `C` is the four-coordinate set of largest `|d_i|` containing `k`, the star branch further gives
\[
\|A_{C\setminus\{k\},k}\|_2\ge1/2
\quad\text{or}\quad
\|A_{C^c,k}\|_2\ge1/2.
\tag{1.6}
\]

## 2. Multi-square rank-two receiver

### Theorem 2.1 — `QFORM-R2-MULTISQUARE-STRICHARTZ-v1`

Assume
\[
A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad \max_i c_i\le1/3,
\tag{2.1}
\]
with `Lambda` real symmetric invertible. Let `K` be a set of `m` distinct original coordinates, `2<=m<=4`, such that `d_i!=0` for every `i in K`. Arbitrary deterministic affine terms are allowed.

For `i in K`, define
\[
q_i=c_i^{-1}\quad(c_i>0),\qquad q_i=\infty\quad(c_i=0),
\]
\[
{1\over r_i}={1-2c_i\over4},\qquad
\alpha:=\sum_{i\in K}{1\over r_i}
={m\over4}-{1\over2}\sum_{i\in K}c_i.
\tag{2.2}
\]
Then
\[
{m\over12}\le\alpha\le{m\over4}\le1.
\tag{2.3}
\]
There is a universal finite constant `C_m`, depending only on `m<=4`, such that the output has a bounded continuous density and
\[
\boxed{
\|p_Q\|_\infty
\le C_m\left[
1+\left(
D_\Lambda^{-1/2}
\prod_{i\in K}|d_i|^{-1/r_i}
\right)^{1/(1+\alpha)}
\right].
}
\tag{2.4}
\]
The conclusion is uniform over all independent cap-one input laws and over all affine terms.

### Proof

For fixed `t`, put
\[
G_i(t,s)=\int f_i(x)e^{it(d_ix^2+b_ix)}e^{isx}\,dx.
\tag{2.5}
\]
The rank-two Fresnel representation used in r44 gives
\[
|\phi_Q(t)|
\le (4\pi|t|)^{-1}D_\Lambda^{-1/2}J(t),
\quad
J(t)=\int_{\mathbb R^2}\prod_i
|G_i(t,\langle u_i,\xi\rangle)|\,d\xi.
\tag{2.6}
\]

For `c_i>0`, write `u_i=sqrt(c_i) v_i`; then
\[
\sum_i c_i v_iv_i^T=I_2.
\]
Geometric Brascamp--Lieb gives
\[
J(t)\le
\prod_{c_i>0}c_i^{-c_i/2}
\|G_i(t,\cdot)\|_{L^{1/c_i}}.
\tag{2.7}
\]
Zero rows factor outside the two-dimensional integral as `|G_i(t,0)|`; they correspond exactly to the `q_i=infinity` endpoint below.

For every nonspecial row, sharp Hausdorff--Young gives
\[
c_i^{-c_i/2}\|G_i(t,\cdot)\|_{1/c_i}
\le (2\pi)^{c_i}(1-c_i)^{-(1-c_i)/2}.
\tag{2.8}
\]
Since `-(1-c)log(1-c)<=c`, the product of all nonspecial factors is bounded by a universal constant depending only on total dimension two. For special positive-leverage rows retain the norms in (2.7); the extra factors `c_i^{-c_i/2}` are uniformly bounded for `0<c_i<=1/3`. Thus
\[
|\phi_Q(t)|
\le C D_\Lambda^{-1/2}|t|^{-1}
\prod_{i\in K}F_i(t),
\quad
F_i(t):=\|G_i(t,\cdot)\|_{L^{q_i}},
\tag{2.9}
\]
with the evident `F_i(t)=|G_i(t,0)|` when `c_i=0`.

By the one-dimensional mixed parabola estimate (1.1),
\[
\|F_i\|_{L_t^{r_i}}
\le S_*|d_i|^{-1/r_i}.
\tag{2.10}
\]
For `T>=1`, apply Holder to (2.9) on `|t|>T`. If `alpha<1`, use the remaining exponent `s=1/(1-alpha)`; if `alpha=1`, use `s=infinity`. In either case
\[
\int_{|t|>T}|\phi_Q(t)|dt
\le C_m D_\Lambda^{-1/2}
\left(\prod_{i\in K}|d_i|^{-1/r_i}\right)T^{-\alpha}.
\tag{2.11}
\]
The Holder constant is uniform because `m>=2` and (2.3) gives `alpha>=1/6`.

On `|t|<=T`, use only `|phi_Q(t)|<=1`, giving cost `2T`. With
\[
B=D_\Lambda^{-1/2}
\prod_{i\in K}|d_i|^{-1/r_i},
\]
choose `T=max(1,B^{1/(1+alpha)})`. Then
\[
\|\phi_Q\|_1\le C_m(1+B^{1/(1+\alpha)}).
\tag{2.12}
\]
Fourier inversion yields a bounded continuous density, proving (2.4). No pointwise law-uniform quadratic decay estimate was used: all law-uniform control is in integrated mixed norms. QED.

## 3. Uniform two-square corollary

For `m=2`,
\[
{1\over6}\le\alpha\le{1\over2}.
\]
If the two selected physical diagonals satisfy `|d_i|,|d_j|>=delta`, with `0<delta<=1`, and `0<D_Lambda<=1`, then (2.4) gives
\[
\boxed{
\|p_Q\|_\infty
\le C_2'\left(1+\delta^{-1/3}D_\Lambda^{-3/7}\right).
}
\tag{3.1}
\]
Indeed the determinant exponent is
\[
\beta(\alpha)={1\over2(1+\alpha)}\le{3\over7},
\]
and the diagonal exponent is
\[
\gamma(\alpha)={\alpha\over1+\alpha}\le{1\over3}.
\]
Because `delta,D_Lambda<=1`, replacing the exact exponents by these maxima only enlarges the right side.

## 4. High density forces two literal physical squares

Return to the surviving diffuse exact-rank-two target chamber and diagonalize `Lambda` only in its two-dimensional latent space:
\[
U\Lambda U^T=\lambda_1 vv^T+\lambda_2ww^T,
\qquad |\lambda_1|\ge|\lambda_2|.
\tag{4.1}
\]
This preserves every physical input coordinate and every row leverage.

The r44/partner branch (1.3) gives
\[
D_\Lambda=|\lambda_1\lambda_2|\le H\rho^{-2}.
\]
Hence
\[
|\lambda_2|\le\sqrt{D_\Lambda}
\le\sqrt H\,\rho^{-1},
\qquad \sqrt H=10.321552950446\ldots .
\tag{4.2}
\]

Because `lambda_1 vv^T` has rank one, the singular-value rank inequality gives
\[
s_3(A)\le s_2(D+\lambda_2ww^T).
\tag{4.3}
\]
The target has `s_3(A)>=1`, so
\[
1\le s_2(D+\lambda_2ww^T)
\le s_2(D)+|\lambda_2|.
\tag{4.4}
\]
Therefore
\[
\boxed{s_2(D)\ge1-|\lambda_2|.}
\tag{4.5}
\]
For `rho>=2sqrt(H)`, there are consequently at least two original coordinates `i,j` with
\[
\boxed{|d_i|,|d_j|\ge1/2.}
\tag{4.6}
\]
This implication uses only the target spectral hypothesis and the already-proved determinant branch; it does not rotate or condition the input law.

## 5. New self-improvement: determinant collapse rho^{-7/3}

For sufficiently high `rho`, (1.3) also gives `D_Lambda<=1`, so apply (3.1) to the two coordinates in (4.6) with `delta=1/2`:
\[
\rho\le\|p_Q\|_\infty
\le K_2(1+D_\Lambda^{-3/7})
\tag{5.1}
\]
for one universal finite `K_2`.

Thus, whenever additionally `rho>=2K_2`,
\[
{\rho\over2K_2}\le D_\Lambda^{-3/7},
\]
and hence
\[
\boxed{
D_\Lambda\le (2K_2)^{7/3}\rho^{-7/3}.
}
\tag{5.2}
\]
In particular the secondary entangled carrier mode obeys
\[
\boxed{
|\lambda_2|\le (2K_2)^{7/6}\rho^{-7/6},
\qquad
\rho|\lambda_2|=O(\rho^{-1/6})\to0.
}
\tag{5.3}
\]
This is stronger than the preceding `O(rho^{-1})` control on the second mode. It does **not** authorize deleting that mode from the random quadratic form; arbitrary fragmented and remotely translated supports still make coefficient-small perturbation arguments unsafe.

## 6. Applying the newest account04/B13 physical-star theorem

Now apply the partner's actual inequality (1.5), not just its structural language. Let
\[
L:=3072e^2=22699.180335914956\ldots .
\]
Every high-ratio witness has one of two alternatives.

### A. Ultra-near-rank-one packet

If
\[
D_\Lambda<L\rho^{-4},
\]
then
\[
\boxed{|\lambda_2|<\sqrt L\,\rho^{-2}
=150.662471557833\ldots\rho^{-2}.}
\tag{6.1}
\]

### B. Fixed original-coordinate physical star

Otherwise the partner gives
\[
\|A_{-k,k}\|_2\ge2^{-1/2}.
\]
Since the diagonal matrix contributes no off-diagonal star,
\[
A_{-k,k}
=\lambda_1v_kv_{-k}+\lambda_2w_kw_{-k}.
\]
For a unit vector `w`,
\[
|w_k|\|w_{-k}\|_2\le1/2,
\]
so (5.3) yields
\[
\boxed{
\|\lambda_1v_kv_{-k}\|_2
\ge2^{-1/2}-{1\over2}|\lambda_2|
=2^{-1/2}-O(\rho^{-7/6}).
}
\tag{6.2}
\]
Thus the partner's fixed physical star asymptotically belongs to the **dominant rank-one mode**, not the vanishing second mode.

Let `C` be the partner's four-coordinate diagonal core. From (1.6), one also has the source-compatible localized fork
\[
\boxed{
\|\lambda_1v_kv_{C\setminus\{k\}}\|_2
\ge1/2-{1\over2}|\lambda_2|
}
\tag{6.3}
\]
or
\[
\boxed{
\|\lambda_1v_kv_{C^c}\|_2
\ge1/2-{1\over2}|\lambda_2|.
}
\tag{6.4}
\]
This is the requested equation-level use of the designated partner result.

## 7. Sharpened high-density normal form

Combine (1.4), (5.3), and the latent spectral decomposition. Every sufficiently high-ratio survivor in the diffuse exact-rank-two chamber has
\[
\boxed{
A=D_C+\lambda_1vv^T+E_{\rm sep}+E_{\rm ent},
\qquad |C|\le4,
}
\tag{7.1}
\]
where
\[
E_{\rm sep}=D_{C^c},\qquad
\|E_{\rm sep}\|_{op}\le C_5\rho^{-1},
\tag{7.2}
\]
and
\[
E_{\rm ent}=\lambda_2ww^T,
\qquad
\boxed{\|E_{\rm ent}\|_{op}=O(\rho^{-7/6})=o(\rho^{-1}).}
\tag{7.3}
\]
Moreover either the stronger ultra-collapse (6.1) holds, or the dominant rank-one mode carries the fixed physical star (6.2), with the finite-core/outside-bank split (6.3)--(6.4).

This separates the remaining error by provenance: the only `O(rho^{-1})` tail is **coordinate-separable diagonal curvature**, while the genuinely entangled residual is now `o(rho^{-1})`. The distinction matters because separable phases can be retained harmlessly in several completed Fourier receivers, whereas a general nonseparable small quadratic tail cannot simply be discarded.

## 8. Extremal-product transfer

The designated account04/B13 optimizer-free theorem applies coordinate by coordinate: for every bounded nonnegative slab kernel, each cap-one mass-one marginal can be replaced by a unit-measure indicator up to arbitrarily small loss, and the product replacement is iterated over the original coordinates. Equivalently, the earlier exact barycentric formulation represents every cap-one marginal as a mixture of arbitrary unit-measure indicators.

Therefore all slab-ratio consequences above transfer to arbitrary admissible product densities with no interval, centered-uniform, bounded-diameter, or fixed-fragment hypothesis. The two-square analytic theorem itself is already proved directly for arbitrary cap-one product densities, so no extremizer attainment is required.

## 9. What remains

**Full QFORM remains OPEN / not proved / not disproved. Full-target continuity remains OPEN.** Theorem 2.1 proves continuity only in its exact diagonal-plus-diffuse-rank-two scope; in particular the high-density diffuse rank-two survivor has a continuous density.

The remaining structural endpoint is much narrower:

`QFORM-RANK1-4DIAG-SEPARABLE1OVERrho-ENTANGLED7OVER6-RECEIVER-v1`:

> retain the four-coordinate diagonal core and the `O(rho^-1)` separable diagonal tail exactly, while consuming either the dominant physical star or the ultra-near-rank-one packet; the second nonseparable mode is now `O(rho^-7/6)` and must still be retained rather than deleted.

A promising next mechanism is to group the dominant rank-one outside bank as an original-coordinate product projection while carrying the entire diagonal tail as complex separable phases, then pay the `rho^-7/6` second mode inside the same Fresnel integral rather than by random-variable perturbation.

No full-solution claim is made and no independent end-to-end review is claimed for this run.
