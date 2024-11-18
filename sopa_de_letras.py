import json

def find_word(letter_soup, word):
    rows = len(letter_soup)
    cols = len(letter_soup[0])

    def check_direction(start_row, start_col, delta_row, delta_col):
        for i in range(len(word)):
            row = start_row + i * delta_row
            col = start_col + i * delta_col
            if row < 0 or row >= rows or col < 0 or col >= cols or letter_soup[row][col] != word[i]:
                return False
        return True

    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (-1, -1), (1, -1), (-1, 1),
    ]

    for row in range(rows):
        for col in range(cols):
            for delta_row, delta_col in directions:
                if check_direction(row, col, delta_row, delta_col):
                    return True

    return False

def find_words(letter_soup, words):
    result = {}
    for word in words:
        result[word] = find_word(letter_soup, word.upper())
    return result

def get_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    print("Contenido leído desde el archivo:")
    print(repr(content))

    content = content.strip().split("---")
    if len(content) != 2:
        raise ValueError("El archivo de entrada no tiene el formato esperado. Asegúrate de incluir '---' como separador.")

    soup_part = content[0].strip().splitlines()
    words_part = content[1].strip().splitlines()
    letter_soup = [list(line.replace(" ", "").upper()) for line in soup_part]
    words = [word.strip() for word in words_part]
    return letter_soup, words

def write_json_report(report, output_path):
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(report, json_file, indent=4)

def main(input_file, output_file):
    letter_soup, words = get_file_content(input_file)
    results = find_words(letter_soup, words)
    write_json_report(results, output_file)
    print(f"Reporte generado exitosamente: {output_file}")

if __name__ == "__main__":
    input_file = r"C:\Users\xXSta\OneDrive\Escritorio\Sopa_de_letras\sopa_de_letras.txt"
    output_file = r"C:\Users\xXSta\OneDrive\Escritorio\Sopa_de_letras\resultado.json"

    main(input_file, output_file)
