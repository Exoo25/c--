def log(  text):
        print(text)
def error(  text):
        print(f"\033[31m× \033[37m{text}\033[0m")
def info(  text):
        print(f"\033[32m𝔦\033[37m{text}\033[0m")
def clear():
        print("\033[H\033[J",  end="")  # Moves cursor to the top and clears the screen
