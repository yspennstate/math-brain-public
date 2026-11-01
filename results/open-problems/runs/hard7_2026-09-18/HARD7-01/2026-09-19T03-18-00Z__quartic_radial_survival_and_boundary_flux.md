Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No movement in the frozen metric: `B=infinity -> B=infinity`. Methods tried: B8 / B13 / B21.**

# HARD7-01 run 7 — quartic radial-survival counterexample and boundary-flux reduction

Status: **PARTIAL / source OPEN / continuing the quartic-product recovery selected at STUCK1**. The frozen block-product metric is already saturated, so this run cannot honestly manufacture movement in `B`. It does materially change the remaining obligation: the run-6 suggestion that one might control the conditional quartic-energy moments from the monotonicity of the angular survival function alone is false, even for bounded centrally symmetric star-shaped sets. Convexity is therefore essential. For convex bodies I derive exact virial/boundary-flux identities and rewrite the run-6 energy-balance/variance-surplus obstruction as a boundary inequality. This gives a new, source-valid target that retains the angular convexity information lost by a one-dimensional Gamma truncation.

## 1. Continuity, source, ownership, repository state, and current-status check

I resumed the exclusive claim

`operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`

owned by HARD7-01. The canonical source target remains the full dimensional Brunn--Minkowski conjecture

\[
\mu((1-\lambda)K+\lambda L)^{1/n}
\ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}
\tag{DBM}
\]

for every `n>=1`, every even log-concave probability measure `mu` on `R^n`, every pair of nonempty centrally symmetric convex sets `K,L`, and every `lambda in [0,1]`.

This run continues the exact recovery chosen in the STUCK1 report: dimension three, the quartic product probability measure

\[
d\mu_4(x)=Z^{-1}e^{-V(x)}dx,
\qquad
V(x)=\frac{x_1^4+x_2^4+x_3^4}{4},
\tag{1.1}
\]

and arbitrary centrally symmetric convex bodies, with the source exponent `1/3`.

At run start I reread the controlling HARD7 file, the current new-methods policy and owner directive, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, the newest HARD7-01 report, the newest visible neighboring HARD7 state, and repository/intake alias searches relevant to dimensional Brunn--Minkowski. The claim remains exclusive to HARD7-01; no posted/retired/equivalent active owner was found.

