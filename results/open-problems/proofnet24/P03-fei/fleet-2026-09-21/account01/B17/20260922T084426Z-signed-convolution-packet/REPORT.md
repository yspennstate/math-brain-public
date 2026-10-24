# account01/B17 — signed convolution packet theorem for the live Gibbs residual

**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full Friedgut–Kalai FEI:** **OPEN / NOT PROVED**.

## 0. Bound candidate and exact inherited statements

The live all-gate candidate is the immutable `LIMIT-PRIME-GATE-LIFT-v1`

\[
C^\dagger=6.521851214,\qquad
\Gamma^\dagger(z)=\Gamma_0(z)+0.268204856\,z(1-z),
\]

with the exact Gibbs normalization `B-GIBBS-KL-v1` from account03/B18, `20260922T075546Z-gibbs-price-bellman/REPORT.md`.

On the balanced uniform slice, for a Boolean gate \(f:\{-1,+1\}^k\to\{-1,+1\}\), write ordinary Walsh coefficients \(a_S=\widehat f(S)\), \(w(S)=a_S^2\), and \(a_\varnothing=0\). Put

\[
x=2^{-C^\dagger},\qquad y=x^{1-\lambda},\qquad
A=(1+y)^k-1,
\]

and on nonempty subsets

\[
\rho_y(S)=\frac{y^{|S|}}{A}.
\]

The exact account03/B18 identity is

\[
R_B(f)=D_{\rm KL,2}(w\|\rho_y)
+\lambda C^\dagger I(f)-\log_2\frac{A}{x}.
\tag{0.1}
\]

Thus the scalar Bellman relaxation is already exact and the first missing inference is a quantitative lower bound on the residual \(D_{\rm KL,2}(w\|\rho_y)\) coming from Boolean realizability.

The named other-account input used substantively is account04/B16,
`20260922T081206Z-signed-gibbs-phase-residual/REPORT.md`, blob
`2ff82a8e044d035beb32d8fa48a7bc6303abbc14`.
It proves from the exact Boolean convolution identities

\[
\sum_S a_Sa_{S\triangle T}=0\quad(T\ne\varnothing)
\tag{0.2}
\]

that, after sign-aligning Gibbs amplitudes

\[
b_S=\operatorname{sgn}(a_S)\sqrt{\rho_y(S)},\qquad b_\varnothing=0,
\tag{0.3}
\]

the unordered \(T\)-pair sum has magnitude at least

\[
L_{k,t}(y)=\frac{y^{t/2}}{A}
\left[1-2^{t-1}\big((1+y)^{k-t}-1\big)\right]_+
\tag{0.4}
\]
for every \(|T|=t\ge2\). B16 used one \(T\) at a time and explicitly left open a packet/sum version that does not lose the dimension factor.

This run proves such a packet statement for **all two-coordinate equations simultaneously**.

## 1. PROVED — all-pairs convolution packet lower bound

Let \(g\) be the real function whose Walsh coefficients are the signed Gibbs amplitudes \(b_S\). Then

\[
\|g\|_2^2=\sum_Sb_S^2=1.
\]

For every two-set \(T\), (0.4) with \(t=2\) gives

\[
\left|\sum_{\{S,S\triangle T\}}b_Sb_{S\triangle T}\right|
\ge
\frac{y}{A}\left[3-2(1+y)^{k-2}\right]_+.
\tag{1.1}
\]

The Fourier coefficient of \(g^2\) at \(T\) is the **ordered** convolution

\[
\widehat{g^2}(T)=\sum_Sb_Sb_{S\triangle T},
\]
so (1.1) doubles. Since \(f^2\equiv1\), all nonempty Fourier coefficients of \(f^2\) vanish. Parseval therefore accumulates the \(\binom{k}{2}\) distinct two-coordinate equations orthogonally:

\[
\boxed{
\|g^2-1\|_2
\ge P_k(y):=
2\sqrt{\binom{k}{2}}\,
\frac{y}{A}\left[3-2(1+y)^{k-2}\right]_+.
}
\tag{1.2}
\]

There is no triangle-inequality loss across the different \(T\)'s; their Fourier packets are orthogonal.

## 2. Turning packet defect into Hellinger distance

Let

\[
d:=\|a-b\|_{\ell^2}
=\|f-g\|_2
=\left(\sum_{S\ne\varnothing}
(\sqrt{w(S)}-\sqrt{\rho_y(S)})^2\right)^{1/2}.
\tag{2.1}
\]

Set \(r=g-f\). Because \(f^2=1\),

\[
g^2-1=2fr+r^2,
\]
whence

\[
\|g^2-1\|_2\le2d+\|r\|_4^2.
\tag{2.2}
\]

Fix any real moment exponent \(q>4\), and put

\[
\alpha=\frac{q-4}{q-2}\in(0,1).
\tag{2.3}
\]

Bonami hypercontractivity gives a sign-independent radial bound for \(g\). Indeed write

\[
g=T_{1/\sqrt{q-1}}u,
\qquad
\widehat u(S)=(q-1)^{|S|/2}b_S.
\]
Then

\[
\|g\|_q\le\|u\|_2
=\left(\frac{(1+(q-1)y)^k-1}{A}\right)^{1/2}.
\]
As \(\|f\|_q=1\),

\[
\|r\|_q\le
Q_{k,q}(y):=
1+\left(\frac{(1+(q-1)y)^k-1}{A}\right)^{1/2}.
\tag{2.4}
\]

Interpolating \(L^4\) between \(L^2\) and \(L^q\), where

\[
\frac14=\frac\theta2+\frac{1-\theta}{q},
\qquad 2\theta=\alpha,
\]
gives

\[
\|r\|_4^2\le d^\alpha Q_{k,q}(y)^{2-\alpha}.
\tag{2.5}
\]

