def read_list(doc):
    with open(doc, 'rt', encoding='utf-8') as file:
        list = file.readlines()
        res = [doc, str(len(list))]
        for line in list:
            res.append(line.strip())
        return res


def write_file(doc_1, doc_2, doc_3):
    all_list = [read_list(doc_1), read_list(doc_2), read_list(doc_3)]
    all_list.sort(key=len)
    with open('4.txt', 'w', encoding='utf-8') as f:
        for i in all_list:
            for doc in i:
                f.write(f'{doc} \n')

write_file('1.txt', '2.txt', '3.txt')





