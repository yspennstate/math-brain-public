# B14 — hereditary moving-erasure selector for the full restriction closure of width-two tribes

**Run:** `B14-20260921T131405Z-r11`  
**Role:** FEI erasure and selector proof  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / PROVED family-level selector theorem. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Priority:** publication priority **UNVERIFIED**; no novelty claim is made.

This run implements the owner’s creative FEI instruction and the active sprint assignment for fleet04/B14: prove or refute an existential restriction selector on a growing family. It starts from the fresh P03 state, in particular the exact restriction identity, the restriction-critical descendant lemma, and the newer strong-concavity repair
\[
\Delta_iH=B_i+JS_i,\qquad
JS_i\le j(M_i)\le j(p_i),
\]
for \(p_i=\operatorname{Inf}_i(f)\le1/2\), where
\[
j(t)=1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right).
\]
The previous B14 run showed that the older fixed erasure target is actually false on width-two tribes at \(s=8\), while the moving target \(B_i+j(p_i)\le Cp_i\) survives there. The new result below upgrades that one state to the **entire hereditary physical-restriction closure** of the family.

The unrestricted FEI numerical target \(6.4547837\) is no longer current: the fresh owner entry records a July-2026 balanced monotone seed with \(H/I>6.521845710923046575\). The theorem below is family-specific and does not make a claim about the sharp unrestricted constant.

## 1. The hereditary family

Let
\[
T_s=\bigvee_{r=1}^s (x_{2r-1}\wedge x_{2r})
\]
be width-two tribes. Every nonconstant physical restriction of some \(T_s\), after deleting irrelevant coordinates, is of the form
\[
F_{a,b}=x_1\vee\cdots\vee x_a\vee(y_1\wedge z_1)\vee\cdots\vee(y_b\wedge z_b)
\tag{1}
\]
for integers \(a,b\ge0\), not both zero. Indeed, restricting one input of an intact pair either kills that clause or turns it into a singleton; a satisfied singleton makes the state constant.

Put
\[
q=2^{-a}(3/4)^b,
\]
the probability that no clause in (1) is satisfied. For the usual \(\{\pm1\}\)-encoding, the empty Fourier coefficient has square \((1-2q)^2\). Every nonempty Fourier coefficient meeting exactly \(m\) intact pair-blocks has squared magnitude
\[
4q^2\,9^{-m}.
\tag{2}
\]
The presence or absence of a singleton variable changes only the sign, not the magnitude, in (2).

## 2. Exact restriction formulas depend on one influence parameter

Assume first that \(b\ge1\) and choose either coordinate \(i\) in an intact pair. Its influence is
\[
p=\operatorname{Inf}_i(F_{a,b})=\frac12\,2^{-a}(3/4)^{b-1}.
\tag{3}
\]
On the erased Fourier fibres for \(i\):

- when its mate is present, the two fibre masses are equal;
- when its mate is absent and the residual label is nonempty, the two masses are in ratio \(9:1\);
- the empty fibre has masses \((1-3p)^2\) and \(p^2\).

Consequently the exact erasure entropy is
\[
B_{\rm pair}(p)=p+A_B\left(\frac92p-9p^2\right)+F((1-3p)^2,p^2),
\tag{4}
\]
where
\[
A_B=\frac{10}{9}h_2(1/10),\qquad
F(x,y)=(x+y)h_2\!\left(\frac{y}{x+y}\right).
\]
This is the same scalar formula previously derived for the symmetric root \(T_s\), but (2) proves that it remains exact after **arbitrary physical restrictions** that produce any \(F_{a,b}\).

If \(b=0\) and \(a\ge2\), choose a singleton coordinate. Its influence is \(p=2^{1-a}\), and all nonempty erased fibres have equal masses. Therefore
\[
B_{\rm sing}(p)=2p-2p^2+F((1-p)^2,p^2).
\tag{5}
\]

A targeted direct Walsh calculation in this run checked seven mixed states \(F_{a,b}\) against the closed decrement formulas; the maximum absolute discrepancy was \(1.23\times10^{-15}\). This finite check supports the algebra only; the formulas above are proved directly from the product Fourier coefficients.

## 3. Low-influence pair states satisfy the repaired moving selector

The inherited B14 strong-concavity theorem gives
\[
JS_i\le j(p)\le c_*\left(p-\frac{p^2}{3}\right),\qquad c_*=\frac2{\ln2}.
\tag{6}
\]
Also, for \(x,y\ge0\),
\[
F(x,y)=y\log_2(1+x/y)+x\log_2(1+y/x)
\le y\log_2(1+x/y)+\frac{y}{\ln2}.
\tag{7}
\]
For \(0<p\le81/512\), \((1-3p)^2\le1\). Combining (4), (6), and (7),
\[
\frac{\Delta_iH}{p}\le\frac{B_{\rm pair}(p)+j(p)}p\le G(p),
\tag{8}
\]
where
\[
G(p)=1+A_B\!\left(\frac92-9p\right)+c_*\left(1-\frac p3\right)+p\log_2(1+p^{-2})+\frac p{\ln2}.
\tag{9}
\]
The key point is that this one-variable envelope has the exact concavity certificate
\[
G''(p)=\frac{2(p^2-1)}{\ln2\,p(1+p^2)^2}<0\qquad(0<p<1).
\tag{10}
\]
Take the rational point \(p_0=173/2000\). Outward interval evaluation gives
\[
G(p_0)\in[6.4781048235915905,6.4781048235915986],
\]
\[
G'(p_0)\in[0.0000477384131665,0.0000477384131826].
\]
Because a concave function lies below every tangent and this tangent has positive slope, for the whole interval \(0<p\le81/512\),
\[
G(p)\le G(p_0)+G'(p_0)\left(\frac{81}{512}-p_0\right)<6.478108246585007.
\tag{11}
\]
Hence every such low-influence intact-pair coordinate obeys
\[
\boxed{\Delta_iH<6.478109\,p.}
\tag{12}
\]
This is a mass-weighted erasure proof: it keeps \(B_i\) exact and only upper-bounds the recombination term.

