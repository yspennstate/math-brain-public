SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B15, 2026-09-24T09:15:16Z.
attacking: bounded-size physical localization versus diffuse spectral banks; quantify how many original coordinates are required to retain three curvatures, then test operator-small truncation on the same target family.

# Early calculation

For m>=2 split 3m original coordinates into three banks and let u_k be the normalized constant vector on bank k. Put

A_m=u_1u_1^T+u_2u_2^T-u_3u_3^T.

Then spec(A_m)={1,1,-1,0,...,0}. If S contains k_j coordinates from bank j, then

(A_m)_{S,S}=J_{k_1}/m \oplus J_{k_2}/m \oplus (-J_{k_3}/m),

so its nonzero eigenvalues are k_1/m,k_2/m,-k_3/m. Hence for |S|=r,

s_3((A_m)_{S,S})=min(k_1,k_2,k_3)/m

(with value 0 if one k_j=0), and therefore

max_{|S|=r} s_3((A_m)_{S,S})=floor(r/3)/m.

Thus any original-coordinate principal carrier with three curvatures >=c must use at least 3cm coordinates. In particular every fixed-size physical localization degenerates as m->infinity even though the global matrix has exactly three unit curvatures.

For arbitrary independent cap-one inputs define Y_k=m^{-1/2} sum_{j in bank k} X_{k,j}. The one-dimensional product-projection bound gives ||p_{Y_k}||_infinity<=sqrt(2), hence

p_{Y_k^2}(s)<=sqrt(2)/sqrt(s), s>0.

Therefore

||p_{Y_1^2+Y_2^2}||_infinity<=2 int_0^t [u(t-u)]^{-1/2}du=2pi,

and convolution with the independent law of -Y_3^2 gives

||p_{Q_m}||_infinity<=2pi,
Q_m=Y_1^2+Y_2^2-Y_3^2.

The required e5f71d79... Theorem F also applies to the full law: use I=all coordinates, B=0, G_I=I_3, and row leverage 1/m<=1/2. It independently yields ||p_{Q_m}||_infinity<=12.

Next step in this run: combine this exact diffuse localization obstruction with the latest fleet03/B15 translation-robust operator-perturbation barrier by adjoining one tiny diagonal coefficient on an extra remote-support coordinate. This will test whether bounded localization can be rescued by discarding an operator-small tail.