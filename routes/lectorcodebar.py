import cv2
from pyzbar.pyzbar import decode

# Inicializar la captura de video
cap = cv2.VideoCapture(0)

while True:
    # Capturar un fotograma
    ret, frame = cap.read()
    
    # Decodificar códigos de barras en el fotograma
    decoded_objects = decode(frame)
    
    for obj in decoded_objects:
        # Dibujar un rectángulo alrededor del código de barras
        (x, y, w, h) = obj.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Mostrar el texto del código de barras
        cv2.putText(frame, obj.data.decode('utf-8'), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Mostrar el fotograma con los códigos de barras detectados
    cv2.imshow('Video', frame)
    
    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar ventanas
cap.release()
cv2.destroyAllWindows()