from tqdm import tqdm
import time

def count(n):
    count = 0
    for i in tqdm(
        range(n),
        desc="Йде підрахунок",
        ncols=70,
        colour="#009FBD",
    ):
        count += 1
        time.sleep(0.1)
    return count
total = count(20)
print(f"Всього підраховано: {total}")