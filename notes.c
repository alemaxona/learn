// Ручное компилирование 
// Из cmd: gcc myFile.c -o myFile.exe

# include <stdio.h> // По сути подключения файла с функциями 
// include (подключить) - деректива препроцессора / 
 // <stdio.h> (Заголовочный файл) - standart input output . headers
 // h (headers - заголовки) 

// Тип char от -128 до +127
// Из таблицы ASCII:
// Символ  буква А = 65 в десятичной системе
// Поэтому char сможет иметь только один знак буква А,
// так как 65 + 65 > 127!
// Также невозможно иметь число, например дробное - 5,2, или десятичное - 300!
// char и signed char  - Почти Один и тот же тип. signed(со знаком)
// unsigned char - без знака. То есть от 0 до 255.
char a = 'a'; // В основном используем для символов
unsigned char b = 125; // В основном используем для цифр

// short int или short: от 32  от −32767 до +32767
// signed short int или signed short: от −32767 до +32767
// unsigned short int или unsigned short: от 0 до +65535

// Маркеры вывода
printf ("%d", 10);
// %d - десятичные цифры(decimal)
// %c - символьные знаки(char)
// %i  - десятичные числа (до 2 мирд.)
// %s - строки (string)

// main - основная/главная
void main() {  // void - пустота, ничего не возвращает!
    return;
}

// Если параметров нет, то желательно указывать void
void main(void) {  // void - пустота, ничего не передаем и не возвращаем!
    return;
}


#include <stdio.h>
int main()
{
    float num1 = 5;
    float num2 = 9; 
    printf ("Helo world!\n%.0f / %.0f = %.3f\n", num1, num2, num1 / num2);
    return 0;
    getchar();
}

// #define определяет символьное имя, или именованную константу, для заданной строки символов:
#define MAX = 300 // именованные константы, а не переменные, поэтому для них нет объявлений.
// То есть мы назвали число 300 словом - MAX



// Homme work
// Б. Керниган, Д. Ритчи. Язык программирования Си:
// Дочитать Главу 1
// Прочитать главу 2 до 2.4 включительно
// Изучить escape-последовательности в 2.3
// Изучить <limits.h> и <float.h>
// Опытным путем выяснить сколько байт в VSC занимают типы:
//  char, short int, long int, long long, long double
// (Опционально) Написать программу, выводящую на экран самое большое число из базовых типов.
// #include <stdio.h>
// #include <limits.h>

// int main() {
//     unsigned int i = UINT_MAX;

//     printf("UINT_MAX = %u\n", i);
//     printf("UINT_MAX + 1 = %u\n", i + 1);

//     return 0;
// }

#include <stdio.h>
#include <limits.h>

int main() {
    
    char c = CHAR_MAX;
    short int si = SHRT_MAX;
    int i = INT_MAX;
    long int li = LONG_MAX; 
    long long ll = LLONG_MAX;
    long double ld = __LDBL_MAX__;

    // char
    printf("CHAR_MAX = %d\n", c);
    printf("CHAR_MAX + 1 = %d\n", c + 1);

    // shrot int
    printf("SHRT_MAX = %hi\n", si);
    printf("SHRT_MAX + 1 = %hi\n", si + 1);

    // int
    printf("INT_MAX = %i\n", i);
    printf("INT_MAX + 1 = %i\n", i + 1);

    // long int
    printf("LONG_MAX = %ld\n", li);
    printf("LONG_MAX + 1 = %ld\n", li + 1);

    // long long
    printf("LLONG_MAX = %lld\n", c);
    printf("LLONG_MAX + 1 = %lld\n", c + 1);

    // double long
    printf("LDBL_MAX = %Le\n", c);
    printf("LDBL_MAX + 1 = %Le\n", c + 1);

    // EOF
    printf("EOF: %d\n", EOF);
}

// 1.8. from book
// #include <stdio.h>

// int main() {
//     int i;
//     int tab = 0;
//     while ((i = getchar()) != EOF) {
//         if (i == '\t')  // or ' ' or '\n'
//             tab++;
//         i++;
//     }
//     printf("Tab: %d\n", tab);
// }


// 1.9
// #include <stdio.h>

// int main() {
 
//     int i, j; 
//     j = 0;
//     while ((i = getchar()) != EOF) {
//         if (i == ' ' && j == 0) {
//             putchar(i);
//             ++j;
//         }
//         if (i == ' ' && j != 0) {
//             ++j;
//         }
//         if (i != ' ') {
//             putchar(i);
//             j = 0;
//         }
//     } 
// }

// 1.10
// #include <stdio.h>

// int main() {
// 	int i;
// 	while ((i = getchar()) != EOF) {
// 		if (i == '\t') {
// 			putchar('\\');
// 			putchar('t');
// 		}
// 		else if (i == '\b') {
// 			putchar('\\');
// 			putchar('b');
// 		} else if (i == '\\') {
// 			putchar('\\');
// 		}
// 		putchar(i);
// 	}
// }


// int a, b;
// float c;
// scanf ("%d %d", &a, &b);
// c = (float)a/b  // На время выполнения делает переменную a - float
// printf("%f", c)

