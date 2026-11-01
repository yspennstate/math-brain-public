# C0032 — endpoint deformation, Struve-K inversion, and an exact nonlinear radial ODE

Target: Charles Bordenave and Djalil Chafaï, *Around the circular law*, Probability Surveys 9 (2012), Section 6.6 / p. 39, asking for an explicit identification of the isotropic density of the heavy-tailed limiting law `mu_alpha`; underlying scalar law from Bordenave–Caputo–Chafaï, *Spectrum of non-Hermitian heavy tailed random matrices*, CMP 307 (2011).

Status of this artifact: theorem-sized **PARTIAL** progress. It does not claim source-level closure or novelty. It executes the post-STUCK1 recovery methods B6/B17/B20. The frozen campaign metric `M_jet` was already saturated at `+infinity` and is not replaced here.

## 1. Exact starting point inherited from the preceding C0032 runs

Put

\[
\beta=\alpha/2\in(0,1),\qquad c_\beta=\Gamma(1-\beta),\qquad C_\beta=\Gamma(1-\beta)\Gamma(1+\beta).
\]

Let `S,S'` be independent positive beta-stable variables normalized by

\[
\mathbb E e^{-tS}=e^{-c_\beta t^\beta}.
\]

Let `T=SS'`.  The earlier R7-06 elimination gives the ordinary Stieltjes transform

\[
q_\beta(a):=\mathbb E\frac{T}{a+T},\qquad a>0,
\tag{1.1}
\]

and the physical squared-radius map

\[
R_\beta(a)
=a\left(\frac{q_\beta(a)}{C_\beta}\right)^{1/\beta}.
\tag{1.2}
\]

`R_beta` is a smooth strictly increasing bijection `(0,infinity)->(0,infinity)`. If

\[
M_\beta(r):=\mu_\alpha\{|z|^2\le r\},
\]

then exactly

\[
1-M_\beta(R_\beta(a))=q_\beta(a),
\tag{1.3}
\]

and, with `g_alpha` the planar isotropic density,

\[
g_\alpha(\sqrt{R_\beta(a)})
=-\frac{q_\beta'(a)}{\pi R_\beta'(a)}.
\tag{1.4}
\]

The Mellin transform is

\[
\widehat q_\beta(s)
=c_\beta^{2s/\beta}
\frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)},
\qquad 0<\Re s<\beta.
\tag{1.5}
\]

Thus the remaining source-level operation is the inverse of (1.2).  The point of this run is to understand that inverse in the easiest endpoint deformation and in the exactly solvable `alpha=1` specialization.

---

# 2. B6 — deform to the classical endpoint and identify exactly what breaks

The endpoint `beta=1` is singular in the BCC normalization because `c_beta=Gamma(1-beta)` diverges.  The right comparison therefore first removes that deterministic scale.

Define

\[
V_\beta:=\frac{S}{c_\beta^{1/\beta}}.
\]

Then

\[
\mathbb E e^{-tV_\beta}=e^{-t^\beta}.
\tag{2.1}
\]

Hence, as `beta↑1`, the Laplace transforms converge pointwise to `e^{-t}`, the Laplace transform of the constant one. Therefore

\[
V_\beta\Rightarrow1,
\qquad
U_\beta:=V_\beta V_\beta'\Rightarrow1.
\tag{2.2}
\]

## 2.1 Scaled Stieltjes coordinate

Put

\[
a=c_\beta^{2/\beta}x
\]

and define

\[
Q_\beta(x)
:=q_\beta(c_\beta^{2/\beta}x)
=\mathbb E\frac{U_\beta}{x+U_\beta}.
\tag{2.3}
\]

For each fixed `x>0`, the integrand is bounded and continuous, so (2.2) gives

\[
\boxed{Q_\beta(x)\longrightarrow\frac1{1+x}.}
\tag{2.4}
\]

Now rescale the physical squared radius by the remaining deterministic factor:

\[
\mathcal R_\beta(x)
:=\frac{R_\beta(c_\beta^{2/\beta}x)}{c_\beta^{1/\beta}}.
\tag{2.5}
\]

Using `C_beta=c_beta Gamma(1+beta)` in (1.2),

\[
\boxed{
\mathcal R_\beta(x)
=x\left(\frac{Q_\beta(x)}{\Gamma(1+\beta)}\right)^{1/\beta}.
}
\tag{2.6}
\]

Therefore

\[
\boxed{
\mathcal R_\beta(x)\longrightarrow\frac{x}{1+x}.
}
\tag{2.7}
\]

Together with (1.3), this gives

