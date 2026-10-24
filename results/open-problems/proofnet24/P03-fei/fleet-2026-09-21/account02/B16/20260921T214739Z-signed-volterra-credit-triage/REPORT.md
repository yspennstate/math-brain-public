# B16 FEI signed transport — finite-window signed Volterra flag map and compensation triage

**Date:** 21 September 2026  
**Scope:** `account02 / B16`, joint FEI interface C  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Full unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact finite-window signed representation, an explicit authentic-parent-to-physical-flag pushforward on the noncharacter parent sector, and a source-exact obstruction showing that two previously plausible refund banks cannot supply the compensation required by the genuine half-band counterfamily. No novelty or publication-priority claim.

## 0. Why this run changes mechanism

The last three completed substantive B16 reports were:

1. `20260921T173238Z-qflip-frame-coordinate-incidence`: a fixed nonnegative q-flip frame is paid if and essentially only if its original-coordinate incidence is bounded;
2. `20260921T184541Z-actual-current-parent-mask-incidence`: the genuine same-syndrome current was compressed to the authentic nonnegative parent masses `mu_j`;
3. `20260921T193735Z-codimension-normalization-parent-bridge`: independent inversion of each scalar parent charge through the parent plaquette kernel incurs a linear codimension loss, so the source must stay signed before that compression.

All three left the same universal interface unpaid: the **finite live Borel-window signed source -> original-coordinate physical flag** map with every refund used at most once. The joint order therefore requires a materially different representation now.

This run does that. It does **not** seek another positive parent-pair measure. It keeps the authentic signed same-syndrome coefficient field through a finite-window Volterra integration by parts, then pushes the resulting **signed boundary/bulk charges** to deterministic physical flags. The total-variation estimate of this map is explicitly forbidden by the earlier codimension obstruction; cancellation must be retained after pushforward.

Two new peer results are used substantively:

* account03/B16 `20260921T211732Z-signed-square-root-resolvent/REPORT.md`, blob `be465709537514dc3d483fa61532630ac78dce66`: the terminal projector and same-syndrome signs can be retained inside a local `L^{-1/2}` q-flip field, and any necessary refund must be inserted **before** the final positive local square;
* account03/B18 `20260921T212630Z-positive-contraction-no-go/REPORT.md`, blob `2025b99b0086b01b6a9833d0ddc02fb4aae4b161`: on a genuine sparse Boolean family the exact central half-band positive current is `Theta(n^-3)` while every `J`-paid positive physical sink is exponentially smaller, so the formerly requested all-Boolean positive/PSD contraction is impossible. It also proves that any valid signed replacement needs compensation of asymptotic size at least `11/(864 n^3)` before outer averaging.

The exact R16 response formula used below is from account01/B16 `20260921T143714Z-high-resolvent-compression/REPORT.md`, blob `5318c4d60d7c53731686b08f02706e6b232245c2`.

## 1. Authentic central parent field before positivity

Fix one genuine ordered q-flip system and a live Borel scale `s`. After retaining the terminal-code subtraction and aggregating every dual-code contribution with the **same** active syndrome before any square, write the signed odd coefficient field

\[
b(s)=(b_R(s))_{R\ {m odd}}.
\]

For a syndrome `R`, write

\[
q_R=|R|,\qquad k_R=\#\{\text{clone pairs hit oddly}\},\qquad
r_R=(q_R-k_R)/2.
\]

The genuine central double-resolvent multiplier is

\[
\varepsilon_R
=2\frac{2^{-q_R}}{q_R}
\left(\frac{2^{-k_R}}{k_R}-\frac{2^{-q_R}}{q_R}\right)\ge0.
\]

For every coarse parent `j` define the diagonal operator

\[
(M_jb)_R=
1_{\{j\ {m doubled\ in}\ R\}}
\frac{\varepsilon_R}{r_R}b_R,
\]

with the `r_R=0` sector interpreted as zero, and put

\[
u_j(s)=M_j^{1/2}b(s).
\tag{1.1}
\]

