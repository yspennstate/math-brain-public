# ProofNet24 P23 — Kernel Obstruction Audit / Post-Closure Hard-Edge Assist

**Run timestamp:** 2026-09-15 16:27:00 Asia/Jerusalem  
**Canonical transport correction:** this complete report supersedes the same-run file `2026-09-15_16-27-00__run-report.md`, which is preserved immutably but contains a transport typo in the displayed coherent-state formula (`\nuu^T` instead of `uu^T`). No historical file was overwritten.  
**Track:** P23 — Gaussian-kernel obstruction audit  
**Scope:** P04 Target 3; after audit closure, assist unresolved kernel/RMT tracks. NO number theory.  
**Delivery:** GitHub-only. No email/Gmail action used.  
**Runtime model / effort:** runtime metadata exposes GPT-5.6 Sol. The requested GPT-6 / maximum-reasoning selector is not an exposed run control, so no GPT-6 switch, hidden agent, or unverified effort setting is claimed.

## 0. Executive state

The original P04 Target 3 remains **PROVED / AUDIT-CLOSED**. For iid `X_i ~ Unif(S^{d-1})`, `n=2^d`, zero signal, independent Gaussian training noise variance `sigma^2`, and fixed-bandwidth Gaussian kernel

```text
K_h(x,y) = exp(-||x-y||^2/(2 h^2)),
```

the audited one-window theorem gives

```text
liminf_d E_training[ExcessRisk]/sigma^2 >= 5/36.
```

The stronger P23 ten-window strengthening remains

```text
liminf_d E_training[ExcessRisk]/sigma^2
  >= 3882594969529/12500000000000
  = 0.31060759756232.
```

No Target-3 dependency is reopened. Per the shared protocol, substantive work after closure assists the still-open P04 Target 4 / P20 quadratic hard edge.

The new theorem of this run is:

## `P23-T4-PAIR-024-SUMRULE-26` — PROVED

Let

```text
V = Sym_d^0,
m = (d-1)(d+2)/2,
h(u) = sqrt(d(d+2)/2) * (u u^T - I/d).
```

Let `K_2(u,v)=<h(u),h(v)>_F` be the physical degree-two projector kernel, `K_4` the physical degree-four projector kernel, and `K_0=1`.

Fix any deterministic rank-s coefficient projection `P`, `s>=2`, with Frobenius-orthonormal basis `A_1,...,A_s`. Define

```text
f_a(u) = <h(u),A_a>_F,
F_P(u) = sum_a f_a(u)^2,
K_P(u,v) = sum_a f_a(u) f_a(v),
C(P) = sum_a A_a^2,
Acal(P) = tr(C(P)^2),
R(P) = sum_{a,b} tr(A_a A_b A_a A_b),
delta(P) = Acal(P)-R(P)
         = (1/2) sum_{a,b} ||[A_a,A_b]||_F^2,
e(P) = Acal(P)-s^2/d,
alpha_d = d(d+2)/[(d+4)(d+6)],
beta_d = 8 d(d+2)/(d+4)^2.
```

If `U,V` are two distinct labeled points from the rank-s projection DPP with kernel `K_P`, then

```text
E[K_2(U,V) | P]
 = beta_d/[2s(s-1)] * [ delta(P) - 2s(s-1)/d ],
```

and the new identity is

```text
E[K_4(U,V) | P]
 = -1
   + beta_d/[2s(s-1)] * [ 2s(s-1)/d - delta(P) ].
```

Therefore

```text
E[K_0(U,V)+K_2(U,V)+K_4(U,V) | P] = 0.
```

Both projector-kernel pair overlaps are exactly independent of the Jordan defect `e(P)`. More generally, for every linear zonal low-even pair kernel

```text
L = a_0 K_0 + a_2 K_2 + a_4 K_4,
```

one has

```text
E[L(U,V)|P]
 = a_0-a_4
   + (a_2-a_4) beta_d/[2s(s-1)]
     * [delta(P)-2s(s-1)/d].
```

Thus the full linear physical zonal sector `span{K_0,K_2,K_4}` collapses to the single commutator coordinate `delta(P)` and contains no pair information about `e(P)`.

A second new result is an exact finite-dimensional witness:

## `P23-T4-LOW-SECTOR-NONIDENTIFIABILITY-26` — PROVED

In `d=4`, identify diagonal traceless matrices with

```text
H = { x in R^4 : sum_i x_i = 0 }.
```

