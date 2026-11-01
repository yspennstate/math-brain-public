SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B14, 2026-09-23T17:41:17Z.
attacking: whether the interval-only square-root slice estimate used in the heavy-null receiver can actually survive arbitrary distant fragmentation; isolate the precise localization obstruction and keep a target-valid control through the designated fleet04/B14 theorem.

# fleet03/B14 — finite-fragment counterexample to the interval-only single-hub receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T174117Z-fleet03-B14-QFORM-auto11b`  
Status: `NEW EXPLICIT INTERMEDIATE-RECEIVER COUNTEREXAMPLE / FULL QFORM OPEN / PARTNER CONTROL VALID`  
Continuity: this report does not prove full-target continuity.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Why this run changed mechanism

The fresh owner continuation explicitly corrects the heavy-null assembly: the interval-only frozen-slice square-root estimate proved in fleet02/B05 and fleet04/B14 r9 cannot be used as though it were a Borel-set profile for an arbitrary rough hub. In particular, the claimed rough-law heavy-null closure in those reports is unsupported by the displayed argument. The valid slice Fourier and interval estimates remain useful.

This run tests the missing implication directly. The result is negative and quantitative: **interval Frostman control alone is insufficient even when every original input law is a compact finite-fragment cap-one density.** The obstruction is exactly distant fragmentation. Thus no tail truncation, moment estimate, or fixed-fragment localization can repair that receiver interface without an additional product/Fourier structure.

The unrestricted QFORM conjecture remains open. The construction below has only two large eigenvalues and therefore is not a counterexample to the owner target.

## 2. The false abstract receiver implication

A frequently used single-hub template is

\[
T=2XL+Y,
\]

where `X` is independent of `(L,Y)` and has density at most one. Disintegrate the law of `(L,Y)` as

\[
\Pr\{L\in dl,Y\in dy\}=\mu_l(dy)\,dl.
\]

The challenged implication is:

> if for a universal `K` every interval `I` obeys
> \[
> \mu_l(I)\le K|I|^{1/2}\qquad\text{for a.e. }l,
> \]
> then `T` has a density bounded by a universal function of `K`.

This implication is false.

## 3. Explicit compact finite-fragment construction

Fix `0<epsilon<1/2` and let

\[
N=\lceil \epsilon^{-1}\rceil\ge2.
\]

Define the unit-measure finite-fragment set

\[
E_N=\bigcup_{k=1}^N I_k,
\qquad
I_k=[4k,4k+N^{-1}].
\tag{3.1}
\]

Let `X,X'` be independent with density

\[
f_N=\mathbf 1_{E_N}.
\]

Let `L` be independent and uniform on `[epsilon,epsilon+1]`, hence also cap one, and set

\[
Y=-2LX'.
\tag{3.2}
\]

Then

