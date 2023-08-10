import cv2
# Diccionario de nombres y sus identificadores de rostros
nombres = {
    1: "Cesar Herrera",
    
    # Agrega aquí más nombres y sus identificadores de rostros
}

face_cascade = cv2.CascadeClassifier('haarcascade-frontalface-default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 5)

        # Obtén el identificador del rostro actual
        face_id = 1  # Cambia este valor por el identificador correcto correspondiente al rostro detectado

        # Muestra el nombre asociado al identificador del rostro
        if face_id in nombres:
            nombre = nombres[face_id]
            cv2.putText(img, f"Hola, {nombre}!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow('Facial Recognizing', img)
    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()



# CODIGO DE PROYECTO  ***** CAPTURA LAS IMAGENES *****
# import cv2
# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk

# class CapturaImagenesApp:
#     def __init__(self, root, video_source=0):
#         self.root = root
#         self.root.title("Captura de imágenes")
#         self.video_source = video_source

#         self.cap = cv2.VideoCapture(self.video_source)

#         self.canvas = tk.Canvas(root, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         self.canvas.pack()

#         self.btn_capturar = tk.Button(root, text="Capturar", command=self.capturar_imagen)
#         self.btn_capturar.pack()

#         self.contador = 1

#         self.mostrar_camara()

#     def capturar_imagen(self):
#         ret, frame = self.cap.read()
#         if ret:
#             cv2.imwrite(f"imagen_capturada_{self.contador}.png", frame)
#             messagebox.showinfo("Captura Exitosa", f"Imagen capturada y guardada como imagen_capturada_{self.contador}.png")
#             self.contador += 1

#     def mostrar_camara(self):
#         ret, frame = self.cap.read()
#         if ret:
#             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = Image.fromarray(frame)
#             img_tk = ImageTk.PhotoImage(image=img)
#             self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
#         self.root.after(10, self.mostrar_camara)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CapturaImagenesApp(root)
#     root.mainloop()