For a unit `n in H`, let `P_n = H intersect n^perp`, a rank-two diagonal plane. All its matrices commute, hence `delta(P_n)=0`.

The diagonal entries of `C(P_n)` are

```text
ell_i = 3/4 - n_i^2,
```

so

```text
e(P_n) = sum_i ell_i^2 - 1.
```

For

```text
n^(0) = (1,1,-1,-1)/2,
```

all `ell_i=1/2` and `e(P_n0)=0`.

For

```text
n^(1) = (1,-1,0,0)/sqrt(2),
```

`ell=(1/4,1/4,3/4,3/4)` and `e(P_n1)=1/4`.

Yet both have `delta=0`. Since `beta_4=3` and `s=2`, both ordinary DPP pair laws satisfy

```text
E[K_2|P] = -3/4,
E[K_4|P] = -1/4.
```

By contrast, two conditionally independent replicas from the one-point density `q_P=F_P/2` satisfy

```text
E_replica[K_2|P] = (3/4) e(P),
```

so the two planes give `0` and `3/16`. Ordinary low-even DPP pair data therefore fail to identify the Jordan defect even pointwise.

---

## 1. Canonical evidence read

### Shared protocol

Read from `master`:

- `README.md`, blob `9d18531dff608e0165fe4434614d8c9121903c4c`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, blob `a5773ae98d59ab7d6420f809452c3b20565c3379`.

These make GitHub the canonical archive, disable research email, require a complete immutable run report, require readback after commit, and require an independently reasoned peer-lemma audit.

### Latest canonical P23

Read:

`proofnet24/P23-kernel-obstruction/runs/2026-09-15/2026-09-15_15-25-08__run-report__transport-correction.md`

- creation commit `452092afd52246c5fd04b880e72418aa6b8e7834`;
- blob `60424525d5130bb221a43f45fb1920d7337fcc21`.

Retained claims include:

- `P23-T4-DPP-PAIR-JORDAN-BLINDNESS-25`;
- `P23-T4-REPLICA-JORDAN-OVERLAP-25`;
- `P23-T4-TRIPLE-KERNEL-JORDAN-25`;
- `P23-T4-REPLICA-COFACTOR-25`;
- `P23-T4-CROSS-COFACTOR-REDUCTION-25`.

The cross-cofactor identity remains correct. Its earlier interpretation as an irreducible inverse-volume singularity is superseded by P26's polynomialization below.

### Latest complete P04

Read:

`proofnet24/P04-kernel-conjectures/runs/2026-09-15/2026-09-15_15-47-58__run-report.md`

- creation commit `60ecfb92a21cf8e22230180dd258f5c24c0a4d91`;
- blob `50b4f41f80b08090d9f5ee36bb2be47ca9f10690`.

Its ledger has Target 3 audit-closed and Target 4 open. Relevant new claim: `P04-T4-POINTWISE-024-SECTOR-37`, the deterministic pointwise physical 0/2/4 conditional-intensity decomposition.

### Kernel/RMT peer A — P22

Read:

`proofnet24/P22-kernel-benign/runs/2026-09-15/2026-09-15_15-23-56__run-report.md`

- creation commit `faa7df619d5388c5448e1cc1e5f7ca855252053c`;
- blob `0bc84e9157c2a28c569fdbc97fe0b2e57f284764`;
- audited claim: `P22-T4-EXACT-04-SECTOR-BALANCE-28`.

### Kernel/RMT peer B — P26

