class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_birthday = Song(["Last time that I checked",
                        "I'm the streets voice out west",
                        "lengendary, self made project."])

bull_on_parade = Song(["I'm the type that gon go get it",
                        "no kiddin!"])


happy_birthday.sing_me_a_song()
bull_on_parade.sing_me_a_song()
