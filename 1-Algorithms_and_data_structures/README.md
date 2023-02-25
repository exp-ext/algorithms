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
</details>



  <p>B. Список дел</p>
  <p>C. Нелюбимое дело</p>
  <p>D. Заботливая мама</p>
  <p>E. Всё наоборот</p>
  <p>F. Стек - Max</p>
  <p>G. Стек - MaxEffective</p>
  <p>H. Скобочная последовательность</p>
  <p>I. Ограниченная очередь</p>
  <p>J. Списочная очередь</p>
  <p>K. Рекурсивные числа Фибоначчи</p>
  <p>L. Фибоначчи по модулю</p>
  <p>A. Дек</p>
  <p>B. Калькулятор</p>

