# account02/B12 — invariant spectral-subspace shield under an arbitrary dense tail

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T125143Z-account02-B12-QFORM-auto11`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / PARTNER APPLIED / e5f D5 APPLIED / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and new mechanism

The owner target remains: if `X_1,...,X_n` are independent real random variables with densities bounded by one and `A=A^T` has at least three eigenvalues of absolute value at least one, prove a universal bound on the essential density of `X^TAX`, or give a valid counterexample. No moment, support, log-concavity, diagonal-basis, or post-rotation-independence assumption is permitted.

This run changes mechanism from the preceding B12 singular-reserve arguments. Instead of spending extra singular directions against hostile added spectrum, it protects a **diffuse invariant physical subspace**. Inside that subspace the matrix may be changed by an arbitrary symmetric operator of unbounded norm and arbitrary rank. A genuinely dense full-rank tail is then paid only through matrix operator norm, by controlling how much the final high-spectral subspace can leak out of the diffuse shield. The probabilistic receiver is the already-proved one-scale spectral-window theorem in ORIGINAL coordinates.

The full conjecture is not proved: bare `s_3(A)>=1` does not force the diffuse shield below.

## 2. Sources consumed

Required source lineage `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:

- `RESULTS.md` — current compatible version read;
- `FOURIER_ROUTE_REPORT.md` — current compatible version read and the pinned e5f version checked;
- `COUNTEREXAMPLE_SEARCH.md` — current compatible version read.

The completed result used below is **D5**:

\[
\|p_Q\|_\infty\le 5\sqrt{2e}\,Z_5^{-1/10},
\qquad Z_5=e_5(M^TM),
\tag{2.1}
\]

for any actual original-coordinate cross block `M=A[I,J]`, with no marginal condition. In particular, if `s_5(M)>=sigma>0`, then

\[
\|p_Q\|_\infty\le {5\sqrt{2e}\over\sigma}.
\tag{2.2}
\]

The spectral-window receiver used for the new theorem is the completed report
`math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`:
if `Pi` is the spectral projection of the **final** matrix onto `|lambda|>=1/64`, the final matrix has at least three eigenvalues of modulus at least one, and

\[
\max_i \Pi_{ii}\le {1\over32},
\tag{2.3}
\]

then the full quadratic form has a continuous `C_0` density and

\[
\|p_Q\|_\infty\le {288\sqrt{3e}\over13}<64.
\tag{2.4}
\]

The latest designated partner account03/B12 result consumed is
`math-open-problems@e25e41c0ef49da042d5969a2949e5c8fc5faf95b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T114533Z-qform-eigenvalue-r32/REPORT.md`:
for symmetric `B,R` and `j+r<=m`,

\[
s_j(B+R)\ge s_{j+r}(B)-s_{r+1}(R).
\tag{2.5}
\]

Its physical-core receiver is applied in Section 7.

## 3. Outer spectral-projector leakage lemma

### Theorem 3.1 (`QFORM-OUTER-PROJECTOR-LEAKAGE-v1`)

Let `B=B^T` on `R^n`. Let `P` be an orthogonal projection which reduces `B`, and put `Q=I-P`. Assume

\[
\|QBQ\|_{\rm op}\le\beta<a.
\tag{3.1}
\]

Let

\[
A=B+T,\qquad T=T^T,\qquad \|T\|_{\rm op}\le\delta,
\tag{3.2}
\]

and let

\[
\Pi=1_{\{|A|\ge a\}}
\tag{3.3}
\]

be the spectral projection of the **actual final matrix** onto eigenvalues of magnitude at least `a`. Then

\[
\boxed{
\|Q\Pi\|_{\rm op}
\le {\sqrt2\,\delta\over a-\beta}.
}
\tag{3.4}
\]

Consequently, if

\[
\mu:=\max_i P_{ii},
\tag{3.5}
\]

then every final high-window coordinate leverage satisfies

\[
\boxed{
\sqrt{\Pi_{ii}}
\le \sqrt{P_{ii}}+{\sqrt2\,\delta\over a-\beta},
\qquad
\max_i\Pi_{ii}
\le
\left(\sqrt\mu+{\sqrt2\,\delta\over a-\beta}\right)^2.
}
\tag{3.6}
\]

No bound at all is imposed on `PBP`: it may have arbitrary rank, arbitrary signs, and arbitrarily large norm.

### Proof

Split the final outer spectral projection into its positive and negative pieces

