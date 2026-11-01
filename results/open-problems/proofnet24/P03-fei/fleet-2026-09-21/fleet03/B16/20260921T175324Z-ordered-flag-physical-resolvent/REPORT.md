# B16 FEI signed transport — ordered-flag physical resolvent

**Date:** 21 September 2026  
**Scope:** `fleet03 / B16`, FEI signed transport proof  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact source-side transport/resolvent identities and a new compiler-facing flag-frame criterion. No novelty or publication-priority claim.

## 0. Route change and exact entering state

This run followed the current `FEI-SEVEN-TASKS-2026-09-21` owner order and did not audit the read-once certificate. The required `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md` were read before new mathematics.

The freshest compatible signed-transport inputs were:

1. fleet04/B16's parity-current theorem: after equal-syndrome **signed** aggregation, the ordinary/block selector defect is an exact minimum current with a positive double-resolvent energy; singleton syndrome is killed, while negative R32 credits remain inside the aggregate before squaring;
2. fleet02/B18's arbitrary-q-flip source theorem: every nonzero translation `u` has a central Radon square `S_u <= E_u^2/40`;
3. fleet02/B16/fleet01/B16's projective-incidence theorem: a nonnegative arbitrary-pivot frame is paid by physical influence once its original-coordinate incidence is bounded;
4. fleet02's explicit ordered-min q-flip relation basis: if `i` is the earliest coordinate of a basis displacement, then the q-flip consists of two physical `i`-edges separated by a vector using only coordinates **later** than `i`;
5. the previous fleet03/B16 independence-slope identity: the remaining low signed first-hit payment is an exact inverse-number/Hardy object, not a total-variance object.

The existing frame route had one conceptual defect: collapsing the ordered-min q-flip geometry immediately to an unoriented arbitrary translation forgets the physical pivot coordinate `i`. The calculation below changes route. It keeps the oriented pair `(i,w)` long enough to exploit the exact physical cut field, and only afterwards records what happens if orientation is collapsed.

No R32 coefficient is absolute-valued. No R16 moment refund, negative `2 mod 4` entropy credit, dual-code multiplicity or terminal-band payment is spent here.

---

## 1. Ordered-min q-flips are an exact coordinate flag

Fix a total order `pi` of the physical coordinates `[n]`. For a physical coordinate `i`, let

\[
L_i^\pi:=\{j:\pi(j)>\pi(i)\},\qquad m_i:=|L_i^\pi|.
\tag{1.1}
\]

In the ordered-min q-flip basis, every generator with pivot `i` is uniquely

\[
B_{i,w}(a)
=\{a,a+e_i,a+e_i+w,a+w\},
\qquad \varnothing\ne w\subseteq L_i^\pi.
\tag{1.2}
\]

Indeed the basis displacement is `v=e_i+w`, and `i` is its earliest support coordinate iff every coordinate of `w` occurs after `i`. The excluded case `w=0` would have basis displacement of weight one and is not a relation-code generator.

For later formulas it is harmless to add `w=0` with zero source cost.

Define the **flag law**

\[
\boxed{
\nu_i^\pi(w)=2^{-m_i}\mathbf 1_{\{w\subseteq L_i^\pi\}}.
}
\tag{1.3}
\]

This is the uniform law on all subsets of the later-coordinate flag at `i`.

---

## 2. PROVED — oriented physical flag payment

For a physical coordinate `i`, let

\[
\eta_i(x)=\frac{1-f(x)f(x+e_i)}2,
\qquad \alpha_i=\mathbb E\eta_i,
\tag{2.1}
\]

and define the q-flip derivative-disagreement kernel

\[
p_i(w)=\Pr_x[\eta_i(x)\ne\eta_i(x+w)].
\tag{2.2}
\]

Because `eta_i(x+e_i)=eta_i(x)`, its nonconstant Walsh support lies in the `i`-free quotient. Put

\[
a_i(U)=\widehat\eta_i(U)^2,
\qquad
E_i:=\sum_{U\ne0}a_i(U)=\alpha_i(1-\alpha_i).
\tag{2.3}
\]

The inherited q-flip Radon identity is

\[
p_i(w)=2E_i-2\sum_{U\ne0}a_i(U)(-1)^{U\cdot w}.
\tag{2.4}
\]

### Theorem 2.1 — `P03-B16-ORIENTED-FLAG-PAYMENT` — PROVED

For every Boolean `f`, every coordinate order `pi` and every physical coordinate `i`,