Combining (1.2), (2.2), and (2.5) proves

\[
\boxed{
P_k(y)\le
2d+Q_{k,q}(y)^{2-\alpha}d^\alpha.
}
\tag{2.6}
\]

Let \(d_*(k,y,q)>0\) be the unique positive solution of

\[
2d+Q_{k,q}(y)^{2-\alpha}d^\alpha=P_k(y)
\tag{2.7}
\]
whenever \(P_k(y)>0\). Then

\[
\boxed{d\ge d_*(k,y,q).}
\tag{2.8}
\]

Finally, the base-two KL/Hellinger inequality gives

\[
\boxed{
D_{\rm KL,2}(w\|\rho_y)
\ge \frac{d_*(k,y,q)^2}{\ln2}.
}
\tag{2.9}
\]

This is the desired packet strengthening of the single-\(T\) signed phase credit.

## 3. PROVED — dimension-independent mesoscopic Boolean-realizability gap

The packet theorem becomes dimension independent at the natural radial scale \(y=\eta/k\).
Fix

\[
0<\eta<\ln(3/2),\qquad q>4,
\]
put

\[
P(\eta)=
\frac{\eta(3-2e^\eta)}{e^\eta-1}>0,
\tag{3.1}
\]

\[
Q(\eta,q)=
1+\left(\frac{e^{(q-1)\eta}-1}{\eta}\right)^{1/2},
\qquad
\alpha=\frac{q-4}{q-2},
\tag{3.2}
\]
and

\[
\delta(\eta,q)=
\min\left\{
\frac{P(\eta)}4,
\left(
\frac{P(\eta)}{2Q(\eta,q)^{2-\alpha}}
\right)^{1/\alpha}
\right\}>0.
\tag{3.3}
\]

For every \(k\ge2\), with \(y=\eta/k\),

\[
A=(1+\eta/k)^k-1\le e^\eta-1,
\]

\[
3-2(1+\eta/k)^{k-2}\ge3-2e^\eta,
\]
and

\[
2\sqrt{\binom{k}{2}}\frac\eta k\ge\eta.
\]
Hence \(P_k(\eta/k)\ge P(\eta)\). Also \(A\ge\eta\) and

\[
(1+(q-1)\eta/k)^k-1\le e^{(q-1)\eta}-1,
\]
so \(Q_{k,q}(\eta/k)\le Q(\eta,q)\). Equation (2.6) therefore implies

\[
P(\eta)\le2d+Q(\eta,q)^{2-\alpha}d^\alpha.
\]
If \(d\) were smaller than both terms in (3.3), the two terms on the right would each be \(<P(\eta)/2\), a contradiction. Thus

\[
\boxed{
D_{\rm KL,2}(w\|\rho_{\eta/k})
\ge
\frac{\delta(\eta,q)^2}{\ln2}
\quad\text{for every balanced Boolean }f
\text{ and every }k\ge2.
}
\tag{3.4}
\]

This is a **finite, dimension-independent KL separation from the mesoscopic radial Gibbs law**. It is a direct Boolean-realizability statement, not a finite-dimensional enumeration.

For orientation only, taking \(\eta=0.01\) and \(q=20\) gives the diagnostic values

\[
P(\eta)\approx0.9750083333,\quad
Q(\eta,q)\approx5.574380807,\quad
\delta(\eta,q)\approx0.05202712545,
\]
so the explicit analytic floor in (3.4) is about \(0.00390511836\) bits. These decimals are not used in the proof.

## 4. Exact insertion into the live candidate

Substituting (2.9) into the exact account03/B18 identity (0.1) yields, whenever \(P_k(y)>0\),

\[
\boxed{
R_B(f)\ge
\lambda C^\dagger I(f)
-\log_2\frac{(1+y)^k-1}{x}
+\frac{d_*(k,y,q)^2}{\ln2},
\qquad y=x^{1-\lambda}.
}
\tag{4.1}
\]

Thus every scalar Bellman-safe region is strictly enlarged by a source-valid signed Boolean packet payment. No coordinate labels or signs are discarded before the Boolean cancellation; the only positivity contraction occurs after the packet is assembled.

## 5. Exact old/new missing implication

**Old missing implication.** Account04/B16 had a positive single-convolution-equation KL credit but its unconditional \(t=k\) version can be exponentially small. Its report explicitly identified the next needed inference as a simultaneous packet of convolution equations.

**New implication proved here.** All \(\binom{k}{2}\) two-coordinate Boolean convolution equations can be accumulated orthogonally in \(L^2\), and hypercontractivity turns that packet defect into the quantitative KL bound (2.9). At \(y=\eta/k\) this gives the dimension-free separation (3.4).

**Remaining gap.** This does not prove `LIMIT-PRIME-GATE-LIFT-v1` for all gates. At \(y=\eta/k\), the corresponding Bellman tilt \(\lambda\) eventually becomes negative as \(k\to\infty\), so the scalar term \(\lambda C^\dagger I(f)\) in (4.1) cannot simply be discarded or paid by Poincare. The unresolved inference is to obtain a packet credit at the Bellman-optimal/low-price tilt uniformly over arity and arbitrary product bias, or to construct a genuine Boolean gate+bias violating the live candidate.

Accordingly this run is `ESSENTIAL_STEP_APPLIED`, not a full proof candidate.

## 6. Finite sanity check

A standard-library checker exhausts all balanced truth tables for \(k=2,3,4\) (12,946 functions total), directly computes Walsh coefficients, the signed Gibbs amplitude function \(g\), the packet norm, Hellinger distance, and KL divergence, and checks (1.2), (2.8), and (2.9) at \(\eta=0.01,q=20\). It returns `PASS`. The finite calculation is only a sanity check; the theorem above is analytic.