SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B05, 2026-09-24T09:35:16Z.
attacking: QFORM-WITT-PURE13-CLOSURE-AND-HIGHLEVERAGE-COMPILER-v1 — retire the r42 pure-13 endpoint using the fresh zero-pivot closure, then expose the exact aggregate curvature that remains in the neighboring nonzero-pivot collar.

# fleet03/B05 r44 — high-leverage transverse-star compiler and aggregate coarea debt

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** quadratic coarea / equivalent interval bounds preserving arbitrary original-coordinate product densities.  
**Status:** `PROVED SUPPORTING IDENTITIES + OLD ENDPOINT RETIRED + TARGET-VALID STRESS FAMILY / FULL QFORM OPEN`.  
**Regularity:** continuity is inherited only on the cited mixed-Fresnel null-pivot branch; the pair-star and definite-pair branches used below establish essential boundedness. Full-target continuity remains open.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.


## 1. The r42 pure-13 endpoint is no longer an open branch

My immediate predecessor r42 is

`yspennstate/math-open-problems@05c329eb1b76b40cefe12e4554b96788382203fa:`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260924T074130Z-fleet03-B05-QFORM-r42/REPORT.md`.

It reduced the exact high-leverage physical-null-pivot Witt packet to

\[
Q=2aV(H+\kappa U)+\alpha V^2+2\gamma VW+\delta W^2,
\qquad S_i=a^2|\delta|\ge \frac12,
\tag{1.1}
\]

with `H` a literal original coordinate and `U,V,W` orthonormal residual product projections. At the exact rank-two-bank endpoint it isolated the `pure-13` orientation

\[
p_{12}=p_{23}=0,\qquad p_{13}^2=1,
\tag{1.2}
\]

and left `QFORM-WITT-PURE13-SHARED-MIDDLE-COAREA-v1` as the next debt.

That debt has since been superseded. The fresh fleet01/B05 theorem

`QFORM-HIGHLEVERAGE-NULLPIVOT-WITT-CLOSURE-v1`,

canonical source

`yspennstate/math-open-problems@1ca1fc77ae8435274325c25657c496fd703c0b51:`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B05/20260924T072900Z-fleet01-B05-QFORM-auto11/REPORT.md`,

proves the entire exact-rank-three high-leverage literal-null-pivot branch, without any bank-rank or `pure-13` exception:

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<781.}
\tag{1.3}
\]

Its two cases are: if all transverse physical leverages are at most `1/2`, the fleet03/B10 mixed-Fresnel null-hub theorem gives a continuous density and a bound `<9.525`; if one transverse leverage exceeds `1/2`, my earlier pair-anchored determinant-star theorem gives `<780.581`. Therefore every r42 `pure-13` state is already paid. No further run should try to interpolate its `Gamma=0` bank geometry inside the exact-null scope.

The useful successor is the neighboring **nonzero physical pivot** collar. The rest of this report derives the exact coarea currencies there.

## 2. Exact rank-three setup around an arbitrary physical pivot

Let

\[
A=RMR^T,\qquad R^TR=I_3,
\tag{2.1}
\]

have exact rank three, with `M=M^T` invertible, and write

\[
D:=|\det M|.
\tag{2.2}
\]

Fix one ORIGINAL coordinate `i` and let its spectral row have leverage

\[
c:=\|r_i\|^2>0.
\tag{2.3}
\]

A deterministic orthogonal change of basis inside the three-dimensional coefficient space, used only for algebra, puts

\[
r_i=\sqrt c\,e_1,
\tag{2.4}
\]

and then a rotation in `e_1^\perp` puts

\[
M=
\begin{pmatrix}
\mu&\beta&0\\
\beta&\alpha&\gamma\\
0&\gamma&\delta
\end{pmatrix}.
\tag{2.5}
\]

For every `j\ne i`, write

\[
r_j=(x_j,y_j,z_j),\qquad t_j=(y_j,z_j)^T,\qquad q_j=\|t_j\|^2.
\tag{2.6}
\]

No random coordinates are rotated. All probabilistic applications below remain in the original product coordinates.

Parseval immediately gives the exact transverse frame identity

