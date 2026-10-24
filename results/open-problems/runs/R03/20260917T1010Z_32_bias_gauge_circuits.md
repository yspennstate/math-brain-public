Model actually ran: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but the exposed runtime provides no model-family selector, no reasoning-effort selector, and no authenticated applied-runtime telemetry, so I do not claim otherwise. NO MOVEMENT on the frozen full-domain metric: `r(10)=222.6104736743168493957921796888577...` remains exact and `r(11)<=523.9022787113135428552389980...` remains the best certified upper bound; unchanged count `1 -> 2`. Methods #6 DEFORM TO A POINT YOU CAN SOLVE, #8 GO THE OTHER WAY AND DISCRETIZE, #26 HUNT THE SPORADIC CASE.**

# R03 run32 — gauge-averaged bias deformation, circuit discretization, and a prior-art correction

Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL; source OPEN.** This run does not lower the finite full-domain remainder envelope. It does three things that materially change the route map:

1. finds a directly relevant 2006 theorem showing that the conceptual affine-hyperplane reduction of run31 was already known in a closely equivalent 0/1 formulation, so the novelty status of C285 is corrected;
2. derives an exact row/column-gauge-averaged change-of-measure formula for a vanishing sign bias and a sharp subcritical second-moment limit, exposing a concrete triangular-array route from the solved non-uniform regime toward the uniform problem;
3. discretizes affine excess into weighted hypercube-circuit completions and exhibits a full-support two-level family showing simultaneously why pointwise section bounds fail and why a low-complexity exceptional family is nevertheless harmless after basis weighting.

No new exact-arithmetic checker is manufactured this run. The new claims are symbolic identities/asymptotic proofs with no finite computational core; adding a checker solely to record activity would violate the owner's 90/10 rule.

## 1. Continuity, fixed quantity, and source match

I continued from `runs/R03/20260917T0917Z_31_affine_excess.md`; no killed route, certificate, metric, or stagnation count was reset.

