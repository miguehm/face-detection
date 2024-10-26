import cv2
from random_images import random_images
# from face_color import face_color
# from transforms import to_crystal
# from transforms import to_gaussian


def face_detection(img):
    # Cargar las cascadas de Haar
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_eye.xml')
    nose_cascade = cv2.CascadeClassifier(
        'haarcascade_mcs_nose.xml')  # Cambiar ruta si es necesario

    # Cargar una imagen
    # img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar caras
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    face = faces[0]

    x, y, w, h = face

    # Recortar la región de interés (ROI) de la cara para detectar ojos y nariz
    roi = gray[y:y+h, x:x+w]

    # Detectar ojos en la región de la cara
    eyes_detected = eye_cascade.detectMultiScale(roi)

    eyes = []
    # Detectar los dos ojos que se encuentren mejor alineados en el eje x
    for i in range(len(eyes_detected)):
        for j in range(i+1, len(eyes_detected)):
            if eyes_detected[i][0] < eyes_detected[j][0]:
                eyes = [eyes_detected[i], eyes_detected[j]]
            else:
                eyes = [eyes_detected[j], eyes_detected[i]]

    # Detectar nariz en la región de la cara
    noses_detected = nose_cascade.detectMultiScale(roi)

    # Seleccionar la nariz que se encuentre en el rango de los ojos
    nose = []
    for (nx, ny, nw, nh) in noses_detected:
        if nx > eyes[0][0] and nx < eyes[1][0] and ny > eyes[0][1] and ny > eyes[1][1]:
            nose = (nx, ny, nw, nh)
            break

    # sumar la posición de la cara para obtener la posición real de los ojos
    eyes = [(x+ex, y+ey, ew, eh) for (ex, ey, ew, eh) in eyes]

    # sumar la posición de la cara para obtener la posicion real de la nariz
    if nose:
        nx, ny, nw, nh = nose
        nose = (x+nx, y+ny, nw, nh)

    return face, eyes, nose


if __name__ == '__main__':
    img = cv2.imread(random_images())

    face, eyes, nose = face_detection(img)

    fx, fy, fw, fh = face

    # Dibujar un rectángulo alrededor de la cara
    cv2.rectangle(img, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), 2)

    for (ex, ey, ew, eh) in eyes:
        # Dibujar un rectángulo alrededor de los ojos
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    # Dibujor un rectángulo alrededor de la nariz
    if nose:
        nx, ny, nw, nh = nose
        cv2.rectangle(img, (nx, ny), (nx+nw, ny+nh), (0, 0, 255), 2)

    cv2.imshow('Deteccion de ojos y nariz', img)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
