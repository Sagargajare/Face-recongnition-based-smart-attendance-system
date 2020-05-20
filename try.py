# import os
# import pickle
# attendancedict = {}
# def update():
#         # for dirpath, dnames, fnames in os.walk("./faces"):
#         #         for f in fnames:
#         #                 attendancedict.update({f[:5]: "absent"})
#         # output = open('attend.pickle', 'wb')
#         # pickle.dump(attendancedict, output)
#         # output.close()
#
#
#
#         # mydict = {}
#         # # update dict and write to the file again
#         # mydict.update({'d': 4})
#         # output = open('data.pickle', 'wb')
#         # pickle.dump(mydict, output)
#         # output.close()
#
#         # read python dict back from the file
#         # pkl_file = open('data.pickle', 'rb')
#         # mydict = pickle.load(pkl_file)
#         # pkl_file.close()
#         # print (mydict)
#         pkl_file = open('attend.pickle', 'rb')
#         mydict = pickle.load(pkl_file)
#         pkl_file.close()
#         print(mydict)
#         # print(attendancedict)
# update()
import os
import pickle

attendancedict = {}
for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
                attendancedict.update({f[:5]: "absent"})
output = open('attend.pickle', 'wb')
pickle.dump(attendancedict, output)
output.close()