\[
\boxed{
\mathbb E_{W\sim\nu_i^\pi}p_i(W)
=2\sum_{U:\,U\cap L_i^\pi\ne\varnothing}a_i(U)
\le 2E_i.
}
\tag{2.5}
\]

Since `0<=p_i<=1`, also

\[
\boxed{
\mathbb E_{W\sim\nu_i^\pi}p_i(W)^2\le2E_i.
}
\tag{2.6}
\]

After the standard character fold, write

\[
\beta_i=\min\{\alpha_i,1-\alpha_i\},
\qquad J(f)=\sum_i\beta_i.
\]

The kernel `p_i` and `E_i` are invariant under complementing `eta_i`, so

\[
E_i=\beta_i(1-\beta_i)\le\beta_i.
\]
Therefore, **without any `1/n` normalization**, the whole oriented ordered-min flag satisfies

\[
\boxed{
\sum_i\mathbb E_{W\sim\nu_i^\pi}p_i(W)^2
\le
\sum_i\mathbb E p_i(W)
\le2J(f).
}
\tag{2.7}
\]

#### Proof

For a Walsh character `chi_U(w)=(-1)^{U dot w}`, fair independent choice of every coordinate in `L_i^pi` gives

\[
\mathbb E_{\nu_i^\pi}\chi_U(W)
=
\begin{cases}
1,&U\cap L_i^\pi=\varnothing,\\
0,&U\cap L_i^\pi\ne\varnothing.
\end{cases}
\]

Insert this into (2.4). The terms whose frequency misses the later flag cancel the constant `2E_i`; the terms meeting the flag contribute exactly twice their Fourier energy, proving (2.5). Equations (2.6)--(2.7) follow from `0<=p_i<=1` and the folded identity for `E_i`. `square`

### Why this is materially different from the arbitrary-pivot frame

Equation (2.7) pays **all physical pivots simultaneously** because every physical coordinate has its own genuine cut-energy budget `E_i`. No coordinate-incidence count of the separation vector `w` is needed as long as the source remains the oriented physical kernel `p_i(w)`.

This suggests a different compiler target from the current arbitrary-pivot one: retain the physical pivot `i` through the fully refunded parity-current map and dominate the resulting nonnegative source square by the ordered-flag measure (1.3). If that can be done with an absolute density constant, (2.7) gives a dimension-free sink directly.

This compiler domination is **OPEN**; (2.7) itself is proved.

---

## 3. PROVED — random order is exactly a Hardy resolvent

The flag law is not merely a convenient counting normalization. Averaging the coordinate order realizes the inverse-number operator exactly in the **original physical quotient**.

Fix `i` and average over a uniform random total order `Pi`. Conditional on `Pi`, sample `W` from `nu_i^Pi`.

### Theorem 3.1 — `P03-B16-FLAG-HARDY-RESOLVENT` — PROVED

For every Walsh frequency `U` not containing `i`,

\[
\boxed{
\mathbb E_{\Pi,W}(-1)^{U\cdot W}
=\frac1{|U|+1}.
}
\tag{3.1}
\]

Equivalently, if `D` is the Walsh degree operator on the `i`-free quotient, convolution by the random ordered flag is exactly

\[
\boxed{\mathcal R=(I+D)^{-1}.}
\tag{3.2}
\]

Thus its complementary high-pass is

\[
\boxed{I-\mathcal R=D(I+D)^{-1}.}
\tag{3.3}
\]

For the physical q-flip kernel,

\[
\boxed{
\mathbb E_{\Pi,W}p_i(W)
=2\sum_{U\ne0}a_i(U)\frac{|U|}{|U|+1}.
}
\tag{3.4}
\]

The corresponding exact positive refund is

\[
\boxed{
2E_i-\mathbb E_{\Pi,W}p_i(W)
=2\sum_{U\ne0}\frac{a_i(U)}{|U|+1}.
}
\tag{3.5}
\]

#### Proof

Generate a uniform random order from iid continuous priorities `R_j`. Conditional on `R_i=t`, a coordinate `j!=i` lies later than `i` independently with probability `1-t`. The fair-subset thinning in (1.3) then includes `j` in `W` independently with probability

\[
p=\frac{1-t}{2}.
\]

Hence, conditional on `t`,

\[
\mathbb E(-1)^{U\cdot W}=t^{|U|}.
\]

Since `R_i` is uniform on `[0,1]`, integration gives `1/(|U|+1)`. This proves (3.1)--(3.3). Inserting the multiplier into (2.4) gives (3.4)--(3.5). `square`

### Exact noise-mixture form

