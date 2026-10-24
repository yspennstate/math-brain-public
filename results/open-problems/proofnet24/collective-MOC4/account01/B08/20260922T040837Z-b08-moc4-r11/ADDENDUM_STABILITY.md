# Addendum — quantitative cross-ratio stability from support deficits

This addendum records the first quantitative half of `MOC4-CHAIN-CUBE-TRANSVERSE-COLLAR-v1`.

Normalize a support functional as `L(z)=Re(eta z)` with `|eta|=1`. For any two nonzero complex edge differences `E,F`, write

\[
\eta E=x+iy,\qquad \eta F=u+iv.
\]

Then

\[
|\Im(E\overline F)|=|yu-xv|
\le |E|\,|u|+|F|\,|x|
=|E|\,|L(F)|+|F|\,|L(E)|.
\]

Hence the exact elementary estimate

\[
\boxed{
|\sin\arg(E/F)|
\le \frac{|L(E)|}{|E|}+\frac{|L(F)|}{|F|}.}
\tag{A1}
\]

If `H_sigma=L(v_sigma)=M-d_sigma` with `d_sigma>=0`, an edge `E=v_sigma-v_tau` obeys

\[
|L(E)|=|d_\tau-d_\sigma|\le d_\sigma+d_\tau.\tag{A2}
\]

Applying (A1)-(A2) to the five edge ratios in `REPORT.md`, one obtains explicit phase-defect bounds for the five cross ratios used in the common-circle propagation theorem. For example,

\[
\left|\sin\arg\frac{z_{11}z_{22}}{z_{12}z_{21}}\right|
\le
\frac{d_{1234}+d_{1243}}{|v_{1234}-v_{1243}|}
+
\frac{d_{2134}+d_{2143}}{|v_{2134}-v_{2143}|},
\tag{A3}
\]

and

\[
\left|\sin\arg
\frac{(x_2-x_3)z_{11}}{(x_1-x_3)z_{21}}\right|
\le
\frac{d_{1234}+d_{1324}}{|v_{1234}-v_{1324}|}
+
\frac{d_{2134}+d_{3124}}{|v_{2134}-v_{3124}|}.
\tag{A4}
\]

The analogous three inequalities are obtained from the edge pairs

- `2134--2431` versus `1234--4231`;
- `2143--2341` versus `4123--4321`;
- `2143--4123` versus `2341--4321`.

Thus, on any compact generic region where those ten spectral edge differences are bounded below by `m>0`, if all eleven face deficits in the propagation theorem are at most `epsilon`, every one of the five defining cross-ratio phase defects is at most

\[
\boxed{4\epsilon/m}
\]

in sine distance from the real axis. This is a source-exact quantitative statement: no arbitrary bistochastic or compound-minor relaxation is introduced.

What is still missing for the full transverse collar is to convert these five controlled cross-ratio phases, together with the actual edge magnitudes/conditioning, into a lower bound for the ellipse payment margin `delta_0 delta_1-C^2`. The exact tie theorem is the `epsilon=0` endpoint of this estimate.
