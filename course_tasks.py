import this
import calendar
from datetime import date

# 2.3.3
print("\n2.3.3")
number = int(input("Enter three digits (each digit for one pig): "))
sum = number % 100 % 10 + number % 100 // 10 + number // 100
print(sum)
print(sum // 3)
print(sum % 3)
print(not bool(sum % 3))

# 3.2.1
print("\n3.2.1")
print('"Shuffle, Shuffle, Shuffle", say it together!\n Change colors and directions,\n Don\'t back down and stop\
 the player!\n\t\t Do you want to play Taki?\n\t\t Press y\\n')

# 3.3.3
print("\n3.3.3")
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
print(encrypted_message[::-2])

# 3.4.2
print("\n3.4.2")
stri = input("Please enter a string: ")
first = stri[:1]
print(first + stri[1:].replace(first, "e") * bool(stri))

# 3.4.3
print("\n3.4.3")
strin = input("Please enter a string: ")
print(strin[:len(strin) // 2].lower() + strin[len(strin) // 2:].upper())

# 4.2.2
print("\n4.2.2")
word = input("Enter a word: ")
if word[::-1] == word:
    print("OK")
else:
    print("NOT")

# 4.2.3
print("\n4.2.3")
temp = input("Insert the temperature you would like to convert: ")
num = float(temp[:-1])
if temp[-1] == "F":
    c_num = (num * 5 - 160) / 9
    if c_num.is_integer():
        print(str(int(c_num)) + "C")
    else:
        print(str(c_num) + "C")
elif temp[-1] == "C":
    f_num = (9 * num + (32 * 5)) / 5
    if f_num.is_integer():
        print(str(int(f_num)) + "F")
    else:
        print(str(f_num) + "F")
else:
    print("not legal")

# 4.2.4
print("\n4.2.4")
date = input("Enter a date: ")
num_day = calendar.weekday(int(date[-4:len(date)]), int(date[3:5]), int(date[0:2]))
if num_day == 0:
    print("Monday")
elif num_day == 1:
    print("Tuesday")
elif num_day == 2:
    print("Wednesday")
elif num_day == 3:
    print("Thursday")
elif num_day == 4:
    print("Friday")
elif num_day == 5:
    print("Saturday")
else:
    print("Sunday")

# 5.3.4
print("\n5.3.4")
def last_early(my_str):
    if len(my_str) <= 1:
        return False
    elif my_str[-1].upper() in my_str[0:-1] or my_str[-1].lower() in my_str[0:-1]:
        return True
    return False
print(last_early("X"))

# 5.3.5
print("\n5.3.5")
def distance(num1, num2, num3):
    if (abs(num1 - num2) == 1 or abs(num1 - num3) == 1) and (
            abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2 or abs(num3 - num2) >= 2 and abs(num3 - num1) >= 2):
        return True
    else:
        return False
print(distance(1, 2, 10))

# 5.3.6
print("\n5.3.6")
def fix_age(age):
    if 13 <= age <= 19 and age != 15 and age != 16:
        age = 0
    return age
def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)
print(filter_teens(2, 1, 15))

# 5.3.7
print("\n5.3.7")
def chocolate_maker(small, big, x):
    if x - small - big * 5 <= 0:
        return True
    return False
print(chocolate_maker(3, 2, 10))

# 6.1.2
print("\n6.1.2")
def shift_left(my_list):
    a, b, c = my_list
    my_list[0] = b
    my_list[1] = c
    my_list[2] = a
    return my_list
print(shift_left(['monkey', 2.0, 1]))

# 6.2.3
print("\n6.2.3")
def format_list(my_list):
    new_list = my_list[::2]
    str = ", ".join(new_list) + ", and " + my_list[-1]
    return str
print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))

# 6.2.4
print("\n6.2.4")
def extend_list_x(list_x, list_y):
    list_x[0:0] = list_y
    return list_x
print(extend_list_x([4, 5, 6], [1, 2, 3]))

# 6.3.1
print("\n6.3.1")
def are_lists_equal(list1, list2):
    if sorted(list1) == sorted(list2):
        return True
    return False
list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
print(are_lists_equal(list1, list2))
print(are_lists_equal(list1, list3))

# 6.3.2
print("\n6.3.2")
def longest(my_list):
    return max(my_list, key=len)
list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))

# 7.1.4
print("\n7.1.4")
def squared_numbers(start, stop):
    my_list = []
    while start <= stop:
        my_list.append(start ** 2)
        start += 1
    return my_list
print(squared_numbers(-3, 3))

# 7.2.1
print("\n7.2.1")
def is_greater(my_list, n):
    new_list = []
    for x in my_list:
        if x > n:
            new_list.append(x)
    return new_list
result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)

