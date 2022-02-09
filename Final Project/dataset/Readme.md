# XÂY DỰNG DATASET

Trong bài báo cáo lần này nhóm em sử dụng bộ dữ liệu NTIRE 2021 do NTIRE 2021 NonHomogeneous Dehazing Challenge là một workshop của CVPR 2021.

Bộ dữ liệu có được xây dựng trên phiên bản mở rộng của tập NH-TIRE. Bộ dũ liệu NTIRE 2021 gồm 35 cặ p hình ảnh mờ và hình ảnh không mờ và chúng cùng một cảnh. NTIRE 2021 chứa các cảnh ngoài trời với sương mù thật và mật độ sương mù không đồng nhất được tạo ra kỹ thuật tạo sương mù chuyên nghiệp. Để tạo ra những ảnh này ban tổ chức đã sử dụng hai máy tạo khói mù chuyên nghiệp tạo ra các hạt hơi có kích thước đường kính (1-10 microns) tương tự các hạt sương mù trong khí quyển.

Để ghi lại cảnh ban tổ chức sử dụng máy ảnh Sony A7 được điêu khiển từ xa các thông số của mỗi lần lấy ảnh đều được chỉnh thủ công, và được giữ nguyên giữa hai phiên quay liên tiếp.

Quá trình lấy một cặp ảnh mất tầm 20-30 phút. Các tham số camera đươc set là (aperture-exposure-ISO), để cân bằng trắng (18percent gray) của color checker.

# SỬ DỤNG DỮ LIỆU

Do ban tổ chức chỉ public 25 ảnh nên nhóm thực hiện chia ra làm 20 ảnh train và 5 ảnh validation.
Với bộ data này nhóm thực hiện random crop 256x256, xoay trái phải, xoay (90,180, 270). Sau đó chuẩn hóa standard normal.
