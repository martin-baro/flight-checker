from APIs.kiwicom import kiwi

class App():
    def __init__(self):
        pass

    def run(self, dest, start_d, return_d):
        s = kiwi.Search()
        print("search done")
        return


if __name__ == "__main__":
    app = App()
    destination = "DPS"
    start_date = "04/04/2019"
    return_date = "24/04/2019"
    app.run(destination, start_date, return_date)
    print("all done")
