# B12 FEI spectral compression — depth-only bridge refuted; equality-rigidity route isolated

TASK: B12 ACCOUNT: account02 RUN: 2026-09-21T16:56:22.505070Z  
CURRENT WORK: spectral-prefix reverse data processing, Palm-row depth versus Boolean equality rigidity  
ROLE: FEI approach 1 — spectral-sample compression / sequential prediction  
EXECUTION: WITHOUT_VERIFIED_BRAIN  
STATUS: **FULL FEI REMAINS OPEN.** This run proves a new-to-this-track exact obstruction to the current depth-only bridge and an exact Boolean equality classification that removes that obstruction at zero defect. It does not prove a dimension-independent FEI constant or claim literature novelty for the underlying edge-isoperimetric facts.

## 0. Fresh state and complementary scope

I read the owner-prescribed FEI continuation in the required order (`TASKS_2026-09-21.md`, the read-once `REPORT.md`, `APPROACHES.md`), then the fresh P03 README and the newest B12/B13 dependencies. The active unrestricted lower bound remains above 6.521845710923046575, while the certified read-once theorem is a structured result only. The immediately preceding B12 run reduced the approach-1 bottleneck to terminal-to-prefix information loss and proved two Boolean Palm-row depth controls. B13's current one-point-defect work independently identifies the same family as saturating a block/isoperimetric scale, so this run concentrates on what equality of the B12 depth inequality really forces rather than duplicating B13's projection calculations.

FLEET_RULES moves used here were **#2 attack the negation first**, **#12 find what is conserved**, and **#18 say it in another language**. The negation attack constructs a non-Boolean subset law that satisfies all current scalar depth tests while losing unbounded information. The conserved quantity is the exact decomposition of depth defect into edge-isoperimetric slack plus internal-sign slack. The language change is from spectral-sample prediction to equality/stability in cube edge isoperimetry.

A current literature check found David Ellis, *Almost Isoperimetric Subsets of the Discrete Cube* (CPC 2011), which gives sharp stability toward subcubes near equality in the weak cube edge-isoperimetric inequality, and Ellis–Keller–Lifshitz's later biased/full stability work. Potapov's 18 September 2026 preprint proves FEI for Boolean plateaued functions with class constant 4, but not full FEI. I therefore make no priority claim for the equality/stability ingredients; the contribution here is their exact insertion into the B12 Palm-row obstruction.

## 1. Setup from the previous B12 run

Let
\[
p_B=\widehat f(B)^2,\qquad \lambda=I(f)=\sum_B |B|p_B.
\]
Under the size-biased experiment, draw
\[
\Pr(B^*=B)=\frac{|B|p_B}{\lambda},
\]
then choose \(X\) uniformly from \(B^*\). Put
\[
j_i=\operatorname{Inf}_i(f),\qquad \pi_i=\frac{j_i}{\lambda}.
\]
Given \(X=i\), write \(C=B^*\setminus\{i\}\) and \(Z=|C|\). The preceding B12 run proved, for the Boolean derivative slice
\[
g_i=\frac{f(x_i=1)-f(x_i=-1)}2\in\{-1,0,1\},
\]
that
\[
\Pr(C=D\mid X=i)=\frac{\widehat g_i(D)^2}{j_i}.
\tag{1}
\]
It also proved the all-scale hypercontractive Palm moment bound
\[
\mathbb E[t^Z\mid X=i]
\le j_i^{(1-t)/(1+t)},\qquad 0\le t\le1,
\tag{2}
\]
and, when \(j_i\le1/2\), the sharp mean-prefix estimate
\[
\mathbb E[|A|\mid X=i]=\frac12\mathbb E Z
\ge \frac14\log_2\frac1{j_i}.
\tag{3}
\]
Here \(A\) is the random predecessor set before \(X\). The open hope was that (2), (3), plus the exact subset/shadow consistency might already force a bounded reverse-data-processing loss.

This section disproves that hope.

## 2. A symmetric subset-law surrogate satisfies all current depth tests but loses unbounded information

Fix an integer \(k\ge2\), put
\[
d=k-1,\qquad n=k4^d,
\tag{4}
\]
and let \(p\) be the **uniform law on all \(k\)-subsets of \([n]\)**. This is an honest subset probability law and therefore satisfies every purely probabilistic shadow recurrence, reversibility identity, size-bias identity, and random-prefix consistency used by approach 1. It is not asserted to be the squared Fourier spectrum of a Boolean function.

Because \(|B|=k\) always, \(B^*=B\), \(X\) is uniform on \([n]\), and
\[
j_i=\Pr(i\in B)=\frac{k}{n}=4^{-d}=2^{-2d}.
\tag{5}
\]
Conditional on \(X=i\), \(C\) is a uniformly random \(d\)-subset of \([n]\setminus\{i\}\), hence
\[
Z\equiv d.
\tag{6}
\]

### 2.1 It satisfies the entire hypercontractive moment envelope (2)

