// Типы данных (всего - 6)
// number - 4, 4.32 Нет разделения на дробное и целое!
// Строки как в Python
// Boolean как в Python, только с маленькой буквы!

// И еще 3:
// null
// object ({objKey: "balue"})
// undefined - Значение неопределено!
// null - тоже почти тоже самое, что и undefined. ХЗ, даже Соболев не знает)

// ; - Можно ставить, можно - нет, но в некоторых местах она нужна! Лучше всегда ставить!

'use strict'; // Необходимо всегда писать в начале! Почитать про это!

// В JS используется кэмел кейс!
// Ковычки могуть быть и те и другие.
var s = 'My var';
var myVar = "My var"

s = undefined
console.log(s)
// undefined
s = null
console.log(s)
// null

s = 'My var'

console.log(s == myVar)  // Вывод на экран
// true
console.log(s === myVar)
// true
console.log(typeof(s))
// string

console.error(s)  // Вывод ошибок
// My var  // Error

// Объекты
var o = {}
console.log(o)
// {}
console.log(typeof(o))
// object

// Объект в JS - это как dict в Python!
// Наследования нет, классов нет!
o['key'] = 12
console.log(o.key)  // Но уже ['some key'] через точку не получится!
// 12
console.log(o["key"])
// 12

// Списки - так же, как и в Python, но это не тип, а - объект! О_о
// В данном случае ключ 0 = 1, ключ 1 = 2 и ключ 2 = 3!
var list = [1, 2, 3]
// (3) [1, 2, 3]
console.log(typeof(list))
// object
list.push('str')  // Добавление в список
console.log(list)
// 4) [1, 2, 3, "str"]

