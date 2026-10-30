# B16 FEI signed transport — central-band Hardy/Ward radial resolvent

**Date:** 21 September 2026  
**Scope:** `fleet04 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed identities plus a dimension-free one-dimensional Hardy reduction. No novelty or publication-priority claim.

## 0. Entering state and route

This run continues the newest compatible signed first-hit chain. In particular it consumes:

- the fleet04 parity-safe Hardy/R16 bridge for the low radial half;
- the fleet03 exact first-hit Ward/Hoeffding/plaquette resolvent, including the final-frustration projection and two-sided prefix/suffix identity;
- the fleet01 high-resolvent compression, so no R16 high-resolvent channel is re-paid here.

The new observation is that the **low radial Hardy demand itself is already an exact two-sided Ward transform of the same signed plaquette-plus-terminal field that controls the internal first-hit bank**. Moreover, because this is the low Hardy half, it samples only Bernoulli prefix densities between `1/4` and `3/4`. Thus the radial low-half problem does not need an endpoint estimate or a generic all-prefix norm.

No R32 coefficient is absolute-valued. The terminal mixed difference remains inside the signed plaquette field. The original q-flip basis, dual-code multiplicity, R16 refunds, negative entropy credits and terminal-band accounting are unchanged.

---

## 1. Radial first-hit notation

Let

\[
C(z)=\sum_A c_A\prod_{v\in R_A}z_v,
\qquad q_A=|R_A|\ \text{odd},
\]

be the final-frustrated signed survivor polynomial on the actual active q-flips. For each active q-flip `v`, put

\[
m_v(t):=\partial_v C(t\mathbf 1)
=\sum_{A:v\in R_A} c_A t^{q_A-1}.
\tag{1.1}
\]

The Hardy multiplier used in the preceding radial factorization is

\[
\mathsf H:=D(I+D)^{-1},
\qquad D=t\frac d{dt}.
\]

On a monomial `t^d`,

\[
\mathsf H(t^d)=\frac d{d+1}t^d.
\tag{1.2}
\]

Hence the `q_A=1` mode is annihilated exactly. The fleet04 Hardy/R16 calculation gives the actual low-half radial contribution as

\[
\boxed{
\mathcal L_-
=\sum_v\int_0^{1/2}[\mathsf Hm_v(t)]^2dt.
}
\tag{1.3}
\]

This is the same quantity previously written as
\(\sum_{j\ge6,\ j\text{ even}}\Gamma_j/((j-1)2^{j-1})\).

---

## 2. `P03-B16-CENTRAL-HARDY-CESARO` — PROVED

For every differentiable polynomial `m`,

\[
\boxed{
\mathsf Hm(t)
=m(t)-\frac1t\int_0^t m(s)ds
=\frac1t\int_0^t s m'(s)ds
=\int_0^1 \lambda t\,m'(\lambda t)d\lambda.
}
\tag{2.1}
\]

### Proof

The inverse of `I+D` with the regular boundary condition at zero is

\[
[(I+D)^{-1}m](t)=\frac1t\int_0^t m(s)ds.
\]

Subtracting from `m` and integrating by parts gives (2.1). `square`

Thus the Hardy factor is not an unexplained degree multiplier: it is the **Cesaro deviation from the radial prefix average**.

A useful consequence, by Cauchy--Schwarz, is the dimension-free weighted derivative bound

\[
\boxed{
\int_0^T[\mathsf Hm(t)]^2dt
\le \frac12\int_0^T t(T-t)m'(t)^2dt
\qquad(T>0).
}
\tag{2.2}
\]

Indeed

\[
\left[\frac1t\int_0^t s m'(s)ds\right]^2
\le \frac12\int_0^t s m'(s)^2ds,
\]

and Fubini yields (2.2). No sign is removed inside `m'`.

For the live low half `T=1/2`,

\[
\boxed{
\mathcal L_-
\le\frac12\sum_v\int_0^{1/2}
 t\left(\frac12-t\right)
 \left(\sum_{u\ne v}\partial_{uv}C(t\mathbf1)\right)^2dt.
}
\tag{2.3}
\]