The same proof says

\[
\boxed{
W\ \stackrel{d}{=}\ \operatorname{Ber}(P)^{\otimes(n-1)},
\qquad P\sim\operatorname{Unif}[0,1/2],
}
\tag{3.6}
\]

on the coordinates other than `i`, with the Bernoulli bits independent conditional on `P`.

This gives a concrete original-coordinate realization of the same inverse-number mechanism that appears abstractly in the Hardy/current calculations. It is not yet an identification of the syndrome degree with the physical Walsh degree; no such unproved identification is claimed.

---

## 4. PROVED — normalized flag frame closes the positive arbitrary-pivot source side

The oriented payment in Section 2 deliberately retains the physical pivot. For comparison, collapse the orientation but insert the normalization forced by the full coordinate flag.

Define the nonnegative translation frame

\[
\boxed{
\lambda_\pi(w)
:=\frac1n\sum_{i=1}^n
2^{-m_i}\mathbf1_{\{w\subseteq L_i^\pi\}}.
}
\tag{4.1}
\]

It is a probability measure if the harmless atom `w=0` is included. Put the zero-pivot B18 square equal to zero.

If coordinate `j` has zero-based rank `r_\pi(j)` in the order, then

\[
\boxed{
d_j(\lambda_\pi)
:=\sum_{w:w_j=1}\lambda_\pi(w)
=\frac{r_\pi(j)}{2n}.
}
\tag{4.2}
\]

Indeed, exactly the `r_pi(j)` coordinates preceding `j` have `j` in their later set, and each such fair-subset law includes `j` with probability `1/2`.

Therefore

\[
\boxed{
D(\lambda_\pi)=\frac{n-1}{2n}<\frac12.
}
\tag{4.3}
\]

The fleet02/B16 incidence theorem and fleet02/B18 source theorem immediately give:

### Corollary 4.1 — `P03-B16-NORMALIZED-FLAG-RADON-FRAME` — PROVED

For every fixed coordinate order,

\[
\boxed{
\sum_{w\ne0}\lambda_\pi(w)\mathcal S_w(f)
\le\frac{n-1}{540n}J(f)
<\frac1{540}J(f).
}
\tag{4.4}
\]

If the order is also averaged, symmetry gives

\[
\mathbb E_\Pi d_j(\lambda_\Pi)
=\frac{n-1}{4n},
\]
so for the averaged frame

\[
\boxed{
\sum_{w\ne0}\mathbb E_\Pi\lambda_\Pi(w)\mathcal S_w(f)
\le\frac{n-1}{1080n}J(f)
<\frac1{1080}J(f).
}
\tag{4.5}
\]

This is an actual dimension-free positive source frame tailored to the **same ordered-min q-flip flag** used by the signed compiler. What is open is proving that the fully refunded compiler weights have bounded density/energy relative to this flag frame.

---

## 5. REFUTED shortcuts and why orientation matters

### 5.1 REFUTED as a closure route: collapse the whole flag without its normalization

If the factor `1/n` is omitted in (4.1), then

\[
\widetilde d_j=\frac{r_\pi(j)}2,
\qquad
\widetilde D=\frac{n-1}{2}.
\tag{5.1}
\]

Thus the existing arbitrary-pivot incidence theorem immediately loses `Theta(n)`. This is an exact obstruction, not a loose estimate.

By contrast, the **oriented** physical flag in Section 2 needs no `1/n`: it costs at most `2J` because each physical pivot retains its own cut-energy budget. Therefore forgetting the physical pivot before payment can itself manufacture the ambient-dimension loss.

This is the main conceptual outcome of the run.

### 5.2 REFUTED: replace the random flag by one fixed `Ber(1/4)` law

The random-order flag has one-coordinate inclusion probability

\[
\Pr(j\in W)=\frac14,
\]

but for two distinct coordinates

\[
\boxed{
\Pr(j,k\in W)=\mathbb E P^2=\frac1{12},
}
\tag{5.2}
\]

whereas independent `Ber(1/4)` bits would give `1/16`. The covariance is `1/48`.

So the exact inverse-number multiplier in (3.1) genuinely comes from the **mixture** (3.6); replacing it by one fixed noise level is false. The mixture must be retained if one wants the exact Hardy resolvent.

---

## 6. Compiler-facing conditional target

The current signed compiler should still perform all of the following **before** a nonnegative source square is formed:

