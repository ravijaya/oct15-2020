from psdirectorylisting import DirectoryListing
from json import dump


class DirectoryListing2JSON(DirectoryListing):
    def to_json(self, json_file):
        dump(self.container, open(json_file, 'w'), indent=2)


if __name__ == '__main__':
    DirectoryListing2JSON('/tmp', '/home/ravijaya', '/home/ravijaya/Downloads').to_json('tmp.json')
