import json

class SearchByTag:

    def __init__(self, data_file, query_tag):
        self._data = data_file
        self.query = query_tag

    def search(self):
        try:
            for i in self._data["items"]:
                if 'tags' in i:
                    if self.query in i['tags']:
                        yield i
                else:
                    return
        except StopIteration:
            return 


    def first(self):        
        try:
            for i in self._data["items"]:
                if 'tags' in i:
                    if self.query in i['tags']:
                        return i
                else:
                    return 
        except StopIteration:
            return         

       
            

file2 = { "items": [
     {"name": "The Shawshank Redemption", "tags": ["90s", "drama"]},
     {"name": "The Godfather", "tags": ["70s", "drama", "crime"]},
     {"name": "The Dark Knight", "tags": ["action", "crime", "drama"]},
     {"name": "The Godfather: Part II", "tags": ["70s", "crime", "drama"]},
     ]
}

file = { "items": [
     {"name": "The Shawshank Redemption"},
     {"name": "The Godfather"},
     {"name": "The Dark Knight"},
     {"name": "The Godfather: Part II"},
     ]
}

search = SearchByTag(file2, '70s')
gen = search.search()
for i in gen:
    print(i) 

#print(search.first())