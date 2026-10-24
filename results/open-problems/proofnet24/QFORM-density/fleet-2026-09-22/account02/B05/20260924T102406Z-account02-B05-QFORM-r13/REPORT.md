SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-24T10:24:06Z.
attacking: QFORM-DIFFUSE-ISOTROPIC-STAR-MIXEDBASIS-CLOSURE-v1 — close the fresh account03/B05 diffuse isotropic-star stress family by an original-coordinate mixed-basis interval/Fourier receiver, then isolate the aggregate nonzero-pivot compiler still missing.

# account02/B05 r13 — diffuse isotropic-star mixed-basis closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Status:** `PROVED SUPPORTING THEOREM / FRESH r44 STRESS FAMILY CLOSED`; full unrestricted QFORM remains **OPEN**.  
**Regularity:** continuous density is proved for the `m>=8` mixed-basis branch; the `m=4` principal-block branch gives essential boundedness from the pinned theorem. Full-target continuity remains separate/open.  
**Execution:** authenticated GitHub brain/control retrieval was used in this run; no native learned-memory ingestion is claimed.

The live corrections remain binding. Nothing below uses an arbitrary-joint rank-three coarea estimate, post-rotation probabilistic independence, an unrestricted curved-fiber supremum, a conditional projected-density cap, law-uniform pointwise quadratic-phase decay, moments, bounded support, connected support, log-concavity, or deletion of a small random tail.

## 1. Fresh sources and the first unpaid implication

Fresh owner control was resolved from `yspennstate/math-research-brain/main` at pre-write head

`e77cb487f09dc2224415a17c34ca01a3ef271883`,

with OWNER CONTROL revision `2026-09-22.15`, QFORM-only.  The current exclusive-sign-in continuation, proof-first request, mutable Claude/Fisher continuation, programme MANIFEST/CURRENT_RESEARCH/CLAIMS/DELTAS/CORRECTION_INBOX/PATHWAYS/MEMORY_PROTOCOL, `fleet.json`, `roles.json`, `PROTOCOL.md`, and `assignments/account02/B05.json` were read fresh.

The latest compatible designated partner account03/B05 result is r44; the path-local commit stream was checked through its 09:59:13Z receipt commit

`4ee5ba1696f8d586477af9933d031e5ab3c1369c`,

