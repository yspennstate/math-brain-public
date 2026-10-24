// R17-C025 SEARCH ONLY: long-double Perron power iteration for the true h=8 transition table.
// Compile: g++ -O3 -march=native -fopenmp -std=c++17 this.cpp -o search
// C025 command: OMP_NUM_THREADS=8 ./search r17_trans.bin 256717 800000 380 pfld380.bin
// The output vector is only a candidate generator. No theorem inequality relies on floating arithmetic;
// the companion exact cone checker rounds the candidate and recomputes every component ratio exactly.
#include <bits/stdc++.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <omp.h>
using namespace std;
int main(int argc,char**argv){if(argc<6){cerr<<"trans ZN ZD niter out\n";return 2;}string tf=argv[1],out=argv[5];uint64_t ZN=stoull(argv[2]),ZD=stoull(argv[3]);int niter=stoi(argv[4]);const size_t N=6419109;const int deg=30;int fd=open(tf.c_str(),O_RDONLY);struct stat st;fstat(fd,&st);auto*tr=(const uint32_t*)mmap(nullptr,st.st_size,PROT_READ,MAP_SHARED,fd,0);long double z=(long double)ZN/ZD,w[30];int jj=0;for(int c=0;c<2;c++)for(int l=-7;l<=7;l++){int a=abs(l);w[jj++]=(a<7)?powl(z,a+2):powl(z,9)/(1-z);}vector<long double>v(N,1.0L),av(N);long double mn=0,mx=0;for(int it=0;it<niter;it++){mn=LDBL_MAX;mx=-LDBL_MAX;long double vmax=0;
#pragma omp parallel for reduction(min:mn) reduction(max:mx,vmax) schedule(static)
for(long long ii=0;ii<(long long)N;ii++){const uint32_t*row=tr+(size_t)ii*deg;long double s=0;for(int j=0;j<deg;j++){uint32_t q=row[j];if(q)s+=w[j]*v[q-1];}av[ii]=s;long double r=s/v[ii];mn=min(mn,r);mx=max(mx,r);vmax=max(vmax,s);}
#pragma omp parallel for schedule(static)
for(long long ii=0;ii<(long long)N;ii++)av[ii]/=vmax;v.swap(av);if((it+1)%20==0)cerr<<it+1<<" "<<setprecision(22)<<mn<<" "<<mx<<" gap="<<mx-mn<<"\n";}FILE*f=fopen(out.c_str(),"wb");fwrite(v.data(),sizeof(long double),N,f);fclose(f);}
