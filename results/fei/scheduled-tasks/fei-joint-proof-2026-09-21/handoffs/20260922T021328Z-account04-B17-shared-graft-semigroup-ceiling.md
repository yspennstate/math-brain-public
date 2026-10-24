# account04/B17 handoff — source-valid shared-graft semigroup ceiling

**Run:** `20260922T021328Z-b17-fei-r16`  
**Status:** `ESSENTIAL_STEP_APPLIED`; full FEI remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T021328Z-shared-graft-semigroup-ceiling/REPORT.md`, commit `3335677efb8ac237950319cca5c29bcea885189e`, blob `d79b4923409f6856c5408bf6d45225750a736abc`.

Checker: commit `6655cb834367d698d3c3bc95df057a1b504d7389`, blob `75b657b5cd030fcc406b5f1e53029f4f77747abf`. Verification output: commit `b6f42c6d4fc4fc6c6fa592a6bbc37a0c236d776f`, blob `3b01567733ae42be35626e59d706a60cc5c5b3da`.

Newest compatible other-account B15 result actually consumed: `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T012556Z-iterated-shared-graft/REPORT.md`, blob `aff93b999538a8b8baeab270ff739f405c79ee7c`. It certifies the finite shared-graft obstruction through `F6` and asks for upper control of the whole iterated mechanism before another center cap is frozen.

For the source nine-host shared-core transform `T(h,b)`, with `alpha=9/256`, `d0=133/128`, and `K(b)=H_core(b)+alpha[-phi(b^2)+16(1-b^2)]`, the exact identities are

`H(T)=alpha H(h)+K(b)`,

`I(T)-1=alpha[I(h)-1]+d0`.

A rigorous 18-interval tangent certificate proves

`K(b) < (133/128)*6.5218513`

for every `0<=b<=1`. Therefore `R(h)=H(h)/(I(h)-1)<=6.5218513` implies `R(T(h,b))<6.5218513`.

Balanced disjoint functional composition has the exact excess cocycle

`E_C(f(g_i))=E_C(f)+sum_i Inf_i(f) E_C(g_i)`, with `E_C=H-C(I-1)`,

so the same cap is preserved under arbitrary heterogeneous balanced disjoint compositions.

Hence every finite balanced monotone Boolean gate generated from seeds below the cap by any interleaving of balanced disjoint compositions and this exact nine-host shared-core transform remains below `R=6.5218513`. This closes all depth changes and mixed-depth variants that keep the same shared core, not just the old `d=4` recurrence.

The known actual Boolean `F7` satisfies

`R(F7)>6.521850949550448184840160538860511501350329679`,

so the entire remaining room for this mechanism is below `3.50449551815159839461139488498649670321e-7`.

The checker records a worst certified tangent gap `3.7741447258356244193928659064059438317e-9` below the exact threshold `(133/128)*6.5218513=6.77661111640625`. A near-maximizer probe gives `K(b)/(133/128)≈6.5218512130128777`; the probe is not used for the upper theorem.

This is not a universal FEI upper bound. A stronger all-gate adversary must change the shared host/core, use a biased product point, or use a composition-prime interference mechanism outside this semigroup. The older arithmetic/KL-credit representation is not weakened or credit-stripped here; the later owner all-gate target evaluates the exact Boolean construction directly.