Equation (2.3) is radial-only. It does not claim that the full radial bank is absorbed by the internal bank; the previously proved star obstruction to that stronger statement remains valid.

---

## 3. `P03-B16-CENTRAL-BAND-WARD-RESOLVENT` — PROVED

Let `G=(8/N)P=E-R_d` be the retained full compiler set function from the newest fleet03 handoff. For an unordered q-flip pair `{u,v}`, retain the signed compiler plaquette-plus-terminal field

\[
\mathcal P_{uv}(S)
:=\kappa_{g_S}(g_u,g_v)+\Delta_{uv}R_d(g_S),
\tag{3.1}
\]

so that

\[
\Delta_{uv}G=-\mathcal P_{uv}.
\tag{3.2}
\]

For `0<=t<=1`, set

\[
p_t:=\frac{1-t}{2}
\]

and define the two-sided plaquette divergence

\[
\boxed{
A_v(t):=\sum_{u\ne v}
\left[
\mathbb E_{p_t}\mathcal P_{uv}
-
\mathbb E_{1-p_t}\mathcal P_{uv}
\right].
}
\tag{3.3}
\]

The fleet03 two-sided Ward identity gives, pair by pair,

\[
\frac{32}{N}\partial_{uv}C(t\mathbf1)
=
\mathbb E_{p_t}\mathcal P_{uv}
-
\mathbb E_{1-p_t}\mathcal P_{uv}.
\tag{3.4}
\]

Summing `u` therefore yields

