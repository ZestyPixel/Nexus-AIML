def remove_and_strip(word, lst):
    new_list = []
    for item in lst:
        new_list.append(item.strip(word))
    return new_list

my_list = ['  apple', 'banana', ' cherry ', 'date']
print(remove_and_strip('e', my_list))