The newest own checkpoint was

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T02-58-00Z__quartic_dilation_energy_reduction.md`

at commit `36bc4a751be78e8ff251d668d1d9e9e9ffaa2d1c`. It proved that any quartic-product counterexample can be normalized to a finite interior common-dilation scale satisfying an exact conditional-energy balance and a necessary variance-surplus inequality. It explicitly selected the next methods B8/B13/B21; this run follows that checkpoint rather than restarting.

A bounded fresh literature search on 2026-09-19 checked the exact source family, the quartic-product special case, the `(B)`-conjecture, and 2026 dimensional Brunn--Minkowski papers. Relevant current references remain:

- Kai-Wen Yang, *A uniform bound in the dimensional Brunn--Minkowski inequality for even log-concave measures*, arXiv:2607.10104 (11 July 2026), proving a general exponent at least `c/(n^2 log n)`, not the conjectured `1/n`.
- Alexandros Eskenazis, Apostolos Giannopoulos, Natalia Tziotziou, *Functional perimeter and the dimensional Brunn-Minkowski inequality for log-concave measures*, arXiv:2605.02747 (4 May 2026), proving a smaller general exponent and identifying gradient-geometric obstructions.
- Sotiris Armeniakos and Jacopo Ulivelli, *A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture*, arXiv:2602.23350 (26 February 2026), which confirms that dimensional Brunn--Minkowski and dilation-log-concavity mechanisms are structurally linked.
- Dario Cordero-Erausquin and Liran Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), proving both the `(B)` and Gardner--Zvavitch conjectures in the rotationally invariant class.
- Arnaud Marsiglietti, *A note on an L^p-Brunn-Minkowski inequality for convex measures in the unconditional case*, Pacific J. Math. 277 (2015), giving `(B)`-type consequences under unconditional assumptions on both the measure/body configuration.

The quartic product measure (1.1) is unconditional but not rotationally invariant; the recovery here allows an arbitrary symmetric convex body, not necessarily an unconditional one. The bounded search found no paper settling this exact source-valid quartic-product arbitrary-body `1/3` case. This is bounded negative evidence only, not a worldwide novelty certificate. The virial identities below are elementary enough that they may be folklore; novelty is **UNVERIFIED**.

## 2. Frozen metric

The canonical claim fixes

`B = largest number of 1D/2D factors for which (DBM) is proved at the source exponent for every common block-product instance`.

Run 1 already proved every finite block count, so

\[
\boxed{B=\infty\longrightarrow B=\infty.}
\]

There is **no movement** in the frozen metric. The source conjecture remains OPEN and the track remains PARTIAL.

This is the second substantive iteration in the recovery selected at STUCK1. The mathematical obligation changes in this run: a proposed one-dimensional monotonicity route is now rigorously ruled out and replaced by an exact convex-boundary criterion.

## 3. B8 — discretize the radial problem: exact Gamma/angular factorization

Put

\[
q(x)=\|x\|_4=(|x_1|^4+|x_2|^4+|x_3|^4)^{1/4},
\qquad
V(x)=q(x)^4/4.
\]

Let

\[
S_q=\{u:q(u)=1\}
\]

and let `sigma` denote the normalized cone measure on `S_q`. Quartic polar integration has the form

\[
\int_{\mathbb R^3} f(x)\,dx
=c_q\int_{S_q}\int_0^\infty f(ru)r^2\,dr\,d\sigma(u).
\tag{3.1}
\]

For `X~mu_4`, write `X=RU`, where `R=q(X)`, and define

\[
T=V(X)=R^4/4.
\]

Because `V(ru)=r^4/4` on `S_q`, (3.1) factorizes the radial and angular variables. Under `t=r^4/4`,

\[
r^2dr = c\, t^{-1/4}dt,
\]

so we obtain the exact law

\[
\boxed{
U\perp T,
\qquad
U\sim\sigma,
\qquad
T\sim \mathrm{Gamma}(a,1),\quad a=\frac34.
}
\tag{3.2}
\]

Here the Gamma density is

\[
\frac{t^{a-1}e^{-t}}{\Gamma(a)}\,dt.
\]

Now let `A` be any bounded centrally symmetric star-shaped set with positive radial function `rho_A(u)`. Define its energy cutoff

\[
H_A(u)=\frac{\rho_A(u)^4}{4}
\tag{3.3}
\]

and its angular survival function

\[
S_A(t)=\sigma\{u:H_A(u)\ge t\}.
\tag{3.4}
\]

Then `S_A` is nonincreasing and, by (3.2), the conditional radial-energy law is exactly

\[
\boxed{
\mathbb P(T\in dt\mid X\in A)
=
\frac{t^{a-1}e^{-t}S_A(t)\,dt}
{\int_0^\infty s^{a-1}e^{-s}S_A(s)\,ds},
\qquad a=3/4.
}
\tag{3.5}
\]

This is the precise one-dimensional object suggested at the end of run 6. It is useful, but the next theorem shows that **monotonicity of `S_A` alone is too weak**.

### Theorem 3.1 — two-level survival refutes the monotonicity-only moment route

There exist bounded centrally symmetric star-shaped sets `A` for which, with

\[
m_A=\mathbb E[T\mid X\in A],
\qquad
v_A=\operatorname{Var}(T\mid X\in A),
\]

we have

\[
\boxed{v_A>m_A.}
\tag{3.6}
\]

In particular, no proof of `v_A<=m_A` can use only the facts that the radial law is Gamma`(3/4,1)` and that the angular survival function `S_A(t)` is nonincreasing. Any such proof must use genuine cross-direction convexity information.

#### Proof

Set `a=3/4` and fix `c>0`. For small `eps>0`, put

\[
\delta_\varepsilon=c\varepsilon^a,
\qquad
R_\varepsilon=\varepsilon^{-1},
\]

so `delta_eps<1`. Since cone measure is atomless, choose a centrally symmetric measurable angular set `E_eps subset S_q` with

\[
\sigma(E_\varepsilon)=\delta_\varepsilon.
\]

Define a bounded centrally symmetric star-shaped set by the energy cutoff

\[
H_\varepsilon(u)=
\begin{cases}
R_\varepsilon,&u\in E_\varepsilon,\\
\varepsilon,&u\notin E_\varepsilon.
\end{cases}
\tag{3.7}
\]

Equivalently, its radial cutoff is `(4H_eps(u))^(1/4)`. Its survival function is the exact two-level function

\[
S_\varepsilon(t)=
\begin{cases}
1,&0\le t\le\varepsilon,\\
\delta_\varepsilon,&\varepsilon<t\le R_\varepsilon,\\
0,&t>R_\varepsilon.
\end{cases}
\tag{3.8}
\]

Let `gamma(s,x)` denote the lower incomplete Gamma integral. The unnormalized conditional moments are therefore

\[
D_\varepsilon
=(1-\delta_\varepsilon)\gamma(a,\varepsilon)
+\delta_\varepsilon\gamma(a,R_\varepsilon),
\tag{3.9}
\]

and, for `k=1,2`,

\[
N_{k,\varepsilon}
=(1-\delta_\varepsilon)\gamma(a+k,\varepsilon)
+\delta_\varepsilon\gamma(a+k,R_\varepsilon).
\tag{3.10}
\]

As `eps downarrow 0`,

\[
\gamma(a,\varepsilon)=\frac{\varepsilon^a}{a}+o(\varepsilon^a),
\qquad
\gamma(a+k,\varepsilon)=O(\varepsilon^{a+k}),
\tag{3.11}
\]

while `R_eps to infinity` gives

\[
\gamma(a+k,R_\varepsilon)\to\Gamma(a+k).
\tag{3.12}
\]

Hence

\[
\frac{D_\varepsilon}{\varepsilon^a}
\to \frac1a+c\Gamma(a),
\tag{3.13}
\]

and

\[
\frac{N_{k,\varepsilon}}{\varepsilon^a}
\to c\Gamma(a+k),\qquad k=1,2.
\tag{3.14}
\]

Define

\[
w=\frac{c\Gamma(a)}{a^{-1}+c\Gamma(a)}\in(0,1).
\tag{3.15}
\]

Using `Gamma(a+1)=a Gamma(a)` and `Gamma(a+2)=a(a+1)Gamma(a)`, (3.13)--(3.14) yield

\[
m_{A_\varepsilon}\to wa,
\qquad
\mathbb E[T^2\mid A_\varepsilon]\to wa(a+1).
\tag{3.16}
\]

Therefore

\[
v_{A_\varepsilon}-m_{A_\varepsilon}
\to
wa(a+1)-w^2a^2-wa
=w(1-w)a^2>0.
\tag{3.17}
\]

For all sufficiently small `eps`, (3.6) follows. `QED`

**B8 outcome:** the proposed survival-function discretization succeeded as a diagnostic and produced an exact counterexample to the monotonicity-only route. The failure is not a source counterexample because the constructed set is star-shaped rather than convex. It shows precisely what a valid proof must retain: convex compatibility between radial cutoffs in different directions.

## 4. B13 — exact boundary flux identities for convex bodies

The preceding failure suggests keeping the convex boundary instead of compressing it to the one-dimensional survival function.

Let `A` now be a bounded full-dimensional convex body containing the origin. Put

\[
Z_A=\int_A e^{-V(x)}dx,
\quad
m_A=\frac1{Z_A}\int_A V e^{-V}dx,
\quad
v_A=\frac1{Z_A}\int_A (V-m_A)^2e^{-V}dx.
\tag{4.1}
\]

Let `nu_A` be the outer unit normal, defined almost everywhere on `partial A`, and define the normalized boundary fluxes

\[
\beta_A
=\frac1{Z_A}\int_{\partial A}
\langle x,\nu_A(x)\rangle e^{-V(x)}\,d\mathcal H^2(x),
\tag{4.2}
\]

\[
\kappa_A
=\frac1{Z_A}\int_{\partial A}
V(x)\langle x,\nu_A(x)\rangle e^{-V(x)}\,d\mathcal H^2(x).
\tag{4.3}
\]

Convexity and `0 in A` imply `beta_A>=0`.

### Proposition 4.1 — quartic virial identities

For every such `A`,

\[
\boxed{\beta_A=3-4m_A,}
\tag{4.4}
\]

\[
\boxed{\kappa_A=7m_A-4(m_A^2+v_A),}
\tag{4.5}
\]

and hence

\[
\boxed{
m_A-v_A
=\frac{\kappa_A-m_A\beta_A}{4}.
}
\tag{4.6}
\]

If `beta_A>0` and

\[
r_A=\kappa_A/\beta_A
\tag{4.7}
\]

is the boundary-flux mean of `V`, then

\[
\boxed{
m_A-v_A=\frac{\beta_A}{4}(r_A-m_A).
}
\tag{4.8}
\]

#### Proof

Euler homogeneity gives

\[
\langle x,\nabla V(x)\rangle=4V(x).
\tag{4.9}
\]

Apply the divergence theorem to `x e^{-V}`:

\[
\operatorname{div}(xe^{-V})=(3-4V)e^{-V}.
\tag{4.10}
\]

After integration over `A` and division by `Z_A`, this is exactly (4.4).

Next apply the divergence theorem to `Vx e^{-V}`. Using (4.9),

\[
\operatorname{div}(Vxe^{-V})
=4Ve^{-V}+V(3-4V)e^{-V}
=(7V-4V^2)e^{-V}.
\tag{4.11}
\]

Divide the resulting boundary identity by `Z_A` to obtain

\[
\kappa_A=7m_A-4\mathbb E[V^2\mid A]
=7m_A-4(m_A^2+v_A),
\]

which is (4.5). Combining (4.4) and (4.5) gives (4.6), and (4.8) is just (4.6) divided by `beta_A`. `QED`

These identities remain valid for ordinary convex bodies with Lipschitz boundary; smooth approximation is available if one wants to avoid almost-everywhere normal language.

### Proposition 4.2 — the sought monovariant is exactly a `(B)`-property derivative

For the common-dilation orbit `A_s=e^sA`, define

\[
\Phi_A(s)=\log\mu_4(e^sA).
\tag{4.12}
\]

Then

\[
\boxed{\Phi_A'(s)=\beta_{A_s}=3-4m_{A_s},}
\tag{4.13}
\]

and

\[
\boxed{
\Phi_A''(s)
=-16(m_{A_s}-v_{A_s})
=-4(\kappa_{A_s}-m_{A_s}\beta_{A_s}).
}
\tag{4.14}
\]

Equivalently,

\[
\boxed{
\frac{d}{ds}\beta_{A_s}
=-4(\kappa_{A_s}-m_{A_s}\beta_{A_s}).
}
\tag{4.15}
\]

#### Proof

The change of variables `x=e^s y` gives

\[
\mu_4(e^sA)
=Z^{-1}e^{3s}\int_A e^{-e^{4s}V(y)}dy.
\]

Differentiation yields `Phi_A'=3-4m`, which agrees with (4.4). The run-6 exponential-family identity

