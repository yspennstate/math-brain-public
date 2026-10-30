# B16 FEI — exact Ward/Hoeffding face decomposition and a two-sided plaquette resolvent

**Date:** 21 September 2026  
**Fleet scope:** `fleet03 / B16`  
**Execution label:** **WITHOUT_VERIFIED_BRAIN**  
**Live role:** FEI signed transport proof; sprint subrole: martingale/Shapley stopping without a false local charge  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact algebraic/probabilistic identities plus an exact admissible q-flip packet obstruction. No novelty or publication-priority claim.

## 0. Route change and newest compatible state

This run first read the owner-required `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`, and consumed the newest compatible B16 dependencies rather than rechecking a settled certificate.

The entering signed first-hit state is:

- fleet03: the exact common-order first-hit selector and centered Jaccard kernel;
- fleet04: the exact split of that covariance into an internal Bernoulli bank plus a radial moment bank;
- fleet01: the radial Hardy/resolvent factorization and, more recently, the exact high-resolvent spectral compression. In particular the inherited R16 high-resolvent response is already bounded by `2 ln(3/2) J` and can alternatively be absorbed by one third of Fourier entropy. The live compiler obstruction is therefore concentrated on the signed small-resolvent/first-hit channel plus the separately retained terminal response.

The previous fleet04 internal estimate used Bernoulli Poincare:

\[
\mathcal K_{\rm int}(C)
\le \int_0^1 t(1-t)\sum_{v}\sum_{u\ne v}
\mathbb E_t[(\partial_{uv}C(Y))^2]dt.
\]

That estimate is dimension-free as an inequality but it hides exactly how much higher q-flip interaction order is being overpaid. The new route diagonalizes the internal bank *exactly* in Bernoulli Hoeffding chaoses and then inserts the inverse number operator before any absolute value. This produces an exact noisy-plaquette resolvent and an exact prefix/suffix Ward bridge to the signed compiler. It also yields a genuine `n=4` Boolean q-flip packet showing that the diagonal mean plaquette alone can vanish while the internal covariance remains positive.

No R32 coefficient is absolute-valued. `0 mod 4` debits and `2 mod 4` negative credits remain signed inside every derivative before squaring. Original q-flip coordinates and their physical disagreement-edge identities are unchanged. R16 moment refunds/high-resolvent reserves and the terminal band are not spent again below.

---

## 1. Entering first-hit polynomial

Let `M` be the actual active q-flip set. For every final-frustrated retained relation `A`, let

\[
R_A\subseteq M,\qquad q_A=|R_A|\ \text{odd},
\]

and let `c_A` be its signed R32 coefficient. Define the multilinear survivor polynomial

\[
\boxed{C(z)=\sum_A c_A\prod_{v\in R_A}z_v.}\tag{1.1}
\]

For `v in M`, put

\[
P_v(y)=\partial_v C(y).
\tag{1.2}
\]

If `Y^{(t)}` has independent `Bernoulli(t)` coordinates, the fleet04 first-hit calculation gives the exact internal bank

\[
\boxed{
\mathcal K_{\rm int}(C)
=\sum_{v\in M}\int_0^1
\operatorname{Var}_t(P_v(Y^{(t)}))\,dt.
}\tag{1.3}
\]

This is one part of the exact centered first-hit covariance; the radial moment bank remains separate and is not altered here.

---

## 2. `P03-B16-WARD-HOEFFDING-FACE-DECOMPOSITION` — **PROVED**

Put

\[
w(t)=t(1-t).
\]

### Theorem 2.1

For every real multilinear signed relation polynomial `C`,

\[
\boxed{
\mathcal K_{\rm int}(C)
=\sum_{\substack{F\subseteq M\\|F|\ge2}}
|F|\int_0^1
w(t)^{|F|-1}
\bigl(\partial_F C(t\mathbf 1)\bigr)^2dt.
}\tag{2.1}
\]

All relation signs are summed inside `partial_F C` before the square.

### Proof

Fix `v` and `t`. Multilinearity gives the exact Taylor expansion about the diagonal point `t 1`:

\[
P_v(Y)=
\sum_{T\subseteq M\setminus\{v\}}
\partial_{T\cup\{v\}}C(t\mathbf1)
\prod_{u\in T}(Y_u-t).
\tag{2.2}
\]

Under independent `Bernoulli(t)` coordinates, the centered monomials

\[
\prod_{u\in T}(Y_u-t)
\]

are pairwise orthogonal and have squared norm `w(t)^{|T|}`. Therefore

