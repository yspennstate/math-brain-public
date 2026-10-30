# B16 FEI signed transport — projective geometric charges give an exact noise-resolvent payment

**Date:** 21 September 2026  
**Scope:** `fleet01 / B16`, full FEI creative proof search  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Route:** APPROACH 10/13, signed transport / noise interpolation / Boolean correlation constraints  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Novelty / publication priority:** unverified; no priority claim.

## 0. Result of this run

The preceding fleet01 calculation proved that q-flip activity has one-sided Walsh sign and that a centered ordered-min kernel with nonnegative codimension charges has only an `O(Q_n/n)` negative-multiplier debit. The fleet03/fleet04 Ward calculations then showed that dummy-coordinate refinement forces exact signed Shapley/plaquette refunds, and on the two-variable parity-switch diagnostic changes the raw codimension charge `H_c` to the geometric charge `2^{3-c}`. The remaining fleet01 question was how to handle the **constant displacement mode** without destroying the favorable signed cancellation.

This run proves that for every projectively stable codimension-only charge law, the constant mode and all nonconstant modes combine **exactly** into a bounded noise-resolvent energy. No separate constant-mode payment is needed.

> **Main theorem.** If a local codimension charge is invariant under one harmless dummy split, so that a codimension-`c` generator of charge `q_c` is replaced by two codimension-`c+1` descendants with the same total charge, then necessarily
> \[
> q_c=\Lambda 2^{-c}.
> \]
> For the associated random-order ordered-min kernel, every Walsh multiplier is explicit:
> \[
> A_{n,r}^{\Lambda}
> =\frac{\Lambda}{2(r+1)}-\frac{\Lambda}{n}+\frac{\Lambda 2^{-n}}n,
> \qquad 0\le r\le n-1.
> \]
> Hence the dangerous constant mode cancels against the matching nonconstant mode in the q-flip pairing:
> \[
> \boxed{
> \langle \mathcal K_n^{\Lambda},p_i\rangle
> =\Lambda\sum_{U\ne0}\frac{|U|}{|U|+1}\widehat\eta_i(U)^2
> =\Lambda\langle \eta_i-\alpha_i,
> L(I+L)^{-1}(\eta_i-\alpha_i)\rangle.
> }
> \]
> In particular
> \[
> 0\le \langle \mathcal K_n^{\Lambda},p_i\rangle
> \le \Lambda E_i
> \le \Lambda\min(\alpha_i,1-\alpha_i).
> \]
> This is dimension-free and includes the DC mode.

For the proved parity-switch Shapley-refunded charge `q_c=2^{3-c}` one has `Lambda=8`. Each of its two active physical cuts has one Fourier mode of weight one and squared mass `1/4`, so the complete refunded q-flip kernel payment is exactly `1` bit per active coordinate, hence `2` bits total, independent of how many dummy coordinates are appended. This matches the spectral entropy `H_2=2` of that diagnostic. Thus the earlier `Theta(n)` raw constant-mode obstruction is completely removed on the diagnostic, not merely centered away.

The universal gap is now sharper: the fleet04 block Ward theorem proves **block-total** projective invariance for arbitrary Boolean phase games, but it does not prove that an interacting Shapley block disintegrates into nonnegative **local codimension-only** projective charges. The next sufficient theorem is therefore a positive projective disintegration of the fully refunded residual into geometric components plus already-negative signed credits. The resolvent theorem below would then pay every geometric component without an absolute-value loss.

---

## 1. Entering exact q-flip Fourier identity

For a physical coordinate `i`, write
\[
\eta_i(x)=\frac{1-f(x)f(x^{\oplus i})}{2},
\qquad
\alpha_i=\mathbb E\eta_i,
\qquad
E_i=\alpha_i(1-\alpha_i).
\]
Identify `eta_i` with a Boolean function on `W_i=F_2^{n-1}`. Its q-flip frustration profile is
\[
p_i(w)=\Pr_x[\eta_i(x)\ne\eta_i(x+w)].
\]
The earlier fleet01 theorem gives the normalized Walsh transform
\[
\widehat p_i(0)=2E_i,
\qquad
\widehat p_i(U)=-2\widehat\eta_i(U)^2\quad(U\ne0),
\tag{1.1}
\]
and Parseval gives
\[
E_i=\sum_{U\ne0}\widehat\eta_i(U)^2.
\tag{1.2}
\]
No absolute value will be inserted into (1.1).

