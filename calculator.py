class StringCalculator(object):
  def has_control_code(self, string):
    return string[0:2] == "//"

  def get_delims(self, string):
    if(self.has_control_code(string)):
      partition = string.partition('\n')
      delimiters = partition[0].lstrip('/')
      return delimiters.split(',')
    return ','

  def remove_control_code(self, string):
    if(self.has_control_code(string)):
      partition = string.partition('\n')
      return partition[2]
    return string

  def delimit_string(self, string, delims):
    delimited = string
    for delim in delims:
      delimited = delimited.replace(delim, ",")
    return delimited.split(",")

  def create_sequence(self, string, delims):
    delimited = self.delimit_string(string, delims)
    return [int(x) for x in delimited if int(x) <= 1000]

  def verify_sequence(self, sequence):
    negatives = list(filter(lambda x: x < 0, sequence))
    if negatives:
      raise ValueError("Add cannot be invoked on negative numbers, found the following negatives: {}".format(negatives))
    
  def Add(self, string):
    if(string == ""):
      return 0
    delims = self.get_delims(string)
    cleaned_string = self.remove_control_code(string)
    sequence = self.create_sequence(cleaned_string, delims)
    self.verify_sequence(sequence)
    return sum(sequence)