Read:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-15/2026-09-15_15-58-44__run-report.md`

- creation commit `ae23b478a83de58b2ca52ea5624ffe98935b61d2`;
- blob `d6b2a32a14b26b7a25ab4b560b795e4ec739db62`;
- relevant claims `P26-T4-DEG2-DELETION-MARTINGALE-05` and `P26-T4-CROSS-COFACTOR-POLYNOMIALIZATION-05`.

P26 proves pointwise

```text
C_uv = D h(u)^T P_2 h(v),
C_uv^2/D = D [h(u)^T P_2 h(v)]^2.
```

Thus the P23 cross-cofactor identity is retained, but the interpretation that its difficulty is an uncancelled `D^{-1}` tail is **DISPROVED / SUPERSEDED**. The real difficulty is the volume-biased residual-plane Jordan statistic.

---

## 2. Target-3 reduction retained

With Gaussian-kernel harmonic blocks

```text
K_s = lambda_s Phi_s Phi_s^T,
t_s = Tr(K^{-1} K_s),
q_s = Tr(K^{-1} K_s K^{-1}),
```

and multiplicities `N_s`, one has exactly

```text
V(X)/sigma^2 = sum_s lambda_s q_s.
```

Spherical addition gives

```text
||Phi_s||_F^2 = n N_s,
```

and Hilbert-Schmidt Cauchy gives

```text
t_s^2 <= n N_s lambda_s q_s.
```

For a finite deterministic window `B`, with

```text
D_B = sum_{s in B} N_s,
T_B = sum_{s in B} t_s,
```

weighted Cauchy gives

```text
V(X)/sigma^2 >= T_B^2/(n D_B).
```

This is a reduction only. The expected-leverage bridge and the original Target-3 implication chain are already independently audited and closed. No high-probability statement is substituted for the expectation target.

---

## 3. Primary-source Gaussian Mercer check

For fixed `h`, write `a=h^{-2}`. The exact spherical Gaussian-kernel Mercer eigenvalue is

```text
lambda_{d,s}
 = exp(-a) Gamma(d/2) (2/a)^(d/2-1) I_{s+d/2-1}(a).
```

NIST DLMF 10.25.2 was refreshed this run:

`https://dlmf.nist.gov/10.25.E2`.

It states

```text
I_nu(z)
 = (z/2)^nu sum_{k>=0} (z^2/4)^k/[k! Gamma(nu+k+1)].
```

For positive `a`, all terms are positive, yielding the retained adjacent-degree bound

```text
lambda_{d,s+1}/lambda_{d,s} <= a/(d+2s).
```

No special-function asymptotic is reconstructed from memory.

---

## 4. Fourth spherical product identity

For `A in V`, set

```text
f_A(u) = <h(u),A>_F = c_d u^T A u.
```

Let `g=R u ~ N(0,I_d)`, with `R` independent of `u`. For traceless symmetric `A,B`, write `Q_A=g^T A g`, `Q_B=g^T B g`.

The centered Gaussian quadratic-form cumulants give

```text
E[Q_A^2 Q_B^2]
 = 4 tr(A^2) tr(B^2)
   + 8 tr(AB)^2
   + 32 tr(A^2 B^2)
   + 16 tr(ABAB).
```

Also

```text
E R^8 = d(d+2)(d+4)(d+6),
c_d^4 = d^2(d+2)^2/4.
```

Therefore

```text
int f_A(u)^2 f_B(u)^2 dmu(u)
 = alpha_d [
     tr(A^2) tr(B^2)
     + 2 tr(AB)^2
     + 8 tr(A^2 B^2)
     + 4 tr(ABAB)
   ].
```

For an orthonormal basis `A_1,...,A_s`, summing gives

```text
sum_{a,b} ||f_a f_b||_2^2
 = alpha_d [ s^2 + 2s + 8 Acal(P) + 4 R(P) ].
```

This is the total physical 0/2/4 product energy.

---

## 5. Degree-zero and degree-two product energies

Because

```text
int f_a f_b dmu = delta_ab,
```

the total degree-zero product energy is

```text
S_0 = sum_{a,b} ||Pi_0(f_a f_b)||_2^2 = s.
```

The polarized degree-two product formula is

```text
Pi_2(f_A f_B)(u)
 = (gamma_d/2)
   < h(u), AB+BA - [2 tr(AB)/d] I >_F,
```

with `gamma_d^2=beta_d`.

For symmetric `A,B`,

```text
||AB+BA||_F^2
 = 2 tr(A^2 B^2) + 2 tr(ABAB).
```

Therefore

```text
S_2
 = sum_{a,b} ||Pi_2(f_a f_b)||_2^2
 = (beta_d/2) [ Acal(P)+R(P)-2s/d ].
```

Since products of physical degree-two harmonics contain only degrees 0, 2 and 4,

```text
S_4
 = alpha_d [s^2+2s+8 Acal+4 R]
   - s
   - (beta_d/2)[Acal+R-2s/d].
```

---

## 6. Degree-four part of the Christoffel intensity

Recall

```text
F_P = sum_a f_a^2.
```

Its total square norm is

```text
||F_P||_2^2
 = alpha_d [s^2+2s+8 Acal+4 R].
```

Its mean is `s`, hence

```text
||Pi_0 F_P||_2^2 = s^2.
```

The degree-two projection is

```text
Pi_2 F_P(u)
 = gamma_d <h(u), C(P)-(s/d)I>_F,
```

