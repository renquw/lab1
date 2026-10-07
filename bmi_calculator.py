while True:
    try:
        weight = float(input("Введіть вашу вагу (в кг): "))
        height = float(input("Введіть ваш зріст (в м): "))
        if weight <= 0 or height <= 0:
            raise ValueError("Вага та зріст повинні бути додатними числами.")
        break
    except ValueError as e:
        print(f"Помилка: {e} Спробуйте ще раз.\n")
bmi = weight / (height ** 2)
print("\nРезультати обчислень:")
print(f"Ваш індекс маси тіла (ІМТ): {bmi:.2f}")
if bmi < 18.5:
    print("Це свідчить про недостатню масу тіла.")
elif 18.5 <= bmi < 24.9:
    print("Це нормальна маса тіла.")
else:
    print("Це свідчить про надмірну масу тіла.")
