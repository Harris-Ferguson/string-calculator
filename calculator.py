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

  def verify_sequence(self, sequence):
    negatives = list(filter(lambda x: x < 0, sequence))
    if negatives:
      raise ValueError("Add cannot be invoked on negative numbers, found the following negatives: {}".format(negatives))
    
  def Add(self, string):
    if(string == ""):
      return 0
    delim = self.get_delim(string)
    cleaned_string = self.remove_control_code(string)
    sequence = self.create_sequence(cleaned_string, delim)
    self.verify_sequence(sequence)
    return sum(sequence)


