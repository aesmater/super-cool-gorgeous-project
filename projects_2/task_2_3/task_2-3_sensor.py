operator=input("Имя оператора: ")
bar_count=input("Текущее значение давления (Па): ")
with open(r'C:\Users\ready\Documents\alekseen_id\projects_2\task_2_3\sensor_log.txt', "w", encoding="utf-8") as list:
    
    list.write(f"ОПЕРАТОР\t\tЗНАЧЕНИЕ\n{operator}\t\t{bar_count}")

print("Данные успешно сохранены в sensor_log.txt")