# Paper 19 — The Extremal Hard Edge: master plan

**Working title.** *The extremal hard edge: minimal least singular values of random
submatrices, with universality, large deviations, and phase-retrieval stability.*

**Author.** Yitzchak Shmalo.

**Source paper being generalized.**
"Extreme least singular values of Gaussian row submatrices and a phase retrieval
stability problem" (ACHA). Main result: for $A_m\in\mathbb F^{N_m\times m}$ iid standard
Gaussian, $N_m/m\to\gamma>1$, $\mathbb F\in\{\mathbb R,\mathbb C\}$, $d_\mathbb F=\dim_\mathbb R\mathbb F$,
$$ M_m^\mathbb F=\min_{|T|=m}\sigma_{\min}(A_{m,T}),\qquad \tfrac1m\log M_m^\mathbb F\xrightarrow{P}-\tfrac{h(\gamma)}{d_\mathbb F},\quad h(\gamma)=\gamma\log\gamma-(\gamma-1)\log(\gamma-1).$$
Application: real phase retrieval at $N=2m-1$ has Balan--Wang base $\omega=4^{-m+o_\mathbb P(m)}$.

## The one idea
The base is `entropy / small-ball-exponent`:
$$\boxed{\ \tfrac1m\log M_m \to -H/a\ }$$
where $H=\lim\tfrac1m\log(\#\text{submatrices})=h(\gamma)$ and $a=$ exponent in
$\mathbb P\{\sigma_{\min}\le t\}\asymp t^a$ (here $a=d_\mathbb F$).
**Every generalization changes $H$ or $a$ (or the pair-correlation control).** That is the
backbone. Proof template: union bound (lower) + second moment over random hyperplanes (upper).

## Architecture (parts → target theorems)

### Part I. The abstract extremal small-ball principle  [TIER 1, must be airtight]
Family $\{Y_T\}_{T\in\mathcal T_m}$, nonnegative. Hypotheses:
- (E) entropy: $\tfrac1m\log|\mathcal T_m|\to H\in(0,\infty)$.
- (SB+) uniform upper small-ball: $\mathbb P\{Y_T\le t\}\le C m^{B}t^{a}$, $0<t\le1$.
- (SB-) lower small-ball: $\mathbb P\{Y_T\le t\}\ge c\,t^{a}$ (poly slack ok).
- (PC) pair correlation: $Z_t=\sum_T\mathbf 1\{Y_T\le t\}$ has $\mathrm{Var}\,Z_t/(\mathbb E Z_t)^2\to0$ along $t=e^{-sm}$, each $s<H/a$.
**Theorem A.** Then $\tfrac1m\log\min_T Y_T\xrightarrow{P}-H/a$, with quantitative rates
(lower: union $\le|\mathcal T_m|Cm^Bt^a$; upper: Chebyshev on $Z_t$).
The same union-bound half has a finite-budget form with no limiting entropy:
if $\sup_T\mathbb P\{Y_T\le t\}\le C_m t^{a_m}$, then
\[
\mathbb P\left\{\min_TY_T\le
\exp[-(\log|\mathcal T_m|+\log C_m+u_m)/a_m]\right\}\le e^{-u_m}.
\]
The lower union bound also gives almost-sure lower envelopes whenever the
bad-event probabilities are summable; in the finite-budget form, deterministic
budgets with $\sum_m e^{-u_m}<\infty$ give the displayed finite threshold
eventually almost surely.  The polynomial/exponential small-ball applications
below have this property after an $\varepsilon$-slack.
The finite-budget union bound has a nonuniform version as well: per-index
constants \(C_{m,T}\) may be summed directly, replacing
\(|\mathcal T_m|\sup_T C_{m,T}\) by a weighted budget \(B_m\).
When those weighted budgets are deterministic, the same summable
\(e^{-u_m}\) Borel--Cantelli upgrade gives the weighted finite threshold
eventually almost surely; no independence across dimensions or inside the
tested family is used.
For square row submatrices this gives a clean row-wise heterogeneous-density
budget: if row \(i\) has scalar density bound \(K_{m,i}\), replace
\(\log\binom{N_m}{m}+\log K_m\) by
\(\log\binom{N_m-1}{m-1}+\log\sum_iK_{m,i}\), with the polynomial hard-edge
factor retained.
The original paper = instance $Y_T=\sigma_{\min}(A_T)$, $a=d_\mathbb F$, $H=h(\gamma)$.
Frame honestly as an *organizing principle* (first/second moment method); the real work is (PC).

### Part II. Universality  [flagship — TIER 1 lower, TIER 2 upper]
$A_m$ iid entries, mean 0, var 1 (complex: proper/circular).
- **II.A Lower bound, universal under an explicit tail.** Uses a one-matrix least-singular-value
  tail with no residual term surviving the union over $\exp(h(\gamma)m)$ submatrices.  The safe
  theorem assumes
  $\mathbb P\{\sigma_{\min}(G)\le e^{-sm}\}\le \exp(-(as+o(1))m)$, or a polynomial bound
  $Cm^B t^a$ with no additive exponential error.  For bounded-density iid entries over
  $\mathbb R$ or $\mathbb C$, the distance-to-hyperplane argument gives
  $a=d_\mathbb F$ and the lower side; the real case is Shmalo's Proposition 6.1 and
  the complex case is the same codimension-two calculation.  If the scalar density
  bound is $K_m=\exp((\kappa+o(1))m)$, the lower threshold shifts to
  $(h(\gamma)+\kappa)/d_\mathbb F$; in particular $K_m=e^{o(m)}$ preserves the Gaussian
  lower-side base.  These lower sides also hold as almost-sure lower envelopes on
  any common coupling, and the finite-entropy version has the full finite-budget
  eventual a.s. form when $\sum_m e^{-u_m}<\infty$. EASY/SOLID.
  Row-dependent Gaussian smoothing \(F_m+D_mG_m\) has the corresponding
  weighted budget
  \(\log\binom{N_m-1}{m-1}+\log\sum_i\sigma_{m,i}^{-d_\mathbb F}\);
  the lower-side shift is
  \((d_\mathbb F m)^{-1}\log\sum_i\sigma_{m,i}^{-d_\mathbb F}\).
  Entrywise density profiles are covered by the same row-distance argument
  after replacing each row by \(K_{m,i}^*=\max_j K_{m,i,j}\); averages over
  columns would need new normal-delocalization input and are not claimed.
  The finite entrywise budget has the same summable a.s. upgrade.
  More generally, independent rows need not have independent coordinates:
  affine directional anti-concentration
  \(\mathbb P\{|\langle R_i,u\rangle-z|\le r\}\le L_i r^{d_\mathbb F}\)
  gives the square finite budget
  \(\log\binom{N_m-1}{m-1}+\log\sum_i L_i+(d_\mathbb F/2)\log m\).
  Real iid isotropic log-concave rows therefore have the lower-side base
  \(h(\gamma)\), but their exact law still needs pair-correlation input.
- **II.B Upper bound, continuous case.** Entries sub-Gaussian + bounded density $\le K$.
  Second moment. Crux = pair bound $q_D(t)\le(1+o(1))p(t)^2(1+C/D)$ WITHOUT Gaussianity:
  1. Normals $u_I$ to $m-1$ iid rows are *incompressible* ($\|u_I\|_\infty\le m^{-c}$) with prob
     $1-e^{-cm}$, uniformly over $I$ (universal invertibility of the $(m-1)$-row system).
  2. On incompressible normals, 2-dim local-CLT / Berry–Esseen density bound gives the sharp
     factorization for the bulk (small overlap,
     $\varrho_{I,J}=\langle u_I,u_J\rangle=O(D(I,J)^{-1/2})$).
  3. $D=2$ term and rare compressible normals negligible (combinatorics + $e^{-cm}$).
  ⇒ same base $h(\gamma)/d_\mathbb F$. HARD but standard circle of ideas; split lemmas to agents,
  adversarially verify. Be explicit about the density/moment hypotheses.
- **II.C Atomic/discrete obstruction.** Do **not** use $\log(1/p^\*)$ as a theorem-level
  singularity exponent without a cited singularity theorem.  Safe content:
    - first-moment obstruction: for Rademacher entries at $N=2m-1$, the expected number of
      singular square row submatrices is exponential;
    - finite alphabet theorem: for
      \(\Pi(\mathcal A)=\{[a:b]\in\mathbb P^1(\mathbb K):a,b\in\mathcal A,
      (a,b)\ne(0,0)\}\), every \(\mathcal A^{N\times m}\) matrix over
      \(\R\) or \(\C\) with \(m\ge2\) and
      \(N\ge|\Pi(\mathcal A)|(m-1)+1\) (with the all-zero alphabet handled by
      \(N\ge m\)) has a singular \(m\)-row minor by the two-column
      projective-pair pigeonhole argument;
    - stronger sign-frame theorem: every $\{\pm1\}^{N\times m}$ matrix with $m\ge2$ and
      $N\ge2m-1$ has a singular $m$-row submatrix, by the two-column agree/disagree
      pigeonhole argument; this is the \(|\Pi(\{\pm1\})|=2\) alphabet case;
    - no high-probability exact singularity conclusion follows without a second-moment or
      dependence theorem for singular minors in general atomic laws.
  Qualitatively different from Gaussian; critical sign-frame failure is PROVEN, general
  atomic thresholds remain PARTIAL/CONJECTURAL.
- **II.D Random row count and Poissonization.**  For Gaussian row arrays, randomizing the
  number of available rows does not change the exponential base as long as
  \(N_m/m\to\gamma>1\) in probability.  This is a pathwise monotone squeeze between
  deterministic row counts and does not require independence of \(N_m\) from the row array.
  Bounded-density lower sides transfer by the same upper bracket.  Poisson, binomial, and
  independent Bernoulli thinning are included; value-dependent thinning is not.

### Part III. Geometric generalizations  [TIER 1–2, clean second moment]
- **III.A Rectangular submatrices** $\ell\times m$, $\ell\ge m$: fixed excess has an
  exponential lower-side base; proportional excess has no negative exponential scale under
  subexponential density growth, while the finer $\sqrt m$ edge is a separate Wishart-LDP
  problem.  The fixed-excess and proportional-excess lower envelopes are almost sure
  because their failure probabilities are summable.  Fixed-excess finite budgets now also
  allow row-wise and entrywise deterministic heterogeneous density bounds, with the
  entrywise budget summing over the bad column and the Cauchy--Binet row block;
  summable finite-budget failures give eventual a.s. lower bounds.  Independent
  rows with one-dimensional directional anti-concentration have a fixed-excess
  lower side as well, using an \(m-1\)-row cofactor certificate and an exact
  elementary-symmetric row budget.  Moving-excess finite budgets keep the exact
  unit-ball volume, coordinate-minor, and row-set factors rather than hiding
  them in fixed-excess constants.  The proportional-excess lower side also
  transfers to possibly dependent random prefix row counts by the same
  upper-bracket monotonicity argument, with a doubled exponential threshold for
  the selected-row normalized column-Gram statistic.  Positive realized-prefix
  row weights and one global all-column right factor with subexponential
  absolute singular scale preserve these random-prefix proportional-excess
  lower sides by a pathwise sandwich; this remains distinct from the open
  \(\sqrt m\) Wishart-edge/LDP law.
- **III.B $k$-th smallest singular value** $\min_{|T|=m}\sigma_{m-k+1}(A_T)$:
  the Gaussian lower side is now proved by a finite-\(m\), polynomial-loss
  Laguerre--Selberg tail with exponent \(e_k=d_\mathbb F k^2\).  The normalized
  fixed-excess version
  \(M_m^{(r)}[k]=\min_{|T|=m+r}\sigma_{m-k+1}(A_T)\) has the proved Gaussian
  lower-side exponent \(d_\mathbb F k(k+r)\), finite row-family budget
  \((\log\binom{N_m}{m+r}+O_{\mathbb F,r,k}(\log m))/(d_\mathbb F k(k+r))\),
  and fixed-aspect lower base \(h(\gamma)/(d_\mathbb F k(k+r))\).  The normalized
  Gram eigenvalue statistics inherit doubled lower bases by pathwise squaring:
  \(\min_{|T|=m}\lambda_{(k)}(m^{-1}A_T^*A_T)\) has lower base
  \(2h(\gamma)/(d_\mathbb F k^2)\), while
  \(\min_{|T|=m+r}\lambda_{(k)}((m+r)^{-1}A_T^*A_T)\) has lower base
  \(2h(\gamma)/(d_\mathbb F k(k+r))\), with the same summable/a.s. lower
  envelopes.  The exact extremal law still needs a codimension-\(k\)
  pair-correlation/second-moment theorem.
- **III.C Both-sided submatrices** $\min_{|R|=|C|=k}\sigma_{\min}(A_{R,C})$:
  entropy adds, $H=h(\gamma_R)+h(\gamma_C)$.  The union-bound lower side is
  proved for Gaussian and density-rate bounded-density entries, and has an almost-sure
  lower-envelope version.  The finite-entropy moving-aspect form keeps
  \(\log\binom{N_k}{k}+\log\binom{n_k}{k}\) exactly and upgrades to an eventual
  a.s. finite-budget lower bound when the chosen \(u_k\)-budget is summable.
  A conservative heterogeneous-density refinement follows from the nonuniform
  union budget by summing the row/column-set constants
  \(K_{k,i,C}=\max_{j\in C}K_{k,i,j}\); it is lower-side only and does not add a
  new exact-base claim.  Its deterministic finite-budget form also has the
  summable a.s. upgrade.  The random-prefix two-sided density-rate lower side,
  its diagonal transfer, and Gaussian full-prefix normalization also pass to the
  selected-minor normalized Gram/sample-covariance statistic by deterministic
  squaring, with doubled lower-side constants and the same a.s. lower envelopes.
  The exact base is conditional on a two-overlap pair-correlation theorem.
- **III.D Aspect $\gamma\downarrow1$ and $\gamma\to\infty$ asymptotics** of the entropy
  base are proved as deterministic calculus: \(h(1+\delta)=\delta\log(1/\delta)+\delta+O(\delta^2)\),
  \(h(\gamma)=\log\gamma+1-\frac1{2\gamma}+O(\gamma^{-2})\).  These calibrate fixed
  aspect ratios only.  Moving-aspect lower sides have finite-entropy union-bound
  forms for square, fixed-excess, and two-sided submatrices; matching exact
  moving-aspect laws still need uniform small-ball and pair-correlation input.

### Part IV. Large deviations  [TIER 1 upper tail, TIER 3 lower tail]
- **IV.A Upper tail (min atypically small).** For $s>h/d$, the proved bound is
  $d s-h\le I_-(s)\le d s$.  The exact rate $I_-(s)=d s-h$ is a conjecture;
  Bonferroni is obstructed by highly overlapping row sets.
- **IV.B Lower tail (min atypically large).** $s<h/d$: $\mathbb P\{M_m>e^{-sm}\}$ — all submatrices avoid
  being small; genuine LDP with dependence. Partial bounds + conjecture.

### Part V. Other random ensembles (in-area; NO Toeplitz/structured-symbol matrices)  [TIER 2–3]
> SCOPE NOTE (user, 2026-06-27): stay in the area of the source paper — extreme least singular
> values of random row submatrices + phase-retrieval stability. "Other random matrices" means
> other ENTRY LAWS and ENSEMBLES, NOT Toeplitz/Hankel/circulant/structured-symbol matrices.
> Do not work on Toeplitz anything.
- **V.A Division algebras** $\mathbb F\in\{\mathbb R,\mathbb C,\mathbb H\}$, $d_\mathbb F\in\{1,2,4\}$: the square iid
  quaternion Gaussian base is theorem-quality:
  \(m^{-1}\log M_m\to-h(\gamma)/4\), by exact \(\Sp(m)\)-invariance,
  quaternion Gaussian small-ball exponent \(4\), and the Haar-normal overlap
  moment.  Positive real diagonal row/column weights with subexponential
  logarithmic extrema, including row-normalized and full-matrix column-normalized
  quaternion Gaussian matrices, preserve this exact square-row convergence in
  probability; the normalized square Gram base is \(-h(\gamma)/2\).  The same
  square law is unchanged by random prefix row counts \(N_m/m\to\gamma\), with
  Poisson/binomial and independent-thinning examples but no value-dependent
  selection.  Across \(\R,\C,\HH\), the square random-prefix exact law also
  survives positive real prefix row weights and one global all-column right
  factor \(S_m\in GL_m(\F)\) when the realized-prefix row-weight extrema and the
  absolute singular-value scale of \(S_m\) are subexponential; positive column
  diagonals, row-normalized random-prefix Gaussian rows, and full-prefix column
  normalization are included.  The same deterministic-count square all-column law survives global
  right quaternion conditioning factors \(S_m\in GL_m(\HH)\) whose absolute
  singular-value scale is subexponential; condition number alone is not enough.  Only lower envelopes
  transfer almost surely unless an a.s. upper source is proved.  The beta-4
  Laguerre--Selberg tail also gives fixed-excess fixed-\(k\) quaternion lower
  sides with base \(h(\gamma)/(4k(k+r))\), and normalized column-Gram lower sides
  with doubled base \(h(\gamma)/(2k(k+r))\).  Positive real diagonal row/column
  weights with subexponential extrema inherit these fixed-excess lower sides and
  their a.s. lower envelopes, but not fixed-excess exact laws.  More generally,
  random prefix row counts preserve the real/complex/quaternion fixed-excess
  fixed-\(k\) lower sides and normalized column-Gram lower sides by the upper
  deterministic-bracket monotonicity argument; these random-prefix lower sides
  also survive positive real diagonal row/column weights with subexponential
  realized-prefix logarithmic extrema, including row-normalized random-prefix
  Gaussian rows and full-prefix column normalization.  More generally, the same
  lower-side transfer allows one global all-column right factor
  \(S_m\in\F^{m\times m}\) when its absolute smallest and largest singular
  scales are subexponential; condition number alone is not enough.  This is
  weaker than the exact square random-prefix laws when \(r=0,k=1\).
  This is separate from the spherical-radial transfer cleanup; fixed-excess
  quaternion upper/exact laws and beta/division-algebra interpolation remain
  open.
- **V.B Deterministic conditioning / product variance profiles.**  For
  $A=D_mG\Sigma_m^{1/2}$ with positive deterministic row weights and column covariance
  whose extreme singular factors are only $e^{o(m)}$, the extremal log scale is unchanged.
  This proves the uniformly elliptic common-covariance case and bounded product variance
  profiles.  The same min--max sandwich transfers fixed-excess fixed-\(k\)
  row-submatrix statistics and their normalized column-Gram versions, preserving only the
  inherited lower-side status; on common couplings, a.s. \(o(m)\) absolute conditioning
  factors also transfer the inherited almost-sure lower envelopes.  The same pathwise diagonal sandwich covers positive random row weights, even
  when dependent on the matrix, provided their global extrema are $e^{o_\PP(m)}$; in
  particular row-normalized Gaussian frames inherit the Gaussian base.  The fixed-excess
  fixed-\(k\) and normalized column-Gram lower sides obey the same random diagonal
  row/column-weight transfer, with doubled log error for Gram variables; this
  diagonal transfer composes with random prefix counts, still only on the lower
  side.  Row- and column-normalized Gaussian matrices inherit these lower sides
  and their a.s. lower envelopes.  The same transfer
  proves spherical-direction ensembles \(A_m=D_m^{\rm rad}\Theta_m\): if
  \(m^{-1}\log b_m\to\alpha\) and
  \(\max_i|\log(r_{im}/b_m)|=o_\PP(m)\), then the base shifts by \(\alpha\) and is otherwise
  unchanged.  With almost-sure \(o(m)\) radial extrema, the same sandwich gives an
  almost-sure lower envelope.  The right-diagonal analogue covers positive random column
  weights and column-normalized Gaussian matrices, and applies to two-sided minors only for
  diagonal column factors; non-diagonal covariance still fails to commute with column
  selection, even though square row-only all-column right factors are covered separately.
  Arbitrary variance profiles remain a variational problem.
- **V.C Gram / sample-covariance submatrices.** Passing from a selected matrix
  \(B_T\) to \(q^{-1}B_T^*B_T\) is pathwise:
  \(\lambda_{\min}(q^{-1}B_T^*B_T)=q^{-1}\smin(B_T)^2\).  Thus every proved
  singular-value log-scale result transfers to Gram/sample-covariance minima
  with doubled logarithmic constants and unchanged proof status.  Square
  Gaussian row submatrices give bases \(2h(\gamma)/d_\F\) for \(\R,\C\), and
  the quaternion Gaussian square base gives \(h(\gamma)/2\); the fixed-excess
  fixed-\(k\) quaternion column-Gram lower sides have base
  \(h(\gamma)/(2k(k+r))\).  Random-prefix two-sided selected \(k\times k\)
  minors inherit the doubled threshold
  \(2(h(\gamma_R)+h(\gamma_C)+\kappa)/d_\F\) under the same diagonal-transfer
  hypotheses, and the Gaussian full-prefix-normalized case has \(\kappa=0\).
  The same one-sided
  covariance transfer applies to \(D_mG_m\Sigma_m^{1/2}\) only when the absolute
  extreme eigenvalues of \(\Sigma_m\) are subexponential on the \(m\)-scale; a
  small condition number alone does not prevent an exponential scalar shift.
  Fixed-excess exact covariance laws are only as strong as
  Conjecture~\ref{rect:exact}.  This does not solve the proportional-excess
  Wishart edge/LDP problem.
- **V.D Isotropic / log-concave / sub-Gaussian rows** (rows are random vectors, entries not iid):
  affine directional anti-concentration gives the square lower side for
  independent rows, and the cofactor row-block argument gives the fixed-excess
  lower side for the same one-dimensional hypothesis.  This includes real iid
  isotropic log-concave rows for every fixed excess.  Matching exact laws remain
  conditional on a row-distribution pair-correlation theorem.
- **V.E Heavy-tailed entries.** Bounded scalar density, without moment assumptions, gives the
  lower side with exponent $a=d_\mathbb F$.  Density bounds that grow like
  $\exp((\kappa+o(1))m)$ shift the lower-side threshold by $\kappa/d_\mathbb F$.  This also
  gives a smoothed deterministic-frame lower side for $F_m+\sigma_mG_m$, with shift
  $\limsup m^{-1}\log\sigma_m^{-1}$.  The same density-rate bookkeeping now covers
  fixed-excess, random-prefix proportional-excess lower sides, their pathwise
  conditioning transfers, two-sided minors, random-prefix two-sided lower
  sides, random-prefix two-sided diagonal row/column transfers, Gaussian
  full-prefix normalizations of those two-sided prefixes, and the corresponding
  selected-minor normalized Gram lower-side transfers.  The matching upper
  law remains conditional on pair-correlation input and typical normalization.

### Part VI. Phase retrieval, generalized  [TIER 1 continuous, TIER 3 complex]
- **VI.A** Conditional universality ⇒ Balan–Wang base $1/4$ for continuous bounded-density
  frames once the pair-correlation theorem is proved.  The lower side is already proved
  and strengthens to an almost-sure lower envelope; exact Balan--Wang bases remain
  in probability/conditional unless summable upper-side estimates are proved.  Positive
  diagonal coordinate preconditioning with subexponential logarithmic extrema preserves
  the Gaussian critical base; column normalization is included but is not measurement-vector
  normalization.  Random square-row-submatrix counts are RMT statements, not critical
  Balan--Wang corollaries unless the count equals \(2m-1\) with high probability; for
  \(r>0\), fixed-excess tall submatrices are only one branch of the supercritical partition
  minimum.  The directional fixed-excess lower side gives this deficient-complement branch
  the lower base \(\log4/(r+1)\) under subexponential elementary-symmetric directional
  budgets, but it is not a full supercritical Balan--Wang theorem.
- **VI.B** Discrete frames: finite alphabets have deterministic projective-pair
  full-spark obstructions, and critical real sign frames fail injectivity
  deterministically.  General discrete laws require separate singular-minor
  analysis below the deterministic row counts.
- **VI.C** Complex PR threshold $4m-4$ and the complex Balan–Wang base — careful/honest, mostly
  conjecture + the clean RMT quantity $M_m^\mathbb C$. The paper itself flags this is NOT the
  complex-PR threshold; respect that.

### Part VII. Open problems  [the second deliverable]
Genuine open problems related to Shmalo's work:
1. Poisson/Gumbel extreme process of Gaussian minors.  The first-moment
   intensity and one-sided bound at the exact centering are recorded; the full
   process, critical overlap clusters, and exact centering refinements remain
   open.
2. Overlap-resolved pair-correlation universality for bounded-density sub-Gaussian entries.
3. Complex phase-retrieval Balan–Wang base (conjecture + bounds).
4. Hard-edge avoidance speed / lower-tail LDP rate function (IV.B).
5. Proportional rectangular extremal edge via Wishart lower-tail LDP.
6. Sharp concentration / a.s. fluctuation scale of $\log M_m$.
7. Frame-design dependence: which continuous frame ensembles minimize/maximize the Balan--Wang
   base, especially beyond the subexponential radial-weight regime.
8. Heavy-tailed and below-threshold-discrete universality classes.
9. Division-algebra interpolation beyond the proved Gaussian square bases for
   \(d_\mathbb F=1,2,4\): whether a $\beta$-ensemble interpolation
   ($\beta>0$ real) is meaningful for the extremal edge.

## Rigor policy
- Every theorem gets: a development pass, then ≥2 adversarial verification passes that TRY TO
  BREAK it (find a counterexample, a gap, a wrong constant). Only verified content enters the
  manuscript. Mark each result PROVEN / PARTIAL / CONJECTURE explicitly in STATE.md.
- No hand-waving of constants where the exponent depends on them. Poly-in-$m$ slack is fine
  (exponential scale), but say so.
- Honest about hypotheses. Distinguish what is universal from what needs Gaussianity.

## Writing voice
Human academic. Neutral. No "headline/remarkably/notably/delve", no emoji, no bold-fests,
no meta-commentary about honesty or AI. Short boring commit messages. Standalone artifact.