\[
\Pi_+=1_{[a,\infty)}(A),
\qquad
\Pi_-=1_{(-\infty,-a]}(A),
\qquad
\Pi=\Pi_++\Pi_-.
\tag{3.7}
\]

Because `P` reduces `B`, so does `Q`, and the compression

\[
B_Q:=QBQ\big|_{Q\mathbb R^n}
\tag{3.8}
\]

has spectrum in `[-beta,beta]`.

For the positive piece set

\[
X_+=Q\Pi_+ : \operatorname{Ran}\Pi_+\to\operatorname{Ran}Q,
\qquad
A_+=A\big|_{\operatorname{Ran}\Pi_+}.
\]

Since `A_+>=aI`, the identity `A=B+T` and invariance of `Ran Pi_+` give the Sylvester equation

\[
B_QX_+-X_+A_+=-QT\Pi_+.
\tag{3.9}
\]

The spectra are ordered with a gap `a-beta`. The convergent semigroup formula

\[
X_+
=
\int_0^\infty e^{tB_Q}(QT\Pi_+)e^{-tA_+}\,dt
\tag{3.10}
\]

therefore yields

\[
\|X_+\|_{\rm op}
\le {\delta\over a-\beta}.
\tag{3.11}
\]

For the negative piece, `A_-:=A|_{Ran Pi_-}<=-aI`. The same Sylvester identity, now integrated in the opposite direction (equivalently apply the preceding argument to `-B,-A`), gives

\[
\|Q\Pi_-\|_{\rm op}
\le {\delta\over a-\beta}.
\tag{3.12}
\]

For any vector `x`, the vectors `Pi_+x` and `Pi_-x` are orthogonal. Hence by (3.11)--(3.12),

\[
\begin{aligned}
\|Q\Pi x\|
&\le \|Q\Pi_+x\|+\|Q\Pi_-x\|\\
&\le {\delta\over a-\beta}
   (\|\Pi_+x\|+\|\Pi_-x\|)\\
&\le {\sqrt2\,\delta\over a-\beta}\|\Pi x\|
\le {\sqrt2\,\delta\over a-\beta}\|x\|,
\end{aligned}
\]

proving (3.4).

Finally

\[
\begin{aligned}
\sqrt{\Pi_{ii}}
&=\|\Pi e_i\|\\
&\le \|\Pi Pe_i\|+\|\Pi Qe_i\|\\
&\le \|Pe_i\|+\|\Pi Q\|_{\rm op}\\
&=\sqrt{P_{ii}}+\|Q\Pi\|_{\rm op},
\end{aligned}
\]

which together with (3.4) proves (3.6). QED.

## 4. Diffuse invariant-subspace QFORM shield

### Theorem 4.1 (`QFORM-DIFFUSE-INVARIANT-SPECTRAL-SHIELD-v1`)

Let `P` be an orthogonal projection on ORIGINAL coordinates and let

\[
B=B^T,\qquad PB=BP,
\tag{4.1}
\]

satisfy

\[
\|(I-P)B(I-P)\|_{\rm op}\le\beta<{1\over64},
\qquad
\max_i P_{ii}\le\mu.
\tag{4.2}
\]

Let `T=T^T` be a completely arbitrary dense perturbation with

\[
\|T\|_{\rm op}\le\delta.
\tag{4.3}
\]

Assume

\[
\boxed{
\sqrt\mu+
{\sqrt2\,\delta\over 1/64-\beta}
\le {1\over\sqrt{32}}
}
\tag{4.4}
\]

and that `B` has at least three singular values at least `1+delta`:

\[
s_3(B)\ge1+\delta.
\tag{4.5}
\]

Then for every independent product source with marginal density caps one,

\[
\boxed{
\|p_{X^T(B+T)X}\|_\infty
\le {288\sqrt{3e}\over13}<64,
}
\tag{4.6}
\]

and the density is continuous and vanishes at infinity.

### Proof

Weyl gives

\[
s_3(B+T)\ge s_3(B)-\delta\ge1,
\tag{4.7}
\]

so the final matrix is in the exact owner target class. Apply Theorem 3.1 with `a=1/64`. Its final high-window spectral projection `Pi` satisfies

\[
\max_i\Pi_{ii}
\le
\left(\sqrt\mu+{\sqrt2\delta\over1/64-\beta}\right)^2
\le{1\over32}.
\tag{4.8}
\]

The completed spectral-window theorem (2.3)--(2.4) now applies directly to the actual final matrix. QED.

### Why this is an additional-eigenvalue theorem

