import face_recognition
import os


known_face_encodings = []
known_face_names = []

# Load sample pictures and learn how to recognize it.
dirname = 'knowns'
files = os.listdir(dirname)

for filename in files:
    name, ext = os.path.splitext(filename)
    if ext == '.jpg' or ext == '.jpeg' or ext == '.png':
        pathname = os.path.join(dirname, filename)
        img = face_recognition.load_image_file(pathname)
        face_encoding = face_recognition.face_encodings(img)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(name)


unknown_image1 = face_recognition.load_image_file("who/iuiu.jpeg")
unknown_encoding1 = face_recognition.face_encodings(unknown_image1)[0]

unknown_image2 = face_recognition.load_image_file("who/Song.png")
unknown_encoding2 = face_recognition.face_encodings(unknown_image2)[0]

unknown_encodings = [
    unknown_encoding1,
    unknown_encoding2
]

for unknown_encoding in unknown_encodings:
    # See how far apart the test image is from the known faces
    face_distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)

    min_value = int(1e9)
    index = -1
    for i, face_distance in enumerate(face_distances):
        if min_value > face_distance:
            min_value = face_distance
            index = i

    if min_value < 0.4:
        print(known_face_names[index])
    else:
        print('Unknown')