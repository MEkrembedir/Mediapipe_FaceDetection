# Mediapipe_FaceDetection
**EN** This Python code demonstrates an example application that uses the MediaPipe library to detect faces in a video file, draw the location of the faces on the image, and create an output video file.

Here's a breakdown of the code:

- First, the OpenCV and MediaPipe libraries are loaded.
- Instances of the MediaPipe Face Detection class and MediaPipe Drawing Utilities class are created.
- Then, a video file is opened and an output video file is created using the width, height, and frame rate of the input video file.
- Each frame of the video file is processed using the MediaPipe Face Detection class.
- For each frame, faces are detected using the MediaPipe Face Detection class, and the locations of the faces are drawn on the image using the MediaPipe Drawing Utilities class.
- The processed frames are written to the output video file.
- The processed frames are also displayed on the screen.
- The user can end the application by pressing the ESC key to close the display window.
- Finally, the source files and open windows are released.
To run this code, the MediaPipe and OpenCV libraries must be installed, and a video file as specified in the code must be available.


**TR**  Bu Python kodu, MediaPipe kütüphanesi kullanarak bir video dosyasındaki yüzleri algılayan ve görüntü üzerinde yüzlerin konumunu çizdirerek bir çıkış video dosyası oluşturan bir uygulama örneği göstermektedir.

Kodun açıklaması:

- İlk olarak, OpenCV ve MediaPipe kütüphaneleri yüklenir.
- MediaPipe Face Detection sınıfı ve MediaPipe Drawing Utilities sınıfı örnekleri oluşturulur.
- Ardından, bir video dosyası açılır ve bu dosyanın genişliği, yüksekliği ve kare hızı alınarak bir çıkış video dosyası oluşturulur.
- Video dosyasındaki her kare, MediaPipe Face Detection sınıfı ile işlenir.
- Her bir kare için, MediaPipe Face Detection sınıfı kullanılarak yüzler algılanır ve yüzlerin konumları MediaPipe Drawing Utilities sınıfı kullanılarak görüntü üzerinde çizdirilir.
- İşlenmiş kareler, çıkış video dosyasına yazılır.
- İşlenmiş kareler ayrıca ekranda da gösterilir.
- Kullanıcı, ekrandaki pencereyi kapatmak için ESC tuşuna basarak uygulamayı sonlandırabilir.
- Son olarak, kaynak dosyalar ve açık pencereler serbest bırakılır.
Bu kodun çalışması için, MediaPipe ve OpenCV kütüphanelerinin kurulu olması gerekmektedir. Ayrıca, kodda belirtilen video dosyasının mevcut olması gerekmektedir.
