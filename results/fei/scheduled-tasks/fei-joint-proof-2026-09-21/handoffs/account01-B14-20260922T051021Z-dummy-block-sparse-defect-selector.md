# Source-bound FEI handoff — account01/B14 — dummy-block sparse-defect selector

**Status:** `AUXILIARY_ONLY / SPARSE-DEFECT-OBSTRUCTION-PAID`. Full unrestricted FEI remains **OPEN / NOT PROVED**.

**Live candidate:** `LIMIT-PRIME-GATE-LIFT-v1`, with `C_*=6.5218512`, `a_*=0.2682048`, `Gamma_*=Gamma_RO+a_*p(1-p)`. The universal missing statement remains `D_{Gamma_*}(P;p)>=0` for every finite composition-prime Boolean gate and every interior product bias.

**Scientific source:** `proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260922T051021Z-dummy-block-sparse-defect-selector/REPORT.md`, creation commit `a839406fd8c81ab0fea5133fd437b471b0c90d10`, report blob `008a1c063f47f31084806495cca89e9e40abb0f7`.

## Exact other-account results consumed

1. account02/B18 `20260922T051105Z-random-depth-barycenter`: the existential random-depth criterion is terminally tautological if `r=n-1` is allowed; useful selector work must exhibit a genuinely nonterminal block or a multigeneration compensation. Its exact signed barycenter keeps child slack and both information terms.
2. account02/B17 `20260922T044637Z-radius2-dust-compensation`: for the genuine balanced sparse-pair dust family `g_m` built from a fixed balanced `r`-bit source `f`, with `q_m=2^{2-r-m}`,
   `D_*(g_m)-D_*(f)=(C_*-4)(r+m)q_m+O_{f,a,b}(q_m)`.

## New physical selector theorem

Let `Y` be the `m` genuine dummy/tag coordinates in the sparse-pair family and reveal the actual block `T=Y`. It is nonempty and proper and leaves every original source coordinate alive. The branches are exactly

`g_m|_{Y=0^m}=f^a`, `g_m|_{Y=e_1}=f^b`, and `g_m|_Y=f` otherwise.

Hence, with

`K_{f,a,b}=D_*(f^a)+D_*(f^b)-2D_*(f)`, 

the exact block residual is

`R_m = D_*(g_m)-E_Y D_*(g_m|Y) = [D_*(g_m)-D_*(f)]-2^{-m}K_{f,a,b}`.

Applying the account02/B17 asymptotic gives

`lim_{m->infty} (2^m/m) R_m = 2^{2-r}(C_*-4) > 0`.

Therefore, for every fixed source/opposite-sign pair, the genuine nonterminal dummy block is paid for all sufficiently large dilution `m`. This rules out indefinite recycling of the sparse local debit through dummy dilution.

For the canonical literal seed `r=1`, the same selector is paid for every `m`: the two special children are constants and all other children are the literal, so child defect is zero. The exact spectrum gives

`I(g_m)-1=(n-2)q`, `H(g_m)=h_2(d)+d log_2(2^{n-1}-1)`, `d=2q-q^2`,

and the report proves `H(g_m)<=6[I(g_m)-1]` for all `n=m+1>=2`. Since `C_*>6`, `D_*(g_m)>=0` at every depth.

## Scope

This is not universal coverage. It does not pay arbitrary addressing, majority, tribes, tensor-critical, or fully biased prime gates. The next useful target is an intrinsic nonterminal block or two-generation compensation theorem for arbitrary composition-prime gates, retaining child slack and all information credits. Do not replace it by an `r=n-1` terminal existential statement.

**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were genuinely consumed, but no installed/native brain receiver-context mechanism was used.
