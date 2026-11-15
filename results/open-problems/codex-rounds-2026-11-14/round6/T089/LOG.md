# T089 log

Task: "take the NEXT checkable step on this problem, building on that work."
Received 2026-11-15 approximately 10:40 Asia/Tbilisi (UTC+04).

## Orientation and bounded literature check

All writes are confined to this folder. The current task's explicit restriction
overrides the earlier instructions to mutate the shared mesh, checklist and
brain. Read startup memory and compute_state.json directly; no shared-state
commands, git, or subagents. The compute state is warn / owner_away_open,
cpu_saturated. Computations will be small standard-library jobs, one process,
with OMP_NUM_THREADS=1 and nice -n 15, with actual priority checked inside Python.

The initial web check finished within five minutes. Queries:
`Bohigas Giannoni Schmit conjecture proof billiard GOE 2025 2026` and
`GOE quantum chaos Sinai billiard spectral statistics rigorous conjecture 2026`.
Opened primary sources:

- Julien Moy, *Smooth spectral statistics of random perturbations of
  Schrödinger operators near Anosov energy levels*, arXiv:2610.09869,
  https://arxiv.org/abs/2610.09869 . The page still lists v1, 7 October 2026;
  random perturbations and smooth mesoscopic statistics do not prove the
  requested microscopic spacing limit for a fixed billiard.
- Matic Orel, *Perturbed quantum billiards on the hyperbolic plane*,
  arXiv:2607.03786, https://arxiv.org/abs/2607.03786 . Numerical eigenvalue
  sequences and an arithmetic-to-GOE crossover, not a fixed-billiard theorem.
- Alexander I. Bufetov, Pavel P. Nikitin, Yanqi Qiu, *On Number Rigidity
  for Pfaffian Point Processes*, arXiv:1810.09223,
  https://arxiv.org/html/1810.09223 . Opened the full HTML for the orthogonal
  sine-process kernel used by the predecessor.

No resolution found in this bounded search. No SOLVED_ELSEWHERE.md warranted.

## First analytic recheck

Reading the original, round 3, round 4 and round 5 reports, logs, proofs and
scripts, without executing scripts in their read-only source folders.
The round 5 main argument is consistent: transform only the smooth v rows
and columns by normalized divided differences. Its determinant is
F_k/(pi^K Vandermonde), K=k(k-1)/2, F_k=product n! (0<=n<k).
The remaining entry bounds are 1/2 in the u/u block, 1/i in smooth column i
of the mixed block, and pi/(i+j) in the v/v block off the diagonal.
Hadamard and det=(Pf)^2 give

    r_k(x) <= (22/7)^K |Vandermonde(x)| d_k^(1/4) / F_k.

The jump block is not differentiated. The diagonal v/v entries remain zero.
The Chebyshev maximum bound then reproduces the predecessor's M_k(R).
An independent exact arithmetic check of its displayed constants is next.

## Extension chosen before computation

Evaluate the ordered Vandermonde integral exactly, replacing the maximum
bound in round 5. This is the alternative next step explicitly named in its
report. Prove the integration identity directly using determinants and
Pfaffians, so the new constants need no unverified numerical integration.
Use two independent exact evaluations to audit the constants and test even
and odd dimensions separately. This changes only the GOE target remainder;
it supplies no chaotic-billiard moment errors or target moment tables.

## Independent round 5 recheck passed

