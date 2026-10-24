# account03/B16 FEI handoff — arbitrary-selector nonamplification

Source run: `account03/B16/20260922T065209Z-selector-gating-transfer` in `yspennstate/math-open-problems`.

Scientific report commit: `8295b9fa8e6ad4b38e0d9f4a5b3314d9dde0e003`; report blob: `a6d2b964ef8286c691a53b0d75c38487eb477201`.

Status: `AUXILIARY_ONLY / EXACT_ADVERSARIAL_FAMILY_EXCLUDED`. Full FEI remains OPEN / NOT PROVED. Execution is `WITHOUT_VERIFIED_BRAIN`.

For an arbitrary Boolean selector `a` with `delta=Pr[a=-1]`, a balanced Boolean core `f` on disjoint variables, and a fresh unbiased character `z`, define `G=z AND(a,f)`. For every real `C`, exactly

`S_C(G) = (1/2) E_C(a) + delta S_C(f) + delta [C-T(delta)]`,

where `S_C(f)=C(I(f)-1)-H(f)`, `E_C(a)=C I(a)-H(a)`, and

`T(d)=[2 h_2(d)-(1/2)h_2(4d(1-d))]/d`.

The source report proves algebraically that this `T(d)` is exactly the scalar `Q(d)` from the completed cross-account theorem `account04/B17/20260922T061604Z-character-cofactor-local-threshold`, blob `865131123fbceeb0d41109308d531ace9e926af6`. Hence `T(d)<5.1` on `0<d<=1/2`; for `d>=1/2`, `T(d)<=4`. Therefore any selector and balanced core already safe at a common `C>=5.1` produce a strictly safe parent. At the live `C^dagger=6.521851214`, the extra reserve is at least `1.421851214 delta` before component slack.

A second exact identity shows arbitrary Boolean MUX selection between two balanced safe disjoint children is also nonamplifying. Balanced tensor products satisfy `S_C(fg)=S_C(f)+S_C(g)+C`, so independent tensor amplification is impossible as well.

Checker readback: `42,120` selector/core/constant identity cases, `6,084` tensor cases, and `1,022` dyadic `T=Q` checks passed; report contains the exact scope and proof. The floating grid maximum `4.872321071783793` is diagnostic only; the rigorous upper bound comes from the account04/B17 theorem.

Remaining universal implication: prove `D_{Gamma^dagger}(P;p)>=0` for every finite composition-prime Boolean gate `P` and every interior product bias, or find a source-valid counterexample. Next recipients: account02/B18 (all-gate lead) and account02/B17 (prime-gate adversary). Arbitrary disjoint selector gating and tensoring should be removed from the adversary list; remaining attacks must be genuinely prime/shared-variable or off-center.
