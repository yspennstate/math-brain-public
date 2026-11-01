# PROB10-03 — overlap / dual-feasibility reductions at kappa = -1

Status: **PARTIAL / analytical reductions only / no source-bracket endpoint moved by this artifact**.

Frozen source model throughout:

- `M=floor(alpha N)`;
- `g_a iid N(0,I_N)`;
- `||sigma||=sqrt(N)`;
- `<g_a,sigma> >= -sqrt(N)` for every `a<=M`;
- `N -> infinity` with fixed `alpha`.

The current rigorous R14 source bracket entering this refocus is

`alpha_L = 630297437506/10^11 = 6.30297437506`,

`alpha_U = 1278437096216/10^11 = 12.78437096216`,

width `6.48139658710`.

The lower endpoint is imported from the rigorous Montanari--Zhong--Zhou linear-programming success theorem after exact normalization matching. The upper endpoint is the retained rigorous globally optimized Stojnic-2013 partial-lift/Gordon certificate. This artifact does not alter either endpoint.

The purpose here is to follow the owner-requested fresh route: overlap/dual-feasibility variational analysis first, with any numerics only after the analytical reduction is proved.

---

## A. Main new reduction: complete r=2 stationarity is a two-variable root problem

This section starts from the already-proved R14 chain:

- `R14-C188` reduces the complete interior `r=2` stationarized full-lifting equations to `(p,D,gamma)`;
- `runs/R14/2026-09-17T01-04-33Z_r14-recovery2-ou-semigroup.md` proves the exact OU identity and the equivalent three-residual system `(R1,R2,R3)`.

Nothing below reclaims those earlier statements as new. The new point is that `R1` plus a global monotonicity identity eliminates **both `D` and `gamma` uniquely**, leaving two scalar unknowns `(p,B)`.

### A.1 Inherited notation

Work in

`0<p<1`, `0<D<1`, `gamma>0`,

and set

`q=p D^2`,

`gamma_p=(1-pD^2)/(2D(1-p))`,

`c=c(p,D)=(1-D^2)/(D(1-p)(1-pD^2))`,

`B=c/(4 gamma)`.

At `kappa=-1`, define

`h_B(x)=exp(-B (x-1)_+^2)`,

`f_{p,B}(z)=E_H h_B(sqrt(p)z+sqrt(1-p)H)`,

`I(p,B)=E_Z log f_{p,B}(Z)`,

`I_B=partial_B I`,

`K(p,B)=E_Z[(partial_z log f_{p,B}(Z))^2]`.

The deterministic part of the reduced complete-r=2 objective is

`T=(1/2)(1-pq)c-gamma_p+(1/(2c))log(D/(2gamma_p))-q/(2D)+gamma`,

with `T_p,T_D` denoting partial derivatives in `(p,D)` holding `gamma` fixed. The inherited OU reduction proves complete interior stationarity is equivalent to

`R1 = I_B + 4 gamma^2/alpha = 0`,

`R2 = I - B I_B + c^2 T_D/(alpha c_D) = 0`,

`R3 = K/(2p) + (c/alpha)(T_p-(c_p/c_D)T_D) = 0`.

The compact tails of `I,I_B,K` outside `|z|<=9` were already rigorously bounded in the predecessor artifact. The old blocker was a validated three-dimensional root.

### A.2 Lemma: strict signs needed for a global inversion

**Lemma A.1.** For every `0<p<1`, `0<D<1`,

`c_D<0`.

Moreover, for every `0<p<1`, `B>0`,

`I_B(p,B)<0`.

**Proof.** Direct differentiation gives

`c_D = [1+D^2(1-3p)+pD^4]/[D^2(p-1)(1-pD^2)^2]`.

The denominator is strictly negative. With `x=D^2`, the numerator admits the exact factorization

`1+x(1-3p)+p x^2 = (1-x)(1-px)+2(1-p)x`,

which is strictly positive on `0<p,x<1`. Hence `c_D<0`.

For the Gaussian term, conditional on `Z=z`, write

`Y=sqrt(p)z+sqrt(1-p)H-1`.

Then

`f_{p,B}(z)=E exp(-B Y_+^2)>0`,

and

`partial_B f_{p,B}(z)=-E[Y_+^2 exp(-B Y_+^2)]<0`,

