// Ручное компилирование 
// Из cmd: gcc myFile.c -o myFile.exe

# include <stdio.h> // По сути подключения файла с функциями 
// #include (подключить) - деректива препроцессора / 
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

#include <stdio.h>
int main()
{
    float num1 = 5;
    float num2 = 9; 
    printf ("Helo world!\n%.0f / %.0f = %.3f\n", num1, num2, num1 / num2);
    return 0;
    getchar(); // Ожидает ввода
}


// Константы  // Определяются всегда перед main()
#define NUMBER 23 // Имя константы принато писать с большой буквы! // Именованные константы, а не переменные, поэтому для них нет объявлений.
// То есть мы назвали число 23 словом - NUMBER
// Данные константы - неизменяемые
// #define определяет символьное имя, или именованную константу, для заданной строки символов:
#define XOR(a, b) (a && !b) || (!a && b) // Макро подстановка как замена функции!
// Дешевле функции

// Еще один вид константы
const char a = 2  // Иногда может быть изменена в зависимости от компилятора!


// Спецификаторы вывода
printf ("%d", 10);
// %d - десятичные цифры(decimal)
// %c - символьные знаки(char)
// %i  - десятичные числа (до 2 мирд.)
// %s - строки (string)
// %x - вывод в шестнадцатеричном формате
// ...


//Функции
// main - основная/главная
void main() {  // void - пустота, ничего не возвращает!
    return;
}

// Если параметров нет, то желательно указывать void
void test(void) {  // void - пустота, ничего не передаем и не возвращаем!
    return;
}
// Параметры функции (у них тоже должен быть указан тип!)
unsigned short sum(unsigned char a, unsigned char b) {
    unsigned short total = 0;
    total = a + b ;
    return total;
}
// Вызов в main()
sum(1, 255);


// Разница в ++а и а++ видна только в выраждении!
// ++i увеличивает значение, а затем возвращает его.
// i++ возвращает значение, а затем увеличивает его.
// Это тонкая разница.
// Для цикла for используйте ++i, так как он немного быстрее. i++ создаст дополнительную копию, которая просто будет выброшена.

int a = 5, b;
b = -a; // b = -5 
b = --a; // Выражение! // b = 4, a = 4    
// !=
b = -a; // -4
b = a--; // b = 3, a = 4

int a = 5, b;
b = -a;
a--; // or --a Одно и тоже. // Не выражение!
// ==
int a = 5, b;
b = -a;
--a; 

// В С нет логического типа (типа True в Python)
#define false 0
#define true 1

// Или использовать из <stdbool.h>:
bool a = 1

//
int a= 10
int b = (5 > 3) && (a = 15) // b = 1


// Указатели. Храянат адрес переменной в памяти (https://learnc.info/c/pointers.html)
char value = 100;
char *pointer = NULL; // Или сразу: char *pointer = &value;
//Получаем адрес переменной value
pointer = &value;
//Выводим адрес переменной value
printf("%x\n", pointer);
//Выводим содержимое переменной value
printf("%d\n", *pointer);
//Меняем содержимое переменной value
*pointer = 200;
printf("%d\n", value);
printf("%d", *pointer);


// Массивы
int array[4] = {};  // Все элементы могут быть чем угодно!
int array[4] = { 0 };  // Все элементы = 0! 
int array[4] = {1, 2, 3 ,6};
int array[4] = {[3] = 2};  // Инициализирует только элемент под индексом 3 из 4! Все остальные = 0!

printf("%\n", array[0])  // 1
// ==
printf("%i\n", *array)  //  По сути указатель на первый элемент в массиве!
// ==
printf("%i\n", *(array + 0)
 
float array[4] = {100.000, 2000.000, 300.000 ,600.000};
printf("%f\n", *(array + 1));  // Сдвиг на размер байт! 1 - в данном случае float -  это 4 байта
printf("%f\n", *(array + 2));  // Сдвиг на размер байт! 2 - в данном случае float -  это 8 байт
// Подсчет размера типов
size_t floatSize;  // ???Специальный тип для работы с памятью
floatSize = sizeof(float);
size_t intSize = sizeof(int);
size_t charSize = sizeof(char);
printf("%zu\n", floatSize);  //%zu - специальный спецификатор для вывода типов наподобие size_t
// 4 (bytes)
printf("%zu\n", intSize)
// 4 (bytes) 
printf("%zu\n", charSize)
// 1 (bytes)
// Соответственно размер масиива в данном примере (float array[4] = {100.000, 2000.000, 300.000 ,600.000};) = 
// 4 (bytes) 
printf("%zu\n", sizeof array)  // Без скобок
// 16 (bytes) 
 // Посмотреть адрес в памяти (в шестнадцатеричной системе счисления)
printf("%p\n", &floatSize)
// 0x7ffeefbff578


// Преобразование типов


// Приведение типов 
// (тип) выражение  // Явное преобразование
sqrt((float) n)
// Переменные при преобразовании не меняются!

int a, b;
float c;
scanf ("%d %d", &a, &b);
c = (float)a/b  // На время выполнения делает переменную a - float
printf("%f", c)

/*

/*
 Б. Керниган, Д. Ритчи. Язык программирования Си:
 Прочитать разделы 2.11 - 3.4
 Написать программу, выводящую в консоль результат вычисления квадратного уравнения в области действительных и комплексных чисел.Параметры a, b и с – действительные числа (тип double) запросить из консоли с помощью функции getchar(). Формат результата: Уравнение x*x + 1 = 0 имеет 1 корень x1 = 1.000000*i
 (Опционально) В программе выше предварительно проверить введенные значения на корректность.
 
 Б. Керниган, Д. Ритчи. Язык программирования Си:
 Прочитать главу 4 до раздела 4.3
 Для программы из ДЗ №5 подготовить объявления использованных ранее функций и вынести все функции вычислений и ввода-вывода в отдельные файлы.
 

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#define MAX_SIZE 50

double a, b, c;


double convertValue(void) {
    
    char array[MAX_SIZE] = {};
    signed char c;
    double result;
    char i = 0;
    
    while((c = getchar()) != EOF && c != '\n') {
        if (isdigit(c) || c == '.' || c == '-') {
            array[i] = c;
            i++;
        } else {
            array[i] = '\0';
        }
    }
    
    result = atof(array);
    return result;
}


void inputUserValue() {
    
    printf("Enter a: ");
    a = convertValue();
    printf("a = %.1f", a);
    
    printf("\n\nEnter b: ");
    b = convertValue();
    printf("b = %.1f", b);
    
    printf("\n\nEnter c: ");
    c = convertValue();
    printf("c = %.1f", c);
    
}


void calculateEquation() {
    
    if (b == 0 && c == 0) {
        printf("\n\nThe quadratic equation has no roots");
    } else if (a != 0 && (b == 0 || c == 0)) {
        printf("\n\nThe quadratic equation is not Full");
    } else if (a != 0 && b != 0 && c != 0) {
        printf("\n\nThe quadratic equation is Full");
    } else {
        printf("\na = 0");
    }
    return;
}


double searchDiscriminant(double a, double b, double c) {
    
    return (b*b) - (4 * (a * c));
}


int main(void) {
    
    inputUserValue();
    calculateEquation();
    printf("D = %.2f", searchDiscriminant(2.4, 1.5, 1));
    
//    printf("\n\nsum: %f", a + b + c);
    
    getchar();
    
    return 0;
}


*/
