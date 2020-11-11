#test

class Config:
    def __init__(self):
        self.server = ""
        self.databas = ""
        self.tabeller = ""
        with open('config.txt', 'r') as fil:
            data = fil.readlines()
            self.server = data[0]
            self.databas = data[1]
            self.tabeller = data[2].split()


def main():
    config = Config()
    print(config.server)
    for tabell in config.tabeller:
        print(tabell)

if __name__ == "__main__":
    main()