\[
\operatorname{Var}_t(P_v)
=\sum_{\varnothing\ne T\subseteq M\setminus\{v\}}
w(t)^{|T|}
\bigl(\partial_{T\cup\{v\}}C(t\mathbf1)\bigr)^2.
\tag{2.3}
\]

Now set `F=T union {v}`. A fixed face `F` of size `k>=2` occurs once for each of its `k` choices of `v`. Summing `v` and integrating `t` proves (2.1). `square`

### Pair-kernel recovery

For two relation supports `R_A,R_B`, write

\[
r=|R_A|,\quad s=|R_B|,\quad h=|R_A\cap R_B|,\quad \nu=|R_A\cup R_B|.
\]

The cross contribution of the order-`k` face layer is

\[
\binom hk k\,B(r+s-k,k),\qquad 2\le k\le h,
\tag{2.4}
\]

where `B` is the beta function. Summing `k` gives exactly

\[
h\left(\frac1\nu-\frac1{r+s-1}\right),
\tag{2.5}
\]

the fleet04 internal pair kernel. Thus (2.1) is not a new upper bound; it is an exact diagonalization of the already identified internal covariance.

---

## 3. `P03-B16-WARD-PLAQUETTE-RESOLVENT` — **PROVED**

The exact face formula can be written using only second q-flip derivatives, but with the correct inverse-number resolvent rather than a raw Poincare charge.

For fixed `t`, let `T_{rho,t}` be the product noise operator on the q-flip mask cube with stationary measure `Bernoulli(t)`: on the centered Hoeffding basis it acts by

\[
\mathsf T_{\rho,t}
\prod_{u\in T}(Y_u-t)
=\rho^{|T|}\prod_{u\in T}(Y_u-t).
\tag{3.1}
\]

### Theorem 3.1

For every signed multilinear `C`,

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm int}(C)
=2\int_0^1\!\int_0^1
&\rho\,t(1-t)
\sum_{v\in M}\sum_{u\ne v}
\mathbb E_t\Big[
\big(\mathsf T_{\rho,t}\partial_{uv}C(Y)\big)^2
\Big]\,d\rho\,dt.
\end{aligned}
}\tag{3.2}
\]

This is an exact signed noisy-plaquette square, not a Poincare upper bound.

### Proof

For `Q=P_v-E_tP_v`, write its Hoeffding expansion as

\[
Q=\sum_{\varnothing\ne T}a_T
\prod_{i\in T}(Y_i-t).
\]

Its variance is

\[
\sum_{T\ne\varnothing}a_T^2w(t)^{|T|}.
\tag{3.3}
\]

The Bernoulli Dirichlet form of `T_{rho,t}Q` is

\[
w(t)\sum_u\mathbb E_t
[(\partial_u\mathsf T_{\rho,t}Q)^2]
=
\sum_{T\ne\varnothing}|T|\rho^{2|T|}
a_T^2w(t)^{|T|}.
\tag{3.4}
\]

Since

\[
2|T|\int_0^1\rho^{2|T|-1}d\rho=1,
\tag{3.5}
\]

integrating (3.4) against `2 d rho/rho` recovers (3.3) exactly. Finally

\[
\partial_u\mathsf T_{\rho,t}P_v
=\rho\,\mathsf T_{\rho,t}\partial_{uv}C,
\]

which turns `2 d rho/rho` into the `2 rho d rho` form in (3.2). Sum over `v` and integrate `t`. `square`

### What the resolvent removes

If one drops the noise contraction in (3.2), the fleet04 Poincare bank is recovered. On a face of size `k`, the raw Poincare bank charges exactly `k-1` times the true contribution in (2.1). The `rho` integral in (3.2) inserts the exact factor `1/(k-1)`. Therefore the new representation removes the entire high-interaction-order loss without discarding a sign or a physical q-flip coordinate.

This is the q-flip analogue of the `z/(1+z)` resolvent mechanism that appeared independently in the fleet01 spatial/radial work: high interaction order is damped by an exact inverse number operator rather than bounded by counting it.

---

## 4. `P03-B16-FINAL-FRUSTRATION-PROJECTION` — **PROVED**

The survivor polynomial uses only relations that are frustrated at the final active set. To connect it correctly to the full compiler one must project onto those odd final syndromes; simply identifying it with the unrestricted parity game is wrong.

Let

\[
P(S)=\sum_{A\in C_0\setminus D_d}
 c_A\,1_{\{|R_A\cap S|\ \mathrm{odd}\}},
\qquad S\subseteq M,
\tag{4.1}
\]

be the full retained R32 parity set function on generator subsets, and let

\[
\Pi(S)=\sum_{A:q_A\ \mathrm{odd}}
 c_A\,1_{\{|R_A\cap S|\ \mathrm{odd}\}}
\tag{4.2}
\]

