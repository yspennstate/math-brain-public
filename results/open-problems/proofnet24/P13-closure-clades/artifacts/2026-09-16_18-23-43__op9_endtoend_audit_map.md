# P13 / I0051 — end-to-end audit map for Aldous–Janson Open Problem 9

Date: 2026-09-16, Asia/Jerusalem.

Purpose: closure-support artifact only. This file does **not** add a new mathematical theorem, does not count as an independent audit, and does not alter the tracked metric. It freezes the exact implication chain that P26 and a distinct OTHER track must independently traverse before the P13 source-matching claim can close.

## Outside source and target

David J. Aldous and Svante Janson, *The Critical Beta-splitting Random Tree II: Overview and Open Problems*, arXiv:2303.02529v3, Open Problem 9 / intake `I0051`.

For `N_m^(n)` equal to the number of size-`m` clades in `DTCS(n)`, the source asks to study the joint distribution `(N_m^(n),2<=m<=n)` in a way permitting covariance calculations and CLTs.

Excluded from this package: Open Problem 8 / Ansatz 20; Open Problem 14; the historical random-matrix P13 work (owned solely by P12 under the revised fleet assignment).

## Canonical author-side proof chain

### A. Exact finite law and counterexample-first gate

1. `P13-I0051-INDEPENDENCE-NOGO-01`.
   Exact witness at `n=4`:
   `Cov(N_4(2),N_4(3))=-24/121`, so coordinate independence is false.

2. Exact joint PGF recursion, for `F_1=1`:

   `F_n(z)=z_n sum_{i=1}^{n-1} q(n,i) F_i F_{n-i}`,

   with `q(n,i)=n/[2 h_{n-1} i(n-i)]`.

Finite exact checkers and outputs are archived under `proofnet24/P13-closure-clades/artifacts/`; the newest independent author-side stuck self-check extends the DTCS recurrence comparisons through `n=12`. Those are self-checks, not closure audits.

### B. Exact covariance recursion and maximal finite block

Define

`mu_r(n)=E N_n(r)`,
`g_r(n,i)=mu_r(i)+mu_r(n-i)`,
`eta_rs(n)=n^{-1} Cov_{I~q_n}(g_r(n,I),g_s(n,I))`,
`C_rs(n)=n^{-1} Cov(N_n(r),N_n(s))`.

The exact normalized covariance recursion is

`C_rs(n)=sum_{i=1}^{n-1} C_rs(i)/[h_{n-1}(n-i)] + eta_rs(n)`.

If `a(n,j)` is the harmonic-descent occupation probability, then

`C_rs(n)=sum_{j=2}^n a(n,j) eta_rs(j)`.

Since `eta_rs(j)=0` for `j<max(r,s)`, this gives every entry of the complete sizes-`2,...,n` covariance block. This is the reason the frozen metric has reached the maximal possible value `m=n`.

Canonical theorem report for this step:
`proofnet24/P13-closure-clades/runs/2026-09-16/2026-09-16_16-03-16__run-report.md`, creation commit `7edf5ee6907526b7dae4dfd359b7c3d91d457cfd`, verified blob `3807cbfebf8c752d86d8e1f34d14b20a1b1b78d2`.

### C. Uniform covariance kernel

The same report proves the uniform mean remainder and full-kernel estimate. With

`rho_r = 6 h_{r-1}/[pi^2 r(r-1)]`,
`e_r(j)=mu_r(j)-rho_r j`,

one has a uniform bound `|e_r(j)| <= 2/log 2`, hence `|eta_rs(n)| <= 16/[n (log 2)^2]`.

Defining

`Sigma_rs = sum_{j=2}^infty a(j) eta_rs(j)`,
`a(j)=6 h_{j-1}/[pi^2(j-1)]`,

and `alpha=(3-sqrt(5))/2`, the author-side proof establishes

`sup_{r,s>=2} |C_rs(n)-Sigma_rs| = O(n^{-alpha})`.

### D. Trace forcing and Hilbert tail

Canonical theorem report:
`proofnet24/P13-closure-clades/runs/2026-09-16/2026-09-16_16-31-13__run-report.md`, verified blob `21b97be166462de66533ada5b8485087b30cfeed`.

Claim IDs:
- `P13-I0051-TRACE-FORCING-03`;
- `P13-I0051-HILBERT-TAIL-03`.

Writing

`T_j=sum_{r>=2} eta_rr(j)`,

it proves

`T_j <= C (1+log(j+1))/j`,

and therefore `Sigma` is trace class. If `Q_R` projects onto clade-size coordinates `r>R`, then

`sup_n E ||Q_R Z_n||_2^2 = O(R^{-alpha} log R)`,

where `Z_n(r)=(N_n(r)-E N_n(r))/sqrt(n)` is zero-padded for `r>n`.

This three-region Green-kernel summation is the most important remaining step for an end-to-end independent audit. A component audit that assumes this bound does not certify it.

### E. Full moving-vector CLT and exact-covariance Gaussian comparison

Claim IDs:
- `P13-I0051-HILBERT-FULL-CLT-03`;
- `P13-I0051-EXACTCOV-GAUSSIAN-03`.

The author-side proof concludes

`Z_n => G` in `H=ell^2({2,3,...})`,

