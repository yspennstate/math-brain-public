Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum reasoning was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding scheduler selector, so I do not claim otherwise.

# P07-B — cubic preconditioning, a proved initial weighted-kurtosis step, and the exact same-mask recoupling gap

**Status:** **OPEN / PROVED PARTIAL** on Randomstrasse101 Conjecture 18.  
**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`.  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`.  
**Fresh pre-write master:** `fd79845ecc0c83bd1b3ee59dc97011536ffbfc2f`.  
**Previous own substantive checkpoint:** `probability_campaigns/progress_first_2026-09-20/P07/fourier_dual/2026-09-20T1912+0300__gauge_projected_involution_clipping.md`.  
**Latest complementary P07-A checkpoint read:** `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T1845+0300__orthogonal_core_mass_variance_bridge.md`. P07-A owns the orthogonal-core mass / variance / influence route to the sharp leading constant. This report stays on the Fourier-dual bounded-certificate route.

**Outside target:** Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18.  
**Primary partial result:** A. S. Bandeira, J. Błasiok, D. Dmitriev, U. Faure, A. Kireeva, D. Kunisky, *The Lovász number of random circulant graphs*, arXiv:2502.16227.  
**Exact source endpoint:** for the dense random undirected circulant model on odd `n`,
\[
\mathbb E\vartheta(G_n)=(1+o(1))\sqrt n.
\]
The primary partial-result paper still gives
\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]
Hence the fixed full-source metric remains
\[
\boxed{\alpha_{LL}=1/2\to1/2.}
\]
No new arbitrary-`n` theta asymptotic is claimed in this report.

The assignment-time source and repository recovery has already been done and is not repeated as an admission screen. For continuity, the source-equivalent Fourier LPs used in this line are
\[
\max n y_0
\quad\text{s.t.}\quad
 y_k=y_{n-k},\ \|y\|_1=1,\ y\ge0,\ \langle y,f_k\rangle=0
\ \text{on selected edge differences},
\]
and
\[
\min 1+n t_0
\quad\text{s.t.}\quad
 t_k=t_{n-k},\ Ft\ge0,\ t_k=-1/n
\ \text{on selected edge differences}.
\]
The equivalent moment-depth normalization inherited from the P07 line is
\[
\mathbb E\vartheta(G_n)=1+\mathbb E\frac1{\delta_D}.
\tag{0.1}
\]
The previous P07-B report proved that
\[
\mathbb E[K_D^{(2)}\mathbf 1_{\mathcal B_n}]=O(1),
\qquad
\mathcal B_n=\{n/8\le |D|\le3n/8\},
\tag{0.2}
\]
would already imply
\[
\mathbb E\vartheta(G_n)=O(\sqrt n),
\tag{0.3}
\]
removing the source `sqrt(log log n)` loss. It then reduced (0.2) to a gauge-projected multiscale clipping orbit and isolated `GQOK4`, a weighted fourth-moment statement on that endogenous orbit.

This run makes two changes. First, before any nonlinear clipping, the quadratic target is passed once through the exact same-mask involution. The resulting field is a degree-at-most-three Rademacher chaos with **uniformly bounded Walsh multiplicity and `O(1/n)` coordinate influences**. This proves the weighted-kurtosis condition at the initial preconditioned state. Second, an independent-multiplier calculation proves a dimension-free `2 -> 4` estimate for every deterministic residual, thereby isolating the remaining difficulty to a precise **same-mask recoupling** step rather than a generic Fourier `L^4` problem. No dependent Fourier coordinates are treated as independent.

---

## 1. Normalization and the exact quadratic interpolation target

Let
\[
M=\{1,\ldots,(n-1)/2\},
\qquad
\varepsilon_a=2\mathbf1_{\{a\in D\}}-1,
\]
and extend the signs evenly to `Z_n` by
\[
Y(0)=0,
\qquad
Y(\pm a)=\varepsilon_a.
\tag{1.1}
\]
Use the unnormalized DFT
\[
\widehat f(\xi)=\sum_{x\in\mathbb Z_n}f(x)e^{-2\pi i\xi x/n},
\qquad
f(x)=\frac1n\sum_{\xi\in\mathbb Z_n}\widehat f(\xi)e^{2\pi i\xi x/n}.
\tag{1.2}
\]
Define
\[
G=\frac{\widehat Y}{\sqrt n},
\qquad
\mathcal K f=\frac1{\sqrt n}G*f.
\tag{1.3}
\]
Then
\[
\widehat{\mathcal K f}(\xi)=Y(\xi)\widehat f(\xi).
\tag{1.4}
\]
Thus `K` is self-adjoint, kills the zero Fourier mode, and is an isometry on the nonzero-frequency subspace. For every transverse selected-frequency test
\[
f_z(x)=\sum_{a\in D}z_a\cos(2\pi ax/n),
\qquad
\sum_{a\in D}z_a=0,
\tag{1.5}
\]
we have exactly
\[
\boxed{\mathcal K f_z=f_z.}
\tag{1.6}
\]

