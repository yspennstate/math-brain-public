# B16 FEI signed transport — independence-slope Hardy factorization

**Date:** 21 September 2026  
**Scope:** `fleet03 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact signed reduction plus a decisive refutation of a tempting norm closure. No novelty/publication-priority claim.

## 0. Route change and entering state

This run read the current `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` before substantive work. It used the newest compatible signed-transport chain rather than rechecking the read-once certificate.

The entering obstruction from the fleet04 Hardy/R16 handoff was that the exact low-half kernel still contained, relation by relation,

\[
|R_A\cap R_B|\frac{(q_A-1)(q_B-1)}{q_Aq_B},
\qquad q_A=|R_A|,
\]

while the two-point MacWilliams collapse is naturally organized by symmetric difference. The previous fleet03 run separately gave a double-resolvent third-curvature current. The present route changes representation again: it eliminates the separate first-hit factors from the *positive* part of the low Hardy demand and identifies the entire inverse-degree correction as one explicit negative square. The remaining positive quantity is exactly a **degree-one biased-noise slope at independence** of the live signed MacWilliams potential.

No R32 coefficient is replaced by its absolute value. The live terminal subtraction remains inside the potential, and q-flip multiplicity, original-coordinate geometry, R16 refunds and negative `2 mod 4` credits are not spent again.

Throughout this report fix a Borel time `s`; the identities are pointwise in `s` and therefore may be integrated against the inherited nonnegative Borel measure afterwards.

---

## 1. Live odd syndrome potential

Let `M` be the active q-flip coordinate set. Aggregate the exact signed live R32 coefficients by active syndrome:

\[
b_R=b_R(s),\qquad R\subseteq M,
\]

with only odd `|R|` retained in the frustrated sector. Define

\[
\Phi(S)=\sum_{\substack{R\subseteq M\\ |R|\ {m odd}}}
b_R(-1)^{|S\cap R|},\qquad S\subseteq M.
\tag{1.1}
\]

For an active coordinate `v`, put

\[
m_v(t)=\sum_{R\ni v}b_Rt^{|R|-1},
\qquad 0\le t\le\tfrac12.
\tag{1.2}
\]

The inherited Hardy multiplier is

\[
h_v(t)=\sum_{R\ni v}
\frac{|R|-1}{|R|}b_Rt^{|R|-1}.
\tag{1.3}
\]

The exact low-half demand is

\[
\boxed{
\mathcal L_-(s)=
\sum_{v\in M}\int_0^{1/2}h_v(t)^2\,dt.
}
\tag{1.4}
\]

This is the same quantity whose collision-order expansion has weights
`1/((j-1)2^(j-1))` and signed coefficients `Gamma_j` in the prior Hardy/R16 bridge.

---

## 2. `P03-B16-BIASED-FIRST-LEVEL-IDENTITY` — **PROVED**

For `0<=t<=1/2`, set

\[
p_t=\frac{1-t}{2}.
\]

Let `E_{p_t}` denote product Bernoulli expectation on subsets of `M`. With

\[
\Delta_v\Phi(S)=\Phi(S)-\Phi(S\cup\{v\}),
\]

where `v` is absent from the sampled `S`, one has

\[
\boxed{
 m_v(t)=\frac12\,\mathbb E_{p_t}\Delta_v\Phi.
}
\tag{2.1}
\]

### Proof

For one odd Walsh monomial `R` containing `v`,

\[
\Delta_v(-1)^{|S\cap R|}=2(-1)^{|S\cap(R\setminus\{v\})|}.
\]

Under `Ber(p_t)`, each remaining active coordinate has sign mean
`1-2p_t=t`, hence its expectation is `2t^{|R|-1}`. Summing the signed coefficients proves (2.1).

Because every retained `R` is odd, complementing all selector bits leaves `Delta_v Phi` invariant. Thus the two complementary Bernoulli expectations appearing in the earlier central compiler are actually equal at the first-difference level; (2.1) is the compressed form of that symmetry.

Now let `W_1^{(p)}(Phi)` denote the level-one squared Fourier mass of `Phi` in the normalized `p`-biased Walsh basis. For a single coordinate,

\[
\widehat\Phi_p(\{v\})^2
=p(1-p)\left(\mathbb E_p\Delta_v\Phi\right)^2.
\]

Therefore

\[
\boxed{
\sum_v m_v(t)^2
=
\frac{W_1^{(p_t)}(\Phi)}{1-t^2}.
}
\tag{2.2}
\]

The previous relation-pair overlap has thus become exactly a first-level biased Fourier energy, with no triangle inequality and no positive-part operation on the signed R32 field.

---

## 3. `P03-B16-HARDY-NEGATIVE-SQUARE-IDENTITY` — **PROVED**

Define the Hardy averaging operator

\[
(Hm)(t)=\frac1t\int_0^t m(u)\,du.
\]

On the monomial `t^(q-1)`, `H` acts by `1/q`; consequently

\[
\boxed{h_v=(I-H)m_v.}
\tag{3.1}
\]

For every square-integrable polynomial `m` on `[0,T]`,

\[
\boxed{
\int_0^T(m-Hm)^2dt
=
\int_0^T m(t)^2dt
-rac1T\left(\int_0^T m(t)dt\right)^2.
}
\tag{3.2}
\]

Indeed, if `A(t)=integral_0^t m`, then

\[
-2mA/t+A^2/t^2=-\frac d{dt}(A^2/t),
\]

and integration gives (3.2).

At `T=1/2`, combining (1.4), (2.2) and (3.2) yields the main identity of this run:

\[
\boxed{
\begin{aligned}
\mathcal L_-(s)
&=
\int_0^{1/2}
\frac{W_1^{(p_t)}(\Phi)}{1-t^2}\,dt\\
&\quad-
2\sum_{v\in M}
\left[
\sum_{R\ni v}
\frac{b_R}{|R|2^{|R|}}
\right]^2.
\end{aligned}
}
\tag{3.3}
\]

The second line is a genuine **nonnegative refund subtracted from the demand**. It is not a new external bank and must not be spent twice; it is exactly the inverse-degree part already present in the Hardy multiplier.

### Relation-pair form

Let `q=|R|`, `r=|T|`, `j=q+r`, `o=|R cap T|`, and `d=|R triangle T|=j-2o`. Then (3.3) is equivalent term by term to

\[
\frac{o(q-1)(r-1)}{qr(j-1)2^{j-1}}
=
\frac{o}{(j-1)2^{j-1}}
-
\frac{o}{qr2^{j-1}}.
\tag{3.4}
\]

The complete second term in (3.4) is

\[
\boxed{
2\sum_v\left(
\sum_{R\ni v}\frac{b_R}{|R|2^{|R|}}
\right)^2\ge0.
}
\tag{3.5}
\]

Thus the previously awkward two factors `(q-1)/q` and `(r-1)/r` do **not** require two independent payments. They are exactly one positive unfiltered first-level energy minus one PSD square refund.

This is the structural simplification sought by the previous handoff.

---

## 4. `P03-B16-INDEPENDENCE-SLOPE-TRANSPORT` — **PROVED**

Fix `p in (0,1)`. Let `(X^rho,Y^rho)` be coordinatewise independent across active coordinates, with each coordinate pair having Bernoulli-`p` marginals and covariance

\[
\operatorname{Cov}(X_v^\rho,Y_v^\rho)=\rho p(1-p).
\]

Define the biased noise stability

\[
\operatorname{Stab}_{p,\rho}(\Phi)
:=\mathbb E\,\Phi(X^\rho)\Phi(Y^\rho).
\]

The normalized biased-Walsh expansion gives

\[
\operatorname{Stab}_{p,\rho}(\Phi)
=
\sum_{A\subseteq M}\rho^{|A|}\widehat\Phi_p(A)^2.
\tag{4.1}
\]

Therefore

\[
\boxed{
\left.\partial_\rho\operatorname{Stab}_{p,\rho}(\Phi)\right|_{\rho=0}
=W_1^{(p)}(\Phi).
}
\tag{4.2}
\]

Substituting (4.2) into (3.3) yields

\[
\boxed{
\begin{aligned}
\mathcal L_-(s)
&=
\int_0^{1/2}\frac1{1-t^2}
\left.
\partial_\rho\operatorname{Stab}_{p_t,\rho}(\Phi_s)
\right|_{\rho=0}dt\\
&\quad-
2\sum_v
\left[
\sum_{R\ni v}
\frac{b_R(s)}{|R|2^{|R|}}
\right]^2.
\end{aligned}
}
\tag{4.3}
\]

Equation (4.3) is an exact **integrated transport payment representation at independence**. It packages all cross-relation overlap into the first derivative of an honest two-copy product-noise coupling. Since the live potential already has the exact representation

\[
\Phi_s(S)=\Phi_{C_0,s}(g_S)-\Phi_{D_d,s}(g_S),
\]

(4.3) retains the actual terminal code, dual-code multiplicity and original physical MacWilliams geometry. The natural next move is to evaluate the independence slope through that physical representation before any norm or positive part is taken.

---

## 5. Tempting closure by total biased variance — **REFUTED AS A USEFUL ROUTE**

Parseval gives the valid inequality

\[
W_1^{(p)}(\Phi)\le\operatorname{Var}_p(\Phi).
\tag{5.1}
\]

It is tempting to insert (5.1) into (4.3) and then attack only total biased variance. This loses exactly the high-syndrome damping that the Hardy/R16 route worked to preserve.

Take one isolated odd syndrome monomial of degree `q>=3` with coefficient `b`. Then the exact low demand is

\[
\boxed{
\mathcal L_-^{(q)}
=
\frac{(q-1)^2}{q(2q-1)2^{2q-1}}\,b^2.
}
\tag{5.2}
\]

But the variance surrogate is

\[
\int_0^{1/2}
\frac{\operatorname{Var}_{p_t}(b\chi_R)}{1-t^2}dt
=
 b^2\int_0^{1/2}\frac{1-t^{2q}}{1-t^2}dt,
\tag{5.3}
\]

which tends to

\[
\operatorname{artanh}(1/2)b^2
=0.549306144334\ldots\,b^2
\]

as `q` grows, while (5.2) is asymptotic to `4^{-q}b^2`.

Exact-rational checks give the loss ratios

- `q=3`: `65.75`;
- `q=5`: `790.919643`;
- `q=9`: `172121.744`;
- `q=15`: `6.54511854e8`;
- `q=25`: `6.57654581e14`.

Hence replacing the independence slope by total biased variance is decisively unusable for a dimension-free closure. This also explains why the previously killed generic endpoint-`L2` route cannot be revived under a new name.

The degree-one slope in (4.3), not the whole variance, must be transported to physical influence.

---

## 6. Exact checker

`check_independence_slope_hardy.py` uses standard-library exact rational arithmetic. It tests 50 deterministic signed odd-syndrome coefficient families in dimensions 2, 3 and 4 and verifies:

1. `2 m_v(t)=E_{p_t} Delta_v Phi` at three rational central-band points;
2. `(1-t^2) sum_v m_v(t)^2 = W_1^{(p_t)}(Phi)`;
3. the derivative at independent coupling `rho=0` equals the same biased level-one mass;
4. the Hardy-filtered direct integral equals unfiltered energy minus the explicit negative square;
5. the negative square and unfiltered energy are separately nonnegative.

The run passed **918 exact assertions**. The checker also prints the single-monomial variance-surrogate losses quoted above.

Finite checks are falsification evidence only; the identities in Sections 2--4 are proved analytically.

---

## 7. What is now OPEN and the next attack

**PROVED:** the full low-half first-hit kernel has been reduced to a central integral of a degree-one biased-noise slope of the live signed MacWilliams potential, minus an explicit PSD refund. The separate factors `|R_A cap R_B|`, `(q_A-1)/q_A` and `(q_B-1)/q_B` no longer appear in the positive payment object.

**REFUTED:** replacing that degree-one slope by total biased variance; the loss is exponential in syndrome degree.

**OPEN:** a dimension-free physical payment of

\[
\int_0^{1/2}\frac1{1-t^2}
\left.\partial_\rho\operatorname{Stab}_{p_t,\rho}(\Phi_s)\right|_{\rho=0}dt
\]

after the genuine Borel integration and with the terminal subtraction retained.

The next attack is to differentiate the exact `C_0-D_d` MacWilliams representation under this **one-coordinate correlated selector coupling**. The derivative at `rho=0` marks exactly one active q-flip coordinate. That should be compared directly, order/anchor averaged if necessary, with the fleet01 physical q-flip energy-distance/Radon bank, whose odd physical multipliers already have a dimension-free `J/270` square budget. The target is an exact marked multiplier or Radon kernel; no total-variance relaxation is allowed.

Full FEI remains **OPEN / NOT PROVED**.