\[
\frac{d}{ds}m_{A_s}=4(m_{A_s}-v_{A_s})
\]

then gives the first equality in (4.14); Proposition 4.1 gives the second. `QED`

Thus the attractive B13 candidate "prove `beta_A(s)` is nonincreasing" is not an elementary new monovariant waiting to be noticed. It is exactly the statement

\[
v_{A_s}\le m_{A_s},
\tag{4.16}
\]

or equivalently concavity of `s -> log mu_4(e^s A)`, i.e. the weak `(B)`-property for this measure/body pair. This recognition prevents the track from silently re-proving a disguised famous open mechanism.

## 5. Exact boundary form of the run-6 counterexample obstruction

The boundary identities do more than identify `(B)`. They turn the run-6 normalized-counterexample conditions into a cross-body geometric inequality.

Assume a quartic-product source counterexample exists. Run 6 shows that, after common dilation, we may work at an interior minimizing scale. Replace `K,L,M` by those scaled bodies and write

\[
M=(1-\lambda)K+\lambda L.
\]

Let

\[
w=
\frac{(1-\lambda)\mu_4(K)^{1/3}}
{(1-\lambda)\mu_4(K)^{1/3}+\lambda\mu_4(L)^{1/3}},
\qquad 1-w=w_L.
\tag{5.1}
\]

