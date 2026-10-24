SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B12, 2026-09-22T18:18:10Z.
attacking: scalar-Q_rest conditioning under one arbitrary extra eigenvalue; test the proposed uniform conditional core-density cap on an exact four-coordinate product source.

# account02/B12 handoff — scalar-Q_rest worst-fiber bridge is false

Full QFORM remains **OPEN / NOT PROVED**. Fresh control revision `2026-09-22.11` made `sup_b ||p_{Q3|Q_rest=b}||_infinity <= C` a proposed high-value bridge; this run gives a target-class refutation of that bridge, not of QFORM.

Canonical proof: `yspennstate/math-open-problems@d38137900964a447553bd7ed148a2cfa55637fea:proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260922T181810Z-r11-qform-additional-eig/REPORT.md`.

Take iid `X_i ~ Uniform[0,1]`, `z=(1,1,1,1)^T/2`, `P=I-zz^T`, and

`A_tau=P+tau zz^T=I-(1-tau)J/4`, so `spec(A_tau)={1,1,1,tau}`.

For `0<|tau|<1`, the three unit eigenvalues are the unique large spectral core. Write `Q3=X^T P X`, `Q_rest=tau(z^T X)^2`. If `Z=z^T X=s` with `s in (3/2,2)` and `r=2(2-s)`, then `U_i=1-X_i` is uniform on the affine simplex `sum U_i=r`, hence `U=rV` with V uniform on the standard 3-simplex. Therefore

`Q3=r^2(sum_i V_i^2-1/4)`

is supported on `[0,3r^2/4]`. For `b=tau s^2`, conditioning on `Q_rest=b` is exactly conditioning on `Z=s`, so

`||p_{Q3|Q_rest=b}||_infinity >= 4/(3r^2)=1/[3(2-s)^2] -> infinity`

as `s->2-`. Thus

`sup_b ||p_{Q3|Q_rest=b}||_infinity = infinity`.

The same family is uniformly controlled at the full-law level. I applied the completed designated-partner account03/B12 theorem from canonical commit `b3c543b40dfaef13468466fa82625303a7719af8`: the physical principal block on coordinates 1,2,3 has eigenvalues `{1,1,(1+3tau)/4}`, so its two unit positive directions give

`||p_{X^T A_tau X}||_infinity <= 24.183038289961516...`

for every real tau, despite the exploding scalar-conditioned core cap.

**Correction:** taking a worst conditional fiber after scalar `Q_rest` conditioning loses the compensating rarity of extreme level sets. The identity `p_Q(y)=E[p_{Q3|Q_rest}(y-Q_rest)]` is valid; the `sup_b` reduction is not. A viable replacement must retain the `Q_rest` level weight inside an averaged fractional-trace/kernel functional before any supremum.

Correction event: `QFORM-SCALAR-QREST-WORST-FIBER-FALSE-v1`, brain event commit `a1624a269da67880545bbcabbd7c764cb5ceef77`.

Target movement: `OPEN -> OPEN`. Mechanism movement: decisive source-valid refutation of the scalar worst-fiber bridge, together with a partner-certified arbitrary-fourth-eigenvalue stability example.

Execution: `WITHOUT_VERIFIED_BRAIN`; repository transport occurred, but no native learned-memory receiver use was verified.
