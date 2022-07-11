# Do not modify this list
phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323", "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]

ugly_phone_list = ["98-333-111", "12--323-566", "123-34-221", "99-948-321", "-12-123-346",
                   "894-58438-543", "85-234-222",
                   "12-333-444-", "99-888--433", "15-465-876", "98-555-22", "-3-355-333", "3--344-53", "--2--45---",
                   "11-111-222", "12#22$34$222", "98 223 555"]

correct = phone_list.copy()
incorrect = []

for i in correct:
    if 10 != len(i):
        correct.remove(i)
print("Correct List of Phone Numbers")
print(correct)

for i in phone_list:
    if len(i) != 10:
        incorrect.append(i)
print("Incorrect List of Phone Numbers")
print(incorrect)

print("The area Codes:")
list_area = []
list_area_codes = []
for i in correct:
    list_area.append(i[0:2])
print(list_area)

numbers_without_area_codes = []
for i in correct:
    numbers_without_area_codes.append(i[3:10])
print("The Numbers without area codes:")
print(numbers_without_area_codes)

list_area_codes = sorted(set(list_area))
print("The unique area Codes")
print(list_area_codes)

total_34 = 0
for i in correct:
    if i[0:2] == '34':
        total_34 = total_34 + 1

total_72 = 0
for i in correct:
    if i[0:2] == '72':
        total_72 = total_72 + 1

total_98 = 0
for i in correct:
    if i[0:2] == '98':
        total_98 = total_98 + 1

print(f"You have {total_34} numbers from area 34, {total_72} numbers from area 72 and {total_98} numbers from area 98.")