with report

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T093516Z-account03-B05-QFORM-r44/REPORT.md`.

R44 retires the old exact-null `pure-13` endpoint using the completed high-leverage null-pivot closure and moves to the neighboring **nonzero physical pivot collar**.  For an exact-rank-three representation

\[
A=RMR^T,\qquad R^TR=I_3,\qquad D=|\det M|,
\]

with distinguished spectral row `r_i=sqrt(c)e_1`, it puts

\[
M=\begin{pmatrix}
\mu&\beta&0\\
\beta&\alpha&\gamma\\
0&\gamma&\delta
\end{pmatrix},
\qquad
r_j=(x_j,y_j,z_j),\quad t_j=(y_j,z_j).
\]

Its exact aggregate identities are

\[
\sum_{j\ne i} t_jt_j^T=I_2,
\qquad
T_{ij}:=\sum_k|\det A_{\{i,j,k\}}|=cD\,\|t_j\|^2,
\]

and

\[
\boxed{\sum_{j<k}|\det A_{\{i,j,k\}}|=cD.} \tag{1.1}
\]

After the existing pair-star and definite-pair exits, the hard collar can have every individual transverse row small while the total star (1.1) stays universal.  R44 supplies an exact target-valid family demonstrating that this obstruction is real.

The first unpaid implication at the start of this run was therefore not the retired null-pivot interpolation.  It was to determine whether r44's diffuse isotropic-star family is itself a counterexample mechanism or whether its aggregate curvature can be spent before selecting a minor.

## 2. The r44 diffuse isotropic-star target family

Let `m` be divisible by four.  The physical spectral frame consists of

\[
r_0=(2^{-1/2},0,0), \tag{2.1}
\]

and residual rows

\[
r_j=\left((2m)^{-1/2},\frac{s_j}{\sqrt m},\frac{t_j}{\sqrt m}\right),
\qquad (s_j,t_j)\in\{\pm1\}^2, \tag{2.2}
\]

with each of the four sign pairs occurring exactly `m/4` times.  Take

\[
M=\operatorname{diag}(1,1,-1). \tag{2.3}
\]

The sign balance gives `R^TR=I_3`, so the nonzero spectrum of `A=RMR^T` is exactly

\[
\{1,1,-1\}. \tag{2.4}
\]

This is an exact instance of the owner's target for every `m`.  R44 proves:

- the distinguished leverage is `c=1/2` and `A_{00}=1/2`;
- every transverse row has `q_j=2/m`;
- every individual anchored determinant star is `T_{0j}=1/m ->0`;
- the total anchored star remains `1/2`;
- every hub-residual physical pair is singular and every residual physical principal pair has nonpositive determinant, so **no definite physical pair exists anywhere**.

Thus a single-pair or single-minor coarea strategy genuinely loses dimension on this family.  I now show that the whole family nevertheless has a uniform bounded density by a product-preserving mixed-basis receiver.

## 3. Exact original-coordinate factorisation

Partition the residual coordinates into the four sign classes

\[
A=(+,+),\qquad B=(+,-),\qquad C=(-,+),\qquad D=(-,-), \tag{3.1}
\]

all of size `m/4`.

Let

\[
L=B\cup C,\qquad R_*=A\cup D. \tag{3.2}
\]

On the ORIGINAL coordinates of `L` define

\[
u_j=\begin{cases}
\sqrt{2/m},&j\in B,\\
-\sqrt{2/m},&j\in C,
\end{cases}
\qquad U=u\cdot X_L, \tag{3.3}
\]

and on the disjoint ORIGINAL coordinates of `R_*` define

\[
v_j=\begin{cases}
\sqrt{2/m},&j\in A,\\
-\sqrt{2/m},&j\in D,
\end{cases}
\qquad V=v\cdot X_{R_*}. \tag{3.4}
\]

Both coefficient vectors have Euclidean norm one, and the two active banks are independent because they are disjoint sets of original independent coordinates.

Write the three spectral linear forms as

\[
Y_k=\langle R e_k,X\rangle. \tag{3.5}
\]

From (2.2),

\[
Y_2-Y_3=\sqrt2\,U,
\qquad
Y_2+Y_3=\sqrt2\,V. \tag{3.6}
\]

Therefore

\[
Y_2^2-Y_3^2=(Y_2-Y_3)(Y_2+Y_3)=2UV. \tag{3.7}
\]

The remaining spectral coordinate is

\[
H:=Y_1=rac{X_0}{\sqrt2}+\frac1{\sqrt{2m}}\sum_{j=1}^m X_j. \tag{3.8}
\]

Consequently the **entire quadratic form** is exactly

\[
\boxed{Q=H^2+2UV.} \tag{3.9}
\]

No random coordinate has been rotated.  The variable `H` is allowed to share the active `L` and `R_*` sources; only the literal coordinate `X_0` is the independent outside variable in the mixed-basis theorem below.

## 4. Spend the account01/B03 mixed-basis theorem

The source-valid theorem `QFORM-MIXED-BASIS-TRIPLE-FRESNEL-v1` is in

`yspennstate/math-open-problems@3d991ad3ab91593155b0b465007f4938968a14bf:`
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T111508Z-account01-B03-QFORM-auto11/REPORT.md`.

Its packet is

\[
T=a^{-1}H^2+2\sigma UV
\]

with `U` and `V` living on disjoint original-coordinate banks, while `H` may contain linear forms from both banks plus an independent outside variable.  If on the right bank the two-column rows `(h_j,v_j)` have squared two-volume

\[
E_2=\det\sum_{j\in R_*}(h_j,v_j)^T(h_j,v_j)>0,
\]

and `delta_mix` is the probability that two iid mixed determinant-basis triples are source-disjoint, then

\[
\boxed{
\|p_T\|_\infty
\le12\left(\frac{|a|}{\sigma^2E_2\delta_{mix}}\right)^{1/3}.
} \tag{4.1}
\]

The proof is an integrated Fourier/Brascamp--Lieb estimate in original product coordinates and gives a continuous `C_0` density.

