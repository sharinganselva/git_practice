import requests


def test_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    print(data)
    assert data["id"] == 1, f"expected: id = 1, received: {data["id"]}"

    print("Test Passed")


def test_another_api():
    url = "http://www.google.com"
    response = requests.get(url)
    assert response.status_code == 200

    result = response.text
    print(result)
    print(response.headers.get("Content-Type"))


if __name__ == "__main__":
    test_api()
    test_another_api()
