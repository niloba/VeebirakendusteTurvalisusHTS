from PIL import Image

morse_code_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7",
    "---..": "8", "----.": "9", "-----": "0", "/": " ",
}

def analyze_morse_code(image_path):

    image = Image.open(image_path)
    pixels = image.load()

 
    width, height = image.size
    row_length = width

    morse_code_symbols = []


    last_white_pixel = -1
    for row in range(height):
        for col in range(row * row_length, (row + 1) * row_length):
            pixel = pixels[col % width, row]

        
            if pixel == (255, 255, 255):
                if last_white_pixel != -1:
                    offset = col - last_white_pixel
                    morse_code_symbols.append(offset)

                last_white_pixel = col

  
    morse_code = ""
    for symbol in morse_code_symbols:
        if symbol > 0:
            morse_code += "."
        elif symbol < 0:
            morse_code += "-"
        elif symbol == 0:
            morse_code += "/"

   
    words = morse_code.split(" / ")
    decoded_message = ""
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            if letter in morse_code_dict:
                decoded_message += morse_code_dict[letter]
            else:
                decoded_message += "?"
        decoded_message += " "

    return decoded_message.strip()


image_path = "MorzaImage.png"
decoded_text = analyze_morse_code(image_path)
print(decoded_text)