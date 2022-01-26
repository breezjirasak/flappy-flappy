import csv


class DATA:
    def __init__(self, score=0, name=''):
        """ Initializes a DATA object with score, name attribute.

        :param score: int
        :param name: str
        """
        self.name = name
        self.score = score
        # list of dict that keep name and score
        self.list_score = []

    def insert(self):
        """ read and write data file """

        # to check that the file exist or not
        try:
            # read data file
            with open('score.csv', mode='r') as csv_file:
                csv.DictReader(csv_file)
        # if file does not exist then create and write new file
        except FileNotFoundError:
            # write data file
            with open('score.csv', mode='w') as csv_file:
                fieldnames = ['name', 'score']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'name': self.name, 'score': self.score})
        # if the file exist then update
        else:
            # write data file
            with open('score.csv', mode='a+', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([self.name, self.score])

    def score_name(self):
        """ create dict and send to list """
        with open('score.csv', mode='r') as csv_file:
            data = csv.DictReader(csv_file)
            for i in data:
                self.list_score.append(i)