For nonnegative codimension charges `q_2,...,q_n`, the random-order ordered-min normalized kernel has multiplier at Walsh weight `r` (`0<=r<=n-1`)
\[
A^q_{n,r}
=\frac1n\sum_{c=2}^n q_c
\left[
2^{c-1}
\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}
-1
\right],
\tag{1.3}
\]
with the binomial ratio interpreted as zero when `c-1>n-1-r`. Formula (1.3) is the same layer-counting identity used in the preceding B16 multiplier reports; here we retain `r=0` rather than centering it out.

---

## 2. Projective consistency forces a geometric charge law

Call a codimension-only charge sequence `(q_c)_{c>=2}` **one-dummy projectively consistent** when splitting a codimension-`c` local generator into its two dummy slices preserves its total local charge:
\[
q_c=2q_{c+1}\qquad(c\ge2).
\tag{2.1}
\]
This is the local scalar analogue of the exact block-total Ward identity proved in the fleet04 dummy-tower handoff. It is an additional locality assumption: block-total projective consistency alone does not imply (2.1) for an interacting game.

### Theorem 2.1 — `B16-PROJECTIVE-CHARGE-UNIQUENESS`

A codimension-only charge law is one-dummy projectively consistent iff there is a scalar `Lambda` such that
\[
\boxed{q_c=\Lambda 2^{-c}\quad(c\ge2).}
\tag{2.2}
\]
For nonnegative charges, `Lambda>=0`.

#### Proof

Equation (2.1) says `2^c q_c=2^{c+1}q_{c+1}`. Hence `2^cq_c` is independent of `c`; call the common value `Lambda`. The converse is immediate. `square`

Thus the geometric law observed in the exact parity-switch Ward calculation is not an arbitrary convenient ansatz: it is the **unique** codimension-only fixed law under harmless binary refinement, up to one scalar.

---

## 3. Exact multipliers of the projective kernel

Set
\[
q_c=\Lambda 2^{-c}.
\tag{3.1}
\]
Then
\[
q_c2^{c-1}=\frac\Lambda2,
\qquad
\sum_{c=2}^nq_c=\Lambda\left(\frac12-2^{-n}\right).
\tag{3.2}
\]
Put `N=n-1`, `k=c-1`. For `0<=r<=N`,
\[
\frac{\binom{N-r}{k}}{\binom Nk}
=\frac{\binom{N-k}{r}}{\binom Nr}.
\tag{3.3}
\]
Therefore the hockey-stick identity gives
\[
\begin{aligned}
\sum_{c=2}^n
\frac{\binom{n-1-r}{c-1}}{\binom{n-1}{c-1}}
&=\frac1{\binom{n-1}{r}}
\sum_{j=r}^{n-2}\binom jr\\
&=\frac{\binom{n-1}{r+1}}{\binom{n-1}{r}}\\
&=\frac{n-r-1}{r+1}
=\frac n{r+1}-1.
\end{aligned}
\tag{3.4}
\]
The formula remains valid at `r=n-1`, when both sides are zero.

### Theorem 3.1 — `B16-PROJECTIVE-KERNEL-MULTIPLIERS`

For every `n>=2` and `0<=r<=n-1`,
\[
\boxed{
A_{n,r}^{\Lambda}
=\frac{\Lambda}{2(r+1)}
-\frac{\Lambda}{n}
+\frac{\Lambda2^{-n}}n.
}
\tag{3.5}
\]
In particular the multiplier **difference from the constant mode** is independent of ambient dimension:
\[
\boxed{
A_{n,0}^{\Lambda}-A_{n,r}^{\Lambda}
=\frac\Lambda2\frac r{r+1}.
}
\tag{3.6}
\]

#### Proof

Insert (3.2) and (3.4) into (1.3):
\[
A_{n,r}^{\Lambda}
=\frac{\Lambda}{2n}
\left(\frac n{r+1}-1\right)
-\frac\Lambda n\left(\frac12-2^{-n}\right),
\]
which is (3.5). Subtract the `r=0` case to obtain (3.6). `square`

