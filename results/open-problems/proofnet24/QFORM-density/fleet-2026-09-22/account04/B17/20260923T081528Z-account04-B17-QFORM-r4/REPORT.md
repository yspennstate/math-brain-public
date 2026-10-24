SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B17, 2026-09-23T08:15:28Z.
attacking: replace the numerical Householder-cube stress test by an exact analytic dense shared-coordinate witness certificate.

# QFORM B17 — exact dense Householder cube witness

Run: `20260923T081528Z-account04-B17-QFORM-r4`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING ANALYTIC WITNESS CERTIFICATE; FULL QFORM OPEN / NOT PROVED**  
Full-target continuity remains separate. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. The witness

Let (X_1,X_2,X_3) be independent (mathrm{Unif}[-1/2,1/2]) variables. Their densities are exactly one on disjoint physical coordinates and integrate to one. Put
[
 e=rac1{sqrt3}(1,1,1)^T,qquad
 A=I-2ee^T=rac13
 egin{pmatrix}
 1&-2&-2\
 -2&1&-2\
 -2&-2&1
 end{pmatrix}.
	ag{1.1}
]
All nine entries of (A) are nonzero, so this is genuinely shared-coordinate and is not a separated rank-one-bank example. Since (A) is the Householder reflection across (e^perp),
[
 A^2=I,qquad Ae=-e,qquad A|_{e^perp}=I,
]
and hence
[
 oxed{operatorname{spec}(A)={1,1,-1}.}
	ag{1.2}
]
Thus the example satisfies the original target hypothesis exactly, with no unused spectral slack and no post-rotation independence claim.

For (Q=X^TAX), the canonical coarea density at the cone tip satisfies
[
oxed{
 p_Q(0)
 =6sqrt3,
 operatorname{artanh}!left(rac{sqrt2-1}{sqrt3}ight)
 =2.5343552034856036ldots .
}
	ag{1.3}
]
Equivalently,
[
 lim_{arepsilondownarrow0}
 rac{mathbb P(|Q|learepsilon)}{2arepsilon}
 =6sqrt3,
 operatorname{artanh}!left(rac{sqrt2-1}{sqrt3}ight).
	ag{1.4}
]
Consequently (1.3) is a genuine small-ball/density certificate, not a histogram height.

## 2. Exact cone calculation

Choose an orthonormal basis (u,v) of (e^perp). In spectral coordinates,
[
 Q=y_1^2+y_2^2-y_3^2.
]
The two nappes of (Q=0) are parametrized by
[
 F_sigma(r,	heta)
 =r(cos	heta,u+sin	heta,v+sigma e),
 quad r>0,quad sigmain{pm1}.
	ag{2.1}
]
For the standard Lorentz form,
[
 |partial_rF_sigma	imespartial_	heta F_sigma|
 =sqrt2,r,
 qquad
 |
abla Q(F_sigma)|=2sqrt2,r.
]
Therefore its coarea density is exactly
[
 rac{dS}{|
abla Q|}=rac12,dr,d	heta
	ag{2.2}
]
on each nappe.

Write
[
 d_sigma(	heta)
 =cos	heta,u+sin	heta,v+sigma e,qquad
 M_sigma(	heta)=max_i|d_{sigma,i}(	heta)|.
]
The ray (r d_sigma(	heta)) stays in the original cube
([-1/2,1/2]^3) precisely for
[
 0le rle R_sigma(	heta)
 :=rac1{2M_sigma(	heta)}.
	ag{2.3}
]
Because the input joint density is one on this cube, (2.2) gives
[
 p_Q(0)
 =rac14int_0^{2pi}
 left(rac1{M_+(	heta)}+rac1{M_-(	heta)}ight)d	heta.
	ag{2.4}
]
Central symmetry yields
(M_-(	heta)=M_+(	heta+pi)), so
[
 p_Q(0)=rac12int_0^{2pi}rac{d	heta}{M_+(	heta)}.
	ag{2.5}
]

