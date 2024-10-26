import cv2
from cristal import crystal_transform
from gaussian_blur import gaussian_blur as gaussian_transform
from face_detection import face_detection
from random_images import random_images


def to_crystal(img, body_part, block_size: int):
    bx, by, bw, bh = body_part
    body_section = img[by:by+bh, bx:bx+bw]

    img[by:by+bh, bx:bx+bw] = crystal_transform(body_section,
                                                block_size=block_size)
    return img


def to_gaussian(img, body_part, elements: int):
    bx, by, bw, bh = body_part
    body_section = img[by:by+bh, bx:bx+bw]

    img[by:by+bh, bx:bx+bw] = gaussian_transform(body_section,
                                                 elements=elements)
    return img


if __name__ == "__main__":
    img = cv2.imread(random_images())
    face, eyes, nose = face_detection(img)

    for eye in eyes:
        img_gaussian = to_gaussian(img, eye, elements=80)
        # cv2.imshow('Deteccion de ojos y nariz', img_gaussian)

    img_cristal = to_crystal(img, nose, block_size=20)
    cv2.imshow('Deteccion de ojos y nariz', img_cristal)

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
