# B15 — zero-valuation one-point family forces exponential cancellation in the physical height tilt

**Status:** **OPEN / PARTIAL. Full uniform-cube FEI remains OPEN / NOT PROVED.**

**Execution:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-context use entered this mathematics.

**Role / interface:** fleet01/B15, joint interface D (spectral magnitude/arithmetic remainder). This run attacks the negation of the most immediate next lemma from the preceding valuation-escort handoff: can the second-stage physical-height tilt, or either of its KL directions, be paid positively by folded influence after the valuation escort has been stripped? The answer is **no**, already on an explicit Boolean family with *zero carry depth everywhere*.

Scientific base before this run: master `a898d648224df38aafea65765f820ab32ac7b8d1`.

---

## 0. Other-account results consumed substantively

Two compatible peer results are used, not merely cited.

1. **fleet02/B15 valuation-tail majorization**, `20260921T170301Z-valuation-tail-majorization/REPORT.md`, blob `7633ed3dca15ea17d4c17af94e621f4ab3745691`. It proves, for packet carry depth `r_a` and folded marginals `q_1^down >= ... >= q_n^down`,

   \[
   \mathbf E_p(r_a-m+1)_+\le 2\sum_{k=m}^n q_k^\downarrow,
   \]

   hence `R=E_p r_a <=2J`. The family below has `r_a=0` for **every** packet, so this entire paid valuation ledger vanishes identically. Therefore any surviving obstruction is genuinely in the physical unequal-magnitude core, exactly the residual interface D asks us to isolate.

2. **fleet03/B15 real-restriction softmax current**, `20260921T211127Z-real-restriction-softmax-credit/REPORT.md`, blob `b79c3bd39fa798f73edeb169056c0711ded90cb6`. It defines

   \[
   \mathcal W(f)=\frac12\sum_{\{S,S\triangle\{i\}\}}
   \min(p_S,p_{S\triangle\{i\}})
   \log_2\frac{p_S+p_{S\triangle\{i\}}}{2\min(p_S,p_{S\triangle\{i\}})}
   \]

   (sum over Fourier-cube coordinate edges) and shows that a bound `mathcal W <= kappa J` would imply full FEI with a finite constant. I compute this statistic exactly on the same family below. It stays *tiny*, even though the global physical-height Gibbs tilt has exponentially unpayable KL divergences. This separates the promising real-restriction statistic from the bad global height-tilt statistic.

The fleet02 Jeffreys-recombination identity from `20260921T210305Z-jeffreys-tail-crossing/REPORT.md` is also used conceptually: in a genuine source recombination fibre the raw debit decomposes as a tilted geometric gap plus half a Jeffreys divergence. The theorem below shows that one must **not** promote that local identity into a global positive Jeffreys bound for the entire `p^val -> q^N` physical-height tilt.

---

## 1. The explicit Boolean family

For `n>=3`, put `N=2^n` and define

\[
 f_n(0)=1,\qquad f_n(x)=-1\quad(x\ne0).
\]

With the standard Walsh characters,

\[
 \widehat f_n(\varnothing)=-\frac{N-2}{N},
 \qquad
 \widehat f_n(S)=\frac2N\quad(S\ne\varnothing).
 \tag{1.1}
\]

Thus there are exactly two distinct magnitude packets:

\[
 A=\frac{N-2}{N}\quad\text{with multiplicity }1,
 \qquad
 b=\frac2N\quad\text{with multiplicity }N-1.
 \tag{1.2}
\]

Their spectral packet masses are

\[
 p_L=\frac{(N-2)^2}{N^2},
 \qquad
 p_S=\frac{4(N-1)}{N^2}.
 \tag{1.3}
\]

### Lemma 1.1 — both signed packet carry depths are exactly zero

For the large packet the signed mask is the constant `-1`, hence `r_L=0`.
For the small packet all signs are positive and

\[
 V_S(x)=\sum_{T\ne\varnothing}\chi_T(x)
       =N\mathbf 1_{\{x=0\}}-1.
\]

Its values are `N-1` at zero and `-1` elsewhere; both are odd because `N` is even. Hence `r_S=0`.

Therefore

\[
 \boxed{R(f_n)=0,\qquad p^{\rm val}=p.}
 \tag{1.4}
\]

This is the decisive point: **valuation tails have nothing left to pay on this family**.

---

## 2. Exact second-stage physical-height tilt

Write packet height `h=log_2(1/a)`. Then

\[
 h_L=\log_2\frac{N}{N-2},
 \qquad h_S=n-1.
 \tag{2.1}
\]

The previous fleet01/B15 handoff factors the arithmetic Gibbs law as