# 7.2.2
print("\n7.2.2")
def numbers_letters_count(my_str):
    my_list = [0, 0]
    for tav in my_str:
        if tav.isdigit():
            my_list[0] += 1
        else:
            my_list[1] += 1
    return my_list
print(numbers_letters_count("Python 3.6.3"))

# 7.2.4
print("\n7.2.4")
def seven_boom(end_number):
    my_list = []
    for num in range(end_number + 1):
        if num % 7 == 0 or '7' in str(num):
            my_list.append("BOOM")
        else:
            my_list.append(num)
    return my_list
print(seven_boom(17))

# 7.2.5
print("\n7.2.5")
def sequence_del(my_str):
    new_string = ""
    if len(my_str) > 0:
        last_str = my_str[0]
    else:
        return new_string
    new_string += last_str
    for letter in my_str:
        if last_str != letter:
            new_string += letter
            last_str = letter
    return new_string
print(sequence_del("Heeyyy   yyouuuu!!!"))

# 7.2.6
print("\n7.2.6")
products_str = input("Enter the groceries: ")
products_list = products_str.split(",")
while True:
    num = int(input("Enter action: "))
    if num == 1:
        print(",".join(products_list))
    elif num == 2:
        print(len(products_list))
    elif num == 3:
        name = input("Enter product name to search: ")
        if name in products_list:
            print(name)
    elif num == 4:
        name = input("Enter product name to count: ")
        print(products_list.count(name))
    elif num == 5:
        name = input("Enter product name to delete: ")
        products_list.remove(name)
    elif num == 6:
        name = input("Enter product name to add: ")
        products_list.append(name)
    elif num == 7:
        for product in products_list:
            if len(product) < 3:
                print(product)
            else:
                for letter in product:
                    if not letter.isalpha():
                        print(product)
                        break;
    elif num == 8:
        products_list = list(dict.fromkeys(products_list))
    elif num == 9:
        break

# 7.2.7
print("\n7.2.7")
def arrow(my_char, max_length):
    str = ""
    for i in range(max_length):
        str += (my_char + " ") * i + my_char + "\n"
    for i in range(max_length - 1, 1, -1):
        str += (my_char + " ") * (i - 1) + my_char + "\n"
    if max_length > 0:
        str += my_char
    return str
print(arrow('*', 5))

# 8.2.1
print("\n8.2.1")
data = ("self", "py", 1.543)
format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"
print(format_string % data)

# 8.2.2
print("\n8.2.2")
def tuples_product_key(my_tuple):
    return my_tuple[1]
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=tuples_product_key, reverse=True)
products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))

# 8.2.3
print("\n8.2.3")
def mult_tuple(tuple1, tuple2):
    combinations = []
    for a in range(len(tuple1)):
        for b in range(len(tuple2)):
            combinations.append((tuple1[a], tuple2[b]))
    for a in range(len(tuple2)):
        for b in range(len(tuple1)):
            combinations.append((tuple2[a], tuple1[b]))
    return tuple(combinations)
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))

# 8.2.4
print("\n8.2.4")
def sort_anagrams(list_of_strings):
    my_list_of_strings = list_of_strings.copy()
    all_list = []
    processed_words = []
    for current_word in my_list_of_strings:
        if current_word in processed_words:
            continue
        current_list = []
        for word in my_list_of_strings:
            if sorted(current_word) == sorted(word):
                current_list.append(word)
                processed_words.append(word)
        all_list.append(current_list)
    return all_list
list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',\
                 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))

# 8.3.2
print("\n8.3.2")
mariah_dict = {"first name": "Mariah", "last name": "Carey", "birth date": "27.03.1970",
               "hobbies": ["Sing", "Compose", "Act"]}
action = int(input("Enter action (1-7): "))
if action == 1:
    print(mariah_dict["last name"])
elif action == 2:
    print(mariah_dict["birth date"][3:5])
elif action == 3:
    print(len(mariah_dict["hobbies"]))
elif action == 4:
    print(mariah_dict["hobbies"][len(mariah_dict["hobbies"]) - 1])
elif action == 5:
    mariah_dict["hobbies"] = "hobbies"
elif action == 6:
    original_tuple = tuple(mariah_dict["birth date"].split("."))
    new_list = []
    for number in original_tuple:
        new_list.append(int(number))
    mariah_dict["birth date"] = tuple(new_list)
    print(mariah_dict["birth date"])
elif action == 7:
    birthday_tuple = tuple(mariah_dict["birth date"].split("."))
    new_list = []
    for number in birthday_tuple:
        new_list.append(int(number))
    birthday_tuple = tuple(new_list)
    today = date.today()
    age = today.year - birthday_tuple[2] - ((today.month, today.day) < (birthday_tuple[1], birthday_tuple[0]))
    mariah_dict["age"] = age
    print(mariah_dict["age"])

