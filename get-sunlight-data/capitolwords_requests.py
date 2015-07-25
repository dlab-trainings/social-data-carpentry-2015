#!/usr/bin/env python

from requests import get
from os import getenv


class SunLight:

    def __init__(self):
        with open(getenv('HOME') + '/.sunlight.key') as keyfile:
            self.url_scheme = (
                'http://capitolwords.org/api/1/text.json?{}&apikey=' +
                keyfile.read().strip() )

    def get(self, query):
        '''Get some data'''
        url = self.url_scheme.format(query)
        response = get(url)
        return response.json()


if __name__ == '__main__':
    from sys import argv
    print(SunLight().get(argv[1]))
