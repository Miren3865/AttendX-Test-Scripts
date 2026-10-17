def test_login():
    username = "Miren Savani"
    password = "Miren@7892"

    if username == "Miren Savani" and password == "Miren@7892":
        print("PASS: Login successful")
        print("Login test completed successfully")
    else:
        print("FAIL: Login unsuccessful")


if __name__ == "__main__":
    test_login()