so

```text
||Pi_2 F_P||_2^2
 = beta_d [Acal(P)-s^2/d]
 = beta_d e(P).
```

Therefore

```text
||Pi_4 F_P||_2^2
 = alpha_d [s^2+2s+8 Acal+4 R]
   - s^2
   - beta_d e.
```

Dividing by `s^2`, since `q_P=F_P/s`, independently recovers P04's pointwise physical degree-four intensity identity.

---

## 7. Proof of the new ordinary-pair degree-four identity

The labeled pair density is

```text
p_{2,P}(u,v)
 = [F_P(u)F_P(v)-K_P(u,v)^2]/[s(s-1)].
```

Because `K_4` is an orthogonal projector kernel,

```text
intint K_4(u,v) F_P(u)F_P(v) dmu(u)dmu(v)
 = ||Pi_4 F_P||_2^2.
```

Also

```text
K_P(u,v)^2
 = sum_{a,b} f_a(u)f_b(u) f_a(v)f_b(v),
```

hence

```text
intint K_4(u,v) K_P(u,v)^2 dmu(u)dmu(v)
 = S_4.
```

Thus

```text
E[K_4(U,V)|P]
 = [||Pi_4 F_P||_2^2-S_4]/[s(s-1)].
```

Subtracting the formulas above gives

```text
||Pi_4 F_P||_2^2-S_4
 = -s^2+s-beta_d e
   + (beta_d/2)[Acal+R-2s/d].
```

Since

```text
Acal = s^2/d + e,
R = Acal-delta,
```

one has

```text
Acal+R-2s/d-2e
 = 2s(s-1)/d - delta.
```

Therefore

```text
E[K_4(U,V)|P]
 = -1
   + beta_d/[2s(s-1)]
     * [2s(s-1)/d-delta(P)].
```

Adding the previously proved `K_2` formula yields

```text
E[K_2+K_4|P] = -1,
```

and with `K_0=1`,

```text
E[K_0+K_2+K_4|P] = 0.
```

QED.

---

## 8. Actual residual-DPP consequence

For the actual residual rank-s harmonic DPP, the exact commutator mean is

```text
E delta(P_s) = d s(s-1)/[2(m-1)].
```

Hence the degree-two ordinary-pair overlap is rank-independent:

```text
E K_2(U,V)
 = theta_d
 = -4(d-2)(d+2)/[(d+4)(d^2+d-4)].
```

The new sum rule gives

```text
E K_4(U,V) = -1-theta_d,
```

again independent of residual rank `s>=2`.

Thus the two low-even projector-kernel pair moments cannot infer the rank-dependent Jordan energy `e_s`.

---

## 9. Exact d=4 witness

For the diagonal rank-two planes `P_n` described in the executive section,

```text
n^(0)=(1,1,-1,-1)/2:
  delta=0,
  e=0;

n^(1)=(1,-1,0,0)/sqrt(2):
  delta=0,
  e=1/4.
```

Both ordinary pair laws have

```text
(E K_2, E K_4)=(-3/4,-1/4),
```

while the independent-replica `K_2` overlaps are

```text
0,
3/16.
```

This is a finite exact nonidentifiability counterexample.

---

## 10. Independent peer audit

### `P23-AUDIT-P22-EXACT-04-SECTOR-26`

**AUDIT_FOR:** P22 kernel/RMT hard-edge assistance  
**Source path:** `proofnet24/P22-kernel-benign/runs/2026-09-15/2026-09-15_15-23-56__run-report.md`  
**Source creation commit:** `faa7df619d5388c5448e1cc1e5f7ca855252053c`  
**Source blob SHA:** `0bc84e9157c2a28c569fdbc97fe0b2e57f284764`  
**Claim ID:** `P22-T4-EXACT-04-SECTOR-BALANCE-28`  
**Verdict:** **PROVED / PASS.**

P22 claims

```text
E ||Pi_4(q_{P_s}-1)||_2^2
 = B_s + [d/(2(d+6))] E_{2,s},
```

where

```text
E_{2,s}=E||Pi_2(q_{P_s}-1)||_2^2,
B_s=[2d/(d+6)] * [(m-s)/(s(m-1))].
```

From the independent derivation above,

```text
||Pi_4(q_P-1)||_2^2
 = (4 alpha_d/s^2) [
     s(d+2s+2)/(2(d+2))
     - delta(P)
     + [d/(d+4)] e(P)
   ].
```

