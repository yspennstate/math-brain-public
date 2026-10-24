# FOREST / account01 B20 — all-triple Simpson tensor and a positive-compensation energy cap

**Run:** `20260922T082137Z-account01-B20-forest-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Candidate:** `FOREST-MINIMAL-GRAPHIC-SIGNED-ENERGY-v1`  
**Parent target:** OPEN  
**Context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Source target and freshness boundary

The source target is unchanged: for every finite simple graph `G`, if `F` is uniform over **all** acyclic edge subsets (empty forest and disconnected forests included, every size allowed, unit physical-edge weights), prove for distinct present edges `e,f`

`P(e,f in F) <= P(e in F) P(f in F)`.

Equivalently the covariance `C_ef=Cov(X_e,X_f)` is nonpositive.

The active owner directive is `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`, owner-control revision `2026-09-22.2`. No brain-installation or benchmark work is performed here.

The newest complete campaign-lead report consumed is account01/B01 `20260922T080733Z-b01-forest-auto11`, report blob `7eccff21a034648951b1a5886db0330b60c3a5da`, candidate `FOREST-CERTIFIED-CONTRACTION-STAR2-v2`. Its STAR-2 representation, physical-mark bookkeeping, component likelihood-ratio formula and exact activity-2 gadget are useful. However its repeated use of a **rank-degree** completely-log-concave homogenization is not accepted: account01/B02 `20260922T054825Z-b02-forest-auto11`, report blob `7b500e2bc01d8788d526de9db984f52d6abe5d65`, gives an exact `K3` counterexample to that rank-degree log-concavity assertion. The source-valid homogenization has ground-set degree `m`, not graphic rank `R`.

The named OTHER-account result consumed and applied is the assigned partner account04/B03 `20260922T070756Z-B03-forest-r12-34330b0f`, report blob `a09681b45ae7e7e2d470fb5a2cdcd23c5c51fa38`. It proves the source-equivalent loopless-multigraph minimal-counterexample reduction, all-conditioner Simpson inequality, positive-pair matching geometry, the correct ground-set CLC budget, and the occupancy floor. This supersedes the lead's remaining STAR-2 induction debt without invoking a fixed-graph weighted-Cocks theorem.

I also use the exact path-cut transport identities T1--T5 from account04/B02 `20260922T011134Z-account04-B02-forest-r11`, report blob `70dd12f1c272a763642737810ecf5505b9f9438f`, together with its later `20260922T070653Z-account04-B02-forest-exchange-v4`, blob `536a2157ede22dbddcafeb4f1b28b308ac8222ff`, which refutes every union/intersection-preserving Hall coupling already on `K4`. Thus the next transport mechanism must genuinely cross multiplicity/union fibers.

## 2. Correct inherited minimal-counterexample frame

Assume the simple-graph source theorem is false. By the account04/B03 path-bundle equivalence one may choose a counterexample `M` with the minimum number `m` of **labelled physical edges** among finite loopless multigraphs. Fix a violating pair `e,f` and write

- `p_i=E X_i`, `v_i=p_i(1-p_i)`;
- `C_ij=Cov(X_i,X_j)`;
- `rho_ij=C_ij/sqrt(v_i v_j)`;
- `a=rho_ef>0`;
- `K=|F|`, `mu=E K`, `L=m-mu`;
- `c_i=Cov(X_i,K)`.

Every physical edge satisfies `0<p_i<=1/2`, by the usual deletion injection.

For every third edge `g`, deletion and contraction (after discarding contraction-created loops) are smaller loopless-multigraph instances. Hence the two conditional covariances of `e,f` given `X_g=0,1` are nonpositive. The exact total-covariance identity gives

`C_eg C_fg >= C_ef v_g`,

or

`rho_eg rho_fg >= a`.

The partner further proves that positive-covariance pairs form a matching. Consequently, for the selected positive pair `e,f`, every third edge `g` satisfies

`rho_eg<0`, `rho_fg<0`.

Write

`x_g=-rho_eg>0`, `y_g=-rho_fg>0`.

Then

`x_g y_g >= a` for all `g notin {e,f}`.                 (S)

The correct ground-set-degree completely-log-concave row inequality is

`T_i + sum_{h!=i}(1-p_h) rho_ih^2 <= p_i`,               (CLC)

where

`T_i=c_i^2/(L v_i)`.

No rank-degree replacement is used in this report.

## 3. New theorem A — the complete all-triple Simpson tensor

The preceding Simpson implication is not special to the selected positive pair.

### Theorem A

For **every three distinct physical edges** `i,j,k` of the minimal counterexample,

`boxed: rho_ij <= rho_ik rho_jk.`                         (T)

### Proof

Conditioning on `X_k=0` gives the uniform independent-set law of the smaller deletion minor. Conditioning on `X_k=1`, then removing the compulsory `k`, gives the smaller contraction minor after loops are discarded. By edge minimality, in both conditional laws the pair `(i,j)` is nonpositively correlated. Therefore

`C_ij
 = E[ Cov(X_i,X_j | X_k) ]
   + Cov(E[X_i|X_k],E[X_j|X_k])
 <= Cov(E[X_i|X_k],E[X_j|X_k]).`

For a Bernoulli conditioner,

`Cov(E[X_i|X_k],E[X_j|X_k]) = C_ik C_jk/v_k`.

Divide by `sqrt(v_i v_j)` to obtain (T). QED.

### Immediate geometric consequences

For the fixed positive pair `(e,f)`, (T) recovers (S). It also gives the two-sided ratio controls

`x_g >= a y_g`, `y_g >= a x_g`,

hence

`a <= x_g/y_g <= 1/a`.

More generally, if a second positive pair `{g,h}` has `b=rho_gh>0`, then applying (T) with conditioner `e` and with conditioner `f` gives

`boxed: b <= x_g x_h,  b <= y_g y_h.`                    (PPAIR)

This is a global compatibility relation that the previous local three-edge witnesses did not impose simultaneously across every positive matched pair.

## 4. New theorem B — positive third-third correlation has a finite energy budget

Let `U=E(M)\{e,f}`, `N=|U|=m-2`, and let

`P_+ = sum_{ {g,h} subset U : rho_gh>0 } rho_gh`.

The positive pairs in this sum are vertex-disjoint because the positive-covariance graph is a matching.

Put

`p=p_e+p_f`, `T=T_e+T_f`,

and define the available third-edge CLC energy

`E_* = p - T - (2-p)a^2.`

Adding (CLC) for `e` and `f` gives the exact inequality

`T + (2-p)a^2 + sum_{g in U}(1-p_g)(x_g^2+y_g^2) <= p`.

Thus `E_*>=0`. Since every `p_g<=1/2`,

`(1/2) sum_{g in U}(x_g^2+y_g^2) <= E_*`.               (E1)

Now take one positive pair `{g,h}` in `U`, with `b=rho_gh>0`. By (PPAIR),

`2b <= x_g x_h + y_g y_h
    <= (x_g^2+x_h^2+y_g^2+y_h^2)/2`.

Summing over the disjoint positive matching and using (E1) gives

`boxed: P_+ <= E_*/2.`                                   (E2)

This is the new paid step. It does not merely say that positive third-third correlations form a matching: it bounds their **total available mass** by the same ground-set CLC energy already spent by the marked pair.

If

`tau = 2 sum_{g<h, g,h in U} rho_gh`,

then all negative third-third correlations only decrease `tau`, so (E2) yields

`boxed: tau <= E_*.`                                     (E3)

This is a source-safe signed-compensation cap. It uses only the source-equivalent minimal multigraph frame, exact total covariance, positive-pair matching, ordinary AM--GM and the correct ground-set CLC inequality.

## 5. New theorem C — a scalar spectral consequence

Let

`A=sum_{g in U}(x_g+y_g)`.

From (S), `x_g+y_g>=2 sqrt(a)`, hence

`A>=2N sqrt(a)`.                                         (L)

The ordinary Pearson correlation matrix is positive semidefinite. Test it on the vector having equal value `t` in the `e,f` coordinates and value `1` on every coordinate in `U`. The resulting quadratic is

`2(1+a)t^2 - 2A t + N + tau >=0`

for all real `t`. Therefore

`A^2 <= 2(1+a)(N+tau)`.                                  (R)

Combining (L), (R), and (E3) gives the new necessary condition

`boxed: 2 N^2 a <= (1+a)(N+E_*).`                        (SC)

Since `p<=1`, `T>=0`, and `2-p>=1`, one has `E_*<=1-a^2`; therefore every such minimal counterexample also obeys

`a^3+a^2+(2N^2-N-1)a-(N+1) <=0`.                         (SC0)

The universal scalar relaxation (SC0) is **not claimed to improve every earlier scalar cap**. The substantive gain is (E2): it identifies and quantitatively limits the only positive third-third compensation that can rescue the PSD block. This is directly usable by the surviving cross-fiber transport route.

## 6. New theorem D — global graphic structure forced by the same tensor

The minimal counterexample matroid is connected. If some physical edge `g` belonged to a different direct-sum component from `e`, then `X_e` and `X_g` would be independent, giving `C_eg=0`, contradicting the strict negativity forced above for every third edge. Thus all physical edges lie in the same matroid component.

There is also no third physical edge that is a parallel or series clone of an endpoint of a positive pair. For example, if `g != e,f` is parallel to `e`, transposing the two labelled parallel copies is a matroid automorphism, so

`C_gf=C_ef>0`,

contradicting the matching theorem. If `g` is series to `e`, the same statement follows in the dual: a series pair in `M` is a parallel pair in `M*`, so their transposition is again a matroid automorphism of `M`. Hence `C_gf=C_ef>0`, again impossible.

Therefore each endpoint of the violating pair has no **third** parallel or series mate. In graphic language, the positive pair cannot be accompanied by a labelled parallel clone at either mark, nor by a third edge in a 2-edge cocircuit with either mark. This is a genuine graphic constraint unavailable in a generic correlation-matrix model.

## 7. Integration with the exact transport route

The account04/B02 T1--T5 path-cut identities remain valid verbatim for the loopless labelled multigraph frame: unique paths in forests still exist, and cut capacities count physical labels with multiplicity. Its later `K4` theorem proves that neither one-way transfer nor any union/intersection-preserving recoloring can satisfy the needed Hall condition universally. Therefore this run does not return to that refuted support.

The new signed-energy theorem provides a precise quantitative interface for a surviving cross-fiber proof. Any external-edge cut/join, alternating-exchange, or defect-routing theorem that turns failure of the residual product inequality into

`P_+ > E_*/2`

would immediately contradict (E2). More generally it is enough to force

`tau > E_*`,

contradicting (E3).

Thus the first unpaid universal implication is now sharply stated:

> **GRAPHIC DEFECT-TO-POSITIVE-MASS STEP.** In the exact residual `A00 x D` path-cut network, show that a Hall/flow deficit for a multiplicity-changing support forces positive third-edge correlation mass exceeding the CLC budget `E_*/2` (or an equivalent violation of (SC)).

This step must genuinely use graphic path/cut structure; abstract PSD+CLC+three-variable inequalities alone admit synthetic correlation matrices with the same sign pattern.

## 8. Exact algebra audit

The theorem is algebraic and does not depend on finite graph enumeration. I nevertheless ran `signed_energy_checker.py` as an exact symbolic regression. Captured output:

```text
FOREST_SIGNED_ENERGY_CHECK
spectral_gap = -2*N**2*a + N*a + N - T*a - T + a**3*p - 2*a**3 + a**2*p - 2*a**2 + a*p + p
universal_polynomial = 2*N**2*a - N*a - N + a**3 + a**2 - a - 1
matching_square_slack = (x1**2 - 2*x1*x2 + x2**2 + y1**2 - 2*y1*y2 + y2**2)/2
STATUS=PASS
```

The checker verifies the spectral algebra, the cubic rearrangement, and the exact square identity behind the positive-matching charge. It is regression evidence only; Sections 3--7 are the proof.

## 9. Corrections and failures preserved

1. The rank-degree CLC strengthening appearing in the newest B01 lead report is rejected; the correct denominator here is `L=m-mu`.
2. The old fixed-graph Cocks unit-to-weighted bridge is not used.
3. Global STAR-2 is not assumed; the loopless-multigraph minimality frame removes that conditioning debt source-equivalently.
4. The union/intersection-preserving Hall route is not revived; account04/B02 has an exact `K4` obstruction.
5. (E2)--(SC) do not by themselves close FOREST. The remaining step is graphic: turn residual transport failure into forbidden positive-correlation mass or otherwise contradict the signed-energy budget.

## 10. Honest status / handoff

**Outcome: `ESSENTIAL_STEP_APPLIED`.** The parent Grimmett--Winkler uniform-forest conjecture remains **OPEN** in this report.

The useful new package for the next FOREST worker is:

- minimal loopless multigraph counterexample;
- complete all-triple inequality `rho_ij <= rho_ik rho_jk`;
- positive pairs form a matching and every other edge is negative to either endpoint;
- correct ground-set CLC row budget;
- positive third-third mass cap `P_+<=E_*/2`;
- signed sum cap `tau<=E_*` and spectral condition (SC);
- matroid connectedness and no third series/parallel clone at a positive-pair endpoint;
- exact T1--T5 cross-fiber path/cut transports, with union-preserving Hall already refuted.

The next run should attack `GRAPHIC DEFECT-TO-POSITIVE-MASS` rather than another scalar-only inequality or another same-fiber recoloring.

No verified brain context was consumed. No installation/benchmark work, credential handling, email, Drive action, public posting, paid model/API/Codex call, remote workflow, permission change, or cross-account native action occurred.

Model self-report: `GPT-5.6 Sol`. Requested effort: maximum actually supported. Configured reasoning effort: `UNKNOWN_NOT_EXPOSED`. Provider reasoning-token/time counters: `NOT_EXPOSED`; unknown is not zero. Elapsed execution is recorded separately in the finish record and is not pure thinking time.
