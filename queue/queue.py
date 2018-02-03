test_case_num = int(input())

for test_case in range(test_case_num):
    people_in_queue = int(input())
    before_queue = list(range(1, people_in_queue + 1))
    after_queue = [int(i) for i in input().split(' ')]
    changed = 0
    too_chaotic = False
    for person_num in before_queue:
        new_index = after_queue.index(person_num) + 1
        if new_index < person_num:
            change_diff = person_num - new_index
            print(change_diff)
            if change_diff > 2:
                too_chaotic = True
                break
            changed += change_diff
    if too_chaotic:
        print('Too chaotic')
    else:
        print(changed)
