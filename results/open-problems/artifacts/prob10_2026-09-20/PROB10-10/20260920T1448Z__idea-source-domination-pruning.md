Model request: GPT-6 maximum. Applied model/effort telemetry is not authenticated by this runtime; report as UNVERIFIED.

# PROB10-10 idea before certificate code — source-domination pruning for asynchronous Exp(1) blocks

Frozen source/model: nearest-neighbor **undirected** FPP on `Z^2`, iid physical-edge weights `Exp(1)`. Canonical first checkpoint remains `Delta_12=2 mu(e1)-mu(1,1)>0`; retained axis lower certificate makes `mu(1,1)<0.6005646` sufficient. This note does not claim that inequality.

## New mechanism

The canonical asynchronous-carry theorem has paid the band-to-band dependence and finite-to-infinite interface error, while P20's newest delayed-Richardson theorem can exactly evaluate a finite block with asynchronous boundary activation times. The remaining practical obstruction is the huge active-source/subset state space.

For a finite block with input sources `s_i` activated at times `y_i`, delete a high source `i` only when a retained source `a(i)` is nearby on the same input boundary and satisfies

`y_i-y_{a(i)} >= R`.

If `P_i` is a deterministic boundary-chain path from `s_{a(i)}` to `s_i`, define

`eps_i=(y_{a(i)}+tau(P_i)-y_i)_+`.

Conjectured/proof target for this run: deleting all such high sources can delay **every** output arrival by at most `max_i eps_i`, samplewise. The reason is that a retained source can reach `s_i` by time `y_i+eps_i` and then imitate any route which would have started from source `i`. This is a global source-domination argument, not independent local surgery.

On the rotated input boundary, sources `q` indices apart have a deterministic simple zig-zag path of `2q` physical edges. Hence `tau(P_i)~Gamma(k_i,1)`, `k_i<=2q`. If the block Bellman scalar `Q` is a nonnegative convex combination of first-output time, last-output time and weighted output times (the P20 functional), it is 1-Lipschitz in the output sup norm. Therefore the desired quantitative pruning loss is

`E[Q_pruned-Q_full] <= |J| psi_{2q}(R)`,

where

`psi_k(R)=E[(Gamma(k,1)-R)_+]`
`        = exp(-R) sum_{r=0}^{k-1} (k-r) R^r/r!`.

No independence among the paths `P_i` is needed.

For the width-48 / 49-source profile core used by P20, the concrete stress point to certify is `q=4,R=35`. Preliminary hand arithmetic indicates the worst-case loss from deleting as many as 49 dominated sources is below `10^-6`, small compared with the `L=4` source-facing Bellman threshold `lambda_*=2.4022584`.

## Negation test before acceptance

Zero-loss deletion is false. Even with one retained source `a`, one high source `i`, and one output, there is positive Exp(1) probability that the retained route to `i` takes longer than the activation gap and source `i` wins. Therefore P20's monotone source deletion is safe as an *upper* certificate, but treating it as free would destroy quantitative margin. The positive-part Gamma tail above is intended to pay exactly this missing loss.

## Three routes compared

1. **Source-domination pruning (pursue):** quantify the loss from removing high asynchronous sources by a local boundary Gamma tail, then hand the reduced source set to the exact delayed-Richardson evaluator. This is different from the retired R08 local-detour argument because it is a samplewise global domination of arrival fields and never multiplies local gains.
2. **Full unpruned projected Bellman enumeration (retain, do not duplicate):** canonical/P20 machinery is rigorous but state explosion is the current bottleneck. Pruning is meant as a certified reduction layer, not a replacement of its proof.
3. **True-geodesic Busemann/Jacquet residual contradiction (do not duplicate P20):** geometrically distinct and still blocked by the possibility of positive-density near-co-calibration under a flat-face hypothesis.

If the domination inequality fails under an explicit finite counterexample, abandon it in this run rather than tuning code around it. If it survives, certify the Gamma-tail formula and concrete rational bounds exactly, then record source-level `c_*` separately from this mechanism delta.
