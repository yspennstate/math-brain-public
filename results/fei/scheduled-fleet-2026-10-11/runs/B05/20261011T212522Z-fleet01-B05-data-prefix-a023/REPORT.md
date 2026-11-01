# B05 / A023: a one-coordinate-per-pair prefix telescopes the rare logarithm

Run ID: `20261011T212522Z-fleet01-B05-data-prefix-a023`  
Primary packet: `A023` (Amortized rarity budget)  
Stable gap / obstruction: `B05_RARE_REFUNDS` / `O-B05`  
Attempt: `A023-DATA-PREFIX-2`  
Full FEI status: **OPEN**

## 1. Exact objective and prior status

The accepted B05 obstruction proves that no fixed local expression

\[
L\le Kd+A V+B M
\]

pays the selector packet of the sparse activated bent one-point-defect family. The immediately preceding A023 run then proved that revealing all activation controls before the selector merely transports the same debt:

\[
L/d=k+\log_2e+o(1).
\]

Its concrete next action was to query data before the selector on the surviving activation branch and determine whether a nonlocal credit pays the logarithm or merely moves it again.

This run proves a positive, family-level answer. Query one coordinate from each quadratic bent pair, stopping the selector analysis as soon as one queried coordinate equals one. The exact expected selector packet decomposes into nonnegative, single-use order-swap credits plus an (O(d)) terminal packet. The (dk) logarithm is telescoped, not charged to a pointwise (O(d)) local refund.

This is a complete rarity-payment theorem for the declared stopping rule and family. It is not a universal amortization theorem and does not prove FEI.

## 2. Genuine Boolean family

Let (k=2h\ge4),

\[
\delta=2^{-k},\qquad \rho=2^{-h}=\sqrt\delta,
\qquad p=\delta^2,\qquad d=p\delta.
\]

Write the data variables as (h) pairs ((u_j,v_j)), and define the genuine Boolean bent sign

\[
b(u,v)=(-1)^{\sum_{j=1}^h u_jv_j}.
\]