\[
 q_a^N=\frac{p_a^{\rm val}4^{h_a}}
              {\mathbf E_{p^{\rm val}}4^h}.
\]

Here `p^val=p`, and because `p_a 4^{h_a}` is exactly the packet multiplicity,

\[
 Z_h:=\mathbf E_p4^h=1+(N-1)=N,
 \tag{2.2}
\]

and therefore

\[
 \boxed{q_L^N=\frac1N,\qquad q_S^N=\frac{N-1}{N}.}
 \tag{2.3}
\]

So the height tilt almost completely reverses the packet law: spectral mass is almost all on the large coefficient, while `q^N` is almost all on the sea of tiny coefficients.

---

## 3. PROVED obstruction: neither KL direction, nor Jeffreys, is influence-payable

All divergences use base-2 logs. Because

\[
 q^N_a=\frac{p_a4^{h_a}}{Z_h},
\]

we have the exact tilt identities

\[
 K_\to:=D_2(p\|q^N)=\log_2 Z_h-2\mathbf E_p h,
 \tag{3.1}
\]

\[
 K_\leftarrow:=D_2(q^N\|p)=2\mathbf E_{q^N}h-\log_2 Z_h.
 \tag{3.2}
\]

Since `R=0`, the Fourier entropy is simply

\[
 H(f_n)=2\mathbf E_p h.
\]

Hence

\[
 \boxed{K_\to=n-H(f_n).}
 \tag{3.3}
\]

Also (2.1)-(2.3) give

\[
 \boxed{
 K_\leftarrow
 =n-2-\frac{2n-2}{N}
   +\frac2N\log_2\frac{N}{N-2}.
 }
 \tag{3.4}
\]

The influence is exact. For every coordinate `i`, exactly `N/2` nonempty Fourier sets contain `i`, each with squared coefficient `4/N^2`, so

\[
 \operatorname{Inf}_i(f_n)=\frac2N.
\]

For `n>=3` this is already the folded marginal. Therefore

\[
 \boxed{J(f_n)=I(f_n)=\frac{2n}{N}.}
 \tag{3.5}
\]

Finally,

\[
 H(f_n)
 =2\frac{(N-2)^2}{N^2}\log_2\frac{N}{N-2}
 +\frac{8(N-1)}{N^2}(n-1).
 \tag{3.6}
\]

As `n->infinity`,

\[
 \frac{H(f_n)}{I(f_n)}\to4,
 \tag{3.7}
\]

whereas

\[
 \boxed{
 \frac{K_\to}{I(f_n)}\sim\frac N2,
 \qquad
 \frac{K_\leftarrow}{I(f_n)}\sim\frac N2,
 \qquad
 \frac{K_\to+K_\leftarrow}{I(f_n)}\sim N.
 }
 \tag{3.8}
\]

### Consequence

There is **no** dimension-independent constant `C` for any of

\[
 D_2(p^{\rm val}\|q^N)\le C J,
 \qquad
 D_2(q^N\|p^{\rm val})\le C J,
 \qquad
 J_2(p^{\rm val},q^N)\le C J.
 \tag{3.9}
\]

This remains false even when **all packet valuations are zero**. Therefore the second-stage height tilt cannot be controlled by adding a positive forward, reverse, or symmetrized information budget after the valuation escort.

This is a genuine Boolean counterexample family to those proposed universal lemmas, not a synthetic packet law.

---

## 4. The cancellation that a correct D proof must preserve is exponentially delicate

Equation (3.3) can be rearranged as

\[
 \boxed{
 \log_2 Z_h-D_2(p\|q^N)=H(f_n).
 }
 \tag{4.1}
\]

On this family the two terms on the left are both order `n`:

\[
 \log_2Z_h=n,
 \qquad
 D_2(p\|q^N)=n-o(1),
\]

while their difference is only order `n/N`:

\[
 H(f_n)\sim\frac{8n}{N}.
\]

Equivalently,

\[
 \frac{\log_2Z_h-D_2(p\|q^N)}{\log_2Z_h}
 =\frac{H(f_n)}n
 \sim\frac8N.
 \tag{4.2}
\]

Thus the negative forward-KL term is not a decorative improvement. A valid global arithmetic argument must retain cancellation between the positive partition term and this negative information credit to **exponentially small relative scale** on a perfectly legitimate Boolean family.

This sharpens the fleet02 directive “preserve and spend negative information credits”: separate positive estimates of `log Z_h`, forward KL, or reverse KL cannot possibly close interface D.

