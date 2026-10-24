# account03/B14 r13 — rough-law audit and a 361 constant at multiplicity nine

**Objective:** `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
**Run:** `20260924T153814Z-account03-B14-fixedmult-r13`  
**Role:** rough densities, measurable versions, Tonelli, conditional laws; translations/localization  
**Execution label:** `WITHOUT_VERIFIED_BRAIN`

## Source pin

Latest standalone candidate audited/retuned here:

- repository: `yspennstate/math-open-problems`;
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`;
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`;
- git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`;
- SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`;
- source length: 955 lines.

I also read the package `README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json`. The exact nine/400 source has subsequently received separate complete end-to-end PASS reconstructions; this report does not self-award any owner/release label.

## Result

The proof architecture in the pinned nine-eigenvalue manuscript admits the following stricter rational retuning.

### Theorem (nine large eigenvalues, constant 361)

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K`, let `A=A^T` be arbitrary, let `b` and `c` be arbitrary, and suppose

\[
 s_9(A)\ge s>0.
\]

Then

\[
 Q=X^TAX+b^TX+c
\]

has a density satisfying

\[
 \boxed{\|p_Q\|_{\infty,\mathrm{ess}}<361\,\frac{K^2}{s}.}
\]

No moment, support, smoothness, iid, sign, exact-rank, leverage, Gaussian, log-concavity, or diagonal-basis hypothesis is added. The conclusion is an essential density bound. This report does **not** prove global continuity.

The new ingredients are only a parameter retuning and exact rational certificates; all analytic lemmas are the ones proved in the pinned manuscript.

## 1. Retuned parameters

Normalize first to `K=s=1`. Use

\[
 d=\frac3{40},\qquad
 p=\frac{57}{20000},\qquad
 h=\frac{823}{10000},\qquad
 \kappa=h^2.
\]

A pivot means either a scalar entry `|A_ii|>=d` or a principal two-coordinate determinant of modulus at least `p`.

If there is no pivot, then

\[
 |A_{ii}|<d,
 \qquad
 |A_{ij}|^2<p+d^2
 =\frac{339}{40000}.
\]

Since

\[
 \left(\frac{921}{10000}\right)^2-rac{339}{40000}
 =\frac{741}{10^8}>0,
\]

we may use the strict off-diagonal bound

\[
 |A_{ij}|<c:=\frac{921}{10000}.
\]

The volume-sampled interpolation/completion proof from the source changes only through this numerical `c` and the error scale `h`. For `r=1,2`, its diagonal-dominance margins become

\[
 1-d-r c-(r+1)^2h
 =\begin{cases}
 5037/10000,&r=1,\\[2mm]
 1/10000,&r=2.
 \end{cases}
\]

Both are positive. The `r=0` branch also closes because `d+h<1`. Therefore the source proof of the no-pivot spectral-to-volume proposition remains valid verbatim in structure:

\[
 s_{4k-3}(A)\ge1,\quad k\le3,
 \qquad\Longrightarrow\qquad
 V_k(A)\ge h^{2k}.
\]

A fair coordinate cut hence gives a literal crossing block with

\[
 Z_k\ge4^{-k}h^{2k}.
\]

No rotation of random coordinates is used.

## 2. Exact upper bound for the order-three receiver

The manuscript proves

\[
 C_3=3\sqrt2\,e\,(9/2)^{1/6}
\]

for the marginal-free order-three crossing receiver. We need a slightly sharper elementary rational upper bound than the manuscript's convenient `C_3<15`.

The following inequalities are rigorous:

\[
 \sqrt2<\frac{283}{200},
 \qquad
 e<\frac{2719}{1000},
 \qquad
 (9/2)^{1/6}<\frac{257}{200}.
\]

For the middle one, the exponential series through degree eight plus the geometric tail estimate gives

\[
 e<\sum_{j=0}^{8}\frac1{j!}+\frac{10}{9\,9!}
 =\frac{8877691}{3265920}
 <\frac{2719}{1000}.
\]

The other two follow by squaring and sixth powers; explicitly

\[
 (257/200)^6-9/2
 =\frac{136807515649}{64000000000000}>0.
\]

Hence

