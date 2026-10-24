// R17-C027 SEARCH-ONLY recipe.
// Input: the already independently validated Lueker h=8 transition table
//        (6,419,109 rows x 30 uint32 destinations), whose SHA-256 is
//        c6d12e75e87b7c6b00a95f0c7f3580fa1cdee4996ce690a2f922f7eaeea1fbd1.
// Output: a positive double vector used only as a candidate for the exact checker.
// No floating-point inequality produced here is part of the theorem.
//
// Search path used in C027:
//   (i) 600 scalar power steps near the C026 scalar optimum;
//   (ii) floor that direction at scale 18e18 (matching the scalar warm start);
//   (iii) 40 bivariate power steps at x=256701/800000, y=256733/800000;
//   (iv) one Aitken-style extrapolation u = v + 9(v-v_prev);
//   (v) 20 further bivariate power steps;
//   (vi) write the positive double vector.  The companion exact checker then
//        freezes/rounds it and checks every row with exact integer arithmetic.

#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
using namespace std;

int main(int argc,char**argv){
    if(argc<3){cerr<<"usage: search_recipe h8_transition_table.bin candidate_double.bin\n"; return 2;}
    const string tf=argv[1], out=argv[2];
    const size_t N=6419109; const int deg=30;
    int fd=open(tf.c_str(),O_RDONLY); if(fd<0){perror("open");return 3;}
    struct stat st; fstat(fd,&st);
    if((size_t)st.st_size!=N*(size_t)deg*4){cerr<<"bad transition-table size\n";return 4;}
    auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);
    if(tr==MAP_FAILED){perror("mmap");return 5;}

    // Scalar warm start.  Search only.
    const long double z0=0.320896250000000001555829L;
    long double ws[30]; int jj=0;
    for(int c=0;c<2;c++) for(int l=-7;l<=7;l++){
        int a=abs(l); ws[jj++]=(a<7)?powl(z0,a+2):powl(z0,9)/(1-z0);
    }
    vector<long double> vl(N,1.0L), al(N);
    for(int it=0;it<600;it++){
        long double vmax=0;
        #pragma omp parallel for reduction(max:vmax) schedule(static)
        for(long long ii=0;ii<(long long)N;ii++){
            const uint32_t*row=tr+(size_t)ii*deg; long double s=0;
            for(int j=0;j<deg;j++){uint32_t q=row[j];if(q)s+=ws[j]*vl[q-1];}
            al[ii]=s; vmax=max(vmax,s);
        }
        #pragma omp parallel for schedule(static)
        for(long long ii=0;ii<(long long)N;ii++) al[ii]/=vmax;
        vl.swap(al);
    }
    const uint64_t SCALE=18000000000000000000ULL;
    vector<uint64_t> V0(N); uint64_t V0max=0;
    for(size_t i=0;i<N;i++){
        long double q=floorl(vl[i]*(long double)SCALE); if(q<1)q=1;
        V0[i]=(uint64_t)q; V0max=max(V0max,V0[i]);
    }

    // Bivariate diagonal tilt.
    const double x=256701.0/800000.0, y=256733.0/800000.0;
    double w[30]; jj=0;
    for(int c=0;c<2;c++) for(int l=-7;l<=7;l++){
        double ww;
        if(l==0) ww=x*y;
        else if(l>0 && l<7) ww=pow(x,l+1)*y;
        else if(l<0 && -l<7) ww=x*pow(y,-l+1);
        else if(l==7) ww=pow(x,8)*y/(1-x);
        else ww=x*pow(y,8)/(1-y);
        w[jj++]=ww;
    }
    vector<double> v(N), a(N), prev(N);
    #pragma omp parallel for schedule(static)
    for(long long i=0;i<(long long)N;i++) v[i]=(double)V0[i]/(double)V0max;

    auto step=[&](){
        double vmax=0;
        #pragma omp parallel for reduction(max:vmax) schedule(static)
        for(long long ii=0;ii<(long long)N;ii++){
            const uint32_t*row=tr+(size_t)ii*deg; double s=0;
            for(int j=0;j<deg;j++){uint32_t q=row[j];if(q)s+=w[j]*v[q-1];}
            a[ii]=s; vmax=max(vmax,s);
        }
        #pragma omp parallel for schedule(static)
        for(long long ii=0;ii<(long long)N;ii++) a[ii]/=vmax;
        v.swap(a);
    };

    for(int it=0;it<40;it++){ prev=v; step(); }
    #pragma omp parallel for schedule(static)
    for(long long i=0;i<(long long)N;i++){
        double q=v[i]+9.0*(v[i]-prev[i]);
        if(q<=0) q=numeric_limits<double>::min();
        v[i]=q;
    }
    double renorm=*max_element(v.begin(),v.end());
    #pragma omp parallel for schedule(static)
    for(long long i=0;i<(long long)N;i++) v[i]/=renorm;
    for(int it=0;it<20;it++) step();

    FILE*f=fopen(out.c_str(),"wb");
    if(!f||fwrite(v.data(),sizeof(double),N,f)!=N){cerr<<"write fail\n";return 6;}
    fclose(f);
    munmap((void*)tr,st.st_size); close(fd);
    return 0;
}
