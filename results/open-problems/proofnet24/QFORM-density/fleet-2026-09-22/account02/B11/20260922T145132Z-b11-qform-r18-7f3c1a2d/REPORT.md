# account02/B11 — null-heavy Walsh-bank compiler for genuinely rotated indefinite rank three

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Control revision:** 2026-09-22.5  
**Run:** 20260922T145132Z-b11-qform-r18-7f3c1a2d  
**Assignment:** Indefinite signatures  
**Status:** ESSENTIAL_STEP_APPLIED / FULL CONJECTURE OPEN  
**Execution:** WITHOUT_VERIFIED_BRAIN

## First unpaid implication attacked

The preceding B11 report reduced the heavy minority-sign exact-rank-three branch to the null-cone chamber. After a spectral change of basis that does **not** rotate the independent physical inputs, the hard model is

\[
H_0=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},
\qquad Q=2Z_1Z_3+Z_2^2,
\]

with one physical row of the Parseval frame equal to \((\sqrt c,0,0)\), \(c\ge 1/2\). The unpaid issue was that, in general, \(Z_1,Z_2,Z_3\) are dependent projections of the same product source; one may not replace them by independent rotated coordinates.

This run proves a uniform arbitrary-law theorem for a genuinely dependent Hadamard/Walsh subclass of that chamber and, simultaneously, gives an exact counterexample to any proof that first selects one well-conditioned original-coordinate \(3\times3\) principal triple. The mechanism is **aggregate original coordinates into independent sign-pattern banks first, then apply the partner's physical three-variable theorem.**

## Sources and corrections actually used

