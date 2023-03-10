<h1>Рекурсия</h1>

<p align="center">
  <img src="https://pythonru.com/wp-content/uploads/2021/01/rekursivnaya-funkciya-v-python.png">
</p>

<details> <summary><h2><a href="A_bracket_generator.py">A. Генератор скобок</a></h2></summary>
<p>Рита по поручению Тимофея наводит порядок в правильных скобочных последовательностях (ПСП), состоящих только из круглых скобок (). Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке &mdash;&ndash; алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.</p>
<p>Помогите Рите &mdash;&ndash; напишите программу, которая по заданному n выведет все ПСП в нужном порядке.</p>
<p>Рассмотрим второй пример. Надо вывести ПСП из четырёх символов. Таких всего две:</p>
<ol>
<li>(())</li>
<li>()()</li>
</ol>
<p>(()) идёт раньше ()(), так как первый символ у них одинаковый, а на второй позиции у первой ПСП стоит (, который идёт раньше ).</p>
<h3>Формат ввода</h3>
<div>
<p>На вход функция принимает n &mdash; целое число от 0 до 10.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Функция должна напечатать все возможные скобочные последовательности заданной длины в алфавитном (лексикографическом) порядке.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
3
</pre>
</td>
<td>
<pre>
((()))
(()())
(())()
()(())
()()()
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="B_combinations.py">B. Комбинации</a></h2></summary>
<p>На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:</p>
<p>2:'abc',<br />3:'def',<br />4:'ghi',<br />5:'jkl',<br />6:'mno',<br />7:'pqrs',<br />8:'tuv',<br />9:'wxyz'</p>
<p>Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий. <img src="https://contest.yandex.ru/testsys/statement-image?imageId=c9a2bef9474efcb47fabe3c0be11d7bde9a773ec32dfb68486bddef964647ac7" /></p>
<h3>Формат ввода</h3>
<div>
<p>На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Выведите все возможные комбинации букв через пробел.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
23
</pre>
</td>
<td>
<pre>
ad ae af bd be bf cd ce cf
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="C_subsequence.py">C. Подпоследовательность</a></h2></summary>
<p>Гоша любит играть в игру &laquo;Подпоследовательность&raquo;: даны 2 строки, и нужно понять, является ли первая из них подпоследовательностью второй. Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос, просто посмотрев на них. Помогите Гоше написать функцию, которая решает эту задачу.</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке записана строка s.</p>
<p>Во второй &mdash;- строка t.</p>
<p>Обе строки состоят из маленьких латинских букв, длины строк не превосходят 150000. Строки не могут быть пустыми.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Выведите True, если s является подпоследовательностью t, иначе &mdash;&ndash; False.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
abc
ahbgdcu
</pre>
</td>
<td>
<pre>
True
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="D_cookies.py">D. Печеньки</a></h2></summary>
<p>К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.</p>
<p>Но не всё так просто. Печенья могут быть разного размера. А у каждого ребёнка есть фактор жадности &mdash;&ndash; минимальный размер печенья, которое он возьмёт. Нужно выяснить, сколько ребят останутся довольными в лучшем случае, когда они действуют оптимально.</p>
<p>Каждый ребёнок может взять не больше одного печенья.</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке записано n &mdash;&ndash; количество детей.</p>
<p>Во второй &mdash;&ndash; n чисел, разделённых пробелом, каждое из которых &ndash;&mdash; фактор жадности ребёнка. Это натуральные числа, не превосходящие 1000.</p>
<p>В следующей строке записано число m &ndash;&mdash; количество печенек.</p>
<p>Далее &mdash;&ndash; m натуральных чисел, разделённых пробелом &mdash;&ndash; размеры печенек. Размеры печенек не превосходят 1000.</p>
<p>Оба числа n и m не превосходят 10000.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Нужно вывести одно число &ndash;&mdash; количество детей, которые останутся довольными</p>
</div>
<h3>Пример 1</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
2
1 2
3
2 1 3
</pre>
</td>
<td>
<pre>
2
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="E_home_buying.py">E. Покупка домов</a></h2></summary>
<p>Тимофей решил купить несколько домов на знаменитом среди разработчиков Алгосском архипелаге. Он нашёл n объявлений о продаже, где указана стоимость каждого дома в алгосских франках. А у Тимофея есть k франков. Помогите ему определить, какое наибольшее количество домов на Алгосах он сможет приобрести за эти деньги.</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке через пробел записаны натуральные числа n и k.</p>
<p>n &mdash; количество домов, которые рассматривает Тимофей, оно не превосходит 100000;</p>
<p>k &mdash; общий бюджет, не превосходит 100000;</p>
<p>В следующей строке через пробел записано n стоимостей домов. Каждое из чисел не превосходит 100000. Все стоимости &mdash; натуральные числа.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Выведите одно число &mdash;&ndash; наибольшее количество домов, которое может купить Тимофей.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
3 300
999 999 999</pre>
</td>
<td>
<pre>
0
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="F_triangle_perimeter.py">F. Периметр треугольника</a></h2></summary>
<p>Перед сном Рита решила поиграть в игру на телефоне. Дан массив целых чисел, в котором каждый элемент обозначает длину стороны треугольника. Нужно определить максимально возможный периметр треугольника, составленного из сторон с длинами из заданного массива. Помогите Рите скорее закончить игру и пойти спать.</p>
<p>Напомним, что из трёх отрезков с длинами a &le; b &le; c можно составить треугольник, если выполнено неравенство треугольника: c &lt; a + b</p>
<p>Разберём пример:<br />даны длины сторон 6, 3, 3, 2. Попробуем в качестве наибольшей стороны выбрать&nbsp;6. Неравенство треугольника не может выполниться, так как остались 3, 3, 2 &mdash;&ndash; максимальная сумма из них равна 6.</p>
<p>Без шестёрки оставшиеся три отрезка уже образуют треугольник со сторонами&nbsp;3, 3, 2. Неравенство выполняется:&nbsp;3 &lt; 3 + 2. Периметр равен 3 + 3 + 2 = 8.</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке записано количество отрезков&nbsp;n, 3&le; n&le; 10000.</p>
<p>Во второй строке записано&nbsp;n&nbsp;неотрицательных чисел, не превосходящих&nbsp;10 000, &ndash;&mdash; длины отрезков.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Нужно вывести одно число &mdash;&ndash; наибольший периметр треугольника.</p>
<p>Гарантируется, что тройка чисел, которая может образовать треугольник, всегда есть.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
4
6 3 3 2</pre>
</td>
<td>
<pre>
8
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="G_cloakroom.py">G. Гардероб</a></h2></summary>
<p>Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового. После того как вещи других расцветок были убраны, Рита захотела отсортировать свой новый гардероб по цветам. Сначала должны идти вещи розового цвета, потом &mdash;&ndash; жёлтого, и в конце &mdash;&ndash; малинового. Помогите Рите справиться с этой задачей.</p>
<p>Примечание: попробуйте решить задачу за один проход по массиву!</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке задано количество предметов в гардеробе: n &ndash;&mdash; оно не превосходит 1000000. Во второй строке даётся массив, в котором указан цвет для каждого предмета. Розовый цвет обозначен 0, жёлтый &mdash;&ndash; 1, малиновый &ndash;&mdash; 2.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Нужно вывести в строку через пробел цвета предметов в правильном порядке.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
7
0 2 1 2 0 0 1</pre>
</td>
<td>
<pre>
0 0 0 1 1 2 2
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="H_large_number.py">H. Большое число</a></h2></summary>
<p>Вечером ребята решили поиграть в игру &laquo;Большое число&raquo;. <br />Даны числа. Нужно определить, какое самое большое число можно из них составить.</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке записано n &mdash; количество чисел. Оно не превосходит 100.<br />Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Нужно вывести самое большое число, которое можно составить из данных чисел.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
3
15 56 2
</pre>
</td>
<td>
<pre>
56215
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="I_conference lovers.py">I. Любители конференций</a></h2></summary>
<p>На IT-конференции присутствовали студенты из разных вузов со всей страны. Для каждого студента известен ID университета, в котором он учится.</p>
<p>Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло больше всего учащихся.</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке дано количество студентов в списке &mdash;&ndash; n (1 &le; n &le; 15 000).</p>
<p>Во второй строке через пробел записаны n целых чисел &mdash;&ndash; ID вуза каждого студента. Каждое из чисел находится в диапазоне от 0 до 10 000.</p>
<p>В третьей строке записано одно число k.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Выведите через пробел k ID вузов с максимальным числом участников. Они должны быть отсортированы по убыванию популярности (по количеству гостей от конкретного вуза). Если более одного вуза имеет одно и то же количество учащихся, то выводить их ID нужно в порядке возрастания.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
7
1 2 3 1 2 3 4
3
</pre>
</td>
<td>
<pre>
1 2 3
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="J_Bubble_sort lovers.py">J. Пузырёк</a></h2></summary>
<p>Чтобы выбрать самый лучший алгоритм для решения задачи, Гоша продолжил изучать разные сортировки. На очереди сортировка пузырьком &mdash; <a href="https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%BF%D1%83%D0%B7%D1%8B%D1%80%D1%8C%D0%BA%D0%BE%D0%BC">https://ru.wikipedia.org/wiki/Сортировка_пузырьком</a></p>
<p>Её алгоритм следующий (сортируем по неубыванию):</p>
<ol>
<li>На каждой итерации проходим по массиву, поочередно сравнивая пары соседних элементов. Если элемент на позиции i больше элемента на позиции i + 1, меняем их местами. После первой итерации самый большой элемент всплывёт в конце массива.</li>
<li>Проходим по массиву, выполняя указанные действия до тех пор, пока на очередной итерации не окажется, что обмены больше не нужны, то есть массив уже отсортирован.</li>
<li>После не более чем n &ndash; 1 итераций выполнение алгоритма заканчивается, так как на каждой итерации хотя бы один элемент оказывается на правильной позиции.</li>
</ol>
<p><br />Помогите Гоше написать код алгоритма.</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке на вход подаётся натуральное число n &mdash; длина массива, 2 &le; n &le; 1000.<br /> Во второй строке через пробел записано n целых чисел.<br /> Каждое из чисел по модулю не превосходит 1000.<br /> <br />Обратите внимание, что считывать нужно только 2 строки: значение n и входной массив.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>После каждого прохода по массиву, на котором какие-то элементы меняются местами, выводите его промежуточное состояние.<br /> Таким образом, если сортировка завершена за k меняющих массив итераций, то надо вывести k строк по n чисел в каждой &mdash; элементы массива после каждой из итераций.</p>
<p>Если массив был изначально отсортирован, то просто выведите его.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
5
4 3 9 2 1</pre>
</td>
<td>
<pre>
3 4 2 1 9
3 2 1 4 9
2 1 3 4 9
1 2 3 4 9
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="K_merge_sorting lovers.py">K. Сортировка слиянием</a></h2></summary>
<div>Гоше дали задание написать красивую сортировку слиянием. Поэтому Гоше обязательно надо реализовать отдельно функцию merge и функцию merge_sort.
<ul>
<li>Функция merge принимает два отсортированных массива, сливает их в один отсортированный массив и возвращает его. Если требуемая сигнатура имеет вид merge(array, left, mid, right), то первый массив задаётся полуинтервалом [left,mid) массива array, а второй &ndash; полуинтервалом [mid,right) массива array.</li>
<li>Функция merge_sort принимает некоторый подмассив, который нужно отсортировать. Подмассив задаётся полуинтервалом &mdash; его началом и концом. Функция должна отсортировать передаваемый в неё подмассив, она ничего не возвращает.</li>
<li>Функция merge_sort разбивает полуинтервал на две половинки и рекурсивно вызывает сортировку отдельно для каждой. Затем два отсортированных массива сливаются в один с помощью merge.</li>
</ul>
<p>Заметьте, что в функции передаются именно полуинтервалы [begin,end), то есть правый конец не включается. Например, если вызвать merge_sort(arr, 0, 4), где arr=[4,5,3,0,1,2], то будут отсортированы только первые четыре элемента, изменённый массив будет выглядеть как arr=[0,3,4,5,1,2]. </p>
<p>Реализуйте эти две функции. </p>
<p>Мы рекомендуем воспользоваться заготовками кода для данной задачи, расположенными по <a href="https://disk.yandex.ru/d/ZZUss9NZoyRwwg">ссылке</a>.</p>
</div>
<h3>Формат ввода</h3>
<div>Передаваемый в функции массив состоит из целых чисел, не превосходящих по модулю 109. Длина сортируемого диапазона не превосходит 105.</div>
<h3>Формат вывода</h3>
<div>При написании и отправке решений соблюдайте следующие правила:
<ul>
<li>Отправляйте решение в виде файла. Если текст решения будет вставлен в форму, то будет возвращена ошибка.</li>
<li>В качестве компилятора выберите Make.</li>
<li>На Java назовите файл с решением Solution.java и реализуйте внутри класса указанные функции, для C# &ndash; Solution.cs</li>
<li>Для остальных решений не используйте в качестве имени файла слово solution</li>
<li>Укажите правильное разрешение для файла (.cpp, .java, .go. .js, .py). Для решений на C++ разрешение .h не поддерживается.</li>
</ul>
<p>Ниже приведены сигнатуры функций, которые необходимо реализовать, для различных языков программирования. <br />C++<br /> </p>
<div>using&nbsp;Iterator&nbsp;=&nbsp;std::vector&lt;int&gt;::iterator;&nbsp;<br />using&nbsp;CIterator&nbsp;=&nbsp;std::vector&lt;int&gt;::const_iterator;&nbsp;<br />std::vector&lt;int&gt;&nbsp;merge(CIterator&nbsp;left_begin,&nbsp;CIterator&nbsp;left_end,&nbsp;<br /> CIterator&nbsp;right_begin,&nbsp;CIterator&nbsp;right_end);&nbsp;<br />void&nbsp;merge_sort(Iterator&nbsp;begin,&nbsp;Iterator&nbsp;end);</div>
<p>Java </p>
<div>public&nbsp;class&nbsp;Solution&nbsp;{&nbsp;<br /> public&nbsp;static&nbsp;int[]&nbsp;merge(int[]&nbsp;arr,&nbsp;int&nbsp;left,&nbsp;int&nbsp;mid,&nbsp;int&nbsp;right);&nbsp;<br /> public&nbsp;static&nbsp;void&nbsp;merge_sort(int[]&nbsp;arr,&nbsp;int&nbsp;left,&nbsp;int&nbsp;right);&nbsp;<br />}</div>
<p>Python </p>
<div>merge(arr:&nbsp;list,&nbsp;left:&nbsp;int,&nbsp;mid:&nbsp;int,&nbsp;right:&nbsp;int)&nbsp;-&gt;&nbsp;array&nbsp;<br />merge_sort(arr:&nbsp;list,&nbsp;left:&nbsp;int,&nbsp;right:&nbsp;int)&nbsp;-&gt;&nbsp;None</div>
<p>Go </p>
<div>package&nbsp;main&nbsp;<br />func&nbsp;merge(arr&nbsp;[]int,&nbsp;lf&nbsp;int,&nbsp;mid&nbsp;int,&nbsp;rg&nbsp;int)&nbsp;[]int&nbsp;<br />func&nbsp;merge_sort(arr&nbsp;[]int,&nbsp;lf&nbsp;int,&nbsp;rg&nbsp;int)</div>
<p>JavaScript </p>
<div>merge&nbsp;::&nbsp;(Array&nbsp;arr,&nbsp;Number&nbsp;lf,&nbsp;Number&nbsp;mid,&nbsp;Number&nbsp;rg)&nbsp;-&gt;&nbsp;Array&nbsp;<br />merge_sort&nbsp;::&nbsp;(Array&nbsp;arr,&nbsp;Number&nbsp;lf,&nbsp;Number&nbsp;rg)&nbsp;-&gt;&nbsp;void</div>
</div>
</details>

