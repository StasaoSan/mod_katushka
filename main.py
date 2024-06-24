import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def calculate_inductance_and_field(L, D, d, l, mu, mu_0):
    length_per_turn = 2 * np.pi * (D + d) / 2  # Вычисляем длину одного витка
    N = int(L / length_per_turn)  # Общее число витков
    if N * d > l:
        return 0, 0, 0
    n = N / l  # Плотность витков
    S = np.pi * (D / 2) ** 2  # Площадь поперечного сечения сердечника

    # Индукция в центре катушки
    B = mu * mu_0 * n  # при единичном токе

    # Индуктивность катушки
    L_c = mu * mu_0 * (N ** 2) * S / l

    return B, L_c, N

# Функция для обновления графиков и результатов
def update_graphs():
    L = float(L_entry.get())
    d = float(d_entry.get())
    D = float(D_entry.get())
    left_gran = float(left_gran_entry.get())
    right_gran = float(right_gran_entry.get())
    mu = float(mu_entry.get())
    mu_0 = float(mu_0_entry.get())

    lengths = np.linspace(left_gran, right_gran, 20000)
    B_values = []
    L_c_values = []
    N_values = []
    valid_lengths = []

    for l in lengths:
        B, L_c, N = calculate_inductance_and_field(L, D, d, l, mu, mu_0)
        if B != 0 and L_c != 0 and N != 0:
            B_values.append(B)
            L_c_values.append(L_c)
            N_values.append(N)
            valid_lengths.append(l)

    max_B = max(B_values)
    index_max_B = B_values.index(max_B)
    best_l = valid_lengths[index_max_B]
    best_L_c = L_c_values[index_max_B]
    best_N = N_values[index_max_B]

    result_text.set(f'Длина каркаса l (м): {format_number(best_l)}\n'
                    f'Магнитная индукция B (Тл): {format_number(max_B)}\n'
                    f'Индуктивность L (Гн): {format_number(best_L_c)}\n'
                    f'Число витков N: {best_N}')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.plot(valid_lengths, B_values, label='Магнитная индукция B')
    ax1.set_xlabel('Длина каркаса l (м)')
    ax1.set_ylabel('Магнитная индукция B (Тл)')
    ax1.set_title('Зависимость магнитной индукции B\nот длины каркаса l')
    ax1.grid(True)
    ax1.legend()

    ax2.plot(valid_lengths, L_c_values, label='Индуктивность L', color='orange')
    ax2.set_xlabel('Длина каркаса l (м)')
    ax2.set_ylabel('Индуктивность L (Гн)')
    ax2.set_title('Зависимость индуктивности L\nот длины каркаса l')
    ax2.grid(True)
    ax2.legend()

    for widget in right_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def format_number(number):
    if number == 0:
        return '0'
    elif 0.01 <= abs(number) < 100:
        return f'{number:.2f}'
    else:
        return f'{number:.2e}'

# Создание основного окна
root = tk.Tk()
root.title("Расчет индуктивности катушки")

# Создание фреймов для размещения элементов
left_frame = ttk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N)

right_frame = ttk.Frame(root)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N+tk.E+tk.S+tk.W)
right_frame.pack_propagate(False)

# Ввод параметров
ttk.Label(left_frame, text="Длина провода L (м):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
L_entry = ttk.Entry(left_frame)
L_entry.grid(row=0, column=1, padx=5, pady=5)
L_entry.insert(0, "10")

ttk.Label(left_frame, text="Диаметр провода d (м):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
d_entry = ttk.Entry(left_frame)
d_entry.grid(row=1, column=1, padx=5, pady=5)
d_entry.insert(0, "0.001")

ttk.Label(left_frame, text="Диаметр каркаса D (м):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
D_entry = ttk.Entry(left_frame)
D_entry.grid(row=2, column=1, padx=5, pady=5)
D_entry.insert(0, "0.1")

ttk.Label(left_frame, text="Левая граница l (м):").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
left_gran_entry = ttk.Entry(left_frame)
left_gran_entry.grid(row=3, column=1, padx=5, pady=5)
left_gran_entry.insert(0, "0.01")

ttk.Label(left_frame, text="Правая граница l (м):").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
right_gran_entry = ttk.Entry(left_frame)
right_gran_entry.grid(row=4, column=1, padx=5, pady=5)
right_gran_entry.insert(0, "10")

ttk.Label(left_frame, text="Магнитная проницаемость Гн/м:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
mu_entry = ttk.Entry(left_frame)
mu_entry.grid(row=5, column=1, padx=5, pady=5)
mu_entry.insert(0, "1")

ttk.Label(left_frame, text="Магнитная постоянная Гн/м:").grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
mu_0_entry = ttk.Entry(left_frame)
mu_0_entry.grid(row=6, column=1, padx=5, pady=5)
mu_0_entry.insert(0, "1.257e-7")

# Кнопка для обновления графиков
ttk.Button(left_frame, text="Рассчитать", command=update_graphs).grid(row=7, columnspan=2, pady=10)

# Вывод результатов
result_text = tk.StringVar()
ttk.Label(left_frame, textvariable=result_text).grid(row=8, columnspan=2, pady=10)

# Настройки для масштабирования
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(0, weight=1)

root.mainloop()

