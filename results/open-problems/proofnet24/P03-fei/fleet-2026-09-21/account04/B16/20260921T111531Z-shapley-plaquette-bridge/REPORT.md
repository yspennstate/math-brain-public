# P03 FEI — Shapley/plaquette bridge for signed q-flip transport

Date: 21 September 2026  
Fleet scope: `account04/B16`  
Live role: **FEI signed transport proof**  
Execution label: **WITHOUT_VERIFIED_BRAIN**  
Status of unrestricted FEI: **OPEN / NOT PROVED**

## 0. What moved

This run combines three fresh compatible signed routes without taking absolute values:

1. account04/B16's exact Fourier plaquette curvature and quotient no-reentry identity;
2. account02/B16's weight-four relation-code basis and Aumann--Shapley signed R32 disintegration;
3. account01/B16's physical cut-indicator Fourier field, which is the source side of its signed noise-square payment.

The new result is an exact **Shapley--plaquette bridge**: every one-q-flip R32 charge is the entropy of the dual quotient generator minus an explicitly weighted signed sum of account04 plaquette curvatures minus the matching Shapley share of the terminal response. Thus the large positive generator entropy is not a debit to be paid separately; it is paired exactly with signed plaquette/frustration credits and the retained terminal band.

A second exact identity shows that q-flip frustration is literally a Radon transform of the Fourier energy of the original-coordinate disagreement indicator. This gives a direct algebraic interface to the account01 signed `L2` bank.

The three deliberate FLEET_RULES moves were **#5 add a parameter and differentiate** (the Shapley/Aumann--Shapley path), **#18 say it in another language** (relation syndromes versus phase-quotient generators), and **#25 count the same thing twice** (the same R32 charge as a syndrome derivative and as a plaquette telescope).

No terminal endpoint is converted into cumulative variation. No `2 mod 4` relation is positive-parted. No minimum-T-join length bound is assumed. No killed absolute-reflection or absolute-correlation shortcut is revived.

## 1. Entering exact state

Write `V=F_2^n`, `N=2^n`. The retained R32 identity is

\[
F_d(f):=H_{\rm nat}(f)-R_d(f)
=\frac8N\sum_{\substack{A\in C_0\setminus D_d\\ f_A=-1}}c_A,
\qquad
c_A=(-1)^{|A|/2}I_{|A|,N}.
\tag{1.1}
\]

Here `C_0=RM(1,n)^perp`. The signs in `c_A`, the exclusion `D_d`, dual-code multiplicities, the R16 moment refunds/high-resolvent bank and the already proved terminal-band payment are inherited unchanged.

Account02 fixes, for an anchor `a` and each `v` of Hamming weight at least two, a pivot `i(v) in supp(v)` and the weight-four relation

\[
B_v(a)=\{a,a+e_{i(v)},a+v,a+v+e_{i(v)}\}.
\tag{1.2}
\]

These form a basis of `C_0`. If

\[
z_v(f)=f_{B_v(a)}\in\{\pm1\},
\qquad M(f)=\{v:z_v(f)=-1\},
\tag{1.3}
\]

then every relation has a unique coordinate vector `a_v(A)`, and account02's exact signed load is

\[
L_v(f)
=1_{\{v\in M\}}
\sum_{\substack{A\in C_0\setminus D_d\\ f_A=-1\\a_v(A)=1}}
\frac{c_A}{q_A},
\quad
q_A=|\{v\in M:a_v(A)=1\}|.
\tag{1.4}
\]

It satisfies

\[
F_d(f)=\frac8N\sum_{v\in M}L_v(f).
\tag{1.5}
\]

Every active q-flip contains exactly one genuine physical disagreement edge, so the loads can be regrouped on the original cube without changing signs.

## 2. The dual phase basis, explicitly

Translate the anchor to `0`; translation only relabels truth-table coordinates. Let `Q` be the Boolean phase group modulo affine characters. The pairing with `C_0` is perfect, so the relation basis `{B_v}` has a dual phase basis `{g_v}` in `Q` characterized by

\[
(g_u)_{B_v}=(-1)^{1_{\{u=v\}}}.
\tag{2.1}
\]

Then the syndrome of `f` gives the exact quotient expansion

\[
[f]=\prod_{v\in M(f)}[g_v].
\tag{2.2}
\]

This is already enough for the Shapley bridge below. For the useful ordered-pivot family it is also completely explicit.

### Theorem 2.1 — ordered-min q-flip duals are subcube defects

Fix a total order on the physical coordinates and take `i(v)` to be the first coordinate of `supp(v)` in that order. Put

\[
p(v)=v+e_{i(v)}.
\]

Choose the affine gauge for a phase exponent `q:V->F_2` with `q(0)=q(e_i)=0`. Its q-flip syndrome exponent is

