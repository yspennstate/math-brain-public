# Correction and mechanism log

1. The earliest y-block run used a one-sided event `K_s>=s/3` to infer `s-K_s>=s/3`; this is false (e.g. `K_s=s`). That proof is superseded.
2. The two-sided repair uses `s/3<=K_s<=2s/3` for every suffix length and retains the terminal extension in `R_i(V)`.
3. The prior corrected endpoint-crossing proof gave `P(B)>=1/3072` using an initial central window plus a negative endpoint increment.
4. This run changes mechanism to an occupation-time second moment: `X` counts visits `Z_s=0` at even suffix lengths. Exact central-binomial bounds yield `EX>=sqrt(n)/14`, `EX^2<=n`, hence `P(B)>=1/196`.
5. The upper-extension estimate remains a separate Chernoff-plus-union-bound lemma and is not conflated with the base-hit event. The event `A cap B` costs `P(A^c)<1/6144`, so its probability is bounded below by `1/196-1/6144>1/204`.
6. No finite computation is treated as proof of the all-dimensional statement. The result remains conditional pending A092/A088 independent end-to-end reconstruction.