Completed all requested predecessor proof, report, log and script reads.
Wrote recheck_previous.py without importing predecessor code. Command (exit 0):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py > recheck_output.txt 2>&1
```

Output: previous_result_holds=true; 72 exact fourth-power comparisons between
the displayed formula and a full envelope matrix with incrementally formed
normalization factors; first even orders 6,8,10 at R=1/2,1,2; both saved
order-10 and order-20 fractions agree; the rational order-10 enclosure and
order-20 <10^-89 assertion hold. Also checked 1,365 alternating binomial
identities. Elapsed 0.103 s; peak RSS 15,040,512 bytes; actual nice=20.
The nice launcher prints a sandbox warning, but the inherited priority passes.
The analytic and exact arithmetic main claims of round 5 hold.

## Integration identity derived

For ordered nodes in [0,1], the determinant integral is

    integral_(x1<...<xk) Vandermonde(x) dx
      = (1/k!) product_(1<=i<j<=k) (j-i)/(i+j).

For even k, expand the sign-kernel Pfaffian under the determinant integral.
Its entries become (j-i)/(ij(i+j)). Factoring 1/i from row and column i
reduces this to the Schur Pfaffian product. For odd k augment by the vector
1/i; obtain that product by taking a final Schur parameter to infinity.
A dummy atom after the interval proves the odd determinant-integral formula
with the same normalization. A full proof and independent exact checks follow.

The product of the numerators j-i is exactly F_k. It cancels the F_k in
the predecessor's pointwise bound. The proposed integrated remainder is

    N_k(R) = (22/7)^K R^(k+K) d_k^(1/4)
               / [ k! product_(i<j)(i+j) ].

This identity evaluates the Vandermonde envelope, not the GOE moments.

## Exploratory constants and parity check

Two tiny inline standard-library commands used the required environment,
`nice -n 15 python3 -B -`, and checked actual nice>=15. The first evaluated
N_k(R)^4 exactly and printed diagnostic fourth roots. At R=2, the even-order
threshold remains 10, but N_10(2) is approximately 8.2532e-12. Thus integration
alone does not lower the first successful EVEN order to 8: N_8(2) is about
6.2246e-5. No such order-8 claim will be made.

The adjacent Bonferroni comparison is valid for odd orders too: at odd k,
U=S_(k-1), L=S_k, and U-L=b_k, so exactly the same target-only estimate
uses the errors of moments 1,...,k. This is an application of the existing
comparison, with its parity convention reversed. The chosen integration
extension covers odd dimensions as well, so its final constants and checker
will test both parities. A direct determinant integration by subset dynamic
programming will independently check the Pfaffian product, without numerical
quadrature or importing predecessor code.

## Exact integration audit passed

Wrote check_integration.py. Command (exit 0):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_integration.py > integration_output.txt 2>&1
```

Every determinant integral was evaluated three independent ways: signed
monomial integration by subset dynamic programming, recursive Pfaffian
matching expansion, and the pair-product formula. All 54 checks passed:
ordinary Vandermondes in dimensions 1,...,14, plus 40 exponent sets, including
reversed exponents and repeated rows. Both parities are included. A fourth
evaluation, product_j ((j-1)!)^2/(2j-1)!, agrees in all ordinary cases.

The constant audit passed 100 exact fourth-power comparisons with an
independently assembled entrywise envelope, 14 checks of cancellation
against the uncancelled integral expression, and 20 maximum-versus-integral
comparisons. Exact integer fourth-root enclosures give

    55771278/10^15 < N_9(2) < 55771279/10^15 < 10^-6,
    8253202/10^18 < N_10(2) < 8253203/10^18 < 10^-11.

All smaller positive orders were checked. First unrestricted successful
orders are 5,6,9 at R=1/2,1,2; first even orders are 6,6,10. These concern
this bound, not the actual moments. The order-10 bound improves the previous
bound by a factor greater than 60,000, certified by a rational fourth-power
comparison. The R=2 order-9 ordered integral is exactly

    1/5954093444023153228800000.

The comparison audit passed 38,988 checks for 57 rational count laws,
including 19,494 odd-order checks and a rare count-64 cluster. In particular
the odd-order inclusion-exclusion comparison is valid without an empirical
tail estimate. No mathematical check failed.

Elapsed 0.888 s, measured peak RSS 17,416,192 bytes, one process, actual
nice=20. Both scripts use 256 MiB measured RSS and 120-second elapsed guards;
no OS-enforced cap is claimed. Full outputs and exact fractions are saved in
integration_output.txt and integration_data.json. The compute state was
re-read before the audit: warn / owner_away_open, no distress.

