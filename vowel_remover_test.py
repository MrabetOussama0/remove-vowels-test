#imports
import pytest
import vowel_remover
from unittest.mock import Mock
from unittest.mock import patch

vr = vowel_remover.VowelRemover()

###############################
############# TDD #############
###############################
#test tdd 0 : check the function with simple string
def test_tdd_0():
  assert vr.vowelRemover('string') == 'strng'
#test tdd 1 : check the function with capitalized string
def test_tdd_1():
  assert vr.vowelRemover('STRING') == 'STRNG'
#test tdd 2 : check the function with integer
def test_tdd_2():
  assert vr.vowelRemover('12345') == '12345'
#test tdd 3 : check the function with different characters
def test_tdd_3():
  assert vr.vowelRemover('1234 oussama mrabet 5678') == '1234 ssm mrbt 5678'
#test tdd 4 : check the function with special characters
def test_tdd_4():
  assert vr.vowelRemover('*-+&€#@/') == '*-+&€#@/'
#test tdd 5 : check the function with long text
def test_tdd_5():
   assert vr.vowelRemover("""It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).""") == """t s  lng stblshd fct tht  rdr wll b dstrctd by th rdbl cntnt f  pg whn lkng t ts lyt. Th pnt f sng Lrm psm s tht t hs  mr-r-lss nrml dstrbtn f lttrs, s ppsd t sng 'Cntnt hr, cntnt hr', mkng t lk lk rdbl nglsh. Mny dsktp pblshng pckgs nd wb pg dtrs nw s Lrm psm s thr dflt mdl txt, nd  srch fr 'lrm psm' wll ncvr mny wb sts stll n thr nfncy. Vrs vrsns hv vlvd vr th yrs, smtms by ccdnt, smtms n prps (njctd hmr nd th lk)."""

#test tdd 6 : check the function with other data types :
#boolean
def test_tdd_6_0():
  with pytest.raises(vowel_remover.WrongInputType):
    vr.vowelRemover(True)
#integer
def test_tdd_6_1():
  with pytest.raises(vowel_remover.WrongInputType):
    assert vr.vowelRemover(12345)
#float
def test_tdd_6_2():
  with pytest.raises(vowel_remover.WrongInputType):
    vr.vowelRemover(3.14)
#hexadecimal
def test_tdd_6_3():
  with pytest.raises(vowel_remover.WrongInputType):
    vr.vowelRemover(0xFF0F4)

###############################
############ MOCKS ############
###############################
#test mock 0 : using Patch:
def newVowelRemoverFunctionForPatchTest(string):
  output = 'Strng t tst vwlRmvr fnctn wth ptch'
  return output
def test_mock_0():
  with patch.object(vowel_remover.VowelRemover,'vowelRemover',side_effect=newVowelRemoverFunctionForPatchTest):
    assert vr.vowelRemover('String to test vowelRemover function with patch') == 'Strng t tst vwlRmvr fnctn wth ptch' 
#test mock 1 : using Mock/return_value:
def newVowelRemoverFunctionForMockTest(string):
  output = 'Strng t tst vwlRmvr fnctn wth Mck'
  return output
#MOCK
def test_mock_1_0():
  vr.vowelRemover = Mock(side_effect=newVowelRemoverFunctionForMockTest)
  assert vr.vowelRemover('String to test vowelRemover function with Mock') == 'Strng t tst vwlRmvr fnctn wth Mck'
#return_value
def test_mock_1_1():
  vr.vowelRemover = Mock(return_value='Strng t tst vwlRmvr fnctn wth Mck Rtrn_Vl')
  assert vr.vowelRemover('String to test vowelRemover function with Mock Return_Value') == 'Strng t tst vwlRmvr fnctn wth Mck Rtrn_Vl'
#test mock 2 : using Mock/side_effect:
def newVowelRemoverFunctionForMockSideEffectTest(string):
  output = 'Strng t tst vwlRmvr fnctn wth Mck Sd ffct'
  return output
def test_mock_2():
  vr.vowelRemover = Mock()
  vr.vowelRemover.side_effect = newVowelRemoverFunctionForMockSideEffectTest
  assert vr.vowelRemover('String to test vowelRemover function with Mock Side Effect') == 'Strng t tst vwlRmvr fnctn wth Mck Sd ffct'