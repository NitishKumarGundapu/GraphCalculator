#include<stdio.h>
typedef struct {
 int pid;
 int b;
 int t;
 int w;
}pro;

int main()
{
   int n, i, j, ti = 0, tq;
   printf("Round Robin Scheduling\n\n");
   printf("Please enter the number of processes.\t");
   scanf("%d", & n);
   pro p[n], t;
   printf("Enter Process IDs\t");
   for (i = 0; i < n; i++)
   scanf("%d", & p[i].pid);
   printf("Enter Burst Time\t");
   for (i = 0; i < n; i++)
   scanf("%d", & p[i].b);
   printf("Enter time quantum/slice\n");
   scanf("%d", & tq);
   for (i = 0; i < n; i++)
   {
      for (j = 0; j < n; j++)
       {
          if (p[i].b < p[j].b) {
           t = p[i];
           p[i] = p[j];
           p[j] = t;
           }
       }
   }
   for (i = 0; i < n; i++) {
   ti = ti + p[i].b;
   p[i].t = ti;
   p[i].w = p[i].t - p[i].b;
   }
   for (i = 0; i < n; i++){
   for (j = 0; j < n; j++){
   if (p[i].pid < p[j].pid){
   t = p[i];
   p[i] = p[j];
   p[j] = t;}
   }}
   printf("Table\n");
   printf("Process_ID\tBurst_Time\tTurnAroundTime\tWaiting_Time\n");
   for (i = 0; i < n; i++)
    printf("%7d\t\t%7d\t\t%7d\t\t%7d\n", p[i].pid, p[i].b, p[i].t, p[i].w);
   float avgta, avgwt;
   int s1 = 0, s2 = 0;
   for (i = 0; i < n; i++) {
   s1 += p[i].t;
   s2 += p[i].w;
   }
   avgta = (1.0 * s1) / (1.0 * n);
   avgwt = (1.0 * s2) / (1.0 * n);
   printf("Average Turn Around Time : %.2f units\n", avgta);
   printf("Average Waiting Time : %.2f units\n", avgwt);
   return 0;
}
