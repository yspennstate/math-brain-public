"use strict";
// Agent095: exact rational checks for P24 anchor and ANOVA identities.
// Run with Node.js; no packages or input files are required.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const c=a%b;a=b;b=c;}return a;}
class Q{
  constructor(a,b=1n){a=BigInt(a);b=BigInt(b);if(!b)throw Error("zero denominator");if(b<0n){a=-a;b=-b;}const g=gcd(a,b);this.a=a/g;this.b=b/g;}
  add(x){x=q(x);return new Q(this.a*x.b+x.a*this.b,this.b*x.b);}
  sub(x){x=q(x);return new Q(this.a*x.b-x.a*this.b,this.b*x.b);}
  mul(x){x=q(x);return new Q(this.a*x.a,this.b*x.b);}
  div(x){x=q(x);return new Q(this.a*x.b,this.b*x.a);}
  pow(k){if(k<0)throw Error("negative power");return new Q(this.a**BigInt(k),this.b**BigInt(k));}
  le(x){x=q(x);return this.a*x.b<=x.a*this.b;}
  eq(x){x=q(x);return this.a===x.a&&this.b===x.b;}
  toString(){return this.b===1n?""+this.a:this.a+"/"+this.b;}
}
const q=x=>x instanceof Q?x:new Q(x);
function assert(b,msg){if(!b)throw Error(msg);}
function binom(n,k){if(n<0||k<0||k>n)return 0n;k=Math.min(k,n-k);let z=1n;for(let j=1;j<=k;j++)z=z*BigInt(n-j+1)/BigInt(j);return z;}
function rcoef(m,D,s){return new Q(binom(m-D,s),binom(m-1,s));}
function dcoef(m,D,s){return s===0?q(0):new Q(binom(m-D,s-1),binom(m-1,s));}
let mixtureChecks=0,gaussianChecks=0;
for(let m=3;m<=24;m++){
 const n=m-1;
 for(let D=1;D<=m;D++){
  let R=q(0);for(let s=0;s<=n;s++)R=R.add(rcoef(m,D,s).div(m));
  assert(R.eq(new Q(1n,BigInt(D))),"Gaussian purity");gaussianChecks++;
 }
 for(let noise=2;noise<m;noise++){
  const p=new Q(BigInt(noise),BigInt(4*n)),theta=q(1).sub(p);
  let influence=q(0);
  for(let s=0;s<=n;s++){
   let mixture=q(0);
   for(let h=0;h<n;h++){
    const prob=q(binom(n-1,h)).mul(p.pow(h)).mul(theta.pow(n-1-h));
    mixture=mixture.add(prob.mul(dcoef(m,h+2,s)));
   }
   const deriv=s===0?q(0):q(s).mul(theta.pow(s-1));
   assert(mixture.mul(n).eq(deriv),"Bernstein derivative identity");mixtureChecks++;
   influence=influence.add(q(s).mul(theta.pow(s)).div(m));
  }
  const B=influence.mul(2).div(n);
  assert(new Q(1n,BigInt(8*noise*noise)).le(B),"Gaussian lower q^-2");
  assert(B.le(new Q(32n,BigInt(noise*noise))),"Gaussian upper q^-2");
 }
}
// iid vector columns supported on a centered, non-product three-point law.
// Full rank is not imposed: this checks the generalized expected-nullity theorem.
const support=[[1,0],[0,1],[-1,-1]],m=3;
let mean=Array.from({length:m},()=>Array.from({length:m},()=>q(0)));
let expectedNullity=q(0);
for(const c1 of support)for(const c2 of support)for(const c3 of support){
 const cols=[c1,c2,c3],r0=cols.map(c=>q(c[0])),r1=cols.map(c=>q(c[1]));
 const dot=(a,b)=>a.reduce((s,x,i)=>s.add(x.mul(b[i])),q(0));
 const a=dot(r0,r0),b=dot(r0,r1),c=dot(r1,r1),det=a.mul(c).sub(b.mul(b));
 const P=Array.from({length:m},()=>Array.from({length:m},()=>q(0)));
 let rank;
 if(!det.eq(0)){
  rank=2;
  for(let i=0;i<m;i++)for(let j=0;j<m;j++){
   const hat=c.mul(r0[i]).mul(r0[j]).sub(b.mul(r0[i]).mul(r1[j])).sub(b.mul(r1[i]).mul(r0[j])).add(a.mul(r1[i]).mul(r1[j])).div(det);
   P[i][j]=q(i===j?1:0).sub(hat);
  }
 }else{
  rank=1;const row=!a.eq(0)?r0:r1,den=dot(row,row);
  for(let i=0;i<m;i++)for(let j=0;j<m;j++)P[i][j]=q(i===j?1:0).sub(row[i].mul(row[j]).div(den));
 }
 expectedNullity=expectedNullity.add(new Q(BigInt(m-rank),27n));
 for(let i=0;i<m;i++)for(let j=0;j<m;j++)mean[i][j]=mean[i][j].add(P[i][j].div(27));
}
assert(expectedNullity.eq(new Q(10n,9n)),"expected nullity");
for(let i=0;i<m;i++)for(let j=0;j<m;j++)assert(mean[i][j].eq(i===j?new Q(10n,27n):new Q(-2n,27n)),"mean null projector");
let purity=q(0);for(const row of mean)for(const a of row)purity=purity.add(a.mul(a));
assert(purity.eq(new Q(4n,9n)),"anchor purity");
assert(purity.le(expectedNullity.mul(expectedNullity).div(m-1)),"generalized anchor");
console.log(JSON.stringify({
  mixture_checks:mixtureChecks,
  gaussian_purity_checks:gaussianChecks,
  dimensions:"3 through 24",
  all_integer_noise_scales:true,
  anchor_example:{mean_diagonal:"10/27",mean_off_diagonal:"-2/27",expected_nullity:"10/9",purity:"4/9"},
  result:"PASS"
},null,2));