Suppose a baseline `A_0` reduces `P` and its complement obeys the small bound in (4.2). Let

\[
S=PSP
\tag{4.9}
\]

be **any** symmetric operator supported inside the shield. Then `B=A_0+S` still reduces `P`, and

\[
(I-P)B(I-P)=(I-P)A_0(I-P).
\]

Thus the norm, rank, inertia and spectral multiplicities of `S` do not appear in (4.4). The update may contain arbitrarily many positive and negative eigenvalues of arbitrarily large magnitude and arbitrary mixing inside `Ran P`.

Literal eigenvalue replacement is a special case. If `Ran P` is a degenerate eigenspace of `A_0`, then adding an arbitrary symmetric matrix inside a chosen part of that eigenspace replaces those baseline eigenvalues by an arbitrary multiset of real eigenvalues, while (4.6) remains uniform as long as three protected modes keep (4.5).

The dense tail `T` is never interpreted as a small random variable. Only the final deterministic spectral projector is controlled.

## 5. Exact target-class family with arbitrarily many arbitrary replacements

Let `m` be a power of two and let `h_1,...,h_m` be the normalized Sylvester-Hadamard basis of `R^m`. On `R^{2m}=R^I\oplus R^J` define

\[
g_k={1\over\sqrt2}(h_k,h_k),\qquad k=1,\ldots,d,
\tag{5.1}
\]

and let

\[
V=\operatorname{span}\{g_1,\ldots,g_d\},
\qquad P=P_V.
\tag{5.2}
\]

Every coordinate has the same leverage

\[
P_{ii}={d\over2m}.
\tag{5.3}
\]

Choose `m>=128d`, so

\[
\max_iP_{ii}\le{1\over256}.
\tag{5.4}
\]

Take the baseline

\[
A_0
=4\sum_{k=1}^5g_kg_k^T
+2\sum_{k=6}^dg_kg_k^T,
\tag{5.5}
\]

and write `W=span{g_6,...,g_d}`. For an **arbitrary** symmetric operator `Theta` on `W`, set

\[
S_\Theta=U_W\Theta U_W^T,
\qquad
B_\Theta=A_0+S_\Theta.
\tag{5.6}
\]

Because `A_0|_W=2I_W`, the eigenvalues on `W` become exactly the arbitrary eigenvalues of

\[
2I_W+\Theta.
\tag{5.7}
\]

Thus `d-5` baseline eigenvalues are replaced simultaneously by arbitrary real values; they may independently become smaller, larger, cross zero, acquire either sign, or tend to either infinity. Off-diagonal `Theta` additionally permits arbitrary mixing inside the degenerate baseline eigenspace.

The five protected vectors `g_1,...,g_5` retain eigenvalue `4`, and `B_Theta` vanishes on `V^perp`. Hence

\[
\beta=0,\qquad s_3(B_\Theta)\ge4.
\tag{5.8}
\]

Now add **any** symmetric full-rank dense matrix `T` satisfying

\[
\|T\|_{\rm op}\le {1\over1024}.
\tag{5.9}
\]

With `a=1/64`, Theorem 3.1 gives

\[
\|P_{V^\perp}\Pi\|_{\rm op}
\le {\sqrt2(1/1024)\over1/64}
={\sqrt2\over16}.
\tag{5.10}
\]

Therefore

\[
\max_i\Pi_{ii}
\le
\left({1\over16}+{\sqrt2\over16}\right)^2
={3+2\sqrt2\over256}
=0.0227672934560\ldots
<{1\over32}.
\tag{5.11}
\]

The final matrix also has at least five eigenvalues at least

\[
4-{1\over1024}>1.
\tag{5.12}
\]

Hence the spectral-window theorem gives

\[
\boxed{
\|p_{X^T(B_\Theta+T)X}\|_\infty
\le {288\sqrt{3e}\over13}
=63.2640518778\ldots
}
\tag{5.13}
\]

uniformly in `d`, in every entry/eigenvalue of `Theta`, in the dense tail `T`, and in every admissible product law.

This already proves the requested dense-tail-plus-arbitrary-spectrum stability family by a mechanism independent of low-rank cross-footprint reserve.

## 6. Required e5f completed result applied to an actual final inequality

The same family gives a direct equation-level application of the completed e5f D5 theorem.

Across the original-coordinate cut `I|J`, the contribution of a protected mode is

\[
4g_kg_k^T[I,J]=2h_kh_k^T.
\tag{6.1}
\]