\[
M_\beta\!\left(c_\beta^{1/\beta}\mathcal R_\beta(x)\right)
=1-Q_\beta(x)
\longrightarrow\frac{x}{1+x}.
\tag{2.8}
\]

If `s=x/(1+x)`, the limiting CDF is exactly `s`.  Thus, after the natural BCC endpoint rescaling, the squared-radius law tends to the uniform-disc squared-radius CDF.  At the endpoint the inverse is elementary:

\[
\boxed{x=\frac{s}{1-s}.}
\tag{2.9}
\]

This already identifies the structural break: the random product `U_beta` collapses to the deterministic value one only at `beta=1`.  For every `beta<1`, `V_beta` and hence `U_beta` are nondegenerate.  If (2.4) were exactly `Q_beta(x)=1/(1+x)` for all `x>0`, uniqueness of the Stieltjes transform would force `U_beta=1` almost surely, impossible for a nondegenerate stable law.  So the algebraic endpoint inversion is destroyed immediately for every `beta<1`.

## 2.2 First-order deformation from the endpoint

The previous conclusion can be made quantitative.  Scaling (1.5) gives

\[
\boxed{
\widehat Q_\beta(s)
=\frac{\Gamma(s)\Gamma(1-s/\beta)^2}{\Gamma(1-s)},
\qquad 0<\Re s<\beta.
}
\tag{2.10}
\]

At `beta=1`,

\[
\widehat Q_1(s)=\Gamma(s)\Gamma(1-s),
\]

which is the Mellin transform of `(1+x)^{-1}`. Differentiating (2.10) with respect to `beta` at `beta=1` gives

\[
\left.\partial_\beta\widehat Q_\beta(s)\right|_{\beta=1}
=2s\psi(1-s)\Gamma(s)\Gamma(1-s).
\tag{2.11}
\]

The inverse Mellin transform is elementary.  Indeed, for `0<Re(s)<1`, direct beta-integral differentiation gives

\[
\int_0^\infty x^{s-1}
\frac{2x\{1-\gamma_E-\log(1+x)\}}{(1+x)^2}\,dx
=2s\psi(1-s)\Gamma(s)\Gamma(1-s).
\tag{2.12}
\]

Hence

\[
\boxed{
\left.\partial_\beta Q_\beta(x)\right|_{\beta=1}
=
\frac{2x\{1-\gamma_E-\log(1+x)\}}{(1+x)^2}.
}
\tag{2.13}
\]

Choose a fixed Mellin line `Re(s)=c` with `0<c<1`.  For `beta` in a sufficiently small neighborhood of one, Stirling estimates on the gamma factors and their first two beta derivatives give an integrable exponential majorant on that line.  Therefore Mellin inversion may be differentiated twice, and the following expansion is locally uniform for `x` in compact subsets of `(0,infinity)`.  Writing

\[
\varepsilon=1-\beta,
\]

we obtain

\[
\boxed{
Q_{1-\varepsilon}(x)
=
\frac1{1+x}
-
2\varepsilon\,
\frac{x\{1-\gamma_E-\log(1+x)\}}{(1+x)^2}
+O(\varepsilon^2).
}
\tag{2.14}
\]

Now differentiate the logarithm of (2.6).  Define

\[
D(x)
:=
\log(1+x)
+\frac{2x}{1+x}\{1-\gamma_E-\log(1+x)\}
-(1-\gamma_E).
\tag{2.15}
\]

Then

\[
\boxed{
\mathcal R_{1-\varepsilon}(x)
=
\frac{x}{1+x}
\left[1-\varepsilon D(x)+O(\varepsilon^2)\right].
}
\tag{2.16}
\]

Fix a compact subinterval of `0<s<1` and solve `s=mathcal R_{1-epsilon}(x)`.  At `epsilon=0`, `x_0=s/(1-s)` and `d[x/(1+x)]/dx=(1+x)^{-2}>0`, so the implicit-function theorem applies uniformly on compact subintervals.  Since

\[
D(x_0)
=(2s-1)\{1-\gamma_E+\log(1-s)\},
\tag{2.17}
\]

we get the explicit inverse deformation

\[
\boxed{
 x(s,\varepsilon)
=
\frac{s}{1-s}
+
\varepsilon\,
\frac{s(2s-1)\{1-\gamma_E+\log(1-s)\}}{(1-s)^2}
+O(\varepsilon^2).
}
\tag{2.18}
\]

Substitute this into `M=1-Q`.  The terms simplify to

\[
\boxed{
M_{1-\varepsilon}\!\left(c_{1-\varepsilon}^{1/(1-\varepsilon)}s\right)
=
s
+
\varepsilon s\{1-\gamma_E+\log(1-s)\}
+O(\varepsilon^2),
}
\tag{2.19}
\]

