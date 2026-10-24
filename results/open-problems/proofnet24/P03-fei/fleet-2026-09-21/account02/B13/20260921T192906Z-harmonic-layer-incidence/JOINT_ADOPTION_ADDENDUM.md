TASK: B13 ACCOUNT: account02 RUN: 2026-09-21T19:29:06.213374Z — joint-directive addendum: centered gated-majority no-go and mixed-curvature bank

# Directive adoption and partner

During this invocation the live common control advanced to `FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z`. This addendum implements its cross-account requirement rather than freezing the run at the earlier account02-only handoff.

**Consumed other-account result:** `account04/B18/20260921T191147Z-mixed-curvature-global-rigidity/REPORT.md`, immutable report blob `0e8c2cc28da81af8843b565cb47285684b164480` on the scientific lineage observed in this run.

The exact partner theorem used below is the mixed-derivative conservation law. For one Boolean function `f`, if `g_i=D_i f`,

\[
\kappa^{\rm phys}_{ik}
:=\mathbb E\bigl(g_i(x)-g_i(x+e_k)\bigr)^2,
\]

then

\[
\kappa^{\rm phys}_{ik}=\kappa^{\rm phys}_{ki}
=p^{\rm supp}_{ik}+4o_{ik},
\qquad
\sum_{k\ne i}\kappa^{\rm phys}_{ik}=4d_i,
\tag{A.1}
\]

where `d_i=sum_{k!=i} ||D_k g_i||_2^2`. This is a jointly realizable signed Boolean identity; the `4 o_ik` opposite-sign term cannot be discarded.

# 1. Strengthening the majority obstruction to a centered marker

The main report refuted a universal local harmonic-Palm estimate

\[
H(Q_i)\le A+B\kappa_i^{\rm harm}
\tag{A.2}
\]

using an odd-majority derivative with marker influence one. A character gauge can remove such a deterministic marker. The following strengthened family shows that this is **not** the reason (A.2) fails.

Let `n=2m+1` be odd and `h=Maj_n`. Introduce one gate bit `y` and define the ternary derivative row

\[
g(y,z)=1_{\{y=0\}}h(z).
\tag{A.3}
\]

It is an actual first derivative of a Boolean function: on the active gate fibres choose the two endpoint values to be `h(z),-h(z)`, and on the inactive gate fibres choose equal Boolean endpoint values. Hence the marker influence is exactly

\[
j=\mathbb E g^2=\frac12,
\tag{A.4}
\]

already in the folded/centered range.

The normalized squared spectrum of `g` is the product of a uniform Bernoulli gate-frequency bit `B` and the majority spectral law `A`. Put

\[
a:=\mathbb E\frac1{1+B+|A|}.
\tag{A.5}
\]

The harmonic marker mass is `r=ja`, and the harmonic residual mean is

\[
\kappa^{\rm harm}=a^{-1}-1.
\tag{A.6}
\]

For odd majority the first-level spectral mass satisfies `W_1>=1/2`. Restricting (A.5) to `|A|=1` gives

\[
a\ge W_1\left(\frac12\frac12+\frac12\frac13\right)
=\frac5{12}W_1
\ge\frac5{24}.
\tag{A.7}
\]

Therefore

\[
\boxed{\kappa^{\rm harm}\le\frac{19}{5}.}
\tag{A.8}
\]

In the harmonic row `Q`, the two groups `(B=0,|A|=1)` and `(B=1,|A|=1)` consist of `n` equal atoms each. Their combined `Q` mass is

\[
\alpha=\frac{5W_1}{12a}\ge\frac5{24},
\tag{A.9}
\]

because `a<=1`. Keeping only their entropy contribution yields

\[
\boxed{H(Q)\ge\alpha\log_2 n\ge\frac5{24}\log_2 n.}
\tag{A.10}
\]

Thus no finite constants `A,B` can make (A.2) hold even after requiring the marked coordinate to have folded influence exactly `1/2`. This closes the obvious gauge loophole in the main-report obstruction.

# 2. Applying the account04 mixed-curvature theorem: where the hidden resource went

For the same gated-majority row (A.3), direct product calculation gives

\[
d=\frac14+\frac12 I(h).
\tag{A.11}
\]

Since `j=1/2`, its sharp depth defect is

\[
\delta
=\frac dj-\frac12\log_2\frac1j
=I(h).
\tag{A.12}
\]

Hence the row can have bounded harmonic mean (A.8) and logarithmically growing harmonic-row entropy (A.10), while the account04/B18 joint Boolean bank sees an unbounded amount of transverse curvature:

\[
\boxed{
\sum_{k\ne i}\kappa^{\rm phys}_{ik}
=4d
=1+2I(Maj_n).
}
\tag{A.13}
\]

This is the exact incompatibility between the false B13 row-local closure and the partner's joint stability mechanism. The harmonic scalar `kappa_harm` forgets the transverse mixed-derivative resource; the jointly realizable signed curvature does not.

For arbitrary `f`, define

\[
a_i:=\frac{r_i}{p_i}
=\mathbb E\left[\frac1{|S|}\mid i\in S\right]
\quad(p_i>0).
\tag{A.14}
\]

The partner conservation law yields the exact **harmonically weighted mixed-curvature bank**

\[
\boxed{
\mathcal B_{\rm mix}
:=\sum_i a_i d_i
=\frac18\sum_{i\ne k}(a_i+a_k)\kappa^{\rm phys}_{ik}
}
\tag{A.15}
\]

and therefore, retaining the signed orientation term,

\[
\boxed{
\mathcal B_{\rm mix}
=\frac18\sum_{i\ne k}(a_i+a_k)
\bigl(p^{\rm supp}_{ik}+4o_{ik}\bigr).
}
\tag{A.16}
\]

Equation (A.16) is not a new profile assumption: it is forced by derivative commutation for one actual Boolean source. It is also not yet an FEI payment. No dimension-independent proof of `B_mix<=C I` or `R_inc<=C(I+B_mix)` is supplied here. In fact the account04 report already warns that the unweighted depth sum `sum_i d_i` is a second factorial spectral moment and need not be `O(I)`; the harmonic weights are precisely the new feature that would have to make a global estimate possible.

# 3. FULL-PROBLEM CHANGE / MECHANISM CHANGE after the live joint order

**FULL-PROBLEM CHANGE:** unchanged from the main report: full FEI remains OPEN. The proved universal reduction remains

\[
H(f)\le6.416127927200970\ldots\,I(f)+\mathcal R_{\rm inc}(f).
\]

The cross-account input does not supply a bound on `R_inc`.

**MECHANISM CHANGE:** the false local target is now refuted **inside the centered range**, and the hidden resource is localized to the genuinely joint signed curvature bank (A.16), not to another sign-free marginal profile. This consumes account04/B18's theorem in the argument and identifies the precise B13/B18 compatibility question.

**Shared missing implication:** derive either

\[
\mathcal R_{\rm inc}^{+}(f)
\le C_1 I(f)+C_2\mathcal B_{\rm mix}(f)
\quad\text{and}\quad
\mathcal B_{\rm mix}(f)\le C_3 I(f),
\]

or a restriction telescope in which the positive layer-incidence debt is eliminated while the mixed-curvature bank is spent without reuse. The second displayed pair is a target, not a theorem.

**Next recipient:** account04/B18 (joint derivative stability) and account01/B13 (joint marginal/Han constraints). The concrete handoff is the centered gated-majority obstruction (A.8)--(A.13) plus the exact weighted bank (A.15)--(A.16). Any proposed quantitative stability compiler should be tested against this family before asserting that a harmonic-row mean or sign-free support statistic controls the row entropy.
