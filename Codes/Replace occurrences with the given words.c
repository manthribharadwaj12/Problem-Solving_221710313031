//Replace occurrences with the given words
//https://www.geeksforgeeks.org/c-program-replace-word-text-another-given-word/
#include<stdio.h> 
#include<stdlib.h> 
#include<string.h> 
int main() 
{ 
    char string[1010],a[30],b[30];
    scanf ("%s", a);
    scanf ("%s", b);
    fflush (stdin);
    scanf ("%[^\n]s", string);
    char *p;
    p = strtok (string, " ");
    while (p != NULL)
    {
        if (strcmp (a, p) == 0)
        printf ("%s ", b);
        else
        printf ("%s ", p);
        p = strtok (NULL, " ");
    }
return 0;
}



