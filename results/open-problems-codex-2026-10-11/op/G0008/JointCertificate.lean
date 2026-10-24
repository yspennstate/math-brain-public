import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

-- Kernel checks the finite integer comparison certificate, not the graph DP.
def jointCoefficients : List Int := [4,148,2640,30160,247338,1547512,7667748,30845208,102524812,285288204,671510680,1348925352,2332160230,3501939952,4616183220,5410569388,5718734248,5518012068,4888609184,3959929024,2894507102,1876414204,1061430556,517519260,215651364,76294772,22754084,5664400,1159528,190720,24300,2256,136,4]
def binomialBaseline : List Int := [4,132,2112,21824,163680,949344,4430272,17088192,55536624,154268400,370244160,774146880,1419269280,2292665760,3275236800,4148633280,4667212440,4667212440,4148633280,3275236800,2292665760,1419269280,774146880,370244160,154268400,55536624,17088192,4430272,949344,163680,21824,2112,132,4]
theorem joint_certificate_lengths :
    jointCoefficients.length = 34 /\ binomialBaseline.length = 34 := by
  decide +kernel

theorem joint_integer_certificate :
    (jointCoefficients.zip binomialBaseline).all
      (fun ab => decide (ab.2 <= ab.1)) = true := by
  decide +kernel

theorem join_kernel_obstruction (q : Real) (hlo : 1 < q) (hhi : q < 2) :
    q * (q-1) * (q-2) < 0 := by
  have hq : 0 < q := by linarith
  exact mul_neg_of_pos_of_neg (mul_pos hq (sub_pos.mpr hlo)) (sub_neg.mpr hhi)

#print axioms joint_integer_certificate
#print axioms join_kernel_obstruction
