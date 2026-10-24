"use strict";
// Exact rational checks for Agent 105. Node.js, no external packages.
// This checks algebraic identities and deterministic obstruction scales;
// it does not certify any random harmonic-matrix theorem.
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){let t=a%b;a=b;b=t;}return a;}
class Q{
 constructor(n,d=1n){n=BigInt(n);d=BigInt(d);if(!d)throw Error("zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=n/g;this.d=d/g;}
 add(o){o=q(o);return new Q(this.n*o.d+o.n*this.d,this.d*o.d);}
 sub(o){o=q(o);return new Q(this.n*o.d-o.n*this.d,this.d*o.d);}
 mul(o){o=q(o);return new Q(this.n*o.n,this.d*o.d);}
 div(o){o=q(o);return new Q(this.n*o.d,this.d*o.n);}
 pow(k){return new Q(this.n**BigInt(k),this.d**BigInt(k));}
 eq(o){o=q(o);return this.n===o.n&&this.d===o.d;}
 le(o){o=q(o);return this.n*o.d<=o.n*this.d;}
 str(){return this.d===1n?String(this.n):String(this.n)+"/"+String(this.d);}
 num(){return Number(this.n)/Number(this.d);}
}
function q(x){return x instanceof Q?x:new Q(x);}
let checks=0;
function assert(test,label){if(!test)throw Error(label);checks++;}
function chiMoment(d,k){let a=q(1);for(let j=0;j<k;j++)a=a.mul(d+2n*BigInt(j));return a;}
function inverseChiMoment(d,k){let a=q(1);for(let j=1;j<=k;j++)a=a.div(d-2n*BigInt(j));return a;}
function radial(d){
 const c2=q(d+2n).div(2),r1=inverseChiMoment(d,1),r2=inverseChiMoment(d,2),r3=inverseChiMoment(d,3),r4=inverseChiMoment(d,4);
 const variance=c2.mul(d*d).mul(r2.sub(r1.pow(2)));
 const fourth=c2.pow(2).mul(d**4n).mul(r4.sub(r1.mul(r3).mul(4)).add(r1.pow(2).mul(r2).mul(6)).sub(r1.pow(4).mul(3)));
 const expectedVariance=q((d+2n)*d*d).div((d-2n)**2n*(d-4n));
 const expectedKurt=q(3n*(d-4n)*(d+10n)).div((d-6n)*(d-8n));
 const fisher=chiMoment(d,4).sub(chiMoment(d,3).mul(2n*(d+2n))).add(chiMoment(d,2).mul((d+2n)**2n)).div(2n*(d+2n)*d*d);
 assert(variance.eq(expectedVariance),"variance");
 assert(fourth.div(variance.pow(2)).eq(expectedKurt),"central fourth");
 assert(fisher.eq(q(1).add(q(6).div(d))),"Fisher");
 assert(q(1).le(variance)&&variance.le(2),"uniform variance");
 assert(fourth.le(48),"uniform fourth");
 return {variance,fourth,fisher,mu2:q(2n*(d+2n)).div((d-2n)**2n)};
}
function obstruction(d,rho){
 const {variance,fourth,fisher,mu2}=radial(d);
 const m=(d-1n)*(d+2n)/2n,beta=q(1).sub(rho).div(m-1n),delta=rho.sub(beta);
 const contraction=delta.pow(2).div(2).add(delta.mul(beta).mul(m).div(d).mul(2)).add(beta.pow(2).mul(m*m).div(d));
 const meanEnergy=mu2.mul(m).mul(rho);
 const meanFourth=meanEnergy.pow(2).div(2),energy=variance.add(meanEnergy);
 assert(rho.add(beta.mul(m-1n)).eq(1),"weight sum");
 assert(q(0).le(delta),"dominant mode");
 assert(contraction.mul(d).le(6),"contraction bound");
 return {d:String(d),m:String(m),rho:rho.str(),d_contraction:contraction.mul(d).num(),mean_energy:meanEnergy.num(),d_mean_fourth_over_total_energy_squared:meanFourth.mul(d).div(energy.pow(2)).num(),fisher:fisher.str(),variance:variance.str(),fourth:fourth.str()};
}
const momentRows=[16n,25n,64n,100n,256n,1024n].map(d=>{const r=radial(d);return {d:String(d),variance:r.variance.str(),fourth:r.fourth.str(),fisher:r.fisher.str()};});
const dominantRows=[4n,8n,16n,32n,64n].map(t=>obstruction(t*t,q(1).div(t)));
const vanishingMeanRows=Array.from({length:8},(_,i)=>{const r=BigInt(i+1);return obstruction(2n**(8n*r),q(1).div(2n**(11n*r)));});
const output={status:"PASS",checks,momentRows,dominantRows,vanishingMeanRows,scope:"Exact rational identities and finite scalar diagnostics only. Probability conclusions are proved in the report."};
if(typeof module!=="undefined")module.exports=output;
if(typeof console!=="undefined")console.log(JSON.stringify(output,null,2));
output;