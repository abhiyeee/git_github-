import cv2

# Try Windows Media Foundation
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

print("Camera opened:", cap.isOpened())

while True:

    ret, frame = cap.read()

    print("Frame received:", ret, "Frame size:", frame.shape if ret else None)

    if not ret:
        print("No frame received")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()