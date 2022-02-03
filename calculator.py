class StringCalculator(object):

  def has_control_code(self, string):
    return string[0:2] == "//"

  def get_delim(self, string):
    if(self.has_control_code(string)):
      partition = string.partition('\n')
      delimiter = partition[0]
      return delimiter.lstrip('/')
    return ','

  def remove_control_code(self, string):
    if(self.has_control_code(string)):
      partition = string.partition('\n')
      return partition[2]
    return string

  def create_sequence(self, string, delim):
    delimited = string.split(delim)
    return [int(x) for x in delimited]
    
  def Add(self, string):
    if(string == ""):
      return 0
    delim = self.get_delim(string)
    cleaned_string = self.remove_control_code(string)
    sequence = self.create_sequence(cleaned_string, delim)
    return sum(sequence)