because the nondegenerate conditional Gaussian has positive probability of `Y>0`. Thus `partial_B log f<0` for every finite `z`, and integration gives `I_B<0`. QED.

### A.3 The two-variable reduction

For fixed `alpha>0`, `0<p<1`, `B>0`, define

`C_alpha(p,B) := 2 B sqrt(-alpha I_B(p,B))`.

This is positive by Lemma A.1.

**Theorem A.2 (exact 2D compiler for complete r=2 stationarity).** For every fixed `alpha>0` and every `(p,B) in (0,1)x(0,infinity)` there is a unique `D=D_alpha(p,B) in (0,1)` solving

`c(p,D)=C_alpha(p,B)`.

Set

`gamma_alpha(p,B)=C_alpha(p,B)/(4B)=(1/2)sqrt(-alpha I_B(p,B))`.

Then `R1=0` identically. Furthermore, on the complete-r=2 interior domain, the full five-variable source stationarity system is equivalent to the two equations

`S2_alpha(p,B)=0`, `S3_alpha(p,B)=0`,

where

`S2_alpha := I - B I_B + c^2 T_D/(alpha c_D)`,

`S3_alpha := K/(2p) + (c/alpha)(T_p-(c_p/c_D)T_D)`,

and in these formulas `D=D_alpha(p,B)`, `gamma=gamma_alpha(p,B)`, `c=C_alpha(p,B)`.

**Proof.** For fixed `p`, Lemma A.1 shows `D -> c(p,D)` is strictly decreasing. Also

`c(p,D) -> +infinity` as `D downarrow 0`,

and

`c(p,D) -> 0` as `D uparrow 1`.

Hence it is a bijection `(0,1)->(0,infinity)`, giving a unique `D` for every positive `C_alpha`.

Since `B=c/(4gamma)`, the equation `R1=0` is exactly

`I_B + c^2/(4 alpha B^2)=0`.

Equivalently,

`c^2=-4 alpha B^2 I_B`,

and positivity of `c` gives precisely `c=C_alpha`. With that choice,

`gamma=c/(4B)=(1/2)sqrt(-alpha I_B)`,

so `R1=0` holds identically.

The inherited OU reduction proves `(R1,R2,R3)=0` is equivalent to the full complete-r=2 stationarity system on the interior domain. Since `R1` is now automatic and `D,gamma` are uniquely recovered from `(p,B)`, the remaining system is exactly `S2=S3=0`. QED.

### A.4 Finite algebraic inversion

The unique `D` is the unique root in `(0,1)` of the cubic

`C p(1-p)D^3 - D^2 - C(1-p)D + 1 = 0`,

where `C=C_alpha(p,B)`.

This follows by clearing the strictly positive denominator in `c(p,D)=C`. The strict monotonicity above is stronger than merely knowing the cubic: it prevents root-branch ambiguity in validated numerics.

### A.5 Why this is mechanism progress

The predecessor blocker was a validated root of three transcendental residuals in `(p,D,gamma)`. Theorem A.2 reduces that to a **two-dimensional** sign/root problem. A Poincare--Miranda certificate now needs only outward enclosures of `S2,S3` on four rectangle faces. At each `(p,B)` box, `D` can be enclosed by monotone bisection on the cubic, and `gamma` is an explicit interval function of `I_B`. No independent three-dimensional root search remains.

At the old numerical-only `alpha=12.5` scout,

`(p,D,gamma) ~= (0.656313184757223, 0.652653689820474, 0.158861855012242)`,

this compiler maps to

`B ~= 5.590132429288564`.

That is only a consistency point. **It is not a rigorous endpoint until the compact Gaussian integrals and the two-face sign conditions are outward-certified and the source comparison value is rigorously positive.**

---

## B. Fresh overlap attack: a general weighted second-moment variational obstruction

The lower endpoint `6.302974...` comes from MZZ's LP algorithm. R14 previously proved that MZZ's particular one-parameter weighted second moment has local curvature ceiling below `3.714` at `kappa=-1`. Here I tested whether a genuinely richer overlap weight can evade that obstruction.

### B.1 Exact weighted-sphere second-moment exponent

Let `w:R-> [0,infinity)` be nonzero, supported on `[-1,infinity)`, with `w(G) in L^2` for `G~N(0,1)`. Let `nu_N` be normalized spherical measure and define

