SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B14, 2026-09-23T05:10:13Z.

# B14 r7 — scale-covariant shear-before-conditioning theorem

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** 20260923T051013Z-account04-B14-scale-shear-r7  
**Status:** new target-level supporting theorem; full conjecture open.  
**Continuity:** separate and not claimed here.

## 1. Inputs used

This report uses the following completed results.

1. Account01/B14 auto11, read at
   (yspennstate/math-open-problems@87bfcc80a0279fa02e80f926e8430bc633e32703):
   for independent cap-one (X_3,X_4),
   [
   W_alpha=(1-alpha)X_3+(1+alpha)X_4-eta
   ]
   has density cap
   [
   |p_{W_alpha}|_infty
   le L_alpha:=(1+|alpha|)^{-1}.
   ]
   The estimate is uniform in the translation (eta).
2. The completed physical-pair logarithmic envelope:
   [
   p(t)le rac{2sqrt2}{r}
   +D^{-1/2}mathbb Elog_+
     rac{2r^2}{kappa|t-R|}.
   ]
3. The account04/B14 finite-mixture localization theorem: every cap-one product law is a total-variation limit of finite mixtures of compact finite-fragment indicator product laws, and uniform interval estimates transfer with no constant loss.

No rotated coordinates are declared independent. No moment, bounded-support, fragment-count, or continuity hypothesis is used.

## 2. Scale-covariant family

Let (X_1,ldots,X_4) be independent real random variables with densities at most one. For nonzero (c,d), real (alpha), and an arbitrary translation (eta), define
[
Q=2cX_1X_2+rac d2
 ig((1-alpha)X_3+(1+alpha)X_4-etaig)^2
 +ell_1X_1+ell_2X_2+gamma .
]
The affine coefficients and scalar shift are arbitrary.

Write
[
M_alpha=1+|alpha|,
qquad
	heta=rac{|c|}{|d|M_alpha^2}.
]

### Theorem — QFORM-SCALE-COVARIANT-CONJUGATE-SHEAR-v1

The output has an essentially bounded density satisfying
[
oxed{
|p_Q|_inftyle |c|^{-1}H(	heta),
}
]
where
[
H(	heta)=
egin{cases}
8sqrt2,	heta^{1/4},&0<	hetale 1/64,\[2mm]
4+2log(8sqrt	heta),&	hetage1/64.
end{cases}
]

The bound is uniform in (eta,ell_1,ell_2,gamma), in support locations and diameters, and in the number and separation of fragments.

## 3. Proof

Divide the form by (c). Reflection changes no density height, so the physical pair is normalized to
[
2X_1X_2,
qquad
D=1,quad kappa=1.
]
Put
[
W=(1-alpha)X_3+(1+alpha)X_4-eta,
qquad
R=rac{d}{2c}W^2.
]
Account01/B14 gives
[
|p_W|_inftyle L_alpha=M_alpha^{-1}.
]

For every center (t) and (ho>0), the inverse image under (wmapsto (d/(2c))w^2) of an interval of radius (ho) has total length at most
[
4sqrt{rac{|c|}{|d|}}sqrtho.
]
Consequently
[
sup_tPr{|R-t|<ho}
le
min{1,4sqrt	heta,sqrtho}.
]

Insert this into the logarithmic envelope. Layer cake gives, for every (r>0),
[
|p_{Q/c}|_infty
le
rac{2sqrt2}{r}
+2Psi(4sqrt2,rsqrt	heta),
]
where
[
Psi(z)=
egin{cases}
z,&0le zle1,\
1+log z,&zge1.
end{cases}
]

On the low branch, differentiation gives
[
r_*=rac1{2	heta^{1/4}},
]
which lies in that branch exactly when (	hetale1/64), and the value is
[
8sqrt2,	heta^{1/4}.
]

On the logarithmic branch the unique minimizer is (r_*=sqrt2), valid exactly when (	hetage1/64), and the value is
[
4+2log(8sqrt	heta).
]
Rescaling the output by (c) proves the theorem.

No pointwise value of an arbitrary density on a quadratic surface is used; the argument is entirely an interval/small-ball calculation.

## 4. Uniform target-level corollary

The homogeneous matrix of (Q) has nonzero eigenvalues
[
c,quad -c,quad d(1+alpha^2).
]
Therefore it lies in the original target whenever
[
|c|ge1,
qquad
|d|(1+alpha^2)ge1.
]

Because
[
M_alpha^2=(1+|alpha|)^2ge1+alpha^2,
]
the target hypothesis implies
[
|d|M_alpha^2ge1,
qquad
	hetale|c|.
]
The function (H) is increasing. Since (|c|ge1), only the logarithmic formula is needed at (|c|), and
[
|p_Q|_infty
le
rac{4+2log(8sqrt{|c|})}{|c|}.
]
The right side decreases for (|c|ge1). Hence
[
oxed{
|p_Q|_infty
le 4+2log8
<8.159 .
}
]

This is uniform simultaneously in (c,d,alpha), although the third eigenvalue may be supplied by an arbitrarily small coefficient (d) and an arbitrarily large shear (alpha). The improvement (L_alpha=(1+|alpha|)^{-1}) is exactly what prevents a logarithmic scale loss.

## 5. Conditioning-generated translations

Let (Z) denote arbitrary independent outside original coordinates. The same result holds conditionally if
[
eta=eta(Z),quad
ell_j=ell_j(Z),quad
gamma=gamma(Z)
]
are arbitrary measurable functions, because for each fixed (Z=z):

- the active original coordinates remain independent;
- the shear cap is uniform in (eta(z));
- the pair-log estimate is uniform in the active-pair affine terms;
- (gamma(z)) only shifts the output.

Averaging the conditional interval estimate preserves the same constant. This retains translations and arbitrary unbounded or fragmented supports without a tail term.

This statement does not hide kernel leakage: it covers precisely the branch in which the leakage is the coordinatewise conjugate shear displayed above. A component outside this shear span remains unpaid and cannot be translated away or charged to a normalized conditional density cap.

## 6. Finite-mixture transfer

For completeness, first apply the proof to compact finite-fragment indicator laws. The resulting interval inequality is uniform in fragment count, diameter, separation and translation. The account04/B14 finite-mixture theorem then transfers it, with exactly the same constant, to all cap-one product laws by product total variation and pushforward contraction.

This is a simultaneous law approximation, not an assumption that a bathtub threshold or interval extremizer is attained.

## 7. Remaining full-target implication

The full conjecture remains open. The present theorem closes every conditioning branch whose dangerous moving affine term is a coordinatewise conjugate shear and whose remaining active core is the physical hyperbolic pair.

The residual B14 problem is now:

- decompose a general conditioning-generated kernel component into disjoint conjugate shears before normalized fiber conditioning; or
- if such a decomposition is impossible, extract a quantitative genuinely joint leakage/cross-volume certificate and apply an existing physical-fiber theorem.

Conditioning first and paying any unbounded function of the normalized thin-fiber cap remains invalid on arbitrarily fragmented laws.
