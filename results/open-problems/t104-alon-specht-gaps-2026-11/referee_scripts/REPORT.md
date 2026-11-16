# Referee report on T104_NOTE.md

Theorem 5.2: **SOUND**. Theorem 5.3: **SOUND**.

The finite certificate omitted from the submitted note has been independently reproduced here for every n=5,...,13. There is a false additional assertion at the end of Section 5: the proposed state need not satisfy the transposition-by-transposition inequalities of Proposition 2.1. That assertion is unnecessary for the two theorems and should be removed or weakened.

| Item | Statement checked | Verdict | Reason |
|---|---|---|---|
| 1 | The matrix model, projection, norm and class sum | CORRECT | The pair permutation module splits as [n]+[n-1,1]+[n-2,2]; the displayed projection and class sum hold. |
| 2 | Jucys–Murphy calculation, star, edge, and (5.1) | CORRECT | Independent Young-form matrices give the stated spectra and both equalities. |
| 3 | Two-eigenvalue parametrisation and equivalence of theorems | CORRECT | The spectral decomposition gives precisely the stated weights; all degenerate cases are covered. |
| 4 | Lemma 5.4 | CORRECT | Every intermediate formula checks; exact rational matrix calculations give zero residuals. The hypothesis n>=5 is essential for defining R everywhere. |
| 5 | Deduction and equality cases of Theorem 5.3 | CORRECT | The trial-state quotient bounds lambda_max; its identity and Theorem 6.1 give the result. The equality argument is complete. |
| 6 | Direct check of Theorem 5.2 at n=5,6 | CORRECT | Independent Young-form calculations give minimum defined ratios 3/4 and 4/5. |
| 7 | Cone reduction and finite certificates | CORRECT | Exact expansions have no negative coefficients for every n=5,...,13; the omitted certificate is supplied by the checker here. |
| 8 | Whole-note consistency | WRONG | The last Section 5 paragraph falsely identifies a state satisfying Proposition 2.1. The other checked structural claims agree. |

Detailed proofs, intermediate calculations, exact vectors and chronological verdicts are in [LOG.md](LOG.md). The provisional certificate gap recorded there was subsequently filled; it is not an outstanding mathematical gap.

## The false claim

The note says:

> In the terms of Proposition 2.1, the state matched to the top eigenvector x of L_G is A A^*/tr(A A^*), the image of the uniform state on {1, x}^perp.

Take n=5 and

\[
x=(1,1,0,0,-2)/\sqrt6,\qquad D=AA^*/\operatorname{tr}(AA^*).
\]

An exact rational construction using permutation conjugation of matrices gives

\[
\operatorname{tr}(AA^*)=2,\qquad
\operatorname{tr}(D\rho_{[3,2]}((1\,5)))=-5/18.
\]

For the sign-twisted modules in Conjecture F, Proposition 2.1 would require

\[
2-(x_1-x_5)^2\ \ge\ \frac34\left(1+\operatorname{tr}(D\rho_{[3,2]}((1\,5)))\right).
\]

This reads 1/2 >= 13/24, and fails by 1/24. This x is the top eigenvector of a graph in Theorem 5.2: take g=1 and c=m(x)=1/6, giving mu=5/6 and lam=11/6. Thus restricting the sentence to that family does not fix it. Lemma 5.4 proves the required weighted inequality for the family; it does not prove all the coordinate inequalities of Proposition 2.1.

This is a counterexample to the claimed state matching, not to either main theorem. The exact and floating-point constructions are saved in [step8.json](step8.json).

## Mathematical checks

For item 1, the row-sum map on the unordered-pair module has matrix B with BB^t=(n-2)I+J, so its kernel has dimension n(n-3)/2. The commutant of the pair action has dimension three, since two edges intersect in zero, one or two vertices. Removing the trivial and standard summands leaves one irreducible. A nonzero [n-2,2] polytabloid lies in this kernel, identifying it. For d=diag T, the matrix H=Pi diag(d) Pi satisfies diag H=(n-2)d/n, <T,H>=|d|^2 and |H|^2=(n-2)|d|^2/n. These establish (5.2), including orthogonality and the norm identity. Summing the conjugates entry by entry gives the class-sum scalar (n-1)(n-4)/2. For n=4,...,8 the dimensions were 2,5,9,14,20; projection errors were at most 5.33e-15 and class-sum errors at most 7.11e-15.