The quadratic interpolation target from the previous reports is represented in physical space by
\[
\boxed{w=\frac{G^2}{16}.}
\tag{1.7}
\]
Any bounded `h` satisfying
\[
\langle f_z,h\rangle=\langle f_z,w\rangle
\quad\text{for every transverse selected }f_z
\tag{1.8}
\]
is an exact quadratic interpolant and yields
\[
K_D^{(2)}\le\|h\|_\infty.
\tag{1.9}
\]
The key observation for this run is that before clipping `w`, one may pass it through `K` at **zero interpolation cost**:
\[
\boxed{
\langle f_z,w\rangle
=\langle \mathcal K f_z,w\rangle
=\langle f_z,\mathcal K w\rangle.
}
\tag{1.10}
\]
Put
\[
\boxed{u:=\mathcal K w.}
\tag{1.11}
\]
Unlike `w`, whose physical tail is quadratic in a subgaussian field, `u` has a useful finite-chaos structure in the **independent source mask bits**.

---

# 2. New theorem: cubic preconditioning has bounded Walsh multiplicity

Since
\[
\widehat{G^2}(\xi)=\sum_{\eta\in\mathbb Z_n}Y(\eta)Y(\xi-\eta),
\]
(1.4) gives
\[
\widehat u(\xi)
=\frac1{16}Y(\xi)\sum_{\eta}Y(\eta)Y(\xi-\eta).
\tag{2.1}
\]
Therefore, for every physical site `x`,
\[
\boxed{
u(x)=\frac1{16n}
\sum_{\xi,\eta\in\mathbb Z_n}
Y(\xi)Y(\eta)Y(\xi-\eta)e^{2\pi i\xi x/n}.
}
\tag{2.2}
\]
Terms involving `Y(0)` vanish.

Each nonzero `Y(\xi)` is one of the independent Rademacher variables `epsilon_a`, indexed by the pair class `[xi]={xi,-xi}`. Hence every nonzero summand in (2.2) reduces, after `epsilon_a^2=1`, to a Walsh monomial of degree one or three.

## Lemma P07-B.31 — bounded fiber multiplicity

Fix odd `n` and a physical site `x`. Group the ordered pairs `(xi,eta)` in (2.2) according to the reduced Walsh monomial
\[
\varepsilon_{[\xi]}\varepsilon_{[\eta]}\varepsilon_{[\xi-\eta]}.
\]
Every degree-three Walsh monomial has at most `24` preimages, and every degree-one Walsh monomial has at most an absolute constant number of preimages. In particular, a uniform fiber bound
\[
\boxed{L_*:=48}
\tag{2.3}
\]
is valid for all odd `n`.

### Proof

For a degree-three monomial, the three pair classes are distinct. There are at most `3!` ways to assign those classes to `[xi]`, `[eta]`, and `[xi-eta]`. Once the first two assigned pair classes are fixed, there are at most `2^2` sign choices for representatives `xi` and `eta`; the third class is then determined by `xi-eta`. Hence there are at most `6*4=24` preimages.

For a degree-one monomial, two of the three pair classes must coincide and cancel, or all three coincide. Consider, for example, `[xi]=[eta]`. The choice `eta=xi` makes `xi-eta=0` and the term vanishes, so any nonzero term has `eta=-xi` and the surviving class is `[2xi]`. Because `n` is odd, multiplication by `2` is invertible on `Z_n`, hence `[2xi]` determines `[xi]` uniquely. The cases `[xi]=[xi-eta]` and `[eta]=[xi-eta]` are identical after relabeling. The all-equal case can occur only through the finite `3`-torsion degeneracy and contributes only another absolute number of representations. The conservative bound `48` therefore covers all cases. QED.

## Theorem P07-B.32 — uniform cubic-chaos moment bound

