from PIL import Image

# Загружаем изображение
image = Image.open("new23.png").convert("RGB")
pixels = image.load()

# Читаем координаты из файла
coords = []
with open("keys23.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.replace("(", "")
        line = line.replace(")", "")
        x, y = line.split(",")
        coords.append((int(x), int(y)))

# Извлекаем синий канал и собираем байты
text_bytes = []
for x, y in coords:
    r, g, b = pixels[x, y]  # Получаем значения RGB
    text_bytes.append(b)  # Берём только синий канал

# Преобразуем байты в текст
decoded_text = bytes(text_bytes).decode("utf-8", errors="ignore")
print("Декодированный текст:")
print(decoded_text)






message = "what the f" # Текст для кодирования
message += "#" # Добавляем символ конца строки

# Переводим текст в биты
bits = ""
for symbol in message:
    bits += format(ord(symbol), "08b")

# Выводим биты первого символа
first_symbol_bits = format(ord(message[0]), "08b")
print("\nБиты первого символа:")
print(message[0], "->", first_symbol_bits)

# Кодирование текста
bit_index = 0
for y in range(image.height):
    for x in range(image.width):
        if bit_index < len(bits):
            r, g, b = pixels[x, y]
            old_pixel = (r, g, b) # Исходное значение пикселя
            bit = int(bits[bit_index]) # Берём очередной бит сообщения
            b = (b & 254) | bit # Меняем младший бит синего канала
            new_pixel = (r, g, b) # Изменённый пиксель
            pixels[x, y] = (r, g, b) # Сохраняем пиксель

            # Вывод информации
            print("\nПиксель:", (x, y))
            print("Исходный:", old_pixel)
            print("Изменённый:", new_pixel)

            bit_index += 1

# Сохраняем изображение
image.save("encoded_image.png")
print("\nКодирование завершено")





encoded = Image.open("encoded_image.png")
pixels2 = encoded.load()

decoded_bits = ""
for y in range(encoded.height):
    for x in range(encoded.width):
        r, g, b = pixels2[x, y]
        decoded_bits += str(b & 1) # Считываем младший бит синего канала

# Преобразуем биты в текст
decoded_message = ""
for i in range(0, len(decoded_bits), 8):
    byte = decoded_bits[i:i+8]
    if len(byte) == 8:
        symbol = chr(int(byte, 2))
        if symbol == "#": break # Символ конца сообщения
        decoded_message += symbol

print("\nДекодированное сообщение:")
print(decoded_message)