Let (b') be obtained by flipping only the all-zero input. With a fresh physical selector (y), put

\[
s(y,u,v)=\frac{b+b'}2+y\frac{b-b'}2.
\]

With (2k) fresh controls (z) and (A(z)=1_{\{z=0\}}), activate by

\[
F=1+A(z)(s-1).
\]

As in the previous run, the controls are queried first. The nonconstant branch has probability (p), so every core ledger below is multiplied by (p).

## 3. Data-prefix stopping rule

On the branch (z=0):

1. Query (u_1,u_2,\ldots,u_h) in order.
2. If some (u_j=1), then the origin is excluded, so (b=b') on that restriction and the selector is irrelevant. Its remaining packet is zero.
3. If (u_1=\cdots=u_h=0), query (y).

This rule is physical, adaptive and finite. Each (u_j) is queried at most once, and the activation event is owned only at the control prefix.

## 4. Exact spectrum after (m) surviving data queries

Suppose (u_1=\cdots=u_m=0), where (0\le m\le h). Let (b_m,b'_m) be the restricted selector children and let (L_m) be their selector conditional-entropy packet.

Set

\[
c_m=2^m\rho,\qquad e_m=2^m\delta=c_m\rho.
\]

The Fourier transform of (b_m) has support size (c_m^{-2}), coefficient magnitudes (c_m), and is zero off that support. The positive and negative support counts are

\[
N_+(m)=\frac{c_m^{-2}+c_m^{-1}}2,
\qquad
N_-(m)=\frac{c_m^{-2}-c_m^{-1}}2.
\]

The one-point flip shifts every remaining Fourier coefficient by (-2e_m). Thus the selector midpoint/half-difference at a support frequency are

\[
a=e_m\left(\frac{\pm1}{\rho}-1\right)=c_m(\pm1-\rho),
\qquad v=e_m=c_m\rho,
\]

while off the support (a=-e_m,v=e_m).

Define

\[
P_\pm(\rho)=\bigl((\pm1-\rho)^2+\rho^2\bigr)
h_2\!\left(\frac{\rho^2}{(\pm1-\rho)^2+\rho^2}\right),
\]

and

\[
A_L=\frac{P_++P_-}{2},\qquad B_L=\frac{P_+-P_-}{2}.
\]

Summing the support and off-support packets gives the exact affine formula

\[
\boxed{
L_m=A_L-2\delta+c_m(B_L+2\rho).
}\tag{1}
\]

No asymptotic approximation is used in (1).

## 5. PROVED: constant raw credit and geometric expected payment

If (u_{m+1}) is queried, its (1)-child has zero selector packet and its (0)-child has packet (L_{m+1}). Hence the raw order-swap credit at the surviving node is

\[
\Gamma_m=L_m-\frac12L_{m+1}.
\]

Since (c_{m+1}=2c_m), equation (1) yields

\[
\boxed{
\Gamma_m=\Gamma:=\frac{A_L-2\delta}{2},
\qquad 0\le m<h.
}\tag{2}
\]

The credit is nonnegative. Indeed, for (ho\le1/2), both support parameters (	heta_\pm) lie in ([0,1/2]), and concavity of binary entropy gives (h_2(t)\ge2t) there. Consequently (P_\pm\ge2\rho^2=2\delta), so (A_L\ge2\delta).

The probability of reaching node (m) is (2^{-m}). Therefore the credits are spent exactly once with the exact telescope

\[
\boxed{
L_0=\sum_{m=0}^{h-1}2^{-m}\Gamma+2^{-h}L_h.
}\tag{3}
\]

After restoring activation, the global credit at level (m) is (p2^{-m}\Gamma). There is no descendant reuse.

As (delta\downarrow0),

\[
\Gamma=\frac\delta2\left(k+\log_2e-2+O(\rho k)\right),
\]

and hence

\[
p\sum_{m=0}^{h-1}2^{-m}\Gamma
=d\left(k+\log_2e-2+o(1)\right).
\]

This is the previously unpaid logarithm, now represented by a nonlocal sequence of explicit single-use credits rather than a bounded local refund.

## 6. Terminal selector packet is (O(d))

At (m=h), the background (b_h) is constant one on the remaining (v)-variables and (b'_h) flips only their origin. Thus

\[
L_h=Psi(1-\rho,\rho^2)+(\rho^{-1}-1)2\rho^2,
\]

where

\[
\Psi(a,e)=(a^2+e)h_2\!\left(\frac e{a^2+e}\right).
\]

Using (Psi(a,e)\le e\log_2(e_{\rm Euler}(a^2+e)/e)) and
((1-\rho)^2+\rho^2\le1),

\[
\boxed{
2^{-h}L_h=\rho L_h
\le2\delta+\delta\rho(k+\log_2e).
}\tag{4}
\]

Therefore the actual activated terminal selector packet obeys

\[
\boxed{
p2^{-h}L_h\le d\,[2+\rho(k+\log_2e)]=O(d).
}\tag{5}
\]

The phase/JS packet contains no unpaid logarithm. The source split inequality gives

\[
Q_h\le\frac2{\ln2}I_y(s_h)=\frac{2\rho}{\ln2},
\]

so

\[
\boxed{
p2^{-h}Q_h\le\frac{2d}{\ln2}.
}\tag{6}
\]

Equations (3), (5), and (6) retain both the rare logarithm and the phase term. The full selector entropy decrement at the eventual selector is bounded by

\[
d\left(2+\frac2{\ln2}+\rho(k+\log_2e)\right).
\]

## 7. Interpretation: what moved and what did not

The previous control-first rule left (dk) below the activation prefix. The present data prefix does not produce a hidden scalar KL cancellation. Instead:

* the logarithmic conditional-entropy packet (L_0) is split exactly into the nonnegative credits (2^{-m}\Gamma) and the terminal packet;
* the credits are the selector/data order-swap terms and are absorbed at distinct physical data-query nodes;
* the remaining selector (L) and phase/JS (Q) are both (O(\delta)) at core scale, hence (O(d)) after activation;
* the full entropy telescope is preserved: moving the selector below a data query transfers the corresponding interaction term into that data split. Nothing is deleted or spent twice.

Thus the answer to the declared test is: a carefully chosen data-interleaving does pay the logarithm on this family. Querying the paired mate variables would not have this property; the useful prefix takes exactly one coordinate from each bent pair.

## 8. Mandatory falsifiers and scope

* **Sparse one-point defect / rare restriction:** the theorem is proved on the exact activated origin-flip family, with (p=\delta^2).
* **Near tensor:** (b) is a tensor of two-bit quadratic prime gates, while the origin flip destroys exact tensorization. Formula (1) retains both support and off-support mass.
* **Actual prime Boolean gates:** every queried (u_j), selector (y), and quadratic pair is a physical Boolean coordinate/gate.
* **Shared-variable interference:** both selector children share all remaining data and controls; the spectrum is computed after the physical restrictions.
* **Parity-zero erasure:** no erasure-entropy lower bound is used. The proof uses the complete midpoint/half-difference packets.
* **Addressing/multiplexers:** the affine formula (1) relies on the bent pair support counts and is not asserted for addressing. Whole-set addressing remains a separate mandatory control on any universal extension.
* **Biased prime gates:** no product-biased scalar tax is used; the terminal phase term is retained through the uniform-cube JS bound.

This is a specified-family amortization, not a universal estimate. It neither proves existential good-coordinate selection nor bounds arbitrary restriction trees.

## 9. Deterministic verification

`data_prefix_checker.py` independently constructs the genuine restricted Boolean truth tables and normalized Walsh transforms for (k=2,4,6,8,10,12). It verifies (1), the constant-credit identity (2), telescope (3), terminal bound (4), and the terminal phase bound. Aggregated closed forms are additionally checked at (k=16,20,24,32,40,60).

Command:

```text
python3 data_prefix_checker.py
```

Observed runtime: 1.2 seconds. The script reports at least 210 deterministic assertions and zero failures. It uses IEEE-754 binary64 only as corroboration; the all-(k) result is the analytic proof above. There is no random seed and no search.

At (k=40),

\[
L_0/\delta\approx41.442695,
\quad
\text{credit sum}/\delta\approx39.442657,
\quad
2^{-h}L_h/\delta\approx2.000038.
\]

## 10. Status and handoff

Claim `B05-A023-BENT-DATA-PREFIX-TELESCOPE-v1` is **ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW**.

This supplies A023's requested positive nonlocal rarity payment on one declared unbounded family and stopping rule. Packet A023 remains **OPEN / PARTIAL_PROGRESS** because the result is not universal and does not yet cover addressing or arbitrary Boolean cores.

Independent review requested from A087 or A094. The reviewer should reconstruct the support/sign counts, affine formula (1), and nonnegativity of (2), then verify that the activation factor (p) is applied only after the core telescope.

Next action: test whether the same one-coordinate-per-component telescope survives a near-bent tensor whose factors are unequal prime gates. The exact question is whether the raw credits remain nonnegative when the common ratio (e_m/c_m=\rho) is replaced by factor-dependent ratios; a failure would precisely delimit this positive mechanism.

## 11. Source pins

* Accepted local no-go: open-problems commit `80cc2e5027efa56d79c4ecdf7d4949759ef2068b`, B05 run `20261011T193057Z-fleet01-B05-rare-restrictions`.
* Independent review: open-problems commit `7955d427222392911dc6af2e4ee3aa8aab67ac8c`, B19 run `20261011T195038Z-fleet01-B19-independent-review`.
* Prior A023 order-transport report: open-problems commit `440ecfff652a0b02f072c98bc4524d59a2a8bf2a`, report blob `4b02b427aaf3f2d683a4ec195c9b747976035272`.
* Current B05 contract blob: `05447e6d999437bb82a266b427bd76a4b37266b6`.
* Current campaign status blob: `8c9c63579ecdd4afa385bb94caf79ee6296addcf`.

No literature novelty is claimed. No protected evaluation material, held request, scheduler state, email, public release, merge, or live-store mutation was accessed.

## 12. Execution metadata

The runtime exposed Codex based on GPT-5. No model selector, reasoning-effort selector, continuous-hour guarantee, billing identity, or remaining allowance meter was exposed. Natural derivation, computation, persistence, review, and ingestion are recorded separately.