Run 6 proved the exact energy balance

\[
m_M=wm_K+(1-w)m_L
\tag{5.2}
\]

and the necessary variance surplus

\[
v_M
\ge wv_K+(1-w)v_L
+\frac13w(1-w)(m_K-m_L)^2.
\tag{5.3}
\]

By (4.4), (5.2) is equivalent to the exact boundary-flux balance

\[
\boxed{
\beta_M=w\beta_K+(1-w)\beta_L.
}
\tag{5.4}
\]

Define

\[
g_A=\kappa_A-m_A\beta_A=4(m_A-v_A).
\tag{5.5}
\]

Substituting `v_A=m_A-g_A/4` into (5.3) and using (5.2) gives

\[
g_M
\le wg_K+(1-w)g_L
-\frac43w(1-w)(m_K-m_L)^2.
\tag{5.6}
\]

Since (4.4) also gives

\[
m_K-m_L=-\frac14(\beta_K-\beta_L),
\]

we obtain the exact boundary obstruction

\[
\boxed{
 g_M
\le wg_K+(1-w)g_L
-\frac1{12}w(1-w)(\beta_K-\beta_L)^2.
}
\tag{5.7}
\]

Equivalently,

\[
\boxed{
\kappa_M-m_M\beta_M
\le
w(\kappa_K-m_K\beta_K)
+(1-w)(\kappa_L-m_L\beta_L)
-\frac1{12}w(1-w)(\beta_K-\beta_L)^2.
}
\tag{5.8}
\]

