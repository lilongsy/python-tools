# -*- coding: utf-8 -*-

class MakeFiles(object):

    def main(self):
        i=1
        for f in range(0, 210, 21):
            with open("start/%s.txt" % str(i), 'w') as hf:
                hf.write(str(f))
                i += 1
                
of = MakeFiles()
of.main()
