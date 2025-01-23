import os
import subprocess

# Пароль для файлов .p12
password = "12345678"

# Имя выходного файла
output_file = "output.txt"

# Получение списка всех файлов в текущем каталоге с расширением .p12
p12_files = [f for f in os.listdir(os.getcwd()) if f.endswith(".p12")]

if not p12_files:
    print("Файлы .p12 не найдены в текущем каталоге.")
else:
    with open(output_file, "w", encoding="utf-8") as out:
        for file in p12_files:
            try:
                # Выполнение команды openssl
                result = subprocess.run(
                    [
                        "openssl", "pkcs12", "-info", "-in", file, "-passin", f"pass:{password}"
                    ],
                    text=True,
                    capture_output=True,
                    check=True
                )

                # Запись результата в выходной файл
                out.write(f"===== {file} =====\n")
                out.write(result.stdout)
                out.write("\n\n")
                print(f"Обработан файл: {file}")
            except subprocess.CalledProcessError as e:
                out.write(f"===== {file} =====\n")
                out.write("Ошибка обработки файла:\n")
                out.write(e.stderr)
                out.write("\n\n")
                print(f"Ошибка при обработке файла {file}. Подробности записаны в {output_file}.")

    print(f"Содержимое всех файлов записано в {output_file}.")
