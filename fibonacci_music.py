import winsound
import time


# A 440, Bb 466.16, B 493.88, C 261.63, Db 277.18, D 293.66,
#  Eb 311.13, E 329.63, F 349.21, Gb 369.99, G 392, Ab 425.3

pentatonic_c_major = ['C', 'D', 'E', 'G', 'A']
blues_c_major = ['C', 'Eb', 'F', 'Gb', 'Bb']
ionian_c_major = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
phrygian_c_major = ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E']

all_notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
frequencies = [261, 277, 294, 311, 330, 349, 370, 392, 425, 440, 466, 494]

array_of_scales = [pentatonic_c_major, blues_c_major, ionian_c_major, phrygian_c_major, all_notes]


def fibonacci(n):
    # fibonacci sequence is used to determine next note to be played
    a, b = 0, 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


def note_len(n):
    # this determines the length of the note based on the num in fibonacci sequence
    # for simplicity notes are just split into 4 note lengths
    if n % 4 == 0:
        return 1000
    elif n % 4 == 1:
        return 750
    elif n % 4 == 2:
        return 500
    else:
        return 250


def play_music(scale):
    print("You selected the scale\n{}\n".format(scale))
    for i in range(2, 50):
        # fibonacci note is the next num in fibonacci sequence mod the scale length so we do not leave the scale
        fibonacci_note = fibonacci(i) % len(scale)

        # print out all info
        print("fibonacci {} = {} : {} Hz".format(fibonacci(i), scale[fibonacci_note],
                                                 frequencies[fibonacci_note]))
        # play sound
        winsound.Beep(frequency=frequencies[fibonacci_note], duration=note_len(fibonacci(i)))


print("\nWelcome!\n")
while True:
    selection = int(input("Please select a scale to work from."
                      "\n 1. Pentatonic in C Major\n 2. Blues in C Major\n 3. Ionian in C\n 4. Phrygian in C\n "
                      "5. All notes\n 0. Enter a custom scale\n"))

    if selection == 0:
        custom_scale = input("Enter a list of strings, separated by spaces.\n"
                             "select from the following notes'Ab', 'A', 'Bb', 'B','C', 'Db', 'D', 'Eb', 'E', 'F', "
                             "'Gb','G'\n").split(' ')
        play_music(custom_scale)
    else:
        play_music(array_of_scales[selection])
