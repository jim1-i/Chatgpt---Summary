def read_txt_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def write_txt_file(file_path: str, content: str):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
