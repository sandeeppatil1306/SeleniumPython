with open('TestFile.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('TestFile.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
