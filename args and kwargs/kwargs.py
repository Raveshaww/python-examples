# returns a dict
def fav_colors(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}'s favorite color is {v}")


fav_colors(rave="blue", fid="green")

def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word
