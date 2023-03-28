import os

def get_file_path(filename=None):
    if filename:
        return os.path.join(os.path.dirname(__file__), filename)
    return os.path.dirname(__file__)

def get_file_content(filename=None):
    if filename:
        with open(get_file_path(filename), "r") as f:
            return f.read()
    return None

def get_file_lines(content=None):
    if content:
        return content.splitlines()
    return None

def filter_lines_by_keywoard(lines=None, keyword=None):
    if lines and keyword:
        return [line for line in lines if keyword in line]
    return None

def save_to_file(filename=None, lines=None):
    if filename and lines:
        with open(get_file_path(filename), "w") as f:
            for line in lines:
                f.write(line + "\n")
        return True
    return None

if __name__ == "__main__":
    keywoard = "sova"
    content = get_file_content("text.txt")
    lines = get_file_lines(content)
    filtered = filter_lines_by_keywoard(lines, keywoard)
    save_to_file("filtered.txt", filtered)


