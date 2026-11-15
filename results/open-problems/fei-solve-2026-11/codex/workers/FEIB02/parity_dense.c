// Dense all-dimension parity-times-threshold census via exact Pascal updates.
// At fixed k: L(n,k,r)=L(n-1,k,r)+L(n-1,k,r-1), and likewise Q.
// Reflection r -> n-r+1 halves storage. At n=k, L=|F_threshold,0|, Q=L^2.
#include <gmp.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
typedef mpz_t Z;
static Z scratch;
static double lz(const Z x){
 size_t b=mpz_sizeinbase(x,2),s=b>63?b-63:0;mpz_tdiv_q_2exp(scratch,x,s);
 return log2((double)mpz_get_ui(scratch))+(double)s;
}
static double logadd(double a,double b){if(isinf(a))return b;if(isinf(b))return a;double hi=fmax(a,b),lo=fmin(a,b);return hi+log1p(exp2(lo-hi))/log(2.);}
static double loglogratio(const Z difference,const Z den){
 if(!mpz_sgn(difference))return -INFINITY;
 if(mpz_sgn(difference)<0){fprintf(stderr,"negative log ratio difference\n");exit(5);}
 double t=lz(difference)-lz(den);
 if(t<-50)return t-log2(log(2.));if(t>50)return log2(t);
 return log2(log1p(exp2(t))/log(2.));
}
static double logneglogdyadic(const Z num,int bits,Z delta){
 mpz_set_ui(delta,1);mpz_mul_2exp(delta,delta,bits);mpz_sub(delta,delta,num);
 if(!mpz_sgn(delta))return -INFINITY;
 if(mpz_sgn(delta)<0){fprintf(stderr,"Q exceeds dyadic scale\n");exit(6);}
 if(mpz_sizeinbase(num,2)<=(size_t)(bits-1))return log2(bits-lz(num));
 double t=lz(delta)-bits;if(t<-50)return t-log2(log(2.));
 return log2(-log1p(-exp2(t))/log(2.));
}
static void print_metric(const char*name,double logv,int r,int comma){
 printf("%s\"%s\":{\"value\":%.17g,\"log2_value\":%.17g,\"threshold\":%d}",comma?",":"",name,exp2(logv),logv,r);
}
int main(int argc,char **argv){
 int M=argc>1?atoi(argv[1]):2000;int first=argc>2?atoi(argv[2]):2;if(M<2||M>2000)return 2;int width=(M+1)/2;
 // Final allocation estimate <= 1.7 GiB for M=2000, before starting allocation.
 uint64_t estimate=0;
 for(int k=1;k<=M;k++)estimate+=(uint64_t)width*(2*sizeof(Z)+48+(M+7)/8+(M+k+7)/8);
 fprintf(stderr,"matrix_allocation_estimate_bytes=%llu\n",(unsigned long long)estimate);fflush(stderr);
 if(estimate>2500ULL*1024*1024)return 3;
 Z **L=calloc(M+1,sizeof(Z*)),**Q=calloc(M+1,sizeof(Z*));
 mpz_init(scratch);
 Z total,prevtotal,choose,cum,base,den,num,delta,square,R,temp,fzero;
 mpz_inits(total,prevtotal,choose,cum,base,den,num,delta,square,R,temp,fzero,NULL);
 Z *f=malloc(width*sizeof(Z)),*fn=malloc(width*sizeof(Z)),*de=malloc(width*sizeof(Z)),*zer=malloc(width*sizeof(Z));
 for(int r=0;r<width;r++){mpz_init(f[r]);mpz_init(fn[r]);mpz_init(de[r]);mpz_init(zer[r]);}
 double *A=malloc(width*sizeof(double)),*B=malloc(width*sizeof(double)),*G=malloc(width*sizeof(double));
 int prevm=0;
 for(int n=1;n<=M;n++){
  int m=(n+1)/2;mpz_set_ui(total,1);mpz_mul_2exp(total,total,n);mpz_fdiv_q_2exp(prevtotal,total,1);
  // Allocate only the newly appearing row; each mpz has a fixed sufficient capacity.
  L[n]=malloc(width*sizeof(Z));Q[n]=malloc(width*sizeof(Z));
  for(int r=0;r<width;r++){mpz_init2(L[n][r],M+2);mpz_init2(Q[n][r],M+n+2);}
  for(int k=1;k<n;k++)for(int j=m-1;j>=0;j--){
   if(j>=prevm){mpz_mul_2exp(L[k][j],L[k][j-1],1);mpz_mul_2exp(Q[k][j],Q[k][j-1],1);}
   else if(j){mpz_add(L[k][j],L[k][j],L[k][j-1]);mpz_add(Q[k][j],Q[k][j],Q[k][j-1]);}
   else {mpz_add(L[k][0],L[k][0],prevtotal);mpz_mul_2exp(temp,prevtotal,k);mpz_add(Q[k][0],Q[k][0],temp);}
  }
  // New diagonal and initial Fourier row. f[r] here excludes its common factor 2.
  mpz_set_ui(choose,1);mpz_set_ui(cum,0);
  for(int j=0;j<m;j++){
   mpz_add(cum,cum,choose);mpz_mul_ui(temp,cum,2);mpz_sub(zer[j],temp,total);mpz_abs(L[n][j],zer[j]);mpz_mul(Q[n][j],L[n][j],L[n][j]);
   mpz_bin_uiui(base,n-1,j);mpz_set(f[j],base);if(j%2)mpz_neg(f[j],f[j]);
   mpz_mul_ui(temp,base,2);mpz_sub(temp,total,temp);mpz_mul_ui(de[j],temp,n);mpz_mul_2exp(de[j],de[j],n);
   A[j]=B[j]=G[j]=-INFINITY;
   mpz_mul_ui(choose,choose,n-j);mpz_divexact_ui(choose,choose,j+1);
  }
  prevm=m;if(n==1||n<first)continue; // parity times a 1-variable threshold is constant.
  mpz_set_ui(choose,1);
  for(int k=0;k<=n;k++){
   if(k){mpz_mul_ui(choose,choose,n-k+1);mpz_divexact_ui(choose,choose,k);}
   for(int j=0;j<m;j++){
    if(k<n)mpz_mul_ui(num,f[j],2);else mpz_set(num,zer[j]);
    if(!mpz_sgn(num))continue;
    mpz_mul(square,num,num);mpz_mul(temp,square,choose);double lw=lz(temp)-lz(de[j]);
    mpz_abs(den,num);
    double la,lb,lg;
    if(!k){
     la=-INFINITY;mpz_mul(R,total,total);mpz_sub(delta,R,square);lb=loglogratio(delta,square);mpz_sub(delta,total,den);lg=loglogratio(delta,den);
    }else{
     la=logneglogdyadic(Q[k][j],n+k,delta);
     mpz_mul_2exp(R,Q[k][j],n-k);mpz_sub(delta,R,square);lb=loglogratio(delta,square);
     mpz_sub(delta,L[k][j],den);lg=loglogratio(delta,den);
    }
    if(!isinf(la))A[j]=logadd(A[j],lw+la);
    if(!isinf(lb))B[j]=logadd(B[j],lw+lb);
    if(!isinf(lg))G[j]=logadd(G[j],lw+lg);
   }
   if(k<n-1){
    for(int j=0;j<m;j++){mpz_set(fn[j],f[j]);if(j){mpz_add(fn[j],fn[j],f[j-1]);mpz_add(fn[j],fn[j],fn[j-1]);}}
    Z*sw=f;f=fn;fn=sw;
   }
  }
  int ia=0,ib=0,ig=0;for(int j=1;j<m;j++){if(A[j]>A[ia])ia=j;if(B[j]>B[ib])ib=j;if(G[j]>G[ig])ig=j;}
  printf("{\"n\":%d,\"maxima\":{",n);print_metric("A/I",A[ia],ia+1,0);print_metric("B/I",B[ib],ib+1,1);print_metric("Gamma/I",G[ig],ig+1,1);
  printf("},\"central_threshold\":{\"r\":%d,\"A/I\":%.17g,\"B/I\":%.17g,\"Gamma/I\":%.17g}}\n",n/2+1,exp2(A[m-1]),exp2(B[m-1]),exp2(G[m-1]));fflush(stdout);
 }
 for(int k=1;k<=M;k++){for(int j=0;j<width;j++){mpz_clear(L[k][j]);mpz_clear(Q[k][j]);}free(L[k]);free(Q[k]);}free(L);free(Q);
 for(int j=0;j<width;j++){mpz_clear(f[j]);mpz_clear(fn[j]);mpz_clear(de[j]);mpz_clear(zer[j]);}free(f);free(fn);free(de);free(zer);free(A);free(B);free(G);
 mpz_clears(total,prevtotal,choose,cum,base,den,num,delta,square,R,temp,fzero,scratch,NULL);
 return 0;
}
