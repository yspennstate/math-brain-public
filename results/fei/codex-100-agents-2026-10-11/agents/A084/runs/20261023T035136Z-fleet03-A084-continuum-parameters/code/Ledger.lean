import Std
namespace A084
theorem shifted_credit (r0 r1 a b : Int) :
    2*r0+2*(a+b)-(r0+r1) = (2*r0+2*a-(r0+r1))+2*b := by omega
theorem conserved_credit (r0 r1 a : Int) :
    (2*r0+2*a-(r0+r1))+(2*r1+2*a-(r0+r1))=4*a := by omega
end A084
#print axioms A084.shifted_credit
#print axioms A084.conserved_credit
