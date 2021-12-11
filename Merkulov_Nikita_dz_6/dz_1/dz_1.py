with open('nginx_logs.txt', 'r', encoding='utf-8') as i:
    for line in i:
        content = [line.split()[0], line.split()[5][1:], line.split()[6]]
        for f in content:
            print(f)
# i.close()
