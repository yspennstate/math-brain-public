Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-10 idea before code — contiguous frontier carry, synchronization obstruction, and a longer-memory axis dual

Frozen model: nearest-neighbor **undirected** first-passage percolation on `Z^2` with iid `Exp(1)` physical-edge weights. Frozen source milestone: `Delta_12=2 mu(e1)-mu(1,1)` and `c_*`, the largest rigorously proved nonnegative lower bound on `Delta_12`.

The previous three PROB10-10 reports left `c_*=0`. The newest block certificate gives `mu(1,1)<=0.758507818076`, while the retained R08 axis lower bound is `mu(e1)>=0.30024`. Merely adding another reverse layer to that finite block is not the method attempted here.

## New block mechanism to test first

Carry a **contiguous frontier of k possible endpoints** across fresh antidiagonal edge bands rather than collapsing every block to one winning endpoint. The simplest exact version deliberately synchronizes those k frontier vertices before each new slab. This makes the finite-to-infinite dependence accounting completely transparent and tests whether endpoint reset, rather than local passage cost, is the real obstruction.

If k consecutive vertices on an antidiagonal have all been reached by a common time, then after exposing only the fresh edges to the next antidiagonal the completion time of the better of the two overlapping k-windows is

`C_k = max(Y_1,...,Y_{k-1}, min(Y_0,Y_k))`,

where `Y_0,Y_k~Exp(1)` are the two boundary arrival increments and the k-1 interior increments are iid `Exp(2)`. Since `min(Y_0,Y_k)~Exp(2)` and is independent of the interior variables, `C_k` is the maximum of k iid `Exp(2)`, hence

`E C_k = H_k/2`.

This predicts an exact **synchronization obstruction**: resetting a k-frontier on every antidiagonal costs diagonal time at least `H_k`, so widening a synchronized frontier makes the local rate worse. Therefore any useful frontier-carry method must retain the *asynchronous arrival-label differences*, not only the set of reachable frontier vertices.

I will also test a more general r-level synchronized slab. Let `Q_{k,r}` be the first time, using only oriented fresh edges in r consecutive antidiagonal bands, that some k consecutive vertices of the terminal antidiagonal are all reached from k synchronized consecutive seeds. Symmetry chooses a random terminal k-window with zero-mean lateral shift. Concatenating independent slabs and paying a fresh final connector should give the rigorous compiler

`mu(1,1) <= 2 E Q_{k,r}/r`,

with a finite-N correction at most `2/sqrt(N)` plus the finite startup cost divided by distance. Exact small `(k,r)` values will be used only as a diagnostic unless they improve a rigorous source-relevant bound.

## Independent auxiliary route

The source metric can also benefit if the old R08 axis lower bound is strengthened, but this is **auxiliary** and is not the required method change by itself. I will extend the R08 finite-memory simple-path transfer matrix from six remembered vertices to eight remembered vertices. The candidate Perron/Collatz vector may be generated numerically, but every inequality used in the theorem will be rechecked with exact rational arithmetic. The intended target is a certified improvement from `mu(e1)>=0.30024` to at least `0.30027`, which would raise the sufficient diagonal target from `0.60048` to `0.60054` while leaving `c_*=0` unless the diagonal bound also crosses it.

## Three materially different routes for this run

1. **Synchronized contiguous-frontier slabs:** exact dependence-controlled compiler; attack its negation by calculating the one-level cost and small multi-level slabs.
2. **Asynchronous frontier labels / average-cost Bellman:** use the synchronization obstruction to isolate the missing state variable. I will formulate the precise average-cost inequality a rigorous interval-rounded state compression would have to prove; no theorem will be claimed without that certificate.
3. **Longer-memory axis dual:** strengthen the rigorous axis ingredient through a different finite-state path-count certificate, explicitly labelled auxiliary. I will also compare against the recent Jacquet unrestricted-vs-directed inequality rather than mistaking it for the desired directional strict triangle inequality.

Peer P20 currently owns the complementary Busemann-residual/predictable-pivot route, so this run will consume that report but will not duplicate its local Bellman-gap theorem.