For (3.9), `a=sigma=1`.  On `R_*=A union D`,

\[
h_j=(2m)^{-1/2},\qquad
v_j=\begin{cases}\sqrt{2/m},&j\in A,\\-\sqrt{2/m},&j\in D.\end{cases} \tag{4.2}
\]

The exact right-bank Gram matrix is

\[
\sum_{j\in R_*}
\binom{h_j}{v_j}(h_j,v_j)
=egin{pmatrix}1/4&0\\0&1\end{pmatrix}, \tag{4.3}
\]

hence

\[
\boxed{E_2=1/4.} \tag{4.4}
\]

The only nonzero two-row determinants in `R_*` pair one `A` coordinate with one `D` coordinate.  For such a pair,

\[
D_{AD}=h_Av_D-h_Dv_A=-\frac2m,
\qquad D_{AD}^2=\frac4{m^2}. \tag{4.5}
\]

A mixed determinant basis therefore consists of one coordinate from `L`, one from `A`, and one from `D`.  Since `u_l^2=2/m` for every `l in L`, every such triple has the same normalized weight:

\[
\frac{(2/m)(4/m^2)}{E_2}=rac{32}{m^3}. \tag{4.6}
\]

There are `(m/2)(m/4)(m/4)=m^3/32` such triples, so the induced basis law is exactly uniform and factorises across the three class choices.

Two iid bases are disjoint iff their `L`, `A`, and `D` coordinates are all different.  Hence

\[
\boxed{
\delta_{mix}=\left(1-\frac2m\right)
              \left(1-\frac4m\right)^2.
} \tag{4.7}
\]

For every divisible-by-four `m>=8`, each factor is increasing in `m`, and at `m=8`

\[
\delta_{mix}=\frac34\left(\frac12\right)^2=\frac3{16}. \tag{4.8}
\]

Thus

\[
E_2\delta_{mix}\ge\frac3{64}. \tag{4.9}
\]

Substitution into (4.1) gives the full-line estimate

\[
\boxed{
\|p_Q\|_\infty
\le12\left(\frac{64}{3}\right)^{1/3}
=\frac{48}{3^{1/3}}
=33.2813411688\ldots,
\qquad m\ge8.
} \tag{4.10}
\]

This is the central new result.  It pays exactly the family on which **every definite physical pair disappears and every individual anchored star tends to zero**.  The proof spends a mixed three-coordinate volume distribution before choosing any reciprocal minor.

## 5. The exceptional case m=4: apply the pinned completed principal-block theorem

When `m=4`, the mixed-basis disjointness parameter in (4.7) is zero because the classes `A` and `D` each contain only one coordinate.  This is a finite-dimensional entropy degeneracy, not an output-density obstruction.

Take the ORIGINAL principal triple consisting of coordinate `0`, the unique `A=(+,+)` coordinate, and the unique `B=(+,-)` coordinate.  Its physical matrix is exactly

\[
C_4=
\begin{pmatrix}
1/2&1/4&1/4\\
1/4&1/8&5/8\\
1/4&5/8&1/8
\end{pmatrix}. \tag{5.1}
\]

A direct determinant calculation gives

\[
\det(\lambda I-C_4)
=\frac{(\lambda-1)(2\lambda+1)(4\lambda-1)}8, \tag{5.2}
\]

so

\[
\operatorname{spec}(C_4)=\{1,-1/2,1/4\}. \tag{5.3}
\]

Now apply the pinned `e5f71d79.../COUNTEREXAMPLE_SEARCH.md` Theorem A to this **actual original-coordinate principal block**.  Conditioning the other two original coordinates introduces only affine terms in the retained triple, and Theorem A allows those.  Since every eigenvalue of `C_4` has modulus at least `1/4`,

\[
\boxed{
\|p_Q\|_{\infty,\mathrm{ess}}
\le\frac{6\sqrt\pi}{1/4}
=24\sqrt\pi
=42.5388924217\ldots .
} \tag{5.4}
\]

Thus the r44 stress family is uniformly paid for **every** allowed `m`.

### Theorem `QFORM-DIFFUSE-ISOTROPIC-STAR-MIXEDBASIS-CLOSURE-v1`

