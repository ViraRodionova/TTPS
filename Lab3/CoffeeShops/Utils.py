def load_content(filename):
    f = open(filename, 'r')
    content = f.readlines()
    f.close()

    return content


def get_string(content, i):
    c = content[i]
    c = c[:-1]
    c = c.split(' ')

    return c
