#include<stdio.h>
#include<conio.h>
void main()
{
char r1[100],s2[100];
int res;
clrscr();
printf("Enter r1 and r2:");
gets(r1);
gets(r2);
res=strcmp(r1,r2);
if(res==0)
printf("Strings are equal");
else
printf("Strings are not equal");
getch();
}
int strcmp(char *r1,char *r2)
{
int i=0;
while(r1[i]!='\0'||r2[i]!='\0')
{
if(r1[i]!=r2[i])
return (r2[i]-r1[i]);
i++;
}
return 0;
}
