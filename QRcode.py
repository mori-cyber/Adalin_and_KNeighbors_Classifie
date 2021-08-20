import cv2

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()

    data, bbox, _ = detector.detectAndDecode(img)

    if bbox is not None:

        for i in range(len(bbox)):

            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        if data:
            print("[+] QR Code detected, data:", data)

    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()