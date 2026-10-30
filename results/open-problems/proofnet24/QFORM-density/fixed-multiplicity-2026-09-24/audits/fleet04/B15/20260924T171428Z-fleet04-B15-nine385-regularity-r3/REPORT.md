# Nine-eigenvalue regularity-scope audit

## Verdict

**PASS** for Gaussian inversion, the Riesz negative-half-moment lemma, and the stated essential-boundedness theorem.

**PASS, with a useful strengthening:** in the no-pivot chamber the canonical density is not merely bounded and continuous; it lies in \(C_0(\mathbb R)\).

**UNCHECKED / not proved by this manuscript:** continuity of the output density in the scalar-pivot and two-coordinate-pivot chambers. The paper correctly does not claim it. Its full theorem is an \(L^\infty_{\rm ess}\) statement only.

This report is a focused independent audit, not a second end-to-end validation of all 955 source lines.

## Source pin

- Repository: \`yspennstate/math-open-problems\`
- Source: \`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex\`
- Commit: \`eeb752c8943536541b34b42b8bf48e924f4d3d2f\`
- Git blob: \`19fb119877426b640b2c0dae19ec2f78a399fe11\`
- SHA-256: \`bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3\`

## 1. Fourier and Gaussian inversion (lines 87–116): PASS

With
\[
\widehat f(t)=\int e^{itx}f(x)\,dx,
\]
the Plancherel constant \(2\pi\), the density inversion factor \(1/(2\pi)\), and the Gaussian formula
\[
\mathbb E e^{-v(Z-a)^2}
 =\frac1{2\sqrt{\pi v}}\int_{\mathbb R}
 e^{-t^2/(4v)}e^{-ita}\phi_Z(t)\,dt
\]
are mutually consistent.

The regularization proof is legitimate:

1. \(p_\varepsilon\) is the density of \(\mu*g_\varepsilon\).
2. If \(\phi_Z\in L^1\), dominated convergence gives uniform convergence of \(p_\varepsilon\) to the inverse Fourier integral.
3. Weak convergence of \(\mu*g_\varepsilon\) to \(\mu\) identifies the limiting continuous function as a density of \(Z\).

There is no hidden pointwise evaluation of an arbitrary density representative.

## 2. Riesz half potential (lines 128–156): PASS

The gamma identity
\[
|z|^{-1/2}
 =\Gamma(1/4)^{-1}\int_0^\infty v^{-3/4}e^{-vz^2}\,dv
\]
has the correct homogeneity. After Gaussian inversion,
\[
\int_0^\infty v^{-5/4}e^{-t^2/(4v)}\,dv
 =\sqrt2\,\Gamma(1/4)|t|^{-1/2},
\]
so the prefactor is exactly \(1/\sqrt{2\pi}\). Tonelli is applied only to nonnegative majorants, including the extended-value case. For
\[
|\phi_Z(t)|\le \min\{1,(u/|t|)^{3/4}\},
\]
the split at \(u\) gives
\[
2\int_0^u t^{-1/2}dt+
2u^{3/4}\int_u^\infty t^{-5/4}dt=12\sqrt u.
\]
Thus
\[
\sup_a\mathbb E|Z-a|^{-1/2}\le12\sqrt{u/(2\pi)}
\]
is correct.

## 3. No-pivot branch actually gives \(C_0\): PASS / strengthening

The marginal-free crossing theorem (lines 489–522) produces an integrable exponent-\(3/2\) characteristic-function envelope in the order-three case. Lemma 2.1 then gives a continuous density. Since the inverse Fourier transform of an \(L^1\) function vanishes at infinity,
\[
A\text{ has no pivot},\quad s_9(A)\ge1
\quad\Longrightarrow\quad
p_Q\in C_0(\mathbb R),\qquad \|p_Q\|_\infty<375.
\]
After general scaling this becomes
\[
p_Q\in C_0(\mathbb R),\qquad
\|p_Q\|_\infty<375\,K^2/s
\]
in the no-pivot chamber.

The assertion follows directly from the paper's proof but is stronger than the wording of Corollary 7.8 (lines 754–765).

## 4. Pivot branches prove \(L^\infty_{\rm ess}\), not continuity: scope PASS

Lines 830–858 close scalar, definite-pair, and indefinite-pair branches through conditional density domination against nonnegative output test functions and Tonelli. This rigorously proves absolute continuity and the interval inequality
\[
\mathbb P\{Q\in J\}\le C|J|.
\]
It does not yield a uniform output modulus of continuity.

That distinction is material:

- Conditional square profiles have moving critical boundaries and square-root kernels.
- Definite-pair profiles can have a jump at a critical value before averaging. For example, if \(U,V\) are uniform on \([-1/2,1/2]\), the density of \(U^2+V^2\) has positive right limit at zero and is zero to the left.
- The hyperbolic-pair argument supplies a logarithmic envelope and then an averaged \(L^\infty\) bound, but no translation-continuity estimate in the output variable.

The manuscript is accurate at line 71 in saying that the full theorem asserts essential boundedness.

## 5. Why cap-preserving smooth approximation alone cannot add continuity

Let
\[
f=\mathbf 1_{[0,1]},\qquad f_\varepsilon=f*g_\varepsilon .
\]
Then each \(f_\varepsilon\) is a smooth probability density with \(0\le f_\varepsilon\le1\), and
\[
\|f_\varepsilon-f\|_1\to0.
\]
Nevertheless there is no uniform convergence to any continuous representative of \(f\): a uniform limit of continuous functions is continuous, whereas no continuous function equals \(\mathbf 1_{[0,1]}\) almost everywhere.

Consequently, the rough-law trace step
\[
p_{Q_\varepsilon}\,dx\Longrightarrow p_Q\,dx,\qquad
\sup_\varepsilon\|p_{Q_\varepsilon}\|_\infty\le C,
\]
is sufficient for \(\|p_Q\|_{\infty,\rm ess}\le C\), but not for \(p_Q\in C_0\). A continuity theorem needs an equicontinuous output family, an \(L^1\) characteristic-function majorant, or another genuine translation-modulus estimate.

## 6. Downstream status

- The nine-eigenvalue bounded-density theorem is unaffected.
- No-pivot continuity is closed quantitatively.
- Full nine-eigenvalue continuity remains open at the pivot branches.
- This regularity issue does not lower the multiplicity from nine to eight and does not solve the unrestricted three-eigenvalue conjecture.
