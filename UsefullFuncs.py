def ldr(list):
  """Removes duplicates by using a for loop"""
  new_list= []
  for current_item in list:
    if current_item not in new_list:
      new_list.append(current_item)
    return new_list
def convert_string_to_int(string):
    """Converts a string to an integer even if it has other characters"""
    digits = 0
    for char in string:
        if char.isdigit():
            digits = digits * 10 + int(char)
    return digits