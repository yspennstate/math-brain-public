# account01/B01 — row-aggregate random-slope lemma closes the high-ridge-leverage endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T183610Z-b01-qform-auto11`  
**Assignment:** Oscillatory replacement  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`

## 1. Fresh target and correction boundary

Fresh `math-research-brain` control was read on this invocation and refreshed again immediately before publication. The active programme is still QFORM-only and the OWNER CONTROL is revision `2026-09-22.11`; no later B01 stop was present. The owner asks for the full theorem, not another status loop.

The full target remains OPEN: for every dimension, independent real coordinates with densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal finite essential bound for the density of `Q=X^T A X`, or give a target-valid counterexample. Continuity remains a separate requested conclusion.

The live corrections are retained. In particular:

* no law-uniform pointwise estimate `|E exp(itX^2)| <= C|t|^-1/2` exists for arbitrary cap-one scalar densities;
* diagonalizing the matrix destroys input-coordinate independence in general;
* a single good physical minor need not exist;
* arbitrary-joint coarea bounds and positive conditional-projection moments recorded as false are not used;
* the revision-.11 pointwise scalar-residual conditioning obligation `sup_b ||p_(Q3|Q'=b)||_infinity` is false. The exact target-valid Hadamard counterexample in account02/B01 r26 is consumed below as a correction, not as a premise for a positive theorem.

The scalar phase-alignment falsifier remains explicit: for any prescribed `s>0` and small `delta>0`, the set

`{x : dist(s x^2, 2*pi*Z) <= delta}`

has infinite Lebesgue measure. Choose a finite measurable subset of total measure one and use its indicator as a probability density. Then `Re E exp(isX^2) >= cos(delta)`. Thus the theorem below cannot come from scalar quadratic curvature. It comes from averaging a genuine random **linear slope** across an original-coordinate bank.

## 2. Exact dependencies actually used

### 2.1 Outer physical-pair quarter kernel

Account03/B19 r13, canonical source

`yspennstate/math-open-problems@0e6d1715955458010d43193cab3dafc293c0e28c`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T154500Z-account03-B19-QFORM-r13/REPORT.md`

proves the following product-preserving reduction. For a physical opposite-sign pivot pair

`B0 = [[a,c],[c,-b]],   a,b>=m>0,   Delta=ab+c^2`,

let `S` be the exact Schur complement on the remaining original coordinates and put `kappa(Z)=Z^T S Z`. Then

`p_Q(x) <= 2 Delta^(-1/4)m^(-1/4) E |x-kappa(Z)|^(-1/4)`.       (2.1)

In its live one-effective-direction branch one may take

`m=7/8`, `Delta>=49/64`,

and if no physical Schur diagonal already pays, it forces disjoint original-coordinate sets `I,J` with

`sigma := s_1(S[I,J]) > 27/2240`.                               (2.2)

### 2.2 Previous B01 quarter-Riesz ridge splice

Account01/B01 r16:09, canonical source

`yspennstate/math-open-problems@4bbd127e5bdb15f172f37b9112660b4ead3a9483`

proves that for the same outer physical pair, if `C=S[I,J]`, `gamma=sigma/sqrt(3)`, and

`K_gamma = C C^T (gamma^2 I + C C^T)^(-1)`,

then

`max_i (K_gamma)_ii <= 1/2`                                         (2.3)

already closes the branch. In the B19 numerical regime (2.2), the resulting essential-density bound is `<42.984`.

This prior result used the exact quarter-Riesz identity

`E |x-R|^(-1/4) <= c_(1/4) int_R |t|^(-3/4)|phi_R(t)| dt`,

`c_(1/4)=Gamma(3/4)sin(pi/8)/pi = 0.14927036108294766...`.       (2.4)

### 2.3 Projection-density source behind the new aggregate step

The previous B01 random-slope report

`yspennstate/math-open-problems@508b0985ba8bb658a7f6a935af5138a195cb89de`

records the bounded-density projection theorem used here: if independent coordinates have densities bounded by one, every one-dimensional linear image `c^T X` has density bounded by

`C_proj / ||c||_2`,                                                  (2.5)

where `C_proj` is one universal finite constant (the report sources this to Rudelson--Vershynin, *Small Ball Probabilities for Linear Images of High-Dimensional Distributions*, IMRN 2015, Thm. 1.1). Only universality is needed below.

### 2.4 Assigned partner account02/B01

The latest partner r26 is a decisive negative correction: its target-valid four-dimensional Hadamard example proves `sup_b ||p_(Q3|Q'=b)||_infinity=infinity`. I use that to reject the pointwise scalar-conditioning interface.

For the required positive partner application I use the immediately preceding completed account02/B01 r25 theorem, source-pinned in r26 at

`yspennstate/math-open-problems@bf4ba08b75ab774aef671c62ba4898a371059c0d`.

It proves that for an invertible physical symmetric `3 x 3` principal block `H` of a quadratic form on independent cap-one inputs, with arbitrary affine leakage and arbitrary remaining couplings,

`||p||_infinity <= 216 |det H|^(-1/3)`.                            (2.6)

Section 7 below applies (2.6) inside a new outer-quarter-kernel inequality.

## 3. New row-aggregate random-slope lemma

### Theorem 3.1 — `QFORM-RANDOM-SLOPE-ROW-AGGREGATE-v1`

Let `Z=(Z_1,...,Z_N)` have independent probability densities bounded by one and let `S` be any real symmetric matrix. Put

`kappa(Z)=Z^T S Z`.

Suppose there is one original coordinate `i` and a disjoint original-coordinate set `J` such that the physical cross row

`c=S[i,J]`

is nonzero. Set

`r=||c||_2`.

Then, for every `t!=0`,

`|phi_kappa(t)| <= min(1, sqrt(pi C_proj/(r|t|))).`                  (3.1)

No hypothesis is made on `S_ii`, on `S[J,J]`, on the rank of the full cross block, on signs, moments, compact support, or any remaining coupling.

### Proof

Condition on all original coordinates outside `{i} union J`. Write `x=Z_i`, `y=Z_J`. Under this conditioning,

`kappa = S_ii x^2 + 2x c^T y + 2 alpha x + H(y)`,                   (3.2)

where `alpha` is a deterministic number under the conditioning and `H` contains every term not involving `x`. Define

`F_t(beta)=int_R exp(it[S_ii x^2+beta x]) f_i(x) dx`.              (3.3)

The conditional characteristic function is

`E_y [ exp(it H(y)) F_t(2c^T y+2alpha) ]`.

Cauchy--Schwarz discards only the unit-modulus phase:

`|phi_(kappa|outside)(t)|^2
 <= E_y |F_t(2c^Ty+2alpha)|^2`.                                   (3.4)

By (2.5), `L=c^T Z_J` has a density bounded by `C_proj/r`. Therefore `beta=2L+2alpha` has density bounded by

`C_proj/(2r)`.                                                       (3.5)

On the other hand, as a function of `beta`, (3.3) is a Fourier transform sampled at frequency `t beta`. Plancherel gives the exact identity

`int_R |F_t(beta)|^2 d beta
 = (2*pi/|t|) int_R f_i(x)^2 dx
 <= 2*pi/|t|`,                                                       (3.6)

because `0<=f_i<=1` and `int f_i=1`. Combining (3.4)--(3.6), uniformly in the conditioned outside variables,

`|phi_(kappa|outside)(t)|^2 <= pi C_proj/(r|t|)`.

Average the conditional characteristic functions and use the triangle inequality. This proves (3.1). QED.

### Why this is different from the refuted pointwise Fresnel claim

The scalar factor `exp(it S_ii x^2)` may be arbitrarily phase-aligned by a fragmented cap-one density. It never supplies decay here. The decay comes from Plancherel in the **linear coefficient beta** and from the bounded density of the whole original-coordinate linear image `c^T Z_J`. Thus an arbitrarily diffuse row with tiny individual entries is aggregated before any reciprocal payment.

## 4. Quarter-Riesz lift of one aggregate row

### Theorem 4.1 — `QFORM-QUARTER-RIESZ-ROW-AGGREGATE-v1`

In the outer physical-pair setup (2.1), suppose the Schur form `S` contains a row aggregate as in Theorem 3.1 with norm `r>0`. Then `Q` has an essentially bounded density and

`||p_Q||_infinity
 <= 32 c_(1/4) (pi C_proj)^(1/4)
    Delta^(-1/4) m^(-1/4) r^(-1/4).`                               (4.1)

No continuity claim is made.

### Proof

From Theorem 3.1,

`|phi_kappa(t)| <= min(1,(t0/|t|)^(1/2))`,

where

`t0=pi C_proj/r`.                                                     (4.2)

The weighted integral in (2.4) is exactly

`int_R |t|^(-3/4) min(1,(t0/|t|)^(1/2)) dt`
`=2[ int_0^t0 t^(-3/4)dt
     +t0^(1/2) int_t0^infinity t^(-5/4)dt ]`
`=16 t0^(1/4).`                                                       (4.3)

Insert (4.3) into (2.4), and then into (2.1). This gives (4.1). QED.

The exponent is exactly at the useful endpoint: one aggregate random slope provides one half Fourier power, and the outer physical pair has already converted the required potential to a quarter-Riesz weight.

## 5. High ridge leverage automatically creates the row aggregate

Let `C=S[I,J]` be the forced B19 cross block, `sigma=s_1(C)>0`, and set

`gamma=sigma/sqrt(3)`,
`K_gamma=C C^T(gamma^2I+C C^T)^(-1)`.

Since, spectrally,

`0 <= C C^T(gamma^2I+C C^T)^(-1) <= gamma^(-2) C C^T`,              (5.1)

any physical row `i` with `(K_gamma)_ii>1/2` satisfies

`||C[i,*]||_2^2 > gamma^2/2 = sigma^2/6`.                           (5.2)

Hence

`r=||C[i,*]||_2 > sigma/sqrt(6)`.                                   (5.3)

This implication uses the whole row norm. It does not choose a large entry and therefore does not lose on the singleton-plus-diffuse-bank examples that defeat reciprocal-minor arguments.

## 6. The B19 forced-Schur-cross branch is now paid at both leverage endpoints

Return to the exact account03/B19 r13 one-effective-direction residue. If a physical Schur diagonal satisfies its stated threshold, B19 already gives a `<25` target-level bound.

Otherwise B19 forces a disjoint original-coordinate cross block `C=S[I,J]` satisfying

`sigma=s_1(C)>27/2240`.                                               (6.1)

Take `gamma=sigma/sqrt(3)`.

* **Diffuse ridge endpoint.** If `max_i(K_gamma)_ii<=1/2`, the previous B01 quarter-Riesz ridge splice gives

  `||p_Q||_infinity <42.984`.                                        (6.2)

* **Heavy ridge endpoint.** If `max_i(K_gamma)_ii>1/2`, (5.3) and Theorem 4.1 give

  `||p_Q||_infinity
   <= 32 c_(1/4)(pi C_proj)^(1/4) 6^(1/8)
      Delta^(-1/4)m^(-1/4)sigma^(-1/4)`.

  Using `m=7/8`, `Delta>=49/64`, and (6.1),

  `boxed( ||p_Q||_infinity <= 26.540 C_proj^(1/4) ).`                (6.3)

Thus the leverage split is exhaustive, and the high-leverage case that was explicitly left unpaid in the previous B01 run is no longer an obstruction.

**Conclusion of this splice.** Subject to the already-stated account03/B19 r13 one-effective-direction reduction, that entire residue now has a universal essential-density bound:

`||p_Q||_infinity
 <= max(25, 42.984, 26.540 C_proj^(1/4)).`                            (6.4)

This is a genuine branch closure, not the full conjecture. Other global overlap/aggregate branches in the proof assembly remain unpaid. In particular nothing here establishes that every target matrix enters this B19 one-effective-direction normal form.

Continuity is not obtained from (4.1)/(6.4); this run proves essential boundedness on the stated branch only.

## 7. Assigned partner theorem applied to a new inequality

Here is an independent concrete use of account02/B01 r25 rather than a citation-only dependency.

Suppose the Schur critical-value form `kappa=Z^T S Z` contains an invertible physical principal triple `H=S[T,T]`, and write

`d=|det H|>0`.

By account02/B01 r25,

`M_kappa:=||p_kappa||_infinity <=216 d^(-1/3)`.                       (7.1)

For any probability density `p<=M`, the one-dimensional bathtub principle gives

`sup_x int |x-y|^(-1/4)p(y)dy
 <= M int_(-1/(2M))^(1/(2M)) |u|^(-1/4)du
 = (2^(9/4)/3) M^(1/4).`                                            (7.2)

Combining (7.2) with the outer physical-pair kernel (2.1),

`||p_Q||_infinity
 <= (2^(13/4)/3) Delta^(-1/4)m^(-1/4) M_kappa^(1/4)`
`<= [ (2^(13/4)/3) 216^(1/4) ]
    Delta^(-1/4)m^(-1/4)d^(-1/12).`                                 (7.3)

The coefficient is

`boxed( (2^(13/4)/3)216^(1/4) = 12.15737097042548... ).`            (7.4)

This is a literal new inequality produced by applying the completed partner result. It is useful as a secondary exit when a residual principal triple is quantitatively available. It does not assert that such a triple is forced by the three-eigenvalue hypothesis.

The newest partner r26 scalar-conditioning counterexample is also applied negatively: no step in this report replaces an average over residual states by `sup_b ||p_(Q3|Q'=b)||_infinity`.

## 8. Verification

`check_constants.py` and `CHECK_RESULTS.txt` are committed beside this report. They verify:

* `c_(1/4)=0.1492703610829477...`;
* the exact weighted-envelope identity (4.3) at three positive scales;
* the high-leverage implication `gamma^2/2=sigma^2/6` for `gamma=sigma/sqrt(3)`;
* the B19 high-endpoint coefficient `26.539635869538305...` multiplying `C_proj^(1/4)`;
* the partner-lift coefficient `12.157370970425480...`.

The output terminates `STATUS=PASS`. The checker validates algebra/constants only; the proof is the symbolic argument above.

A manual changed-file review was performed on the explicit allowlist for this run (`check_constants.py`, `CHECK_RESULTS.txt`, `REPORT.md`): it contains mathematical text/code only, no credentials, scheduler identifiers, machine paths, unrelated private data, or benchmark material. No public release or remote workflow was invoked.

## 9. What remains unpaid

The result removes the **high-ridge-leverage endpoint of the B19 r13 one-effective-direction residue**, complementing the previous low-leverage ridge splice. It does not solve the global structural reduction from three large eigenvalues.

The first remaining proof obligation for B01 is now outside this closed local branch: obtain a product-preserving fractional-trace / random-slope mechanism that handles the unresolved O0 one-/two-heavy aggregate skeletons and the broader O1/O2/O3 overlap classes without requiring one well-conditioned principal triple or one fixed minor. The row-aggregate lemma suggests the correct currency is a sum/linear image of an entire physical bank before reciprocal payment.

Full QFORM remains **OPEN**. No full-proof candidate is claimed, and the full continuity conclusion is also OPEN.
