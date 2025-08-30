import requests


def test_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    print(data)
    assert data["id"] != 1, f"expected: id = 1, received: {data["id"]}"

    print("Test Passed")


if __name__ == "__main__":
    test_api()