## Proof completed and attempted breaks

Wrote PROOF.md with the full pointwise-envelope derivation, even and odd
determinant integration identities, a polynomial proof of the Schur Pfaffian
product, the exact constants, and the nine-moment/grid certificates.

Checks of the load-bearing normalizations:

- The factorial correlation integral has 1/k! on the cube. Passing to the
  ordered chamber removes it; the determinant integral itself has a separate
  factor 1/k!. The direct signed-monomial integration confirms both factors.
- The Vandermonde has degree K, so scaling contributes R^(k+K), including
  the k volume factors. The entrywise-product audit builds that exponent as
  sum_(i=1)^k i, independently of the closed formula.
- In odd dimension the dummy atom contributes once, at the right endpoint
  of the order; repeated atom coordinates give zero determinants. The
  added moment column is +1/i above the diagonal. Tests include k=1,
  reversed exponent order, and repeated exponent rows to catch a sign error.
- In the polynomial Pfaffian proof, specializing the last parameters to
  a,-a leaves only their pairing. Its sign is positive. Both the multiplied
  Pfaffian and Vandermonde acquire (-2a) product_i(t_i^2-a^2), giving
  constant one, with no missing sign or multiplicity.
- The pointwise GOE bound uses only divided differences of smooth rows.
  Coincident nodes are a null set; no continuity through the jump in I is
  asserted. The transformed v/v diagonal is zero by antisymmetry.
- R=0 gives zero and k=1 gives N_1(R)=R. The exact audit includes R=0
  and tests both parities through order 20 for the constants.
- The proposed even order 8 still fails at R=2. The useful improvement is
  the smaller order-10 constant and the successful odd order 9.

An additional inline exact command, using the same environment and nice
launcher, evaluated the OLD bound at orders 8,9,10 and checked every old
order 1,...,9 against 10^-6. This rules out attributing the order-9 improvement
merely to reversing the parity convention. The output is recorded next.

No GOE moments were numerically integrated: only an explicit envelope was
integrated exactly. There are no certified moment tables and no billiard
eigenvalue computations. The determinant and Pfaffian test models verify
algebraic integration, not a GOE sampling experiment. No test of the final
result failed.

The extra old-bound output was:

```text
previous order 8 enclosure endpoints /10^12: 305683053963 305683053964
previous order 9 enclosure endpoints /10^12: 976415769 976415770
previous order 10 enclosure endpoints /10^12: 517385 517386
all previous orders 1 through 9 exceed 1e-6: True
```

One subsequent formatting patch missed its context and changed no files;
this corrected append records the output. No mathematical computation failed.

## Report and final independent artifact audit

Created REPORT.md with the partial verdict, the nine-moment result, commands,
limits and the next target-table task. Added the explicit empty-integral
convention A_0=1 and nonnegative-integer exponent domain to PROOF.md.

A final read-only inline standard-library audit ran with
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B -`.
It independently rebuilt A_9 and A_10 from the factorial recurrence and
assembled the UNCANCELLED original pointwise envelope from every individual
row-norm contribution. Both resulting fourth powers equal the saved fractions
and lie strictly between the displayed rational endpoints. It re-derived
every reported audit count and checked the nine deliverables and report
verdict. Exit status 0; output:

```text
independent uncancelled integral and row-product audit passed at k=9
independent uncancelled integral and row-product audit passed at k=10
Final artifact and independent count audit passed; nine required files checked.
nice=20; peak_rss_bytes_macos=14680064
```

The nine deliverables are REPORT.md, PROOF.md, LOG.md, recheck_previous.py,
check_integration.py, recheck_output.txt, integration_output.txt,
recheck_data.json and integration_data.json. No predecessor file was
executed or edited. All explicit writes remained in this folder.
