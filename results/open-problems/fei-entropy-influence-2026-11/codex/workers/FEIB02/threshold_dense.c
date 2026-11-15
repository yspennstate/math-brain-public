// All thresholds, exact GMP integer recurrences. Final sums use long double.
#include <gmp.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <float.h>
#include <time.h>
typedef mpz_t Z;
static Z tmp;
static long double logarithm(const Z z){
 size_t bits=mpz_sizeinbase(z,2);size_t shift=bits>63?bits-63:0;
 mpz_tdiv_q_2exp(tmp,z,shift);return log2l((long double)mpz_get_ui(tmp))+(long double)shift;
}
static long double ratio(const Z x,const Z y){
 size_t bx=mpz_sizeinbase(x,2),by=mpz_sizeinbase(y,2),sx=bx>63?bx-63:0,sy=by>63?by-63:0;
 mpz_tdiv_q_2exp(tmp,x,sx);long double u=mpz_get_ui(tmp);
 mpz_tdiv_q_2exp(tmp,y,sy);long double v=mpz_get_ui(tmp);
 return ldexpl(u/v,(int)sx-(int)sy);
}
static Z *newrow(int n){Z *a=malloc(n*sizeof(Z));for(int j=0;j<n;j++)mpz_init(a[j]);return a;}
static void clearrow(Z *a,int n){for(int j=0;j<n;j++)mpz_clear(a[j]);free(a);}
static void dimension(int n){
 Z *base=newrow(n),*den=newrow(n),*f=newrow(n),*fn=newrow(n),*q=newrow(n),*qp=newrow(n),*qn=newrow(n);
 Z choose,cum,total,L,num,v,z,m,twom;mpz_inits(choose,cum,total,L,num,v,z,m,twom,NULL);mpz_set_ui(total,1);mpz_mul_2exp(total,total,n);
 long double *A=calloc(n,sizeof(long double)),*B=calloc(n,sizeof(long double)),*G=calloc(n,sizeof(long double));
 mpz_set_ui(choose,1);
 for(int r=0;r<n;r++){
  mpz_bin_uiui(base[r],n-1,r);mpz_set(f[r],base[r]);mpz_set(q[r],base[r]);
  mpz_mul_ui(den[r],base[r],2*n);mpz_mul_2exp(den[r],den[r],n);
  mpz_add(cum,cum,choose);mpz_sub(m,total,cum);if(mpz_cmp(cum,m)<0)mpz_set(m,cum);
  mpz_mul_ui(twom,m,2);long double x=ratio(twom,total);
  mpz_mul_ui(L,base[r],2*n);long double xI=ratio(twom,L);
  long double factor=x<1e-9L?2/logl(2):x==1?0:-2*(1-x)*(1-x)*log1pl(-x)/(x*logl(2));
  B[r]=xI*factor;G[r]=B[r]/2;
  mpz_mul_ui(choose,choose,n-r);mpz_divexact_ui(choose,choose,r+1);
 }
 mpz_set_ui(choose,1);
 for(int k=1;k<=n;k++){
  mpz_mul_ui(choose,choose,n-k+1);mpz_divexact_ui(choose,choose,k);
  for(int r=0;r<n;r++)if(mpz_sgn(f[r])){
   mpz_mul(num,f[r],f[r]);mpz_mul(num,num,choose);mpz_mul_ui(num,num,4);
   long double w=ratio(num,den[r]),lf=1+logarithm(f[r]),lq=logarithm(q[r]);
   A[r]+=w*(n+k-2-lq);B[r]+=w*(lq+n-k+2-2*lf);G[r]+=w*(1+logarithm(base[r])-lf);
  }
  if(k==n)break;
  for(int r=0;r<n;r++){
   mpz_set(fn[r],f[r]);if(r){mpz_sub(fn[r],fn[r],f[r-1]);mpz_sub(fn[r],fn[r],fn[r-1]);}
   if(k==1){mpz_set(qn[r],q[r]);continue;}
   mpz_set(v,q[r]);if(r){mpz_mul_ui(z,q[r-1],2);mpz_add(v,v,z);}if(r>1)mpz_add(v,v,q[r-2]);mpz_mul_ui(v,v,2*k-1);
   mpz_set(z,qp[r]);if(r){mpz_mul_ui(m,qp[r-1],2);mpz_sub(z,z,m);}if(r>1)mpz_add(z,z,qp[r-2]);mpz_mul_ui(z,z,k-1);mpz_sub(v,v,z);
   if(!mpz_divisible_ui_p(v,k)){fprintf(stderr,"division failed %d %d %d\n",n,k,r);exit(2);}mpz_divexact_ui(qn[r],v,k);
   if(r){mpz_mul_ui(z,qn[r-1],2);mpz_sub(qn[r],qn[r],z);}if(r>1)mpz_sub(qn[r],qn[r],qn[r-2]);
   if(mpz_sgn(qn[r])<0){fprintf(stderr,"negative Q\n");exit(3);}
  }
  Z *swap=f;f=fn;fn=swap;swap=qp;qp=q;q=qn;qn=swap;
 }
 long double *vals[]={A,B,G};const char *names[]={"A/I","B/I","Gamma/I"};
 printf("{\"n\":%d,\"maxima\":{",n);
 for(int z=0;z<3;z++){
  int r=0;for(int j=1;j<n;j++)if(vals[z][j]>vals[z][r])r=j;
  printf("%s\"%s\":{\"value\":%.18Lg,\"threshold\":%d}",z?",":"",names[z],vals[z][r],r+1);
 }
 printf("},\"central_threshold\":{\"r\":%d,\"A/I\":%.18Lg,\"B/I\":%.18Lg,\"Gamma/I\":%.18Lg}}\n",n/2+1,A[n/2],B[n/2],G[n/2]);fflush(stdout);
 clearrow(base,n);clearrow(den,n);clearrow(f,n);clearrow(fn,n);clearrow(q,n);clearrow(qp,n);clearrow(qn,n);
 mpz_clears(choose,cum,total,L,num,v,z,m,twom,NULL);free(A);free(B);free(G);
}
int main(int argc,char **argv){mpz_init(tmp);int first=argc>1?atoi(argv[1]):1,last=argc>2?atoi(argv[2]):first;for(int n=first;n<=last;n++)dimension(n);mpz_clear(tmp);return 0;}
