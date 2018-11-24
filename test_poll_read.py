from poll import Poll
import mlab


mlab.connect()

poll_list = Poll.objects()
p         = poll_list[3]

print(p.symnonyms)