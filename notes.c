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

// Константы  // Определяются всегда перед main()
#define NUMBER 23 // Имя константы принато писать с большой буквы!
// Данные константы - неизменяемые

// Еще один вид константы
const char a = 2  // Может быть изменена в зависимости от компилятор!

// Спецификаторы вывода
printf ("%d", 10);
// %d - десятичные цифры(decimal)
// %c - символьные знаки(char)
// %i  - десятичные числа (до 2 мирд.)
// %s - строки (string)

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



// --- Еще рано
// int a, b;
// float c;
// scanf ("%d %d", &a, &b);
// c = (float)a/b  // На время выполнения делает переменную a - float
// printf("%f", c)

//------------------------------------------------------
// Б. Керниган, Д. Ритчи. Язык программирования Си:
// Прочитать разделы 2.5 и 2.6
// Упражнение 2.2

// Написать программу c функцией реализующую бинарную операцию исключающего логического ИЛИ (XOR). 
// Программа должна протестировать работу функции на корректность и вывести в консоль полные результаты проверки. 
// При написании использовать заголовочный файл stdbool.h. 
// Пример формата вывода результатов проверки: 
// 	XOR (true, false) = true

// (Опционально) Изменить программу на слайде 6 так, 
// чтобы рассчитанное среднее сошлось с ожидаемым и составляло 10.1. 
// Размерность массива и количество итераций изменять нельзя.

//??
// (Опционально) Написать программу, выводящую на экран самое большое число из базовых типов.


// #include <stdio.h>
// #define ARRAY_SIZE 10
// #define VALUE 10.1

// /* Returns the mean value of the array */
// float mean(float array[], int size) {
// 	float total = 0.0;
// 	for (char i = 0; i < size; i++) {
// 		total += array[i];
// 		printf("array[%hhu] = %f and total is %f\n", i, array[i], total);
// 	}
// 	if (size != 0)
// 		return total / size;
// 	else
// 		return 0.0;
// }

// int main(void) {
// 	float array[ARRAY_SIZE];
// 	float avg;
// 	size_t i;
// 	for (i = 0; i < ARRAY_SIZE; i++)
// 		array[i] = VALUE;

// 	avg = mean(array, ARRAY_SIZE);
// 	printf("mean is %f\n", avg);
// 	if (avg == array[0]) {
// 		printf("array[0] is the mean\n");
// 	}
// 	else {
// 		printf("array[0] is not the mean\n");
// 	}
// 	getchar();
// 	return 0;
// }




// // Также сделать черз формулу
// #include <stdio.h>
// #include <stdbool.h>

// bool XOR(bool a, bool b) {
// 	bool c = a ^ b;
// 	return c;

// }

// void main() {

// 	printf("XOR(true, true): %i\n", XOR(true, true));
// 	printf("XOR(true, false): %i\n", XOR(true, false));
// 	printf("XOR(false, true): %i\n", XOR(false, true));
// 	printf("XOR(false, false): %i\n", XOR(false, false));

// 	getchar();
// 	return;
// }


#include <stdio.h>

void main() {
    
    float i = 10.1;
    float arr [3] = {0.3, 0.2, 0.7};
    for(int a = 0; a < 3; a++) {
        i += arr[a];
    }
    printf("%f\n", i);
    return;
}
