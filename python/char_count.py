import pprint
def char_count(str):

  #text = "an apple a day will keep the doctor away"
  a = str.replace(" ", "")
  # Create an empty dictionary
  d = dict()
  
  # Loop through each line of the file
  for line in a:

    line = line.lower()

    # Iterate over each word in line
    for word in line:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  #creat a list sd, to sort dict d in descending order
  sd = sorted(d.items(), key=lambda x: x[1], reverse=True)
  #print(sd)
  nd = dict(sd)
  #print(nd)
  # Print the contents of list
  # for k,v in sd:
  #     print(k, ":", v)
  pprint.pprint(nd, sort_dicts=False)