The three coordinates of (d_+(	heta)) are phase shifts by (2pi/3) of
[
 a+bcos	heta,qquad
 a=rac1{sqrt3},quad b=sqrt{rac23}.
	ag{2.6}
]
Their minimum possible value is (a-b=(1-sqrt2)/sqrt3), while their sum is (sqrt3); hence the largest absolute coordinate is always the largest positive coordinate. Each coordinate is maximal on one sector of angular width (2pi/3). Thus
[
 int_0^{2pi}rac{d	heta}{M_+(	heta)}
 =3int_{-pi/3}^{pi/3}
 rac{d	heta}{a+bcos	heta}.
	ag{2.7}
]
With (t=	an(	heta/2)),
[
 int_{-pi/3}^{pi/3}rac{d	heta}{a+bcos	heta}
 =rac4{sqrt{b^2-a^2}},
 operatorname{artanh}!left[
 	anracpi6sqrt{rac{b-a}{b+a}}
 ight].
	ag{2.8}
]
Here
[
 sqrt{b^2-a^2}=rac1{sqrt3},qquad
 sqrt{rac{b-a}{b+a}}=sqrt2-1.
]
Substitution of (2.8) into (2.5) proves (1.3).

For completeness, (1.4) follows from the same ray parametrization applied to the thickness-(arepsilon) tubular neighborhood of the cone. Away from the origin the level is regular; at the origin the nondegenerate three-dimensional Morse contribution is (O(arepsilon^{3/2})), hence disappears after division by (2arepsilon). The cube cutoff is piecewise Lipschitz in angle, so dominated convergence gives exactly the coarea integral (2.4).

## 3. Application of the completed account01/B17 architecture

The completed account01/B17 rotational-witness report
[
	exttt{math-open-problems@87ad97a024629ad6f7eddb9db55fdbaaea1e0ba8}
]
constructs exact product-provenance matrices (A=RJR^T), with
(J=operatorname{diag}(1,1,-1)), by taking physical rows from an
orthogonal frame. Apply that architecture at the actual finite endpoint
[
 (m_1,m_2,m_3)=(1,1,1)
]
and choose the minority-sign column to be (e=(1,1,1)/sqrt3).
Then (R) is orthogonal and its matrix is exactly
[
 RJR^T=I-2ee^T=A.
	ag{3.1}
]
Thus (1.3) is an equation-level application of the completed partner
construction, not an unrelated example.

The partner report proves that diffuse rotated interval banks approach
(3sqrt2) from below and that a one-heavy/two-Gaussianized rotated
limit is also strictly below (3sqrt2). Formula (1.3) pays the opposite
all-heavy, maximally shared, finite endpoint exactly:
[
oxed{
 p_Q(0)=2.5343552034ldots
 <pi
 <3sqrt2=4.2426406871ldots .
}
	ag{3.2}
]
It therefore rules out this canonical dense three-heavy Householder cone
as a counterexample mechanism at the cone tip.

## 4. Relation to the newest Claude search

The required Claude counterexample search at
[
	exttt{math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837}
]
reported only a numerical value (2.53) for the (n=3) family
(I-2ee^T). Equation (1.3) converts that specific numerical observation
into an exact analytic certificate. Claude's ruled-side theorem also
gives (p_Q(s)lepisqrt2) for (sge0); (1.3) is much sharper at
the tip but does not address the two-sheet side (s<0).

## 5. What remains

This calculation does **not** prove the universal theorem and does not
show that the global maximum of this witness occurs at zero. It pays only
the exact cone-tip value of the maximally symmetric dense three-heavy
Householder example.

The witness frontier therefore remains:

1. off-tip/two-sheet peaks for dense shared-coordinate forms;
2. asymmetric or fragmented laws in several heavy coordinates;
3. multiscale/growing-activity constructions and coupled non-rank-one tails;
4. arbitrary additional spectrum.

The certified universal lower obstruction remains (3sqrt2), from the
diffuse family. The present exact value is evidence against, not proof
against, a finite dense counterexample.

## 6. Provenance and correction discipline

Fresh brain main resolved at start to
(	exttt{cdd7543a77304d8b212104532969bf8631df9781}).
The owner control remains revision `2026-09-22.15`, QFORM-only. The
live correction inbox and required request were consumed. This proof
uses no post-rotation independence, no arbitrary-joint coarea bound, no
conditional projection-density moment, no fixed-fragment localization,
and no histogram extrapolation.

Sources:

- Claude counterexample search:
  `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.
- completed account01/B17 rotational witness theorem:
  `math-open-problems@87ad97a024629ad6f7eddb9db55fdbaaea1e0ba8`.
- earlier exact diffuse lower-obstruction calculation:
  `math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`.
