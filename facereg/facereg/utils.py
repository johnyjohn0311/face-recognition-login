import cv2 
import os
from profiles.models import Profile

path = 'D:\\computer-vision-project\\assignment\\facereg\\facereg\\output'

"""
hàm so sánh histogram của hai ảnh
"""
def compare_histograms(imageA, imageB, method='correlation'):
    # chuyển mảng màu của hình ảnh thành dạng HSV để dễ so sánh hơn
    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2HSV)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2HSV)

    # tính toán histogram
    histA = cv2.calcHist([imageA], [0, 1], None, [50, 60], [0, 180, 0, 256])
    histB = cv2.calcHist([imageB], [0, 1], None, [50, 60], [0, 180, 0, 256])

    # chuẩn hoá histogram
    cv2.normalize(histA, histA, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    cv2.normalize(histB, histB, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    # Sử dụng correlation hoặc các công thức so sánh khác
    methods = {
        'correlation': cv2.HISTCMP_CORREL,
        'chi-square': cv2.HISTCMP_CHISQR,
        'bhattacharyya': cv2.HISTCMP_BHATTACHARYYA
    }

    comparison = cv2.compareHist(histA, histB, methods[method])
    return comparison

"""
hàm lấy ra khuôn mặt
"""
def extract_face(img):    
    # phần dò tìm khuôn mặt
    try:
        image = cv2.imread(img)
        # sử dụng mô hình 
        face_cascade = cv2.CascadeClassifier('D:\\computer-vision-project\\assignment\\.venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt2.xml')
        # chuyển đổi hình ảnh thành ảnh xám
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.1, 4) 
    except:
        pass
    
    # vẽ một hình chữ nhật quanh khuôn mặt và lưu dưới định dạng jpg 
    for (x, y, w, h) in faces: 
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2) 
        faces = image[y:y + h, x:x + w] 
        cv2.imwrite(os.path.join(path, 'face2.jpg'), faces) 

"""
hàm so sánh ảnh khuôn mặt của người dùng chụp 
để đăng nhập với từng ảnh trong cơ sở dữ liệu
"""
def classify_face(img):
    # đọc hình ảnh người dùng đăng nhập chụp qua webcam
    image = cv2.imread(img) 

    # chuyển hình ảnh người dùng chụp qua webcam thành ảnh xám 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    # sử dụng mô hình haarcascade 
    face_cascade = cv2.CascadeClassifier('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml') 
    
    # dò tìm khuôn mặt trong ảnh của người dùng chụp qua webcam
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) 
    
    # vẽ một hình chữ nhật quanh khuôn mặt và lưu dưới định dạng jpg 
    for (x, y, w, h) in faces: 
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2) 
        faces = image[y:y + h, x:x + w] 
        cv2.imwrite(os.path.join(path, 'face1.jpg'), faces) 
   
    # trả về false nếu không thể dò tìm khuôn mặt
    if (len(faces) == 0):
        return False
    
    # khởi tạo best_match là kết quả tính toán cho ra 
    # giá trị cao nhất khi so sánh hai khuôn mặt
    best_match = 0
    # khởi tạo name để trả về tên người dùng
    name = ''

    # lấy tất cả hình ảnh của người dùng trong cơ sở dữ liệu
    # và duyệt qua từng ảnh
    qs = Profile.objects.all()
    for p in qs:
        photoPath = str(p.photo.path)
        extract_face(photoPath)
        imageA = cv2.imread(str(path) + '\\face1.jpg')
        imageB = cv2.imread(str(path) + '\\face2.jpg')
        hist_score = compare_histograms(imageA, imageB, method='correlation')
        
        if (hist_score > best_match):
            best_match = hist_score
            name = p.user.username
        print(best_match)
    if (best_match >= 0.8):
        print(best_match)
        return name
    return False
