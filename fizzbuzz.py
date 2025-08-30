def fizzbuzz(n=100, fizz=3, buzz=5):
    for i in range(1, n+1):
        s = ""
        if i % fizz == 0:
            s = "fizz"
        if i % buzz == 0:
            s += "buzz"
        if s == "":
            s = str(i)
        print(f"For {i}: {s}")


if __name__ == "__main__":
    fizzbuzz(200, 2, 5)