For every odd `n` and every physical site `x`, `u(x)` is a real multilinear Rademacher polynomial of degree at most three and
\[
\boxed{
\mathbb E_D u(x)^2\le \frac{L_*}{256}=\frac3{16}.
}
\tag{2.4}
\]
Consequently, by Bonami hypercontractivity,
\[
\boxed{
\bigl(\mathbb E_D|u(x)|^q\bigr)^{1/q}
\le (q-1)^{3/2}\sqrt{\frac3{16}}
\qquad(q\ge2),
}
\tag{2.5}
\]
and in particular
\[
\boxed{
\mathbb E_D\|u\|_4^4\le
3^6\left(\frac3{16}\right)^2
<26.
}
\tag{2.6}
\]
There are absolute constants `c,C>0` such that
\[
\boxed{
\Pr_D\{|u(x)|>t\}\le C e^{-c t^{2/3}}
\qquad(t\ge C),
}
\tag{2.7}
\]
uniformly in `n` and `x`.

### Proof

Before grouping, (2.2) contains fewer than `n^2` nonzero ordered pairs and every term has coefficient modulus `1/(16n)`. If a group has at most `L_*` terms, Cauchy-Schwarz inside each group gives
\[
\sum_S|\widehat u_x(S)|^2
\le L_*\sum_{\xi,\eta}\frac1{(16n)^2}
\le \frac{L_*}{256}.
\]
Walsh orthogonality gives (2.4). Degree-three Bonami hypercontractivity gives (2.5), and `q=4` gives (2.6). Optimizing Markov's inequality using (2.5), with `q` of order `t^{2/3}`, gives (2.7). QED.

### Significance

This is a source-exact statement about the same Rademacher mask that defines the graph. It is not a Gaussian replacement and does not make the dependent physical Fourier coordinates independent. The involution `K` has converted the quadratic interpolation target into a uniformly controlled degree-three chaos before any nonlinear operation occurs.

---

# 3. New theorem: every mask bit has only `O(1/n)` influence on the preconditioned field

For a function `F(epsilon)` on the Boolean cube, let
\[
D_aF(\varepsilon)=\frac{F(\varepsilon)-F(\varepsilon^{(a)})}{2},
\qquad
I_a(F)=\mathbb E(D_aF)^2.
\tag{3.1}
\]

## Theorem P07-B.33 — low source-bit influence

Uniformly in odd `n`, physical site `x`, and pair index `a in M`,
\[
\boxed{
I_a(u(x))\le\frac{C}{n}
}
\tag{3.2}
\]
for an absolute constant `C`. Consequently
\[
\boxed{
\sum_{a\in M}I_a(u(x))\le C.
}
\tag{3.3}
\]

### Proof

In the Walsh expansion of `u(x)`, `I_a` is the sum of squared coefficients of reduced monomials containing `epsilon_a`. A raw summand in (2.2) can reduce to such a monomial only if at least one of the pair classes `[xi]`, `[eta]`, `[xi-eta]` equals `a`. There are at most `2n` choices with `[xi]=a`, at most `2n` with `[eta]=a`, and at most `2n` with `[xi-eta]=a`. Thus at most `6n` raw summands can enter groups whose reduced monomial contains `a`. Applying the same fiber Cauchy-Schwarz bound as above,
\[
I_a(u(x))
\le L_*\frac{6n}{(16n)^2}
=O(n^{-1}).
\]
Summing over `|M|<n/2` gives (3.3). QED.

This low-influence property is absent from an arbitrary element of the selected Fourier subspace and is therefore genuinely target-specific.

---

# 4. The initial weighted-kurtosis obligation is now proved

Write
\[
\sigma_0(D)^2:=\|u\|_2^2,
\qquad
\kappa_0(D):=\frac{\|u\|_4^4}{\sigma_0(D)^4}.
\tag{4.1}
\]
The preceding P07-B quadratic-energy concentration theorem proved, with `O_epsilon(n^{-1})` failure, that the selected transverse quadratic target has nonvanishing squared norm tending to a positive constant (`1/512` in that normalization). By Parseval this selected transverse energy is a sub-energy of `u=K w`, because `K` preserves every nonzero Fourier magnitude. Hence there is an absolute `c_0>0` such that
\[
\boxed{
\Pr_D\{\sigma_0(D)^2<c_0\}=O(n^{-1}).
}
\tag{4.2}
\]
Call its complement `G_n`.

