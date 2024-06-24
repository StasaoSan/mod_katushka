# Моделирование "Оптимизация катушки"
Из провода длиной L и диаметром d требуется намотать катушку на цилиндрический каркас диаметром D и длиной l, таким образом, чтобы получить максимальную индукцию магнитного поля на оси катушки в центре. Число витков N должно быть одинаково по всей длине катушки. Определите индуктивность получившейся катушки. Параметры должны задаваться. Построить график зависимости B=f(l).

1. **Запуск:**
   Для использования программы необходимо запустить main.py, после чего запустится графический интерфейс написанный при помощи библиотеки tkinter.
<img width="250" alt="Снимок экрана 2024-06-24 в 10 47 59" src="https://github.com/StasaoSan/mod_katushka/assets/113228941/d7aa22ba-9581-4556-abd8-13c7b0986608"
Где указываются все необходимые параметры.
Левая граница, правая граница - левая и правая границы отображения l для построения графиков соответственно.

Нажать расчитать и получить результат.

2. **В данной модели использовались следующие формулы:**
   1. Общее число витков (N):
    \[ N = \frac{L}{\pi\cdot D} \]
    где:
    - \( L \) — длина провода,
    - \( D \) — диаметр каркаса.

  2. Плотность витков (n):
    \[ n = \frac{N}{l} = \frac{L}{\pi \cdot D \cdot l} \]

    где:
    - \( l \) — длина каркаса.

  3. Площадь поперечного сечения сердечника (S):
    \[ S = \pi \left(\frac{D}{2}\right)^2 \]

    где:
    - \( D \) — диаметр каркаса.
    
  4. Магнитная индукция (B) в центре катушки:
    \[ B = \mu \cdot \mu_0 \cdot n \cdot I\]

    где:
    - \( \mu \) — магнитная проницаемость материала сердечника,
    - \( \mu_0 \) — магнитная постоянная (4\pi\cdot 10^-7 \frac{Гн}{м}),
    - \( n \) — плотность витков,
    - \( I \) - ток. (в нашем случае = 1 А)

  5. Индуктивность катушки (L_c):
    \[ L_c = \frac{\mu \cdot \mu_0 \cdot N^2 \cdot S}{l} \]

    где:
    - \( N \) — общее число витков,
    - \( S \) — площадь поперечного сечения сердечника,
    - \( l \) — длина каркаса.

3. **Итог:**
   При стандартных значениях вывод программы будет таким:
   <img width="1503" alt="Снимок экрана 2024-06-24 в 18 14 02" src="https://github.com/StasaoSan/mod_katushka/assets/113228941/14abd028-aa82-4c51-bf44-488306d1850c">
