from functions.get_file_content import get_file_content


def test():
    result = get_file_content("calculator", "lorem.txt")
    print("Result for lorem.txt:")
    # Extract content length and check for truncation
    if '\n[...File "lorem.txt"Content truncated' in result:
        content_part = result.split('\n[...File "lorem.txt"Content truncated')[0]
        content_length = len(content_part)
        truncation_message = result.split('\n[...File "lorem.txt"Content truncated')[1].strip(']')
        print(f"Content length: {content_length}")
        print(f"Truncation message: {truncation_message}")
    else:
        content_length = len(result)
        print(f"Content length: {content_length}")
        print("Truncation message: None")
    print("")

    result = get_file_content("calculator", "main.py")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin' directory:")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()