Combining (2.6) with (4.2) gives
\[
\boxed{
\mathbb E_D\left[
\kappa_0(D)\sigma_0(D)^2\,\mathbf1_{\mathcal G_n}
\right]
=
\mathbb E_D\left[
\frac{\|u\|_4^4}{\|u\|_2^2}\,\mathbf1_{\mathcal G_n}
\right]
\le \frac{26}{c_0}.
}
\tag{4.3}
\]
Thus the weighted-kurtosis statement sought in the previous report is **proved at the preconditioned initial state**, with an `O(n^{-1})` exceptional event already smaller than the `O(n^{-1/2})` scale needed for the expectation theorem.

This is not merely an annealed `L^4` estimate: the denominator that made `GQOK4` difficult is controlled by the already-proved target-energy concentration.

---

# 5. Self-normalized clipping gives deterministic contraction at bounded expected first cost

For `b>0`, define
\[
C_b(t)=\operatorname{sgn}(t)\min\{|t|,b\},
\qquad
R_b(t)=t-C_b(t).
\tag{5.1}
\]
For any nonzero field `v`, let
\[
\sigma(v)=\|v\|_2,
\qquad
b_A(v)=A\frac{\|v\|_4^2}{\|v\|_2}
=A\sqrt{\kappa(v)}\,\sigma(v),
\qquad A>1.
\tag{5.2}
\]
Since
\[
|R_b(t)|^2\le \frac{|t|^4}{b^2},
\]
we obtain the deterministic estimate
\[
\boxed{
\|R_{b_A(v)}(v)\|_2
\le \frac1A\|v\|_2.
}
\tag{5.3}
\]
No probabilistic assumption is used here.

Apply this to `v=u` on `G_n`. The bounded correction
\[
h_0=C_{b_A(u)}(u)
\tag{5.4}
\]
has exact interpolation pairing up to the tail, while (4.3) and Cauchy-Schwarz give
\[
\boxed{
\mathbb E_D[b_A(u)\mathbf1_{\mathcal G_n}]
\le
A\left(
\mathbb E_D\frac{\|u\|_4^4}{\|u\|_2^2}\mathbf1_{\mathcal G_n}
\right)^{1/2}
=O_A(1).
}
\tag{5.5}
\]
The tail contracts by the fixed factor `A^{-1}` on **every good mask**.

Now define
\[
v_1:=Q_D\mathcal K R_{b_A(u)}(u),
\tag{5.6}
\]
where `Q_D` is the free gauge projection from the previous report. Since both `Q_D` and `K` are `L^2` contractions,
\[
\boxed{
\|v_1\|_2\le A^{-1}\|u\|_2.
}
\tag{5.7}
\]
The exact interpolation identity is
\[
\boxed{
\langle f_z,w\rangle
=\langle f_z,h_0\rangle+\langle f_z,v_1\rangle.
}
\tag{5.8}
\]
Thus the first nonlinear correction now has both **bounded expected cost** and **deterministic per-mask `L^2` contraction** on the source-good event.

Compared with the previous `GQOK4` formulation, one no longer needs a numerical inequality `C_4<A^2` to force contraction: the threshold itself is self-normalized and forces contraction. What remains is only summability of the future expected clipping costs.

---

# 6. Deterministic clipping leaves a quantitatively low-influence tail

For the next decoupling attack it is useful to keep a deterministic threshold `L` instead of the self-normalized one. Put
\[
r_L(x)=R_L(u(x)).
\tag{6.1}
\]
Because `R_L` is one-Lipschitz,
\[
I_a(r_L(x))\le I_a(u(x)).
\]
The cubic structure gives a stronger tail-weighted estimate. If both `|u(epsilon)|` and `|u(epsilon^(a))|` are at most `L`, then `D_a r_L=0`; otherwise
\[
|D_a r_L|\le |D_a u|.
\]
Moreover `D_a u` has Walsh degree at most two. Hence Bonami and Cauchy-Schwarz, together with the sub-Weibull tail (2.7), give absolute `c,C>0` such that for all sufficiently large fixed `L`,
\[
\boxed{
I_a(r_L(x))
\le \frac{C}{n}e^{-cL^{2/3}}.
}
\tag{6.2}
\]
Summing in `a` and averaging in `x`,
\[
\boxed{
\sum_{a\in M}\mathbb E_x I_a(r_L(x))
\le C e^{-cL^{2/3}}.
}
\tag{6.3}
\]
Similarly, layer-cake integration of (2.7) yields
\[
\boxed{
\mathbb E_D\|r_L\|_2^2
\le C(1+L^2)e^{-cL^{2/3}}.
}
\tag{6.4}
\]
Thus after one bounded correction of fixed cost `L`, both the residual energy and its total dependence on the source mask bits can be made arbitrarily small by choosing `L` to be a sufficiently large **absolute constant**, with no `n`-dependent loss.