# 8.3.3
print("\n8.3.3")
def count_chars(my_str):
    dict = {}
    for letter in my_str:
        if letter == " ":
            continue
        if letter in dict.keys():
            dict[letter] = dict[letter] + 1
        else:
            dict[letter] = 1
    return dict
magic_str = "abra cadabra"
print(count_chars(magic_str))

# 8.3.4
print("\n8.3.4")
def inverse_dict(my_dict):
    new_dict = {}
    for item in my_dict.items():
        if item[1] in new_dict.keys():
            new_dict[item[1]].append(item[0])
        else:
            new_dict[item[1]] = [item[0]]
    return new_dict
course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))

# 9.1.1
print("\n9.1.1")
def are_files_equal(file1, file2):
    file_object1 = open(file1, 'r')
    file_object2 = open(file2, 'r')
    if file_object1.read() == file_object2.read():
        value = True
    else:
        value = False
    file_object1.close()
    file_object2.close()
    return value
# print(are_files_equal("vacation.txt", "work.txt"))

# 9.1.2
print("\n9.1.2")
# sampleFile.txt
path = input("Enter a file path: ")
action = input("Enter a task: ")
my_file = open(path, 'r')
if action == "sort":
    words_list = []
    for line in my_file:
        if "\n" in line:
            line_list = line[:-1].split(" ")
        else:
            line_list = line.split(" ")
        for word in line_list:
            if word not in words_list:
                words_list.append(word)
    words_list.sort()
    print(words_list)
elif action == "rev":
    for line in my_file:
        if "\n" in line:
            print(line[-2::-1])
        else:
            print(line[::-1])
elif action == "last":
    n = int(input("Enter a number: "))
    read_file = my_file.read()
    lines = read_file.count("\n") + 1
    list_lines = read_file.split("\n")
    for i in range(lines - n, lines):
        print(list_lines[i])
my_file.close()

# 9.2.2
print("\n9.2.2")
def copy_file_content(source, destination):
    source_file = open(source, 'r')
    destination_file = open(destination, 'w')
    destination_file.write(source_file.read())
    source_file.close()
    destination_file.close()
# copy_file_content("copy.txt", "paste.txt")

# 9.2.3
print("\n9.2.3")
def who_is_missing(file_name):
    my_file = open(file_name, 'r')
    numbers_list = my_file.read().split(",")
    for number in range(len(numbers_list)):
        numbers_list[number] = int(numbers_list[number])
    my_file.close()
    last_number = len(numbers_list) + 1
    for i in range(1, last_number + 1):
        if i not in numbers_list:
            break
    found_file = open("found.txt", 'w')
    found_file.write(str(i))
    found_file.close()
    return i
# print(who_is_missing("findMe.txt"))

# 9.3.1
print("\n9.3.1")
def my_mp3_playlist(file_path):
    songs_file = open(file_path, 'r')
    songs_data = songs_file.read()
    songs_file.close()
    songs_list = songs_data.split("\n")
    max_length = -1
    longest_song = "no songs"
    artists_dict = {}
    for song in songs_list:
        song_details = song.split(';')
        song_length = int(song_details[2][0]) * 60 + int(song_details[2][2]) * 10 + int(song_details[2][3])
        if song_length > max_length:
            max_length = song_length
            longest_song = song_details[0]
        if song_details[1] in artists_dict:
            artists_dict[song_details[1]] += 1
        else:
            artists_dict[song_details[1]] = 1
    max_artist = 0
    max_artist_name = "no artist"
    for artist in artists_dict.keys():
        if artists_dict[artist] > max_artist:
            max_artist = artists_dict[artist]
            max_artist_name = artist
    my_tuple = (longest_song, len(songs_list), max_artist_name)
    return my_tuple
# print(my_mp3_playlist("songs.txt"))

# 9.3.2
print("\n9.3.2")
def my_mp4_playlist(file_path, new_song):
    songs_file = open(file_path, 'r')
    songs_data = songs_file.read()
    songs_file.close()
    songs_list = songs_data.split("\n")
    if len(songs_list) >= 3:
        line3_list = songs_list[2].split(";")
        line3_list[0] = new_song
        new_line3 = ';'.join(line3_list)
        songs_list[2] = new_line3
        new_data = '\n'.join(songs_list)
    else:
        lines_to_create = 3 - len(songs_list)
        for i in range(lines_to_create):
            songs_list.append("")
        songs_list[2] = new_song
        new_data = '\n'.join(songs_list)
    songs_file = open(file_path, 'w')
    songs_file.write(new_data)
    songs_file.close()
    songs_file = open(file_path, 'r')
    print(songs_file.read())
    songs_file.close()
# my_mp4_playlist("songs.txt", "Python Love Story")