For item 3, L=mu Pi+gxx^t gives w_ij=c-gx_i x_j, c=mu/n. Conversely these weights give L=cn Pi+gxx^t. Admissibility is exactly c>=g m, and m>=0. The remaining formulas are

\[
\lambda=cn+g,\quad 2W=cn(n-1)+g,\quad
L(G,[n-2,2])=(2c(n-1)+g/2)I+gX(x).
\]

For g>0, (5.1) is equivalent to lambda_max(X)>=1/2-2(n-1)c/g. Applying Theorem 5.2 at c=gm gives Theorem 5.3; Theorem 5.3 gives all c>=gm, with strict inequality when c>gm. When mu=0, admissibility forces an edge vector. When mu=lam>0, the graph is uniform complete and the right side of (5.1) is mu(3n-4)/n>=mu. The zero graph is immediate. No graph in the stated spectral class is lost. The representation formula needs n>=4; n>=5 is needed for the uniform positivity of Z and the subsequent inequality.

For item 4, permutation conjugation preserves both M_n and its orthogonal complement, so each summand commutes with P. Substitution of Q_ij=delta_ij-1/n-x_i x_j gives all three replacements. Expanding the powers of x_i-x_j and using sum x_i=0 and sum x_i^2=1 proves all seven pair sums; the p_6 terms cancel. The two traces and final identity then follow exactly as displayed. Full derivations are in the log.

For n>=5, Z>0. At n=4, Z=2q-1/2, which vanishes exactly at permutations of (1,1,-1,-1)/2. There A=0 and R is undefined. Add “n>=5” explicitly to the standalone lemma. At other n=4 vectors the algebraic identities remain valid.

For item 5, AA^* is positive semidefinite with positive trace, so R<=lambda_max(X). Lemma 5.4 and Theorem 6.1 therefore prove the bound. At c=gm the two named vectors give, respectively, an edge of weight g/2 and a star of edge weight g/(n-1). The earlier equality calculations and the reversible reduction prove the claimed equalities. The note does not claim an exhaustive equality classification for Theorem 5.3.

## Reproducible numbers

All commands below run from this folder. Every numerical script fixes the random seed, limits numerical libraries to one thread, and sets a 270-second alarm. Raw results are retained alongside the code.

### Item 2: independent Young-form modules

Command:

```sh
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 2
```

| n | Graph, unit weights | lambda_min(tau) | lambda_min(sigma) | Left side (5.1) | Right side (5.1) |
|---|---|---:|---:|---:|---:|
| 5 | Star | 3 | 4 | 5 | 5 |
| 5 | Single edge | 0 | 0 | 2 | 2 |
| 6 | Star | 4 | 5 | 6 | 6 |
| 6 | Single edge | 0 | 0 | 2 | 2 |

The Young matrices pass the involution, braid and distant-commutation checks. Jucys–Murphy diagonal residuals are at most 4.45e-16. The single edge gives equality 0=0 in Conjecture F; its ratio is undefined. Full results: [step2.json](step2.json).

### Item 4: exact matrix calculation

Command:

```sh
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 4
```

Each x is an exact rational unit, sum-zero vector, obtained by a rational Householder reflection. X is built from actual permutation conjugations, and A from the matrix projection, independently of the claimed trace formulas.

| n | tr(AA*) approximately | tr(XAA*) approximately | Exact residuals of both traces and final identity |
|---|---:|---:|---|
| 4 | 1.231400125670322 | 0.084350187866898 | 0, 0, 0 |
| 5 | 1.117047223796596 | 0.120787532345922 | 0, 0, 0 |
| 6 | 2.177599606532613 | 0.519197813417424 | 0, 0, 0 |
| 7 | 3.264011326270933 | 0.996506684627284 | 0, 0, 0 |

