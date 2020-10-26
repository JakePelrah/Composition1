import random


class PlayableNote:
    def __init__(self, note, note_value):
        self.note = note
        self.note_value = note_value

    def get_note_name(self):
        return self.note

    def get_note_value(self):
        return self.note_value

    def __str__(self):
        ratio_tuple = self.note_value.as_integer_ratio()
        ratio = str (ratio_tuple[0]) + '/' + str(ratio_tuple[1])
        return 'Note Name:{}\nNote Value:  {}\n'.format(self.note, ratio )


def get_bar_length(bar):
    return sum([length.note_value for length in bar])


def create_random_playable_note(notes, note_values):
    return PlayableNote(random.sample(notes, 1)[0], random.sample(note_values, 1)[0])


def create_bar(notes, note_values):
    bar = []
    while get_bar_length(bar) != 4:
        if get_bar_length(bar) > 4:
            bar = []
        bar.append(create_random_playable_note(notes, note_values))
    return bar


def create_bars(num_bars, notes, note_values):
    bars = []
    for num in range(0, num_bars):
        bars.append(create_bar(notes, note_values))
    return bars


def main():
    # Notes of A dorian
    notes = ['A', 'B', 'C', 'D', 'E', 'F#', 'G', 'REST']
    # half, quarter, eighth, sixteenth
    note_values = [2, 1, 1/2, 1/4]
    bars = create_bars(20, notes, note_values)
    with open('randomLine.txt', 'w') as outfile:
        for index, bar in enumerate(bars):
            row = 30 * '*' + ' Bar: {} '.format(index + 1) + 30 * '*' + '\n'
            print(row)
            outfile.write(row)
            for notes in bar:
                print(notes)
                outfile.write(str(notes) + '\n')


if __name__ == "__main__":
    main()