For the actual residual law,

```text
E delta(P_s) = d s(s-1)/[2(m-1)],
E_{2,s} = (beta_d/s^2) e_s.
```

The `e_s` coefficient satisfies exactly

```text
4 alpha_d d/[s^2(d+4)]
 = [d/(2(d+6))] * beta_d/s^2.
```

The remaining baseline simplifies exactly to

```text
(4 alpha_d/s^2) [
  s(d+2s+2)/(2(d+2))
  - d s(s-1)/(2(m-1))
]
 = [2d/(d+6)] * [(m-s)/(s(m-1))]
 = B_s.
```

Thus the P22 theorem is exact. No independence approximation or iid-coordinate surrogate is used.

Verdict:

```text
P22-T4-EXACT-04-SECTOR-BALANCE-28: PASS.
```

The audit also independently reproduces P04's newer pointwise degree-four formula.

---

## 11. Exact low-dimensional regression checks

### d=2 circle

For `d=2`, `m=2`, on `S^1` one may take

```text
K_2(theta,phi)=2 cos(2(theta-phi)),
K_4(theta,phi)=2 cos(4(theta-phi)).
```

For the full rank-two DPP, `F=2`, and the labeled pair density is

```text
p_2(theta,phi)=1-cos(4(theta-phi)).
```

Exact Fourier integration gives

```text
E K_2=0,
E K_4=-1,
E(K_0+K_2+K_4)=0.
```

PASS.

### Symbolic algebra

Exact symbolic simplification verifies

```text
S_0+S_2+S_4
 = alpha_d [s^2+2s+8 Acal+4 R]
```

and

```text
E[K_2|P]+E[K_4|P]=-1
```

identically in symbolic variables `(d,s,delta,e)`.

PASS.

### d=4 witness

Exact arithmetic gives

```text
(delta,e)=(0,0)
and
(delta,e)=(0,1/4)
```

for the two diagonal planes, while both have

```text
(EK_2,EK_4)=(-3/4,-1/4).
```

Replica overlaps are `0` and `3/16`.

PASS.

These are regression checks only; the analytic derivations are the proofs.

---

## 12. Correction to the previous cross-cofactor route

The prior P23 identity

```text
beta_d e_2
 = 2 theta_d
   + (1/M) E[ K_2(u,v) C_uv^2/D ]
```

remains correct.

P26 proves

```text
C_uv = D h(u)^T P_2 h(v),
```

so

```text
C_uv^2/D = D [h(u)^T P_2 h(v)]^2.
```

Therefore the prior statement that the remaining obstacle is an irreducible inverse-determinant tail is **DISPROVED / SUPERSEDED**. The remaining object is a polynomial triple-kernel/Jordan statistic under the volume-biased residual-plane law.

---

## 13. Route implications

The new theorem rules out:

1. ordinary degree-two projector-kernel pair moments as a Jordan probe;
2. ordinary degree-four projector-kernel pair moments as a repair;
3. every linear low-even zonal pair probe in `span{K_0,K_2,K_4}`.

The exact `d=4` witness shows this is genuine nonidentifiability, not merely cancellation after averaging over the actual residual law.

Objects that still retain the Jordan defect include:

- conditionally independent replicas from `q_P`;
- the physical degree-two Christoffel energy `||Pi_2(q_P-1)||_2^2`;
- P26's degree-two deletion-martingale innovation budget;
- the polynomialized triple-kernel/cofactor statistic.

The preferred next attack should therefore be replica, innovation, or genuine three-point, not another ordinary low-sector pair moment.

---

## 14. Cumulative ledger

### PROVED / AUDIT-CLOSED

Original P04 Target 3:

```text
liminf_d E_training[ExcessRisk]/sigma^2 >= 5/36.
```

### PROVED — stronger P23 Target-3 strengthening

```text
liminf_d E_training[ExcessRisk]/sigma^2 >= 0.31060759756232.
```

### PROVED — inherited hard-edge structure

- exact pure degree-two feature/traceless-symmetric isometry;
- exact residual projection-DPP representation;
- exact commutator mean;
- Jordan matrix martingale;
- likelihood-information bridge;
- P04 Christoffel/Jordan degree-two identity;
- P04/P22 physical 0/2/4 sector decomposition;
- P23 ordinary degree-two pair Jordan blindness;
- P23 replica Jordan overlap;
- P23 triple-kernel degree-two identity;
- P23 cofactor identities;
- P26 degree-two deletion martingale;
- P26 cross-cofactor polynomialization.

