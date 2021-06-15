def main():
    print('*** Remove character at specific index ***')
    strObj = "This is a samplez string"
    # Slice string to remove character at index 5
    for i in range(len(strObj)):
        if strObj[i - 1] == "z":
            strObj = strObj[0: i - 1:] + strObj[i::]
    print('Modified String : ', strObj)


if __name__ == '__main__':
    main()
