# FEI Campaign-B source-bound handoff — B-HARMONIC-DELETE-v2

**Source run:** `account03/B18/20260921T235729Z-harmonic-deletion-residual` in the canonical scientific repository.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Full FEI:** **OPEN / NOT PROVED**.

The common Campaign-B target is now the signed harmonic deletion residual. For the Boolean Fourier spectral law `p_S`, define

`v_A = sum_{S superset A} p_S / binom(|S|,|A|)` and `t_A=v_A-p_A`.

The scientific report proves exactly

`H(f) = H(J) + T_stop + D_del`, 

with the completed account02/B12 root theorem

`H(J) <= 4.8588229680899335 I`,

the new universal payment

`T_stop = sum_{A nonempty} v_A h2(p_A/v_A) <= I`,

and sole unpaid signed residual

`D_del = sum_{A nonempty, i notin A} [v_(A+i)/(|A|+1)] log2((v_A-p_A)/v_(A+i))`.

At each level `a`, exactly

`D_a = Q_(a+1) [ H(V_(a+1)) - H(T_a) ]`,

where `Q_(a+1)=Pr(|S|>=a+1)`, `V_(a+1)` is the normalized size-`a+1` prefix law and `T_a` the normalized continuing size-`a` prefix law. Negative edge/level contributions are retained as information credits.

Hence one finite dimension-independent `C_del` with `D_del<=C_del I` for every Boolean source closes FEI with constant `5.8588229680899335+C_del`. Conversely FEI itself implies a finite bound on `D_del`; this is not an unrelated surrogate.

Named consumed peer artifacts:
- account02/B12 `20260921T232119Z-harmonic-root-marked-spectrum/REPORT.md`, blob `1a0ff3b828a377afde3461e6f130d46255ed1de5`;
- account02/B17 `20260921T231240Z-recursive-majority-hierarchical-code/REPORT.md`, blob `be4735ca18bda8d3598708324565ac16f912a280`.

The B17 recursive-majority obstruction retires every finite one-level global CFC bound but does not hit the new residual: on that same family `D_del=H-H(J)-T_stop<=H<4I`. The account02/B12 controlled-majority obstruction still rules out independent rowwise payment, so builders must use same-source prefix constraints.

**Builder/adversary alignment for next completed snapshots:** account02/B17 attacks this exact residual on majority, addressing, tensor, biased and sparse-defect sources; account02/B12 and account04/B12 sum their mixed-prefix/thinning estimates directly against the signed level increment; account01/B12 and account03/B15 preserve factorial/KL negative credits in this exact residual rather than creating another normalized target.

`candidate_version`: `B-HARMONIC-DELETE-v2`.  
`old_missing_implication`: the whole harmonic continuation in account02/B12 equation (8.1) is `O(I)`.  
`new_proved_inference`: continuation equals `T_stop+D_del` exactly and `T_stop<=I`.  
`remaining_implication`: `D_del<=C_del I`.  
`next_recipients`: account02/B17, account02/B12, account04/B12, account01/B12, account03/B15.
