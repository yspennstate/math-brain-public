SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B12, 2026-09-24T02:13:41Z.
attacking: exact low-rank spectral resonances by using the transverse positive Gram term to repair the kernel of the relative gain on an actual original-coordinate carrier.

# B12 — transverse repair of exact spectral resonances

Programme: QFORM-DENSITY-3EIG-20260922  
Status: PROVED SUPPORTING THEOREM / FULL QFORM OPEN.  
Continuity: not claimed; the density conclusion below is essential boundedness.

The target remains the unrestricted quadratic-form problem for independent original coordinates with one-dimensional density caps at one. No moment, support, smoothness, Gaussian, log-concavity, or post-rotation independence hypothesis is added.

## 1. Input from completed account01/B12

Use account01/B12, commit 6bbaa340406b8febd0270e186cc79040af81872a. Let \(H\) be \(m\) literal original coordinates, let \(P:\mathbb R^m\to\mathbb R^n\) be their coordinate embedding, and let
\[
M_0=A_0P,\qquad G_0=M_0^TM_0>0.
\]
For a signed spectral packet \(E=U\Theta U^T\), account01 defines
\[
V=P^TU,\quad R=M_0^\dagger U,\quad
U_\perp=(I-M_0M_0^\dagger)U,\quad
L=I_m+R\Theta V^T,
\]
and proves the exact identity
\[
(A_0+E)P=M_0L+U_\perp\Theta V^T                         \tag{1.1}
\]
with orthogonal codomain components. Hence, writing
\[
W=U_\perp\Theta V^T,
\]
one has the actual final-carrier Gram identity
\[
((A_0+E)^2)[H,H]=L^TG_0L+W^TW.                              \tag{1.2}
\]
Account01 used the first term to prove nonresonant stability. The new point here is that the second term repairs an exact resonance of \(L\).

## 2. Deterministic transverse-repair lemma

Let \(K=\ker L\), \(q=\dim K\), and let \(K^\perp\) denote its Euclidean orthogonal complement. Assume \(q\ge1\). Define
\[
a=s_{m-q}\!\left(G_0^{1/2}L\right)>0,
\qquad
b=\inf_{\substack{x\in K\\\|x\|=1}}\|Wx\|>0,
\qquad
M=\|W\|_{\rm op}.                                             \tag{2.1}
\]
Then
\[
\boxed{
s_m\bigl((A_0+E)P\bigr)
\ge
\frac{ab}{2(a+b+M)}.
}                                                               \tag{2.2}
\]

Proof.  Put \(F x=(G_0^{1/2}Lx,Wx)\). By (1.2),
\[
\|Fx\|^2=\|(A_0+E)Px\|^2.
\]
For a unit vector \(x=x_0+x_1\) with \(x_0\in K\), \(x_1\in K^\perp\), write \(t=\|x_1\|\). Then
\[
\|G_0^{1/2}Lx\|\ge at
\]
and
\[
\|Wx\|\ge b\|x_0\|-Mt\ge b(1-t)-Mt=b-(b+M)t.                 \tag{2.3}
\]
If \(t\ge b/[2(a+b+M)]\), the first component is at least
\[
ab/[2(a+b+M)].
\]
If \(t<b/[2(a+b+M)]\), then (2.3) is larger than \(b/2\), hence again at least the same quantity. Taking the infimum over unit \(x\) proves (2.2). QED.

The hypothesis \(b>0\) is exactly the account01 collapse criterion:
\[
\ker L\cap\ker W=\{0\}.
\]
Thus an exact zero of the finite-dimensional Woodbury resonance matrix is not a carrier collapse unless the transverse packet also vanishes on the resonant direction.

## 3. Local dense-tail stability

Let the actual matrix be
\[
A=A_0+U\Theta U^T+E_{\rm low}+S+T,
\]
where
\[
\|E_{\rm low}\|_{\rm op}\le h,\qquad SP=0,\qquad \|TP\|_{\rm op}\le\delta.
\]
No norm, rank, sign, or spectral restriction is imposed on the complementary part of \(S\), and \(\|T\|_{\rm op}\) may be arbitrarily large. Rectangular Weyl and (2.2) give the actual principal-block gate
\[
\boxed{
\sqrt{\lambda_m((A^2)[H,H])}
=s_m(AP)
\ge
\left[
\frac{ab}{2(a+b+M)}-h-\delta
\right]_+.
}                                                               \tag{3.1}
\]
This is a deterministic coefficient-matrix statement. It never treats a small matrix as a small random quadratic error under unbounded inputs.