\[
\boxed{\sum_{j\ne i}t_jt_j^T=I_2,\qquad \sum_{j\ne i}q_j=2.}
\tag{2.7}
\]

The physical scalar pivot is

\[
\boxed{A_{ii}=c\mu.}
\tag{2.8}
\]

Thus `mu=0` is exactly the literal-null-pivot interface, while `mu!=0` is the punctured collar.

## 3. Exact anchored principal-triple star identities

For a literal pair `{i,j}`, define the anchored determinant star

\[
T_{ij}:=\sum_{k\notin\{i,j\}}|\det A_{\{i,j,k\}}|.
\tag{3.1}
\]

Because `A_S=R_SMR_S^T` for every three-element set `S`, Cauchy-Binet gives

\[
|\det A_{\{i,j,k\}}|
=D\,\det[r_i;r_j;r_k]^2
=cD\,(y_jz_k-z_jy_k)^2.
\tag{3.2}
\]

Using (2.7),

\[
\sum_k(y_jz_k-z_jy_k)^2
=t_j^T J\left(\sum_kt_kt_k^T\right)J^Tt_j
=\|t_j\|^2=q_j,
\tag{3.3}
\]

where `J=[[0,1],[-1,0]]`. Hence, for **every** physical pivot value `mu`,

\[
\boxed{T_{ij}=cDq_j.}
\tag{3.4}
\]

Summing over `j` and observing that every anchored triple `{i,j,k}` is counted twice gives the stronger aggregate identity

\[
\boxed{
\sum_{\substack{j<k\\j,k\ne i}}|\det A_{\{i,j,k\}}|=cD,
\qquad
\sum_{j\ne i}T_{ij}=2cD.
}
\tag{3.5}
\]

This is the central new B05 currency: **the total anchored principal-triple curvature is exactly the leverage times the full rank-three determinant**, even when every individual physical pair/star is tiny.

### Immediate paid branch

My earlier theorem `QFORM-PAIR-ANCHORED-DETSTAR-COAREA-v1` gives

\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le C_\star T_{ij}^{-1/3},
\qquad
C_\star=24(3+\sqrt2)10^{2/3}=491.735145127\ldots .
\tag{3.6}
\]

Therefore under target normalization `D>=1` and a high-leverage pivot `c>=1/2`, if some

\[
q_j\ge\frac12,
\tag{3.7}
\]

then `T_{ij}>=1/4` and

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}<780.581.}
\tag{3.8}
\]

At `mu=0`, the complementary gate `q_j<=1/2` for all `j` is exactly the fleet03/B10 mixed-Fresnel null-hub hypothesis, which gives a continuous density with `<9.525`. This recovers the complete zero-pivot high-leverage closure without the r41-r42 rank-two-bank detour.

For `mu!=0`, the genuinely new hard collar can therefore be assumed to satisfy

\[
\boxed{c\ge\frac12,\quad D\ge1,\quad \mu\ne0,\quad q_j<\frac12\ \text{for every }j.}
\tag{3.9}
\]

## 4. Exact physical-pair pencil in the punctured collar

The determinant of the literal physical pair `{i,j}` also simplifies completely. Direct expansion from (2.5)-(2.6) gives

\[
\det A_{\{i,j\}}
=A_{ii}A_{jj}-A_{ij}^2
=c\Big[(\mu\alpha-\beta^2)y_j^2
      +2\mu\gamma y_jz_j
      +\mu\delta z_j^2\Big].
\tag{4.1}
\]

Define the transverse pivot pencil

\[
K:=
\begin{pmatrix}
\mu\alpha-\beta^2&\mu\gamma\\
\mu\gamma&\mu\delta
\end{pmatrix}.
\tag{4.2}
\]

Then

\[
\boxed{\det A_{\{i,j\}}=c\,t_j^TKt_j.}
\tag{4.3}
\]

Moreover

\[
\boxed{\det K=\mu\det M,\qquad |\det K|=|\mu|D.}
\tag{4.4}
\]

If `mu!=0`, `K=mu S` where `S` is the two-dimensional Schur complement of the scalar spectral pivot. Equation (4.3) is important because **all longitudinal coefficients `x_j` cancel exactly**. The physical-pair geometry in the punctured collar is controlled only by the transverse Parseval frame and the fixed quadratic pencil `K`.

