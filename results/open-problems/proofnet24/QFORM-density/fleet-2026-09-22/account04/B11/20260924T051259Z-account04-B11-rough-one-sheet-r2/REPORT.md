SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B11, 2026-09-24T05:12:59Z.
attacking: a rigorous rough-input one-sheet interval theorem for exact rank-three indefinite forms, followed by the unresolved two-sheet/same-bank branch.

# account04/B11 — anisotropic rough one-sheet theorem

Status: **NEW SUPPORTING THEOREM / account01/B11 APPLIED / FULL QFORM OPEN / CONTINUITY NOT CLAIMED**.

## 1. Scope

Let (X_1,dots,X_n) be independent with probability densities (0le f_ile1). Let (Uinmathbb R^{n	imes3}) have orthonormal columns and put (Z=U^TX). Consider
[
F(Z)=lambda_1(Z_1-c_1)^2+lambda_2(Z_2-c_2)^2-mu(Z_3-c_3)^2+q_*,
]
where (lambda_1,lambda_2,mu>0). This includes every exact-rank-three quadratic form of signature ((2,1)), after deterministic spectral coordinates; the random variables (Z_j) are not asserted independent. The translation (c) is retained.

The only probabilistic input is the completed two-dimensional product-projection theorem: every orthogonal two-dimensional projection of the original product law has density at most (2). Equivalently, if (ho) is the density of (Z), every affine line (ellsubsetmathbb R^3) obeys
[
int_ell ho,dmathcal H^1le2.
	ag{1}
]
For rough inputs, (1) and the result below are interpreted through smooth convolution and total-variation passage; no pointwise trace of an arbitrary density representative is used.

## 2. Theorem — rough anisotropic one-sheet interval estimate

For every Borel set (Esubset(q_*,infty)),
[
oxed{Pr{F(Z)in E}le {2pioversqrt{lambda_1lambda_2}},|E|.}
	ag{2}
]
In particular, if (lambda_1,lambda_2ge1),
[
oxed{Pr{F(Z)in I, F(Z)>q_*}le2pi |I|}
	ag{3}
]
for every interval (I).

After negating the form, the identical statement holds for signature ((1,2)) on its one-sheet side, with the product of the two same-sign eigenvalue magnitudes in the denominator.

This is a half-line/one-sheet theorem. It is not a full rank-three density theorem.

## 3. Coarea calculation with the exact Jacobian

First assume the original densities are smooth. Set
[
y_1=sqrt{lambda_1}(z_1-c_1),quad
y_2=sqrt{lambda_2}(z_2-c_2),quad
y_3=sqrt{mu}(z_3-c_3).
]
For (s>0), parameterize the one-sheet hyperboloid
(y_1^2+y_2^2-y_3^2=s) by
[
r_s(	heta,t)=
(sqrt scos	heta-tsin	heta, 
 sqrt ssin	heta+tcos	heta, t),
quad 0le	heta<2pi, tinmathbb R.
	ag{4}
]
A direct calculation gives
[
|partial_	heta r_s	imespartial_t r_s|
=sqrt{s+2t^2},qquad
|
abla(y_1^2+y_2^2-y_3^2)|=2sqrt{s+2t^2}.
	ag{5}
]
Thus the coarea quotient is exactly (1/2), not an unspecified constant.

Writing (D=operatorname{diag}(sqrt{lambda_1},sqrt{lambda_2},sqrtmu)), the density at (q_*+s) is
[
p_F(q_*+s)
={1over2sqrt{lambda_1lambda_2mu}}
int_0^{2pi}int_{mathbb R}
ho!left(c+D^{-1}r_s(	heta,t)ight),dt,d	heta.
	ag{6}
]
For fixed (	heta), the inner integral runs along an affine line with velocity
[
d_	heta=left(-{sin	hetaoversqrt{lambda_1}},
{cos	hetaoversqrt{lambda_2}},
{1oversqrtmu}ight).
	ag{7}
]
By (1),
[
int_{mathbb R}ho(c+D^{-1}r_s(	heta,t)),dt
le {2over|d_	heta|}.
	ag{8}
]
Moreover
[
sqrt{lambda_1lambda_2mu},|d_	heta|
=
sqrt{lambda_2musin^2	heta+
lambda_1mucos^2	heta+lambda_1lambda_2}
gesqrt{lambda_1lambda_2}.
	ag{9}
]
Substituting (8)-(9) into (6) yields
[
p_F(q_*+s)le {2pioversqrt{lambda_1lambda_2}},
quad s>0,
	ag{10}
]
and integration proves (2).

The argument retains all translations. It uses spectral coordinates only to parameterize the deterministic level surface; it never declares the projected coordinates independent.

## 4. Rough-law passage

Let (arphi_arepsilon) be a smooth probability mollifier and set
(f_{i,arepsilon}=f_i*arphi_arepsilon). Then
[
0le f_{i,arepsilon}le1,qquad
|f_{i,arepsilon}-f_i|_1	o0.
]
For fixed finite (n),
[
left|igotimes_i f_{i,arepsilon}-igotimes_i f_iight|_1
lesum_i|f_{i,arepsilon}-f_i|_1	o0.
	ag{11}
]
Hence the laws of (F(U^TX^{(arepsilon)})) converge in total variation to the law of (F(U^TX)). The uniform interval estimate (2) therefore passes to the limit. This is the required marginal-trace justification: no value of a rough density on a line is ever selected.

## 5. Completed account01/B11 theorem applied at an actual inequality

Account01/B11 proved the Witt-aligned zero-pivot theorem
[
|p_Q|_{infty,mathrm{ess}}
le3,2^{4/3}(kappa^2|lambda|)^{-1/3},
]
and, under the exact rank-three spectral gate
(kappa^2|lambda|ge1), the bound is (<7.560).

Apply it to
[
Q=2X_1X_2+X_3^2,qquad
A=egin{pmatrix}0&1&0\1&0&0\0&0&1end{pmatrix}.
]
The spectrum is ({-1,1,1}), the physical zero pivot is (A_{11}=0), and the Witt parameters are (kappa=|lambda|=1,gamma=0). Therefore, for every cap-one product law,
[
oxed{|p_Q|_{infty,mathrm{ess}}
le3,2^{4/3}<7.560.}
	ag{12}
]
This is a full-line bound for this target-valid family, distinct from the one-sheet estimate.

## 6. Remaining obstruction

On the two-sheet side (s<0), the level surface is not ruled by real affine lines. Its natural parameterization produces circular sections and a moving square-root height. The line-X-ray cap (1) does not control those traces; indeed the later Claude source constructs capped three-dimensional densities with bounded line integrals but unbounded two-sheet quadratic output. That example is not itself a product-law counterexample, but it rules out closing the branch from line marginals alone.

Thus the unrestricted conjecture remains open. The next B11 debt is a genuinely product-sensitive two-sheet or same-bank Witt-leakage estimate. A half-line bound has not been promoted to a full density theorem, and continuity is not claimed.

## 7. Sources

- Base Claude package: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.
- Later two-sheet source: `math-open-problems@2b68faa56c5a562d18c51c788bbeb7ecb6f23bd2`.
- Completed account01/B11 theorem used in (12): `math-open-problems@64a3abbb4fab96d4bc296e7c79dd0e5023530c3d`.
- Brain control refreshed from current `main`; authenticated login `yspennstate`.
