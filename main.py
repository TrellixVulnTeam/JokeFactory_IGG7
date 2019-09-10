import pyfiglet as pyf
import requests as rq
import termcolor as tc

def initial_message(msg):
    heading = pyf.figlet_format(msg)
    heading = tc.colored(heading, color="magenta")
    print(heading)
    #print ('')

def data_fetcher(key):
    url= "https://icanhazdadjoke.com/search?term=" + key
    #print(url)
    res = rq.get(url,
           headers = {"Accept" : "application/json"},
           params  = {"term" : key , "limit" : "10"}
           )

    data = res.json()
    #total_output = data['total_jokes']
    data_sorter(data)
    #print(data)


def data_sorter(final_data):
    #print(final_data)
    repeats = final_data['total_jokes']
    #print(repeats)
    if repeats == 0:
        print('Sorry buddy ! Cant find a joke with that keyword ')
    elif repeats == 1:
        print('We found one joke related to ' + final_data['search_term'] + '. Here it is:')
        print()
        print(final_data['results'][0]['joke'])
    else:
        print('We found ' + str(final_data['total_jokes']) + ' jokes related to ' + final_data['search_term'] + ' Here is one:' )
        print(final_data['results'][0]['joke'])



def main():
    initial_message("Joke-Factory")
    keyword = input("Enter a keyword ---->>>  ")
    data_fetcher(keyword)

if __name__== "__main__":
    main()