locally uniformly on every compact subset of `0<s<1`.

Consequently the rescaled squared-radius density satisfies

\[
\frac{d}{ds}M_{1-\varepsilon}
=
1+arepsilon
\left[
1-\gamma_E+\log(1-s)-\frac{s}{1-s}
\right]
+O(\varepsilon^2).
\tag{2.20}
\]

The pole as `s↑1` shows explicitly that this regular expansion develops a boundary layer at the circular edge.  Thus B6 does more than recover the endpoint: it identifies the first correction and the exact place where regular endpoint perturbation stops being uniform.

**B6 outcome.** The classical endpoint is algebraically invertible because the normalized stable product collapses to one. For `beta<1` the nondegenerate product remains inside a genuine Stieltjes transform.  Equations (2.18)–(2.20) give a constructive first-order inverse/CDF deformation away from the endpoint, but not an all-beta closed inverse.

---

# 3. B17 — identify the `alpha=1` inverse in the classical special-function literature

The STUCK1 report had written the `alpha=1`, `beta=1/2` relation as

\[
\rho
=
\frac\pi2\left[\mathbf H_0(z)-Y_0(z)\right],
\qquad
z=\frac\pi{2\sqrt a}.
\tag{3.1}
\]

The current NIST DLMF notation removes one ambiguity: DLMF 11.2.5 **defines** the Struve function of the second kind

\[
\mathbf K_\nu(z):=\mathbf H_\nu(z)-Y_\nu(z).
\tag{3.2}
\]

This is not the modified Bessel `K_nu`; here bold `mathbf K` is the DLMF Struve function.  Hence the exact inverse problem is simply

\[
\boxed{\rho=L(z):=\frac\pi2\mathbf K_0(z).}
\tag{3.3}
\]

DLMF 11.5.2 and 11.5.3 give two positive integral representations.  For `z>0`,

\[
\mathbf K_0(z)
=
\frac2\pi\int_0^\infty\frac{e^{-zu}}{\sqrt{1+u^2}}\,du
=
\frac2\pi\int_0^\infty e^{-z\sinh t}\,dt.
\tag{3.4}
\]

Therefore

\[
\boxed{
L(z)
=
\int_0^\infty\frac{e^{-zu}}{\sqrt{1+u^2}}\,du
=
\int_0^\infty e^{-z\sinh t}\,dt.
}
\tag{3.5}
\]

This has several immediate exact consequences:

1. `L(z)>0` for `z>0`.
2. For every integer `n>=0`,
   \[
   (-1)^nL^{(n)}(z)
   =\int_0^\infty
     \frac{u^n e^{-zu}}{\sqrt{1+u^2}}\,du>0,
   \tag{3.6}
   \]
   so `L` is completely monotone and strictly decreasing.
3. `L(z)->infinity` as `z↓0` and `L(z)->0` as `z->infinity`, so (3.3) has a unique positive inverse for every `rho>0`.

Thus the simplest remaining inverse is not an unidentified Lommel-like combination: it is the functional inverse of the standard DLMF Struve `mathbf K_0`, equivalently the inverse of the completely monotone Laplace transform (3.5).

### Bounded literature/inverse-function check, 2026-09-19 UTC

The search was deliberately restricted to the functional inverse of (3.3), not to ordinary evaluation of Struve/Lommel functions.  Queries included `inverse Struve K`, `inverse Struve function H0 Y0`, `inverse Lommel function`, `functional inverse H_0-Y_0`, and common CAS documentation.  DLMF supplies the direct function, its ODE and its integral transforms, but no named functional inverse was located.  SciPy documents direct Struve functions and some integrals, but the located API listings contain no inverse-Struve primitive.  A paper titled *The inverse Laplace transform of the modified Lommel functions* concerns inverse **Laplace transforms**, not the functional inverse in (3.3).  These are bounded negative checks only; they do **not** prove that no naming convention or later paper exists.

**B17 outcome.** The `alpha=1` obstruction is now exactly identified as inversion of a standard completely monotone Struve-`K_0` Laplace transform.  No standard named functional inverse was found in the bounded search, so merely renaming (3.3) does not close the source problem.

---

# 4. B20 — derive the exact inverse ODE and classify the obstruction

DLMF 11.2.7–11.2.8 state that `mathbf K_nu` satisfies Struve's inhomogeneous Bessel equation.  At `nu=0`,

\[
\mathbf K_0''(z)+\frac1z\mathbf K_0'(z)+\mathbf K_0(z)
=\frac{2}{\pi z}.
\tag{4.1}
\]

