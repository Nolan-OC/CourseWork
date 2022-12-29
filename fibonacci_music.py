import winsound


def fibonacci(n):
    # fibonacci sequence is used to determine next note to be played
    a, b = 0, 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


# A 440, Bb 466.16, B 493.88, C 261.63, Db 277.18, D 293.66,
#  Eb 311.13, E 329.63, F 349.21, Gb 369.99, G 392, Ab 425.3

notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
frequencies = [261, 277, 294, 311, 330, 349, 370, 392, 425, 440, 466, 494]


for i in range(2, 100):
    # fibonacci note is the next num in fibonacci sequence mod 11 so we never exceed the current octave
    fibonacci_note = fibonacci(i) % 11

    #print out all info
    print("fibonacci {} = {} : {} Hz".format(fibonacci(i), notes[fibonacci_note], frequencies[fibonacci_note]))
    # play sound
    winsound.Beep(frequency=frequencies[fibonacci_note], duration=500)