For every divisible-by-four `m>=4`, every choice of independent original-coordinate input laws with densities at most one, and the r44 matrix defined by (2.1)-(2.3),

\[
\boxed{
\|p_{X^TAX}\|_{\infty,\mathrm{ess}}<42.539.
} \tag{5.5}
\]

For `m>=8` the stronger continuous-density bound (4.10) holds.

## 6. The pinned ruled theorem applied to the same family

The required pinned `e5f71d79.../COUNTEREXAMPLE_SEARCH.md` Theorem C proves, for an exact normalized signature `(2,1)` form, the one-sheet side bound

\[
p_Q(s)\le\pi\sqrt2. \tag{6.1}
\]

Our family has exact nonzero spectrum `{1,1,-1}`, so Theorem C applies directly and gives

\[
\boxed{p_Q(s)\le\pi\sqrt2=4.4428829381\ldots\quad(s\ge0).} \tag{6.2}
\]

Hence the genuinely new content of Sections 3-5 is not a reproof of the ruling.  It supplies a **full-line bound**, and therefore pays the convex/two-sheet side of this diffuse isotropic-star construction as well.

The pinned counterexample search reports no target-valid counterexample.  The present calculation further removes r44's sharpest pair-selection stress family as a counterexample mechanism.

## 7. What this teaches about the general nonzero-pivot collar

R44's total star identity (1.1) says that high-leverage rank-three curvature can remain universal while every individual pair certificate tends to zero.  The successful factorisation here explains how that aggregate resource can be used without selecting a tiny minor:

1. diagonalise only the **deterministic transverse coefficient geometry** into complementary sign banks;
2. factor the indefinite transverse quadratic as a product `2UV` of linear forms supported on disjoint original-coordinate banks;
3. keep the hub square `H^2` sharing both banks rather than conditioning on it;
4. use the determinant-basis distribution and its source-disjointness probability before Fourier inversion.

The family is unusually symmetric, so this factorisation is exact with `E2=1/4` and a simple basis law.  The general r44 collar does not yet supply a universal lower bound for the analogous mixed-basis determinant entropy.

The first unpaid implication is therefore

`QFORM-PUNCTURED-TRANSVERSE-STAR-MIXEDBASIS-COMPILER-v1`:

> In the exact-rank-three high-leverage nonzero-pivot collar
> \(c\ge1/2, D\ge1, \mu\ne0, q_j<1/2\), use the aggregate identity
> \(\sum_{j<k}|\det A_{\{i,j,k\}}|=cD\)
> to force either an already-paid pair-star/definite-pair/Fresnel exit or a source-disjoint mixed-basis packet whose quantity \(\sigma^2E_2\delta_{mix}\) is bounded below by a universal multiple of the available spectral currency.  The aggregation must occur before reciprocal minor selection.

A valid proof may not regard the small pivot `mu` as a small random perturbation, condition on a projected shared variable and assign it a cap, replace the product projection by an arbitrary bounded joint law, or take a curved-fiber supremum.

## 8. Source audit and finite algebra checks

Required pinned inputs were read at exact source commit

`e5f71d79eff325201dd0274053d20268ce65b837`:

- `RESULTS.md`;
- `FOURIER_ROUTE_REPORT.md`;
- `COUNTEREXAMPLE_SEARCH.md`.

The fresh partner r44 path history was checked after the global math branch refresh; no later account03/B05 report than r44 was present in the path-local commit stream.  The `m=4` matrix (5.1) was independently symbolically checked to have characteristic polynomial (5.2), eigenvalues `{1,-1/2,1/4}`, and determinant `-1/8`.  The constant in (4.10) is `33.281341168830465`; the finite case constant is `24 sqrt(pi)=42.538892421732385`.

Changed-file scope was manually reviewed before publication: this report and its companion early calculation contain only authorized mathematical/control provenance, no credentials, account secrets, scheduler identifiers, machine paths, unrelated private data, or public-release action.  No automated repository secret scanner is exposed through the present connector, so this is a limited manual fallback review rather than a claim of an automated scan.

**Independent review:** PENDING.  
**Full unrestricted QFORM:** OPEN.  
**Full-target continuity:** OPEN.
