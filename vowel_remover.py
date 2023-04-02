class WrongInputType(Exception):
  "Raised When input type is wrong"
  pass
vowels = 'aeiou'
class VowelRemover:
  def vowelRemover(self,string):
    output = ''
    if(type(string) is str):
      for char in string:
        if(char.lower() not in vowels):
          output += char
      return output
    else:
      raise WrongInputType()