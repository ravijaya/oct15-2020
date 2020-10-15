"""test case, collections of test  """


class TestSampleCase:
    """test case"""

    def test_one(self):
        s = 'a sample string'
        assert 'ring' in s

    def test_attrib(self):
        s = 'a sample string'
        assert hasattr(s, 'upper')

