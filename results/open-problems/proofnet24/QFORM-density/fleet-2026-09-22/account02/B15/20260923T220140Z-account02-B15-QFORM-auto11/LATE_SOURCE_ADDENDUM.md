# Late-source addendum — newest Claude hub-roughness theorem does not close the rough endpoint

After the main B15 report was committed, fresh `math-open-problems` master advanced to Claude-attributed commit `44568becca495a4cf41f1f2314c6c24c24563266`, adding Proposition 3.18 in `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`.

That proposition is a genuine improvement for its single-hub normal form with zero hub diagonal: for arbitrary cross term and light laws, it replaces previous power dependence on hub roughness by logarithmic dependence. In particular, with `|lambda|>=1`, it bounds the output in terms of any of:

- hub support interval length `D` through `O(1+log D)`;
- a uniform number `n` of intervals in every hub-density superlevel set through `O(1+log n)`;
- hub density total variation `V` through `O(1+log(1+V))`.

This later theorem is compatible with, but does not close, the arbitrary-rough B15 endpoint. None of `D,n,V` is uniformly controlled by the owner assumption `0<=f<=1`, `int f=1`.

For example, for every integer `N>=1`, let

`E_N = union_{k=1}^N [2k, 2k+1/N]`, `f_N=1_{E_N}`.

Then `f_N` is a probability density with cap one, while:

- its support diameter is at least `2N-2`;
- every nontrivial superlevel set is exactly a union of `N` intervals;
- its total variation is `2N`.

Hence Proposition 3.18 produces a bound growing at least at the level of its stated logarithmic roughness parameter along this source-valid family; it supplies no universal constant over the owner class by itself. Smoothing the interval endpoints can make the densities continuous (indeed smooth after a narrow cap-preserving mollification) while retaining arbitrarily large variation, so continuity does not repair this gap.

By contrast, the grouped determinant receiver in the main report uses no hub-roughness norm: the only averaging object is `A=2M^TP+beta`, whose multidimensional density cap `1/(2^d|det M|)` follows directly from original-coordinate product structure. Thus the new late source reinforces the precise next obligation rather than superseding it: any extension that introduces a one-dimensional hub roughness parameter must remove that parameter before claiming the unrestricted rough-input theorem.

Full QFORM status remains OPEN.