Let \(0<t\le1\). The elementary logarithmic inequality
\[
-\ln t\ge 2\frac{1-t}{1+t}
\tag{7}
\]
and \(2\ge\ln4\) imply
\[
t\le 4^{-(1-t)/(1+t)}.
\]
Raising to the \(d\)-th power and using (5)--(6),
\[
\boxed{
\mathbb E[t^Z\mid X=i]=t^d
\le j_i^{(1-t)/(1+t)}.
}
\tag{8}
\]
The case \(t=0\) is immediate. Thus even the full one-parameter Palm hypercontractive bound cannot distinguish this surrogate from an admissible Boolean row.

### 2.2 It exactly saturates the sharp scalar mean-depth bound (3)

A uniformly random predecessor rank has mean \(d/2\), while
\[
\frac14\log_2\frac1{j_i}
=\frac14(2d)=\frac d2.
\tag{9}
\]
Therefore (3) holds with equality for every coordinate.

### 2.3 Nevertheless terminal-to-prefix information loss diverges

The terminal set gives
\[
I(X;B^*)=H(X)-H(X\mid B^*)
=\log_2 n-\log_2 k
=2d.
\tag{10}
\]
Condition on predecessor rank \(R=r\). Sampling a uniform \(k\)-set and then a uniform ordering is the same as taking the first \(k\) entries of a uniformly random permutation of \([n]\). Consequently, after observing the unordered prefix \(A\) of size \(r\), the next coordinate \(X\) is uniform on the \(n-r\) unseen coordinates. Hence
\[
H(X\mid A)
=\frac1k\sum_{r=0}^{k-1}\log_2(n-r),
\tag{11}
\]
and
\[
I(X;A)
=\log_2n-rac1k\sum_{r=0}^{k-1}\log_2(n-r).
\tag{12}
\]
Since \(n-k+1>n/2\), every summand in
\[
I(X;A)=\frac1k\sum_{r=0}^{k-1}\log_2\frac n{n-r}
\]
is below one bit. Thus
\[
I(X;A)<1,
\qquad
\boxed{
L:=I(X;B^*)-I(X;A)>2d-1=2k-3.
}
\tag{13}
\]
So \(L\to\infty\) even though the law obeys (2), saturates (3), and satisfies all generic subset/shadow identities.

**Conclusion.** No proof of bounded terminal-to-prefix loss can use only the current scalar Palm degree/tail controls plus generic subset-law consistency. It must use a genuinely Boolean **shape** constraint on the derivative Fourier rows.

## 3. Boolean equality in the mean-depth theorem is rigid

The surrogate above also shows exactly where scalar information was discarded. The same proof that gave (3) contains a rigid equality case.

Fix a genuine Boolean \(f\), a coordinate \(i\) with
\[
0<j_i\le\frac12,
\]
and abbreviate \(g=g_i\), \(j=j_i\),
\[
E=\{x:g(x)\ne0\},\qquad \mu(E)=j.
\]
Let
\[
d_g:=\sum_{r\ne i}\|D_rg\|_2^2.
\]
By (1),
\[
\mathbb E[Z\mid X=i]=\frac{d_g}{j}.
\tag{14}
\]
For the support indicator \(1_E\), the previous proof used
\[
4d_g\ge I(1_E)
\ge 2j\log_2\frac1j.
\tag{15}
\]
The first inequality is pointwise on cube edges; the second is the weak edge-isoperimetric inequality.

### Lemma (exact equality classification)

If
\[
\mathbb E[Z\mid X=i]
=\frac12\log_2\frac1j,
\tag{16}
\]
then there is an integer
\[
m=\log_2(1/j)
\]
and a set \(M_i\) of \(m\) coordinates such that, conditional on \(X=i\),
\[
\boxed{C\text{ is a product Bernoulli}(1/2)\text{ subset of }M_i.}
\tag{17}
\]
Equivalently, the row law in (1) is uniform on all \(2^m\) subsets of \(M_i\), and
\[
Z\sim\operatorname{Bin}(m,1/2).
\tag{18}
\]

### Proof

Equation (16) gives
\[
4d_g=2j\log_2(1/j),
\]
so both inequalities in (15) are equalities.

Equality in the weak cube edge-isoperimetric inequality forces \(E\) to be a subcube. Thus \(j=2^{-m}\) for an integer \(m\), and \(E\) fixes exactly \(m\) coordinates, say \(M_i\).

Now inspect equality in the first part of (15). Along an edge on which exactly one endpoint lies in \(E\), the contribution of \(4\|D_rg\|_2^2\) exactly matches the support-boundary contribution. An edge whose two endpoints lie in \(E\) but carry opposite signs contributes strictly positive derivative energy while contributing nothing to the support boundary. Equality therefore forbids every internal sign-changing edge. A subcube is connected, so \(g\) has one constant sign on \(E\):
\[
g=\sigma 1_E,\qquad \sigma\in\{\pm1\}.
\tag{19}
\]
For a codimension-\(m\) subcube, the Walsh expansion of \(1_E\) has magnitude \(2^{-m}\) on every subset of the \(m\) fixed coordinates and is zero elsewhere. Therefore
\[
\frac{\widehat g(D)^2}{j}=2^{-m}
\quad(D\subseteq M_i),
\]
which is exactly (17)--(18). \(\square\)