The arbitrary update `S_Theta` acts only on the orthogonal span of `h_6,...,h_d`, so it cannot alter the five protected cross singular directions `h_1,...,h_5`. Therefore, before the dense tail,

\[
s_5(B_\Theta[I,J])\ge2.
\tag{6.2}
\]

The final cross perturbation from `T` has operator norm at most `1/1024`, so Weyl gives

\[
\boxed{
s_5((B_\Theta+T)[I,J])
\ge2-{1\over1024}.
}
\tag{6.3}
\]

Consequently

\[
Z_5=e_5(M^TM)
\ge\prod_{j=1}^5s_j(M)^2
\ge\left(2-{1\over1024}\right)^{10}.
\tag{6.4}
\]

Substituting (6.4) into the completed D5 theorem (2.1) gives the concrete density inequality

\[
\boxed{
\|p_{X^T(B_\Theta+T)X}\|_\infty
\le
{5\sqrt{2e}\over 2-1/1024}
=5.83195758953\ldots .
}
\tag{6.5}
\]

D5 is stronger than the ridge-window bound on this deliberately five-protected-mode family. The significance of Theorem 4.1 is different: it needs only diffuse confinement of the entire final high spectral subspace and can work when no five-volume certificate is available. Equation (6.5) is included because the owner request requires an actual use of a completed result from the e5f source line, not a citation-only mention.

## 7. Designated account03/B12 result applied to a real dense-tail core inequality

The latest account03/B12 theorem (2.5) also combines cleanly with a dense tail at matrix level.

Take an actual physical core `H` of size eight with baseline

\[
B_0=2I_8.
\tag{7.1}
\]

Let `R=R^T` be an arbitrary added spectral packet satisfying only

\[
s_3(R)\le{1\over4};
\tag{7.2}
\]

its two largest singular values are completely unrestricted in magnitude, sign and orientation. Add an arbitrary dense symmetric `T` with

\[
\|T\|_{\rm op}\le{1\over8}.
\tag{7.3}
\]

Lipschitz continuity of singular values gives

\[
s_3(R+T)
\le s_3(R)+\|T\|_{\rm op}
\le {3\over8}.
\tag{7.4}
\]

Apply the partner theorem with `r=2`, `j=3`. Since `s_5(B_0)=2`,

\[
\boxed{
s_3(B_0+R+T)
\ge 2-{3\over8}
={13\over8}.
}
\tag{7.5}
\]

Conditioning on every coordinate outside the ORIGINAL physical core preserves the eight retained independent cap-one inputs. The current physical-core receiver therefore yields

\[
\boxed{
\|p_Q\|_\infty
\le
{2\sqrt{48\pi}\over13/8}
=15.11374830198\ldots .
}
\tag{7.6}
\]

No convolution with a supposedly independent quadratic remainder is used. The dense matrix `T` is paid only through (7.4).

## 8. Why small matrix norm is not used probabilistically

Nothing above asserts that `X^TTX` is small when `||T||_op` is small. That principle is false uniformly over the owner source class: already for

\[
T=\delta e_1e_1^T,
\qquad X_1\sim\operatorname{Unif}[R,R+1],
\]

one has

\[
X^TTX=\delta X_1^2\ge\delta R^2
\]

almost surely. The only roles of `delta` in this report are deterministic: spectral-subspace leakage, Weyl control of actual final singular values, and the partner's actual physical-core inequality.

Likewise, no spectral rotation is used as a probabilistic change of variables. Hadamard vectors in Section 5 define matrices only; all probabilistic receivers condition or decouple in original coordinates.

## 9. First unpaid implication

The new theorem closes a genuine additional-eigenvalue regime: an arbitrarily complicated and arbitrarily large signed spectral operator is harmless if it is confined to a sufficiently diffuse invariant original-coordinate subspace, while the complement is spectrally below the receiver window and the dense tail is small enough to keep final high-window leverage below `1/32`.

What is still unpaid is the structural implication from bare `s_3(A)>=1`. In the current no-pivot survivor one must force at least one of:

1. a diffuse invariant/approximately invariant spectral shield satisfying a quantitative version of (4.4);
2. an actual D5 / three-volume / collective-tail cross certificate;
3. a bounded physical core with enough singular reserve for the account03/B12 compiler;
4. one of the already-paid hub, ridge, grouped-bank, physical-pair, physical-triple, or scalar-Schur exits.

Known diffuse exact-rank-three and singleton-plus-two-bank constructions prevent replacing this with a claim that one uniformly good bounded physical core or one uniformly rank-three cross cut always exists.

The full QFORM conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**.
