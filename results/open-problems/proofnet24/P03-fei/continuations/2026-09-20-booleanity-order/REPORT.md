# Exact Booleanity versus finite-order Fourier constraints

Research continuation for Yitzchak Shmalo — 20 September 2026.

**Status.** This work does not prove the unrestricted Friedgut–Kalai Fourier entropy–influence conjecture. It proves an obstruction to a specific attempted full-scope relaxation, including a uniformly almost-Boolean version, and an exact Boolean rigidity theorem for the spectral pattern used in the construction. The counterexamples to the relaxation are real-valued, **not Boolean functions**. Finite verification was executed and independently replayed in a second local directory, with byte-identical output; this is reproducibility, not independent mathematical review or proof-assistant formalization. Publication priority has not been established.

## 1. The attempted universal argument

For a real function on a uniform cube, write
\[
a_S=\widehat f(S),\qquad \sum_Sa_S^2=\mathbb E f^2=1,
\]
\[
H(f)=\sum_Sa_S^2\log_2(1/a_S^2),\qquad
I(f)=\sum_S|S|a_S^2,
\]
and let \(S\) have law \(a_S^2\). Define
\[
B(f)=\sum_i H(S_i\mid S_{-i}).
\tag{1.1}
\]
For real functions, \(I\) here is the spectral Dirichlet energy. It equals
\(\sum_i\mathbb E[(f-f^{\oplus i})/2]^2\); it is a disagreement probability only when the function is Boolean. Zero-mass entropy terms are zero.

The existing project proves that a finite universal bound \(B(f)\le K I(f)\), **for all Boolean functions**, would imply full FEI with constant \(K+2/\ln2\). The converse follows from \(B\le H\). This is a statement about uniform constants over all functions, not a pointwise estimate of \(H\) from \(B\).

The exact real-amplitude constraints for Booleanity are
\[
\sum_Sa_Sa_{S\triangle U}=\widehat{f^2}(U)=0
\quad(U\ne\varnothing),\qquad \sum_Sa_S^2=1.
\tag{1.2}
\]
A route tested here was to retain dyadic amplitudes, normalization, and a finite range of these signed identities, possibly together with proximity to a Boolean function. Theorems 2–4 show precisely why those weaker assumptions do not suffice. This does not prohibit a proof using a finite argument that exploits **other consequences of full Booleanity**.

For a nonnegative pair define the homogeneous binary entropy
\[
\mathcal E(r,s)=(r+s)h_2\!\left(\frac{s}{r+s}\right),
\]
with continuous boundary conventions. Then
\[
B(f)=\sum_i\sum_{T\not\ni i}\mathcal E(a_T^2,a_{T+i}^2).
\tag{1.3}
\]
The function \(\mathcal E\) is nondecreasing in both arguments: in the positive quadrant its partial derivatives are \(\log_2(1+s/r)\) and \(\log_2(1+r/s)\).

### Three distinct conclusions

1. **Dyadic finite-order obstruction.** Real functions with dyadic Fourier coefficients, \(\mathbb E f^2=1\), bounded fourth moment, and all signed identities through any prescribed finite order can have \(B/I\) arbitrarily large. In fact every physical restriction of up to that order has squared norm exactly one.
2. **Uniformly almost-Boolean obstruction.** Even the additional condition \(\|f-1\|_\infty\to0\) does not suffice. This version retains exact finite-order identities but does not claim dyadic Fourier coefficients.
3. **Exact Boolean contrast.** In the block-linear/data-affine spectral pattern below, genuine Booleanity forces either a character or exactly four Fourier coefficients of magnitude one half. These functions satisfy \(H\le(4/3)I\). This rigidity is a theorem for the stated pattern, not a representation theorem for all Boolean functions.

## 2. A dyadic construction with many exact cancellation identities