This is now the cleanest recovery target I know for the quartic special case. It contains angular convexity information through the actual boundary of each convex body, unlike the scalar survival function `S_A`.

A theorem proving the strict reverse of (5.7) for every nontrivial balanced Minkowski triple would eliminate all normalized counterexamples. A non-strict reverse inequality together with a rigidity analysis of equality would also suffice. I do **not** prove that reverse inequality here.

**B13 outcome:** succeeded structurally. The candidate moment monovariant was identified exactly with the `(B)`-property, and the stronger source-specific remaining obstruction was converted to the boundary-flux inequality (5.7).

## 6. B21 — who else has this shape: what the `(B)` literature gives and what it does not

Equation (4.14) makes the relation precise:

\[
\Phi_A''(s)\le0
\quad\Longleftrightarrow\quad
m_{A_s}-v_{A_s}\ge0
\quad\Longleftrightarrow\quad
g_{A_s}\ge0.
\tag{6.1}
\]

The bounded literature check shows why simply proving `g_A>=0` should not be treated as a routine Gamma-moment lemma:

1. The `(B)`-conjecture is a genuine named log-concavity problem for dilates of symmetric convex bodies under even log-concave measures.
2. It is known in important special settings, including Gaussian/rotationally invariant measures and several unconditional configurations.
3. The quartic product measure here is unconditional, but the source recovery allows an **arbitrary symmetric convex body**, so the standard unconditional-body theorem does not dispose of this case.
4. Armeniakos--Ulivelli (2026) explicitly connect a strengthening of dimensional Brunn--Minkowski to the `(B)`-conjecture, consistent with (4.14).

Even a proof of `g_A>=0` for every convex `A` would still not by itself contradict the normalized-counterexample condition (5.7): (5.7) is a **relative three-body curvature inequality**, not three separate sign inequalities. The useful new object is therefore

\[
A\mapsto (\beta_A,g_A)
\]

under Minkowski interpolation, with the exact quadratic correction `1/12` in (5.7).

A nearby generic Brascamp--Lieb estimate illustrates the quantitative gap. For the quartic potential,

\[
\nabla V=(x_1^3,x_2^3,x_3^3),
\qquad
\nabla^2V=\operatorname{diag}(3x_1^2,3x_2^2,3x_3^2),
\]

and formally

\[
\langle(\nabla^2V)^{-1}\nabla V,\nabla V\rangle
=\frac13\sum_i x_i^4
=\frac43V.
\tag{6.2}
\]

The convex-domain Brascamp--Lieb variance bound therefore gives, after the standard regularization at coordinate hyperplanes,

\[
v_A\le\frac43m_A.
\tag{6.3}
\]

The desired `(B)` sign would be the stronger `v_A<=m_A`. Thus the naive Hessian argument misses the decisive coefficient by exactly a factor `4/3 -> 1`; it cannot prove (6.1), much less the cross-body correction in (5.7).

**B21 outcome:** the nearest standard machinery identifies the right language but does not close the quartic recovery. The run now has an exact statement of what additional geometry a successful proof needs: a Minkowski-interpolation inequality for boundary flux/energy that is stronger than separate Brascamp--Lieb or separate `(B)` signs.

## 7. What was refuted, what was proved, and what remains open

### Refuted auxiliary route

The following strategy is now rigorously dead:

