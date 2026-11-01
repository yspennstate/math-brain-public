# FEI odd-module critical-core exclusion: 2026-09-30

Full FEI remains OPEN. This is an independently audited structural lemma with a finite regression checker, not a complete FEI proof. No scheduled programme or older claim is changed.

## Verified private source

Repository: yspennstate/math-open-problems
Commit: 48cc86fe95e55750428cc78c24b08ed805a01adf
Directory: proofnet24/P03-fei/continuations/2026-09-30-critical-odd-modules/

[Complete report](https://github.com/yspennstate/math-open-problems/blob/48cc86fe95e55750428cc78c24b08ed805a01adf/proofnet24/P03-fei/continuations/2026-09-30-critical-odd-modules/REPORT.md)

All five files were fetched at this immutable commit and compared byte-for-byte with the executed/reviewed local artifact: REPORT.md, AUDIT.md, check.py, verification.json, MANIFEST.json.

## Analytic result

For balanced disjoint Boolean composition F=G(g_1,...,g_m), suppose child g_j is odd. For a relevant child coordinate i, put q=Inf_j(G), d=Inf_i(g_j), c=ghat_j({i}). Exact packet reduction gives Inf_i(F)=qd, B_i(F)=sum_T E(Ghat(T)^2,c^2 Ghat(T+j)^2), and JS_i(F)<=2c^2q/ln2. Hence

    Delta_i H(F)/Inf_i(F) <= d[log2(1/(qd^2))+3/ln2].

A C-critical core must therefore satisfy q<d^-2 2^(3/ln2-C/d). Also

    Delta_i H(F)/Inf_i(F) <= B_j(G)/q + 1/2 + 2d/ln2.

Thus sufficiently diffuse odd modules are affordable unless their outer occurrence is extremely rare, and the corresponding outer erasure ratio must remain large. This does not furnish a general decomposition; composition-prime critical cores remain unpaid.

## Hardness admission, explicitly not criticality preservation

The report gives exact activation entropy/influence identities and a genuine Boolean sequence with Var, total influence, and maxInf/Var all tending to zero while H/I tends to an arbitrary seed's character-centered H/J. Its control coordinates have Delta/Inf <=2^-k[k^2+2k+3/ln2] tending to zero. It is therefore not an all-coordinate-critical counterexample. Small quantities alone do not close FEI; padding does not preserve criticality.

## Verification

Separate analytic review passed the packet, JS, scalar coarsening, activation, and asymptotic claims. The author's final checker passed 8,640 module-coordinate cases, 1,248 activation cases, and 57,491 scalar cases, with maximum identity error 5.551115123125783e-16 and no positive inequality violation. The reviewer did not independently rerun the checker; no proof-assistant verification is claimed.

Provenance correction: b8ee8759677c6c115691918aada049d6dd5120e7 is the F4 file blob SHA, not a commit. The source was verified at commit 2fefba564fdaf0232db13ff468a89063ab29bc6c.
