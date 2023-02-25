<h1>Алгоритмы и структуры данных</h1>

<details> <summary><h2><a href="A_Monitoring.py">A. Мониторинг</a></h2></summary>
  <span>
    <p>
      Алла получила задание, связанное с мониторингом работы различных серверов. Требуется понять, сколько времени обрабатываются
      определённые запросы на конкретных серверах. Эту информацию нужно хранить в матрице, где номер столбца соответствуют идентификатору
      запроса, а номер строки — идентификатору сервера. Алла перепутала строки и столбцы местами. С каждым бывает. Помогите ей исправить
      баг.
    </p>
  </span>
  <p>
  Есть ма трица размера <span class="tex-math-text">m × n</span>. Нужно написать функцию, которая её транспонирует.
  </p>
  <p>Транспонированная матрица получается из исходной заменой строк на столбцы.</p>
  <p>Например, для матрицы <span class="tex-math-text">А</span> (слева) транспонированной будет следующая матрица (справа):</p>
  <p><img class="user-image" src="https://contest.yandex.ru/testsys/statement-image?imageId=69ff475b66bdbc91024d48b48ee588d5a58645a20b1433663a9e7981bef14e3d"></p>
  <h3>Формат ввода</h3>
  <span>
    <p>
      В первой строке задано число <span>n</span> — количество строк матрицы.<br>Во второй строке задано <span>m</span> — число столбцов, <span>m</span> и <span>n</span> не превосходят <span class="tex-math-text">1000</span>. В следующих <span class="tex-math-text">n</span> строках задана матрица. Числа в ней не превосходят по модулю <span>1000</span>.
    </p>
  </span>
  <h3>Формат вывода</h3>
  <span>
    <p>
      Напечатайте транспонированную матрицу в том же формате, который задан во входных данных. Каждая строка матрицы выводится на
      отдельной строке, элементы разделяются пробелами.
    </p>
  </span>   
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
        <td><pre>
4
3
1 2 3
0 2 6
7 4 1
2 7 0
        </pre></td>
        <td><pre>
1 0 7 2
2 2 4 7
3 6 1 0
        </pre></td>
      </tr>
    </tbody>
  </table>
</details>

<details> <summary><h2><a href="B_Todo_ list.py">B. Список дел</a></h2></summary>
  <p>Васе нужно распечатать свой список дел на сегодня. Помогите ему: напишите функцию, которая печатает все его дела. Известно, что дел у Васи не больше 5000.</p>
  <p><span style="font-weight: bold;">Внимание: </span>в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову списка и печатает его элементы. Ниже дано описание структуры, которая задаёт узел списка. <!--l. 51--></p>
  <p>Используйте заготовки кода для данной задачи, расположенные по ссылкам:</p>
  <ul>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/cpp/sprint2/B">c++</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/java/sprint2/B">Java</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/js/sprint2/B">js</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/python/sprint2/B">Python</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/csharp/sprint2/B">C#</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/go/sprint2/B">go</a></li>
  </ul>
  <p><span style="font-weight: bold;">Решение надо отправлять только в виде файла с расширением,</span> <span style="font-weight: bold;">которое соответствует вашему языку. Иначе даже корректно</span> <span style="font-weight: bold;">написанное решение не пройдет тесты.</span></p>
  <h3>Формат ввода</h3>
  <div>
    В качестве ответа сдайте только код функции, которая печатает элементы списка. Длина списка не превосходит 5000 элементов. Список не бывает пустым.
  </div>
  <h3>Формат вывода</h3>
  <p>Функция должна напечатать элементы списка по одному в строке.</p>
  <p>&nbsp;</p>
</details>