\[
b_v=q(v)+q(p(v)).
\tag{2.3}
\]

Hence

\[
q(v)=b_v+q(p(v)).
\tag{2.4}
\]

For the dual generator `g_u`, `b_v=1_{u=v}`. Therefore `g_u(x)=-1` exactly when the repeated parent-deletion chain from `x` passes through `u`.

If the pivot coordinate of `u` has rank `r` in the order and

\[
c=n-r+1,
\]

then the descendant set is an affine subcube of codimension `c`. Thus `g_u` is a one-subcube defect: it is `-1` on a fraction `q=2^{-c}` of the cube and `+1` elsewhere.

#### Proof

Equation (2.3) is just the parity of `q` on `{0,e_i,v,v+e_i}` after the affine gauge kills the first two terms. Since `p(v)` has weight one less, recursion gives (2.4). For `b=delta_u`, the recursion is one precisely on the descendants of `u`. Under an ordered-min parent rule, the only free coordinates of a descendant are those preceding the pivot of `u`; all coordinates from the pivot onward are fixed. There are `r-1` free coordinates and hence codimension `c=n-r+1`. `square`

The squared spectrum of this dual generator has

\[
p_0=(1-2^{1-c})^2,
\qquad
p_1=2^{2-2c}
\tag{2.5}
\]

with `p_1` repeated `2^c-1` times. In bits,

\[
H_c^{(2)}=-p_0\log_2p_0-(2^c-1)p_1\log_2p_1.
\tag{2.6}
\]

The values begin

\[
H_2^{(2)}=2,
\quad H_3^{(2)}=2.216917186688699\ldots,
\quad H_4^{(2)}=1.701237775599294\ldots,
\tag{2.7}
\]

and `H_c^{(2)}=8c2^{-c}+O(2^{-c})`. In natural entropy units multiply by `ln 2`.

So a random-coordinate-order q-flip basis has dual generators with a very rigid physical meaning; this is not an abstract existence basis.

## 3. Exact Shapley--plaquette bridge

Let `E` denote spectral entropy in the same normalization used in (1.1). For commuting Boolean phases define account04's plaquette curvature

\[
\kappa_\sigma(g,h)
=E(g\sigma)+E(h\sigma)-E(\sigma)-E(gh\sigma).
\tag{3.1}
\]

For a set function `G` on the active generator set `M`, define the Shapley marginal of `v in M` by a uniform random permutation `pi` of `M`:

\[
\phi_v(G)
=\mathbb E_\pi\bigl[G(S_{\pi,v}\cup\{v\})-G(S_{\pi,v})\bigr],
\tag{3.2}
\]

where `S_{pi,v}` is the set preceding `v`.

Account02's Aumann--Shapley identity is equivalently

\[
\phi_v(P_c)=L_v,
\tag{3.3}
\]

where `P_c` is the signed relation polynomial with `F_d=(8/N)P_c`.

Define the signed curvature bank

\[
\mathcal C_v^M
:=\mathbb E_\pi
\sum_{h\prec_\pi v}
\kappa_{g_{S_{\pi,h}}}(g_v,g_h),
\tag{3.4}
\]

and the terminal Shapley share

\[
\Theta_v^M:=\phi_v(R_d).
\tag{3.5}
\]

### Theorem 3.1 — `B16-SHAPLEY-PLAQUETTE-BRIDGE`

For every active q-flip coordinate,

\[
\boxed{
\frac8N L_v
=E(g_v)-\mathcal C_v^M-\Theta_v^M.
}
\tag{3.6}
\]

No sign has been discarded. Negative plaquette curvature and negative terminal Shapley shares remain literal credits.

#### Proof

Write

\[
\Delta_vE(\sigma)=E(g_v\sigma)-E(\sigma).
\]

From (3.1),

\[
\Delta_vE(g_h\sigma)=\Delta_vE(\sigma)-\kappa_\sigma(g_v,g_h).
\tag{3.7}
\]

Iterating (3.7) along the prefix before `v` in a permutation gives

\[
\Delta_vE(g_{S_{\pi,v}})
=E(g_v)-E(1)-
\sum_{h\prec_\pi v}\kappa_{g_{S_{\pi,h}}}(g_v,g_h).
\]

Since `E(1)=0`, averaging gives

\[
\phi_v(E)=E(g_v)-\mathcal C_v^M.
\tag{3.8}
\]

But `F_d=E-R_d=(8/N)P_c`, so by linearity of Shapley values and (3.3),

\[
\frac8N L_v=\phi_v(E)-\phi_v(R_d),
\]

which is (3.6). `square`

There is an explicit subset formula with no random object left. If `m=|M|`,

\[
\boxed{
\mathcal C_v^M
=\sum_{h\in M\setminus\{v\}}
\sum_{S\subseteq M\setminus\{v,h\}}
\frac{|S|!(m-|S|-1)!}{m!}
\kappa_{g_S}(g_v,g_h),
}
\tag{3.9}
\]

