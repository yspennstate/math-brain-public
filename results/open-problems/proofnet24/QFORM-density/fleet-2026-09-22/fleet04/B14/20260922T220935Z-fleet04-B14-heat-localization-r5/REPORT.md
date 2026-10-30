# QFORM heat-kernel localization at the sharp constant

**Run:** `20260922T220935Z-fleet04-B14-heat-localization-r5`  
**Account/slot:** fleet04/B14  
**Status:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_LOCALIZATION_THEOREM / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and conclusion

Let (C_{m full}) be the sharp constant in the quadratic-form problem, equivalently
[
 C_{m full}=sup |p_{X^TAX}|_infty ,
]
where the supremum runs over every dimension, every independent product law with
(0le f_ile1), (int f_i=1), and every real symmetric (A) with third singular
value (s_3(A)ge1). The value is allowed to be (+infty).

For
[
 gamma_arepsilon(u)=rac{1}{sqrt{2pi}arepsilon}
 e^{-u^2/(2arepsilon^2)}
]
define
[
 {cal H}(A,arepsilon,y;f_1,dots,f_n)
 =int_{mathbb R^n}gamma_arepsilon(x^TAx-y)
   prod_{i=1}^n f_i(x_i),dx.
]

The main result of this run is the exact identity
[
oxed{
 C_{m full}
 =
 sup_{substack{n, s_3(A)=1\ arepsilon>0, yinmathbb R\
 E_i {m bounded finite unions}\ |E_i|=1}}
 int_{E_1	imescdots	imes E_n}
 gamma_arepsilon(x^TAx-y),dx .
}
	ag{1}
]
There is no loss in the constant, no support-radius bound, no bound on the number
of fragments, and no bound on distances between fragments.

Thus the remaining conjecture is exactly a positive geometric integral inequality
over product sets of measure one. This is stronger than interval-by-interval
bathtub selection: one fixed finite-scale positive functional is extremized over
product indicators.

## 2. Partner theorem actually applied

The completed fleet01/B14 theorem
`QFORM-EXACT-OPTIMAL-CONSTANT-LOCALIZATION`, canonical commit
`5bc2e2b9fc2fa28fdf0d74c5028dcf96ba746128`, proves that for every bounded
measurable (0lePhile1),
[
 sup_{substack{0le f_ile1\ int f_i=1}}
 intPhi(x)prod_i f_i(x_i),dx
 =
 sup_{substack{|E_i|=1}}
 int_{prod_iE_i}Phi(x),dx,
	ag{2}
]
and the last supremum is unchanged if every (E_i) is a bounded finite union of
intervals.

Apply (2) to the actual target functional
[
 Phi(x)=sqrt{2pi}arepsilon,
 gamma_arepsilon(x^TAx-y)
 =e^{-(x^TAx-y)^2/(2arepsilon^2)}in[0,1].
]
After dividing by (sqrt{2pi}arepsilon), one obtains, for every fixed
(A,arepsilon,y),
[
oxed{
 sup_{f_i}{cal H}(A,arepsilon,y;f_i)
 =
 sup_{substack{E_i {m bounded finite unions}\|E_i|=1}}
 int_{prod_iE_i}gamma_arepsilon(x^TAx-y),dx .
}
	ag{3}
]
This is the requested application of a completed partner result to an actual
inequality.

For completeness, the finite-union part is constant preserving: measurable
unit sets can be approximated in symmetric difference by bounded finite unions
of total measure exactly one, and for (0lePhile1)
[
 left|int_{prod E_i}Phi-int_{prod F_i}Phiight|
 le sum_i |E_i	riangle F_i|.
]

## 3. Proof of the sharp target identity

The heat-height theorem from fleet04/B15, canonical commit
`ad7e5daa036cc8330b1432285ad40fec611d37dd`, gives for every probability law
(mu)
[
 sup_{arepsilon>0,y}(mu*gamma_arepsilon)(y)
 =|p_mu|_infty,
	ag{4}
]
with value (+infty) when (mu) has no bounded density.