Let \(K=4^k\), \(k\ge1\), and \(m=3K/4\). Fix an integer \(w\ge1\). Take mutually disjoint blocks \(C_z\) of \(w\) physical sign coordinates, indexed by \(z\in\mathbb F_2^{2k}\), and \(m\) further independent sign coordinates \(x_i\), indexed by any \(m\) distinct nonzero elements of \(\mathbb F_2^{2k}\). Set
\[
Y_z=\chi_{C_z}(y),\qquad
\epsilon_{z,i}=(-1)^{z\cdot i},
\]
\[
L_z(x)=\frac1{\sqrt K}\left(\frac12+
\frac1{\sqrt K}\sum_{i=1}^{m}\epsilon_{z,i}x_i\right),
\qquad
G_{K,w}(x,y)=\sum_zY_zL_z(x).
\tag{2.1}
\]
The physical dimension is \(n=Kw+m\). Its nonzero Fourier coefficients are exactly
\[
\widehat G(C_z)=\frac1{2\sqrt K},\qquad
\widehat G(C_z\cup\{x_i\})=\frac{\epsilon_{z,i}}K.
\tag{2.2}
\]
They are dyadic rationals. Since their denominators divide \(2^n\), even the elementary integer-Walsh-denominator condition is satisfied; this alone does not make the inverse transform Boolean.

### Theorem 2.1

The function in (2.1) satisfies
\[
\mathbb E G^2=1,\qquad
\widehat{G^2}(U)=0\quad(1\le |U|\le2w-1),
\tag{2.3}
\]
\[
I(G)=w+\frac34,\qquad
H(G)=\frac74\log_2K+\frac12,
\tag{2.4}
\]
\[
\boxed{
B(G)=\frac34\log_2(1+K/4)
+\frac{3K}{16}\log_2(1+4/K).
}
\tag{2.5}
\]
Consequently
\[
\boxed{
\frac{B(G)}{I(G)}>
\frac{3}{4w+3}\log_2(1+K/4).
}
\tag{2.6}
\]
Every physical coordinate has spectral influence \(1/K\), so folded spectral energy also equals \(I(G)\). Moreover
\[
\mathbb E G^4=3-\frac{23}{4K}+\frac3{K^2}<3,
\qquad
\|G\|_\infty\le\sqrt K.
\tag{2.7}
\]
The function is not Boolean.

### Proof: normalization and exact cancellation