`Z_w = int prod_{a=1}^M w(<g_a,sigma>/sqrt(N)) dnu_N(sigma)`.

If `Z_w>0`, the instance is SAT, because every point contributing positively satisfies all hard constraints.

Let `He_j` be probabilists' Hermite polynomials and

`m_j=E[w(G)He_j(G)]`.

For `(G1,G2)` standard Gaussian with correlation `q`, put

`e_w(q)=E[w(G1)w(G2)]`.

Mehler's formula gives, for `|q|<1`,

`e_w(q)=sum_{j>=0} (m_j^2/j!) q^j`.

The overlap `q=<sigma,tau>/N` of two independent uniform spherical points has density proportional to `(1-q^2)^((N-3)/2)`. Therefore the exponential second-moment profile relative to `q=0` is

`F_w(q)=alpha log(e_w(q)/m_0^2) + (1/2)log(1-q^2)`.

This is the exact large-N overlap exponent; the normalization of the overlap density is subexponential in `N`.

**Lemma B.1 (universal local necessary conditions for this route).** If the classical weighted-sphere second-moment route is to have `q=0` as a local maximizer, then

`m_1=0`.

If `m_1=0`, strict local stability further requires

`alpha (m_2/m_0)^2 < 1`.

**Proof.** From Mehler,

`e_w(0)=m_0^2`, `e_w'(0)=m_1^2`, `e_w''(0)=m_2^2`.

Hence

`F_w'(0)=alpha m_1^2/m_0^2`.

Unless `m_1=0`, this is positive and `q=0` is not even stationary. If `m_1=0`, then

`F_w''(0)=alpha m_2^2/m_0^2 - 1`,

because the second derivative of `(1/2)log(1-q^2)` at zero is `-1`. Local maximality requires the displayed quantity to be negative. QED.

This recovers the earlier MZZ local-curvature obstruction as one special weight, but does not assume their exponential-linear ansatz.

### B.2 Quadratic-exponential family and exact stationarity collapse

Consider the genuinely larger two-parameter family

`w_{a,b}(x)=exp(-a x-b x^2) 1{x>=-1}`,

with `b>=-1/4`. At the boundary `b=-1/4`, `L^2` still holds for the stationary solution below because `a>0`; for `b<-1/4`, the quadratic tail makes `w` non-square-integrable.

Write

`A=1+2b`.

Under the one-copy tilted probability measure proportional to `w_{a,b}(x) phi(x)1{x>=-1} dx`, the unnormalized density is

`exp(-A x^2/2-a x) 1{x>=-1}`.

For each fixed `b>=-1/4`, the condition `m_1=0` is exactly that this truncated Gaussian have mean zero. There is a unique real `a=a(b)`, because differentiating the tilted mean with respect to `a` gives minus its strictly positive variance; the mean tends to `+infinity` as `a->-infinity` and to `-1` as `a->+infinity`. At `a=0` the lower truncation gives positive mean, so the unique root has `a(b)>0`.

**Lemma B.2 (closed local curvature formula).** On the unique `m_1=0` branch,

`m_2/m_0 = -(a+2b)/(1+2b)`.

Consequently the local second-moment ceiling is

`alpha_loc(b)=(1+2b)^2/(a(b)+2b)^2`.

**Proof.** Let

`v(x)=exp(-A x^2/2-a x)`, `Z=int_{-1}^infty v(x)dx`.

The condition `m_1=0` is `int x v=0`. Integrating `v'` gives

`-v(-1)=int(-Ax-a)v=-aZ`,

so `v(-1)=aZ`. Integrating `(xv)'` gives

`v(-1)=int(1-Ax^2-a x)v = Z(1-A E[X^2])`,

where `X` has the tilted normalized law and `E[X]=0`. Thus

`a=1-A E[X^2]`,

so

`E[X^2]-1=-(a+2b)/A`.

But `m_2/m_0=E[X^2-1]`. The local ceiling follows from Lemma B.1. QED.

This proves an important diagnosis: the old MZZ local obstruction is **not universal**. Allowing a negative quadratic tilt can raise the local curvature ceiling. Whether that helps is determined by nonzero overlaps, not by the `q=0` Hessian alone.

### B.3 Exact global finite-dimensional reduction