be its final-frustrated projection. Then relation by relation,

\[
\boxed{
\Pi(S)=\frac12\left[P(S)-P(M\setminus S)+P(M)\right].
}\tag{4.3}
\]

Indeed even-`q_A` relations cancel between `S` and its complement, while for odd `q_A` exactly one of `S` and `M\setminus S` has odd intersection and `P(M)` supplies the remaining constant.

Let `F subset M`, `|F|=k`, and `S subset M\setminus F`. With `Delta_F` the iterated set difference,

\[
\boxed{
\Delta_F\Pi(S)
=\frac12\left[
\Delta_FP(S)-(-1)^k
\Delta_FP\big((M\setminus F)\setminus S\big)
\right].
}\tag{4.4}
\]

Thus even-order interactions are **prefix-minus-complementary-suffix**, while odd-order interactions are prefix-plus-suffix. This is the exact Ward symmetry forced by final frustration.

---

## 5. `P03-B16-TWO-SIDED-WARD-HIERARCHY` — **PROVED**

The final-frustration projection converts the exact Hoeffding faces into signed two-sided finite differences of the full compiler.

### Theorem 5.1

For every nonempty face `F`, `k=|F|`, and `0<=t<=1`, put

\[
p=\frac{1-t}{2}.
\]

If `S` is an independent `Bernoulli(p)` subset of `M\setminus F`, then

\[
\boxed{
\mathbb E_p\Delta_F\Pi(S)
=(-1)^{k+1}2^{k-1}\partial_FC(t\mathbf1).
}\tag{5.1}
\]

Consequently, if `G=(8/N)P=E-R_d` is the retained full compiler set function,

\[
\boxed{
\partial_FC(t\mathbf1)
=(-1)^{k+1}\frac{N}{2^{k+3}}
\left[
\mathbb E_p\Delta_FG
-(-1)^k\mathbb E_{1-p}\Delta_FG
\right].
}\tag{5.2}
\]

### Proof

For one relation, the parity game is

\[
c_A\frac{1-\prod_{v\in R_A}(1-2x_v)}2.
\]

If `F subset R_A`, its `k`th discrete derivative is

\[
(-1)^{k+1}2^{k-1}c_A(-1)^{|R_A\cap S|};
\]
if `F` is not contained in `R_A`, it is zero. Under `Bernoulli(p)` on the remaining coordinates,

\[
\mathbb E(-1)^{|R_A\cap S|}
=(1-2p)^{q_A-k}=t^{q_A-k}.
\]

Summing final-frustrated relations proves (5.1). Combine (5.1) with the projection identity (4.4), noting that the complementary subset has `Bernoulli(1-p)` law, and use `P=(N/8)G` to obtain (5.2). `square`

### Exact hierarchy for the internal bank

Substituting (5.2) into (2.1) gives

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm int}(C)
=\frac{N^2}{64}
\sum_{k\ge2}\frac{k}{4^k}
\sum_{|F|=k}
\int_0^1 w(t)^{k-1}
\Big[
&\mathbb E_{(1-t)/2}\Delta_FG\\
&-(-1)^k\mathbb E_{(1+t)/2}\Delta_FG
\Big]^2dt.
\end{aligned}
}\tag{5.3}
\]

The coefficient is exponentially damped in interaction order before any inequality is used. Equation (5.3) is exact.

### The ordinary plaquette layer

For `F={u,v}`, define the signed compiler plaquette field

\[
\mathcal P_{uv}(S)
:=\kappa_{g_S}(g_u,g_v)+\Delta_{uv}R_d(g_S).
\tag{5.4}
\]

Because `Delta_uv E=-kappa`,

\[
\Delta_{uv}G=-\mathcal P_{uv}.
\]

Therefore

\[
\boxed{
\frac{32}{N}\partial_{uv}C(t\mathbf1)
=
\mathbb E_{(1-t)/2}\mathcal P_{uv}
-
\mathbb E_{(1+t)/2}\mathcal P_{uv}.
}\tag{5.5}
\]

This is the exact two-sided Ward identity for the mean plaquette channel. The terminal mixed difference is retained *inside* `P_uv`; splitting it by triangle inequality would throw away cancellation and risk spending the terminal band twice.

---

## 6. `P03-B16-ANISOTROPIC-PLAQUETTE-RESOLVENT` — **PROVED**

The previous identity can be strengthened from a diagonal mean to a pointwise transform and inserted into the exact resolvent (3.2).

For a function `h` on subsets of `M\setminus{u,v}`, let `N_y h(emptyset)` denote anisotropic Walsh noise evaluated at the all-plus character:

\[
\mathsf N_yh(\varnothing)
=\sum_T\widehat h(T)\prod_{j\in T}y_j,
\qquad 0\le y_j\le1.
\tag{6.1}
\]

Let `J` be complement on `M\setminus{u,v}`. From the parity Fourier expansion,

\[
\Delta_{uv}\Pi(S)
=-2\sum_{A:q_A\,\mathrm{odd},\ u,v\in R_A}
 c_A(-1)^{|(R_A\setminus\{u,v\})\cap S|}.
\tag{6.2}
\]

Hence, for every anisotropic parameter vector `y`,

\[
\boxed{
\partial_{uv}C(y)
=-\frac12\mathsf N_y(\Delta_{uv}\Pi)(\varnothing)
=\frac{N}{32}
\mathsf N_y(\mathcal P_{uv}-\mathsf J\mathcal P_{uv})(\varnothing).
}\tag{6.3}
\]

Now multilinearity gives

\[
\mathsf T_{\rho,t}F(Y)
=F\big(t\mathbf1+\rho(Y-t\mathbf1)\big).
\tag{6.4}
\]

Put

\[
y^{t,\rho,Y}=t\mathbf1+\rho(Y-t\mathbf1).
\]

Substitution into (3.2) yields the exact compiler-facing identity

\[
\boxed{
\begin{aligned}
\mathcal K_{\rm int}(C)
=\frac{N^2}{512}
\int_0^1\!\int_0^1
&\rho\,t(1-t)
\sum_{v}\sum_{u\ne v}
\mathbb E_{Y\sim\mathrm{Ber}(t)}\\
&\left[
\mathsf N_{y^{t,\rho,Y}}
(\mathcal P_{uv}-\mathsf J\mathcal P_{uv})(\varnothing)
\right]^2
d\rho\,dt.
\end{aligned}
}\tag{6.5]

Equation (6.5) is the main transport advance of this run. The previously opaque internal first-hit covariance is exactly a random-anisotropic-noise square of the **antisymmetric prefix/suffix compiler plaquette plus terminal field**. All higher first-hit interaction orders have already been resummed by the inverse-number resolvent. No false local charge, no absolute R32 coefficient, and no scale-dependent selector is introduced.

The bracket in (6.5) is still not proved to be paid by the inherited original-coordinate fractional noisy-square bank. That is the remaining analytic bridge, not an identity I claim here.

---

## 7. Attempted shortcut and a genuine Boolean q-flip packet obstruction

A tempting simplification of (5.3) is to keep only the mean two-sided plaquette layer `k=2` and discard the higher Ward chaoses. That shortcut is **REFUTED**, and it already fails inside an actual `n=4` one-point Boolean phase.

Use the ordered-min anchored q-flip basis at anchor `0` and choose six active q-flips

\[
\begin{aligned}
v_1&=3=\{0,1\},& v_2&=5=\{0,2\},& v_3&=6=\{1,2\},\\
v_4&=10=\{1,3\},&v_5&=11=\{0,1,3\},&v_6&=13=\{0,2,3\}.
\end{aligned}
\tag{7.1}
\]

For the one-point phase `f(0)=-1`, `f(x)=+1` otherwise, all of these basis q-flips are active. Consider the Pasch trade of triple supports

\[
\mathcal T_+=\{123,145,246,356\},
\qquad
\mathcal T_-=\{124,135,236,456\}.
\tag{7.2}
\]

The corresponding actual dual-code relation weights are

\[
4,4,8,8\quad\text{on }\mathcal T_+,
\qquad
6,6,6,6\quad\text{on }\mathcal T_-.
\tag{7.3}
\]

Thus their R32 signs are exactly `+,+,+,+,-,-,-,-`. At the Borel point `s/N=pi/4`, `N=16`, every coefficient has the same magnitude

\[
2N\,2^{-N/2}=\frac18.
\tag{7.4}
\]

Every q-flip pair occurs equally often with `+` and `-` sign in this packet. Therefore for its survivor polynomial

\[
\boxed{
\partial_{ij}C(t\mathbf1)=0
\quad\text{for every pair }i<j\text{ and every }t.
}\tag{7.5}
\]

So the entire `k=2` diagonal mean-plaquette layer in (2.1) is zero.

But the eight third derivatives are the nonzero coefficients `plus/minus 1/8`. Hence the exact internal bank of this packet is

\[
\boxed{
8\cdot3\cdot\frac1{64}
\int_0^1t^2(1-t)^2dt
=\frac1{80}>0.
}\tag{7.6}
\]

Before the `1/8` Borel scaling, the abstract signed Pasch trade has internal bank `4/5` with zero diagonal pair layer.

This does **not** disprove FEI and does not assert that these eight relations can be isolated from the rest of the full R32 compiler. It does prove that any packetwise/local proof which replaces the exact noisy plaquette resolvent by only its diagonal expected plaquette is invalid even on genuine Boolean/q-flip/R32 data. The hidden order-three fluctuation must be retained. Formula (6.5) retains it automatically.

---

## 8. Exact checker

`check_ward_hoeffding_resolvent.py` uses only the Python standard library and `Fraction`. It checked:

- 21 deterministic signed odd-support relation families on active sets of sizes 3, 4 and 5;
- exact equality of the direct internal pair kernel and the face decomposition (2.1);
- 336 exact conditional-variance comparisons between brute-force Bernoulli enumeration and the Hoeffding expansion;
- 742 exact finite-difference/parity-bridge identities (5.1);
- inverse-number resolvent normalization through interaction order 20;
- the abstract Pasch trade `K_int=4/5`, pair-diagonal layer `0`;
- the actual `n=4` one-point q-flip packet, including its eight dual-code relation weights/signs, exact Borel coefficient magnitude `1/8`, pair-diagonal layer `0`, and `K_int=1/80`.

The checker returned `PASS`. These computations are falsification evidence; Theorems 2.1–6.1 are proved algebraically above.

---

## 9. Status ledger

**PROVED**

- `P03-B16-WARD-HOEFFDING-FACE-DECOMPOSITION`: exact all-order face-square diagonalization of the internal first-hit covariance.
- `P03-B16-WARD-PLAQUETTE-RESOLVENT`: exact inverse-number/noise factorization using only second q-flip derivatives; the raw Bernoulli Poincare bank overpays a face of size `k` by exactly `k-1`.
- `P03-B16-FINAL-FRUSTRATION-PROJECTION`: exact prefix/complement projection onto relations frustrated at the final active set.
- `P03-B16-TWO-SIDED-WARD-HIERARCHY`: exact exponentially normalized prefix/suffix interaction hierarchy for the retained compiler.
- `P03-B16-ANISOTROPIC-PLAQUETTE-RESOLVENT`: exact representation (6.5) of the internal bank as a random anisotropic-noise square of the antisymmetric signed plaquette-plus-terminal field.
- an exact admissible `n=4` Boolean/q-flip/R32 packet where every diagonal mean pair charge vanishes but the internal bank equals `1/80`.

**REFUTED / DEAD AT ITS EXACT SCOPE**

- replacing the internal first-hit bank by only the `k=2` diagonal mean-plaquette layer;
- any packetwise argument that treats vanishing expected plaquette curvature as vanishing selector fluctuation.

The older dead routes remain dead: relationwise diagonal-only Ward energy, generic endpoint selector `L2`, absolute-correlation transport, and absorbing the radial bank into the internal bank.

**PRESERVED / UNSPENT**

- signed `0 mod 4` / `2 mod 4` R32 cancellation;
- dual-code multiplicity and the ordered q-flip basis;
- each active q-flip's inherited original-coordinate disagreement-edge identity;
- the R16 moment/high-resolvent refund bank, including the new explicit high-resolvent reserve;
- the separate terminal-band payment. Terminal differences appear inside the exact plaquette field but have not been separately upper-bounded or spent here.

**OPEN / CONDITIONAL**

Full FEI remains **OPEN / NOT PROVED**. The new exact internal identity must still be paid by an already retained source-side bank. The radial first-hit moment bank remains separately subject to the fleet01 Hardy/R16/terminal bridge.

---

## 10. Next attack

The next B16 step should not return to a raw Poincare estimate. It should compare the exact square in (6.5) to the existing original-coordinate q-flip Radon/noisy-square bank.

The concrete target is now:

> prove a dimension-independent bound for the random-anisotropic-noise norm of the antisymmetric compiler plaquette field `P_uv - J P_uv` in (6.5), using the exact fleet01 q-flip frustration Fourier inversion and the fleet03 fractional noisy-square bank, while retaining the terminal mixed difference inside the same signed transform until an authorized terminal payment can be separated without triangle inequality.

The advantage over the previous target is precise: all higher q-flip interaction orders have already been resummed with the exact `1/(k-1)` resolvent, so a source-side comparison no longer needs to pay an extra face-order factor. The `n=4` Pasch packet shows this resolvent is not optional.

If the resulting source operator has unbounded norm on an admissible Boolean family, this common-order first-hit mechanism should be abandoned. If it is bounded, the internal selector obstruction closes, leaving the already isolated radial moment/terminal bridge plus the small-resolvent compiler bookkeeping.