All seven exact pair-sum residuals and all exact replacement residuals are zero for every test. The maximum floating-point error in the preliminary identities and pair sums, over n=4,...,9, is 1.17e-15. Exact vectors and fractional traces: [step4.json](step4.json).

### Item 5: equality and counterexample search

Command:

```sh
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 5
```

Write Delta=lambda_max(X)-1/2+2(n-1)m. At the edge vector lambda_max(X)=1/2. At the star vector it is 1/2-2/n; numerical discrepancies are below 4e-16.

| n | Evaluations | Smallest Delta, including equality checks | Best Powell Delta | Star lambda_max(X) |
|---|---:|---:|---:|---:|
| 5 | 4,473 | -5.56e-17 | 6.84e-12 | 0.100000000000000 |
| 6 | 5,822 | 5.55e-17 | 1.96e-11 | 0.166666666666667 |
| 7 | 6,246 | -5.56e-17 | 1.59e-11 | 0.214285714285714 |
| 8 | 8,426 | -5.56e-17 | 9.65e-12 | 0.250000000000000 |
| 9 | 7,510 | 0 | 1.52e-11 | 0.277777777777778 |

For each n the search includes 1,500 Gaussian vectors; every two-value multiplicity split; twelve random three-value vectors for every positive multiplicity split; 280 perturbations of the edge and star vectors at scales 1e-1 through 1e-10; and five Powell runs. Some optimiser runs reached their evaluation cap. No value below -1e-9 was found. This search is supplementary evidence, not a global optimisation proof. Counts by category, vectors and optimiser outcomes: [step5.json](step5.json).

### Item 6: direct Specht-module comparison

Command:

```sh
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 6
```

The modules are built directly for tau=[2,1^(n-2)] and sigma=[2,2,1^(n-4)] in Young's orthogonal form. No matrix model or conjugation identity is used in their Laplacian calculation. Set g=1 and c=m+delta.

| n | Graphs checked | Minimum ratio, delta=0 | delta=0.01 | delta=0.2 | delta=1 | Target |
|---|---:|---:|---:|---:|---:|---:|
| 5 | 2,264 | 0.7499999999999998 | 0.803571428571429 | 1.102941176470588 | 1.211538461538462 | 3/4 |
| 6 | 2,268 | 0.8000000000000006 | 0.866666666666667 | 1.120000000000000 | 1.180952380952381 | 4/5 |

The smallest ratio divided by its target is 0.9999999999999997 and 1.0000000000000007, respectively. Each n has one excluded zero denominator, the single edge. Its signed inequality was also checked. Full results: [step6.json](step6.json).

### Item 7: exact certificates

The requested Python expansions are produced by:

```sh
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 7
```

| n | Cone | Extreme rays | Nonzero coefficients | Zero coefficients | Negative coefficients |
|---|---|---:|---:|---:|---:|
| 5 | R1 | 5 | 209 | 1 | 0 |
| 5 | R2 | 5 | 208 | 2 | 0 |
| 6 | R1 | 6 | 461 | 1 | 0 |
| 6 | R2 | 6 | 460 | 2 | 0 |
| 7 | R1 | 11 | 8,007 | 1 | 0 |
| 7 | R2 | 10 | 5,003 | 2 | 0 |

The complete ray lists and expanded coefficients are in `certificate_nN_RC.txt`. Enumeration is exhaustive: in nonnegative gap coordinates there are only two additional halfspaces, so an extreme ray has support at most three. All such supports and active constraints are enumerated exactly. A separate count proves the claimed R1 formulas s^2+s-1 for n=2s+1 and s^2+s for n=2s+2; enumeration agrees through n=20.

I also checked the rest of the finite range, filling the submission's missing certificate. Commands:

```sh
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 7prep
nice -n 15 /usr/bin/clang++ -O2 -std=c++17 certificate_stream.cpp -o certificate_stream
nice -n 15 ./certificate_stream rays_n13_R1.input
nice -n 15 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 referee.py 7audit
```

