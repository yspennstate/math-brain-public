# B18 — read-once-Gamma gate candidate refuted; exact balanced-excess reformulation of full FEI

**Outcome classification:** `CANDIDATE_REFUTED` for the live read-once-Gamma universal-gate candidate.  
**Full uniform-cube Friedgut--Kalai FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated GitHub sources were used, but no authenticated mathematical/cognitive brain retrieval was delivered into this reasoning context.

## 0. Source binding and the exact candidate attacked

The live owner target is the all-gate inequality from

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, current blob
`1c0596f786fccf542f1f9ea65cc728b2c21ddef5`:

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{G}
\]

For the read-once value-iteration potential with cap
\(C_0=\Gamma(1/2)=6.4548\), the gate-margin statistic is

\[
c_G(p)=\frac{-D_G(p)}{I(G;p)/4-p_{\rm out}(1-p_{\rm out})}.
\tag{0.1}
\]

The universal candidate under active owner control was that no Boolean gate asks for a margin larger than the two-input AND constraint.  The operational README says “minimum” once, but the source definition (0.1), the gate code, and the accompanying instruction “find a gate with \(c_G\) above the AND's” show that the relevant extremum is the **maximum**.

## 1. Exact named other-account result consumed

I substantively consumed

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T002607Z-readonce-gamma-counterexample/REPORT.md`, current blob
`e49efe403698395b700278d067c245c12a7b15eb`.

That report applies the gate formula to the source-valid published balanced monotone 18-variable seed already tracked in the FEI campaign.  It records

\[
I(G)=\frac{261}{128},
\tag{1.1}
\]

and the certified entropy interval

\[
6.776605309005978082519790221891882314787235038
\le H(G)\le
6.776605309005978082519790221891882314787235039.
\tag{1.2}
\]

At the all-unbiased bias vector this gives

\[
\frac{H(G)}{I(G)-1}
\ge
6.5218457109230465756581439729485784683666622922105\ldots
\tag{1.3}
\]

and therefore, for the current read-once potential,

\[
c_G(1/2,\ldots,1/2)
\ge
0.2681828436921863026325758917943138734666491688421\ldots,
\tag{1.4}
\]

more than sixty times the currently measured two-input AND margin
\(0.0043974201\ldots\).  The peer checker records the corresponding gate defect as strictly negative even after adding the full current AND margin.

Thus the active candidate

> “the read-once fixed-point \(\Gamma\) at cap 6.4548 is universal for all gates / the AND margin is maximal among all gates”

is **refuted at its stated scope**.  This does not refute the gate reformulation and does not refute FEI.

The rest of this report applies that counterexample rather than continuing the now-dead AND-extremality proof attempt.

## 2. New exact theorem: full FEI is equivalent to a balanced excess-influence inequality

For a Boolean function \(f\) on the uniform cube, write

\[
H(f)=-\sum_S \widehat f(S)^2\log_2\widehat f(S)^2,
\qquad
I(f)=\sum_S |S|\widehat f(S)^2.
\]

Call \(g\) **balanced** when \(\mathbb E g=0\), equivalently \(\widehat g(\varnothing)=0\).

### Theorem 2.1 — balanced-excess equivalence

For every finite \(C\), the following statements are equivalent.

1. **FEI(C):**
   \[
   H(f)\le C I(f)
   \quad\text{for every uniform-cube Boolean }f.
   \tag{2.1}
   \]

2. **Balanced excess inequality BEI(C):**
   \[
   \boxed{H(g)\le C\,[I(g)-1]}
   \quad\text{for every balanced Boolean }g.
   \tag{2.2}
   \]

Consequently, allowing the value \(+\infty\), the optimal constants satisfy

\[
\boxed{
C_{\rm FEI}
=
\sup_{\substack{g\ \mathrm{balanced}\\ I(g)>1}}
\frac{H(g)}{I(g)-1}.
}
\tag{2.3}
\]

Balanced dictators have \(I=1,H=0\) and obey (2.2) with equality; they are omitted only from the ratio notation.

### Proof: BEI(C) implies FEI(C)

Let \(f(x)\) be arbitrary and let \(y\) be one fresh unbiased bit.  In \(\{-1,+1\}\) notation define

\[
g(y,x)=y f(x).
\tag{2.4}
\]

Then \(g\) is balanced.  Fourier coefficients are shifted by the fresh coordinate:

\[
\widehat g(S\cup\{y\})=\widehat f(S),
\qquad
\widehat g(T)=0\ \text{if }y\notin T.
\tag{2.5}
\]

Therefore the squared spectral probabilities are unchanged, only every spectral set receives one extra element.  Hence

\[
H(g)=H(f),
\qquad
I(g)=I(f)+1.
\tag{2.6}
\]

Applying (2.2) to \(g\),

\[
H(f)=H(g)\le C[I(g)-1]=CI(f).
\]

This proves FEI(C).

### Proof: FEI(C) implies BEI(C)

Fix balanced \(g\), with \(a:=I(g)\).  If \(a=1\), the spectral law is supported on level one; Booleanity then gives a dictator/negated dictator and \(H(g)=0\), so (2.2) is trivial.  Assume \(a>1\).

Recursively self-compose \(g\) on disjoint fresh blocks.  Let \(g^{\circ m}\) denote the depth-\(m\) balanced composition, starting from a fresh balanced input at depth zero.  The standard exact balanced composition identities give

\[
I_m=a^m,
\qquad
H_m=H(g)\sum_{j=0}^{m-1}a^j
=H(g)\frac{a^m-1}{a-1}.
\tag{2.7}
\]

FEI(C) applied to every \(g^{\circ m}\) gives

\[
H(g)\frac{a^m-1}{a-1}\le C a^m.
\]

Divide by \(a^m\) and let \(m\to\infty\):

\[
H(g)\le C(a-1)=C[I(g)-1].
\]

Thus BEI(C) follows.  This proves the equivalence and (2.3).  \(\square\)

## 3. Spectral-sample form: FEI is entropy per excess degree above a singleton

Let \(S_g\) be the Fourier spectral sample of a balanced Boolean function, so

\[
\Pr(S_g=S)=\widehat g(S)^2.
\]

Balancedness means

\[
\Pr(S_g=\varnothing)=0.
\]

Therefore

\[
H(g)=H(S_g),
\qquad
I(g)-1=\mathbb E(|S_g|-1).
\]

Theorem 2.1 is exactly

\[
\boxed{
H(S_g)\le C\,\mathbb E(|S_g|-1)
\quad\text{for every balanced Boolean }g.
}
\tag{3.1}
\]

This is not an auxiliary weakening: (3.1) with one finite universal \(C\) is **equivalent to full FEI**.

It also exposes why the balanced 18-variable seed is decisive for the gate potential.  At the all-unbiased gate point, every \(\Gamma\)-value in (G) is the single number \(\Gamma(1/2)=C\).  No change in the shape of \(\Gamma\) away from \(1/2\) can compensate a cap below
\(H(G)/(I(G)-1)\).

Thus the peer report's alternative phrase that one might keep a lower cap and “compensate through a different shape” does **not** apply to this balanced-uniform obstruction.  Necessarily

\[
\boxed{
\Gamma(1/2)
\ge
\sup_{g\ \mathrm{balanced},\ I(g)>1}\frac{H(g)}{I(g)-1}
=C_{\rm FEI}.
}
\tag{3.2}
\]

Of course (3.2) is an identity/reformulation, not a proof that the supremum is finite.

## 4. New exact composition law for the balanced excess ratio

The balanced formulation has one useful closure property that the failed read-once-\(\Gamma\) candidate obscured.

Let \(G\) be a balanced Boolean outer gate.  Let \(f_1,\ldots,f_k\) be balanced Boolean functions on pairwise disjoint variable blocks, and form

\[
F=G(f_1,\ldots,f_k).
\tag{4.1}
\]

Since the child outputs are independent unbiased bits, the exact spectral composition identities are

\[
I(F)=\sum_{i=1}^k \operatorname{Inf}_i(G)\,I(f_i),
\tag{4.2}
\]

\[
H(F)=H(G)+\sum_{i=1}^k \operatorname{Inf}_i(G)\,H(f_i).
\tag{4.3}
\]

Write

\[
\delta(G)=I(G)-1,
\qquad
\delta_i=I(f_i)-1.
\]

Using \(\sum_i\operatorname{Inf}_i(G)=I(G)\), (4.2) gives the exact excess decomposition

\[
\boxed{
\delta(F)
=
\delta(G)+\sum_i\operatorname{Inf}_i(G)\,\delta_i.
}
\tag{4.4}
\]

Hence, whenever the denominators are positive and with zero-denominator dictator terms omitted,

\[
\boxed{
\frac{H(F)}{I(F)-1}
=
\frac{
\delta(G)\,\rho(G)
+
\sum_i \operatorname{Inf}_i(G)\,\delta_i\,\rho(f_i)
}{
\delta(G)+\sum_i \operatorname{Inf}_i(G)\,\delta_i
},
}
\tag{4.5}
\]

where

\[
\rho(h)=\frac{H(h)}{I(h)-1}.
\]

Thus the balanced excess ratio of a balanced disjoint composition is a **literal convex combination** of the outer and child ratios:

\[
\boxed{
\rho(F)\le
\max\{\rho(G),\rho(f_1),\ldots,\rho(f_k)\}.
}
\tag{4.6}
\]

In particular, recursive self-composition of one balanced gate preserves \(\rho\) exactly at every finite depth:

\[
\frac{H(g^{\circ m})}{I(g^{\circ m})-1}
=
\frac{H(g)}{I(g)-1}.
\tag{4.7}
\]

The ordinary ratio \(H/I\) of those compositions approaches the same number, which is the peer B15 lower-bound mechanism.

This means balanced disjoint composition itself can never manufacture a larger excess ratio than one of its atomic balanced constituents.  Any proof at the level of (3.1) may therefore focus its genuinely new work on balanced functions not already controlled by such a balanced functional decomposition.  This is a structural reduction only; it does not assert that every balanced Boolean function admits a nontrivial balanced decomposition.

## 5. Application to the live gate campaign

The source-valid 18-variable seed has

\[
I-1=\frac{133}{128},
\]

so (1.2) gives

\[
\rho(G)=\frac{H(G)}{I(G)-1}
\ge 6.5218457109230465756581439729485784683666622922105\ldots.
\tag{5.1}
\]

Therefore:

1. the read-once \(\Gamma\) cap \(6.4548\) is impossible universally;
2. the current read-once margin-adjusted cap near \(6.4559\) is also impossible universally;
3. no off-center reshaping of that \(\Gamma\) can fix this balanced-uniform gate while retaining a smaller cap;
4. the correct universal target is at least the balanced excess ratio in (5.1), and in fact the supremum of all such balanced excess ratios is **exactly the optimal FEI constant** by Theorem 2.1.

This decisively supersedes the current “AND is extremal among all gates for the read-once \(\Gamma\)” proof target.  It does **not** supersede the gate equivalence itself.

## 6. Exact old/new missing implication

**Old live missing implication (now refuted):**

> prove \(c_G\) for every Boolean gate is at most the two-input AND margin for the read-once fixed-point \(\Gamma\) at cap 6.4548.

**Refutation:** the source-valid balanced 18-variable gate has \(c_G\ge0.26818284369\ldots\), while the current AND floor is approximately \(0.0043974201\).

**New source-exact equivalent missing implication:**

> prove that
> \[
> \sup_{g\ \mathrm{balanced},\ I(g)>1}
> \frac{H(g)}{I(g)-1}<\infty.
> \tag{6.1}
> \]

By Theorem 2.1, (6.1) is neither weaker nor stronger than full FEI; it is exactly full FEI in balanced excess form.

The first structural simplification now proved is (4.6): balanced disjoint composition cannot increase the ratio.  The remaining hard case is the genuinely non-compositional balanced Boolean geometry.  No finite universal bound for that case is proved here.

## 7. Classification

**`CANDIDATE_REFUTED`.**

The specific universal read-once-\(\Gamma\)/AND-extremality candidate under live owner control is source-exactly false.  I also derived and proved the balanced-excess equivalence (Theorem 2.1) and the exact convex composition law (4.5), which give the replacement target after that refutation.

**Full FEI remains OPEN / NOT PROVED.**