\[
 C_3<
 3\frac{283}{200}\frac{2719}{1000}\frac{257}{200}
 =\frac{593266767}{40000000}.
\]

For the no-pivot `s_9` branch,

\[
 Z_3^{-1/6}\le\frac2h,
\]

so

\[
 \|p_Q\|_\infty
 <\frac{2}{h}\frac{593266767}{40000000}
 =\frac{593266767}{1646000}
 =360.4293845\ldots<361.
\]

The exact margin is

\[
 361-\frac{593266767}{1646000}
 =\frac{939233}{1646000}>0.
\]

## 3. Five-direction half potential under the same parameters

The source proves the order-two receiver constant `C_2<14`. The no-pivot `s_5` branch therefore satisfies

\[
 \sup_a\mathbb E|Q-a|^{-1/2}
 \le C_2\sqrt{2/h}<70,
\]

because `h=823/10000>2/25`.

For a pair pivot, the source's full pair half-potential gives

\[
 16p^{-1/4}<70.
\]

Indeed this is equivalent to `p>(8/35)^4`, and

\[
 p\,35^4-8^4
 =\frac{5785}{32}>0.
\]

Thus in the five-direction proposition the no-pivot and pair-pivot alternatives both cost less than `70`.

## 4. Scalar-pivot branches

Since

\[
 d^{-1/2}=\sqrt{40/3}<4,
\]

the outer scalar profile turns either of the preceding `<70` half-potential branches into a density bound `<280`.

The remaining nested-scalar branch is

\[
 d^{-1/2}+\frac{J_0+2L_0}{d},
\]

where the source proves

\[
 J_0=\pi+4\log2,
 \qquad
 L_0=4+4\log5.
\]

Use the rigorous elementary bounds

\[
 \pi<\frac{22}{7},\qquad
 \log2<\frac{347}{500},\qquad
 \log5<\frac{161}{100},
 \qquad
 \sqrt{40/3}<\frac{183}{50}.
\]

The logarithm inequalities follow from positive Taylor partial sums:

\[
 \sum_{j=0}^{4}\frac{(347/500)^j}{j!}-2
 =\frac{289173281}{1500000000000}>0,
\]

and

\[
 \sum_{j=0}^{7}\frac{(161/100)^j}{j!}-5
 =\frac{11628664174467}{8000000000000000}>0.
\]

Consequently

\[
 J_0+2L_0
 <\frac{23449}{875},
\]

and therefore

\[
 d^{-1/2}+\frac{J_0+2L_0}{d}
 <\frac{183}{50}+\frac{40}{3}\frac{23449}{875}
 =\frac{379027}{1050}
 =360.9780952\ldots<361.
\]

The exact margin here is `23/1050`.

## 5. Direct two-coordinate pivot branches

A definite pair pivot has density at most

\[
 \frac{\pi}{\sqrt p}<361
\]

with enormous room.

For an indefinite pair, the source's conditional logarithmic envelope and the Schur-remainder quarter-power estimate give

\[
 \|p_Q\|_\infty
 \le p^{-1/2}\bigl(6+\log16+L_0\bigr)+1/e
 =p^{-1/2}\bigl(10+4\log10\bigr)+1/e.
\]

We use

\[
 p^{-1/2}=\sqrt{20000/57}<\frac{937}{50},
 \qquad
 \log10<\frac{2303}{1000},
 \qquad
 \frac1e<\frac38.
\]

The square-root bound follows from

\[
 (937/50)^2-20000/57
 =\frac{44233}{142500}>0.
\]

For the logarithm, the positive exponential Taylor polynomial through degree nine satisfies

\[
 \sum_{j=0}^{9}\frac{(2303/1000)^j}{j!}-10
 =\frac{139703700879629880300092908769}
 {51840000000000000000000000000000}>0.
\]

Finally `e>8/3` follows already from the first four positive terms of its series. Thus

\[
 \|p_Q\|_\infty
 <\frac{937}{50}\left(10+4\frac{2303}{1000}\right)+\frac38
 =\frac{9010197}{25000}
 =360.40788<361.
\]

The exact margin is `14803/25000`.

The six normalized branches are therefore all strictly below `361`:

- no physical pivot: `<360.430`;
- scalar pivot with no-pivot Schur remainder: `<280`;
- scalar pivot with pair-pivot Schur remainder: `<280`;
- scalar pivot with scalar-pivot Schur remainder: `<360.979`;
- definite pair pivot: `<361` with large slack;
- indefinite pair pivot: `<360.408`.

This proves the normalized theorem.

## 6. Scaling back to arbitrary `K,s`

Exactly as in the source, set `Y=KX` and

\[
 \widetilde Q
 =Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]

The `Y_i` have densities bounded by one, `s_9(A/s)>=1`, and

\[
 Q=(s/K^2)\widetilde Q.
\]

Scalar density scaling therefore yields

\[
 \|p_Q\|_\infty<361K^2/s.
\]

All affine terms and all matrix signs remain present.

## 7. B14 rough-law and translation compiler

I checked the pinned source specifically for the B14 measurable/conditional layer.

1. It explicitly chooses globally bounded Borel representatives of the coordinate densities, so pointwise evaluations in inverse-branch formulas do not silently strengthen the hypotheses.
2. The scalar-square profile is stated as domination against nonnegative output test functions; Tonelli then averages a random Schur remainder without requiring a common exceptional slice.
3. The hyperbolic pair proof makes the same test-function/Tonelli formulation explicit, including a random critical value.
4. In the grouped compiler, the complex image measure is dominated in total variation by the ordinary product projection, hence has an `L^1 cap L^2` density. Mollification makes the copied-law expansion absolutely integrable, and the estimate is uniform in the mollifier scale before taking the `L^2` approximate-identity limit. No moment or support bound enters.

A useful general compiler behind these steps is: if conditional laws `mu_y` satisfy, for almost every `y` and every nonnegative Borel `h`,

\[
 \int h(z)\,\mu_y(dz)
 \le\int h(z)k(y,z)\,dz,
\]

where `k>=0` is jointly measurable, then Tonelli gives

\[
 \mu(dz)\le\left(\int k(y,z)\,\nu(dy)\right)dz.
\]

No common pointwise exceptional set in `z` is required.

### Completed partner result applied to an actual inequality

I also applied the completed account04/B14 cap-preserving compact-completion theorem:

- `yspennstate/math-open-problems@430065de1a8e478dc6156f6b489aa46a63681c09`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T171953Z-account04-B14-QFORM-r2/REPORT.md`.

It says arbitrary cap-one product laws can be approximated in product total variation by compactly supported cap-one laws, with total variation contracting under every measurable pushforward. Therefore, if the `<361|J|` interval estimate is first established on compact product laws, it transfers to arbitrary unbounded, remotely fragmented product laws with **zero loss**.

For deterministic coordinate translations,

\[
 (X+t)^TA(X+t)
 =X^TAX+2(At)^TX+t^TAt.
\]

The theorem is uniform over arbitrary affine terms, so the concrete translation-uniform inequality is

\[
 \boxed{
 \sup_{t\in\mathbb R^n}
 \|p_{(X+t)^TA(X+t)}\|_{\infty,\mathrm{ess}}
 <361\,\frac{K^2}{s}
 }
 \qquad (s_9(A)\ge s).
\]

The partner completion then transfers this same inequality from compact approximants to arbitrary unbounded supports and arbitrarily distant fragments without a tail, moment, translation-size, diameter, or fragment-count term.

This localization argument preserves essential `L^infinity` interval domination. Total-variation convergence by itself does **not** transfer continuity, so no global continuous-density conclusion is claimed here.

## 8. Scope and remaining problem

This is a constant improvement at the already-supported multiplicity nine. It does **not** lower the multiplicity. The eight-eigenvalue endpoint remains open: the pinned overlap theorem supplies

\[
 W_{2,1}^{\times}\ge2V_2-9V_3,
\]

but a product-preserving analytic receiver for the shared original coordinate is still missing. The unrestricted three-eigenvalue conjecture likewise remains **OPEN / NOT PROVED / NOT DISPROVED**, and full-target continuity remains **OPEN**.

A code search before publication found no QFORM occurrence of the retuned pair threshold `p=57/20000`; I therefore treat this as a new repository contribution, not as a priority claim outside the repository.