This is stronger than separately bounding the centered kernel. The large DC term is not paid on its own; only the exact spectral **gap** between `r=0` and the mode actually occupied by the cut survives.

---

## 4. Exact uncentered signed payment and its noise-semigroup form

Let `mathcal K_n^Lambda` denote the normalized displacement kernel whose Walsh multipliers are (3.5). Using (1.1), normalized Parseval gives
\[
\begin{aligned}
\langle\mathcal K_n^\Lambda,p_i\rangle
&=2E_iA_{n,0}^\Lambda
-2\sum_{U\ne0}A_{n,|U|}^\Lambda\widehat\eta_i(U)^2\\
&=2\sum_{U\ne0}
\bigl(A_{n,0}^\Lambda-A_{n,|U|}^\Lambda\bigr)
\widehat\eta_i(U)^2.
\end{aligned}
\tag{4.1}
\]
Insert (3.6).

### Theorem 4.1 — `B16-PROJECTIVE-NOISE-RESOLVENT-PAYMENT`

For every Boolean cut field `eta_i` and every `Lambda>=0`,
\[
\boxed{
\langle\mathcal K_n^\Lambda,p_i\rangle
=\Lambda\sum_{U\ne0}
\frac{|U|}{|U|+1}\widehat\eta_i(U)^2.
}
\tag{4.2}
\]
Consequently
\[
\boxed{
0\le\langle\mathcal K_n^\Lambda,p_i\rangle
\le\Lambda E_i.
}
\tag{4.3}
\]
After the legitimate minimizing-character gauge,
\[
E_i=\alpha_i(1-\alpha_i)
\le \min(\alpha_i,1-\alpha_i)=:j_i,
\]
so whenever the same projective component is present across coordinates,
\[
\boxed{
\sum_i\langle\mathcal K_n^\Lambda,p_i\rangle
\le\Lambda J(f).
}
\tag{4.4}
\]

#### Noise-semigroup interpretation

On `W_i`, let the number operator be
\[
L\chi_U=|U|\chi_U
\]
and let `T_t` be the standard Walsh noise operator
\[
T_t\chi_U=t^{|U|}\chi_U.
\]
Writing `g_i=eta_i-alpha_i`, (4.2) is exactly
\[
\boxed{
\langle\mathcal K_n^\Lambda,p_i\rangle
=\Lambda\langle g_i,L(I+L)^{-1}g_i\rangle.
}
\tag{4.5}
\]
Since
\[
\frac r{r+1}=\int_0^1rt^r\,dt,
\]
we also have the genuine noise interpolation
\[
\boxed{
\langle\mathcal K_n^\Lambda,p_i\rangle
=\Lambda\int_0^1
\langle g_i,LT_tg_i\rangle\,dt.
}
\tag{4.6}
\]
Thus the projectively stable transport charge is literally a bounded noise-resolvent energy. The operator norm of `L(I+L)^{-1}` on the nonconstant Walsh space is at most one; (4.3) is therefore not a lossy Cauchy--Schwarz estimate but the exact spectral identity followed by the scalar bound `r/(r+1)<=1`.

This is the requested APPROACH-10 bridge in a class where the Ward/projective structure is exact.

---

## 5. The former parity-switch obstruction is completely paid, DC included

The fleet03 Shapley--dummy Ward theorem proved that for the dummy-extended two-variable parity-switch / one-corner defect, the exact entropy share of a codimension-`c` active generator after signed Shapley curvature refund is
\[
\widetilde H_c=2^{3-c}=8\,2^{-c}.
\tag{5.1}
\]
So this diagnostic is exactly the projective law with `Lambda=8`.