1. Previous account02/B11 theorem, canonical source `yspennstate/math-open-problems@245a4e2a4414294fbb20b9dd4f292f6b001e5aa2`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/20260922T135203Z-b11-qform-6080e0b3/REPORT.md`. I use its self-contained one-dimensional projection lemma: for independent cap-one variables and coefficients of squared sum one, the linear combination has density at most \(\sqrt e\).
2. Assigned partner account03/B11, canonical source `yspennstate/math-open-problems@860d849b7f2e0198bf7c3531a71b14e59f03e430`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260922T121353Z-account03-B11-QFORM-r11/REPORT.md`. I use Corollary 6.1: for a physical independent three-variable block \(B\) with a nonzero majority-sign pivot \(a\) and indefinite Schur complement,
\[
\|p_Q\|_\infty\le 8\,|a\det B|^{-1/4},
\]
with arbitrary outside coordinates conditioned.
3. Live corrections were consumed through brain main `3a8b28b1aef5d3c8aa7c74496e8f655e628493a2`, in particular `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, and `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`. No rotated conditional-density cap, fixed cross-rank-three cut, or best-principal-triple hypothesis is used.

## 1. The null-heavy Walsh family

Fix \(c\in[1/2,1]\) and put \(\alpha=\sqrt{1-c}\). Let \(m=4k\). Besides a distinguished original coordinate \(X_0\), split the other \(m\) independent coordinates into four equal banks indexed by \((\sigma,\tau)\in\{\pm1\}^2\). Define the normalized bank sums
\[
Y_{\sigma\tau}=k^{-1/2}\sum_{r=1}^k X_{\sigma\tau,r}.
\]
The four \(Y_{\sigma\tau}\) are independent because their source banks are disjoint.

Define
\[
\begin{aligned}
Z_1&=\sqrt c\,X_0+\frac{\alpha}{2}
 (Y_{++}+Y_{+-}+Y_{-+}+Y_{--}),\\
Z_2&=\frac12(Y_{++}+Y_{+-}-Y_{-+}-Y_{--}),\\
Z_3&=\frac12(Y_{++}-Y_{+-}+Y_{-+}-Y_{--}).
\end{aligned}
\]
In the original coordinate space, the coefficient vectors of \(Z_1,Z_2,Z_3\) are orthonormal. Hence
\[
Q=2Z_1Z_3+Z_2^2
\]
is an exact-rank-three quadratic form with nonzero eigenvalues \(1,1,-1\). For \(c<1\), all three spectral coordinates share the same four residual banks, so this is genuinely rotated/dependent for arbitrary non-Gaussian input laws.

Every normalized bank sum has density at most
\[
K:=\sqrt e
\]
by the one-dimensional projection lemma from the preceding B11 report.

## 2. Uniform density theorem after bank aggregation

Consider only the three **independent bank-level variables**
\[
X_0,\qquad Y_{++},\qquad Y_{+-},
\]
and condition on the other two bank sums. Their spectral row vectors are
\[
r_0=(\sqrt c,0,0),\quad
r_+=(\alpha/2,1/2,1/2),\quad
r_-=(\alpha/2,1/2,-1/2).
\]
For \(H_0\) above, the corresponding physical \(3\times3\) principal block is
\[
B=
\begin{pmatrix}
0&\sqrt c/2&-\sqrt c/2\\
\sqrt c/2&1/4+\alpha/2&1/4\\
-\sqrt c/2&1/4&1/4-\alpha/2
\end{pmatrix}.
\]
Since
\[
\det[r_0;r_+;r_-]=-\frac{\sqrt c}{2},
\qquad \det H_0=-1,
\]
we have
\[
\det B=-\frac c4.
\]
Use \(Y_{++}\) as pivot:
\[
a=B_{++}= \frac14+\frac\alpha2=\frac{1+2\alpha}{4}>0.
\]
Because \(\det B<0\), its \(2\times2\) Schur complement at this positive pivot is indefinite, exactly the assigned partner's majority-pivot branch.

The selected variables do not all have cap one: \(X_0\) has cap one and the two bank sums have cap \(K\). Set \(\widetilde Y=K Y\), whose density is at most one. Under this separate rescaling the block becomes \(D^{-1}BD^{-1}\), \(D=\operatorname{diag}(1,K,K)\). Therefore
\[
a'\,|\det B'|=\frac{a|\det B|}{K^6},
\]
and the partner theorem gives
\[
\|p_Q\|_\infty
\le
8K^{3/2}\,[a|\det B|]^{-1/4}.
\]
Now
\[
a|\det B|
=\frac{c(1+2\sqrt{1-c})}{16}.
\]
For \(c\in[1/2,1]\),
\[
c(1+2\sqrt{1-c})\ge1.
\]
Indeed, with \(t=\sqrt{1-c}\in[0,1/\sqrt2]\), the left side is
\((1-t^2)(1+2t)\), whose only interior critical point is a maximum and whose endpoint minimum is one. Consequently
\[
\boxed{\ \|p_Q\|_\infty\le16e^{3/4}<33.873.\ }
\]

This holds for **every** collection of independent original input densities bounded by one, every \(k\ge1\), and every \(c\in[1/2,1]\). Negating \(Q\) gives the dual \((+,-,-)\) statement with the same constant.

The proof never conditions on a conjugate spectral sum/difference. Independence is used only after exact grouping of disjoint original-coordinate banks.

## 3. Why the third direction removes the opposite-sign logarithmic singularity here

If the term \(Z_2^2\) is deleted, the spectral matrix drops from \(H_0\) to the rank-two saddle
\[
H_{\rm sad}=\begin{pmatrix}0&0&1\\0&0&0\\1&0&0\end{pmatrix},
\]
so every bank-level \(3\times3\) determinant above becomes zero. For standard Gaussian original inputs (used only as a control example, not in the proof), \(Z_1,Z_3\) are independent standard Gaussians because their coefficient vectors are orthogonal, and \(2Z_1Z_3\) has the classical logarithmic density divergence at zero.

Restoring \(Z_2^2\) changes \(\det H_{\rm sad}=0\) to \(\det H_0=-1\). In the two opposite-\(\tau\) banks \(Y_{++},Y_{+-}\), the \(Z_2\)-coefficients agree while the \(Z_3\)-coefficients have opposite signs. Together with the heavy null row this creates the fixed determinant
\[
|\det B|=c/4,
\]
after bank aggregation. The partner theorem then uses the bounded half-order potential of the residual opposite-sign binary form and the square-root Abel kernel contributed by the third pivot. Thus the logarithmic rank-two singularity is retained as a control and is removed by a concrete third-direction determinant at the **bank level**, not by false post-rotation independence.

## 4. Exact obstruction to best original-coordinate triple selection

The same family shows why the aggregation step is essential.

For each residual original coordinate \(i\), its spectral row is
\[
r_i=\frac1{\sqrt m}(\alpha,\sigma_i,\tau_i),
\]
while \(r_0=(\sqrt c,0,0)\). For a triple containing the heavy coordinate and two residual coordinates,
\[
|\det A[\{0,i,j\}]|
=
\frac{c(\sigma_i\tau_j-\sigma_j\tau_i)^2}{m^2}
\le\frac{4c}{m^2}.
\]
Every residual diagonal pivot obeys
\[
|A_{ii}|=\frac{|1+2\alpha\tau_i|}{m}
\le \frac{1+2\alpha}{m}.
\]
Hence every partner local scale in a heavy-containing original triple satisfies
\[
\bigl(|A_{ii}\det A[\{0,i,j\}]|\bigr)^{1/4}
\le
[4c(1+2\alpha)]^{1/4}m^{-3/4}\to0.
\]
For triples of three residual coordinates,
\[
|\det A[I]| \le \frac{16\alpha^2}{m^3},
\]
and the corresponding pivot scale is \(O(m^{-1})\).

So **every fixed physical \(3\times3\) determinant/pivot chart degenerates**, although the bank-aggregated law has the uniform bound \(16e^{3/4}\).

At the same time there is macroscopic determinant mass:
\[
\sum_{1\le i<j\le m} |\det A[\{0,i,j\}]|
=
c\sum_{i<j}(v_iw_j-v_jw_i)^2
=c,
\]
by the Cauchy--Binet identity for the orthonormal transverse pair \(v,w\). Likewise
\[
\sum_{j\ne0}A_{0j}^2=c.
\]
Thus the near-null cross export is not missing; it is spread over a dimension-growing bank. This is a source-valid counterexample to the stronger mechanism
“macroscopic heavy-row export implies one uniformly good original-coordinate principal triple.”
It is not a counterexample to QFORM.

## 5. Exact regression

`verify_null_walsh_bank.py` checks the algebra at \(c=3/4,m=8\):
- \(R^TR=I_3\);
- characteristic polynomial \(\lambda^6(\lambda-1)^2(\lambda+1)\);
- heavy diagonal \(A_{00}=0\) and cross-row squared norm \(3/4\);
- total heavy-triple determinant bank \(3/4\);
- maximum original principal \(3\times3\) determinant \(3/64\);
- maximum original partner scale \(3^{1/4}/4\);
- aggregated bank block determinant \(-3/16\), pivot \(1/2\), and product \(3/32\).

It also evaluates the maximum original partner scale for \(m=4,8,12,16\), confirming the predicted decay. Terminal marker:

`QFORM_NULL_WALSH_BANK_CHECK_PASS`.

Checker SHA-256: `33d4a9b2a290ce72b1f45bb906b1d45d41abbffe44a1f6e2ef34e54b29a23d48`.  
Captured-output SHA-256: `30301781bcd402f399e4d9b775a6acc3c9c9a7ef6d0636acb808da2aa6012404`.

The calculation is algebraic regression of the displayed identities, not a finite-census proof.

## 6. What is now paid and what remains

**Paid.** A nontrivial genuinely rotated/dependent family in the exact heavy-null canonical chamber \(2Z_1Z_3+Z_2^2\) has a dimension- and law-independent density bound. The proof explicitly compiles a diffuse physical determinant bank into three independent aggregate variables and then applies the assigned partner result. It therefore gives a concrete successful model for the aggregation demanded by the live corrections.

**Still unpaid.** An arbitrary Parseval frame need not have four exact sign-pattern banks. The next essential implication is a **stable bank compiler**:

> Given a null-heavy Parseval frame with row \(r_0=(\sqrt c,0,0)\), \(c\ge1/2\), construct a bounded number of disjoint original-coordinate aggregates whose induced \(3\times3\) block has determinant/pivot scale bounded below universally, or else pass to a diffuse-range/cross-block theorem already proved elsewhere.

The exact Walsh proof suggests the needed invariant is not the best minor but the total heavy-triple Cauchy--Binet mass
\(\sum_{i<j}|\det A_{0ij}|=c\). What is missing is a dimension-free way to round that determinant mass into a bounded number of **independent physical banks** without losing the sign geometry of the \(Z_2,Z_3\) plane.

Extra nonzero spectrum outside the selected rank-three piece remains a separate nonseparable debt. The full QFORM conjecture is therefore still OPEN.
