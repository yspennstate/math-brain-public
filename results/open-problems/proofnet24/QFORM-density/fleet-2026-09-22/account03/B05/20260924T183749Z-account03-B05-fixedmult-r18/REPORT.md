SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T18:37:49Z.
attacking: QFORM-PHYSICAL-FLAT-PAIR-CROSSGRAM-v1 — a product-preserving interval/coarea receiver for a literal zero 2x2 source block with rank-two cross Gram, and its application to the previous kernel-angle stress family.

# account03/B05 r18 — flat physical pair cross-Gram receiver

Run: `20260924T183749Z-account03-B05-fixedmult-r18`  
Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.  
Programme: `QFORM-DENSITY-3EIG-20260922`.  
Status: **PROVED SUPPORTING COAREA THEOREM / PREVIOUS r17 STRESS FAMILY PAID / s7 AND FULL s3 TARGET OPEN**.  
Regularity: essential boundedness proved; continuity is **not** claimed by this theorem.

## 1. Sources and live restrictions


The proof below does **not** use:
- independence after an orthogonal rotation;
- a conditional density cap for a projected variable;
- an arbitrary-joint coarea theorem;
- a pointwise law-uniform van-der-Corput bound;
- any moment, support, log-concavity, Gaussian, iid, or connected-support hypothesis.

The fresh input that changes the r17 mechanism is account01/B05's shared-bank two-hub receiver at
`yspennstate/math-open-problems@0d25e16cc969a36e96e46976f0990611ad2e80c4`,
`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account01/B05/20260924T182517Z-account01-B05-fixedmult-r13/REVIEW_AND_IMPROVEMENT.md`.
That report gives the same structural theorem with constant (e\sqrt{2\pi}). Section 3 below sharpens the planar negative-moment step and improves the constant to (e\sqrt\pi).

The designated partner result actually applied is account04/B05,
`QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`,
`yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`.

## 2. The flat-pair theorem

### Theorem `QFORM-PHYSICAL-FLAT-PAIR-CROSSGRAM-v1`

Let (X_1,\dots,X_n) be independent real variables whose one-dimensional densities satisfy
[
0\le f_i\le K.
]
Let (A=A^T) be arbitrary, and allow arbitrary affine terms (b^TX+c).

Assume there are two **literal original coordinates** (H=\{i,j\}) such that
[
A[H,H]=0_{2\times2}.
	ag{2.1}
]
Put
[
B=A[H,H^c]\in\mathbb R^{2\times(n-2)},\qquad
g=\det(BB^T).
	ag{2.2}
]
If (g>0), then
[
\boxed{
 \|p_{X^TAX+b^TX+c}\|_{\infty,\mathrm{ess}}
 \le e\sqrt\pi\,K^2 g^{-1/4}.
}
	ag{2.3}
]

Equivalently, for every interval (I\subset\mathbb R),
[
\boxed{
 \Pr\{X^TAX+b^TX+c\in I\}
 \le e\sqrt\pi\,K^2 g^{-1/4}|I|.
}
	ag{2.4}
]

The theorem keeps arbitrary quadratic curvature on the bank (H^c), arbitrary outside couplings already contained in (A), and arbitrary affine shifts. No density or independence is asserted for the two coordinates of the projected bank vector (BZ).

### Proof

Write
[
U=(X_i,X_j)^T,\qquad Z=X_{H^c}.
]
By (2.1),
[
Q=2U^T(BZ+\beta)+G(Z),
	ag{2.5}
]
where (eta=b_H/2) and (G) is the entire remaining quadratic-affine expression in the literal bank (Z).

Set
[
R=BZ+\beta\in\mathbb R^2.
]
The two-dimensional product-projection theorem used in the current fixed-multiplicity source gives
[
\|p_R\|_\infty
\le M:=\frac{eK^2}{\sqrt g}.
	ag{2.6}
]
This is an unconditional statement about the honest original-coordinate product bank (Z); it does not say the two components of (R) are independent.

