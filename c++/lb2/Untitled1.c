#include <stdio.h>
#include <io.h>
#include <Windows.h>
#include <wincon.h>
#include <conio.h>
#include <locale.h>

int main(void)
{
    setlocale(LC_ALL, "Russian");
    printf("Vvedite '1'ili '0'\n");
    int (a);
    scanf("%d",&a);
    if (a==0){
        FILE *t1=fopen("1.txt","rt");
        FILE *t2=fopen("2.txt","wt");
        while (!feof(t1))
            fputc(fgetc(t1),t2);
            fclose(t1);
            fclose(t2);
            return 0;}
    else{
        FILE *t1=fopen("1.txt","rt");
        FILE *t2=fopen("2.txt","wt");
        while (!feof(t1)){
            int N, i;
            char sl[80];
            fgets(sl, 80, t1);
            N = strlen(sl);
            i = N;
            for (i = N - 1; i > 0; i--)
                if (sl[i] != '\n')
                    fprintf(t2, "%c", sl[i]);
                    fprintf(t2, "%c", sl[0]);
                    fprintf(t2, "%c", '\n');}
    return(0);   }
}
