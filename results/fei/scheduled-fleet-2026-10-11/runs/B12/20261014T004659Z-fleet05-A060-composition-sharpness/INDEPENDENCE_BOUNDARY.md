# Necessity of independence for the selector variance reserve

Use a fresh fair selector z, a shared fair sign x, and t>=1 fresh private bits w. Put delta=2^-t, A=1[w=0], u=x, v=x(1-2A). The controller selects u on z=+1 and v on z=-1. These are distinct balanced actual Boolean cores, with correlation E(uv)=1-2delta. The core cubes overlap at x, so the disjoint-independent-core hypothesis is deliberately violated.

The nominal selector variance reserve remains R=(1/2)*1+(1/2)*1=1. Its actual exclusive controller influence is Inf_z=Pr(u!=v)=delta. Therefore R/I_ctrl=2^t: no finite reserve funding R<=K I_ctrl survives unrestricted shared cores, even with balanced cores, a one-bit controller, one shared physical data bit, and correlations arbitrarily close to one.

The precise missing edge identity is

    Var(u)+Var(v)=2(1-E uv)-(E u-E v)^2+2 Cov(u,v).

It reduces to A057's independent edge inequality when Cov=0. In this balanced family the fair-mux reserve is exactly R=2I_ctrl+Cov(u,v). The covariance belongs to the shared data and cannot be treated as a free control credit. This is a source-hypothesis guard, not a refutation of the stated independent-core theorem.

All physical costs and terminal entropies remain explicit. The root is

    F=x[1-2*1[z=-1]*A(w)],
    I(F)=1+(t+1)delta,
    E I(F|z)=1+t delta,
    H(F)=eta((1-delta)^2)+2t(2delta-delta^2),
    H(u)=0,
    H(v)=eta((1-2delta)^2)+(2t-2)(4delta-4delta^2),
    E H(F|z)=H(v)/2.

These follow from exact point-indicator Fourier coefficients and tensoring with x. The shared x influence is exactly one. The t private coordinates and selector each have root influence delta; in v the private influences are 2delta. The terminal formula includes its delta=1/2 endpoint by eta(0)=0.

For t>=2, eta((1-delta)^2)<=2delta/ln2 (use -a ln a<=1-a), so H(F)<=4t delta+2delta/ln2 tends to zero, while I(F) tends to one. There is no FEI disproof. This elementary family pins which precise control-reserve hypothesis is necessary and which shared physical account would have to replace it. It does not assert that the collision entropy itself is large, or require that a valid shared-core theorem retain the same nominal R.

For independent balanced u and v, the same fair mux has R=1 and I_ctrl=1/2. Thus the original factor 2 is attained exactly, as already proved by A038. This stage credits that result and adds the above quantitative removal-of-independence boundary.
