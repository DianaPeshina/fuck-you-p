from calculate import isMatch, SqrtWrk


class TestInputValidating:
    def test_incorrect(self):
        result = isMatch('test')
        assert result[0] == 0 and result[1] == 'Error'

    def test_positive_integer(self):
        result = isMatch(74543)
        assert result[0] == 1 and result[1] == 74543

    def test_positive_integer_text(self):
        result = isMatch('74543')
        assert result[0] == 1 and result[1] == 74543

    def test_positive_float_text_dot(self):
        result = isMatch('121.121')
        assert result[0] == 2 and result[1] == 121.121

    def test_positive_float_text_comma(self):
        result = isMatch('121,121')
        assert result[0] == 2 and result[1] == 121.121

    def test_positive_complex_text(self):
        result = isMatch('74543+1j')
        assert result[0] == 3 and result[1] == complex('74543+1j')

    def test_negative_integer_text(self):
        result = isMatch('-4')
        assert result[0] == 3 and result[1] == complex('-4+0j')

    def test_negative_float_text_dot(self):
        result = isMatch('-121.121')
        assert result[0] == 3 and result[1] == complex('-121.121+0j')

    def test_negative_complex_text(self):
        result = isMatch('-121-1j')
        assert result[0] == 3 and result[1] == complex('-121-1j')


class TestCalculateSqrt:
    def test_calculate_integer_positive(self):
        result = isMatch('4')
        result = SqrtWrk(result)
        assert result == '±2.0'

    def test_calculate_float_positive(self):
        result = isMatch('1.21')
        result = SqrtWrk(result)
        assert result == '±1.1'

    def test_calculate_complex_posititve(self):
        result = isMatch('1.21+4j')
        result = SqrtWrk(result)
        assert result == '±(1.64+1.22j)'

    def test_calculate_integer_negative(self):
        result = isMatch('-4')
        result = SqrtWrk(result)
        assert result == '±2j'

    def test_calculate_float_negative(self):
        result = isMatch('-1.21')
        result = SqrtWrk(result)
        assert result == '±1.1j'

    def test_calculate_complex_negative(self):
        result = isMatch('-1.21-4j')
        result = SqrtWrk(result)
        assert result == '±(1.22-1.64j)'
