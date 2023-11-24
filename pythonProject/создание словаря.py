N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]
slov = {PITCHES[0]: LONG_PITCHES[0],
        PITCHES[1]: LONG_PITCHES[1],
        PITCHES[2]: LONG_PITCHES[2],
        PITCHES[3]: LONG_PITCHES[3],
        PITCHES[4]: LONG_PITCHES[4],
        PITCHES[5]: LONG_PITCHES[5],
        PITCHES[6]: LONG_PITCHES[6]}


class Note:
    def __init__(self, nota, is_long=False):
        self.is_long = is_long
        if is_long:
            self.nota = slov[nota]
        else:
            self.nota = nota

    def __str__(self):
        return self.nota

    def __rshift__(self, other):
        if self.nota in PITCHES:
            if PITCHES.index(self.nota) + other > 6:
                a = PITCHES.index(self.nota) + other
                while a > 6:
                    a -= 6
                return PITCHES[a]
            else:
                return PITCHES[PITCHES.index(self.nota) + other]
        else:
            if LONG_PITCHES.index(self.nota) + other > 6:
                a = LONG_PITCHES.index(self.nota) + other
                while a > 6:
                    a -= 6
                return LONG_PITCHES[a - 1]
            else:
                return LONG_PITCHES[LONG_PITCHES.index(self.nota) + other]

    def __lshift__(self, other):
        if self.nota in PITCHES:
            if PITCHES.index(self.nota) - other < 0:
                a = PITCHES.index(self.nota) - other
                while a < -6:
                    a += 6
                return PITCHES[a]
            else:
                return PITCHES[PITCHES.index(self.nota) - other]
        else:
            if LONG_PITCHES.index(self.nota) + other > 6:
                a = LONG_PITCHES.index(self.nota) + other
                while a > 6:
                    a -= 6
                return LONG_PITCHES[a - 1]
            else:
                return LONG_PITCHES[LONG_PITCHES.index(self.nota) + other]


    def __lt__(self, other):
        if PITCHES.index(self.nota[0:2]) < PITCHES.index(other.nota[0:2]):
            return True
        else:
            return False

    def __gt__(self, other):
        if PITCHES.index(self.nota[0:2]) > PITCHES.index(other.nota[0:2]):
            return True
        else:
            return False

    def __eq__(self, other):
        if len(self.nota) >= 4 and len(other) >= 4:
            if PITCHES.index(f'{self.nota[0:2]}{self.nota[-2]}{self.nota[-1]}')\
                    == PITCHES.index(f'{other[0:2]}{other[-2]}{other[-1]}'):
                return True
            else:
                return False
        else:
            if PITCHES.index(self.nota[0:2]) == PITCHES.index(other.nota[0:2]):
                return True
            else:
                return False

    def __ne__(self, other):
        if PITCHES.index(self.nota[0:2]) != PITCHES.index(other.nota[0:2]):
            return True
        else:
            return False

    def __le__(self, other):
        if PITCHES.index(self.nota[0:2]) <= PITCHES.index(other.nota[0:2]):
            return True
        else:
            return False

    def __ge__(self, other):
        if PITCHES.index(self.nota[0:2]) >= PITCHES.index(other.nota[0:2]):
            return True
        else:
            return False

    def get_interval(self, other):
        if self.nota in PITCHES:
            return INTERVALS[PITCHES.index(self.nota) - PITCHES.index(other)]
        else:
            return INTERVALS[LONG_PITCHES.index(self.nota) - LONG_PITCHES.index(other)]


class LoudNote:
    def __init__(self, nota, is_long=False):
        self.is_long = is_long
        if is_long:
            self.nota = slov[nota].upper()
        else:
            self.nota = nota.upper()

    def __str__(self):
        return self.nota


class DefaultNote:
    def __init__(self, nota='до', is_long=False):
        self.is_long = is_long
        if is_long:
            self.nota = slov[nota]
        else:
            self.nota = nota

    def __str__(self):
        return self.nota


class NoteWithOctave:
    def __init__(self, nota, octave, is_long=False):
        self.octave = octave
        self.is_long = is_long
        if is_long:
            self.nota = slov[nota]
        else:
            self.nota = nota

    def __str__(self):
        return f'{self.nota} ({self.octave})'

fa1 = Note("соль", True)
fa2 = Note("соль")
print(fa1 == fa2)
