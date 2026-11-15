"""Base-2 logs of positive terms, including values below binary64 range."""
import math
LN2=math.log(2);LOGLN2=math.log2(LN2)
def add(x,y):
 if x is None:return y
 if y is None:return x
 a,b=max(x,y),min(x,y)
 return a+math.log1p(2.**(b-a))/LN2

def log_log_ratio(diff,den):
 """log2(log2(1+diff/den)); None for exact zero."""
 if not diff:return None
 assert diff>0 and den>0
 q=math.log2(diff)-math.log2(den)
 if q<-50:return q-LOGLN2
 if q>50:return math.log2(q)
 return math.log2(math.log1p(2.**q)/LN2)

def log_neg_log_dyadic(num,bits):
 """log2(-log2(num/2**bits)); None for exact one."""
 den=1<<bits
 assert 0<num<=den
 if num==den:return None
 if 2*num<=den:return math.log2(bits-math.log2(num))
 q=math.log2(den-num)-bits
 if q<-50:return q-LOGLN2
 return math.log2(-math.log1p(-2.**q)/LN2)