Multiplying by `pi/2`, the function `L` from (3.3) satisfies

\[
\boxed{
L''(z)+\frac1zL'(z)+L(z)=\frac1z.
}
\tag{4.2}
\]

Let

\[
Z(\rho):=L^{-1}(\rho),\qquad \rho>0.
\tag{4.3}
\]

Since `L'<0`, the inverse is smooth.  From inverse differentiation,

\[
L'(Z)=\frac1{Z'},
\qquad
L''(Z)=-\frac{Z''}{(Z')^3}.
\tag{4.4}
\]

Substitute `z=Z(rho)` and `L(Z)=rho` into (4.2):

\[
-\frac{Z''}{(Z')^3}
+\frac1{ZZ'}
+\rho
=\frac1Z.
\]

After multiplying by `Z(Z')^3`,

\[
\boxed{
ZZ''=(Z')^2+(\rho Z-1)(Z')^3.
}
\tag{4.5}
\]

This answers one part of the STUCK1 question exactly:

\[
\boxed{
Z \text{ is differential-algebraic over }\mathbb C(\rho)
\text{ of differential order at most }2.
}
\tag{4.6}
\]

The equation does **not** show that `Z` is D-finite, and no D-finiteness claim is made.

## 4.1 `Z` is not algebraic

The integral (3.5) gives the two endpoint asymptotics.  Expanding the Laplace kernel at infinity,

\[
L(z)=\frac1z-\frac1{z^3}+\frac9{z^5}-\frac{225}{z^7}+O(z^{-9}),
\qquad z\to\infty.
\tag{4.7}
\]

At the other endpoint, the standard small-argument expansions of `H_0` and `Y_0` give

\[
L(z)=-\log(z/2)-\gamma_E+O(z),
\qquad z\downarrow0.
\tag{4.8}
\]

Therefore

\[
Z(\rho)\sim\frac1\rho
\quad(\rho\downarrow0),
\qquad
\boxed{
Z(\rho)\sim2e^{-\gamma_E}e^{-\rho}
\quad(\rho\to\infty).
}
\tag{4.9}
\]

The second asymptotic rules out algebraicity over `C(rho)` by an elementary polynomial-balance argument.  If a nonzero polynomial

\[
P(\rho,Z)=\sum_{j=0}^m p_j(\rho)Z^j
\]

vanished identically, let `j0` be the least index with nonzero `p_j0`. Divide by `Z^{j0}`.  By (4.9), every term with `j>j0` is exponentially small times a polynomial in `rho`, whereas the nonzero polynomial `p_j0(rho)` cannot be exponentially small as `rho->infinity`. Contradiction. Hence

\[
\boxed{Z \text{ is differential-algebraic but not algebraic}.}
\tag{4.10}
\]

This is a genuine classification of the simplest physical inverse, although it does not exclude D-finite or broader named inverse-special-function descriptions.

## 4.2 Direct nonparametric ODE for the `alpha=1` radial law

For `beta=1/2`, `C_{1/2}=pi/2`.  From the exact formula used to obtain (3.1),

\[
F(a)=\frac{\rho}{\sqrt a},
\qquad
\sqrt a=\frac\pi{2Z(\rho)}.
\]

Since `q=C F`, this simplifies exactly to

\[
\boxed{
Q(\rho):=1-\mu_1\{|w|\le\rho\}
=\rho Z(\rho).
}
\tag{4.11}
\]

Thus the auxiliary inverse can be eliminated from the final radial equation by setting `Z=Q/rho`.  A direct calculation gives

\[
Z'=\frac{\rho Q'-Q}{\rho^2},
\qquad
Z''=\frac{Q''}{\rho}-\frac{2Q'}{\rho^2}+\frac{2Q}{\rho^3}.
\tag{4.12}
\]

Insert (4.12) into (4.5) and multiply by `rho^6`.  The result is the exact nonlinear second-order ODE

\[
\boxed{
\rho^2Q\bigl(\rho^2Q''-2\rho Q'+2Q\bigr)
=
\rho^2(\rho Q'-Q)^2
+(Q-1)(\rho Q'-Q)^3.
}
\tag{4.13}
\]

There is no PWIT variable, stable expectation, Mellin parameter, or inverse symbol left in (4.13).  The planar density is

\[
\boxed{
 g_1(\rho)=-\frac{Q'(\rho)}{2\pi\rho}.
}
\tag{4.14}
\]

The physical solution is selected by

\[
Q(0+)=1,
\qquad
Q(\infty)=0,
\qquad
0<Q(\rho)<1.
\tag{4.15}
\]

The endpoint expansions supply nontrivial cross-checks.  Reversion of (4.7) gives

\[
Z(\rho)
=\rho^{-1}-\rho+7\rho^3-178\rho^5+O(\rho^7),
\tag{4.16}
\]

so

\[
Q(\rho)
=1-\rho^2+7\rho^4-178\rho^6+O(\rho^8)
\tag{4.17}
\]

and therefore

\[
\boxed{
 g_1(\rho)=\frac1\pi-\frac{14}{\pi}\rho^2+\frac{534}{\pi}\rho^4+O(\rho^6).
}
\tag{4.18}
\]

The first two terms independently reproduce the earlier R7-06 origin value and curvature.  At the opposite endpoint, (4.9) gives

\[
Q(\rho)\sim2e^{-\gamma_E}\rho e^{-\rho},
\qquad
\boxed{
 g_1(\rho)\sim\frac{e^{-\gamma_E}}\pi e^{-\rho},
}
\tag{4.19}
\]

again reproducing the earlier independently derived corrected tail.

**B20 outcome.** The `alpha=1` physical law has an exact second-order differential-algebraic description with no auxiliary parameter.  The inverse itself is differential-algebraic but nonalgebraic.  This shows that the obstruction is more than notational, while also showing it is not an arbitrary transcendental black box.  The remaining gap is to turn such differential characterizations into an accepted all-alpha explicit identification, or to prove an appropriate no-go statement for narrower named-function classes.

---

# 5. What moved mathematically, and what did not

The fixed campaign metric remains

\[
M_{\rm jet}=+\infty\longrightarrow+\infty.
\]

There is **NO MOVEMENT** in that already-saturated metric.  Nevertheless this run adds three source-relevant facts:

1. a rigorous classical-endpoint scaling limit plus the first explicit `beta↑1` correction, including the inverse coordinate (2.18) and CDF correction (2.19);
2. identification of the `alpha=1` inversion as the inverse of the standard DLMF Struve `mathbf K_0` and its completely monotone Laplace representation (3.5);
3. the exact inverse ODE (4.5), the classification `differential-algebraic but nonalgebraic`, and the direct radial-tail ODE (4.13).

None of these is the full source closure criterion.  The source asks for the density for **every** `0<alpha<2` and every radius.  Arbitrary irrational beta still requires the monotone inverse of the Mellin/Stieltjes map, and no accepted named inverse was located in the bounded literature search.

No finite source-resolution claim arises here, so no finite exact checker is required.  The algebraic manipulations above were independently re-derived symbolically during the run, but that self-check is not an independent audit and is not recorded as closure evidence.

# 6. Dated literature check — 2026-09-19 UTC

- Bordenave–Chafaï, arXiv:1109.3343v4 / Probability Surveys 9 (2012), remains the source survey located for C0032.
- Bordenave–Caputo–Chafaï, arXiv:1006.1713 / CMP 307 (2011), remains the source of the heavy-tailed law and scalar/PWIT characterization.
- Current NIST DLMF Chapter 11, release displayed as 2026-09-15, defines `mathbf K_nu=mathbf H_nu-Y_nu`, gives its inhomogeneous Bessel equation, and gives the positive integral representations used in Sections 3–4.
- Bounded searches for `inverse Struve K`, `inverse Struve function H0 Y0`, `inverse Lommel function`, and `functional inverse H_0-Y_0` did not surface a standard named functional inverse.  A located 2013 paper about the **inverse Laplace transform** of modified Lommel functions concerns a different operation.
- Bounded searches for a later all-radius explicit formula or corrigendum for the BCC heavy-tailed density recovered the original sources and neighboring heavy-tail random-matrix work but no source-matching closure.  Search failure is negative evidence only, not a novelty or openness certificate.

# 7. Next nonrepeating methods

If C0032 remains active, the next ordinary triple should not repeat B6/B17/B20.  A productive sequence is:

- **B3 — prove something stronger:** seek a direct physical-radius integral/differential equation for `Q_beta(rho)` valid for every beta, so the inverse parameter disappears before specializing to rational beta;
- **B18 — say it in another language:** recast the physical inverse as a quantile/complete-Bernstein/Nevanlinna problem and determine whether a canonical inverse class exists beyond finite Meijer-G;
- **B22 — read the failures:** search the differential-algebraic and inverse-special-function literature specifically for obstructions to D-finite or classical-special-function inverses of completely monotone Struve/Stieltjes transforms.

Because this is the first ordinary unchanged run after STUCK1, the post-STUCK1 ordinary unchanged count is `0 -> 1`; the HARD stuck-recovery count remains `1`.  STUCK2 is not yet triggered.