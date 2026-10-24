SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B09, 2026-09-23T10:16:59Z.
attacking: physical cross-bank smoothing with arbitrary dense self-couplings.

# B09 — dense-self-coupling bilinear Fourier closure

## Status

A new source-coordinate theorem proves a universal linear interval bound whenever an actual cross block between two disjoint original-coordinate banks has rank at least three with quantitative determinant. The two same-side quadratic blocks, conditioning-generated affine terms, outside spectrum, and outside couplings are completely arbitrary. The unrestricted three-eigenvalue conjecture remains open; continuity is separate and is proved only on this branch.

No coordinate rotation of the random variables, post-rotation independence, moment bound, support restriction, pointwise scalar stationary-phase estimate, or small-random-error argument is used.

## 1. Completed partner actually applied

This report uses account01/B09 \`QFORM-QUOTIENT-FRAME-DEGENERATION-ROUTING-v1\`, commit \`6f8979f8a677663e955befaeb1b4aebb3f0b6a2b\`:

\`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260923T091527Z-account01-B09-QFORM-auto11/REPORT.md\`, blob \`cb6de49bc3f9822d3623e7026e01bfc4ff922eae\`.

For one displayed curvature direction \(v\), two literal physical hub coupling columns \(c_1,c_2\), \(C=[c_1,c_2]\), and
\[
\Delta_\perp=\det(C^TP_{v^\perp}C)>0,
\]
that theorem gives the actual inequality
\[
\boxed{\;
 \|p_Q\|_\infty
 \le {5\over3}e^{3/5}
 [\rho |\lambda|\Delta_\perp]^{-1/5}.
\;}
\tag{1.1}
\]
The quotient determinant identity
\[
\det([v,C]^T[v,C])=\|v\|_2^2\det(C^TP_{v^\perp}C)
\tag{1.2}
\]
keeps all dependence on the same-side curvature span explicit.

For the partner's literal target-valid family
\[
Q_m=2X_1\langle c_1,Y\rangle+
    2X_2\langle c_2,Y\rangle+
    \langle v,Y\rangle^2,
\tag{1.3}
\]
where \(v,c_1,c_2\) are unit-flat on three disjoint size-\(m\) physical groups, (1.1) has
\[
\rho=(1-1/m)^3,\quad |\lambda|=\Delta_\perp=1,
\]
and hence
\[
\boxed{\;
\|p_{Q_{16}}\|_\infty
\le {5\over3}e^{3/5}(15/16)^{-3/5}<3.157.
\;}
\tag{1.4}
\]
This is a direct application of the completed partner result, not a restatement of a conjectural extension.

## 2. New theorem: arbitrary dense same-side blocks are harmless across a paid physical cross block

Let \(S,T\) be disjoint sets of original coordinates with
\[
|S|=|T|=r>2.
\]
Condition on every coordinate outside \(S\cup T\). Write the surviving conditional form as
\[
Q_z(x,y)
=x^TB_zx+2x^TCy+y^TD_zy
+a_z^Tx+b_z^Ty+c_z,
\tag{2.1}
\]
where \(C=A[S,T]\) is the actual physical cross block. The matrices \(B_z,D_z\) may be arbitrary symmetric matrices. The affine terms and constant may depend arbitrarily on the conditioned outside value \(z\).

### Theorem 2.1 (physical cross-determinant smoothing)

If \(C\) is invertible, then for every admissible cap-one product law,
\[
\boxed{\;
 \|p_{X^TAX}\|_\infty
 \le {r\over r-2}\,|\det C|^{-1/r}.
\;}
\tag{2.2}
\]
Moreover the characteristic function is integrable, so this branch has a continuous density.

For \(r=3\),
\[
\boxed{\;
 \|p_{X^TAX}\|_\infty
 \le 3|\det A[S,T]|^{-1/3}.
\;}
\tag{2.3}
\]

### Proof

Let \(f\) and \(g\) be the joint densities of \(X_S\) and \(X_T\). They are products of the original one-dimensional densities, hence
\[
0\le f,g\le1,\qquad \|f\|_1=\|g\|_1=1,
\]
and therefore
\[
\|f\|_2,\|g\|_2\le1.
\tag{2.4}
\]

For fixed \(z\) and \(t\ne0\), absorb every same-side quadratic and affine term into unit-modulus phases:
\[
F_{t,z}(x)=f(x)e^{it(x^TB_zx+a_z^Tx)},\qquad
G_{t,z}(y)=g(y)e^{it(y^TD_zy+b_z^Ty)}.
\tag{2.5}
\]
Using the Fourier convention
\[
\widehat G(\xi)=\int_{\mathbb R^r}G(y)e^{i\xi\cdot y}\,dy,
\]
the conditional characteristic function is
\[
\phi_z(t)
=e^{itc_z}\int_{\mathbb R^r}
F_{t,z}(x)\widehat G_{t,z}(2tC^Tx)\,dx.
\tag{2.6}
\]
Cauchy--Schwarz, the invertible change of variables \(\xi=2tC^Tx\), and Plancherel give
\[
\begin{aligned}
|\phi_z(t)|
&\le \|F_{t,z}\|_2
 \left(\int|\widehat G_{t,z}(2tC^Tx)|^2\,dx\right)^{1/2}\\
&=\|f\|_2(2|t|)^{-r/2}|\det C|^{-1/2}
 \|\widehat G_{t,z}\|_2\\
&=\pi^{r/2}|t|^{-r/2}|\det C|^{-1/2}
 \|f\|_2\|g\|_2\\
&\le \pi^{r/2}|t|^{-r/2}|\det C|^{-1/2}.
\end{aligned}
\tag{2.7}
\]
This bound is uniform in \(z\). Averaging the conditional characteristic functions therefore yields
\[
|\phi_Q(t)|
\le \min\{1,A|t|^{-\alpha}\},
\quad
\alpha={r\over2},
\quad
A=\pi^{r/2}|\det C|^{-1/2}.
\tag{2.8}
\]
Since \(r>2\), \(\alpha>1\), so the majorant is integrable. Fourier inversion gives a continuous density and
\[
\begin{aligned}
\|p_Q\|_\infty
&\le {1\over2\pi}\int_{\mathbb R}
 \min\{1,A|t|^{-\alpha}\}\,dt\\
&={\alpha\over\pi(\alpha-1)}A^{1/\alpha}\\
&={r\over r-2}|\det C|^{-1/r}.
\end{aligned}
\tag{2.9}
\]
This proves (2.2).

The calculation never separates or bounds the dense self-couplings \(B_z,D_z\): they remain inside \(F_{t,z},G_{t,z}\) and disappear only because their phases have modulus one.

## 3. Concrete target-valid dense-self-coupling family

Let \(r=3\), let \(C=I_3\), and let \(B,D\) be arbitrary real symmetric \(3\times3\) matrices. For independent cap-one coordinates \(X,Y\in\mathbb R^3\), define
\[
Q=X^TBX+2X^TY+Y^TDY.
\tag{3.1}
\]
The theorem gives
\[
\boxed{\|p_Q\|_\infty\le3}
\tag{3.2}
\]
uniformly over all \(B,D\), regardless of their norms, signs, resonances, or density of entries.

The coefficient matrix is
\[
H=\begin{pmatrix}B&I_3\\ I_3&D\end{pmatrix}.
\tag{3.3}
\]
The estimate requires no spectral hypothesis on \(H\). Whenever \(H\) has at least three eigenvalues of absolute value at least one, it is therefore an instance of the full target with the same constant \(3\). In particular \(B=D=0\) gives eigenvalues \(+1,+1,+1,-1,-1,-1\).

Arbitrary outside coordinates, outside quadratic spectrum, and couplings into the six active coordinates remain allowed: condition on them first, use the uniform affine-family estimate, and average.

## 4. How this interfaces with the B07 diffuse-star survivor

The newest account04/B07 reduction leaves an unpaid original-coordinate survivor with four disjoint banks carrying substantial star norm, while individual physical coefficients are small. Theorem 2.1 supplies a rigorous exit whenever three source rows and three source columns drawn from two disjoint banks form a cross minor \(C\) with quantitative determinant:
\[
|\det C|\ge\delta
\quad\Longrightarrow\quad
\|p_Q\|_\infty\le3\delta^{-1/3}.
\tag{4.1}
\]
Crucially, every self-coupling internal to either bank may be dense and arbitrarily large.

Thus the arbitrary dense-self-coupling obstruction is removed from the nondegenerate cross-minor chamber. The remaining structural task is now sharper: prove that the four-bank star survivor either contains a quantitative physical \(3\times3\) cross minor, satisfies the existing diffuse cross-volume theorem, or has sufficiently low/concentrated cross geometry to feed the partner's quotient-frame/puncture certificate. Large star norm alone does not force (4.1), so this report does not claim that final routing implication.

## 5. Exact residual

The unrestricted conjecture is still open. The first unpaid implication is:

> Starting only from the no-pivot condition and the four-bank star certificate, route the case where every physical \(3\times3\) cross minor is small and the diffuse volume hypotheses fail into a quantitative low-rank quotient-frame certificate of account01/B09, without rotating the random variables or discarding dense cross terms.

Theorem 2.1 shows that dense same-side curvature is not the difficulty. The residual is quantitative cross-geometry alignment.

## Pins

- account04/B09 assignment blob: \`12ee29f582f98c9b25e4fab492f825a73dd858b8\`.
- Current request blob: \`165c570ecb4dcc6299c38fc3298771e4a8339dac\`.
- Memory protocol blob: \`0d902d56688f4b5c575f5b921ddf9f6709e88312\`.
- AGENTS blob: \`e2aa9d53924e2d4e015b7c6680b0009241bec619\`.
- scheduled_tasks/README blob: \`fca13a89d221115332ce5e60d49554ee0e213efa\`.
- Execution label: \`WITHOUT_VERIFIED_BRAIN\`.