Because each charged mode has exactly `r_R` doubled parents,

\[
\boxed{
\sum_j\|u_j(s)\|_2^2
=\sum_R\varepsilon_R b_R(s)^2
=\mathcal E_{\rm cen}(s).
}
\tag{1.2}
\]

This is the authentic parent split, but unlike scalar `mu_j` compression the sign of every `b_R(s)` is still present in the field `u_j(s)`. Dual-code multiplicity, the retained terminal subtraction, and `0 mod 4 / 2 mod 4` cancellation have already happened inside `b_R`.

## 2. `P03-B16-LIVE-VOLTERRA-PARENT` — PROVED

Let the exact live Borel interval be

\[
W=[a,b]
\]

(for the half-band stress test one may take the actual retained corridor inside `[40,S_f]`). Define the parentwise signed Volterra primitives

\[
v_j(s)=\int_a^s u_j(t)\frac{dt}{t^3},
\qquad
w_j(s)=\int_s^b u_j(t)\frac{dt}{t^3}.
\tag{2.1}
\]

The Borel coefficient functions are analytic, so ordinary integration by parts applies componentwise. From `v_j'=u_j/s^3` and `w_j'=-u_j/s^3`,

\[
\boxed{
\mathcal P_W^{\rm cen}:=
\int_a^b\mathcal E_{\rm cen}(s)\frac{ds}{s^3}
=
\sum_j\langle u_j(b),v_j(b)\rangle
-
\sum_j\int_a^b\langle u_j'(s),v_j(s)\rangle ds.
}
\tag{2.2}
\]

Equivalently,

\[
\boxed{
\mathcal P_W^{\rm cen}
=
\sum_j\langle u_j(a),w_j(a)\rangle
+
\sum_j\int_a^b\langle u_j'(s),w_j(s)\rangle ds.
}
\tag{2.3}
\]

These are **finite-window identities**, not a full-line majorization. No `W^c` tail is discarded, no coefficient is replaced by its absolute value, and no terminal endpoint is spent. They turn the positive current into an exactly equal **signed boundary plus signed bulk** representation while parent and syndrome identities remain visible.

The point is not that (2.2) is smaller than the positive current—it is equal to it. The point is that account03's new square-root-resolvent theorem says the missing source credit has to enter before final positivity. Equations (2.2)-(2.3) expose the precise finite-window location where such a signed companion can be paired without first collapsing to total variation.

## 3. `P03-B16-SIGNED-PARENT-FLAG-PUSHFORWARD` — PROVED AS AN IDENTITY, NOT A PAYMENT

Take one authentic ordered parent mask

\[
g_j=1-2\,1_{Q_j},\qquad
Q_j=\{x:x_{F_j}=a_j\},\qquad c_j=|F_j|.
\]

For `c_j>=2`, choose deterministically two distinct defining coordinates `i_j,l_j in F_j` and put `w_j^*=e_{l_j}`. The account03/B18 parent-pivot theorem gives the exact physical signed curvature

\[
\kappa^{g_j}_{i_j}(w_j^*)=2^{2-c_j}=:\kappa_j>0.
\tag{3.1}
\]

For any real scalar charge `h`, define the signed physical-flag atom

\[
T_j(h)=\frac{h}{\kappa_j}\,\delta_{(i_j,w_j^*)}.
\tag{3.2}
\]

Then exactly

\[
\boxed{\int\kappa^{g_j}_i(w)\,dT_j(h)(i,w)=h.}
\tag{3.3}
\]

Apply (3.2) **componentwise in the genuine syndrome index** to (2.2):

\[
\Lambda^{\rm bdry}_{j,R}
=T_j\!\left(u_{j,R}(b)v_{j,R}(b)\right),
\]

