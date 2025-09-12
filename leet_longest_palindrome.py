def find_longest_palindrome(my_string):
    longest_palindrome = ''
    palindromes = []
    for i in range(len(my_string)):
        current_odd_palindrome = find_palindrome(my_string, i - 1, i + 1)
        current_even_palindrome = find_palindrome(my_string, i, i + 1)
        if current_even_palindrome != '':
            palindromes.append(current_even_palindrome)

        if current_odd_palindrome != '':
            palindromes.append(current_odd_palindrome)

        longest_palindrome = max(
            current_odd_palindrome, current_even_palindrome, longest_palindrome)

    return longest_palindrome, palindromes


def find_palindrome(my_string, i, j):
    start, end = i, j
    current_palindrome = ''
    print(f"Value of start, end = {start}, {end}")
    while start >= 0 and end <= len(my_string) - 1 and my_string[start] == my_string[end]:
        current_palindrome = my_string[start:end+1]
        print(f"Current Palindrome = {current_palindrome}")
        print(f"Value of start, end = {start}, {end}")
        start -= 1
        end += 1

    return current_palindrome


if __name__ == "__main__":
    longest_palindrome, palindromes = find_longest_palindrome("pabbapaqa")
    print(f"The list of palindromes are {palindromes}")
    print(f"The longest palindrome is {longest_palindrome}")
