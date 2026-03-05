nutrient_medium=input("Название среды: ")
agar_concentration=input("Концентрация агара(%): ")
sterilization_t=input("Температцра стерилизации(°C): ")
with open(r'C:\Users\ready\Documents\alekseen_id\projects_2\task_2_3\recipe.txt', "w", encoding="utf-8") as recipe:
    
    recipe.write(f"\t {nutrient_medium.upper()}\n")
    recipe.write(f"Концентрация агара(%): {agar_concentration}\n")
    recipe.write(f"Температура стерилизации(°C) {sterilization_t}\n")

print("Файл 'recipe.txt' успешно сформирован!")