Walsh orthogonality of the chosen columns gives, for every fixed \(x\),
\[
\sum_zL_z(x)^2=\frac14+\frac mK=1.
\tag{2.8}
\]
The \(Y_z\) are independent symmetric signs. Hence
\[
G^2=1+2\sum_{z<z'}Y_zY_{z'}L_z(x)L_{z'}(x).
\tag{2.9}
\]
Every nonconstant monomial on the right contains exactly two complete control blocks, hence \(2w\) control coordinates, and zero, one, or two data coordinates. This proves normalization and (2.3). The only possible nonconstant Fourier degrees of \(G^2\) are \(2w,2w+1,2w+2\).

There is a stronger restriction statement. For any set \(A\) of at most \(2w-1\) physical coordinates and every assignment \(z\),
\[
\mathbb E[G^2\mid x_A=z]=1.
\tag{2.10}
\]
Indeed conditional expectation retains only square-spectrum labels contained in \(A\), and all nonempty such coefficients vanish. Thus **every such restricted function has squared norm one**, not merely the average of the restrictions. Fixing an arbitrary collection of data coordinates alone also preserves this normalization, by (2.8).

### Proof: entropy, energy, and erasure

The squared Fourier law is a product of a uniform choice among \(K\) control labels \(C_z\), and a data-label law with mass \(1/4\) at the empty label and \(1/K\) at each of the \(m\) singletons. This gives (2.4). Each control coordinate occurs with probability \(1/K\); each data coordinate also occurs with probability \(1/K\).

No two distinct control labels differ by a single coordinate, so every control-coordinate erasure entropy is zero. For each data coordinate the only nontrivial pairs are
\(C_z,C_z\cup\{x_i\}\). Homogeneity therefore gives
\[
B_i(G)=\mathcal E(1/4,1/K).
\]
Summing over \(m=3K/4\) coordinates yields
\[
B(G)=\frac{3(K+4)}{16}h_2\!\left(\frac4{K+4}\right),
\]
which expands to (2.5). Its second term is strictly positive, proving (2.6).

### Proof: fourth moment and non-Booleanity

Conditionally on \(x\), the fourth moment of a Rademacher sum with squared coefficient norm one is
\[
\mathbb E_yG^4=3-2\sum_zL_z(x)^4.
\]
For each \(z\), expand the fourth moment of the affine Rademacher sum in (2.1), using \(m=3K/4\). This gives
\[
q_K:=\mathbb E_x\sum_zL_z^4
=\frac{23}{8K}-\frac3{2K^2}.
\tag{2.11}
\]
Substitution proves (2.7). The fourth moment is strictly greater than one for \(K\ge4\), so
\[
\mathbb E(G^2-1)^2=2-\frac{23}{4K}+\frac3{K^2}>0;
\]
therefore \(G\) is not Boolean. Finally, (2.8) and Cauchy–Schwarz give \(\sum_z|L_z|\le\sqrt K\). ∎

For every fixed cancellation order \(r\), choose \(w=\lceil(r+1)/2\rceil\) and let \(K\to\infty\). All identities through order \(r\) hold, while \(B/I\to\infty\). One may also let \(w\to\infty\) with \(w=o(\log K)\); then the range of exact identities tends to infinity while the ratio still diverges. This last assertion is about these explicit sequences, not every possible prescribed hierarchy depth.

## 3. Dyadic coefficients, vanishing energy, and small square defect simultaneously

The preceding construction has a square defect of constant order. The following extension makes that defect vanish without losing the ratio obstruction.

Let \(R\ge8\) be a power of two. Use \(R-1\) independent copies \(G_a\) of \(G_{K,w}\), all on disjoint physical variables, and an additional disjoint control block \(C_0\) of size \(w\), with parity \(Z_0\). Set
\[
c=1-2/R,\quad b=2/R,\quad
\delta=(R-1)b^2=1-c^2,
\]
\[
F_{R,K,w}=c+bZ_0\sum_{a=1}^{R-1}G_a.
\tag{3.1}
\]
All its Fourier coefficients are dyadic.

### Theorem 3.1

This family satisfies
\[
\mathbb EF^2=1,\qquad
\widehat{F^2}(U)=0\quad(1\le |U|\le2w-1),
\tag{3.2}
\]
\[
I(F)=\delta(2w+3/4),\qquad B(F)=\delta B(G),
\tag{3.3}
\]
\[
H(F)=h_2(\delta)+\delta\bigl[\log_2(R-1)+H(G)\bigr],
\tag{3.4}
\]
\[
\|F-1\|_2^2=4/R,\qquad
\boxed{
\|F^2-1\|_2^2=4\delta-2\delta^2
-2(R-1)b^4q_K<16/R.
}
\tag{3.5}
\]
All coordinate spectral influences are at most one half. This is an \(L^2\)-proximity statement; uniform proximity is not asserted for this dyadic family.

**Proof.** The nonconstant spectra in (3.1) occupy disjoint labels, all containing \(C_0\) and exactly one control block from one copy. Their total mass is \(\delta\), with each copy contributing mass \(b^2\). This proves normalization, the energy and entropy formulas, and the per-coordinate influences: \(\delta\) on coordinates of \(C_0\), and \(b^2/K\) elsewhere.

There are no additional erasure edges between different copies or between the nonconstant support and the empty label. Thus erasure entropy scales by the sum \((R-1)b^2=\delta\), proving (3.3). Expanding \(F^2\) shows that all nonconstant terms have exactly \(2w\) control variables and at most two data variables; this proves (3.2) and, as before, normalization after any restriction fixing at most \(2w-1\) variables.

Put \(X=bZ_0\sum_aG_a\). Its odd moments vanish, \(\mathbb EX^2=\delta\), and independence gives
\[
\mathbb EX^4=3\delta^2-2(R-1)b^4q_K.
\]
Expansion of \((c+X)^4\), using \(c^2=1-\delta\), yields (3.5). The first distance formula follows from \(\mathbb EF=c\) and \(\mathbb EF^2=1\). ∎

For example, take \(K=4^k\), let \(w\ge1\) vary with \(w=o(k)\), and choose powers of two \(R\) with \(w=o(R)\) and \(R=o(k)\). Equations (2.4)–(3.5) then give
\[
I(F)\to0,\quad \|F-1\|_2\to0,\quad
\|F^2-1\|_2\to0,\qquad H(F),B(F)\to\infty.
\tag{3.6}
\]
The permitted exact cancellation depth also tends to infinity if \(w\to\infty\). Thus no dimension-independent entropy or erasure estimate can be obtained merely by combining these normalization, dyadic, finite-order, and small-square-defect conditions. Explicit error bounds depending on dimension or additional structure are not refuted.

## 4. Even uniform proximity does not repair the relaxation

The next family strengthens proximity to a uniform norm condition. It does **not** retain dyadic Fourier coefficients; the two conclusions must not be conflated.

Fix \(w\ge2\). Set
\[
Q=G_{K,w}/\sqrt K,\qquad
\varepsilon=\frac1{8\sqrt K},\qquad
U_{K,w}=\sqrt{1+\varepsilon Q},
\tag{4.1}
\]
using the positive square root. Since \(\|Q\|_\infty\le1\), this is well defined.

### Theorem 4.1

The real function \(U\) satisfies
\[
\mathbb EU^2=1,\qquad \|U-1\|_\infty\le\varepsilon\to0,
\tag{4.2}
\]
\[
\widehat{U^2}(A)=0\quad(1\le |A|\le w-1),
\tag{4.3}
\]
while
\[
\boxed{
\frac{B(U)}{I(U)}>
\frac45\frac{B(G)}{I(G)}>
\frac{12}{5(4w+3)}\log_2(1+K/4).
}
\tag{4.4}
\]
The energy tends to zero for fixed \(w\), with
\[
0<I(U)\le\frac{w+3/4}{256K^2(1-\varepsilon)}.
\tag{4.5}
\]
There is a stronger failure even after adding a natural squared-Booleanity-defect budget. Put
\[
D(U)=\mathbb E(U^2-1)^2=\varepsilon^2/K=\frac1{64K^2}.
\]
Then
\[
\boxed{
\frac{B(U)}{I(U)+D(U)}>
\frac45\frac{B(G)}{w+19/4}
>\frac{12}{5(4w+19)}\log_2(1+K/4).
}
\tag{4.11}
\]
Consequently, for every fixed positive integer \(r\), every \(\eta>0\), and every finite \(C\), there is a real function with squared norm one, \(\|U-1\|_\infty\le\eta\), all signed identities through order \(r\), and
\[
B(U)>C\bigl[I(U)+\mathbb E(U^2-1)^2\bigr].
\]
Every restriction fixing at most \(r\) variables also has squared norm one. Thus a universal linear error term in this squared defect does not repair the tested relaxation.

### Proof: exact constraints and uniform proximity

The identity \(U^2=1+\varepsilon Q\) is exact. The function \(Q\) has mean zero and Fourier support only in degrees \(w,w+1\). This proves (4.2)–(4.3) except the norm estimate, which follows from
\[
|\sqrt{1+t}-1|=\frac{|t|}{1+\sqrt{1+t}}\le |t|
\quad(|t|\le\varepsilon<1).
\]
Restriction normalization follows by conditional expectation as in (2.10).

### Proof: preserving enough of the erasure edges

Use the exact Taylor remainder
\[
\sqrt{1+t}=1+\frac t2-
\frac{t^2}{2(1+\sqrt{1+t})^2}.
\tag{4.6}
\]
For \(|t|\le1/2\) the absolute remainder is at most \(t^2/4\). Since \(\mathbb EQ^2=1/K\), every Fourier coefficient of the remainder in \(U=1+(\varepsilon/2)Q+R\) is bounded by
\[
|\widehat R(A)|\le\mathbb E|R|
\le\frac{\varepsilon^2}{4K}.
\tag{4.7}
\]
The smallest nonzero amplitude of \(Q\) has magnitude \(K^{-3/2}\). On all of its nonzero labels, the error relative to \((\varepsilon/2)\widehat Q(A)\) is at most
\[
\frac{\varepsilon^2/(4K)}{\varepsilon/(2K^{3/2})}
=\frac{\varepsilon\sqrt K}{2}=\frac1{16}.
\]
Therefore
\[
\widehat U(A)^2\ge
\left(\frac{15}{16}\right)^2\frac{\varepsilon^2}{4}\widehat Q(A)^2
\quad(A\in\operatorname{supp}\widehat Q).
\tag{4.8}
\]
Retain only the erasure edges already present in \(Q\). Monotonicity and homogeneity of \(\mathcal E\) give
\[
B(U)\ge\left(\frac{15}{16}\right)^2\frac{\varepsilon^2}{4}B(Q).
\tag{4.9}
\]
Additional Fourier coefficients or edges cannot reduce this lower bound.

### Proof: energy control

Across every physical edge,
\[
U-U^{\oplus i}
=\frac{\varepsilon(Q-Q^{\oplus i})}
{\sqrt{1+\varepsilon Q}+\sqrt{1+\varepsilon Q^{\oplus i}}}.
\]
It follows that
\[
\frac{\varepsilon^2}{4(1+\varepsilon)}I(Q)
\le I(U)\le
\frac{\varepsilon^2}{4(1-\varepsilon)}I(Q).
\tag{4.10}
\]
Combining (4.9) and (4.10), and using \(\varepsilon\le1/16\),
\[
\frac{B(U)}{I(U)}\ge
\left(\frac{15}{16}\right)^2(1-\varepsilon)\frac{B(Q)}{I(Q)}
\ge\left(\frac{15}{16}\right)^3\frac{B(G)}{I(G)}
>\frac45\frac{B(G)}{I(G)}.
\]
This proves (4.4); (4.5) follows from \(I(Q)=(w+3/4)/K\). For (4.11), use \(D(U)=\varepsilon^2/K\) and divide (4.9) by the upper bound
\[
I(U)+D(U)\le\frac{\varepsilon^2}{4K}
\left[\frac{w+3/4}{1-\varepsilon}+4\right].
\]
The resulting ratio is at least
\[
\left(\frac{15}{16}\right)^2(1-\varepsilon)
\frac{B(G)}{w+3/4+4(1-\varepsilon)}
>\frac45\frac{B(G)}{w+19/4},
\]
which proves (4.11). Taking \(w=r+1\) and then sufficiently large \(K\) proves the quantified assertion. ∎

### Energy-negligible defects still do not suffice

The failure persists even when the squared-Booleanity defect is negligible **relative to the energy**, rather than merely absolutely small. From the lower bound in (4.10),
\[
\frac{D(U)}{I(U)}\le\frac{4(1+\varepsilon)}{w+3/4}.
\tag{4.12}
\]
For the explicit sequence \(K=4^{j^2}\), \(w=j\), \(j\ge2\), we have
\[
\|U_j-1\|_\infty\to0,\quad I(U_j)\to0,\quad
\frac{\mathbb E(U_j^2-1)^2}{I(U_j)}\to0,
\]
\[
\widehat{U_j^2}(A)=0\quad(1\le|A|\le j-1),
\qquad
\frac{B(U_j)}{I(U_j)}\to\infty.
\tag{4.13}
\]
Thus the example also defeats a uniform continuity argument that assumes a small relative square defect together with an increasing range of exact cancellations. It does not defeat estimates with additional quantitative hypotheses or an error modulus that already includes the necessary logarithmic scale.

The function \(U\) is positive but nonconstant, hence it is not \(\{-1,1\}\)-valued. Rounding it to its sign gives the constant one and removes its entire nonconstant spectrum. That rounding does not produce a Boolean FEI counterexample or a proof of the missing bound.

## 5. What exact Booleanity forces in the same spectral pattern

The counterexamples used a function linear in independent control-block parities, with affine coefficients in the data. Exact Booleanity is much stronger in this setting than the low-order cancellation identities.

### Theorem 5.1: block-linear/data-affine rigidity

Let \(C_1,\ldots,C_q\) be disjoint physical control blocks, each of size \(w\ge1\), disjoint from data variables \(x\). Suppose
\[
f(x,y)=\sum_{z=1}^q\chi_{C_z}(y)L_z(x),\qquad
L_z(x)=c_z+\sum_i a_{z,i}x_i,
\tag{5.1}
\]
with real affine \(L_z\), and suppose \(f(x,y)\in\{-1,1\}\) **for every input**. Then either:

- \(f\) is a Walsh character up to an overall sign, so \(H(f)=0\); or
- \(f\) has exactly four nonzero Fourier coefficients, each of magnitude \(1/2\), and
\[
H(f)=2,\qquad I(f)\ge w+\frac12.
\]

In particular
\[
\boxed{H(f)\le\frac4{2w+1}I(f)\le\frac43 I(f).}
\tag{5.2}
\]
The bound \(4/(2w+1)\) is sharp within this pattern. No priority claim is made for this elementary classification.

### Proof

For fixed \(x\), the independent block parities can realize all sign assignments. Squaring (5.1) and comparing their characters gives the pointwise identities
\[
\sum_zL_z(x)^2=1,\qquad L_z(x)L_{z'}(x)=0\quad(z\ne z').
\tag{5.3}
\]
Exactly one \(L_z(x)\) is therefore \(\pm1\), and all the others vanish.

Each nonzero affine \(L_z\) takes values only in \(\{-1,0,1\}\). We record the elementary classification of such affine forms. Flipping a data coordinate shows that every nonzero coefficient has magnitude \(1/2\) or one. Also
\[
\|c+\sum_i a_ix_i\|_\infty=|c|+\sum_i|a_i|\le1.
\]
If some coefficient has magnitude one, all other coefficients and the constant vanish. If there are two nonzero coefficients, both have magnitude one half and the constant vanishes. If there is exactly one coefficient of magnitude one half, the two attained values force the constant to be \(\pm1/2\). If there are none, the nonzero constant is \(\pm1\). Thus the possible nonzero forms are exactly
\[
\pm1,\quad \pm x_i,\quad
\frac{\pm1\pm x_i}{2},\quad
\frac{\pm x_i\pm x_j}{2}\quad(i\ne j).
\tag{5.4}
\]
The first two have full support; the last two have support of measure exactly one half. By (5.3) the nonzero supports partition the data cube. Hence either a single full-support form occurs, giving a character, or exactly two half-support forms occur. In the latter case each form contributes exactly two Fourier coefficients of magnitude one half. Distinct control blocks keep all four labels distinct.

Every spectral label contains \(w\) control coordinates. For each half-support form, the average number of data coordinates in its two Fourier labels is at least one half. Therefore \(I(f)\ge w+1/2\), proving (5.2). Equality is attained by
\[
f(x,y)=\frac{1+x_1}{2}\chi_{C_1}(y)
+\frac{1-x_1}{2}\chi_{C_2}(y).
\]
∎

The contrast is exact: Hadamard orthogonality in (2.8) pays only the first identity in (5.3). The higher control-degree coefficients enforce the pairwise pointwise products in (5.3), which the truncated relaxation leaves unconstrained. For a general Boolean function, however, multiple-control terms and high-degree data coefficients can occur. Theorem 5.1 does not remove or control those terms, so it cannot be substituted for a proof of unrestricted FEI.

### A separate genuine-Boolean test: thresholding costs growing influence

There is another way to convert the real construction into a genuine Boolean function: set
\[
f_{K,w}=\operatorname{sgn}G_{K,w},\qquad \operatorname{sgn}(0)=+1.
\]
This does not preserve the bounded influence of the real function. In fact
\[
\boxed{
I(f_{K,w})\ge I_{\rm control}(f_{K,w})
\ge\frac{w\sqrt K}{4\sqrt{3\ln(4K)}}.
}
\tag{5.5}
\]
Here the logarithm is natural. This estimate applies to genuine Boolean functions; it does not bound their Fourier entropy and is not claimed as an FEI theorem for all quadratic thresholds.

To prove (5.5), fix the data input \(x\). The resulting function of independent parity variables is the linear threshold
\(\operatorname{sgn}\sum_zL_z(x)Y_z\). It is unate in each \(Y_z\), and hence its singleton Fourier coefficient has magnitude equal to the influence in that variable. Therefore
\[
\sum_z |L_z(x)|\operatorname{Inf}_{Y_z}(f\mid x)
=\mathbb E_Y\left|\sum_zL_z(x)Y_z\right|.
\]
By (2.8), the variable inside the absolute value has second moment one and fourth moment at most three. Hölder's inequality gives its first absolute moment at least \(1/\sqrt3\). It follows that
\[
\sum_z\operatorname{Inf}_{Y_z}(f\mid x)
\ge\frac1{\sqrt3\max_z|L_z(x)|}.
\tag{5.6}
\]
For each fixed \(z\), the sum in (2.1) is a sum of \(m\) independent signs. The elementary Chernoff bound, obtained from \(\cosh t\le e^{t^2/2}\), and a union bound imply with probability at least one half over \(x\) that
\[
\max_z |L_z(x)|
\le\frac{1/2+\sqrt{(3/2)\ln(4K)}}{\sqrt K}
\le\frac{2\sqrt{\ln(4K)}}{\sqrt K}.
\]
Average (5.6) over this event. Each of the \(w\) physical bits in a control block has the same influence as the corresponding block parity, which proves (5.5).

Thus both natural repairs were examined: taking the sign of the uniformly positive function in Section 4 gives a constant, while taking the sign of the oscillating Hadamard function incurs influence growing at least as \(\sqrt{K/\log K}\). Neither operation converts the relaxed counterexample into an established FEI counterexample. The numerical illustration in the checker computes only the actual seven-variable \(K=4,w=1\) threshold, not large-dimensional truth tables.

### Approximate conditional-mean Boolean lifts also have a quantified cost

A more flexible repair is to introduce independent auxiliary cube coordinates \(z\), seeking a Boolean \(F(x,z)\) whose conditional mean approximates \(U(x)/(1+\varepsilon)\). Suppose
\[
\left|\mathbb E_zF(x,z)-\frac{U(x)}{1+\varepsilon}\right|
\le\frac\varepsilon{16}\quad\text{for every }x.
\tag{5.7}
\]
Then, irrespective of the number of auxiliary variables or the form of the lift,
\[
\boxed{I_{\rm auxiliary}(F)\ge
\frac\varepsilon4\log_2(8/\varepsilon).}
\tag{5.8}
\]
This is a cost for the stated conditional-mean model, not a claim that all Boolean representations are impossible.

To see it, use \(\sqrt{1-\varepsilon}\le U\le\sqrt{1+\varepsilon}\). Before the approximation error, the conditional negative probability lies between \(\varepsilon/[4(1+\varepsilon)]\) and \(\varepsilon/(1+\varepsilon)\); the error in that probability is at most \(\varepsilon/32\). Since \(\varepsilon\le1/16\), the actual negative probability \(q_x\) belongs to \([\varepsilon/8,2\varepsilon]\).

The edge-isoperimetric inequality for a Boolean function of negative density \(q\) gives \(I\ge2q\log_2(1/q)\). One elementary induction proves the needed form: split the negative set into two slices of densities \(q_0,q_1\), use at least \(|q_0-q_1|\) disagreement between the slices, and apply the induction hypothesis within each. The remaining scalar inequality is \(h_2(t)\ge2t\) for \(0\le t\le1/2\), which follows from concavity. As \(q\log(1/q)\) increases on the interval used here, applying this to each conditional auxiliary function yields (5.8), then averaging over \(x\) proves the assertion.

In the current construction the lower bound (5.8) is of order \(K^{-1/2}\log K\), whereas the original real energy is of order \(w/K^2\). Thus this common lifting operation cannot be assumed to preserve the small energy underlying the relaxed counterexample. The checker verifies an explicit approximate lift in the 11-variable example using ten auxiliary bits and lexicographic negative sets; it checks each conditional mean and computes the auxiliary boundary exactly, without enumerating the full enlarged cube.

## 6. Executed verification

Run:

```sh
python verify_booleanity_order.py
```

The checker requires Python 3.10 or later and NumPy. Its assertions use integer/Fraction arithmetic, exact symbolic prime-log cancellation, and outward rational enclosures. Displayed decimal midpoints are not used to decide signs. Logarithms use the existing project's standard 48-term atanh-series enclosure after range reduction. For the uniformly close example, every square root is enclosed on a \(2^{-120}\) rational grid using an integer square root; signed interval Walsh butterflies then enclose the amplitudes.

The actual `verification.json` records:

| Family | Actual scope |
|---|---|
| Base Hadamard construction | Seven \((K,w)\) cases, \(K=4,16\), with full sparse square convolution, exact fourth moments, entropy identities, energies and erasure expressions; 624 nonzero erasure edges |
| Restricted norms | 1,778 exact physical-restriction checks for the base functions, including exhaustive cases and seeded samples |
| Dyadic almost-Boolean extension | Four sparse cases, up to 167 formal physical variables; 96 exact restriction checks; exact norm, energy, entropy, erasure, and square-defect identities |
| Uniformly close construction | All 2,048 values of the actual 11-variable square-root function enclosed; all 16 selected amplitude bounds and 12 retained erasure edges certified; 2,048 conditional-mean certificates for an explicit ten-auxiliary-bit Boolean lift |
| Genuine Boolean threshold | The actual 128-entry truth table of the seven-variable sign of the base construction, with exact control and total influences |
| Exact Boolean rigidity | All 65,536 Boolean functions on four variables examined; exactly 36 meet the stated support hypothesis, comprising 12 characters and 24 four-coefficient functions; 16 attain the \(4/3\) ratio |
| Parametric formulas | Seven rigorously enclosed ratio calculations, including \(K=4^{256}\); no truth tables at those huge dimensions were generated |

For the 11-variable square-root example, the directly certified lower bound on \(B(U)/I(U)\) is greater than \(0.51158\), while four fifths of the base ratio is less than \(0.43637\). This small example verifies the coefficient and energy comparison. The all-dimensional divergence follows from the analytic formulas, not from extrapolating this numerical value.

The complete checker was copied to a separate directory and rerun. Its output was byte-identical to the saved output. Neither run was an independent mathematical audit or a formal proof-assistant verification.

## 7. Earlier exploratory computation and scope corrections

Before this construction, an exploratory Walsh search considered the aggregate ratio \(B/J\), rather than fitting another special-class coefficient. It enumerated dimension four and ran seeded single-entry-flip searches with 20,000 evaluations each in dimensions five through eight. Its floating-point output is preserved under `exploratory/` and is **not an exact certificate or a new record claim**.

The repository's existing exact 80-variable NAND example has \(4.007<B/I<4.008\), exceeding all those sampled values. It prevents using the small search to propose \(B\le4I\). That counterexample and the previously retired absolute-overlap, resolvent, affine-drift, raw shared-control, and scalar-affinity routes remain retired. No new disproof of \(B\le4I\) is claimed here.

The dimension-adaptive endpoint potential was also reviewed through the affine-fibre handoff. Its individual-fibre obstruction does **not** refute the whole-function endpoint selector; neither does the real-valued construction in this report refute a selector quantified only over genuine Boolean functions. That full-scope Boolean route remains unresolved here.

## 8. Remaining full-scope obligation

The new results rule out replacing exact Booleanity by the particular weaker hypotheses above. They do not show that the Boolean erasure bound is false, or that a proof using full signed convolution constraints cannot work.

The full obligation is still
\[
\sup_{n\ge1}\ \sup_{f:\{-1,1\}^n\to\{-1,1\},\ I(f)>0}
\frac{\sum_iH(S_i\mid S_{-i})}{I(f)}<\infty.
\tag{8.1}
\]
A complete proof must control the dependent high-degree terms excluded by (5.1), or provide a different uniformly paid restriction/entropy argument. The present pointwise rigidity proof does not do that. It would be incorrect to conclude full FEI from it or to describe a real-valued relaxation counterexample as a Boolean counterexample.

## 9. Source ledger, attribution, and delivery

The following repository files were actually read in this continuation, all from `yspennstate/math-open-problems`, branch `master`:

- `proofnet24/P03-fei/README.md`, blob `1156fab7d6b2e8360bcbaa138855b97345b8def1`: current positive classes, concave restriction update, and superseded targets.
- `proofnet24/P03-fei/continuations/2026-09-20-affine-fibres/HANDOFF.md`, blob `5f236046ea4cb44c91b74866e7677b83266dbd02`: correct whole-function versus individual-fibre endpoint scope.
- `proofnet24/P03-fei/continuations/2026-09-20-entropy-continuity/ERASURE_RIGIDITY.md`, blob `52a0834a88d957d0331da95aa444406530741f7f`: exact independent-bit rigidity and its almost-independent bent-background limitation.
- `proofnet24/P03-fei/solo-2026-09-17/COMPOSITION_AND_BARRIERS.md`, blob `7ce27b3d2d5667e9b3b6e5f2b8548496c3d57e59`: the exact \(B\le4I\) obstruction and prior logarithmic/overlap limitations.
- `proofnet24/P03-fei/continuations/2026-09-20-polynomial-cores-and-tags/UNITARY_ERASURE_OBSTRUCTION.md`, blob `f35419c90fc304f7b8c77255fb5d4978e830121d`: the distinct obstruction to dropping the convolution requirement for a general orthogonal involution. The construction here is different: it retains convolution, but drops exact involutivity/Booleanity.

The prior conversation ZIP containing the concave-restriction report, checker and output was extracted locally for computational context. No claim is made to have reread every older project report or independently re-audited all earlier theorems.

Primary literature checked: María José González, Paul MacManus and María Cristina Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, revised 9 June 2026, https://arxiv.org/abs/2606.00246 . The paper supplies current context for the existing restriction/stopping-tree approach, not a premise needed to justify the explicit constructions in Sections 2–5. Bounded searches for related Fourier/Booleanity constraints did not establish novelty. Standard Walsh orthogonality, Rademacher moments, entropy homogeneity and conditional-expectation identities are not claimed as new.

**Delivery limitation for this continuation.** The GitHub read actions worked. The currently exposed GitHub actions did not include file creation or update; plugin discovery returned the same installed GitHub integration. A Git CLI connection attempt (`git ls-remote`) failed to resolve `github.com`. Accordingly, this report does not claim a new remote commit or later-worker uptake. The attached append-only patch and complete local package preserve the work without altering earlier proofs, schedules, ownership, visibility, or repository metrics.