## 5. Required fleet04/B05 theorem applied to an actual inequality

The designated partner theorem is fleet04/B05's

`QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`,

canonical source

`yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14:`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B05/20260924T011830Z-fleet04-B05-convex-pair-r3/REPORT.md`.

For any literal original-coordinate definite principal pair `C`, with arbitrary outside coupling retained,

\[
\|p_Q\|_{\infty,\mathrm{ess}}\le\frac\pi{\sqrt{|\det C|}}.
\tag{5.1}
\]

Apply it to `C=A_{\{i,j\}}`. If the exact pencil evaluation satisfies

\[
c\,t_j^TKt_j\ge\frac1{16},
\tag{5.2}
\]

then the pair determinant is positive, so the pair is definite, and (5.1) yields

\[
\boxed{\|p_Q\|_{\infty,\mathrm{ess}}\le4\pi<12.567.}
\tag{5.3}
\]

Thus any surviving punctured-collar state after the designated partner payment must satisfy

\[
0<c\,t_j^TKt_j<\frac1{16}
\quad\text{for every positive pencil evaluation.}
\tag{5.4}
\]

The next subsection shows why no determinant-only argument can force (5.2) from (4.4): the transverse product frame may sit exactly on the isotropic cone of `K`.

## 6. Target-valid diffuse isotropic-star family: pairwise coarea can vanish while aggregate star mass stays fixed

Let `m` be divisible by four. Define an `(m+1) x 3` Parseval frame `R` as follows. The distinguished row is

\[
r_0=(1/\sqrt2,0,0).
\tag{6.1}
\]

For the remaining `m` rows put

\[
r_j=\left(\frac1{\sqrt{2m}},\frac{s_j}{\sqrt m},\frac{t_j}{\sqrt m}\right),
\qquad s_j,t_j\in\{\pm1\},
\tag{6.2}
\]

with each of the four sign pairs `(s_j,t_j)` occurring exactly `m/4` times. Then the sign balance gives

\[
R^TR=I_3.
\tag{6.3}
\]

Take

\[
M=\operatorname{diag}(1,1,-1),\qquad A=RMR^T.
\tag{6.4}
\]

Hence

\[
\operatorname{spec}_{\ne0}(A)=\{1,1,-1\},
\tag{6.5}
\]

so this is an exact instance of the owner's three-large-eigenvalue target for every `m`. The distinguished physical pivot has

\[
c=\frac12,\qquad A_{00}=\frac12,
\tag{6.6}
\]

and every transverse row has

\[
q_j=\frac2m.
\tag{6.7}
\]

Thus the individual anchored stars are

\[
T_{0j}=cDq_j=\frac1m\longrightarrow0,
\tag{6.8}
\]

while the total anchored curvature stays fixed:

\[
\sum_{j<k}|\det A_{\{0,j,k\}}|=cD=\frac12.
\tag{6.9}
\]

Even more strongly, **there is no definite physical principal pair anywhere in this family**. For the hub-residual pairs, (4.3) has

\[
K=\operatorname{diag}(1,-1),
\tag{6.10}
\]

and every transverse row is isotropic, so

\[
\det A_{\{0,j\}}=0.
\tag{6.11}
\]

For two residual rows, each diagonal entry is `1/(2m)`. Their off-diagonal entry is

\[
A_{jk}=\frac1m\left(\frac12+s_js_k-t_jt_k\right),
\tag{6.12}
\]

where `s_js_k-t_jt_k` belongs to `{0,2,-2}`. Consequently

\[
\det A_{\{j,k\}}
\in\left\{0,-\frac6{m^2},-\frac2{m^2}\right\}\le0.
\tag{6.13}
\]

So the fleet04/B05 definite-pair mechanism is genuinely unavailable on this exact target family, and the best single anchored star tends to zero, despite the dimension-free aggregate identity (6.9). This is **not** a counterexample to QFORM. It is a sharp obstruction to pair selection and confirms the existing correction that product curvature must be aggregated before reciprocal physical-minor payment.

The example also shows the exact missing factor in the punctured collar: one must spend the constant total star mass (3.5) **jointly across the diffuse isotropic transverse frame**, rather than select one `j` or one definite physical pair.

## 7. New compiler and next exact implication

Combining the preceding identities gives the following deterministic/probabilistic compiler.

### `QFORM-HIGHLEVERAGE-TRANSVERSE-STAR-COMPILER-v1`

For every exact-rank-three target-normalized form `A=RMR^T` and every original coordinate `i` with spectral leverage `c_i>=1/2`:

1. the anchored total principal-triple mass is exactly
   \[
   \sum_{j<k}|\det A_{\{i,j,k\}}|=c_i|\det M|\ge\frac12;
   \]
2. if some transverse row has `q_j>=1/2`, the pair-star theorem gives `||p_Q||_(infinity,ess)<780.581`;
3. if the physical pivot is zero and all `q_j<=1/2`, the mixed-Fresnel null-hub theorem gives a continuous density with `||p_Q||_infinity<9.525`;
4. if the physical pivot is nonzero, the literal pair determinants are exactly `c_i t_j^T Kt_j`, with `det K=mu det M`; any positive determinant at least `1/16` is paid by the designated fleet04/B05 theorem with `||p_Q||_(infinity,ess)<=4pi`.

Therefore the remaining high-leverage exact-rank-three B05 obstruction is not the r42 pure-13 endpoint. It is the **diffuse nonzero-pivot aggregate-star collar** where

\[
\mu\ne0,\qquad q_j<\frac12\ \forall j,
\tag{7.1}
\]

and the fixed mass `cD` in (3.5) is spread over arbitrarily many small stars, potentially along the isotropic cone of `K` as in Section 6.

The first next implication is

`QFORM-HIGHLEVERAGE-AGGREGATE-STAR-COAREA-v1`:

> Prove a product-preserving interval/coarea inequality that spends
> \[
> \sum_{j<k}|\det A_{\{i,j,k\}}|=c_iD
> \]
> before selecting or inverting a physical pair, uniformly through the nonzero-to-zero scalar-pivot interface. A bound of the form
> \[
> \|p_Q\|_{\infty,\mathrm{ess}}\le C(c_iD)^{-1/3}
> \]
> in this exact-rank-three high-leverage scope would close the entire branch.

The fresh fleet01/B05 stress theorem shows why the scalar-pivot-first half-Riesz route is not this receiver: on an exact target family its certificate has an unavoidable `log(1/|A_ii|)` divergence even though another grouped mechanism controls the actual density uniformly. The grouped star must therefore be spent before the one-sided square majorant or a reciprocal physical minor.

## 8. Scope audit

**Proved in this run:** the exact star identities (3.4)-(3.5) for arbitrary pivot; the exact transverse pair-pencil identity (4.3)-(4.4); the quantitative compiler in Section 7; the target-valid family (6.1)-(6.13) with no definite physical pair, vanishing maximum anchored star, and fixed aggregate anchored curvature; retirement of the r42 pure-13 endpoint by a fresh complete existing-worker theorem.

**Partner actually applied:** fleet04/B05 definite-pair coarea theorem at (5.2)-(5.3).

**Not proved:** the aggregate-star coarea inequality in Section 7, the full exact-rank-three problem, arbitrary higher-rank matrices, the full QFORM conjecture, or full-target continuity. No counterexample to QFORM is claimed.

## 9. Sources actually used

- Own r42: `math-open-problems@05c329eb1b76b40cefe12e4554b96788382203fa`.
- Fresh zero-pivot high-leverage closure: `math-open-problems@1ca1fc77ae8435274325c25657c496fd703c0b51`.
- Null-hub mixed-Fresnel theorem: `math-open-problems@c0d7e627b3b877fcecc3004a58335658f6541d64`.
- Designated fleet04/B05 definite-pair theorem: `math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`.
- Fresh scalar-pivot logarithmic-barrier report: `math-open-problems@1ac275fbdb84feaca340834f7e127ae042ed66d7`.

Manual changed-file review: only mathematical content and nonsecret repository/run identifiers are present. No credentials, personal archives, financial/client data, model/API purchases, remote workflows, permissions, or public-release settings are involved.