because the coefficient is exactly the probability that the set before `h` is `S` and that `h` occurs before `v`.

### Corollary 3.2 — exact global cancellation ledger

Shapley efficiency yields

\[
\boxed{
\sum_{v\in M}\mathcal C_v^M
=\sum_{v\in M}E(g_v)-E(f),
}
\tag{3.10}
\]

and

\[
\sum_{v\in M}\Theta_v^M=R_d(f),
\tag{3.11}
\]

because `R_d(1)=0` follows from `E(1)=P_c(1)=0`. Therefore summing (3.6) returns exactly (1.5), with the terminal response and all negative credits retained once and only once.

This is the requested identification of the one-q-flip Aumann--Shapley derivative with an average of the account04 baseline-cancelled plaquette curvatures.

## 4. The correct edge-local closure target

For each chosen q-flip basis, route an active `v` to its unique physical disagreement edge `epsilon_v(f)`. Put

\[
D_v:=E(g_v)-\mathcal C_v^M-\Theta_v^M=\frac8N L_v.
\tag{4.1}
\]

For any distribution over valid bases, define

\[
\overline D_e
=\mathbb E_{\mathcal B}
\sum_{v:\epsilon_v(f)=e}D_v.
\tag{4.2}
\]

Then exactly

\[
F_d(f)=\sum_{e\in\mathcal D_f}\overline D_e.
\tag{4.3}
\]

Hence a dimension-free residual payment would follow from the **signed**, normalized edge condition

\[
\boxed{
\overline D_e\le \frac{2K}{N}
\quad\text{for every disagreement edge }e.
}
\tag{4.4}
\]

Indeed `|D_f|=NJ(f)/2`, so (4.3) gives `F_d(f)<=KJ(f)`. Adding the inherited one-sided terminal estimate then gives FEI with the sum of the two constants.

Condition (4.4), not an absolute variation estimate, is the smallest local target produced by this run. Negative `D_v` are useful and must stay in the average.

## 5. A scale calculation: unsigned baseline geometry still misses by a factor n

The ordered-min construction can be randomized without losing account02's physical channel sparsity: choose a uniform coordinate order and use its first support coordinate as every pivot, plus a uniform anchor. For each fixed `v`, its pivot is then uniform over `supp(v)`, so the same incidence count used by account02 remains valid.

Fix a physical edge `e` in direction `i`. If `i` has rank `r`, put `c=n-r+1`. Exactly `2^{c-1}-1` q-flip basis elements have pivot `i`, and each has dual entropy `E_c`. For any one of them, exactly four anchors make its two-edge support contain `e`. Thus the expected **raw baseline support load** in relation-load units, before the active/frustrated filter and before plaquette/terminal refunds, is

\[
\boxed{
B_n=\frac1{2n}\sum_{c=2}^n(2^{c-1}-1)E_c.
}
\tag{5.1}
\]

In bit units the checker gives

\[
B_5=3.7545699\ldots,
\quad B_{10}=9.4717760\ldots,
\quad B_{20}=19.9536678\ldots.
\tag{5.2}
\]

Using `H_c^{(2)}=8c2^{-c}+O(2^{-c})`,

\[
B_n^{(2)}=n+O(1).
\tag{5.3}
\]

So random q-flip geometry plus the raw positive generator entropies gets the local scale down from an individual `Theta(N)` relation charge to only `Theta(n)` per edge, but **not** to `O(1)`. The missing factor is exactly the signed cancellation in `C_v+Theta_v`. This decisively rules out a proof that pays the dual-generator entropy baseline separately and treats the plaquette/terminal terms only as harmless errors.

This is not a counterexample to the signed route; it identifies the cancellation that the route must exploit.

## 6. Original-coordinate cut spectrum = q-flip frustration profile

Now connect the q-flip basis directly to the physical cut field used by account01. For a physical coordinate `i` define

\[
\tau_i(x)=f(x)f(x+e_i),
\qquad
\eta_i(x)=\frac{1-\tau_i(x)}2.
\tag{6.1}
\]

Thus `eta_i` is the disagreement-edge indicator and

\[
\mathbb E\eta_i=\operatorname{Inf}_i(f).
\]

It is invariant under `x -> x+e_i`, so `\widehat\eta_i(U)=0` whenever `i in U`.

For a nonzero displacement `w` with `w_i=0`, the physical q-flip based at `a` is the pair of parallel `i`-edges separated by `w`, and its syndrome is

\[
z_{i,w}(a)=\tau_i(a)\tau_i(a+w).
\tag{6.2}
\]

### Theorem 6.1 — `B16-QFLIP-CUT-RADON`

With normalized Walsh coefficients,

