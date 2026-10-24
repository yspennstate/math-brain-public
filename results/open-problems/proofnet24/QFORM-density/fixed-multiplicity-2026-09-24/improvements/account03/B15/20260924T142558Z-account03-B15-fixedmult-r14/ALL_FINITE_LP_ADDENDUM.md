# Addendum — multiplicity eight has universal all-finite-Lp and exponential density-value control

This addendum uses the strong-cross pair extracted in `REPORT.md` and the already completed grouped product-Fourier receiver from account03/B04. It strengthens the regularity conclusion at multiplicity eight but does not prove `L^infinity`.

## 1. A strong rank-two physical cross map gives a critical `1/|t|` envelope

The completed B04 grouped product-Fourier argument proves, for two literal physical original coordinates crossing the complementary product bank through a row-rank-two matrix `C`, while retaining arbitrary same-bank quadratic curvature and affine phases,

`|phi_Q(t)| <= min(1, pi sqrt(e) det(CC^T)^(-1/4)/|t|).`          (1.1)

No condition on the two-by-two self block is needed for (1.1); it is absorbed into the complex physical-coordinate pushforward.

In the terminal multiplicity-eight collar, `REPORT.md` proved that one physical pair `H` has

`det(C_H C_H^T)>=g_*:=delta_*^2/2
                         =0.36494426588270207... .`              (1.2)

Therefore throughout the **entire** terminal collar, including the nonzero weak-self chamber,

`|phi_Q(t)| <= min(1, pi C_* /|t|),`                             (1.3)

where

`C_*:=sqrt(e) g_*^(-1/4)
     =sqrt(e) 2^(1/4)/sqrt(delta_*)
     =2.121243892402635... .`                                    (1.4)

This is the exact critical endpoint: it is not integrable in time and therefore does not by itself prove a bounded density.

## 2. Every finite Lp is nevertheless uniformly controlled

Fix `p>=2` and let `q=p/(p-1) in (1,2]`. From (1.3),

`||phi_Q||_q^q
 <=2 pi C_* + 2 (pi C_*)^q int_(pi C_*)^infinity t^(-q)dt
 =2 pi C_* q/(q-1)
 =2 pi C_* p.`                                                   (2.1)

With the manuscript Fourier convention, inverse Hausdorff--Young gives

`||p_Q||_p <=(2pi)^(-1/q)||phi_Q||_q
            <=(C_* p)^(1/q)
            =(C_* p)^(1-1/p).`                                  (2.2)

There is no circular density assumption: convolve the output law with a Gaussian approximate identity, apply the same Fourier bound to each smooth density, use weak compactness of `L^p` for `1<p<infinity`, and identify the weak limit with the original law. This is the same rigorous endpoint passage used by account04/B15 in its thirteen-direction all-finite-`L^p` theorem.

Thus the terminal eight-direction collar satisfies

`boxed: ||p_Q||_p <=(2.121244 p)^(1-1/p),  2<=p<infinity.`        (2.3)

Interpolating `||p_Q||_1=1` with the `p=2` case gives, for `1<p<=2`,

`||p_Q||_p <=(2 C_*)^(1-1/p).`                                  (2.4)

The `O(p)` growth in (2.3) is compatible with a logarithmic singularity, so it still does not imply `L^infinity`.

## 3. Exponential Orlicz bound for the density values

For every integer `m>=1`, (2.2) and mass one give

`int p_Q(x)^m dx <=(C_* m)^(m-1).`                               (3.1)

Consequently

`int [exp(p_Q/(e C_*))-1]
 <= (1/C_*) sum_(m>=1) m^(m-1)/(e^m m!).`                        (3.2)

The classical rooted-tree generating function

`T(z)=sum_(m>=1) m^(m-1) z^m/m!`

satisfies `T= z exp(T)`; at `z=e^(-1)` its nonnegative solution is `T=1`. Hence

`boxed: int_R [exp(p_Q(x)/(e C_*))-1] dx <=1/C_* .`              (3.3)

This is a universal exponential integrability statement for the **values of the output density** in the terminal collar, not a tail or moment assumption on the inputs.

For every measurable set `E` of Lebesgue measure `delta>0`, Jensen on `E` and (3.3) yield

`exp(P{Q in E}/(e C_* delta))-1
 <= 1/(C_* delta)`,

so

`boxed: P{Q in E}
 <= e C_* delta log(1+1/(C_* delta)).`                           (3.4)

Numerically `e C_*=5.766138726447817...`. Thus the unresolved eight-direction terminal branch is quantitatively only one logarithm away from the desired linear small-ball estimate.

## 4. Global s8 all-finite-Lp theorem

The completed B04 threshold-eight reduction also states that every pivot branch is already paid at `s_8>=1`, while the alternative no-pivot `V_3` branch has `L^infinity` height `<2400`. Keeping the safe manuscript scalar-pivot cap `6010`, all normalized `s_8(A)>=1` instances therefore satisfy

`boxed:
 ||p_Q||_p <=
   { 6010^(1-1/p),                         1<p<=2,
     max(6010,C_* p)^(1-1/p),              2<=p<infinity. }`     (4.1)

This retains arbitrary signs, remaining spectrum, affine terms, rough fragmented/unbounded product laws, and arbitrary dimension.

For general coordinate density cap `K` and spectral scale `s`, let `alpha=K^2/s`. The standard normalization gives

`boxed:
 ||p_Q||_p <= alpha^(1-1/p)
   { 6010^(1-1/p),
     max(6010,C_* p)^(1-1/p) }`                                (4.2)

in the respective ranges above.

Hence **multiplicity eight now has a universal density in every finite `L^p` with explicit dimension-free constants**, even though its universal `L^infinity` endpoint remains open. Qualitative `C_0` regularity for each fixed matrix is already supplied separately by the completed fixed-instance affine theorem; no uniform continuity modulus is claimed.

## 5. Relation to the designated partner result

Account04/B15 had previously proved the analogous critical-envelope-to-all-finite-`L^p` conclusion at multiplicity thirteen. Equation (2.1) applies that completed endpoint mechanism to the new actual eight-direction inequality (1.3), lowering this regularity threshold from thirteen to eight. Separately, the same-constant account04/B15 `C_0` compiler is applied in `REPORT.md` to the exact-zero `L^infinity` subchamber.

The remaining mathematical debt is now especially narrow: upgrade the strong-cross/weak-self pair from the critical `1/|t|` envelope to a genuinely integrable joint estimate, or exploit cancellation beyond the absolute Fourier envelope. No claim of multiplicity-eight `L^infinity` is made here.