Now condition on (Z=z). For (r=R(z)\ne0), the remaining random expression in (U) is the scalar linear projection
[
2r\cdot U+G(z).
]
The one-dimensional product-projection bound gives
[
\|p_{Q\mid Z=z}\|_\infty
\le \frac{\sqrt e,K}{2|r|}.
	ag{2.7}
]
Since (R) has an absolutely continuous planar law by (2.6), (Pr(R=0)=0). Therefore, for every interval (I),
[
\Pr\{Q\in I\}
\le
\frac{\sqrt e,K}{2}|I|\,\mathbb E\frac1{|R|}.
	ag{2.8}
]

It remains to estimate the planar negative moment without any support or moment assumptions. If a probability density (p\) on (mathbb R^2) satisfies (p\le M), then layer cake and the disk-area bound give
[
\mathbb E\frac1{|R|}
=
\int_0^\infty
\Pr\{|R|<t^{-1}\}\,dt
\le
\int_0^\infty
\min\left(1,\frac{\pi M}{t^2}\right)dt.
	ag{2.9}
]
Splitting at (t_0=\sqrt{\pi M}),
[
\int_0^{t_0}1\,dt+
\int_{t_0}^\infty\frac{\pi M}{t^2}\,dt
=2\sqrt{\pi M}.
	ag{2.10}
]
Thus
[
\boxed{
\mathbb E|R|^{-1}\le2\sqrt{\pi M}.
}
	ag{2.11}
]
Combining (2.6), (2.8), and (2.11),
[
\Pr\{Q\in I\}
\le
\frac{\sqrt e,K}{2}
\cdot
2\sqrt{\pi\frac{eK^2}{\sqrt g}}
\,|I|
=
e\sqrt\pi,K^2g^{-1/4}|I|.
	ag{2.12}
]
Interval domination yields absolute continuity and (2.3). (square)

## 3. Constant sharpening relative to the fresh account01/B05 result

The account01/B05 proof uses a valid but nonsharp planar estimate
[
\mathbb E|R|^{-1}\le2\sqrt{2\pi M}.
]
The exact layer-cake computation (2.9)--(2.10) removes the extraneous (sqrt2):
[
\boxed{
\mathbb E|R|^{-1}\le2\sqrt{\pi M}.
}
	ag{3.1}
]
Hence the structural theorem's constant improves from
[
e\sqrt{2\pi}
quad\text{to}\quad
\boxed{e\sqrt\pi}.
	ag{3.2}
]
No other part of the proof changes.

## 4. The r17 kernel-angle stress family is now paid

The preceding B05 run constructed the strict no-pivot family
[
A_\delta=
\begin{pmatrix}
B_\delta&C_\delta\\
C_\delta^T&0
\end{pmatrix},
\qquad
C_\delta
=
c\begin{pmatrix}
0&\delta\\
1&0\\
0&1
\end{pmatrix},
\qquad c=\frac{99}{1000},
	ag{4.1}
]
with (0<\delta\le1/25). After scaling by (1/c), its spectrum is
[
\{0,\pm1,\pm\sqrt{2+\delta^2}\},
	ag{4.2}
]
so the algebraic kernel-angle obstruction occurs inside the unrestricted owner target.

In r17 the two last literal coordinates form exactly the (2\times2) zero principal block. Their cross block is (C_\delta^T). Hence
[
g_\delta
=
\det(C_\delta^TC_\delta)
=
c^4(1+\delta^2).
	ag{4.3}
]
Theorem 2 therefore gives, for cap-one inputs,
[
\boxed{
\|p_{Q_\delta}\|_{\infty,\mathrm{ess}}
\le
\frac{e\sqrt\pi}
{c(1+\delta^2)^{1/4}}
<
\frac{e\sqrt\pi}{c}
<
48.667.
}
	ag{4.4}
]

