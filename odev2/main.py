import cv2
import numpy as np

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir çerçeve al
    ret, frame = cap.read()

    # RGB renk uzayından HSV'ye dönüşüm
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını belirler
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Maske oluştur
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Görüntü üzerine maskeyi uygula
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonuçları göster
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # Çıkış için 'f' tuşuna basılıp basılmadığını kontrol et
    if cv2.waitKey(1) & 0xFF == ord('f'):
        break

# Kamera bağlantısını kapat
cap.release()
cv2.destroyAllWindows()