This classification includes the one-point Boolean defect from the preceding B12/B13 work: there the derivative support is a point, and the conditional co-spectrum is exactly uniform on all subsets of its fixed coordinates.

## 4. The surrogate is rejected precisely by the equality shape, not by depth

For the surrogate in Section 2,
\[
j_i=2^{-2d},\qquad \mathbb EZ=d
=\frac12\log_2(1/j_i).
\]
If this row came from a Boolean derivative, the lemma would force
\[
Z\sim\operatorname{Bin}(2d,1/2).
\]
But the surrogate has \(Z\equiv d\). This contradiction holds already for \(d=1\).

Thus the missing Boolean input is now sharply localized: **near-minimal Palm depth cannot be arbitrarily arranged across identities and degrees.** Exact minimal depth forces a signed subcube derivative, whose Fourier row is maximally spread over all subset sizes rather than concentrated on one level.

## 5. A conserved defect identity points to a quantitative route

Define the nonnegative depth defect
\[
\Delta_i
:=\mathbb E[Z\mid X=i]
-\frac12\log_2\frac1{j_i}.
\tag{20}
\]
Let
\[
\operatorname{Slack}_{\rm sign}
:=4d_g-I(1_E)\ge0,
\]
\[
\operatorname{Slack}_{\rm iso}
:=I(1_E)-2j_i\log_2(1/j_i)\ge0.
\]
Using \(d_g=j_i\mathbb EZ\), the two discarded quantities satisfy the exact conservation law
\[
\boxed{
\operatorname{Slack}_{\rm sign}
+
\operatorname{Slack}_{\rm iso}
=4j_i\Delta_i.
}
\tag{21}
\]
This is the useful new potential from the run. Small \(\Delta_i\) simultaneously means:

1. the derivative support is near an edge-isoperimetric minimizer; and
2. there is little internal sign-change energy beyond the support boundary.

Ellis's sharp stability theorem for the weak cube edge-isoperimetric inequality says, after matching boundary normalization, that sufficiently small isoperimetric excess forces the support close to a subcube, quantitatively. Equation (21) supplies that excess directly from the Palm-row depth defect. The remaining work is to combine this with the sign slack and prove a **stable row-shape theorem**: small \(\Delta_i\) should force the normalized spectral row in (1) close to the Bernoulli-subcube law (17), while large \(\Delta_i\) supplies extra depth that can potentially pay erasure loss.

I have **not** proved that stable row-shape statement, nor the final information inequality. Existing edge-isoperimetric stability controls the support set; an additional Fourier/sign stability step is still required. This is the next nontrivial bridge, not an automatic corollary.

## 6. Executed check and limitations

`check_uniform_level_surrogate.py` was executed in this run with only the Python standard library. For \(2\le k\le12\) it checked the exact parameter identities and mean-depth equality, and independently evaluated the random-prefix information formulas. It passed 11 rows, 55 exact parameter checks, and 44 numerical information checks. The numerical values approach the proved asymptotic obstruction rapidly: by \(k=12\), terminal information is 22 bits, prefix information is about \(1.58\times10^{-7}\) bits, and the loss is about 21.999999842 bits.

The continuum hypercontractive inequality (8), the divergence (13), and the Boolean equality classification are proved algebraically above; the finite script is supporting evidence only.

## 7. Ledger and next attack

**PROVED in this run**

- The family (4) of uniform fixed-level subset laws satisfies the complete current Palm hypercontractive moment envelope (2).
- It exactly saturates the scalar mean-depth bound (3).
- Its terminal-to-prefix information loss obeys \(L>2k-3\), hence is unbounded.
- For a genuine Boolean derivative row with \(j_i\le1/2\), equality in the scalar mean-depth theorem forces a signed subcube derivative and a conditional row law uniform over all subsets of a fixed coordinate set.
- The exact slack conservation identity (21).

**DISPROVED**

- “Palm hypercontractive depth + sharp mean depth + generic subset/shadow consistency suffice for bounded reverse-data-processing loss.”

**OPEN**

- Full uniform-cube FEI.
- A quantitative stable row-shape theorem turning small \(\Delta_i\) into proximity to a signed-subcube spectral row.
- An amortized information inequality showing that large depth defect pays loss while near-subcube rows preserve enough identity information under random-prefix thinning.

**Next B12 attack:** import the exact constants from cube edge-isoperimetric stability with the present derivative normalization, prove a sign-stability lemma from `Slack_sign`, and test whether the resulting two-regime estimate can bound the selector loss without assuming a fixed level, plateaued amplitudes, or a structured Boolean class.
