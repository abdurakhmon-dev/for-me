number = int(input())
p = "🌹"
ch = "💋"

for v in range(1,abs(number)+1):
    if(number<0):
        print(ch*(v-1),end="")
        print(p*(abs(number)-(v-1)))
    else:
        print(ch*(abs(number)-v),end="")
        print(p*(v))