Before new mathematics I recovered/read the current campaign `INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest own report, the newest neighboring R04 retirement handoff, and targeted F0001/Rademacher-singularity history. No posted/excluded result closes F0001, R03 has not reached the hard-task stuck limit, and no queue rotation is authorized.

The original/current source is Jain--Sah--Sawhney, `arXiv:2010.06554` / GAFA 31 (2021). Their Conjecture 1.1 gives, for a discrete entry law `xi`, the elementary contribution

\[
2n\Pr(E_{e_1})+n(n-1)\Pr(E_{e_1-e_2})+n(n-1)\Pr(E_{e_1+e_2}).
\]

For iid uniform signs, the zero-row term vanishes and each equal/opposite column event has probability `2^(-n)`. Hence the source-matched target is exactly

\[
\boxed{\Pr(\det B_n=0)=(1+o(1))\,n(n-1)2^{1-n}.}
\]

Jain--Sah--Sawhney still prove the sharp full elementary-mechanism formula only when the entry law is **not uniform on its support**. For the uniform-support case they obtain the correct exponential scale and a sharp structured/compressible contribution, not the polynomial prefactor. Their paper explicitly calls uniform support the main remaining case and records unresolved issues in Irmatov's 2020 claimed proof.

Later literature was rechecked. Song--Wang `arXiv:2607.00495` controls growing corank, and Hunter--Kwan--Sauermann--Sawhney `arXiv:2510.12933` (now IMRN 2026(12), rnag126) gives `exp(-c n k)` large-corank suppression. Neither determines the sharp corank-one prefactor. A bounded fresh search on 2026-09-17 found no later primary resolution; this is negative-search evidence, not a worldwide novelty certificate.

As before, with `T_n` the exact union of signed equal/opposite row-pair and column-pair events,

\[
r(n):=2^n\Pr(\det B_n=0,T_n^c),
\]

and retained C225 reduces source closure to

\[
\boxed{r(n)=o(n^2).}
\]

The strongest replay-certified finite envelope is unchanged:

\[
\boxed{r(10)=222.6104736743168493957921796888577\ldots}
\]

exactly, and

\[
\boxed{r(11)\le 523.9022787113135428552389980\ldots .}
\]

All earlier certified branches for the rest of the full `n`-range remain retained.

The dated source/prior-art record for this run is `artifacts/R03/20260917T1010Z_32_source_status.md`, creation commit `e3170bea10363bee07753a886686fb3b6383cff4`.

## 2. Prior-art correction: run31's geometric equivalence is not conceptually new

A directly relevant paper missed by the preceding affine-excess runs is Thomas Voigt and Guenter M. Ziegler, *Singular 0/1-Matrices, and the Hyperplanes Spanned by Random 0/1-Vectors*, CPC 15 (2006), 463--471, `arXiv:math/0308050`.

Let `P_s(d)` be the singularity probability of a uniform `d x d` 0/1 matrix, and let `E_VZ(d)` be the expected number of cube vertices in the hyperplane spanned by a random independent `(d-1)`-set of 0/1 vectors. Their Theorem 1.1 states

\[
\boxed{
P_s(d)=\left(2^{-d}E_{VZ}(d)+\frac{d^2}{2^{d+1}}\right)(1+o(1)).
}
\tag{VZ}
\]

They give the lower bound `E_VZ(d) >= d^2/2(1+o(1))` from the fat coordinate/equality hyperplanes and state the strict equivalence between the conjectured singularity asymptotic and

\[
E_{VZ}(d)\sim d^2/2.
\]

They also explicitly note that symmetry permits an affine version.

The sign problem is exactly the same `0/1` problem with one dimension removed. Given a uniform sign matrix of order `n=d+1`, row/column sign normalization makes the first row and column all `+1`, leaving an independent uniform sign block `C` of order `d`. Subtracting the first row gives

\[
\det B_n=0
\quad\Longleftrightarrow\quad
\det(C-J)=0
\quad\Longleftrightarrow\quad
\det\left(\frac{J-C}{2}\right)=0,
\]

where `(J-C)/2` is a uniform `d x d` 0/1 matrix. Thus

\[
\Pr(\det B_{d+1}=0)=P_s(d)
\]

exactly, and the Rademacher target becomes

\[
P_s(d)\sim d(d+1)2^{-d}\sim d^2 2^{-d}.
\]

Substituting into (VZ) shows again that the source conjecture is equivalent to `E_VZ(d)~d^2/2`.

**Correction to the R03 novelty ledger.** C285 remains a valid exact, collision-deleted, sign-gauge normalization that is convenient for the present campaign. But its conceptual statement — sharp singularity is equivalent to saying a random cube-spanned hyperplane has only the trivial expected excess — is prior art, essentially Voigt--Ziegler Theorem 1.1 / Corollary 1.2. Future paper-level discussion must cite Voigt--Ziegler and must not present C285's geometric equivalence as novel.

This correction is itself useful: Voigt--Ziegler already use strong-rank stratification and Littlewood--Offord to make the lower-rank pieces negligible. The genuinely missing quantity has been the rank-`d-1` weighted hyperplane excess for at least twenty years.

## 3. Method #6 — deform the uniform law, but average over its exact symmetry first

The naive idea is to approach the uniform sign law from the non-uniform regime solved by Jain--Sah--Sawhney. A raw product-measure change of measure loses too much. The new move is to exploit the fact that the event of interest is invariant under **all independent row and column sign flips** before comparing measures.

For `|m|<1`, let `P_m` be the iid sign law with

\[
\Pr_m(B_{ij}=+1)=\frac{1+m}{2},\qquad
\Pr_m(B_{ij}=-1)=\frac{1-m}{2}.
\]

Thus `m=0` is the target uniform law. Relative to `P_0`, the raw likelihood is

\[
L_m(B)=\prod_{i,j}(1+mB_{ij}).
\]

Let independent `r_i,c_j in {+/-1}` act by

\[
B_{ij}\mapsto r_i c_j B_{ij}.
\]

For any event `A` invariant under row/column sign flips — in particular `A={det B=0,T_n^c}` — average the biased law over this group. Its likelihood relative to `P_0` is

\[
\overline L_m(B)
=
2^{-2n}\sum_{r,c}\prod_{i,j}(1+m r_i c_j B_{ij}),
\]

and invariance gives the exact identity

\[
\boxed{P_m(A)=E_0[1_A\overline L_m].}
\tag{C286.1}
\]

### C286(a): exact cycle-space Fourier expansion

Expand the product. A monomial indexed by an edge set `F subset E(K_{n,n})` survives the average over `r,c` iff every row-vertex and every column-vertex has even degree in `F`. Therefore

\[
\boxed{
\overline L_m(B)
=
\sum_{F\in\mathcal E(K_{n,n})}
 m^{|F|}\chi_F(B),
}
\tag{C286.2}
\]

where `mathcal E(K_{n,n})` is the binary cycle space (Eulerian edge sets) and `chi_F(B)=prod_{(i,j) in F}B_{ij}`.

This shows exactly what the full gauge symmetry buys: there are no nonconstant Fourier terms of degrees `1,2,3`; the first possible perturbations are 4-cycles.

### C286(b): universal lower bound and a one-sided transfer theorem

Every factor is positive for `|m|<1`, so Jensen's inequality gives

\[
\log\overline L_m(B)
\ge
E_{r,c}\sum_{i,j}\log(1+m r_i c_j B_{ij}).
\]

For each edge, `r_i c_j B_{ij}` is marginally uniform on `{+/-1}`, hence

\[
E\log(1+m r_i c_j B_{ij})
=\frac12\log(1-m^2).
\]

Thus, **uniformly in the matrix `B`**,

\[
\boxed{
\overline L_m(B)\ge(1-m^2)^{n^2/2}.
}
\tag{C286.3}
\]

Combining with (C286.1), every gauge-invariant event obeys

\[
\boxed{
P_0(A)
\le
(1-m^2)^{-n^2/2}P_m(A).
}
\tag{C286.4}
\]

This is an actionable reduction. At the triangular bias

\[
m_n=c/n,
\]

one has

\[
(1-m_n^2)^{-n^2/2}\to e^{c^2/2}.
\]

Moreover a fixed signed row pair is equal or opposite under `P_m` with total probability

\[
2^{-n}\big[(1+m^2)^n+(1-m^2)^n\big].
\tag{C286.5}
\]

At `m=c/n`, this is `2^{1-n}(1+o(1))`, the same elementary scale as the uniform problem. Consequently:

> **If the Jain--Sah--Sawhney non-uniform sharp remainder estimate could be extended uniformly to the triangular two-point law with bias `m_n=c/n` (any fixed nonzero `c`), in the form**
> \[
> P_{m_n}(\det B_n=0,T_n^c)=o(n^2 2^{-n}),
> \]
> **then (C286.4) would immediately imply the full uniform Rademacher conjecture.**

This is much more precise than the vague instruction “let the bias go to zero.”

### C286(c): exact second moment and the critical `n^{-1/2}` scale

Under `P_0`, Walsh characters are orthonormal, so (C286.2) gives

\[
E_0\overline L_m^2
=
\sum_{F\in\mathcal E(K_{n,n})}m^{2|F|}.
\tag{C286.6}
\]

Put `x=m^2`. The even-subgraph generating function has the exact spin representation

\[
Z_n(x):=\sum_{F\in\mathcal E(K_{n,n})}x^{|F|}
=2^{-2n}\sum_{r,c}\prod_{i,j}(1+x r_i c_j).
\]

If `S_n=sum_i r_i`, summing first over the column spins gives

\[
\boxed{
Z_n(x)
=(1-x^2)^{n^2/2}
E\left[\cosh(\operatorname{artanh}(x)S_n)^n\right].
}
\tag{C286.7}
\]

Now set

\[
m=t/\sqrt n,\qquad x=t^2/n.
\]

For every fixed `|t|<1`, the central limit theorem and uniform integrability give

\[
\boxed{
E_0\overline L_{t/\sqrt n}^{\,2}
\longrightarrow
\frac{e^{-t^4/2}}{\sqrt{1-t^4}}.
}
\tag{C286.8}
\]

**Proof of the uniform-integrability step.** Write `a_n=artanh(t^2/n)`. Then

\[
n\log\cosh(a_nS_n)
=\frac{t^4}{2}\frac{S_n^2}{n}+o_P(1).
\]

Also `log cosh u <= u^2/2`, so the integrand is bounded by

\[
\exp\left(\beta_n S_n^2/n\right),
\qquad
\beta_n=\frac{n^2a_n^2}{2}\to t^4/2<1/2.
\]

For any fixed `beta<1/2`, the Gaussian integral identity and `cosh z <= exp(z^2/2)` give

\[
E\exp(\beta S_n^2/n)
\le (1-2\beta)^{-1/2},
\]

uniformly in `n`. Hence the family is uniformly integrable, and the limit is the Gaussian moment

\[
E\exp(t^4G^2/2)=(1-t^4)^{-1/2},
\]

multiplied by `(1-t^4/n^2)^{n^2/2}->e^{-t^4/2}`. QED.

Thus, after quotienting the exact symmetry, the biased and uniform laws have **bounded chi-square divergence at the natural mechanism-changing scale `m=t/sqrt(n)` for `|t|<1`**. The first nontrivial small-`t` term is order `t^8`, reflecting the 4-cycle minimum in the Eulerian Fourier expansion.

This is genuine structural information, but it is not yet a rare-event transfer theorem: an `L^2` comparison square-roots probabilities and cannot by itself control an event of size `2^{-n}` sharply.

### Why the published JSS non-uniform proof still does not bridge the needed window

The final deduction of Jain--Sah--Sawhney Theorem 1.2 chooses an auxiliary `epsilon>0` with

\[
\exp(2\epsilon-H(p))<\|p\|_2^2.
\]

The available entropy margin is therefore

\[
\Delta(p):=H(p)+\log\|p\|_2^2,
\]

strictly positive precisely for non-uniform laws and zero at a uniform law.

For the two-point sign law with bias `m`, direct expansion gives

\[
\boxed{
\Delta(m)=\frac{m^2}{2}-\frac{7m^4}{12}+\frac{3m^6}{10}+O(m^8).
}
\tag{C286.9}
\]

So the current proof's exponential separation degenerates on the scale `n m^2`. But (C286.5) shows that returning the elementary mechanism to the uniform one requires `n m^2 -> 0`. The existing entropy-gap argument therefore loses its growing margin **exactly in the window needed for the deformation**.

This does not prove that a new triangular-array extension is impossible. It identifies the precise step that must be replaced. The strongest concrete next question coming from Method #6 is:

\[
\boxed{
\text{Can the JSS non-uniform remainder estimate be reproved for }m_n=c/n
\text{ without using an }\exp(\Theta(n\Delta(m_n)))\text{ entropy gap?}
}
\]

If yes, C286.4 closes the uniform source target.

I do **not** claim C286's high-temperature cycle expansion is publication-novel; it is closely related to standard Ising/high-temperature expansions. Its value here is the exact connection to the row/column-gauge invariant singularity event and the resulting triangular-array reduction.

## 4. Method #8 — discretize affine excess into hypercube circuits

Run31's affine variable can be made completely finite/combinatorial. Put `d=n-1`. For an invertible sign matrix `R` with rows `r_1,...,r_d`, let

\[
w_R=R^{-1}{\bf1},\qquad
C_R=\{x\in\{\pm1\}^d:\langle x,w_R\rangle=1\},\qquad
M_R=|C_R|.
\]

Homogenize a cube vertex by

\[
\widehat x=(x,1)\in\mathbb R^{d+1}.
\]

Because the rows of `R` are linearly independent, the `d` homogenized row vectors `\widehat r_i` are linearly independent as well. If `x in C_R` is not already a row, then `\widehat x` lies in their span. Therefore `\{\widehat r_1,...,\widehat r_d,\widehat x\}` has a **unique fundamental affine circuit** containing `x`.

Let `mathfrak C_d` denote the affine circuits of the sign cube. For a circuit `C` and a distinguished `x in C`, define

\[
N_d^\circ(C,x)
:=
\#\left\{R:\begin{array}{l}
R\text{ is an invertible sign matrix},\\
w_R\notin\{\pm e_j\},\\
C\setminus\{x\}\subseteq\operatorname{Row}(R),\\
x\notin\operatorname{Row}(R)
\end{array}\right\}.
\]

The condition `w_R notin {+/- e_j}` deletes the exact distinguished-column collision charts.

### R03-C287 — exact circuit-completion identity

**STATUS: PROVED.**

\[
\boxed{
\sum_{\substack{R\text{ invertible}\\w_R\notin\{\pm e_j\}}}(M_R-d)
=
\sum_{C\in\mathfrak C_d}\sum_{x\in C}N_d^\circ(C,x).
}
\tag{C287.1}
\]

**Proof.** A pair `(R,x)` on the left, with `x` an extra section vertex, determines its unique fundamental circuit inside `Row(R) union {x}`. Conversely, if a cube circuit `C` and distinguished point `x` satisfy `C\{x} subset Row(R)`, then minimal affine dependence gives `x in aff(C\{x}) subset aff(Row(R))=C_R`; excluding `x` from the row set makes it an extra vertex. The two maps are inverse. QED.

The sign cube has no three distinct collinear vertices, so every affine circuit has size at least four. If `|C|=s`, then a crude but exact combinatorial completion bound is

\[
N_d^\circ(C,x)
\le
(d)_{s-1}\,2^{d(d-s+1)}.
\tag{C287.2}
\]

Indeed, place the `s-1` prescribed circuit vertices into ordered row positions in `(d)_{s-1}` ways, then ignore all independence/nontriviality restrictions and fill the remaining `d-s+1` rows arbitrarily.

If `I_d` is the number of invertible sign matrices, then

\[
E_d^\circ
:=
\mathbb E_R[(M_R-d)1_{\{w_R\notin\pm e_j\}}]
\]

obeys

\[
\boxed{
E_d^\circ
\le
\frac1{I_d}
\sum_{s=4}^{d+1}
 s\,|\mathfrak C_{d,s}|\,(d)_{s-1}\,2^{d(d-s+1)}.
}
\tag{C287.3}
\]

Since `I_d=2^{d^2}(1-o(1))`, a sufficient circuit-count condition for the source conjecture is

\[
\sum_{s=4}^{d+1}
 s\,|\mathfrak C_{d,s}|\,(d)_{s-1}\,2^{-d(s-1)}
=o(d^2),
\]

with the obvious improvement obtained by replacing the crude completion bound by the exact nontrivial completion counts `N_d^circ`.

This does not solve the problem; it changes the discrete object. The old bounded-support / strong-rank arguments control small circuit sizes, while the unsolved mass lives in circuits whose size grows with `d`. That is precisely the gluing obstruction.

The current computational geometry literature now reaches farther than the older R03 searches: Aichholzer--Aurenhammer enumerated cube-spanned hyperplanes through dimension eight, and Rambau `arXiv:2607.05967v2` (2026) develops symmetry-aware circuit/cocircuit enumeration and reports new hypercube circuit/cocircuit counts. But these are finite-dimensional enumerations. They do not provide the weighted asymptotic completion estimate in (C287.3), especially for circuits of size `Theta(d)`.

So the circuit route is an exact discretization and a possible finite-testing language, not a claimed asymptotic solution.

## 5. Method #26 — hunt a sporadic high-section family, then charge its orbit complexity

A natural hope after C285 would be a deterministic statement saying that every nontrivial/dense hyperplane has a small cube section. That is false in a strong way, even for full-support normals with two macroscopic coefficient levels.

Fix an even integer `K>=2`. Let `d=2m` with `m` odd and sufficiently large, and define

\[
w^{(K)}=(\underbrace{1,\ldots,1}_{m},\underbrace{K,\ldots,K}_{m}).
\]

Consider

\[
C^{(K)}_d
=
\left\{(x,y)\in\{\pm1\}^m\times\{\pm1\}^m:
\sum_i x_i+K\sum_j y_j=1\right\}.
\]

### R03-C288(a): a nontrivial full-support hyperplane can contain `Theta(2^d/sqrt d)` cube vertices and an invertible sign basis

**STATUS: PROVED.** For fixed even `K`,

\[
\boxed{|C^{(K)}_d|=\Theta_K(2^d/\sqrt d).}
\tag{C288.1}
\]

For the upper bound, apply the classical Littlewood--Offord point-mass bound to the `d` nonzero coefficients. For the lower bound, write `X=sum x_i`, `Y=sum y_j`. For `Theta(sqrt m)` admissible odd values of `Y` in a central window of width `c_K sqrt m`, the required value `X=1-KY` is also in a fixed central `O(sqrt m)` window. Stirling's formula gives each of the two corresponding sign-sum fibers size `Theta_K(2^m/sqrt m)`, so summing over `Theta_K(sqrt m)` values of `Y` gives `Theta_K(4^m/sqrt m)`.

Moreover `C_d^(K)` affinely spans its defining hyperplane. Choose a base point with `Y=1`, `X=1-K`. Swapping a `+` and `-` sign inside the first block spans the `(m-1)`-dimensional zero-sum tangent space of that block, and the analogous swaps span the second block's zero-sum tangent space. A further move flipping `K` first-block negatives to positives and one second-block positive to negative changes `(X,Y)` by `(2K,-2)` and therefore preserves `X+KY`; it supplies the missing tangent direction. Hence there are `d` affinely independent cube vertices in the section. Because every section point satisfies `w^(K) dot x=1`, affine independence of those `d` vertices implies linear independence. Taking them as rows gives an invertible sign matrix `R` satisfying

\[
Rw^{(K)}={\bf1},
\qquad\text{so}\qquad
w_R=w^{(K)}.
\]

Since `w^(K)` has full support and is not a signed coordinate vector, this is not a distinguished-column collision chart.

This is an infinite explicit obstruction to any pointwise claim of the form “nontrivial `R` forces `M_R` to be polynomial.” In fact `M_R` can still be of Littlewood--Offord order `2^d/sqrt d`.

The normalized bordered normal has two macroscopic coefficient levels. For any fixed `delta<1/2` and sufficiently small fixed `rho`, taking `K` large enough also puts this family outside a `Cons(delta,rho)`-type near-constant class. Thus merely deleting the most obvious almost-constant normals does not create a useful deterministic pointwise section bound.

### R03-C288(b): the whole fixed two-level orbit is nevertheless negligible after basis weighting

The sporadic family is large pointwise but simple combinatorially. Up to coordinate permutations and sign symmetries, a fixed `K` produces only `exp(O(d))` such hyperplanes. Each has

\[
M\le C_K2^d/\sqrt d.
\]

The number of ordered sign bases it can contain is at most `M^d`, and each basis contributes at most another factor `M` to affine excess. Since the total number of invertible sign matrices is `I_d=2^{d^2}(1-o(1))`, the entire fixed-`K` symmetry orbit contributes at most

\[
\boxed{
\exp(O_K(d))\frac{M^{d+1}}{2^{d^2}}
=
\exp\left(-\frac12d\log d+O_K(d)\right)
}
\tag{C288.2}
\]

to the mean excess.

So this family is a concrete example of the distinction the proof must exploit:

- **pointwise concentration can be enormous;**
- **a low-complexity orbit carrying that concentration is still harmless after `d` basis rows have to land in it.**

The real danger is not one Hadamard-like or two-level hyperplane. It is an entropy-versus-section-size question: are there sufficiently many inequivalent high-section hyperplanes, with sufficiently many basis completions, to survive the `d`-fold basis penalty?

That is exactly the weighted counting problem already implicit in Voigt--Ziegler and made explicit in C287.

## 6. What moved mathematically, and what did not

The fixed numerical metric **did not move**, so this run is not reported as quantitative progress on the frozen envelope. The unchanged streak is now `2`, not reset.

The route map did move in three substantive ways:

1. **Prior-art correction:** the affine-hyperplane equivalence is known from Voigt--Ziegler 2006; C285 is a collision-deleted normalization/refinement, not a conceptually new equivalence.
2. **New deformation identity:** full row/column gauge averaging converts a sign bias into an Eulerian-cycle Fourier perturbation. The exact one-sided transfer (C286.4) shows that a triangular sharp theorem at bias `m=c/n` would solve the uniform case, while the JSS entropy gap degenerates as `Delta(m)~m^2/2` and therefore does not currently reach that window.
3. **Exact discrete target:** C287 rewrites mean affine excess as weighted fundamental-circuit completions. C288 shows why pointwise Littlewood--Offord bounds are the wrong endpoint and why orbit complexity is the quantity that must pay for high concentration.

The strongest next attack is therefore **not** another bounded-support plane catalog. It is one of the following two genuinely source-level routes:

- audit/replace the JSS entropy-gap step so their sharp non-uniform theorem becomes uniform for the triangular bias `m_n=c/n`, then invoke C286.4; or
- prove an entropy-versus-basis-completion inequality for cube hyperplanes/circuits strong enough to make the nontrivial weighted sum in C287 `o(d^2 I_d)`.

The first route now has a very explicit bottleneck (`Delta(m)~m^2/2`); the second has an exact finite combinatorial object (`N_d^circ(C,x)`).

## 7. Neighboring-track audit obligation

The newest neighboring R04 state remains `runs/R04/20260917T0310Z_i0027_retirement_handoff.md`, its six-unchanged-run retirement/handoff. It contains no new theorem package requiring another R03 audit. Earlier R03 audits of its C8/C11 chain remain preserved. I did not manufacture a duplicate audit.

## 8. Runtime/model-control status

The requested model line remains prompt-only. The exposed task-control interface provides prompt/title, schedule/timing, enablement controls, but **no model-family field, no reasoning-effort field, and no authenticated runtime telemetry**. Hence this report honestly states GPT-5.6 Sol / UNVERIFIED and does not claim GPT-6 maximum.

The repository policy also records earlier `You cannot modify this task` responses for P26/P01/P03 in one authorization context and later successful modification of P26 from a different authorized context. The legitimate workaround is an owning/admin-authorized product context that actually exposes the required model controls, or platform support. There is no repository-side bypass, and this run made no scheduler or permission change.

## 9. Exact status and ledger delta

```yaml
ledger_delta:
  track: R03
  target: sharp iid Rademacher singularity asymptotic
  status: PARTIAL
  source_status: OPEN
  fixed_metric:
    definition: "r(n)=2^n P(det B_n=0, T_n^c), full certified n-range retained"
    before:
      r10: "222.6104736743168493957921796888577... exact"
      r11_upper: "523.9022787113135428552389980..."
    after:
      r10: "222.6104736743168493957921796888577... exact"
      r11_upper: "523.9022787113135428552389980..."
    movement: false
  unchanged_count:
    before: 1
    after: 2
  methods: [6, 8, 26]
  new_claims:
    - "C286: gauge-averaged bias likelihood / Eulerian cycle-space expansion / exact one-sided transfer / subcritical L2 limit"
    - "C287: exact fundamental-circuit completion identity for collision-deleted affine excess"
    - "C288: full-support two-level high-section family; pointwise huge but fixed-orbit basis-weight negligible"
  prior_art_correction:
    claim: "C285 conceptual hyperplane-excess equivalence"
    corrected_to: "Voigt-Ziegler 2006 prior art; C285 retained only as exact collision-deleted sign-gauge refinement"
  remaining_obligation: "Either triangular JSS at m_n=c/n without entropy-gap collapse, or weighted circuit/hyperplane completion sum o(d^2 I_d)"
  next_if_unchanged: "One more unchanged run triggers the mandatory Section-I stuck protocol; do not add another local lemma."
```

No email, Drive, public posting, purchase, permission change, workflow execution, shared-root edit, peer-file edit, or scheduler modification was made.
