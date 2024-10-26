import cv2
import numpy as np
from face_detection import face_detection
from random_images import random_images


def face_color(img, face, channel_add: list):
    img = img.astype(np.int16)
    fx, fy, fw, fh = face
    face_section = img[fy:fy+fh, fx:fx+fw]

    b, g, r = channel_add

    face_section[:, :, 0] = np.clip(face_section[:, :, 0] + b, 0, 255)
    face_section[:, :, 1] = np.clip(face_section[:, :, 1] + g, 0, 255)
    face_section[:, :, 2] = np.clip(face_section[:, :, 2] + r, 0, 255)

    img = img.astype(np.uint8)

    return img


if __name__ == '__main__':
    img = cv2.imread(random_images())
    face, eyes, nose = face_detection(img)

    max_value = 150
    increment = 10
    duration = 30

    # normal a presencia
    range_values = [x for x in range(0, max_value, increment)]

    # presencia a normal
    range_values += [x for x in range(max_value, -1, -increment)]

    # normal a ausencia
    range_values += [x for x in range(0, -1*(max_value)-1, -increment)]

    # ausencia a normal
    range_values += [x for x in range(-max_value, 0, increment)]

    # Cambiar el color de la cara (rojo)
    for i in range_values:
        img_color = face_color(img, face, [0, 0, i])
        cv2.imshow('Deteccion de ojos y nariz', img_color)
        cv2.waitKey(duration)

    # Cambiar el color de la cara(amarillo)
    for i in range_values:
        img_color = face_color(img, face, [0, i, i])
        cv2.imshow('Deteccion de ojos y nariz', img_color)
        cv2.waitKey(duration)

    # Cambiar el color de la cara(verde)
    for i in range_values:
        img_color = face_color(img, face, [0, i, 0])
        cv2.imshow('Deteccion de ojos y nariz', img_color)
        cv2.waitKey(duration)

    # Cambiar el color de la cara(cian)
    for i in range_values:
        img_color = face_color(img, face, [i, i, 0])
        cv2.imshow('Deteccion de ojos y nariz', img_color)
        cv2.waitKey(duration)

    # Cambiar el color de la cara(azul)
    for i in range_values:
        img_color = face_color(img, face, [i, 0, 0])
        cv2.imshow('Deteccion de ojos y nariz', img_color)
        cv2.waitKey(duration)

    # Cambiar el color de la cara(magenta)
    for i in range_values:
        img_color = face_color(img, face, [i, 0, i])
        cv2.imshow('Deteccion de ojos y nariz', img_color)
        cv2.waitKey(duration)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
