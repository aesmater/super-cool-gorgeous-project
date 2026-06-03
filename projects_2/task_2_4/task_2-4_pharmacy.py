total=int(input("Общее число капсул: "))
quantity=int(input("Число капсул в одной "))
int=total // quantity
rest=total % quantity
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок: {int}")
print(f"Остаток капсул: {rest}")

