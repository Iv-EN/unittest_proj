import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def test_get(self):
        data = {
            'vcs': 'mercurial',
            'studies': 'skypro',
        }
        self.assertEqual(dicts.get_val(data, 'vcs'), 'mercurial')
        self.assertEqual(dicts.get_val(data, 'studies', 'git'), 'skypro')
        data = {}
        self.assertEqual(dicts.get_val(data, 'studies', 'git'), 'git')
        self.assertEqual(dicts.get_val(data, 'studies', 'bazaar'), 'bazaar')
