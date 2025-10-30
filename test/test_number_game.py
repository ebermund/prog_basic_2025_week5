import random

MAX_TRIES = 7

def ask_int(prompt: str, input_func=input) -> int:
    """整数を入力させる。失敗時は再入力を求める"""
    while True:
        s = input_func(prompt)
        try:
            return int(s)
        except ValueError:
            print("整数を入力してください。")

def play(randint_func=random.randint, input_func=input, print_func=print) -> None:
    answer = randint_func(1, 100)
    tries = 0
    print_func("1〜100の数を当ててください！")

    while tries < MAX_TRIES:
        guess = ask_int("予想した数: ", input_func)
        tries += 1

        if guess == answer:
            print_func(f"正解！{tries}回で当たりました！")
            return
        elif guess < answer:
            print_func("もっと大きいです。")
        else:
            print_func("もっと小さいです。")

    print_func(f"残念！正解は {answer} でした。")

if __name__ == "__main__":
    play()
