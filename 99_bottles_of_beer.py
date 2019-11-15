# project to write the song 99 bottles of beer on the wall
# cannot use numbers in song, except "take 1 down"
for i in range(99, 0, -1):
    if i > 1:
        print(f'\n\n{i} bottles of beer on the wall. \n{i} bottles of beer.')
        print("Take one down, pass it around...")
        i -= 1
        if i > 1:
            print(f'{i} bottles of beer on the wall.')
        else:
            print(f'{i} bottle of beer on the wall.')
    else:
        print(f"\n\n{i} bottle of beer on the wall. {i} bottle of beer.")
        print("Take one down, pass it around...")
        print("No more bottles of beer on the wall.")
input("Press ENTER to exit: ")
