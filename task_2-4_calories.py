protein_mass=int(input("Белки: "))
fats_mass=int(input("Жиры: "))
carbs_mass=int(input("Углеводы: "))
calories=protein_mass*4+fats_mass*9+carbs_mass*4
print(f"Общая калорийность: {calories}")