Run the third command separately for each input `rays_nN_RC.input`, N=5,...,13 and C=1,2. The checker computes each coefficient by exact polarization, divides by repeated-index factorials, and streams its sign. Its full coefficient dictionaries agree with the Python expansions for n=5,6,7.

| n | R1 rays | R1 degree-six monomials | R2 rays | R2 degree-six monomials | Negative coefficients, both cones |
|---|---:|---:|---:|---:|---:|
| 8 | 12 | 12,376 | 11 | 8,008 | 0 |
| 9 | 19 | 134,596 | 17 | 74,613 | 0 |
| 10 | 20 | 177,100 | 18 | 100,947 | 0 |
| 11 | 29 | 1,344,904 | 26 | 736,281 | 0 |
| 12 | 30 | 1,623,160 | 27 | 906,192 | 0 |
| 13 | 41 | 9,366,819 | 37 | 5,245,786 | 0 |

There is exactly one zero coefficient on R1 and two on R2 in every case. The log proves the polarization formula. The largest moment-lookup allocation is 23,184,352 bytes. An explicit integer bound puts the sum of absolute coefficient numerators below 2.712e21, well below signed 128-bit capacity; lookup moments fit signed 64-bit integers. The longest coefficient pass reported 0.646 seconds. Results and agreement checks: [step7audit.json](step7audit.json); overflow and allocation bounds: [certificate_bounds.json](certificate_bounds.json).

The cone reduction is valid, including vectors with one negative coordinate. Sign change and sorting put every nonzero sum-zero vector into R1 or R2. Each M_i is an actual pair product, hence M>=M_i; its multiplier in G is positive. No unstated sign condition on the middle coordinates is needed for this finite-cone argument.

## Remaining consistency checks and revisions

The hook mean argument works when eigenvalues vanish: it compares ordered averages and never divides by an eigenvalue. Section 1's theorem numbers, constants and equality claims agree with the later statements. The parametrised graph family has generic dimension n.

The Littlewood–Richardson restriction formula and the horizontal-strip criterion in Section 7 are correct. Interlacing, nu_i>=alpha_i>=nu_(i+1), gives the following complete lists for alpha of size four:

| n | tau | alpha for tau | sigma | alpha for sigma | Ratio on the full star |
|---|---|---|---|---|---:|
| 6 | 2211 | 211 only | 222 | 22 only | 5/6 |
| 7 | 3211 | 211 only | 322 | 22 only | 1 |
| 8 | 4211 | 211 only | 422 | 22 only | 1 |

For tau, the first three lower bounds already sum to 2+1+1=4; for sigma the first two sum to 2+2=4. This proves completeness by hand. Making the connected complementary component arbitrarily fast leaves only its trivial representation, so the limiting ratio is the four-vertex value 2/3 in all three cases. If a horizontal-strip indexing set is empty, state the convention min(empty)=+infinity or restrict that limit statement to nonempty sets.

The note should make three revisions: correct the false state-matching sentence; state n>=5 explicitly in Lemma 5.4; and attach a reproducible finite certificate. The checker in this folder fills the last omission independently. The numerical-evidence paragraph should describe “smallest ratios found”; local search does not certify global minima.

No external references were checked, in accordance with the no-browsing instruction. The previously refereed Sections 2–4 and n>=14 proof were checked for compatibility with Section 5, rather than independently re-refereed in full. The broad all-partition numerical searches reported in Section 7 were not reproduced; the narrower independent searches requested here were completed. The n>=14 uniqueness-of-equality claim is not extended here to the finite range.

The sandbox rejected every attempted `nice` priority change with `setpriority: Operation not permitted`. All computations were nevertheless launched with the requested prefix, serially, with small memory use and short runtimes; actual scheduling priority could not be enforced. No files outside this folder were edited, no network access or agents were used, and no push or visible-window launch was made.

Task: “You are refereeing a short mathematical note.” Started 2026-11-11, 22:04 +04.