This changes the interpretation of r17. The identity
[
\sum_h d_h^2=\Delta\|Bv\|^2
\quad\text{while}\quad
\Delta(v^TBv)^2=(v^Td)^2
]
remains a correct refutation of the structural inference
“bordered-star mass forces null-square curvature.” But the explicit r17 stress family is **not** an unpaid density configuration once the fresh shared-bank receiver is applied: its literal flat physical pair pays the whole form uniformly without using the alignment factor.

## 5. Designated partner application

The completed account04/B05 theorem states that for a literal original-coordinate definite principal pair (P),
[
\|p_Q\|_{\infty,\mathrm{ess}}
\le
\frac{\pi K^2}{\sqrt{|\det P|}},
	ag{5.1}
]
with arbitrary outside coupling retained.

Thus, at the current normalized pair-pivot threshold,
[
P\text{ definite},\qquad |\det P|\ge\frac1{100}
\quad\Longrightarrow\quad
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}\le10\pi K^2<31.416K^2.
}
	ag{5.2}
]

The r17 stress family has no nondegenerate definite principal pair, so (4.4) is not a disguised use of the partner convex exit. The two coarea receivers cover genuinely different physical geometries:
- definite two-coordinate curvature is paid by (5.1);
- a literal flat two-coordinate source block with rank-two cross Gram is paid by (2.3).

## 6. Precise surviving obstruction

A fresh account03/B16 result, `QFORM-SMALL-INDEFINITE-SOURCEBLOCK-PERTURBATION-FALSE-v1`, shows that the flat-pair theorem cannot be extended by a naive continuity argument to a small **indefinite** source block while retaining arbitrary same-bank curvature. Its explicit uniform-box family has a fixed full-rank crossing but logarithmically unbounded output; the full matrix has only two nonzero eigenvalues, so this is not a QFORM counterexample. It proves only that genuine third curvature must be spent before such a reduction.

Therefore the next B05 obligation is narrower than the r17 “kernel-angle” debt:

> In the multiplicity-seven overlap/shared-anchor terminal chamber, after removing definite-pair exits and exact flat-pair rank-two cross-Gram exits, retain the common physical anchor and the genuine third curvature jointly. Prove an interval/coarea bound for the remaining nonflat indefinite source-sharing geometry, or derive from the s7 structural packet a dimension-free lower bound on one of the already-paid physical currencies.

The alignment factor
[
\alpha=\frac{|v^Td|}{\|d\|}
]
by itself is **not** the correct final missing factor: (alpha) can vanish while the full form is still uniformly paid by the literal flat-pair cross-Gram theorem.

## 7. Scope and regularity

- Fixed multiplicity eight: a complete candidate with at least two separate end-to-end PASS reconstructions exists in the repository; this report does not self-award an owner release flag.
- Fixed multiplicity seven: **OPEN**.
- Unrestricted three-large-eigenvalue QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Theorem 2 proves an essentially bounded density. It does **not** establish a continuous representative for arbitrary rough inputs.
- Repository transport is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.

## 8. Source pins

- Fresh control objective: `math-research-brain/main`, `scheduled_tasks/CURRENT_OBJECTIVE.md`, blob `194c09609c2ce750efaa9634a0849b5a27ff651c`.
- Fresh correction inbox blob: `ba7aeac3d879f59da5ec8a12daad74ea85714465`.
- Fresh shared-bank theorem: `math-open-problems@0d25e16cc969a36e96e46976f0990611ad2e80c4`.
- Previous account03/B05 kernel-angle result: `math-open-problems@7ab90cc16db0b0a767b51d1f5a2ad1e1871f511c`.
- Designated account04/B05 definite-pair theorem: `math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`.
- Fresh small-indefinite perturbation barrier: account03/B16 run `20260924T180743Z-account03-B16-QFORM-auto11-r49`, statement commit `cb50c373a8f4638c198fa09b066f59b82003a2a2`.

No scheduler state, task identity, enabled/paused state, notification/email setting, permission, account connection, remote workflow, paid call, or public-release setting was changed.