This does not by itself prove the required interpolation theorem: a very rare, coherent same-mask recoupling could in principle turn a low-energy low-influence residual into a high-kurtosis next iterate. The next section isolates exactly that point.

---

# 7. Exact benchmark: with an independent Fourier multiplier, the `2 -> 4` problem is dimension-free

This subsection is a **comparison calculation only**. The independent multiplier below is not a valid source certificate because it does not fix the selected frequencies. It is introduced solely to identify how much of the remaining problem is caused by same-mask coupling.

Let `epsilon'_a` be an independent Rademacher family and let `K'` be the Fourier multiplier
\[
\widehat{\mathcal K' r}(\pm a)=\varepsilon'_a\widehat r(\pm a),
\qquad
\widehat{\mathcal K' r}(0)=0.
\tag{7.1}
\]
Fix any deterministic real even `r`. Write its normalized Fourier coefficients as
\[
\rho_a=\frac1n\widehat r(a),
\qquad a\in M.
\]
Then
\[
\mathcal K' r(x)=2\sum_{a\in M}\varepsilon'_a\rho_a\cos(2\pi ax/n).
\tag{7.2}
\]
Conditional Khintchine gives
\[
\mathbb E_{\varepsilon'}|\mathcal K'r(x)|^4
\le3\left(4\sum_a\rho_a^2\cos^2(2\pi ax/n)\right)^2.
\tag{7.3}
\]
Because `n` is odd, the doubled pair-frequencies `2a` remain distinct modulo sign, and cosine orthogonality gives
\[
\mathbb E_x\left(\sum_a q_a\cos^2(2\pi ax/n)\right)^2
=\frac14\left(\sum_aq_a\right)^2
+\frac18\sum_aq_a^2
\le\frac38\left(\sum_aq_a\right)^2.
\tag{7.4}
\]
Using Parseval, `2 sum_a rho_a^2 <= ||r||_2^2`. Therefore
\[
\boxed{
\mathbb E_{\varepsilon'}\|\mathcal K'r\|_4^4
\le\frac92\|r\|_2^4.
}
\tag{7.5}
\]
This holds for **every deterministic residual `r`**, with no sparsity or additive-energy hypothesis.

Equation (7.5) shows that the Fourier `L^4` geometry itself is not the obstruction. If the multiplier signs were fresh, the required fourth-moment smoothing would be automatic with an absolute constant. The actual problem is precisely that the multiplier `epsilon_a` is the same bit that helped create the residual `r=r(epsilon)`.

---

# 8. The remaining exact lemma is now a same-mask recoupling statement

For a random residual field `r=r(epsilon)`, write
\[
\rho_a(\varepsilon)=\frac1n\widehat r(a).
\]
Decompose each matched Fourier coefficient with respect to its own source bit:
\[
\rho_a=A_a+\varepsilon_a B_a,
\tag{8.1}
\]
where `A_a,B_a` do not depend on `epsilon_a`. Then
\[
\varepsilon_a\rho_a=\varepsilon_aA_a+B_a.
\tag{8.2}
\]
The second term is the exact **self-recoupling bias** absent from the independent benchmark. Moreover
\[
\mathbb E|B_a|^2
\le \mathbb E|D_a\rho_a|^2.
\tag{8.3}
\]
By Parseval and (6.3), the deterministic cubic tail satisfies
\[
\boxed{
\sum_{a\in M}\mathbb E|B_a|^2
\le C e^{-cL^{2/3}}.
}
\tag{8.4}
\]
Thus the directly matched part of the same-mask dependence is already exponentially small after one constant-cost cubic clipping.

The only surviving issue is whether **off-diagonal dependence cycles** — dependence of `rho_a` on bits `epsilon_b`, `b ne a`, which can interact around quartic additive relations — can coherently defeat the independent estimate (7.5).

This isolates the next theorem-sized obligation.

## Missing lemma `SMR4` — same-mask recoupling for the low-influence clipping orbit

For the actual residuals generated after cubic preconditioning and bounded clipping, prove an absolute-constant comparison of the form
\[
\boxed{
\mathbb E_D\|Q_D\mathcal K_D r\|_4^4
\le
C\,\mathbb E_{D,D'}\|\mathcal K_{D'}r(D)\|_4^4
+C\,\mathfrak I_{\rm match}(r)^2,
}
\tag{SMR4}
\]
where `D'` is an independent multiplier copy used only on the comparison side and
\[
\mathfrak I_{\rm match}(r)
:=\left(\sum_a\mathbb E|D_a\rho_a|^2\right)^{1/2}.
\tag{8.5}
\]
A slightly stronger version may use the full Boolean Dirichlet energy in place of `I_match`; (6.3) still makes that quantity exponentially small after fixed cubic clipping.

By (7.5), `SMR4` reduces the actual fourth moment to a constant multiple of `E||r||_2^4` plus an exponentially small recoupling error. The first iterate already has bounded weighted kurtosis by Section 4. Repeating the self-normalized clipping step then gives deterministic `L^2` contraction; a corresponding energy-regularity estimate on the resulting orbit makes the clipping costs summable in expectation. This yields
\[
\mathbb E[K_D^{(2)}\mathbf1_{\mathcal B_n}]=O(1),
\]
and the previous adaptive positive quadratic certificate then gives
\[
\boxed{\mathbb E\vartheta(G_n)=O(\sqrt n).}
\]
Thus `SMR4` plus the orbit energy-regularity step would remove the entire published `sqrt(log log n)` loss. This implication is **CONDITIONAL**; `SMR4` is not claimed proved here.

The important reduction is that the missing statement is no longer a generic same-mask `L^4` estimate. The independent `2 -> 4` theorem is exact, the matched self-bias is exponentially small after one absolute-cost clip, and only quartic off-diagonal dependence cycles remain.

---

# 9. Next concrete attack

The next run should expand the fourth moment of the actual same-mask transform in normalized Fourier coordinates and compare term-by-term with (7.3). Every contribution is indexed by an additive quadruple
\[
a+b=c+d
\]
and a Walsh parity constraint. Split these contributions into:

1. **paired terms**, identical to the independent Khintchine pairings and already bounded by `(9/2)||r||_2^4`;
2. **matched terms**, where a multiplier bit appears inside its own coefficient, controlled by (8.4);
3. **genuine dependence cycles** of length at least two among distinct frequency bits.

For the deterministic cubic tail `r_L`, each coordinate influence is `O(n^{-1}e^{-cL^{2/3}})`. The target is to charge every genuine cycle to at least two such influences. If this succeeds, the total cycle contribution is `O(e^{-cL^{2/3}})||r_L||_2^2` rather than an `n`-dependent loss. This is a finite combinatorial/Walsh calculation on the original source bits and does not require treating the physical Fourier coordinates as independent.

A proof of that cycle charge for the first clipped residual would already establish the first genuinely nonlinear instance of `SMR4`; the propagation question can then be attacked separately using the same influence bookkeeping.

---

# 10. Obligation ledger

**PROVED PARTIAL this run**

- Exact zero-cost cubic preconditioning `u=K(G^2/16)` for the transverse quadratic target.
- Uniform bounded fiber multiplicity of its Walsh expansion for every odd `n`.
- Uniform degree-three hypercontractive moment and sub-Weibull tail bounds.
- `O(1/n)` influence of every source mask bit at every physical site.
- Using the previously proved quadratic-energy concentration, the weighted-kurtosis condition is proved at the initial preconditioned state outside an `O(n^{-1})` event.
- Self-normalized clipping gives deterministic per-mask `L^2` contraction with bounded expected first clipping cost.
- Deterministic cubic clipping yields exponentially small residual energy and Boolean influence at fixed absolute cost.
- For a genuinely independent Fourier multiplier, the exact dimension-free estimate `E||K'r||_4^4 <= (9/2)||r||_2^4` holds for every deterministic even residual.
- The matched self-recoupling bias of the clipped cubic residual has exponentially small squared energy.

**CONDITIONAL**

- `SMR4` plus orbit energy regularity implies `Mean-QBI`, hence `E theta(G_n)=O(sqrt(n))` and removal of the source iterated-log loss.

**NOT CLAIMED**

- No full proof of Conjecture 18.
- No sharp leading constant `1`.
- No independent-coordinate model for the actual Fourier field.
- The independent multiplier in Section 7 is only a comparison device and is not itself a feasible source certificate.

**Complementary P07-A handoff**

P07-A's orthogonal-core scalar `S_D` and variance/influence criterion remain separate and stronger toward the sharp constant. The reusable lemma from this report is the source-bit statement: after one exact same-mask involution, the P07-B quadratic residual is a degree-three chaos with uniformly bounded Walsh fibers and `O(1/n)` individual influences. If P07-A encounters a transverse covariance correction generated by the same quadratic field, this low-influence fact may be imported without duplicating the primal/core-mass argument.
