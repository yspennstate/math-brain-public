Model: GPT-5.6 Sol. Reasoning: UNVERIFIED runtime level; GPT-6/maximum was requested, but the scheduler exposes no model/reasoning selector, so I do not claim GPT-6 maximum ran.
Problem: planar self-avoiding-walk displacement — Flory (1949) / Nienhuis (1982). Metric: **no movement** — before \((a,C,n_0)=(2,1,1)\); after \((a,C,n_0)=(2,1,1)\) for the original uniform nearest-neighbor \(n\)-step SAW on \(\mathbb Z^2\). Status: **OPEN**. Unchanged-count: **1**.

# R11 immutable run report — 2026-09-16

Run ID: `2026-09-16T14-40-03Z_saw-quantitative-renewal-trace-b7c2`  
Repository: `yspennstate/math-open-problems`, branch `master`.

## 1. Required repository continuation

Read before new mathematics:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/FLEET_2026-09-16.md` and `operations/RFLEET_2026-09-16.md`;
- newest canonical own report `runs/R11/2026-09-16T13-37-28Z_saw-rate-modulus-a31f.md` and its checker/output;
- newest neighboring canonical reports actually present: R10 `runs/R10/20260916T143504Z_7b31c4e9.md`, R12 `runs/R12/2026-09-16T14-30-05Z_6d92bf.md`, and directed-audit target R14 `runs/R14/2026-09-16T13-53-07Z_r14-c175-baseline.md` plus its checker/output;
- repository inventory and the current intake ledgers `probability_1000_intake_{D,E,F,G,H,I}_*/problems.jsonl` and `probability_1000_intake_claude_20260907/problems.jsonl`.

The connector can enumerate the intake ledgers and materialize targeted line ranges, but a literal row-by-row model-visible reread of all roughly 780 JSONL records exceeds the connector response budget. I therefore record the intake sweep as **ACCESS-LIMITED / INCOMPLETE** rather than pretending a complete row-by-row read. No ownership/admission decision in this run depends on stale `admitted=true`: R11's assignment is explicit in the current fleet files and RESULTS/QUEUE state.

The root shared ledger remains P26-owned; this run does not edit `RESULTS.md`.

Incoming independent audit already present: R10's newest report independently audits prior R11-GH-C001 and marks the **conditional compiler** PASS (`R10-AUDIT-R11-C001-20260916`).

## 2. Outside source and current-status refresh — 2026-09-16

### Original source normalization

Paul J. Flory, *The Configuration of Real Polymer Chains*, J. Chem. Phys. 17 (1949), 303--310, DOI `10.1063/1.1747243`, is the excluded-volume polymer-scaling origin. Its abstract says that excluded-volume interference changes the random-flight exponent and predicts an exponent approaching 0.60 for long chains in good solvents. I do **not** attribute the exact planar lattice value \(3/4\) directly to that paper.

Bernard Nienhuis, *Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions*, Phys. Rev. Lett. 49 (1982), 1062--1065, DOI `10.1103/PhysRevLett.49.1062`, is the Coulomb-gas source behind the two-dimensional SAW exponent \(\nu=3/4\). Its published abstract explicitly says the calculation is subject to plausible assumptions.

Duminil-Copin--Hammond, arXiv:1205.0401 / CMP 324 (2013), gives the exact rigorous law used here: `SAW_n` is the **uniform** law on nearest-neighbor self-avoiding walks \(\gamma:\{0,\ldots,n\}\to\mathbb Z^d\) with \(\gamma_0=0\). Their introduction records the two-dimensional Coulomb-gas prediction \(\nu=3/4\), and their Question 1 asks for any fixed-power improvement over the ballistic second-moment exponent.

Their theorem is fixed-speed exponential sub-ballisticity:
\[
\forall v>0\ \exists c(v)>0:\qquad
\mathbb P_{\mathrm{SAW}_n}\!\left(\max_{k\le n}\|\gamma_k\|>vn\right)
\le e^{-c(v)n}.
\]
It does not give a modulus of \(c(v)\) as \(v\downarrow0\).

Fresh bounded searches on 2026-09-16 included exact Flory/Nienhuis/Duminil-Copin--Hammond locators, `square lattice self avoiding walk exponent 3/4 rigorous proof 2026`, and later-author/citing-work searches. I found no accepted theorem for ordinary square-lattice uniform SAW giving a fixed second-moment power \(a<2\). This is a bounded search statement, not a proof of bibliographic nonexistence.

Krachun--Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, Ann. Probab. 54 (2026), 1109--1125, proves \(O(n/\log n)\) radius with high probability on the **hexagonal lattice** and polynomial decay of a critical bridge-height partition function. It is not a square-lattice exponent theorem.

### Frozen metric

For the original walk law,
\[
\|\omega_n\|_2\le n
\]
deterministically, hence
\[
\boxed{\mathbb E\|\omega_n\|_2^2\le n^2}
\]
with
\[
(a,C,n_0)=(2,1,1).
\]
Duminil-Copin--Hammond improve this qualitatively to \(o(n^2)\), but not to any verified fixed power \(n^{2-\varepsilon}\). Thus the tracked metric does not move this run.

## 3. Retained canonical R11 state

Prior R11-GH-X001 proves that the logical form
\[
\forall v>0\ \exists c(v)>0:
\mathbb P(R_n>vn)\le e^{-c(v)n}
\]
alone does not imply any fixed power improvement of the second moment.

Prior R11-GH-C001 proves the quantitative compiler: if uniformly for the original SAW law
\[
\mathbb P(R_n>vn)\le e^{-c_0nv^\kappa}
\]
for all small \(v\), then every \(\eta<1/\kappa\) gives
\[
\mathbb E\|\omega_n\|^2\le 2n^{2-2\eta}
\]
for explicit sufficiently large \(n\). In particular, \(\kappa<4\) would give the target upper exponent \(a=3/2\) by choosing \(\eta=1/4\).

This run asks whether direct quantitative tracking of the published Duminil-Copin--Hammond bridge proof can supply such a polynomial small-speed modulus.

## 4. Refute-first result: the straightforward quantitative DCH route degenerates doubly exponentially

The run first tried to **refute** the optimistic route “track the constants in Proposition 3.2 and obtain \(c(v)\ge c_0v^\kappa\).” The result is R11-GH-X002 below: the branch-aware constant-tracking compiler itself has a worst-case doubly-exponential cap in \(1/v\). This does not refute the SAW target; it refutes this direct proof strategy as a source of the needed polynomial modulus.

To state the obstruction cleanly, I first isolate two quantitative components of the published bridge argument.

## 5. R11-GH-C002 — fixed-parameter quantitative one-step crossing-number reduction

**STATUS: PROVED (quantitative unpacking of the published DCH maps; no novelty claim about the underlying surgery).**

Duminil-Copin--Hammond use sets \({\rm SAB}^{k}_{n,v,\delta}\) of length-\(n\), height-at-least-\(vn\) bridges for which at least \(\delta n\) horizontal levels have crossing number between 1 and \(k\). Their reduction is a three-case trichotomy: many renewal points; few zigzags and unfold all zigzags; or many zigzags but few renewal points and apply `MultiUnf` to many short zigzags.

Fix
\[
0<z\le\frac18,\qquad k\ge2,\qquad v>0,\qquad\delta>0.
\]
Put
\[
L=\left\lceil\frac1z\right\rceil,
\quad
r=\frac{z}{8L},
\quad
s=\frac{z}{24L^2},
\quad
d=\frac{s}{2}=\frac{z}{48L^2},
\]
and
\[
\delta_*:=\min\{\delta,r,d\}.
\]
Let
\[
h(z)=H(4z):=-4z\log(4z)-(1-4z)\log(1-4z).
\]
Then, as \(n\to\infty\), the published one-step maps imply
\[
\boxed{
|{\rm SAB}^{k-1}_{n,v,\delta_*}|
\ge
\exp\{-(h(z)+o(1))n\}
|{\rm SAB}^{k}_{n,v,\delta}|.
}
\tag{R11-GH-C002}
\]

### Proof

Write \(A={\rm SAB}^{k}_{n,v,\delta}\).

**Case 1: many renewal points.** If at least \(|A|/4\) source bridges have at least \(rn\) renewal points, those bridges already lie in \({\rm SAB}^{1}_{n,v,r}\subseteq{\rm SAB}^{k-1}_{n,v,\delta_*}\). The factor 4 is \(e^{o(n)}\).

Assume henceforth that more than \(3|A|/4\) bridges have fewer than \(rn\) renewal points.

**Case 2: few zigzags.** If at least \(|A|/4\) bridges have at most \(2zn\) zigzags, DCH's unfold-all-zigzags map sends each such bridge to \({\rm SAB}^{k-1}_{n,v,\delta}\). Their inverse reconstruction marks at most \(4zn\) zig/zag vertices, so
\[
\#\text{preimages}
\le
\sum_{j\le4zn}\binom{n+1}{j}
=
\exp\{(H(4z)+o(1))n\},
\]
where \(4z\le1/2\). The multi-valued-map principle gives the claimed loss.

**Case 3: many zigzags and few renewal points.** Otherwise more than \(3|A|/4\) bridges have more than \(2zn\) zigzags; intersecting the two \(3/4\)-large source classes leaves at least \(|A|/2\) bridges with both many zigzags and fewer than \(rn\) renewals.

The central sections of distinct zigzags are disjoint. Since each long central section has length at least \(L\), at most \(n/L\le zn\) zigzags are long. Thus at least \(zn\) zigzags are short.

Apply the published `MultiUnf` map selecting \(\lfloor sn\rfloor\) short zigzags, with their notation specialized to
\[
\delta'=z,
\qquad
\varepsilon=r,
\qquad
\delta''=s.
\]
The two finite conditions in the reconstruction estimate hold with room:
\[
r+3Ls
=
\frac{z}{8L}+\frac{z}{8L}
=
\frac{z}{4L}
\le z,
\]
and
\[
\frac{z-s}{(r+3Ls)L}
=
4\left(1-\frac1{24L^2}\right)
\ge\frac{23}{6}>2.
\]
Hence the DCH multi-valued-map criterion applies. The image lies in \({\rm SAB}^{1}\) and gains \(\lfloor sn\rfloor\) renewal points. For all sufficiently large \(n\), \(\lfloor sn\rfloor\ge dn\). The output multiplicity gain is exponential in \(sn\), while the inverse multiplicity is controlled by the displayed criterion; in particular there is no positive exponential loss that needs to be charged here. Therefore Case 3 also implies the stated bound after weakening to the common cost \(h(z)\).

The three cases exhaust \(A\), proving C002.

The exact checker verifies the displayed finite inequalities for every reduced rational \(z=p/q\in(0,1/8]\) with \(q\le400\).

## 6. R11-GH-C003 — exact renewal Laplace-rate compiler

**STATUS: PROVED.**

Let \(Q=\mathbb P_{\rm iSAB}\) be Kesten's probability law on irreducible bridges,
\[
Q(\eta)=\mu^{-\lvert\eta\rvert},
\]
and write \(\ell=|\eta|\). For \(t>0\), set
\[
\psi(t)=E_Q[e^{-t\ell}].
\]
For \(0<\delta<1\), define
\[
\boxed{
I(\delta)=\sup_{t>0}
\{\delta[-\log\psi(t)]-t\}.
}
\tag{6.1}
\]
Let \(N_n\) be the number of renewal points of a uniform \(n\)-step bridge. Then
\[
\boxed{
\limsup_{n\to\infty}
\frac1n\log
\mathbb P_{{\rm SAB}_n}(N_n\ge\delta n)
\le-I(\delta).
}
\tag{R11-GH-C003}
\]
Moreover
\[
I(\delta)>0,
\qquad
I(\delta)\le\delta\log\mu\le\delta\log3<2\delta.
\tag{6.2}
\]

### Proof

Under the infinite iid concatenation of irreducible bridges, let \(S_m=\ell_1+\cdots+\ell_m\). If the concatenation has a renewal at total time \(n\) and the resulting bridge has at least \(\delta n\) renewal points, then with
\[
m=\lfloor\delta n\rfloor-1
\]
we have \(S_m\le n\). Therefore for every \(t>0\),
\[
\mathbb P(S_m\le n)
\le e^{tn}\psi(t)^m.
\]
DCH Lemma 3.8 identifies the iid-renewal law conditioned on \(n\) being a renewal time with the uniform law on \({\rm SAB}_n\). Also
\[
\mathbb P(n\in\mathcal R)=|{\rm SAB}_n|\mu^{-n}
\ge e^{-C\sqrt n},
\]
using Hammersley--Welsh and \(|{\rm SAW}_n|\ge\mu^n\). Dividing by the renewal-time denominator, taking \(n^{-1}\log\), and using \(m/n\to\delta\) gives
\[
\limsup\frac1n\log P(N_n\ge\delta n)
\le t+\delta\log\psi(t).
\]
Infimize over \(t>0\) to obtain C003.

DCH Theorem 2.5 gives \(E_Q\ell=\infty\). By Fatou/monotone truncation,
\[
\frac{1-\psi(t)}{t}
=E\frac{1-e^{-t\ell}}t\to\infty
\quad(t\downarrow0).
\]
Since \(-\log x\ge1-x\), for every fixed \(\delta>0\) some sufficiently small \(t\) satisfies \(\delta[-\log\psi(t)]>t\), so \(I(\delta)>0\).

For the upper bound, the single northward edge is an irreducible bridge and has \(Q\)-mass \(\mu^{-1}\). Hence
\[
\psi(t)\ge\mu^{-1}e^{-t}
\]
and
\[
\delta[-\log\psi(t)]-t
\le\delta\log\mu-(1-\delta)t
\le\delta\log\mu.
\]
Finally \(\mu\le3\) on the square lattice because after the first step a self-avoiding walk has at most three choices at each further step. This proves (6.2).

## 7. R11-GH-C004 — branch-aware quantitative DCH bridge-rate compiler

**STATUS: PROVED CONDITIONAL REDUCTION.**

Fix \(v\in(0,1]\) and put
\[
K=\lceil2/v\rceil,
\qquad
m=K-1.
\]
DCH Proposition 3.2 starts from
\[
{\rm SAB}_{n,v}
\subseteq
{\rm SAB}^{K}_{n,v,v/2}.
\]
Choose arbitrary parameters \(z_1,\ldots,z_m\in(0,1/8]\). For each stage put
\[
L_j=\lceil1/z_j\rceil,
\qquad
h_j=H(4z_j),
\qquad
 d_j=\frac{z_j}{48L_j^2},
\]
and
\[
S_j=\sum_{i=1}^j h_i,
\quad S_0=0.
\]
Then the direct DCH maps plus C003 certify the bridge ballistic rate
\[
\boxed{
\liminf_{n\to\infty}
-\frac1n\log
\mathbb P_{{\rm SAB}_n}(y(\gamma_n)\ge vn)
\ge c_{\rm cert}(v;z_1,\ldots,z_m),
}
\tag{7.1}
\]
where
\[
\boxed{
 c_{\rm cert}
=
\min\left\{
 I(v/2)-S_m,
 \min_{1\le j\le m}\big(I(d_j)-S_{j-1}\big)
\right\}.
}
\tag{R11-GH-C004}
\]
A negative right side is simply a non-useful certificate, not a probability lower bound.

### Proof

Apply C002 stage by stage, decreasing the crossing-number bound from \(K\) toward 1, but do **not** replace all three branches by a common worst-case terminal set.

At stage \(j\):

- in **Case 1**, the process stops immediately in \({\rm SAB}^{1}\) with renewal density at least \(r_j\ge d_j\); only the previous Case-2 entropy losses \(S_{j-1}\) have been paid;
- in **Case 3**, it also stops immediately in \({\rm SAB}^{1}\) with renewal density at least \(d_j\); the MultiUnf step has an exponential gain, which may be discarded safely;
- only in **Case 2** is the entropy loss \(h_j\) paid and the reduction proceeds from \(k\) to \(k-1\), retaining the original density parameter \(v/2\).

If the process terminates at stage \(j\), C003 bounds the terminal renewal-dense bridge family at exponent \(I(d_j)\), leaving net exponent \(I(d_j)-S_{j-1}\). If all \(m\) stages take Case 2, one reaches crossing number 1 while retaining renewal density \(v/2\); the net exponent is \(I(v/2)-S_m\). Taking the least branch exponent proves (7.1).

Since \(I(\delta)>0\) for every fixed \(\delta>0\) and \(h(z)\to0\) as \(z\downarrow0\), one can choose the \(z_j\)'s backwards so that every branch margin is positive. Thus C004 gives a fully quantitative fixed-\(v\) bridge rate in terms of the exact renewal rate function \(I\). This recovers the qualitative fixed-speed exponential conclusion in a form suitable for diagnosing the small-\(v\) degeneration.

## 8. R11-GH-X002 — direct DCH constant tracking is at best doubly exponential in \(1/v\)

**STATUS: PROVED METHOD LIMITATION. This does not refute the SAW conjecture or the DCH theorem.**

Suppose a choice \(z_1,\ldots,z_m\) makes the C004 certificate strictly positive. Then for every \(j\ge2\),
\[
S_{j-1}<I(d_j).
\]
But
\[
S_{j-1}\ge h(z_{j-1}).
\]
For \(0<z\le1/8\),
\[
h(z)=H(4z)
\ge4z\log\frac1{4z}
\ge4z\log2
>2z.
\tag{8.1}
\]
On the other hand, by C003,
\[
I(d_j)\le d_j\log\mu<2d_j.
\]
Since \(L_j\ge1/z_j\),
\[
d_j=\frac{z_j}{48L_j^2}
\le\frac{z_j^3}{48}.
\]
Therefore positivity forces
\[
2z_{j-1}
<\frac{z_j^3}{24},
\qquad\text{hence}\qquad
\boxed{z_{j-1}<\frac{z_j^3}{48}.}
\tag{8.2}
\]
Iterating and using \(z_m\le1/8\),
\[
z_1\le8^{-3^{m-1}}
\]
(the omitted powers of 48 only make this smaller). Any positive certificate also obeys
\[
c_{\rm cert}
\le I(d_1)
\le\frac{z_1^3}{24},
\]
so
\[
\boxed{
 c_{\rm cert}(v;z_1,\ldots,z_m)
\le
\frac1{24}\,8^{-3^m},
\qquad
m=\lceil2/v\rceil-1.
}
\tag{R11-GH-X002}
\]

Thus the **unmodified worst-case branch compiler extracted from the published DCH three-case proof cannot certify a polynomial small-speed modulus**. Its best possible positive certificate under this parameterization is bounded above by a quantity doubly exponential in \(1/v\).

This is the central new diagnosis of the run. The prior missing estimate was written vaguely as “prove \(c(v)\ge c_0v^\kappa\).” The present analysis shows why direct constant tracking of the published maps cannot produce it. One must change at least one structural feature:

1. reduce the Case-2 inverse entropy cost \(H(4z)\asymp z\log(1/z)\) to a scale comparable to the terminal renewal density;
2. improve the Case-3 terminal renewal density from the present \(d(z)\asymp z^3\) scale;
3. batch many crossing-number reductions so an entropy cost is not paid at \(O(1/v)\) nested stages; or
4. replace this unfolding step by a different polygon-surgery / endpoint-redirection construction.

Even perfect knowledge of \(I(\delta)\) cannot by itself cure the nesting, because the elementary upper bound \(I(\delta)\le\delta\log\mu\) already forces (8.2).

### Bridge-to-walk transfer warning

The Hammersley--Welsh bridge/walk comparison costs \(e^{C\sqrt n}\). If a bridge estimate only gives
\[
\mathbb P_{{\rm SAB}_n}(R_n>vn)\lesssim e^{-c_0nv^\kappa},
\]
a naive transfer to walks at \(v=n^{-\eta}\) must beat the \(e^{C\sqrt n}\) overhead, requiring
\[
nv^\kappa\gg\sqrt n,
\qquad\text{i.e.}\qquad
\eta<\frac1{2\kappa}.
\]
Thus even a polynomial **bridge** modulus with exponent \(\kappa\) would need \(\kappa<2\) to reach \(\eta=1/4\) through this naive bridge-to-walk transfer. Improving the bridge modulus and improving the transfer are distinct obligations.

## 9. Independent R14 audit

**Audit ID: `R11-AUD-R14-C175-20260916`. Result: PASS for R14-C175; R14 remains PARTIAL/OPEN.**

Package audited:

- `runs/R14/2026-09-16T13-53-07Z_r14-c175-baseline.md`;
- `artifacts/R14/2026-09-16T13-53-07Z_r14-c175-baseline_checker.py`;
- archived checker output.

R14's normalization is the standard spherical perceptron one. At \(\kappa=-1\), Stojnic's rigorous upper-bound theorem uses
\[
f_{\rm gar}(-1)=\int_1^\infty(z-1)^2\phi(z)\,dz.
\]
Gaussian integration by parts gives
\[
\int_1^\infty z\phi(z)\,dz=\phi(1),
\]
\[
\int_1^\infty z^2\phi(z)\,dz=\bar\Phi(1)+\phi(1),
\]
so
\[
\boxed{f_{\rm gar}(-1)=2\bar\Phi(1)-\phi(1).}
\]
Therefore the rigorous UNSAT endpoint is
\[
\alpha_U=\frac1{2\bar\Phi(1)-\phi(1)}.
\]
The SAT endpoint \(\alpha_L=2\) is valid because \(\kappa=-1\) constraints are weaker than the classical zero-margin spherical constraints, whose threshold is 2. The archived exact-rational checker certifies
\[
13.273<\alpha_U<13.274
\]
and
\[
11.273<\alpha_U-2<11.274.
\]
I independently checked the theorem direction and the Gaussian integral identity. The package correctly labels the result PARTIAL and does not promote later lifted numerical/stationary values to rigorous capacity endpoints. **PASS.**

## 10. Exact self-check artifacts

Finite/algebraic claims are backed by an executed exact-arithmetic checker:

- `artifacts/R11/2026-09-16T14-40-03Z_saw-quantitative-renewal-trace-b7c2_checker.py`
- `artifacts/R11/2026-09-16T14-40-03Z_saw-quantitative-renewal-trace-b7c2_checker_output.txt`

The checker uses `fractions.Fraction` and certifies:

- `log(2)>1/2` and `log(3)<2` by exact rational exponential-series comparisons;
- all finite C002 parameter inequalities on 6,084 reduced rational \(z=p/q\in(0,1/8]\), \(q\le400\);
- the C003 floor/rounding lemma on 1,010,000 rational/integer cases;
- the X002 nested-threshold algebra for \(m=1,\ldots,6\).

Archived checker-output SHA-256:

`5d306a2b045edf8a5da4156c390c6aeab5881522b4faa40fd55e0b5bd170e8ae`.

The checker exits 0 and prints `PASS`. These exact finite checks certify only constants/algebra; they are not asymptotic SAW exponent evidence.

## 11. Failures, remaining obligation, next attack

### Failed route retained

The direct quantitative reading of DCH Proposition 3.2 is now diagnosed sharply:
\[
\boxed{
\text{the nested Case-2/Case-3 constants force a doubly-exponential worst-case rate in }1/v.
}
\]
Therefore another run should not merely tune \(z,r,s\) inside the same one-stage trichotomy.

### Precise remaining obligation

To move the tracked exponent below \(2\), one still needs a bound on the **original uniform walk law** strong enough to feed R11-GH-C001, or a different direct moment argument. The cleanest missing uniform estimate is
\[
\boxed{
\mathbb P_{\mathrm{SAW}_n}(R_n>vn)
\le
\exp\{-c_0nv^\kappa\}
\quad\text{for all sufficiently small }v,
}
\]
with finite \(\kappa\); reaching the target upper exponent \(3/2\) by C001 requires \(\kappa<4\) directly on walks.

For the bridge route, the Hammersley--Welsh transfer warning means a naive polynomial bridge modulus needs the stronger \(\kappa<2\) to reach \(3/2\).

### Simplest next special case

The next concrete target is the **single reduction \(k=2\to1\)**: replace the unfold-all-zigzags inverse count \(e^{H(4z)n}\) by a surgery whose logarithmic inverse multiplicity is \(O(z^3n)\), or prove a correspondingly larger terminal renewal density. This is the first place where the X002 recursion can be broken without yet solving the whole \(O(1/v)\)-stage problem.

A polygon-surgery version should be tested refute-first on exact finite bridges before any asymptotic claim.

R11 is not yet at the three-consecutive-no-movement stuck threshold; this is unchanged-count 1.

## 12. Ledger delta for P26

```yaml
ledger_delta:
  track: R11
  source:
    authors: [Paul J. Flory, Bernard Nienhuis]
    years: [1949, 1982]
    modern_rigorous_reference: arXiv:1205.0401
  target: "E||omega_n||_2^2 = n^(3/2+o(1)) for uniform n-step nearest-neighbor SAW on Z^2"
  metric: "smallest rigorously proved a with E||omega_n||_2^2 <= C n^a for all n>=n0, retaining C,n0 and original law"
  before:
    a: 2
    C: 1
    n0: 1
  after:
    a: 2
    C: 1
    n0: 1
  movement: "no movement"
  status: OPEN
  unchanged_count: 1
  exact_evidence:
    new_claims:
      - R11-GH-C002
      - R11-GH-C003
      - R11-GH-C004
      - R11-GH-X002
    checker: artifacts/R11/2026-09-16T14-40-03Z_saw-quantitative-renewal-trace-b7c2_checker.py
    checker_output: artifacts/R11/2026-09-16T14-40-03Z_saw-quantitative-renewal-trace-b7c2_checker_output.txt
    checker_sha256: 5d306a2b045edf8a5da4156c390c6aeab5881522b4faa40fd55e0b5bd170e8ae
  audit_ids:
    incoming:
      - R10-AUDIT-R11-C001-20260916
    outgoing:
      - R11-AUD-R14-C175-20260916
  remaining_obligation: "break the DCH nested entropy/renewal-density recursion and obtain a polynomial small-speed rate on the original SAW law, or a direct fixed-power moment bound"
```

## Primary references

- P. J. Flory, *The Configuration of Real Polymer Chains*, J. Chem. Phys. 17 (1949), 303--310, DOI 10.1063/1.1747243.
- B. Nienhuis, *Exact Critical Point and Critical Exponents of O(n) Models in Two Dimensions*, Phys. Rev. Lett. 49 (1982), 1062--1065, DOI 10.1103/PhysRevLett.49.1062.
- H. Duminil-Copin and A. Hammond, *Self-avoiding walk is sub-ballistic*, Commun. Math. Phys. 324 (2013), 401--423, arXiv:1205.0401.
- D. Krachun and C. Panagiotis, *Quantitative sub-ballisticity of self-avoiding walk on the hexagonal lattice*, Ann. Probab. 54 (2026), 1109--1125, DOI 10.1214/24-AOP1730.