for a centered trace-class Gaussian with covariance `Sigma`. If `C_n=Cov(Z_n)` and `Gamma_n=N_H(0,C_n)`, then

`d_BL^H(Law(Z_n),Gamma_n) -> 0`.

The exact finite-`n` singular constraints are preserved, including `Z_n(n)=0` and `sum_{r=2}^{n-1} Z_n(r)=0`.

### F. Source-match claim

`P13-I0051-OP9-SOURCE-MATCH-03` is currently labelled **mathematically PROVED / NOT CLOSURE-CERTIFIED**: exact finite joint recursion + complete finite covariance matrix + covariance asymptotics + full moving-vector Gaussian approximation appear to meet the stated Open Problem 9 request.

An independent auditor must check the implication against the exact current source wording rather than accepting the author-side label.

## Current independent-audit evidence

### P12 component audit 1

`P12-AUDIT-P13-I0051-HILBERT-GAUSSIAN-52 = PASS` in
`proofnet24/P12-smooth-iid/runs/2026-09-16/2026-09-16_17-17-00__run-report.md`, creation commit `375064e47624449481ea8cc3094bc8b31ef617b2`, verified blob `6b3d09976d1b7241bce240f12df18d2c0e5aacdc`.

Scope: independently checks the terminal Hilbert compact-containment / exact-covariance Gaussian comparison **conditional on the P13 Hilbert-tail and preceding inputs**. Not an end-to-end audit.

### P12 component audit 2

`P12-AUDIT-P13-I0051-INDEPENDENCE-NOGO-53 = PASS` in
`proofnet24/P12-smooth-iid/runs/2026-09-16/2026-09-16_18-19-23__run-report.md`, creation commit `de48ffa8f3e90c6b484d267fcb3cbce89bfe4e4c`, verified report blob `dc25b972d524f507b8ad6728c4e3216a7aee1b5a`.

Its independent exact checker is
`proofnet24/P12-smooth-iid/artifacts/2026-09-16_18-19-23__p13_n4_cov_audit.py`, creation commit `32ae81ba3a2e48de31d2c17cff0847659fa06c7b`, blob `785b787888208a3030c86140e066c58260ad5b64`; executed output creation commit `75188f3b83e93743c2ba93d9b53a43380a65445c`, output blob `8274bb28cfc9028a96cd0b91bfc4447c2932b547`.

Scope: exact `n=4` dependence witness only. Not an end-to-end audit.

### P26 audit slot

No durable `P26-AUDIT-P13` record was located in the current repository search. The newest observed P26 audit work is on C31 / Aldous–Fill 4.49(ii), not P13. Therefore the P26 full-audit slot remains OPEN.

## Closure checklist for each full auditor

A qualifying full audit must independently verify, in order:

1. current arXiv revision and exact Open Problem 9 scope;
2. DTCS split normalization and the full joint PGF recursion;
3. mean/covariance root recursions and normalization conventions;
4. Green representation via the harmonic-descent chain;
5. imported Brandenberger–Chin–Mossel hypotheses and the precise monotonicity / short-time estimates used;
6. the uniform mean-remainder bound and its quantifiers in `r,n`;
7. trace forcing `T_j=O(log j/j)`;
8. the three-region Hilbert-tail estimate uniformly in `n`;
9. fixed-dimensional scalar contraction CLTs and Cramér–Wold passage;
10. Hilbert compact containment / weak convergence;
11. convergence of exact finite covariance Gaussian laws and singular constraints;
12. the final source-match implication;
13. a current prior-art search for a previously published static terminal full-vector covariance/CLT theorem.

Passing only items 9–11 or only a finite exact witness does not count as a full audit.

## Closure gate

Use

`ClosureReady(I0051) = S & E & A26 & Aother & P`,

where `S` is the source-matching proof, `E` the exact finite core, `A26` a P26 end-to-end audit, `Aother` a distinct OTHER-track end-to-end audit, and `P` final prior-art/source-scope clearance.

At creation of this map the supported state is

`(S,E,A26,Aother,P) = (1,1,0,0,0)`.

The two P12 PASS records above are valuable component audits but do not change `Aother` from zero.

## Directed P13 -> P14 audit evidence

Under the revised fleet, P13 audits P14. P13 independently checked P14 equation (5.1), the forest decomposition recurrence

`F_G(S)=sum_{T subseteq S, min(S) in T} tau_G(T) F_G(S\T)`.

Exact checker:
`proofnet24/P13-closure-clades/artifacts/2026-09-16_18-05-19__audit_P14_forest_recurrence.py`, creation commit `d6cca1f38668dc76d4b1ae8244f2fbd56f5e8968`, blob `e7147e5bc259840e37498f4b5a7101cbde7a8dc6`.

Executed output:
`proofnet24/P13-closure-clades/artifacts/2026-09-16_18-05-19__audit_P14_forest_recurrence.out`, creation commit `a71b50bf91d5df55eddacfa65be9068d5f71b003`, blob `2905d08356cc82229991a9e4179252ef8291c9aa`.

Scope: every labeled simple graph on `n=1,...,5` and every nonempty vertex subset; `1099` graphs and `32767` subset recurrences; result `PASS`. This independently validates that concrete recurrence lemma only, not P14's complete n=8 certificate.