\[
T=2LX+Y=2L(X-X').
\tag{3.3}
\]

All three original coordinates `X,X',L` are independent cap-one laws. The two fragmented laws are compact finite unions of intervals; no limiting or noncompact construction is being used.

For `l\in[epsilon,epsilon+1]`, because the density of `L` is exactly one, the unnormalised slice measure `mu_l` is simply the conditional law of `Y` given `L=l`. Its density is

\[
h_l(y)=\frac1{2l}\mathbf 1_{-2lE_N}(y).
\tag{3.4}
\]

## 4. Uniform interval half-Frostman estimate with constant one

We prove

\[
\boxed{\mu_l(J)\le |J|^{1/2}}
\tag{4.1}
\]

for every interval `J` and every `l\in[epsilon,epsilon+1]`.

Scale `J` back by `-2l`. If `H=-J/(2l)` has length

\[
r=\frac{|J|}{2l},
\]

then

\[
\mu_l(J)=|E_N\cap H|.
\tag{4.2}
\]

Suppose first that `H` meets only one component of `E_N`. Then

\[
|E_N\cap H|\le \min\{r,N^{-1}\}.
\]

Since `N^{-1}\le\epsilon\le l`, if `r\le N^{-1}` then

\[
\frac{|E_N\cap H|}{\sqrt{2lr}}
\le\sqrt{\frac r{2l}}
\le\frac1{\sqrt2},
\]

while if `r\ge N^{-1}` then

\[
\frac{|E_N\cap H|}{\sqrt{2lr}}
\le\frac{N^{-1}}{\sqrt{2l/N}}
=\frac1{\sqrt{2lN}}
\le\frac1{\sqrt2}.
\]

Now suppose `H` meets `m>=2` components. Adjacent components of `E_N` are separated by at least `4-1/N>=3`, hence

\[
r\ge 3(m-1).
\tag{4.3}
\]

Also `|E_N\cap H|\le m/N`. Therefore, using again `lN>=1`,

\[
\frac{|E_N\cap H|}{\sqrt{2lr}}
\le
\frac{m}{N\sqrt{6l(m-1)}}
\le
\frac{m}{\sqrt{6N(m-1)}}.
\tag{4.4}
\]

For `2\le m\le N`,

\[
\frac{m^2}{N(m-1)}\le\frac{N}{N-1}\le2,
\]

so the last expression is at most `1/sqrt(3)<1`. Combining the two cases and recalling `|J|=2lr` proves (4.1).

Thus the frozen slices satisfy the exact interval estimate used by the heavy-null receiver, with the fixed constant `K=1`, uniformly as `epsilon->0` and `N->infinity`.

## 5. Nevertheless the output density grows logarithmically

The difference `D=X-X'` has density

\[
g_D(t)=\int \mathbf 1_{E_N}(x)\mathbf 1_{E_N}(x-t)\,dx,
\]

hence

\[
g_D(0)=|E_N|=1.
\tag{5.1}
\]

Conditioned on `L=l`, `T=2lD`, so

\[
p_{T\mid L=l}(0)=\frac1{2l}.
\tag{5.2}
\]

Averaging over the unit-density law of `L` gives the exact value

\[
\boxed{
p_T(0)=\frac12\int_\epsilon^{\epsilon+1}\frac{dl}{l}
=\frac12\log\frac{1+\epsilon}{\epsilon}.
}
\tag{5.3}
\]

Consequently

\[
\sup_{\epsilon\in(0,1/2)}\|p_T\|_\infty=\infty
\]

although the slice interval constant in (4.1) is identically one.

Equivalently, for any requested height `M`, choosing

\[
0<\epsilon<\frac1{e^{2M}-1}
\]

forces `p_T(0)>M`.

The mechanism is transparent at the Borel-set level. For the fragmented set

\[
B_l=-2lE_N,
\]

one has

\[
\mu_l(B_l)=1,
\qquad |B_l|=2l,
\]

so no bound of the form `mu_l(B)<=C|B|^{1/2}` with universal `C` can follow from the interval estimate when `l` is small. The rough hub sees the whole union of separated fragments simultaneously.

## 6. This is a genuine quadratic-form interface counterexample, not a QFORM counterexample

Equation (3.3) is the quadratic form on the three independent original coordinates `(L,X,X')` with matrix

\[
A_2=
\begin{pmatrix}
0&1&-1\\
1&0&0\\
-1&0&0
\end{pmatrix}.
\tag{6.1}
\]

Its eigenvalues are

\[
\sqrt2,-\sqrt2,0.
\]

Hence it has only two eigenvalues of modulus at least one. The logarithmic blow-up is exactly the mandatory rank-two opposite-sign control and does not refute the three-large-eigenvalue conjecture.

What it refutes is the **intermediate inference** from interval-only `1/2`-Holders/Frostman slice control to a universal rough-hub `L^infinity` receiver.

## 7. Designated partner fleet04/B14 applied at an actual inequality

The completed partner theorem `QFORM-SCALE-COVARIANT-CONJUGATE-SHEAR-v1` is available in

`yspennstate/math-open-problems@ac574a6ed1858634443bf76098e21c56dd8114c5`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260923T051013Z-fleet04-B14-scale-shear-r7/REPORT.md`.

It gives, for independent cap-one inputs,

\[
Q=2cU_1U_2+\frac d2((1-\alpha)X+(1+\alpha)X'-\beta)^2+\text{affine terms},
\]

an essential-density bound `|c|^{-1}H(theta)` with

\[
\theta=\frac{|c|}{|d|(1+|\alpha|)^2}.
\]

Apply it to the **same fragmented laws** `X,X'~1_{E_N}`, arbitrary cap-one `U_1,U_2`, and

\[
c=d=1,\qquad \alpha=0.
\]

Then `theta=1` and the partner theorem gives the concrete target-valid inequality

\[
\boxed{
\left\|p_{\,2U_1U_2+\frac12(X+X'-\beta)^2}\right\|_\infty
\le 4+2\log 8
<8.159
}
\tag{7.1}
\]

uniformly in `N`, `epsilon`, every translation `beta`, and the arbitrarily distant fragment locations.

The homogeneous matrix in (7.1) has nonzero eigenvalues `1,-1,1`, so (7.1) is inside the exact three-large-eigenvalue target. This control is important: the fragmented construction above exposes a false receiver interface, while the completed partner's direct small-ball/shear mechanism remains uniformly valid on the same rough input geometry.

The partner's earlier finite-mixture compiler is also directly relevant: the present negative example already lies in the compact finite-fragment indicator class that suffices for any positive affine-uniform localization theorem. Therefore this failure cannot be blamed on passage to general rough laws or on an approximation artifact.

## 8. Consequences for current fleet claims

1. The fleet04/B14 r9 slice estimate
   \[
   \mu_{l,g}(I)\le C_*|\gamma|^{-1/2}|I|^{1/2}
   \]
   remains a valid interval statement in its proved scope.
2. The step that feeds only that interval estimate into an arbitrary rough-hub receiver is not justified and, as an abstract inference, is false by Sections 3--5.
3. Any earlier fleet03/B14 corollary that used the same interval-only heavy-null receiver as a complete rough-law `L^infinity` endpoint must be treated as conditional/unsupported at that endpoint. In particular, the whole-support chirp and hybrid receiver reports remain valid in their independent Plancherel/Lp components, but no conclusion should silently inherit the corrected r9 heavy-null closure.
4. A repair must keep stronger product/Fourier provenance through the hub integration, or establish a genuine `L^2`/Borel-profile bound on the frozen slice; interval Frostman control alone is insufficient.
5. Distant fragmentation is essential to this obstruction. There is no fixed fragment-count or bounded-diameter localization consistent with the interface.

## 9. Next mathematical step

The most promising repair is to retain the original-coordinate product Fourier representation of the slice while integrating the hub simultaneously, instead of first collapsing the slice to the scalar interval bound (4.1). In the heavy-null normal form this means estimating

\[
\int dl\,\widehat f_0(2tl)\,\widehat\mu_l(t)
\]

directly from the translated two-dimensional Brascamp--Lieb integrand before absolute values erase the fragment phase geometry. This is a genuinely joint estimate and is consistent with the source correction against pointwise one-dimensional decay.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains OPEN.