<details> <summary><h2><a href="L_two_bicycles.py">L. Два велосипеда</a></h2></summary>
<p>Вася решил накопить денег на два одинаковых велосипеда &mdash; себе и сестре. У Васи есть копилка, в которую каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая возможность). В процессе накопления Вася не вынимает деньги из копилки.</p>
<p>У вас есть информация о росте Васиных накоплений &mdash; сколько у Васи в копилке было денег в каждый из дней.</p>
<p>Ваша задача &mdash; по заданной стоимости велосипеда определить</p>
<ul>
<li>первый день, в которой Вася смог бы купить один велосипед,</li>
<li>и первый день, в который Вася смог бы купить два велосипеда.</li>
</ul>
<p>Подсказка: решение должно работать за O(log n).</p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 &le; n &le; 10<sup>6</sup>.</p>
<p>В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания. Каждое из чисел не превосходит 10<sup>6</sup>.</p>
<p>В третьей строке записано целое положительное число s &mdash; стоимость велосипеда. Это число не превосходит 10<sup>6</sup>.</p>
</div>
<h3>Формат вывода</h3>
<div>
<p>Нужно вывести два числа &mdash; номера дней по условию задачи.</p>
<p>Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
6
1 2 4 4 6 8
3
</pre>
</td>
<td>
<pre>
3 5
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="N_flowerbeds.py">N. Клумбы</a></h2></summary>
<p>Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. На схеме земельного участка клумбы обозначаются просто горизонтальными отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято n садовников. Каждый из них обрабатывал какой-то отрезок на схеме. Процесс был организован не очень хорошо, иногда один и тот же отрезок или его часть могли быть обработаны сразу несколькими садовниками. Таким образом, отрезки, обрабатываемые двумя разными садовниками, сливаются в один. Непрерывный обработанный отрезок затем станет клумбой. Нужно определить границы будущих клумб.</p>
<p>Рассмотрим примеры.</p>
<p>Пример 1:<br />Два одинаковых отрезка [7,8] и [7,8] сливаются в один, но потом их накрывает отрезок [6,10]. Таким образом, имеем две клумбы с координатами [2,3] и [6,10].</p>
<p>Пример 2<br />Отрезки [2,3], [3,4] и [3,4] сольются в один отрезок [2,4]. Отрезок [5,6] ни с кем не объединяется, добавляем его в ответ.</p>
<h3>Формат ввода</h3>
<div>В первой строке задано количество садовников n. Число садовников не превосходит 100000.
<p>В следующих n строках через пробел записаны координаты клумб в формате:&nbsp;start end, где start &mdash;&ndash; координата начала, end &mdash;&ndash; координата конца. Оба числа целые, неотрицательные и не превосходят 107. start строго меньше, чем end.</p>
</div>
<h3>Формат вывода</h3>
<div>Нужно вывести координаты каждой из получившихся клумб в отдельных строках. Данные должны выводится в отсортированном порядке &mdash;&ndash; сначала клумбы с меньшими координатами, затем &mdash;&ndash; с бОльшими.</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
4
7 8
7 8
2 3
6 10
</pre>
</td>
<td>
<pre>
2 3
6 10
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="final_search_in_broken_array.py">A. Поиск в сломанном массиве</a></h2></summary>
<p>Алла ошиблась при копировании из одной структуры данных в другую. Она хранила массив чисел в кольцевом буфере.&nbsp;Массив был отсортирован по возрастанию, и в нём можно было найти элемент за логарифмическое время. Алла скопировала данные из кольцевого буфера в обычный массив, но сдвинула данные исходной отсортированной последовательности. Теперь массив не является отсортированным. Тем не менее, нужно обеспечить возможность находить в нем элемент за O(logn).</p>
<p>Можно предполагать, что в массиве только уникальные элементы.</p>
<p>Задачу необходимо сдавать с компилятором Make, он выбран по умолчанию, других компиляторов в задаче нет. Решение отправляется файлом. Требуемые сигнатуры функций лежат в заготовках кода на диске.</p>
<p>От вас требуется реализовать функцию, осуществляющую поиск в сломанном массиве. Файлы с заготовками кода, содержащими сигнатуры функций и базовый тест для поддерживаемых языков, находятся на Яндекс.Диске по <a href="https://disk.yandex.ru/d/d7C1HkKCNrDg8g">ссылке</a>. Обратите внимание, что считывать данные и выводить ответ не требуется.</p>
<p>Расширение файла должно соответствовать языку, на котором вы пишете (.cpp, .java, .go, .js, .py). Если вы пишете на Java, назовите файл с решением Solution.java, для C# &ndash; Solution.cs. Для остальных языков название может быть любым, кроме solution.ext, где ext &ndash; разрешение для вашего языка.</p>
<h3>Формат ввода</h3>
<div>Функция принимает массив натуральных чисел и искомое число k. Длина массива не превосходит 10000. Элементы массива и число k не превосходят по значению 10000.
<p>В примерах:</p>
<p>В первой строке записано число n &ndash;&mdash; длина массива.</p>
<p>Во второй строке записано положительное число k &ndash;&mdash; искомый элемент.&nbsp;</p>
<p>Далее в строку через пробел записано n натуральных чисел &ndash; элементы массива.</p>
</div>
<h3>Формат вывода</h3>
<div>Функция должна вернуть индекс элемента, равного k, если такой есть в массиве (нумерация с нуля). Если элемент не найден, функция должна вернуть &minus;1.
<p>Изменять массив нельзя.</p>
<p>Для отсечения неэффективных решений ваша функция будет запускаться от 100000 до 1000000 раз.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
9
5
19 21 100 101 1 4 5 7 12
</pre>
</td>
<td>
<pre>
6
</pre>
</td>
</tr>
</tbody>
</table>
</details>