Combining (3) and (4), and then taking the supremum over (A), gives (1), except
for the normalization (s_3(A)=1). Let (s=s_3(A)ge1) and (A_0=A/s).
Then
[
 gamma_arepsilon(su-y)
 =s^{-1}gamma_{arepsilon/s}(u-y/s).
	ag{5}
]
Consequently the heat height for (A) is (s^{-1}) times the heat height for
(A_0), and therefore cannot exceed it. The sharp supremum is thus unchanged
when restricted to (s_3(A)=1).

No diagonalization of the inputs is used. The variables remain independent only
in the original physical coordinates throughout.

## 4. Exact translation/affine normal form

Equation (1) has an equivalent centered affine formulation. For a bounded
finite-union unit set (E_i), let
[
 m_i=int_{E_i}x,dx,qquad F_i=E_i-m_i.
]
Then (|F_i|=1), (F_i) is a bounded finite union, and
(int_{F_i}z,dz=0). Writing (x=z+m),
[
 x^TAx-y
 =z^TAz+2(Am)^Tz-(y-m^TAm).
	ag{6}
]
Hence
[
oxed{
 C_{m full}
 =
 sup_{substack{s_3(A)=1, bin{m Ran}(A)\
 arepsilon>0, yinmathbb R\
 F_i {m centered bounded finite unions}\|F_i|=1}}
 int_{prod_iF_i}
 gamma_arepsilon(z^TAz+b^Tz-y),dz .
}
	ag{7}
]
Conversely, every (bin{m Ran}(A)) equals (2Am) for some (m), so (7)
does not enlarge the class. Formula (7) isolates all coordinate translations
as a range-compatible affine term. Arbitrarily remote fragments remain allowed,
and no moment bound enters.

## 5. Geometric sublevel consequence

On (|u|le r),
[
 gamma_r(u)ge rac{e^{-1/2}}{sqrt{2pi},r}.
]
Therefore for every product set in (1),
[
 left|{xinprod_iE_i:|x^TAx-y|le r}ight|
 le sqrt{2pi e},r
 int_{prod_iE_i}gamma_r(x^TAx-y),dx .
	ag{8}
]
Thus a universal bound (K) for the right-hand heat integral implies
[
 Pr{|Q-y|le r}le sqrt{2pi e},K,r
]
for all original cap-one product inputs, by (3). Conversely, the exact sharp
height constant is already the heat supremum by (4); (8) is only the direct
sublevel conversion and is not used to claim equality of constants.

## 6. Regularity status and remaining implication

The completed fixed-instance theorem consumed by fleet01/B15 shows that every
fixed rank-at-least-three target instance has an instance-dependent density in
(C_0(mathbb R)). Therefore the laws in (1), despite their fragmented input
supports, have continuous densities and attained maxima. The localization
identity nevertheless addresses the height constant, not a uniform modulus of
continuity.

The full universal bound remains open. The first unpaid implication is now the
pure geometric estimate
[
 sup_{substack{s_3(A)=1,arepsilon>0,y\
 E_i {m bounded finite unions}, |E_i|=1}}
 int_{prod_iE_i}gamma_arepsilon(x^TAx-y),dx<infty.
	ag{9}
]
Any proof of (9) solves the central (L^infty) conjecture with exactly the same
constant. It must allow unbounded fragment count, arbitrarily large fragment
separation, all signatures, and fully rotated matrices.

## 7. Source and correction compliance

The live correction inbox was respected: no pointwise van-der-Corput decay,
spectral-coordinate independence, bounded projection trace, bounded-diameter
localization, fixed fragment count, or single-minor reciprocal estimate is used.
Continuity and universal height are recorded separately. Repository use here is
not authenticated native mathematical-brain ingestion, hence
`WITHOUT_VERIFIED_BRAIN`.