\[
\boxed{
m_v'(t)=\frac N{32}A_v(t).}
\tag{3.5}
\]

Combining (2.1), (3.5), and (1.3) gives the exact low-radial representation

\[
\boxed{
\mathcal L_-
=
\frac{N^2}{1024}
\sum_v\int_0^{1/2}
\left[
\frac1t\int_0^t s A_v(s)ds
\right]^2dt.
}
\tag{3.6}
\]

This is an exact signed **radial Ward resolvent**. In contrast to the internal fleet03 resolvent, which requires all noisy plaquette chaoses, the radial channel sees only the two-sided **mean plaquette divergence** and then applies a one-dimensional Cesaro/Hardy resolvent.

Using (2.2),

\[
\boxed{
\mathcal L_-
\le
\frac{N^2}{2048}
\sum_v\int_0^{1/2}
 t\left(\frac12-t\right)A_v(t)^2dt.
}
\tag{3.7}
\]

Now put `p=(1-t)/2`. Since `0<=t<=1/2`, both `p` and `1-p` lie in the **central Bernoulli band** `[1/4,3/4]`. Thus (3.7) is equivalently

\[
\boxed{
\mathcal L_-
\le
\frac{N^2}{1024}
\sum_v\int_{1/4}^{1/2}
(1-2p)\left(2p-\frac12\right)
\left[
\sum_{u\ne v}
(\mathbb E_p\mathcal P_{uv}-\mathbb E_{1-p}\mathcal P_{uv})
\right]^2dp.
}
\tag{3.8}
\]

The terminal mixed difference has **not** been split from `mathcal P_uv`. Therefore (3.6)--(3.8) do not spend the terminal band twice.

### Equivalent first-difference form

For completeness, let

\[
B_v(p)=\mathbb E_p\Delta_vG+\mathbb E_{1-p}\Delta_vG.
\]

The `k=1` Ward identity gives

\[
m_v(t)=\frac N{16}B_v\left(\frac{1-t}{2}\right).
\tag{3.9}
\]

Hence, for `p in [1/4,1/2]`,

\[
\boxed{
\mathsf Hm_v(1-2p)
=\frac N{16}
\left[
B_v(p)-
\frac1{1/2-p}\int_p^{1/2}B_v(q)dq
\right].
}
\tag{3.10}
\]

So the low Hardy load is exactly the squared deviation of the **symmetric central-prefix marginal** from its average toward `p=1/2`.

---

## 4. The newest Pasch obstruction is purely internal

The newest fleet03 handoff produced an admissible `n=4` signed Pasch packet of eight `q=3` relations, with signs

\[
\mathcal T_+=\{123,145,246,356\},
\qquad
\mathcal T_-=\{124,135,236,456\}.
\tag{4.1}
\]

Each q-flip vertex occurs exactly twice with `+` sign and twice with `-` sign. Since every support has the same size `q=3`,

\[
m_v(t)
=t^2\sum_{A:v\in R_A}c_A
=0
\quad\text{for every }v.
\tag{4.2}
\]

Therefore

\[
\boxed{\mathcal K_{\rm rad}=\mathcal L_-=0}
\tag{4.3}
\]

for the abstract signed Pasch trade, while the exact internal bank is

\[
\boxed{\mathcal K_{\rm int}=\frac45.}
\tag{4.4}
\]

At the genuine Borel coefficient magnitude `1/8` from the one-point `n=4` Boolean phase,

\[
\boxed{\mathcal K_{\rm int}=\frac1{80},\qquad
\mathcal K_{\rm rad}=\mathcal L_-=0.}
\tag{4.5}
\]

Thus the Pasch packet is a **pure internal-chaos obstruction**, not a radial obstruction. This sharply separates the two remaining mechanisms:

- internal first-hit fluctuation requires the full fleet03 noisy plaquette resolvent and cannot be replaced by a mean plaquette;
- low radial fluctuation requires only the central-band mean plaquette divergence in (3.6).

More generally, any fixed-`q` signed packet satisfying

\[
\sum_{A:v\in R_A}c_A=0
\quad\text{for every }v
\]

has identically zero radial bank, even though higher signed incidence chaoses may leave a positive internal bank.

---

## 5. What this changes

Before this run, the low Hardy half had only the collision-order/R16 representation

\[
\mathcal L_-
=\sum_{j\ge6,\ j\text{ even}}
\frac{\Gamma_j}{(j-1)2^{j-1}},
\]

and the open bridge was a signed comparison of `Gamma_j` to the authentic R16 first-separation deposits.

Now the **same quantity** also has the exact compiler-facing Ward representation (3.6). This gives two independent possible payment interfaces:

1. the parity-safe R16 collision bridge from the preceding fleet04 run;
2. the central-band two-sided plaquette-divergence bridge proved here.

The second route is structurally attractive because the fresh fleet03 internal theorem already places the internal bank in the same signed plaquette-plus-terminal field. It does not prove a source-side influence bound by itself. In particular, the square of the divergence `sum_u(...)` cannot be replaced by a sum of pair squares without potentially paying a dimension factor. That is the next analytic issue.

No claim is made that the terminal term can be separated from (3.3) by triangle inequality, or that the old R16 bank can now be spent twice. Full FEI remains open.

---

## 6. Next exact target

The clean combined source target is now to prove a dimension-free **divergence estimate** for the central-band antisymmetric plaquette field,

\[
\sum_v\int_{1/4}^{1/2}
(1-2p)(2p-1/2)
\left[
\sum_{u\ne v}
(\mathbb E_p\mathcal P_{uv}-\mathbb E_{1-p}\mathcal P_{uv})
\right]^2dp,
\]

using the original-coordinate q-flip Radon/Fourier identity and the inherited signed fractional noisy-square bank, while keeping `Delta_uv R_d` inside the same transform.

If that divergence norm is unbounded on an admissible Boolean family, preserve the counterexample and fall back to the already exact R16 collision-weight interface rather than reviving a generic absolute-value estimate.

---

## 7. Exact self-check

`check_central_hardy_ward.py` uses only standard-library exact rational arithmetic. It verifies:

- 20 exact Cesaro/Hardy identities across four signed odd-support relation families;
- 100 exact `k=1` two-sided Ward identities at rational Bernoulli parameters;
- 205 exact `k=2` plaquette Ward identities;
- 20 exact weighted Hardy bounds (2.2);
- the signed Pasch identities `K_rad=L_-=0`, `K_int=4/5`, and after the genuine `1/8` Borel scaling `K_int=1/80`.

The checker returned `PASS`. The calculations are falsification evidence; equations (2.1)--(3.10) are proved analytically above.