<details> <summary><h2><a href="final_efficient_quick_sorting.py">B. Эффективная быстрая сортировка</a></h2></summary>
<p>Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров. Задачи подобраны, участники зарегистрированы, тесты написаны. Осталось придумать, как в конце соревнования будет определяться победитель.</p>
<p>Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя: количество решённых задач P<sub>i</sub> и размер штрафа F<sub>i</sub>. Штраф начисляется за неудачные попытки и время, затраченное на задачу.</p>
<p>Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот, у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.</p>
<p>Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин. В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов. Так как Тимофей любит спортивное программирование и не любит зря расходовать оперативную память, то ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных данных (такая модификация быстрой сортировки называется "in-place"). <br /><br />Как работает in-place quick sort<br /> Как и в случае обычной быстрой сортировки, которая использует дополнительную память, необходимо выбрать опорный элемент (англ. pivot), а затем переупорядочить массив. Сделаем так, чтобы сначала шли элементы, не превосходящие опорного, а затем &mdash;&ndash; большие опорного.</p>
<p>Затем сортировка вызывается рекурсивно для двух полученных частей. Именно на этапе разделения элементов на группы в обычном алгоритме используется дополнительная память. Теперь разберёмся, как реализовать этот шаг in-place.</p>
<p>Пусть мы как-то выбрали опорный элемент. Заведём два указателя left и right, которые изначально будут указывать на левый и правый концы отрезка соответственно. Затем будем двигать левый указатель вправо до тех пор, пока он указывает на элемент, меньший опорного. Аналогично двигаем правый указатель влево, пока он стоит на элементе, превосходящем опорный. В итоге окажется, что что левее от left все элементы точно принадлежат первой группе, а правее от right &mdash; второй. Элементы, на которых стоят указатели, нарушают порядок. Поменяем их местами (в большинстве языков программирования используется функция swap()) и продвинем указатели на следующие элементы. Будем повторять это действие до тех пор, пока left и right не столкнутся. <br /> На рисунке представлен пример разделения при pivot=5. Указатель left &mdash; голубой, right &mdash; оранжевый. <img src="https://contest.yandex.ru/testsys/statement-image?imageId=79587b4867d6af95afb4a295be8023fa21036db1cfa1b70b2768309a1fdb8ad4" /></p>
<h3>Формат ввода</h3>
<div>
<p>В первой строке задано число участников n, 1 &le; n &le; 100 000. <br />В каждой из следующих n строк задана информация про одного из участников.<br /> i-й участник описывается тремя параметрами:</p>
<ul>
<li>уникальным логином (строкой из маленьких латинских букв длиной не более 20)</li>
<li>числом решённых задач P<sub>i</sub></li>
<li>штрафом F<sub>i</sub></li>
</ul>
F<sub>i</sub> и P<sub>i</sub> &mdash; целые числа, лежащие в диапазоне от 0 до 10<sup>9</sup>.
</div>
<h3>Формат вывода</h3>
<div>
<p>Для отсортированного списка участников выведите по порядку их логины по одному в строке.</p>
</div>
<h3>Пример</h3>
<table>
<thead>
<tr>
<th>Ввод</th>
<th>Вывод</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<pre>
5
alla 4 100
gena 6 1000
gosha 2 90
rita 2 90
timofey 4 80</pre>
</td>
<td>
<pre>
gena
timofey
alla
gosha
rita
</pre>
</td>
</tr>
</tbody>
</table>
</details>