For either active physical coordinate `i`, the cut field depends on only the other active coordinate:
\[
\eta_i=\frac{1-\chi_{\{j\}}}{2}
\quad\text{up to complement/translation}.
\tag{5.2}
\]
Hence its only nonconstant Walsh mass has
\[
|U|=1,
\qquad
\widehat\eta_i(U)^2=\frac14.
\tag{5.3}
\]
Equation (4.2) gives
\[
\boxed{
\langle\mathcal K_n^{8},p_i\rangle
=8\cdot\frac12\cdot\frac14=1
}
\tag{5.4}
\]
for every ambient `n>=2`. There are exactly two active physical coordinates, so
\[
\boxed{
\sum_i\langle\mathcal K_n^{8},p_i\rangle=2.
}
\tag{5.5}
\]
The spectral entropy of the two-variable one-corner defect is `H_2=2` bits. Therefore the complete **refunded entropy-displacement kernel pairing**, including its constant Walsh mode, is exactly dimension-stable on the family that previously exhibited `Theta(n)` raw growth.

This is stronger than the preceding bounded-multiplier diagnostic. The large raw DC mode has disappeared through the exact spectral gap (3.6), not through an independent positive payment.

No claim is made here that every other terminal/R16 compiler term vanishes term-by-term on this diagnostic; (5.5) identifies the refunded q-flip entropy-displacement component itself.

---

## 6. What this proves about the universal target — and what remains open

The fleet04 dummy-tower theorem proves a stronger **block** statement than scalar (2.1): when an old Boolean phase is split through arbitrarily many dummy coordinates and the descendants are kept as one coupled block, their total Shapley share is exactly the old share. The theorem is fully projective, but in a general interacting Boolean phase game the share of one descendant can depend on the prefix state and on other blocks. Therefore it does **not** yet imply that the fully refunded residual can be written using a nonnegative scalar codimension sequence satisfying (2.1).

The present theorem says that if such a positive projective disintegration exists, its payment problem is solved exactly.

### Sufficient compiler statement

Suppose for every physical coordinate `i` the fully refunded q-flip residual admits a decomposition
\[
R_i=\sum_a\mathcal K^{\Lambda_{i,a}}+C_i,
\qquad \Lambda_{i,a}\ge0,
\tag{6.1}
\]
where each `mathcal K^{Lambda}` is a projective geometric kernel as above, the remainder is a genuine signed credit
\[
\langle C_i,p_i\rangle\le0,
\tag{6.2}
\]
and
\[
\sup_i\sum_a\Lambda_{i,a}\le L<\infty.
\tag{6.3}
\]
Then (4.3) gives immediately
\[
\boxed{
\sum_i\langle R_i,p_i\rangle\le L J(f).
}
\tag{6.4}
\]
No absolute value is taken on the credit remainder.

So the next live B16 question is a **representation theorem**, not a norm bound:

> Can the exact block-coupled Shapley/plaquette/terminal/R16 residual be disintegrated into positive projectively consistent geometric components of uniformly bounded total `Lambda` mass, plus the already-known negative R32/moment credits?

The newest fleet04 two-scale first-hit handoff gives a complementary route to this representation: its aggregate selector covariance splits into an internal Bernoulli curvature square and a one-dimensional radial moment variance. The geometric resolvent identity above suggests testing whether the radial piece is precisely a positive mixture of `L(I+L)^{-1}` resolvents after the authentic alternating R16 moment coefficients are inserted. That is the next calculation; a generic unsigned radial-to-internal comparison is already known to be false.

**Full FEI remains OPEN.**

---

## 7. Independent exact self-check

`check_projective_resolvent.py` checks only the new algebra, not the settled read-once certificate and not FEI itself.

It verifies:

1. the exact multiplier formula (3.5) for four rational values of `Lambda`, every `2<=n<=40`, and every `0<=r<n` — **3,276 exact rational cases**;
2. the direct displacement-space q-flip pairing against the resolvent formula (4.2) for **all Boolean cut fields through `dim(W)=3`**, for two rational `Lambda` values — **552 exact cases**;
3. the dummy-extended parity-switch pairing through ambient dimension `n=12` — **11 exact cases**, always exactly one unit per active coordinate for `Lambda=8`.

Observed output:

```text
PASS
exact_multiplier_cases 3276
exact_boolean_cut_pairing_cases 552
parity_switch_dummy_dimensions 11
projective_lambda8_A0_minus_A1 2
parity_switch_payment_per_active_coordinate 1
parity_switch_two_coordinate_total 2
```

The checker is a consistency test; the proof is the finite algebra above.