<details> <summary><h2><a href="C_Unloved_business.py">C. Нелюбимое дело</a></h2></summary>
  <div>
    Вася размышляет, что ему можно не делать из того списка дел, который он составил. Но, кажется, все пункты очень важные! Вася решает загадать число и удалить дело, которое идёт под этим номером. Список дел представлен в виде односвязного списка. Напишите функцию solution, которая принимает на вход голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
    <p><span style="font-weight: bold;">Внимание: </span>в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову списка и номер удаляемого элемента и возвращает голову обновлённого списка.</p>
    <p>Используйте заготовки кода для данной задачи, расположенные по ссылкам:</p>
    <ul>
      <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/cpp/sprint2/C">c++</a></li>
      <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/java/sprint2/C">Java</a></li>
      <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/js/sprint2/C">js</a></li>
      <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/python/sprint2/C">Python</a></li>
      <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/csharp/sprint2/C">C#</a></li>
      <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/go/sprint2/C">go</a></li>
    </ul>
    <p><span style="font-weight: bold;">Решение надо отправлять только в виде файла с расширением,</span> <span style="font-weight: bold;">которое соответствует вашему языку. Иначе даже корректно</span> <span style="font-weight: bold;">написанное решение не пройдет тесты. </span></p>
    <p>&nbsp;</p>
  </div>
  <h3>Формат ввода</h3>
  <div>
    Функция принимает голову списка и индекс элемента, который надо удалить (нумерация с нуля). Список содержит не более 5000 элементов. Список не бывает пустым.&nbsp;
  </div>
  <h3>Формат вывода</h3>
  <p>Верните голову списка, в котором удален нужный элемент.</p>
  <p>&nbsp;</p>
</details>

<details> <summary><h2><a href="D_Caring_mother.py">D. Заботливая мама</a></h2></summary>
  Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: напишите функцию solution, определяющую индекс первого вхождения передаваемого ей на вход значения в связном списке, если значение присутствует.
  <p><span style="font-weight: bold;">Внимание: </span>в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову списка и искомый элемент, а возвращает целое число &mdash; индекс найденного элемента или -1.</p>
  <p style="text-indent: 0em;">Используйте заготовки кода для данной задачи, расположенные по ссылкам:</p>
  <ul>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/cpp/sprint2/D">c++</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/java/sprint2/D">Java</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/js/sprint2/D">js</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/python/sprint2/D">Python</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/csharp/sprint2/D">C#</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/go/sprint2/D">go</a></li>
  </ul>
  <h2>Формат ввода</h2>
  Функция на вход принимает голову односвязного списка и элемент, который нужно найти. Длина списка не превосходит 10000 элементов. Список не бывает пустым.
  <h2>Формат вывода</h2>
  <div>Функция возвращает индекс первого вхождения искомого элемента в список(индексация начинается с нуля). Если элемент не найден, нужно вернуть -1.</div>
  <p>&nbsp;</p>
</details>

<details> <summary><h2><a href="E_All_opposite.py">E. Всё наоборот</a></h2></summary>
  Вася решил запутать маму &mdash;&ndash; делать дела в обратном порядке. Список его дел теперь хранится в двусвязном списке. Напишите функцию, которая вернёт список в обратном порядке.
  <p><span style="font-weight: bold;">Внимание: </span>в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход голову двусвязного списка и возвращает голову перевёрнутого списка. Ниже дано описание структуры, которая задаёт вершину списка.</p>
  <p>Используйте заготовки кода для данной задачи, расположенные по ссылкам:</p>
  <ul>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/cpp/sprint2/E">c++</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/java/sprint2/E">Java</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/js/sprint2/E">js</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/python/sprint2/E">Python</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/csharp/sprint2/E">C#</a></li>
    <li><a href="https://github.com/Yandex-Practicum/algorithms-templates/tree/main/go/sprint2/E">go</a></li>
  </ul>
  <h2>Формат ввода</h2>
  Функция принимает на вход единственный аргумент &mdash; голову двусвязного списка. 
  <p>Длина списка не превосходит 1000 элементов. Список не бывает пустым.&nbsp;</p>
  <p>&nbsp;</p>
</details>

<details> <summary><h2><a href="F_Stack_max.py">F. Стек - Max</a></h2></summary>


</details>

  <p>F. Стек - Max</p>
  <p>G. Стек - MaxEffective</p>
  <p>H. Скобочная последовательность</p>
  <p>I. Ограниченная очередь</p>
  <p>J. Списочная очередь</p>
  <p>K. Рекурсивные числа Фибоначчи</p>
  <p>L. Фибоначчи по модулю</p>
  <p>A. Дек</p>
  <p>B. Калькулятор</p>