## 4. Low-influence singleton states are easier

From (5)–(7),
\[
\frac{\Delta_iH}{p}\le G_{\rm sing}(p):=2-2p+c_*\left(1-\frac p3\right)+p\log_2(1+p^{-2})+\frac p{\ln2}.
\tag{13}
\]
This has the same negative second derivative as (10). At \(p=1/8\), interval evaluation gives
\[
G_{\rm sing}(1/8)<5.448298351776859,\qquad G_{\rm sing}'(1/8)>1.662266694856250.
\]
Since the derivative of a concave function decreases with \(p\), it is positive throughout \(0<p\le1/8\). Therefore
\[
\boxed{G_{\rm sing}(p)\le G_{\rm sing}(1/8)<5.448299.}
\tag{14}
\]

## 5. The discrete influence gap closes the high-influence states

The inherited exact concave restriction cap is
\[
\Delta_iH\le\Psi(p_i),\qquad \kappa(p):=\Psi(p)/p\text{ decreases on }(0,1/2].
\tag{15}
\]
An interval evaluation at \(3/16\) gives
\[
\kappa(3/16)<6.385275938720897<6.478109.
\tag{16}
\]
For a pair coordinate,
\[
p=2^{-a-1}(3/4)^{b-1}.
\]
The allowed values have a gap:
\[
p\ge3/16\quad\text{or}\quad p\le81/512.
\tag{17}
\]
Indeed, for \(a=0\) the last high value is \(27/128\) and the next is \(81/512\); for \(a=1\) the last high value is \(3/16\) and the next is \(9/64\); for \(a\ge2\), \(p\le1/8\).

For a singleton-only state, \(p=2^{1-a}\), so, once at least two variables remain,
\[
p\ge1/4\quad\text{or}\quad p\le1/8.
\tag{18}
\]
Thus every nonterminal state is covered: a high-influence chosen coordinate is paid by (15)–(16), while the low-influence coordinate is paid by (12) or (14).

## 6. Hereditary selector theorem

### Theorem

For every nonconstant physical restriction descendant \(g\) of every width-two tribes function, if \(g\) has at least two relevant variables then there exists a relevant physical coordinate \(i\) such that
\[
\boxed{\Delta_iH(g)\le6.478109\,\operatorname{Inf}_i(g).}
\tag{19}
\]
More concretely:

- if an intact pair remains, either coordinate of any intact pair satisfies (19);
- if no intact pair remains, the state is an OR of singleton literals and any singleton satisfies (19);
- with one relevant variable, the Fourier entropy is zero and restriction induction stops.

Therefore ordinary physical-restriction induction compiles (19) to
\[
H(g)\le6.478109\,I(g)
\tag{20}
\]
throughout this hereditary class.

Equation (20) is **not** an improved class entropy bound: the current read-once certificate already proves \(H\le6.4573I\) on the larger read-once class. The new content is route-specific: the **potential-free / moving-erasure restriction selector itself is hereditary on the whole width-two-tribes restriction tree**, even though the earlier fixed erasure target was refuted by the \(s=8\) root.

That is exactly the sort of stability the unrestricted restriction-induction route needs: the hard family does not merely have one good root coordinate; all of its descendants continue to expose a paying coordinate under the repaired mass-weighted erasure rule.

## 7. What this does not prove, and next target

Full FEI remains **OPEN**. This theorem handles an infinite hereditary read-once family and cannot be promoted to a universal selector. In particular, it does not rule out a restriction-critical non-read-once core.

The next nonredundant B14 target is to identify a structural property weaker than the explicit product Fourier law (2), but stable under arbitrary Boolean restrictions, that still forces either
\[
B_i+j(M_i)\le C p_i
\]
for one coordinate, or a block analogue with a summable influence cost.

A natural candidate is a quantitative near-product fibre condition: (9) only needs control of the exceptional empty fibre plus a fixed ratio on the remaining fibres. The current all-shift Boolean orthogonality and block prediction-error results may provide a way to replace the exact \(9:1\) ratio by a mass-weighted dispersion term. Any attempted generalization must preserve the known counterexample to every-prescribed-coordinate payment.

### Claim ledger

**PROVED here**
- the exact pair-coordinate formula (4) for every mixed restriction state \(F_{a,b}\);
- the exact singleton formula (5);
- the analytic low-pair envelope and concavity (8)–(11);
- the low-singleton bound (13)–(14);
- the hereditary selector theorem (19) for the complete physical-restriction closure of width-two tribes.

**COMPUTATIONAL SUPPORT**
- direct Walsh checks on seven mixed states, maximum discrepancy \(1.23\times10^{-15}\);
- interval enclosures for the scalar constants used in (11), (14), and (16).

**NOT CLAIMED**
- a universal selector;
- a better read-once \(H/I\) constant;
- a proof of full FEI;
- publication priority.
