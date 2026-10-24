import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

set_option maxRecDepth 20000
set_option maxHeartbeats 4000000

-- Exact arithmetic checks only; the analytic comparison is proved in ATTEMPT.md.
def pc (x : Nat) : Nat := (Finset.range 5).sum fun i => if x / 2^i % 2 = 1 then 1 else 0

def pairFunction (edges : List Nat) (x : Nat) : Int :=
  if pc x >= 4 then 1
  else if pc x = 3 then (if edges.contains (31-x) then -1 else 1)
  else if pc x = 2 then (if edges.contains x then 1 else -1)
  else -1

def overlap (x s : Nat) : Nat :=
  (Finset.range 5).sum fun i =>
    if And (x / 2^i % 2 = 1) (s / 2^i % 2 = 1) then 1 else 0

def character (x s : Nat) : Int := if overlap x s % 2 = 0 then 1 else -1

def coefficient (edges : List Nat) (s : Nat) : Int :=
  (Finset.range 32).sum fun x => pairFunction edges x * character x s

def level (edges : List Nat) (k : Nat) : Int :=
  (Finset.range 32).sum fun s => if pc s = k then (coefficient edges s)^2 else 0

def spectrum (edges : List Nat) : List Int := (List.range 6).map (level edges)

theorem majority_spectrum : spectrum [] = [0,720,0,160,0,144] := by decide +kernel
theorem one_pair_spectrum : spectrum [3] = [0,704,0,256,0,64] := by decide +kernel
theorem two_star_spectrum : spectrum [3,5] = [0,720,0,288,0,16] := by decide +kernel
theorem three_star_spectrum : spectrum [3,5,9] = [0,768,0,256,0,0] := by decide +kernel
theorem triangle_spectrum : spectrum [3,5,6] = [0,768,0,256,0,0] := by decide +kernel
theorem four_star_spectrum : spectrum [3,5,9,17] = [0,848,0,160,0,16] := by decide +kernel

-- Identities controlling the single turning point of squared derivative ratios.
theorem g_turn (t : Rat) :
  -(11+12*t+5*t^2)^2 + 2*(1-t)*(11+12*t+5*t^2)*(12+10*t)
  = (11+12*t+5*t^2)*(13-16*t-25*t^2) := by ring

theorem m_turn (t : Rat) :
  -(45+30*t+45*t^2)^2 + 2*(1-t)*(45+30*t+45*t^2)*(30+90*t)
  = (45+30*t+45*t^2)*(15+90*t-225*t^2) := by ring

theorem two_star_gap (r : Rat) :
  (45*r+18*r^3+r^5) - (44*r+16*r^3+4*r^5)
  = r*(1-r^2)*(1+3*r^2) := by ring

theorem maj3_gap (r : Rat) :
  (48*r+16*r^3) - (44*r+16*r^3+4*r^5)
  = 4*r*(1-r^2)*(1+r^2) := by ring

theorem four_star_gap (r : Rat) :
  (53*r+10*r^3+r^5) - (44*r+16*r^3+4*r^5)
  = 3*r*(1-r^2)*(3+r^2) := by ring

theorem dictator_gap (r : Rat) :
  64*r - (44*r+16*r^3+4*r^5)
  = 4*r*(1-r^2)*(5+r^2) := by ring
