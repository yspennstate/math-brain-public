// Complete NPN orbit census. Bit x = 1 means f(x) = -1.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <vector>
int main(int argc,char**argv){
 int n=argc>1?atoi(argv[1]):5, N=1<<n;
 if(n<1||n>5)return 2;
 uint64_t count=uint64_t(1)<<(N-1),words=(count+63)/64;
 std::vector<uint64_t> seen(words,0);
 uint32_t full=N==32?~uint32_t(0):(uint32_t(1)<<N)-1;
 std::array<int,5> perm={0,1,2,3,4};
 using Table=std::array<std::array<uint32_t,256>,4>;
 std::vector<Table> tables;
 do{
   Table T={};
   for(int c=0;c<4;c++)for(int v=0;v<256;v++)for(int b=0;b<8;b++)if(v>>b&1){
     int x=c*8+b;if(x>=N)continue;int y=0;
     for(int j=0;j<n;j++)if(x>>j&1)y|=1<<perm[j];
     T[c][v]|=uint32_t(1)<<y;
   }
   tables.push_back(T);
 }while(std::next_permutation(perm.begin(),perm.begin()+n));
 uint32_t low[5]={};for(int j=0;j<n;j++)for(int x=0;x<N;x++)if(!(x>>j&1))low[j]|=uint32_t(1)<<x;
 char name[80];snprintf(name,sizeof(name),"npn%d.bin",n);FILE*out=fopen(name,"wb");
 uint64_t reps=0;auto start=std::chrono::steady_clock::now();
 for(uint64_t wi=0;wi<words;wi++){
   uint64_t allowed=~uint64_t(0);if(wi+1==words&&count%64)allowed=(uint64_t(1)<<(count%64))-1;
   while((seen[wi]&allowed)!=allowed){
     int bit=__builtin_ctzll(~seen[wi]&allowed);uint64_t idx=64*wi+bit;
     uint32_t tt=uint32_t(idx<<1);fwrite(&tt,4,1,out);reps++;
     for(const auto&T:tables){
       uint32_t v=T[0][tt&255]|T[1][tt>>8&255]|T[2][tt>>16&255]|T[3][tt>>24];
       for(int k=0;k<N;k++){
         uint32_t vnorm=(v&1)?v^full:v;uint64_t at=vnorm>>1;
         seen[at>>6]|=uint64_t(1)<<(at&63);
         if(k+1<N){int j=__builtin_ctz(unsigned(k+1)),h=1<<j;v=((v&low[j])<<h)|((v>>h)&low[j]);}
       }
     }
     if(reps%100000==0){fprintf(stderr,"n=%d reps=%llu elapsed_seconds=%.3f\n",n,(unsigned long long)reps,std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count());fflush(stderr);}
   }
 }
 fclose(out);printf("n=%d representatives=%llu bitset_bytes=%llu elapsed_seconds=%.3f\n",n,(unsigned long long)reps,(unsigned long long)(8*words),std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count());
}
