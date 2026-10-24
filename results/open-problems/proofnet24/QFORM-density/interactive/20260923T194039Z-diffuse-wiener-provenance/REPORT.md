# Diffuse product projections: an integrable Fourier certificate

**Status:** proved scoped theorem. This excludes the specific dependent-light entropy counterexample as a diffuse product projection. It does not bound the leakage quadratic and does not prove the full QFORM conjecture.

## Theorem

Let \(X_i\) be independent real variables with densities \(0\le f_i\le1\). Let \(U\in\mathbb R^{n\times d}\) have orthonormal columns and rows \(u_i^\mathsf T\). Assume the **full \(d\)-dimensional row leverages** \(c_i=\|u_i\|_2^2\) satisfy \(c_i\le1/2\). For arbitrary measurable separate phases \(|\omega_i(x)|\le1\), define
\[
\Phi_\omega(\xi)=
\mathbb E\left[\prod_i\omega_i(X_i)
 e^{i\langle\xi,U^\mathsf TX\rangle}\right].
\]
With Fourier convention \(\widehat f(t)=\int e^{-itx}f(x)\,dx\),
\[
\boxed{\int_{\mathbb R^d}|\Phi_\omega(\xi)|\,d\xi
 \le (2\pi\sqrt e)^d.}                                      \tag{1}
\]
For \(d=3\), the constant is \((2\pi)^3e^{3/2}<1112\).
Original-coordinate affine modulations \(e^{i\theta_iX_i}\) are included.

In particular, for a light orthonormal three-frame
\(U=[p\ \ell\ v]\), the two-column frame \([\ell\ v]\)
also has row leverages at most \(1/2\). Thus, for every
\(\theta\in\mathbb R^n\),
\[
\sup_{s\in\mathbb R}
\iint_{\mathbb R^2}
\left|\mathbb E e^{i(\theta\cdot X+s p\cdot X+
                         y\ell\cdot X+zv\cdot X)}\right|
\,dy\,dz
\le(2\pi\sqrt e)^2.                                         \tag{2}
\]

**Proof.** Put \(h_i=f_i\omega_i\). Independence gives
\(\Phi_\omega(\xi)=\prod_i\widehat h_i(-u_i\cdot\xi)\).
Zero rows contribute factors at most one. For positive \(c_i\),
write \(u_i=\sqrt{c_i}w_i\), where \(\|w_i\|=1\).
Then \(\sum_i c_i w_iw_i^\mathsf T=I_d\) and
\(\sum_i c_i=d\). Geometric rank-one Brascamp–Lieb,
applied with exponents \(c_i\), yields
\[
\int_{\mathbb R^d}\prod_i
|\widehat h_i(-\sqrt{c_i}\,w_i\cdot\xi)|\,d\xi
\le\prod_{i:c_i>0}
\left[c_i^{-1/2}\int_\mathbb R
     |\widehat h_i(t)|^{1/c_i}dt\right]^{c_i}.                \tag{3}
\]
For \(q\ge2\), sharp scalar Hausdorff–Young and
\(\|h_i\|_{q/(q-1)}\le1\) give
\[
\int|\widehat h_i(t)|^qdt
\le\frac{2\pi}{\sqrt q}
 \left(\frac q{q-1}\right)^{(q-1)/2}
\le\frac{2\pi\sqrt e}{\sqrt q}.                             \tag{4}
\]
The last inequality uses \(\log(1+x)\le x\).
Since \(c_i\le1/2\), set \(q=1/c_i\) in (4).
Every bracket in (3) is at most \(2\pi\sqrt e\);
\(\sum c_i=d\) proves (1).
The uniform scalar Fourier shift \(s p_i+\theta_i\)
and the two-dimensional frame give (2). No projected
coordinates are declared independent. This is the geometric
Fourier mechanism of the archive's rank-two-fusion Lemma 3.1
and hub_decoupling Tool (T3), written here with its precise
full-frame provenance.

The full-leverage assumption is essential. For \(U=I_3\)
and three independent uniform \([0,1]\) inputs, the Fourier
transform is a product of sinc functions and is not in
\(L^1(\mathbb R^3)\); each row leverage is \(1\).

## What this says about the dependent-light fake

The dependent light density \(g(L,V,P)\) in
proofnet24/QFORM-density/interactive/
20260923T192452Z-independent-hub-all-projections-fake/REPORT.md
satisfies every numerical one-, two-, and three-dimensional
projection-density cap. But it consists of
\(512^{-1}\sum_k\mathbf1_{E_k}\) plus a smooth Gaussian filler.
At a smooth boundary portion of one shell \(E_k\), its density
jumps by exactly \(1/512\); other shells have separated
\(P\)-ranges. Thus \(g\) has no continuous representative.
If \(\widehat g\in L^1(\mathbb R^3)\), Fourier inversion
would supply a continuous representative. Therefore
\[
\boxed{\|\widehat g\|_{L^1(\mathbb R^3)}=\infty.}             \tag{5}
\]
Equation (1) excludes this exact law as a projection of
cap-one independent inputs with every **full three-frame**
row leverage at most \(1/2\).

It excludes even weak approximation by such diffuse projections:
pointwise convergence of characteristic functions and Fatou
would otherwise give
\(\|\widehat g\|_1
 \le\liminf_m\|\widehat g_m\|_1
 \le(2\pi\sqrt e)^3\), contradicting (5).
For any other probability density \(h\) satisfying (1), the
pointwise estimate
\(|\widehat g-\widehat h|\le\|g-h\|_1\) also gives, for each \(R>0\),
\[
\|g-h\|_1\ge
\frac{\bigl(\int_{[-R,R]^3}|\widehat g(\xi)|\,d\xi
 -(2\pi\sqrt e)^3\bigr)_+}{(2R)^3}.                         \tag{6}
\]
For some finite \(R\), (5) makes this positive; no numerical
distance is claimed.

## Open boundary

For the leakage phase \(e^{i\tau PL}\), the desired
\(J(\tau)=\sup_\theta\iint|
\mathbb E e^{i(\theta\cdot X+yL+zV+\tau PL)}|\,dy\,dz\)
has \(J(0)\le(2\pi\sqrt e)^2\) by (2).
At \(\tau\ne0\), the phase couples original coordinates and
destroys the product factorization in (3). Neither (1) nor
(2) proves \(J(\tau)\lesssim1+|\tau|\), and a six-coordinate
product counterexample to taking absolute values *conditional*
on \(P\) rules out that shortcut. The full rank-three
near-hub density problem remains open.