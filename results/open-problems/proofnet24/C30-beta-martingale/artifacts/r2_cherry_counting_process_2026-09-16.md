# The size-2 clade count as an explicit counting-process martingale

This specializes the fixed C30 martingale family to `r=2` and gives a particularly simple source-relevant form.

For a realization `T=CTCS(n)`, call a singleton leaf `v` **free** if it is not contained in a size-2 clade (equivalently, its parent is not a cherry). Let

`S_T(v)=exp(-sum_{A strict ancestor of v} ell_A/|A|)`

be the probability of surviving every finite clade edge on the root-to-`v` path after `v` has been selected as target. Define

`g_2(T) = (1/n) sum_{v free singleton leaf} S_T(v)`.

## Claim

Conditional on `T_n=T`,

`N_2(T_{n+1})-N_2(T_n)`

is exactly a Bernoulli random variable of parameter `g_2(T)`.

### Proof

Use the general one-step increment formula from the C30 run report,

`d_2(T,C)=1_{|C|+1=2} + #{A strict ancestor C: |A|=1} - #{A strict ancestor C: |A|=2}`.

A strict ancestor can never have size 1. If `C` is not a singleton, the first term is zero and a strict size-2 ancestor is impossible because every strict ancestor is larger than `C`; hence `d_2(T,C)=0`.

If `C={v}` is a singleton, the first term is 1. There is a strict size-2 ancestor exactly when `v` already belongs to a cherry, in which case the insertion creates a new cherry but simultaneously promotes the old cherry to size 3, giving net change zero. If `v` is free, no such subtraction occurs and the net change is one.

The probability of hitting the infinite singleton ray of a particular leaf `v` is `S_T(v)/n`: first select `v` with probability `1/n`, then survive all finite ancestral edges. Summing over free leaves gives `g_2(T)`. Therefore the increment is Bernoulli(`g_2(T)`). QED.

## Martingale and exact bracket

Consequently

`M_2(N)=N_2(T_N)-sum_{n=1}^{N-1} g_2(T_n)`

is a martingale with

`<M_2>_N = sum_{n=1}^{N-1} g_2(T_n)(1-g_2(T_n)).`

This is stronger than merely having a generic bounded-increment compensator: `N_2` is a genuine adapted counting process whose one-step conditional hazard is an explicit function of the current CTCS edge lengths and cherry locations.

The source occupation theorem gives `E[N_2(T_N)]/N -> 3/pi^2`. Hence the mean accumulated hazard satisfies

`E[sum_{n<N} g_2(T_n)]/N -> 3/pi^2`.

A CLT for the 2-clade count is therefore reduced to controlling the random accumulated hazard and its Bernoulli bracket; the martingale-noise part is already explicit.

The structural facts used here were included in the exact checker `check_clade_martingale.py`, whose archived output verifies every clade-count increment on all 626 ordered full binary tree shapes with pre-state size at most 8.