\[
\boxed{
\Pr_a[z_{i,w}(a)=-1]
=4\sum_{U:\,U\cdot w=1}\widehat\eta_i(U)^2.
}
\tag{6.3}
\]

Averaging over all nonzero `w` in the `(n-1)`-dimensional subspace `w_i=0`,

\[
\boxed{
\mathbb E_{w\ne0,\,w_i=0}
\Pr_a[z_{i,w}(a)=-1]
=
\frac{2^n}{2^{n-1}-1}
\operatorname{Inf}_i(f)(1-\operatorname{Inf}_i(f)).
}
\tag{6.4}
\]

#### Proof

The q-flip is frustrated exactly when `eta_i(a)` and `eta_i(a+w)` differ. Hence

\[
\Pr[z=-1]
=\mathbb E(\eta_i(a)-\eta_i(a+w))^2
=2\left(\mathbb E\eta_i-\mathbb E\eta_i(a)\eta_i(a+w)\right).
\]

Fourier expansion of the correlation gives

\[
2\sum_U\widehat\eta_i(U)^2(1-(-1)^{U\cdot w}),
\]

which is (6.3). For every nonzero Fourier frequency in the `i`-free subspace, exactly `2^{n-2}` of the nonzero `w` have `U dot w=1`. Finally Parseval gives

\[
\sum_{U\ne0}\widehat\eta_i(U)^2
=\mathbb E\eta_i^2-(\mathbb E\eta_i)^2
=\operatorname{Inf}_i(1-\operatorname{Inf}_i).
\]

Substitution gives (6.4). `square`

This is the concrete source bridge requested by the account01 noise-square route: the activity profile of the exact relation-code q-flips is a halfspace/Radon transform of the **same original-coordinate cut Fourier energy** whose total over `(i,U)` is bounded by influence. No synthetic edge geometry has been introduced.

## 7. What remains

The run does **not** prove (4.4), so full FEI remains open. The exact residual obligation is now narrower and uses all three compatible signed constructions:

- source: the q-flip activity/cut-spectrum identity (6.3), retaining original-coordinate disagreement geometry;
- transport: the Aumann--Shapley `1/q_A` relation allocation, retaining exact dual-code multiplicity and alternating R32 signs;
- sink/refund: the signed Fourier plaquette bank `C_v`, the R16/moment refunds already present in the compiler, and the terminal Shapley bank `Theta_v`;
- target: prove the basis-averaged edge residual `overline D_e` is `O(1/N)`, not merely that its positive baseline is small.

A natural next calculation is to substitute account04's exact signed log-cross-ratio formula for every curvature in (3.9), then group the result by the physical q-flip activity frequencies in (6.3). The account01 signed `L2` bank is exactly the kind of quadratic sink that may control this grouped expression. The crucial test is whether the resulting operator from `hat eta_i(U)` to the weighted cross-ratio field has dimension-free norm **after** the `n+O(1)` baseline in (5.3) is cancelled. If the norm still grows, that growth is the next rigorous obstruction.

## 8. Executed self-check

Companion code: `check_shapley_plaquette_bridge.py`.

It passed `py_compile` and returned `PASS` with:

- 814 exact dual-basis syndrome checks through `n=5`;
- 42 dual-generator entropy-formula checks through `n=5` (maximum absolute error `0` in the executed floating representation);
- 182 Shapley/plaquette identities through `n=4`, maximum absolute error `5.56e-16`;
- 33 exact-rational Aumann--Shapley identities with signed synthetic relation weights through `n=3`;
- 2,336 exact-rational cut-Radon identities, and 800 exact averaged identities, for **every Boolean function through n=3**.

The code SHA-256 is `f1c95c87e0652fed0b7150a0594be15126bf4d7d51c6bbc8a4d59c754b8a189d`; the output SHA-256 is `88df68f14dc74e381b39ba796c3391f1083d414d1c3ff25dd332698b4bf775eb`.

These are self-checks of formulas. The all-dimensional statements above have written algebraic proofs and are not inferred from finite enumeration.

## 9. Before / after

**Before:** the account02 route had an exact q-flip signed R32 disintegration and an open `L_v=O(n)` sufficient target; account04 had exact signed Fourier plaquette curvature but no formula identifying it with the q-flip charge; account01 had a dimension-free signed noise-square bank and asked for the actual cut-to-sink operator.

**After:** equation (3.6) exactly identifies each q-flip R32 charge with a Shapley average of the account04 plaquette bank plus the retained terminal share, while (6.3) exactly identifies q-flip activity with the Fourier energy of the physical disagreement indicator. Equation (5.1) proves that an unsigned baseline-only treatment still costs `Theta(n)` per edge, so a further signed refund is genuinely necessary rather than bookkeeping.

**Status:** `PARTIAL / PROVED IDENTITIES / FULL FEI OPEN`.
