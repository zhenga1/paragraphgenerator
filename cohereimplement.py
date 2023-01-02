import cohere
class prompt_str:
  prompt_q = "\n--\nQuestion: Why are you interested in applying for coding club?\nAnswer:"
  cprompt = ""
  def __init__(self, string):
    self.string = string
  def append(self,stri):
    i=0
    while i<len(stri):
      if stri[i]=='.':
        if i<len(stri)-1:
          stri=stri[:i+1]+'\n'+stri[i+1:]
        else:
          stri=stri[:i+1]+'\n'
      i+=1
    self.string = self.string+"\n--\n"+stri
  def getprompt(self):
    if self.cprompt == "":
      self.cprompt = self.prompt_q
    return self.string+self.cprompt
    #return self.string+self.prompt_q
  def build_prompt(self,activity):
    self.cprompt = "\n--\nQuestion: Why are you interested in applying for "+activity+" club?\nAnswer:"
def creating_string(word):
  string = "This programe will generate an essay to apply to a competitive club, based on a given prompt.\n--\nQuestion: Why are you interested in studying computer science?\nAnswer: I chose to major in computer science because it affords me the opportunity to explore both of my passions: solving problems and producing creative experiences. Through code, I can generate ideas that solve user-specific problems, design and ideate possible solutions, and then execute them. Ultimately, engaging in this end-to-end experience is fulfilling to me because I get to not only imagine an experience but also bring it to fruition.\n--\nQuestion: Why are you interested in applying for kickboxing club?\nAnswer:Throughout my time of being a black belt, I have noticed many changes that have occurred since becoming one. Many changes are minor, like different classes, practicing more, and learning more curriculum. Being a black belt has a stronger impact on a person than most belts. It teaches a person, including myself, a lot more of how amazing one person can be. During my journey to become a  junior black belt, I didn’t realize how much work and effort went into becoming one."
  i=0
  while i<len(string):
    if string[i]=='.':
      if i<len(string)-1:
        string=string[:i+1]+'\n'+string[i+1:]
      else:
        string=string[:i+1]+'\n'
    i+=1
  current_prompt = prompt_str(string)
  newstr = "Question: Why are you passionate in Technology?\nAnswer: Technology has the ability to impact lives at a level and scale that has never been realized in the history of mankind. The idea that something I create can impact someone across the world now, or in the future is what drives my passion for Technology. And, with skill and hard work - anyone can do it."
  current_prompt.append(newstr)
  current_prompt.build_prompt(word)
  co = cohere.Client('JlYLcnvnGJDaeus6XjcmyROr5Uy33brYDwPej8Dw')
  response = co.generate(
    model='medium-20220926',
    prompt=current_prompt.getprompt(),
    max_tokens=700,
    stop_sequences=["--"])
  return str('Prediction: {}'.format(response.generations[0].text))
