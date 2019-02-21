// IF
// Условие всегда в фигурных скобах!
// Можно писать в одну строку, если тело состоит из одной операции:
var i = 1
if (i == 1) alert(i)

// Но лучше всегда с телом
var userName = prompt('Yor name?', '')
if (userName == 'Max') {
    alert('Yeaaaah!')
} else if (userName == 'Den') {
    alert('Ops')
} else {
    alert('Baddd')
}

if (1) {
    // Всегда выполнится! Как в python: if True: ...
}

// '?', но лучше всегда использовать if else!
// --------------
var age = prompt('возраст?', 18);

var message = (age < 3) ? 'Здравствуй, малыш!' :
  (age < 18) ? 'Привет!' :
  (age < 100) ? 'Здравствуйте!' :
  'Какой необычный возраст!';

alert( message );

// Тоже самое:
var age = prompt('возраст?', 18);

if (age < 3) {
  message = 'Здравствуй, малыш!';
} else if (age < 18) {
  message = 'Привет!';
} else if (age < 100) {
  message = 'Здравствуйте!';
} else {
  message = 'Какой необычный возраст!';
}
// --------------

// Условие IF в одну строку
var x = 1 === 1 ? console.log('true') : 'false'

var company = prompt('Какая компания создала JavaScript?', '');
(company == 'Netscape') ?
   alert('Да, верно') : alert('Неправильно');


// Циклы
var a = 1;
while (a < 3) {
    alert(a);
    a++;
}

// Бесконечный цикл
while (true) {
    alert('Infinity')
}

// Условие в скобках интерпретируется как логическое значение, поэтому вместо while (i!=0) обычно пишут while (i):
while (i) { // при i, равном 0, значение в скобках будет false и цикл остановится.
}

// do while // В любом случае выполнится 1 раз!
var i = 0;
do {
    alert(i);
    i++
} while (i <3);
// Синтаксис do..while редко используется, т.к. обычный while нагляднее – в нём не приходится искать глазами условие и ломать голову, почему оно проверяется именно в конце.

// Цикл for
// Тут больше итерирование по условию, а не по коллекции, как в Python(for i in array: ...)!
// Чаще всего применяется цикл for. Выглядит он так:
// Пример цикла, который выполняет alert(i) для i от 0 до 2 включительно (до 3):
var i;
for (i = 0; i < 3; i++) {
  alert( i );
}
// Здесь:
// Начало: i=0.
// Условие: i<3.
// Шаг: i++.
// Тело: alert(i), т.е. код внутри фигурных скобок (они не обязательны, если только одна операция)

// В цикле также можно определить переменную:
for (var i = 0; i < 3; i++) {
  alert(i); // 0, 1, 2
}

// Итерация по списку
// через in
var list = ['a', 'b', 3, 4, 5]
for ( var i in list) { // i сдесь индекс!
  console.log(list[i]) // Выведет значения листа
  console.log(i)  // Выведет индексы значений листа // В Python вывел бы значения!
}
// через of  // Поддерживает мало браузеров (ES6)!
var list = ['a', 'b', 3, 4, 5]
for ( var i of list) { // i сдесь индекс!
  console.log(i)  // Выведет значения листа
}

// Пропуск частей:
var i = 0;

for (; i < 3; i++) {  // ';' - обязательны
  alert( i ); // 0, 1, 2
}
// Можно убрать и шаг:

var i = 0;

for (; i < 3;) {
  alert( i );
  i++;
  // цикл превратился в аналог while (i<3)
}

// Бесконечный цикл
for (;;) {
  // будет выполняться вечно
}


// Прерывание цикла: break
var sum = 0;

while (true) {

  var value = +prompt("Введите число", '');

  if (!value) break; // Выход из цикла

  sum += value;

}
alert( 'Сумма: ' + sum );


// Прерываение Continue
for (var i = 0; i < 10; i++) {

  if (i % 2 == 0) continue; // Если остаток от деления равен 0 - прерываем цикл и начинаем следующий проход цикла, если он есть! 
  alert(i);
}
// ==
for (var i = 0; i < 10; i++) {

  if (i % 2) {  // Так как if 0 - false
    alert( i );
  }
}

// swith - Это некое подобие IF, сравнение констант 
//Здесь обязателен break или return!
var value = 12
switch (value) {
  case 12:
    console.log('12');
    break;
  case 1:
    console.log('< 12');
    break;
  default:
    console.log('> 12')
    break;
}

//  Группировка case
var a = 2+1;
switch (a) {
  case 4:
    alert('Верно!');
    break;

  case 3:  // При 3 выполнится от сюда
  case 5:
    alert('Неверно!');
    alert('Немного ошиблись, бывает.');
    break;  // До сюда

  default:
    alert('Странный результат, очень странный');
}


// Выход сразу из нескольких уровне цикла
// Использование меток для break и continue
out: for(var i = 0; i < 3; i++) {
  for (var j = 0; j < 3; j++) {
    var input = prompt()
    if (!input) {
      break out;  // Метка выхода
    }
  }
}

// Функции
function test (a, b) {
  return a + b
}
test(1, 2)  
// Если не ввести аргументы, - то вернется NaN
// test() == test(undefined, undefined)
// Если ввести больше значений чем нужно, то JS возьмет только те, которые определены.
// *args, *kwargs тут нет! В другом(современном) JS - есть!

// ==
// Объвление в переменной
var myFunc = function test (a, b) {
  return a + b
}
console.log(myFunc(1, 2)) 
// Если передать без параметров, то выведется имходный код функциии!
console.log(myFunc)
// ƒ test (a, b) {
//   return a + b
// } 

typeof(myFunc)
// "function"  - Тип данных


// Объекты в JS
// Прототипы / this
var myClass = function (title) { // title - Тут что-то типа значения  конструктора
  this.title = title;  // Что-то типа self в Python
  var privateValue = 'Secret';

  this.tellTitle = function () {
    console.log(this.title);
    console.log(this);
  };
  function privateFunction() {
    console.log(privateValue);  // Замыкание - использование функцией чужих аргументов
    console.log('This is: ', this);
  }
  privateFunction();

  this.runPrivate = function() {  // Оберктка
    privateFunction();
  }

  this.runPrivateWithCall = function() {
    privateFunction.call(this);
    privateFunction.apply(this, []);
  }
}

console.log(typeof(myClass))
// "function"  Не класс!
// Создание объекта из "Класса"
// new - параметр обязателен! 
var o = new myClass('Some title ')  // new - Инициализация экземпляра ("объекта" / прототипа)
console.log(typeof(o))
// "object"
console.log(o.runPrivateWithCall())
console.log(myClass.prototype)


myClass.prototype.test = function() {
  console.log('TEST')
}
o.test()
// TEST
