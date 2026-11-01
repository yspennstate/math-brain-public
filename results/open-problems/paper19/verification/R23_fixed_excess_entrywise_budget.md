# R23 verification - fixed-excess entrywise heterogeneous budget

## Scope

Round R23 checked the fixed-excess rectangular lower side with deterministic
entrywise scalar density bounds \(K_{m,a,q}\).  This refines the row-wise
heterogeneous fixed-excess budget and remains a lower-side finite-budget result.

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0c68-892c-71f2-9d86-d60b8e5273c0` checked the fixed-row-set
   one-matrix estimate, including the Cauchy--Binet determinant factor and the
   complex Jacobian.
2. `019f0c68-b870-72d2-86c0-720af0b9285d` checked the nonuniform finite-budget
   sum and verified the row-wise and uniform specializations.
3. `019f0c68-df21-7e62-9725-00f7349344c5` checked placement and recommended
   adding the result after the existing row-wise fixed-excess corollary.
4. `019f0c69-00d4-7e43-bc71-6e36b5c630ca` red-teamed adaptive column and
   Cauchy--Binet block choices, random budgets, singular parts, and overclaims.
5. `019f0c69-1fb7-7380-b381-970b3894f7f0` checked the standalone/master
   integration plan and ledger wording.

## Result

Set \(p=r+1\).  For a selected row set \(T\), \(|T|=m+r\), and column
\(q\in[m]\), define
\[
  \kappa_{T,q}^{(r)}
  =
  \max_{\substack{S\subset T\\ |S|=p}}\prod_{a\in S}K_{m,a,q}.
\]
The one-row-set estimate is
\[
  \PP\{\smin(A_{m,T})\le t\}
  \le
  C_{\F,r}m^{d_\F p}t^{d_\F p}
  \sum_{q=1}^m \kappa_{T,q}^{(r)},
  \qquad 0<t\le1.
\]
The finite-family budget is
\[
  \Xi_{m,r}
  =
  \sum_{\substack{T\subset[N_m]\\ |T|=m+r}}
  \sum_{q=1}^{m}\kappa_{T,q}^{(r)} .
\]
Applying the nonuniform finite-budget corollary gives threshold numerator
\[
  \log\Xi_{m,r}+d_\F(r+1)\log m+O_{\F,r}(1)+u_m
\]
and denominator \(d_\F(r+1)\).

If \(K_{m,a,q}=K_{m,a}\), then \(\Xi_{m,r}=m\Theta_{m,r}\), so this recovers the
row-wise fixed-excess budget.  If all \(K_{m,a,q}=K_m\), then
\[
  \Xi_{m,r}=mK_m^{r+1}\binom{N_m}{m+r},
\]
and the numerator becomes
\[
  L_m^{(r)}+(r+1)\log K_m+(1+d_\F(r+1))\log m+O_{\F,r}(1)+u_m,
\]
matching the uniform finite-entropy statement.

## Guardrails

The density bounds are deterministic and the entries are independent.  The
complex case requires genuine two-real-dimensional scalar densities on
\(\C\simeq\R^2\).  The Cauchy--Binet coordinate block is chosen after
conditioning on all other columns, so the proof pays the maximum over
\(S\subset T\), \(|S|=r+1\).  Singular or atomic parts, random or
value-dependent budgets, nonuniform exponents, upper sides, exact bases,
moving-aspect exact laws, Poisson laws, and phase-retrieval stability claims
are not covered.

## Manuscript changes

- `parts/geometric.tex`: added `rect:entrywise-heterogeneous-fixed-excess`.
- `master/chO_phase_retrieval_rmt.tex`: added a compact Lane O paragraph.
- `PLAN.md`, `STATE.md`, and `MASTER_STATE.md` were updated.

## Build verification

`pdflatex -interaction=nonstopmode extremal_hard_edge.tex` was rerun after the
initial cross-reference warning; the final standalone PDF has 38 pages and is
587,597 bytes.

`pdflatex -interaction=nonstopmode master.tex` was rerun in
`~/math-open-problems-fleet/master`; the final master PDF has 853
pages and is 7,759,351 bytes.  It was copied to
`~/Downloads/master.pdf`.

Targeted log scans found no errors, undefined references/citations, or rerun
requests; the only matched lines were the two final `Output written` lines.
