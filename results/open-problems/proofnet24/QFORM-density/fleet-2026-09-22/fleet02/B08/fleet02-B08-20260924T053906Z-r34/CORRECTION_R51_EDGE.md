# r34 correction — do not apply fleet03/B08 r51 at beta=0

This later correction is normative over the subsection `Newest partner r51 on the same family` in `REPORT.md` Section 7.

That subsection is **withdrawn as an application of r51**. In the Walsh stress family, deleting the separate coordinate `z` gives star vector `b=0`, hence `beta=||(I-VV^T)b||=0`. Although the displayed inequality `beta>=zeta||b||` is formally true, the proof of fleet03/B08 r51 normalizes `u=w/beta` in its half-cut argument and is written for the genuinely distributed-star state inherited from fleet01/B08 r43, where `||b||>rho_*L` and the transverse branch has `beta>0`. I therefore do not extend r51 to the zero-star endpoint by continuity or by an unstated convention.

The use of the newest fleet03/B08 r51 theorem in `REPORT.md` Section 6 remains valid and is the intended partner application: on the actual star-dominated deletion sub-branch inherited from fleet01/B08 r43, r51 pays the transverse/diffuse-two-child state and leaves only child localization or near-alignment with the child top-two carrier. This is intersected there with the new rank-two/cancellation packet.

For the Walsh family itself, the completed designated **fleet04/B08 physical-deletion child-window theorem** applies directly, without passing through r51: after deleting `z`, the child has four eigenvalues of modulus `L`; at child scale `m=L` its `L/64` spectral-window projection is the rank-four Walsh frame and has physical leverage `4/m_size<=1/32` for `m_size>=128`. Therefore it gives

`||p_Q||_infinity<64/L`, `p_Q in C_0`.

The required fixed-source rank-four Fresnel--Brascamp--Lieb theorem remains sharper on the same family and gives `||p_Q||_infinity<=8/L`.

Accordingly, the numerical constants `theta_51=0.017775950827372714` and `3600.36999548` remain correct values from r51 but should not be advertised as an r51 payment for the zero-star Walsh family. No other theorem or calculation in the r34 report is affected.
