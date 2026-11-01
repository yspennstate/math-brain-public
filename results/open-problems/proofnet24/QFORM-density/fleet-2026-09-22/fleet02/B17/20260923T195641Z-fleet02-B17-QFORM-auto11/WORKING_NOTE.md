# Early calculation — unequal opposite banks

Let `a in R^m`, `b in R^n` be unit vectors.  With disjoint independent centered unit-interval banks set

`S=a.U`, `T=b.V`,

and let `X` have an arbitrary independent probability density `f<=1`.  The physical matrix

`A=diag(1, aa^T, -bb^T)`

has exact nonzero spectrum `{1,1,-1}`.  Write `h,k` for the densities of `S,T`.  They are even and decreasing on `[0,infinity)`.  Ball/Rogozin cube projection gives `||h||inf,||k||inf<=sqrt(2)`, and applying the same cube projection to `(S-S')/sqrt(2)` and `(T-T')/sqrt(2)` gives `||h||_2^2,||k||_2^2<=1`.

The key replacement for the identical-bank symmetry is the one-dimensional three-factor rearrangement lemma: if `F1,F2` are symmetric decreasing, `0<=f<=1`, `int f=1`, then for every shifts `c1,c2`,

`int f(x) F1(x-c1) F2(x-c2) dx <= int_{-1/2}^{1/2} F1(x)F2(x) dx`.

Layer cake proves it: for each three levels the intersection of an arbitrary measurable set and two shifted centered intervals has length at most the minimum of the three lengths, achieved when all three intervals are centered; integrate the levels and use the bathtub principle.

For the positive one-sheet level `q=X^2+S^2-T^2=R^2`, the proved ruled parametrisation in pinned `e5f71d79.../COUNTEREXAMPLE_SEARCH.md` is

`(x,s,tau)=(R cos(theta)-u sin(theta), R sin(theta)+u cos(theta),u)`,

with `delta(q-R^2) dxdSdt = (1/2) dtheta du`.  For each theta, after changing from `u` to the heavy coordinate `x`, the two bank factors are symmetric decreasing functions with centers `R/cos(theta)` and `R cos(theta)`; at `R=0` the centers coincide.  The rearrangement lemma therefore gives each ruled line integral at `R>0` no larger than its cone-tip value with `f=1_[-1/2,1/2]`.

For negative levels `q=-r`, direct root integration in `T` gives

`p(-r)=int f(x)h(s) k(sqrt(r+x^2+s^2))/sqrt(r+x^2+s^2) dx ds`.

The kernel is even decreasing in `|x|` and in `r`, hence the same centered heavy interval and `r=0` dominate.  Thus both signs reduce to the single cone integral

`C(a,b)=int_|x|<=1/2 int h(s) k(sqrt(x^2+s^2))/sqrt(x^2+s^2) ds dx`.

The remaining task in this run is to certify a universal `C(a,b)<3sqrt(2)` from the `L^infty/L^2` cube-projection bounds and publish the complete proof with exact constants.
