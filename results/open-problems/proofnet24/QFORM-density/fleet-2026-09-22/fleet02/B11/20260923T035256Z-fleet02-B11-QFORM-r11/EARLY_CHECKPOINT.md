# Early substantive checkpoint — heavy-null angular reduction

Status: partial supporting implication; full QFORM open.

Work on exact rank three first: `A=R Lambda R^T`, `R^T R=I_3`, signature `(2,1)` (reflection gives `(1,2)`), and all three nonzero eigenvalues have magnitude at least one. Put `c_i=||r_i||^2` and `a_i=A_ii`.

The required Claude source `e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, Theorem F gives the real inequality

`max_i c_i <=1/2  ==>  ||p_Q||_infinity <=12 |det Lambda|^(-1/3) <=12`.

Thus any unpaid exact-rank-three case has a heavy ORIGINAL row `c_i>1/2`. The reviewed rank-three scalar-pivot theorem at `e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, equation (1.2), gives

`||p_Q||_infinity <=128 [c_i |a_i| |det Lambda|]^(-1/4)`.

At the fixed threshold `tau=1/64`, a heavy row with `|a_i|>=tau` is therefore paid by `<431`.

The remaining heavy rows have `|a_i|<tau`. For `u_i=r_i/sqrt(c_i)`, let `z_i=|Lambda|^(1/2)u_i`, `y_i=z_i/||z_i||`, and `J=diag(1,1,-1)`. Then

`|y_i^T J y_i| <= |u_i^T Lambda u_i|=|a_i|/c_i < 2 tau =1/32`.

For a unit Lorentz vector `y` with `|y^TJy|=delta<1`, the unit null vector with the same spatial angle and time sign lies within Euclidean distance at most `delta`. Hence every unpaid heavy row lies within `1/32` of a definite projective null ray in the `|Lambda|^(1/2)` geometry.

Next calculation: if two such heavy rows have null angles separated by at least `pi/3`, their normalized Lorentz bilinear is at least `3/16`, hence their ORIGINAL physical `2x2` principal determinant has magnitude `>35/4096>1/120` and is indefinite. The determinant-only pair theorem should then give a global `<176` density bound, with the pair's logarithmic singularity absorbed by the third-direction Schur remainder rather than falsely removed.

The expected remaining exact-rank-three chamber is therefore a single angular cluster of heavy near-null rows. A separate diffuse family will be recorded to show why small physical diagonals alone do not imply near-null spectral directions.
