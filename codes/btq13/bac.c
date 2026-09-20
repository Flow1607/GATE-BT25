#include<stdio.h>
#include<math.h>
double euler(double y){
	return (y+0.01*(log(2)*(y+2)));
}
int main(){
	double y=1;
	double h=0.01;
	double x=0;
	FILE *fp1=fopen("y.dat","w");
	FILE *fp2=fopen("x.dat","w");
	for (int i=0;i<200;i++){	
	fprintf(fp1,"%lf\n",euler(y));
	y=euler(y);
	fprintf(fp2,"%lf\n",x);
	x+=h;

	}
}