- aggregate equal active syndromes with their R32 signs;
- retain `2 mod 4` negative entropy credits;
- keep the double-resolvent/minimum-current cancellation, including exact annihilation of the singleton syndrome layer;
- preserve dual-code multiplicity;
- leave R16 moment refunds and the terminal Shapley/band payment in their existing ledgers.

After those operations, there are now two precise sufficient interfaces.

### Oriented interface

If the resulting source can be represented as nonnegative weights `Lambda_{i,w}` on genuine ordered-min physical q-flips with

\[
\sum_{i,w}\Lambda_{i,w}\,\mathfrak q_{i,w}
\le C\sum_i\mathbb E_{\nu_i^\pi}\mathfrak q_{i,W}
\tag{6.1}
\]

for the relevant local source square `mathfrak q` dominated by `p_i(w)^2`, with one absolute `C`, then (2.7) gives an `O(J)` payment **without** any all-translation incidence estimate.

### Collapsed interface

If instead the compiler produces B18 central squares `S_w`, it is enough to prove that its post-current frame has a bounded density or bounded coordinate incidence relative to `lambda_pi`; (4.4)--(4.5) then give the dimension-free source payment.

Neither compiler comparison has yet been proved. Full FEI therefore remains OPEN.

The next attack should keep the `(i,w)` orientation through the fleet04 parity-current edge map and calculate the exact Radon--Nikodym weight relative to `2^{-m_i}`. The double inverse-number current and the dummy-Ward removal of the raw `m_i` factor are structurally compatible with this flag normalization. The decisive question is whether the authentic R32/R16 coefficients leave an absolute flag-density bound after signed aggregation. If not, preserve the authentic counterexample and move to a different signed mechanism.

---

## 7. Exact verification

`check_ordered_flag_resolvent.py` uses only the Python standard library and exact `Fraction` arithmetic. It does not rerun the read-once certificate.

It exhaustively checks every coordinate order through `n=7`:

- **5,912** complete orders;
- **40,318** exact coordinate-incidence identities;
- the exact normalized-frame formula `D=(n-1)/(2n)`.

It also averages every order for a fixed pivot through `n=7` and checks:

- **126** exact Walsh multipliers `1/(|U|+1)`;
- **56** one- and two-coordinate inclusion moments;
- `Pr(j in W)=1/4` and `Pr(j,k in W)=1/12`;
- the fixed-`Ber(1/4)` shortcut is therefore refuted exactly.

Executed checker SHA-256: `005feb8cb684f752d6aac3aa63436b0c63903c7f8c511a614e91a72a3032ed86`.  
Executed output SHA-256: `ec654fb0fc5ba97f479422caf5856da784bb3f33b3057c01096acd63293d2023`.  
Committed checker creation commit: `7659adb4909c82d6488d112f7351c279b4a70fe4`; readback Git blob: `9bdf74d3f959c8d70698bae688125d47e987a38f`.  
Verification creation commit: `2c3df9f419746263ea983e05c63202bfefe5eb2e`; its readback blob is recorded in the run receipt.

The finite checks are falsification evidence only. The all-dimensional statements in Sections 2--4 have explicit algebraic proofs above.

---

## 8. Ledger

**PROVED this run**

1. `P03-B16-ORIENTED-FLAG-PAYMENT`: for every fixed coordinate order, the complete unnormalized oriented q-flip flag has `sum_i E_W p_i(W)^2 <= 2J`.
2. `P03-B16-FLAG-HARDY-RESOLVENT`: random ordered-min flag convolution is exactly `(I+D)^-1` on the physical cut quotient, with high-pass multiplier `|U|/(|U|+1)`.
3. `P03-B16-NORMALIZED-FLAG-RADON-FRAME`: the collapsed normalized flag has deterministic incidence `(n-1)/(2n)` and pays B18 source square by `<J/540`; after order averaging the incidence is `(n-1)/(4n)` and the payment is `<J/1080`.

**REFUTED / DEAD SHORTCUTS**

1. collapsing the unnormalized full flag to arbitrary pivots: exact incidence `(n-1)/2`, hence a `Theta(n)` positive-frame loss;
2. replacing the exact random flag by fixed `Ber(1/4)`: pair moment `1/12 != 1/16`.

**PRESERVED**

Signed R32 cancellation; original-coordinate physical pivot geometry; dual-code multiplicity; R16 odd/moment refunds; negative entropy credits; terminal Shapley/band payment.

**OPEN**

Prove the authentic post-current compiler-to-source map has bounded ordered-flag density while retaining the physical pivot `(i,w)`, or produce an authentic R32 family refuting that bound. Full unrestricted FEI is **OPEN / NOT PROVED**.
