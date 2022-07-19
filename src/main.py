import cv2


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("cam not found")
        return

    _, base = cap.read()
    base_g = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
    base_b = cv2.blur(base, (15, 151))

    while True:
        _, frame = cap.read()
        frame_g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = cv2.absdiff(frame_g, base_g)
        mask[mask < 50] = 0
        mask[mask >= 50] = 255
        mask = cv2.blur(mask, (25, 25))
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

        dst1 = cv2.bitwise_and(base_b, mask)
        dst2 = cv2.bitwise_and(base, 255-mask)

        cv2.imshow("window", dst1+dst2)
        # cv2.imshow("window1", dst1)
        # cv2.imshow("window2", dst2)
        # cv2.imshow("window3", mask)

        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('b'):
            base = frame
            base_g = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
            base_b = cv2.blur(base, (15, 15))


if __name__ == "__main__":
    main()
