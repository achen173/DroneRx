import cv2

# print cv2.__version__
camera = cv2.VideoCapture(1+ cv2.CAP_DSHOW)
while(1):
    retval, im = camera.read()
    cv2.imshow("image", im)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
camera.release()
# import cv2
#
# cams_test = 0
# cap = cv2.VideoCapture(cams_test)
# while(True):
#
#     test, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) or 0xFF == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()