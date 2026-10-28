import Lean.Elab.Tactic.Omega

theorem a017_rank_refund (r rp rm e ep em : Int)
    (hp : rp <= r) (hm : rm <= r) :
    (2 * (r + e) - (rp + ep) - (rm + em) - (2 * r - rp - rm)
        = 2 * e - ep - em) ∧
    (0 <= 2 * r - rp - rm) ∧
    (2 * e - ep - em <= 2 * (r + e) - (rp + ep) - (rm + em)) := by
  omega