\[
d\Lambda^{\rm bulk}_{j,R}(s)
=T_j\!\left(-u'_{j,R}(s)v_{j,R}(s)\right)ds.
\tag{3.4}
\]

Thus, on the `c_j>=2` parent sector,

\[
\boxed{
\mathcal P_{W,\,c\ge2}^{\rm cen}
=
\sum_{j,R:c_j\ge2}
\int\kappa^{g_j}_i(w)\,
 d\bigl(\Lambda^{\rm bdry}_{j,R}+\Lambda^{\rm bulk}_{j,R}\bigr)(i,w).
}
\tag{3.5}
\]

The `c_j=1` character-parent sector is retained as an explicit source remainder

\[
\mathfrak R_{c=1}(W)
=\int_a^b\sum_{j:c_j=1}\|u_j(s)\|_2^2\frac{ds}{s^3},
\tag{3.6}
\]

because the one-subcube parent plaquette curvature is identically zero there. No false flag is manufactured for that sector.

Equation (3.5) is the requested **explicit authentic-parent -> physical-flag map including the live window**. It is deliberately a **signed measure identity**. Taking its total variation would reproduce the already-proved codimension loss because `1/kappa_j=2^{c_j-2}`. Therefore (3.5) is not yet the universal FEI payment. The remaining task is a cancellation/nonreuse inequality for the pushed-forward signed boundary and bulk fields, plus the character-parent remainder, after a genuine source credit is inserted.

## 4. The genuine half-band obstruction rules out the R16 bank as that missing compensation

Now apply the account03/B18 half-band compensation floor to its genuine Boolean source family. After the mandatory dummy split the fine cube has dimension `D`, `N=2^D`, `n=D-1`, and the negative set is an affine two-plane

\[
Q=a+V,\qquad \dim V=2,
\]

so

\[
f=1-2\,1_Q,
\qquad
J(f)=\frac{8n}{N}.
\tag{4.1}
\]

The Fourier spectrum is elementary and exact. For a character `xi`,

\[
\widehat f(\xi)
=1_{\{\xi=0\}}
-\frac2N\sum_{x\in a+V}(-1)^{\xi\cdot x}.
\]

Hence

\[
\widehat f(0)=1-\frac8N,
\]

and for every nonzero `xi in V^perp`,

\[
|\widehat f(\xi)|=\frac8N,
\]

while all other coefficients vanish. Thus the squared Fourier law is

\[
p_0=\left(1-\frac8N\right)^2,
\qquad
p=\frac{64}{N^2}
\quad\text{with multiplicity}\quad
M=\frac N4-1.
\tag{4.2}
\]

In particular `p_0+Mp=1`, and

\[
H_{\rm nat}(f)
=-p_0\log p_0-Mp\log p,
\qquad
\frac{H_{\rm nat}(f)}{J(f)}\longrightarrow4\log2.
\tag{4.3}
\]

So this is a low-ratio FEI family, not an FEI counterexample; it is only a stress test for interface C.

Account01's exact full R16 high-resolvent response is

\[
\Delta_{\infty,>2}
=\sum_Sp_S\log\frac3{2+p_S}.
\tag{4.4}
\]

Put `delta=1-p_0=16/N-64/N^2<=16/N`. Then

\[
p_0\log\frac3{2+p_0}
=p_0\left[-\log(1-\delta/3)\right]
\le\frac{\delta}{3-\delta}
\le\frac8N,
\]

and

\[
Mp\log\frac3{2+p}
\le\frac{16}{N}\log\frac32.
\]

Therefore

\[
\boxed{
0\le\Delta_{\infty,>2}
\le\frac{8+16\log(3/2)}{N},
\qquad
\frac{\Delta_{\infty,>2}}{J(f)}
\le\frac{1+2\log(3/2)}{n}.
}
\tag{4.5}
\]

At `d=ceil(D/2)`, the inherited R16 saturation estimate gives

\[
|\Delta_{d,>2}-\Delta_{\infty,>2}|
\le\epsilon_dJ,
\qquad \epsilon_d=2^{3-2^d},
\]

and the booked R16 bank is

\[
B_d=\kappa_2J-\Delta_{d,>2}.
\]

Consequently

\[
\boxed{0\le B_d\le(\kappa_2+\epsilon_d)J=O(n2^{-D}).}
\tag{4.6}
\]

But account03/B18 proves that any signed replacement of the impossible positive contraction needs compensation

\[
\liminf_{D\to\infty} n^3\mathcal C_D\ge\frac{11}{864}
\tag{4.7}
\]

on this same unaveraged source channel. Since `n^3 B_d=O(n^4 2^{-D})->0`, the **entire booked R16 high-resolvent bank alone is exponentially too small to supply the required interface-C compensation on this family**.

This does not spend or bound the distinct negative R32 entropy credits, the separate terminal endpoint, or any other still-reserved signed term.

## 5. The central/Ward gap also vanishes exactly on the obstruction

Every charged active syndrome in the same source family has

\[
(q,k)=(3,1).
\]

For this mode,

\[
W_{3}=1-1/3=2/3,
\qquad
\varepsilon_{3,1}=11/288,
\]

and therefore

\[
\boxed{
\rho_{3,1}:=\frac{11}{192}W_3-\varepsilon_{3,1}=0.
}
\tag{5.1}
\]

Hence account04's nonnegative Ward **gap** refund

\[
\mathcal R_{\rm Ward}=\sum_R\rho_Rb_R^2
\]

contributes exactly zero on every charged mode of the genuine obstruction. The full Ward comparison quantity is not thereby promoted to a booked refund; the peer handoff explicitly warns that this would require a separate no-reuse ledger identity.

Combined with account03/B18's theorem that the terminal-code subtraction already inside `b_R` is exponentially small relative to the surviving polynomial current, the current obstruction now eliminates three tempting repairs:

1. bounded positive/PSD contraction of the whole current — **REFUTED by account03/B18**;
2. the booked R16 high-resolvent bank alone — **too small by (4.6)-(4.7)**;
3. the nonnegative central/Ward gap — **identically zero by (5.1)**.

The separate terminal endpoint and the genuinely signed negative-R32/small-resolvent credits remain reserved and are **not** ruled out here.

## 6. Exact self-check

`check_signed_volterra_credit_triage.py` was executed natively. It checks:

* 37 exact Fourier-mass identities for `D=4,...,40`;
* the explicit R16 upper bound in (4.5) on all those cases;
* the exact rational equality `rho_(3,1)=0`;
* three exact rational polynomial instances of the finite-window Volterra identity (2.2).

Output status is `PASS`; the maximum observed `Delta_infty/J` on `D=4,...,40` is `0.25259466524513263`, and at `D=40` it is `0.037886838726735532`, consistent with the proved `O(1/n)` decay. The finite computations are self-check evidence only; the all-dimensional statements above are symbolic.

## 7. Full-problem and mechanism status

**FULL-PROBLEM CHANGE: NONE.** Full uniform-cube FEI remains **OPEN / NOT PROVED**. No dimension-independent FEI constant is claimed here.

**MECHANISM CHANGE: YES.** Before this run, interface C still sought a positive or scalar-parent contraction after current formation. The genuine half-band source now rules that out, and this run executes the required replacement: a **finite-window signed Volterra parent field** followed by an explicit signed physical-flag pushforward, with no total-variation step.

**Exact remaining universal gap.** Identify a source-exact, nonreused signed companion `C_W` at the same `(parent, syndrome, time)` level—coming from still-reserved negative-R32/small-resolvent and/or terminal terms, or derive a justified high-ratio critical-core reduction—such that the **compensated** signed boundary/bulk measure from (3.4) plus the `c=1` remainder admits an original-coordinate payment `O(J(f))`. The companion must meet the `Theta(n^-3)` floor on the sparse half-band family; the R16 bank and Ward gap cannot do so there. Any proof that takes total variation before this cancellation revives the killed codimension obstruction.

**Next recipient:** account03/B16 for the live logarithmic/polarization side and account04/B16 for source-side phase-switch cancellation; account02/B15 is the natural arithmetic-credit partner for testing whether an unspent signed credit has the required half-band scale.
