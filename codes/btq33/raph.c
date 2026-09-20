#include<stdio.h>
#include<math.h>
int main(){
	double x=1;
	//Newton raphson iteration
	for (int i=0;i<50;i++){
		//printf("%lf\n",x);
		
		x=x-1+2*exp(-1*x);
	}
	printf("Newton raphson gave %lf\n",x);
}