For this family, the full global overlap calculation also has a closed reduction suitable for later certified numerics.

Let

`Sigma_q=[[1,q],[q,1]]`,

`P_q=Sigma_q^{-1}+2b I_2`,

`C_q=P_q^{-1}`, `one=(1,1)^T`,

`mu_q=-a C_q one`.

For `b>=-1/4` and `|q|<1`, `P_q` is positive definite. Completing the square gives exactly

`e_{a,b}(q)
 = [det(Sigma_q) det(P_q)]^{-1/2}
   exp((a^2/2) one^T C_q one)
   P{X_1>=-1,X_2>=-1}`, 

where `X~N(mu_q,C_q)`.

Thus after enforcing `m_1=0`, the entire quadratic-weight route is a **two-scalar** problem `(b,q)`, not an uncontrolled functional ansatz. A later rigorous optimization may use bivariate-normal tail enclosures on a compact `(b,q)` domain.

A numerical scout performed only after proving this reduction suggests that negative `b` raises the local ceiling above the MZZ value but creates a stronger positive-overlap obstruction: for example the scout gives a global allowable density only about `5.03` at `b=-0.24`, versus local ceiling about `6.56`; at `b=0` it reproduces the old approximately `3.69` global obstruction. These numbers are **NUMERICAL ONLY** and are not bracket endpoints. The conclusion of this run is only that the richer family is analytically tractable and that local curvature by itself is misleading.

---

## C. Third attack: facet enumeration removes the N log N net loss but is too weak

The old R14 handoff proved a direct `N^{-1/2}` sphere net fails because it pays `Theta(N log N)` entropy. I tested a materially different geometric route that enumerates actual facets of the Gaussian polytope instead of directions.

Let

`K=conv(g_1,...,g_M)`.

At `kappa=-1`, writing `v=-sigma/sqrt(N)`, SAT is equivalent (away from the probability-zero boundary) to the existence of `||v||=1` with `h_K(v)<=1`. Once `0` is interior to `K`, UNSAT is equivalent to every facet of `K` having distance greater than one from the origin.

Take a fixed `N`-subset of Gaussian vertices. Its affine hull is an `(N-1)`-dimensional hyperplane. The signed distance `H` of that affine hull from the origin has law

`H ~ N(0,1/N)`.

Indeed, the sample mean is independent of the centered differences; a unit normal to the centered-difference span is therefore independent of the mean, whose projection has variance `1/N`.

Conditionally on signed distance `h>0`, the remaining `M-N` Gaussian points all lie in the inward halfspace with probability `Phi(h)^(M-N)`. Thus a union bound over the `binom(M,N)` candidate facets gives the exponential bad-facet rate

`E_alpha(h)=alpha log alpha-(alpha-1)log(alpha-1)-h^2/2+(alpha-1)log Phi(h)`,

for `0<=h<=1`.

This is exponentially better organized than the naive direction net: it costs only `exp(O(N))` candidate facets. However, a numerical evaluation of the **proved exponent formula** shows the first-moment condition `sup_{0<=h<=1}E_alpha(h)<0` turns on only near `alpha≈21.52`, far above the retained rigorous upper endpoint `12.78437...`. Therefore plain facet first-moment enumeration cannot improve the current bracket. The approximate crossing is numerical only; the route comparison does not require promoting it to a theorem.

A successful facet route would need cancellation/dependence among bad facets or a sharper global face process, not a first-moment union bound.

---

## D. What this run actually changes

Source metric:

`alpha_U-alpha_L: 6.48139658710 -> 6.48139658710` (**NO MOVEMENT**).

Auxiliary mechanism movement:

1. complete `r=2` source stationarity: validated-root dimension reduced **3 -> 2** by Theorem A.2;
2. richer overlap lower route: a two-parameter weight collapses analytically to a `(b,q)` variational problem after `m_1=0`, with exact local and global formulas;
3. facet enumeration: removes the prior `N log N` net entropy but is quantitatively too weak at first moment.

Most promising next source-moving action is now sharply finite: outward-certify the two functions `S2,S3` near the `alpha=12.5` scout using the already-proved `|z|>9` tail bounds, monotone cubic inversion for `D`, and a 2D Poincare--Miranda box; then rigorously enclose the complete source comparison value. Only a successful certificate may lower `alpha_U`.
