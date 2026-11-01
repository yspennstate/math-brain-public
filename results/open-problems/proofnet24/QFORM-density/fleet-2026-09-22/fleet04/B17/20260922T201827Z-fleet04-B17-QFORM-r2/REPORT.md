SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B17, 2026-09-22T20:18:27Z.

# QFORM-EDGEWORTH-FRAME-DEFICIT-SHARP-v1

Run: \`20260922T201827Z-fleet04-B17-QFORM-r2\`  
Classification: **PROVED SUPPORTING LEMMA / SHARP WITNESS CONSTRAINT**  
Full conjecture: **OPEN / NOT PROVED**  
Continuity for the full conjecture: **OPEN**

## Result

Let \(J=\operatorname{diag}(1,1,-1)\). Let \(v_1,\ldots,v_r\in\mathbb R^3\) be a tight frame,
\[
\sum_{j=1}^r v_jv_j^\top=I_3.
\]
Write
\[
s_j=v_{j1}^2+v_{j2}^2,\qquad t_j=v_{j3}^2
\]
and use the fleet01/B17 Edgeworth cone polynomial
\[
E_J(v_j)=\frac{57}{32}s_j^2+\frac{15}{4}s_jt_j+\frac34t_j^2.
\]
Then
\[
\boxed{
\sum_{j=1}^rE_J(v_j)
\ge \frac{\kappa_*}{r}
+\gamma_*\sum_{j=1}^r s_jt_j,
}
\]
where
\[
\kappa_*=
\left(2\sqrt{\frac{57}{32}}+\sqrt{\frac34}\right)^2
=\frac{63}{8}+\sqrt{\frac{171}{8}}
=12.4983105022\ldots
\]
and
\[
\gamma_*=\frac{15}{4}-2\sqrt{\frac{57}{32}\frac34}
=\frac{15}{4}-\sqrt{\frac{171}{32}}
=1.4383447488\ldots>0.
\]
In particular,
\[
\boxed{\sum_jE_J(v_j)\ge\kappa_*/r.}
\]
This strengthens the previous orientation-free lower bound \(27/(4r)=6.75/r\) by a factor \(1.8516\ldots\). It also isolates a strictly positive penalty for every physical row loading both the positive and negative spectral sectors.

## Proof

Put
\[
u=\sqrt{57/32},\qquad v=\sqrt{3/4}.
\]
For every \(s,t\ge0\),
\[
\begin{aligned}
E(s,t)
&=\frac{57}{32}s^2+\frac{15}{4}st+\frac34t^2\\
&=(us+vt)^2+\left(\frac{15}{4}-2uv\right)st\\
&=(us+vt)^2+\gamma_*st.
\end{aligned}
\]
The coefficient \(\gamma_*>0\), because
\[
(15/4)^2>4(57/32)(3/4).
\]
The tight-frame identity gives
\[
\sum_js_j=2,\qquad \sum_jt_j=1.
\]
Therefore Cauchy--Schwarz gives
\[
\sum_j(us_j+vt_j)^2
\ge \frac1r\left(\sum_j(us_j+vt_j)\right)^2
=\frac{(2u+v)^2}{r}
=\frac{\kappa_*}{r}.
\]
Adding the exact nonnegative mixed-sector term proves the theorem. No probabilistic or post-rotation independence assertion enters this inequality.

## Application of the completed fleet01/B17 theorem

The designated partner proved the following fixed-pattern expansion for independent \(\operatorname{Uniform}[-1/2,1/2]\) physical coordinates. Repeat the frame pattern \(m\) times, with rows \(v_j/\sqrt m\), set \(U_m^\top U_m=I_3\), \(A_m=U_mJU_m^\top\), and \(Q_m=X^\top A_mX\). Then
\[
p_{Q_m}(0)
=3\sqrt2\left[
1-\frac1{20m}\sum_jE_J(v_j)+O(m^{-2})
\right].
\]
Every finite \(A_m\) has exact nonzero spectrum \(\{1,1,-1\}\), so this is a target-admissible genuinely rotated stress family whenever the frame is not axis-aligned.

Applying the proved inequality yields
\[
\boxed{
p_{Q_m}(0)
\le 3\sqrt2\left[
1-\frac{\kappa_*}{20rm}
-\frac{\gamma_*}{20m}\sum_js_jt_j
+O(m^{-2})
\right].
}
\]
Writing \(n=rm\), the orientation-free first-order deficit is
\[
\boxed{
p_{Q_m}(0)
\le3\sqrt2\left[
1-\frac{0.6249155251\ldots}{n}
+O(n^{-2})
\right]
}
\]
for each fixed frame pattern. The earlier coefficient was only \(27/80=0.3375\).

Mixed-sign loading in a physical row carries the additional penalty
\[
\frac{\gamma_*}{20m}\sum_js_jt_j.
\]
Thus, within this periodic diffuse-cube class, rotating individual physical rows across the positive and negative eigenspaces cannot improve the leading correction toward a witness above \(3\sqrt2\); it makes the correction more negative unless every row lies wholly in one sign sector.

## Sharpness of the coefficient

The constant \(\kappa_*\) is asymptotically sharp among tight frames as the pattern size grows. Split the rows into \(r_+\) rows in the positive plane and \(r_-\) rows on the negative axis. Choose an equal-norm tight frame in the positive plane, so each positive row has
\[
s=2/r_+,\qquad t=0,
\]
and take \(r_-\) copies of \(\pm e_3/\sqrt{r_-}\), so each negative row has
\[
s=0,\qquad t=1/r_-.
\]
Then
\[
\sum_jE_J(v_j)=\frac{57}{8r_+}+\frac{3}{4r_-}.
\]
Over positive real \(r_+,r_-\) with \(r_++r_-=r\), the minimum occurs at
\[
\frac{r_+}{r_-}
=\sqrt{\frac{57/8}{3/4}}
=\sqrt{\frac{19}{2}},
\]
and equals \(\kappa_*/r\). Choosing integer counts nearest this ratio gives
\[
\sum_jE_J(v_j)=\frac{\kappa_*}{r}+O(r^{-2}).
\]
Thus the coefficient cannot be increased uniformly in \(r\). Equality in the pointwise decomposition forces \(s_jt_j=0\); equality in Cauchy forces \(us_j+vt_j\) constant. These are precisely the sign-segregated equality conditions, up to the integer-count obstruction.

## Hadamard check

For the four-row Hadamard frame, every row has \(s=1/2\), \(t=1/4\). Hence
\[
\sum_jE_J(v_j)=123/32.
\]
The refined identity gives
\[
\sum_jE_J(v_j)=\kappa_*/4+\gamma_*/2=123/32
\]
exactly. Cauchy is an equality because \(us_j+vt_j\) is constant across the rows; the entire gap from the optimal sign-segregated frame is the mixed-sector penalty.

## Scope and remaining problem

This theorem does not improve the already proved target lower bound \(C\ge3\sqrt2\) and does not prove that \(3\sqrt2\) is the sharp universal constant. It closes a witness mechanism: no fixed periodic diffuse uniform-cube frame can exceed the Gaussian ceiling through its first non-Gaussian correction, and sign-mixing rotation makes that correction strictly worse.

A witness above \(3\sqrt2\), if one exists, must use a mechanism outside this fixed-pattern Edgeworth neighborhood: mesoscopic/nonperiodic geometry, non-uniform density-one supports, non-infinitesimal leverage, or a finite-row spike not represented by the expansion. The full arbitrary-law upper bound remains open.

Only densities in the partner's stated periodic uniform-cube family are used here. No Gaussian, log-concavity, moment, post-rotation independence, pointwise Fourier decay, fiber-supremum, or conditional-projection-cap hypothesis is inserted into the full conjecture.

## Source pins

- Partner theorem: \`yspennstate/math-open-problems@755c11cf5ac40926bc86827a88395a6be2ef953d\`, \`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260922T123638Z-fleet01-B17-qform-diffuse-edgeworth-v1/REPORT.md\`.
- Partner Gaussian ceiling: \`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260922T120821Z-fleet01-B17-qform-sharp-constant-v1/ADDENDUM_NONCENTRAL_GAUSSIAN.md\`.
- Final control refresh: revision \`2026-09-22.15\`, README blob \`fca13a89d221115332ce5e60d49554ee0e213efa\`.
- Final correction refresh: blob \`c7000cf3822ae4935a2faf43b89ac92ea65ac0fe\`.

Repository use is separate from native brain ingestion. Status: \`WITHOUT_VERIFIED_BRAIN\`.
