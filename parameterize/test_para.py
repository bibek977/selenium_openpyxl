import pytest

count_list = [123, 245]

class TestPara:

    @pytest.mark.parametrize('count',count_list)
    @pytest.mark.parametrize('count_2',["a",'b'])
    def test_para_met(self,count, count_2):
        print(str(count) + count_2)