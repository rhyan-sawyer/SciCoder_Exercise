import random

random.seed()

sdss_file = open('sdss_spectra_links.txt')

url_list = list()

flag = 0
endline = 0


for line,url in enumerate(sdss_file):
    url = url.rstrip("\n")
    
    endline = len(url_list)-1
    
    if line == 0:
        url_list.append(url)
    else:
        while endline >= 0:
            if url == url_list[endline]:
                flag = 1
                endline -= 1
            else:
                endline -= 1
        if flag == 0:
            url_list.append(url)
        else:
            flag = 0

sdss_file.close()

randBegin = random.randint(0,line)
randEnd = randBegin + random.randint(0,line)

if randEnd >= line:
    randEnd = line
    
print( "The interval being considered is: "'[','line = ',randBegin, ' , ','line = ', randEnd, ']')
print(url_list[randBegin:randEnd])

#1st read line
#compare to all previous lines
#if line[current] == line[any prev] --> DONT APPEND
#if line[current] != any previous lines --> APPEND
