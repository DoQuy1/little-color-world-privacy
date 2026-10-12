p = "index.html"
s = open(p, encoding="utf8").read()


def sub(old, new):
    global s
    assert old in s, old[:60]
    s = s.replace(old, new, 1)


sub("""A future version may offer downloadable picture packs from a server; this policy would be updated before such a feature is released.</p>""",
    """</p>

  <h3>5a. Downloadable pictures (Cloudinary)</h3>
  <p>When a parent chooses to download the extra picture packs in the parent area, the app downloads picture files over HTTPS from Cloudinary (res.cloudinary.com). Like any web request, this lets Cloudinary see technical data such as the device's IP address and the file requested. The app sends no account, name or other personal information with the request, and the downloaded files are checked and stored on the device so they work offline afterwards. Cloudinary's handling of such data is described in its own privacy policy.</p>""")
sub("""The publisher does not run a server for the app and does not collect personal information from users.""",
    """The publisher does not run a server for the app and does not collect personal information from users. The only outside services the app contacts are Google AdMob (ads) and Cloudinary (optional picture downloads).""")
sub("""Apart from the Google Mobile Ads SDK described above, none of them is used by the app to send data to a third party.""",
    """Apart from the Google Mobile Ads SDK and the Cloudinary picture downloads described in this policy, none of them is used by the app to send data to a third party.""")

sub("""Phiên bản sau có thể cung cấp gói tranh tải từ máy chủ; chính sách này sẽ được cập nhật trước khi tính năng đó ra mắt.</p>""",
    """</p>

  <h3>5a. Tranh tải về (Cloudinary)</h3>
  <p>Khi phụ huynh chọn tải các gói tranh bổ sung trong khu vực dành cho phụ huynh, ứng dụng tải tệp tranh qua HTTPS từ Cloudinary (res.cloudinary.com). Như mọi yêu cầu web, Cloudinary có thể thấy dữ liệu kỹ thuật như địa chỉ IP của thiết bị và tệp được yêu cầu. Ứng dụng không gửi tài khoản, tên hay thông tin cá nhân nào kèm theo yêu cầu, và các tệp tải về được kiểm tra rồi lưu trên thiết bị nên dùng được offline sau đó. Cách Cloudinary xử lý dữ liệu được mô tả trong chính sách riêng của họ.</p>""")
sub("""Nhà phát hành không vận hành máy chủ cho ứng dụng và không thu thập thông tin cá nhân của người dùng.""",
    """Nhà phát hành không vận hành máy chủ cho ứng dụng và không thu thập thông tin cá nhân của người dùng. Dịch vụ bên ngoài mà ứng dụng liên hệ chỉ gồm Google AdMob (quảng cáo) và Cloudinary (tải tranh tùy chọn).""")
sub("""Ngoài SDK Google Mobile Ads nêu trên, ứng dụng không dùng thư viện nào để gửi dữ liệu cho bên thứ ba.""",
    """Ngoài SDK Google Mobile Ads và việc tải tranh từ Cloudinary nêu trong chính sách này, ứng dụng không dùng thư viện nào để gửi dữ liệu cho bên thứ ba.""")
open(p, "w", encoding="utf8", newline="").write(s)
print("ok")
