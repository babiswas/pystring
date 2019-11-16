from collections import Counter

def find_winner(booth):
    votes=Counter(booth)
    vote_count={}
    for key,val in votes.items():
        if val not in vote_count:
           vote_count[val]=[]
           vote_count[val].append(key)
        else:
           vote_count[val].append(key)
    max_vote=sorted(vote_count.keys(),reverse=True)[0]
    if len(vote_count[max_vote])!=0:
        print(sorted(vote_count[max_vote])[0])
    else:
        print("Could not find any winner")

if __name__=="__main__":
   booth=["john", "johnny", "jackie","johnny", "john", "jackie","jamie", "jamie", "john","johnny", "jamie", "johnny","john"]
   find_winner(booth)