## 4. Exact resonant target family

Take \(n=12\), \(H=\{1,\ldots,6\}\), and
\[
A_0=
\begin{pmatrix}
0&2I_6\\
2I_6&0
\end{pmatrix}.
\]
Then \(M_0=A_0P_H\) has six singular values equal to \(2\).

Set
\[
u=(e_1+e_7)/\sqrt2,\qquad E=-4uu^T.
\]
Here
\[
V=2^{-1/2}e_1,\qquad R=2^{-3/2}e_1,
\]
so
\[
L=I_6+R(-4)V^T=I_6-e_1e_1^T.                                 \tag{4.1}
\]
Thus \(L\) is exactly singular and the account01 nonresonance lower bound through \(s_6(L)\) is zero.

But
\[
U_\perp=2^{-1/2}e_1,\qquad
W=U_\perp(-4)V^T=-2e_1e_1^T.                                 \tag{4.2}
\]
Therefore \(K=\operatorname{span}\{e_1\}\), and the transverse term repairs the resonance exactly. Directly,
\[
(A_0+E)e_1=-2e_1,\qquad
(A_0+E)e_j=2e_{6+j}\quad(2\le j\le6),
\]
so these six carrier columns are mutually orthogonal and
\[
\boxed{
s_6((A_0+E)P_H)=2,\qquad
\lambda_6(((A_0+E)^2)[H,H])=4.
}                                                               \tag{4.3}
\]

Now add simultaneously any symmetric packets satisfying
\[
\|E_{\rm low}\|_{\rm op}\le1/32,\qquad SP_H=0,\qquad
\|TP_H\|_{\rm op}\le1/64.
\]
The outside spectrum of \(S\) and the outside-outside spectrum of \(T\) are unrestricted. For the actual final matrix,
\[
\boxed{
s_6(AP_H)\ge2-\frac1{32}-\frac1{64}=\frac{125}{64}.
}                                                               \tag{4.4}
\]
Consequently \(s_3(A)\ge s_6(A)\ge s_6(AP_H)\ge125/64>1\), so this is genuinely inside the original target class.

## 5. Completed six-mode theorem applied at an equation

Apply the completed account02/B12 theorem QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1, source commit e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004, to the actual gate (4.4). With
\[
m=6,\qquad N={6\choose2}=15,\qquad g=s=\frac{125}{64},
\]
its four exhaustive constants are
\[
653.3974,\qquad96.5098,\qquad343.1921,\qquad6.8925.
\]
Hence every independent cap-one product law satisfies
\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}<654.
}                                                               \tag{5.1}
\]
This holds uniformly at an exact destructive Woodbury resonance, with arbitrary carrier-invisible complementary spectrum and a dense tail charged only through \(\|TP_H\|\).

The account01/B12 theorem is also applied literally: its identity (1.2), rather than only its nonresonant consequence, is the equation that supplies the repaired carrier. At the rank-one specialization above, the relative gain is exactly singular, while its transverse term gives the full missing singular value.

## 6. Scope and remaining gap

The unrestricted conjecture remains open. This theorem removes the need to exclude exact low-rank signed-packet resonances whenever the transverse packet is quantitatively injective on \(\ker L\). The remaining structural problem is to extract, from \(s_3(A)\ge1\) alone, a bounded original-coordinate carrier for which either:

1. the account01 relative gain is quantitatively nonresonant;
2. the transverse repair parameter \(b\) is quantitative on its resonance kernel; or
3. another already-paid physical-pair, grouped-bank, ridge, Schur, or diffuse-volume exit applies.

Continuity is not claimed by this branch. No counterexample to the full conjecture is produced.

## Source pins

- Latest account01/B12 input: math-open-problems@6bbaa340406b8febd0270e186cc79040af81872a.
- Completed account02/B12 compiler: math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004.
- Required Claude starting package: math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837.
