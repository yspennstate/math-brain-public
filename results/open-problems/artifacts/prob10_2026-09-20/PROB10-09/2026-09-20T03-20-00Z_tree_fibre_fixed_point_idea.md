# PROB10-09 idea before code — exact infinite-tree fibre activation by a rational fixed-point supersolution

Parent target stays frozen: iid bond percolation on Cayley graphs of finitely generated nonamenable groups, seeking `p_c(G)<p_u(G)` universally. This iteration remains on the R20-delimited quantitative surface-product/nonbacktracking route; it does not take NM13-11's free-core/complement or higher-rank-lattice lane.

## New idea

The previous `X_{3,4}` certificate upper-bounded `p_c` using a radius-two truncation of the vertical `T_10` cluster inside the embedded product `T_10 square T_14`. That truncation is the present quantitative bottleneck. Replace it by the exact Galton-Watson probability-generating-function recursion for the full subcritical `T_10` cluster, but certify it without solving any high-degree polynomial or using floating point.

For `T_d`, let `p<1/(d-1)`, `s=1-p`, and define

`F(h)=s(1-p+p h)^(d-1)`.

The branch-cluster pgf at `s` is the unique fixed point `h_*` of `F` in `[0,1]`, because `F'(h)<=s p(d-1)<1`. The full root-cluster pgf is

`E[s^{|C(o)|}] = s(1-p+p h_*)^d`.

Hence the probability that the vertical cluster sends at least one open edge into a specified forward fibre is

`phi_d(p)=1-s(1-p+p h_*)^d`.

For `T_d square T_{q+1}`, the usual forward-fibre Galton-Watson comparison is supercritical if `q phi_d(p)>1`.

The exact-certificate trick is: choose rational `u` with `F(u)<=u`. Since `F(h)-h` is strictly decreasing, this implies `u>=h_*`, and therefore

`phi_d(p) >= 1-s(1-p+p u)^d`.

So two exact rational inequalities,

`F(u)<=u` and `q[1-s(1-p+p u)^d]>1`,

certify `p_c(T_d square T_{q+1})<p` using the *full infinite tree* rather than a depth truncation.

## Frozen graph and proposed exact point

Keep the same frozen graph `X_{3,4}` and the same embedded `T_10 square T_14`, so `d=10`, `q=13`. Test

`p0 = 4540551/100000000 = 0.04540551`

and

`u = 9261812689/10000000000 = 0.9261812689`.

The predecessor's `p_{2->2}` lower bound is retained. For a clean new fully rational `p_u` floor, also test the older exact spectral bound against `719/10000`: with `R_34 = 2159/250 + 2 sqrt(13)`, show the larger nonbacktracking root is `<10000/719` using `sqrt(13)<1803/500`.

If both sides pass, this will yield the clean rational frozen-family gap

`p_u(X_{3,4})-p_c(X_{3,4}) > 719/10000 - 4540551/100000000 = 2649449/100000000 = 0.02649449`,

improving the preceding certified bound `0.02441444290890310...`.

## Negation test and three distinct routes

1. **Full tree-fibre pgf / rational supersolution (new; primary).** Try to falsify the proposed supersolution and activation inequalities exactly. If either fails, do not tune a numerical SDP; change method or rational point.
2. **Reverse the fibre orientation.** Use vertical `T_14` with nine forward children instead of vertical `T_10` with thirteen forward children. Preliminary analytic comparison says the reverse orientation has a larger activation threshold, so it is unlikely to improve the frozen metric; verify only enough to decide route choice, not as a claimed theorem.
3. **Improve the `p_u` side from a genus-four surface spectral bound.** Search current primary literature for a rigorous genus-four analogue sharper than the conservative Freiheitssatz bound. Bartholdi's Theorem 1.3 explicitly records the sharp Nagnibeda upper bounds only for genus 2 and 3, so absent a current genus-four theorem this route is not available in this bounded iteration.

A fourth possible route, the free-core/complement higher-rank-lattice mechanism, is intentionally not taken here because NM13-11 owns that complementary lane and has current 20 September reports through the triangle-fibre degree-9 construction.
