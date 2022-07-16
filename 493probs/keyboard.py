num_kb, num_note = [int(i) for i in input().split()]
keyboards = []
for _ in range(num_kb):
    line = [int(i) for i in input().split()[1:]]
    line = set(line)
    keyboards.append(line)
song = [int(i) for i in input().split()]


def countNotes(keyboard, notes):
    for i, note in enumerate(notes):
        if not note in keyboard:
            return i
    return len(notes)


count = 0
while len(song) > 0:
    notes_played = max([countNotes(keyboard, song) for keyboard in keyboards])
    song = song[notes_played:]
    count += 1

print(count-1)