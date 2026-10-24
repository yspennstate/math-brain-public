# Thirteen-eigenvalue all-finite-Lp theorem with sharpened constants

Run: `20260924T141316Z-account04-B15-fixedmult-s13-allfiniteLp-r2`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh master observed before publication: `3a901aa5c1eda9b8291041cfc548fe4686685101`.

Status: **PROVED SUPPORTING IMPROVEMENT.** This strengthens the thirteen-eigenvalue L2 theorem to every finite Lp and incorporates the sharper graph determinant and pivot constant. It does **not** prove an L-infinity bound at thirteen eigenvalues. The unrestricted three-eigenvalue conjecture remains open.

## Theorem

Let (X=(X_1,ldots,X_n)) have independent real coordinates with probability densities bounded by (K>0). Let (A=A^T), (binmathbb R^n), (cinmathbb R), and
[
 Q=X^TAX+b^TX+c.
]
If
[
 s_{13}(A)ge s>0,
]
then (Q) has a density (p_Qin L^p(mathbb R)) for every finite (p>1). Quantitatively,
[
 oxed{;
 |p_Q|_p
 le
 left(rac{K^2}{s}ight)^{1-1/p}
 egin{cases}
  3810^{,1-1/p},&1<ple2,\[2mm]
  igl(max{3810,160sqrt{2e},p}igr)^{1-1/p},&2le p<infty.
 end{cases}
 ;}
	ag{1}
]
In the normalized no-pivot branch, the sharper estimate is
[
 oxed{quad
 |p_Q|_ple(160sqrt{2e},p)^{1-1/p},
 qquad 2le p<infty.
 quad}
	ag{2}
]

The (O(p)) growth in (2) is the precise endpoint obstruction left by the present absolute Fourier envelope. It is compatible with a logarithmic density singularity and therefore cannot be promoted to (L^infty) by abstract interpolation.

## Proof: normalized no-pivot branch

Set (K=s=1). Use the manuscript parameters
[
 eta=10^{-2},qquad kappa=80^{-2}.
]
If there is no (eta)-pivot, the audited spectral-to-volume proposition at order (k=4), followed by the random physical-coordinate cut, gives
[
 V_4(A)gekappa^4,qquad
 Z_4(M)ge4^{-4}kappa^4.
	ag{3}
]
The sharpened graph determinant theorem proved in account03/B18 gives
[
 |phi_Q(t)|
 le
 det!left(I+rac{t^2}{2pi^2e}M^TMight)^{-1/8}.
	ag{4}
]
Keeping the four singular directions encoded by (Z_4(M)) yields
[
 |phi_Q(t)|lemin{1,u/|t|},
 qquad
 u=pisqrt{2e},Z_4(M)^{-1/8}.
	ag{5}
]
Indeed, this is the manuscript volume-envelope computation with the determinant coefficient changed from (1/(pi^2e^2)) to (1/(2pi^2e)). From (3),
[
 Z_4(M)^{-1/8}
 le 4^{4/8}kappa^{-1/2}
 =2cdot80=160,
]
and hence
[
 oxed{ule160pisqrt{2e}.}
	ag{6}
]

Fix (pge2), and write (q=p/(p-1)in(1,2]). From (5),
[
 |phi_Q|_q^q
 le2u+rac{2u}{q-1}
 =2u,rac q{q-1}
 =2up.
	ag{7}
]
For the Fourier convention (widehat f(t)=int e^{itx}f(x),dx), inverse Hausdorff--Young is
[
 |mathcal F^{-1}g|_p
 le(2pi)^{-1/q}|g|_q.
	ag{8}
]
Equations (6)--(8) give
[
 |p_Q|_p
 le(2pi)^{-1/q}(2up)^{1/q}
 =(up/pi)^{1/q}
 le(160sqrt{2e},p)^{1-1/p},
]
which proves (2).

There is no circular assumption that the law already has a density. Let (mu) be the law of (Q) and (g_arepsilon) a Gaussian approximate identity. The density of (mu*g_arepsilon) has Fourier transform (phi_Q(t)e^{-arepsilon t^2}); (8) gives the same uniform (L^p) bound. Since (1<p<infty), weak compactness in (L^p) supplies a weakly convergent subsequence. Since (mu*g_arepsilon	omu) weakly as measures, its weak (L^p) limit represents (mu). Thus (mu=p_Q,dx) and the bound passes by lower semicontinuity.

## Pivot branches

Under (s_{13}(A)ge1), all manuscript pivot branches already give bounded densities.

- A scalar pivot leaves at least twelve large Schur directions, so the nine-eigenvalue half-potential theorem applies. With the sharpened half-potential constant from account03/B18, the normalized density cap is (<3810).
- A definite two-coordinate pivot gives (10pi).
- An indefinite two-coordinate pivot gives (<251).

Consequently every pivot branch satisfies
[
 |p_Q|_infty<3810
 quadLongrightarrowquad
 |p_Q|_ple3810^{,1-1/p}.
	ag{9}
]
Combining (2) and (9) proves the normalized (pge2) part of (1).

The audited thirteen-eigenvalue (L^2) theorem gives
[
 |p_Q|_2<sqrt{3810}.
	ag{10}
]
Interpolating (|p_Q|_1=1) with (10) gives, for (1<ple2),
[
 |p_Q|_p
 le
 |p_Q|_1^{2/p-1},
 |p_Q|_2^{2-2/p}
 <3810^{,1-1/p}.
	ag{11}
]

## Scaling

Put (Y=KX) and
[
 widetilde Q
 =Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c
 =rac{K^2}{s}Q.
]
The coordinates of (Y) have density cap one and (s_{13}(A/s)ge1). If (alpha=K^2/s), then
[
 |p_Q|_p=alpha^{1-1/p}|p_{widetilde Q}|_p,
]
which gives (1).

## Concrete near-endpoint small-ball consequence

In the normalized no-pivot branch, for an interval (I) with (0<|I|le e^{-2}), choose (p=log(1/|I|)). Hölder and (2) give
[
 oxed{;
 Pr(Qin I)
 le160esqrt{2e},|I|log(1/|I|).
 ;}
	ag{12}
]
Thus the order-four mechanism is exactly one logarithm short of the desired linear interval bound.

## Scope and endpoint

All original quantifiers are retained: arbitrary dimension, signs, remaining spectrum, affine terms, fragmented or unbounded supports, and rough non-identically-distributed product inputs. No moments, support bound, Gaussianity, log-concavity, or independence after rotation is used.

The completed bounded-density threshold remains seventeen eigenvalues. At thirteen eigenvalues the density is now known to lie in every finite (L^p), with explicit dimension-free (O(p)) norm growth. Removing that growth requires cancellation or a second compatible crossing mechanism before absolute values are taken; the critical (1/|t|) envelope alone cannot yield (L^infty).