It also explains why importing the fleet02 local Jeffreys identity wholesale into the global height tilt is unsafe. Their Jeffreys term is part of a source-weighted recombination debit that can sometimes itself be paid. Here the global height-tilt Jeffreys divergence is order `n` while the entire FEI budget is order `n/N`.

---

## 5. The fleet03 real-restriction softmax current survives this obstruction

Now evaluate the compatible fleet03 statistic `mathcal W` exactly on the same family.

For a fixed coordinate `i`, Fourier edges pair `T` with `T union {i}`. Every pair except `T=emptyset` joins two small coefficients of equal magnitude `2/N`, and therefore contributes zero to `W_i`. The unique unequal pair has squared masses

\[
 P=\frac{(N-2)^2}{N^2},\qquad s=\frac4{N^2}.
\]

Hence

\[
 W_i(f_n)
 =\frac{2}{N^2}
   \log_2\frac{N^2-4N+8}{8},
\]

and

\[
 \boxed{
 \mathcal W(f_n)
 =\frac{2n}{N^2}
   \log_2\frac{N^2-4N+8}{8}.
 }
 \tag{5.1}
\]

Using (3.5),

\[
 \boxed{
 \frac{\mathcal W(f_n)}{J(f_n)}
 =\frac1N\log_2\frac{N^2-4N+8}{8}
 \longrightarrow0.
 }
 \tag{5.2}
\]

So the fleet03 minority-weighted real-restriction current **does not inherit** the catastrophic global height-tilt divergence. In fact this r=0 family becomes asymptotically easy for `mathcal W/J` even though both global KL directions blow up by a factor `Theta(N)` relative to influence.

This is evidence for a precise methodological separation:

- global `p^val -> q^N` positive-divergence payment is false;
- local real-restriction minority weighting removes the giant packet-count tilt;
- the hard remaining theorem should therefore couple the physical-height remainder to **actual restriction/recombination geometry and its negative credits**, not to the global arithmetic Gibbs law in isolation.

No universal `mathcal W <= (3/4)J` theorem is claimed here.

---

## 6. Why valuation tails cannot repair this example

The consumed fleet02 stop-loss theorem controls every increasing functional of `r_a`. Here

\[
 r_L=r_S=0.
\]

Therefore every positive-depth tail is exactly zero:

\[
 \Pr(r_a\ge m)=0\qquad(m\ge1),
\]

and every valuation-tail payment vanishes. Nevertheless the physical heights differ by almost `n`:

\[
 h_S-h_L=n-1-\log_2\frac{N}{N-2}=n-1-o(1).
\]

Thus no inequality of the form “large physical height gap forces large valuation depth” can hold, even spectrally weighted. The unequal-magnitude/carry separation is genuine, not an artifact of a weak estimate.

---

## 7. Literature boundary

Fresh primary-source checks on 21 September 2026 remain consistent with unrestricted FEI being open. Potapov, arXiv:2609.21563 (18 September 2026), proves the sharp constant `4` for plateaued functions and `2` for partially bent functions, not arbitrary unequal-magnitude spectra. González–MacManus–Pereyra, arXiv:2606.00246 (29 May 2026), develop a restriction/stopping-tree route and explicitly leave a universal restriction inequality as the missing step.

No novelty or priority claim is made for the elementary one-point Fourier calculation itself. The point of this report is its use as an exact stress test for the **new two-stage valuation/height factorization** and for the competing KL/softmax proof interfaces.

The old conjecture that Hod's `beta(1/2)` is the sharp universal FEI constant remains retired: the recovered Numaro 18-variable example is already above it. Hod's constant remains relevant to the read-once subclass.

---

## 8. Full-problem status and next target

**Before:** OPEN. The valuation escort was information-paid, leaving the second-stage physical-height tilt plus negative credits.

**After:** OPEN. Three tempting positive second-stage bounds are now rigorously refuted on a zero-valuation Boolean family:

1. forward height-tilt KL `<= C J`;
2. reverse height-tilt KL `<= C J`;
3. height-tilt Jeffreys `<= C J`.

Their ratios grow exponentially in `n`, while `H/I -> 4`. The forward KL must remain as a **negative credit** canceling the positive height partition term; the fleet03 real-restriction softmax current avoids this obstruction and tends to zero relative to `J` on the same family.

**Next B15 target:** work directly with a restriction-local or recombination-local *canceled* quantity. A viable candidate must keep `log Z - KL_forward` together (or an equivalent conditional-information difference) and must never introduce the full reverse KL of the global height tilt as a separately positive term. The cleanest next question is whether the canceled physical-height remainder can be represented as an integral of the fleet03 minority-weighted softmax currents plus valuation-tail-paid terms and a nonpositive conditional-KL correction.

Full FEI remains OPEN.