> Use only the facts that `T~Gamma(3/4,1)` before conditioning and that the radial survival function `S_A(t)` is nonincreasing to force `v_A<=m_A`.

Theorem 3.1 gives bounded centrally symmetric star-shaped counterexamples to that implication. This does **not** refute (DBM), (Q3), or the `(B)`-property for convex bodies.

### Proved in this run

For the quartic-product measure:

- exact independence and Gamma`(3/4,1)` radial-energy factorization (3.2);
- exact survival-function representation (3.5);
- an analytic two-level counterexample showing monotonicity alone permits `v>m`;
- exact convex-body virial identities (4.4)--(4.8);
- exact equivalence of the candidate flux monovariant to dilation log-concavity (4.13)--(4.15);
- exact transformation of the run-6 variance-surplus obstruction into the boundary inequality (5.7)/(5.8).

These are theorem-sized analytic claims with proofs on the page. No finite exhaustive claim is made, so no new exact-arithmetic checker was manufactured merely to certify that the run happened.

### Still open

The source target remains **OPEN**. The quartic-product `n=3` arbitrary symmetric convex-body case remains **PARTIAL**. The immediate missing theorem is a reverse/rigidity inequality strong enough to rule out (5.7) for balanced Minkowski triples.

## 8. Next route if the track continues

The next unused Section-B triple selected for this problem is

**B9 / B14 / B25**.

- **B9 (randomize):** test whether randomized centrally symmetric polytopes make the sign/size of the flux defect in (5.7) concentrate around a tractable mixed-volume expression, without treating simulation as proof.
- **B14 (find the group acting):** exploit the hyperoctahedral symmetry of `mu_4` to quotient facet configurations and isolate which irreducible angular modes can make the cross-body flux inequality fail.
- **B25 (count the same thing twice):** compute `beta_A` and `kappa_A` both from boundary facets and from the volume/energy identities (4.4)--(4.5), seeking an exact mixed-volume double count under `M=(1-lambda)K+lambda L`.

The point is no longer to prove another scalar Gamma truncation lemma. The new target must keep the convex angular coupling visible.

## 9. Capability honesty / scheduler issue requested by the owner

The requested first-line configuration still cannot be enforced by the scheduler surface exposed to this run. The interface available here provides task title, prompt, schedule, timing mode and enabled state, but **no binding model-family selector and no reasoning-effort selector**. The actual model visible to this run is GPT-5.6 Sol; the reasoning level is not exposed, so it is reported as UNVERIFIED. GPT-6/maximum remains text-requested only.

Changing this would require the platform to expose a model/reasoning selector for scheduled executions, or an authorized account/workspace control that binds those fields. A repository edit cannot change runtime model selection.

The repository policy records historical native modification probes for P26/P01/P03 that returned `You cannot modify this task`; current `RESULTS.md` also records that P26 later succeeded in a different authorized native context. For any task that still refuses modification, the compliant workaround remains authorized task/account/workspace ownership resolution or platform support, not a permission bypass and not creation of a duplicate schedule. This run made no scheduler changes.

## 10. ledger_delta

```yaml
track: HARD7-01
source: even log-concave dimensional Brunn-Minkowski conjecture
claim: operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md
status: PARTIAL
source_status: OPEN
metric: maximum low-dimensional block count B covered at source exponent for all common block-product instances
metric_before: infinity
metric_after: infinity
movement: no movement
recovery_scope: n=3 quartic product measure, arbitrary centrally symmetric convex bodies
methods: [B8, B13, B21]
new_exact_results:
  - q-radial energy T is Gamma(3/4,1), independent of cone direction
  - conditional radial law equals Gamma density times angular survival S_A(t)
  - two-level monotone survival gives bounded symmetric star-shaped examples with Var(T|A) > E[T|A]
  - beta_A = 3 - 4 m_A
  - kappa_A = 7 m_A - 4(m_A^2 + v_A)
  - m_A - v_A = (kappa_A - m_A beta_A)/4
  - normalized counterexample implies beta_M = w beta_K + (1-w) beta_L
  - normalized counterexample implies g_M <= w g_K + (1-w) g_L - w(1-w)(beta_K-beta_L)^2/12
auxiliary_route_refuted: monotone-survival-only proof of v_A <= m_A
next_methods: [B9, B14, B25]
novelty: UNVERIFIED
shared_root_modified: false
scheduler_modified: false
```