### PROVED — new this run

- `P23-T4-PAIR-024-SUMRULE-26`;
- `P23-T4-LOW-SECTOR-PAIR-BLINDNESS-26`;
- `P23-T4-LOW-SECTOR-NONIDENTIFIABILITY-26`;
- `P23-AUDIT-P22-EXACT-04-SECTOR-26` — PASS.

### CONDITIONAL

None added this run.

### DISPROVED / REJECTED

- ordinary `K_2` pair overlap can control the rank-two Jordan defect;
- adding ordinary `K_4` pair overlap repairs that blindness;
- the whole linear physical 0/2/4 zonal ordinary-pair sector identifies `e(P)`;
- static physical invariance plus exterior moments determine the hard-edge endpoint;
- first-moment deletion identities alone force the endpoint;
- telescoping the existing Jordan recurrence with the scalar information bridge produces new contraction;
- the P23 cross-cofactor remainder contains an irreducible inverse-determinant singularity;
- bulk Marchenko-Pastur or ordinary local laws automatically imply the fixed-t hard edge;
- adaptive harmonic coefficient coordinates may be replaced by iid surrogates.

### OPEN

Immediate angular endpoint:

```text
e_2 = O(1/d).
```

Equivalent repository formulations include

```text
E ||Pi_2(q_{P_2}-1)||_2^2 = O(1/d),
```

the P20 Hodge/Jordan quotient, and the P26 degree-two innovation-budget estimate.

Even after this angular endpoint, the full fixed-t hard-edge universality statement still has downstream ordinary-law/radial-transfer and least-singular-value obligations.

---

## 15. Failed-route ledger

### Target 3

- finite-window reduction alone proves leverage — FALSE;
- high-probability leverage is required for the expectation target — FALSE;
- Frobenius concentration is necessary for the source obstruction — FALSE;
- hard-edge universality or MP is necessary for Target 3 — FALSE.

### Target 4

- static isotropy determines the endpoint — FALSE;
- exact exterior design determines the endpoint — FALSE;
- first-moment DPP deletion identities determine the endpoint — FALSE;
- ordinary degree-two pair moments identify Jordan energy — FALSE;
- ordinary degree-four pair moments repair degree-two blindness — FALSE;
- all linear 0/2/4 zonal ordinary-pair moments identify Jordan energy — FALSE;
- the Jordan recurrence plus information bridge hides extra contraction after telescoping — FALSE;
- the cross-cofactor obstacle is fundamentally an uncancelled inverse-volume tail — FALSE after P26 polynomialization.

---

## 16. Next concrete attack

The highest-value next theorem is to control P26's exact degree-two reverse-martingale innovation budget

```text
(beta_d e_2)/4
 = sum_{t=3}^m E[V_t(P_t)]/(t-1)^2.
```

The current run proves that ordinary projector-kernel pair moments through physical degree four cannot control this budget.

Proposed next claim:

`P23-T4-INNOVATION-THREEPOINT-27`.

Express `V_s(P)` as an exact positive three-point or two-replica functional under the actual residual harmonic DPP and seek a summable bound sufficient for `e_2=O(1/d)`. Do not replace adaptive harmonic deletion directions by iid sphere vectors.

A second route is the polynomialized triple-kernel statistic

```text
E_{Q_2} intint K_2(u,v) K_{P_2}(u,v)^2 dmu(u)dmu(v),
```

which now has no inverse-determinant singularity after exact cofactor factorization.

---

## Bottom line

The Gaussian-kernel logarithmic-dimension obstruction remains audit-closed, with the stronger P23 constant `0.31060759756232`.

After closure, this run advances the unresolved hard-edge program by proving the exact sum rule

```text
E[K_0(U,V)+K_2(U,V)+K_4(U,V) | P] = 0
```

for every deterministic residual coefficient projection of rank at least two.

Consequently, every linear ordinary-pair observable in the physical zonal 0/2/4 sector depends only on commutator energy and is blind to the Jordan defect.

An exact `d=4` counterexample gives two rank-two residual planes with identical ordinary 0/2/4 pair data but Jordan energies `0` and `1/4`.

Therefore the live hard-edge endpoint cannot be solved by adding more ordinary low-sector pair moments. The next useful objects are the degree-two deletion innovation, conditional replicas, or genuinely three-point polynomial statistics.
